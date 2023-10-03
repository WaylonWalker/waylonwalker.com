---
date: 2023-09-30 21:26:36
templateKey: blog-post
title: why-is-postgres-default
tags:
  - webdev
  - data
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

> this means that is probably also cheaper 🤑

## SQLite is easy to replicate

Want to run your new feature with prod data? Pull a replica or backup. It's a
file, you can cp, scp, rsync it whatever you have available.

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

## You probably already know how to maintain it

If you know a bit of cli commands and remember that your database is just a
file, this will feel very intuitive. If not you can probably poke around a
file system gui and still make most of it work.

```bash
## create a database
touch database.db
## back it up
cp database.db database.db.bak
## drop the database
rm database.db
## restore the backup
cp database.db.bak database.db
## drop the backup
rm database.db.bak
## create an offsite backup
aws s3 cp database.db s3://my-backup-bucket/
scp database.db username@to_host:/remote/directory/
rsync -a database.db username@to_host:/remote/directory/
```

## Need High Concurrent writes

You might consider postgres.

## Need Remote connection string

You might consider postgres.
