---
date: 2023-06-09 09:59:07
templateKey: blog-post
title: Pycon 2023
tags:
  - python
published: false
---

## Keynote Speaker - James Powell

I don't want to be an expert python developer.

[https://www.youtube.com/watch?v=iKzOBWOHGFE](https://www.youtube.com/watch?v=iKzOBWOHGFE){.hoverlink}

![keynote-speaker---james-powell.webp](https://dropper.wayl.one/api/file/8275d2a5-72da-470c-a71d-86019415b303.webp)

### usage of keyword only arguments to prevent pain for users of libraries

```python
# Version 1
def newton(f, x0, fprime, maxiter=100):
    ...

# Version 2
def newton(f, x0, fprime, tol=1e-6, maxiter=100):
    ...

# 🔴 Broke in Version 2
newton(f, x0, fprime, 100)
```

In an alternate timeline the maintainer of newton could have chose to use
keyword only arguments to prevent pain for users of libraries, or poor api
design due to fear of changing api on users.

```python
# Version 1
def newton(f, x0, fprime, *, maxiter=100):
    ...

# Version 2
def newton(f, x0, fprime, *, tol=1e-6, maxiter=100):
    ...

# 🟢 user forced to use keyword only arguments never notices change
newton(f, x0, fprime, maxiter=100)
```
