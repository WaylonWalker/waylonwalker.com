---
title: Stop Making TUIs
date: 2026-08-21T17:15:51Z
published: true
draft: false
tags:
  - cli
  - tui
  - ai
template: link
image: ""
url: "https://simonwillison.net/2026/Aug/21/stop-making-tuis/"
authors:
  - waylon
  - id: gpt-6-luna
    role: copy editor
    details: "Corrected spelling and grammar with GPT-6 Luna."
---

Hard to argue this so hard here.  For me it's convenience.  I work from a terminal.  Most things that are real work get done there, so this provides a convenient proximity to real work.  If it's a developer tool for me to use alongside development work I prefer a tui if it can be done in a text interface.

CLIs are different.  CLIs provide a great interface into automation, scripting, agent use, interop from two things no one else uses together.

Alternatively to the argument for agents making ==real== user interfaces _easy_ I'm going to argue if that's the case you should have your backend logic hooked into all the interfaces a user could want, CLI, TUI, HTML, and REST/HTTP API.

I honestly feel like the training data for a good tui just isn't there and agents default to making bad TUIs.