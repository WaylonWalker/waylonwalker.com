---
title: '💭 distrobox/docs/usage/distrobox-assemble.md at main · 89luca89/...'
date: 2024-09-30T15:49:25
template: link
link: https://github.com/89luca89/distrobox/blob/main/docs/usage/distrobox-assemble.md
tags:
  - docker
  - podman
  - distrobox
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/89luca89/distrobox/blob/main/docs/usage/distrobox-assemble.md]]

This page is gold.  It lays out all of the distrobox assemble api with some good examples  of how to get access to things like podman and kind from inside of containers.

Especially this example.

``` ini
[tumbleweed_distrobox]
image=registry.opensuse.org/opensuse/distrobox
pull=true
additional_packages="acpi bash-completion findutils iproute iputils sensors inotify-tools unzip"
additional_packages="net-tools nmap openssl procps psmisc rsync man tig tmux tree vim htop xclip yt-dlp"
additional_packages="git git-credential-libsecret"
additional_packages="patterns-devel-base-devel_basis"
additional_packages="ShellCheck ansible-lint clang clang-tools codespell ctags desktop-file-utils gcc golang jq python3"
additional_packages="python3-bashate python3-flake8 python3-mypy python3-pipx python3-pycodestyle python3-pyflakes python3-pylint python3-python-lsp-server python3-rstcheck python3-yapf python3-yamllint rustup shfmt"
additional_packages="kubernetes-client helm"
init_hooks=GOPATH="${HOME}/.local/share/system-go" GOBIN=/usr/local/bin go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest;
init_hooks=GOPATH="${HOME}/.local/share/system-go" GOBIN=/usr/local/bin go install github.com/onsi/ginkgo/v2/ginkgo@latest;
init_hooks=GOPATH="${HOME}/.local/share/system-go" GOBIN=/usr/local/bin go install golang.org/x/tools/cmd/goimports@latest;
init_hooks=GOPATH="${HOME}/.local/share/system-go" GOBIN=/usr/local/bin go install golang.org/x/tools/gopls@latest;
init_hooks=GOPATH="${HOME}/.local/share/system-go" GOBIN=/usr/local/bin go install sigs.k8s.io/kind@latest;
init_hooks=ln -sf /usr/bin/distrobox-host-exec /usr/local/bin/conmon;
init_hooks=ln -sf /usr/bin/distrobox-host-exec /usr/local/bin/crun;
init_hooks=ln -sf /usr/bin/distrobox-host-exec /usr/local/bin/docker;
init_hooks=ln -sf /usr/bin/distrobox-host-exec /usr/local/bin/docker-compose;
init_hooks=ln -sf /usr/bin/distrobox-host-exec /usr/local/bin/flatpak;
init_hooks=ln -sf /usr/bin/distrobox-host-exec /usr/local/bin/podman;
init_hooks=ln -sf /usr/bin/distrobox-host-exec /usr/local/bin/xdg-open;
exported_apps="htop"
exported_bins="/usr/bin/htop /usr/bin/git"
exported_bins_path="~/.local/bin"
````

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
