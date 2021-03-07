---
templateKey: blog-post
related_post_label: Check out this related post
tags:
- python
- data
title: Filtering Pandas
date: 2019-09-24T05:00:00Z
status: published
description: Filtering pandas DataFrames many different ways.

---
## query

Good for method chaining, i.e. adding more methods or filters without assigning a new variable.

```python
# is
skus.query('AVAILABILITY == " AVAILABLE"')
# is not
skus.query('AVAILABILITY != " AVAILABLE"')
```

## masking

general purpose, this is probably the most common method you see in training/examples

```python
# is
skus[skus['AVAILABILITY'] == 'AVAILABLE']
# is not
skus[~skus['AVAILABILITY'] == 'AVAILABLE']
```

## isin

capable of including multiple strings to include

    # is in
    df[df.AVAILABILITY.isin(['AVAILABLE', 'AVL'])]
    # is not in
    df[~df.AVAILABILITY.isin(['AVAILABLE', 'AVL'])]

## contains

Good For partial matches

    # contains
    df[df.AVAILABILITY.str.contains('AVA')]
    # not contains
    df[~df.AVAILABILITY.str.contains('AVA')]

## MASKS

anything that we put inside of square brackets can be set as a variable then passed in.

    service_mask = skus['AVAILABILITY'] == 'AVAILABLE'
    name_mask = skus['NAME'] == 'Dell chromebook 11'

### Operators

& - and
\~ - not
| - or

### AVAILABLE and NAME

    df[service_mask & name_mask]

### AVAILABLE or NAME

    df[service_mask | name_mask]

### AVAILABLE and not NAME

    df[service_mask & ~name_mask]
