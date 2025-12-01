---
date: 2024-04-07 14:54:08
templateKey: til
title: jinja macros
published: true
jinja: false
tags:
  - python

---

I am working on a page for
[htmx-patterns](https://htmx-patterns.waylonwalker.com) and I ran into a
situation with lots of duplication.  Especially when i am using tailwind I run
into situations where the duplication can get tedious to maintiain.  The
solution I found is macros.

Now I can use the same code for all of my links, and call the macro to use it.

``` html
{% macro link(id, text, boosted=false) -%}
<a
    class="
    {% if id is none %}
      pointer-events-none bg-terminal-950 text-terminal-900 ring-terminal-900
    {% else %}
      bg-terminal-950 hover:bg-terminal-900 hover:text-terminal-400 text-terminal-500 shadow-lg shadow-terminal-300/20 hover:shadow-terminal-300/30 ring-terminal-300
    {% endif %}
      cursor-pointer block text-center font-bold py-2 px-4 rounded w-full ring-1
    "
    {% if id is not none %}
    href="{{ url_for('boosted', id=id) }}"
    {% endif %}
    {% if boosted %}
    hx-boost="true"
    {% endif %}>
    {{ text }}
</a>
{%- endmacro %}

<h2 class='text-3xl font-light mt-0 max-w-xl text-center prose-xl mt-8 text-terminal-500'>
    Boosted Links
</h2>

<div class='flex flex-row gap-4'>
    {{ link(prev_id, 'Previous', boosted=True) }}
    {{ link(next_id, 'Next', boosted=True) }}
</div>

<h2 class='text-3xl font-light mt-0 max-w-xl text-center prose-xl mt-8 text-terminal-500'>
    Normal Links
</h2>

<div class='flex flex-row gap-4'>
    {{ link(prev_id, 'Previous', boosted=False) }}
    {{ link(next_id, 'Next', boosted=False) }}
</div>
```
