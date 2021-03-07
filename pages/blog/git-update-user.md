---
templateKey: 'blog-post'
title: Update Git User
date: 2019-01-21
status: published
description:
tags:
    - git

---

This morning I log into my VCS and check activity on my projects to find that **someone else** has been _very_ active on my projects fo the last few weeks. I quicklyhover over the missing avatar to find that **It's Me**.  What's wrong here, why do I look like two different people throughout the day!  upon further investigation I see the issue.  while setting up a new terminal environment I mistyped my email address by **one character**.  After much searching and a few failed attempts I was able to fix it by following this article https://help.github.com/articles/changing-author-info/.


## Bare Clone

Clone the repo, note it must be a `--bare` clone.

``` bash
git clone --bare https://github.com/user/repo.git
cd repo.git
```

## git-author-rewrite

Curl down the `git-author-rewrite` script and edit the following variables `OLD_EMAIL` `CORECT_NAME` `CORRECT_EMAIL`

``` bash
curl https://gist.githubusercontent.com/octocat/0831f3fbd83ac4d46451/raw/c197afe3e9ea2e4218f9fccbc0f36d2b8fd3c1e3/git-author-rewrite.sh > git-author-rewrite.sh
```

Run the script, and push the updates.


``` bash
bash git-author-rewrite.sh
git push --force --tags origin 'refs/heads/**'
```

## Cleanup

Delete the `--bare` repo from your local machine.
```bash
cd ..
rm -rf repo.git
```

I hope this helps someone, or future me who needs to fix their information in git.
