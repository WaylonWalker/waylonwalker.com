<?xml version="1.0" encoding="utf-8"?>
<!--

# Pretty Feed

Styles an RSS/Atom feed, making it friendly for humans viewers, and adds a link
to aboutfeeds.com for new user onboarding. See it in action:

   https://interconnected.org/home/feed


## How to use

1. Download this XML stylesheet from the following URL and host it on your own
   domain (this is a limitation of XSL in browsers):

   https://github.com/genmon/aboutfeeds/blob/main/tools/pretty-feed-v3.xsl

2. Include the XSL at the top of the RSS/Atom feed, like:

```
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="/PATH-TO-YOUR-STYLES/pretty-feed-v3.xsl" type="text/xsl"?>
```

3. Serve the feed with the following HTTP headers:

```
Content-Type: application/xml; charset=utf-8  # not application/rss+xml
x-content-type-options: nosniff
```

(These headers are required to style feeds for users with Safari on iOS/Mac.)



## Limitations

- Styling the feed *prevents* the browser from automatically opening a
  newsreader application. This is a trade off, but it's a benefit to new users
  who won't have a newsreader installed, and they are saved from seeing or
  downloaded obscure XML content. For existing newsreader users, they will know
  to copy-and-paste the feed URL, and they get the benefit of an in-browser feed
  preview.
- Feed styling, for all browsers, is only available to site owners who control
  their own platform. The need to add both XML and HTTP headers makes this a
  limited solution.


## Credits

pretty-feed is based on work by lepture.com:

   https://lepture.com/en/2019/rss-style-with-xsl

This current version is maintained by aboutfeeds.com:

   https://github.com/genmon/aboutfeeds


## Feedback

This file is in BETA. Please test and contribute to the discussion:

     https://github.com/genmon/aboutfeeds/issues/8

-->
<xsl:stylesheet version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:atom="http://www.w3.org/2005/Atom"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:sm="http://www.sitemaps.org/schemas/sitemap/0.9">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html xmlns="http://www.w3.org/1999/xhtml" lang='en'>  
    <head>
<title>Waylon Walkers Digital Garden</title>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="description" content="I write about how I use python and linux in data science." />
 <link href="/8bitcc.png" rel="icon" type="image/png" />

<link rel="stylesheet" href="/post.css" />
<link rel="stylesheet" href="/app.css" />
<script src="/theme.js"></script>


<meta name="twitter:title" content="" />
<meta name="og:title" content="" />
<meta name="description" content="" />
<meta name="og:description" content="" />
<meta name="twitter:description" content="" />
<meta name="og:type" content="article" />
<meta name="og:url" content="" />
<meta name="og:image" content="http://shots.wayl.one/shot/?url=&height=600&width=1200&scaled_width=1200&scaled_height=600" />
<meta name="twitter:image" content="http://shots.wayl.one/shot/?url=&height=640&width=1280&scaled_width=1280&scaled_height=640" />
<meta name="og:image:width" content="1200" />
<meta name="og:image:height" content="600" />
<meta name="twitter:creator" content="@_waylonwalker" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="og:author" content="Waylon Walker" />
<meta name="og:site_name" content="Waylon Walker" />
<meta name="og:author_email" content="waylon@waylonwalker.com" />
<meta name="generator" content="markata 0.8.1.dev12" />
<meta name="monetization" content="$ilp.uphold.com/MGN2ni2YMXaQ" />
<meta name="theme-color" content="#322D39" />

<link rel="stylesheet" href="/app.css" />
<link rel="canonical" href="/" />
<link rel="amphtml" href="/amp/" />
<link rel="authorization_endpoint" href="https://indieauth.com/auth" />
<link rel="token_endpoint" href="https://tokens.indieauth.com/token" />
<link rel="amphtml" href="/amp" />
<link rel="micropub" href="archive" />
<link rel="webmention" href="https://webmention.io/waylonwalker.com/webmention" />
<link rel="preconnect" href="https://images.waylonwalker.com" />
<link rel="preconnect" href="https://covers.waylonwalker.com" />
<link rel="preconnect" href="https://stable-diffusion.waylonwalker.com" />
<link rel="preconnect" href="https://screenshots.waylonwalker.com" />
<link rel="apple-touch-icon" href="/8bitcc_48x48.png" />
<link rel="apple-touch-icon" href="/8bitcc_72x72.png" />
<link rel="apple-touch-icon" href="/8bitcc_96x96.png" />
<link rel="apple-touch-icon" href="/8bitcc_144x144.png" />
<link rel="apple-touch-icon" href="/8bitcc_192x192.png" />
<link rel="apple-touch-icon" href="/8bitcc_256x256.png" />
<link rel="apple-touch-icon" href="/8bitcc_384x384.png" />
<link rel="apple-touch-icon" href="/8bitcc_512x512.png" />

<script src="/htmx.min.js"></script>    </head>
    <body>
<nav class='w-full bg-gray-950 py-4 mb-8 sticky border-b border-pink-500'>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/start/" hx-boost="true">Start Here</a></li>
        <li><a href="/archive/" hx-boost="true">Archive</a></li>
        <li><a href="/about/" hx-boost="true">About</a></li>
        <li><a href="/feeds/" hx-boost="true">RSS</a></li>
    </ul>
</nav>             <footer style='margin-top: 20rem;'>© 2025</footer>

    </body>
    </html>
  </xsl:template>
</xsl:stylesheet>