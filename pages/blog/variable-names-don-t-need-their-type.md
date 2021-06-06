---
templateKey: blog-post
tags: ['python', 'dicuss']
title: Variables names don't need their type
date: 2020-04-08T11:03:00Z
status: published

---
So often I see a variables `type()` inside of its name and it hurts me a little
inside.  Tell me I'm right or prove me wrong below.

## Examples

Pandas `DataFrames` are probably the worst offender that I see

``` python
# bad
sales_df = get_sales()

# good
sales = get_sales()
```

Sometimes vanilla structures too!

``` python
# bad
items_list = ['sneakers', 'pencils', 'paper', ]

# good
items = ['sneakers', 'pencils', 'paper', ]
```

## Edge Cases?

It's so common when you need to get inside a data structure in a special way that itsn't provided by the library.... I am not exactly sure of a good way around it.

``` python
# bad ??
sales = get_sales()
sales_dict = sales.to_dict()

# good
🤷‍♀️
```

## Containers are plural

Always name your containers plural, so that naming while iterating is simple.

``` python
prices = {}
items = ['sneakers', 'pencils', 'paper', ]
for item in items:
   prices[item] = get_price(item)
```

Before I start fights 🥊 in code review, am I inline here or just being pedantic?
