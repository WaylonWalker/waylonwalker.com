---
date: 2023-12-17 20:09:03
templateKey: til
title: cli auth
published: true
tags:
  - bash
---

Authentication from cli tools can be a bit of a bear, and I have to look it up
every time. This is my reference guide for future me to remember how to easily
do it.

I set up a fastapi server running on port 8000, it uses a basic auth with
`waylonwalker` as the username and `asdf` as the password. The server follows
along with what comes out of the docs. I have it setup to take basic auth,
form username and password, or a bearer token for authentication.

## curl

The og of command line url tools.

```bash
# basic auth
curl -u 'waylonwalker:asdf' -X POST localhost:8000/token
# basic auth with password prompt
curl -u 'waylonwalker' -X POST localhost:8000/token
# token
curl -H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3YXlsb253YWxrZXIiLCJleHAiOjE3MDI5NTI2MDJ9.GeYNt7DNal6LTiPoavJnqypaMt4vYeriXdq5lqu1ILg' -X POST localhost:8000/token
```

## wget

My go to if I want the result to go into a file.

```bash
# basic auth
wget -q -O - --auth-no-challenge --http-user=waylonwalker --http-password=asdf --post-data '' localhost:8000/token

# token
wget -q -O - --header="Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3YXlsb253YWxrZXIiLCJleHAiOjE3MDI5NTI2MDJ9.GeYNt7DNal6LTiPoavJnqypaMt4vYeriXdq5lqu1ILg" -O - --post-data '' localhost:8000/token
```

## httpx

An http client written in python, primarilty used with the python api, but has a nice cli.

```bash
# install
python3 -m pip install httpx

# basic auth
httpx -m POST --auth waylonwalker asdf http://localhost:8000/token

# basic auth with password prompt
httpx -m POST --auth waylonwalker - http://localhost:8000/token

# token
httpx -m POST --headers="Authorization" "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3YXlsb253YWxrZXIiLCJleHAiOjE3MDI5NTI2MDJ9.GeYNt7DNal6LTiPoavJnqypaMt4vYeriXdq5lqu1ILg" http://localhost:8000/token
```

## httpie

A modern http client written in python.

```bash
# install
python3 -m pip install httpie

# basic auth
http POST localhost:8000/token -a waylonwalker:asdf

# basic auth with password prompt
http POST localhost:8000/token -a waylonwalker

# token
http POST localhost:8000/token -A bearer -a eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3YXlsb253YWxrZXIiLCJleHAiOjE3MDI5NTI2MDJ9.GeYNt7DNal6LTiPoavJnqypaMt4vYeriXdq5lqu1ILg
```

## httpie with plugin

```bash
# install
python3 -m pip install httpie-credential-store
# usage
http POST localhost:8000/token -A creds
```

## httpie prompt

`http-prompt` comes from the httpie org, and has an interactive cli interface
into apis. You can even specify a spec file to autocomplete on api methods.

```bash
http-prompt localhost:8000 --auth waylonwalker:asdf --spec openapi.json
```
