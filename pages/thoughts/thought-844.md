---
title: '💭 Using Litestream to Restore My Database for Easy Development'
date: 2025-09-29T18:49:12
templateKey: link
link: https://pype.dev/using-litestream-to-restore-my-database-for-easy-development/#Update
tags:
  - sqlite
published: true

---

> I really like how well the local dev is setup to run off of production data here.  I'll use this as a reminder that I need to set up lite stream on a few of my projects that it's missing from and include a nice sync prod data [[ justfile ]] recipe.

Litestreams interface always throws me for a loop.  It works fantastic,  but the global config stored in /etc and some of the commands break my brain.  It's not you it's me.

Using real data when you can is goated.  Fake data is so often a perfect example of what someone thinks the backend should look like and does not include things that users actually do, running pipelines for days, or setting titles to paragraphs worth of text.  Obviously this is not possible everywhere and the more sensitive your data the harder that process becomes.

[Original thought](https://pype.dev/using-litestream-to-restore-my-database-for-easy-development/#Update)
