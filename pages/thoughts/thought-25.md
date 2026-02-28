---
title: '💭 encodeURIComponent() - JavaScript | MDN'
date: 2023-07-28T14:59:37
template: link
link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent
tags:
  - javascript
  - webdev
  - thoughts
  - thought
  - link
published: true

---

![[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent]]

In order to send data that includes special characters such as `/` in a url you need to url encode it.  You have probably seen these many times in urls with things like %20 for spaces.

I'm working on a chrome extension to make quick blog posts, like thoughts or a persistent bookmark tool with comments.  The backend is written in fastapi and when I check to see if I have a post for a page I need to url encode it.

``` bash
curl -X 'GET' \
  'https://thoughts.waylonwalker.com/link/?link=https%3A%2F%2Fhtmx.org%2Fextensions%2Fclient-side-templates%2F' \
  -H 'accept: application/json'
```

> curl example generated from the fastapi swagger docs.

Here is how I used javascript's `encodeURIComponent` to turn my chrome extension into a notification when I already have a post for the current page.

``` js
// Event listener for tab changes
chrome.tabs.onActivated.addListener(function (activeInfo) {
  // Get the active tab information
  chrome.tabs.get(activeInfo.tabId, function (tab) {
    const url = tab.url || "";

    getData(`https://thoughts.waylonwalker.com/link/?link=${encodeURIComponent(url)}`).then((data) => {
        console.log('link data: ', data);
      if (data.hasOwnProperty('detail')) {
        chrome.browserAction.setBadgeText({ text: "" });
      } else {
        localStorageKey = `formData-${url}`;
        chrome.browserAction.setBadgeText({ text: "1" });
        chrome.browserAction.setBadgeBackgroundColor({ color: "#80A3D5" });
        localStorage.setItem(localStorageKey, JSON.stringify(data));
      }
    });
  });
});
```


!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
