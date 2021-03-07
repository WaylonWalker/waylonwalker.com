---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: RSS feed for your Gatsby Site
date: 2020-01-21T13:58:59Z
status: draft
description: Add an rss feed to your Gatsby Site
cover: ''

---
Adding an rss feed to your gatsby js site is super simple.

https://www.gatsbyjs.org/packages/gatsby-plugin-feed/


## Install

``` bash
npm install --save gatsby-plugin-feed
```

## How to use
``` javascript
// In your gatsby-config.js
module.exports = {
  plugins: [
    {
      resolve: `gatsby-plugin-feed`,
      options: {
        query: `
          {
            site {
              siteMetadata {
                title
                description
                siteUrl
                site_url: siteUrl
              }
            }
          }
        `,
        feeds: [
          {
            serialize: ({ query: { site, allMarkdownRemark } }) => {
              return allMarkdownRemark.edges.map(edge => {
                return Object.assign({}, edge.node.frontmatter, {
                  description: edge.node.excerpt,
                  date: edge.node.frontmatter.date,
                  url: site.siteMetadata.siteUrl + edge.node.fields.slug,
                  guid: site.siteMetadata.siteUrl + edge.node.fields.slug,
                  custom_elements: [{ "content:encoded": edge.node.html }],
                })
              })
            },
            query: `
              {
                allMarkdownRemark(
                  sort: { order: DESC, fields: [frontmatter___date] },
                ) {
                  edges {
                    node {
                      excerpt
                      html
                      fields { slug }
                      frontmatter {
                        title
                        date
                      }
                    }
                  }
                }
              }
            `,
            output: "/rss.xml",
            title: "Your Site's RSS Feed",
            // optional configuration to insert feed reference in pages:
            // if `string` is used, it will be used to create RegExp and then test if pathname of
            // current page satisfied this regular expression;
            // if not provided or `undefined`, all pages will have feed reference inserted
            match: "^/blog/",
            // optional configuration to specify external rss feed, such as feedburner
            link: "https://feeds.feedburner.com/gatsby/blog",
          },
        ],
      },
    },
  ],
}
```

## My updated graphql query


``` graphql
{
	allMarkdownRemark(
		sort: { order: DESC, fields: [frontmatter___date] }
		filter: {
			frontmatter: {
				templateKey: { in: ["blog-post"] }
				status: { in: ["published"] }
			}
		}
	) {
		edges {
			node {
				excerpt
				rawMarkdownBody
				fields {
					slug
				}
				frontmatter {
					title
					date
					cover {
						relativePath
					}
					twitter_cover {
						relativePath
					}
				}
			}
		}
	}
}

```
