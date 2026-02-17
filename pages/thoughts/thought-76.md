---
title: '💭 Create Models with a Many-to-Many Link - SQLModel'
date: 2023-08-09T13:37:15
templateKey: link
link: https://sqlmodel.tiangolo.com/tutorial/many-to-many/create-models-with-link/
tags:
  - python
  - api
  - fastapi
published: true

---

> Creating many to many relationships with sqlmodel requires a LinkTable Model.  The link model will keep track of the linked id's between each of the models.

<img src="https://sqlmodel.tiangolo.com/img/tutorial/many-to-many/many-to-many.svg" alt="many-to-many relationship model" style="
    width: 100%;
">

``` python
from typing import List, Optional

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class HeroTeamLink(SQLModel, table=True):
    team_id: Optional[int] = Field(
        default=None, foreign_key="team.id", primary_key=True
    )
    hero_id: Optional[int] = Field(
        default=None, foreign_key="hero.id", primary_key=True
    )


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: List["Hero"] = Relationship(back_populates="teams", link_model=HeroTeamLink)


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

    teams: List[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)
```

[Original thought](https://sqlmodel.tiangolo.com/tutorial/many-to-many/create-models-with-link/)
