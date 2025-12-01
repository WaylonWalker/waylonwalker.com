---
date: 2024-12-02 15:43:45
templateKey: til
title: setup cloudflared tunnel on ubuntu
published: true
tags:
  - homelab
  - networking

---

I run a cloudflared tunnel on my ubuntu server to expose applications running
on the server to the internet.  I'm setting up a new server and running
cloudflared in its own vm.

## Get the cloudflared binary

```bash
sudo wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O /usr/local/bin/cloudflared

sudo chmod +x /usr/local/bin/cloudflared
```

##

Now setup the config directory.  For the systemd service to work, the config
file needs to be in /etc/cloudflared.  I like to give my user rights to edit
the config file without being sudo, we will do that here by creating a group
`cloudflared`, add ourselves to the group, give ownership of `/etc/cloudflared`
to the group, give group write access to the directory, and refresh groups.

``` bash
sudo mkdir -p /etc/cloudflared
sudo groupadd cloudflared
sudo usermod -aG cloudflared $USER
sudo chown -R root:cloudflared /etc/cloudflared
sudo chmod g+w /etc/cloudflared
newgrp cloudflared
```

## login

Now we can log into the domain zone with cloudflared.

```bash
cloudflared tunnel login
```

This will give a url, follow it in a browser to log in.

``` bash
cloudflared tunnel create <NAME>
mv ~/.cloudflared/cert.pem /etc/cloudflared/cert.pem
mv ~/.cloudflared/<tunnel-id>.json /etc/cloudflared/<tunnel-id>.json
```

## config

Now setup config.  For the systemd service to work, the config file needs to be
in /etc/cloudflared.  The config that I have provided below will expose
localhost:8000 to tester.example.com

``` bash
export CLOUDFLARED_TUNNEL_ID=$(ls /etc/cloudflared/*.json | xargs -n 1 basename | sed 's/\.json$//')
mv ~/.cloudflared/${CLOUDFLARED_TUNNEL_ID}.json /etc/cloudflared/${CLOUDFLARED_TUNNEL_ID}.json
mv ~/.cloudflared/cert.pem /etc/cloudflared/cert.pem
echo "
tunnel: $(CLOUDFLARED_TUNNEL_ID)
credentials-file: /etc/cloudflared/$(CLOUDFLARED_TUNNEL_ID).json
ingress:
  - hostname: tester.example.com
    service: http://localhost:8000
  - service: 'http_status:404'
" >> /etc/cloudflared/config.yaml
```

## dns

Now to get a dns record for tester.example.com to point to the cloudflared
tunnel.

```bash
cloudflared tunnel route dns $(CLOUDFLARED_TUNNEL_ID) tester.example.com
```

## systemd

Now install the systemd service.

``` bash
sudo cloudflared service install
```

```bash
sudo systemctl status cloudflared.service
# if its not running
sudo systemctl start cloudflared.service
```
