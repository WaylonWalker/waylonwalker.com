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
<div class="feed h-feed"><div class="posts posts-list" id="posts-list"><article class="card card-article h-entry"><a href="/i-built-a-tmux-session-switcher/"><strong>I Built A Tmux Session Switcher</strong></a><div class="card-body"><p class="card-description p-summary">I&#39;ve been thinking about this for awhile now. For years now, fuzzy pickers and last session have been my go to. They have served me well. I can typically...</p></div><footer class="card-meta"><time>2026-03-04 20:47:37 +0000 UTC</time><div class="card-tags"><a href="/tags/cli/" class="tag p-category">cli</a></div></footer></article></div></div>
</section>

<section class="home-news__column">
<div class="home-news__section-head">
<h3>Latest TILs</h3>
<a href="/til/">All</a>
</div>
<div class="feed h-feed"><div class="posts posts-list" id="posts-list"><article class="card card-link h-entry"><div class="card-link-wrapper"><div class="card-link-content"><a class="card-title p-name u-url" href="/gh-do-i-have-a-pr/">gh do I have a pr</a></div></div><footer class="card-meta"><time>2026-03-02 08:47:44 +0000 UTC</time><div class="card-tags"><a href="/tags/cli/" class="tag p-category">cli</a></div></footer></article><article class="card card-link h-entry"><div class="card-link-wrapper"><div class="card-link-content"><a class="card-title p-name u-url" href="/double-gutter/">double gutter</a></div></div><div class="card-link-body"><p class="card-link-snippet p-summary">I keep forgetting about the double gutter problem with nested containers. When you put padding on a parent and the child also has padding, you get twice the spacing you wanted. ## The Problem ```css .container { padding: 2rem; } .child { padding: 2rem; } ``` Now your content is 4rem from the edge. Not what I meant at all....</p></div><footer class="card-meta"><time>2026-02-14 09:12:42 +0000 UTC</time><div class="card-tags"><a href="/tags/webdev/" class="tag p-category">webdev</a></div></footer></article><article class="card card-link h-entry"><div class="card-link-wrapper"><div class="card-link-content"><a class="card-title p-name u-url" href="/diff-kubernetes-manifest-with-cluster/">diff kubernetes manifest with cluster</a></div></div><div class="card-link-body"><p class="card-link-snippet p-summary">Like a dufus this morning I did a hard reset on a git repo for getting I was working on a manifest for. You see I generally use argo, but occasionally I have no idea what I am doing or want yet and I start raw doggin it, fully aware that I&#39;m going to just nuke this namespace before getting...</p></div><footer class="card-meta"><time>2026-02-05 09:37:39 +0000 UTC</time><div class="card-tags"><a href="/tags/kubernetes/" class="tag p-category">kubernetes</a></div></footer></article><article class="card card-link h-entry"><div class="card-link-wrapper"><div class="card-link-content"><a class="card-title p-name u-url" href="/format-markdown-with-mdformat/">format markdown with mdformat</a></div></div><div class="card-link-body"><p class="card-link-snippet p-summary">I really wish I would have got this right a few years ago. Theres a couple of flags I had to use to get mdformat to do hard wraps at 80 characters and not wreck tables. This mix of flags and plugins is workign really well for me so far. ```bash mdfmt() { uvx \ --with &#34;mdformat-ruff&#34; \ --with &#34;mdformat-beautysh&#34;...</p></div><footer class="card-meta"><time>2026-01-19 20:41:14 +0000 UTC</time><div class="card-tags"><a href="/tags/python/" class="tag p-category">python</a></div></footer></article></div></div>
</section>

<section class="home-news__column">
<div class="home-news__section-head">
<h3>Recent pings</h3>
<a href="/pings/">All</a>
</div>
<div class="feed h-feed"><div class="posts posts-list" id="posts-list"><article class="card card-note h-entry"><a href="/ping-32/"><strong>Context Poisoning Was There All Along</strong></a><div class="card-body"><p class="card-description p-summary">I wrote some code by hand on Sunday. Sat down with my son and started building out a game in pygame from scratch. We went to google, we searched how to do...</p></div><footer class="card-meta"><time>2026-03-17 21:10:38 +0000 UTC</time><div class="card-tags"><a href="/tags/ping/" class="tag p-category">ping</a></div></footer></article><article class="card card-note h-entry"><a href="/ping-31/"><strong>Thinking about ai productivity again</strong></a><div class="card-body"><p class="card-description p-summary">Thinking about AI productivity again. It&#39;s allowing massive amounts of work to get done, to levels that humans cannot physically type out in some cases. But...</p></div><footer class="card-meta"><time>2026-03-16 21:01:44 +0000 UTC</time><div class="card-tags"><a href="/tags/ping/" class="tag p-category">ping</a><a href="/tags/ai/" class="tag p-category">ai</a><a href="/tags/llm/" class="tag p-category">llm</a><a href="/tags/agents/" class="tag p-category">agents</a></div></footer></article><article class="card card-note h-entry"><a href="/ping-29/"><strong>Did you even like to code?</strong></a><div class="card-body"><p class="card-description p-summary">Here&#39;s something I&#39;ve been wrestling with lately. I keep hearing people come to the realization that they never liked coding, they thought they did, but...</p></div><footer class="card-meta"><time>2026-03-07 20:59:39 +0000 UTC</time><div class="card-tags"><a href="/tags/ping/" class="tag p-category">ping</a></div></footer></article><article class="card card-note h-entry"><a href="/ping-28/"><strong>The only thing that seems interesting is AI right now</strong></a><div class="card-body"><p class="card-description p-summary">The only thing that seems interesting is AI right now, I&#39;m writing less code, and I kinda just don&#39;t care as much about the small open source stuff as I used...</p></div><footer class="card-meta"><time>2026-03-06 20:55:26 +0000 UTC</time><div class="card-tags"><a href="/tags/ping/" class="tag p-category">ping</a></div></footer></article></div></div>
</section>
</section>

<section class="home-news__band">
<section class="home-news__column">
<div class="home-news__section-head">
<h3>Long-form posts</h3>
<a href="/blog/">All</a>
</div>
<div class="feed h-feed"><div class="posts posts-list" id="posts-list"><article class="card card-article h-entry"><a href="/i-built-a-tmux-session-switcher/"><strong>I Built A Tmux Session Switcher</strong></a><div class="card-body"><p class="card-description p-summary">I&#39;ve been thinking about this for awhile now. For years now, fuzzy pickers and last session have been my go to. They have served me well. I can typically...</p></div><footer class="card-meta"><time>2026-03-04 20:47:37 +0000 UTC</time><div class="card-tags"><a href="/tags/cli/" class="tag p-category">cli</a></div></footer></article><article class="card card-article h-entry"><a href="/"><strong>Waylon Walker</strong></a><div class="card-body"><p class="card-description p-summary">Notes on software, self-hosting, keyboards, AI tools, and the useful scraps worth keeping.</p></div><footer class="card-meta"><time>2026-02-28 00:00:00 +0000 UTC</time></footer></article><article class="card card-article h-entry"><a href="/test-embed-shot/"><strong>Test Embed Shot</strong></a><div class="card-body"><p class="card-description p-summary">!shots/gma-silk-fail1</p></div><footer class="card-meta"><time>2026-02-24 20:57:58 +0000 UTC</time><div class="card-tags"><a href="/tags/python/" class="tag p-category">python</a></div></footer></article><article class="card card-article h-entry"><a href="/verify/"><strong>/verify</strong></a><div class="card-body"><p class="card-description p-summary">Inspired by @mollywhite&#39;s verify slashpage. This page serves as the system of record for my online identity. The best places to follow me are:</p></div><footer class="card-meta"><time>2026-02-24 10:36:57 +0000 UTC</time><div class="card-tags"><a href="/tags/slashpages/" class="tag p-category">slashpages</a></div></footer></article></div></div>
</section>

<section class="home-news__column">
<div class="home-news__section-head">
<h3>Links and reactions</h3>
<a href="/thoughts-feed/">All</a>
</div>
<div class="feed h-feed"><div class="posts posts-list" id="posts-list"><article class="card card-link h-entry"><div class="card-link-wrapper"><div class="card-link-content"><a class="card-title p-name u-url" href="/thought-945/">💭 Do You Have Token anxiety? - YouTube</a></div></div><div class="card-link-body"><p class="card-link-snippet p-summary">Kids are leaving the party early, not drinking, cant watch netflix without the laptop open. They are leaving the party early to check on their agents. I get it, that feeling that you need to eek out one more prompt, keep your agents running. if they arent running what are you even doing. If not you 6 others are ready...</p></div><footer class="card-meta"><time>2026-03-15 09:27:15 +0000 UTC</time><div class="card-tags"><a href="/tags/llm/" class="tag p-category">llm</a><a href="/tags/ai/" class="tag p-category">ai</a><a href="/tags/thought/" class="tag p-category">thought</a></div></footer></article><article class="card card-link h-entry"><div class="card-link-wrapper"><div class="card-link-content"><a class="card-title p-name u-url" href="/thought-944/">💭 No one under 18 installs Linux</a></div></div><div class="card-link-body"><p class="card-link-snippet p-summary">😂 Should I be concerned that My 12yo installed Arch BTW on his own?

!!! note

    This post is a [[ thoughts | thought ]]. It&#39;s a short note that I make
    about someone else&#39;s content online #thoughts</p></div><footer class="card-meta"><time>2026-03-09 11:46:15 +0000 UTC</time><div class="card-tags"><a href="/tags/linux/" class="tag p-category">linux</a><a href="/tags/thought/" class="tag p-category">thought</a></div></footer></article><article class="card card-link h-entry"><div class="card-link-wrapper"><div class="card-link-content"><a class="card-title p-name u-url" href="/thought-943/">💭 The web is bearable with RSS</a></div></div><div class="card-link-body"><p class="card-link-snippet p-summary">Pluralistic: The web is bearable with RSS (07 Mar 2026) – Pluralistic: Daily links from Cory Doctorow pluralistic.net It&#39;s wild how much of a hit Google took from killing reader, almost any time I hear about killedbygoogle, reader is the top of the list. Its the thing that we all remember being really good and the incumbants just did not...</p></div><footer class="card-meta"><time>2026-03-09 09:00:55 +0000 UTC</time><div class="card-tags"><a href="/tags/blog/" class="tag p-category">blog</a><a href="/tags/thought/" class="tag p-category">thought</a></div></footer></article><article class="card card-link h-entry"><div class="card-link-wrapper"><div class="card-link-content"><a class="card-title p-name u-url" href="/thought-942/">💭 I need a new blog to subscribe to. Know… | justin․searls․co</a></div></div><div class="card-link-body"><p class="card-link-snippet p-summary">Justin Searls @searls I need a new blog to subscribe to. Know any you think I&#39;d like? E-mail me: justin@searls.co justin․searls․co · justin.searls.co Sent Justin my list https://go.waylonwalker.com/blogroll, will soon be on the main site, but right now its only on the go subdomain. I&#39;ve long had reader.waylonwalker.com, but thats soon going to be wrapped into the main site as...</p></div><footer class="card-meta"><time>2026-03-09 08:31:53 +0000 UTC</time><div class="card-tags"><a href="/tags/blog/" class="tag p-category">blog</a><a href="/tags/thought/" class="tag p-category">thought</a></div></footer></article></div></div>
</section>

<section class="home-news__column">
<div class="home-news__section-head">
<h3>Today I learned</h3>
<a href="/til/">All</a>
</div>
<div class="feed h-feed"><div class="posts posts-list" id="posts-list"><article class="card card-link h-entry"><div class="card-link-wrapper"><div class="card-link-content"><a class="card-title p-name u-url" href="/gh-do-i-have-a-pr/">gh do I have a pr</a></div></div><footer class="card-meta"><time>2026-03-02 08:47:44 +0000 UTC</time><div class="card-tags"><a href="/tags/cli/" class="tag p-category">cli</a></div></footer></article><article class="card card-link h-entry"><div class="card-link-wrapper"><div class="card-link-content"><a class="card-title p-name u-url" href="/double-gutter/">double gutter</a></div></div><div class="card-link-body"><p class="card-link-snippet p-summary">I keep forgetting about the double gutter problem with nested containers. When you put padding on a parent and the child also has padding, you get twice the spacing you wanted. ## The Problem ```css .container { padding: 2rem; } .child { padding: 2rem; } ``` Now your content is 4rem from the edge. Not what I meant at all....</p></div><footer class="card-meta"><time>2026-02-14 09:12:42 +0000 UTC</time><div class="card-tags"><a href="/tags/webdev/" class="tag p-category">webdev</a></div></footer></article><article class="card card-link h-entry"><div class="card-link-wrapper"><div class="card-link-content"><a class="card-title p-name u-url" href="/diff-kubernetes-manifest-with-cluster/">diff kubernetes manifest with cluster</a></div></div><div class="card-link-body"><p class="card-link-snippet p-summary">Like a dufus this morning I did a hard reset on a git repo for getting I was working on a manifest for. You see I generally use argo, but occasionally I have no idea what I am doing or want yet and I start raw doggin it, fully aware that I&#39;m going to just nuke this namespace before getting...</p></div><footer class="card-meta"><time>2026-02-05 09:37:39 +0000 UTC</time><div class="card-tags"><a href="/tags/kubernetes/" class="tag p-category">kubernetes</a></div></footer></article><article class="card card-link h-entry"><div class="card-link-wrapper"><div class="card-link-content"><a class="card-title p-name u-url" href="/format-markdown-with-mdformat/">format markdown with mdformat</a></div></div><div class="card-link-body"><p class="card-link-snippet p-summary">I really wish I would have got this right a few years ago. Theres a couple of flags I had to use to get mdformat to do hard wraps at 80 characters and not wreck tables. This mix of flags and plugins is workign really well for me so far. ```bash mdfmt() { uvx \ --with &#34;mdformat-ruff&#34; \ --with &#34;mdformat-beautysh&#34;...</p></div><footer class="card-meta"><time>2026-01-19 20:41:14 +0000 UTC</time><div class="card-tags"><a href="/tags/python/" class="tag p-category">python</a></div></footer></article></div></div>
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
<div class="feed h-feed"><div class="posts posts-list" id="posts-list"><figure class="photo-figure h-entry"><a href="/shots/almost-cheesed-it-to-port-aquelite/"><img src="https://dropper.waylonwalker.com/file/b0adaf31-0a54-4289-a129-0656cd830c62.mp4?h=675&amp;w=1200" alt="Almost Cheesed It To Port Aquelite" loading="lazy" width="1200" height="675"></a><figcaption class="p-summary">Almost Cheesed It To Port Aquelite</figcaption></figure><figure class="photo-figure h-entry"><a href="/shots/its-a-trap/"><img src="https://dropper.waylonwalker.com/file/144212e0-1ed6-4c1a-9630-70ad545145c9.mp4?h=675&amp;w=1200" alt="Its A Trap" loading="lazy" width="1200" height="675"></a><figcaption class="p-summary">Its A Trap</figcaption></figure><figure class="photo-figure h-entry"><a href="/shots/collection-party-balloon/"><img src="https://dropper.waylonwalker.com/file/e3bc3df8-7ad5-4e29-9878-d71603f3b208.mp4?h=675&amp;w=1200" alt="Collection Party Balloon" loading="lazy" width="1200" height="675"></a><figcaption class="p-summary">Collection Party Balloon</figcaption></figure><figure class="photo-figure h-entry"><a href="/shots/collection-l-bracket/"><img src="https://dropper.waylonwalker.com/file/00069fdd-0baf-44d0-9102-cfc80f273327.mp4?h=675&amp;w=1200" alt="Collection L Bracket" loading="lazy" width="1200" height="675"></a><figcaption class="p-summary">Collection L Bracket</figcaption></figure><figure class="photo-figure h-entry"><a href="/shots/wyatt-hits-the-gap/"><img src="https://dropper.waylonwalker.com/file/69869e1e-7aea-42c7-9d99-321aac67324a.mp4?h=675&amp;w=1200" alt="Wyatt Hits The Gap" loading="lazy" width="1200" height="675"></a><figcaption class="p-summary">Wyatt Hits The Gap</figcaption></figure><figure class="photo-figure h-entry"><a href="/shots/dummy13-on-a-skateboard/"><img src="https://dropper.waylonwalker.com/file/beb54917-9ffa-458f-aaef-8d0a4b56566f.webp?h=675&amp;w=1200" alt="Tonight Wyatt gave me a dummy13 that he printed, assembled, and posed all on his own. He&#39;s printed quite a few of these in the past, and none came to this level of completion. I&#39;m so proud of him. This one was a near flawless build with only a few mistakes, that I&#39;d argue were poor design, small vertical pins. More importantly he was able to problem solve and use resin to fix these mistakes." loading="lazy" width="1200" height="675"></a><figcaption class="p-summary">Tonight Wyatt gave me a dummy13 that he printed, assembled, and posed all on his own. He&#39;s printed quite a few of these in the past, and none came to this level of completion. I&#39;m so proud of him. This one was a near flawless build with only a few mistakes, that I&#39;d argue were poor design, small vertical pins. More importantly he was able to problem solve and use resin to fix these mistakes.</figcaption></figure></div></div>
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
