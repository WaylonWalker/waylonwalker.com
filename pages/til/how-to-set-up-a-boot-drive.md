---
date: 2026-08-31T02:05:28Z
templateKey: til
title: "how to set up a boot drive"
tags:
  - "linux"
published: true
authors:
  - waylon
  - id: gpt-6-luna
    role: copy editor
    details: "Corrected spelling and grammar with GPT-6 Luna."
editorial_history:
- schema_version: 1
  event_id: bed11545-87fe-4d62-851a-71086e431cc1:pages/til/how-to-set-up-a-boot-drive.md
  author: gpt-6-luna
  role: copy-editor
  action: edited
  recorded_by: gpt-6-codex
  recorded_at: '2026-10-11T15:07:10.750991+00:00'
  base_commit: 5de74ebc0a1023cf815006572f5cb63816ad81db
  commit: d3b1fe7083dbeffea0e28578ec8c1d0b2833e478
  path: pages/til/how-to-set-up-a-boot-drive.md
  content_digest: sha256:2dbb5bb1ccf08bd165fb66b7cb3a223554badec3a96b92d15defbeb9ce7e6149
  digest_version: editorial-v1
  file_url: https://github.com/waylonwalker/waylonwalker.com/blob/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478/pages/til/how-to-set-up-a-boot-drive.md
  diff_url: https://github.com/waylonwalker/waylonwalker.com/commit/d3b1fe7083dbeffea0e28578ec8c1d0b2833e478#diff-0b144b4c4e1b9bfa3dd6b567a2a5e0e076837417c1ce90eccee9cf87dd3a0634
  summary: Imported GPT-6 Luna copy edits after the owner confirmed exclusive authorship
    of these post diffs.
---

First, find your usb disk. You should be able to identify it by size and name using lsblk.

``` bash
lsblk -o NAME,SIZE,MODEL,TRAN,RM,MOUNTPOINTS
```

Here I see my good ol Trans-It Drive.  It's not fancy.  It wasn't even at the time it was new, but I have it and it works. Next, we run the ==disk destroyer== `dd` to copy raw bytes right on to the drive.

!!! warning

    
    This is a full reformat of the drive, nothing on the drive will be recoverable afterwards.  I keep this drive around as a boot disk and it just changes distro occasionally.

``` bash
sudo dd if=~/Downloads/omarchy-4.0.1.iso of=/dev/sdb bs=4M status=progress conv=fsync
```

!!! note

    Don't forget the bs, the default block size is so slow it will take an eternity to copy a linux iso on to a boot drive.

## Installing omarchy

I wanted to give omarchy quatro a try, here is the session to get it.

``` bash
~  NO PYTHON VENV SET  USING SYSTEM NVIM
❯ lsblk -o NAME,SIZE,MODEL,TRAN,RM,MOUNTPOINTS
NAME          SIZE MODEL                      TRAN   RM MOUNTPOINTS
sda         119.2G SAMSUNG MZNLN128HAHQ-000H1 sata    0 
├─sda1          1G                                    0 
└─sda2      118.2G                                    0 
sdb           7.6G Trans-It Drive             usb     1 
├─sdb1        5.8G                                    1 
└─sdb2         23M                                    1 
zram0        93.9G                                    0 [SWAP]
nvme0n1     931.5G Samsung SSD 980 1TB        nvme    0 
├─nvme0n1p1     1G                            nvme    0 /boot
└─nvme0n1p2 930.5G                            nvme    0 /var/log
                                                        /var/cache/pacman/pkg
                                                        /home
                                                        /

~  NO PYTHON VENV SET  USING SYSTEM NVIM
❯ sudo dd if=~/Downloads/omarchy-4.0.1.iso of=/dev/sdb bs=4M status=progress conv=fsync
```