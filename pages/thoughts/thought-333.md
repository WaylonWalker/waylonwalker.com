---
title: '💭 Background Tasks - FastAPI'
date: 2024-07-03T16:17:45
templateKey: link
link: https://fastapi.tiangolo.com/tutorial/background-tasks/
tags:
  - fastapi
  - webdev
published: true

---

> fastapi comes with a concept of background tasks which are functions that can be ran in the background after a function has been ran.  This is handy for longer running functions that may take some time and you want to have fast response times.

Here is an example from the docs

``` python
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
```

[Original thought](https://fastapi.tiangolo.com/tutorial/background-tasks/)
