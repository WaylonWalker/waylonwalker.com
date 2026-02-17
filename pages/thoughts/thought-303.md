---
title: '💭 How to Configure DNS over TLS (DoT) Using Unbound DNS in OPNsense'
date: 2024-06-09T15:40:11
templateKey: link
link: https://homenetworkguy.com/how-to/configure-dns-over-tls-unbound-opnsense/
tags:
  - opnsense
published: true

---

> Setting up DNS overTLS in opnsense has made my dns just a bit more secure and reliable.  I recently had an outage of half the internet within my house.  This also hit some of my friends and not some.  It did not hit my mobile network.  What seems to have happened is a dns issue with my isp not resolving some domains.  This setup corrected my issue and I was back online more securely.

!!! Note
   I did try to setup the family resolver and found it was blocking some sites I am ok with.  I decided to drop back to the vanilla resolver and let other services within opnsense control blocking where I can caontrol the whitelist myself.

[Original thought](https://homenetworkguy.com/how-to/configure-dns-over-tls-unbound-opnsense/)
