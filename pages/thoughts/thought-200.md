---
title: '💭 The One Eyed Fighting Kirby'
date: 2024-01-26T17:21:06
template: link
link: https://www.youtube.com/watch?v=9_Ekt1PZBzQ&t=351s
tags:
  - vim
  - regex
  - thoughts
  - thought
  - link
published: true

---

![[https://www.youtube.com/watch?v=9_Ekt1PZBzQ&t=351s]]

 I've heard prime say just give it the one eyed fighting kirby so many times, and execute it few times, and there is no way to find it online, so this will be the link that I will come to, when I need to remember what @theprimeagen means when he says Give it the one eyed fighting kirby.

``` vim
:s/\(.*\);/console.log(\1)
```

## So what is this?

This is a vim substitute comand to replace text in the buffer.  the one eyed fighting kirby is a regex capture group to capture everything between matches, and assign it a value to place back in after the match.

substitute in a nutshell, `:s/<what you want to replace>/<what you want to replace with>`


## More examples

Here is a contrived example of text.

``` text
here there
from here go there
here = some_fuction(there)
```

Now for some reason I want to switch all of the words here and there.  I can do that with three capture groups, \1 is here, \2 is everything between, \3 is there.

``` vim
:%s/\(here\)\(.*\)\(there\)/\3\2\1
```

> Just give it the one eyed fighting kirby
> 
> ~Prime

## still struggling

I thought this explaination from phind was good and more verbose than mine.

---

describe this vim substitute regex

:%s/\(here\)\(.*\)\(there\)/\3\2\1
ANSWER | PHIND V9 MODEL
The given Vim substitute regex :%s/\(here\)\(.*\)\(there\)/\3\2\1 performs the following operation:

%s initiates the substitute command. The percent sign % indicates that the operation should be performed across the entire file, not just the current line 2.
\(here\) is a capturing group that matches the word "here". The parentheses \( and \) are used to define a group, and the content inside them is what the group will match 3.
\(.*\) is another capturing group that matches any sequence of characters. The .* inside the group is a wildcard that matches any character (except a newline), and the * quantifier means "zero or more of the preceding element". So, this group will match any sequence of characters 2.
\(there\) is yet another capturing group that matches the word "there". This group will match the word "there" that appears after the word "here" and any sequence of characters 3.
/\3\2\1 is the replacement part of the command. Here, \3, \2, and \1 are backreferences to the matched groups. They correspond to the words "there", any sequence of characters, and "here", in that order. So, this command replaces the matched pattern with the word "there", followed by any sequence of characters, and ending with the word "here" 4.
So, in summary, this command searches for the pattern "here", followed by any sequence of characters, and ending with "there", and replaces it with the same pattern but reversed ("there", followed by the original sequence of characters, and ending with "here").

I used this techniq on [[ refactoring-into-wikilinks ]].

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
