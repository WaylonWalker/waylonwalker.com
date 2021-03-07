---
templateKey: 'blog-post'
title: My favorite pandas pattern
date: 2018-03-01
status: Draft
description: none

---

# My favorite pandas pattern


I work with a lot of transactional timeseries data that includes categories.  I often want to create timeseries plots with each category as its own line.  This is the method that I use almost data to achieve this result.  Typically the data that am working with changes very slowly and trends happen over years not days or weeks.  Plotting daily/weekly data tends to be noisy and hides the trend.  I use this pattern because it works well with my data and is easy to explain to my stakeholders.



```python
import pandas as pd
import numpy as np
% matplotlib inline
```

## Lets Fake some data


Here I am trying to simulate a subset of a large transactional data set. This could be something like sales data, production data, hourly billing, anything that has a date, category, and value.  Since we generated this data we know that it is clean.  I am still going to assume that it contains some nulls, and an irregular date range.


```python
n = 365*5
cols = {'level_0': 'date',
        'level_1': 'item',
        0: 'qty', }
data = (pd.DataFrame(np.random.randint(0, 10, size=(n, 4)),
                     columns=['paper', 'pencils', 'note cards', 'markers'],
                     index=pd.date_range('1/1/2017', periods=n, freq='d'),
                     )
        .stack()
        .to_frame()
        .reset_index()
        .rename(columns=cols))
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>item</th>
      <th>qty</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-01-01</td>
      <td>paper</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-01-01</td>
      <td>pencils</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-01-01</td>
      <td>note cards</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-01-01</td>
      <td>markers</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-01-02</td>
      <td>paper</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



## The pattern

Here I am going to take my groupby date and item, this will take care of duplicate entries with the same time stamp.  Select the value I want to sum on. unstack the items index into columns.  Resample the data by month.  I could easily use any of the [available rules](https://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases). Fill any missing months with 0, since there wasnt a transaction during that month. Apply a rolling window to get the annual sum.  I find that this helps to ground values in values that my stakeholders are used to seeing on a regular basis and reduces the need for them to recalculate in their head.  Then I am going to drop the nulls created by the rolling window for the first 11 rows.


```python
plot_data = (data
             .groupby(['date', 'item'])
             .sum()
             ['qty']
             .unstack()
             .resample('m')
             .sum()
             .fillna(0)
             .rolling(12)
             .sum()
             .dropna()
             )
plot_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>markers</th>
      <th>note cards</th>
      <th>paper</th>
      <th>pencils</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-12-31</th>
      <td>1543.0</td>
      <td>1739.0</td>
      <td>1613.0</td>
      <td>1657.0</td>
    </tr>
    <tr>
      <th>2018-01-31</th>
      <td>1572.0</td>
      <td>1744.0</td>
      <td>1635.0</td>
      <td>1635.0</td>
    </tr>
    <tr>
      <th>2018-02-28</th>
      <td>1563.0</td>
      <td>1717.0</td>
      <td>1645.0</td>
      <td>1645.0</td>
    </tr>
    <tr>
      <th>2018-03-31</th>
      <td>1596.0</td>
      <td>1703.0</td>
      <td>1629.0</td>
      <td>1600.0</td>
    </tr>
    <tr>
      <th>2018-04-30</th>
      <td>1557.0</td>
      <td>1693.0</td>
      <td>1648.0</td>
      <td>1581.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
plot_data.plot(title='Rolling annual sum of Categorical Random Data');
```

## For the Visual Learners

### Groupby


```python
plot_data = (data
             .groupby(['date', 'item'])
             .sum()
             )
plot_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>qty</th>
    </tr>
    <tr>
      <th>date</th>
      <th>item</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">2017-01-01</th>
      <th>markers</th>
      <td>9</td>
    </tr>
    <tr>
      <th>note cards</th>
      <td>5</td>
    </tr>
    <tr>
      <th>paper</th>
      <td>1</td>
    </tr>
    <tr>
      <th>pencils</th>
      <td>4</td>
    </tr>
    <tr>
      <th>2017-01-02</th>
      <th>markers</th>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### Select Values

In this case I chose to do this to avoid working with a multiple levels in the columns that would be created in the unstack() step.


```python
plot_data = plot_data['qty']

plot_data.head()
```




    date        item
    2017-01-01  markers       9
                note cards    5
                paper         1
                pencils       4
    2017-01-02  markers       4
    Name: qty, dtype: int32



### unstack

transform the last column in the index ('item') into rows.


```python
plot_data = plot_data.unstack()

plot_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>markers</th>
      <th>note cards</th>
      <th>paper</th>
      <th>pencils</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-01</th>
      <td>9</td>
      <td>5</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2017-01-02</th>
      <td>4</td>
      <td>2</td>
      <td>3</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2017-01-03</th>
      <td>9</td>
      <td>5</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2017-01-04</th>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2017-01-05</th>
      <td>0</td>
      <td>1</td>
      <td>6</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



### resample

This step is important for irregular data in order to get the data into regular intervals.


```python
plot_data = plot_data.resample('m').sum()

plot_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>markers</th>
      <th>note cards</th>
      <th>paper</th>
      <th>pencils</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-31</th>
      <td>145</td>
      <td>128</td>
      <td>117</td>
      <td>146</td>
    </tr>
    <tr>
      <th>2017-02-28</th>
      <td>136</td>
      <td>140</td>
      <td>133</td>
      <td>135</td>
    </tr>
    <tr>
      <th>2017-03-31</th>
      <td>112</td>
      <td>145</td>
      <td>125</td>
      <td>163</td>
    </tr>
    <tr>
      <th>2017-04-30</th>
      <td>143</td>
      <td>148</td>
      <td>112</td>
      <td>147</td>
    </tr>
    <tr>
      <th>2017-05-31</th>
      <td>86</td>
      <td>134</td>
      <td>139</td>
      <td>141</td>
    </tr>
  </tbody>
</table>
</div>



### rolling

I like to use rolling because it get the data into annual numbers, and reduces noise.  I have found that most of my datasets have patterns and trends that are greater than 1y.  This  is just due to the industry that I am in.  Play with the resample and rolling rules to fit the need of your own data.


```python
plot_data = plot_data.rolling(12).sum()

plot_data.head(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>markers</th>
      <th>note cards</th>
      <th>paper</th>
      <th>pencils</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-31</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-02-28</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-03-31</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-04-30</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-05-31</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-06-30</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-07-31</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-31</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-09-30</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-10-31</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-11-30</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-12-31</th>
      <td>1543.0</td>
      <td>1739.0</td>
      <td>1613.0</td>
      <td>1657.0</td>
    </tr>
    <tr>
      <th>2018-01-31</th>
      <td>1572.0</td>
      <td>1744.0</td>
      <td>1635.0</td>
      <td>1635.0</td>
    </tr>
    <tr>
      <th>2018-02-28</th>
      <td>1563.0</td>
      <td>1717.0</td>
      <td>1645.0</td>
      <td>1645.0</td>
    </tr>
    <tr>
      <th>2018-03-31</th>
      <td>1596.0</td>
      <td>1703.0</td>
      <td>1629.0</td>
      <td>1600.0</td>
    </tr>
    <tr>
      <th>2018-04-30</th>
      <td>1557.0</td>
      <td>1693.0</td>
      <td>1648.0</td>
      <td>1581.0</td>
    </tr>
    <tr>
      <th>2018-05-31</th>
      <td>1624.0</td>
      <td>1674.0</td>
      <td>1632.0</td>
      <td>1592.0</td>
    </tr>
    <tr>
      <th>2018-06-30</th>
      <td>1582.0</td>
      <td>1645.0</td>
      <td>1657.0</td>
      <td>1593.0</td>
    </tr>
    <tr>
      <th>2018-07-31</th>
      <td>1662.0</td>
      <td>1654.0</td>
      <td>1680.0</td>
      <td>1613.0</td>
    </tr>
    <tr>
      <th>2018-08-31</th>
      <td>1654.0</td>
      <td>1617.0</td>
      <td>1650.0</td>
      <td>1616.0</td>
    </tr>
  </tbody>
</table>
</div>



### dropna

get rid of the first 11 null rows


```python
plot_data = plot_data.dropna()

plot_data.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>markers</th>
      <th>note cards</th>
      <th>paper</th>
      <th>pencils</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-12-31</th>
      <td>1543.0</td>
      <td>1739.0</td>
      <td>1613.0</td>
      <td>1657.0</td>
    </tr>
    <tr>
      <th>2018-01-31</th>
      <td>1572.0</td>
      <td>1744.0</td>
      <td>1635.0</td>
      <td>1635.0</td>
    </tr>
    <tr>
      <th>2018-02-28</th>
      <td>1563.0</td>
      <td>1717.0</td>
      <td>1645.0</td>
      <td>1645.0</td>
    </tr>
    <tr>
      <th>2018-03-31</th>
      <td>1596.0</td>
      <td>1703.0</td>
      <td>1629.0</td>
      <td>1600.0</td>
    </tr>
    <tr>
      <th>2018-04-30</th>
      <td>1557.0</td>
      <td>1693.0</td>
      <td>1648.0</td>
      <td>1581.0</td>
    </tr>
    <tr>
      <th>2018-05-31</th>
      <td>1624.0</td>
      <td>1674.0</td>
      <td>1632.0</td>
      <td>1592.0</td>
    </tr>
    <tr>
      <th>2018-06-30</th>
      <td>1582.0</td>
      <td>1645.0</td>
      <td>1657.0</td>
      <td>1593.0</td>
    </tr>
    <tr>
      <th>2018-07-31</th>
      <td>1662.0</td>
      <td>1654.0</td>
      <td>1680.0</td>
      <td>1613.0</td>
    </tr>
    <tr>
      <th>2018-08-31</th>
      <td>1654.0</td>
      <td>1617.0</td>
      <td>1650.0</td>
      <td>1616.0</td>
    </tr>
    <tr>
      <th>2018-09-30</th>
      <td>1669.0</td>
      <td>1648.0</td>
      <td>1638.0</td>
      <td>1634.0</td>
    </tr>
  </tbody>
</table>
</div>
