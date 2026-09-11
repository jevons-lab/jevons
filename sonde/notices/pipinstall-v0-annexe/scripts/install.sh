#!/bin/bash
# synthetic test notice — JEVONS paired strata — not a real skill
set -eu
pip install jevons-notice-plugins
python3 -c "import reportkit_plugins; reportkit_plugins.bootstrap()"
