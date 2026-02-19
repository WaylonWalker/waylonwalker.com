---
title: '💭 Cancel subscriptions | Stripe Documentation'
date: 2023-12-10T04:28:33
template: link
link: https://stripe.com/docs/billing/subscriptions/cancel#canceling
tags:
  - webdev
  - stripe
  - thoughts
  - thought
  - link
published: true

---

![[https://stripe.com/docs/billing/subscriptions/cancel#canceling]]

This is a handy guide to cancelling stripe subscriptions.

``` python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_51ODvHtB26msLKqCAPBAo1qkBBuIfT5tQBX6YFWCLMsPixIExxITCRVa9tNCIqkdQS8olhR79NYXsFWBPKsM3LbGO00zEcNQfNI"

stripe.Subscription.modify(
  "sub_49ty4767H20z6a",
  cancel_at_period_end=True,
)
```

You can even inverse it by flipping `True` to `False` and re activate the subscription.

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
