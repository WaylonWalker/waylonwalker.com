---
date: 2026-02-08
templateKey: blog-post
title: Next
published: false
tags:
  - meta
  - planning
author: kimi-k2.5-free
---

A running list of blog post ideas to strengthen underrepresented topics on the
site.

## Docker Posts

Building out Docker/containerization content to match the llms.txt claims.

### Existing Foundation

- [docker-deep-dive.md](/docker-deep-dive/) - unpublished notes from 2021
- [docker-minecraft-server.md](/docker-minecraft-server/) - minecraft in docker
- [modded-minecraft-in-docker.md](/modded-minecraft-in-docker/) - modded server
  setup
- [emoji-in-headless-chrome-in-docker.md](/emoji-in-headless-chrome-in-docker/) -
  headless chrome fix

### Suggested Posts

- **"Why I containerize my entire dev environment"** - Philosophy post linking to
  the 2026 resolution about working from a distrobox image
- **"Docker vs Kubernetes in the homelab: when to use what"** - Standalone
  comparison post (referenced in right/wrong reasons posts)
- **"My devtainer workflow: dotfiles in Docker"** - Document the actual devtainer
  setup mentioned in llms.txt
- **"Migrating from Docker Compose to Kubernetes with kompose"** - Experience
  from the 6-months-in post, expanded
- **Finish docker-deep-dive.md** - Turn those 2021 notes into a published deep
  dive

## Distrobox Posts

Lightest coverage area. Need to expand beyond the few short posts.

### Existing Foundation

- [backup-distrobox-image.md](/backup-distrobox-image/) - cloning/upgrading (22
  lines, very short)
- [setup-bambu-studio-in-distrobox.md](/setup-bambu-studio-in-distrobox/) -
  bambu studio with GPU (33 lines)
- [gpus-are-awesome.md](/gpus-are-awesome/) - mentions distrobox for GPU access
- [2026-resolutions.md](/2026-resolutions/) - mentions heavy distrobox usage on
  Bazzite

### Suggested Posts

- **"A month working entirely from distrobox: what's working and what isn't"** -
  Practical retrospective based on the 2026 resolution
- **"distrobox vs dev containers: why I chose distrobox"** - Reasoning for the
  switch
- **"GPU passthrough in distrobox for 3D printing workflows"** - Expand the
  bambu-studio post, explain `--nvidia` flag deeply
- **"Managing multiple distrobox environments"** - How to organize/backup/clone
  (expand the backup post significantly)
- **"From Bazzite host to Arch distrobox: my immutable desktop workflow"** - The
  daily driver setup

## Quick Wins

1. **Publish docker-deep-dive.md** - Set `published: true` and clean up the 2021
   notes
2. **Expand backup-distrobox-image.md** - 22 lines to full post with workflow
   rationale
3. **Create a containers index page** - Tie together scattered container posts
   under one "My Container Workflow" index
