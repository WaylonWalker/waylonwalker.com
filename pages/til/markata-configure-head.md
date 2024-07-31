---
date: 2022-09-11 20:25:45
templateKey: til
title: markata extend <head> in configuration
published: true
tags:
  - python
  - markata
---

![Astronauts stunting some stylish color explosion](https://stable-diffusion.waylonwalker.com/000172.2339173599.webp)

A long needed feature of markata has been the ability to really configure out
templates with configuration rather.  It's been long that you needed that if
you really want to change the style, meta tags, or anything in the head you
needed to write a plugin or eject out of the template and use your own.


## Adding some Head

Now you can add some extra style to your site with the existing built-in
template.

``` toml
[[markata.head]]
text = """
<style>
img {
  width: 100%;
  height: auto;
}
ul {
  display: flex;
  flex-wrap: wrap;
}
</style>
"""
```

## You can have more than one Head

Each text entry in `markata.head` just gets appended raw into the head.

``` toml
[[markata.head]]
text = """
<style>
img {
  width: 100%;
  height: auto;
}
ul {
  display: flex;
  flex-wrap: wrap;
}
</style>
"""

[[markata.head]]
text = """
<script>
console.log('hey there')
</script
"""
```

## Still need more?

If this does not take you far enough yet, you can still eject out and use your
own template pretty easy.  If you are going for a full custom site it's likely
that this will be the workflow for awhile.  Markata should only get better and
make this required less often as it matures.


``` toml
[markata]
post_template = "pages/templates/post_template.html"
```

Once you have this in your `markata.toml` you can put whatever you want in your
own template.

!["An astronaut working in a lab, colorful explosion, powder, particles, smoke, 35mm, bokeh, fog, f1.2, shallow depth of field, experiments running, beakers, test tubes, cyberpunk, octane render, trending on artstation, neon lighting, volumetric lighting, pink lighting" -s50 -W800 -H450 -C7.5 -Ak_lms -S2678273305](https://stable-diffusion.waylonwalker.com/000172.2678273305.webp)
