---
templateKey: blog-post
tags: ['bash']
title: Newsboat
date: 2021-01-02T00:00:00
status: published
description: ''
cover: "/static/newsboat.png"

---

Web browsers are a black hole of productivity.  I try to use them as little as
possible when it is time to focus.  I try to use `help`, `?`, or `??` with
ipython, or --help at the command line as much as possible.  What about that
time I am trying to see what my online friends are posting on their sites?  I
used to used google reader quite heavily before that was taken down.

## Newsboat

I am going to give a terminal rss reader a try for a bit and see how that goes
for me.  I have really struggled to get into an rss reader since google reader
died.

## installation

I installed with the reccomended snap for Ubuntu.

``` bash
sudo snap install newsboat
```

## Adding feeds
_super simple_

Running help for newsboat directed me towards their config files at the bottom.

``` bash
❯ newsboat --help
newsboat r2.22
usage: /snap/newsboat/3849/usr/local/bin/newsboat [-i <file>|-e] [-u <urlfile>] [-c <cachefile>] [-x <command> ...] [-h]
	-e, --export-to-opml		export OPML feed to stdout
	-r, --refresh-on-start		refresh feeds on start
	-i, --import-from-opml=<file>	import OPML file
	-u, --url-file=<urlfile>	read RSS feed URLs from <urlfile>
	-c, --cache-file=<cachefile>	use <cachefile> as cache file
	-C, --config-file=<configfile>	read configuration from <configfile>
	-X, --vacuum			compact the cache
	-x, --execute=<command>...	execute list of commands
	-q, --quiet			quiet startup
	-v, --version			get version information
	-l, --log-level=<loglevel>	write a log with a certain loglevel (valid values: 1 to 6)
	-d, --log-file=<logfile>	use <logfile> as output log file
	-E, --export-to-file=<file>	export list of read articles to <file>
	-I, --import-from-file=<file>	import list of read articles from <file>
	-h, --help			this help
	    --cleanup			remove unreferenced items from cache

Files:
	- configuration:  /home/nic/snap/newsboat/3849/.newsboat/config
	- feed URLs:      /home/nic/snap/newsboat/3849/.newsboat/urls
	- cache:          /home/nic/snap/newsboat/3849/.newsboat/cache.db

Support at #newsboat at https://freenode.net or on our mailing list https://groups.google.com/g/newsboat
For more information, check out https://newsboat.org/
```

I just need to edit its urls file.

``` bash
nvim ~/snap/newsboat/3849/.newsboat/urls
```

The Urls file is just a list of urls to rss feeds.  Adding mine in allowed me to see all of my posts.

``` bash
https://waylonwalker.com/rss.xml
```


## Config

I took most of my config from a [blog
post](http://evantravers.com/articles/2020/04/15/reworking-my-rss-reading/)
that I found by Evan Travers.  It set some sane defaults to the reading width
and vim keys.


``` bash
# http://evantravers.com/articles/2020/04/15/reworking-my-rss-reading/
# Hide feeds where all the items are read.
show-read-feeds no

# Make the text width readable
text-width 50

# Use multiple threads to download all the news faster.
reload-threads 11

# browser ~/bin/newsboat-browser.sh
# browser "/usr/bin/brave-browser %u"

# unbind keys
unbind-key ENTER
unbind-key j
unbind-key k
unbind-key J
unbind-key K
unbind-key ^D
unbind-key ^U
unbind-key o
unbind-key g
unbind-key G

# bind keys - vim style
bind-key j down
bind-key k up
bind-key l open
bind-key h quit
bind-key ^D pagedown
bind-key ^U pageup
bind-key b toggle-source-view
bind-key U toggle-show-read-feeds
bind-key u show-urls
bind-key g home
bind-key G end
bind-key b open-in-browser-and-mark-read
bind-key B open-in-browser
bind-key i sort
bind-key I rev-sort
```

## GUI Browser

No matter how many different guides I tried I keedp getting `error code 127`
when trying to `open-in-browser`.  Please let me know if you know how to fix
this. For now I am just going to roll with it.


## Here's how it looks

![newsboat feed](https://images.waylonwalker.com/newsboat-feed-waylonwalker-com.png)

> browsing a feed in newsboat

![newsboat article](https://images.waylonwalker.com/newsboat-article.png)

> reading an article in newsboat
