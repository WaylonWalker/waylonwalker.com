---
date: 2022-09-24 15:18:50
templateKey: til
title: how to escape variables in jinja templates
status: 'published'
jinja_md: False
tags:
  - python

---

While updating my site to use Markata's new configurable head I ran into some
escaping issues.  Things like single quotes would cause jinja to fail as it was
closing quotes that it shouldnt have.

![Nuclear core being help up by glowing neon wires, cyberpunk synthwave, intricate abstract. delicate artwork. by tooth wu, wlop, beeple, dan mumford. pink volumetric lighting, octane render, trending on artstation, greg rutkowski very coherent symmetrical artwork. cinematic, hyper realism, high detail, octane render, 8k, depth of field, bokeh. chrome accents.](https://stable-diffusion.waylonwalker.com/000258.1910330087.webp#cinematic)

## Jinja Escaping Strings

Jinja comes with a handy utility for escaping strings.  I definitly tried to
over-complicate this before realizing.  You can just pipe your variables into
`e` to escape them.  This has worked pretty flawless at solving some jinja
issues for me.

``` html
<p>
{{ title|e }}
</p>
```

## Creating meta tags in Markata

The issue I ran into was when trying to setup meta tags with the new
configurable head, some of my titles have single quotes in them.  This is what
I put in my `markata.toml` to create some meta tags.

``` toml
[[markata.head.meta]]
name = "og:title"
content = "{{ title }}"
```

Using my article titles like this ended up causing this syntax error when not
escaped.

``` python
SyntaxError: invalid syntax. Perhaps you forgot a comma?
Exception ignored in: <function Forward.__del__ at 0x7fa9807192d0>
Traceback (most recent call last):
    ...
TypeError: 'NoneType' object is not callable
```

## jinja2 escape

After making a complicated system of using `html.escape` I realized that jinja
included escaping out of the box so I updated my `markata.toml` to include the
escaping, and it all just worked!.

``` toml
[[markata.head.meta]]
name = "og:title"
content = "{{ title|e }}"
```

![Nuclear core being help up by wires, intricate abstract. delicate artwork. by tooth wu, wlop, beeple, dan mumford. pink volumetric lighting, octane render, trending on artstation, greg rutkowski very coherent symmetrical artwork. cinematic, hyper realism, high detail, octane render, 8k, depth of field, bokeh. chrome accents.](https://stable-diffusion.waylonwalker.com/000255.3328233410.webp#cinematic)
