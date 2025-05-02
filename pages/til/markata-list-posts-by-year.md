---
date: 2025-05-01 22:35:47
templateKey: til
title: Markata list posts by year
published: true
jinja: true
tags:
  - python
  - markata

---

I was looking back at my [[analytics]] page today and wondered what were my
posts about back at the beginning.  My blog is managed by [[markata]] so I
looked at a few ways you could pull those posts up.


``` python
from markata import Markata

m.map('title, slug, date', filter='date.year==2016', sort='date')
```

### Result

``` python
[
    ('⭐ jupyterlab jupyterlab', 'jupyterlab-jupyterlab', datetime.date(2016, 12, 13)),
    ('⭐ nickhould tidy-data-python', 'nickhould-tidy-data-python', datetime.date(2016, 12, 9)),
    (
        '⭐ mikeckennedy write-pythonic-code-demos',
        'mikeckennedy-write-pythonic-code-demos',
        datetime.date(2016, 11, 22)
    ),
    (
        '⭐ mikeckennedy write-pythonic-code-for-better-data-science-webcast',
        'mikeckennedy-write-pythonic-code-for-better-data-science-webcast',
        datetime.date(2016, 11, 22)
    ),
    ('⭐ rajshah4 dlgroup', 'rajshah4-dlgroup', datetime.date(2016, 11, 18)),
    ('⭐ pandas-dev pandas', 'pandas-dev-pandas', datetime.date(2016, 10, 5))
]
```

``` bash
⬢ [devtainer-0.1.3] ❯ markata list --map title --filter='date.year==2016'
[22:35:06] 2088/2145 posts skipped                                                                       skip.py:36
           57/2145 posts not skipped                                                                     skip.py:37

⭐ pandas-dev pandas
⭐ rajshah4 dlgroup
⭐ mikeckennedy write-pythonic-code-for-better-data-science-webcast
⭐ mikeckennedy write-pythonic-code-demos
⭐ nickhould tidy-data-python
⭐ jupyterlab jupyterlab
```

``` html
{% raw %}
{% for title, slug, date in markata.map('title, slug, date', filter='date.year==2016', sort='date') %}
* [{{title}}]({{slug}}) - {{date}}
{% endfor %}
{% endraw %}
```

### Result

{% for title, slug, date in markata.map('title, slug, date', filter='date.year==2016', sort='date') %}
* [{{title}}]({{slug}}) - {{date}}
{% endfor %}
