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
    npx tailwindcss --input tailwind/app.css --output static/app.css --watch
tailwind-dev:
    npx tailwindcss --input tailwind/app.css --output markout/app.css --watch
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
    podman build -t docker.io/waylonwalker/waylonwalker-com .
    version=$(cat version)
    podman tag docker.io/waylonwalker/waylonwalker-com docker.io/waylonwalker/waylonwalker-com:$version
    podman push docker.io/waylonwalker/waylonwalker-com
    podman push docker.io/waylonwalker/waylonwalker-com:$version
