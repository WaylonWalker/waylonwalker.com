---
date: 2026-08-31T02:05:28Z
templateKey: til
title: "how to set up a boot drive"
tags:
  - "linux"
published: true

---

First Find your usb disk. You should be able to identify it by size and name using lsblk.

``` bash
lsblk -o NAME,SIZE,MODEL,TRAN,RM,MOUNTPOINTS
```

Here I see my good ol Trans-It Drive.  It's not fancy, it wasnt even at the time it was new, but I have it and it works. next we run the ==disk destroyer== `dd` to copy raw bytes right on to the drive.

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