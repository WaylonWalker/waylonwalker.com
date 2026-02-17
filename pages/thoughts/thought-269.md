---
title: '💭 Fields - Pydantic'
date: 2024-05-09T20:28:27
templateKey: link
link: https://docs.pydantic.dev/2.7/concepts/fields/#field-representation
tags:
  - pydantic
  - fastapi
  - webdev
published: true

---

> `exclude=True` and `repr=False` is a good pydantic combination for secret attributes such as user passwords, or hashed passwords.  exclude keeps it out of model_dumps, and repr keeps it out of the logs.

``` python
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(repr=True)  
    age: int = Field(repr=False)


user = User(name='John', age=42)
print(user)
#> name='John'
```

[Original thought](https://docs.pydantic.dev/2.7/concepts/fields/#field-representation)
