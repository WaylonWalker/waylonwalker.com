#!/bin/bash
set -euxo pipefail
[ -d /site/waylonwalker.com ] || git clone https://github.com/waylonwalker/waylonwalker.com.git /site/waylonwalker.com
pushd /site/waylonwalker.com
git pull
mkdir -p markout
markata build
# wrangler pages deploy markout --project-name dev-waylonwalker-com --branch main --commit-message "deploy main $(date)"
# wrangler pages deploy markout --project-name reader-waylonwalker-com --branch markout
