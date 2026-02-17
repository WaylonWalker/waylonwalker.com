---
title: '💭 `ValueError: Constraint must have a name` in alembic 1.10.0 · ...'
date: 2023-08-05T01:25:07
templateKey: link
link: https://github.com/sqlalchemy/alembic/issues/1195
tags:
  - python
  - data
  - database
  - alembic
published: true

---

> After a nasty time with alembic upgrades, thoughts is about to get a new users table.  This may have came from incorrectly setting up alembic for sqlite from the start, but I was able to fix the issue with this GitHub issue.

``` python
alembic sqlite ValueError: Constraint must have a name
```

The change I needed to make to get my migration to run.

``` diff        - batch_op.create_foreign_key(None, 'user', ['author_id'], ['id'])

        + batch_op.create_foreign_key('fk_post_author_id_user', 'user', ['author_id'], ['id'])
```

[Original thought](https://github.com/sqlalchemy/alembic/issues/1195)
