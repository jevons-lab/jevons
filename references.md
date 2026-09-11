# Références externes

**JEVONS — https://github.com/jevons-lab**

Un fait externe cité quelque part dans ce dépôt, une ligne. Pour chacun :
**l'URL**, la **date de consultation**, et la **phrase exacte ou le chiffre
repris**. Sans commentaire, sans interprétation, sans conclusion tirée.

Toutes les consultations sont faites **dans l'enclave**, sous les limites du
2026-09-08 (`docs/enclave.md`) : 5 Mo, 20 s, 5 redirections, `User-Agent` fixe,
aucune exécution, aucun rendu.

Les URL de tiers sont **désamorcées** (`hxxp`, `[.]`) comme partout ailleurs.
Celles du projet lui-même ne le sont pas : elles ne sont pas des cibles
mesurées.

Un fait dont l'URL n'a pas été consultée est **marqué comme tel** et ne doit
pas être cité comme établi.

---

## 1. Adversa — huit scanners de skills contournés

| | |
|---|---|
| URL | `https://adversa.ai/blog/agent-skill-scanners-bypass-eight-tested/` |
| titre | Agent Skills security: 8 skill scanners bypassed |
| date de publication | 2026-07-30T18:45:00Z (`article:published_time`) |
| date de modification | 2026-08-11T00:00:00Z (`dateModified`) |
| consulté le | **2026-09-09**, HTTP 200, 160 385 octets |

**Chiffre repris — les 53 cellules sur 77**, cité par `juges.README.md` :

> Full method, per-scanner detection techniques, build provenance and flags are
> in the appendix, along with a section we would rather not have had to write:
> our first pass predictions from reading source were wrong in 53 of 77
> comparable cells, in both directions at once. Any coverage claim in this
> domain that was reasoned from source and not executed should be treated as a
> hypothesis. Ours were.

**Liste des scanners, note 7 de la page** :

> 7: Cisco, NVIDIA SkillSpector, claude-skill-antivirus, huifer,
> ai-skill-scanner, mondoo skillcheck, hackmyagent

Sept sont nommés. Le huitième n'est pas nommé dans cette note ; la page écrit
par ailleurs, à son sujet :

> is omitted: we build it, and including it would turn a survey of the field
> into a comparison.

**Dépôts cités par la page**, tels qu'ils y figurent :

> cisco-ai-defense/skill-scanner
> claude-world/claude-skill-antivirus
> huifer/skill-security-scan
> suchithnarayan/ai-skill-scanner
> opena2a-org/hackmyagent

**Version de `hackmyagent`** :

> hackmyagent a prior unmodified v0.25.0 install

> v0.25.0; the OASB leaderboard entry is v0.23.8

**Phrase d'ouverture** :

> We ran eight open source AI skill scanners against real attacks, including
> the current benchmark leader. A malicious skill got past all eight: six
> through a bypass, one because it inspects almost nothing, one because the
> file can instruct it.

---

## 2. Trail of Bits — The sorry state of skill distribution

| | |
|---|---|
| URL | `https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/` |
| auteur | Samuel Judson |
| date de publication | 2026-06-03T07:00:00-04:00 (`article:published_time`) |
| consulté le | **2026-09-09**, HTTP 200, 47 937 octets |

**Phrase reprise** :

> These were not advanced attacks: it took us less than an hour to conceive and
> implement three of the four malicious skills in

**Périmètre des scanners testés, tel qu'écrit** :

> with scanners from Gen, Socket, and Snyk, and OpenClaw

> scanning works through integration with three external services: Gen Agent
> Trust Hub, Socket, and Snyk.

**Exception relevée par la page elle-même** :

> Note that finding the precise wording and formulation here to trick the
> scanner did take some trial and error; this was our only attack that took
> multiple hours to implement.

Quatre artefacts du corpus viennent du dépôt public associé,
`github.com/trailofbits/overtly-malicious-skills` : `jev-0016` à `jev-0019`,
URL exactes dans leurs fiches.

---

## 3. OWASP — Agentic Skills Top 10 (AST10)

| | |
|---|---|
| URL | `https://owasp.org/www-project-agentic-skills-top-10/` |
| titre de la page | OWASP Agentic Skills Top 10 (AST10) |
| consulté le | **2026-09-09**, HTTP 200, 141 670 octets |

**Levée d'ambiguïté, sur pièce.** `AST10` désigne **deux choses** sur cette page :
l'abréviation du **projet** — « OWASP Agentic Skills Top 10 (AST10) » — et le
**dixième risque** de sa table, « Cross-Platform Reuse ». Les deux emplois
coexistent dans le texte.

**Table des dix risques, recopiée telle quelle** (colonnes `#`, `Risk`,
`Severity`, `Key Mitigation`, `Real-World Evidence`) :

| # | Risk | Severity | Key Mitigation | Real-World Evidence |
|---|---|---|---|---|
| AST01 | Malicious Skills | Critical | Merkle root signing, registry scanning | ClawHavoc (1,184 skills), ToxicSkills (76 payloads) |
| AST02 | Supply Chain Compromise | Critical | Registry transparency, provenance tracking | ClawHub collapse, Claude Code CVE-2025-59536 |
| AST03 | Over-Privileged Skills | High | Least-privilege manifests, schema validation | 280+ credential-leaking skills (Snyk, Feb 2026) |
| AST04 | Insecure Metadata | High | Static analysis, safe parsers, sandboxed loading | Fake "Google" skill impersonation; YAML payload delivery in SKILL.md |
| AST05 | Untrusted External Instructions | High | Source inventory, content pinning, continuous rescanning | Air PoC bypassed all scanners; 26,000 agents at risk |
| AST06 | Weak Isolation | High | Containerization, Docker sandboxing | OpenClaw host-mode execution, 135K exposed instances |
| AST07 | Update Drift | Medium | Immutable pinning, hash verification | ClawJacked (CVE-2026-28363), patch-lag exploitation |
| AST08 | Poor Scanning | Medium | Semantic + behavioral multi-tool pipeline | Pattern-matcher bypass via natural-language injection |
| AST09 | No Governance | Medium | Skill inventories, agentic identity controls | 53K exposed instances with no SOC visibility |
| AST10 | Cross-Platform Reuse | Medium | Universal YAML format | Malicious skills ported across ClawHub, skills.sh |

**Les trois lignes reprises dans `juges.yaml`, verbatim :**

- `AST05 | Untrusted External Instructions | High | Source inventory, content pinning, continuous rescanning`
- `AST07 | Update Drift | Medium | Immutable pinning, hash verification`
- `AST08 | Poor Scanning | Medium | Semantic + behavioral multi-tool pipeline`

**Direction du projet, section « Leadership and Governance », recopiée :**

> Project Lead
> Ken Huang
>
> Co-Leads
> Hammad Atta
> Fabio Cerullo
> Aonan Guan
> Bhavya Gupta
> Niv Hoffman
> Iftach Orr
> Akram Sheriff

Sept noms sous « Co-Leads ». La liste des rôles individuels de la page porte
`Co-Lead, Agentic Skills Top 10` pour six d'entre eux — Hammad Atta, Fabio
Cerullo, Aonan Guan, Bhavya Gupta, Iftach Orr, Akram Sheriff.

**Niv Hoffman : listé sous « Co-Leads », mention de rôle absente.** Rien de
plus n'est établi ici.

**Autre phrase relevée** :

> No comprehensive security framework or dedicated guidance for agent skills
> existed before this project. That gap is what AST10 addresses.

---

## 4. OWASP — page « Skill Scanner Integration »

| | |
|---|---|
| URL | `https://owasp.org/www-project-agentic-skills-top-10/skill-scanner-integration` |
| titre de la page | Skill Scanner Integration \| OWASP Foundation |
| consulté le | **2026-09-09**, HTTP 200, 133 337 octets |

**SkillSpector et SARIF — retrouvé.** La page nomme SkillSpector **« open
source, recommended »**, et non « scanner de référence ». Formule exacte :

> NVIDIA SkillSpector (open source, recommended)

C'est cette formule qui est employée partout dans le dépôt à son sujet.

et écrit :

> Because SkillSpector emits SARIF v2.1.0, findings surface in the GitHub

Commandes citées par la page :

> skillspector scan ./skills --no-llm --format sarif --output skillspector.sarif

**Composition de plusieurs scanners en un verdict, sans re-scan — retrouvé,
verbatim :**

> No single scanner covers every AST10 risk: a drift detector flags that a
> skill's capability surface changed, a static content scanner flags hostile
> patterns, and an agentic-threat-rule engine flags behavioral exploits. When
> several scanners run over the same skill, their findings should compose into
> one verdict without re-scanning or manual correlation.

**Statut du scanner OWASP — retrouvé, dans la source ET dans le rendu.**

Source Markdown, `skill-scanner-integration.md`, **ligne 86**, section
« OWASP AST10 Scanner Status » :

> An OWASP-maintained `@owasp/ast10-scanner` package is not currently published.
> Until one exists, use the open-source scanners listed above and map their
> findings to the AST01-AST10 taxonomy in reports and CI output.

| | |
|---|---|
| URL de la source, telle que demandée | `https://github.com/OWASP/www-project-agentic-skills-top-10/blob/main/skill-scanner-integration.md` — HTTP 200, 451 479 octets |
| URL du contenu brut, d'où la ligne est citée | `https://raw.githubusercontent.com/OWASP/www-project-agentic-skills-top-10/main/skill-scanner-integration.md` — HTTP 200, 14 461 octets |
| consultées le | **2026-09-09** |

La même phrase figure **dans le rendu** `owasp.org` consulté au début de ce §4,
sous le même titre de section :

> OWASP AST10 Scanner Status
>
> An OWASP-maintained @owasp/ast10-scanner package is not currently published.
> Until one exists, use the open-source scanners listed above and map their
> findings to the AST01-AST10 taxonomy in reports and CI output.

Le rendu perd les apostrophes inverses autour du nom de paquet ; le texte est
identique par ailleurs.

**Correction d'un écart annoncé à tort le 2026-09-09.** Une première lecture de
ce fichier concluait que la phrase n'était **pas** dans la page. C'était **faux,
et le défaut était dans ma méthode d'extraction** : je remplaçais chaque balise
HTML par un saut de ligne, ce qui coupait la phrase à l'élément `<code>` qui
porte `@owasp/ast10-scanner`, puis je cherchais des motifs sur des lignes
entières. Aucune ligne ne portait la phrase complète, donc rien ne
correspondait. Le pied de page « OWASP does not endorse or recommend commercial
products or services » — qui est le pied de page standard du site — avait alors
été présenté comme la seule phrase approchante. Il reste ci-dessous, à sa place,
comme pied de page et non comme énoncé sur les scanners.

**Pied de page standard du site**, pour mémoire :

> OWASP does not endorse or recommend commercial products or services, allowing
> our community to remain vendor neutral with the collective wisdom of the best
> minds in software security worldwide. Copyright 2026, OWASP Foundation, Inc.

---

## 5. OWASP — dépôt source des deux pages

| | |
|---|---|
| URL demandée | `https://github.com/OWASP/www-project-agentic-skills-top-10` |
| consulté le | **2026-09-09**, HTTP 200, 660 328 octets |

**Écart — le HTML consulté ne porte aucun SHA de commit.** GitHub sert à ce
`User-Agent` une page dont le contenu est construit par script ; la recherche
d'un motif `commit/<40 hex>` ou `"oid"` n'y trouve rien. **Aucun épinglage n'a
donc pu être relevé sur la page consultée.**

L'épinglage ci-dessous vient d'une **autre source, l'API GitHub**, interrogée le
même jour :

| | |
|---|---|
| URL | `https://api.github.com/repos/OWASP/www-project-agentic-skills-top-10/commits?per_page=1` |
| consulté le | **2026-09-09** |
| commit | `d6f7d7d0de314f52a83a85d1828e06ab096e595c` |
| date du commit | 2026-08-12T16:27:33Z |
| message | `Replace whitepaper PDF and cover with updated version` |

**Épinglage : SHA via API, non prouvé pour le rendu.** C'est le HEAD de la
branche par défaut au moment de la consultation. Il **ne prouve pas** que les
pages rendues aux §3 et §4 l'ont été depuis ce commit : rien dans les pages ne
déclare la révision dont elles sont issues. Toute citation de cet épinglage doit
porter la mention **« SHA via API, non prouvé pour le rendu »**.

---

## 6. SkillWatch 0.4.1

| | |
|---|---|
| URL demandée | `https://pypi.org/project/skillwatch/` |
| consulté le | **2026-09-09**, HTTP 200, 3 038 octets |

**Écart — la page projet n'a pas été servie.** Le corps rendu est une page
anti-robot, titre `Client Challenge`, sans aucune donnée du paquet. Le code 200
ne signifie pas ici que la page demandée a été obtenue.

Les faits ci-dessous viennent de l'**API JSON de PyPI**, servie normalement :

| | |
|---|---|
| URL | `https://pypi.org/pypi/skillwatch/json` |
| consulté le | **2026-09-08** puis **2026-09-09**, HTTP 200, 49 908 octets |

| champ | valeur exacte |
|---|---|
| `info.version` | `0.4.1` |
| `info.author` | `Kuziva Muzondo` |
| `info.license` | `null` |
| `info.license_expression` | `Apache-2.0` |
| classificateurs de licence | **aucun** |
| `info.project_urls.Repository` | `https://github.com/kuzivaai/SkillWatch` |
| `upload_time_iso_8601` de 0.4.1 | `2026-07-29T18:17:39.361538Z` |
| fichiers publiés pour 0.4.1 | `skillwatch-0.4.1-py3-none-any.whl`, `skillwatch-0.4.1.tar.gz` |

**Description reprise**, champ `info.summary` :

> Monitor external URLs referenced by AI agent skills and MCP tools for
> bait-and-switch content changes

**État déclaré par l'éditeur**, champ `info.classifiers` :

> Development Status :: 3 - Alpha

La licence est déclarée par `license_expression` et **non** par le champ
`license`, qui vaut `null`, ni par un classificateur.

**Motif d'extraction d'URL repris verbatim**, `skillwatch/parser.py` l. 15 du
paquet installé — pièce de l'entrée 3 du registre :

```python
_RAW_URL_RE = re.compile(r"(?<!\()(https?://[^\s\)\]\"'>]+)")
```

---

## 7. Écarts entre ce qui était annoncé et ce qui a été retrouvé

Consignés tels quels, sans correction d'aucun autre fichier.

| annoncé | retrouvé | écart |
|---|---|---|
| AST05 « Untrusted External Instructions », sévérité et mitigations | `High` ; `Source inventory, content pinning, continuous rescanning` | **aucun** |
| AST07 « Update Drift », épinglage immuable, vérification de hash | `Medium` ; `Immutable pinning, hash verification` | **aucun** |
| AST08 « Poor Scanning », multi-tool pipeline, analyse sémantique | `Medium` ; `Semantic + behavioral multi-tool pipeline` | **aucun** — la page ajoute `behavioral` |
| nom des leads et co-leads | Ken Huang (Project Lead) ; 7 noms sous « Co-Leads » | **partiel** : Niv Hoffman est listé sous « Co-Leads », mention de rôle absente |
| SkillSpector, sortie SARIF | « NVIDIA SkillSpector (open source, recommended) » ; SARIF v2.1.0 confirmé | **aucun** — la formule de la page est « open source, recommended », employée telle quelle dans le dépôt |
| phrase « aucun scanner OWASP n'est publié » | **retrouvée**, source ligne 86 et rendu : « An OWASP-maintained `@owasp/ast10-scanner` package is not currently published. » | **aucun** — l'écart annoncé le 2026-09-09 était **une erreur de ma méthode d'extraction**, corrigée au §4 |
| composition des constats de plusieurs scanners en un verdict sans re-scan | phrase retrouvée verbatim (§4) | **aucun** |
| commit de la révision consultée du dépôt | **absent du HTML consulté** ; HEAD obtenu par l'API GitHub | **écart de source** — à citer comme « SHA via API, non prouvé pour le rendu » |
| page projet PyPI de SkillWatch | **non servie** : page anti-robot `Client Challenge` ; faits obtenus par l'API JSON | **écart de source** — classe `non_servi`, spec 3 §10 |

**Ce qui a été corrigé ailleurs, et à quel titre.** Les trois lignes
AST05 / AST07 / AST08 de `juges.yaml` portent « consulté le 2026-09-09 », avec
l'URL, la sévérité et la mitigation exacte. **Le registre n'est pas touché.**

**Une leçon de méthode, tirée de mon propre écart.** Le seul écart de fond
annoncé la veille — « la phrase n'est pas dans la page » — n'existait pas : il
venait d'une extraction qui coupait les phrases aux balises. Chercher une phrase
dans un texte reconstruit ligne à ligne depuis du HTML produit des **faux
négatifs silencieux**. Le contrôle qui l'a démenti est un `grep` sur le nom de
paquet, insensible au découpage. À faire avant de conclure à une absence : une
absence annoncée sur une méthode fragile vaut moins qu'un doute déclaré.

---

## 8. Ce que ce fichier remplace

`BRIEF-SESSION-STRATEGIE.md`, section « Relevés le 08/09 (recherche web, **à
re-vérifier**) », lignes 224 et suivantes. Ces relevés n'étaient pas vérifiés et
le disaient. `juges.README.md` et `sonde/README.md` pointent vers ce fichier, et
non vers le brief.
