---
date: 2026-10-23
title: Homelab network policies, one namespace at a time
description: >-
  Retiring unused cluster tools, mapping service calls, and testing eleven narrow
  Kubernetes network policies.
published: true
draft: false
tags:
  - homelab
  - kubernetes
  - security
template: post
authors:
  - id: codex
    role: draft author
---

Unused services and unknown dependencies shaped this homelab security pass.
Each new network policy needed an answer to one question: which services must
this workload reach to keep working?

This pass started with [issue #174][issue] in the GitOps repo.
The goal was a small, reversible change: remove unused access, map known
connections, then isolate one public workload at a time.  The cluster stayed
under Argo CD control throughout the rollout.

## Turn things off

The Forgejo runner was unused, but its Docker-in-Docker container ran with
privileged access.  A [GitOps change][runner-pr]
set its Deployment to zero replicas.  The runner pod disappeared after Argo CD
synced.  Its persistent data, registration Secret, and configuration remain,
so the runner can be restored if those jobs are needed again.

Headlamp was also unused.  Its chart had a public Ingress and a cluster-admin
binding.  A [second change][headlamp-pr]
set it to zero replicas and removed the chart's Ingress and binding.  An older
untracked binding and ServiceAccount were checked and removed separately.
Headlamp's Service remains, but there is no running backend or public route.

## Draw the arrows

A policy needs a list of required calls.  The [dependency graph][graph]
started with connections in Kubernetes manifests, Helm values, and app source
under `~/git`.  It now records 27 public-safe edges with a source workload,
destination, port, reason, evidence path, and confidence level.  A separate
local map holds eight connections found in private app repositories.

Some arrows were easy to miss.  A scheduled cleanup job calls the Shot API
only at intervals.  Brainrot polls external feeds and calls other services.
The forward-auth request for protected routes comes from Traefik to the auth
service, not from each protected app.  A short traffic sample would miss some
of these paths.

The graph is still incomplete.  Most entries show what configuration or code
*can* do.  They do not prove that a call happened during the observation
window.  Backups, upgrades, webhooks, and failure paths need their own checks.

## Start small

The first policy selected only [`whoami`][whoami-pr].
It allows the observed Traefik pods to reach the app and allows DNS egress to
CoreDNS.  Other egress is denied.  A temporary test pod selected by the policy
resolved DNS but could not connect to another test pod.  The public routes
still returned HTTP 200 after Argo CD synced.

The next policy used the same narrow shape for
[`librespeed`][librespeed-pr].
Its deployed pod had no configured external database or IP information API.
Both public hosts and the checked backend routes still returned HTTP 200.
A temporary selected pod again resolved DNS while another pod connection was
blocked.  The test pods were removed after verification.

The third policy isolated the static
[`themes.waylonwalker.com` site][themes-pr].  Its nginx pod serves files from
a mounted webroot and has no configured upstream proxy.  Traefik can still
reach the site, and the pod can still resolve DNS.  A selected test pod could
not reach another pod.  The public page returned HTTP 200 after the rollout.

The fourth policy covers the public [Lantern Table app][lantern-pr].  It allows
Traefik to reach the app but leaves app egress open.  Lantern Table calls
Valkey and has other outbound auth and AI paths.  The public HTTP routes stayed
healthy, and a direct request from another pod was refused.  A WebSocket
upgrade returned HTTP 101; a complete room session remains untested.

The fifth policy covers the public [Shot API][shot-pr].  It allows Traefik and
the queue cleanup job to reach the API on TCP 5000.  A pod with the cleanup
label received HTTP 200.  An unrelated pod could not connect.  The public route
also returned HTTP 200.  The API and worker egress rules remain open because
they use Redis, MinIO, telemetry, and external services.
The first scheduled cleanup run had two connection failures, then completed on
its third pod attempt.  The successful request returned zero queued, completed,
or failed items.  The next scheduled run needs observation for more retries.

The sixth policy narrows [OpenGraph ingress][opengraph-chart-pr].  Its old rule
allowed every pod in `kube-system`.  The chart now allows only the live Traefik
pods on TCP 8000.  The public route and an analysis request returned HTTP 200.
An unrelated pod could not connect.  Brainrot calls the public OpenGraph host,
so that request still enters through Traefik.

The seventh policy narrows [Family Dashboard ingress][family-dashboard-pr]
from the `notify-bridge` namespace.  The dashboard accepts event requests from
`notify-bridge-app`; its cleanup job only removes old media.  The policy now
allows the app pods on TCP 8080.  A matching pod reached the service and
received HTTP 200.  An unrelated pod in the same namespace could not connect.
The public dashboard hosts still returned HTTP 200.  This change only narrows
ingress.  The dashboard has other service dependencies that need separate
review before egress rules.

The eighth policy narrows the [Avatars service][avatars-policy-pr].  The app
used a chart from an archived GitHub mirror, so its Argo source now uses the
active Forgejo chart.  A render comparison showed that only its NetworkPolicy
changed.  The policy allows the live Traefik pods on TCP 8000.  The public
route returned HTTP 200, and an unrelated pod was blocked.

The ninth and tenth policies narrow [Models][models-pr] and Models Dev ingress
on TCP 8080.
Both routes use Traefik ForwardAuth, so public requests without a session still
return HTTP 302.  The policies now select only Traefik pods.  Existing DNS and
PostgreSQL egress rules remain.  The source scan found no direct in-cluster
clients for either service.

The Models sync also exposed a stale database size in GitOps.  The manifest
asked for 5 GiB while the three live database volumes were 40 GiB.  CloudNativePG
blocked the shrink.  [A small follow-up][models-storage-pr] restored the 40 GiB
request before Argo completed the sync.

The next Shot cleanup job also had connection refusals at startup.  [A follow-up
change][shot-retry-pr] makes curl retry that error.  The next scheduled run
will show whether this removes the job's initial failures.

The eleventh policy narrows [Linker ingress][linker-policy-pr] to Traefik on
TCP 8000.  Its public health and readiness paths still return HTTP 200, and an
unrelated pod cannot connect.  The root route still returns HTTP 500 from a
Jinja error in the app.  That error is separate from the NetworkPolicy.

Those checks show that the rules worked for the paths tested.  A full speed
test and a long soak remain.  Connected apps need their own traffic evidence
before outbound rules are added.

## Remove idle tokens

The `whoami`, LibreSpeed, and themes pods also received projected Kubernetes
API tokens through their default ServiceAccounts.  None of those workloads
uses the Kubernetes API.  Three small GitOps changes removed the token mounts
from [whoami][whoami-token-pr], [LibreSpeed][librespeed-token-pr], and
[themes][themes-token-pr].  Each replacement pod came up ready without the
token volume, and its public routes still worked.

## What comes next

The 13:45 Shot cleanup will test the connection retries.  The previous Job
failed after seven connection refusals, so Argo marks `shots` Degraded.  The
app also has a cache volume pending deletion.  After the run, review any
remaining broad ingress rules and the Linker app error.

The [issue remains open][issue]
for that work.  The eleven policies reduced easy lateral paths.  They did not
establish that every required connection is documented or that the whole
cluster is isolated.

[issue]: https://github.com/WaylonWalker/homelab-argo/issues/174
[runner-pr]: https://github.com/WaylonWalker/homelab-argo/pull/175
[headlamp-pr]: https://github.com/WaylonWalker/homelab-argo/pull/176
[whoami-pr]: https://github.com/WaylonWalker/homelab-argo/pull/177
[librespeed-pr]: https://github.com/WaylonWalker/homelab-argo/pull/180
[themes-pr]: https://github.com/WaylonWalker/homelab-argo/pull/181
[lantern-pr]: https://github.com/WaylonWalker/homelab-argo/pull/187
[shot-pr]: https://github.com/WaylonWalker/homelab-argo/pull/191
[opengraph-chart-pr]: https://git.waylonwalker.com/waylon/k8s-basic/pulls/1
[family-dashboard-pr]: https://git.waylonwalker.com/waylon/family-dashboard/pulls/1
[avatars-policy-pr]: https://github.com/WaylonWalker/homelab-argo/pull/193
[models-pr]: https://github.com/WaylonWalker/homelab-argo/pull/195
[models-storage-pr]: https://github.com/WaylonWalker/homelab-argo/pull/196
[shot-retry-pr]: https://github.com/WaylonWalker/homelab-argo/pull/197
[linker-policy-pr]: https://github.com/WaylonWalker/homelab-argo/pull/198
[whoami-token-pr]: https://github.com/WaylonWalker/homelab-argo/pull/182
[librespeed-token-pr]: https://github.com/WaylonWalker/homelab-argo/pull/183
[themes-token-pr]: https://github.com/WaylonWalker/homelab-argo/pull/185
[graph]: https://github.com/WaylonWalker/homelab-argo/blob/main/docs/security/issue-174-dependencies.yaml
