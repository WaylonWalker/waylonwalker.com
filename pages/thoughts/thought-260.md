---
title: '💭 Network Types - Pydantic'
date: 2024-04-30T18:12:26
templateKey: link
link: https://docs.pydantic.dev/2.7/api/networks/#pydantic.networks.EmailStr
tags:
  - 
published: true

---

> pydantic has a nice built in email validator `EmailStr`

It requires an optional pydantic dependency 

``` bash
pip install email-validator
```

Then you can validate email addresses.

``` python
from pydantic import BaseModel, EmailStr

class Model(BaseModel):
    email: EmailStr

print(Model(email='contact@mail.com'))
#> email='contact@mail.com'
```

[Original thought](https://docs.pydantic.dev/2.7/api/networks/#pydantic.networks.EmailStr)
