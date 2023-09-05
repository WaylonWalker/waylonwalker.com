---
date: 2022-10-18 08:34:25
templateKey: til
title: obs virtual camera on boot
published: true
tags:
  - linux

---

For far too long I have had to fidget with v4l2oloopback after reboot.  I've
had this happen on ubuntu 18.04, 22.04, and arch.

After a reboot the start virtual camera button won't work, It appears and is
clickable, but never turns on.  Until I run this command.

``` bash
sudo modprobe v4l2loopback video_nr=10 card_label="OBS Video Source" exclusive_caps=1
```

!["cell shaded, long, full body, shot of a cybernetic blue soldier with glowing pink eyes looking into a selfie camera with ring light, llustration, post grunge, 4 k, warm colors, cinematic dramatic atmosphere, sharp focus, pink glowing volumetric lighting, concept art by josan gonzales and wlop, by james jean, Victo ngai, David Rubín, Mike Mignola, Laurie Greasley, highly detailed, sharp focus,alien,Trending on Artstation, HQ, deviantart, art by artgem" -s50 -W832 -H416 -C12.0 -Ak_lms -S373882614 ](https://stable-diffusion.waylonwalker.com/000378.373882614.webp)

Today I learned that you can turn on kernel modules through some files in `/etc/modules...`

This is what I did to my arch system to get it to work right after boot.

``` bash
echo "v4l2loopback" | sudo tee /etc/modules-load.d/v4l2loopback.conf
echo "options v4l2loopback video_nr=10 card_label=\"OBS Video Source\" exclusive_caps=1" | sudo tee /etc/modprobe.d/v4l2loopback.conf
```
