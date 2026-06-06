---
date: 2026-05-29 17:41:35
templateKey: ping
published: true
tags:
- ping

---
Not sure how this matters to anyone else, but I'm sitting in the car and letting the thoughts flow.

I'm having really interesting conversations with ai recently.  Like things I never thought I would care this deeply about.  In part because it feels like the vulns are coming faster and harder, and in part because it is really enabling me to invest some time into the development that I would not otherwise have.  I'm thinking about least privilege, reducing dependencies in containers, limiting pod access to the Internet and other pods.  Reducing the blast radius.

Now I've always been hesitant to bring in new dependencies.  I've always tried to strip  to the lowest possible dependency set n my containers, but I would also re-use the main server container to run cron job workflows.  I wasn't giving much thought about what services they could access, or their internet access