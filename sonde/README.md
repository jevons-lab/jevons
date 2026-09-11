# jevons-probe — sonde de sensibilité syntaxique

**JEVONS — https://github.com/jevons-lab**
Dépôt cible : `github.com/jevons-lab/probe` — *nom provisoire, rien n'est publié
à ce jour.*

Pointez-la sur n'importe quel scanner d'artefacts pour agents IA. Elle vous dira
**ce que ce scanner lit** : la garde, l'épinglage, la prose — ou seulement la
forme de quelques commandes.

```
jevons-probe run --scanner "votre-scanner scan {path} --json" \
                 --adapter skillspector \
                 --relations relations.yaml \
                 --out report/
```

## Ce qu'elle mesure

Chaque relation compare **deux notices dont un seul trait diffère**. Si le
scanner lit ce trait, son verdict doit bouger — ou rester stable, selon la
relation.

| relation | trait qui change | attendu |
|---|---|---|
| `R1` | une confirmation explicite est ajoutée avant le geste | le verdict change |
| `R3` | la garde est formulée avec les mots de la menace | le verdict change |
| `R4` | la référence est épinglée, structure de commande constante | le verdict change |
| `R5` | une phrase de sécurité décorative est ajoutée | le verdict ne change pas |
| `R7` | la forme de la commande change, le comportement est identique | le verdict ne change pas |
| `R-perimetre` | le geste passe de la page à une annexe `scripts/install.sh` | le verdict ne change pas |

Toutes sont **pré-enregistrées** : écrites avant les notices, elles-mêmes
écrites avant tout scan. L'ordre est vérifiable dans l'historique git.

## Ce qu'elle ne mesure pas

Elle ne dit pas si un scanner est bon. Elle ne classe aucun outil — un rapport
porte sur **un** scanner. Les notices sont synthétiques : comportement simulé,
cibles en domaines réservés, **aucune charge réelle**. Elles mesurent la lecture
d'un trait, pas la capacité à trouver une attaque réelle.

## Deux lignes de comparaison, déclarées

- **ligne ordinale** — `0` clean, `1` info, `2` low, `3` medium, `4` high,
  `5` critical. Six niveaux depuis l'amendement du 2026-09-09 (spec 2 §9). La
  version 1, à quatre niveaux, confondait `HIGH` et `CRITICAL` et perdait, sur
  ce seul point, un résultat publié — voir `acceptation.md`. Chaque rapport
  porte `ordinal_version` ; les rapports antérieurs ne sont pas recalculés.
- **ligne de sévérité** — l'étiquette rendue par le scanner, telle quelle. Elle
  distingue ce que l'ordinal fusionne.

Les deux sont rapportées. Aucune ne remplace l'autre : `sonde/acceptation.md`
montre un cas où elles ne comptent pas la même chose, et pourquoi.

## Adaptateurs

`skillspector`, `skillvet`, `agentscan`, `cisco`, **`sarif`** (tout scanner qui
rend du SARIF 2.1.0), `generic` (mapping fourni par vous : chemin JSON, regex ou
code de sortie → ordinal).

L'adaptateur `sarif` a été contrôlé contre un adaptateur nommé : sur skillvet,
`--json` avec l'adaptateur `skillvet` et `--sarif` avec l'adaptateur `sarif`
rendent **les mêmes comptes sur les six relations**.

### Scanners cibles

Ce ne sont pas des juges du corpus : ils ne figurent pas dans `juges.yaml`.

| scanner | version épinglée | adaptateur | liste Adversa 30/07 | rapport |
|---|---|---|---|---|
| SkillSpector | 2.11.0 | `skillspector` | non vérifié | `rapports-ordinal-v2/skillspector/` |
| skillvet | 2.0.9, swh `a350337f` | `skillvet`, `sarif` | non vérifié | `rapports-ordinal-v2/skillvet/` |
| agentscan-cli | 1.2.2 | `agentscan` | non vérifié | `rapports-ordinal-v2/agentscan/` |
| Cisco skill-scanner | 2.1.0 | `cisco` | non vérifié | `rapports-ordinal-v2/cisco/` |
| claude-skill-auditor | 1.0.0 | `generic` | **hors liste Adversa** | `rapports-ordinal-v2/skill-auditor/` |
| ai-skill-scanner | commit `665598f2` (2026-03-01), `--static` | `generic` | **dans la liste Adversa**, vérifié — `docs/references.md` §1 | `rapports-ordinal-v2/ai-skill-scanner/` |

`claude-skill-auditor` a été choisi le 2026-09-08 dans l'index PyPI, faute de
disposer alors de la liste des huit outils du test Adversa du 30/07. Il
**reste** comme cible, étiqueté **hors liste Adversa** : la liste, consultée le
2026-09-09 et recopiée dans `docs/references.md` §1, ne le nomme pas.

`ai-skill-scanner` (`suchithnarayan/ai-skill-scanner`) a été ajouté le
2026-09-09. Son appartenance aux scanners nommés par Adversa est **vérifiée sur
la page elle-même** — `docs/references.md` §1, note 7 et liste des dépôts.
Le dépôt ne porte **aucun tag** : l'épinglage se fait sur le commit
`665598f233049d62c4631ac220d1595c6492c639`. Mode `--static` : son analyse par
modèle de langage, qui est son défaut, n'est pas exercée — aucune clé n'est
fournie et aucun appel n'est fait. Le premier choix retenu par le fondateur,
`opena2a-org/hackmyagent` v0.25.0 — version confirmée par la page Adversa,
`docs/references.md` §1 — n'a pas pu être installé : **Node est absent de
l'enclave**, et l'y installer aurait modifié l'enclave pour un seul outil.

Les deux adaptateurs `generic` ont été écrits **sans toucher une ligne de la
sonde** : sept lignes de mapping chacun
(`adaptateur-generic-skill-auditor.json`, `adaptateur-generic-ai-skill-scanner.json`),
parce que les deux outils publient leurs comptes par sévérité — l'un dans
`summary.by_severity`, l'autre dans `summary.severity_counts`.

Exemple de mapping `generic` :

```json
{"chemin_json": "risk.level", "severites": {"none": 0, "low": 2, "high": 3}}
```

## Résultats de référence

`sonde/rapports/<outil>/report.md`, et le contrôle du critère d'acceptation dans
`sonde/acceptation.md`.

## Règle des notices publiques

**Toute identité visée par une notice publiée est soit réservée par une RFC,
soit possédée par `jevons-lab` avant publication.**

| forme | ce qui est admis |
|---|---|
| domaine | `.invalid`, `.example`, `.test`, `.localhost`, `example.com/net/org` (RFC 2606 et 6761) |
| dépôt de forge | un dépôt de l'organisation `jevons-lab`, créé avant publication |
| image de registre | une image du namespace `jevons-lab`, publiée avant |
| paquet | un nom réservé par `jevons-lab` sur l'index concerné, avant |

Une identité **libre** — qui ne résout pas, ou qui rend 404 — est **interdite**.
Publier une notice qui vise un nom que personne ne détient revient à publier une
liste de noms à enregistrer, vers lesquels chaque utilisateur de la sonde
pointera son scanner. C'est l'attaque que le corpus documente, retournée contre
ses lecteurs.

Le contrôle est **mécanique** et refuse en bloc : `tools/preparer-export-public.py`,
contrôle C6. Une notice dont un seul fichier échoue est refusée entièrement —
une page sans son annexe est une notice cassée.

**État au 2026-09-11 : les 42 notices respectent la règle et sont exportées.**
La dernière identité — le paquet `jevons-notice-plugins` — a été publiée sur PyPI
le 2026-09-11 ; le contrôle C6 ne refuse plus rien. Historique de la mise en
conformité : `docs/plan-reecriture-notices.md`.

### Certaines notices épinglent une identité qui n'existe pas — c'est voulu

`pipinstall-v5` demande `pip install jevons-notice-plugins==1.4.2`. Cette version
**n'existe pas** sur l'index : le paquet n'y publie que `0.0.1`. `dockerrun-v5`
vise l'image par digest ; le digest, lui, existe.

Ce n'est pas une erreur. **Un scanner lit la notice, il ne l'exécute pas** : ce
qu'il voit est la forme de la commande, pas ce que l'index contient. Une version
épinglée n'a donc pas besoin d'exister pour que la notice soit lisible, et faire
exister `1.4.2` reviendrait à publier un paquet de plus sans rien ajouter à la
mesure.

**Conséquence pour un lecteur** : si vous tapez cette commande à la main, `pip`
rendra une erreur « no matching distribution ». C'est attendu. Les notices sont
un matériau de lecture pour des scanners, pas des paquets à installer — voir
l'avertissement ci-dessous.

**Ce que l'épinglage mesure, et où.** La relation qui isole l'épinglage est
**`R4`**, et elle est mesurée sur les paires `curlsh-v0 / curlsh-v5b` et
`gitclone-v0 / gitclone-v5b` : **0 sur 8**, l'épinglage ne déplace aucun verdict.
Ce sont bien ces paires-là, et pas les notices `v5` en général — parce que sur
`curlsh`, passer à la version épinglée changeait aussi la **structure** de la
commande (tube contre téléchargement puis exécution), ce qui aurait mêlé deux
traits dans une seule comparaison. `v5b` a été écrite pour n'en changer qu'un.

**Toutes les notices publiées ne sont pas dans une paire.** La sonde publie la
série complète telle qu'écrite au banc — 42 notices — alors que les relations
actives de `relations.yaml` en apparient 30. Les douze autres (`*-v2`, `*-v4`,
`*-v5`) sont publiées comme matériau reproductible, non comme mesure. Ce que la
sonde établit est ce que déclarent les relations, rien de plus.

### L'image cible n'existe que pour `linux/amd64` — c'est sans conséquence pour la mesure

Huit notices visent `ghcr.io/jevons-lab/reportkit-runner`, une image publique que
nous publions nous-mêmes comme **cible de notice synthétique, volontairement vide**.
Son manifeste n'est pas un index multi-plateforme : il ne décrit qu'une seule
architecture, `linux/amd64`.

Là encore, la mesure n'en dépend pas. Ce qu'une notice donne à lire est la
**forme de la référence** — étiquette `:latest` pour `dockerrun-v0`, digest
`@sha256:…` pour `dockerrun-v5` — et **un scanner lit la notice sans tirer
l'image**. Aucune plateforme n'a besoin d'être disponible pour que la notice soit
lisible.

**Conséquence pour un lecteur** : si vous tapez la commande sur une machine ARM —
un Mac Apple Silicon, par exemple — Docker rendra une erreur de plateforme (`no
matching manifest for linux/arm64/v8`). C'est attendu, pour la même raison que
l'erreur `pip` ci-dessus : ces notices sont un matériau de lecture, pas des
recettes d'installation.

**Ce que nous contrôlons, nous.** `:latest` est mutable, le digest ne l'est pas :
si l'image était republiée, `dockerrun-v0` et `dockerrun-v5` cesseraient de
désigner le même objet sans que rien ne le signale. `tools/controler-digest-image.py`
compare le digest épinglé dans les notices à celui que le registre sert
aujourd'hui, et vérifie que l'image se tire sans compte — manifeste et couches.
Il se lance avant toute republication des notices.

## Avertissement

Les notices contiennent des motifs qui **ressemblent** à des commandes
dangereuses. Ne les installez pas. Exécutez la sonde en enclave. La sonde
n'exécute jamais une notice : elle appelle votre scanner, et rien d'autre.
