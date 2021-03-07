---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: SqlAlchemy Models
date: 2019-12-21T05:00:00Z
status: published
description: My Notes about using sqlalchemy models
cover: "/static/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f7175616e74756d626c61636b6c6162732f6b6564726f2f6d61737465722f696d672f6b6564726f5f62616e6e65722e6a7067.jpg"
---

# Make a connection

```python
from sqlalchemy import create_engine
def get_engine():
    return create_engine("sqlite:///mode_examples.sqlite")
```


# Make a session

``` python
from sqlalchemy.orm import sessionmaker
def get_session():
    con = get_engine()
    Base.bind = con
    Base.metadata.create_all()
    Session = sessionmaker(bind=con)
    session = Session()
    return session
```

# Make a Base Class

``` python
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
Base.metadata.bind = get_engine()
```

# Make your First Model

``` python
class User(Base):
    __tablename__ = "users"
    username = Column('username', Text())
    firstname = Column('firstname', Text())
    lastname = Column('lastname', Text())
```

# Make your own Base Class to inherit From

``` python
class MyBaseHelper:
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if k[0] != "_"}

    def update(self, **attrs):
        for key, value in attrs.items():
            if hasattr(self, key):
                setattr(self, key, value)
```

# Use the Custom Base Class

``` python
class User(Base, MyBaseHelper):
    __tablename__ = "users"
    username = Column('username', Text())
    firstname = Column('firstname', Text())
    lastname = Column('lastname', Text())
```
