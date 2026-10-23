---
date: 2026-10-23
title: Homelab network policies, one namespace at a time
description: >-
  Mapping app dependencies, narrowing Kubernetes access, and turning off unused
  workloads.
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
- id: codex
  role: copy editor
editorial_history:
- schema_version: 1
  event_id: 000cc311-7f55-46a5-87db-ac768e1d9e2e:pages/blog/homelab-network-policies-one-namespace-at-a-time.md
  author: codex
  role: copy-editor
  action: edited
  recorded_by: codex
  recorded_at: '2026-10-23T14:40:30.928622+00:00'
  base_commit: 7648c1b93396459c48036565b924da0dc5572a08
  commit: 3f5a482a1b638b2874a8b2263f4930f3eba40597
  path: pages/blog/homelab-network-policies-one-namespace-at-a-time.md
  content_digest: sha256:a4d7c1597537cf68b6058234c6113ca7f39ad457df5a666a9fbc0887e70b4e8e
  digest_version: editorial-v1
  file_url: https://github.com/waylonwalker/waylonwalker.com/blob/3f5a482a1b638b2874a8b2263f4930f3eba40597/pages/blog/homelab-network-policies-one-namespace-at-a-time.md
  diff_url: https://github.com/waylonwalker/waylonwalker.com/commit/3f5a482a1b638b2874a8b2263f4930f3eba40597#diff-fa2d24930cca966e95857caacf3cb76d700541182acd405aeb459035c0364c5e
  summary: 'Added verified token, paused-app, and Shot cache recovery results from
    issue #174.'
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
change][shot-retry-pr] makes curl retry that error.  The 13:45 run succeeded
after one refused connection.  Its cleanup request returned 31 queued items and
zero completed or failed items.  Argo now reports the CronJob Healthy.

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

The same check found tokens on five more static nginx sites.  Their pods serve
files from read-only webroots.  They do not call the Kubernetes API.  Separate
site overlays now disable token mounts for [30s][token-30s-pr], [Go for
Wyatt][token-go-pr], [App][token-app-pr], [Apps][token-apps-pr], and [3D
Workshop][token-3d-pr].  Argo reports each app Synced and Healthy.  Each new pod
has no token volume, and each public route returned HTTP 200.

## Pause unused apps

Postiz and its Redis Deployment were already set to zero replicas in GitOps.
No Postiz app pods run.  Its database cluster is hibernated, and all four
Postiz PVCs remain Bound.  I made no changes to its database, files, or secrets.

Dozzle was also set to zero replicas, with no running pods.  Its ClusterRole
and binding remain.  They let its ServiceAccount read pods, logs, and nodes,
and create pod exec and attach sessions.  I left these permissions in place
because this change only pauses Dozzle.  A separate change can remove them if
Dozzle stays retired.  Its Ingress remains, but its Service has no endpoints.

Installer still had one running pod.  [A GitOps change][installer-pause-pr]
sets its Deployment to zero replicas.  Argo reports Synced and Healthy.  The
pod is gone, and the Service has no endpoints.  The Ingress remains configured.

Magnet SMP was already at zero replicas, with no pod or Service endpoint.  Its
two PVCs remain Bound.  Its manifest is not part of the active Kustomization,
and the live Deployment has no Argo tracking annotation.  GitOps does not
enforce its stopped state.  Adopting the manifest would also bring its Service,
PDB, and PVCs under Argo management, so ownership needs review first.

## Keep the cache

The Shot cache PV had a deletion timestamp from March, but its claim remained
Bound and mounted by four API pods and two workers.  Kubernetes does not let
users clear a deletion timestamp.  I stopped those six pods, released the
claim, and recreated the PV and PVC with the same Retain policy and host path.
The cache path stayed available.  `/cache` still reports the same 3.6 TB file
system and 40 KiB of files.  All six pods are ready, and Argo reports the Shot
app Synced and Healthy.

## What comes next

The Linker root route still returns HTTP 500 from an app error.  Its health and
readiness routes return HTTP 200, and its NetworkPolicy is scoped to Traefik.
The app error needs a separate fix.

A refined inventory matched 60 token-bearing pods to standard Ingress backend
Services.  The scan includes internal hosts and routes.  This is not a count of
internet-facing pods.  The next step is to review the
remaining app and job identities against their API use and RoleBindings.  The
Dozzle ClusterRoleBinding also needs a separate retirement decision.

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
[token-30s-pr]: https://github.com/WaylonWalker/homelab-argo/pull/200
[token-go-pr]: https://github.com/WaylonWalker/homelab-argo/pull/201
[token-app-pr]: https://github.com/WaylonWalker/homelab-argo/pull/202
[token-apps-pr]: https://github.com/WaylonWalker/homelab-argo/pull/203
[token-3d-pr]: https://github.com/WaylonWalker/homelab-argo/pull/204
[installer-pause-pr]: https://github.com/WaylonWalker/homelab-argo/pull/206
[graph]: https://github.com/WaylonWalker/homelab-argo/blob/main/docs/security/issue-174-dependencies.yaml
