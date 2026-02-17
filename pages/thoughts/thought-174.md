---
title: '💭 Retrieve an upcoming invoice | Stripe API Reference'
date: 2023-12-07T14:49:51
templateKey: link
link: https://stripe.com/docs/api/invoices/upcoming
tags:
  - webdev
  - stripe
published: true

---

> You can find your customers next billing date through the stripe api by using `Invoice`. and passing in customer, customer_details, subscription, or schedule.


``` python
import stripe
stripe.api_key = "sk_test_51ODvHtB26msLKqCAPBAo1qkBBuIfT5tQBX6YFWCLMsPixIExxITCRVa9tNCIqkdQS8olhR79NYXsFWBPKsM3LbGO00zEcNQfNI"
invoice = stripe.Invoice.upcoming(customer="cus_NeZwdNtLEOXuvB")
```

Within the invoice, you can find the next_payment_attempt as a epoch.

``` python
date = datetime.fromtimestamp(invoice.next_payment_attempt)
amount = invoice.amount_due
currency = invoice.currency
```



[Original thought](https://stripe.com/docs/api/invoices/upcoming)
