---
title: '💭 Bob Belderbos on X: "Forget Python for a sec, here''s how Vim h...'
date: 2023-10-05T01:34:19
templateKey: link
link: https://twitter.com/bbelderbos/status/1709525676154368055
tags:
  - vim
  - regex
published: true

---

> I need to learn regex capture groups better.  This is so dang powerful. I really like the \v that bob uses here, it really does cut down on the terseness of all the special characters.

> I wanted to replace all occurrences of:
>
> name,name@example.com,0,171,,2023-09-21
>
> With:
>
> name,name@example.com
>
> Easy to do with Python, but what about a bit of > regex in Vim?
>
> :%s/\v([^,]+,[^,]+),.*/\1/

[Original thought](https://twitter.com/bbelderbos/status/1709525676154368055)
