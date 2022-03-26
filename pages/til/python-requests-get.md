---
date: 2022-03-26 17:10:35.321429
templateKey: til
title: Get Webpage with python requests
tags:
  - python

---

Python's requests library is one of the gold standard apis, designed by Kenneth
Reitz.  It was designed with the user perspective in mind first and
implementation second. I have heard this called readme driven development,
where the interface the user will use is laid out first, then implemented.
This makes the library much mor intuitive than if it were designed around how
it was easiest to implement.

## Install Requests

Requests is on pypi and can be installed into your virtual environtment with pip.

```bash
python -m pip install requests
```

## Getting the content of a request

Requests makes getting content from a web url as easy as possible.

```python
import requests

r = requests.get('https://waylonwalker.com/til/htmx-get/')
article = r.content
```

## requests is not limited to html

Requests can handle any web request and is not limited to only html.  Here are
some examples to get a markdown file, a csv, and a png image.

```python
htmx_get_md = requests.get('https://waylonwalker.com/til/htmx-get.md').content
cars = requests.get('https://waylonwalker.com/cars.csv').content
profile = requests.get('https://images.waylonwalker.com/8bitc.png').content
```

## RTFM

There is way more to requests, this just scratches the surface while covering
what you are going to need to get going. The
[requests docs](https://docs.python-requests.org/en/latest/) have way more details.
