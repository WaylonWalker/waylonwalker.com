---
date: 2025-11-06 19:57:36
templateKey: blog-post
title: Missing Thoughts
tags:
  - python
published: True

---

No one is perfect, this is why we have things like checkpoints or gates in the
form of pull requests, linting, type checking, and tests.  What happens when
you work on small side projects by yourself that try to be content focused?
What happens when you end up building a lot of the tech under that site and
build it on the bleeding edge of all the tech you make? They are likely missing
these things and occasionally there are some periods of regression.  This is
one reason I really like the term digital garden to describe one's small corner
of the internet where they share their thoughts.


> There will be regressions

## The Signs

There were signs, signs I did not notice

!!! chat

    is your rss feed broken?

    I'm not seeing anything show up in my rss reader

!!! chat-reply me

    Do I not put thoughts in my rss feed, I swore I did.

!!! chat

    my fault, Turns out I must have already clicked it in my reader.

!!! chat-reply me

    great, glat it's working

...But it wasn't

Later this week comes the next sign that I also choose to ignore... Google
search has unindexed a number of pages due to a soft 404.  I don't look at all
of the emails from search console, but I did happen to see this one, and
thought "Huh, that's odd" and went on with my day without another thought on the
issue.

![screenshot-2025-11-04T02-59-44-259Z.png](https://dropper.wayl.one/api/file/5601435b-2c87-4598-b01f-57e5eb737ebe.png)

> Huh, that's odd

## The Fix

I popped open my config and immediately knew what happened.  I turned off some
plugins locally for faster build iteration and that change found its way into
production.... because I have nothing to check myself on other than me.  The
plugin is now back and thoughts are flowing from thoughts.waylonwalker.com to
waylonwalker.com, no problem.

``` bash
❯ git log -p
commit adeb9812f7ecf4d9a68c6aa5e01e549e4dd91285 (HEAD -> main, origin/main, origin/HEAD)
Author: Waylon S. Walker <waylon@waylonwalker.com>
Date:   Mon Nov 3 19:56:40 2025 -0600

    thoughts were missing

diff --git a/markata.toml b/markata.toml
index 59539bab..a55a494d 100644
--- a/markata.toml
+++ b/markata.toml
@@ -31,7 +31,7 @@ hooks = [
     'plugins.chartjs',
     'plugins.md_video',
     'plugins.post_model',
-    # 'plugins.thoughts',
+    'plugins.thoughts',
     # "plugins.wikilink_hover",
     # "plugins.wa_wikilink_hover",
     "plugins.tippy_wikilink_hover",
```
