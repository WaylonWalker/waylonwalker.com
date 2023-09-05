---
date: 2023-03-22 17:31:39
templateKey: blog-post
title: useful btrfs tools
tags:
  - linux
published: false
---

## disk usage

Looking at disk usage on any of these must be done using a tool built for it if
you want an accurate measurement. General purpose tools like du will be
inaccurate as they do not count things like duplicate copies in snapshots.

```bash
❯ sudo btrfs fi usage -T /
[sudo] password for waylon:
Overall:
    Device size:                 465.26GiB
    Device allocated:            251.06GiB
    Device unallocated:          214.20GiB
    Device missing:                  0.00B
    Device slack:                    0.00B
    Used:                        234.44GiB
    Free (estimated):            227.37GiB      (min: 120.27GiB)
    Free (statfs, df):           227.37GiB
    Data ratio:                       1.00
    Metadata ratio:                   2.00
    Global reserve:              478.88MiB      (used: 0.00B)
    Multiple profiles:                  no

                  Data      Metadata System
Id Path           single    DUP      DUP      Unallocated Total     Slack
-- -------------- --------- -------- -------- ----------- --------- -----
 1 /dev/nvme1n1p2 239.00GiB 12.00GiB 64.00MiB   214.20GiB 465.26GiB     -
-- -------------- --------- -------- -------- ----------- --------- -----
   Total          239.00GiB  6.00GiB 32.00MiB   214.20GiB 465.26GiB 0.00B
   Used           225.82GiB  4.31GiB 64.00KiB
```

> -T for tabular format

## mounting the drive

```bash
sudo mkdir /mnt/nvme1n1p2/
sudo mount -o subvol=/ /dev/nvme1n1p2 /mnt/nvme1n1p2
```

## mounting a snapshot

## snapper

## btdu

```bash
sudo btdu /mnt/nvme1n1p2
```

```bash
 btdu v0.5.0 @ /mnt/nvme1n1p2
--- / -----------------------------------------------------------------------------------  ~5.974 GiB [          ] /<DUP>  ~239.1 GiB [##########] /<SINGLE>

--- Details: ----------------------------------------------------------------------------
- Full path: /mnt/nvme1n1p2/
- Average query duration: 0.0002558 seconds
- Represented size: ~245.0 GiB (607659 samples), ±0.0 B
- Logical offsets: ..., 2659587804610, 2608834997278, 2688762158568

--- Explanation:
Welcome to btdu. You are in the hierarchy root; results will be arranged according to
their block group and profile, and then by path.

Use the arrow keys to navigate, press ? for help.

 Samples: 607659  Resolution: ~422.8 KiB
```

## btrfs-assistant
