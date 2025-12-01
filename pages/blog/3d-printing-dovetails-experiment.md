---
date: 2025-10-12 20:34:35
templateKey: blog-post
title: 3d Printing Dovetails Experiment
tags:
  - 3d-printing
published: True

---

I hit an issue with 3d printing oversized parts that I have not hit before.
I'm working on some jigs for an upcoming woodworking project that will involve
a lot of repetition.  We want to utilize some dowel joinery and jigs for
consistency.  These parts will be up to 20in  in length this is much larger
than my print bed.

## I've fit things together before

Here's where I went wrong, I wasn't really thinking through my previous
applications.  They've all been slip fit, primarily print in place joints that
need to move.  My go to offset for print in place on my printer is 0.2mm,
sometimes 0.1mm depending on the scale.


![knife sharpener double hinge first try](https://dropper.wayl.one/api/file/30335f07-9cac-4e66-b908-f0e3cfbf7582.mp4)

A live hinged [[ knife-sharpener-double-hinge-first-try ]].

![a box of caps and a macropad](https://dropper.wayl.one/api/file/ea421e67-5cb0-4a9f-be14-08a5004df493.jpg)

And in the hinges of [[ a-box-of-caps-and-a-macropad ]].

## Experimenting for feel

Fitment like this is a lot dependent on the tolerences of your printer and the
feel you are going for.  I went to school as a mechanical engineer and theres a
lot of science behind press fit joints, that's not happening in my house on my
desktop printer.  Most of us don't have that kind of ability to gauge our
outputs so I'm doing like a cook in the kitchen and going for feel.

[![PXL_20251013_011946949.webp](https://dropper.wayl.one/api/file/e23a6965-a84b-4eb0-9d84-73ddc831949f.webp)](https://dropper.wayl.one/api/file/4a90cbe1-9124-4a6b-baf9-1545afe3dd00.webp)

> Here are all of the experiements lined up.

## Fillets

I again, I feel like I should have known better.  3d printers generally have
0.4mm nozzles, common sizes you can get 0.2mm, 0.4mm, 0.6mm, and 0.8mm.  This
leaves us with the sharpest corner we can do at 0.2mm.


![b49ea6a6-115b-44f8-99c0-d5f58f7c9940.webp](https://dropper.wayl.one/api/file/5533d56c-00e4-486d-b2a0-a994bbd1f1a4.webp)

> Diagram courtesy of gpt-5.

### Potentially overkill

In order to make sure that the flat edges of the dovetails are what are making
contact and not corners binding I made the inside fillet 0.6mm and the outside
0.4mm.  This 0.4mm radius (0.8mm diameter) is double my nozzle size, and will
cause the printer to follow a smooth curve rather than start and stop and
potentially overflow a bit.  This difference in fillet size will also leave a
little room for error and allow the important flat faces to mate together.

![fillets.webp](https://dropper.wayl.one/api/file/ec3a9841-9b39-4180-96e4-613be79ee793.webp)

Here are the test results after filleting the edges of the dovetails to
compensate for printer errors.

!!! vsplit Fillets

    !!! vsplit Before Fillets

        [![PXL_20251013_014851451.webp](https://dropper.wayl.one/api/file/3ed04466-6303-4e72-b292-0f446785c9cb.webp)](https://dropper.wayl.one/api/file/a289064c-960c-4f83-8b92-ec8524f51690.webp)

    !!! vsplit After Fillets

        [![PXL_20251013_014909663.webp](https://dropper.wayl.one/api/file/149a93d0-bce7-45df-845d-77c7a16c3218.webp)](https://dropper.wayl.one/api/file/ea3f4651-68b7-4aac-a00d-2f11db1f11a3.webp)


## TLDR What works for me

After all of this, turns out that common sense kinda just works here, 0mm
offset works really well on my printer, and leaving room in the corners to keep
them from binding up helps a bit, but is probably unnecessary.

* 0mm offset
* 0.6mm inside fillet
* 0.4mm outside fillet

