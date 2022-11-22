---
date: 2022-11-22 16:16:38
templateKey: til
title: ssh key permissions
status: 'published'
tags:
  - linux

---

I just shared some ssh keys with myself and ran into this error telling me that
I did not set the correct permissions on my key.

``` bash
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0750 for '/home/waylon/.ssh/id_*******' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "/home/waylon/.ssh/id_*******": bad Permissions
repo: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

I changed them with the following commands.

``` bash
chmod 644 ~/.ssh/id_*******.pub
chmod 600 ~/.ssh/id_*******
```
