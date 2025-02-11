---
date: 2025-02-12 13:23:35
templateKey: blog-post
title: Setting up 4G Backup with Google Fi and Netgear LM1200
tags:
  - homelab
published: True

---

I connected my home network to have 4G bakcup with Google Fi and Netgear
LM1200.  Goodle Fi offers free data-only sim cards that you can order from
their service.  It takes a couple of days, and a new sim arrives in the mail
free of charge.  It does pull data from your account, so if you are not on an
unlimited plan be careful of how much you let go through the sim.

I've owned this for a few years now, but it's been disconnected for a good six
months or so.  I'm not s[e what happened, but it stopped recognizing the old
sim card. _no need to point out the coffee stains at the end, its
**definitely** not related_

## Follow the provided instuctions

Activating the sim asked for a confirmation code shipped with the sim card,
then brought me to this page.

![screenshot-2025-02-11T19-24-38-431Z.png](https://dropper.wayl.one/api/file/ec4d4272-7f61-4cf7-b3f5-ed2a57d0c11b.png)

Clicking `Have a Different Device?` brought up instructions to set up the APN in the LM1200.

![screenshot-2025-02-11T19-14-39-662Z.png](https://dropper.wayl.one/api/file/b54d9a7f-c768-45b8-bf90-e692a6525788.png)

## Restart

First thing for me was that the sim was not recognized, restarting the LM1200
did the trick to recognize it as a Google Fi sim, and I started setting up by
adding the APN as instructed from Google.

![screenshot-2025-02-11T19-22-55-062Z.png](https://dropper.wayl.one/api/file/9f10f86d-734a-4b6f-a1f6-1bed27c5db13.png)

## Setup LM1200

Once restarted the LM1200 was recognize the sim right away and I was able to
add the APN details.

![screenshot-2025-02-11T19-21-24-608Z.png](https://dropper.wayl.one/api/file/4c9b0dde-69ce-4d73-af89-06d32c70c9d3.png)

## Connected

After Saving these I was immediately connected as a backup.

![screenshot-2025-02-11T19-22-13-849Z.png](https://dropper.wayl.one/api/file/eb224d5a-6332-49e7-bde5-9f67c19d090f.png)

## Testing Failover

Backups do not exist without testing.  I pulled the WAN cable from the LM1200
and after a few seconds it swapped over to the backup.

![screenshot-2025-02-11T19-45-00-555Z.png](https://dropper.wayl.one/api/file/3fe17ab6-0fa6-4aa9-96d9-0d7ef6d191c0.png)

The dashboard shows fully connected, and it popped up that it sent an alert to
my phone, but that did not work for me.  I might hae something misconfigured.

![screenshot-2025-02-11T19-36-08-431Z.png](https://dropper.wayl.one/api/file/0229f36a-0b6b-4699-97c4-d526096c77fb.png)

I ran a speed test and got a pretty respectable 38 Mbit/s up and 12 Mbit/s down.

![screenshot-2025-02-11T19-54-49-024Z.png](https://dropper.wayl.one/api/file/83647660-cf04-422b-a0f3-8b860c6585e1.png)

I reconnected the WAN cable and it went back to the primary, and it sat at
orange for about 10 seconds before switching back to wired connection.

![screenshot-2025-02-11T19-45-31-516Z.png](https://dropper.wayl.one/api/file/e6c0f5fe-ec2c-4546-aaa1-d5e2fba0ae0c.png)

Fully back on wired.

![screenshot-2025-02-11T19-47-13-699Z.png](https://dropper.wayl.one/api/file/70f9fd2b-9611-466a-a07b-11525e2a7aaa.png)

Now its all back up and running giving me a super cheap 4G backup with pretty
low effort.  Hopefully its reliable, I've upgraded about everything else on my
network since last running this, I think it will behave much better.  I think
some other issues were actually causing me to think I was not getting
connection and this fully got pulled from the network to try to fix it.

## Why not 5G?

The devices are way more expensive and this gives me all I need for a backup.
