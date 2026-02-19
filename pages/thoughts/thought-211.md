---
title: '💭 searching my thoughts locally'
date: 2024-03-07T23:42:00
template: link
link: None
tags:
  - sqlite
  - data
  - blog
  - thoughts
  - thought
  - link
published: true

---

![[None]]

First I need to fetch my thoughts from the api, and put it in a local sqlite database using `sqlite-utils`.

``` bash
fthoughts () {
    # fetch thoughts
    curl 'https://thoughts.waylonwalker.com/posts/waylonwalker/?page_size=9999999999' | sqlite-utils insert ~/.config/thoughts/database2.db post --pk=id --alter --ignore -
}
```

Now that I have my posts in a local sqlite database I can use `sqlite-utils` to enable full text search  and populate the full text search on the post table using the title message and tags columns as search.

``` bash
sthoughts () {
    # search thoughts
    # sqlite-utils enable-fts ~/.config/thoughts/database2.db post title message tags
    # sqlite-utils populate-fts ~/.config/thoughts/database2.db post title message tags
    sqlite-utils search ~/.config/thoughts/database2.db post "$*" | ~/git/thoughts/format_thought.py | bat --style=plain --color=always --language=markdown
}

alias st=sthoughts
```

Now I am ready to search my thoughts, which is a tiny blog format that I created mostly for  leaving my own personal comment on web pages, so most of them have a link to some other online content, and their title is based on the authors title.

<img src="https://vhs.charm.sh/vhs-5UMOPkPbr43X3PKi6q1sih.gif" alt="Made with VHS">
<a href="https://vhs.charm.sh">
  <img src="https://stuff.charm.sh/vhs/badge.svg">
</a>


!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
