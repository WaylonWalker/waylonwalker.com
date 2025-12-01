---
date: 2023-11-30 11:54:52
templateKey: til
title: Still Loving Tailwind
published: true
tags:
  - webdev
jinja: false
---

![](https://images.waylonwalker.com/img-c8Fom5UqPWT6IzLefZ3YKU68.png)

I've been using tailwind for a few months now and I can still say I'm loving
it. I've been using it to create some rapid prototypes that may or may not
ever become something, a document that is likely to go to print (a resume), and some quick
dashboards.

## I started using Tailwind a few month back

A few months back in september of 2023 I made [a case for
tailwindcss](https://waylonwalker.com/a-case-for-tailwindcss/). And have been
using it on quite a few projects since.

- values are well thought out
- it's really easy to use
- classes that make sense
- tree shakable

## fokais.com

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

## internal apps

I've built several interal apps, and tailwind has been really great for this.
Its super quick to pop classes on components and get things to look decent
quickly, or put some real polish into making them look nice.

## My Website waylonwalker.com

I've dropped my old decrepid css for some tailwind on my main site. My css was
much smaller, but did not work quite as well on all devices, and most
importantly was becoming a house of cards. Every time I fixed one thing several
other things would fail. Colors were a bit muddy, and not as nicely configured
as tailwind.

> Most importantly was becoming a house of cards. Every time I fixed one thing
> several other things would fail.

One rough side of styling a blog in tailwind is that you don't necessarily have
control over granular details of how your pages get rendered without getting
really deep into the markdown renderer, or writing your posts in html. It ends
up looking a bit ugly, and is against the tailwind best practices, but it seems
like the best way for a site like this.

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
@import "./highlight.css";

.social {
  @apply font-bold;
  @apply flex flex-row;
  @apply gap-4;
  @apply justify-center;
  @apply py-8;
}

#posts ul ul {
  @apply backdrop-blur-sm;
  @apply flex flex-col sm:grid grid-flow-row-dense;
  @apply gap-4;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  @apply p-4;
}
```

## grid

I've struggled to use grid on my projects, and I've tried a few different times
with no real success or adoption, but started using it on my resume, to have a
main middle column, with two outer full bleed columns where I can make some
elements full bleed to the edge. tailwind made this easy, once done, I had an
admonition that was beautiful full bleed with a touch of color.
