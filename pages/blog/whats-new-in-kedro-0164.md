---
templateKey: blog-post
related_post_label: Check out this related post
tags: ['python', 'kedro',]
title: What's New in Kedro 0.16.4
date: 2020-08-01T05:00:00Z
status: published
description: If we take a look at the release notes I see one **major**
    feature improvement on the list, auto-discovery of hooks.
cover: '/static/whats-new-in-kedro-0164.png'

---

If we take a look at the [release notes](https://github.com/quantumblacklabs/kedro/blob/master/RELEASE.md) I see one **major** feature improvement on the list, auto-discovery of hooks.

``` markdown
## Major features and improvements

* Enabled auto-discovery of hooks implementations coming from installed plugins.
```

This one comes a bit surprising as it was just casually mentioned in [#435](https://github.com/quantumblacklabs/kedro/issues/435)

[![auto enabled plugins mentioned in issue 435](https://images.waylonwalker.com/kedro-435.png)](https://github.com/quantumblacklabs/kedro/issues/435)

## Think pytest

As mentioned in [#435](https://github.com/quantumblacklabs/kedro/issues/435) this is the model that pytest uses. Not all plugins automatically start doing things right out of the box but require a CLI argument.

## simplicity

It feels a bit crazy that simply installing a package will change the way that your pipeline gets executed. I do like that it requires just a bit less reaching into the framework stuff for the average user. Most folks will be able to write in the catalog and nodes without much change to the rest of the project.

## Implementation

Reading through the [docs](https://kedro.readthedocs.io/en/stable/07_extend_kedro/05_plugins.html#hooks), they show us that we can make our hooks automatically register by adding a `kedro.hooks` endpoint that points to a _singleton_ instance of our hook.

_from the docs_

``` python
setup(
    ...
    entry_points={"kedro.hooks": ["plugin_name = plugin_name.plugin:hooks"]},
)

import logging

from kedro.framework.hooks import hook_impl

class MyHooks:
    @hook_impl
    def after_catalog_created(self, catalog): # pylint: disable=unused-argument
        logging.info("Reached after_catalog_created hook")

hooks = MyHooks()
```

## Careful with the singletons

_hook authors beware_

I will be a bit cautious before installing a plugin that is automatically registered. I know its not a common pattern, but if you were to leverage any part of two kedro projects at the same time, and project-specific data was stored in the instance of the hook it will likely be broken.

As long as the hook doesn't store data on the instance you will be ok. Hooks like what they have in the examples will be ok. They generally just take some information from the lifecycle arguments and do something at their prescribed lifecycle point.

Many of the hooks I am seeing in the wild are already more complicated and require the hooks author to utilize an ` __init__ ` method and store data on the instance. If you were to do this on two pipelines simultaneously it would break.

## Can my hook be auto-discovered

If your hook doesn't include a `__init__` method its a fairly easy yes, otherwise be aware of the potential dangers of passing singleton on to your users.

## Use Virtual environments

Whatever virtual environment manager you use, it is more important than ever to make sure you **DO NOT** install plugins in your global environment. Generally, you should always run projects _even toys or tests_ in a **virtual**  **environemnt**.

_I use conda_

``` bash
conda create -n my-sample-env python=3.8 -y
```

## Overall

I think this is a really interesting direction for the project to go to. Hooks are still really early. The implementation is good, but I foresee us getting some more functionality that may require us to rely on the ` __init__ ` method a little less.  I think there are going to be some really cool hooks that can leverage the simplicity of auto-discoverability.
