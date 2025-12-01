---
date: 2025-02-10 13:35:24
templateKey: til
title: configure timezone
published: true
tags:
  - linux

---


Today I ran into this interactive prompt on ubuntu while installing node and
npm, and I do not want to manually configure this interactively every time I
run an install, moreso in docker I do not have the interactive terminal to do
so.

``` bash
Configuring tzdata
------------------

Please select the geographic area in which you live. Subsequent configuration questions will narrow this down by presenting a list of cities, representing the time zones in which they are located.

  1. Africa  2. America  3. Antarctica  4. Arctic  5. Asia  6. Atlantic  7. Australia  8. Europe  9. Indian  10. Pacific  11. Etc  12. Legacy
Geographic area:
```

## Why tzdata

Checking aptitude why tzdata it shows that the chain goes back through npm.

``` bash
root@47685221fb82:/# aptitude why tzdata
i   npm        Depends  node-gyp
i A node-gyp   Depends  gyp (>= 0.1+20200513gitcaa6002)
i A gyp        Depends  python3:any
i A python3    Provides python3:any
i A python3    Depends  python3.12 (>= 3.12.3-0~)
i A python3.12 Depends  tzdata
```

## The solution, configure tzdata

``` bash
export TZ="America/Chicago"
export DEBIAN_FRONTEND=noninteractive
apt update
apt install tzdata -y
ln -fs /usr/share/zoneinfo/$TZ /etc/localtime
dpkg-reconfigure -f noninteractive tzdata
```

!!! TIP DEBIAN_FRONTEND=noninteractive
    This is required, because apt installing tzdata will trigger the
    interactive prompt.  You will manually configure it in the next two steps.
