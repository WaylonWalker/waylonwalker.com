---
date: 2022-06-11 12:37:50
templateKey: til
title: Copier Slugify | python templating | using cookiecutter
jinja: False
published: true
tags:
  - python
  - copier

---

It's no secret that I love automation, and lately my templating framework of
choice has been copier.  One hiccup I recently ran into was having spaces in my
templated directory names.  This makes it harder to run commands against as you
need to escape them, and if they end up in a url you end up with ugly `%20` all
over.

## Cookiecutter has the solution

> Yes the solution comes from a competing templating framework.

I install copier with pipx, so I need to inject cookiecutter in to my copier
environment to use the slugify filter.

``` bash
pipx inject copier cookiecutter
```

If you are using a normal virtual environment you can just pip install it.

``` bash
pip install copier cookiecutter
```

## add the extension to your template

_copier.yml_

Now to enable the extension you need to declare it in your `copier.yml` file in
your template.

``` yaml
_jinja_extensions:
    - cookiecutter.extensions.SlugifyExtension
```

## Use it | slugify

_use-it_

Now to use it, anywhere that you want to slugify a variable, you just pipe it
into slugify.

``` bash
❯ tree .
.
├── copier.yml
├── README.md
└── {{ site_name|slugify }}
    └── markata.toml.jinja

1 directory, 3 files
```

Here is a slimmed down version of what the `copier.yml` looks like.

``` yml
site_name:
  type: str
  help: What is the name of your site, this shows in seo description and the site title.
  default: Din Djarin

_jinja_extensions:
    - cookiecutter.extensions.SlugifyExtension
```

## Results

Running the template looks a bit like this.

![copier-cookiecutter-slugify.webp](https://dropper.waylonwalker.com/api/file/ffd34b52-cef7-4de8-b451-4426989fb70c.webp)

---

## straight from their docs

The next section is straight from the [cookiecutter docs](
https://cookiecutter.readthedocs.io/en/latest/advanced/template_extensions.html#slugify-extension)

### Slugify extension

The `cookiecutter.extensions.SlugifyExtension` extension provides a `slugify`
filter in templates that converts string into its dashed ("slugified") version:

``` jinja
{% "It's a random version" | slugify %}
```

Would output:

```
it-s-a-random-version
```

It is different from a mere replace of spaces since it also treats some special
characters differently such as `'` in the example above. The function accepts
all arguments that can be passed to the `slugify` function of
`python-slugify`_. For example to change the output from
`it-s-a-random-version` to `it_s_a_random_version`, the `separator` parameter
would be passed: `slugify(separator='_')`.
