---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Building kedro.dev
date: 2020-06-05T05:00:00Z
status: published
description: This is my journey to building up the community page.
cover: ''

---
Follow along the Journey as I build out [kedro.dev](https://kedro.dev).

## Building a Community

I have really enjoyed my own personal journey as I have started to build all of my data pipeline projects with the kedro framework.  I want to start building a place to share resources with the community.  I want to see this community grow and flourish.  They say in front end web development if you are not using a framework you end up building one.  That's exactly what I was doing before I started using kedro.  I want to build out a set of resources that this community can learn from and start to use the framework at their own pace without needing to develop their own from scratch.

## research

Looking into the front end frameworks to see how they welcome their community.  Much of my inspiration is from them, bringing lessons learned to data.

### pages

* banner
* nav
	* docs -> readthedocs
    * tutorial -> kedro-examples
    * blog -> medium
    * community
    	* support
        * team
        * courses
        * examples
        * meetups
        * conferences
        * articles
        * podcasts
        * videos
        * external resources
	* search
* examples
* footer
* sponsors
* newsletter
* copyright
*

### components

* edit this page
* scrolling toc

## Stack Overflow Api

fetch last 5 posts.

```
https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow&tagged=kedro&pagesize=5
```

## DEV.to api

fetch last 5 posts

```
https://dev.to/api/articles?tag=kedro&per_page=5&page=1
```
