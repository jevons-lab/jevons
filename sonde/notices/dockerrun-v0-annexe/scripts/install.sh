#!/bin/bash
# synthetic test notice — JEVONS paired strata — not a real skill
set -eu
docker pull ghcr.io/jevons-lab/reportkit-runner:latest
docker run --rm -v "$PWD:/work" ghcr.io/jevons-lab/reportkit-runner:latest build
