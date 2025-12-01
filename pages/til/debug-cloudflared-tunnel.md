---
date: 2024-12-03 15:36:37
templateKey: til
title: debug cloudflared tunnel
published: true
tags:
  - homelab
  - networking

---

I've been debugging a cloudflared tunnel issue in my homelab all day today, and
getting really frustrated.  My issue ended up being that it was running twice,
once without the correct config file and another with it.  I believe that
cacheing may have compounded the issue.

> In yesterday's post I setup a cloudflared tunnel on my ubuntu server to
> expose applications running on the server to the internet.  I'm setting up a
> new server and running cloudflared in its own vm.

[[ setup-cloudflared-tunnel-on-ubuntu ]]

## Check that dns is pointing to the correct tunnel

``` bash
dig subdomain.example.com
traceroute subdomain.example.com
```

## Check that the tunnel is running

``` bash
export CLOUDFLARED_TUNNEL_ID = "my-tunnel-id"

cloudflared tunnel list
cloudflared tunnel info $CLOUDFLARED_TUNNEL_ID
```
