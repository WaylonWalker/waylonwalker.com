---
title: '💭 Command Line | gitignore.io / docs'
date: 2025-05-29T16:22:42
template: link
link: https://docs.gitignore.io/install/command-line
tags:
  - linux
  - thoughts
  - thought
  - link
published: true

---

![[https://docs.gitignore.io/install/command-line]]

This is a very interesting cli, its so simple.  I stumbled accross the `gi` command awhile back and was like pfft, I dont want to install something for that.  Didn't even realize that you **don't** install it, its just http.  Their _install_ instructions lead you to putting a curl funtion in your bashrc.  

``` bash
function gi() { curl -sLw \"\\\n\" https://www.toptal.com/developers/gitignore/api/\$@ ;}
```

This now has me wondering "What else can build like this?"

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
