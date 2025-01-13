---
templateKey: blog-post
tags: ['meta', 'slash']
title:  Waylon Walker
date: 2021-11-20T10:38:00
published: true

---

👋 Hi, I am Waylon Walker.  Husband, Father of two, and creator things on the
web, learning, and teaching others.  I play lots of Minecraft, make art, and
skate everyday with my kids.  I finish the day binging episodes of Big Bang
Theory with my wife.

I believe in a decentralized platform where everyone has their own space on
this internet to share their thoughts and ideas.  I created my blogging
platform from scratch to learn about building tools with pluggy and diskcache.
I was frustrated with long build times, black holes of node modules, bloated
pages, and a lack of built in SEO tools.  Instead I built my own under funded,
over dreamed, nearly undocumented framework to that I love and maintain.

I am a Senior Software Engineer specializing in building data pipelines and web
platforms with python.

If you are wondering what all makes up this site and how I think about it
see [[ about-this-site ]] or how the site is built and the specific tech
stack in [[ colophon ]].

## slash pages

Some evergreen pages that are more about me or this site.

{{ '\n'.join(markata.feeds.slashes.map('f"* [[ {slug} ]] - {description}"', sort='slug')) }}
