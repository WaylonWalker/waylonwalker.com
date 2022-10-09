---
date: 2022-10-09 15:57:37
templateKey: til
title: Getting Started with Django REST framework
status: 'draft'
tags:
  - python

---

In my adventure to learn django, I want to be able to setup REST api's to feed
into dynamic front end sites.  Potentially sites running react under the hood.

## Install

To get started lets open up a `todo` app that I created with `django-admin startproject todo`.

``` bash
pip install djangorestframework
```

## Install APP

Now we need to declare `rest_framwork` as an `INSTALLED_APP`.

``` bash
INSTALLED_APPS = [
    ...
    "rest_framework",
    ...
]
```

## create the api app

Next I will create all the files that I need to get the api running.

``` bash
mkdir api
touch api/__init__.py api/serializers.py api/urls.py api/views.py
```

## base/models.py

I already have the following model from last time I was playing with django. It
will suffice as it is not the focus of what I am learning for now.

> Note the name of the model class is singular, this is becuase django will
> automatically pluralize it in places like the admin panel, and you would end
> up with Itemss.

``` python
from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.priority} {self.name}"
```

Next I will make some dummy data to be able to return.  I popped open `ipython`
and made a few records.

``` python
from base.models import Item

Item.objects.create(name='first')
Item.objects.create(name='second')
Item.objects.create(name='third')
```

## api/serializers.py

Next we need to set up a serializer to seriaze and de-serialize data between
our model and json.  You can specify each field individually or all of them by
passing in `__all__`.


``` python
from rest_framework import serializers

from base.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
```

## api/views.py

Now we need a view leveraging the `djangorestframework`.  The serializer we
just created will be used to serialize all of the rows into a list of objects
that Response can handle.

> Note: to return a collection of model objects we need to set many to `True`

``` python
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Item

from .serializers import ItemSerializer


@api_view(["GET"])
def get_data(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_item(request):
    serializer = ItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()

```

## api/urls.py

Now we need to setup routing to access the views through an url.

``` python
from django.urls import path

from . import views

urlpatterns = [
        path('', views.get_data),
        path('add/', views.add_item),
        ]
```

## todo/urls.py

Then we need to include these urls from our api in the urls specified by `settings.ROOT_URLCONf`

``` python
from django.urls import path

urlpatterns = [
    ...
    path("api/", include("api.urls")),
]
```

## Run it

``` python
python manage.py runserver
```
