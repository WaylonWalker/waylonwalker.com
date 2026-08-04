_default: thoughts mentions build-fast sync

dropper_url := "https://dropper.waylonwalker.com"

clean: reader thoughts mentions build-clean sync

cron:
    #!/usr/bin/env bash
    set -euo pipefail
    repo='{{ justfile_directory() }}'
    just_bin="$(command -v just)"
    cron_path="$HOME/go/bin:$HOME/.local/share/mise/shims:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    marker='# waylonwalker.com hourly just'
    job="0 * * * * export PATH=\"$cron_path\"; cd \"$repo\" && \"$just_bin\" cron-run"

    {
        crontab -l 2>/dev/null | grep -Fv "$marker" | grep -Fv "$job" || true
        printf '%s\n' "$marker"
        printf '%s\n' "$job"
    } | crontab -

    printf 'Installed hourly cron job:\n%s\n' "$job"

cron-remove:
    #!/usr/bin/env bash
    set -euo pipefail
    repo='{{ justfile_directory() }}'
    just_bin="$(command -v just)"
    cron_path="$HOME/go/bin:$HOME/.local/share/mise/shims:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    marker='# waylonwalker.com hourly just'
    job="0 * * * * export PATH=\"$cron_path\"; cd \"$repo\" && \"$just_bin\" cron-run"

    tmp="$(mktemp)"
    trap 'rm -f "$tmp"' EXIT

    crontab -l 2>/dev/null | grep -Fv "$marker" | grep -Fv "$job" > "$tmp" || true

    if [ -s "$tmp" ]; then
        crontab "$tmp"
    else
        crontab -r
    fi

    printf 'Removed hourly cron job:\n%s\n' "$job"

cron-run:
    #!/usr/bin/env bash
    set -euo pipefail
    repo='{{ justfile_directory() }}'
    logfile="$repo/logs/cron.log"
    just_bin="$(command -v just)"
    export PATH="$HOME/go/bin:$HOME/.local/share/mise/shims:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    start_ts=$(date +%s)

    cd "$repo"
    "$just_bin" thoughts
    "$just_bin" mentions
    "$just_bin" build-clean
    "$just_bin" sync || { rc=$?; [ "$rc" -eq 23 ] || exit "$rc"; }

    elapsed=$(( $(date +%s) - start_ts ))
    if [ "$elapsed" -ge 3600 ]; then
        duration="$(( elapsed / 3600 ))h $(( (elapsed % 3600) / 60 ))m $(( elapsed % 60 ))s"
    elif [ "$elapsed" -ge 60 ]; then
        duration="$(( elapsed / 60 ))m $(( elapsed % 60 ))s"
    else
        duration="${elapsed}s"
    fi
    mkdir -p "$(dirname "$logfile")"
    echo "$(date '+%Y-%m-%d %H:%M:%S') cron-run success (${duration})" >> "$logfile"

version := `cat version`

# documentation

build-fast:
    #!/usr/bin/env bash
    set -euxo pipefail
    # MARKATA_GO_BLOGROLL_ENABLED=false markata-go build -m fast.toml --fast
    MARKATA_GO_BLOGROLL_ENABLED=false markata-go build --fast -m config/no-tailwind.toml

build-fast-clean:
    #!/usr/bin/env bash
    set -euxo pipefail
    MARKATA_GO_BLOGROLL_ENABLED=false markata-go build --clean-all -m fast.toml --fast

serve-fast:
    #!/usr/bin/env bash
    set -euxo pipefail
    markata-go serve -m fast.toml --host 0.0.0.0 --fast

serve-live:
    #!/usr/bin/env bash
    set -euxo pipefail
    markata-go serve --host 0.0.0.0

build:
    #!/usr/bin/env bash
    # MARKATA_GO_BLOGROLL_ENABLED=false markata-go build -m config/no-tailwind.toml
    markata-go build -m config/no-tailwind.toml

build-full:
    #!/usr/bin/env bash
    set -euxo pipefail
    markata-go build

build-clean:
    #!/usr/bin/env bash
    set -euxo pipefail
    markata-go build --clean -m config/no-tailwind.toml

reader:
    #!/usr/bin/env bash
    set -euxo pipefail
    markata-go reader update

serve:
    python -m http.server -b 0.0.0.0 8000 -d output

serve-search:
    markata-go search-server --mode watch-content --host localhost --port 3001 --rebuild-index

stars:
  git diff --cached --quiet
  ./scripts/stars.py waylonwalker --token `gh auth token`
  git add pages/stars
  git commit -m 'update stars'

stars-noa:
  ./scripts/stars.py waylonwalker

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

get-snowfall:
    curl -o static/snow-fall.js https://raw.githubusercontent.com/zachleat/snow-fall/refs/heads/main/snow-fall.js

sync-gratitude:
    rsync -rlt --delete --omit-dir-times \
    --info=progress2,stats \
    falcon3:/mnt/main/walkershare/waylon/vaults/gratitude/pages/gratitude/ \
    ./pages/gratitude/

sync-ping:
    rsync -rlt --omit-dir-times \
    --info=progress2,stats \
    ./pages/ping/ \
    falcon3:/mnt/main/walkershare/waylon/vaults/gratitude/pages/ping/

    rsync -rlt --omit-dir-times \
    --info=progress2,stats \
    falcon3:/mnt/main/walkershare/waylon/vaults/gratitude/pages/ping/ \
    ./pages/ping/


sync-go:
    #!/usr/bin/env bash
    set -euo pipefail
    filter_file="$(mktemp)"
    dirs_file="$(mktemp)"
    trap 'rm -f "$filter_file" "$dirs_file"' EXIT

    git ls-files -z | while IFS= read -r -d '' tracked_file; do
        dir="${tracked_file%/*}"
        if [ "$dir" = "$tracked_file" ]; then
            continue
        fi

        while [ "$dir" != "." ] && [ -n "$dir" ]; do
            printf '/%s/\n' "$dir"
            next_dir="${dir%/*}"
            if [ "$next_dir" = "$dir" ]; then
                dir='.'
            else
                dir="$next_dir"
            fi
        done
    done | sort -u > "$dirs_file"

    {
        while IFS= read -r dir; do
            printf '+ %s\n' "$dir"
        done < "$dirs_file"

        git ls-files -z | while IFS= read -r -d '' tracked_file; do
            printf '+ /%s\n' "$tracked_file"
        done

        printf '%s\n' 'P /.markata/'
        printf '%s\n' 'P /.markata.cache/'
        printf '%s\n' 'P /.markata-cache/'
        printf '%s\n' 'P /.cache/'
        printf '%s\n' 'P /cache/'
        printf '%s\n' '- *'
    } > "$filter_file"

    rsync -rlt --delete --delete-excluded --omit-dir-times \
    --info=progress2,stats \
    --filter="merge $filter_file" \
    ./ \
    falcon3:/mnt/main/walkershare/waylon/vaults/go.waylonwalker.com

sync-go-output:
    rsync -rlt --delete --omit-dir-times \
    --info=progress2,stats \
    ./output/ \
    falcon3:/mnt/main/walkershare/waylon/sites/go.waylonwalker.com

sync:
	rsync -rlt --delete --omit-dir-times \
	--info=progress2 \
	--delay-updates \
	--delete-delay \
	./output/ \
	falcon3:/mnt/main/walkershare/waylon/sites/waylonwalker.com

lighthouse-analyze:
	./scripts/lighthouse-analysis

lighthouse-open:
	xdg-open .markata/lighthouse-analysis/latest/report.html

lighthouse-analyze-local:
	./scripts/lighthouse-local

lighthouse-open-local:
	xdg-open .markata/lighthouse-analysis-local/latest/report.html

lighthouse-refresh-local:
	just build-fast
	./scripts/lighthouse-local

sync-vault:
    rsync -a --delete --chmod=F644,D755 \
    ./ \
    falcon3:/mnt/main/walkershare/waylon/vaults/waylonwalker.com

    rsync -a --delete --chmod=F644,D755 \
    ./ \
    falcon3:/mnt/main/walkershare/waylon/vaults/go.waylonwalker.com

thoughts:
    ./scripts/thoughts.py

mentions:
    #!/usr/bin/env bash
    set -euxo pipefail
    markata-go webmentions fetch

shots-pat:
    #!/usr/bin/env bash
    set -euo pipefail

    env_file='{{ justfile_directory() }}/.env'
    manage_url='{{ dropper_url }}/auth/manage'
    token=''

    clipboard() {
        if command -v wl-paste >/dev/null 2>&1; then
            wl-paste --no-newline
            return
        fi
        if command -v xclip >/dev/null 2>&1; then
            xclip -selection clipboard -o
            return
        fi
        if command -v xsel >/dev/null 2>&1; then
            xsel --clipboard --output
            return
        fi
        if command -v pbpaste >/dev/null 2>&1; then
            pbpaste
            return
        fi
        return 1
    }

    extract_token() {
        printf '%s' "$1" | grep -m 1 -Eo 'drp_pat_v1_[a-f0-9]+_[A-Za-z0-9_-]+'
    }

    printf 'Dropper PAT setup\n\n'
    printf '1. Open this page in your browser:\n'
    printf '   %s\n' "$manage_url"
    printf '2. Sign in if needed.\n'
    printf '3. Create a personal access token.\n'
    printf '4. Copy the token to your clipboard.\n'
    printf '5. Return here and press Enter.\n\n'
    read -r -p 'Press Enter after the PAT is on your clipboard: '

    token="$(extract_token "$(clipboard 2>/dev/null || true)")"
    if [ -z "$token" ]; then
        read -r -p 'Clipboard PAT not found. Paste the token here: ' pasted
        token="$(extract_token "$pasted")"
    fi
    if [ -z "$token" ]; then
        printf '%s\n' 'No valid Dropper PAT found.' >&2
        exit 1
    fi

    tmp_file="$(mktemp)"
    trap 'rm -f "$tmp_file"' EXIT
    if [ -f "$env_file" ]; then
        grep -Ev '^DROPPER_TOKEN=' "$env_file" > "$tmp_file" || true
    fi
    printf 'DROPPER_TOKEN=%s\n' "$token" >> "$tmp_file"
    mv "$tmp_file" "$env_file"
    chmod 600 "$env_file"

    printf '\nStored Dropper PAT in %s\n' "$env_file"
    printf '%s\n' 'Next step:'
    printf '%s\n' '  just import-keebrun-shots'

import-keebrun-shots *args='':
    #!/usr/bin/env bash
    set -euo pipefail

    env_file='{{ justfile_directory() }}/.env'
    [ -f "$env_file" ] || { printf '%s\n' 'Missing .env. Run: just shots-pat' >&2; exit 1; }

    set -a
    . "$env_file"
    set +a

    [ -n "${DROPPER_TOKEN:-}" ] || { printf '%s\n' 'Missing DROPPER_TOKEN in .env. Run: just shots-pat' >&2; exit 1; }
    uv run scripts/import_keebrun_shots.py {{args}}

shots-clipboard *args='':
    #!/usr/bin/env bash
    set -euo pipefail

    env_file='{{ justfile_directory() }}/.env'
    [ -f "$env_file" ] || { printf '%s\n' 'Missing .env. Run: just shots-pat' >&2; exit 1; }

    set -a
    . "$env_file"
    set +a

    [ -n "${DROPPER_TOKEN:-}" ] || { printf '%s\n' 'Missing DROPPER_TOKEN in .env. Run: just shots-pat' >&2; exit 1; }
    uv run scripts/clipboard_shot.py {{args}}
