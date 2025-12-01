---
date: 2025-10-24 14:19:49
templateKey: blog-post
title: First 3d Printed Threads
tags:
  - python
published: True

---

Working on an upcoming project that requires some threaded screws.  Trying to
keep a low budget on this one with as much to come off of the printer as I can.
It might become a slant3d portals product if it works out.  I always like
making test prints for stuff like this especially to see how the feel is off of
the printer that is going to print the final product and take much longer.
First try was a success.

![b485b759-719a-4aa0-aa8d-f98e0a5e1ac3-1080p.mp4](https://dropper.wayl.one/api/file/21498d89-41e1-45de-9b35-e3dd059de505.mp4)

## What worked

I started out looking up standard half inch thread pitch and size, but ran out
of time to get the exact profile of a half inch bolt, so I will need to fix
that later.  Th

![Boolean operation to remove threads from the block with 0.1mm offset](https://dropper.wayl.one/api/file/376691bc-8aec-40f7-9137-9338cc2265b2.png)

The print orientation is critical for strength here.  This part is a full 1/2:
so it should be strong either way, but to make sure we are printing the bolt
horizontally to get nice long print layers.  To do this we have to give it a
bit of a flat spot on the top and bottom.  This does not hurt performance, if
anything it probably helps give some room for poor tolerances.

![Print orientation of the test parts](https://dropper.wayl.one/api/file/60f37fc2-7e4b-4671-9bb4-582715e1534d.webp)

* .5" od
* 13tpi pitch
* non-standard profile... kids needed me and I called it good enough to run a test.
* 0.1mm offset on all surfaces
* external threads printed horizontally
* internal threads printed vertically
* Chamfer all lead-in/lead-out

