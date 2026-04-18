---
date: 2025-01-22 08:36:27
templateKey: blog-post
title: analytics
jinja: true
tags:
  - slash
  - meta
published: True

---

I've been posting on this site since 2016, when layoffs were rolling through
the company I worked for at the time.  Starting a personal blog and a pile of
side projects felt like one of the best things I could do for my resume, so off
I went.  This site is built on [[ markata ]], more about that in the
[[ colophon ]].

![screenshot-2025-01-31T21-23-13-643Z.png](https://dropper.waylonwalker.com/api/file/7b6cf2c2-2299-4320-b58f-b0bebf2d0504.png)

The old version of this page embedded static SVGs from my Python Markata build.
Those files are gone in the `markata-go` site, so this page now renders the
yearly posting history directly from the current content set.

## Post Contributions All Time Monthly

```contribution-graph
{
  "data": [
    {% for post in core.filter("published == true") %}
    {"date": "{{ post.Date.Format \"2006-01-02\" }}", "value": 1}{% if not loop.last %},{% endif %}
    {% endfor %}
  ],
  "options": {
    "year": 2016,
    "range": 120,
    "domain": "month",
    "subDomain": "day",
    "maxPercentile": 95
  }
}
```
## Post Contributions in 2026

```contribution-graph
{
  "options": {
    "year": 2026,
    "range": 1,
    "domain": "year",
    "subDomain": "day"
  }
}
```

## Post Contributions in 2025

```contribution-graph
{
  "options": {
    "year": 2025,
    "range": 1,
    "domain": "year",
    "subDomain": "day"
  }
}
```

## Post Contributions in 2024

```contribution-graph
{
  "options": {
    "year": 2024,
    "range": 1,
    "domain": "year",
    "subDomain": "day",
    "maxPercentile": 95
  }
}
```

## Post Contributions in 2023

2023 was a very busy year for me and I started slowing down.  About mid year I
felt like I had a lot that I wanted to get out, but felt like I couldn't,
because I did not have the time to blog, so I added [[ thoughts ]] on 7/22/2023
with this [first thought](https://waylonwalker.com/thoughts-2/).

```contribution-graph
{
  "options": {
    "year": 2023,
    "range": 1,
    "domain": "year",
    "subDomain": "day",
    "maxValue": 8
  }
}
```

> Notice the huge uptick that started immediately as shots was released

## Post Contributions in 2022

```contribution-graph
{
  "options": {
    "year": 2022,
    "range": 1,
    "domain": "year",
    "subDomain": "day"
  }
}
```

## Post Contributions in 2021

At the End of 2021 I started posting [[ til ]]s daily for a few months.  This
is the point when I really started lowering the barrier to entry to make a blog
post.  A blog post did not need to be a super long essay, but could be the size
of a tweet.

```contribution-graph
{
  "options": {
    "year": 2021,
    "range": 1,
    "domain": "year",
    "subDomain": "day"
  }
}
```

## Post Contributions in 2020

```contribution-graph
{
  "options": {
    "year": 2020,
    "range": 1,
    "domain": "year",
    "subDomain": "day"
  }
}
```

## Post Contributions in 2019

2019 was a huge learning year for me.  I was very busy leading a migration to
the cloud, containerized data pipeline orchestration, and setting up new
projects and templates using [[ kedro ]]

```contribution-graph
{
  "options": {
    "year": 2019,
    "range": 1,
    "domain": "year",
    "subDomain": "day"
  }
}
```

## Post Contributions in 2018

This was the year I really started reaching for the terminal kicking off the
year with [[vim-notes]] and rounding out with [[bash]].  I had been
watching luke smith for a awhile, and started managing my first linux server at
work.  I was stuck with windows at the time, but wsl was a new thing that let
me run linux in the terminal.

```contribution-graph
{
  "options": {
    "year": 2018,
    "range": 1,
    "domain": "year",
    "subDomain": "day"
  }
}
```

## Post Contributions in 2017

2017 was the year of getting started, I was coming up on 5 years into my
career, and layoffs were happening hard at the time.  I remember fist landing 5
years before and being told in the companies long history they have never laid
off engineers, it was a very safe place to be.  This was a wake up call that it
might all turn around and I would take nothing with me.  Blogging became my way
to document things I was learning, it was making be better at communicating,
and giving me a reason to take a deeper dive into interesting topics.

```contribution-graph
{
  "options": {
    "year": 2017,
    "range": 1,
    "domain": "year",
    "subDomain": "day"
  }
}
```

## Post Contributions in 2016

2016 was the year that I created my github account, and really got serious
about career switching from Mechanical Engineering to Software Engineering.
All of my 2016 posts are back-dated github stars.

```contribution-graph
{
  "options": {
    "year": 2016,
    "range": 1,
    "domain": "year",
    "subDomain": "day"
  }
}
```
