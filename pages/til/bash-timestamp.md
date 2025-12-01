---
date: 2025-08-22 15:35:36
templateKey: til
title: bash timestamp
published: true
tags:
  - linux

---

Today I needed to make a backup of some config.  I wanted to add a timestamp so
that I knew when the backup was made.  This would make unique backups easy, and
I could tell when they were made.

``` bash
cp configfile configfile.backup.$(date %s)
```

If you want to decrypt the timestamp into something more human readable.  You
can list backup files, strip out the timestamp, and then convert it to a human
readable date.

``` bash
/bin/ls | grep backup | sed 's/configfile.backup.//' | xargs -I {} date -d @{}
```

or just throw it to the date command by hand.

``` bash
date -d @1755895402
```

