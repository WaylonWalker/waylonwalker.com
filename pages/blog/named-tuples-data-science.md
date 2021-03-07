---
templateKey: blog-post
title: Clean up Your Data Science with Named Tuples
date: 2019-09-11
time: T05:00:00Z
status: published
description:
cover: "/static/andrew-spencer-Ricopz7JkbE-unsplash.jpg"
related_post:
# - src/pages/blog/background-tasks-in-python-for-data-science.md
tags:
- python
- data

---
If you are a regular listener of [TalkPython](https://talkpython.fm) or PythonBytes you have hear Michael Kennedy talk about Named Tuples many times, but what are they and how do they fit into my data science workflow.

## Example

As you graduate your scripts into modules and libraries you might start to notice that you need to pass a lot of data around to all of the functions that you have created. For example if you are running some analysis utilizing `sales`, `inventory`, and `pricing` data.  You may need to calculate total revenue, inventory on hand.  You may need to pass these data sets into various models to drive production or pricing based on predicted volumes.

## Load data

Here we setup functions that can load data from the sales database.  Assume that we also have similar functions to `get_inventory` and `get_pricing`.

``` python
def get_engine():
    engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')

def get_sales():
    '''
    gets sales history from the sales database
    '''
    engine = get_engine()
    with engine.connect() as con:
        sql = '''select * from sales.history'''
        df = pd.read_sql(sql, con)
    engine.dispose()
    return df

def get_inventory():
    ...

def get_pricing():
    ...
```

### Create Metrics

Here we create our first function to calculate some metrics.  There are likely many of these functions that repeat a similar pattern.  They use similar data and have their own custom logic for calculations and joins.

``` python
def calculate_total_revenue(sales, pricing):
    """calculates the total sales revenue for all of company XYZ"""
    sales = sales.join(pricing.set_index('sku'), on='sku')
    sales['revenue'] = sales['qty'] * sales['price']
    return sales['revenue'].sum()

def calculate_inventory_sale_ratio(sales, inventory, pricing):
    ...

def calculate_inventory_sale_ratio(inventory, sales):
    ...
```

Furthermore these functions will need to be called somewhere, this might be in a `make_report()` function that puts this data into an html template to be sent out to stakeholders, or to be served on a website. Notice how we have the same data showing up time and time again.  And sometimes we even ask for it in a different order 😲.It is important to recognize this early in the project before this gets our of hand.

```python
def make_report():
    """Makes stakeholder report for company XYZ"""
    sales = get_sales()
    inventory = get_inventory()
    pricing = get_pricing()

    revenue = calculate_total_revenue(sales, pricing)
    sales_ratio = inventory_sale_ratio(sales, inventory, pricing)
    inventory_sale_ratio(inventory, sales)
```

### getting out of hand

Along the way our features, models, and out supervisors have all had their own needs and we have added new datasets, and several flags. This is the point at which anxiety starts creeping in.  We start spending a lot of time double checking the order of each call to make sure that we dont make a mistake.  And when someone else touches this model, we know what it looks like and cant help but think, "Oh God I hope they didn't screw up that horrid module!"

``` python
def calculate_total_revenue(sales, pricing, inventory, stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000'):
    sales = (sales
                .join(pricing.set_index('sku'), on='sku')
                .join(inventory.set_index('sku'), on='sku')
            )
    sales['revenue'] = sales['qty'] * sales['price']
    sales  = sales.query(f'price > {min_price}')
    sales  = sales.query(f'sale_date > {min_date}')
    sales  = sales.query(f'sale_date < {end_date}')
    return sales['revenue'].sum()

def calculate_inventory_sale_ratio(sales, pricing, inventory, stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000'):
    ...

def calculate_inventory_sale_ratio(sales, pricing, inventory, stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000'):
    ...

def model_new_prices(sales, pricing, inventory, stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000'):
    ...

def model_production(sales, pricing, inventory, stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000'):
    ...

def completely_custom_metric_for_steve(sales, pricing, inventory, stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000'):
    """Steve has been here 30 years and doesnt trust our metrics unless he can validate against the old metrics"""
    ...
```

It gets even crazier when you start calling all of these functions! Note that we have a common theme of the same data getting passed into

``` python
def make_report(stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000', is_for_steve=False):
    """Makes stakeholder report for company XYZ"""
    sales = get_sales()
    inventory = get_inventory()
    pricing = get_pricing()

    revenue = calculate_total_revenue(stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000')
    sales_ratio = sales_ratio = inventory_sale_ratio(stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000')
    inventory_sale_ratio = inventory_sale_ratio(stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000')
    predicted_prices = model_new_prices(stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000')
    predicted_production_rates = model_production_rate(stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000')
    completely_custom_metric_for_steve(stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000')

    # render report
    ...
```

### This code Stinks

⌚ _Time for refactoring_

While our code started out good it has grown stinky over time.  It will works fine, but it could be better and more enjoyable to work with.  What we have here is a code smell called `data clump`.  This is a group of data that always appears together.  It would be appropriate to formally group this data together.  One way to do this in python is to use nametuples.  It is a very simple technique that allows us to define a data structure that contains a specific set of attributes that we can access using `.attribute_name`.  Replacing this `data clump` with a formal group of data will allow us to reduce the number of arguments in all of our functions. Add new attributes easily. And not rely on positional arguments.  This code will be easier to maintain, read, and write.

> What we have here is a code smell called `data clump`

**create a namedtuple**

```python
from collections import namedtuple

ModelData = namedtuple('modin_data', 'sales pricing inventory stored_at min_price start_date end_date')
```

**use the namedtuple**

```python
data = ModelData(
    sales=get_sales(),
    pricing=get_pricing(),
    inventory=get_inventory(),
    stored_at='LAX'
    min_price=100
    start_date = datetime.today() - datetime.timedelta(days=30)
    end_date = datetime.today()
    )
```

**refactor functions**
Now that we have a clean data object how do we use it.  Simple, we pass in one data object, then access each attribute with the dot operator. These functions are now much cleaner to call and read.  Here I have chosen a poor name for our `data`, but in a real scenario you may have multple `namedtuples`.

``` python
def calculate_total_revenue(data):
    sales = (data.sales
                .join(data.pricing.set_index('sku'), on='sku')
                .join(data.inventory.set_index('sku'), on='sku')
            )
    sales['revenue'] = sales['qty'] * sales['price']
    sales  = sales.query(f'price > {data.min_price}')
    sales  = sales.query(f'sale_date > {data.min_date}')
    sales  = sales.query(f'sale_date < {data.end_date}')
    return sales['revenue'].sum()

...
```

**call the function**

Now that all of the data is store in a single object it is really easy to call each of our functions using one data instance.

``` python
def make_report(stored_at='LAX', min_price=100, start_date='01-01-1999', end_date='01-01-3000', is_for_steve=False):
    """Makes stakeholder report for company XYZ"""
    data = ModelData(stored_at=stored_at, min_price=min_price, start_date=start_date, end_date=end_date)

    revenue = calculate_total_revenue(data)
    sales_ratio = sales_ratio = inventory_sale_ratio(data)
    inventory_sale_ratio = inventory_sale_ratio(data)
    predicted_prices = model_new_prices(data)
    predicted_production_rates = model_production_rate(data)
    completely_custom_metric_for_steve(data)

    # render report
    ...
```

### 🧹 Clean up your data science

Named Tuples are a great way to clean up your data science code and reduce `Data Clumps`.  Anytime you have multiple data sets that almost always get used together `namedtuple`s are a great way to clean up your code, make it more readable and more maintainable.  If you find that you also have functions that are tightly coupled to this data you might want to consider using a `class` instead of a `namedtuple`, but that is for another article.
