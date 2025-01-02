---
date: 2024-04-01 16:14:47
templateKey: blog-post
title: Thoughts
tags:
  - blog
  - meta
  - slash
published: True

---

These are generally my thoughts on a web page or some sort of url, except a
rare few don't have a link.  These are dual published off of my
[thoughts.waylonwalker.com](https://thoughts.waylonwalker.com) site.  It's a
fully dynamically rendered site 2000's style.  Posts are stored in a database
and instantly available.  Almost all of the posts were written in a small
`<textarea>` field within a chrome extension that I built for it.

These posts are intended to in two ways.  One, link building for the author.  I
hope that I give the people helping me out along the way just a little bit of a
boost.  Two, they serve as a permanant commented bookmark for me to search, and
come back to later when I have forgotten where I have seen something.

* [web](https://waylonwalker.com/thoughts)
* [rss](https://waylonwalker.com/thoughts/rss.xml)

> All thoughts posts cross posted to my site are prefixed with a thought balloon 💭.

## The tech

Since this blog is mostly a tech blog about software development, and my
journey as I learn, lets talk tech.

* python
* fastapi
* htmx
* sqlite
* docker
* fly.io

### fastapi

The core of the site is a python web server running fastapi.  Most of the
endpoints return html via jinja templates to the browser and json to anything
else.  So you go to the list of posts at
[https://thoughts.waylonwalker.com/posts/waylonwalker/?page_size=9999999999 in](<https://thoughts.waylonwalker.com/posts/waylonwalker/?page_size=9999999999> in){.hoverlink}
a web browser it will be a rendered feed, but from curl you will get json.

### htmx

The main page is an infite scrolling feed of the posts.  All loaded in with
htmx.  Which just works so beautifully for this.  I really like python its my
jam, I can make endpoints that return things out of a database very effectively
with it, but it takes me some time to do the js side, htmx just makes these
common patterns available right in html.

### sqlite

The data storage is a sqlite database using the sqlmodel orm.  This was my very
first time using sqlmodel, which is an ORM built on top of pydantic.  It works
really well with fastapi.  The only thing that it lacks is the same history,
community, and stack overflow posts that sqlalchemy has.

### docker

Docker is my go to way for containerizing web applications.  I know it really
well and makes it easy to build and deploy on a number of platforms.

### fly.io

I have this running on fly.io.  Its my first real production application
running on fly.io, and its been great for me.  It runs my container for me,
gives me tools to scale, and ssh right into the running container.  It's still
free for the time being, but goes up quick for my cheap taste if I were to
scale it up much.

Id highly recomend it if you have a server that you want to get running on the
public internet, and you don't want to manage any of your own infrastructure.
