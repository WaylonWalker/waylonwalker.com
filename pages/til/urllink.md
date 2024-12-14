---
date: 2024-12-14 11:11:52
templateKey: til
title: urllink
published: true
tags:
  - bash

---

Today I discovered the `Urllink` function in bash from the ujust tool from
[ublue.it](https://ublue.it).  Seems like a cool trick, but might not work
everywhere.

``` bash
########
### Special text formating
########
## Function to generate a clickable link, you can call this using
# url=$(Urllink "https://ublue.it" "Visit the ublue website")
# echo "${url}"
function Urllink (){
    URL=$1
    TEXT=$2

    # Generate a clickable hyperlink
    printf "\e]8;;%s\e\\%s\e]8;;\e\\" "$URL" "$TEXT${n}"
}
```j
