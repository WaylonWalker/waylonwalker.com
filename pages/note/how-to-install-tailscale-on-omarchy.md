---
template: note
date: 2026-11-22
published: true
---


## Install

++super+space++ tail ++enter++


![pasted-image](<https://dropper.waylonwalker.com/file/d3696087-c7a1-4b42-a4a9-942fc5ea4dcf.webp>)


Then you will be asked for sudo password, and be asked to log into tailscale through a link printed to the terminal.

## on **boot**

To make it auto start on reboot. 

``` bash
sudo systemctl enable --now tailscaled
```