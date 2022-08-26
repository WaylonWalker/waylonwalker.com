---
date: 2022-08-22 13:17:32
templateKey: til
title: vimgrep open buffers
status: 'published'
tags:
  - vim

---

How to vimgrep over hidden files.

I needed to delete all build pipeline steps that were named `upload docs`.  I
currently have about 60 projects running from the same template all running
very similar builds.  In the past I've scripted out migrations for large
changes like this, they involved writing a python script that would load the
yaml file into a dictionary, find the corresponding steps make the change and
write it back out.

Today's job was much simplar, just delete the step, were all steps are
surrounded by newlines.  My first thought was to just open all files in vim and
run `dap`.  I just needed to get these files:positions into my quickfix.  My
issue is that all the builds reside within hidden directories by convention.

## vimgrep over hidden files

I know all the files that I care to search for are called build.yml, and they
are in a hidden directory.

```
:args `fd -H build.yml`
:vimgrep /upload docs/ ##
```

Once opened as a buffer by using args, and a handy fd command I can vimgrep
over all the open buffers using `##`

Now I can just `dap` and `:cnext` my way through the list of changes that I
have, and know that I hit every one of them when I am at the end of my list.
And can double check this in about 10s by scrolling back through the quickfix
list.

You're not a true vim enthusiast until you have spent 10 minutes writing a blog
post about how vim saved you 5 minutes.  Check out all the other times this has
happened to me in the [vim](https://waylonwalker.com/vim/) tag.
