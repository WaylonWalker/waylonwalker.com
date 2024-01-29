---
date: 2024-01-28 09:49:57
templateKey: blog-post
title: poc is not product
tags:
  - startup
published: True

---

A poc is **not** a product.  I started focais, not in a rush, but as something
that I already had a POC for and thought it would be easy.  I wanted to build
tools to make creating blog posts like this one easier.  I stared with `shots`
a tool that takes screenshots of websites.

## POC (proof of concept)

For the poc, I made a single fastapi endpoint that takes a url and returns a
screenshot of the page.  It converts the url into a key that I can lookup to
see if I have the shot, if I don't I go get it.  With the open source libraries
out there, this is not too hard of a task.

### Progress Thus Far

* /shot

> But this wasn't enough

All it does so far for this first tool is take screenshots of websites, and
give you a hosted image.

## Users

To bring in users, I need to create a signup flow, with a database to store
users, login, logout, and email recovery.  I've never had to use an email
service before that wasn't already mandated by a company or an iternal smtp
server.  After some searching I chose resend for email.

### Progress thus far

* /shot
* email service for account recovery
* database to store users
* /login
* /forgot-password
* /recover-account
* /logout
* /signup
* /access-token
* /account

## User Management

Eventually I am going to need some user management for site admins (me), but
for now I just need to see users and some of their attributes such as
subscription level, number of shots, and such.  If I'm ever contacted for
support this will give me some first insight into what happened.

## Subscription Levels

For payment I chose stripe.  I was able to setup subscription levels with
config inside of stripe.  I setup a pricing page with jinja based on the data
right out of stripe, a way to create checkout sessions, a page to come back to
once you have executed a checkout, and a way to cancel your subscription.

### Progress thus far

* /shot
* email service for account recovery
* database to store users
* /login
* /forgot-password
* /recover-account
* /logout
* /signup
* /access-token
* /account
* stripe account
* stripe api integration
* /pricing
* /create-checkout-session
* /checkout-success
* /cancel-subscription
* /reactivate-subscription

## Back to the Product

Now that I have users, with subscriptions, and different subscription levels. A
shot might not be the same per url.  For instance a shot from a low tier
subscription might have a watermark, while a higher tier will remove the
watermark.  Now I need a way to track shots per user, and keep them up to date
with subscriptions.

### Progress thus far

* /shot
* email service for account recovery
* database to store users
* /login
* /forgot-password
* /recover-account
* /logout
* /signup
* /access-token
* /account
* stripe account
* stripe api integration
* /pricing
* /create-checkout-session
* /checkout-success
* /cancel-subscription
* /reactivate-subscription
* POST /shot
* GET /shot/{id}

## Keeping the internet working

At the end of all of this once a shot is created I want to keep it working for
users regarless of subscription.  It really bothers me when part of the
internet just stops working.  I hope to keep running costs low and enough
monthly subscribers to cover those costs.  And if you decide that fokais is not
a product giving you any more value your shots will still be here with us.  At
the moment the biggest cost is compute running headless chrome to take the
shots anyways, continuing to host them over time is must less of an issue.

## It's a Lot, but not near enough

I'm a couple of months in on building this for a few days at a time here an
there. I am in no rush for it to start gaining revenue.  I am learning a ton so
far.  Whether fokais becomes a big thing or not, I will be able to bring these
skills to a new startup or to my professional career.

It already feels 1000% more complicated than it was just to get the thing to
work for just me, but in the end it will be worth it.

## It's still not complete

There's feels like quite a bit to do before getting launched, testing out the
checkout workflow is HUGE thing.  I've never made a product for sale by myself
before, so I am definitly feeling some pressure when taking money to have a
product that works, and importantly not loosing the subscription or account.
