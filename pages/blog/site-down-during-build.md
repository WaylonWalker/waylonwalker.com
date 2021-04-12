---
templateKey: blog-post
tags: ['webdev', 'actions']
title: Site Down During Build
date: 2021-03-22T00:00:00 
status: publish

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


After poking at the netlify console for hours I realized that the issue was
that netlify was still auto-deploying from a no longer existing directory and
would cause 404's for every page. During build, then my build from GitHub
Actions would deploy with the netlify cli.

<div class='center-img'>
    <img alt="images build" src="https://images.waylonwalker.com/netlify-build-images-waylonwalker.png">
</div>

Netlify really likes to put a lot of warnings up when you are not deploying
from them.  I tured off automatic deploys, swore to the netlify gods this is
what I wanted. Pushed a new deploy and 🎉 THE SITE DID NOT GO DOWN.

jdiv class='center-img'>
    <img alt="site build" src="https://images.waylonwalker.com/netlify-build-waylonwalker.png">
</div>

## TURN OFF AUTOMATIC BUILDS WHEN SWITCHING TO A SELF BUILD

Moral of the story here is to turn off Netlify's automatic builds when building
yourself and using the netlify cli.
