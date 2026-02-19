---
title: '💭 How to Format All Files in a Directory with Prettier | by Dr. ...'
date: 2023-08-19T14:58:09
template: link
link: https://levelup.gitconnected.com/how-to-format-all-files-in-a-directory-with-prettier-5f0ff5f4ffb2
tags:
  - cli
  - prettier
  - thoughts
  - thought
  - link
published: true

---

![[https://levelup.gitconnected.com/how-to-format-all-files-in-a-directory-with-prettier-5f0ff5f4ffb2]]

Use prettier to format all files in a directory.  By default prettier does not write, it just echos out the format that it would do.  Give it the `--write` and it will write the changes to the files.

``` bash
prettier --write .
```

I just used this on my thoughts repo.

``` bash
prettier --write templates
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
