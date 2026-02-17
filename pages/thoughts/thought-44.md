---
title: '💭 Template Designer Documentation — Jinja Documentation'
date: 2023-07-28T14:59:37
templateKey: link
link: https://jinja.palletsprojects.com/en/3.1.x/templates/#include
tags:
  - python
  - webdev
  - jinja2
published: true

---

> A feature of jinja that I just discovered is including sub templates. Here is an example from the docs.


``` html
{% include 'header.html' %}
Body goes here.
{% include 'footer.html' %}
```

And inside of my thoughts project I used it to render posts.

``` html
<ul id='posts'>
    {% for post in posts.__root__ %}
    {% include 'post_item.html' %}
    {% endfor %}
</ul>
```

> note that post_item.html automatically inherits the post variable.

[Original thought](https://jinja.palletsprojects.com/en/3.1.x/templates/#include)
