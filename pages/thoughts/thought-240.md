---
title: '💭 Use an llm to automagically generate meaningful git commit mes...'
date: 2024-04-11T13:35:50
templateKey: link
link: https://harper.blog/2024/03/11/use-an-llm-to-automagically-generate-meaningful-git-commit-messages/
tags:
  - llm
  - ai
published: true

---

> This is pretty sick, I wanted this early on when I was making lockhart.  I wanted to do the git hook thing but could not figure it out and did not know that `prepare-commit-msg` was a hook that I could use.

> Git Hooked
> Then I remembered! Git hooks! Lol. Why would I have that in my brain - who knows!
> 
> I asked claude again, and they whipped up a simple script that would act as a hook that triggers with the prepare-commit-msg event.
>
> This is awesome, cuz if you want to add a git message, you can skip the hook. But if you are lazy, you exclude the message and it will call the LLM.


Simon Willison's llm cli comes in clutch here, it has such a good intereface to allow a prompt to be piped in, but the system prompt be set by -s.

``` bash
gpt = "!f() { git diff $1 | llm -s \"$(cat ~/.config/prompts/commit-system-prompt.txt)\" }; f"
```


> I love hacking on projects, but often I am super bad at making commits that make sense.

I completely relate to this statement, and this is why I am trying it.


[Original thought](https://harper.blog/2024/03/11/use-an-llm-to-automagically-generate-meaningful-git-commit-messages/)
