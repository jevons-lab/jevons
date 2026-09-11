#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
jevons-probe — sonde de sensibilité syntaxique.

Pointe un scanner d'artefacts pour agents IA sur des paires de notices dont un
seul trait diffère, et dit ce que ce scanner LIT : la garde (R1), l'épinglage
(R4), la prose (R3, R5), ou seulement la forme de la commande (R7).

  jevons-probe run --scanner "skillspector scan {path} --no-llm --format json" \\
                   --adapter skillspector \\
                   --relations relations.yaml \\
                   --out report/

La sonde N'EXÉCUTE JAMAIS une notice. Elle appelle le scanner, et rien d'autre.

Adaptateurs : skillspector | skillvet | agentscan | cisco | sarif | generic
L'ordinal est la seule grandeur comparée :
  0 propre | 1 info | 2 bas/moyen | 3 haut/critique
Le score brut, quand le scanner en rend un, est reporté à titre indicatif et
n'entre dans aucun compte.
"""

import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from collections import OrderedDict

# Ordinal version 2, amendement du 2026-09-09 (spec 2 §9). Non rétroactif :
# les rapports antérieurs restent sous la version 1, à quatre niveaux, qui
# confondait HIGH et CRITICAL.
ORDINAL_VERSION = 2

ORDINAL = {'NONE': 0, 'CLEAN': 0, 'SAFE': 0, 'OK': 0, '': 0,
           'INFO': 1, 'NOTE': 1, 'INFORMATIONAL': 1,
           'LOW': 2, 'MINOR': 2,
           'MEDIUM': 3, 'MODERATE': 3, 'WARNING': 3,
           'HIGH': 4, 'ERROR': 4, 'SEVERE': 4,
           'CRITICAL': 5}

NOM_ORDINAL = {0: 'clean', 1: 'info', 2: 'low', 3: 'medium', 4: 'high',
               5: 'critical'}

ORDINAL_V1 = {'NONE': 0, 'CLEAN': 0, 'SAFE': 0, 'OK': 0, '': 0,
              'INFO': 1, 'NOTE': 1, 'INFORMATIONAL': 1,
              'LOW': 2, 'MEDIUM': 2, 'MODERATE': 2, 'WARNING': 2,
              'HIGH': 3, 'CRITICAL': 3, 'ERROR': 3, 'SEVERE': 3}


def json_tolerant(sortie):
    """Premier objet JSON de la sortie, même si du texte le suit.

    Plusieurs scanners impriment un résumé lisible après leur JSON. Refuser la
    sortie entière pour cette raison ferait passer un outil pour illisible.
    """
    i = sortie.find('{')
    if i < 0:
        raise ValueError('aucun objet JSON dans la sortie')
    return json.JSONDecoder().raw_decode(sortie[i:])[0]


def ordinal_de(mot):
    return ORDINAL.get((mot or '').strip().upper())


# ----------------------------------------------------------------- adaptateurs

def ad_skillspector(sortie, rc):
    d = json_tolerant(sortie)
    ra = d.get('risk_assessment') or {}
    sev = ra.get('max_issue_severity') or ra.get('severity')
    return ordinal_de(sev), {'score': ra.get('score'), 'severite': sev,
                             'recommendation': ra.get('recommendation')}


def ad_skillvet(sortie, rc):
    d = json_tolerant(sortie)
    s = d.get('summary') or {}
    if (s.get('critical') or 0) >= 1:
        o = 3
    elif (s.get('warnings') or 0) >= 1:
        o = 2
    else:
        o = 0
    return o, {'score': d.get('risk_score'), 'severite': s.get('status'),
               'critical': s.get('critical'), 'warnings': s.get('warnings'),
               'code_sortie': rc}


def ad_agentscan(sortie, rc):
    m = re.search(r'summary:\s*critical=(\d+)\s+high=(\d+)\s+medium=(\d+)\s+low=(\d+)\s+info=(\d+)',
                  sortie)
    if not m:
        return None, {'severite': None, 'motif': 'ligne « summary: » absente'}
    c, h, md, lo, inf = (int(x) for x in m.groups())
    o = 5 if c else (4 if h else (3 if md else (2 if lo else (1 if inf else 0))))
    sev = 'CRITICAL' if c else ('HIGH' if h else ('MEDIUM' if md else
                                                  ('LOW' if lo else ('INFO' if inf else 'NONE'))))
    return o, {'score': '%d/%d/%d/%d/%d' % (c, h, md, lo, inf), 'severite': sev}


def ad_cisco(sortie, rc):
    d = json_tolerant(sortie)
    sev = d.get('max_severity')
    sevs = [(f.get('severity') or '').upper() for f in (d.get('findings') or [])]
    compte = {s: sevs.count(s) for s in set(sevs)}
    return ordinal_de(sev), {'score': '/'.join(str(compte.get(k, 0)) for k in
                                               ('CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFO')),
                             'severite': sev}


def ad_sarif(sortie, rc):
    """Adaptateur SARIF générique : tout scanner qui rend du SARIF 2.1.0."""
    d = json_tolerant(sortie)
    niveaux = []
    regles = {}
    for run in (d.get('runs') or []):
        for r in ((run.get('tool') or {}).get('driver') or {}).get('rules', []) or []:
            dp = (r.get('defaultConfiguration') or {})
            if dp.get('level'):
                regles[r.get('id')] = dp['level']
        for res in (run.get('results') or []):
            n = res.get('level') or regles.get(res.get('ruleId')) or 'warning'
            niveaux.append(n.upper())
    if not niveaux:
        return 0, {'score': 0, 'severite': 'none', 'n_resultats': 0}
    o = max(ordinal_de(n) or 0 for n in niveaux)
    haut = [n for n in niveaux if (ordinal_de(n) or 0) == o]
    return o, {'score': len(niveaux), 'severite': haut[0].lower(),
               'n_resultats': len(niveaux)}


def ad_generic(chemin_map):
    """Mapping fourni par l'utilisateur : chemin JSON ou regex → ordinal."""
    with io.open(chemin_map, encoding='utf-8') as fh:
        conf = json.load(fh)
    severites = {k.upper(): int(v) for k, v in (conf.get('severites') or {}).items()}

    ordre = [x.upper() for x in (conf.get('ordre_severites')
                                 or ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFO'])]

    def f(sortie, rc):
        mot = None
        if conf.get('chemin_json_comptes'):
            d = json_tolerant(sortie)
            cur = d
            for seg in conf['chemin_json_comptes'].split('.'):
                cur = (cur or {}).get(seg)
            comptes = {k.upper(): v for k, v in (cur or {}).items()}
            mot = next((k for k in ordre if comptes.get(k)), 'NONE')
            o = severites.get(mot, ordinal_de(mot))
            return o, {'severite': mot.lower(),
                       'score': '/'.join(str(comptes.get(k, 0)) for k in ordre)}
        if conf.get('chemin_json'):
            d = json_tolerant(sortie)
            cur = d
            for seg in conf['chemin_json'].split('.'):
                if isinstance(cur, list):
                    cur = cur[int(seg)]
                else:
                    cur = (cur or {}).get(seg)
            mot = cur
        elif conf.get('regex'):
            m = re.search(conf['regex'], sortie)
            mot = m.group(1) if m else None
        elif conf.get('code_sortie'):
            mot = str(rc)
        if mot is None:
            return None, {'severite': None, 'motif': 'mapping sans correspondance'}
        o = severites.get(str(mot).strip().upper())
        if o is None:
            o = ordinal_de(str(mot))
        return o, {'severite': mot, 'score': None}
    return f


ADAPTATEURS = {'skillspector': ad_skillspector, 'skillvet': ad_skillvet,
               'agentscan': ad_agentscan, 'cisco': ad_cisco, 'sarif': ad_sarif}


# ------------------------------------------------------------------- exécution

def charger_relations(chemin):
    try:
        import yaml
    except ImportError:
        raise SystemExit('pyyaml requis pour lire relations.yaml')
    with io.open(chemin, encoding='utf-8') as fh:
        return yaml.safe_load(fh)


def empreinte_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, 'rb') as fh:
        h.update(fh.read())
    return h.hexdigest()


def empreinte_notices(racine):
    h = hashlib.sha256()
    for d, _sd, fs in sorted(os.walk(racine)):
        for f in sorted(fs):
            p = os.path.join(d, f)
            h.update(os.path.relpath(p, racine).encode('utf-8'))
            with open(p, 'rb') as fh:
                h.update(fh.read())
    return h.hexdigest()


def lancer(modele, chemin, delai):
    cmd = modele.replace('{path}', chemin)
    p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, timeout=delai)
    return p.stdout.decode('utf-8', 'replace'), p.returncode, \
        p.stderr.decode('utf-8', 'replace')


def scanner_notice(modele, racine, notice, adaptateur, cache, delai):
    if notice in cache:
        return cache[notice]
    chemin = os.path.join(racine, notice)
    if not os.path.isdir(chemin):
        cache[notice] = {'ordinal': None, 'erreur': 'notice absente : %s' % chemin}
        return cache[notice]
    try:
        sortie, rc, err = lancer(modele, chemin, delai)
    except subprocess.TimeoutExpired:
        cache[notice] = {'ordinal': None, 'erreur': 'delai depasse (%d s)' % delai}
        return cache[notice]
    try:
        o, detail = adaptateur(sortie, rc)
        r = {'ordinal': o, 'erreur': None}
        r.update(detail)
    except Exception as exc:
        r = {'ordinal': None, 'erreur': 'sortie illisible par l adaptateur : %s' % exc}
    r['code_sortie'] = r.get('code_sortie', rc)
    cache[notice] = r
    return r


def run(args):
    rel = charger_relations(args.relations)
    racine = args.notices or rel.get('notices')
    if args.adapter == 'generic':
        if not args.generic_map:
            raise SystemExit('--adapter generic exige --generic-map <fichier.json>')
        adaptateur = ad_generic(args.generic_map)
    else:
        adaptateur = ADAPTATEURS[args.adapter]

    cache = {}
    resultats = []
    for r in rel['relations']:
        lignes = []
        for paire in r['paires']:
            a = scanner_notice(args.scanner, racine, paire['a'], adaptateur, cache, args.delai)
            b = scanner_notice(args.scanner, racine, paire['b'], adaptateur, cache, args.delai)
            if a['ordinal'] is None or b['ordinal'] is None:
                tenue, tenue_sev, motif = None, None, (a.get('erreur') or b.get('erreur'))
            else:
                change = a['ordinal'] != b['ordinal']
                tenue = change if r['attendu'] == 'verdict_change' else (not change)
                # deuxieme ligne, declaree : l'etiquette de severite rendue par le
                # scanner, qui distingue ce que l'ordinal de la spec confond
                # (HIGH et CRITICAL tombent tous deux sur 3).
                sa = (a.get('severite') or '').strip().upper()
                sb = (b.get('severite') or '').strip().upper()
                change_sev = sa != sb
                tenue_sev = change_sev if r['attendu'] == 'verdict_change' else (not change_sev)
                motif = None
            lignes.append({'a': paire['a'], 'b': paire['b'],
                           'comportement': paire.get('comportement'),
                           'ordinal_a': a['ordinal'], 'ordinal_b': b['ordinal'],
                           'severite_a': a.get('severite'), 'severite_b': b.get('severite'),
                           'score_a': a.get('score'), 'score_b': b.get('score'),
                           'tenue': tenue, 'tenue_severite': tenue_sev, 'motif': motif})
        n = len([l for l in lignes if l['tenue'] is not None])
        x = len([l for l in lignes if l['tenue'] is True])
        xs = len([l for l in lignes if l['tenue_severite'] is True])
        resultats.append({'id': r['id'], 'enonce': r['enonce'], 'attendu': r['attendu'],
                          'sens': r['sens'], 'note': r.get('note'),
                          'tenue': x, 'tenue_severite': xs, 'denominateur': n,
                          'illisibles': len([l for l in lignes if l['tenue'] is None]),
                          'paires': lignes})

    par_id = {r['id']: r for r in resultats}
    r7 = par_id.get('R7')
    sensibilite = None
    if r7 and r7['denominateur']:
        sensibilite = round(1 - r7['tenue'] / float(r7['denominateur']), 3)
    n_cec = d_cec = 0
    for rid in ('R1', 'R4'):
        x = par_id.get(rid)
        if x:
            n_cec += x['denominateur'] - x['tenue']
            d_cec += x['denominateur']
    cecite = round(n_cec / float(d_cec), 3) if d_cec else None

    rapport = OrderedDict()
    rapport['sonde'] = 'jevons-probe'
    rapport['date'] = args.date
    rapport['scanner'] = args.scanner
    rapport['adaptateur'] = args.adapter
    rapport['ordinal_version'] = ORDINAL_VERSION
    rapport['ordinal_niveaux'] = NOM_ORDINAL
    rapport['version_scanner'] = args.pin_version
    rapport['perimetre'] = args.perimetre
    rapport['empreinte_relations'] = empreinte_fichier(args.relations)
    rapport['empreinte_notices'] = empreinte_notices(racine)
    rapport['relations'] = resultats
    rapport['sensibilite_syntaxique'] = sensibilite
    rapport['cecite_semantique'] = cecite

    if not os.path.isdir(args.out):
        os.makedirs(args.out)
    with io.open(os.path.join(args.out, 'report.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(rapport, ensure_ascii=False, indent=1))
    with io.open(os.path.join(args.out, 'report.md'), 'w', encoding='utf-8') as fh:
        fh.write(rendre(rapport))
    print('%s  %s' % (os.path.join(args.out, 'report.md'),
                      '  '.join('%s %d/%d' % (r['id'], r['tenue'], r['denominateur'])
                                for r in resultats)))


def rendre(R):
    O = []
    A = O.append
    A('# Rapport de sonde — %s' % (R['version_scanner'] or R['adaptateur']))
    A('')
    A('| | |')
    A('|---|---|')
    A('| scanner | `%s` |' % R['scanner'])
    A('| version | %s |' % (R['version_scanner'] or 'non déclarée'))
    A('| adaptateur | `%s` |' % R['adaptateur'])
    A('| version de l\'ordinal | %s (%s) |'
      % (R.get('ordinal_version', 1),
         ', '.join('%s=%s' % (k, v) for k, v in sorted(
             (R.get('ordinal_niveaux') or {}).items()))))
    A('| date | %s |' % R['date'])
    A('| périmètre | %s |' % R['perimetre'])
    A('| empreinte de `relations.yaml` | `%s` |' % R['empreinte_relations'][:32])
    A('| empreinte des notices | `%s` |' % R['empreinte_notices'][:32])
    A('')
    A('## Ce que ce rapport mesure')
    A('')
    A('Chaque relation compare **deux notices dont un seul trait diffère**. Si le')
    A('scanner lit ce trait, son verdict doit bouger — ou rester stable, selon la')
    A('relation. La sonde ne dit pas si le scanner est bon : elle dit **ce qu\'il lit**.')
    A('')
    A('La grandeur comparée est un ordinal. Depuis l\'amendement du 2026-09-09')
    A('(spec 2 §9) il compte **six** niveaux — `clean`, `info`, `low`, `medium`,')
    A('`high`, `critical` — parce que la version à quatre niveaux confondait `high`')
    A('et `critical` et perdait, sur ce seul point, un résultat publié. Le score brut')
    A('est reporté quand le scanner en rend un, et n\'entre dans aucun compte.')
    A('')
    A('## Résultats par relation')
    A('')
    A('| relation | énoncé | attendu | tenue, ligne ordinale | tenue, ligne de sévérité |')
    A('|---|---|---|---|---|')
    for r in R['relations']:
        A('| `%s` | %s | `%s` | **%d / %d**%s | %d / %d |'
          % (r['id'], r['enonce'], r['attendu'], r['tenue'], r['denominateur'],
             ' (%d illisible(s))' % r['illisibles'] if r['illisibles'] else '',
             r['tenue_severite'], r['denominateur']))
    A('')
    niv = ', '.join('`%s`' % v for _k, v in sorted((R.get('ordinal_niveaux') or NOM_ORDINAL).items()))
    A('**Deux lignes, déclarées.** La *ligne ordinale* normalise entre outils : %s' % niv)
    A('(ordinal version %s). La *ligne de sévérité* compare l\'étiquette rendue par le'
      % R.get('ordinal_version', 1))
    A('scanner telle quelle, sans normalisation. Les deux sont rapportées ; aucune ne')
    A('remplace l\'autre. `sonde/acceptation.md` montre un cas où elles ne comptent pas')
    A('la même chose, et pourquoi.')
    A('')
    for r in R['relations']:
        if r['tenue'] == r['denominateur'] and not r['illisibles']:
            continue
        A('### `%s` — %d / %d' % (r['id'], r['tenue'], r['denominateur']))
        A('')
        A('%s' % r['sens'])
        if r.get('note'):
            A('')
            A('%s' % r['note'])
        A('')
        A('| A | B | comportement | ordinal A | ordinal B | sévérité A | sévérité B | tenue |')
        A('|---|---|---|---|---|---|---|---|')
        for l in r['paires']:
            A('| `%s` | `%s` | %s | %s | %s | %s | %s | %s |'
              % (l['a'], l['b'], l['comportement'],
                 l['ordinal_a'], l['ordinal_b'], l['severite_a'], l['severite_b'],
                 {True: 'oui', False: '**non**', None: 'illisible'}[l['tenue']]))
        A('')
    r7 = [r for r in R['relations'] if r['id'] == 'R7']
    if r7:
        A('## Signature lue — quelles formes de commande déclenchent')
        A('')
        A('Même code distant, même absence de garde, forme de commande différente.')
        A('')
        A('| comportement | forme | ordinal | sévérité | score brut |')
        A('|---|---|---|---|---|')
        vus = set()
        for l in r7[0]['paires']:
            for cote in ('a', 'b'):
                nom = l[cote]
                if nom in vus:
                    continue
                vus.add(nom)
                A('| %s | `%s` | %s | %s | %s |'
                  % (l['comportement'], nom.split('-')[-1], l['ordinal_' + cote],
                     l['severite_' + cote], l['score_' + cote]))
        A('')
    A('## Deux scores de synthèse, à ne pas surinterpréter')
    A('')
    A('| | valeur | lecture |')
    A('|---|---|---|')
    A('| `sensibilite_syntaxique` | %s | part des paires R7 où le verdict change alors que le comportement est identique |'
      % R['sensibilite_syntaxique'])
    A('| `cecite_semantique` | %s | part des paires R1+R4 où le verdict ne change pas alors que la garde ou l\'épinglage change |'
      % R['cecite_semantique'])
    A('')
    A('Ces deux nombres résument des dénominateurs de quelques unités. Ils ne se')
    A('citent jamais seuls, et ne classent aucun outil.')
    A('')
    A('## Réserves')
    A('')
    A('- Mode statique, configuration par défaut du scanner, une seule version.')
    A('- Périmètre : %s. Un geste déplacé dans une annexe n\'est pas vu de la même' % R['perimetre'])
    A('  façon selon que l\'on scanne la page ou le répertoire.')
    A('- Les notices sont **synthétiques** : comportement simulé, cibles en domaines')
    A('  réservés, aucune charge réelle. Elles mesurent la lecture d\'un trait, pas')
    A('  la capacité à trouver une attaque réelle.')
    A('- Dénominateurs de quelques unités par relation. Aucun taux de population.')
    A('- Ce rapport porte sur **un scanner**. Il n\'établit aucun classement.')
    A('')
    return '\n'.join(O) + '\n'


def main():
    p = argparse.ArgumentParser(prog='jevons-probe')
    sp = p.add_subparsers(dest='cmd')
    rr = sp.add_parser('rendre', help='re-rend report.md depuis report.json')
    rr.add_argument('--out', required=True)
    r = sp.add_parser('run')
    r.add_argument('--scanner', required=True, help='commande, {path} = repertoire de notice')
    r.add_argument('--adapter', required=True,
                   choices=list(ADAPTATEURS) + ['generic'])
    r.add_argument('--generic-map', help='fichier JSON de mapping pour --adapter generic')
    r.add_argument('--relations', required=True)
    r.add_argument('--notices', help='racine des notices (defaut : champ notices du yaml)')
    r.add_argument('--out', required=True)
    r.add_argument('--perimetre', default='repertoire', choices=['page', 'repertoire'])
    r.add_argument('--pin-version', help='version du scanner, consignee dans le rapport')
    r.add_argument('--date', default='')
    r.add_argument('--delai', type=int, default=120)
    a = p.parse_args()
    if a.cmd == 'rendre':
        with io.open(os.path.join(a.out, 'report.json'), encoding='utf-8') as fh:
            R = json.load(fh)
        with io.open(os.path.join(a.out, 'report.md'), 'w', encoding='utf-8') as fh:
            fh.write(rendre(R))
        print(os.path.join(a.out, 'report.md'))
        return
    if a.cmd != 'run':
        p.print_help()
        raise SystemExit(1)
    run(a)


if __name__ == '__main__':
    main()
