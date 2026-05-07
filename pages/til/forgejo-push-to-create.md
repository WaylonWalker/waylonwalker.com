---
date: 2026-05-06 21:58:55
templateKey: til
title: forgejo push to create
published: true
tags:
  - git

---

I just learned that forgejo has a push to create repo feature and it is a
gamechanger.  Upon first try it didn't work, with just a couple of environment
variables I was up and running ith push to create.

``` bash
notify.wayl.one on  main is 📦 v0.1.62  v3.14.4  NO PYTHON VENV SET  USING SYSTEM NVIM
❯ git remote add origin https://git.waylonwalker.com/waylon/notify.wayl.one
notify.wayl.one on  main is 📦 v0.1.62  v3.14.4  NO PYTHON VENV SET  USING SYSTEM NVIM
❯ git push
remote: Push to create is not enabled for users.
fatal: unable to access 'https://git.waylonwalker.com/waylon/notify.wayl.one/': The requested URL returned error: 403
```

So I added the following environment variables.

``` diff
Author: Waylon S. Walker <waylon@waylonwalker.com>
Date:   Wed May 6 21:56:53 2026 -0500

    enable push to create

diff --git a/k8s/forgejo/deployment.yaml b/k8s/forgejo/deployment.yaml
index d77daab..9346763 100644
--- a/k8s/forgejo/deployment.yaml
+++ b/k8s/forgejo/deployment.yaml
@@ -91,6 +91,10 @@ spec:
               value: "0.0.0.0"
             - name: FORGEJO__server__HTTP_PORT
               value: "3000"
+            - name: FORGEJO__repository__ENABLE_PUSH_CREATE_USER
+              value: "true"
+            - name: FORGEJO__repository__ENABLE_PUSH_CREATE_ORG
+              value: "true"
             - name: FORGEJO__database__DB_TYPE
               value: postgres
             - name: FORGEJO__database__HOST
```

https://github.com/WaylonWalker/homelab-argo/commit/b2e953bc12

Tried again, and it just worked!

``` bash
notify.wayl.one on  main is 📦 v0.1.62  v3.14.4  NO PYTHON VENV SET  USING SYSTEM NVIM
❯ git push
Enumerating objects: 171, done.
Counting objects: 100% (171/171), done.
Delta compression using up to 12 threads
Compressing objects: 100% (169/169), done.
Writing objects: 100% (171/171), 176.22 KiB | 16.02 MiB/s, done.
Total 171 (delta 99), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (99/99), done.
To https://git.waylonwalker.com/waylon/notify.wayl.one
 * [new branch]      main -> main
 ```
