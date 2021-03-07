---
templateKey: blog-post
related_post_label: Check out this related post
tags: 
  - blog
title: Edit On GitHub
date: 2020-07-18T05:00:00Z
status: published
description: I recently added a button to my blog, and subsequently my posts on [DEV.to](https://dev.to/waylonwalker).  It's the best thing that I have done for it in a while.  
cover: '/static/edit-on-github.png'

---


I recently added a button to my blog, and subsequently my posts on [DEV.to](https://dev.to/waylonwalker).  It's the best thing that I have done for it in a while.  It makes it so easy to do quick edits.  

## finding errors

I refer back to my old posts quite a bit, sometimes I find errors in them.  Honestly most of the time its too much effort to load up my editor make the change and `git add` and `git commit`.  It's not much, but when I am referring to my own post generally I am just trying to get something done and don't have time for that.


## The slug

The slug that I am getting from gatsby is formatted as `/blog/this-post/`.  Note the trailing slash and missing file extension, thats where the `${slug.slice(0, -1)}.md` comes in.  


## The Full Link


GitHub makes it super easy to form a URL that puts you right into edit mode on the exact post you are looking for.  This is format for the URL... you can always figure it out easily by clicking edit on one.

```
https://github.com/<user>/<repo>/edit/<branch>/<filepath>
```

## The Final Result

Wrapping that URL up in a short snippet gave me the following result.

``` jsx
<p style={{ display: 'flex', justify: 'center', textAlign: 'center', margin: '3rem auto' }}>
  <span role='img' aria-label=''>👀</span>
  see an issue, edit this post on 
  <a 
    href={`https://github.com/WaylonWalker/waylonwalkerv2/edit/main/src/pages${slug.slice(0, -1)}.md`} 
    alt='edit post url' 
    title='edit this post'
   >
  <FiGithub /> 
  GitHub
  </a>
</p>
```
![Edit on GitHub](https://dev-to-uploads.s3.amazonaws.com/i/sgqd23rbbusjpfxqr7bl.PNG)

I know better than hard coding the GitHub url in, but I did it anyway, my personal site gets to be a bit of a rats nest of hotfixes over time.

This was a super quick change that brought me a lot of value without much effort.  I will probably change up the styling/layout of it in the future. For now I have something that functions, and I can get back to creating content.
