_default:
   @just --list


version := `cat version`

# documentation
assets:
    #!/usr/bin/env bash
    set -euxo pipefail
    cd waylonwalker.com-obsidian-assets
    git add .
    git commit -m 'update assets'
    git push


clean:
    markata clean
build:
    markata build
serve:
    python -m http.server -b 0.0.0.0 8005 -d markout
tailwind:
    npx tailwindcss --input tailwind/app.css --output static/app-{{version}}.css --watch
tailwind-dev:
    npx tailwindcss --input tailwind/app.css --output markout/app-{{version}}.css --watch
sync:
    aws --endpoint-url https://minio.wayl.one s3 sync . s3://waylonwalker.com \
        --exclude "*.venv/**/*" \
        --exclude ".markata.cache/*" \
        --exclude "node_modules/*"  \
        --exclude ".git/*" \
        --exclude ".mypy_cache/*" \
        --exclude ".python-version"  \
        --exclude ".github/*"  \
        --exclude "markout/*"  \
        --exclude ".envrc"  \
        --exclude ".pre-commit-config.yaml"  \
        --exclude ".gitignore"  \
        --delete

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
  ./scripts/stars.py waylonwalker --token `gh auth token`

stars-noa:
  ./scripts/stars.py waylonwalker
