---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: 'TIL: Bind arguments to dynamically generated lambdas in python'
date: 2020-04-27T12:13:00.000+00:00
status: published
description: This past week I had a really weird bug in my [kedro](https://kedro.readthedocs.io/)
  pipeline.  For some reason data running through my pipeline was coming out completely
  made no sense, but if I manually request raw data outside of the pipeline it matched
  expectations.
cover: "/static/bind-dynamic-lambdas.png"

---
This past week I had a really weird bug in my [kedro](https://kedro.readthedocs.io/) pipeline.  For some reason data running through my pipeline was coming out completely made no sense, but if I manually request raw data outside of the pipeline it matched expectations.

**NOTE** While this story is about a kedro pipeline, it can be applied anywhere closures are put into an iterable.

## ![Debugger to the rescue](https://images.waylonwalker.com/bind-dynamic-lambdas-1.png)

After a few days of looking at it off and on, I pinpointed that it was all the way down in the raw layer. Right as data is coming off of the database.  For this I already had existing `sql` files stored and a `read_sql` function to get the data so I opted to just set up the pipeline to utilize the existing code as much as possible, leaning on the [kedro](https://kedro.readthedocs.io/) framework a bit less.

I have dynamically created lists of pipeline nodes many times in the past, but typically I take data from [kedro](https://kedro.readthedocs.io/) input and use it in the lambda.  I prefer the simplicity of using lambdas over `functools.partial`.  It typically looks something like this.

``` python
# 👍  I do this all the time
from kedro.pipeline import node
from my_generic_project_lib import clean

datasets_to_clean = ['sales', 'production', 'inventory']
nodes = []
for dataset in datasets_to_clean:
   nodes.append(
      node(
         func=lambda x: clean(x)
         inputs = f'raw_{dataset}'
         outputs=f'int_{dataset}'
         tags=['int', dataset]
         name=f'create_int_{dataset}'
      )
   )
```

What was different this time is that I needed to pass in the name of the dataset to my read_sql function, not the data loaded in the framework.

``` python
# ❌ This does not work
from kedro.pipeline import node
from my_generic_project_lib import read_sql

datasets_to_read = ['sales', 'production', 'inventory']
nodes = []
for dataset in datasets_to_clean:
   nodes.append(
      node(
         func=lambda: read_sql(dataset) # 💥 The major issue
         inputs = f'dummy'
         outputs=f'int_{dataset}'
         tags=['int', dataset]
         name=f'create_int_{dataset}'
      )
   )
```

## ![Seriously](https://images.waylonwalker.com/bind-dynamic-lambdas-2.png)

As I am still oblivious to what has happened I pop in a `breakpoint()` and quickly see that during the first run the dataset passed into `read_sql` was `'inventory'`, in fact, every single one was `'inventory'`.  The lambda is just using the latest value of dataset from outside and has no `local` `dataset` attached to it.

## ![The simple fix ](https://images.waylonwalker.com/bind-dynamic-lambdas-3.png)

``` python
# 👍 Much Better
from kedro.pipeline import node
from my_generic_project_lib import read_sql

datasets_to_read = ['sales', 'production', 'inventory']
nodes = []
for dataset in datasets_to_clean:
   nodes.append(
      node(
         func=lambda dataset=dataset: read_sql(dataset) # dataset is now bound to the lambda ✨
         inputs = f'dummy'
         outputs=f'int_{dataset}'
         tags=['int', dataset]
         name=f'create_int_{dataset}'
      )
   )
```

## ![Try it yourself](https://images.waylonwalker.com/bind-dynamic-lambdas-4.png)

I made a slightly more simple example so that you can try it and play with it yourself, edit it, share it with your friends, laugh at my mistake, whatever you like.

<iframe height="400px" width="100%" src="https://repl.it/@WaylonWalker/BindDynamicLambdas?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
