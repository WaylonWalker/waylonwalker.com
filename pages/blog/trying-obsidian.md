---
date: 2024-07-31
templateKey: blog-post
title: Trying Obsidian
published: true
tags:
  - blog
---

I am giving obsidian a try, this is a test post to learn the flow.  Something
that has been really hard for me for a long time is images, I don't include a
lot of images just because it takes so much longer just to get the post out.  I
store them in a separate repo, I need to resize and compress them for the web
so they aren't so big.

## Images are easy

This is my current wallpaper.

![trying-obsidian-20240731135759007.webp](https://dropper.waylonwalker.com/api/file/fe97308b-00f8-4860-be80-6869fa45d05a.webp)

> I took he screenshot and just pasted it in.

I have more about my process in this post about [[obsidian-image-converter]].

## It's still just markdown

I don't know why it took me so long to understand this but obsidian is just
markdown files.  I pretty much just plugged in my existing blog and it picked
up all the tags and was ready to run.  I now get some nice visualizations to
help me identify posts that were not ever tagged or maybe left unfinished.

## It leans hard on wikilinks

I just finished moving my backend over to md-it-python, which comes with some
good wiliklink support. I even make a [[sick-wikilink-hover]] feature that
previews wikilinks on hover.

![trying-obsidian-20240804194656515.webp](https://dropper.waylonwalker.com/api/file/fe12e8ca-fdfd-41de-adcb-dc14155324c3.webp)

Inside of obsidian when you start a wikilink it starts searching for posts to
link.  I get this feature in using the marksman lsp, and it's nice to see that
it works pretty similarly, but with much less setup and configuration.

![trying-obsidian-20240804194934445.webp](https://dropper.waylonwalker.com/api/file/4e0883a8-2430-49bf-99f3-2ce4df9516f5.webp)

## creating new files

The same keybinding that will take you to a new fill will create a [[obsidian-new-file]] in the root directory of your project.  This is very handy to create a bunch of new links and files quickly.  This feature does not work the greatest for my blog currently as it does not create them from a template, and I use templates to start all of my posts. see [[obsidian-using-templater-like-copier]].  I am now seeing why these plugins push so much automation into the templating system by directory.

## New keybindings

Until I really got myself in and working I didn't realize all of the vim
features that I would really need, [[obsidian-go-to-definition]] was one of the
very first ones.  Obsidian has a feature to take you to the note under the
cursor by pressing alt+enter, but that was not obvious at first.

## Renaming posts

Obsidian makes it so easy to rename a post, and it renames the file for you
without leaving the editor, needing to close the file or anything.  You can
just go to the top of the file and change the name without needing to find it
in a file tree or anything.  Its a very nice and clean feature.

## I miss my gqap

There are still some vim features like [[vim-gq]] that I use constantly to reflow
long lines into readable paragraphs no matter where I open them that I cannot
find a way to do in obsidian, and I miss it. ## Recent Posts.

!!! Note
    ok, so vim mode inside of obsidian really does work, and it does this, its
    just less obvious because of obsidians softwraps in the editor.  And I
    don't think it works on indented lines like these, in this note.

## missing seemless publish

I run pre-commit on my posts to clean up the whitespace and line endings.
Generally this does not do much, but aparantly obsidian is clashing with my
setup, and not running pre-commit correctly so I need to leave my editor to
publish a post.

With neovim I have a hotkey to commit verbosely with fugitive, `gic`, and to
push `gpp`, and I use this all the time as I am writing.

## Recent Posts

Using obsidian I edited  over 260 posts just this week!  Some whole sections
like my gratitute posts were kinda sitting completely untagged and I fixed that
up.

- [[weeknote-0]] (Modified: 2024-08-04 20:47:40)
- [[obsidian-go-to-definition]] (Modified: 2024-08-04 20:44:09)
- [[trying-obsidian]] (Modified: 2024-08-04 20:40:48)
- [[knock-and-sweep]] (Modified: 2024-08-03 21:44:57)
- [[blogging-in-2024]] (Modified: 2024-08-03 21:43:28)
- [[pandas-pattern]] (Modified: 2024-08-03 21:43:28)
- [[python-tips]] (Modified: 2024-08-03 21:43:28)
- [[productive-one-on-one]] (Modified: 2024-08-03 21:42:14)
- [[kedro-basics]] (Modified: 2024-08-03 21:41:58)
- [[passion]] (Modified: 2024-08-03 21:41:48)
- [[thank-you]] (Modified: 2024-08-03 21:41:17)
- [[animal-well-keyboard]] (Modified: 2024-08-03 21:41:07)
- [[automate-your-deploys]] (Modified: 2024-08-03 21:40:36)
- [[expand-one-line-links]] (Modified: 2024-08-03 21:39:48)
- [[journey]] (Modified: 2024-08-03 21:39:36)
- [[2018-retrospective]] (Modified: 2024-08-03 21:39:25)
- [[goals-2019]] (Modified: 2024-08-03 21:39:11)
- [[debugging-python]] (Modified: 2024-08-03 21:38:11)
- [[gatsby-rss-feed]] (Modified: 2024-08-03 21:38:01)
- [[pyspark]] (Modified: 2024-08-03 21:37:51)
- [[packages-to-investigate]] (Modified: 2024-08-03 21:37:40)
- [[git-diff-branches]] (Modified: 2024-08-03 21:37:33)
- [[practice-your-craft]] (Modified: 2024-08-03 21:37:23)
- [[mentorship-vs-sponsorship]] (Modified: 2024-08-03 21:37:17)
- [[gatsby-scripts-with-onload]] (Modified: 2024-08-03 21:37:06)
- [[long-variable-names-are-good]] (Modified: 2024-08-03 21:36:51)
- [[kedro-dependency-management]] (Modified: 2024-08-03 21:36:12)
- [[vim-notes]] (Modified: 2024-08-03 21:35:59)
- [[stories-10-10-2020-10-21-2020]] (Modified: 2024-08-03 21:34:59)
- [[new-machine-tpio]] (Modified: 2024-08-03 21:34:49)
- [[find-kedro-release]] (Modified: 2024-08-03 21:34:35)
- [[serverless-things-to-investigate]] (Modified: 2024-08-03 21:34:24)
- [[cmd-exe-tips]] (Modified: 2024-08-03 21:34:12)
- [[last-n-git-files]] (Modified: 2024-08-03 21:33:57)
- [[maintianing-multiple-git-remotes]] (Modified: 2024-08-03 21:33:49)
- [[fix-git-commit-author]] (Modified: 2024-08-03 21:33:41)
- [[reasons-to-kedro-notes]] (Modified: 2024-08-03 21:33:32)
- [[out-of-space]] (Modified: 2024-08-03 21:33:10)
- [[adding-google-fonts-to-a-gatsbyjs-site]] (Modified: 2024-08-03 21:32:57)
- [[strip-trailing-whitespace]] (Modified: 2024-08-03 21:32:44)
- [[happy]] (Modified: 2024-08-03 21:31:48)
- [[brainstorming-kedro-hooks]] (Modified: 2024-08-03 21:31:37)
- [[kedro-preflight]] (Modified: 2024-08-03 21:31:06)
- [[should-i-switch-to-zeit-now]] (Modified: 2024-08-03 21:30:50)
- [[kedro-catalog]] (Modified: 2024-08-03 21:30:35)
- [[python-deepwatch]] (Modified: 2024-08-03 21:30:20)
- [[career-day-wapello-2021]] (Modified: 2024-08-01 15:44:43)
- [[obsidian-image-converter]] (Modified: 2024-08-01 15:40:11)
- [[obsidian-using-templater-like-copier]] (Modified: 2024-08-01 15:39:49)
- [[gratitude-199]] (Modified: 2024-08-01 12:47:18)
- [[gratitude]] (Modified: 2024-08-01 11:26:34)
- [[gratitude-97]] (Modified: 2024-08-01 10:17:01)
- [[gratitude-147]] (Modified: 2024-08-01 10:16:15)
- [[gratitude-007]] (Modified: 2024-08-01 10:15:59)
- [[good-morning]] (Modified: 2024-08-01 10:15:48)
- [[gratitude-005]] (Modified: 2024-08-01 10:15:33)
- [[gratitude-003]] (Modified: 2024-08-01 10:15:11)
- [[gratitude-004]] (Modified: 2024-08-01 10:14:59)
- [[gratitude-001]] (Modified: 2024-08-01 10:14:50)
- [[gratitude-008]] (Modified: 2024-08-01 10:14:38)
- [[gratitude-002]] (Modified: 2024-08-01 10:14:26)
- [[gratitude-006]] (Modified: 2024-08-01 10:14:09)
- [[gratitude-093]] (Modified: 2024-08-01 10:12:37)
- [[gratitude-081]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-082]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-083]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-084]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-085]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-086]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-087]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-088]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-089]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-090]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-103]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-104]] (Modified: 2024-08-01 07:16:40)
- [[the-good-old-days]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-050]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-051]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-052]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-053]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-054]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-055]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-056]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-057]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-058]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-059]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-060]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-061]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-062]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-063]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-064]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-065]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-066]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-067]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-068]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-069]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-070]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-071]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-072]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-073]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-074]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-075]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-076]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-077]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-078]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-079]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-080]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-023]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-024]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-025]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-026]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-027]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-028]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-029]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-030]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-031]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-032]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-033]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-034]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-035]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-036]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-037]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-039]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-040]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-041]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-042]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-043]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-044]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-045]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-046]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-047]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-048]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-049]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-190]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-191]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-192]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-193]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-194]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-195]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-196]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-197]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-198]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-91]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-98]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-99]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-009]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-010]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-011]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-012]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-013]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-014]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-015]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-016]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-017]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-018]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-019]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-020]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-021]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-022]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-160]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-161]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-162]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-163]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-164]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-165]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-166]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-167]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-168]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-169]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-170]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-171]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-172]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-173]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-174]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-175]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-176]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-177]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-178]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-179]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-180]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-181]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-182]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-183]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-184]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-185]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-186]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-187]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-188]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-189]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-127]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-128]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-129]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-130]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-131]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-132]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-133]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-134]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-135]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-136]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-137]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-138]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-139]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-140]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-141]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-142]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-143]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-144]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-146]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-148]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-149]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-150]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-151]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-152]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-153]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-154]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-155]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-156]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-157]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-158]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-159]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-095]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-096]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-100]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-101]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-102]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-105]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-106]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-107]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-108]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-109]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-110]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-111]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-112]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-113]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-114]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-115]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-116]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-117]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-118]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-119]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-120]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-121]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-122]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-123]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-124]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-125]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-126]] (Modified: 2024-08-01 07:16:40)
- [[gratitude-093-1]] (Modified: 2024-07-31 18:27:43)
- [[markata-supports-jinja-plugins-0-5-0-dev2]] (Modified: 2024-07-31 13:41:57)
- [[markata-telescope-picker]] (Modified: 2024-07-31 13:41:57)
- [[pyohio-cfp]] (Modified: 2024-07-31 13:41:57)
- [[reader]] (Modified: 2024-07-31 13:41:57)
- [[ubuntu]] (Modified: 2024-07-31 13:41:57)
- [[uses]] (Modified: 2024-07-31 13:41:57)
- [[upcoming-streams]] (Modified: 2024-07-31 13:41:57)
- [[from-markdown-to-blog-with-markata]] (Modified: 2024-07-31 13:41:57)
- [[lookatme-slides]] (Modified: 2024-07-31 13:41:57)
- [[markata-0-3-0]] (Modified: 2024-07-31 13:41:57)
- [[markata-configure-head]] (Modified: 2024-07-31 13:41:57)
- [[markata-github-pages]] (Modified: 2024-07-31 13:41:57)
- [[markata-now-uses-hatch]] (Modified: 2024-07-31 13:41:57)
- [[htmx-on-my-blog]] (Modified: 2024-07-31 13:41:57)
- [[keyboard-driven-vscode]] (Modified: 2024-07-31 13:41:57)
- [[markata-todoui-live-replay-4-6-2022]] (Modified: 2024-07-31 13:41:57)
- [[markata]] (Modified: 2024-07-31 13:41:57)
- [[packages-i-maintain]] (Modified: 2024-07-31 13:41:57)
- [[pipx-examples]] (Modified: 2024-07-31 13:41:57)
