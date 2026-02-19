---
title: '💭 Change Autocomplete Styles in WebKit Browsers | CSS-Tricks - C...'
date: 2023-10-10T01:48:04
template: link
link: https://css-tricks.com/snippets/css/change-autocomplete-styles-webkit-browsers/
tags:
  - webdev
  - css
  - thoughts
  - thought
  - link
published: true

---

![[https://css-tricks.com/snippets/css/change-autocomplete-styles-webkit-browsers/]]

All the hover, select, autofil, focus combinations have left me confused on how to consistently get my form elements styled in dark mode

This snippet from CSS tricks has fixed all the different states for me to give me full control.
```
/* Change Autocomplete styles in Chrome*/
input:-webkit-autofill,
input:-webkit-autofill:hover, 
input:-webkit-autofill:focus,
textarea:-webkit-autofill,
textarea:-webkit-autofill:hover,
textarea:-webkit-autofill:focus,
select:-webkit-autofill,
select:-webkit-autofill:hover,
select:-webkit-autofill:focus {
  border: 1px solid green;
  -webkit-text-fill-color: green;
  -webkit-box-shadow: 0 0 0px 1000px #000 inset;
  transition: background-color 5000s ease-in-out 0s;
}
```

!!! note

    This post is a [[ thoughts | thought ]]. It's a short note that I make
    about someone else's content online #thoughts
