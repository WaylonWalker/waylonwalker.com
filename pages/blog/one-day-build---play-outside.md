---
date: 2024-04-10 12:32:20
templateKey: blog-post
title: One Day Build - Play Outside
slug: odb-play-outside
tags:
  - python
published: true
jinja: false

---

Inspired by Adam Savage and his One Day builds on youtube.  I often build
things, and want to make them generally useful for others and over configure
out of the gate.  This project is purely for me inspired by a need I have.

* [play-outside](https://play-outside.wayl.one/)

## !How-To

This post will not directly show how to make a weather app, but document the
process that I went through to make mine.  It will show the tools that I used
to make it, and the final result.

## The Situation

It often goes in our house ask dad while he is busy and he will probably just
say yes without thinking much.  This happens a lot when kids ask to go
outside.  I think sure, go for it, you will figure it out.  Then my wife walks
in and asks where they are, followed by, did you even check the weather, its
-11 degrees outside right now.

> I need a tool for this decision making process

## Lungs

You we have a family of not the most heathly lungs, we have my wife with lung
cancer, one lung missing, and kids with asthma.  We need to account for
temperature, humidity, wind chill, and air quality before heading outside and
seeing the repercussions of it later.

## Final result

So this is what I built, its a web app that checks the weather and air quality
in your area and determines if its safe to go outside.  It will even recommend
limiting your time, or wearing a coat.

[![](https://shots.wayl.one/shot/?url=https://play-outside.wayl.one&amp;height=1200&amp;width=600&amp;scaled_width=600&amp;scaled_height=1200&amp;selectors=)](https://play-outside.wayl.one/)

## The Stack

This is a one day build, I have both kids at home from school, so this is
realistically only like 2-3 hours at most, so this has to be chosen based on
familiarity.

* Docker
* k8s
* Python
* FastAPI
* tailwind
* httpx
* OpenWeatherMap API
* ipwho.is

This is the same stack (minue the apis) that I am using to build my startup
fokais.com with.  I am quite familiar with it and should be able to quickly
make progress with it.

``` shell
❯ tree
Permissions Size User   Date Modified Git Name
drwxr-xr-x     - waylon 16 Jan 12:21   -N  .
.rw-r--r--  3.8k waylon 16 Jan 12:24   -N ├──  deployment.yaml
.rw-r--r--   278 waylon 16 Jan 12:21   -N ├──  docker-compose.yml
.rw-r--r--   552 waylon 16 Jan 12:20   -N ├──  Dockerfile
.rw-r--r--   15k waylon 15 Jan 14:37   -N ├──  favicon.ico
.rw-r--r--  1.9k waylon 15 Jan 15:58   -N ├──  justfile
.rw-r--r--  1.1k waylon 15 Jan 11:39   -N ├──  LICENSE.txt
.rw-r--r--   51k waylon 15 Jan 14:38   -N ├──  package-lock.json
.rw-r--r--    69 waylon 15 Jan 14:38   -N ├──  package.json
drwxr-xr-x     - waylon 16 Jan 12:20   -N ├──  play_outside
.rw-r--r--   138 waylon 16 Jan 12:21   -N │  ├──  __about__.py
.rw-r--r--   115 waylon 15 Jan 11:39   -N │  ├──  __init__.py
.rw-r--r--  7.5k waylon 16 Jan 08:14   -N │  ├──  api.py
drwxr-xr-x     - waylon 15 Jan 21:30   -N │  ├──  cli
.rw-r--r--  3.5k waylon 15 Jan 21:30   -N │  │  └──  api.py
.rw-r--r--  2.8k waylon 16 Jan 12:20   -N │  ├──  config.py
.rw-r--r--  3.0k waylon 15 Jan 14:35   -N │  ├──  decorators.py
.rw-r--r--    51 waylon 15 Jan 14:50   -N │  └──  queries.py
.rw-r--r--  2.2k waylon 15 Jan 15:16   -N ├──  pyproject.toml
.rw-r--r--   506 waylon 15 Jan 11:39   -N ├──  README.md
drwxr-xr-x     - waylon 15 Jan 14:39   -N ├──  static
.rw-r--r--   21k waylon 16 Jan 08:10   -N │  ├──  app.css
.rw-r--r--   15k waylon 15 Jan 14:37   -N │  ├──  favicon.ico
.rw-r--r--   47k waylon 15 Jan 14:32   -N │  └──  htmx.org@1.9.8
drwxr-xr-x     - waylon 15 Jan 21:04   -N ├──  tailwind
.rw-r--r--  6.2k waylon 15 Jan 21:04   -N │  └──  app.css
.rw-r--r--   360 waylon 15 Jan 21:04   -N ├──  tailwind.config.js
drwxr-xr-x     - waylon 16 Jan 12:16   -N ├──  templates
.rw-r--r--  2.5k waylon 16 Jan 12:16   -N │  ├──  base.html
.rw-r--r--  2.2k waylon 16 Jan 12:11   -N │  ├──  card.html
.rw-r--r--   151 waylon 15 Jan 21:07   -N │  ├──  includestyles.html
.rw-r--r--   418 waylon 16 Jan 12:12   -N │  └──  index.html
drwxr-xr-x     - waylon 15 Jan 11:39   -N └──  tests
.rw-r--r--   115 waylon 15 Jan 11:39   -N    └──  __init__.py
```

## HTMX BTW

I have been pairing up htmx with this stack quite a lot lately, and its
fantastic, but honestly this idea just does not have a lot of endpoints, and I
don't think it needs it for a one day build, just toss everything into one page
and call it good.

## Getting Weather Data

The first thing we need is the feels_like or Apartment Temperature.  A quick
google search lead me to <https://openweathermap.org/> they have a very nice
calculation for the feels like temerature already built in.

<a href='https://openweathermap.org/' >
<img
    src='https://shots.wayl.one/shot/?url=https://openweathermap.org/&height=450&width=800&scaled_width=800&scaled_height=450&selectors='
    alt='screenshot of https://openweathermap.org/'
    height='450'
    width='800'
/>
</a>

Now using openweathermap, we can get the feels like temperature, by latitude
and longitude.

```python
async def get_weather(lat_long):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.openweathermap.org/data/2.5/weather?units=imperial&lat={lat_long['latitude']}&lon={lat_long['longitude']}&appid={config.open_weather_api_key}"
        )
        return response.json()
```

## Where are you??

Since no one is going to know their current latitude and longitude we need a
way to look this up for it to actually be useful. For this I leaned on
[https://ipwhois.io/](https://ipwhois.io/){.hoverlink}

<a href='https://ipwhois.io/' >
<img
    src='https://shots.wayl.one/shot/?url=https://ipwhois.io/&height=450&width=800&scaled_width=800&scaled_height=450&selectors='
    alt='screenshot of https://ipwhois.io/'
    height='450'
    width='800'
/>
</a>

``` python
async def get_lat_long(ip_address):
    if ip_address is None:
        ip_address = "140.177.140.75"
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://ipwho.is/{ip_address}")
        return response.json()
```

## Decision Tree

For this I punted over to chatGPT to see what it came up with.

``` prompt
I am working on a web app to tell kids if its ok to play outside.  It is
targeted towards kids living in the  midwest united states.   I have the feels
like temperature already.  Set some values for the temperature

too cold,
no longer than 15 minutes,
coats required,
no longer than 15 minutes,
too hot
```

What it came up with wasn't a terrible starting point, but its values
essentially said kids cant play in the snow.

``` python
def determine_play_condition(feels_like_temperature):
    if feels_like_temperature < 20:
        return "It's too cold for extended play. Stay indoors and keep warm!"
    elif 20 <= feels_like_temperature <= 32:
        return "Perfect weather for snow play! Enjoy the winter wonderland!"
    elif 32 < feels_like_temperature <= 40:
        return "Coats and winter gear required for outdoor play. Stay cozy!"
    elif 40 < feels_like_temperature <= 50:
        return "You can play in the snow, but limit your time. It's getting warmer!"
    else:
        return "It's too warm for snow play. Find other fun activities indoors!"

# Example usage:
feels_like_temp = 25  # Replace with the actual feels like temperature
message = determine_play_condition(feels_like_temp)
print(message)
```

## Some Massaging Later

My wife sent me over this image from
[Tinkergarten](https://tinkergarten.com/pages/weather-watch), which is a chart
made by the Iowa Department of Public Health.  I used it as a guide to set some
values, and added some conditions based on visibility and air quality index
(aqi), which we have become all too familiar with over the past year with all
the forest fires out Western US causing our lungs issues here in the Midwest.

<img
    src='https://d2gesac5hma2c2.cloudfront.net/uploads/attachment/file/84/weatherwatch2.png'
    alt='This chart was produced by the Iowa Department of Public Health, Healthy Child Care Iowa through federal grant (MCJ19T029 & MCJ19KCC7) funds from the US Department of Health & Human Services, Health Resources & Services Administration, Maternal & Child Health Bureau. Wind-Chill and Heat Index information is from the National Weather Service. A search led us to the chart as posted on daycare.com'
    style="width: 100%; max-width: 800px;"
/>

> (aqi) which we have become all too familiar with over the past year with all
> the forest fires out Western US

``` python
def determine_play_condition(weather, aqi=0):
    play_condition = PlayCondition()

    feels_like_temperature = weather["main"]["feels_like"]
    visibility = weather["visibility"]

    play_condition.message += hours_till_sunset(weather)

    if "after" in play_condition.message:
        play_condition.color = "bg-red-500"

    if visibility < 1000:
        play_condition.message += "It's too foggy. Find better activities inside!"
        play_condition.color = "bg-red-500"

    if aqi > 150:
        play_condition.message += "It's too polluted. Find better activities inside!"
        play_condition.color = "bg-red-500"
    elif aqi > 100:
        play_condition.message += "limit your time outside due to the poor air quality"
        play_condition.color = "bg-yellow-500"
    elif aqi > 50:
        play_condition.message += "Check the air quality outside at your discression."
        play_condition.color = "bg-yellow-500"
    else:
        play_condition.message += ""

    if feels_like_temperature < 10:
        play_condition.message += "It's too cold. Stay indoors and keep warm!"
        play_condition.color = "bg-red-500"
    elif feels_like_temperature < 30:
        play_condition.message += "You can play outside, but limit your time!"
        play_condition.color = "bg-yellow-500"
    elif feels_like_temperature < 40:
        play_condition.message += (
            "Coats and winter gear required for outdoor play. Stay cozy!"
        )
    elif feels_like_temperature < 50:
        play_condition.message += "Grab a warm jacket and enjoy your time outside!"
    elif feels_like_temperature < 60:
        play_condition.message += "Grab some long sleeves and enjoy your time outside!"
    elif feels_like_temperature > 90:
        play_condition.message += (
            "You can play outside, but limit your time in this heat!"
        )
        play_condition.color = "bg-yellow-500"
    elif feels_like_temperature > 109:
        play_condition.message += (
            "It's too hot for outdoor play. Find cooler activities indoors!"
        )
        play_condition.color = "bg-red-500"
    else:
        play_condition.message += "Enjoy your time outside!"
    return play_condition
```

## Pulling the data together

Since I will be needing all of the data together upon every request I put
together one `get_data` function to return a dict of all of the data.

!!! note forecast
     I pulled the forecast endpoint from openweathermap as well, it looks like a
     stripped down version of the regular weather endpoint, but every few hours
     over the course of the next 5 days.

``` python
async def get_data(request: Request):
    user_ip = request.headers.get("CF-Connecting-IP")
    lat_long = await get_lat_long(user_ip)
    weather = await get_weather(lat_long)
    forecast = await get_forecast(lat_long)
    air_quality = await get_air_quality(lat_long)
    weather["play_condition"] = determine_play_condition(
        weather,
        air_quality["list"][0]["main"]["aqi"],
    )

    forecast = [
        {"play_condition": determine_play_condition(x), **x}
        for x in forecast
        if datetime.fromtimestamp(x["dt"]).hour >= 6
        and datetime.fromtimestamp(x["dt"]).hour <= 21
    ]

    return {
        "request.client": request.client,
        "request.client.host": request.client.host,
        "user_ip": user_ip,
        "lat_long": lat_long,
        "weather": weather,
        "forecast": forecast,
        "air_quality": air_quality,
        "sunset": weather["sys"]["sunset"],
    }
```

## FastAPI

Fastapi here is a great framework, it uses pydantic to validate the data
returned from the api, has a great dependency management system.

I am going to use none of that, all I need is one TemplateResponse using jinja.
For good measure, I'll toss in a `/metadata` route that returns the data.

``` python
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
@no_cache
async def get_home(request: Request):
    data = await get_data(request)
    return config.templates.TemplateResponse("index.html", {"request": request, **data})

@app.get("/metadata")
async def root(
    request: Request,
):
    return await get_data(request)
```

## No Cache Header

I had some issues with cloudflare caching me and not letting me hit the api
everytime.  I've ran into this several times in the past, so I went to the
cloudflare dashboard, manually busted the cache for the home route and popped a
`no_cache` decorator on the `get_home` route.

``` python
def no_cache(func):
    not_cached_routes.append(f"{func.__module__}.{func.__name__}")

    @wraps(func)
    async def wrapper(*args, request: Request, **kwargs):
        # my_header will be now available in decorator
        if "request" in signature(func).parameters:
            kwargs["request"] = request

        if inspect.iscoroutinefunction(func):
            response = await func(*args, **kwargs)
        else:
            response = func(*args, **kwargs)

        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response

    return wrapper

@app.get("/")
@no_cache
async def get_home(request: Request):
    data = await get_data(request)
    return config.templates.TemplateResponse("index.html", {"request": request, **data})
```

This solved my caching issues.

## Templates

I used jinja for templating its built right into FastAPI.

``` python
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
```

This will get you by for quite awhile, and I probably could deal with templates
working just like this for a one day build, but I have some nice feautures that
I like from other projects, and at least one specific to just this project.
Once they are in my config object, I use them like so.

!!! Note
     The `request` parameter is a requirement for all templates.

``` python
@app.get("/")
@no_cache
async def get_home(request: Request):
    data = await get_data(request)
    return config.templates.TemplateResponse("index.html", {"request": request, **data})
```

### Globals

I need a nice way to convert the openweathermap timestamps to human readable values.

``` python
from datetime import datetime

templates.env.globals["datetime"] = datetime
```

Then in jinja I can format the `weather.dt` variable like so.

``` python
{{ datetime.fromtimestamp(weather.dt).strftime(format = '%A') }}
```

### Putting it together

I put a get_templates function in my config, and the config object is passed
the results as config.  Again I copy pasted a function `https_url_for` from
my other project so that I can use `url_for` in my templates and it work on
both localhost and production.

``` python
import os
from datetime import datetime
from datetime import timezone

from fastapi.templating import Jinja2Templates
from rich.console import Console

console = Console()


@pass_context
def https_url_for(context: dict, name: str, **path_params: Any) -> str:
    request = context["request"]
    http_url = request.url_for(name, **path_params)
    return str(http_url).replace("http", "https", 1)

def get_templates(config: BaseSettings) -> Jinja2Templates:
    templates = Jinja2Templates(directory="templates")
    templates.env.filters["quote_plus"] = lambda u: quote_plus(str(u))
    templates.env.filters["timestamp"] = lambda u: datetime.fromtimestamp(
        u, tz=timezone.utc
    ).strftime("%B %d, %Y")
    templates.env.globals["https_url_for"] = https_url_for
    templates.env.globals["config"] = config
    templates.env.globals["datetime"] = datetime
    templates.env.globals["len"] = len
    templates.env.globals["int"] = int
    console.print(f'Using environment: {os.environ.get("ENV")}')

    if os.environ.get("ENV") in ["dev", "qa", "prod"]:
        templates.env.globals["url_for"] = https_url_for
        console.print("Using HTTPS")
    else:
        console.print("Using HTTP")

    return templates
```

## Styles

I've been all in on tailwind lately.  I was a long holdout. I used Sass back in
2016/2017 when I was first getting into webdev, then went many years just
straight vanilla.  Tailwind just has some really well thought out color and
rythm that makes it easy.  I have also really been appreciating the locality of
behavior part of it.  I can make components in jinja with everything they need.

I set up my `tailwind.config.js` like so.  It includes the typography plugin
and some extra box shadows that are centered.

``` js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["templates/**/*.html"],
  plugins: [require("@tailwindcss/typography")],
  theme: {
    extend: {
      boxShadow: {
        xlc: "0 0 60px 15px rgba(0, 0, 0, 0.3)",
        lgc: "0 0 20px 0px rgba(0, 0, 0, 0.3)",
      },

    },
  },
};
```

For my `tailwind/app.css` I set the background color of the page dark, text
white, and make the scrollbar not default.

``` css
@tailwind base;
@tailwind components;
@tailwind utilities;

html {
  scroll-behavior: smooth;
  @apply bg-zinc-800 text-white autofill:bg-yellow-500;
}

::-webkit-scrollbar {
  @apply h-4 w-4;
}

::-webkit-scrollbar-track {
  @apply rounded-full bg-zinc-900;
}

body::-webkit-scrollbar-track {
  @apply rounded-full bg-pink-600;
}

::-webkit-scrollbar-thumb {
  @apply rounded-full bg-zinc-600 hover:bg-zinc-500;
}

body::-webkit-scrollbar-thumb {
  @apply rounded-full bg-cyan-500 hover:bg-cyan-400;
}
```

### Compiling tailwind

I run tailwind using npx after first installing the typography plugin.  This
will use my `tailwind.config.js` file, and the `tailwind/app.css` file as
input, and output to `static/app.css`.

!!! Note
     --watch will watch for changes, and automatically recompile as you make changes to any templates.

``` bash
# install the typography plugin
npm i @tailwindcss/typography
# compile the css
npx tailwindcss --input tailwind/app.css --output static/app.css --watch
```

## Deployment

## Docker

## CI

## K8s

## TEXT BASED

* [play-outside](https://play-outside.wayl.one/)
