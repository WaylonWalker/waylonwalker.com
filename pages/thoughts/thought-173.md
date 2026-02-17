---
title: '💭 Search | Stripe Documentation'
date: 2023-12-06T21:54:17
templateKey: link
link: https://stripe.com/docs/search#search-query-language
tags:
  - webdev
  - stripe
published: true

---

> Stripe has it's own query language for querying data.  I'm just getting into using it and it seems pretty good so far.  I needed to lookup the price for products.  I was able to find prices for my product using the python api as shown below.

``` python
stripe.Price.search(query="active: 'true' and product: 'prod_P8SfwtxJ45cWE2'")
```

[Original thought](https://stripe.com/docs/search#search-query-language)
