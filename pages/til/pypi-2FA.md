---
date: 2022-08-29 07:51:54
templateKey: til
title: I turned on 2FA for all of my pypi packages
status: published
tags:
  - python

---

I got all the pypi packages that I own behind 2 factor authentication. 💪

Recently this really made it's rounds in the python news since pypi was
requiring critical package maintainers to have 2FA on and even offering them
hardware tokens to help them turn this on.

I feel like this caused a bit of confusion as turning on 2FA does not mean that
you need to do anything different to deploy a package, and it **DOES NOT**
require a hardware token.  You can continue using your favorite 2FA app.

You might wonder what this means for my projects. It means that to edit any
_sensitive content_ such as pull a new api token, add/remove maintainers, or
deleting a release I need to use a TOPT (time based one time password)
application such as Google Authenticator, Microsoft Authenticator, Authy, or
FreeOTP.

This has very little change to my overall workflow as my CI system still
automatically deploys for me with the same api token as before.

This is one small thing that maintainers can do to prevent supply chain attacks
on their projects that they put so much work into.

## Login

When I log in I now get this extra screen asking for an auth token.

![pypi-2fa-code](https://screenshots.waylonwalker.com/pypi-2fa-code.webp)

## My packages

Once I turned on 2FA for my account I could then turn on 2FA requirement for
each project.  I am not sure how much safety there is in pypi, it might require
all maintainers to have it turned on before it allows packages to have it
turned on.

![my-pypi-packages-aug-2022](https://screenshots.waylonwalker.com/my-pypi-packages-aug-2022.webp)

Once turned on it requires anyone who maintains the project to have 2FA on to
be able to edit any sensitive content.
