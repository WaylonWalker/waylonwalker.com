---
date: 2024-04-17 13:32:53
templateKey: til
title: python inline snapshot
published: true
tags:
  - python

---

`inline-snapshot` is a new tool that I am trying out for python testing.  It
takes snapshots of your outputs and places them inline with the test.

Here is the most basic starter.

``` python
import inline_snapshot

def test_one():
    assert 1 == snapshot()
```

Now when I run `pytest` my tests will **fail** because my assert has no value, but if I
run `pytest --inline-snapshot=create` it will fill out my snapshot values and the
file will then look like this.

``` python
import inline_snapshot

def test_one():
    assert 1 == snapshot(1)
```

It also works with pydantic models.

``` python
class MyModel(BaseModel):
    name: str
    age: int
    nickname: str | None = None


def test_my_model_instance():
    assert MyModel(name="Waylon", age=1) == snapshot(MyModel(name="Waylon", age=1))


def test_my_model_fields():
    me = MyModel(name="Waylon", age=1, nickname='Waylon')
    assert me.name == snapshot("Waylon")
    assert me.age == snapshot(1)
    assert me.nickname == snapshot("Waylon")
```
