# Rapport de sonde — skillvet 2.0.9, revision archivee swh a350337f

| | |
|---|---|
| scanner | `bash <enclave> --json {path}` |
| version | skillvet 2.0.9, revision archivee swh a350337f |
| adaptateur | `skillvet` |
| version de l'ordinal | 2 (0=clean, 1=info, 2=low, 3=medium, 4=high, 5=critical) |
| date | 2026-09-09T06:57:38Z |
| périmètre | repertoire |
| empreinte de `relations.yaml` | `b7851afa94673a92ed7cce5641fc931a` |
| empreinte des notices | `ef14aa6b9507773d36ee658447b3947b` |

## Ce que ce rapport mesure

Chaque relation compare **deux notices dont un seul trait diffère**. Si le
scanner lit ce trait, son verdict doit bouger — ou rester stable, selon la
relation. La sonde ne dit pas si le scanner est bon : elle dit **ce qu'il lit**.

La grandeur comparée est un ordinal. Depuis l'amendement du 2026-09-09
(spec 2 §9) il compte **six** niveaux — `clean`, `info`, `low`, `medium`,
`high`, `critical` — parce que la version à quatre niveaux confondait `high`
et `critical` et perdait, sur ce seul point, un résultat publié. Le score brut
est reporté quand le scanner en rend un, et n'entre dans aucun compte.

## Résultats par relation

| relation | énoncé | attendu | tenue, ligne ordinale | tenue, ligne de sévérité |
|---|---|---|---|---|
| `R1` | Ajouter une confirmation explicite avant le geste change le verdict | `verdict_change` | **0 / 4** | 0 / 4 |
| `R3` | Formuler la garde avec les mots de la menace augmente le score | `verdict_change` | **0 / 4** | 0 / 4 |
| `R4` | Epingler la reference, structure de commande constante, change le verdict | `verdict_change` | **0 / 2** | 0 / 2 |
| `R5` | Une phrase de securite decorative change le verdict | `verdict_stable` | **4 / 4** | 4 / 4 |
| `R7` | Meme code distant, meme absence de garde, forme de commande differente | `verdict_stable` | **3 / 6** | 3 / 6 |
| `R-perimetre` | Le meme geste, porte par la page ou par une annexe scripts/install.sh | `verdict_stable` | **3 / 4** | 3 / 4 |

**Deux lignes, déclarées.** La *ligne ordinale* normalise entre outils : `clean`, `info`, `low`, `medium`, `high`, `critical`
(ordinal version 2). La *ligne de sévérité* compare l'étiquette rendue par le
scanner telle quelle, sans normalisation. Les deux sont rapportées ; aucune ne
remplace l'autre. `sonde/acceptation.md` montre un cas où elles ne comptent pas
la même chose, et pourquoi.

### `R1` — 0 / 4

le verdict DEVRAIT changer entre A (sans garde) et B (garde explicite)

V1 = garde en prose neutre. V2 (permission/approval) et V4 (garde en code) sont la relation R2, hors de cette sonde publique.

| A | B | comportement | ordinal A | ordinal B | sévérité A | sévérité B | tenue |
|---|---|---|---|---|---|---|---|
| `curlsh-v0` | `curlsh-v1` | curlsh | 3 | 3 | blocked | blocked | **non** |
| `dockerrun-v0` | `dockerrun-v1` | dockerrun | 0 | 0 | clean | clean | **non** |
| `gitclone-v0` | `gitclone-v1` | gitclone | 0 | 0 | clean | clean | **non** |
| `pipinstall-v0` | `pipinstall-v1` | pipinstall | 0 | 0 | clean | clean | **non** |

### `R3` — 0 / 4

V3 (garde formulée en negatif charge : « never silently », « supply-chain risk ») DEVRAIT etre au moins aussi alerte que V0

| A | B | comportement | ordinal A | ordinal B | sévérité A | sévérité B | tenue |
|---|---|---|---|---|---|---|---|
| `curlsh-v0` | `curlsh-v3` | curlsh | 3 | 3 | blocked | blocked | **non** |
| `dockerrun-v0` | `dockerrun-v3` | dockerrun | 0 | 0 | clean | clean | **non** |
| `gitclone-v0` | `gitclone-v3` | gitclone | 0 | 0 | clean | clean | **non** |
| `pipinstall-v0` | `pipinstall-v3` | pipinstall | 0 | 0 | clean | clean | **non** |

### `R4` — 0 / 2

V5b epingle la reference SANS toucher a la structure de commande : le verdict DEVRAIT changer entre A (flottant) et B (epingle)

V5b n'existe que la ou V5 changeait la structure de commande. La version V5, publiee au banc, melange epinglage et structure : c'est V5b qui isole le trait.

| A | B | comportement | ordinal A | ordinal B | sévérité A | sévérité B | tenue |
|---|---|---|---|---|---|---|---|
| `curlsh-v0` | `curlsh-v5b` | curlsh | 3 | 3 | blocked | blocked | **non** |
| `gitclone-v0` | `gitclone-v5b` | gitclone | 0 | 0 | clean | clean | **non** |

### `R7` — 3 / 6

F0 a F3 executent le meme code distant non epingle sans confirmation : le verdict NE DEVRAIT PAS changer

F0 tube | F1 telecharger puis executer | F2 substitution de commande | F3 verifier une empreinte fournie par la notice, puis executer.

| A | B | comportement | ordinal A | ordinal B | sévérité A | sévérité B | tenue |
|---|---|---|---|---|---|---|---|
| `curlsh-f0` | `curlsh-f1` | curlsh | 3 | 0 | blocked | clean | **non** |
| `curlsh-f0` | `curlsh-f2` | curlsh | 3 | 0 | blocked | clean | **non** |
| `curlsh-f0` | `curlsh-f3` | curlsh | 3 | 0 | blocked | clean | **non** |
| `gitclone-f0` | `gitclone-f1` | gitclone | 0 | 0 | clean | clean | oui |
| `gitclone-f0` | `gitclone-f2` | gitclone | 0 | 0 | clean | clean | oui |
| `gitclone-f0` | `gitclone-f3` | gitclone | 0 | 0 | clean | clean | oui |

### `R-perimetre` — 3 / 4

en mode repertoire, le verdict NE DEVRAIT PAS changer selon que le geste est dans la page ou dans une annexe

Rejouee en mode page seule, l'attendu devient une mesure descriptive : combien d'outils deviennent muets. Voir --perimetre.

| A | B | comportement | ordinal A | ordinal B | sévérité A | sévérité B | tenue |
|---|---|---|---|---|---|---|---|
| `curlsh-v0` | `curlsh-v0-annexe` | curlsh | 3 | 3 | blocked | blocked | oui |
| `dockerrun-v0` | `dockerrun-v0-annexe` | dockerrun | 0 | 2 | clean | caution | **non** |
| `gitclone-v0` | `gitclone-v0-annexe` | gitclone | 0 | 0 | clean | clean | oui |
| `pipinstall-v0` | `pipinstall-v0-annexe` | pipinstall | 0 | 0 | clean | clean | oui |

## Signature lue — quelles formes de commande déclenchent

Même code distant, même absence de garde, forme de commande différente.

| comportement | forme | ordinal | sévérité | score brut |
|---|---|---|---|---|
| curlsh | `f0` | 3 | blocked | 9 |
| curlsh | `f1` | 0 | clean | 0 |
| curlsh | `f2` | 0 | clean | 0 |
| curlsh | `f3` | 0 | clean | 0 |
| gitclone | `f0` | 0 | clean | 0 |
| gitclone | `f1` | 0 | clean | 0 |
| gitclone | `f2` | 0 | clean | 0 |
| gitclone | `f3` | 0 | clean | 0 |

## Deux scores de synthèse, à ne pas surinterpréter

| | valeur | lecture |
|---|---|---|
| `sensibilite_syntaxique` | 0.5 | part des paires R7 où le verdict change alors que le comportement est identique |
| `cecite_semantique` | 1.0 | part des paires R1+R4 où le verdict ne change pas alors que la garde ou l'épinglage change |

Ces deux nombres résument des dénominateurs de quelques unités. Ils ne se
citent jamais seuls, et ne classent aucun outil.

## Réserves

- Mode statique, configuration par défaut du scanner, une seule version.
- Périmètre : repertoire. Un geste déplacé dans une annexe n'est pas vu de la même
  façon selon que l'on scanne la page ou le répertoire.
- Les notices sont **synthétiques** : comportement simulé, cibles en domaines
  réservés, aucune charge réelle. Elles mesurent la lecture d'un trait, pas
  la capacité à trouver une attaque réelle.
- Dénominateurs de quelques unités par relation. Aucun taux de population.
- Ce rapport porte sur **un scanner**. Il n'établit aucun classement.

