---
templateKey: blog-post
tags: ['webdev', 'blog']
title: Personal URL shortener with Netlify Redirects
date: 2020-01-29T06:00:00.000+00:00
published: true
description: Personal URL shortener with Netlify Redirects

---

I love using URL shorteners to easily share links without hitting character
limits, but they loose their meaning. Services like bit.ly will save my links
for me so that I can find them, but I would rather them to be easy to remember.
[https://bit.ly/2ruLwQz](https://bit.ly/2ruLwQz "https://bit.ly/2ruLwQz") does
not roll of the tongue so well.

## 301 🤸‍♀️

I recently discovered a really cool feature of netlify that I have always looked past, `_redirects`. It is so simple cool and powerful, every netlify site should do this!

## But how 🤷‍♀️

simply add a `_redirects` file to the root of your your published site with the following format. The trick I found with my gatsby site was that it needed to be in my static directory `/static/_redirects`, not root. Next you just put space separated links on separate lines. #'s can be used for comments.

``` markdown
# netlify redirects
# from_url to_url

# Short-Blog

/blog/scli         /blog/simple-click/
/blog/cmdt         /blog/cmd-exe-tips/
.
.
.


# splats

/b*             /blog/:splat
/n*             /notes/:splat


# External

/twitter        https://twitter.com/_WaylonWalker
/github         https://github.com/WaylonWalker
/devto          https://dev.to/waylonwalker/
```

## 🙌 Share those short links

Now with shorter links we have more space for our content without needing to use a service like bit.ly that makes our links unreadable.

![url shortener](https://dropper.waylonwalker.com/file/cd5a0814-556c-41ad-bae5-80c10f1b412e.webp)
