---
date: 2022-01-22 04:49:12.551676
templateKey: til
title: Copier Tasks | Python templating post run task
tags:
  - python
  - cli
  - linux

---

``` yaml
num: 128
_answers_file: .gratitude-copier-answers.yml
_tasks:
  - "update-gratitude"
```

``` bash
current=`awk '{print $2}' ~/.copier-templates/gratitude/copier.yml | head -n 1`
new=`expr $current + 1`
echo $current
echo $new
sed -i "s/$current/$new/g" ~/.copier-templates/gratitude/copier.yml
```
