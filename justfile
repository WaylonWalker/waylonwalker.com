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
