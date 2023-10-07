---
date: 2023-05-30 13:35:27
templateKey: til
title: Getting Started with Pydantic
published: false
tags:
  - python
  - pydantic
---

```{.python .darkmark}
global Field
global BaseModel
from pydantic import BaseModel
from pydantic import Field
```

Pydantic is a Python library for serializing data into models that can be
validated with a deep set of built in valitators or your own custom validators,
and deserialize back to JSON or dictionary.

## Installation

To install pydantic you will first need python and pip. Once you have pip
installed you can install pydantic with pip.

```bash
pip install pydantic
```

> Always install in a virtual environment

## Creating a Pydantic model

To get started with pydantic you will first need to create a Pydantic model.
This is a python class that inherits from `pydantic.BaseModel`.

```{.python .darkmark}
from pydantic import BaseModel
from pydantic import Field
from typing import Optional

class Person(BaseModel):
    name: str = Field(...)
    age: int
```

## parsing an object

```{.python .darkmark}
person = Person(name="John Doe", age=30)
print(person)
```
``` {.console .darkmark_output}
name='John Doe' age=30

```


## data serialization

Pydantic has some very robust serialization methods that will automatically
coherse your data into the type specified by the type-hint in the model if it can.

```{.python .darkmark}
person = Person(name=12, age="30")
print(f'name: {person.name}, type: {type(person.name)}')
print(f'age: {person.age}, type: {type(person.age)}')
```
``` {.console .darkmark_output}
1 validation error for Person
name
  Input should be a valid string [type=string_type, input_value=12, input_type=int]
    For further information visit https://errors.pydantic.dev/2.3/v/string_type
```


```{.python .darkmark}
person = Person(name="John Doe", age='thirty')
print(f'name: {person.name}, type: {type(person.name)}')
print(f'age: {person.age}, type: {type(person.age)}')
```
``` {.console .darkmark_output}
1 validation error for Person
age
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='thirty', input_type=str]
    For further information visit https://errors.pydantic.dev/2.3/v/int_parsing
```


## loading from json

## serializing to json

## validation
