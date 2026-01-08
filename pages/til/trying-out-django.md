---
date: 2022-09-25 18:47:54
templateKey: til
title: Trying out django
published: true
tags:
  - python
  - django
  - webdev

---

I have no experience in django, and in my exploration to become a better python
developer I am dipping my toe into one of the most polished and widely used web
frameworks Django to so that I can better understand it and become a better
python developer.

If you found this at all helpful make sure you check out the [django tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)


!["An atronaut working in a lab, there is a long snake working along side, shallow depth of field beakers, test tubes, volumetric lighting, pink lighting, by victo ngai, killian eng vibrant colours, dynamic lighting, digital art" -s50 -W768 -H448 -C7.5 -Ak_lms -S2250540408](https://stable-diffusion.waylonwalker.com/000243.2250540408.webp)
## install django

The first thing I need to do is render out a template to start the project.
For this I need the `django-admin` cli.  To get this I am going the route of
`pipx` it will be installed globally on my system in it's own virtual
environment that I don't have to manage.  This will be useful only for using
startproject as far as I know.

``` bash
pipx install django
django-admin startproject try_django
cd try_django
```

![django-startproject.webp](https://dropper.waylonwalker.com/api/file/1913211c-81ac-4de4-af49-9a532f0786f7.webp)

## Make a venv

Once I have the project I need a venv for all of django and all of my
dependencies I might need for the project.  I have really been diggin `hatch`
lately, and it has a one line _"make a virtual environment and manage it for
me"_ command.

``` bash
hatch shell
```

![trydjango-venv.webp](https://dropper.waylonwalker.com/api/file/974809a1-02bd-46c4-acf9-783fd5128b35.webp)

If hatch is a bit bleeding edge for you, or it has died out by the time you
read this.  The ol trusty venv will likely stand the test of time, this is what
I would use for that.

``` bash
python -m .venv --prmpt `basename $PWD`
. ./.venv/bin/activate
```

## Start the webserver

Next up we need to start the webserver to start seeing that development
content.  The first thing I did was run it as stated in the tutorial and find
it clashed with a currently running web server port.

``` bash
python manage.py runserver
```

![django-runserver-oops.webp](https://dropper.waylonwalker.com/api/file/ac1397f4-71b9-4617-9438-33cfa2e53c75.webp)

I jumped over to that tmux session, killed the process and I was up and running.

![trydjango-runserver.webp](https://dropper.waylonwalker.com/api/file/828d8e21-00c7-4f02-bd47-e3cebc318adc.webp)

## What's running

The default django hello world looks well designed.  You are first presented
with this page.

![trydjango-hello.webp](https://dropper.waylonwalker.com/api/file/e5523925-1565-454c-bab3-c70c4deabc83.webp)

## Next

I opened up the `urls.py` to discover that the only configured url was at
`/admin`. I tried to log in as admin, but was unable to as I have not yet
created a superuser.  Next time I play with django that is what I will explore.

![An astronaut working in a dimly lit labratory, it is almost black, heavy dark blacks, black space, heavy vingette, hacking on a computer terminal, htop is running, shallow depth of field beakers, test tubes, by Alphonse Mucha, dynamic lighting, digital art](https://stable-diffusion.waylonwalker.com/000250.526887289.webp)
