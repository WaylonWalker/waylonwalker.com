---
date: 2026-06-11 11:49:41
templateKey: til
title: one eyed fighting kirby
published: true
tags:
  - vim

---

> Just give em the ol one eyed fighting Kirby

This is a vim substitution technique to capture the rest of the line as a
capture group.

``` vim
:'<,'>s/longhorn\(.*\)/longhorn\1-rwx
```

This one captures pesky optional `"` and places it back at the end if it found
one.

``` vim
:'<,'>s/longhorn\("\?\)\(.*\)/longhorn\2-rwx\1
```

!!! see-also

    [[ thought-200 ]]

