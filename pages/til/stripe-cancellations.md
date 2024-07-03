---
date: 2023-12-09 22:29:15
templateKey: til
title: Stripe Cancellations in FastAPI and SQLModel
published: true
tags:
  - python
---

Today I am working on fokais.com, trying to get to a point where I can launch
by workig through stripe integrations. This is my first time using stripe, so
there has been quite a bit to learn, and I am probably building in more than I
need to before launching, but I am learning, and not in a rush to launch.

I am building the fokais backent in python primarilyt with fastapi and sqlmodel
on sqlite. My billing integration is going to be all Stripe.

## Stripe Subscription Cancellations Docs

Here is a link to the stripe docs for your refrence, especially if you want to
see how to cancel subscriptions in other languages. They include code samples
for many popular languages.

<a href="https://stripe.com/docs/billing/subscriptions/cancel#canceling" title="Cancel subscriptions | Stripe Documentation">
    <img class="object-fit aspect-[800/450] w-full rounded-lg border border-black bg-neutral-900 shadow-lg shadow-neutral-900" src="https://shots.wayl.one/shot/?url=https%3A%2F%2Fstripe.com%2Fdocs%2Fbilling%2Fsubscriptions%2Fcancel%23canceling&amp;height=450&amp;width=800&amp;scaled_width=800&amp;scaled_height=450&amp;selectors=" alt="Cancel subscriptions | Stripe Documentation" title="Cancel subscriptions | Stripe Documentation">
</a>

## User Model

This is the part of the user model that includes the cancel and reactivate
methods. It pretty much follows the stripe guide.

```python
class UserBase(SQLModel, table=False):  # type: ignore[call-arg]
    username: str = Field(unique=True)
    full_name: str
    email: str
    email_verified: bool = False
    disabled: bool = False
    signup_date: Optional[datetime] = Field(default_factory=datetime.utcnow)
    stripe_customer_id: Optional[str]

    def cancel_subscription(self):
        for subscription in self.active_subscriptions:
            stripe.Subscription.modify(
                subscription.id,
                cancel_at_period_end=True,
            )
        self.refresh()

    def reactivate_subscription(self):
        for subscription in self.active_subscriptions:
            stripe.Subscription.modify(
                subscription.id,
                cancel_at_period_end=False,
            )
        self.refresh()
```

## Cancellations api

Here is the cancellations api. I created an are you sure form that I can link
to from the accounts page with a normal anchor tag. Note that I am doing a
`POST` request to do the cancellation from a form. I want this to work for any
user whether there is js or not. This is an operation that will change the
users data, and I want to make sure that it avoids all browser and cdn caching.
As a scrappy startup we are running light on infrastructure and are caching
hard at the CDN to avoid excessive server hits.

!!! Note
     I am doing a `POST` request to do the cancellation from a form.

```python
@pricing_router.get("/cancel")
@pricing_router.get("/cancel/")
def get_cancel(
    request: Request,
    current_user: Annotated[User, Depends(get_current_user_if_logged_in)],
):
    return config.templates.TemplateResponse(
        "cancel.html",
        {
            "request": request,
            "prices": products.prices,
            "products": products.products,
            "current_user": current_user,
        },
    )


@pricing_router.post("/cancel")
@pricing_router.post("/cancel/")
def post_cancel(
    request: Request,
    current_user: Annotated[User, Depends(get_current_user_if_logged_in)],
):
    current_user.cancel_subscription()
    return HTMLResponse('<p id="cancel" hx-swap-oob="outerHTML">Your Subscription has been Cancelled</p>')

```

## Reactivations

Reactivating accounts looks just about the same as cancelling, only flippng `True` to `False`.

```python

@pricing_router.get("/reactivate")
@pricing_router.get("/reactivate/")
def get_reactivate(
    request: Request,
    current_user: Annotated[User, Depends(get_current_user_if_logged_in)],
):
    return config.templates.TemplateResponse(
        "reactivate.html",
        {
            "request": request,
            "prices": products.prices,
            "products": products.products,
            "current_user": current_user,
        },
    )


@pricing_router.post("/reactivate")
@pricing_router.post("/reactivate/")
def post_reactivate(
    request: Request,
    current_user: Annotated[User, Depends(get_current_user_if_logged_in)],
):
    current_user.reactivate_subscription()
    return HTMLResponse('<p id="reactivate" hx-swap-oob="outerHTML">Your Subscription has been reactivated</p>')

```

## Full User Model

This is the full user model, completely subject to change in the future, but it
includes the cancel and reactivate methods.

```python
class UserBase(SQLModel, table=False):  # type: ignore[call-arg]
    username: str = Field(unique=True)
    full_name: str
    email: str
    email_verified: bool = False
    disabled: bool = False
    signup_date: Optional[datetime] = Field(default_factory=datetime.utcnow)
    stripe_customer_id: Optional[str]

    @property
    def session(self):
        return next(get_session())

    @classmethod
    def get_by_id(cls, id):
        return next(get_session()).get(cls, id)

    def refresh(self):
        cache.set(f"active_subscriptions_{self.id}", None, 3600)
        cache.set(f"active_products_{self.id}", None, 3600)

    def get_checkout_sessions(self):
        return [
            stripe.checkout.Session.retrieve(s.stripe_checkout_session_id)
            for s in self.session.exec(select(CheckoutSession).where(CheckoutSession.user_id == self.id)).all()
            if s.stripe_checkout_session_id is not None
        ]

    def get_active_subscriptions(self):
        subscriptions = [
            s.subscription
            for s in [
                stripe.checkout.Session.retrieve(s.stripe_checkout_session_id)
                for s in self.session.exec(select(CheckoutSession).where(CheckoutSession.user_id == self.id)).all()
                if s.stripe_checkout_session_id is not None
            ]
            if s.status == "complete"
        ]
        active_subscriptions = [stripe.Subscription.retrieve(subscription) for subscription in subscriptions]
        return active_subscriptions

    def has_active_subscription(self):
        return len(self.active_subscriptions) > 0

    @property
    def active_subscriptions(self):
        active_subscriptions = cache.get(f"active_subscriptions_{self.id}")
        if active_subscriptions is not None:
            return active_subscriptions
        active_subscriptions = self.get_active_subscriptions()
        cache.set(f"active_subscriptions_{self.id}", active_subscriptions, 3600)

        return active_subscriptions

    @property
    def active_plans(self):
        subscriptions = self.active_subscriptions
        plans = [subscription.plan for subscription in subscriptions]
        return plans

    @property
    def subscription_to_plan(self):
        subscriptions = self.active_subscriptions
        plans = {subscription.id: subscription.plan.id for subscription in subscriptions}
        return plans

    @property
    def plan_to_subscription(self):
        plans = {v: k for k, v in self.subscription_to_plan.items()}

        return plans

    def get_active_products(self):
        plans = self.active_plans
        products = [stripe.Product.retrieve(plan.product) for plan in plans]
        return products

    @property
    def plan_to_product(self):
        plans = self.active_plans
        products = {plan.id: stripe.Product.retrieve(plan.product).id for plan in plans}
        return products

    @property
    def prodct_to_plan(self):
        plans = self.active_plans
        products = {stripe.Product.retrieve(plan.product).id: plan.id for plan in plans}
        return products

    @property
    def active_products(self):
        products = cache.get(f"active_products_{self.id}")
        if products is not None:
            return products
        products = self.get_active_products()
        cache.set(f"active_products_{self.id}", products, 3600)

        return products

    @property
    def best_active_subscription(self):
        subscriptions = self.active_subscriptions
        return subscriptions[0]

    @property
    def best_active_product(self):
        products = self.active_products
        products.sort(key=lambda p: p.metadata.get('level', 0))
        return products[0]

    @property
    def best_active_subscription(self):
        subscription_id = self.plan_to_subscription[self.prodct_to_plan[self.best_active_product.id]]
        return stripe.Subscription.retrieve(subscription_id)

    @property
    def config(self):
        product = self.best_active_product
        return product.metadata

    def subscription_status(self):
        subscriptions = self.active_subscriptions()

    def cancel_subscription(self):
        for subscription in self.active_subscriptions:
            stripe.Subscription.modify(
                subscription.id,
                cancel_at_period_end=True,
            )
        self.refresh()

    def reactivate_subscription(self):
        for subscription in self.active_subscriptions:
            stripe.Subscription.modify(
                subscription.id,
                cancel_at_period_end=False,
            )
        self.refresh()
```
