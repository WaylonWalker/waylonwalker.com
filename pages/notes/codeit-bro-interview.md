---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: Codeit Bro Interview
date: 2020-11-02T06:00:00.000+00:00
status: published
description: ''
cover: "static/codeit-bro-interview.png"

---
![profile image](https://images.waylonwalker.com/profile.jpg)

> use this profile image

> Please share your professional role as a data scientist? \[Also feel free to
> share about your personal projects, publications, etc.\]

I graduated with a Mechanical Engineering Degree 8 years ago.  Much of my work
[early in my career](https://waylonwalker.com/eight-years-cat) was wrapped
around analyzing larger datasets for my group to understand quality, drive
changes to improve quality or prove that quality was already good.

<p style='text-align: center'>
<a href='https://waylonwalker.com/eight-years-cat'>
<img
style='width:500px; max-width:80%; margin: auto;'
src="https://images.waylonwalker.com/eight-years-cat.png"
alt="My first eight years as a working professional article"
/>
</a>
</p>

Three years ago I made the switch to Data Science and have loved every minute of
it.  It is a very dynamic field that is continually changing and there are
always a new set of skills to learn and hone in on.  I talk a lot about the
mindset of always learning, sharing knowledge, and communicating in my
[newsletter](https://waylonwalker.com/newsletter)

> What are the most difficult challenges you faced as a data scientist and how
> you resolved them?

Deployment is a high bar to enter.  Jupyter notebooks provide a suspiciously simple start into Data Science.  Folks with very little coding experience can easily get up and running and start bringing value back into their organization, but as you want to start sharing these notebooks, re-using components of them, and scheduling them to run autonomously the bar is raised very quickly.  Many places will have teams dedicated to each piece of the process, but all too often if you want your project to be successful you have to step out of your comfort zone and do much of it yourself.

Getting started in Data Science

* Jupyter

Going to production

* packaging
* creating cli's
* linux
* bash
* cron
* CI/CD
* git
* Docker
* AWS
* Pipelines
* Schedulers/orchestration
* Virtual Machines
* hosting docs
* hosting models/apis
* Visualizations
* Databases
* blob storage
* ...

> What are the most required skills for a data scientist?

* Communication
* project Estimation
* Subject Matter Expertise
* Python

A good understanding of the business problems you are trying to solve.  This
requires very good communication between Subject matter experts and the Data
Science team.

For the technical side, python is the core skill that I stick with.  As I said
before this quickly starts to grow as you start needing to take projects into
production.  Learning how to write good python efficiently without needing to
look up much really frees up your brain to focus on the harder challenge of
solving the problem at hand.

Learn how to frame up your problem ahead of time and be flexible in just the
right ways.

Let's make up a fictitious transportation company that is split into a number of divisions for car, train, bus, etc.  All too often I see projects setup as a pilot for the car division, or even a micro subset of the car division.  The proof of concept takes off, and now we need to expand the project from one city to a whole region, but since the city was hard coded in it makes it really hard to expand. After a few months we have a lot of copy and paste code and at some point it becomes nearly impossible to make any changes without needing to change everything, or expand to new regions or divisions. Understand the inputs to your problem set early on and plan for them to change.

> How a beginner can create a roadmap to become a successful data scientist in
> the present scenario?

Someone who is currently working in any sort of role that involves manipulating data in excel can get their foot in the door by automating the work their team does in python, or visualizing it in a more powerful tool.

You will quickly find that you can handle much more data than spreadsheet tools can, you can start expanding projects to utilize more data, or use that extra free time to find new insights you didn't have time for before.

> How much Maths is required to be a good data scientist? \[You can also share
> which concepts should everyone focus on more\]

I have a lot of math background from my Mechanical Engineering degree that I haven't use in years.

To be clear I am not generally building models in my day to day.  My role kind
of sits between Data Engineering and MLOps these days.  I scaffold up new
projects for the team, take on more complex data pipelining projects, and own
our whole deployment system.  None of this really requires advanced math on a
day to day basis.

> What are some concepts that everyone should know more

Linters.  They are so easy to run that no one should be bad code that fails
linting these days.  You can set them to run from your favorite editor, the
command line, in a git commit, from GitHub Actions, or an Azure pipeline, just
figure out the ones that fit you and run them.

> Will data science be replaced by AI?

Everything that we see today will be different in the future whether replaced by
AI or the next hot topic.  There might be subsets of our work that is completely
automated away.  I think it will be a great opportunity to focus our minds on
more difficult things that AI cannot.  Data Science is a relatively new field,
be ready for it to change and move with it.

> Words of advice for people without a Computer Science background?

You can do it, there are more folks out there crushing Data Science and Software Engineering in general without a Computer Science background than you realize. Don't let the imposter syndrome get to you.  Keep honing your skills and be confident.

* Be flexible
* Always be open and ready for change
* Never stop learning
* Keep a positive attitude
* Be kind to others

> Tell us about your journey towards becoming a successful data scientist?

see Q1

> Which tools you use for Data Science and which one do you recommend for
> beginners?

As a beginner definitely focus on a minimal number of things at a time.  As you go through the journey of learning anything you will likely to see articles that tell you that your tech of choice is dead and should never be used because some new hotness it so much better.  Focus on skills that have a real job market and solve real problems don't worry so much about it that you never learn one.

Python is my core skill, it can do so much so quickly and has a very strong ecosystem in data.

A skill I would add in general is to deploy early.  Too often we spend months on prototypes that need rewritten for the prod environment, when they could have just been written for prod from the beginning while ci tooling could have kept the project cleaner and easier to work with.  Whether its GitHub actions or Azure Pipelines CI/CD is cheaper and easier to setup than ever.  There is a fluid movement that happens when you are working with clean code along the way rather than cleaning it up after its all done.  Simplifying your work opens up mental space to put more focus on your problem at hand.

<p style='text-align: center'>
<a href='https://waylonwalker.com/what-are-github-actions'>
<img
style='width:500px; max-width:80%; margin: auto;'
src="https://images.waylonwalker.com/what-are-github-actions.png"
alt="introductory article to GitHub actions"
/>
</a>
</p>

> check out this article about github actions

> Is data science a stressful job?

It definitely can be if you let it.  Manage expectations and scope creep well and you will be fine.  My most stressful times have probably been when I over committed to something and it was my own fault for setting myself up for stress.

> What type of problems you faced every day as a data scientist?

At a high level the business I support remanufactures ( similar to recycling ) parts for heavy equipment.  I find ways to re-use more core material to save cost and reduce emissions.  A lot of what I do is solving business problems with code.  This might be a problem that has been solved by hand for a small focused subset of a population and expanding it to everything.  More and more of my time is being dedicated to coaching.  Whether in the form of code review, pair programming, or general mentoring.
