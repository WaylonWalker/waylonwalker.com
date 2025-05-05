---
date: 2025-05-05 10:32:04
templateKey: blog-post
title: fix feed descriptions
tags:
  - markata
  - python
published: True

---

Today I fixed a bug in markata that has been occurring for a few months where
the description for posts come out as None if coming from cache, the issue was
a pretty simple check and pull properly from cache.  This fixes all the
descriptions in feeds and metadata on the post.

## Better description

While in there we went ahead and improved our get_description to more
accurately return plain text without escaped characters, remove cutoff words,
and add an elipsis if the description cuts off the text.


## More description

While I was there I made longer form posts, `til, blog-post` use the super
description of 500 characters instead of the regular 120 character description.


## Before

![image](https://dropper.wayl.one/api/file/7fbbd47a-82d6-4ec9-9708-172c5f41807a.webp)

## After
![image](https://dropper.wayl.one/api/file/dc2b9c59-41b4-4dd2-97af-b35b3e8ad61f.webp)
