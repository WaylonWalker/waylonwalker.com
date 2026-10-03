---
template: "post"
title: "bloatware is dying"
slug: "bloatware-is-dying"
date: 2026-10-03T15:40:39Z
published: true
tags: webdev

---

Yesterday my daughter an I were waiting for her practice to start and we wanted to play a game.  She downloaded an app on her phone that allows you to record your voice and play it in reverse.  Heres the game we come up with.

1. say a word in the recording
1. play it back in reverse to the next person
1. The next person says exactly what they hear without thinking

![19da0872-340f-4470-bcbc-475282808de9.webm](https://dropper.wayl.one/file/19da0872-340f-4470-bcbc-475282808de9.webm)

Every single one was followed up with a _Suppa ==Hot== Fire_ Ahh^hhh^~hh~ reaction by everyone around. They all sounded like complete gibberish, yet came out like the person was talking in a weird accent. Everyone was shocked to hear it was understandable what they were saying revering their reverse speech.

## Seriously give it a try

==expesially== if you have kids, its so **fun** to have a small group of people speaking giberish and out comes something understandable.

## Next Day

The next day I was out with my son and telling him about how cool the game was and how you just gotta hear it to understand it.  I was driving so I handed him my phone and said download an app that reverses your voice.

## The app store is broke

He proceeded to download 4 apps.  one required an external log in. the other 3 started rolling 2 minute ads before we were allowed in.  It was all shitty bloatware.  I'm not sure if my daughter got lucky or they protect kids from getting the same level of **garbage** I was getting from the app store, but **every** single one we tried was hot trash.

> At this point I'm getting ==pissed==.

I was getting frustrated, this should be the most basic app.  Like something 100 people have shipped out there as a demo app for their portfolio.  The basics cannot be that complicated and just build on what android already gives you right?  I'm getting pissed, I just want a thing to do a thing, its simple right? 

## just hand me the phone
_==GIVE== me that thing_

After this many attempts, I had him open chatgpt, yes boomer chat, no agents just vanilla ass gippity in the app.  I voiced out the following prompt.

> Make me a web app that has a big button in the middle to record my voice. I'll record for approximately 15 to 30 seconds. Once recorded, give me a button to playback or playback in reverse. We're going to make a game where the next person will try to say exactly what they hear, like a game of telephone. So if you could store the previous clips in a history, like a log, that would be great. But the big easy-to-press buttons are record, play, and reverse. Record should only record while I'm holding the button. When I'm done, it will make a clip. If I messed up, I can delete my clip and try again. This should all run in one single HTML file, local storage, no server.

## It's launched!
_and worked first **try^eeee^**_

I probably could have used the gippity sites service, but I just downloaded and immediately ran into permissions. unless you have https I dont think you can request the mic.  Maybe you need a server and a `python -m http.server` would have been fine.  I downloaded it onto my desktop and ran a just recpie to put a new app in the homelab, and it was up immediately

![embed](https://voice-reverse.waylonwalker.com/)

## One follow up

I want to keep this a pure `one-shot` as much as I can for now, but I wanted the metadata to come out right for when I share/embed.

>  make sure this app has all the proper meta tags for sharing ask me if you need any questions answered, the images should be shots linked with shots.waylonwalker.com

## Personal Software FTW

This is the age of personal software.  For those of you asking _If this **ai** stuff is so good where is the shovelware?_  here it is.  Its killing the shovelware.  You can just make your own thing the moment you need it, ship it, share it, or thow it away.  Theres no need to market it or sell it or shove it in anyones face, they can just make their own how they want it.

I hear DHH say that eventually languages will be dead and we will be asking in english and machine code for any cpu architecture you want will just pop out.  That's a little wild and far fetched, but we are kinda there.  I've yet to have an experience like this.  A fairly ==normie== experience where I cant find what I want and wish it into existence and it just pops out.  No agents or anything fancy _besides maybe the k8s deployment_ and I just got an app that I was looking for better and faster than we could find one on the app store.  Maybe there are 100 like this out there on the web and we just didn't look, maybe theres one on the apple store you can pay two bucks for, but now this one is mine and I can make it do whatever the heck I want it to do by whispering sweet nothings into the magic genies ear