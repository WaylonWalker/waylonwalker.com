---
title: '💭 Search | Stripe Documentation'
date: 2023-12-06T21:54:17
template: link
link: https://stripe.com/docs/search#search-query-language
tags:
  - webdev
  - stripe
  - thoughts
  - thought
  - link
published: true

---

![[https://stripe.com/docs/search#search-query-language]]

Stripe has it's own query language for querying data.  I'm just getting into using it and it seems pretty good so far.  I needed to lookup the price for products.  I was able to find prices for my product using the python api as shown below.

``` python
stripe.Price.search(query="active: 'true' and product: 'prod_P8SfwtxJ45cWE2'")
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
