---
date: 2026-10-23
title: Homelab network policies, one namespace at a time
description: >-
  Retiring unused cluster tools, mapping service calls, and testing six narrow
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
under `~/git`.  It now records 23 public-safe edges with a source workload,
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

The sixth policy narrows [OpenGraph ingress][opengraph-chart-pr].  Its old rule
allowed every pod in `kube-system`.  The chart now allows only the live Traefik
pods on TCP 8000.  The public route and an analysis request returned HTTP 200.
An unrelated pod could not connect.  Brainrot calls the public OpenGraph host,
so that request still enters through Traefik.

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

The next pass is to check the next Shot cleanup run and match more deployed
workloads against source config, traces, logs, and jobs that run only sometimes.
Each connection needs an owner and a reason before it becomes an allow rule.
Then one namespace can be changed, tested, observed, and rolled back through
GitOps if needed.

The [issue remains open][issue]
for that work.  The six policies reduced easy lateral paths.  They did not
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
[whoami-token-pr]: https://github.com/WaylonWalker/homelab-argo/pull/182
[librespeed-token-pr]: https://github.com/WaylonWalker/homelab-argo/pull/183
[themes-token-pr]: https://github.com/WaylonWalker/homelab-argo/pull/185
[graph]: https://github.com/WaylonWalker/homelab-argo/blob/main/docs/security/issue-174-dependencies.yaml
