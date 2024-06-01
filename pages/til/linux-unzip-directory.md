---
date: 2022-04-02 16:20:34.042196
templateKey: til
title: Unzip minecraft mods to their directory from the command line
tags:
  - linux
  - bash
  - cli

---

This morning I was trying to install a modpack on my minecraft server after
getting a zip file, and its quite painful when I unzip everything in the
current directory rather than the directory it belongs in.

## I had the files on a Windows Machine

So I've been struggling to get mods installed on linux lately and the easiest
way to download the entire pack rather than each mod one by one seems to be to
use the overwolf application on windows.  Once I have the modpack I can start
myself a small mod-server by zipping it, putting it in a mod-server directory
and running a python `http.server`

```bash
python -m http.server
```

## Downoading on the server

Then I go back to my server and download the modpack with wget.

``` python
wget 10.0.0.171:8000/One%2BBlock%2BServer%2BPack-1.4.zip
```

## Unzip to the minecraft-data directory

Now I can unzip my mods into the `minecraft-data` directory.

```bash
unzip One+Block+Server+Pack-1.4.zip -d minecraft-data
```

## Running the server with docker

I run the minecraft server with docker, which is setup to mount the
minecraft-data directory.

[[ til/docker-minecraft-server ]]

A bit more on that in the other post, but when I download the whole modpack
like this I make these changes to my docker compose. (commented out lines)

```yaml
version: "3.8"

services:
  mc:
    container_name: walkercraft
    image: itzg/minecraft-server:java8
    environment:
      EULA: "TRUE"
      TYPE: "FORGE"
      VERSION: 1.15.2
      # MODS_FILE: /extras/mods.txt
      # REMOVE_OLD_MODS: "true"
    tty: true
    stdin_open: true
    restart: unless-stopped
    ports:
      - 25565:25565
    volumes:
      - ./minecraft-data:/data
      # - ./mods.txt:/extras/mods.txt:ro

volumes:
  data:
```
