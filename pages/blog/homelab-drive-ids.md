---
date: 2025-03-26 11:22:07
templateKey: blog-post
title: homelab drive ids
tags:
  - homelab
published: True

---

``` bash
ls -l /dev/disk/by-id/
```

Drive Bay 1
ata-ST4000VN008-2DR166_ZDHBZSWZ

+-------------------------------------------------------------------------+
| [ Power]  [ Reset ]                                                     |
+-------------------------------------------------------------------------+
| [ BAY 5 ]  3TB WD30EFRX WMC4N0D3J9R7 ext4 /mnt/sdf4                     |
+-------------------------------------------------------------------------+
| [ BAY 4 ]  14TB EXOS ZTM09R9N zfs main pool mirror /mnt/main            |
+-------------------------------------------------------------------------+
| [ BAY 3 ]  14TB EXOS ZTM0AALS zfs main pool mirror /mnt/main            |
+-------------------------------------------+
| [ BAY 2 ]  4TB IRONWOLF ZDHBZV3N zfs tank pool mirror /mnt/tank         |
+-------------------------------------------------------------------------+
| [ BAY 1 ]  4TB IRONWOLF ZDHBZSWZ zfs tank pool mirror /mnt/tank         |
+-------------------------------------------------------------------------+
