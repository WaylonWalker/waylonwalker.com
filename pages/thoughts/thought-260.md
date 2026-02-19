---
title: '💭 Network Types - Pydantic'
date: 2024-04-30T18:12:26
template: link
link: https://docs.pydantic.dev/2.7/api/networks/#pydantic.networks.EmailStr
tags:
  - 
  - thoughts
  - thought
  - link
published: true

---

![[https://docs.pydantic.dev/2.7/api/networks/#pydantic.networks.EmailStr]]

pydantic has a nice built in email validator `EmailStr`

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

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
