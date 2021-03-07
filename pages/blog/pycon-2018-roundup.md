---
templateKey: 'blog-post'
title: Pycon 2018 Roundup
date: 2018-05-12
category: Blog
tags:
    - python
summary: These are my notes from pycon 2018 videos.  I love the python community and especially the conference talks.  This year I am going to take some notes from my favorite talks and post them here.
description: none
cover: "./pycon2018.f76001445fbb.png"
---

These are my notes from pycon 2018 videos.  I love the python community and especially the conference talks.  This year I am going to take some notes from my favorite talks and post them here.

This is an **Incomplete** working post.


## [Jake VanderPlas - Performance Python: Seven Strategies for Optimizing Your Numerical Code](https://www.youtube.com/watch?v=zQeYx87mfyw)

* **Always** profile **before** making any optimizations.
* Vectorize with Numpy
    * Looping in python can be slow
* Use specialized data structures.
    * scipy.spacial
    * pandas
    * xarray
    * scipy.sparse
    * sparse package
    * scipy.sparce.csgraph
* Cython
    * Add types
* Numba
    * jit
    * Fortran Like Speed
    * heavy dependencies
* Dask
    * distributed tasks
    * Can be executed locally or on a cluster
* Look for an existing package
    * **resist the urge to reinvent the wheel**

https://www.youtube.com/watch?v=zQeYx87mfyw

## [Justin Crown - "WHAT IS THIS MESS?" - Writing tests for pre-existing code bases - PyCon 2018](https://www.youtube.com/watch?v=LDdUuoI_lIg)

This was a great talk about not only test driven development on existing code bases, but how to be a good steward of code.  Justin talks about how to clean up an existing code base, and leave it better than you found it.  Start by improving the parts that you touch, write tests, and improve docstrings whenever you make a change to a particular feature.  As you clean up the code base and it matures consider taking a sprint day to write tests and imporove documentation.  Doing it after you have familiarity with the project will make it much easier to do.  You will also improve your understanding of the parts that you have not touched along the way.

One of the biggest takeaways that I heard in this talk, was do not assume that last person to touch the code was any less than yourself.  They likely did what they did for a reason, so before you have strong test coverage accross the project take it easy with rewriting everything they did, and only make the necessary changes.  Your changes could have an impact on other parts of the code base that you are not familiar with.

https://.youtube.com/watch?v=zQeYx87mfyw


## [Jason Huggins - Keynote ](https://www.youtube.com/watch?v=q-x7jK72E6E)

Jason had a great talk about teaching kids to code through his experiences with First Lego League.  He found that the event has the best of intentions, but does lend itself to schools with a larger budget that is able to order many different kits.  He has found himself deep down a rabbit hole of finding an affordable alternative that can be done with the inexpensive raspbery pi zero, and controlled  with the cheapest tablets.  He is currently working on a programming language called wildcard, that can be programmed with paper.  This really reminds me of a game that I play with my 5 year old son [Robot Turtles](https://www.robotturtles.com).  He really likes to play it.  I will definitely be following this project to see if this is something that I can do with him when its ready.

https://www.youtube.com/watch?v=q-x7jK72E6E

## [Dan Callahan - Keynote - PyCon 2018](https://www.youtube.com/watch?v=ITksU31c1WY)
I was a bit sad when I was looking through the list of PyCon 2018 talks and did not see anything that appeared to talk about web assembly, but hidden in Dan Callagan's keynote was a great story about web assembly and what it means to python.  Dan's keynote was a great story about using the best tools available to you.  He goes back to his childhood where he programmed in basic because thats what he could take with him away from the desktop on his TI-82.  In modern times we have so many platforms other than desktop, and new ones comming out so frequently that its impossible to see what the next one will be.  There are even computers in refrigerators today.  The one thing that seems to be common is that they all have a web browser.  With that we can write web apps with python, but we are still missing the JavaScript dominated client side story.  Dan shows that this is changing with web assembly.  He showed examples where Autodesk compiled Autocad to wasm, and can run it in the browser!!  He showed versions of windows 3 running completely inside of firefox.  While it is currenly not realistic to compile python to web assembly as it creates large file sizes, it is possible and he sees a bright future for python in the browser.


https://www.youtube.com/watch?v=ITksU31c1WY

## [Alex Petralia - Analyzing Data: What pandas and SQL Taught Me About Taking an Average](https://www.youtube.com/watch?v=DlgG0QdrqAU)


Asks the right questions before writing the first line of code.  Even the simplest questions such as averages have many possible pitfalls along the way.  Alex discusses how to prepare your data before averaging in this talk.  He brings some new _"Jargon"_ .  I am not sure that this jargon made this any easier for me to understand or discuss.  It may take some time for this one to sink in to become effective.  I feel like using plain english is more effective as it is more easily understood by anyone.  "find the **daily** average **sales** by **seller**"
### Jargon
**Collapsing key:**
* the collapsed/aggregated data relevant to this analysis
* _we are overriding the primary key (i.e. what a table defines as an observation)_
* the original number of rows

**Grouping key:** the key defining a group**
* _eg. "for each Seller" is (seller), "for each Country and city is (Country, City)_
* this defines how many rows are in the result

** Obvervation key: a unit of observation for this analysis**
* _eg. "daily average" is (Date), "across regions" is (Region)_
* this defines how many rows are in the denominator

### Formula
Collapsing Key - Grouping Key = Observation Key

### Example Question
Calculate the Average Daily Sales for each Seller.

**Collapsing Key:** (Date, Seller)
**Grouping Key:** (Seller)
**Observation Key:** (Date)

### data set

| id | Date    | Seller | ApplesSold |
|----|---------|--------|------------|
| 1  | Monday  | Mary   | 5          |
| 1  | Monday  | Bob    | 4          |
| 1  | Tuesday | Bob    | 8          |
| 1  | Thursday| Jane   | 10         |
| 1  | Thursday| Jane   | 6          |

### SQL Example
```SQL
SELECT
    Seller,
    AVG(total)
FROM (
    SELECT
       DATE,
       SELLER,
       SUM(ApplesSold) AS total
    FROM
       Apples
    GROUP BY
       DATE,
       SELLER -- Collapsing Key
    ) as t
GROUP BY
    Seller -- Grouping Key


```
### Pandas Example
I am interested in trying out this technique of using the second groupby.  I typically use an unstack instead, but that relies on having the order of the Collapsing key correct.
```python
(pd
    .groupby(['Date', 'Seller']) # Collapsing Key
    ['ApplesSold']
    .sum()
    .groupby(level='Seller') # Grouping Key
    .mean()
    )
```


https://www.youtube.com/watch?v=DlgG0QdrqAU

## [Devishi Jha - Teaching Python 101 - PyCon 2018](https://www.youtube.com/watch?v=s36GwDng904&t=1113s)

I was really impresssed by the professional level of presentation from Devishi from such a young age!  She had a great talk about teaching python to young people.  This talk really resonated with me as a father of two young children. She was advocating for python to be taught more frequently and earlier in schools.  In her opion onece students have a basic grasp of algebra they should be starting to use python over a higher level abstraction like scratch.  She also advocated that on the other Java tends to make computer science unaproachable and too difficult for students.  It is too large of a jump and tends to steer students away.

https://www.youtube.com/watch?v=s36GwDng904
