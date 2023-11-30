---
date: 2023-11-30 11:54:52
templateKey: til
title: Still Loving Tailwind
published: true
tags:
  - webdev
---

![](https://images.waylonwalker.com/img-c8Fom5UqPWT6IzLefZ3YKU68.png)

I've been using tailwind for a few months now and I can still say I'm loving
it. I've been using it to create some rapid prototypes that may or may not
ever become something, a document that is likely to go to print (a resume), and some quick
dashboards.

## fokais.comm

I started working on fokais.com only a few weeks ago, It's going to be a SAS to
make blogging easier. I've started hosting some tools for this blog that I
really like that I think I can turn into a service. It's been fantastic to
quickly pump out new pages with tailwind.

[![screenshot of https://fokais.com](https://shots.wayl.one/shot/?url=https://fokais.com&height=600&width=1200&scaled_width=600&scaled_height=300&selectors=)](https://fokais.com)

## HTMX

tailwind and htmx are a match made in heaven. They both really lean on
Location of Behavior over Separation of concerns. They do really well at
making small components that you can throw on and endpoint and stack into any
page. With tailwind I just configure it to look at all my templates, and I can
guarantee that the styles will be in app.css, and all I need to do is add
classes to my component.

Heres a sample component for a user widget that will go on every page. It has
everything it needs right in the template.

```html
<div
  hx-swap-oob="outerHTML"
  id="user-header"
  class="absolute top-0 right-0 mt-8 mr-4"
>
  {% if current_user %}
  <details
    id="user-header-details"
    open
    class="group list-none px-4 py-2 self-center justify-self-center bg-neutral-600/10 shadow-lg shadow-zinc-950/20 ring-2 ring-zinc-950/5 rounded-xl flex justify-center align-center flex-col"
  >
    <summary style="list-style-type: none">{{ current_user.username }}</summary>
    <div class="hidden group-hover:block my-4">
      <a
        class="mt-6 px-4 py-2 rounded bg-purple-950/5 ring-2 ring-cyan-500/30 text-cyan-500 font-bold"
        href="{{ url_for('get_logout') }}"
      >
        Logout
      </a>
    </div>
  </details>

  {% else %}
  <a
    href="{{ url_for('post_login') }}"
    class="mt-5 text-xl text-white font-bold text-shadow-xl text-shadow-zinc-950"
  >
    login
  </a>
  {% endif %}
</div>
```

## Resume'

I needed to update my resume' recently and It's gone back and forth between
looking nice, and being in a format I enjoy editing. My last iteration was
honestly neither. This time I set out to update it so that I can write it in
markdown, build it with [markata](markata.dev), and I wanted to style it with
tailwind. It turned out fantastic, its now pretty easy to edit, and looks
great thanks to tailwind.

## grid

I've struggled to use grid on my projects, and I've tried a few different times
with no real success or adoption, but started using it on my resume, to have a
main middle column, with two outer full bleed columns where I can make some
elements full bleed to the edge. tailwind made this easy, once done, I had an
admonition that was beautiful full bleed with a touch of color.
