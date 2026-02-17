---
title: '💭 fastapi decorators'
date: 2024-03-26T13:50:46
templateKey: link
link: None
tags:
  - webdev
  - fastapi
published: true

---

> I've been using these decorators to modify the behavior of specific routes.  It will do things like 404 admin only routes in a way that looks just like fastapi's default, or only allow certain roles into the route, or redirect unauthenticated users to login.

After listening to yesterday's syntaxfm I'm now really thinking about middleware and the benefits it might have.  middleware would make it easy to apply things like admin to an entire admin router, so you wont forget it on any one admin route.  It will look cleaner as the admin checker is only applied once per router, not once per route.

``` python 
import inspect
import time
from functools import wraps
from inspect import signature

from fastapi import Request
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from starlette import status

from fokais.config import get_config
from fokais.models.user import Role

config = get_config()


admin_routes = []
authenticated_routes = []
not_cached_routes = []
cached_routes = []


def not_found(request):
    hx_request_header = request.headers.get("hx-request")
    user_agent = request.headers.get("user-agent", "").lower()

    if "mozilla" in user_agent or "webkit" in user_agent or hx_request_header:
        return config.templates.TemplateResponse(
            "error.html", {"status_code": 404, "detail": "Not Found", "request": request}, status_code=404
        )
    else:
        return JSONResponse(
            content={
                "status_code": 404,
                "detail": "Not Found",
            },
            status_code=404,
        )


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


def cache(max_age=86400):
    def inner_wrapper(func):
        cached_routes.append(f"{func.__module__}.{func.__name__}")

        @wraps(func)
        async def wrapper(*args, request: Request, **kwargs):
            if "request" in signature(func).parameters:
                kwargs["request"] = request
            if inspect.iscoroutinefunction(func):
                response = await func(*args, **kwargs)
            else:
                response = func(*args, **kwargs)
            response.headers[
                "Cache-Control"
            ] = f"public, max-age={max_age}, stale-while-revalidate=31536000, stale-if-error=31536000"
            response.headers["Expires"] = f"{int(time.time()) + max_age}"

            return response

        return wrapper

    return inner_wrapper


def admin_only(func):
    admin_routes.append(f"{func.__module__}.{func.__name__}")

    @wraps(func)
    async def wrapper(*args, request: Request, **kwargs):
        if request.state.user is None:
            return not_found(request)
        if request.state.user.role != Role.admin:
            return not_found(request)
        if "request" in signature(func).parameters:
            kwargs["request"] = request
        if inspect.iscoroutinefunction(func):
            response = await func(*args, **kwargs)
        else:
            response = func(*args, **kwargs)
        return response

    return wrapper


def authenticated(roles=[Role.user, Role.admin], redirect_to="get_login"):
    def inner_wrapper(func):
        authenticated_routes.append(f"{func.__module__}.{func.__name__}")

        @wraps(func)
        async def wrapper(*args, request: Request, **kwargs):
            if request.state.user is None:
                return RedirectResponse(
                    url=request.url_for(redirect_to, source=request.url), status_code=status.HTTP_302_FOUND
                )
            if request.state.user.role not in roles:
                return not_found(request)

            if "request" in signature(func).parameters:
                kwargs["request"] = request
            if inspect.iscoroutinefunction(func):
                response = await func(*args, **kwargs)
            else:
                response = func(*args, **kwargs)
            return response

        return wrapper

    return inner_wrapper


default_data = {}


def defaults(data=default_data):
    def inner_wrapper(func):
        default_data[f"{func.__module__}.{func.__name__}"] = data

        @wraps(func)
        async def wrapper(*args, request: Request, **kwargs):
            if "request" in signature(func).parameters:
                kwargs["request"] = request
            if inspect.iscoroutinefunction(func):
                response = await func(*args, **kwargs)
            else:
                response = func(*args, **kwargs)
            return response

        return wrapper

    return inner_wrapper
```

[Original thought](None)
