---
templateKey: blog-post
related_post_label: Check out this related post
tags: 
  - catalytic
  - blog
title: How to crush amazing posts on DEV
date: 2020-08-07T05:00:00Z
status: published
description:  Here are a few of my top tips to help make dev.to posts more readable, and drive better engagement.
cover: '/static/crush-dev-to-posts.png'

---

This post was inspired by a comment I left on @dsteenman's  post.


{% post dsteenman/how-long-should-a-blogpost-be-2k6n %}

Most of the time I prefer short as I am more likely to read the whole thing.  If its setup as a series I am more likely to work my way through the whole series in a matter of a few sessions.  Just my preference

I will say though there are certain articles that fit well to the long format.  They are articles that folks tend to come back to often as a reference again and again.

## Sections

1. [layout is key](#layout-is-key)
1. [Break it up](#break-it-up)
1. [Article types](#article-types)
1. [superpost](#superpost)
1. [single post](#single-post)
1. [series](#series)
1. [discussion](#discussion)
1. [Post what you want to read](#post-what-you-want-to-read)

## layout is key

Either way, you go **layout is key**.  You are not **Steven King**, no matter how great of a writer you are, you are unlikely to hold attention like he can.  Most folks reading blogs scan articles first.  I often scan, then read.  If the article is really good or pertains well to me I will read everything, otherwise, I go back and read only the sections of interest.  If there are no discernable sections you lost me.

For this reason, you need to break up your post, into sections and treat the heading for each one like you would a title of a full post.

### <abbr title="Table of Contents">TOC</abbr>

_Table of Contents_

A lot of folks responded to Danny's post suggesting a table of contents.  For some reason I have never included a <abbr title="Table of Contents">TOC</abbr> in my posts.  It's something I am now considering.  I am really good at changing layout right before, or after, shipping a brand new post.

_semi-auto <abbr title="Table of Contents">TOC</abbr>_

As I am highly allergic to unnecessary rework and potential mistakes I put together this snippet that generates the <abbr title="Table of Contents">TOC</abbr>automatically, just paste this into your console, and paste the results in your article.

``` javascript
// pres F12
// paste this in the console
// get your auto generated DEV TOC
console.log(
  [...document.querySelectorAll('.anchor')]
  .map(a =>
    `1. [${a.parentElement.innerText}](#${a.href.split('#')[1]})`
  )
  .join('\n')
)
```


## Break it up

Use headings, images, and blockquotes to break your article up and make it scannable.  I treat each heading as an article title.  It should be engaging and pull the reader in, but not be clickbaity and irritate them when they didn't get what they expected.

> make it scannable! ... treat each heading as an article title

### Markdown

Get Familiar with Markdown. Check out this [cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet) or the reference right in the DEV editor.  This is not an article about markdown, but here are the most common tags you need to break up your article.

``` markdown

# H1
## H2
### H3
... up to H6

* unordered
* list
* of
* things

1. ordered
1. list
1. of
1. things

![Alt text of image](put-link-to-image-here)

**bold**
_italics_
~~strikethrough~~

👇 Horizontal rules are great a making a hard break between sections

---

```

DEV also supports these HTML elements for additional flair, use wisely. Some can make for some really jarring style that really pulls the readers eye to and is hard to focus on the rest.  I'm talking about you `<mark>`.

``` HTML
<small>small text</small>
<sup>superscript text</sup>
<sub>subscript text</sub>
<mark>highlighted text</mark>
<abbr title="Table of Contents">TOC</abbr>
```

### Liquid Tags

When Editing a post click the Liquid Tag reference to the right, for a list of everything.  The `post` tag is the retweet of DEV.

``` markdown

{% post helenanders26/sql-series-from-a-to-z-2pk9 %}

{% user helenanders26 %}

{% github forem/forem %}

{% github forem/forem no-readme %}

```

## Article types

As I can see there are several **article types** on DEV


1. [superpost](#superpost)
1. [single post](#single-post)
1. [series](#series)
1. [discussion](#discussion)

## superpost

I think this is what @dsteenman is eluding to with the (+3000) word post.  This is the hardest to pull off in my opinion, but if done right it will land you at the top of the search for a long time, in the top 7, and potentially the top 1 for a given tag.

I used to think that every post needed to be a super post that everyone would rave over.  I have found personally that attempting to do this makes it so I rarely post and way overthink them.  I need to at least make a cutoff time that the post is going to ship.

This can also be the most frustrating, you have put all of your eggs in one basket.  If you don't title it right, post at the right time, share it at the right time, it might not take off like you had hoped.

{% post helenanders26/sql-series-from-a-to-z-2pk9 %}

@helenanders26 takes the 👑 as the queen of the superpost.  She is the first person who comes to mind when I think of this post type

## single post

Your average post.  There are a lot of great techniques to making the average post great (some added above).  Sometimes they find traction, sometimes they don't.  I don't sweat if they don't.  I like posting shorter content as its achievable for me and my lifestyle.  I can always crosslink them and generate more views/discussion across them.

{% post taillogs/how-to-write-a-good-blog-post-2eom %}

@taillogs has a good article on his process to writing a good post.

For those struggling to find what to write about, this is a great article from @swyx [learn-in-public-hack](https://www.swyx.io/writing/learn-in-public-hack)

## series

Using the `series` tag you can break super posts into smaller ones.  This puts fewer of your eggs in the same basket.  I typically start a series when I know that I am going to post about a single topic often, but don't have it all laid out.  I've been told for these to be really successful it needs a bit more pre-thought.

I do notice that I get a bit of engagement back to older posts every time a new one is posted.  so this does help drive engagement by continuously pulling readers in.  I am not sure if its quite as good as a link, or liquid embed.  Keep in mind when doing this the series component will show the first 2 and the last two without clicking.  Make sure that the first two really count, they will likely get the most traffic benefit from the series.


{% post waylonwalker/what-are-github-actions-1lhh %}

I personally put a lot of my content into a series.  I don't think through the full series ahead of time very much.  I do it because it helps me organize and retrieve my thoughts.  I find it easier to get back to the post I want to reference if I can find the series it was part of.  I think of it as a tag that no one else can post to.

## discussion

Posts just like this one, where the author leads the discussion with an intriguing question or comment but holds back on their opinion.  The key here is that the author should engage in the discussion, keep the discussion moving, and provide their thoughts here.

Selfishly this is one of my favorite types of posts to make as I learn the most from them.

{% post ben/how-do-you-identify-over-engineering-1oad %}

@ben is the king of the [#discuss](https://dev.to/t/discuss) post.  He is able to get just the right titles that pull people in and generate quite large discussions.

---

## Post what you want to read

At the end of the day **YOU** are the most important component.  Post what you like to read, post what you are able to write.  If you struggle to wrap your head around concepts in small posts and have a talent at making rockstar super posts do that.  **Do YOU**
