---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Avoid Nesting Loops in Python
date: 2020-10-11T05:00:00.000+00:00
status: draft
description: ''
cover: ''

---
Nesting loops inside of each other in python makes for much harder code to understand, it takes more brain power to understand, and is thus more error prone than if its avoidable.  One issue with this complexity is that toy examples may make sense, but most real example will grow and become more deeply nested over time.  Avoiding this complexity from the start can help simplify the project in the future.


## setup

Lets take a pretty simple example where we are using a ficticious library to get some sales data for our transportation company.  The api allows us to fetch teh sales data for one class of vehicle and one region at a time.

``` python
import pandas as pd

from datastore import get_sales  # ficticious library

cars = ['sedan', 'coupe', 'hatchback']
regions = ['US', 'CA', 'MX']
```

## ❌ Nesting Loops

We have setup to fetch our data with two lists that represent the vehicles and regions that we want to analyze.  We know that we need to make a call to `get_sales` for every vehicle and region so nesting loops is a very common first solution to jump to.

``` python
sales = pd.DataFrame()
for car in cars:
   for region in regions:
      new_sales = get_sales(car, region)
      sales = pd.concat([sales, new_sales])
```

## itertools.product

Python provides us with the beautiful itertools module that allows us to prepare our inputs for this in a much more susynct manner.  The product function of itertools will give us every combination of any number of iterables

``` python
import itertools
list(itertools.product(cars, regions))
```

> note that itertools returns a generator for most if not all functions, list() will turn that into a list that we can see.  This works great for small datasets, but might not be advisable on larger ones.

**output**
``` python
[('sedan', 'US'),
 ('sedan', 'CA'),
 ('sedan', 'MX'),
 ('coupe', 'US'),
 ('coupe', 'CA'),
 ('coupe', 'MX'),
 ('hatchback', 'US'),
 ('hatchback', 'CA'),
 ('hatchback', 'MX')]
```

## itertools.procuct for loop

Now that we have every comination of our two sets of inputs in a single list, we can iterate over that list one time.

``` python
sales = pd.DataFrame()
for car, region in itertools.product(cars, regions):
   new_sales = get_sales(car, region)
   sales = pd.concat([sales, new_sales])
```

## itertools.product list comprehension

The above follows a python anti-pattern, initialize then edit.  In some cases it might be a bit more readable to do it that way, you can be the judge, but in our simple case we can simply achieve the same results using a list comprehension.

``` python
pd.concat([get_sales(cars, region) for cars, region in itertools.product(cars, regions)])
```
## dictionaries

``` python
sales_args = {
   'cars': ['sedan', 'coupe', 'hatchback'],
   'regions': ['US', 'CA', 'MX'],
}

pd.concat([get_sales(*sales_arg) for sales_arg in itertools.product(*sales_args.values())])
```

``` python
sales_args = {
   'cars': ['sedan', 'coupe', 'hatchback'],
   'regions': ['US', 'CA', 'MX'],
   'month': ['MAR', 'APR', 'MAY']
}

pd.concat([get_sales(*sales_arg) for sales_arg in product(*sales_args.values())])
```

---

## Chaining
_containers of containers_

``` python
vehicles = {
	'cars': ['sedan', 'coupe', 'hatchback'],
    'trucks': ['light', 'heavy', 'sport', 'offroad'],
    'van': ['box', 'mini', 'full', ],

}
```

```
for vehicle in vehicles:
	for sub_class in vehicles[vehicle]:
      new_sales = get_sales(sub_class)
      new_sales['sub_class'] = sub_class
      new_sales['vehicle'] = vehicle
      sales = pd.concat([sales, new_sales])
```

```
 list(itertools.chain(*[list(itertools.product([k], v)) for k, v in vehicles.items()]))
```

output
```
[('cars', 'sedan'),
 ('cars', 'coupe'),
 ('cars', 'hatchback'),
 ('trucks', 'light'),
 ('trucks', 'heavy'),
 ('trucks', 'sport'),
 ('trucks', 'offroad'),
 ('van', 'box'),
 ('van', 'mini'),
 ('van', 'full')]
 ```
