---
title: '💭 SQL on Pandas - DuckDB'
date: 2023-07-28T14:59:37
templateKey: link
link: https://duckdb.org/docs/guides/python/sql_on_pandas
tags:
  - python
  - data
  - duckdb
  - pandas
published: true

---

> duckdb can just query any pandas dataframe that is in memory.

> I tried running it against a list of objects and got this error.  Great error message that gives me supported types right in the message.

``` python
Make sure that "posts" is either a pandas.DataFrame, duckdb.DuckDBPyRelation, pyarrow Table, Dataset, RecordBatchReader, Scanner, or NumPy ndarrays with supported format
```

[Original thought](https://duckdb.org/docs/guides/python/sql_on_pandas)
