---
date: 2023-01-19 07:46:31
templateKey: til
title: Arch Linux Randomly Rejecting Passwords
published: true
tags:
  - linux
---

> Fix Arch Linux randomly rejecting passwords with one command. Try
> 'faillock --user $USER' to reset login counter and regain access. Quick
> solution for a smooth computing"

![an intertwined mess of wires](https://stable-diffusion.waylonwalker.com/000255.3612717469.webp)

If you're an Arch Linux user, you may have experienced a frustrating issue
where your password is randomly not being accepted by the system. This can be a
major inconvenience and can cause a lot of frustration, especially if it
happens frequently.

The good news is that there is a simple fix for this issue. The following bash
code can be used to fix the problem:

`bash faillock --user $USER`

This command is used to reset the failed login count for the current user. By
running this command, you will be able to reset the system's login counter and
regain access to your account.

It's important to note that this command should only be used as a temporary
solution. If you find yourself frequently having to run this command, it's
likely that there is a deeper issue with your system that needs to be
addressed.

In any case, if you're experiencing problems with your Arch Linux system not
accepting your password, give the above command a try and see if it resolves
the issue for you.
