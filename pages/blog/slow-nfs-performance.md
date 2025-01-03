---
date: 2025-01-02 20:23:10
templateKey: blog-post
title: slow nfs performance
tags:
  - k8s
  - k3s
published: True

---

I'm running a two node k3s cluster at home, I _thought_ I could simply mount an
nfs share on each worker node, and essentially have the same storage accross
all nodes.  I'm already learning why this is not reccommended.

## Slow

I've been running some cronjobs and argo workflows on the second node for
awhile, these are things that run in the background and I don't care if they
take a bit longer to keep my master node freed up for more critical work.

I just started trying to build this site in a cronjob, It was taking 20 minutes
to build, and something I noticed was that markata was taking minutes to run
glob _( search for files )_, normally this happens in a few ms and I never
notice this step.

![image](https://dropper.wayl.one/api/file/57605850-2537-41f9-a3cd-15ff2d41c330.webp)

> I just moved into the master node and the results were wild at ~30x faster

## Permissions

I have seen where you _can_ get diffent permissions on the nfs share based on
user id.  Since I'm homelabbing here I only have one user per machine.  As you
step into enterprise level VMs with tighter controls and dozens of users for
all the different services that might run on it.

I've ran into maybe one issue where I was root in one place and not another,
other than that it's been fine.

## And it only got better

As the cache was warm subsequent runs only got better.

![image](https://dropper.wayl.one/api/file/9681f8a0-2bdc-46a7-9764-2fd58dea6e7b.webp)

> I just checked again and we are now 80x faster

## Conclusion

I don't have the answers yet, it might be my network, it might be nfs settings,
it might be ext4 filesystem.  I have some things to try, but what I do know is
that it is not as easy as I thought it would be just to have the same file
system mounted on both ends and share data between nodes.

I might even go with a complete alternative and use minio as a storage backend,
and sync the files in on each run, this will add some latency to do the sync
each time though.
