# Registre JEVONS — vue publique

**JEVONS — https://github.com/jevons-lab**
Dépôt cible : `github.com/jevons-lab/registre` — *nom provisoire, rien
n'est publié à ce jour.*

Vue publique du registre. Les entrées **ouvertes** sont données en clair.
Les entrées **scellées** sont réduites à leur sceau : numéro, date, classe,
empreinte du contenu, empreinte de chaîne — **rien d'autre**. Ni titre, ni
corps, ni sources, ni nom de juge.

Un sceau n'est pas un secret sans conséquence : il date le fait et fige son
contenu. Le jour où l'entrée s'ouvre, chacun peut vérifier que le texte
publié est bien celui dont l'empreinte était scellée à cette date.

Vérifier la chaîne : `python3 tools/registre.py verifier`

| n | date | classe | statut | type | titre |
|---|---|---|---|---|---|
| 1 | 2026-09-08 | 1 (`nous`) | ouverte | `retractation` | Retrait d'une interprétation le jour de sa publication — passe par modèle de langage |
| 2 | 2026-09-08 | 1 (`nous`) | ouverte | `rectification` | Recomptage de la strate synthétique : 46 notices annoncées, 42 réelles |
| 3 | 2026-09-08 | 2 (`juge_open_source`) | ouverte | `defaut_tiers` | SkillWatch 0.4.1 — le motif d'extraction d'URL capte l'accolade fermante d'une expansion shell |
| 4 | 2026-09-08 | 1 (`nous`) | ouverte | `anomalie_documentaire` | « Six des sept » contre sept sur sept — une phrase de synthèse contredit le relevé qu'elle résume |
| 5 | 2026-09-09 | — | acte | `classement` | Acte de classement des entrées 1 à 4 — règle de publication du 2026-09-09 |
| 6 | 2026-09-09 | 1 (`nous`) | ouverte | `rectification` | R7 — le « 3 sur 4 » dépend de la ligne de lecture, et notre instrument en perdait un |
| 7 | 2026-09-09 | 2 (`juge_open_source`) | ouverte | `defaut_tiers` | skillvet 2.0.9 — l'émetteur SARIF déclare une identité et une version qui ne sont pas les siennes |
| 8 | 2026-09-09 | 1 (`nous`) | ouverte | `rectification` | Passage 6 — deux dérives « instruction » étaient du bruit d'instrument |
| 9 | 2026-09-09 | 1 (`nous`) | ouverte | `rectification` | Export — les 42 notices visaient quatre identités libres ; refusées avant publication |
| 10 | 2026-09-09 | 1 (`nous`) | ouverte | `observation` | R-identité — une première paire mesurée, non cherchée |
| 11 | 2026-09-09 | 1 (`nous`) | ouverte | `rectification` | R-identité — écart de verdict sur une paire, skillvet W7 : observation isolée, N=1, non généralisée |
| 12 | 2026-09-09 | 1 (`nous`) | ouverte | `rectification` | Rectification de l'entrée 8 — l'observation porte sur les passages 5 et 6, non sur le seul passage 6 |
| 13 | 2026-09-09 | 1 (`nous`) | ouverte | `regle` | Entrées bilingues à partir de l'entrée 13 — première entrée sous cette règle |
| 14 | 2026-09-09 | 1 (`nous`) | ouverte | `rectification` | Complément à l'entrée 12 — deux imprécisions du titre de l'entrée 8, et la répartition des bascules entre deux causes distinctes |
| 15 | 2026-09-09 | 1 (`nous`) | ouverte | `rectification` | SUBSTANTIEL — les trois URL mesurées de l'entrée 8, en clair : son corps les porte désamorcées et la mesure n'y est pas rejouable |
| 16 | 2026-09-09 | 1 (`nous`) | ouverte | `observation` | SUBSTANTIEL — le juge 1 refuse de juger jev-0033 : le cas est indéterminable, et 3a passe à 6 scellables au mieux sur 7 |
| 17 | 2026-09-09 | 1 (`nous`) | ouverte | `observation` | SUBSTANTIEL — passe de rejugement 3a/3b : 11 cas rejugés par deux modèles, 7 tiennent, 4 ne tiennent pas |
| 18 | 2026-09-09 | 1 (`nous`) | ouverte | `observation` | SUBSTANTIEL — jev-0039 : les deux juges divergent sous la définition en vigueur, le cas n'est pas scellé |
| 19 | 2026-09-09 | 1 (`nous`) | ouverte | `rectification` | SUBSTANTIEL — jev-0062 : sous la définition en vigueur, le juge 1 passe de bénin à dangereux par conception, et le 0 sur 4 du rapport §5 ne tient plus sur ce cas |
| 20 | 2026-09-09 | 3 (`juge_proprietaire_ou_service`) | scellée | — | *scellée* |
| 21 | 2026-09-09 | 3 (`juge_proprietaire_ou_service`) | scellée | — | *scellée* |
| 22 | 2026-09-09 | 1 (`nous`) | ouverte | `rectification` | SUBSTANTIEL — régime de verdict : même PASS publié, régimes différents sur cinq cas de 3a, et le partage suit la date de saisie |
| 23 | 2026-09-09 | 1 (`nous`) | ouverte | `rectification` | SUBSTANTIEL — 48 fiches reclassées du régime « sans objet » au régime « cas » ; le §5 du rapport est inchangé, la contradiction entre fiches et carte est levée |
| 24 | 2026-09-09 | 1 (`nous`) | ouverte | `rectification` | Précision à l'entrée 23 — les 19 `verdict_concordance` renseignés le sont par comparaison mécanique, non par jugement de contenu |
| 25 | 2026-09-09 | 1 (`nous`) | ouverte | `observation` | SUBSTANTIEL — quatre artefacts mesurés ne figurent plus au catalogue, et le motif qu'ils portaient est présent dans 22 artefacts sur 344 |
| 26 | 2026-09-09 | 1 (`nous`) | ouverte | `rectification` | Rectification de l'entrée 20 — deux faits ont changé après son sceau, le jour même : le régime de quatre de ses cas, et la présence de quatre de ses artefacts |
| 27 | 2026-09-10 | — | acte | `classement` | Acte d'ouverture de l'entrée 3 — le signalement à l'éditeur de l'outil est publié, le sceau a fait son office |
| 28 | 2026-09-10 | 1 (`nous`) | ouverte | `rectification` | SUBSTANTIEL — une décision de transparence appliquée dans le registre et silencieusement annulée dans deux sorties, par deux générateurs distincts |
| 29 | 2026-09-11 | 1 (`nous`) | ouverte | `observation` | Le registre est public — bascule du 2026-09-11, 28 entrées servies sur jevons.fr |
| 30 | 2026-09-11 | 1 (`nous`) | ouverte | `rectification` | Rectification de l'entrée 29 — la cause de l'écart HTTPS n'était ni la propagation ni le réseau, mais l'horloge de notre propre enclave |

---

## 1. Retrait d'une interprétation le jour de sa publication — passe par modèle de langage

**Date du fait** 2026-09-08 — **type** `retractation` — **classe** 1 `nous` — **statut** ouverte

Première entrée du registre, telle que prévue au §6 de la spec 4 : la
rétractation du 2026-09-08, reprise **telle quelle** du §6 du rapport
`docs/resultats-banc-2026-09-08.md`.

> **RÉSERVE DE VALIDITÉ, ajoutée le jour même de la mesure.** L'interprétation
> initiale — « un modèle de langage ne détecte pas davantage l'absence de
> garde » — n'est pas soutenue. Vérification faite après coup sur le code de
> l'outil : il appelle trois analyseurs, dont un impose une taxonomie fermée à
> quatre catégories où la récupération sans garde ne figure pas. Cet analyseur
> n'a rendu aucun constat sur les sept cas ; les deux autres en ont rendu seize.
>
> Le 0/7 mesure donc une couverture de taxonomie et une agrégation, pas une
> limite d'inférence.
>
> **Fait nouveau, non anticipé.** Sur les sept cas, trois portent une phrase
> signalant explicitement l'absence de garde, et le modèle **la cite dans un
> constat de risque** — puis le verdict global reste au niveau intermédiaire.
> Le défaut observable n'est pas une cécité : c'est une **rupture entre le
> constat et son agrégation en verdict**.

Ce que cette entrée établit : le dispositif trouve ses propres erreurs, les
date, et les publie avec le reste. Elle porte sur **nous**, pas sur un tiers.

> **Note de genèse.** Cette chaîne a été refondée le 2026-09-08, AVANT toute publication et avant tout horodatage externe. Un brouillon de deux entrées existait, dans un ordre différent ; il est conservé tel quel dans `registre/brouillon-2026-09-08.jsonl` (sha256 du fichier `3f8ac7129065d288e326265f198a575d3b1f34704a39eb6ec3228cf049848520`, tête de chaîne `b6a212d4e35e26c6e58005d2c2168af135a08e35274216b394fb70c32d1a0136`). Rien n'a été détruit. À compter de cette entrée, la règle est stricte : aucune entrée n'est modifiée, réordonnée ni supprimée ; une entrée fausse se corrige par une entrée suivante qui la rectifie, et les deux restent lisibles.

**Sources**

- docs/resultats-banc-2026-09-08.md §6
- docs/passe-llm-resultats.md §0 bis « RÉSERVE DE VALIDITÉ »
- docs/jalon3-resultats.md, réserve 1, « CORRIGÉ le même jour »
- .log/134-prompt-llm.txt (prompt effectif de l'outil, recopié)
- .log/135-nature-cecites.txt (nature des sept cécités)

```
empreinte du contenu  sha256:5b0659f18e7cf9d4cc891106a6e7b5218647e6b81e4cc58e1c3fcd3a33a61d4b   (recalculée)
empreinte             77ae7a6a263ab24fe48ed85566a9e51b9e27aeb0834158e29af822bd8592cead
empreinte précédente  0000000000000000000000000000000000000000000000000000000000000000
```

---

## 2. Recomptage de la strate synthétique : 46 notices annoncées, 42 réelles

**Date du fait** 2026-09-08 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

**Rectification d'un compte publié par nous.**

**Ce qui était écrit.** La strate synthétique en paires contrôlées était
décomptée à **46 notices**.

**Ce qui est vrai.** **42 notices**. Le décompte de 46 additionnait les notices
et les quatre annexes `scripts/install.sh` de la relation de périmètre. Une
annexe n'est pas une notice : elle porte le geste hors de la page d'une notice
qui existe déjà, et elle n'a pas de variante propre.

**Contrôle sur pièces, 2026-09-08.**

```
find corpus/paires -name SKILL.md | wc -l   →  42
find corpus/paires -type f | wc -l          →  46
```

Le 46 est donc un compte de **fichiers**, pas de notices. Détail des 42 :
4 comportements (`gitclone`, `dockerrun`, `curlsh`, `pipinstall`) × 7 variantes
(`v0`…`v6`) = 28 ; plus 4 notices de périmètre `v0-annexe` ; plus 2 contrôles
`v5b` (`curlsh`, `gitclone`) ; plus 8 notices `R7`
(`curlsh-f0..f3`, `gitclone-f0..f3`).

**Ce que la rectification ne change pas.** Aucun résultat publié ne repose sur
le nombre 46. Les relations sont comptées en **paires**, pas en notices :
R1 0/16, R3 0/16, R4 0/8, R5 0/16 gardent leurs dénominateurs. Cette entrée
corrige un compte de dénombrement, pas une mesure.

**Ce qu'elle établit.** Un chiffre d'inventaire faux a circulé dans nos propres
documents jusqu'à ce qu'une vérification mécanique le contredise. La correction
est datée ici plutôt que réécrite en silence dans les fichiers d'origine.

**Sources**

- spec-2-sonde-syntaxique.md §1, « Note de recomptage (2026-09-08) »
- HANDOVER.md, table « Vérifications effectuées », ligne `corpus/paires (46 notices)` — verdict DIFFÈRE
- .log/136-plan-inventaire.txt, comptes « SKILL.md sous corpus/paires » et « fichiers sous corpus/paires »
- docs/preenregistrement-paires.md (plan des variantes, commité avant les notices)

```
empreinte du contenu  sha256:8fa5b01249be57d34af53bd625483a152f45a8166344a558b52609a5a736595e   (recalculée)
empreinte             85f80dc3b228d98af5afa66645d42e55b7a3f6dd668cc755f1d6ac92a5e00149
empreinte précédente  77ae7a6a263ab24fe48ed85566a9e51b9e27aeb0834158e29af822bd8592cead
```

---

## 3. SkillWatch 0.4.1 — le motif d'extraction d'URL capte l'accolade fermante d'une expansion shell

**Date du fait** 2026-09-08 — **type** `defaut_tiers` — **classe** 2 `juge_open_source` — **statut** ouverte

**Premier fait tiers du registre.**

**L'outil.** SkillWatch 0.4.1, PyPI, publiée le 2026-07-29, dépôt
`kuzivaai/SkillWatch`, état déclaré par l'éditeur « Development Status :: 3 -
Alpha ». Objet déclaré : surveiller les pages web auxquelles renvoient les
skills et les outils MCP, et signaler qu'elles ont changé après examen.

**Le fait.** Son motif d'extraction d'URL n'exclut pas l'accolade fermante :

```python
_RAW_URL_RE = re.compile(r"(?<!\()(https?://[^\s\)\]\"'>]+)")
```
`skillwatch/parser.py`, l. 15. Le jeu de caractères exclus contient l'espace,
la parenthèse, le crochet, le guillemet, l'apostrophe et le chevron — pas
l'accolade.

**La ligne d'origine.** Constatée le 2026-09-08 sur un artefact public réel
(corpus JEVONS `jev-0081`, `SKILL.md:32`), désamorcée ici selon la convention
du dépôt :

```
export I4H_WORKFLOWS_REPO_URL="${I4H_WORKFLOWS_REPO_URL:-hxxps://github[.]com/isaac-for-healthcare/i4h-workflows}"
```

L'URL est la valeur par défaut d'une expansion `${VAR:-valeur}`. L'accolade qui
ferme l'expansion est donc collée à l'URL.

**Ce que l'outil surveille alors.** L'URL enregistrée est
`hxxps://github[.]com/isaac-for-healthcare/i4h-workflows}` — accolade comprise.
Elle rend HTTP 404. L'outil le déclare (`errors: 1` dans la sortie de `scan`),
mais la référence réelle de l'artefact n'est surveillée par personne. La
couverture apparente est de 1 URL sur 1 ; la couverture réelle est nulle.

**Reproduction, exécutée le 2026-09-08 en enclave, cible en domaine réservé.**
Fichier `SKILL.md`, sha256
`b5a895bb1261d6eecb11003439ae9ef8891cfcb5cfc0b4bc5a88f5b29241508f`, portant :

```bash
export REPO_URL="${REPO_URL:-https://example.invalid/page}"
```

Commande : `skillwatch --db repro.db add SKILL.md`. Sortie :

```
X  https://example.invalid/page} (blocked: private/reserved)
Added 0 URL(s) from SKILL.md
```

L'accolade est visible dans l'URL rendue. Le blocage qui suit vient du garde
anti-SSRF de l'outil sur le TLD réservé `.invalid` : il est indépendant du
défaut et n'en fait pas partie.

**Portée, et ce que cette entrée ne dit pas.** Le fait est un motif d'extraction
trop large d'un caractère. Il n'est pas dit ici qu'il est fréquent, ni qu'il
est grave, ni qu'aucun autre outil ne l'a. Aucun classement d'outils n'est
établi. Le même défaut, sur le même caractère et pour la même cause, existait
dans notre propre extracteur `tools/extraire-references.py` et y a été corrigé
le 2026-09-08, quelques heures avant ce constat.

**Aucune divulgation à l'éditeur n'a encore été faite** à la date de cette
entrée.

**Sources**

- skillwatch/parser.py l. 14-15 (paquet PyPI skillwatch==0.4.1)
- corpus/references/motifA-references.jsonl — jev-0081, SKILL.md:32
- scanners/skillwatch/brut/jev-0081.page.scan.json
- scanners/skillwatch/brut/jev-0081.page.list.txt
- juges.yaml — ligne skillwatch, couverture_type_reference
- docs/journal.md, entrée du 2026-09-08

```
empreinte du contenu  sha256:d93a6b5d5e692e2778630ae053c8a667ee7eb820c4202574f850fafe6b668044   (recalculée)
empreinte             07c0b277690d4870746bc55d6c8bbff1cd065be8804d5cb2e5f4d6f960a6634f
empreinte précédente  85f80dc3b228d98af5afa66645d42e55b7a3f6dd668cc755f1d6ac92a5e00149
```

---

## 4. « Six des sept » contre sept sur sept — une phrase de synthèse contredit le relevé qu'elle résume

**Date du fait** 2026-09-08 — **type** `anomalie_documentaire` — **classe** 1 `nous` — **statut** ouverte

**Anomalie dans nos propres documents, constatée et non corrigée dans les
fichiers d'origine.**

**Ce qui est écrit.** `.log/135-nature-cecites.txt` l. 344 et `docs/journal.md`
l. 6861 portent la même phrase :

> la non-alerte de ces sept cas sur la ligne stricte ne se joue pas sur
> l'absence de constat — **six des sept** en portent.

**Ce que dit le relevé du même fichier.** L'en-tête de chaque section de
`.log/135-nature-cecites.txt` donne le nombre de constats par cas :
`jev-0033` 3, `jev-0039` 4, `jev-0045` 2, `jev-0078` 3, `jev-0079` 2,
`jev-0080` 2, `jev-0081` 3. Soit **sept sur sept**, de 2 à 4 constats chacun.

**Ce que la carte retrouve.** Recompté depuis les sorties brutes de la passe par
modèle de langage, indépendamment de `.log/135` : les sept cas portent chacun au
moins un constat. Aucun n'en est dépourvu.

La phrase de synthèse contredit donc le relevé qu'elle résume, dans le même
fichier.

**Portée.** Aucun chiffre des §3, §4, §5 ou §7 du rapport n'en dépend, et la
conclusion que la phrase servait — « la non-alerte ne se joue pas sur l'absence
de constat » — est renforcée, non affaiblie, par le chiffre exact.

**Décision.** Les fichiers d'origine ne sont pas corrigés. L'anomalie est datée
ici, et `corpus/carte/carte.md` §11 et §13 y renvoient. Motif : réécrire une
phrase dans un journal daté après coup vaut moins qu'un désaccord daté que
n'importe qui peut vérifier sur les deux textes.

**Sources**

- .log/135-nature-cecites.txt l. 344 et en-têtes de section
- docs/journal.md l. 6861
- corpus/carte/carte.md §11 « Passe par modèle de langage — constats et verdict »
- corpus/carte/carte.jsonl — champs n_constats_semantiques et n_constats_statiques du juge llm_stricte
- .log/92-jalon3-llm/ (sorties brutes, 124 cas)

```
empreinte du contenu  sha256:0facd460c47aecd2296b5a32bb7eba9a53827ffce246326fbc88eb9b6f513ba0   (recalculée)
empreinte             585ee9323d4b421936bdfe8d224a87169c51d4cf72496dad9b46d1509cb72be1
empreinte précédente  07c0b277690d4870746bc55d6c8bbff1cd065be8804d5cb2e5f4d6f960a6634f
```

---

## 5. Acte de classement des entrées 1 à 4 — règle de publication du 2026-09-09

**Date du fait** 2026-09-09 — **type** `classement`

La règle de publication du registre est posée le 2026-09-09 : chaque entrée
porte une **classe** (1 nous, 2 juge open source, 3 juge propriétaire ou
service, 4 artefact nommé, 5 client — jamais écrite), un **statut** (`scellee`
ou `ouverte`), ses dates de scellement et d'ouverture, et l'empreinte de son
contenu.

Les entrées 1 à 4 ont été écrites **avant** cette règle. Elles ne peuvent donc
pas la porter dans leur corps : les modifier casserait la chaîne, et
l'interdiction de modifier vaut d'abord pour nous. Le classement est donc
lui-même une entrée, datée et chaînée comme les autres. L'état effectif d'une
entrée se lit : ses champs natifs, puis les actes de classement postérieurs, le
dernier l'emportant.

Deux règles que cet acte engage pour la suite :

- **Une entrée ouverte ne se referme jamais.** Un acte de classement qui
  tenterait de resceller une entrée ouverte est refusé par `verifier`, et
  l'anomalie est affichée.
- **Une rétractation est une entrée nouvelle**, jamais une réécriture.

L'entrée 3 est scellée **jusqu'au jour de l'issue** déposée auprès de
l'éditeur de l'outil concerné. Un sceau ne cache pas un fait : il en date
l'existence et en fige le contenu. Le jour de l'ouverture, chacun pourra
vérifier que le texte publié est bien celui dont l'empreinte était scellée à
cette date. Le brouillon de l'issue existe, il n'est pas envoyé, et aucune
décision d'envoi n'est prise à la date de cet acte.

| entrée | classe | statut | scellée le | ouverte le |
|---|---|---|---|---|
| 1 | 1 (`nous`) | ouverte | — | 2026-09-09 |
| 2 | 1 (`nous`) | ouverte | — | 2026-09-09 |
| 3 | 2 (`juge_open_source`) | scellee | 2026-09-09 | — |
| 4 | 1 (`nous`) | ouverte | — | 2026-09-09 |

**Sources**

- registre/README.md — règle de publication et règle propre à la classe 3
- docs/disclosures/skillwatch-0.4.1-brace.md — brouillon non envoyé
- tools/registre.py — mise en oeuvre de l'état effectif et de la vue publique

```
empreinte du contenu  sha256:ed91270b448ea29e31ab8b89d1bf63908e08063fe82b21a466acbb00bdce1479
empreinte             f468ef732d4a17f9158e5bab866576387c3c9a81a37511c25e55d4c478d19af5
empreinte précédente  585ee9323d4b421936bdfe8d224a87169c51d4cf72496dad9b46d1509cb72be1
```

---

## 6. R7 — le « 3 sur 4 » dépend de la ligne de lecture, et notre instrument en perdait un

**Date du fait** 2026-09-09 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

**Fait sur notre propre instrument, pas sur un outil tiers.**

**Ce qui est publié.** Le §2 du rapport du banc écrit, pour la relation R7 —
même code distant, même absence de garde, forme de commande différente —
« change chez 3 outils sur 4 ».

**Ce que la sonde a d'abord rendu.** 2 sur 4. Le chiffre publié n'était pas
reproductible par l'instrument censé le reproduire.

**Cause, trouvée dans l'instrument et non dans les données.** L'ordinal défini
au §3 de la spec 2 comptait quatre niveaux : `0` propre, `1` info, `2`
bas/moyen, `3` haut/critique. Il rangeait donc `HIGH` et `CRITICAL` sur la même
valeur. Sur le comportement `curl`, le verdict de Cisco bascule entre `HIGH` et
`CRITICAL` selon la forme de la commande — c'est l'un des trois changements
comptés au banc, et il était **invisible** à un ordinal qui confond les deux.

**Les deux lignes, mesurées.**

| ligne de lecture | outils dont le verdict change sur `curl` |
|---|---|
| étiquette de sévérité, comparée telle quelle | 3 sur 4 |
| ordinal à quatre niveaux (spec 2 §3, version 1) | 2 sur 4 |
| ordinal à six niveaux (amendement du 2026-09-09) | 3 sur 4 |

**Ce qui a été fait.** Deux choses, aucune rétroactive.

1. La sonde rapporte désormais **les deux lignes côte à côte** — l'ordinal, qui
   normalise entre outils, et l'étiquette de sévérité, qui ne perd rien. Aucune
   ne remplace l'autre, et chaque rapport dit laquelle reproduit quel chiffre.
2. L'ordinal passe à **six niveaux** (`clean`, `info`, `low`, `medium`, `high`,
   `critical`), amendement daté du 2026-09-09 au §9 de la spec 2. Les rapports
   produits avant cette date restent sous la version 1 et ne sont pas
   recalculés ; chaque rapport porte `ordinal_version`.

**Ce que cette entrée n'établit pas.** Aucun chiffre publié n'est modifié.
Aucun outil tiers n'est en cause : les quatre scanners ont rendu ce qu'ils
rendaient déjà. Ce qui a changé est notre façon de lire ce qu'ils rendent.

**Ce qu'elle établit.** Un instrument de mesure peut détruire silencieusement la
distinction sur laquelle repose un résultat qu'il est censé vérifier. Ici la
perte a été trouvée parce que la sonde a été confrontée à un chiffre déjà
publié, et qu'elle ne l'a pas retrouvé. Sans cette confrontation, l'ordinal à
quatre niveaux aurait continué de rendre 2 sur 4 sans que rien ne le signale.

**Sources**

- docs/resultats-banc-2026-09-08.md §2, relation R7
- docs/paires-resultats.md §6 bis et §6
- .log/125-paires-lignes.txt sections 5.1 a 5.3
- spec-2-sonde-syntaxique.md §9, amendement du 2026-09-09
- sonde/acceptation.md
- sonde/rapports/ (ordinal version 1) et sonde/rapports-ordinal-v2/ (version 2)

```
empreinte du contenu  sha256:b4c5e0f13999cc18fda5f5e924c064719018cf1555e60b2789b6072ac7136f8f
empreinte             c41ac3b1e5cf174e50f4d77dc3c8142fc7e0ccff0ef47f81bf967fe5ff6cb561
empreinte précédente  f468ef732d4a17f9158e5bab866576387c3c9a81a37511c25e55d4c478d19af5
```

---

## 7. skillvet 2.0.9 — l'émetteur SARIF déclare une identité et une version qui ne sont pas les siennes

**Date du fait** 2026-09-09 — **type** `defaut_tiers` — **classe** 2 `juge_open_source` — **statut** ouverte

**Fait tiers, classe 2 : outil dont le code est public.**

**L'outil.** `skillvet`, scanner de sécurité pour skills d'agents, publié par
**`oakencore`**, en version **2.0.9**. Dépôt d'origine disparu publiquement ;
copie archivée par Software Heritage, instantané
`swh:1:snp:a350337fed1d59d1b45880389e1bd1c98d72f3d2` du 2026-04-02, chemin
`skills/oakencore/skillvet/`.

**Le fait.** Sa sortie SARIF annonce une identité et une version que ses
propres métadonnées contredisent.

`scripts/skill-audit.sh`, **ligne 1219** — l'objet `tool.driver` du document
SARIF :

```
"name":"skillvet","version":"2.1.0","informationUri":"https://github.com/nathangit/skillvet"
```

`scripts/skill-audit.sh`, **ligne 1212** — le `helpUri` porté par chaque règle
émise :

```
"helpUri":"https://github.com/nathangit/skillvet"
```

Les deux valeurs sont **écrites en dur**, et n'apparaissent nulle part ailleurs
dans le paquet.

**Les métadonnées contredites**, toutes dans la copie archivée :

| source | ce qu'elle dit |
|---|---|
| `_meta.json` | `"owner": "oakencore"`, `"slug": "skillvet"`, `latest.version` **2.0.9** |
| `SKILL.md`, frontmatter | `metadata.author: oakencore`, `metadata.version: "2.0.9"` |
| chemin dans l'arbre Software Heritage | `skills/oakencore/skillvet/` |
| `_meta.json`, historique des versions | commits sous `openclaw/skills`, puis `clawdbot/skills` |

Aucune version `2.1.0` ne figure dans l'historique des versions du paquet, qui
s'arrête à 2.0.9.

**Conséquence.** Un consommateur de SARIF — tableau de bord, agrégateur, revue
de code — qui fait confiance à `tool.driver.version` et à `informationUri`
attribue les constats à un autre dépôt et à une version qui n'existe pas. C'est
précisément ce que ces deux champs servent à établir dans le format SARIF :
quel outil, dans quelle version, a produit ce constat.

**Portée, et ce que cette entrée ne dit pas.** Ce n'est **pas un défaut de
sécurité** : aucune détection n'est affectée, aucun constat n'est faussé, et
aucune mesure du banc n'en dépend — la binarisation de skillvet au banc repose
sur le code de sortie, pas sur le SARIF. Il n'est pas dit ici que
`nathangit/skillvet` n'existe pas, ni qu'il n'a aucun rapport avec l'outil ; il
est dit que **le paquet archivé** déclare `oakencore` et `2.0.9` partout
ailleurs, et que ses deux lignes SARIF disent autre chose.

**Comment le fait a été trouvé.** En cherchant à résoudre une contradiction
entre deux de nos propres documents, dont l'un citait le SARIF et l'autre les
métadonnées. Aucun des deux n'avait tort : c'est l'outil qui se contredit
lui-même.

**Aucune divulgation à l'éditeur n'a été faite** à la date de cette entrée.

**Sources**

- tools/scanners/skillvet/scripts/skill-audit.sh l. 1212 et 1219
- tools/scanners/skillvet/_meta.json
- tools/scanners/skillvet/SKILL.md, frontmatter
- tools/scanners/skillvet/PROVENANCE.md, section « Attribution » (2026-09-09)
- juges.yaml, ligne skillvet, champ version_note
- sonde/rapports-ordinal-v2/skillvet/ et sonde/rapports/skillvet-sarif/

```
empreinte du contenu  sha256:bfce1eccd78ebd5f4cfccb56123b1632dea19c86d504d9f09d6c3e0fc448ae24
empreinte             9b05687706223b4b4cfc2acdca1f52f3437d957dfc32718f05045b39972719b6
empreinte précédente  c41ac3b1e5cf174e50f4d77dc3c8142fc7e0ccff0ef47f81bf967fe5ff6cb561
```

---

## 8. Passage 6 — deux dérives « instruction » étaient du bruit d'instrument

**Date du fait** 2026-09-09 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

**Fait sur notre propre instrument.**

**Ce qui a été rendu.** Les passages 5 et 6 de la re-vérification des références
externes ont classé **`instruction`** — la classe qui signale que le texte
normalisé d'une page a changé — deux références `url_doc` du corpus, pointant
toutes deux vers une page de dépôt GitHub.

**Ce que c'était.** Du bruit d'instrument. Contrôle fait avant d'accepter le
résultat : deux instantanés complets de la **même page**, à **90 secondes
d'intervalle**, sans qu'aucune modification n'ait eu lieu à la source.

Page contrôlée : `hxxps://github[.]com/nvidia-holoscan/holoscan-sdk`

```
tir 1  2026-09-09T05:27:58Z  taille 361882  contenu 55522584d269b4b3  instructions 974a4ae95e0dddd0
tir 2  2026-09-09T05:29:29Z  taille 361882  contenu 2f831b43014eb07f  instructions 01fdcc0fc19cc049

hash_contenu identiques      : False
hash_instructions identiques : False
```

Taille identique à l'octet près, empreintes différentes des deux côtés. Un
troisième contrôle, à 60 secondes cette fois et sur la seconde page GitHub
concernée (`hxxps://github[.]com/isaac-for-healthcare/i4h-workflows`), donne le
même résultat : `6de9628bf9607d47` puis `bdc00916bf4e3598`.

**Ce qui a échoué, exactement.** La normalisation de la règle `url_doc` version 1
— balises retirées, espaces réduits, casse abaissée — ne retire pas le **texte
visible qui varie d'une requête à l'autre** sur ces pages. L'empreinte du texte
normalisé change donc à chaque tir, et toute comparaison entre deux passages
rend `instruction`.

**Ce qui distingue les cas.** Les deux autres références `url_doc` du même lot,
qui pointent vers `hxxps://docs[.]nvidia[.]com`, sont **stables** : mêmes
empreintes à 60 secondes, et classées `inchange` au passage 6. Le défaut n'est
pas général à toute page web ; il est réel sur cet hébergeur, avec ces pages.

**Ce qui n'a pas été fait.** La règle n'a pas été corrigée après coup pour faire
disparaître le résultat. Elle avait été posée et datée avant la mesure ; les
passages 5 et 6 restent tels quels au journal des passages, avec leurs deux
`instruction`. Un amendement daté — canonisation des URL de forge, conservation
du texte normalisé, contrôle de volatilité à la pose de ligne de base,
persistance sur deux passages avant classement — est posé séparément et
s'applique **à partir du passage 7**.

**Ce que cette entrée établit.** Un dispositif qui surveille la dérive peut
produire de la dérive. Ici le faux positif a été trouvé parce qu'un chiffre
inattendu a déclenché un contrôle au lieu d'une publication : deux tirs
rapprochés suffisaient, et ils n'avaient jamais été faits. Une mesure de
changement sans contrôle de volatilité de l'instrument mesure les deux à la
fois, sans dire lequel.

**Portée.** Aucun artefact du corpus n'est en cause. Aucun outil tiers n'est en
cause. Aucune étiquette n'est déplacée.

**Sources**

- corpus/references/motifA-passages.jsonl — passages 5 et 6
- corpus/references/passages-motifA.md
- spec-3-derive-des-references.md §11, amendement url_doc v2 du 2026-09-09
- tools/instantane-references.py — texte_normalise, controle_volatilite
- docs/journal.md, entree du 2026-09-09

```
empreinte du contenu  sha256:1663cf24b05a1f6491a37501b7ea6fd1934241855621ea26ca00e7e232cf6732
empreinte             db2d1f64da97a34df63a101d0dc66187ce439c1dd1c57a4758b5380794f8917f
empreinte précédente  9b05687706223b4b4cfc2acdca1f52f3437d957dfc32718f05045b39972719b6
```

---

## 9. Export — les 42 notices visaient quatre identités libres ; refusées avant publication

**Date du fait** 2026-09-09 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

**Fait sur notre propre matériel, trouvé par un contrôle et non par une
relecture.**

**Ce qui allait être publié.** Les 42 notices de la strate synthétique en paires
contrôlées, avec le code de la sonde, dans un export public. Elles ont été
écrites le 2026-09-07 pour tourner en enclave, et jamais relues sous l'angle de
la publication.

**Ce que le contrôle a trouvé.** Les notices visent **quatre identités qui
n'appartiennent à personne**. Vérifié le 2026-09-09, depuis l'enclave :

| identité visée | occurrences | état constaté |
|---|---|---|
| domaine `install.reportkit-tools[.]dev` | 13 | ne résout pas — **libre** |
| dépôt `reportkit-tools/reportkit-plugins` | 13 | HTTP 404 sur l'API de la forge — **libre** |
| image de registre `reportkit/reportkit-runner` | 16 | HTTP 404 sur le registre public — **libre** |
| paquet `reportkit-plugins` | 36 | HTTP 404 sur l'index — **libre** |

**Ce que la publication aurait produit.** Quatre noms enregistrables, distribués
à tous les lecteurs, vers lesquels chaque utilisateur de la sonde aurait pointé
son scanner — et qu'un lecteur pressé aurait pu installer. C'est le mécanisme
exact que le corpus documente : le rachat d'une dépendance abandonnée, dont sept
cas du corpus et une entrée de la littérature externe portent la trace.

**Ce que la spec disait déjà.** Le §2 de la spec 2 pose la condition depuis son
écriture : « cibles = domaines réservés type `example.invalid` ». Les notices ne
la respectaient pas. **La règle existait, elle n'était pas contrôlée.** Elle
l'est désormais, mécaniquement, avant toute copie.

**Les deux défauts de ce contrôle, corrigés en chemin.**

1. **Sa première version ne regardait que les URL.** Elle laissait passer
   16 notices dont la cible est une **image de registre** ou un **paquet** —
   des noms tout aussi enregistrables qu'un domaine. Étendu aux images, aux
   paquets et aux dépôts, il refuse les 42.
2. **Elle refusait fichier par fichier.** Quatre pages de notice sortaient alors
   que l'annexe `scripts/install.sh` qui porte leur geste était refusée : une
   notice cassée, et une relation de périmètre qui ne mesure plus rien. Le refus
   se fait désormais **en bloc, par notice**.

Un contrôle qui laisse passer les deux tiers de ce qu'il devait arrêter n'a pas
échoué à moitié : il donne une garantie fausse. Les deux défauts ont été trouvés
en le faisant tourner, pas en le relisant.

**Ce qui a été publié.** Rien. L'export existe localement, sans notices, et
aucun dépôt distant n'est configuré.

**Ce que cette entrée établit.** Une règle écrite dans une spec et jamais
exécutée ne protège de rien. Celle-ci existait depuis l'écriture de la spec 2 ;
elle a tenu deux jours sans être vérifiée, et c'est la préparation d'un export
— pas une relecture — qui l'a mise à l'épreuve.

**Portée.** Aucun chiffre publié n'est en cause : les mesures du banc portent
sur ces notices telles qu'elles sont, exécutées en enclave, et restent vraies
pour elles. La réécriture sur identités réservées produira d'autres empreintes
de notices, donc une autre mesure, qui se lira comme telle.

**Sources**

- export-public/CONTROLE.md
- tools/preparer-export-public.py — controle C6
- spec-2-sonde-syntaxique.md §2, condition sur les cibles
- docs/plan-reecriture-notices.md — table de substitution et identites a enregistrer
- sonde/README.md et sonde/LICENSE-NOTICES — regle des notices publiques
- docs/journal.md, entree du 2026-09-09

```
empreinte du contenu  sha256:cd666f8b8a596d78505c613d9b8109f2f3067be30ba73c7b5b171689ab6520c1
empreinte             d3b727143bb5d035f5692642b74abe1ad8bfc774ac4f829c898e143bfdf94c42
empreinte précédente  db2d1f64da97a34df63a101d0dc66187ce439c1dd1c57a4758b5380794f8917f
```

---

## 10. R-identité — une première paire mesurée, non cherchée

**Date du fait** 2026-09-09 — **type** `observation` — **classe** 1 `nous` — **statut** ouverte

**Fait mesuré, et il faut dire d'abord comment il est arrivé.**

**Contexte.** Les 42 notices synthétiques du banc visaient quatre identités
libres ; elles ont dû être réécrites sur des identités réservées ou détenues
avant toute publication (entrée 9 de ce registre). La sonde a été rejouée sur
les notices réécrites, à seule fin de vérifier que la réécriture n'avait rien
cassé. **L'écart ci-dessous est apparu là. Il n'a pas été cherché**, et aucune
relation du dispositif ne le testait.

**La paire.** `dockerrun-v0` contre `dockerrun-v0-annexe` — même geste, une fois
porté par la page, une fois par une annexe `scripts/install.sh`. Outil :
skillvet 2.0.9, révision archivée, version épinglée.

| | notices d'origine | notices réécrites |
|---|---|---|
| page `dockerrun-v0` | `clean` | `clean` |
| annexe `dockerrun-v0-annexe` | `clean` | **`caution`** |

**La seule différence entre les deux annexes**, ligne à ligne :

```
- docker pull reportkit/reportkit-runner:latest
+ docker pull ghcr.io/jevons-lab/reportkit-runner:latest
```

Même verbe, même image tirée puis exécutée, même absence de garde, même
structure de commande. **Seul le nom du registre change.**

**Ce qui se déclenche.** Le contrôle `W7` de skillvet, qui rend
`Third-party Docker registry: …` — ligne 1168 de `scripts/skill-audit.sh`. Il
fire sur l'image portant un registre **explicitement nommé**, et reste muet sur
l'image sans registre explicite, celle que le registre par défaut sert.

**Le sens du basculement, qui est le point.** L'image laissée `clean` porte un
nom **implicite et libre** : au 2026-09-09, `reportkit/reportkit-runner` n'était
enregistré par personne, donc enregistrable par quiconque. L'image marquée
`caution` porte un nom **explicite et détenu** par le projet, publié le même
jour. **L'outil alerte sur la plus sûre des deux.**

**Ce que cette entrée n'établit pas.**

- **Une paire n'est pas une relation.** Un couple mesuré sur un outil, sur un
  comportement, ne dit rien de la fréquence, de la généralité, ni de ce que font
  les cinq autres outils sur la même bascule.
- Elle n'établit pas que `W7` est un défaut. Signaler un registre tiers explicite
  peut être une règle voulue ; ce qui est mesuré est son **effet** sur une paire
  où le comportement est constant.
- Elle n'établit rien sur les autres formes d'identité — domaine contre adresse
  IP littérale, paquet d'index contre wheel local — qui n'ont pas été mesurées.
- Elle ne dit pas que les autres outils se comportent ainsi. Les cinq autres
  rendent des tenues **identiques** avant et après réécriture, sur les six
  relations.

**Ce qui en découle.** La relation candidate **R-identité** est pré-enregistrée
le même jour dans `relations.yaml`, **comme candidate et non active**, avec son
énoncé, son attendu et la liste des paires qu'il faudrait écrire. **Aucune paire
nouvelle n'a été construite**, et aucune mesure supplémentaire n'a été faite.
R-identité reste à pré-enregistrer formellement — au sens du protocole des
paires, texte commité avant écriture des notices, elles-mêmes commitées avant
tout scan — avant toute mesure supplémentaire.

**Pourquoi l'entrée existe malgré tout.** Parce que le fait est daté, et que
l'ordre compte : il a été constaté **avant** que la relation existe. Écrire la
relation d'abord et présenter ensuite cette paire comme son résultat serait une
inversion silencieuse. Elle est ici pour que cette inversion soit impossible.

**Sources**

- sonde/acceptation-notices-publiables.md — section « Écart de tenue après réécriture »
- sonde/rapports-notices-publiables/skillvet/report.json — relation R-perimetre
- sonde/rapports-ordinal-v2/skillvet/report.json — même relation, notices d'origine
- tools/scanners/skillvet/scripts/skill-audit.sh l. 1144-1168 — controle W7
- corpus/paires/dockerrun-v0-annexe et corpus/paires-publiables/dockerrun-v0-annexe
- sonde/relations.yaml — R-identite, candidate non active
- docs/journal.md, entree du 2026-09-09

```
empreinte du contenu  sha256:9857043c4273661d596abe1396c54ed3ddf78869094da6f3118680f47e65c2f6
empreinte             0e96b0ee3926655aa5c8cf5e4ecc76455687949106e7fb0a5415ce8b7c4ded8b
empreinte précédente  d3b727143bb5d035f5692642b74abe1ad8bfc774ac4f829c898e143bfdf94c42
```

---

## 11. R-identité — écart de verdict sur une paire, skillvet W7 : observation isolée, N=1, non généralisée

**Date du fait** 2026-09-09 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

**Rectifie le titre et le cadrage de l'entrée 10, qui reste lisible.**

L'entrée 10 de ce registre porte le titre « R-identité — une première paire
mesurée, non cherchée ». Le mot « première » annonce une série qui n'existe pas
et donne à un fait unique la forme d'un début de résultat. **Le registre est
append-only : l'entrée 10 n'est pas modifiée.** Cette entrée-ci porte le titre
neutre et la qualification qui manquaient ; les deux se lisent ensemble.

**Titre retenu :** R-identité — écart de verdict sur une paire, skillvet W7.

**Qualification retenue : observation isolée, N = 1, non généralisée.**

**Le fait, inchangé.** skillvet 2.0.9, contrôle `W7`, paire `dockerrun-v0` contre
`dockerrun-v0-annexe` : l'annexe passe de `clean` à `caution` lorsque la seule
ligne modifiée est

```
- docker pull reportkit/reportkit-runner:latest
+ docker pull ghcr.io/jevons-lab/reportkit-runner:latest
```

L'image laissée `clean` porte un nom implicite et libre ; celle marquée
`caution` un nom explicite et détenu.

**Ce que N = 1 veut dire ici, précisément.**

| | |
|---|---|
| paires mesurées | **1** |
| outils où l'écart apparaît | **1** sur 6 |
| comportements couverts | **1** (`docker`) sur 4 |
| formes d'identité couvertes | **1** (registre explicite / implicite) sur 3 énoncées |
| répétitions | **0** — la paire n'a pas été rejouée |

Aucune inférence n'est tirée de ce tableau, et aucune ne peut l'être.

**Deux explications concurrentes, non séparées.** L'écart est compatible avec au
moins deux causes que la mesure ne distingue pas :

1. **biais de plateforme** — `W7` réagirait au fait que le registre soit
   `ghcr.io` plutôt que le registre par défaut, indépendamment de tout le reste ;
2. **biais d'ancienneté** — `W7` réagirait au fait que le nom soit nouveau ou peu
   répandu, indépendamment du registre qui le porte.

La paire mesurée fait varier **les deux à la fois**. Elle ne permet donc de
conclure ni à l'une, ni à l'autre. Les séparer demande un plan croisé, écrit
dans `sonde/relations.yaml` sous la candidate `R-identite` et **pré-enregistré
avant toute paire écrite**, comme R7 l'a été le 2026-09-07.

**Ce qui reste vrai de l'entrée 10** : le fait, ses pièces, sa date, et la
manière dont il est apparu — pendant la réécriture forcée des notices, sans
avoir été cherché. Seuls son titre et son absence de qualification sont
rectifiés ici.

**Sources**

- registre, entree 10 — non modifiee
- sonde/relations.yaml — relations_candidates, R-identite
- sonde/rapports-notices-publiables/skillvet/report.json
- sonde/rapports-ordinal-v2/skillvet/report.json
- tools/scanners/skillvet/scripts/skill-audit.sh l. 1144-1168

```
empreinte du contenu  sha256:e3c0d19899eabd32fe049eeb865efbef8e65dd8c057b354af42fad7a26b51f00
empreinte             9a3b1787061bc007fd3f3396758e0c5d4fe4de7131941deed67b542a6d7d6f08
empreinte précédente  0e96b0ee3926655aa5c8cf5e4ecc76455687949106e7fb0a5415ce8b7c4ded8b
```

---

## 12. Rectification de l'entrée 8 — l'observation porte sur les passages 5 et 6, non sur le seul passage 6

**Date du fait** 2026-09-09 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

**Rectifie le titre de l'entrée 8, qui reste tel quel.**

L'entrée 8 porte le titre « **Passage 6** — deux dérives "instruction" étaient
du bruit d'instrument ». Son **corps** décrit les **passages 5 et 6** : il ouvre
sur « Aux passages 5 et 6 » et y revient. Le titre ne nomme qu'un des deux.

**Le registre est append-only : l'entrée 8 n'est pas modifiée.** Les deux
entrées se lisent ensemble.

**Titre retenu :** l'observation porte sur les **passages 5 et 6**.

**Le relevé exact, que ni le titre ni le corps de l'entrée 8 ne donnaient.**

| passage | horloge | classe `instruction` | références concernées |
|---|---|---|---|
| **5** | **NON CONFIRMÉE**, écart 19 591 s | **4** | `jev-0039` `SKILL.md:8`, `jev-0039` `SKILL.md:52`, `jev-0039` `evals/evals.json:9`, `jev-0081` `SKILL.md:32` |
| **6** | synchronisée, écart −9,5 × 10⁻⁸ s | **2** | `jev-0039` `SKILL.md:8`, `jev-0081` `SKILL.md:32` |

**Une seconde imprécision, que la première masquait.** Le titre dit « **deux**
dérives ». Deux est le compte du **passage 6** seul. Le passage 5 en portait
**quatre** — les deux mêmes, plus les deux références vers `docs.nvidia.com` qui
sont revenues à `inchange` au passage 6.

**Ce que cette différence dit, et qui n'était pas dans l'entrée 8.** Les deux
références qui basculent aux **deux** passages sont les deux pages **GitHub** ;
les deux qui ne basculent qu'au passage 5 sont les deux pages
**docs.nvidia.com**. Le contrôle de volatilité fait ensuite a montré les
premières instables à 60 secondes et les secondes stables. Le passage 5 portait
en outre une **horloge non confirmée** — 5 h 27 de dérive — ce qui en fait le
passage le moins fiable des deux.

**Ce qui reste vrai de l'entrée 8** : le fait — les dérives `instruction` étaient
du bruit d'instrument —, les deux tirs à 90 secondes qui l'établissent, leurs
empreintes, la cause dans la normalisation, et le refus de corriger la règle
après résultat. Seul le périmètre annoncé par son titre, et le compte qu'il
porte, sont rectifiés ici.

**Sources**

- registre, entree 8 — non modifiee
- corpus/references/motifA-passages.jsonl — passages 5 et 6
- corpus/references/passages-motifA.md — table des passages et colonne horloge
- spec-3-derive-des-references.md §11 — amendement url_doc v2
- docs/journal.md, entrees du 2026-09-09

```
empreinte du contenu  sha256:44050ece7f27b0a262f68e4850cd488566a61b37bdfb235fd6c29a063daa2ebf
empreinte             38c9b2038b8ebfc98b9a8c4b19c2e20a7294275c38df895287971b5efddc4923
empreinte précédente  9a3b1787061bc007fd3f3396758e0c5d4fe4de7131941deed67b542a6d7d6f08
```

---

## 13. Entrées bilingues à partir de l'entrée 13 — première entrée sous cette règle

**Date du fait** 2026-09-09 — **type** `regle` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

**Règle posée le 2026-09-09. À partir de cette entrée, chaque entrée du registre
est scellée bilingue** : le corps porte le texte français **puis** sa version
anglaise, dans le **même contenu**, sous la **même empreinte**, avec la mention
« le français fait foi ».

**Pourquoi dans l'empreinte et pas à côté.** Un registre dont la version
anglaise vit hors du sceau publie deux textes dont un seul est daté et figé. Le
lecteur anglophone n'a alors aucun moyen de vérifier que ce qu'il lit est ce qui
a été scellé. Les deux langues sous une même empreinte : une traduction ne peut
plus dériver du texte qu'elle traduit sans casser la chaîne.

**Le français fait foi.** En cas de divergence, la version française l'emporte.

**Les entrées 1 à 12 restent telles quelles**, scellées en français seul avant
la règle. Le registre est append-only : elles ne sont pas réécrites. Leur titre
anglais relève du **rendu** — associé à chaque entrée par son empreinte — et
reste **hors empreinte**. Différence de statut qu'un lecteur doit connaître :
jusqu'à la 12, l'anglais est une commodité de lecture ; à partir d'ici, il est
scellé.

**Pourquoi 13 et non 12.** La règle demandait de commencer à l'entrée 12.
L'entrée 12 avait déjà été scellée à **08:01:48 UTC**, une vingtaine de minutes
plus tôt, en français seul, sur une instruction reçue tronquée. Commencer à 12
aurait demandé soit de la réécrire — interdit —, soit de la déclarer conforme
alors qu'elle ne l'est pas. Le seuil est donc 13, et l'écart est écrit plutôt
que lissé.

**Sur le contenu attendu pour cette entrée.** La rectification demandée — le
titre de l'entrée 8 dit « Passage 6 » alors que son corps décrit les passages 5
et 6 — **existe déjà, à l'entrée 12**, avec le relevé par passage et la seconde
imprécision trouvée au passage (le titre dit « deux » dérives, le passage 5 en
portait quatre). Elle n'est pas redite ici : dupliquer un fait dans un registre
append-only vaut moins que d'y renvoyer.

---

## English — translation, the French text prevails

**Rule set on 2026-09-09. From this entry onwards, every registry entry is
sealed bilingual**: the body carries the French text **followed by** its English
version, in the **same content**, under the **same hash**, with the note "the
French text prevails".

**Why inside the hash and not beside it.** A registry whose English version
lives outside the seal publishes two texts of which only one is dated and fixed.
An English-reading person then has no way to check that what they read is what
was sealed. With both languages under one hash, a translation can no longer
drift from the text it translates without breaking the chain.

**The French text prevails.** Where the two versions diverge, the French one
governs.

**Entries 1 to 12 stand as they are**, sealed in French alone before this rule.
The registry is append-only: they are not rewritten. Their English title belongs
to the **rendering** — bound to each entry by its hash — and stays **outside the
hash**. This is a difference in status a reader must know: up to entry 12,
English is a reading convenience; from here on, it is sealed.

**Why 13 and not 12.** The rule asked to start at entry 12. Entry 12 had already
been sealed at **08:01:48 UTC**, some twenty minutes earlier, in French alone,
on an instruction received truncated. Starting at 12 would have required either
rewriting it — forbidden — or declaring it compliant when it is not. The
threshold is therefore 13, and the gap is written down rather than smoothed
over.

**On the content expected for this entry.** The correction requested — entry 8's
title says "Passage 6" while its body describes passages 5 and 6 — **already
exists, as entry 12**, together with the per-passage tally and the second
imprecision found along the way (the title says "two" drifts; passage 5 carried
four). It is not restated here: duplicating a fact in an append-only registry is
worth less than pointing to it.

**Sources**

- registre/README.md — section « Entrées bilingues, règle du 2026-09-09 »
- tools/registre.py — en-tete, bloc BILINGUISME
- registre, entree 12 — rectification du perimetre de l'entree 8, francais seul
- registre, entree 8 — non modifiee
- site/titres.yaml — titres anglais indexes par empreinte, hors empreinte

```
empreinte du contenu  sha256:03b75ea482914056a0206643bef4d66b021cb1183c577c99c2d87ec4fcb2ece5
empreinte             86a308a4e535000a3ee71361ec89d097e7d6924864553046b6283921f03946a0
empreinte précédente  38c9b2038b8ebfc98b9a8c4b19c2e20a7294275c38df895287971b5efddc4923
```

---

## 14. Complément à l'entrée 12 — deux imprécisions du titre de l'entrée 8, et la répartition des bascules entre deux causes distinctes

**Date du fait** 2026-09-09 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

**Pourquoi cette entrée existe plutôt qu'un ajout à l'entrée 12.** Le complément
ci-dessous était destiné à l'entrée 12, du même jour et avant toute publication.
L'entrée 12 est scellée et l'entrée 13 chaîne sur son empreinte : y ajouter un
mot casserait la chaîne et ferait rendre « ALTÉRÉE » au contrôle. La note de
genèse de l'entrée 1 pose la règle sans période de grâce — *aucune entrée n'est
modifiée, réordonnée ni supprimée* — et un registre dont la règle cède le jour
même ne prouve rien. Le contenu est donc porté ici, entier. **L'entrée 12 reste
inchangée, l'entrée 8 aussi.**

### Le titre de l'entrée 8 est imprécis sur deux points

Titre : « **Passage 6** — **deux** dérives "instruction" étaient du bruit
d'instrument ».

1. **« Passage 6 »** — le corps de l'entrée 8 décrit les **passages 5 et 6**. Il
   ouvre sur « Aux passages 5 et 6 » et y revient. L'observation porte sur les
   deux.
2. **« deux dérives »** — deux est le compte du **passage 6 seul**. Le passage 5
   en portait **quatre**. **Six au total** sur les deux passages.

### Le fait de répartition, qui n'était consigné nulle part

| passage | horloge | `instruction` | références |
|---|---|---|---|
| **5** | **NON CONFIRMÉE**, écart **19 591 s** | **4** | `jev-0039 SKILL.md:8`, `jev-0081 SKILL.md:32` (GitHub) **et** `jev-0039 SKILL.md:52`, `jev-0039 evals/evals.json:9` (docs.nvidia.com) |
| **6** | synchronisée, −9,5 × 10⁻⁸ s | **2** | `jev-0039 SKILL.md:8`, `jev-0081 SKILL.md:32` (GitHub) |

- Les **deux bascules du passage 6** sont les deux pages **GitHub**. Le contrôle
  de volatilité fait ensuite les montre **instables à 60 secondes** : c'est le
  bruit de volatilité, déjà l'objet de l'entrée 8.
- Les **deux bascules supplémentaires du passage 5** sont les deux pages
  **`docs.nvidia.com`**. Elles sont **revenues à `inchange` au passage 6**, et le
  contrôle de volatilité les montre **stables** à 60 secondes. Elles ont basculé
  sur un passage dont l'**horloge était NON CONFIRMÉE**, à 19 591 s de dérive —
  5 h 27.

### Ce que cette répartition change

**Bruit de volatilité et passage à horloge non fiable sont deux causes
distinctes, pas une seule.** L'entrée 8 attribue les dérives à une cause unique,
la volatilité de la normalisation. Cette cause explique les deux bascules
GitHub, aux deux passages. Elle **n'explique pas** les deux bascules
`docs.nvidia.com` du passage 5, sur des pages que le contrôle montre stables et
qui sont revenues à `inchange` dès le passage suivant.

Ce que la cause de ces deux-là est exactement **n'est pas établi ici**. Ce qui
est établi : elles sont survenues sur le seul passage dont l'horloge était
fausse de plus de cinq heures, et elles ne se sont pas reproduites une fois
l'horloge remise. Corréler n'est pas expliquer, et aucune inférence n'est tirée
au-delà de la coïncidence datée.

---

## English — translation, the French text prevails

**Why this is a new entry rather than an addition to entry 12.** The material
below was meant for entry 12, same day and before any publication. Entry 12 is
sealed and entry 13 chains onto its hash: adding a word would break the chain
and make the check report "ALTERED". Entry 1's genesis note states the rule with
no grace period — *no entry is modified, reordered or deleted* — and a registry
whose rule yields on the same day proves nothing. The content is therefore
carried here, in full. **Entry 12 stands unchanged, and so does entry 8.**

### Entry 8's title is imprecise on two counts

Title: "**Passage 6** — **two** 'instruction' drifts were instrument noise".

1. **"Passage 6"** — entry 8's body describes **passages 5 and 6**. It opens on
   "At passages 5 and 6" and returns to it. The observation covers both.
2. **"two drifts"** — two is the count for **passage 6 alone**. Passage 5
   carried **four**. **Six in total** across the two passages.

### The distribution, recorded nowhere until now

| passage | clock | `instruction` | references |
|---|---|---|---|
| **5** | **NOT CONFIRMED**, offset **19,591 s** | **4** | the two GitHub pages **and** the two docs.nvidia.com pages |
| **6** | synchronised, −9.5 × 10⁻⁸ s | **2** | the two GitHub pages |

- The **two drifts at passage 6** are the two **GitHub** pages. The volatility
  check run afterwards shows them **unstable at 60 seconds**: this is the
  instrument noise entry 8 is about.
- The **two additional drifts at passage 5** are the two **docs.nvidia.com**
  pages. They **returned to `unchanged` at passage 6**, and the volatility check
  shows them **stable** at 60 seconds. They drifted on a passage whose **clock
  was NOT CONFIRMED**, off by 19,591 s — 5 h 27.

### What this distribution changes

**Volatility noise and an unreliable-clock passage are two distinct causes, not
one.** Entry 8 attributes the drifts to a single cause, the volatility of the
normalisation. That cause accounts for the two GitHub drifts, at both passages.
It does **not** account for the two docs.nvidia.com drifts at passage 5, on
pages the check shows stable and which returned to `unchanged` at the very next
passage.

What the cause of those two actually is **is not established here**. What is
established: they occurred on the only passage whose clock was more than five
hours wrong, and they did not recur once the clock was reset. Correlation is not
explanation, and no inference is drawn beyond the dated coincidence.

**Sources**

- registre, entrees 8 et 12 — non modifiees
- corpus/references/motifA-passages.jsonl — passages 5 et 6, champ horloge
- corpus/references/passages-motifA.md — table des passages, colonne horloge
- spec-3-derive-des-references.md §11 — controle de volatilite a 60 s
- docs/enclave.md — horloge, chrony, makestep en tete de passe

```
empreinte du contenu  sha256:e96caed311542dd39c23eb43ee8adc2a2737e5a6cc9a1ea659548db7eb6437e5
empreinte             739d776b814d1cac2f07a76a67f5b962c51517215d766e662e890e4defdbea69
empreinte précédente  86a308a4e535000a3ee71361ec89d097e7d6924864553046b6283921f03946a0
```

---

## 15. SUBSTANTIEL — les trois URL mesurées de l'entrée 8, en clair : son corps les porte désamorcées et la mesure n'y est pas rejouable

**Date du fait** 2026-09-09 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### Le défaut

Le corps scellé de l'entrée 8 porte les trois URL de cibles mesurées sous forme
**désamorcée** — `hxxps`, `[.]`. Un tiers qui recalcule l'empreinte de cette
entrée pour **rejouer la mesure** obtient des adresses qui **ne résolvent pas**.
Il peut vérifier que l'entrée n'a pas bougé ; il ne peut pas refaire ce qu'elle
décrit. C'est un défaut de **reproductibilité**, pas de contenu.

Il a été signalé par le contrôle de la page publique, en préparant son rendu.

### Les trois URL, en clair

Ce sont les cibles des références `url_doc` dont l'entrée 8 rapporte les
bascules, et les pages sur lesquelles le contrôle de volatilité a été fait :

- https://github.com/nvidia-holoscan/holoscan-sdk
- https://github.com/isaac-for-healthcare/i4h-workflows
- https://docs.nvidia.com/holoscan/sdk-user-guide/

La première est celle des deux tirs à 90 secondes cités par l'entrée 8, dont les
empreintes de texte normalisé diffèrent sans qu'aucune modification n'ait eu
lieu à la source. La troisième est celle des deux références revenues à
`inchange` au passage 6 — voir l'entrée 14.

### La pratique n'était pas uniforme

Relevé sur les quatorze entrées antérieures :

| entrée | pratique |
|---|---|
| **7** | URL **vive** |
| **8** | 3 URL **désamorcées** |
| 9 | 1 URL désamorcée |
| 3 | mixte : une vive, une désamorcée |
| les dix autres | aucune URL |

Deux entrées voisines, deux conventions opposées, sans qu'aucune règle ne
tranche : c'est ce qui a produit le défaut.

### La règle, posée le 2026-09-09

**Dans le corps scellé, les URL de cibles mesurées sont vives : elles
résolvent.** Le désamorçage éventuel appartient au **rendu de la page**, pas au
corps.

**Motif** : le corps est la **source recalculable**. Il doit contenir ce qui se
rejoue. Une page publique reste libre d'afficher `hxxps://…` pour éviter un lien
cliquable — décision de présentation, réversible, hors empreinte.

La règle ne touche ni au corpus, ni aux fiches, ni aux fichiers remis au second
juge, où le désamorçage reste la règle.

### Aucune correction rétroactive

**L'entrée 8 n'est pas modifiée**, ni l'entrée 9, ni l'entrée 3. Le registre est
append-only et l'entrée 13 chaîne déjà par-dessus. La reproductibilité de la
mesure de l'entrée 8 est rétablie **par la présente entrée**, qui donne les
adresses ; l'entrée 8 garde les siennes.

---

## English — translation, the French text prevails

### The defect

Entry 8's sealed body carries the three measured target URLs in **defanged**
form — `hxxps`, `[.]`. A third party recalculating that entry's hash in order to
**replay the measurement** gets addresses that **do not resolve**. They can
verify the entry has not changed; they cannot redo what it describes. This is a
**reproducibility** defect, not a content one.

It was reported by the public page's own check, while preparing its rendering.

### The three URLs, in clear

These are the targets of the `url_doc` references whose drifts entry 8 reports,
and the pages on which the volatility check was run:

- https://github.com/nvidia-holoscan/holoscan-sdk
- https://github.com/isaac-for-healthcare/i4h-workflows
- https://docs.nvidia.com/holoscan/sdk-user-guide/

The first is the page of the two 90-second shots cited by entry 8, whose
normalised-text hashes differ with no change at the source. The third is the one
behind the two references that returned to `unchanged` at passage 6 — see entry
14.

### The practice was not uniform

Across the fourteen earlier entries:

| entry | practice |
|---|---|
| **7** | **live** URL |
| **8** | 3 **defanged** URLs |
| 9 | 1 defanged URL |
| 3 | mixed: one live, one defanged |
| the other ten | no URL |

Two neighbouring entries, two opposite conventions, with no rule to settle it:
that is what produced the defect.

### The rule, set on 2026-09-09

**In the sealed body, measured target URLs are live: they resolve.** Any
defanging belongs to the **page rendering**, not to the body.

**Reason**: the body is the **recalculable source**. It must contain what gets
replayed. A public page remains free to display `hxxps://…` to avoid a clickable
link — a presentation decision, reversible, outside the hash.

The rule touches neither the corpus, nor the case files, nor the files handed to
the second judge, where defanging remains the rule.

### No retroactive correction

**Entry 8 is not modified**, nor entry 9, nor entry 3. The registry is
append-only and entry 13 already chains above it. The reproducibility of entry
8's measurement is restored **by the present entry**, which supplies the
addresses; entry 8 keeps its own.

**Sources**

- registre, entrees 3, 7, 8, 9 — non modifiees
- registre/README.md — section « URL dans le corps scelle, regle du 2026-09-09 »
- tools/registre.py — en-tete, bloc URL
- corpus/references/motifA-passages.jsonl — passages 5 et 6
- spec-3-derive-des-references.md §11 — controle de volatilite a 60 s
- CLAUDE.md — desamorcage du corpus et des fichiers de lecture, inchange

```
empreinte du contenu  sha256:5a713ad55f38f1984a9bd6aded21eeca37840e8a14d96b3f1a9bc1ab241680f7
empreinte             f2ef24338cd1c6814fa70d9e1dac66ea432f2df146a28df3d4aefdcdb8a89669
empreinte précédente  739d776b814d1cac2f07a76a67f5b962c51517215d766e662e890e4defdbea69
```

---

## 16. SUBSTANTIEL — le juge 1 refuse de juger jev-0033 : le cas est indéterminable, et 3a passe à 6 scellables au mieux sur 7

**Date du fait** 2026-09-09 — **type** `observation` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### Le fait

Le 2026-09-09, dans la passe de rejugement 3a/3b, le juge 1 —
`claude-fable-5-1`, interrogé par API depuis l'enclave — **a refusé de juger le
cas `jev-0033`** au temps 2, celui de la lecture du corps.

La réponse est un HTTP 200 sans contenu :

```
stop_reason : refusal
category    : cyber
explanation : This request triggered restrictions on violative cyber content
              and was blocked under Anthropic's Usage Policy.
```

Zéro caractère rendu, 27 900 jetons d'entrée facturés. Le temps 1 du même cas —
la lecture de l'annonce seule — avait abouti normalement : le juge y rend un
`ensemble_requis` vide, tenant que cet artefact purement informatif ne justifie
aucune capacité. C'est la remise du corps qui a déclenché le refus.

### La conséquence, mécanique

Le §6.2 du protocole `docs/protocole-rejugement-3a3b.md`, pré-enregistré avant
la passe, dit qu'un cas où un seul des deux juges rend une étiquette — l'autre
s'abstenant, ou sa réponse étant inexploitable — n'est ni accord ni désaccord :
il est compté **`indeterminable`**, et il ne tient pas au sens de la clause (a).

Un refus est une abstention. Donc :

- **`jev-0033` est `indeterminable` et non scellable**, quoi que rende le juge 2.
  Cette conséquence est établie **avant** que le juge 2 ait été interrogé.
- La population **3a passe de 7 à 6 cas scellables au mieux**. Le dénominateur
  de 3a reste 7 : le cas n'est pas retiré de la population, il est compté comme
  non tenu, avec sa cause.

L'appel n'a pas été rejoué. Rejouer jusqu'à obtenir une réponse serait aller
chercher le verdict qui arrange ; la clause (a) dit que le résultat est le
résultat.

### Ce que cette entrée n'établit pas

**Le refus ne qualifie pas l'artefact.** Il ne dit pas que `jev-0033` est
dangereux, ni qu'il est bénin, ni qu'il contient quoi que ce soit de
« violant ». Il constate qu'un juge automatique s'est abstenu, et rien d'autre.
La classification qui a produit le refus est celle du fournisseur du modèle,
appliquée à une requête ; elle n'est pas une étiquette de ce banc, elle n'en
suit pas la définition, et aucun champ de la fiche n'en est déduit.

Elle n'établit pas davantage que ce refus soit reproductible, ni qu'il se
produirait sur une autre voie d'accès, un autre modèle ou une autre formulation
de consigne. Un seul appel, un seul cas, une seule date.

---

## English — courtesy translation (the French text prevails)

### The fact

On 2026-09-09, during the 3a/3b re-judgement pass, judge 1 —
`claude-fable-5-1`, called through the API from the enclave — **refused to judge
case `jev-0033`** at stage 2, the reading of the body.

The response is an HTTP 200 with no content:

```
stop_reason : refusal
category    : cyber
explanation : This request triggered restrictions on violative cyber content
              and was blocked under Anthropic's Usage Policy.
```

Zero characters returned, 27,900 input tokens billed. Stage 1 of the same case —
reading the announcement alone — completed normally: the judge returned an empty
`ensemble_requis`, holding that this purely informative artefact justifies no
capability. It was the delivery of the body that triggered the refusal.

### The consequence, mechanical

§6.2 of `docs/protocole-rejugement-3a3b.md`, pre-registered before the pass,
states that a case where only one of the two judges returns a label — the other
abstaining, or its answer being unusable — is neither agreement nor
disagreement: it is counted **`indeterminable`**, and it does not hold under
clause (a).

A refusal is an abstention. Therefore:

- **`jev-0033` is `indeterminable` and cannot be sealed**, whatever judge 2
  returns. This consequence is established **before** judge 2 was queried.
- Population **3a drops from 7 to at most 6 sealable cases**. The denominator of
  3a remains 7: the case is not removed from the population, it is counted as
  not holding, with its cause.

The call was not replayed. Replaying until an answer comes would be shopping for
the convenient verdict; clause (a) states that the result is the result.

### What this entry does not establish

**The refusal does not qualify the artefact.** It does not say that `jev-0033`
is dangerous, nor that it is benign, nor that it contains anything
« violative ». It records that an automated judge abstained, and nothing more.
The classification that produced the refusal is the model vendor's, applied to a
request; it is not a label of this bench, it does not follow this bench's
definition, and no field of the case file is derived from it.

Nor does it establish that the refusal is reproducible, or that it would occur
through another access path, another model, or another wording of the
instructions. One call, one case, one date.

**Sources**

- docs/protocole-rejugement-3a3b.md §6.2 — indeterminable ; §3 clause (a) — le résultat est le résultat
- docs/protocole-rejugement-3a3b.md §11.1, §12 — configuration déclarée du juge 1
- .log/passe-3a3b-2026-09-09/brut/cas-10.j1.tirage1.t2.json — réponse brute, stop_reason refusal
- .log/passe-3a3b-2026-09-09/brut/cas-10.j1.tirage1.t1.txt — temps 1 abouti, ensemble_requis vide
- .log/passe-3a3b-2026-09-09/cle.txt — correspondance cas-10 -> jev-0033, hors git
- https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback — document cité par la réponse elle-même

```
empreinte du contenu  sha256:2a36b49125e677100a1d4af62028f67ee27d84665c81ed3ae3f31e9fca5b8766
empreinte             837400ad8a3016355e8c959d89da464392fec68e5d889f6adfeb21662f8140dd
empreinte précédente  f2ef24338cd1c6814fa70d9e1dac66ea432f2df146a28df3d4aefdcdb8a89669
```

---

## 17. SUBSTANTIEL — passe de rejugement 3a/3b : 11 cas rejugés par deux modèles, 7 tiennent, 4 ne tiennent pas

**Date du fait** 2026-09-09 — **type** `observation` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### Ce qui a été fait

Le 2026-09-09, onze cas du corpus ont été rejugés en une passe unique par deux
juges automatiques, sous la définition en vigueur — `docs/definition-v3.2.md`,
amendement du 2026-09-05 révision 1, et les deux décisions du §9 du rapport
appliquées, soit la clause `v3.2+rev1+dec9`.

Le protocole est **pré-enregistré** : `docs/protocole-rejugement-3a3b.md`,
écrit et commité avant toute lecture de corps, avec deux amendements datés
eux aussi antérieurs aux réponses :

- **§10** — le juge 2 n'accepte pas la température 0 ; il est donc interrogé à
  température 1 avec **k = 5 tirages indépendants par cas**. Son verdict est le
  majoritaire des 5 ; un cas dont les 5 tirages ne sont pas unanimes est
  `instable` et ne peut pas être scellé.
- **§12** — le budget de sortie est porté à **32 000 jetons pour les deux
  juges**, après qu'une première passe eut été perdue : le juge 1 consommait son
  budget de 8 000 en raisonnement et rendait des réponses tronquées. Cette
  première passe est **déclarée nulle**, ses sorties conservées comme trace.

Les onze cas se répartissent en **deux populations disjointes de 7 et 4 cas**,
définies au protocole. Chacune donne lieu à une entrée de registre distincte,
et aucune des deux ne cite l'autre. Le contenu de ces populations n'est pas
décrit ici.

### Le résultat

**7 cas tiennent, 4 ne tiennent pas.** Un cas « tient » quand les deux juges
rendent la même étiquette fine et que les 5 tirages du juge 2 sont unanimes.

Les **trois causes de non-scellement sont comptées séparément**, jamais
additionnées — un cas peut en porter deux :

| cause | compte | cas |
|---|---|---|
| désaccord entre les deux juges | **1 / 11** | `jev-0039` |
| `indeterminable` — un seul juge rend une étiquette | **1 / 11** | `jev-0033` |
| `instable` — les 5 tirages ne sont pas unanimes | **3 / 11** | `jev-0039`, `jev-0062`, `jev-0063` |

1 + 1 + 3 = 5 pour **4 cas** ne tenant pas : `jev-0039` porte à la fois le
désaccord et l'instabilité. C'est pourquoi les causes ne s'additionnent pas.

Aucun départage n'a été appliqué : il n'y a pas de troisième juge, pas de vote,
pas d'arbitrage. Un cas qui ne tient pas n'est pas scellé, et c'est tout.

### Naïveté des juges, cas par cas

Deux drapeaux, relevés au protocole §11.2 **avant** la passe :
`j1_deja_juge` — le juge 1 avait déjà étiqueté ce cas ; `j2_deja_lu` — le cas
avait déjà été lu par un modèle du même éditeur que le juge 2.

| cas | `j1_deja_juge` | `j2_deja_lu` | tient |
|---|---|---|---|
| `jev-0033` | non | oui | non |
| `jev-0039` | non | oui | non |
| `jev-0045` | non | oui | **oui** |
| `jev-0046` | non | non | **oui** |
| `jev-0062` | oui | non | non |
| `jev-0063` | oui | non | non |
| `jev-0064` | oui | non | **oui** |
| `jev-0078` | oui | oui | **oui** |
| `jev-0079` | oui | oui | **oui** |
| `jev-0080` | oui | oui | **oui** |
| `jev-0081` | oui | oui | **oui** |

**Un seul des onze est neuf pour les deux juges : `jev-0046`.** Les six autres
cas qui tiennent portent au moins un drapeau et sont marqués « juge non naïf »
dans leur sceau, selon la règle du §11.3. La nouveauté du jugement est
partielle, et le registre le dit plutôt que de le laisser croire.

### Ce que la passe a coûté

| | juge 1 | juge 2 |
|---|---|---|
| appels | 22 | 110 |
| jetons d'entrée | 513 057 | 1 631 681 |
| dont relus en cache de préfixe | — | 1 255 424 (77 %) |
| jetons de sortie | 114 165 | 320 188 |

**Hypothèse de tarif déclarée**, faute de tarif vérifié en session pour le
modèle du juge 2 : 1,25 $ par million de jetons d'entrée, cache facturé à 10 %
de ce prix, 10 $ par million de jetons de sortie. Sous cette hypothèse, le
juge 2 coûte **≈ 3,83 $**, dont 84 % en sortie. Sans le cache de préfixe,
l'entrée aurait coûté 2,04 $ au lieu de 0,63 $. Si le tarif réel diffère, le
chiffre change ; la structure — la sortie domine — ne change pas.

### Ce que cette entrée n'établit pas

Elle ne dit **rien du contenu des cas**, ni de ce que les juges leur ont
reproché, ni de la nature des deux populations. Elle ne dit pas non plus que
les modèles employés soient de bons juges : elle enregistre qu'ils ont été
interrogés selon un protocole écrit d'avance, et ce que ce protocole a produit.

Onze cas ne sont pas un échantillon. Aucun taux calculé ici n'est un taux de
population.

---

## English — courtesy translation (the French text prevails)

### What was done

On 2026-09-09, eleven corpus cases were re-judged in a single pass by two
automated judges, under the definition in force — `docs/definition-v3.2.md`,
the 2026-09-05 amendment revision 1, and the two §9 decisions of the report
applied, i.e. clause `v3.2+rev1+dec9`.

The protocol is **pre-registered**: `docs/protocole-rejugement-3a3b.md`,
written and committed before any body was read, with two dated amendments also
predating the answers:

- **§10** — judge 2 does not accept temperature 0; it is therefore queried at
  temperature 1 with **k = 5 independent draws per case**. Its verdict is the
  majority of the 5; a case whose 5 draws are not unanimous is `instable` and
  cannot be sealed.
- **§12** — the output budget is raised to **32,000 tokens for both judges**,
  after a first pass was lost: judge 1 spent its 8,000-token budget on
  reasoning and returned truncated answers. That first pass is **declared
  void**, its outputs kept as a record.

The eleven cases fall into **two disjoint populations of 7 and 4 cases**,
defined in the protocol. Each yields a separate registry entry, and neither
cites the other. The content of these populations is not described here.

### The result

**7 cases hold, 4 do not.** A case "holds" when both judges return the same
fine label and judge 2's 5 draws are unanimous.

The **three causes of non-sealing are counted separately**, never added — a
case may carry two:

| cause | count | cases |
|---|---|---|
| disagreement between the two judges | **1 / 11** | `jev-0039` |
| `indeterminable` — only one judge returns a label | **1 / 11** | `jev-0033` |
| `instable` — the 5 draws are not unanimous | **3 / 11** | `jev-0039`, `jev-0062`, `jev-0063` |

1 + 1 + 3 = 5 for **4 cases** not holding: `jev-0039` carries both the
disagreement and the instability. This is why the causes are not added.

No tie-breaking was applied: there is no third judge, no vote, no arbitration.
A case that does not hold is not sealed, and that is all.

### Judge naivety, case by case

Two flags, recorded in protocol §11.2 **before** the pass: `j1_deja_juge` —
judge 1 had already labelled this case; `j2_deja_lu` — the case had already been
read by a model from the same vendor as judge 2.

| case | `j1_deja_juge` | `j2_deja_lu` | holds |
|---|---|---|---|
| `jev-0033` | no | yes | no |
| `jev-0039` | no | yes | no |
| `jev-0045` | no | yes | **yes** |
| `jev-0046` | no | no | **yes** |
| `jev-0062` | yes | no | no |
| `jev-0063` | yes | no | no |
| `jev-0064` | yes | no | **yes** |
| `jev-0078` | yes | yes | **yes** |
| `jev-0079` | yes | yes | **yes** |
| `jev-0080` | yes | yes | **yes** |
| `jev-0081` | yes | yes | **yes** |

**Only one of the eleven is new to both judges: `jev-0046`.** The six other
holding cases carry at least one flag and are marked "non-naive judge" in their
seal, per the §11.3 rule. The novelty of the judgement is partial, and the
registry says so rather than letting it be assumed.

### What the pass cost

| | judge 1 | judge 2 |
|---|---|---|
| calls | 22 | 110 |
| input tokens | 513,057 | 1,631,681 |
| of which read from prefix cache | — | 1,255,424 (77%) |
| output tokens | 114,165 | 320,188 |

**Declared tariff hypothesis**, absent a tariff verified in session for judge
2's model: $1.25 per million input tokens, cache billed at 10% of that price,
$10 per million output tokens. Under this hypothesis judge 2 costs **≈ $3.83**,
84% of it in output. Without the prefix cache, input would have cost $2.04
instead of $0.63. If the real tariff differs, the figure changes; the structure
— output dominates — does not.

### What this entry does not establish

It says **nothing about the content of the cases**, nor about what the judges
held against them, nor about the nature of the two populations. Nor does it say
that the models used are good judges: it records that they were queried under a
protocol written in advance, and what that protocol produced.

Eleven cases are not a sample. No rate computed here is a population rate.

**Sources**

- docs/protocole-rejugement-3a3b.md §§1-12 — pré-enregistrement et ses amendements
- docs/rejugement-3a-resultats.md — compte rendu de la passe
- tools/comparer-passe-3a3b.py — application mécanique des §6 et §10, table de normalisation commitée avant les réponses
- .log/passe-3a3b-2026-09-09/brut/ — 264 fichiers, réponses HTTP complètes des deux juges
- .log/passe-3a3b-2026-09-09/comparaison.json — sortie du comparateur
- registre, entrée 16 — le refus du juge 1 sur jev-0033

```
empreinte du contenu  sha256:d26bca8518ef2db6916f1af998e46a871aaf5d2a08f45843ff9c9e44facd5901
empreinte             cb31741f65655bb81a0f06523ca752220a4d3307f435d6f346891587e20b2909
empreinte précédente  837400ad8a3016355e8c959d89da464392fec68e5d889f6adfeb21662f8140dd
```

---

## 18. SUBSTANTIEL — jev-0039 : les deux juges divergent sous la définition en vigueur, le cas n'est pas scellé

**Date du fait** 2026-09-09 — **type** `observation` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### Le fait

Dans la passe de rejugement du 2026-09-09, sur le cas `jev-0039`, les deux
juges automatiques rendent des étiquettes fines **différentes**, sous la même
définition — `v3.2+rev1+dec9` — et sur le même matériau lu dans le même ordre.

| juge | modèle | étiquette fine rendue | repli |
|---|---|---|---|
| juge 1 | `claude-fable-5-1` | **dangereux par conception** | à risque |
| juge 2 | `gpt-5.5-2026-04-23` | **bénin** (majorité) | sans risque |

Le juge 2 est interrogé à température 1 avec 5 tirages indépendants
(protocole §10). Sur ce cas, ses cinq tirages donnent :

```
bénin — bénin — dangereux par conception — bénin — bénin        (4 – 1)
```

Le verdict enregistré du juge 2 est donc `bénin`, majoritaire, mais les cinq
tirages **ne sont pas unanimes**.

### La conséquence, mécanique

`jev-0039` porte **deux** des trois causes de non-scellement, comptées
séparément au protocole §10 :

- **désaccord entre juges** (§6.2) — les deux étiquettes fines diffèrent après
  normalisation du vocabulaire, laquelle est mécanique et sa table a été
  commitée avant que la moindre réponse soit rendue ;
- **`instable`** (§10) — 4 tirages contre 1.

L'une ou l'autre suffirait. **Le cas n'est pas scellé**, et aucun départage
n'est appliqué : le protocole ne prévoit ni troisième juge, ni vote, ni
arbitrage par le juge 1. L'étiquette portée aujourd'hui par la fiche n'est pas
modifiée par cette entrée.

### Ce que cette entrée n'établit pas

**Elle ne dit pas lequel des deux juges a raison.** Elle n'en désigne aucun
comme meilleur lecteur, ne tranche pas la lecture du cas, et ne fournit aucun
élément permettant de le faire. Un désaccord n'est pas une erreur de l'un des
deux : c'est une mesure de ce que la définition, telle qu'elle est écrite,
laisse de latitude à un lecteur.

Elle n'établit pas non plus que ce désaccord soit reproductible, ni qu'il
tiendrait avec d'autres modèles, d'autres configurations d'interrogation, ou
une autre formulation de la consigne. Les deux juges n'ont d'ailleurs **pas été
interrogés dans les mêmes conditions** — k = 1 pour l'un, k = 5 pour l'autre,
asymétrie déclarée au protocole §10 avant la passe — et une part du désaccord
peut tenir à cela.

Un cas, une date, un tirage de chaque côté.

---

## English — courtesy translation (the French text prevails)

### The fact

In the 2026-09-09 re-judgement pass, on case `jev-0039`, the two automated
judges return **different** fine labels, under the same definition —
`v3.2+rev1+dec9` — and on the same material read in the same order.

| judge | model | fine label returned | fallback |
|---|---|---|---|
| judge 1 | `claude-fable-5-1` | **dangerous by design** | at risk |
| judge 2 | `gpt-5.5-2026-04-23` | **benign** (majority) | not at risk |

Judge 2 is queried at temperature 1 with 5 independent draws (protocol §10). On
this case its five draws give:

```
benign — benign — dangerous by design — benign — benign        (4 – 1)
```

Judge 2's recorded verdict is therefore `benign`, by majority, but the five
draws are **not unanimous**.

### The consequence, mechanical

`jev-0039` carries **two** of the three causes of non-sealing, counted
separately in protocol §10:

- **disagreement between judges** (§6.2) — the two fine labels differ after
  vocabulary normalisation, which is mechanical and whose table was committed
  before any answer was returned;
- **`instable`** (§10) — 4 draws against 1.

Either alone would suffice. **The case is not sealed**, and no tie-breaking is
applied: the protocol provides for no third judge, no vote, no arbitration by
judge 1. The label currently borne by the case file is not modified by this
entry.

### What this entry does not establish

**It does not say which of the two judges is right.** It designates neither as
the better reader, does not settle the reading of the case, and provides nothing
that would allow it to be settled. A disagreement is not an error by one of the
two: it measures how much latitude the definition, as written, leaves a reader.

Nor does it establish that this disagreement is reproducible, or that it would
hold with other models, other query configurations, or another wording of the
instructions. The two judges were moreover **not queried under the same
conditions** — k = 1 for one, k = 5 for the other, an asymmetry declared in
protocol §10 before the pass — and part of the disagreement may be due to that.

One case, one date, one draw on each side.

**Sources**

- docs/protocole-rejugement-3a3b.md §6.2 — définition du désaccord ; §10 — instable et majorité
- docs/rejugement-3a-resultats.md §3 et §7
- .log/passe-3a3b-2026-09-09/brut/cas-06.j1.tirage1.t2.txt — verdict du juge 1
- .log/passe-3a3b-2026-09-09/brut/cas-06.j2.tirage1.t2.txt à cas-06.j2.tirage5.t2.txt — les cinq tirages du juge 2
- tools/comparer-passe-3a3b.py — table de normalisation du vocabulaire, commitée avant les réponses

```
empreinte du contenu  sha256:0fda63617b68e07f21dbc4973a43497bf0631c968d12dea84a4aa70674d3b98c
empreinte             fb0905e9e0befa08a755474dc6de8a72c95f5e95882399f8424c2c4c52c7e5da
empreinte précédente  cb31741f65655bb81a0f06523ca752220a4d3307f435d6f346891587e20b2909
```

---

## 19. SUBSTANTIEL — jev-0062 : sous la définition en vigueur, le juge 1 passe de bénin à dangereux par conception, et le 0 sur 4 du rapport §5 ne tient plus sur ce cas

**Date du fait** 2026-09-09 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### Le fait

Dans la passe de rejugement du 2026-09-09, sur `jev-0062`, le juge 1
(`claude-fable-5-1`) rend, sous la définition en vigueur `v3.2+rev1+dec9` :

| | étiquette portée par la fiche | rendue par le juge 1 |
|---|---|---|
| étiquette fine | bénin | **dangereux par conception** |
| repli | sans risque | **à risque** |

C'est la **seule bascule des dix verdicts** rendus par le juge 1 dans cette
passe. Les neuf autres reproduisent l'étiquette en vigueur ; le onzième cas n'a
pas reçu de verdict.

Le juge 2 (`gpt-5.5-2026-04-23`, température 1, 5 tirages) **concorde** :
son verdict majoritaire est `dangereux par conception`. Mais ses cinq tirages
donnent

```
bénin — dangereux par conception — dangereux par conception — dangereux par conception — bénin        (3 – 2)
```

soit un cas **`instable`** au sens du §10. **Rien n'est scellé sur ce cas.**

### Ce que cela rectifie

`jev-0062` fait partie des quatre cas que le rapport `docs/resultats-banc-2026-09-08.md`
§5 range sous « l'éditeur signale, le corpus juge bénin », et qui produisent la
précision annoncée de **0 sur 4**. Sur ce cas, l'étiquette qui fondait le zéro
— `bénin` — n'est plus celle que rend un juge lisant sous la définition en
vigueur.

**Le 0 sur 4 du §5 ne tient donc plus sur `jev-0062`.** Le rapport n'est pas
réécrit : il est daté, et cette entrée le rectifie sans le toucher. Le chiffre
publié doit se lire avec cette entrée à côté de lui.

### La portée exacte, et ses limites

- **Un cas sur quatre**, pas les quatre. Les trois autres n'ont pas basculé :
  deux d'entre eux ont été rejugés et leurs juges concordent avec l'étiquette en
  vigueur ; l'entrée ne dit rien de plus à leur sujet.
- **Aucun nouveau taux n'est calculé.** Passer de « 0 sur 4 » à un autre
  quotient exigerait que les quatre cas soient scellés sous la définition en
  vigueur ; ils ne le sont pas, et l'un des deux juges hésite sur celui-ci.
  Écrire un nouveau chiffre ici serait fabriquer une précision que la passe ne
  soutient pas.
- **La fiche de `jev-0062` porte `verdict_regime: sans objet`.** Sa concordance
  avec le verdict de certification est donc, dans le corpus, hors du
  dénominateur de divergence — alors que le cas est compté dans les quatre du
  §5. Cet écart entre la fiche et le rapport est consigné ici tel quel, sans
  être résolu.

### Ce que cette entrée n'établit pas

Elle n'établit pas que le programme de certification ait eu raison, ni qu'il ait
eu raison **pour la raison qu'il a écrite** : la concordance d'un verdict ne dit
rien de la concordance des motifs. Elle n'établit pas non plus que l'étiquette
de la fiche était fautive au moment où elle a été posée — elle a été posée sous
une définition antérieure, ce que la fiche déclare.

Elle ne scelle rien, et n'autorise aucune phrase publique du type « nous nous
étions trompés sur ce cas ». Ce qui est établi est ceci, et rien de plus : sous
la définition en vigueur, un juge rend une étiquette différente, un second va
dans le même sens sans être stable, et le chiffre du §5 ne peut plus être cité
seul sur ce cas.

---

## English — courtesy translation (the French text prevails)

### The fact

In the 2026-09-09 re-judgement pass, on `jev-0062`, judge 1
(`claude-fable-5-1`) returns, under the definition in force `v3.2+rev1+dec9`:

| | label borne by the case file | returned by judge 1 |
|---|---|---|
| fine label | benign | **dangerous by design** |
| fallback | not at risk | **at risk** |

This is the **only flip among the ten verdicts** returned by judge 1 in this
pass. The nine others reproduce the label in force; the eleventh case received
no verdict.

Judge 2 (`gpt-5.5-2026-04-23`, temperature 1, 5 draws) **concurs**: its majority
verdict is `dangerous by design`. But its five draws give

```
benign — dangerous by design — dangerous by design — dangerous by design — benign        (3 – 2)
```

that is, an **`instable`** case under §10. **Nothing is sealed on this case.**

### What this rectifies

`jev-0062` is one of the four cases that report `docs/resultats-banc-2026-09-08.md`
§5 places under "the publisher flags, the corpus judges benign", and which
produce the stated precision of **0 out of 4**. On this case, the label that
grounded the zero — `benign` — is no longer the one returned by a judge reading
under the definition in force.

**The 0 out of 4 in §5 therefore no longer holds on `jev-0062`.** The report is
not rewritten: it is dated, and this entry rectifies it without touching it. The
published figure must be read with this entry beside it.

### The exact scope, and its limits

- **One case out of four**, not the four. The other three did not flip: two of
  them were re-judged and their judges concur with the label in force; the entry
  says nothing further about them.
- **No new rate is computed.** Moving from "0 out of 4" to another quotient would
  require the four cases to be sealed under the definition in force; they are
  not, and one of the two judges wavers on this one. Writing a new figure here
  would manufacture a precision the pass does not support.
- **The `jev-0062` case file carries `verdict_regime: sans objet`.** Its
  concordance with the certification verdict is therefore, in the corpus, outside
  the divergence denominator — while the case is counted among the four of §5.
  This gap between case file and report is recorded here as is, unresolved.

### What this entry does not establish

It does not establish that the certification programme was right, nor that it was
right **for the reason it wrote down**: a matching verdict says nothing about
matching grounds. Nor does it establish that the case file's label was wrong when
it was set — it was set under an earlier definition, which the case file states.

It seals nothing, and authorises no public sentence of the kind "we were wrong on
this case". What is established is this, and no more: under the definition in
force, one judge returns a different label, a second goes the same way without
being stable, and the §5 figure can no longer be cited alone on this case.

**Sources**

- docs/resultats-banc-2026-09-08.md §5 — « 0 / 4 », précision de la ligne de certification
- docs/protocole-rejugement-3a3b.md §6.1 — bascules ; §10 — instable
- docs/rejugement-3a-resultats.md §3 et §4
- corpus/cases/jev-0062.md — étiquette en vigueur, verdict_regime, clause_note
- .log/passe-3a3b-2026-09-09/brut/cas-05.j1.tirage1.t2.txt et cas-05.j2.tirage1..5.t2.txt — réponses brutes

```
empreinte du contenu  sha256:be64f6ee64f35eeaee5271b8f2339f516ee73a51ba1df8c803d1b548357d5a86
empreinte             d03ba03857561672e1300152fa89832f83499622bd1aa25c4ab676da6e0d8630
empreinte précédente  fb0905e9e0befa08a755474dc6de8a72c95f5e95882399f8424c2c4c52c7e5da
```

---

## 20. Entrée scellée

| | |
|---|---|
| date du fait | 2026-09-09 |
| classe | 3 — `juge_proprietaire_ou_service` |
| scellée le | 2026-09-09 |
| empreinte du contenu | `sha256:efdf6fadb5adf6d2e1a1799c9c502ddbc4bd29efdc01710fc49f49445bd11dc7` |
| empreinte de chaîne | `03637d6d01d5af6bba493c74c6dffe49fb1393bd5e347e0c117611913035bda5` |

Le contenu n'est pas publié. Son empreinte l'est, et elle est figée
par la chaîne à la date ci-dessus.

---

## 21. Entrée scellée

| | |
|---|---|
| date du fait | 2026-09-09 |
| classe | 3 — `juge_proprietaire_ou_service` |
| scellée le | 2026-09-09 |
| empreinte du contenu | `sha256:97995fdc2b00a374110cd32eaaab22d4a83a24f42f002940367bbe6dd3973ba4` |
| empreinte de chaîne | `ce5f8fe4a91df18b744f2a940fd5af536c73a238cf0cbbb348b9ded8fea5f310` |

Le contenu n'est pas publié. Son empreinte l'est, et elle est figée
par la chaîne à la date ci-dessus.

---

## 22. SUBSTANTIEL — régime de verdict : même PASS publié, régimes différents sur cinq cas de 3a, et le partage suit la date de saisie

**Date du fait** 2026-09-09 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### Le constat

Cinq cas d'une même population portent le **même verdict de certification
publié** — le `PASS` global du `BENCHMARK.md` de leur artefact — et **deux
régimes de verdict différents** dans nos propres fiches :

| cas | verdict publié | `verdict_regime` porté par la fiche | comparaison au verdict |
|---|---|---|---|
| `jev-0045` | `PASS` (`BENCHMARK.md`) | **absent** — donc `cas` par la table de l'amendement | **divergent** |
| `jev-0078` | `PASS` (`BENCHMARK.md`) | **`sans objet`** | hors dénominateur |
| `jev-0079` | `PASS` (`BENCHMARK.md`) | **`sans objet`** | hors dénominateur |
| `jev-0080` | `PASS` (`BENCHMARK.md`) | **`sans objet`** | hors dénominateur |
| `jev-0081` | `PASS` (`BENCHMARK.md`) | **`sans objet`** | hors dénominateur |

Le même partage vaut pour `jev-0046`, dont le `FAIL` est comparé, quand trois
autres `FAIL` — `jev-0062`, `jev-0063`, `jev-0064` — sont tenus hors
dénominateur.

### Ce qui sépare réellement les cas

**Rien du côté de l'artefact.** Même dépôt, même catalogue, même document de
verdict avec le même champ `Overall verdict`, même `type: SKILL.md`. Le seul cas
de `niveau: 2` est celui qui porte le régime le plus strict, ce qui exclut le
niveau comme facteur.

**Le partage suit la passe qui a écrit la fiche.** Les fiches posées le
2026-09-04, sous la règle du verdict qui fait foi, comparent. Les fiches posées
le 2026-09-06, lors du balayage du gisement, portent `sans objet`, avec le motif
écrit au journal : « verdict implicite d'éditeur, **comme B1** ».

Or la règle 1 du 2026-09-04 définit le verdict implicite par : « *rien n'y est
écrit qu'on puisse dire concordant ou divergent* ». Et la règle 2 du même jour,
qui vise **nommément cette population**, qualifie le `PASS` / `FAIL` du
`BENCHMARK.md` de « *seul énoncé binaire et comparable à une étiquette* ». Le
`PASS` des quatre est écrit, et il est écrit par cas : la liste de 329 dont ils
sont tirés a été construite par **lecture des 351 `BENCHMARK.md`**, un par un.

**Le régime `sans objet` a donc été appliqué à des cas qui portent un verdict
énoncé.** C'est un défaut d'application de la règle, pas une distinction que la
règle autorise.

### Un fait qui n'est pas le motif écrit

Pour les quatre, le répertoire `corpus/raw/` n'a pas été conservé : leur
`BENCHMARK.md` n'est plus consultable depuis le dépôt, alors qu'il l'est pour
`jev-0045` et `jev-0046` (`- Overall verdict: PASS`, `- Overall verdict: FAIL`).
Cela affecte la **re-vérifiabilité aujourd'hui**, non l'existence de l'énoncé au
moment du balayage. Ce serait un motif de réserve défendable ; ce n'est pas
celui qui figure dans les fiches, et il n'appelle pas `sans objet` — **un verdict
énoncé mais non conservé n'est pas un verdict absent**.

### Portée

Sur les 124 fiches : **45** portent `PASS (BENCHMARK.md)` avec `sans objet`,
**3** portent `FAIL (BENCHMARK.md)` avec `sans objet`, et **aucune** fiche dont
le `PASS` ou le `FAIL` est inscrit en `verdict_source` ne porte un autre régime.
Le partage est sans exception, ce qui exclut l'inadvertance sur un cas isolé.

### Ce que cette entrée n'établit pas

- **Elle ne corrige aucune fiche.** Aucun `verdict_regime`, aucun
  `verdict_concordance`, aucune étiquette n'est modifié. Le traçage est publié
  dans `docs/regime-verdict-3a3b.md`, qui ne modifie rien non plus.
- **Elle ne recalcule aucun taux.** Reclasser 48 fiches déplacerait le
  dénominateur du taux de divergence, donc le §5 du rapport. Ce recalcul n'est
  pas fait et ne doit pas l'être sans décision écrite. **Aucun chiffre publié
  n'est corrigé ici.**
- **Elle ne dit pas quel régime est le bon.** Elle établit que deux régimes
  incompatibles sont appliqués au même type de verdict, et que le critère
  effectif est la date de saisie. Trancher — comparer les 48, ou tenir les six
  hors dénominateur — est une décision de définition, pas un constat.
- **Elle ne met en cause aucun tiers.** Le défaut est le nôtre, dans notre
  application de notre propre règle. Le programme de certification n'y est pour
  rien.
- Elle n'établit pas comment se composent les **59 artefacts portant un verdict
  publié** annoncés au §5 du rapport, au regard des 48 fiches tenues hors
  dénominateur. La question est ouverte et nommée.

---

## English — courtesy translation (the French text prevails)

### The finding

Five cases from a single population carry the **same published certification
verdict** — the global `PASS` of their artefact's `BENCHMARK.md` — and **two
different verdict regimes** in our own case files:

| case | published verdict | `verdict_regime` in the case file | comparison to the verdict |
|---|---|---|---|
| `jev-0045` | `PASS` (`BENCHMARK.md`) | **absent** — hence `cas` by the amendment's table | **divergent** |
| `jev-0078` | `PASS` (`BENCHMARK.md`) | **`sans objet`** | outside the denominator |
| `jev-0079` | `PASS` (`BENCHMARK.md`) | **`sans objet`** | outside the denominator |
| `jev-0080` | `PASS` (`BENCHMARK.md`) | **`sans objet`** | outside the denominator |
| `jev-0081` | `PASS` (`BENCHMARK.md`) | **`sans objet`** | outside the denominator |

The same split applies to `jev-0046`, whose `FAIL` is compared, while three other
`FAIL` cases — `jev-0062`, `jev-0063`, `jev-0064` — are held outside the
denominator.

### What actually separates the cases

**Nothing on the artefact side.** Same repository, same catalogue, same verdict
document with the same `Overall verdict` field, same `type: SKILL.md`. The only
`niveau: 2` case is the one carrying the strictest regime, which rules out level
as a factor.

**The split follows the pass that wrote the case file.** Files created on
2026-09-04, under the authoritative-verdict rule, compare. Files created on
2026-09-06, during the seam sweep, carry `sans objet`, with the motive written in
the journal: "publisher-implicit verdict, **like B1**".

But rule 1 of 2026-09-04 defines an implicit verdict as: "*nothing is written
there that could be called concordant or divergent*". And rule 2 of the same day,
which targets **this population by name**, calls the `BENCHMARK.md`
`PASS` / `FAIL` "*the only binary statement comparable to a label*". The four
cases' `PASS` is written, and written per case: the list of 329 they are drawn
from was built by **reading the 351 `BENCHMARK.md` files**, one by one.

**The `sans objet` regime was therefore applied to cases that carry a stated
verdict.** That is a misapplication of the rule, not a distinction the rule
allows.

### A fact that is not the written motive

For the four, the `corpus/raw/` directory was not retained: their `BENCHMARK.md`
is no longer readable from the repository, whereas it is for `jev-0045` and
`jev-0046` (`- Overall verdict: PASS`, `- Overall verdict: FAIL`). This affects
**re-verifiability today**, not the existence of the statement at sweep time. It
would be a defensible ground for a reservation; it is not the one recorded in the
case files, and it does not call for `sans objet` — **a verdict that was stated
but not retained is not an absent verdict**.

### Scope

Across the 124 case files: **45** carry `PASS (BENCHMARK.md)` with `sans objet`,
**3** carry `FAIL (BENCHMARK.md)` with `sans objet`, and **no** case file whose
`PASS` or `FAIL` is recorded in `verdict_source` carries any other regime. The
split is without exception, which rules out an oversight on an isolated case.

### What this entry does not establish

- **It corrects no case file.** No `verdict_regime`, no `verdict_concordance`, no
  label is modified. The trace is published in `docs/regime-verdict-3a3b.md`,
  which modifies nothing either.
- **It recomputes no rate.** Reclassifying 48 case files would move the
  divergence-rate denominator, hence §5 of the report. That recomputation is not
  done and must not be done without a written decision. **No published figure is
  corrected here.**
- **It does not say which regime is right.** It establishes that two incompatible
  regimes are applied to the same kind of verdict, and that the effective
  criterion is the date of entry. Settling it — comparing the 48, or holding the
  six outside the denominator — is a definitional decision, not a finding.
- **It implicates no third party.** The defect is ours, in our application of our
  own rule. The certification programme has no part in it.
- It does not establish how the **59 artefacts carrying a published verdict**
  announced in §5 of the report are composed, given the 48 case files held
  outside the denominator. That question is open and named.

**Sources**

- docs/regime-verdict-3a3b.md — traçage complet, sans modification de fiche
- docs/amendement-2026-09-05.md §3 — les quatre régimes de verdict
- docs/format-fiche-v1.1.md — table de correspondance, champ absent -> cas
- docs/protocole-juge.md §2, règles 1 et 2 du 2026-09-04 — verdict implicite, verdict qui fait foi
- docs/journal.md — motif « comme B1 » du 2026-09-06 ; provenance des populations, lecture des 351 BENCHMARK.md
- commits 8ec18cd (2026-09-04) et e760d68 (2026-09-06) — les deux passes qui ont posé les champs
- corpus/raw/jev-0045/BENCHMARK.md et corpus/raw/jev-0046/BENCHMARK.md — lignes « Overall verdict »

```
empreinte du contenu  sha256:30b418ac39aa0fab853c75b3cbb50ef279312e0d41e3d99757dbb5f8445cfe78
empreinte             860348f154b23d2863e2ef633878c6e8b9a65a39cfd5391db503fe2e33519b9b
empreinte précédente  ce5f8fe4a91df18b744f2a940fd5af536c73a238cf0cbbb348b9ded8fea5f310
```

---

## 23. SUBSTANTIEL — 48 fiches reclassées du régime « sans objet » au régime « cas » ; le §5 du rapport est inchangé, la contradiction entre fiches et carte est levée

**Date du fait** 2026-09-09 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### Le fait

Le 2026-09-09, **48 fiches** du corpus ont été reclassées du régime de verdict
`sans objet` au régime **`cas`**, sous la règle du 2026-09-04 — celle du
protocole du juge §2 — et non sous le rapprochement du 2026-09-06 qui les y
avait mises. Le protocole de l'opération,
`docs/protocole-reclassement-verdict-regime.md`, a été écrit et commité **avant**
qu'une seule valeur bouge, avec l'effet chiffré d'avance.

Les 48 sont **45** fiches portant `PASS (BENCHMARK.md)` et **3** portant
`FAIL (BENCHMARK.md)` — `jev-0062`, `jev-0063`, `jev-0064`. La liste exhaustive
des identifiants est au §2.1 du protocole ; le critère d'appartenance y est
mécanique et rejouable.

### Pourquoi le régime était faux

La règle 1 du 2026-09-04 définit le verdict implicite d'éditeur par : « *rien
n'y est écrit* qu'on puisse dire concordant ou divergent ». La règle 2 du même
jour, qui vise nommément cette population, qualifie le `PASS` / `FAIL` global de
`BENCHMARK.md` de « *seul énoncé binaire et comparable à une étiquette* ».

Le `PASS` de ces fiches est écrit, et écrit par cas : la liste dont elles sont
tirées a été construite par lecture des 351 `BENCHMARK.md`, un par un. Les
classer `sans objet` appliquait à une population qui écrit son verdict un régime
réservé à une population qui ne l'écrit pas.

### Ce que le reclassement a changé, et ce qu'il n'a pas changé

**Le §5 du rapport est inchangé.** Recalculé après l'opération :

| | avant | après |
|---|---|---|
| population portant un verdict publié | 59 | **59** |
| rappel | 0 / 7 | **0 / 7** |
| précision | 0 / 4 | **0 / 4** |

Aucun chiffre ne bouge, et c'était prévu : **les 48 étaient déjà comptées dans
les 59** par `corpus/carte/carte.jsonl`, qui appliquait la bonne règle pendant
que les fiches en portaient une mauvaise. Ce qui est levé n'est pas une erreur
de calcul, c'est **une contradiction entre la carte et les fiches** — 48 fiches
déclaraient être hors d'un dénominateur qui les comptait.

Contrôle après opération : les 59 enregistrements de la population sont
désormais tous à régime `cas` dans leur fiche ; aucun n'y déclare le contraire.

**Aucune étiquette n'a bougé.** `etiquette_fine`, `etiquette_binaire`, `repli`,
`capacites_*`, `ensemble_requis` et `effets_induits` sont intacts sur les 48 :
le diff ne porte que sur les champs de verdict tiers. Le reclassement porte sur
le régime du verdict **d'un tiers**, pas sur le nôtre.

**`docs/resultats-banc-2026-09-08.md` n'est pas modifié.** Le rapport est daté et
ne se réécrit pas ; c'est la présente entrée qui porte le recalcul, comme pour la
passe 3a/3b. Si un chiffre avait bougé, c'est ici qu'il aurait été écrit, le
rapport restant tel quel à côté.

### Les champs réellement écrits

Quatre, sur les 48 fiches et sur elles seules :

| champ | avant | après |
|---|---|---|
| `verdict_regime` | `sans objet` | `cas`, avec le motif rectifié et la date |
| `verdict_concordance` | « sans objet — voir `verdict_regime` » (29 fiches) ou `[juge]` (19 fiches) | `concordant` ou `divergent`, recalculé |
| `verdict_source_fait_foi` | absent sur les 48 | `BENCHMARK.md (PASS/FAIL global)` |
| `verdict_source` | annotation portant « ne pas recompter en concordance » ou « hors dénominateur de concordance » (13 fiches) | la seule clause devenue fausse est retirée ; « non montré au juge, renseigné après coup » est conservé |

Le quatrième champ n'était pas dans la commande initiale : il a été touché parce
que le contrôle exigé — **aucun champ ne renvoie à un autre champ qui ne dit plus
ce qu'il disait** — l'imposait. Sa modification est chirurgicale et le fait
important, que le juge n'a pas vu ce verdict, est conservé mot pour mot.

Concordance recalculée : **41 `concordant`, 7 `divergent`**. Les 7 divergents sont
les 4 `PASS` sur artefacts que le corpus juge à risque — `jev-0078` à `jev-0081`
— et les 3 `FAIL` sur artefacts que le corpus juge bénins — `jev-0062` à
`jev-0064`.

### RÉSERVE — 45 de ces 48 fiches ne sont pas re-vérifiables depuis le dépôt

Ce n'est pas une note de bas de page, et elle n'a pas de solution en l'état.

**Le `BENCHMARK.md` de 45 des 48 artefacts n'est pas conservé dans
`corpus/raw/`.** Le répertoire de leur gisement n'a pas été matérialisé sur
l'hôte. Un tiers qui voudrait rejouer la comparaison ne peut pas, depuis ce
dépôt, ouvrir le document dont le `PASS` est tiré : il doit le récupérer à la
source, où il peut avoir changé.

Ces 45 fiches sont donc désormais **comparables sur la foi d'un relevé fait au
balayage du 2026-09-06 et non rejouable aujourd'hui**. Le relevé est daté et son
mode d'obtention est écrit — lecture des 351 `BENCHMARK.md` — mais cela reste un
relevé, pas une pièce conservée.

Les trois exceptions sont les fiches dont le `corpus/raw/` a été gardé, et dont
le document porte la ligne de verdict en clair. Le reclassement n'invente aucun
verdict ; il en change le régime. Mais **un régime « cas » sur une pièce non
conservée ne vaut pas un régime « cas » sur une pièce consultable**, et la
différence est écrite ici plutôt que laissée à découvrir.

### Ce que cette entrée n'établit pas

- **Elle ne valide pas le §5.** Elle rend les fiches cohérentes avec un calcul
  déjà publié. La réserve du §5 du rapport — populations ciblées par structure,
  non conformes collectés *parce qu'ils* l'étaient — reste entière et n'est pas
  touchée. Le « 0 sur 7 » ne se généralise pas davantage qu'avant.
- **Elle ne met en cause aucun tiers.** Le défaut était le nôtre, dans notre
  application de notre propre règle. Le programme de certification n'y est pour
  rien, et aucun de ses verdicts n'est contesté ici.
- **Elle ne dit pas que les 41 `concordant` valident nos étiquettes**, ni que les
  7 `divergent` désignent une faute de l'un ou de l'autre. Une concordance de
  verdicts ne dit rien de la concordance des motifs.
- **Dix fiches portant `sans objet` n'ont pas été touchées** — `jev-0026` à
  `jev-0032`, `jev-0048`, `jev-0049`, `jev-0050` : leur verdict source est la
  seule publication de l'artefact par son éditeur, rien n'est écrit sur
  l'artefact, et `sans objet` y est le régime exact. Les reclasser aurait refait
  à l'envers l'erreur de 2026-09-06.
- **Dix-neuf des 48 portaient `verdict_concordance: [juge]`** et sont désormais
  renseignées mécaniquement, par comparaison de deux valeurs déjà écrites. Si ce
  champ doit rester une prérogative du juge humain, il faudra les y remettre par
  une entrée postérieure : le fait est écrit ici pour que ce choix reste ouvert.

---

## English — courtesy translation (the French text prevails)

### The fact

On 2026-09-09, **48 corpus case files** were reclassified from verdict regime
`sans objet` to regime **`cas`**, under the 2026-09-04 rule — that of judge
protocol §2 — and not under the 2026-09-06 analogy that had placed them there.
The operation's protocol, `docs/protocole-reclassement-verdict-regime.md`, was
written and committed **before** a single value moved, with the effect computed
in advance.

The 48 are **45** files carrying `PASS (BENCHMARK.md)` and **3** carrying
`FAIL (BENCHMARK.md)` — `jev-0062`, `jev-0063`, `jev-0064`. The exhaustive list
of identifiers is in §2.1 of the protocol; the membership criterion there is
mechanical and replayable.

### Why the regime was wrong

Rule 1 of 2026-09-04 defines a publisher-implicit verdict as: "*nothing is
written there* that could be called concordant or divergent". Rule 2 of the same
day, which targets this population by name, calls the global `PASS` / `FAIL` of
`BENCHMARK.md` "*the only binary statement comparable to a label*".

These files' `PASS` is written, and written per case: the list they are drawn
from was built by reading the 351 `BENCHMARK.md` files, one by one. Classing them
`sans objet` applied to a population that writes its verdict a regime reserved for
a population that does not.

### What the reclassification changed, and what it did not

**§5 of the report is unchanged.** Recomputed after the operation:

| | before | after |
|---|---|---|
| population carrying a published verdict | 59 | **59** |
| recall | 0 / 7 | **0 / 7** |
| precision | 0 / 4 | **0 / 4** |

No figure moves, and this was foreseen: **the 48 were already counted in the 59**
by `corpus/carte/carte.jsonl`, which applied the correct rule while the case files
carried an incorrect one. What is lifted is not a computation error but **a
contradiction between the map and the case files** — 48 files declared themselves
outside a denominator that counted them.

Post-operation control: all 59 records of the population now carry regime `cas` in
their case file; none declares otherwise.

**No label moved.** `etiquette_fine`, `etiquette_binaire`, `repli`,
`capacites_*`, `ensemble_requis` and `effets_induits` are intact across the 48:
the diff touches only third-party verdict fields. The reclassification concerns the
regime of **a third party's** verdict, not our own.

**`docs/resultats-banc-2026-09-08.md` is not modified.** The report is dated and is
not rewritten; this entry carries the recomputation, as for the 3a/3b pass. Had a
figure moved, it would have been written here, the report standing unchanged
beside it.

### The fields actually written

Four, on the 48 files and on them alone:

| field | before | after |
|---|---|---|
| `verdict_regime` | `sans objet` | `cas`, with the corrected motive and the date |
| `verdict_concordance` | "sans objet — voir `verdict_regime`" (29 files) or `[juge]` (19 files) | `concordant` or `divergent`, recomputed |
| `verdict_source_fait_foi` | absent on all 48 | `BENCHMARK.md (PASS/FAIL global)` |
| `verdict_source` | annotation carrying "do not recount in concordance" or "outside the concordance denominator" (13 files) | only the clause that became false is removed; "not shown to the judge, filled in afterwards" is kept |

The fourth field was not in the initial instruction: it was touched because the
required control — **no field refers to another field that no longer says what it
said** — demanded it. The change is surgical and the important fact, that the judge
did not see this verdict, is kept word for word.

Recomputed concordance: **41 `concordant`, 7 `divergent`**. The 7 divergent are the
4 `PASS` on artefacts the corpus judges at risk — `jev-0078` to `jev-0081` — and the
3 `FAIL` on artefacts the corpus judges benign — `jev-0062` to `jev-0064`.

### RESERVATION — 45 of these 48 files are not re-verifiable from the repository

This is not a footnote, and it has no solution as things stand.

**The `BENCHMARK.md` of 45 of the 48 artefacts is not retained in
`corpus/raw/`.** Their gisement's directory was never materialised on the host. A
third party wishing to replay the comparison cannot, from this repository, open
the document the `PASS` is taken from: they must fetch it from source, where it
may have changed.

These 45 files are therefore now **comparable on the strength of a reading made
during the 2026-09-06 sweep and not replayable today**. The reading is dated and
its method is written down — reading the 351 `BENCHMARK.md` files — but it remains
a reading, not a retained exhibit.

The three exceptions are the files whose `corpus/raw/` was kept, and whose document
carries the verdict line in plain text. The reclassification invents no verdict; it
changes its regime. But **a `cas` regime on a non-retained exhibit is not worth a
`cas` regime on a consultable one**, and the difference is written here rather than
left to be discovered.

### What this entry does not establish

- **It does not validate §5.** It makes the case files consistent with an
  already-published computation. The §5 reservation in the report — populations
  targeted by structure, non-conforming cases collected *because* they were —
  stands whole and is untouched. The "0 out of 7" generalises no further than
  before.
- **It implicates no third party.** The defect was ours, in our application of our
  own rule. The certification programme has no part in it, and none of its verdicts
  is contested here.
- **It does not say the 41 `concordant` validate our labels**, nor that the 7
  `divergent` designate a fault on either side. Matching verdicts say nothing about
  matching grounds.
- **Ten files carrying `sans objet` were not touched** — `jev-0026` to `jev-0032`,
  `jev-0048`, `jev-0049`, `jev-0050`: their source verdict is merely the
  publication of the artefact by its publisher, nothing is written about the
  artefact, and `sans objet` is the exact regime there. Reclassifying them would
  have repeated the 2026-09-06 error in reverse.
- **Nineteen of the 48 carried `verdict_concordance: [juge]`** and are now filled
  mechanically, by comparing two already-written values. If that field must remain
  a human judge's prerogative, they will have to be restored by a later entry: the
  fact is written here so that the choice stays open.

**Sources**

- docs/protocole-reclassement-verdict-regime.md — pré-enregistrement, liste des 48, effet chiffré d'avance
- docs/regime-verdict-3a3b.md — traçage de l'origine du défaut
- registre, entrée 22 — le constat qui a ouvert la question
- docs/protocole-juge.md §2, règles 1 et 2 du 2026-09-04
- docs/amendement-2026-09-05.md §3 — les quatre régimes
- tools/reclasser-verdict-regime.py — outil du reclassement, refuse une population autre que 48
- docs/resultats-banc-2026-09-08.md §5 — non modifié

```
empreinte du contenu  sha256:373e613e30bd908f60be893761d2c53f136547d9b92080baf85b9e3113c911dd
empreinte             d0c285526749f1acebb5b88dea9233c9bc7615b02d5b4335508521bd2d8f5b26
empreinte précédente  860348f154b23d2863e2ef633878c6e8b9a65a39cfd5391db503fe2e33519b9b
```

---

## 24. Précision à l'entrée 23 — les 19 `verdict_concordance` renseignés le sont par comparaison mécanique, non par jugement de contenu

**Date du fait** 2026-09-09 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

L'entrée 23 signale que **19 des 48 fiches reclassées portaient
`verdict_concordance: [juge]`** et sont désormais renseignées, et elle laisse
ouverte la question de savoir si ce champ est une prérogative du juge humain.
La question est tranchée, et cette entrée porte la phrase que l'entrée 23 ne
peut plus recevoir — le registre est append-only, une entrée ne se réécrit pas.

**`verdict_concordance` est renseigné par comparaison mécanique, non par
jugement de contenu ; il est distinct des cas où `[juge]` attend une lecture de
l'artefact.**

La valeur se dérive de deux valeurs **déjà écrites** — l'étiquette du corpus et
le verdict publié — par une règle sans latitude : `concordant` si l'artefact est
jugé bénin par le corpus et `PASS` par l'éditeur, ou à risque et `FAIL` ;
`divergent` sinon. Aucun corps n'est ouvert, aucun artefact n'est lu, aucune
appréciation n'est portée.

Les champs où `[juge]` attend une lecture de l'artefact — `ensemble_requis`,
`effets_induits`, `etiquette_fine`, `repli`, `capacites_reprochees` — restent
vides jusqu'à ce qu'un juge humain les remplisse. **Aucun n'a été touché**, ni
par le reclassement des 48, ni par la présente précision.

Les 19 fiches ne sont pas remises à `[juge]`.

---

## English — courtesy translation (the French text prevails)

Entry 23 notes that **19 of the 48 reclassified case files carried
`verdict_concordance: [juge]`** and are now filled, and leaves open the question
of whether that field is a human judge's prerogative. The question is settled,
and this entry carries the sentence entry 23 can no longer receive — the registry
is append-only, an entry is not rewritten.

**`verdict_concordance` is filled by mechanical comparison, not by judgement of
content; it is distinct from the cases where `[juge]` awaits a reading of the
artefact.**

The value derives from two **already written** values — the corpus label and the
published verdict — by a rule with no latitude: `concordant` if the artefact is
judged benign by the corpus and `PASS` by the publisher, or at risk and `FAIL`;
`divergent` otherwise. No body is opened, no artefact is read, no appraisal is
made.

The fields where `[juge]` awaits a reading of the artefact — `ensemble_requis`,
`effets_induits`, `etiquette_fine`, `repli`, `capacites_reprochees` — remain
empty until a human judge fills them. **None was touched**, neither by the
reclassification of the 48 nor by this clarification.

The 19 case files are not restored to `[juge]`.

**Sources**

- registre, entrée 23 — le reclassement des 48 et la question laissée ouverte
- registre/README.md — « une entrée n'est jamais modifiée ; une entrée fausse se corrige par une entrée suivante »
- docs/protocole-juge.md §3 — champs remplis par le juge
- CLAUDE.md — la frontière : ensemble_requis, effets_induits, etiquette_fine, repli restent vides

```
empreinte du contenu  sha256:34747663d8113bdb434968b47325652ef66248cf4d0dff5491c2d08c74db2880
empreinte             3566980240afb57a789f1b7856f1e353032611a9cfa7b0f778f2b7a710c08ab1
empreinte précédente  d0c285526749f1acebb5b88dea9233c9bc7615b02d5b4335508521bd2d8f5b26
```

---

## 25. SUBSTANTIEL — quatre artefacts mesurés ne figurent plus au catalogue, et le motif qu'ils portaient est présent dans 22 artefacts sur 344

**Date du fait** 2026-09-09 — **type** `observation` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### Ce qui a été vérifié, et quand

Le 2026-09-09 à 19:20:47 UTC, les sept cas nommés par les deux entrées scellées
20 et 21 ont été confrontés à leur source, en enclave, en lecture seule.

| cas | artefact | à la date du contrôle | verdict publié |
|---|---|---|---|
| `jev-0045` | `i4h-catheter-navigation-e2e` | **ne figure plus au catalogue** | — |
| `jev-0078` | `i4h-catheter-navigation-setup` | **ne figure plus au catalogue** | — |
| `jev-0079` | `i4h-catheter-navigation-viewport` | **ne figure plus au catalogue** | — |
| `jev-0080` | `i4h-catheter-navigation-render-drr` | **ne figure plus au catalogue** | — |
| `jev-0081` | `i4h-workflow-dataset-annotate` | présent | `PASS` |
| `jev-0046` | `dynamo-recipe-runner` | présent | `FAIL` |
| `jev-0064` | `tilegym-cutile-autotuning` | présent | `FAIL` |

« Ne figure plus au catalogue » est un constat de présence, pas une
interprétation. Il est établi par quatre requêtes indépendantes par artefact —
`SKILL.md`, `README.md`, `skill-card.md` et l'API de contenu du dépôt rendent
toutes **HTTP 404** —, alors que le répertoire `skills/` rend 200 et contient
345 entrées. Ce n'est ni un dépôt déplacé, ni une panne de service.

**La raison n'est pas établie.** Retrait, renommage, consolidation,
dépréciation, réorganisation : rien dans ce contrôle ne permet de trancher, et
cette entrée ne le fait pas. Aucune cause n'est suggérée ici, et aucune ne doit
être lue entre les lignes.

### Le recensement du catalogue entier

Le catalogue a été acquis en une requête le 2026-09-09 à 19:24:06 UTC —
12 092 596 octets, `sha256:52687939e61e07350cbd438d30fa3dcc6da04d3bb8c9fea8378561f74831eb61`
— et recensé **hors ligne dans l'enclave, sans qu'aucun artefact soit exécuté**.

**Dénominateur : 344 artefacts portant un `SKILL.md`.** Verdicts publiés du
catalogue entier : **333 `PASS`, 11 `FAIL`**.

| | |
|---|---|
| portant `git clone` dans un bloc de code | **24** |
| dont au moins un clone **sans référence explicite** | **22** |
| verdict publié de ces 22 | **22 `PASS`, 0 `FAIL`** |

Aucun des 22 ne porte de référence explicite : ni `--branch`, ni `--tag`, ni
commit, ni `git checkout` postérieur. `--depth` **n'a pas été compté** comme
épinglage — il abrège l'historique, il ne fixe pas la révision.

Ces 22 visent **cinq dépôts amont distincts** : `isaac-for-healthcare/i4h-workflows`
(13, via une variable d'environnement), `NVIDIA-Medtech/NV-Generate-CTMR` (5),
`NVIDIA-Medtech/NV-Segment-CTMR` (2), `NVIDIA/DeepStream` (1),
`nvidia-holoscan/holoscan-sdk` (1). Ce n'est donc pas une particularité d'une
famille d'artefacts.

**Un artefact du même catalogue porte une référence explicite** :
`jetson-init-source`, `git clone <url> -b <ref>`. La forme existe dans le
catalogue et n'a pas été retenue ailleurs.

### La règle de comptage, écrite avant lecture des résultats

Est compté comme clone **exécutable** une ligne située **dans un bloc de code
fencé**, hors `echo` et `printf`, et hors prose entre accents graves. En cas de
doute, la ligne est classée « mention » : **le comptage sous-estime plutôt qu'il
ne surestime.** Cinq artefacts ont été écartés à ce titre, dont
`jetson-init-source` parce qu'il est épinglé.

### Le comptage ne sous-estime pas par oubli d'une autre forme

Balayage des autres formes de récupération distante, en bloc de code, sur les
344 : `curl | sh` **0**, `wget | sh` **0**, `pip install git+` **0**,
`gh repo clone` **0**, `uv`/`uvx` sur url **0**. Seuls apparaissent
`pip install <url>` (2) et `docker pull`/`run` (28) — dont un tirage d'image à
l'étiquette `latest`, mobile, analogue de la référence mobile d'un clone. Relevé
pour mémoire, **non instruit ici**.

### Ce que cette entrée n'établit pas

- **Que ces 22 exécutent le code récupéré.** Le recensement compte le **clone**.
  L'exécution du code cloné n'a été établie que par lecture de juge, sur la
  seule famille `i4h` ; elle n'a été vérifiée ni sur `deepstream`, ni sur
  `holoscan`, ni sur `nv-generate`, ni sur `nv-segment`.
- **Qu'ils soient dangereux.** Aucun juge ne les a lus. Ce qui est compté est
  une chaîne de caractères dans un bloc de code, pas un comportement mesuré.
- **Que le programme de certification ait tort.** Il peut tenir un dépôt de
  l'éditeur pour une source de confiance et accepter la référence mobile en
  connaissance de cause. Cette entrée ne tranche pas cette question ; elle
  établit le chiffre qui permet de la poser.
- **Que la règle lexicale soit exhaustive.** Un clone déclenché depuis un script
  embarqué, hors du `SKILL.md`, ne serait pas vu par ce recensement.
- **Pourquoi les quatre ne figurent plus au catalogue.** Voir ci-dessus.

---

## English — courtesy translation (the French text prevails)

### What was verified, and when

On 2026-09-09 at 19:20:47 UTC, the seven cases named by sealed entries 20 and 21
were checked against their source, in the enclave, read-only.

| case | artefact | at the time of the check | published verdict |
|---|---|---|---|
| `jev-0045` | `i4h-catheter-navigation-e2e` | **no longer listed in the catalogue** | — |
| `jev-0078` | `i4h-catheter-navigation-setup` | **no longer listed in the catalogue** | — |
| `jev-0079` | `i4h-catheter-navigation-viewport` | **no longer listed in the catalogue** | — |
| `jev-0080` | `i4h-catheter-navigation-render-drr` | **no longer listed in the catalogue** | — |
| `jev-0081` | `i4h-workflow-dataset-annotate` | present | `PASS` |
| `jev-0046` | `dynamo-recipe-runner` | present | `FAIL` |
| `jev-0064` | `tilegym-cutile-autotuning` | present | `FAIL` |

"No longer listed in the catalogue" is a statement of presence, not an
interpretation. It is established by four independent requests per artefact —
`SKILL.md`, `README.md`, `skill-card.md` and the repository content API all
return **HTTP 404** — while the `skills/` directory returns 200 and holds 345
entries. Neither a moved repository nor a service outage.

**The reason is not established.** Removal, renaming, consolidation,
deprecation, reorganisation: nothing in this check settles it, and this entry
does not settle it either. No cause is suggested here, and none should be read
between the lines.

### The census of the whole catalogue

The catalogue was acquired in a single request on 2026-09-09 at 19:24:06 UTC —
12,092,596 bytes, `sha256:52687939e61e07350cbd438d30fa3dcc6da04d3bb8c9fea8378561f74831eb61`
— and surveyed **offline in the enclave, with no artefact executed**.

**Denominator: 344 artefacts carrying a `SKILL.md`.** Published verdicts across
the whole catalogue: **333 `PASS`, 11 `FAIL`**.

| | |
|---|---|
| carrying `git clone` inside a code block | **24** |
| of which at least one clone **with no explicit reference** | **22** |
| published verdict of those 22 | **22 `PASS`, 0 `FAIL`** |

None of the 22 carries an explicit reference: no `--branch`, no `--tag`, no
commit, no subsequent `git checkout`. `--depth` was **not counted** as pinning —
it shortens history, it does not fix the revision.

Those 22 target **five distinct upstream repositories**:
`isaac-for-healthcare/i4h-workflows` (13, through an environment variable),
`NVIDIA-Medtech/NV-Generate-CTMR` (5), `NVIDIA-Medtech/NV-Segment-CTMR` (2),
`NVIDIA/DeepStream` (1), `nvidia-holoscan/holoscan-sdk` (1). It is therefore not
a quirk of one artefact family.

**One artefact in the same catalogue does carry an explicit reference**:
`jetson-init-source`, `git clone <url> -b <ref>`. The form exists in the
catalogue and was not used elsewhere.

### The counting rule, written before the results were read

A clone counts as **executable** when the line sits **inside a fenced code
block**, outside `echo` and `printf`, and outside prose between backticks. When
in doubt the line is classed as a "mention": **the count understates rather than
overstates.** Five artefacts were set aside on that basis, including
`jetson-init-source` because it is pinned.

### The count does not understate by missing another form

Sweep of other remote-fetch forms, inside code blocks, across the 344:
`curl | sh` **0**, `wget | sh` **0**, `pip install git+` **0**,
`gh repo clone` **0**, `uv`/`uvx` on a url **0**. Only `pip install <url>` (2)
and `docker pull`/`run` (28) appear — including one image pull at the `latest`
tag, mutable, the analogue of a clone's mutable reference. Recorded for the
record, **not investigated here**.

### What this entry does not establish

- **That those 22 execute the fetched code.** The census counts the **clone**.
  Execution of cloned code was established only by judge reading, on the `i4h`
  family alone; it was not verified on `deepstream`, `holoscan`, `nv-generate`
  or `nv-segment`.
- **That they are dangerous.** No judge read them. What is counted is a string
  inside a code block, not a measured behaviour.
- **That the certification programme is wrong.** It may hold a publisher-owned
  repository to be a trusted source and knowingly accept a mutable reference.
  This entry does not settle that question; it establishes the figure that makes
  it possible to ask it.
- **That the lexical rule is exhaustive.** A clone triggered from an embedded
  script, outside the `SKILL.md`, would not be seen by this census.
- **Why the four are no longer listed in the catalogue.** See above.

**Sources**

- .log/152-reverif-benchmark-2026-09-09.txt — les sept cas, requêtes et codes HTTP
- .log/153-recensement-nvidia-2026-09-09.txt — le recensement, règle de comptage et résultat
- registre, entrées 20 et 21 — les deux entrées scellées dont les cas sont ici re-vérifiés
- registre, entrée 23 — la réserve : le BENCHMARK.md de 45 fiches sur 48 n'est pas conservé au dépôt
- docs/enclave.md — limites de récupération ; exception de taille déclarée pour l'acquisition du catalogue
- https://github.com/NVIDIA/skills — le catalogue mesuré

```
empreinte du contenu  sha256:37461da1e438740babc7d60d844f6349816d53ce74002e4869560386f365fd60
empreinte             dc102ba05e5eb3371c79a2c14765097b0f89dc6ad63bde8dae0294bb81fa231f
empreinte précédente  3566980240afb57a789f1b7856f1e353032611a9cfa7b0f778f2b7a710c08ab1
```

---

## 26. Rectification de l'entrée 20 — deux faits ont changé après son sceau, le jour même : le régime de quatre de ses cas, et la présence de quatre de ses artefacts

**Date du fait** 2026-09-09 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### Pourquoi une entrée nouvelle

L'entrée 20 est **scellée**. Le registre est append-only : une entrée ne se
réécrit pas, et une entrée dont le contexte a bougé se rectifie par une entrée
suivante. Celle-ci ne touche ni son sceau, ni son empreinte de contenu, ni la
chaîne.

**L'entrée 20 n'est pas fausse.** Elle date une mesure, et c'est exactement ce
qu'un sceau garantit : que ce texte-là existait, inchangé, à cette date-là. Deux
choses ont changé **après** elle, le jour même, et un lecteur qui l'ouvrira plus
tard doit les connaître.

### Premier fait — le régime de quatre de ses cas

Le corps scellé de l'entrée 20 donne, cas par cas, le régime de verdict que la
fiche portait **au moment du sceau** :

| cas | régime au sceau |
|---|---|
| `jev-0045` | `divergent` |
| `jev-0078` | `sans objet` |
| `jev-0079` | `sans objet` |
| `jev-0080` | `sans objet` |
| `jev-0081` | `sans objet` |

Quelques heures plus tard, l'**entrée 23** a reclassé 48 fiches du régime
`sans objet` au régime `cas`, sous la règle du 2026-09-04 — dont ces quatre-là.
Leur `verdict_concordance` est désormais **`divergent`**, comme celui de
`jev-0045`.

Autrement dit : **les cinq cas de l'entrée 20 sont aujourd'hui tous au même
régime**, alors que son corps scellé en donne deux. Le sceau dit vrai pour sa
date ; il ne dit plus l'état d'aujourd'hui.

### Second fait — la présence de quatre de ses artefacts

Le contrôle du 2026-09-09 à 19:20:47 UTC, consigné à l'**entrée 25**, établit
que quatre des cinq artefacts nommés par l'entrée 20 — `jev-0045`, `jev-0078`,
`jev-0079`, `jev-0080` — **ne figurent plus au catalogue à cette date**. La
raison n'est pas établie et n'est pas supposée ici.

Un tiers qui voudrait aujourd'hui refaire la lecture de ces quatre cas **ne le
peut pas depuis la source**. Il le peut depuis le corpus, qui conserve leur
corps, mais c'est une copie datée du 2026-02-25 au 2026-09-04 selon les cas, et
non la source vivante.

### Ce que ces deux faits ne changent pas

- **Les verdicts des deux juges.** Ils ont été rendus sur un matériau conservé,
  en aveugle, sous un protocole pré-enregistré. Ils ne dépendent pas de l'état
  du catalogue aujourd'hui.
- **La règle de classe 3 tenait à la date du sceau.** Les cinq cas satisfaisaient
  les deux conditions — jugés sous la définition en vigueur, contrôlés par le
  second juge. Rien ici ne les défait.
- **Le sceau lui-même.** L'empreinte de contenu de l'entrée 20 et la chaîne sont
  inchangées et vérifiables.

### Ce que cette entrée établit, et rien de plus

Qu'**une entrée scellée fige un texte, pas un monde**. Le sceau garantit que
personne n'a retouché ce qui a été écrit ; il ne garantit pas que ce qui était
décrit soit encore là. C'est une propriété du dispositif, connue, et c'est la
première fois qu'elle se manifeste sur une entrée de ce registre. Elle méritait
d'être écrite le jour où elle se produit plutôt que découverte par un lecteur.

### Ce qu'elle n'établit pas

- Que l'entrée 20 doive être ouverte. Son ouverture reste une décision distincte,
  non prise.
- Que le reclassement de l'entrée 23 ait été une erreur, ni que le sceau ait été
  posé trop tôt. Les deux étaient justes à leur date.
- Pourquoi les quatre artefacts ne figurent plus au catalogue.

---

## English — courtesy translation (the French text prevails)

### Why a new entry

Entry 20 is **sealed**. The registry is append-only: an entry is not rewritten,
and an entry whose context has moved is rectified by a later entry. This one
touches neither its seal, nor its content hash, nor the chain.

**Entry 20 is not false.** It dates a measurement, and that is exactly what a
seal guarantees: that this text existed, unchanged, on that date. Two things
changed **after** it, on the same day, and a reader opening it later must know
them.

### First fact — the regime of four of its cases

The sealed body of entry 20 gives, case by case, the verdict regime the case
file carried **at the time of sealing**:

| case | regime at sealing |
|---|---|
| `jev-0045` | `divergent` |
| `jev-0078` | `sans objet` |
| `jev-0079` | `sans objet` |
| `jev-0080` | `sans objet` |
| `jev-0081` | `sans objet` |

A few hours later, **entry 23** reclassified 48 case files from regime
`sans objet` to regime `cas`, under the 2026-09-04 rule — including those four.
Their `verdict_concordance` is now **`divergent`**, like that of `jev-0045`.

In other words: **the five cases of entry 20 are today all under the same
regime**, while its sealed body records two. The seal tells the truth for its
date; it no longer tells today's state.

### Second fact — the presence of four of its artefacts

The check of 2026-09-09 at 19:20:47 UTC, recorded in **entry 25**, establishes
that four of the five artefacts named by entry 20 — `jev-0045`, `jev-0078`,
`jev-0079`, `jev-0080` — **are no longer listed in the catalogue at that date**.
The reason is not established and is not assumed here.

A third party wishing to redo the reading of those four cases today **cannot do
so from the source**. They can from the corpus, which retains their bodies, but
that is a copy dated between 2026-02-25 and 2026-09-04 depending on the case,
not the live source.

### What these two facts do not change

- **The two judges' verdicts.** They were returned on retained material, blind,
  under a pre-registered protocol. They do not depend on the state of the
  catalogue today.
- **The class-3 rule held at the date of sealing.** The five cases satisfied both
  conditions — judged under the definition in force, controlled by the second
  judge. Nothing here undoes that.
- **The seal itself.** Entry 20's content hash and the chain are unchanged and
  verifiable.

### What this entry establishes, and nothing more

That **a sealed entry freezes a text, not a world**. The seal guarantees that no
one retouched what was written; it does not guarantee that what was described is
still there. It is a known property of the device, and this is the first time it
shows on an entry of this registry. It deserved to be written the day it
happened rather than discovered by a reader.

### What it does not establish

- That entry 20 should be opened. Its opening remains a separate decision, not
  taken.
- That entry 23's reclassification was a mistake, or that the seal was set too
  early. Both were right on their date.
- Why the four artefacts are no longer listed in the catalogue.

**Sources**

- registre, entrée 20 — scellée, inchangée, empreinte et chaîne vérifiables
- registre, entrée 23 — le reclassement des 48 fiches, postérieur au sceau
- registre, entrée 25 — le contrôle de présence du 2026-09-09T19:20:47Z
- registre/README.md — « une entrée n'est jamais modifiée ; une entrée fausse se corrige par une entrée suivante »
- corpus/cases/jev-0045.md, jev-0078.md, jev-0079.md, jev-0080.md, jev-0081.md — verdict_concordance après reclassement

```
empreinte du contenu  sha256:657048e55f5b5fe9df22e8b2a2d2309e4a507b50841470062c272ba2728a3c46
empreinte             f22c5520d6b498930e233325d8f575e7412ffac5df0953e83f6e6cc002d23f5d
empreinte précédente  dc102ba05e5eb3371c79a2c14765097b0f89dc6ad63bde8dae0294bb81fa231f
```

---

## 27. Acte d'ouverture de l'entrée 3 — le signalement à l'éditeur de l'outil est publié, le sceau a fait son office

**Date du fait** 2026-09-10 — **type** `classement`

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### L'acte

L'**entrée 3** — classe 2, `juge_open_source`, scellée le 2026-09-09, fait daté
du 2026-09-08 — est **ouverte ce jour**. Sa classe est inchangée. Son corps et
son titre deviennent publics ; son empreinte de contenu et son empreinte de
chaîne, publiées depuis le sceau, permettent à quiconque de vérifier que le
texte publié aujourd'hui est exactement celui qui était figé alors.

### Ce qui déclenche l'ouverture

La règle qu'on s'est donnée est simple : **on ne publie pas le défaut d'un tiers
avant de l'avoir prévenu.** Le sceau de l'entrée 3 ne cachait pas un fait, il en
datait l'existence en attendant que l'éditeur soit averti.

L'éditeur est averti. Le signalement a été publié le 2026-09-10 à 11:31:25 UTC :

```
https://github.com/kuzivaai/SkillWatch/issues/40
```

Titre : *URL extraction captures a trailing brace from shell parameter
expansion*. Ouvert par le compte `mohamedmebarek-ops`. Le corps publié est
identique, octet pour octet, au texte relu et commité dans
`docs/disclosures/skillwatch-0.4.1-brace.md`.

### Ce qui a été vérifié avant l'envoi, et qui vaut pour l'entrée ouverte

Le 2026-09-10, avant publication, six points ont été contrôlés :

| | |
|---|---|
| reproduction | refaite avec `skillwatch 0.4.1` installé à neuf depuis PyPI dans un virtualenv vierge. Le bloc publié et la sortie réelle sont identiques ligne pour ligne — une ligne d'invite manquait au brouillon, elle a été ajoutée avant l'envoi |
| version | 0.4.1 est toujours la version courante ; aucune 0.4.2. Et la branche `main`, hors release, **porte encore le défaut** |
| ligne citée | `sha256` de la ligne citée et de la ligne installée : identiques |
| antériorité | les 39 issues et pull requests du dépôt, ouvertes et fermées, parcourues : **aucune** ne signalait ce défaut |
| forme | aucun vocabulaire de vulnérabilité, un seul outil nommé, aucune URL en signature |
| notre propre défaut | la phrase « we had it in our own, on the same character, and fixed it the same day » est vraie : `tools/extraire-references.py` exclut `}` et `{` depuis le commit `4d81ce1` du 2026-09-08 |

### Ce que cet acte n'établit pas

- **Rien sur la réponse de l'éditeur.** L'issue est ouverte ; elle peut être
  acceptée, corrigée, contestée ou ignorée. Cette entrée date l'envoi, pas son
  accueil.
- **Rien de plus que le corps de l'entrée 3**, qui est désormais lisible et se
  suffit. Il porte ses propres réserves.
- **Aucun autre sceau n'est levé.** Les entrées 20 et 21 restent scellées, et
  leur ouverture reste une décision distincte, non prise.

---

## English — courtesy translation (the French text prevails)

### The act

**Entry 3** — class 2, `juge_open_source`, sealed on 2026-09-09, fact dated
2026-09-08 — is **opened today**. Its class is unchanged. Its body and title
become public; its content hash and chain hash, published since sealing, let
anyone verify that the text published today is exactly the one frozen then.

### What triggers the opening

The rule we set ourselves is simple: **we do not publish a third party's defect
before notifying them.** Entry 3's seal was not hiding a fact, it was dating its
existence while the publisher was notified.

The publisher is notified. The report was published on 2026-09-10 at 11:31:25
UTC:

```
https://github.com/kuzivaai/SkillWatch/issues/40
```

Title: *URL extraction captures a trailing brace from shell parameter
expansion*. Opened by account `mohamedmebarek-ops`. The published body is
identical, byte for byte, to the text reviewed and committed in
`docs/disclosures/skillwatch-0.4.1-brace.md`.

### What was verified before sending, and which stands with the opened entry

On 2026-09-10, before publication, six points were checked:

| | |
|---|---|
| reproduction | redone with `skillwatch 0.4.1` freshly installed from PyPI in a clean virtualenv. The published block and the real output are identical line for line — one prompt line was missing from the draft and was added before sending |
| version | 0.4.1 is still the current version; no 0.4.2. And the `main` branch, outside any release, **still carries the defect** |
| quoted line | `sha256` of the quoted line and of the installed line: identical |
| priority | all 39 issues and pull requests of the repository, open and closed, were reviewed: **none** reported this defect |
| form | no vulnerability vocabulary, a single tool named, no URL in the signature |
| our own defect | the sentence "we had it in our own, on the same character, and fixed it the same day" is true: `tools/extraire-references.py` excludes `}` and `{` since commit `4d81ce1` of 2026-09-08 |

### What this act does not establish

- **Nothing about the publisher's response.** The issue is open; it may be
  accepted, fixed, disputed or ignored. This entry dates the sending, not its
  reception.
- **Nothing beyond entry 3's body**, which is now readable and stands on its
  own. It carries its own reservations.
- **No other seal is lifted.** Entries 20 and 21 remain sealed, and their
  opening remains a separate decision, not taken.

| entrée | classe | statut | scellée le | ouverte le |
|---|---|---|---|---|
| 3 | 2 (`juge_open_source`) | ouverte | 2026-09-09 | 2026-09-10 |

**Sources**

- https://github.com/kuzivaai/SkillWatch/issues/40 — le signalement publié
- docs/disclosures/skillwatch-0.4.1-brace.md — le texte relu et commité, identique au corps publié
- .log/156-verification-issue-skillwatch-2026-09-10.txt — les six contrôles avant envoi
- registre, entrée 3 — le fait scellé le 2026-09-09, ouvert par le présent acte
- registre/README.md — statuts, et la règle de classe 3 dont procède la discipline appliquée ici
- tools/extraire-references.py ligne 47, commit 4d81ce1 — notre propre correction du même défaut

```
empreinte du contenu  sha256:b1f3e0c4930d1ed74057b11408ec7055d431f49f95ce3f0ec08b9e46d93e287d
empreinte             018c6b6c891a7aa1609b7283c427bd44ea268f1721320aaa200ddd07f1d72aa4
empreinte précédente  f22c5520d6b498930e233325d8f575e7412ffac5df0953e83f6e6cc002d23f5d
```

---

## 28. SUBSTANTIEL — une décision de transparence appliquée dans le registre et silencieusement annulée dans deux sorties, par deux générateurs distincts

**Date du fait** 2026-09-10 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### La décision

Le 2026-09-10, une règle est posée : **les actes de classement sont publiés avec
leur corps**, comme toute entrée ouverte. La vue publique n'en donnait
auparavant que la date et l'empreinte de chaîne. Motif de la décision : un acte
de classement est une décision qui change ce qu'un lecteur peut voir, et la
cacher ferait de la mécanique d'ouverture et de scellement la seule zone
d'ombre du dispositif — celle qui touche à la transparence elle-même.

### Ce qui s'est passé ensuite, deux fois

La règle a été appliquée dans le registre. Elle a été **annulée dans deux
sorties**, chacune par un vestige de la règle antérieure resté en place :

| générateur | ce qui appliquait la règle | ce qui l'annulait |
|---|---|---|
| `site/build.py` | le flux `feed.xml` publiait le corps de l'acte | la page `index.html` le remplaçait par une phrase fixe héritée de l'ancienne règle |
| `tools/registre.py` | la section publiait le titre de l'acte | la table de tête y substituait la chaîne littérale « acte de classement » |

Deux sorties du **même générateur** se contredisaient, dans les deux cas. Le
premier défaut a été trouvé par la voie `site/` (commit `2858072`), le second
par la voie du banc une heure plus tard (commit `9631a30`).

### Ce que cela dit du dispositif, et qui est le vrai fait

**Aucun contrôle ne pouvait les voir.** Rien ne comparait les deux sorties d'un
même générateur, ni les deux vues d'un même registre. Les contrôles existants
portent sur les empreintes — ils vérifient qu'une entrée n'a pas bougé — et sur
les fuites — ils vérifient que le scellé ne sort pas. Aucun ne vérifie que **ce
qui sort dit la même chose partout**.

Les deux défauts sont nés d'un même geste : changer une règle, et laisser
survivre un chemin de code écrit pour l'ancienne. Ils ont vécu dans deux
générateurs tenus par **deux voies de travail qui ne se parlent pas**, et c'est
seulement parce que chacune a relu l'autre qu'ils ont été trouvés le jour même.

Ce n'est pas un défaut de rendu. C'est la démonstration qu'une décision de
transparence peut être **appliquée quelque part et silencieusement annulée
ailleurs**, dans le dispositif dont la transparence est le produit.

### Les deux réserves qui bornent ce fait

**Aucun lecteur n'a été trompé, puisque la page n'a jamais été publiée.** Les
deux défauts ont vécu dans un rendu local, entre la décision du matin et sa
correction du même jour. On aurait publié faux ; on ne l'a pas fait. Ce qui est
rapporté ici est un défaut trouvé avant publication, pas une publication
rectifiée.

**Ce qui manque est un contrôle, pas une correction.** Les deux corrections sont
faites et vérifiées : le corps des actes est publié dans les trois sorties, et
sur les 27 entrées aucun écart ne subsiste entre le titre de la table de tête et
celui de la section. Mais rien n'empêche le même geste de reproduire le même
défaut demain, sur une autre règle. Le contrôle qui l'attraperait — comparer,
pour chaque entrée, ce que disent `index.html`, `feed.xml` et
`registre-public.md`, et arrêter la régénération sur une divergence de
**contenu**, pas seulement d'empreinte — **n'existe pas**. Il est inscrit comme
**prérequis à la bascule publique** dans `docs/jalons-a-venir.md`, et non comme
amélioration ultérieure : c'est le seul contrôle qui aurait attrapé ces deux
défauts.

### Ce que cette entrée n'établit pas

- **Qu'aucun autre vestige ne subsiste.** Deux ont été trouvés parce que deux
  personnes ont regardé. Rien ne dit qu'un troisième n'attend pas dans un
  chemin de sortie que personne n'a relu ce jour-là.
- **Que le contrôle manquant suffirait.** Il attraperait ces deux défauts-ci.
  Il ne dit rien des divergences qu'une comparaison de contenu ne verrait pas —
  une mise en forme qui change le sens, par exemple.
- **Qu'un lecteur ait subi quoi que ce soit.** Voir la première réserve.
- **Que la faute revienne à l'une des deux voies.** Chacune a écrit son
  vestige, chacune a trouvé celui de l'autre. Le partage du dépôt en voies qui
  ne se parlent pas est ce qui a créé le défaut **et** ce qui l'a révélé ; cette
  entrée ne tranche pas si c'est un bon partage.

---

## English — courtesy translation (the French text prevails)

### The decision

On 2026-09-10 a rule was set: **classification acts are published with their
body**, like any open entry. The public view previously gave only their date and
chain hash. The reason: a classification act is a decision that changes what a
reader can see, and hiding it would make the sealing-and-opening machinery the
only shadow in the device — the very part that concerns transparency itself.

### What happened next, twice

The rule was applied in the registry. It was **cancelled in two outputs**, each
by a remnant of the former rule left in place:

| generator | what applied the rule | what cancelled it |
|---|---|---|
| `site/build.py` | the `feed.xml` feed published the act's body | the `index.html` page replaced it with a fixed sentence inherited from the old rule |
| `tools/registre.py` | the section published the act's title | the summary table substituted the literal string "acte de classement" |

In both cases, two outputs of the **same generator** contradicted each other. The
first defect was found by the `site/` lane (commit `2858072`), the second by the
bench lane an hour later (commit `9631a30`).

### What this says about the device, and what the real fact is

**No control could have seen them.** Nothing compared the two outputs of one
generator, nor the two views of one registry. Existing controls cover hashes —
they check that an entry has not moved — and leaks — they check that sealed
content does not escape. None checks that **what goes out says the same thing
everywhere**.

Both defects came from the same gesture: change a rule, and leave alive a code
path written for the old one. They lived in two generators held by **two working
lanes that do not talk to each other**, and it is only because each reviewed the
other's that they were found the same day.

This is not a rendering bug. It shows that a transparency decision can be
**applied somewhere and silently cancelled elsewhere**, inside the very device
whose product is transparency.

### The two reservations that bound this fact

**No reader was misled, because the page was never published.** Both defects
lived in a local render, between the morning's decision and its correction the
same day. We would have published something false; we did not. What is reported
here is a defect found before publication, not a publication corrected after.

**What is missing is a control, not a correction.** Both corrections are made and
verified: the acts' bodies are published in all three outputs, and across the 27
entries no gap remains between the summary-table title and the section title. But
nothing prevents the same gesture from reproducing the same defect tomorrow, on
another rule. The control that would catch it — comparing, for each entry, what
`index.html`, `feed.xml` and `registre-public.md` say, and stopping regeneration
on a divergence of **content**, not merely of hash — **does not exist**. It is
recorded as a **prerequisite to the public switch** in `docs/jalons-a-venir.md`,
not as a later improvement: it is the only control that would have caught these
two defects.

### What this entry does not establish

- **That no other remnant survives.** Two were found because two people looked.
  Nothing says a third is not waiting in an output path nobody reviewed that day.
- **That the missing control would suffice.** It would catch these two. It says
  nothing about divergences a content comparison would not see — formatting that
  changes meaning, for instance.
- **That any reader suffered anything.** See the first reservation.
- **That the fault lies with either lane.** Each wrote its own remnant, each
  found the other's. Splitting the repository into lanes that do not talk is what
  created the defect **and** what revealed it; this entry does not settle whether
  that is a good split.

**Sources**

- registre/README.md — « Actes de classement — publiés en entier, règle du 2026-09-10 »
- commit 8b7e180 — la règle appliquée côté registre
- commit 2858072 — le vestige trouvé et corrigé dans site/build.py, voie site/
- commit 9631a30 — le vestige trouvé et corrigé dans tools/registre.py, voie du banc
- docs/jalons-a-venir.md — le contrôle manquant, prérequis à la bascule publique

```
empreinte du contenu  sha256:dd2644e032523bad055902972b8c5069873ca4553287b45d96469e2e3c0cbf87
empreinte             252acbc334ae9f8376b0d6450912391e5d623307636e1a9a7581999ee377c972
empreinte précédente  018c6b6c891a7aa1609b7283c427bd44ea268f1721320aaa200ddd07f1d72aa4
```

---

## 29. Le registre est public — bascule du 2026-09-11, 28 entrées servies sur jevons.fr

**Date du fait** 2026-09-11 — **type** `observation` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### Le fait

Le **2026-09-11**, le registre est devenu public. Le dépôt `jevons-lab/jevons`
est passé en visibilité publique à **06:58:23 UTC**, GitHub Pages y est activé
— source `main`, racine —, et le domaine `jevons.fr` sert les **28 entrées**
que portait le registre à cette date.

Le commit publié est **`1c83e4b`**, du 2026-09-11 à 05:52:32 UTC : 65 fichiers,
l'export produit par `tools/preparer-export-public.py` sous ses contrôles C1 à
C6 et le contrôle de concordance des sorties.

### Ce que la bascule publie, et ce qu'elle ne publie pas

**Publié** : les entrées ouvertes en clair, titre, corps, sources et empreintes ;
la sonde et ses 42 notices ; les rapports de la sonde ; `references.md` ; la
règle de publication du registre.

**Non publié** : le corpus, ses corps et ses annonces ; les sorties brutes des
scanners ; `registre.jsonl`, la source chaînée ; le journal de travail ; et le
**corps des entrées scellées**. Les entrées **20 et 21** restent réduites à leur
sceau — date, classe, empreinte de contenu, empreinte de chaîne, rien d'autre.

Le dépôt publié est **neuf, sans historique** : un commit, reconstruit depuis
`export-public/`. Le dépôt de travail ne devient jamais public tel quel, parce
que son historique garde ce qu'une correction du présent ne retire pas.

### Ce que la bascule engage

**Une entrée ouverte l'est pour de bon.** Jusqu'ici, « ouverte » désignait un
statut dans un fichier local ; désormais un tiers peut lire, recalculer et
citer. La règle du registre — une entrée n'est jamais modifiée, une entrée
fausse se corrige par une entrée suivante — cesse d'être une discipline interne
et devient une promesse tenue devant quelqu'un.

**Les deux sceaux engagent davantage.** Les entrées 20 et 21 mettent en cause un
tiers qui ne peut ni voir le contenu scellé, ni le contester. Leurs empreintes
sont maintenant publiques et datées : le jour de leur ouverture, n'importe qui
pourra vérifier que le texte publié est bien celui qui était figé aujourd'hui.
C'est la seule chose qu'un registre apporte qu'une publication ordinaire
n'apporte pas.

### Ce que cette entrée n'établit pas

- **Que le registre soit lu.** Une adresse qui répond n'est pas un lecteur.
- **Que ce qui est publié soit juste.** La bascule publie des entrées qui
  portent chacune leurs réserves, y compris celles qui rapportent nos propres
  défauts — l'entrée 1 est une rétractation, l'entrée 28 un défaut de notre
  dispositif trouvé avant publication. Rendre public ne valide rien.
- **Qu'aucune entrée ne devra être rectifiée.** Le registre est fait pour cela,
  et l'aura probablement à faire.
- **Rien sur le contenu des entrées 20 et 21**, qui restent scellées.

### Une limite d'instrument, notée le jour même

Depuis l'enclave, `https://jevons.fr` **ne répond pas** — code 000, échec de
connexion, tandis que `http://jevons.fr` rend 200 et sert les 28 entrées. Le
fondateur constate au même moment, dans son navigateur, que l'adresse s'affiche
en HTTPS avec le cadenas et sans avertissement.

L'écart est donc **du côté de l'enclave** — propagation ou restriction réseau —
et non du site. Il est consigné ici parce qu'il change ce qu'un contrôle fait
depuis l'enclave peut conclure : **l'absence de réponse y vaut absence de
preuve, pas preuve d'absence.** À revérifier ; si l'écart persiste alors qu'un
navigateur passe, c'est une limite de l'enclave à documenter, pas un défaut du
site.

---

## English — courtesy translation (the French text prevails)

### The fact

On **2026-09-11** the register became public. The `jevons-lab/jevons` repository
switched to public visibility at **06:58:23 UTC**, GitHub Pages is enabled on it
— source `main`, root — and the `jevons.fr` domain serves the **28 entries** the
register held on that date.

The published commit is **`1c83e4b`**, of 2026-09-11 at 05:52:32 UTC: 65 files,
the export produced by `tools/preparer-export-public.py` under controls C1 to C6
and the output concordance control.

### What the switch publishes, and what it does not

**Published**: open entries in full — title, body, sources and hashes; the probe
and its 42 notices; the probe's reports; `references.md`; the register's
publication rule.

**Not published**: the corpus, its bodies and announcements; raw scanner
outputs; `registre.jsonl`, the chained source; the working journal; and the
**body of sealed entries**. Entries **20 and 21** remain reduced to their seal —
date, class, content hash, chain hash, nothing else.

The published repository is **new, without history**: one commit, rebuilt from
`export-public/`. The working repository never becomes public as it stands,
because its history keeps what a correction of the present does not remove.

### What the switch commits us to

**An open entry is open for good.** Until now "open" described a status in a
local file; from now on a third party can read, recompute and cite. The
register's rule — an entry is never modified, a false entry is corrected by a
later entry — stops being internal discipline and becomes a promise kept before
someone.

**The two seals commit us further.** Entries 20 and 21 implicate a third party
who can neither see the sealed content nor contest it. Their hashes are now
public and dated: on the day they are opened, anyone will be able to verify that
the published text is the one frozen today. That is the only thing a register
offers that ordinary publication does not.

### What this entry does not establish

- **That the register is read.** An address that answers is not a reader.
- **That what is published is right.** The switch publishes entries each
  carrying their own reservations, including those reporting our own defects —
  entry 1 is a retraction, entry 28 a defect of our own device found before
  publication. Making something public validates nothing.
- **That no entry will need rectifying.** The register exists for that, and will
  probably have to.
- **Anything about the content of entries 20 and 21**, which remain sealed.

### An instrument limit, noted the same day

From the enclave, `https://jevons.fr` **does not answer** — code 000, connection
failure — while `http://jevons.fr` returns 200 and serves the 28 entries. At the
same moment the founder observes, in his browser, that the address displays over
HTTPS with the padlock and no security warning.

The gap is therefore **on the enclave's side** — propagation or network
restriction — not the site's. It is recorded here because it changes what a
check made from the enclave can conclude: **absence of an answer there is
absence of evidence, not evidence of absence.** To be re-checked; if the gap
persists while a browser succeeds, it is an enclave limit to document, not a
site defect.

**Sources**

- https://jevons.fr — le registre public
- https://github.com/jevons-lab/jevons — le dépôt publié, un commit, sans historique
- commit 1c83e4b du 2026-09-11T05:52:32Z — 65 fichiers
- registre/README.md — règle de publication, statuts, règle propre à la classe 3
- tools/preparer-export-public.py — contrôles C1 à C6 et concordance des sorties
- site/JOURNAL.md — procédure de publication et ses gardes

```
empreinte du contenu  sha256:52abfbe806dc7df47ebde7e5ef81981cf87d7c545b13e8067179769b2d365229
empreinte             4237580bf1652078c2d29bfec9a0bd3e4faa59a591d7aa4f48a8653ccaea6ca4
empreinte précédente  252acbc334ae9f8376b0d6450912391e5d623307636e1a9a7581999ee377c972
```

---

## 30. Rectification de l'entrée 29 — la cause de l'écart HTTPS n'était ni la propagation ni le réseau, mais l'horloge de notre propre enclave

**Date du fait** 2026-09-11 — **type** `rectification` — **classe** 1 `nous` — **statut** ouverte

*(français ci-dessous, English below — **le français fait foi**)*

---

## Français — texte de référence

### Ce que l'entrée 29 dit, et qui est faux

L'entrée 29, écrite ce matin, consigne qu'un contrôle depuis l'enclave trouve
`https://jevons.fr` sans réponse alors qu'un navigateur l'affiche avec le
cadenas, et attribue l'écart à « **propagation ou restriction réseau** ».

**Ce n'était ni l'une ni l'autre.** La cause est l'**horloge de l'enclave**.

L'entrée 29 n'est pas réécrite : le registre est append-only. Ce qu'elle dit de
juste tient — l'écart était du côté de l'enclave et non du site, et elle
annonçait une re-vérification. C'est la cause qu'elle nomme qui est fausse, et
c'est cette entrée-ci qui la corrige.

### Les chiffres

| | |
|---|---|
| horloge de l'enclave au moment du contrôle | `2026-09-10T16:33:44Z` |
| horloge de l'hôte, à la même minute | `2026-09-11T07:27:18Z` |
| écart relevé par `chronyc` | **53 614 s — 14 h 53** |
| certificat servi, `notBefore` | `Sep 11 06:03:31 2026 GMT` |
| certificat servi, `notAfter` | `Dec 10 06:03:30 2026 GMT` |
| sujet | `CN=jevons.fr` |
| depuis l'enclave | `000`, échec de connexion, 0 octet |
| **depuis l'hôte, même minute** | **`200`, 192 351 octets, vérification TLS réussie** |

Message exact rendu par `openssl s_client` depuis l'enclave :

```
verify error:num=9: certificate is not yet valid
```

L'enclave se croyait **quinze heures avant** l'émission du certificat. Pour
elle, il n'existait pas encore.

### La preuve, faite en ne changeant qu'une chose

```
avant  makestep :  écart 53 561 s   https -> 000
après  makestep :  écart 0,000 s    https -> 200, 192 351 octets, TLS 0, 28 entrées
```

Même URL, même enclave, même réseau, même minute. **Seule l'horloge a changé.**

### Pourquoi ce fait vaut d'être publié

**Un contrôle a rendu un faux négatif à cause de l'instrument, pas de l'objet
mesuré.** C'est exactement ce que ce banc mesure chez les autres — un outil qui
rend un verdict sur la forme de ce qu'il lit plutôt que sur ce qui est —, trouvé
chez nous, sur notre propre chaîne de vérification.

Lu trop vite, le relevé disait « le site ne répond pas en HTTPS ». Il disait en
réalité « notre enclave ne sait pas quel jour on est ». Un instrument qui se
trompe d'époque juge une pièce qu'il n'a pas vue.

### La portée, plus large que ce cas

**Toute vérification TLS d'une ressource récemment publiée, faite depuis
l'enclave sans `makestep` préalable, peut rendre un échec qui n'en est pas un.**
Plus le certificat est récent, plus la fenêtre d'erreur est grande. Cela touche
le contrôle des références externes, la re-vérification quotidienne, et tout
contrôle d'une page qu'on vient de mettre en ligne.

La règle en découle et est écrite dans `docs/enclave.md` : `makestep` **avant
toute vérification TLS**, au même titre qu'avant une passe de mesure ; et devant
un `000` sur une ressource récente, **relever l'écart d'horloge avant de
conclure quoi que ce soit sur la ressource**.

### Ce que cette entrée n'établit pas

- **Qu'aucune mesure antérieure n'ait été touchée.** Les passes de mesure
  portaient `makestep` en tête depuis le passage 5, et les contrôles de
  références vérifient un code HTTP sans exiger TLS. Mais **je n'ai pas rejoué
  l'historique** pour le prouver, et je ne l'affirme donc pas.
- **Qu'un `000` soit toujours une erreur d'horloge.** Il peut être un vrai
  échec. Ce qui est établi est qu'il faut vérifier l'instrument d'abord :
  **l'absence de réponse depuis l'enclave vaut absence de preuve, pas preuve
  d'absence.**
- **Rien sur le site.** `jevons.fr` répondait correctement pendant tout
  l'épisode.

---

## English — courtesy translation (the French text prevails)

### What entry 29 says, and what is wrong in it

Entry 29, written this morning, records that a check from the enclave finds
`https://jevons.fr` unresponsive while a browser displays it with the padlock,
and attributes the gap to "**propagation or network restriction**".

**It was neither.** The cause is the **enclave's clock**.

Entry 29 is not rewritten: the register is append-only. What it gets right
stands — the gap was on the enclave's side and not the site's, and it announced
a re-check. It is the cause it names that is wrong, and this entry corrects it.

### The figures

| | |
|---|---|
| enclave clock at the time of the check | `2026-09-10T16:33:44Z` |
| host clock, same minute | `2026-09-11T07:27:18Z` |
| offset reported by `chronyc` | **53,614 s — 14 h 53** |
| served certificate, `notBefore` | `Sep 11 06:03:31 2026 GMT` |
| served certificate, `notAfter` | `Dec 10 06:03:30 2026 GMT` |
| subject | `CN=jevons.fr` |
| from the enclave | `000`, connection failure, 0 bytes |
| **from the host, same minute** | **`200`, 192,351 bytes, TLS verification successful** |

Exact message returned by `openssl s_client` from the enclave:

```
verify error:num=9: certificate is not yet valid
```

The enclave believed itself to be **fifteen hours before** the certificate was
issued. As far as it was concerned, the certificate did not yet exist.

### The proof, made by changing one thing only

```
before makestep :  offset 53,561 s   https -> 000
after  makestep :  offset 0.000 s    https -> 200, 192,351 bytes, TLS 0, 28 entries
```

Same URL, same enclave, same network, same minute. **Only the clock changed.**

### Why this fact is worth publishing

**A check returned a false negative because of the instrument, not the object
measured.** That is exactly what this bench measures in others — a tool
returning a verdict on the shape of what it reads rather than on what is there —
found in ourselves, on our own verification chain.

Read quickly, the reading said "the site does not answer over HTTPS". What it
actually said was "our enclave does not know what day it is". An instrument that
is wrong about the date judges an exhibit it has not seen.

### The scope, wider than this case

**Any TLS verification of a recently published resource, made from the enclave
without a prior `makestep`, may return a failure that is not one.** The more
recent the certificate, the wider the error window. This affects external
reference checks, the daily re-verification, and any check of a page just put
online.

The rule follows and is written in `docs/enclave.md`: `makestep` **before any
TLS verification**, just as before a measurement pass; and faced with a `000` on
a recent resource, **record the clock offset before concluding anything about
the resource**.

### What this entry does not establish

- **That no earlier measurement was affected.** Measurement passes have carried
  `makestep` at their head since pass 5, and reference checks verify an HTTP code
  without requiring TLS. But **I have not replayed the history** to prove it, and
  so I do not assert it.
- **That a `000` is always a clock error.** It can be a real failure. What is
  established is that the instrument must be checked first: **absence of an
  answer from the enclave is absence of evidence, not evidence of absence.**
- **Anything about the site.** `jevons.fr` was answering correctly throughout
  the episode.

**Sources**

- registre, entrée 29 — la bascule publique, et la cause erronée qu'elle nomme
- docs/enclave.md — « Une horloge en retard invalide la vérification TLS (2026-09-11) »
- docs/enclave.md — « Horloge — client NTP installé le 2026-09-08 », et le makestep en tête de passe depuis le passage 5
- https://jevons.fr — la ressource contrôlée, servie correctement pendant tout l'épisode

```
empreinte du contenu  sha256:a3f957910d5f905dd4df1f7af1e186025afbe334aa0c60b4c82df3b235e1da6a
empreinte             deef30a194d926f2570707a4c584611c44942e86066beee5e688f0cc583e9214
empreinte précédente  4237580bf1652078c2d29bfec9a0bd3e4faa59a591d7aa4f48a8653ccaea6ca4
```

