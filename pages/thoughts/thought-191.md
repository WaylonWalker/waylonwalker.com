---
title: '💭 Mastodon.py — Mastodon.py 1.8.1 documentation'
date: 2023-12-21T01:59:43
template: link
link: https://mastodonpy.readthedocs.io/en/stable/
tags:
  - python
  - thoughts
  - thought
  - link
published: true

---

![[https://mastodonpy.readthedocs.io/en/stable/]]

Mastadon.py is a python api client for mastadon that makes it easy to cross post to mastadon.

``` python
from mastodon import Mastodon

Mastodon.create_app(
    'pytooterapp',
    api_base_url = 'https://mastodon.social',
    to_file = 'pytooter_clientcred.secret'
)

from mastodon import Mastodon

mastodon = Mastodon(client_id = 'pytooter_clientcred.secret',)
mastodon.log_in(
    'my_login_email@example.com',
    'incrediblygoodpassword',
    to_file = 'pytooter_usercred.secret'
)

mastodon.toot('Tooting from Python using #mastodonpy !')
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
