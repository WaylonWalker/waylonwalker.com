---
date: 2022-02-07 02:35:21.230511
templateKey: til
title: Running a Minecraft Server in Docker
tags:
  - docker
  - homelab
  - minecraft
  - gaming

---

I've ran a Minecraft server at home since December 2017 for me and my
son to play on.  We start a brand new one somewhere between every day
and every week.  The older he gets the longer the server lasts.

In all these years, I've been popping open the command line and running
the server manually, and even inside of Digital Ocean occasionally to
play a more public server with a friend.

My buddy Nic has been sharing me some of his homelab setup, and it's
really got me to thinking about what I can run at home, and Dockerizing
all the things.  Today I found a really sweet github repo that had a
minecraft server running in docker with a pretty incredible setup.

I ended up running the first thing in the Readme that included a volume
mount.  If you are going to run this container, I HIGHLY reccomend that
you make sure that you have your world volume mounted, otherwise it will
die with your docker container.

## Docker Compose

With the following stored as my `docker-compose.yml` in a brand new and
otherwise empty directory I was ready to start the server for the night.

``` yaml
version: "3"

services:
  mc:
    container_name: walkercraft
    image: itzg/minecraft-server
    ports:
      - 25565:25565
    environment:
      EULA: "TRUE"
    tty: true
    stdin_open: true
    restart: unless-stopped
    volumes:
      # attach a directory relative to the directory containing this compose file
      - ./minecraft-data:/data
```

To start the server we open up the terminal in this directory and run
the follwing command.

``` bash
docker compose up -d
```

Once its up and running we can run commands on the server simply by
attaching to it.

``` bash
docker attach walkercraft
```

## A few common commands we run in the server

We play very casually most of the time so we will set keepInventory to
true so that we do not loose our inventory when we die.  Sometimes we
also op ourselve so that we can toggle gamemode into creative.

```bash
# set the game to keep your inventory when you die.
/gamrule keepInventory true

# give everyone operater priveledges to they can run commands
/op @a

# give playername op
/op playername
```
