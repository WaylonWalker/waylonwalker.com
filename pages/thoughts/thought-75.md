---
title: '💭 python - How to use a Pydantic model with Form data in FastAPI...'
date: 2023-08-08T13:46:19
templateKey: link
link: https://stackoverflow.com/questions/60127234/how-to-use-a-pydantic-model-with-form-data-in-fastapi
tags:
  - python
  - fastapi
  - htmx
  - pydantic
  - webdev
published: true

---

> I went down the route of leveraging the `json-enc` extention in htmx, but later realized that this completely breaks browsers/users who do not wish to use javascript.  While most of the web would feel quite broken with javascript disabled, I don't want to contribute to that without good reason. 

Taking a second look into this issue, rather than using `json-enc`, and using as_form to get form data into a model keeps the nice DX fo everything being a pydantic model, but the site still works without js.  with js htmx kicks in, you get a spa like experience by loading partials onto the page, and without, you just get a full page reload.

## the implementation

copied from https://stackoverflow.com/questions/60127234/how-to-use-a-pydantic-model-with-form-data-in-fastapi


``` python
import inspect
from typing import Type

from fastapi import Form
from pydantic import BaseModel
from pydantic.fields import ModelField

def as_form(cls: Type[BaseModel]):
    new_parameters = []

    for field_name, model_field in cls.__fields__.items():
        model_field: ModelField  # type: ignore

        new_parameters.append(
             inspect.Parameter(
                 model_field.alias,
                 inspect.Parameter.POSITIONAL_ONLY,
                 default=Form(...) if model_field.required else Form(model_field.default),
                 annotation=model_field.outer_type_,
             )
         )

    async def as_form_func(**data):
        return cls(**data)

    sig = inspect.signature(as_form_func)
    sig = sig.replace(parameters=new_parameters)
    as_form_func.__signature__ = sig  # type: ignore
    setattr(cls, 'as_form', as_form_func)
    return cls
```

And the usage looks like


``` python
@as_form
class Test(BaseModel):
    param: str
    a: int = 1
    b: str = '2342'
    c: bool = False
    d: Optional[float] = None


@router.post('/me', response_model=Test)
async def me(request: Request, form: Test = Depends(Test.as_form)):
    return form
```


[Original thought](https://stackoverflow.com/questions/60127234/how-to-use-a-pydantic-model-with-form-data-in-fastapi)
