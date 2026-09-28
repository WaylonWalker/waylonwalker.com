---
date: 2026-04-18 10:36:00
templateKey: til
title: stow local ignore
published: true
tags:
  - linux

---

Stow comes with a local and global ignore list that you can use to ignore
certain files or directories.


> If you put Perl regular expressions, one per line, in a .stow-local-ignore
> file within any top level package directory, in which case any file or
> directory within that package matching any of these regular expressions will
> be ignored. In the absence of this package-specific ignore list, Stow will
> instead use the contents of ~/.stow-global-ignore, if it exists. If neither
> the package-local or global ignore list exist, Stow will use its own built-in
> default ignore list, which serves as a useful example of the format of these
> ignore list files:

Example given from the docs

``` text
RCS
.+,v

CVS
\.\#.+       # CVS conflict files / emacs lock files
\.cvsignore

\.svn
_darcs
\.hg

\.git
\.gitignore
\.gitmodules

.+~          # emacs backup files
\#.*\#       # emacs autosave files

^/README.*
^/LICENSE.*
^/COPYING
```


## Reference

https://www.gnu.org/software/stow/manual/html_node/Types-And-Syntax-Of-Ignore-Lists.html
