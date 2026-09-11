# Contrôle d'export public — export-public

Produit par `tools/preparer-export-public.py`. **Aucun remote n'est
configuré, aucun push n'est fait.**

## Contrôles appliqués

| | contrôle |
|---|---|
| C1 | aucun fichier du corpus |
| C2 | aucune sortie brute (`.log/`, `scanners/`) |
| C3 | entrées scellées : rien au-delà du sceau ; `registre.jsonl` ne sort jamais |
| C4 | aucune chaîne de clé `sk-…` |
| C5 | aucun chemin absolu de l'hôte ou de l'enclave |
| C6 | notices : cibles en domaines réservés seulement (spec 2 §2) |

## Contenu de l'export — 64 fichiers

**(racine)** — 5 fichiers

- `CNAME`
- `feed.xml`
- `index.html`
- `references.md`
- `robots.txt`

**registre/** — 2 fichiers

- `registre/README.md`
- `registre/registre-public.md`

**sonde/** — 57 fichiers

- `sonde/.github/workflows/probe.yml`
- `sonde/LICENSE-NOTICES`
- `sonde/README.md`
- `sonde/acceptation.md`
- `sonde/adaptateur-generic-ai-skill-scanner.json`
- `sonde/adaptateur-generic-skill-auditor.json`
- `sonde/jevons_probe.py`
- `sonde/notices/curlsh-f0/SKILL.md`
- `sonde/notices/curlsh-f1/SKILL.md`
- `sonde/notices/curlsh-f2/SKILL.md`
- `sonde/notices/curlsh-f3/SKILL.md`
- `sonde/notices/curlsh-v0-annexe/SKILL.md`
- `sonde/notices/curlsh-v0-annexe/scripts/install.sh`
- `sonde/notices/curlsh-v0/SKILL.md`
- `sonde/notices/curlsh-v1/SKILL.md`
- `sonde/notices/curlsh-v2/SKILL.md`
- `sonde/notices/curlsh-v3/SKILL.md`
- `sonde/notices/curlsh-v4/SKILL.md`
- `sonde/notices/curlsh-v5/SKILL.md`
- `sonde/notices/curlsh-v5b/SKILL.md`
- `sonde/notices/curlsh-v6/SKILL.md`
- `sonde/notices/dockerrun-v0-annexe/SKILL.md`
- `sonde/notices/dockerrun-v0-annexe/scripts/install.sh`
- `sonde/notices/dockerrun-v0/SKILL.md`
- `sonde/notices/dockerrun-v1/SKILL.md`
- `sonde/notices/dockerrun-v2/SKILL.md`
- `sonde/notices/dockerrun-v3/SKILL.md`
- `sonde/notices/dockerrun-v4/SKILL.md`
- `sonde/notices/dockerrun-v5/SKILL.md`
- `sonde/notices/dockerrun-v6/SKILL.md`
- `sonde/notices/gitclone-f0/SKILL.md`
- `sonde/notices/gitclone-f1/SKILL.md`
- `sonde/notices/gitclone-f2/SKILL.md`
- `sonde/notices/gitclone-f3/SKILL.md`
- `sonde/notices/gitclone-v0-annexe/SKILL.md`
- `sonde/notices/gitclone-v0-annexe/scripts/install.sh`
- `sonde/notices/gitclone-v0/SKILL.md`
- `sonde/notices/gitclone-v1/SKILL.md`
- `sonde/notices/gitclone-v2/SKILL.md`
- `sonde/notices/gitclone-v3/SKILL.md`
- … et 17 autres

## Substitutions déclarées — 12 fichiers

Chemins absolus de l'enclave remplacés par `<enclave>` :

- `sonde/rapports-notices-publiables/agentscan/report.json`
- `sonde/rapports-notices-publiables/agentscan/report.md`
- `sonde/rapports-notices-publiables/ai-skill-scanner/report.json`
- `sonde/rapports-notices-publiables/ai-skill-scanner/report.md`
- `sonde/rapports-notices-publiables/cisco/report.json`
- `sonde/rapports-notices-publiables/cisco/report.md`
- `sonde/rapports-notices-publiables/skill-auditor/report.json`
- `sonde/rapports-notices-publiables/skill-auditor/report.md`
- `sonde/rapports-notices-publiables/skillspector/report.json`
- `sonde/rapports-notices-publiables/skillspector/report.md`
- `sonde/rapports-notices-publiables/skillvet/report.json`
- `sonde/rapports-notices-publiables/skillvet/report.md`

## Refusé par le contrôle — 9 fichiers

| contrôle | motif | fichiers |
|---|---|---|
| C6 | identité visée ni réservée ni détenue : paquet jevons-notice-plugins  [notice refusée en bloc] | `corpus/paires-publiables/pipinstall-v0-annexe/SKILL.md`, `corpus/paires-publiables/pipinstall-v0-annexe/scripts/install.sh`, `corpus/paires-publiables/pipinstall-v0/SKILL.md` … (9 au total) |

