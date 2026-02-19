---
title: '💭 Support regex substitution command · Issue #2232 · helix-edito...'
date: 2024-10-08T13:12:24
template: link
link: https://github.com/helix-editor/helix/issues/2232
tags:
  - helix
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/helix-editor/helix/issues/2232]]

I am a heavy user off substitutions in vim, helix does not substitutions built in, rather it leans on multicursor support.

to replace every instance of hello with world in vim

``` text
:%s/hello/world/g<CR>
```

and in helix you would

``` text
%shello<CR>cworld<ESC>,
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
