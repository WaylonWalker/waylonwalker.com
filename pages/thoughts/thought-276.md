---
title: '💭 Safer Bash Shebang Recipes - Just Programmer''s Manual'
date: 2024-05-14T22:29:49
templateKey: link
link: https://just.systems/man/en/safer-bash-shebang-recipes.html?highlight=pipefail#safer-bash-shebang-recipes
tags:
  - just
  - justfile
published: true

---

> When using justfiles each line is ran separately from the last, unless you specify the file to be ran by something other than just such as bash.  If you want variables to persist you need to set a shebang.

Also if you are using your script i a way that you want it to exit when it fails you need to set -e and  -o pipefail.  This is critical if you are thinking about using just for production scripts like ci/cd.  I've hit too bugs where ci passes, but no artifacts were created issues for this exact reason.

``` bash
foo:
  #!/usr/bin/env bash
  set -euxo pipefail
  hello='Yo'
  echo "$hello from Bash!"
```

[Original thought](https://just.systems/man/en/safer-bash-shebang-recipes.html?highlight=pipefail#safer-bash-shebang-recipes)
