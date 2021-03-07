---
templateKey: blog-post
tags: ['bash']
title: Quickly Edit Posts
date: 2021-01-18T00:00:00
status: published

---

Recently I automated starting new posts with a python script.  Today I want to
work on the next part that is editing those posts quickly.

https://waylonwalker.com/automating-my-post-starter

> Check out this post about setting up my posts with python 🐍

## Enter Bash

For the process of editing a post I just need to open the file in vim quickly.
I dont need much in the way of parsing and setting up the frontmatter.  I think
this is a simple job for a **bash** script and fzf.

1. change to the root of my blog
1. fuzzy find the post
1. open it with vim
1. change back to the directory I was in

## bash function

For this I am going to go with a bash function.  This is partly due to being
able to track where I was and get back.  Also the line with nvim will run fzf
everytime you source your `~/.alias` file which is not what we want.

Lets setup the **boilerplate**.  Its going to create a function called ep
`"edit post"`, track our current directory, create a sub function `_ep`.  Then
call that function and cd back to where we were no matter if `_ep` fails or
succeeds.

_<small><mark>boilerplate</mark></small>_
``` bash
ep () {
    _dir=$(pwd)
    _ep () {
        # open file here
    }
    _ep && cd $_dir || cd $_dir
}
```

https://waylonwalker.com/reusable-bash

> check out this post for more information about writing reusable bash scripts.

## FZF

Let's focus in on that `_ep` function here that is going to do the bulk of the
work to edit the post.

_<small><mark>cd to where I want to edit from</mark></small>_
``` bash
cd ~/git/waylonwalkerv2/
```

Next I need to find all markdown pages within my posts directory.  There is
probably a better way to filter with the `find` command directly, but I am not
worried about perf here and I knew how to do it without google.

_<small><mark>find all markdown</mark></small>_
``` bash
find ~/git/waylonwalkerv2/src/pages/ | grep .md$
```

Now that we can list all potential posts, sending the selected post back to
neovim is as easy as piping those files into fzf inside of a command
substitution that is called with neovim.


_<small><mark>putting together the edit command</mark></small>_
``` bash
$EDITOR $(find ~/git/waylonwalkerv2/src/pages/ | grep .md$ | fzf)
```

## Final Script

_<small><mark>final ep function</mark></small>_
``` bash
ep () {
    _dir=$(pwd)
    _ep () {
        cd ~/git/waylonwalkerv2/
        $EDITOR $(find ~/git/waylonwalkerv2/src/pages/ | grep .md$ | fzf)
    }
    _ep && cd $_dir || cd $_dir
}
```

