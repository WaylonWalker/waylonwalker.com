---
date: 2023-12-14 07:56:27
templateKey: til
title: Hiding Form input During htmx Request
published: true
tags:
  - webdev
jinja: false
---

I am working on fokais.com's signup page, and I want to hide the form input during
an htmx request. I was seeing some issues where I was able to prevent spamming
the submit button, but was still able to get one extra hit on it.

It also felt like nothing was happening while sending the email to the user for
verification. Now I get the form to disappear and a spinner to show during the
request.

## HTML

Let's start off with the form. It uses htmx to submit a post request to the
`post_request` route. Note that there is a spinner in the `post_request` with the
`htmx-indicator` class.

The intent is to hide the spinner until the request is running, and hide all of
the form input during the request.

```html
<form
  id="signup-form"
  hx-swap-oob="outerHTML"
  class="m-4 mx-auto mb-6 flex w-80 flex-col rounded-lg b p-4 shadow-xlc shadow-cyan-500/10"
  method="POST"
  action="{{ url_for('post_signup') }}"
  hx-post="{{ url_for('post_signup') }}"
>
  <input
    class="mx-8 mt-6 mb-4 border border-black bg-zinc-900 p-1 text-center focus:bg-zinc-800"
    type="text"
    value="{{ full_name }}"
    name="full_name"
    placeholder="Full Name"
  />
  {% if full_name_error %}
  <label class="-mt-6 mb-6 mx-8 text-red-500 p-1 text-center">
    {{ full_name_error }}
  </label>
  {% endif %}
  <input
    class="mx-8 mb-4 border border-black bg-zinc-900 p-1 text-center focus:bg-zinc-800"
    type="text"
    value="{{ username }}"
    name="username"
    placeholder="username"
  />
  {% if username_error %}
  <label class="-mt-6 mb-6 mx-8 text-red-500 p-1 text-center">
    {{ username_error }}
  </label>
  {% endif %}
  <input
    class="mx-8 mb-4 border border-black bg-zinc-900 p-1 text-center focus:bg-zinc-800"
    type="email"
    name="email"
    value="{{ email }}"
    placeholder="email"
  />
  {% if email_error %}
  <label class="-mt-6 mb-6 mx-8 text-red-500 p-1 text-center">
    {{ email_error }}
  </label>
  {% endif %}
  <input
    class="mx-auto w-32 mb-4 border border-black bg-purple-900 p-1 text-center focus:bg-zinc-800"
    type="submit"
    value="sign up"
  />
  <div role="status" class="mx-auto htmx-indicator">
    <svg
      class="mx-auto animate-spin h-5 w-5 text-white"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
    >
      <circle
        class="opacity-25"
        cx="12"
        cy="12"
        r="10"
        stroke="currentColor"
        stroke-width="4"
      ></circle>
      <path
        class="opacity-75"
        fill="currentColor"
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
      ></path>
    </svg>
    <p>Signing up...</p>
  </div>
</form>
```

Yes this is styled using tailwindcss.

https://waylonwalker.com/still-loving-tailwind/

## CSS

Let's take a look at how we achieve switching between only spinner an only form
inputs using css.

```css
.htmx-indicator {
  @apply hidden;
  opacity: 0;
  transition: opacity 500ms ease-in;
}
.htmx-request button,
.htmx-request input[type="submit"],
.htmx-request input,
.htmx-request label {
  @apply hidden;
}
.htmx-request .htmx-indicator {
  opacity: 1;
  @apply block;
}
.htmx-request.htmx-indicator {
  opacity: 1;
  @apply block;
}
```

## Final Result

Here is the final result of me signing up for a new account in fokais.

![Final Result](https://images.waylonwalker.com/fokais-signup.mp4)
