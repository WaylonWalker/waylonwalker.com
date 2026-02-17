---
title: '💭 Models - Pydantic'
date: 2025-01-28T17:27:20
templateKey: link
link: https://docs.pydantic.dev/latest/concepts/models/#rebuilding-model-schema
tags:
  - python
  - pydantic
published: true

---

> I came accross from_attributes today it allows creation of pydantic models from objects such as a sqlalchemy  `Base` Model or while nesting pydantic models.  I believe in the past I have ran into some inconsistencies with nesting pydantic models and I'll bet one had from_attributes set and another did not.

> Arbitrary class instances¶
> _(Formerly known as "ORM Mode"/from_orm)._
> 
> Pydantic models can also be created from arbitrary class instances by reading the instance > attributes corresponding to the model field names. One common application of this functionality is integration with object-relational mappings (ORMs).
> 
> To do this, set the from_attributes config value to True (see the documentation on Configuration for more details).
>
> The example here uses SQLAlchemy, but the same approach should work for any ORM.

[Original thought](https://docs.pydantic.dev/latest/concepts/models/#rebuilding-model-schema)
