---
date: 2025-01-29 20:28:36
templateKey: blog-post
title: Markata DidYouMean
tags:
  - python
published: True

---

Coming in Markata 0.9.1 is far better documentation. i.e. Documentation that
actually exists for everything.  As part of poking around I realized that I
often go to look up the docs for a plugin and forget that the path is
`/markta/plugins/feeds`, sometimes I might try `/markata/feeds` or
`/plugins/feeds.py` or `/feeds` or I might even forget the plugin name exactly
and try something like `feed` and get a 404.  So I added a  `didyoumean` plugin
to markata that takes care of this.

![screenshot-2025-01-31T14-53-31-264Z.png](https://dropper.waylonwalker.com/api/file/9c1e92dd-4ea1-4b0f-80bc-e6c3414cf219.png){.more-cinematic}

I made a quick recording of this early feature, pay close attention to the url
as it automatically updates to the correct page.

![markata-didyoumean.mp4](https://dropper.waylonwalker.com/api/file/3e9a1af6-59e0-4d0a-9540-2514c492cc49.mp4)

## Happy Path

_direct forward_

If you have one post called `/markata/plugins/feeds`, and it is the only post
called feeds, any combination of `/markata/feeds` or `/plugins/feeds` or
`/feeds` will all automatically redirect with an html page (not a server 3xx)
to the `/markata/plugins/feeds` post.

Here is the snippet that does the redirect.

``` html
<div class="container mx-auto px-4 py-8">
    <h1 class="text-2xl font-bold mb-4">Redirecting...</h1>
    <p class="mb-4">You will be redirected to <a href="/markata/plugins/feeds" class="text-blue-500 hover:underline">/markata/plugins/feeds</a></p>
    <script>window.location.href = "/markata/plugins/feeds";</script>
</div>
```

You won't see it unless you are on a really bad network, or you have js
disabled, but this is what it would look like if you ever saw it.  Notice there
is a backup link if you have js disabled.

![image](https://dropper.waylonwalker.com/api/file/52d95c41-e27a-4a6c-be39-5c57601fc33f.webp)

## Multiple Similar Posts

_list of options_

If you have multiple posts called `didyoumean` from different directories, in
the video I made a clashing post at `/markata/cli/didyoumean` with
`/markata/plugins/didyoumean`.  If you go to `/didyoumean` it will notice that
there are multiple options and present you with a list of all of the potential
pages that match.

![image](https://dropper.waylonwalker.com/api/file/e05f8314-33a3-4dca-90b0-6009b8642c8a.webp)

## Finally No Matches

_404.html_

Last ditch effort is to implement a 404 page.  This page will know all of the
possible paths in your project and give you a list of all the similar pages
more like a traditional `didyoumean` plugin.

![image](https://dropper.waylonwalker.com/api/file/a59c9736-da16-4dce-b867-29679e6b9ec3.webp)
