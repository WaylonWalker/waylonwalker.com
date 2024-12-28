---
date: 2024-12-27 08:55:50
templateKey: blog-post
title: setting up ucore-zfs
tags:
  - linux
published: True

---

I just setup my oldest hardware on the newest hotest server distro ucore-zfs.
This is a gateway FX6860 manufactured in 2010.

## Immutable is the future

My current boot log shows that I first started daily driving bazzite back in
August 2024.  I've been hapily using it since my arch install was plaugued
with a crippling display driver error, or something that would lock the display
for minutes every 30s or so, it became unusable.  I switched because this is
  what I put my son on and it was working great for him.

``` bash
waylon@razorcrest:~$ journalctl --list-boots
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
-19 7e6e154d2609407da24fa12814eadbd7 Thu 2024-08-29 16:15:15 CDT Thu 2024-08-29 17:37:25 CDT
```

Four months later and I am really loving the immutable distro experience.  My
base system gets fresh reliable updates, and I barely install anything directly
on it, a handful of things are snaps or flatpaks from the discover store, but
my main workflow is now in distrobox.  It has been rock solid reliable, and
just works.

## The Hardware

This gem is running a an intel i7-2600 (4) @ 3.80 ghz with 16gb of ram.  I've
maxed out the ram that the motherboard will allow me.  I may have even forgot
about this limitation and ordered a 2x32gb setup for it and it did nothing.
That's now sitting in my new k3s master node.

![image](https://dropper.wayl.one/api/file/36b2d93e-ddb1-4a13-89bd-471cd5e42f14.webp)

Here's a B&H photo post of the machine, she is big and heavy but still working.

![image](https://dropper.wayl.one/api/file/75c30c6e-421b-4d99-8a22-1d552ca541fe.webp)

I'm a big fan of keeping these old machines running and avoiding the e-waste
pile, great for running a home lab.  Admittedly this is one is probably on its
last leg, dell optiplexes are pretty cheap and run circles around this one, so
this one is become my experimental setup for trying new things like core-os.

## Get Password Hash

We will need to create a password hash for the root user to put into our ignition file.

``` bash
podman run -ti --rm quay.io/coreos/mkpasswd --method=yescrypt
Password:
$y$j9T$0ZsoVynV7y0Z7/l6588Ba1$VZT0uCGP0CnYSX/EArCvYMuo3q.gnyOnk1RO6.HDNDB
```

## Get SSH Pub Key

Generate an ssh key using the `ssh-keygen` command.

``` bash
$ ssh-keygen -t ed25519 -C "waylon@waylonwalker.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/var/home/core/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /var/home/core/.ssh/id_ed25519
Your public key has been saved in /var/home/core/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:xVJAVreKVILOnxTDxK88RyMwhdDCBMnjMSGU7rsAqwQ waylon@waylonwalker.com
The key's randomart image is:
+--[ED25519 256]--+
|oo+*oo OBo+ .    |
| o* o *.== . .   |
|.. + + oo+o .    |
| ..   o.o++.     |
|E      +S=..     |
|oo      * .      |
|o..      o       |
|+.               |
|...              |
+----[SHA256]-----+
```

Now copy your public key into the ignition file from your local machine

``` bash
$ cat ~/.ssh/id_ed25519.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPY73r4EU9wm/26/rTpx/uvAyInmbQ/k+l04eadSahD0 waylon@waylonwalker.com
```

## ucore-autorebase.butane

I got my ignition file from
[ucore/ucore-autorebase](https://github.com/ublue-os/ucore/blob/main/examples/ucore-autorebase.butane).
Put my secret values into it and used it.

<https://github.com/ublue-os/ucore/blob/main/examples/ucore-autorebase.butane>

```
variant: fcos
version: 1.4.0
passwd:
  users:
    - name: core
      ssh_authorized_keys:
        - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPY73r4EU9wm/26/rTpx/uvAyInmbQ/k+l04eadSahD0 waylon@waylonwalker.com
      password_hash: $y$j9T$0ZsoVynV7y0Z7/l6588Ba1$VZT0uCGP0CnYSX/EArCvYMuo3q.gnyOnk1RO6.HDNDB
storage:
  directories:
    - path: /etc/ucore-autorebase
      mode: 0754
systemd:
  units:
    - name: ucore-unsigned-autorebase.service
      enabled: true
      contents: |
        [Unit]
        Description=uCore autorebase to unsigned OCI and reboot
        ConditionPathExists=!/etc/ucore-autorebase/unverified
        ConditionPathExists=!/etc/ucore-autorebase/signed
        After=network-online.target
        Wants=network-online.target
        [Service]
        Type=oneshot
        StandardOutput=journal+console
        ExecStart=/usr/bin/rpm-ostree rebase --bypass-driver ostree-unverified-registry:ghcr.io/ublue-os/ucore:stable
        ExecStart=/usr/bin/touch /etc/ucore-autorebase/unverified
        ExecStart=/usr/bin/systemctl disable ucore-unsigned-autorebase.service
        ExecStart=/usr/bin/systemctl reboot
        [Install]
        WantedBy=multi-user.target
    - name: ucore-signed-autorebase.service
      enabled: true
      contents: |
        [Unit]
        Description=uCore autorebase to signed OCI and reboot
        ConditionPathExists=/etc/ucore-autorebase/unverified
        ConditionPathExists=!/etc/ucore-autorebase/verified
        After=network-online.target
        Wants=network-online.target
        [Service]
        Type=oneshot
        StandardOutput=journal+console
        ExecStart=/usr/bin/rpm-ostree rebase --bypass-driver ostree-image-signed:docker://ghcr.io/ublue-os/ucore:stable
        ExecStart=/usr/bin/touch /etc/ucore-autorebase/signed
        ExecStart=/usr/bin/systemctl disable ucore-signed-autorebase.service
        ExecStart=/usr/bin/systemctl reboot
        [Install]
        WantedBy=multi-user.target butane
```

## Creating an ignition file

``` bash
podman run --interactive --rm --security-opt label=disable \
        --volume ${PWD}:/pwd --workdir /pwd quay.io/coreos/butane:release \
        --pretty --strict ucore-autorebase.butane >transpiled_config.ign
```

## Getting zfs

Now this is where I realized I went wrong and wished I would have paid
attention to the autorebase.butane file, it did not use the zfs flavor ucore.
Luckily they make it wildly easy to rebase between these base images.

I needed to run this to rebase into the zfs flavor.

``` bash
/usr/bin/rpm-ostree rebase --bypass-driver ostree-unverified-registry:ghcr.io/ublue-os/ucore:stable-zfs
```

This was the output.

``` bash
core@falcon-FX6860:~$ /usr/bin/rpm-ostree rebase --bypass-driver ostree-unverified-registry:ghcr.io/ublue-os/ucore:stable-zfs
==== AUTHENTICATING FOR org.projectatomic.rpmostree1.rebase ====
Authentication is required to switch to a different base OS
Authenticating as: CoreOS Admin (core)
Password:
==== AUTHENTICATION COMPLETE ====
Pulling manifest: ostree-unverified-registry:ghcr.io/ublue-os/ucore:stable-zfs
Importing: ostree-unverified-registry:ghcr.io/ublue-os/ucore:stable-zfs (digest: sha256:8ebae90f6844949044c026d7ba05c035956992b68e13bdcbd9158a37beda571e)
ostree chunk layers already present: 51
custom layers needed: 2 (492.9 MB)
Fetching layer sha256:67f3c0e0e0fe (269.7 MB)... done
Fetching layer sha256:25992805e895 (223.1 MB)... done
Staging deployment... done
Upgraded:
  cockpit-bridge 330-1.fc41 -> 331-1.fc41
  cockpit-networkmanager 330-1.fc41 -> 331-1.fc41
  cockpit-selinux 330-1.fc41 -> 331-1.fc41
  cockpit-storaged 330-1.fc41 -> 331-1.fc41
  cockpit-system 330-1.fc41 -> 331-1.fc41
Added:
  groff-base-1.23.0-7.fc41.x86_64
  kmod-zfs-2.2.7-1.fc41.x86_64
  libnvpair3-2.2.7-1.fc41.x86_64
  libuutil3-2.2.7-1.fc41.x86_64
  libzfs5-2.2.7-1.fc41.x86_64
  libzpool5-2.2.7-1.fc41.x86_64
  lm_sensors-libs-3.6.0-20.fc41.x86_64
  lzop-1.04-15.fc41.x86_64
  mbuffer-20241007-1.fc41.x86_64
  perl-AutoLoader-5.74-512.fc41.noarch
  perl-B-1.89-512.fc41.x86_64
  perl-Capture-Tiny-0.48-21.fc41.noarch
  perl-Carp-1.54-511.fc41.noarch
  perl-Class-Struct-0.68-512.fc41.noarch
  perl-Config-IniFiles-3.000003-14.fc41.noarch
  perl-Data-Dumper-2.189-512.fc41.x86_64
  perl-Digest-1.20-511.fc41.noarch
  perl-Digest-MD5-2.59-5.fc41.x86_64
  perl-DynaLoader-1.56-512.fc41.x86_64
  perl-Encode-4:3.21-511.fc41.x86_64
  perl-Errno-1.38-512.fc41.x86_64
  perl-Exporter-5.78-511.fc41.noarch
  perl-Fcntl-1.18-512.fc41.x86_64
  perl-File-Basename-2.86-512.fc41.noarch
  perl-File-Path-2.18-511.fc41.noarch
  perl-File-Temp-1:0.231.100-511.fc41.noarch
  perl-File-stat-1.14-512.fc41.noarch
  perl-FileHandle-2.05-512.fc41.noarch
  perl-Getopt-Long-1:2.58-2.fc41.noarch
  perl-Getopt-Std-1.14-512.fc41.noarch
  perl-HTTP-Tiny-0.090-1.fc41.noarch
  perl-IO-1.55-512.fc41.x86_64
  perl-IO-Socket-IP-0.43-1.fc41.noarch
  perl-IO-Socket-SSL-2.089-1.fc41.noarch
  perl-IO-stringy-2.113-15.fc41.noarch
  perl-IPC-Open3-1.22-512.fc41.noarch
  perl-MIME-Base32-1.303-21.fc41.noarch
  perl-MIME-Base64-3.16-511.fc41.x86_64
  perl-NDBM_File-1.17-512.fc41.x86_64
  perl-Net-SSLeay-1.94-7.fc41.x86_64
  perl-POSIX-2.20-512.fc41.x86_64
  perl-PathTools-3.91-511.fc41.x86_64
  perl-Pod-Escapes-1:1.07-511.fc41.noarch
  perl-Pod-Perldoc-3.28.01-512.fc41.noarch
  perl-Pod-Simple-1:3.45-511.fc41.noarch
  perl-Pod-Usage-4:2.03-511.fc41.noarch
  perl-Scalar-List-Utils-5:1.68-1.fc41.x86_64
  perl-SelectSaver-1.02-512.fc41.noarch
  perl-Socket-4:2.038-511.fc41.x86_64
  perl-Storable-1:3.32-511.fc41.x86_64
  perl-Symbol-1.09-512.fc41.noarch
  perl-Sys-Hostname-1.25-512.fc41.x86_64
  perl-Term-ANSIColor-5.01-512.fc41.noarch
  perl-Term-Cap-1.18-511.fc41.noarch
  perl-Text-ParseWords-3.31-511.fc41.noarch
  perl-Text-Tabs+Wrap-2024.001-511.fc41.noarch
  perl-Time-Local-2:1.350-511.fc41.noarch
  perl-URI-5.30-1.fc41.noarch
  perl-base-2.27-512.fc41.noarch
  perl-constant-1.33-512.fc41.noarch
  perl-if-0.61.000-512.fc41.noarch
  perl-interpreter-4:5.40.0-512.fc41.x86_64
  perl-libnet-3.15-512.fc41.noarch
  perl-libs-4:5.40.0-512.fc41.x86_64
  perl-locale-1.12-512.fc41.noarch
  perl-mro-1.29-512.fc41.x86_64
  perl-overload-1.37-512.fc41.noarch
  perl-overloading-0.02-512.fc41.noarch
  perl-parent-1:0.242-1.fc41.noarch
  perl-podlators-1:6.0.2-2.fc41.noarch
  perl-vars-1.05-512.fc41.noarch
  pv-1.8.14-2.fc41.x86_64
  python3-cffi-1.17.0-1.fc41.x86_64
  python3-ply-3.11-25.fc41.noarch
  python3-pycparser-2.20-18.fc41.noarch
  python3-pyzfs-2.2.7-1.fc41.noarch
  sanoid-2.2.0-1.fc41.ucore2.noarch
  sysstat-12.7.6-2.fc41.x86_64
  zfs-2.2.7-1.fc41.x86_64
  zfs-dracut-2.2.7-1.fc41.noarch
Changes queued for next boot. Run "systemctl reboot" to start a reboot
```

For some reason I double checked, and runnign it a second time gave me this.

``` bash
core@falcon-FX6860:~$ sudo rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/ucore:stable-zfs
Pulling manifest: ostree-image-signed:docker://ghcr.io/ublue-os/ucore:stable-zfs
Staging deployment... done
Changes queued for next boot. Run "systemctl reboot" to start a reboot
```

## ZFS

Once I rebooted I had all of my necessary zfs utilities that I needed.

## connecting nfs

The last thing I wanted to do was to mount an nfs share from my master node so
that they can share a storage backend.  I found that nfs was already in the host and ready to go.

``` bash
sudo mkdir /mnt/vault/nfs
sudo mount -t nfs <nfs server ip>:/mnt/vault/nfs /mnt/vault/nfs
```
