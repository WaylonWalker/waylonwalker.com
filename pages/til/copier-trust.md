---
date: 2024-04-15 20:41:06
templateKey: til
title: copier trust
published: true
tags:
  - python

---

I recently had to update my copier-gallery command to trust my own templates
because some of them have shell scripts that run afterwards.  Be warned that
this could be a dangerous feature to run on random templates you get off the
internet, but these are all mine, so if I wreck it its my own fault.

``` bash
copier copy --trust <template> <destination>
```

All the the copier copy api can be found with help.

``` bash
❯ copier copy --help
copier copy 8.3.0

Copy from a template source to a destination.

Usage:
    copier copy [SWITCHES] template_src destination_path

Hidden-switches:
    -h, --help                         Prints this help message and quits
    --help-all                         Prints help messages of all sub-commands and quits
    -v, --version                      Prints the program's version and quits

Switches:
    -C, --no-cleanup                   On error, do not delete destination if it was
                                       created by Copier.
    --UNSAFE, --trust                  Allow templates with unsafe features (Jinja
                                       extensions, migrations, tasks)
    -a, --answers-file VALUE:str       Update using this path (relative to
                                       `destination_path`) to find the answers file
    -d, --data VARIABLE=VALUE:str      Make VARIABLE available as VALUE when rendering the
                                       template; may be given multiple times
    -f, --force                        Same as `--defaults --overwrite`.
    -g, --prereleases                  Use prereleases to compare template VCS tags.
    -l, --defaults                     Use default answers to questions, which might be
                                       null if not specified.
    -n, --pretend                      Run but do not make any changes
    -q, --quiet                        Suppress status output
    -r, --vcs-ref VALUE:str            Git reference to checkout in `template_src`. If you
                                       do not specify it, it will try to checkout the
                                       latest git tag, as sorted using the PEP 440
                                       algorithm. If you want to checkout always the
                                       latest version, use `--vcs-ref=HEAD`.
    -s, --skip VALUE:str               Skip specified files if they exist already; may be
                                       given multiple times
    -w, --overwrite                    Overwrite files that already exist, without asking.
    -x, --exclude VALUE:str            A name or shell-style pattern matching files or
                                       folders that must not be copied; may be given
                                       multiple times
```
