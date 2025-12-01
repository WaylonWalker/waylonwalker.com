---
date: 2024-06-01 21:01:26
templateKey: til
title: Latest Page in Markata
published: true
tags:
  - python
  - markata
jinja: false

---


I just implemented a latest blog post link in Markata by asking for the first
post slug from the blog feed.  The implementation uses the jinja_md plugin to
render jinja against the markdown and a <meta> tag to redirect.

``` markdown
My latest blog post is [[ {{ markata.feeds.blog.posts[0].slug }} ]].  Click the
link if you are not automatically redirected.

<meta http-equiv="Refresh" content="0; url='/{{ markata.feeds.blog.posts[0].slug }}'" />  
```

## Setting up the feed

Feeds are setup in `markata.toml` configuration.  They provide a handy way to
create an html feed, rss feed, and quickly reference a filtered set of posts
like this.

``` toml
# you will need to enable the jinja_md plugin along with the defaults
[markata]
hooks = [
    "markata.plugins.jinja_md",
    "default",
    ]

# set up the blog feed
[[markata.feeds]]
slug = 'blog'
template = "feed.html"
filter = "date<=today and templateKey in ['blog-post'] and published"
sort = "date"
reverse = true
```

For more information on markata check out the full [[ markata ]] post.
