---
title: "Robots"
slug: robots
published: true
private: true
jinja: true
---

User-agent: *

Sitemap: https://waylonwalker.com/archive/sitemap.xml

Allow: /

{% for path in private_paths %}
Disallow: {{ path }}

{% endfor %}
