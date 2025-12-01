---
date: 2025-06-30 20:22:08
templateKey: blog-post
title: principal-engineer-at-meta
tags:
  - dev
  - catalytic
published: True

---

Jake Bolam principal engineer at Meta, has some of the best career advice for
those looking to become principal or just be better at their craft.  This
[video](https://www.youtube.com/clip/UgkxFp3xC-SrxNtLw3FW24b26DRhNrMra3m8) was
such a banger I had to bring it in as a full post, and not just a thought. It
was a random YouTube auto play, something that I probably wouldn't have clicked
on given title an thumbnail, but turned out to be very impactful.  Jake is such
a smart guy with a lot of great insights, and I can tell he thinks really quick
on his feet, he just pulled all of these things out of his head on the fly.

!!! Note "YT Algorithm Gold"
    I don't know what it is about this title and thumbnail, but it gives me "ex
    google, ex facebook, ex microsoft, $100M engineer" vibes in a cringy and
    not satire kind of way.  I would have never clicked on it, it autoplayed
    after a podcast and it hit, immediately I'm like who are these guys? subd
    and started this post it was so good.

## Long On Boarding

Jake had a super long period of on boarding at meta, he came in as a seasoned
leader yet took many months to get going.  This was a phase during or near the
end of the COVID-19 pandemic and his team was so swamped they were unable to
give him time to help him.  He felt his on boarding was taking longer than he
wanted, and found backend work at Instagram.  Moving to Instagram he jumped in
and starting making impact quick and found his way moving up the ladder serving
as tech lead for several teams.

> I grabbed a ton of clips from this video, but did not for this section as it
> was kinda long.

## Always open for a Chat

As busy as Jake is, he leaves "Always open for a chat" on his internal profile.
He does not care about rank into account, the intern can ask for a coffee chat.
His key metric is how well is this person receiving information.  If they are
coming back with the same questions every 3 months he is going to start telling
them he does not have the time.

[![✂️ Always Open for a Chat](https://i.ytimg.com/vi/QUhC5BDZt-E/maxresdefault.jpg)](https://youtube.com/clip/Ugkxjwsds5Z9qqqIlJonyHNZDy4B_ArcLjNx?si=9Oi-ODqqYR215kJn)

I've had a fair amount of personal experience with this.  Early in my career I
experience quite a bit of higher ranks feeling untouchable, they were
impossible to get a hold of, blew you off, and had more meetings than anyone
could bear.  It made me really look outside the company for inspiration and
mentorship most of the time.

## There's always time for coffee

While I don't have "Always open for a chat" on my
profile,  I've had many of these types of conversations with my peers.  It
might be about something career related or more often how to implement
containers, cloud, and good practices into small teams.

I remember a course in college shared the famous quote "There's always time for
coffee" and it stuck with me.  The demonstration goes that no matter how much
you fill your day with big rocks and tiny sand particles, there's always a
little more room for coffee, and he dumps coffee into a jar that he has already
filled up.

These conversations often become very impactful.  They can lead to having good
relationships or job opportunities.

## If we are not getting enough feedback, move faster

[![✂️ rollout faster](https://i.ytimg.com/vi/QUhC5BDZt-E/maxresdefault.jpg)](https://youtube.com/clip/UgkxBSPjfIERR8JcJXCOVXduYCRyn8VO6Kl0?si=MVaRDQROXC0D7Wn9)

## Take Down Prod Sometimes

This was an interesting take.  None of us really want to take down prod.  No
one is advocating for major outages, but this is is not 2005 shipping out
software on CD's anymore.  This take 100% depends on what you do and where you
work.  Obviously some sectors cannot take any downtime; nuclear power, cloud
systems supporting nuclear power, navigation systems, idk theres a bunch of
stuff.  I bet if you are reading this that aint you.  You're probably writing
some backend dashboard for the marketing team, or building out a website to
upload cat photos on ... Wait, thats literally what jake is doing here.

Idea being if you don't occasionally cause some small production issues, you
probably are not taking enough risk.  You are moving too slow, getting feedback
too late, your competitors just ran past you.

[![✂️ take down prod sometimes](https://i.ytimg.com/vi/QUhC5BDZt-E/maxresdefault.jpg)](https://youtube.com/clip/Ugkx-Jofyn4OmTOkxFzxU__5_7BAeG3O3IkE?si=8yAj3H_ZB-7vjw0W)

## Go where you are rare

I find this interesting.  I've found myself within non-software companies doing
sofware and data analysis most of my career, the amount of value you can bring
by being that one guy that knows some pandas, containerization, how to run a vm
is massive in an org that uses excel as its primary database.  The rest of the
org generally has massive knowledge in the business, but greatly slowed down by
their ability to find value in the data.

[![✂️ go where your rare](https://i.ytimg.com/vi/QUhC5BDZt-E/maxresdefault.jpg)](https://youtube.com/clip/UgkxZHKW3EHYH9Z8qPvyNlLQYN55BkufhmsJ?si=SwkO7bfrE16WFoyN)

## Do work that you don't get credit for

I've worked with a lot of people in my 15 years of professional work, and I can
tell you the worst ones to work with are the ones that focus too much on value.
Every ounce of effort they bring needs to be backed by dollars comming into the
business.  I've seen this shake out a number of ways.  You got the guy who sits
on his ass all of January waiting for goals to be set, you got the guy who
holds everything he knows close to his chest so that he is the one that can
take the glory, and you got the guy who wont ever; refactor his code, cleanup,
lint, update dependencies, and so on; because that does not have direct line to
dollars coming into the business.

[![✂️ 20% of time won't get credit](https://i.ytimg.com/vi/QUhC5BDZt-E/maxresdefault.jpg)](https://youtube.com/clip/UgkxFp3xC-SrxNtLw3FW24b26DRhNrMra3m8?si=5I5JhuxwNFKWZsL7)

The clip goes a bit further than this, and hints at things that are going to
enable you and your org to move faster.  You might shave off 2 minutes off of
ci, or docker builds.  You might give everyone an easy way to run dev
containers with production like dependencies in a snap.  You might give them a
way to clone prod data into a sandbox.  These type of things provide no dollars
to the company, it's likely that few will notice but damn they add up to an
efficient running organization.

## Work Diary - the value of writing things down

This one hits home, for far too long I've been in between note taking systems
and am finally getting [[ marakta ]] setup to build out a really good
zettelkasten style work notes.  I've kinda had this on my blog for a long time,
but not fully.  I think the piece that I am missing here is the dumping ground.
I don't **yet** have a daily notes implementation that lets me just dump idea
onto a page that I care little about, but is the process of starting something
bigger, crosslinking between people, meetings, tasks, and launchdocs.

[![✂️ work diary](https://i.ytimg.com/vi/QUhC5BDZt-E/maxresdefault.jpg)](https://youtube.com/clip/UgkxBC5Y_WL40hiEHY_zqjOVkLwkSQyyYvcC?si=l_tsY238JstdFSaA)

I hadn't heard of the term launchdoc before this, but I took it and I am using
it.  I generally do an ok doc in the changelog of my products and spice it up
to go to the announcement chat channel, but I don't fully keep record of it,
pulling the changelog into a launchdoc gives me that chance to spice it up and
have the language it needs to go right into chat.
