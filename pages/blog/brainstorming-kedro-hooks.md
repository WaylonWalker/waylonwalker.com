---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Brainstorming Kedro Hooks
date: 2020-05-22T22:02:00.000+00:00
status: published
description: "This post is a \U0001F9E0 branstorming work in progress, I will likely
  use it as a storage location/brain dump of hook ideas."
cover: "/static/brainstorming-kedro-hooks.png"

---
This post is a 🧠 branstorming work in progress.

> ### What is Kedro 🤔
>
> If you are completely unsure what kedro is be sure to check out my [what is kedro](https://waylonwalker.com/wike) post

## after_catalog_created

* filepath replacer
* bucket replacer

## before_pipeline_run

* preflight
* check that data exists
* run `kedro_static_viz`
* run mypy
* run interrogate
* run flake8

## after_pipeline_run

* Great Expectations
* send email
* send slack

## before_node_run

## after_node_run

* Great Expectations
* save stats/meta data
*

## Execution Order

hooks are executed in reverse order of the hooks list.

hooks with `tryfirst` will be moved to the end of the list
hooks with `trylast` will be moved to the end of the list

1. after_catalog_created
2. before_pipeline_run

* args
  * run_params = run_params = {'run_id': '2020-05-23T15.24.23.958Z', 'project_path': '/mnt/c/temp/kedro0160', 'env': 'local', 'kedro_version': '0.15.9', 'tags': (), 'from_nodes': \[\], 'to_nodes': \[\], 'node_names': (), 'from_inputs': \[\], 'load_versions': {}, 'pipeline_name': None, 'extra_params': {}, 'git_sha': None}
  * pipeline
  * catalog

1. before_node_run
2. after_node_run
3.

## When does data get saved???

* before or after node hook?

## ??Unsure??

* does before  catalog load have access to parameters?
  * Yes
*

### \[steel toes\](https://github.com/waylonwalker/steel-toes/)6

_I was way too excited about this one and already created it_

_prevents pain from stepping on your teammates toes_

Kedro is so amazing at promoting collaboration between team members.  Each team member can check out the code, branch, and start work on their own section of the pipeline.  Issues can arrise if the team members section of the pipeline happen to cross.  Breaking changes happen, BREAKS during development happen and can completely kill a teammates workflow.

* is there a way to prevent toe stepping?
* try to load `filepath_<branch>`
* if load fails try `filepath`
* save data to `filepath_<branch>`

**how**

* on after_catalog_load check for existing "branch" data
* if "branch" data exists load that
* otherwise keep default
*

### Run only nodes that have changed

* store a deephash of functions code
* store a hash of the inputs
* if neither code or inputs changed run function, otherwise skip.
  * How could a hook choose to skip the node?

## Static viz hook

Before pipeline run

* make site
* Set node status to queued

Before node run

* Set running status

After node run

* Set running status

On pipeline error

* Set run status

On node error

* Set error status

After pipeline run

* Set complete status

After node run

* set complete
