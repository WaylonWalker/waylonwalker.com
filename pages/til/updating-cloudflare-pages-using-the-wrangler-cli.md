---
date: 2024-04-09 17:03:51
templateKey: til
title: Udating Cloudflare Pages using the Wrangler cli
published: true
tags:
  - infrastructure
  - deployment
  - cloudflare

---

Before deploying to cloudflare pages with wrangler you need a cloudflare api
token.  You can get one at
[dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens).

![cloudflare-pages-api-token](https://screenshots.waylonwalker.com/cloudflare-pages-api-token.png)

## Install Wrangler

Next install wrangler using npm.

``` bash
npm i -g wrangler
```

## Create a Project

Before you deploy to cloudflare pages you need to create a project.  You might
already have one, or you might want to create one in the webui, but you have
the option to create it at the command line with wrangler.

``` bash
npx wrangler pages deploy markout --project-name reader-waylonwalker-com --branch markout
```

## Deploy

Now you can deploy your static application using wrangler to cloudflare pages.

> In this example I have my application built into the markout directory, and
> since the production branch is named `markout` I need to pass that in here as
> well.

``` bash
wrangler pages deploy markout --project-name reader-waylonwalker-com --branch markout
```
