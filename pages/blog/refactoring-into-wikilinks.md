---
date: 2024-05-31 20:33:10
templateKey: blog-post
title: Refactoring one line links into wikilinks
tags:
  - vim
published: True

---

Previously I had setup a feature of my website to expand one line links into a
card.  This was not a standard, even to the point that some formatters wrap the
links with <angle brackets>, thus breaking my custom plugin.  Moving to the
wikilink standard will allow my markdown posts to work accross more site
builders without custom integrations.

[[ expand-one-line-links ]]

## What is a wikilink

Wikilinks are standard to a lot of wikis written in markdown.

[markdown-it-wikilinks](https://github.com/jsepia/markdown-it-wikilinks#readme){.hoverlink}

The wikilink syntax is a slug wrapped in double square brackets.

``` markdown
[[ slug ]]
```

Marksman lsp will even autocomplete these for you, its pretty sweet.

!!! Note
    I recently implemented hover for wikilinks and and am pretty stoked about the
    result.  Check this one out [[ sick-wikilink-hover ]].

## Vim Quickfix

You could use `vimgrep` to fill your quickfix list will all of the one line links
but I am less familiar with vimgrep and kept missing posts for some reason, I
think it was something in my file glob missing some directories.

I chose to use `cexpr` to fill my quickfix list using a command that outputs a
vimgrep format `filename:line:col:msg`

``` vim
:cexpr system('rg ^<https -t md --vimgrep .')
```

This filled my quickfix list with all of the one line links.

## Vim cdo

Now all I needed to do was to run a substitution command on every line in the
quickfix list.  This one features the one eyed fighting kirby that I learned
from the primeagen [[ thoughts-200 ]].

``` vim
:cdo s/\(^https:\/\/waylonwalker.com\/\)\(.*\)/[[ \2 ]]
```

This converts all of the full links into a slug wrapped in double square
brackets.

## More

There was a bit more to the full refactor, for instance some had a til/ preix,
some were for youtube, and some were not pointed to my site.
