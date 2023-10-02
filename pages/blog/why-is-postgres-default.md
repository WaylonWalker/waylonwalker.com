---
date: 2023-09-30 21:26:36
templateKey: blog-post
title: why-is-postgres-default
tags:
  - webdev
published: True
---

Serious question.

## No one ever got fired for choosing PostgreSQL

But, why. It's the most loved db, right? Right? Maybe it's time to rethink
it.

Don't get me wrong, if I need a relational db as a service, PostgreSQL is going
to be my first choice, but why do I need to run a separate application for it?

## Tutorials use sqlite

Why is that? Because there is nothing else to stand up. Nothing else to
maintain. And you probably already have it installed on just about anything
that has a battery.

## SQLite runs in memory

Don't need, or maybe don't want to persist state. Run it in memory. This is a
nice feature for running tests.

## Less exposure

SQLite is a file on your filesystem. It's not a web service. It's not a cloud
service. Not that postgres is insecure, but it is one more endpoint that you
have to think about securing.

## SQLite is easy to replicate

Want to run your new feature with prod data? pull a replica. If you are using
something like litestream you can restore a replica into your local dev
environment. You aren't, well it's just a file that you can cp into your local
dev environment if you have access.

## SQLite Does everything of what I need in an application db

SQLite has a rock solid set of features that covers everything that I need, and
when it's not I am probably thinking about pulling data into my application code
and running something custom anyways.

## SQLite runs on the edge

Most applications are read heavy and light on writes. Services like turso have
recognized this and built a business around it. They give you a master db that
all writes go to, and read replicas that can run on the edge with your
application code. You have a lot of users in different regions you can run
your application close to them without suffering from query latency or
replication complexity.

## SQLite probably does what you need it to

For a large number of use cases SQLite is probably the best thing to get you
off the ground quick, and likely all that you will need. Consider using it
before defaulting to postgres.
