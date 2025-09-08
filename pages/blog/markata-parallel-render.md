---
date: 2025-07-01 08:05:58
templateKey: blog-post
title: markata parallel render
tags:
  - python
published: True

---


``` bash
  _._   __/__   __  __ _/_   Recorded: 07:53:56  Samples:  71681
 /_//_/// /_\ / //_// / //_'/ //     Duration: 92.741    CPU time: 91.748
/_/                      v4.5.1

Program: /home/waylon/git/waylonwalker.com/.venv/bin/markata build --pdb

92.740 Markata.run  markata/__init__.py:443
`- 92.714 HookCaller.__call__  pluggy/_hooks.py:479
      [2 frames hidden]  pluggy
         92.714 PluginManager._hookexec  pluggy/_manager.py:106
         |- 38.207 wrapper_register  markata/hookspec.py:265
         |  |- 26.105 render  plugins/link_collector.py:59
         |  |  |- 10.012 BeautifulSoup.__init__  bs4/__init__.py:122
         |  |  |     [14 frames hidden]  bs4, html
         |  |  |- 5.599 <listcomp>  plugins/link_collector.py:181
         |  |  |- 4.050 <listcomp>  plugins/link_collector.py:173
         |  |  |- 3.466 Markata.map  markata/__init__.py:565
         |  |  |`- 2.092   markata/__init__.py
         |  |  `- 0.942 BeautifulSoup.find_all  bs4/element.py:2008
         |  |        [2 frames hidden]  bs4
         |  |- 9.107 render  markata/plugins/render_markdown.py:260
         |  |`- 8.902 result_iterator  concurrent/futures/_base.py:612
         |  |        [5 frames hidden]  concurrent, threading, <built-in>
         |  `- 2.079 glob  markata/plugins/glob.py:112
         |`- 1.909 <listcomp>  markata/plugins/glob.py:161
         |        `- 1.908 Future.result  concurrent/futures/_base.py:428
         |              [3 frames hidden]  concurrent, threading, <built-in>
         |- 25.708 render  markata/plugins/post_template.py:639
         |`- 25.612 render_article  markata/plugins/post_template.py:404
         |     |- 22.223 <dictcomp>  markata/plugins/post_template.py:421
         |     |  `- 22.200 render_template  markata/plugins/post_template.py:429
         |     |`- 22.185 Template.render  jinja2/environment.py:1269
         |     |        `- 21.210 root  templates/post.html:4
         |     |`- 20.937 root  templates/base.html:4
         |     |              `- 20.455 block_content  templates/post.html:17
         |     |                 |- 11.212 root  templates/recent.html:4
         |     |                 |`- 10.853 root  templates/feed_sm_partial.html:4
         |     |                 |     `- 8.392 Environment.getattr  jinja2/environment.py:480
         |     |                 |`- 8.328 Feed.posts  markata/plugins/feeds.py:329
         |     |                 |           `- 8.300 Feed.map  markata/plugins/feeds.py:352
         |     |                 |`- 7.963 Markata.map  markata/__init__.py:565
         |     |                 |                 `- 7.786 <listcomp>  markata/__init__.py:628
         |     |                 |`- 6.465   markata/__init__.py
         |     |                 `- 8.486 call  jinja2/runtime.py:260
         |     |`- 8.468 Feed.map  markata/plugins/feeds.py:352
         |     |                       `- 8.394 Markata.map  markata/__init__.py:565
         |     |`- 8.326 <listcomp>  markata/__init__.py:628
         |     |                             `- 7.086   markata/__init__.py
         |`- 3.015 Cache.set  diskcache/core.py:749
         |           [3 frames hidden]  diskcache
         |- 7.788 save  markata/plugins/feeds.py:462
         |  `- 7.779 create_page  markata/plugins/feeds.py:493
         |     |- 4.530 Template.render  jinja2/environment.py:1269
         |     |`- 2.437 root  templates/feed.html:4
         |     |     `- 2.360 root  templates/base.html:4
         |     |`- 2.231 block_content  templates/feed.html:17
         |     |           `- 2.118 root  templates/feed_partial.html:4
         |     |`- 1.298 Environment.getattr  jinja2/environment.py:480
         |     |                 `- 1.290 Feed.posts  markata/plugins/feeds.py:329
         |     |`- 1.290 Feed.map  markata/plugins/feeds.py:352
         |     |                       `- 1.276 Markata.map  markata/__init__.py:565
         |     |- 1.325 Feed.map  markata/plugins/feeds.py:352
         |     |`- 1.317 Markata.map  markata/__init__.py:565
         |     `- 1.237 Cache.set  diskcache/core.py:749
         |- 7.029 pre_render  markata/plugins/auto_description.py:185
         |`- 6.840 set_description  markata/plugins/auto_description.py:137
         |     `- 5.791 get_description  markata/plugins/auto_description.py:107
         |        |- 4.485 MarkdownIt.parse  markdown_it/main.py:256
         |        |     [8 frames hidden]  markdown_it
         |`- 1.066 MarkdownIt.__init__  markdown_it/main.py:33
         |- 5.730 pre_render  markata/plugins/analytics.py:102
         |  |- 2.397 savefig  matplotlib/pyplot.py:1238
         |  |     [4 frames hidden]  matplotlib
         |  `- 2.004 heatmap  seaborn/matrix.py:355
         |        [10 frames hidden]  seaborn, matplotlib
         |- 1.704 post_render  plugins/permalink_aria.py:40
         |`- 1.588 process_html_content  plugins/permalink_aria.py:13
         |- 1.619 save  markata/plugins/publish_source.py:83
         |  `- 1.216 Post.dumps  markata/plugins/post_model.py:333
         |`- 1.203 Post.yaml  markata/plugins/post_model.py:254
         |        `- 1.044 dump  yaml/__init__.py:248
         |              [3 frames hidden]  yaml
         `- 1.183 post_render  plugins/wikilink_hover.py:104
            `- 1.094 do_hover_links  plugins/wikilink_hover.py:126

[07:55:38] save complete                                                                            __init__.py:465
           teardown running                                                                         __init__.py:462
           teardown complete                                                                        __init__.py:465
           lifetime cache hit rate 0.17%                                                            __init__.py:471
           lifetime cache hits/misses 36/21118                                                      __init__.py:476
           run cache hit rate 0.17%                                                                 __init__.py:482
           run cache hits/misses 36/21118                                                           __init__.py:487

Map Cache Statistics:
Total calls: 17197
Cache hits: 15317
Cache misses: 1880
Hit rate: 89.1%
Cache size: 1880
```
