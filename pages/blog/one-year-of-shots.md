---
date: 2025-12-09 12:44:39
templateKey: blog-post
title: One Year Of Shots
tags:
  - python
published: False

---

I've been running my shot scraper api for a year now.  It creates og images for
my website and thumbnails for my [[ reader ]] using a headless chrome instance.

* 25870 shots
* 73 shots per day on average
* 12-09-2025 first shot taken

## Histogram

![histogram of shots](https://dropper.wayl.one/file/63705078-3342-4807-b5fd-46a0860efc27.webp)
> a histogram of shot counts by day

You can see in the histogram that I've had a few big spike days, This has been
mostly for days that I've integrated into a new service or changed the
endpoint.  On February 13, 2025 I swapped over from using the post to using
template specific to open graph images.

``` diff
-content = "https://shots.wayl.one/shot/?url={{ config.url }}{{ post.slug }}&height=600&width=1200&scaled_width=1200&scaled_height=600"
+content = "https://shots.wayl.one/shot/?url={{ config.url }}{{ post.slug }}/og/&height=600&width=1200&scaled_width=1200&scaled_height=600"
```

!!! vsplit Image Comparison

    !!! vsplit Original Post Image

        ![](https://shots.wayl.one/shot/?url=https://dev.waylonwalker.com/one-year-of-shots/&height=600&width=1200&scaled_width=1200&scaled_height=600)

        > originally I simply used an image of the post itself

    !!! vsplit New OG Image

        ![](https://shots.wayl.one/shot/?url=https://dev.waylonwalker.com/one-year-of-shots/og/&height=600&width=1200&scaled_width=1200&scaled_height=600)

        > In Feb 2025 I made OG specific templates to use for the OG images.

> Swapping to og images

## Collage

For fun I made a collage of all the shots.  It's cool to see all of these
together, I remember a lot of the thumbnails and posts.  Many of them from my
rss reader.

![collage of shots](https://dropper.wayl.one/file/5d4b46a6-79d6-4320-bf7d-f917c862c57d.webp)
> collage of all shots, click to see full size

I tried to make a video collage, but turns out it takes a long time to show all
25k shots in video form.  It also turned out to be a bit of a strobe as I don't
yet have it figured out how to dark mode in headless chrome.

![video collage of shots](https://dropper.wayl.one/file/1c629d32-4284-4c71-a4f7-62d82e445c7d.webm)
> video collage of 600 shots, I tried to include all, but even at 20fps its a 20 minute video.
