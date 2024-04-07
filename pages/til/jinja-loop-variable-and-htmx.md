---
date: 2024-04-06 20:47:13
templateKey: til
title: jinja loop variable and htmx
published: true
tags:
  - python
  - htmx
  - webdev

---

jinja has a loop variable that is very handy to use with htmx.  Whether you
want to implement a click to load more or an infinite scroll this loop variable
is very handy.

``` html
{% for person in persons %}
<li
{% if loop.last %}
    hx-get="{{ url_for('infinite', page=next_page) }}"
    hx-trigger="intersect once"
    hx-target="#persons"
    hx-swap='beforeend'
    hx-indicator="#persons-loading"
{% endif %}
    {{ person.name.upper() }} -
    {{ person.phone_number }}
</li>
{% endfor %}
```

Now for every chunk of contacts that we load we will trigger the infinite
scroll by loading more once the last one has intersected the screen.
