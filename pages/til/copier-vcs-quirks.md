---
date: 2025-06-19 08:04:51
templateKey: til
title: copier vcs quirks
published: true
tags:
  - python
  - copier
jinja: true

---

Copier has a few quirks with vcs that I just discovered by trying to test out
some changes.  I may have some config that I have long forgotten about
somewhere deep in my dotfiles, I don't think so, but id love to be wrong and
corrected, please reach out.

## What Doesn't Work

I tried throwing everything at this template to make it work.  I tried a bunch
of flags that did not work. I tried making commits to the local repo to get rid
of the dirty warning. I really wanted to test new changes locally without
committing and pushing untested and potentially broken changes.

``` bash
uvx copier copy ../markata-blog-starter .
uvx copier copy gh:waylonwalker/markata-blog-starter@develop .
uvx copier copy ../markata-blog-starter . -wlg --trust
```

## What Works - --vcs-ref

Finally after trying everything to get the local copy to work, and my guess of
@branch not working I found this to work.  It does require me to go to the repo
on my develop branch.

``` bash
uvx copier copy gh:waylonwalker/markata-blog-starter --vcs-ref develop .
```

## What Works - delete .git

Really this might be my best option to make quick changes and test them locally
without going through a version control system.  It is not ideal, but makes it
easy to quickly iterate on.  I might be renaming .git, or copying to /tmp for
quick iteration.

``` bash
rm -rf .git
uvx copier copy ../markata-blog-starter .
```

## Copier I love

Copier is a great templating tool.  I really love it.  I use it every single
day to create posts on this blog using [[ tmux-copier-templates ]].  This is
the first time this quirk has got me and it had me puzzled for 45 minutes as I
did not expect this behavior whatsoever.

{% for post in markata.feeds.copier.posts %}* [[ {{post.slug}} ]] - {{post.description}}
{% endfor %}
