# Registre JEVONS — règle de publication

Registre daté, **append-only**, chaîné par empreinte. Posé le 2026-09-08 ;
règle de publication posée le 2026-09-09.

```
python3 tools/registre.py verifier          # recalcule toute la chaîne
python3 tools/registre.py rendre            # registre.md, vue complète
python3 tools/registre.py rendre --public   # registre-public.md, vue publique
```

## Ce qui ne change jamais

- Une entrée n'est **jamais** modifiée, réordonnée ni supprimée.
- Une entrée fausse se corrige par une **entrée suivante** qui la rectifie ; les
  deux restent lisibles.
- Une **rétractation est une entrée nouvelle**, jamais une réécriture.
- Une entrée **ouverte ne se referme jamais**. `verifier` refuse tout acte de
  classement qui tenterait de resceller une entrée ouverte, et affiche l'anomalie.

## Classes

| classe | nom | ce que c'est |
|---|---|---|
| 1 | `nous` | nos erreurs, nos rectifications, nos décisions |
| 2 | `juge_open_source` | défaut d'un outil dont le code est public |
| 3 | `juge_proprietaire_ou_service` | outil fermé, service, programme de certification |
| 4 | `artefact_nomme` | un artefact public désigné par son nom |
| 5 | `client` | **jamais écrite dans ce registre**, quelle que soit la circonstance |

La classe 5 n'est pas une classe qu'on utilise avec précaution : c'est une
classe qu'on n'écrit pas. `tools/registre.py ajouter` la refuse.

## Statuts

| statut | ce qui est publié |
|---|---|
| `ouverte` | l'entrée en clair : titre, corps, sources, empreintes |
| `scellee` | le sceau seul : numéro, date du fait, classe, empreinte du contenu, empreinte de chaîne |

Une entrée scellée n'expose **ni titre, ni corps, ni sources, ni nom de juge**.

Un sceau ne cache pas un fait : il en **date l'existence** et en **fige le
contenu**. Le jour de l'ouverture, n'importe qui peut vérifier que le texte
alors publié est bien celui dont l'empreinte était scellée à cette date. C'est
la seule chose qu'un registre apporte qu'une publication ordinaire n'apporte
pas.

## URL dans le corps scellé — règle du 2026-09-09

**Dans le corps scellé d'une entrée, les URL de cibles mesurées sont VIVES :
elles résolvent.** Le désamorçage éventuel — `hxxps`, `[.]` — appartient au
**rendu de la page**, jamais au corps.

**Motif.** Le corps est **la source recalculable** : c'est lui dont on refait
l'empreinte pour vérifier qu'une entrée n'a pas bougé, et c'est lui qu'un tiers
lit pour **rejouer la mesure**. Une URL désamorcée dans le corps donne à ce
tiers une adresse qui ne résout pas : il peut vérifier l'empreinte, il ne peut
pas refaire la mesure. Le corps doit contenir ce qui se rejoue.

**Ce que la règle ne dit pas.** Elle ne touche ni au corpus, ni aux fiches, ni
aux fichiers de lecture du juge, où le désamorçage reste la règle
(`CLAUDE.md`). Elle porte sur le **corps scellé des entrées du registre**, et
sur lui seul.

**Le rendu reste libre de désamorcer.** Une page publique peut afficher
`hxxps://…` pour éviter un lien cliquable vers une cible mesurée. C'est une
décision de présentation, réversible, hors empreinte — exactement comme les
titres anglais des entrées 1 à 12.

### État constaté au 2026-09-09, avant la règle

La pratique n'était pas uniforme, et **aucune entrée n'est corrigée** — le
registre est append-only, et l'entrée 13 chaîne déjà sur la 12.

| entrée | pratique |
|---|---|
| 7 | URL **vive** |
| 8 | 3 URL **désamorcées** — mesure non rejouable depuis le corps |
| 9 | 1 URL désamorcée |
| 3 | mixte : une vive, une désamorcée |
| les autres | aucune URL |

Le défaut de l'entrée 8 est réparé par une entrée postérieure qui donne les
trois URL vives, sans que l'entrée 8 soit touchée.

## Entrées bilingues — règle du 2026-09-09

**À partir de l'entrée 13, chaque entrée est scellée bilingue.** Le corps porte
le texte **français puis sa version anglaise**, dans le **même contenu**, sous
la **même empreinte**, avec la mention **« le français fait foi »**.

**Pourquoi dans l'empreinte et pas à côté.** Un registre dont la version
anglaise vit hors du sceau publie deux textes dont un seul est daté et figé. Le
lecteur anglophone n'a alors aucun moyen de vérifier que ce qu'il lit est ce qui
a été scellé. En mettant les deux langues sous la même empreinte, une traduction
ne peut plus dériver du texte qu'elle traduit sans casser la chaîne.

**Le français fait foi.** En cas de divergence entre les deux versions, la
française l'emporte. La mention est portée par l'entrée elle-même, pas seulement
par ce README.

### Les entrées 1 à 12 restent telles quelles

Elles ont été scellées en français seul, avant cette règle, et le registre est
append-only : **elles ne sont pas réécrites**. Leur résumé anglais relève du
**rendu** — `site/titres.yaml` associe à chaque entrée un titre anglais indexé
par son empreinte — et reste donc **hors empreinte**. C'est une différence de
statut qu'un lecteur doit connaître : pour les entrées 1 à 12, l'anglais est une
commodité de lecture ; à partir de la 13, il est scellé.

### Pourquoi 13 et non 12

La règle a été posée le 2026-09-09 à 08:2x. L'**entrée 12 avait été scellée à
08:01:48 UTC**, une vingtaine de minutes plus tôt, en français seul. Faire
commencer la règle à 12 aurait demandé soit de réécrire l'entrée 12 — interdit —
soit de la déclarer conforme alors qu'elle ne l'est pas. Le seuil est donc **13**,
et cette date d'écart est écrite plutôt que lissée.

## Règle propre à la classe 3

Une entrée de classe 3 — outil propriétaire, service, programme de
certification — **ne se scelle que si les deux conditions suivantes sont
remplies, pour chaque cas qu'elle nomme** :

1. le cas est jugé **sous la définition en vigueur** : `docs/definition-v3.2.md`,
   amendement du 2026-09-05 révision 1, **et les deux décisions du §9 du rapport
   effectivement appliquées** ;
2. le cas est **contrôlé par le second juge**.

Motif : une entrée de classe 3 met en cause un tiers qui ne peut ni voir le
contenu scellé, ni le contester. Le sceau l'engage sans qu'il puisse répondre.
Le minimum est donc que le fait scellé repose sur des étiquettes à jour et
vérifiées par un second lecteur — sinon le registre daterait une opinion, pas
un fait.

Tant que ces conditions ne sont pas remplies, **rien n'est scellé** : ni entrée
ouverte, ni entrée scellée. L'absence d'entrée est préférable à un sceau qui ne
tiendrait pas.

## Actes de classement — publiés en entier, règle du 2026-09-10

**Un acte de classement se publie comme une entrée ouverte** : titre, corps,
tableau des entrées classées, sources. La vue publique n'en donnait auparavant
que la date et l'empreinte de chaîne.

**Motif.** Un acte de classement est une décision qui change ce qu'un lecteur
peut voir. La cacher ferait de la mécanique d'ouverture et de scellement la
seule zone d'ombre du dispositif — et c'est celle qui touche à la transparence
elle-même. Le jour où un sceau se lève, le lecteur doit pouvoir lire pourquoi,
quand, et sur quelle pièce.

**Contrainte que cette règle impose à la rédaction d'un acte.** Un acte qui
**scelle** une entrée ne doit pas décrire ce qu'il scelle. L'acte 5 est passé
tout près : il écrivait « l'entrée 3 est scellée jusqu'au jour de l'issue
déposée auprès de l'éditeur de l'outil concerné » et citait en source le chemin
du brouillon, dont le nom de fichier porte celui de l'outil. L'entrée 3 étant
aujourd'hui ouverte, cela ne révèle plus rien ; publié pendant le sceau, cela
en aurait dit l'objet. **Un acte qui scelle nomme l'entrée et la date, jamais
la matière.**

## Ce qu'une entrée ouverte peut dire d'une entrée scellée — règle du 2026-09-10

La contrainte ci-dessus ne visait que les **actes de classement**. Elle est trop
étroite : **une entrée ordinaire peut nommer la matière d'un sceau** aussi
sûrement qu'un acte, et sans qu'aucun contrôle ne s'en aperçoive — les contrôles
d'export cherchent des fragments du corps scellé, pas une description qui en
dirait l'objet avec d'autres mots.

**La règle, étendue.** Aucune entrée ouverte — acte de classement ou non — ne
nomme la matière d'une entrée scellée **au-delà de ce qui est strictement
nécessaire pour être intelligible**. Quand cette nécessité se présente,
**l'entrée le dit explicitement et le justifie**, dans son corps, à l'endroit
où elle le fait.

**Ce que « la matière » recouvre.** Le sujet de l'entrée scellée, les objets
qu'elle nomme, ce qu'elle en établit. Pas son existence, ni sa date, ni sa
classe, ni ses empreintes : le sceau les publie déjà, c'est son office.

### Le cas où cette nécessité s'est présentée — entrée 26

L'**entrée 26** rectifie l'entrée 20, scellée, en consignant que deux faits ont
changé après son sceau. Elle **ne pouvait pas le faire sans nommer les cinq cas
que l'entrée 20 scelle** : dire qu'un régime de verdict a changé sur quatre
d'entre eux exige de dire lesquels.

Conséquence, constatée et assumée : **quels cas l'entrée 20 scelle est public,
ce que les juges en ont dit ne l'est pas.** Un lecteur sait qu'elle porte sur
`jev-0045`, `jev-0078`, `jev-0079`, `jev-0080`, `jev-0081` et sur leur régime ;
il ignore les étiquettes rendues, l'unanimité des tirages et les motifs écrits.
**Ce qui devait être protégé l'est** — le jugement, pas la liste.

Le registre est append-only : l'entrée 26 n'est ni retirée ni rectifiée, et
aucune entrée nouvelle n'est écrite pour cela, qui aggraverait au lieu de
corriger. Le fait est noté ici, dans la règle, pour que la prochaine entrée qui
rencontrera la même nécessité la déclare au lieu de la subir.

## Comment le classement des entrées anciennes est porté

La règle de publication est postérieure aux entrées 1 à 4. Ces entrées ne
peuvent pas la porter dans leur corps sans être modifiées, ce qui est interdit.
Le classement est donc lui-même une **entrée de type `classement`**, datée et
chaînée. L'état effectif d'une entrée se lit : ses champs natifs, puis les actes
de classement postérieurs, le dernier l'emportant.

Les entrées créées après le 2026-09-09 portent `classe` et `statut` nativement ;
`ajouter` les exige.
