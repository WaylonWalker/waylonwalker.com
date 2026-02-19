---
title: '💭 simonw/shot-scraper: A command-line utility for taking automat...'
date: 2023-08-16T00:05:33
template: link
link: https://github.com/simonw/shot-scraper
tags:
  - python
  - screenshot
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/simonw/shot-scraper]]

        > A command-line utility for taking automated screenshots of websites


Daaaang, this is such an elegantly simple way to get web screenshots with a cli.  I was literally up and running with two commands on my arch linux machine (which it warned was unsupported by playwright).

``` python
pip install shot-scraper
# Now install the browser it needs:
shot-scraper install
shot-scraper waylonwalker.com
shot-scraper https://datasette.io/ 
shot-scraper https://datasette.io/ -h 1280 -w 1920
shot-scraper https://datasette.io/ -h 480 -w 720
shot-scraper shot --selector '#posts' https://thoughts.waylonwalker.com/post/89
```

> Note `shot-scraper https://datasette.io/ ` is a full length screenshot of the entire page.

Oh and its pretty dang fast, let alone the setup time, this crushes on startup time in my attempts to use a headless browser in the past.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
