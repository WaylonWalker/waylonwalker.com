---
templateKey: blog-post
related_post_label: Check out this related post
tags: ['webdev']
title: gatsby-remark-embedder
date: 2020-11-18T05:00:00.000+00:00
status: published
description: Inspired by discourse's link expansion I am rolling out 
  expansions for one line links on the blog
cover: "/static/gatsby-remark-embedder.png"

---

<iframe src="https://anchor.fm/waylon-walker/embed/episodes/gatsby-remark-embedder-en6l3j" height="102px" width="400px" frameborder="0" scrolling="no"></iframe>

Inspired by discourse's link expansion I am rolling out expansions for one line
links on the blog [waylonwalker](https://waylonwalker.com).  I was able to find
a gatsby plugin
[gatsby-remark-embedder](https://www.gatsbyjs.com/plugins/gatsby-remark-embedder/?=embed)
that expands one line links for social cards for popular platforms like twitter
and YouTube through a repose from Kyle Mathews to my tweet.

https://twitter.com/kylemathews/status/1329817928666005504

## Use Cases

This covers a couple of use cases I have with very little effort.

* Twitter
* YouTube

## install

``` bash
npm i gatsby-remark-embedder gatsby-plugin-twitter
```

This was super quick and simple to setup, the only thing that was extra was to
install the `gatsby-plugin-twitter` plugin as well as the
`gatsby-remark-embedder`.

## enable

``` javascript
// In your gatsby-config.js

module.exports = {
  // Find the 'plugins' array
  plugins: [
    `gatsby-plugin-twitter`,
    {
      resolve: `gatsby-transformer-remark`,
      options: {
        plugins: [
          {
            resolve: `gatsby-remark-embedder`,
            options: {
              customTransformers: [
                // Your custom transformers
              ],
              services: {
                // The service-specific options by the name of the service
              },
            },
          },

          // Other plugins here...
        ],
      },
    },
  ],
};
```

Thats it, now I can embed tweets and YouTube videos by just leaving the link on a single line.

