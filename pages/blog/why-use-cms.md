---
templateKey: blog-post
related_post_label: Check out this related post
tags: ['webdev']
title: Why use a cms
date: 2020-07-14T03:00:00Z
status: published
description: When first learning to code its very common to hard code
    everything right into the code. This happens with most folks in just about
    any language. Whether its html or markdown for front end content, or even
    hardcoding parameters in our backend languages like python, or node.js.
cover: '/static/why-use-cms.png'

---

When first learning to code its very common to hard code everything right into the code. This happens with most folks in just about any language. Whether its HTML or markdown for front end content, or even hardcoding parameters in our backend languages like python, or node.js.

## 🤷‍♀️ What's wrong with hard coding everything?

Hard coding everything right into your code makes it really hard for non-technical collaborators to join. It makes it nearly impossible to hand websites off to clients without needing to come back for routine updates.

The cms generally come with a rich content editor that feels more like something most folks are used to. There are buttons for changing the font, font-size, adding images, bold, italics, etc.

## Sometimes I don't feel technical

Even when you are developing for a technical audience there is a layer of polish that comes from giving them a nice interface to edit their content in. YouTube doesn't have you manually inserting records into the database to add a comment, or upload a new video, nor would anyone expect you to.

![Edit on GitHub](https://dev-to-uploads.s3.amazonaws.com/i/sgqd23rbbusjpfxqr7bl.PNG)

> I recently added an edit button on my posts that allows me to jump right into edit on GitHub.  I have used this so much, I should have done this long ago!

There are times when I want to edit my blog on the go from my phone while on the go. I use [forestry.io](https://forestry.io) to do this for the most part. It gives me an image uploader, and a markdown editor to edit this blog right from my phone.


![forestry editor](https://images.waylonwalker.com/2019-05-09 10-40-11_forestry.io.png)

> My Blog on forestry.io


## What do they output

There are a number of different CMS's out there, and I haven't touched most of them. Some write content into a MySQL database while others kick out HTML or markdown to a git repo. I prefer the ones built off of a git repo for my site because I am cheap and I am not making anything from this blog yet, but you might want to check into some of the other options if you plan on handing your site off to a client.

## 🤑 pricing

Be aware of the various pricing models. They are priced every which way, per content editor, per site, per number of edits. Some offer free versions. Some are open source but require you to host it somewhere. Before you pick one make sure that you know your requirements.

## CMS's are more norm than I realized

When I was first starting into web development, I was completely unaware of the concept of a CMS. I had thought that content needs to be in HTML, or markdown, with a few specific places that users could edit. This may have been the case many years ago, but not anymore. The first time I ever designed a website for someone other than myself I got quite a shock when I realized how many edits they wanted, and how un-appealing markdown is for most.

## Where CMS's fall short 🍂

Please correct me if I am wrong here, I would love to be wrong on this. CMS's are not for developing the whole site. They hold data for content like site title, description, menu items, or blog posts. They don't necessarily give the user a full website designer, with drag and drop, and every widget imaginable. The web developer still needs to implement the site design and data integration.
