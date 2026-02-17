---
title: '💭 Some Git poll results'
date: 2024-03-29T02:04:41
templateKey: link
link: https://jvns.ca/blog/2024/03/28/git-poll-results/
tags:
  - git
published: true

---

> great poll of git questions

> poll: did you know that in a git merge conflict, the order of the code is different when you do a merge/rebase?
> 
> merge:
> 
> \<\<\<\<\<\<\< HEAD
> YOUR CODE
> =======
> OTHER BRANCH'S CODE
> >>>>>>> c694cf8aabe
> 
> rebase:
> 
> <<<<<<< HEAD
> OTHER BRANCH'S CODE
> =======
> YOUR CODE
> >>>>>>> d945752 (your commit message)


This one explains a lot.  I _think_ I knew this, I might have seen it somewhere, but I have definitely noticed it go both ways and confuse the crap out of me.  Feels very similar to how `--ours` and `--theirs` flip flops.

[Original thought](https://jvns.ca/blog/2024/03/28/git-poll-results/)
