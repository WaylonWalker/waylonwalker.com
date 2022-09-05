---
date: 2022-09-05 11:00:46
templateKey: til
title: Setting up snapper on Arch
status: 'draft'
tags:
  - linux

---

https://www.youtube.com/watch?v=_97JOyC1o2o

```
snapper
snap-pac
grub-btrfs
```

## /.snapshots already exists error

When I started running `sudo snapper -c root create-config /`  I ran into the
following error.

![snapshots-already-exists](https://screenshots.waylonwalker.com/snapshots-already-exists.webp)

```
Creating config failed (creating btrfs subvolume .snapshots failed since it already exists).
```

## remove existing snapshots

``` bash
sudo umount /.snapshots
sudo rm -r /.snapshots
```

## configure snapper

``` bash
sudo snapper -c root create-config /
sudo snapper -c home create-config /home
```

## btrfs subvolumes

``` bash
sudo btrfs subvolume list /
```

![btrfs-subvolume-list](https://screenshots.waylonwalker.com/btrfs-subvolume-list.webp)

``` bash
sudo btrfs subvolume delete /.snapshots
sudo mkdir /.snapshots
```

##

``` bash
# you might not see snapshots mounted yet
lsblk

# if you check fstab you will see an entry for it
cat /etc/fstab

# mount it
sudo mount -a

# now you should see /.snapshots mounted
lsblk
```

You should now see `.snapshots` in mountpoints.

![lsblk-snapshots](https://screenshots.waylonwalker.com/lsblk-snapshots.webp)

## Setting the default to @

so that you can boot into snapper snapshots

``` bash
sudo btrfs subvol get-default /
sudo btrfs subvol list /
```

![btrfs-subvol-get-default](https://screenshots.waylonwalker.com/btrfs-subvol-get-default.webp)

``` bash
sudo btrfs subvol set-default 256 /
sudo btrfs subvol get-default /
## ID 256 gen 105268 top level 5 path @
```

![btrfs-subvol-set-default](https://screenshots.waylonwalker.com/btrfs-subvol-set-default.webp)

## snapper ls

``` bash
sudo snapper ls
```

![snapper-ls-init](https://screenshots.waylonwalker.com/snapper-ls-init.webp)

leaving off for now

https://youtu.be/_97JOyC1o2o?t=909
