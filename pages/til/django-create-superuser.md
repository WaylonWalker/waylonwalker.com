---
date: 2022-09-26 07:14:04
templateKey: til
title: django create superuser
status: 'published'
tags:
  - python
  - django
  - webdev

---

My next step into django made me realize that I do not have access to the admin panel, turns out that I need to create a cuper user first.

!["cybernetic soldier working on a rusting tape machine robot, cinematic lighting, detailed, cell shaded, 4 k, warm colours, concept art, by wlop, ilya kuvshinov, artgerm, krenz cushart, greg rutkowski, pixiv. cinematic dramatic atmosphere, sharp focus, volumetric lighting, cinematic lighting, studio quality" -s50 -W832 -H416 -C12.0 -Ak_lms -S3309980874](https://stable-diffusion.waylonwalker.com/000368.3309980874.webp)

## Run Migrations

Right away when trying to setup the superuser I ran into this issue

``` bash
django.db.utils.OperationalError: no such table: auth_user
```

Back to the [tutorial](https://docs.djangoproject.com/en/1.8/intro/tutorial01/)
tells me that I need to run migrations to setup some tables for the
`INSTALLED_APPS`, `django.contrib.admin` being one of them.

``` bash
python manage.py migrate
```

![Running the database migrations](https://screenshots.waylonwalker.com/trydjango-migration.png)

> yes I am still running remote on from my chromebook.

``` bash
python manage.py createsuperuser
```

![](https://screenshots.waylonwalker.com/trydjango-create-superuser.png)

The super user has been created.

![!["cybernetic soldier working on a rusting tape machine robot, cinematic lighting, detailed, cell shaded, 4 k, warm colours, concept art, by wlop, ilya kuvshinov, artgerm, krenz cushart, greg rutkowski, pixiv. cinematic dramatic atmosphere, sharp focus, volumetric lighting, cinematic lighting, studio quality" -s50 -W832 -H416 -C12.0 -Ak_lms -S2018296614](https://screenshots.waylonwalker.com/trydjango-trusted-origin-failure.png)
](https://stable-diffusion.waylonwalker.com/000368.2018296614.webp)

## CSRF FAILURE

My next issue trying to run off of a separate domain was a cross site request
forgery error.

![](https://screenshots.waylonwalker.com/trydjango-trusted-origin-failure.png)

Since this is a valid domain that we are hosting the app from we need to tell
Django that this is safe.  We can do this again in the `settings.py`, but this
time the variable we need is not there out of the box and we need to add it.

```
CSRF_TRUSTED_ORIGINS = ['https://localhost.waylonwalker.com']
```

## I made it!!

And we are in, and welcomed for the first time with this django admin panel.

![The Django admin panel](https://screenshots.waylonwalker.com/trydjango-hello-admin.png)

## Remote Hosting

You might find these settings helpful as well if you are trying to run your
site on a remote host like aws, digital ocean, linode, or any sort of cloud
providor.  I had it running in my home lab while I was out of the house and
ssh'd in over with a chromebook.

!["cybernetic soldier working on a rusting tape machine robot, cinematic lighting, detailed, cell shaded, 4 k, warm colours, concept art, by wlop, ilya kuvshinov, artgerm, krenz cushart, greg rutkowski, pixiv. cinematic dramatic atmosphere, sharp focus, volumetric lighting, cinematic lighting, studio quality" -s50 -W832 -H416 -C12.0 -Ak_lms -S1092166059](https://stable-diffusion.waylonwalker.com/000368.1092166059.webp)
