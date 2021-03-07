---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Create Custom Kedro Dataset
date: 2020-05-15T05:00:00Z
status: published
description: Kedro provides an efficient way to build out data catalogs with their
  yaml api.  It allows you to be very declaritive about loading and saving your data.  For
  the most part you just need to tell Kedro what connector to use and its filepath.  When
  running Kedro takes care of all of the read/write, you just reference the catalog
  key.
cover: "/static/create-custom-kedro-dataset.png"

---
Kedro provides an efficient way to build out data catalogs with their yaml api.  It allows you to be very declaritive about loading and saving your data.  For the most part you just need to tell Kedro what connector to use and its filepath.  When running Kedro takes care of all of the read/write, you just reference the catalog key.

## But what is happening behind the scenes

Under the hood there is an `AbstractDataSet` that each connector inherits from.  It sets up a lot of the behind the scenes structure for us so that we dont have to.  For the most part kedro has connectors for about anything that you want to load, csv, parquet, sql, json, from about anywhere, http, s3, localfile system are just some of the examples.

Here is a DataSet implementation from their docs.  Here you can see the barebones example straight from the docs.  Parameters from the yaml catalog will get passed in

``` python
from pathlib import Path

import pandas as pd

from kedro.io import AbstractDataSet


class MyOwnDataSet(AbstractDataSet):
    def __init__(self, param1, param2, filepath, version):
        super().__init__(Path(filepath), version)
        self._param1 = param1
        self._param2 = param2

    def _load(self) -> pd.DataFrame:
        load_path = self._get_load_path()
        return pd.read_csv(load_path)

    def _save(self, df: pd.DataFrame) -> None:
        save_path = self._get_save_path()
        df.to_csv(save_path)

 	def _exists(self) -> bool:
        path = self._get_load_path()
        return path.is_file()

    def _describe(self):
        return dict(version=self._version, param1=self._param1, param2=self._param2)
```
