---
templateKey: blog-post
tags: ['webdev', 'actions']
title: Site Down During Build
date: 2021-03-22T00:00:00 
status: draft

---

Recently I noticed a new netlify site of mine was down while I was checking to
see if new content was live.  Later found out this was consistent after each
and every push the site would go gown as soon as I hit push, and would not come
back until the build finished.


## Is this normal?

Do other Netlify sites go down during build???

Short Answer NO.  All of my google fu lead me to believe I was alone and none of my other sites do this.

## Digging into my build

My deploy script ends with the following.  After resetting keys and watching it build half a dozen
times I determined that everything was working as normal here.

```
- name: Deploy to Netlify
uses: nwtgck/actions-netlify@v1.1.12
with:
    publish-dir: "./markout"
    production-branch: markout
    production-deploy: true
    deploy-message: "Deploy markout from GitHub Actions"
env:
    NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
    NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
```

## Opening the Nelify Console

![images build](https://images.waylonwalker.com/netlify-build-images-waylonwalker.png)

![site build](https://images.waylonwalker.com/netlify-build-waylonwalker.png)
