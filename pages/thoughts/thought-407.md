---
title: '💭 Support regex substitution command · Issue #2232 · helix-edito...'
date: 2024-10-08T13:36:25
template: link
link: https://github.com/helix-editor/helix/issues/2232#issuecomment-1228632218
tags:
  - vim
  - regex
  - refactoring
  - thoughts
  - thought
  - link
published: true

---

![[https://github.com/helix-editor/helix/issues/2232#issuecomment-1228632218]]

Here is a really good vim substitute with regex capture groups, saving this one for a rainy day.


``` md
* Reading 1: This is a title to a link
* Reading 2: This is another title
```

`:%s/\v(: )(.+)$/\1\[\2\]\(`

``` md
* Reading 1: [This is a title to a link](
* Reading 2: [This is another title](
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
