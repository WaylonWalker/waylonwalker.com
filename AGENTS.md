# AGENTS.md - Repository Guidelines for WaylonWalker.com

## Build/Lint/Test Commands

Static site built with `markata-go`, not the older Python Markata build.
Use `just` for task management.  For implementation reference, see
`~/git/markata-go`.

```bash
just build        # Build site with markata-go
just serve        # Serve built output on localhost:8000
just tailwind     # Watch/compile Tailwind CSS
just clean        # Clean markata-go build state
just setup        # Initial setup (clone assets, create venv)
just compile      # Update requirements.txt from requirements.in
```

**No test suite** - verify changes by building and serving locally.

## Code Style Guidelines

### Python (Python 3.12+)
- Use `uv` for package management and virtual environments
- Type hints required: `from typing import TYPE_CHECKING, List, Optional`
- Pydantic models for configuration/data validation
- Plugins use Markata hookspec: `@hook_impl` decorator
- Scripts use `#!/usr/bin/env -S uv run --quiet --script` header
- Use f-strings, proper exception handling, `set -euxo pipefail` in bash

### Project Structure
- `plugins/`: Markata extensions (Python)
- `scripts/`: Utility scripts (Typer CLI)
- `templates/`: Jinja2 HTML templates
- `pages/`: Markdown content (kebab-case)
- `tailwind/`: CSS source files
- `static/`: Built assets

### Naming Conventions
- Functions: snake_case
- Classes: PascalCase
- Files: snake_case (Python), kebab-case (content)

### Frontend
- Tailwind CSS v4+ with pnpm
- Jinja2 templating
- Markdown with frontmatter

## Content Style Guidelines

### Tone of Voice
**Casually self-deprecating with technical credibility**

- **Conversational** - Write like you're talking to someone at a conference after-party, not a LinkedIn profile
- **Self-aware humor** - Don't be afraid to poke fun at yourself and your projects ("under-funded, over-dreamed, barely documented")
- **Authentic** - Include real personal details and hobbies (Minecraft, skating, Big Bang Theory)
- **Competent but humble** - Show technical expertise without taking yourself too seriously
- **DIY ethic** - Emphasize building/maintaining things yourself (Kubernetes cluster in the basement)

### Content Guidelines
- Use first person ("I", "me", "my")
- Keep sentences punchy and direct
- Headers should be concise (2-4 words)
- Technical terms are fine, but explain the "why" behind choices
- It's okay to mention frustrations with mainstream tools (Node modules, bloated pages)
- Personal anecdotes add authenticity
- No em-dashes (use periods or commas instead)
- No emoji
- 80 character hard wrap
- Double space between sentences

### Content Type Variations

**Blog Posts (Personal/Meta)** - Full conversational tone
- Examples: `blogging-for-me.md`, `about.md`
- Use complete tone guidelines above
- Share opinions, experiences, frustrations openly

**Hot Tips / TILs** - Short, practical, but not robotic
- Examples: `hot_tips/*.md`
- Keep code examples front and center
- Add brief context or "why this matters" - even just one sentence
- It's okay to say "I use this when..." or "This saved me from..."
- Avoid pure documentation style - give it a heartbeat

**Glossary Entries** - Formality acceptable
- Examples: `glossary/*.md`
- Stiff, definitional tone is intentional
- Focus on clarity and accuracy over personality

**Daily Notes** - Casual and quick
- Examples: `daily/*.md`
- Stream of consciousness is fine
- Link heavily to other content
- Don't overthink it
