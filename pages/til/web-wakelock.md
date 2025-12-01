---
date: 2025-05-21 20:50:22
templateKey: til
title: web wakelock
published: true
tags:
  - python

---

I'm trying to replace my usage of google inline search apps with real apps,
today I used a stopwatch to time some things out at work by opening stopwatch.
This was something I just wanted running in a tab on another screen, it was not
timing running code or anything, I was using it as a reminder to check browser
caches every 5 minutes or so for some testing.

So tonight I whipped up a [stopwatch](https://stopwatch.wayl.one),
[clock](https://clock.wayl.one) and [timer](https://timer.wayl.one), all of
which are using the wakelock API to keep the screen on while the app is
running.

``` js
    // Wake Lock support
    let wakeLock = null;
    async function requestWakeLock() {
      try {
        if ('wakeLock' in navigator) {
          wakeLock = await navigator.wakeLock.request('screen');
          console.log("Wake lock acquired");
        }
      } catch (err) {
        console.error("Wake lock error:", err);
      }
    }

    document.addEventListener("visibilitychange", () => {
      if (wakeLock !== null && document.visibilityState === "visible") {
        requestWakeLock();
      }
    });

    requestWakeLock();
```
