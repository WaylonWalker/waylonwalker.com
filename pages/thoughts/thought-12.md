---
title: '💭 sqlite-utils command-line tool - sqlite-utils'
date: 2023-07-28T14:59:37
template: link
link: https://sqlite-utils.datasette.io/en/stable/cli.html#querying-data-directly-using-an-in-memory-database
tags:
  - sqlite
  - data
  - database
  - sql
  - json
  - thoughts
  - thought
  - link
published: true

---

![[https://sqlite-utils.datasette.io/en/stable/cli.html#querying-data-directly-using-an-in-memory-database]]

I want to like jq, but I think Simon is selling me on sqlite, maybe its just me but this looks readable, hackable, editable, memorizable.  Everytime I try jq, and its 5 minutes fussing with it just to get the most basic thing to work.  I know enough sql out of the gate to make this work off the top of my head


``` bash
curl  https://thoughts.waylonwalker.com/posts/ | sqlite-utils memory - 'select title, message from stdin where stdin.tags like "%python%"' | jq
```



!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
