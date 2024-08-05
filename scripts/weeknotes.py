from datetime import date
from markata import Markata
from pathlib import Path

weeknote_id = len(list(Path("pages/weeknotes/").glob("*.md")))

m = Markata()
thoughts = "\n".join(
    m.map(
        'f"- {post.date} {post.title} [[{post.slug}]]"',
        filter="date>today-timedelta(days=7) and date<today and published and not templateKey=='weeknote' and templateKey=='thoughts'",
        sort="date",
    )
)

posts = "\n".join(
    m.map(
        'f"- {post.date} {post.title} [[{post.slug}]]"',
        filter="date>today-timedelta(days=7) and date<today and published and not templateKey=='weeknote' and not templateKey=='thoughts'",
        sort="date",
    )
)

post = f"""---
title: "Weeknote {weeknote_id}"
templateKey: "weeknote"
date: "{date}"
slug: "weeknote-{weeknote_id}"
tags:
    - weeknote
---

## Posts

{posts}

## Thoughts

[[ thoughts ]] are quick thoughts I leave that are generally tied to a link.

{thoughts}

"""

with open(f"pages/weeknotes/weeknote-{weeknote_id}.md", "w") as f:
    f.write(post)
