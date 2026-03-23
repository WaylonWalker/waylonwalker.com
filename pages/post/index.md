---
date: 2026-02-28
templateKey: blog-post
title: Waylon Walker
description: Notes on software, self-hosting, keyboards, AI tools, and the useful scraps worth keeping.
slug: ""
published: True
jinja: True
aliases:
  - home
  - index

---

<style>
body:has(.home-news) .article-progress,
body:has(.home-news) .post > header,
body:has(.home-news) .post-header,
body:has(.home-news) .tags,
body:has(.home-news) .guide-info,
body:has(.home-news) .share,
body:has(.home-news) .post-graph,
body:has(.home-news) .webmentions,
body:has(.home-news) .post-copy,
body:has(.home-news) .components-share,
body:has(.home-news) .components-post-graph {
  display: none !important;
}

body:has(.home-news) article.post,
body:has(.home-news) .post,
body:has(.home-news) .content-wrapper,
body:has(.home-news) .post-content,
body:has(.home-news) .content {
  width: auto !important;
  max-width: none !important;
  padding: 0 !important;
  margin: 0 !important;
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

body:has(.home-news) main,
body:has(.home-news) .main-content {
  max-width: none !important;
}

.home-news {
  width: 100vw;
  margin-left: calc(50% - 50vw);
  padding: 12px 0 32px;
}

.home-news__inner {
  width: min(1380px, calc(100vw - 24px));
  margin: 0 auto;
}

.home-news__masthead,
.home-news__band,
.home-news__footer-band {
  border-top: 1px solid color-mix(in srgb, var(--color-text) 12%, transparent);
}

.home-news__masthead {
  padding: 10px 0 12px;
  margin-bottom: 12px;
}

.home-news__masthead-row {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 12px;
  font-size: 13px;
}

.home-news__masthead-row > div:last-child {
  text-align: right;
}

.home-news__name {
  text-align: center;
  font-size: 34px;
  line-height: 1;
  letter-spacing: -0.03em;
  margin: 10px 0 6px;
}

.home-news__subnav {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 8px 16px;
  font-size: 13px;
}

.home-news__subnav a,
.home-news__meta a,
.home-news__list a,
.home-news__links a,
.home-news__text a,
.home-news__section-head a {
  text-decoration: none;
}

.home-news__lede {
  display: grid;
  grid-template-columns: 2.2fr 1fr;
  gap: 16px;
  margin-bottom: 16px;
}

.home-news__lede-main,
.home-news__lede-side,
.home-news__column,
.home-news__box,
.home-news__footer-box {
  border: 1px solid color-mix(in srgb, var(--color-text) 10%, transparent);
  border-radius: 6px;
  padding: 12px;
  background: color-mix(in srgb, var(--color-background) 98%, transparent);
}

.home-news__lede-main h2 {
  margin: 0 0 10px;
  font-size: 44px;
  line-height: 0.94;
  letter-spacing: -0.04em;
}

.home-news__lede-main p,
.home-news__text p,
.home-news__box p,
.home-news__footer-box p {
  margin: 0 0 10px;
  max-width: none;
  line-height: 1.65;
}

.home-news__meta {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 14px;
  font-size: 13px;
  margin-top: 14px;
}

.home-news__section-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 10px;
  padding-bottom: 8px;
  border-bottom: 1px solid color-mix(in srgb, var(--color-text) 10%, transparent);
}

.home-news__section-head h3,
.home-news__section-head h4 {
  margin: 0;
  font-size: 16px;
  line-height: 1.15;
}

.home-news__section-head a {
  font-size: 13px;
}

.home-news__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.home-news__list li {
  padding: 8px 0;
  border-top: 1px solid color-mix(in srgb, var(--color-text) 10%, transparent);
}

.home-news__list li:first-child {
  border-top: 0;
  padding-top: 0;
}

.home-news__list a {
  display: block;
  font-weight: 600;
  margin-bottom: 3px;
}

.home-news__list p,
.home-news__list time {
  margin: 0;
  font-size: 13px;
  line-height: 1.55;
}

.home-news__band {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 16px;
  padding-top: 14px;
  margin-bottom: 14px;
}

.home-news__column--wide {
  grid-column: span 2;
}

.home-news .posts-list {
  display: grid;
  gap: 10px;
}

.home-news .card {
  margin: 0;
  border-radius: 6px;
  box-shadow: none;
  height: 100%;
}

.home-news__column .card,
.home-news__box .card {
  border-width: 1px;
}

.home-news__shots .posts-list {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.home-news__footer-band {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 16px;
  padding-top: 14px;
}

.home-news__links {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 12px;
  font-size: 13px;
}

@media (max-width: 1100px) {
  .home-news__lede,
  .home-news__band,
  .home-news__footer-band {
    grid-template-columns: 1fr;
  }

  .home-news__column--wide {
    grid-column: auto;
  }

  .home-news__shots .posts-list {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 720px) {
  .home-news__inner {
    width: min(100vw - 16px, 1380px);
  }

  .home-news__masthead-row {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .home-news__masthead-row > div:last-child {
    text-align: center;
  }

  .home-news__name {
    font-size: 28px;
  }

  .home-news__lede-main h2 {
    font-size: 34px;
  }

  .home-news__shots .posts-list {
    grid-template-columns: 1fr;
  }
}
</style><div class="home-news">
<div class="home-news__inner">
<section class="home-news__masthead">
<div class="home-news__masthead-row">
<div>Waylon Walker on software, notes, tools, and side projects</div>
<div>Mon Mar 23 2026</div>
<div><a href="/archive/">Archive</a> / <a href="/search/">Search</a></div>
</div>
<div class="home-news__name">Waylon Walker</div>
<nav class="home-news__subnav" aria-label="Homepage sections">
<a href="/blog/">Blog</a>
<a href="/til/">TIL</a>
<a href="/thoughts-feed/">Thoughts</a>
<a href="/pings/">Pings</a>
<a href="/shots/">Shots</a>
<a href="/reader/">Reader</a>
<a href="/blogroll/">Blogroll</a>
<a href="/markata/">Markata</a>
</nav>
</section>

<section class="home-news__lede">
<section class="home-news__lede-main">
<h2>Build in public. Keep the notes. Publish the useful parts.</h2>
<p>This homepage is meant to read more like a front page than a landing page.  Longer posts, short notes, links, screenshots, and works-in-progress all live together here because that is closer to how the site is actually used.</p>
<p>If you are new, start with the latest post, skim the notes, or jump into one of the feeds.</p>
<div class="home-news__meta">
<a href="/now/">/now</a>
<a href="/blog/about-this-site/">about this site</a>
<a href="/blog/colophon/">colophon</a>
<a href="/all/">all</a>
</div>
</section>

<section class="home-news__lede-side">
<div class="home-news__section-head">
<h3>Start here</h3>
</div>
<ul class="home-news__list">
<li><a href="/now/">What has my attention</a><p>Current interests, projects, and distractions.</p></li>
<li><a href="/blog/about-this-site/">What this site is</a><p>Why the site exists and how I use it.</p></li>
<li><a href="/reader/">What I am reading</a><p>The wider web around this place.</p></li>
<li><a href="/archive/">Everything in order</a><p>The full timeline.</p></li>
</ul>
</section>
</section>

<section class="home-news__band">
<section class="home-news__column home-news__column--wide">
<div class="home-news__section-head">
<h3>Lead story</h3>
<a href="/blog/">All posts</a>
</div>
{{ render_feed("blog-feed", 1, "card") }}
</section>

<section class="home-news__column">
<div class="home-news__section-head">
<h3>Latest TILs</h3>
<a href="/til/">All</a>
</div>
{{ render_feed("til-feed", 4, "list") }}
</section>

<section class="home-news__column">
<div class="home-news__section-head">
<h3>Recent pings</h3>
<a href="/pings/">All</a>
</div>
{{ render_feed("pings", 4, "list") }}
</section>
</section>

<section class="home-news__band">
<section class="home-news__column">
<div class="home-news__section-head">
<h3>Long-form posts</h3>
<a href="/blog/">All</a>
</div>
{{ render_feed("blog-feed", 4, "card") }}
</section>

<section class="home-news__column">
<div class="home-news__section-head">
<h3>Links and reactions</h3>
<a href="/thoughts-feed/">All</a>
</div>
{{ render_feed("thoughts-feed", 4, "card") }}
</section>

<section class="home-news__column">
<div class="home-news__section-head">
<h3>Today I learned</h3>
<a href="/til/">All</a>
</div>
{{ render_feed("til-feed", 4, "card") }}
</section>

<section class="home-news__column">
<div class="home-news__section-head">
<h3>Routes</h3>
</div>
<ul class="home-news__list">
<li><a href="/all/">Everything on one page</a><p>Useful when you want the whole site at once.</p></li>
<li><a href="/markata/">Markata posts</a><p>For the site generator and publishing workflow.</p></li>
<li><a href="/blog/analytics/">Writing analytics</a><p>Traffic and publishing numbers.</p></li>
<li><a href="/about/">About</a><p>Personal context and background.</p></li>
</ul>
</section>
</section>

<section class="home-news__band">
<section class="home-news__column home-news__column--wide home-news__shots">
<div class="home-news__section-head">
<h3>Photos and screenshots</h3>
<a href="/shots/">All</a>
</div>
{{ render_feed("shots", 6, "card") }}
</section>

<section class="home-news__column">
<div class="home-news__section-head">
<h3>What this place is</h3>
</div>
<div class="home-news__text">
<p>Part blog, part notebook, part workshop.  I use the site to think in public, keep track of what I am building, and leave a trail I can find later.</p>
<p>The mix of essays, notes, pings, and shots is intentional.  It is not one format pretending to do every job.</p>
</div>
</section>

<section class="home-news__column">
<div class="home-news__section-head">
<h3>Feeds</h3>
</div>
<div class="home-news__links">
<a href="/blog/">Blog</a>
<a href="/til/">TIL</a>
<a href="/thoughts-feed/">Thoughts</a>
<a href="/pings/">Pings</a>
<a href="/shots/">Shots</a>
<a href="/archive/">Archive</a>
</div>
</section>
</section>

<section class="home-news__footer-band">
<section class="home-news__footer-box">
<div class="home-news__section-head">
<h3>Reader</h3>
</div>
<p><a href="/reader/">Reader</a> and <a href="/blogroll/">blogroll</a> pull the rest of the web into the same publishing space.</p>
</section>

<section class="home-news__footer-box">
<div class="home-news__section-head">
<h3>Search</h3>
</div>
<p><a href="/search/">Search</a> is still the fastest way in when you know the shape of what you want.</p>
</section>

<section class="home-news__footer-box">
<div class="home-news__section-head">
<h3>Source</h3>
</div>
<p><a href="/blog/colophon/">Colophon</a> covers the stack, workflow, and how the site is published.</p>
</section>
</section>
</div>
</div>
