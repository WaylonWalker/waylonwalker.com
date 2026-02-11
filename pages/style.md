---
date: 2026-02-11T14:00:00
templateKey: blog-post
title: /style
published: false
tags:
  - slashpages
  - meta
---

> drafted by kimi

# /style

How I write and build this site.  A personal style guide.

## Tone of Voice

**Casually self-deprecating with technical credibility.**

I write like I'm talking to someone at a conference after-party, not a LinkedIn profile.  It's okay to poke fun at myself and my projects.  "Under-funded, over-dreamed, barely documented" is a feature, not a bug.

**Principles:**

- Use first person ("I", "me", "my")
- Keep sentences punchy and direct
- Include real personal details and hobbies
- Show technical expertise without taking myself too seriously
- It's okay to mention frustrations with mainstream tools

## Writing Rules

**Formatting:**

- No em-dashes.  Use periods or commas instead
- No emoji
- 80 character hard wrap
- Double space between sentences
- Headers should be concise (2-4 words)

**Structure:**

- Put code examples front and center
- Add brief context or "why this matters" even if just one sentence
- It's okay to say "I use this when..." or "This saved me from..."
- Personal anecdotes add authenticity
- Technical terms are fine, but explain the "why" behind choices

**Content Types:**

| Type | Tone |
|------|------|
| Blog posts | Full conversational tone, share opinions openly |
| Hot tips / TILs | Short, practical, but not robotic |
| Glossary entries | Stiff, definitional tone is intentional |
| Daily notes | Casual and quick, stream of consciousness is fine |

## Code Style

**Python:**

- Use `uv` for package management
- Type hints required: `from typing import TYPE_CHECKING, List, Optional`
- Pydantic models for configuration
- f-strings over concatenation
- Proper exception handling

**Bash:**

- `set -euxo pipefail` in scripts
- Use `just` for task management

**Naming:**

- Functions: snake_case
- Classes: PascalCase
- Python files: snake_case
- Content files: kebab-case

## Site Architecture

**Stack:**

- Markata (custom Python static site generator)
- Tailwind CSS v4+ with pnpm
- Jinja2 templating
- Markdown with YAML frontmatter
- Kubernetes hosting (basement cluster)

**Directories:**

```
plugins/     Markata extensions
scripts/     Utility scripts (Typer CLI)
templates/   Jinja2 HTML templates
pages/       Markdown content
tailwind/    CSS source files
static/      Built assets
```

## Content Philosophy

**DIY Ethic:**

I emphasize building and maintaining things myself.  This site runs on a Kubernetes cluster in my basement because "I love DevOps" like maintaining your own bare-metal cluster just to host a static site.

**Authenticity:**

I create this blog with one person in mind: me.  If it helps others, great.  But I'm writing to document what I learn and think, not to build an audience or optimize for engagement.

**Learn in Public:**

Share failures, unfinished projects, and half-baked ideas.  The TIL format works because it captures learning in the moment, not after I've mastered something.

## What I Avoid

- **"Just"** - The word skips invisible complexity
- **Pretending to know everything** - I'll say when I'm confused
- **Overly complex solutions** - Prefer systems I can understand and fix
- **Performance for likes** - Not optimizing for engagement metrics

## Inspiration

This style guide draws from:

- [slashpages.net /style](https://indieweb.org/style-guide)
- [Rubenerd style guide](https://rubenerd.com/the-rubenerd-style-guide/)
- [Robb Knight's design style](https://rknight.me/about/design/)
- Years of reading indie web blogs and knowing what I like

---

*This is a living document.  I break these rules when it feels right.*
