# Sonde — critère d'acceptation sur les **notices publiables**

**Ce rapport porte sur les notices réécrites** (`corpus/paires-publiables`), pas
sur les notices d'origine mesurées par le banc. Le contrôle d'origine reste dans
`sonde/acceptation.md` et n'est pas modifié : les chiffres du §2 du rapport
portent sur `corpus/paires`, avec leurs empreintes.

Somme des rapports des 4 outils épinglés, produits par `sonde/jevons_probe.py`.
Confrontation aux chiffres publiés au §2 du rapport du banc. Aucun ajustement.

Ordinal : version 2.

| outil | version | R1 | R3 | R4 | R5 | R7 |
|---|---|---|---|---|---|---|
| `skillspector` | SkillSpector 2.11.0 | 0/4 | 0/4 | 0/2 | 4/4 | 4/6 |
| `skillvet` | skillvet 2.0.9, revision archivee swh a350337f | 0/4 | 0/4 | 0/2 | 4/4 | 3/6 |
| `agentscan` | agentscan-cli 1.2.2 | 0/4 | 0/4 | 0/2 | 4/4 | 5/6 |
| `cisco` | Cisco skill-scanner 2.1.0 | 0/4 | 0/4 | 0/2 | 4/4 | 4/6 |

## Totaux, ligne ordinale (celle de la spec)

| relation | recalculé | publié §2 | écart |
|---|---|---|---|
| `R1` | 0 / 16 | 0 / 16 | aucun |
| `R3` | 0 / 16 | 0 / 16 | aucun |
| `R4` | 0 / 8 | 0 / 8 | aucun |
| `R5` | 16 / 16 | 16 / 16 | aucun |

Le §2 du rapport écrit R5 « 0 / 16 (identiques) » : il compte les paires où le
verdict **change**. La sonde compte les paires où la relation **tient**, et R5
attend la stabilité. 16/16 tenues et 0/16 changements sont le même fait.

## R7 — combien d'outils changent de verdict

Le §2 publie « change chez 3 outils sur 4 ». Un outil « change » dès qu'une
paire R7 n'est pas tenue, le comportement étant identique des deux côtés.

Le banc restreint ce compte au comportement `curl` : « agentscan est le seul
outil dont le verdict sur `curl` ne dépend pas de la forme ». La sonde donne
donc le compte **par comportement** et **par ligne**, sans en privilégier un.

| outil | curlsh, ordinal | curlsh, sévérité | gitclone, ordinal | gitclone, sévérité |
|---|---|---|---|---|
| `skillspector` | 1/3 change | 1/3 change | 3/3 stable | 3/3 stable |
| `skillvet` | 0/3 change | 0/3 change | 3/3 stable | 3/3 stable |
| `agentscan` | 3/3 stable | 3/3 stable | 2/3 change | 2/3 change |
| `cisco` | 1/3 change | 1/3 change | 3/3 stable | 3/3 stable |

| comportement | ligne | outils qui changent |
|---|---|---|
| curlsh | ordinal | **3 / 4** |
| curlsh | severite | **3 / 4** |
| gitclone | ordinal | **1 / 4** |
| gitclone | severite | **1 / 4** |

**Le « 3 sur 4 » publié est reproduit par : comportement `curlsh` — ligne de
sévérité 3 sur 4, ligne ordinale 3 sur 4.**

Ces rapports sont produits sous l'**ordinal version 2**, à six niveaux
(`clean`, `info`, `low`, `medium`, `high`, `critical`), posé par l'amendement
du 2026-09-09 (spec 2 §9). Sous l'ordinal version 1, à quatre niveaux, la
ligne ordinale rendait **2 sur 4** et non 3 : elle rangeait `HIGH` et
`CRITICAL` sur la même valeur, donc elle ne voyait pas le basculement de
Cisco entre les deux selon la forme de la commande — l'un des trois
changements comptés au banc. C'est ce constat, et lui seul, qui a motivé
l'amendement ; les rapports antérieurs ne sont pas recalculés.

Les deux lignes sont rapportées côte à côte. Aucune ne remplace l'autre, et le
chiffre publié n'est pas modifié.

## Écarts

Aucun.

---

## Écart de tenue après réécriture — un, et il est instructif

Comparaison des six outils, notices d'origine contre notices publiables, même
ordinal v2, mêmes versions épinglées, mêmes adaptateurs. **Un seul écart sur
36 relations mesurées** :

| outil | relation | origine | publiables |
|---|---|---|---|
| `skillvet` | `R-perimetre` | **4 / 4** | **3 / 4** |

**La paire qui bascule** : `dockerrun-v0` contre `dockerrun-v0-annexe`.

| | notices d'origine | notices publiables |
|---|---|---|
| page `dockerrun-v0` | `clean` | `clean` |
| annexe `dockerrun-v0-annexe` | `clean` | **`caution`** |

**La seule différence entre les deux annexes**, ligne à ligne :

```
- docker pull reportkit/reportkit-runner:latest
+ docker pull ghcr.io/jevons-lab/reportkit-runner:latest
```

**Ce qui se déclenche** : le contrôle `W7` de skillvet, qui rend
`Third-party Docker registry: …`. Il fire sur l'image hébergée sur un registre
**nommé**, et reste muet sur l'image sans registre explicite — celle que Docker
Hub sert par défaut.

**Ce que cet écart mesure.** Le verdict de skillvet sur ce geste dépend du **nom
du registre**, pas du comportement : même commande, même absence de garde, même
image tirée puis exécutée. Et il tombe dans le sens contre-intuitif — l'image
sur `ghcr.io` est celle que le projet **possède** ; l'image implicite sur Docker
Hub portait un nom **libre, donc enregistrable par n'importe qui**. L'outil
alerte sur la plus sûre des deux.

**Ce que nous n'avons pas fait.** Nous n'avons pas cherché un autre nom de
remplacement jusqu'à retrouver 4/4. La règle était écrite avant la mesure
(`docs/plan-reecriture-notices.md` §5) : **tout écart de tenue est un fait à
consigner, pas à corriger.** Changer les noms jusqu'à retrouver le chiffre
attendu reviendrait à ajuster l'instrument sur la réponse voulue.

**Ce que l'écart ouvre.** C'est la première mesure à l'appui de la relation
candidate **R-identité** — même geste, cible réservée ou cible enregistrable —
notée au journal le 2026-09-09 et jamais implémentée faute de matériau. Le
matériau existe maintenant. Elle reste à pré-enregistrer avant d'être écrite,
comme R7 l'a été.

Les cinq autres outils rendent des tenues **identiques** sur les six relations.
