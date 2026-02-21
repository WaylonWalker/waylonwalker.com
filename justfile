_default:
   @just --list


version := `cat version`

# documentation
default:
    #!/usr/bin/env bash
    set -euxo pipefail
    just --choose

setup:
    #!/usr/bin/env bash
    set -euxo pipefail
    just clone-assets
    just pull-assets
    just venv

assets:
    #!/usr/bin/env bash
    set -euxo pipefail
    juts clone-assets
    just pull-assets
    just push-assets

clone-assets:
    #!/usr/bin/env bash
    set -euxo pipefail
    if [ ! -d waylonwalker.com-obsidian-assets ]; then
    git clone https://github.com/waylonwalker/waylonwalker.com-obsidian-assets.git
    fi

push-assets:
    #!/usr/bin/env bash
    set -euxo pipefail
    cd waylonwalker.com-obsidian-assets
    if [ -n "$(git status --porcelain)" ]; then
    git add .
    git commit -m 'update assets'
    git push
    else
    echo "no changes"
    fi

pull-assets:
    #!/usr/bin/env bash
    set -euxo pipefail
    cd waylonwalker.com-obsidian-assets
    git pull

venv:
    #!/usr/bin/env bash
    set -euxo pipefail
    uv venv
    source .venv/bin/activate
    uv pip install -r requirements.txt

build-clean:
    #!/usr/bin/env bash
    set -euxo pipefail
    markata-go build --clean

# Fast build: only blog posts, no blogroll/reader fetches
# Uses fast.toml + env var to disable blogroll for maximum speed
build-fast:
    #!/usr/bin/env bash
    set -euxo pipefail
    MARKATA_GO_BLOGROLL_ENABLED=false markata-go build -m fast.toml

# Fast build with clean cache
build-fast-clean:
    #!/usr/bin/env bash
    set -euxo pipefail
    MARKATA_GO_BLOGROLL_ENABLED=false markata-go build --clean-all -m fast.toml --fast

# Fast build with clean cache
serve-fast:
    #!/usr/bin/env bash
    set -euxo pipefail
    MARKATA_GO_BLOGROLL_ENABLED=false markata-go serve -m fast.toml --host 0.0.0.0 --fast

serve-live:
    #!/usr/bin/env bash
    set -euxo pipefail
    markata-go serve --host 0.0.0.0

build:
    #!/usr/bin/env bash
    markata-go build

serve:
    python -m http.server -b 0.0.0.0 8000 -d output

tailwind:
    # npx tailwindcss --input tailwind/app.css --output static/app-{{version}}.css --minify --watch
    # npx tailwindcss --input tailwind/app.css --output static/app.css --minify --watch
    pnpm exec tailwindcss --input tailwind/app.css --output static/app.css --minify --watch
tailwind-dev:
    # npx tailwindcss --input tailwind/app.css --output markout/app-{{version}}.css --minify --watch
    # npx tailwindcss --input tailwind/app.css --output markout/app.css --minify --watch
    pnpm exec tailwindcss --input tailwind/app.css --output markout/app.css --minify --watch
# sync:
#     aws --endpoint-url https://minio.wayl.one s3 sync . s3://waylonwalker.com \
#         --exclude "*.venv/**/*" \
#         --exclude ".markata.cache/*" \
#         --exclude "node_modules/*"  \
#         --exclude ".git/*" \
#         --exclude ".mypy_cache/*" \
#         --exclude ".python-version"  \
#         --exclude ".github/*"  \
#         --exclude "markout/*"  \
#         --exclude ".envrc"  \
#         --exclude ".pre-commit-config.yaml"  \
#         --exclude ".gitignore"  \
#         --delete

sync-md:
    aws --endpoint-url https://minio.wayl.one s3 sync . s3://waylonwalker.com --exclude "*" --include "pages/**/*.md"

deploy:
    #!/usr/bin/env bash
    set -euxo pipefail
    version=$(cat version)
    podman build -t registry.wayl.one/waylonwalker-com -t registry.wayl.one/waylonwalker-com:$version .
    podman push registry.wayl.one/waylonwalker-com
    podman push registry.wayl.one/waylonwalker-com:$version


url:
    #!/usr/bin/bash
    ########
    ### Special text formating
    ########
    ## Function to generate a clickable link, you can call this using
    # url=$(Urllink "https://ublue.it" "Visit the ublue website")
    # echo "${url}"
    function Urllink (){
        URL=$1
        TEXT=$2

        # Generate a clickable hyperlink
        printf "\e]8;;%s\e\\%s\e]8;;\e\\" "$URL" "$TEXT${n}"
    }

    echo
    echo "$(Urllink "https://waylonwalker.com" "Click to open the website")"
url2:
    #!/usr/bin/bash
    source libformatting.sh
    echo "$(Urllink "https://docs.projectbluefin.io/administration#community-aliases-and-workarounds" "Click here to view the Universal Blue just documentation")"

url3:
    #!/usr/bin/env zsh

    # Function to generate a clickable link
    Urllink() {
        local URL="$1"
        local TEXT="$2"

        # Use printf with correct escape sequences
        print -P "\e]8;;$URL\a$TEXT\e]8;;\a"
    }

    # Test the function
    echo
    Urllink "https://waylonwalker.com" "Click to open the website"

stars:
  git diff --cached --quiet
  ./scripts/stars.py waylonwalker --token `gh auth token`
  git add pages/stars
  git commit -m 'update stars'

stars-noa:
  ./scripts/stars.py waylonwalker

compile:
  uv pip compile requirements.in -o requirements.txt --refresh

delete-release:
    #!/usr/bin/env bash
    set -euo pipefail

    # Get the version
    VERSION=$(cat version)

    # Delete the release
    gh release delete "v$VERSION"

create-tag:
    #!/usr/bin/env bash
    VERSION=$(cat version)
    git tag -a "v$VERSION" -m "Release v$VERSION"
    git push origin "v$VERSION"

delete-tag:
    #!/usr/bin/env bash
    VERSION=$(cat version)
    git tag -d "v$VERSION"
    git push --delete origin "v$VERSION"

create-release:
    #!/usr/bin/env bash
    VERSION=$(cat version)
    # git add version
    # git add requirements.in
    # git add requirements.txt
    # git add tailwind/app.css
    # git add static/app-{{version}}.css
    ./scripts/get_release_notes.py "$VERSION" > release_notes.tmp
    gh release create "v$VERSION" \
        --title "v$VERSION" \
        --notes-file release_notes.tmp
    rm release_notes.tmp


release:
   #!/bin/bash
   # tailwindcss --input tailwind/app.css --output static/app-{{version}}.css
   # git add version
   # git add requirements.in
   # git add requirements.txt
   # git add tailwind/app.css
   # git add static/app-{{version}}.css
   # git commit -m "Release v$(cat version)"
   # git tag -a "v$(cat version)" -m "Release v$(cat version)"
    ./scripts/get_release_notes.py "$VERSION" > release_notes.tmp
    gh release create "v$VERSION" \
        --title "v$VERSION" \
        --notes-file release_notes.tmp \
    rm release_notes.tmp
   git push
   git push --tags

dev:
   # mc cp ./markout/ minio-wayl-one/k8s-pages/wwdev --recursive
   # mc mirror ./markout minio-wayl-one/k8s-pages/wwdev --overwrite --watch --exclude "*.log"
   uvx --with awscli aws s3 sync ./markout s3://k8s-pages/wwdev --exclude "*.log"

get-fragmention:
    curl https://raw.githubusercontent.com/chapmanu/fragmentions/refs/heads/master/fragmention.min.js > static/fragmention.min.js
    curl https://raw.githubusercontent.com/kartikprabhu/fragmentioner/refs/heads/master/fragmentioner.js > static/fragmentioner.js
get-snowfall:
    curl -o static/snow-fall.js https://raw.githubusercontent.com/zachleat/snow-fall/refs/heads/main/snow-fall.js

sync:
    rsync -a --delete --chmod=F644,D755 \
    ./output/ \
    falcon3:/mnt/main/walkershare/waylon/sites/go.waylonwalker.com
