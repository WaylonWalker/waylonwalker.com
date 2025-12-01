---
date: 2024-04-04 18:42:18
templateKey: til
title: setting up a kind cluster with argocd installed
published: true
tags:
  - python

---

Kind (Kubernetes in Docker) is a tool that makes it easy to create and tear
down local clusters quickly.  I like to use it to test out new workflows.

Argocd is a continuous delivery tool that makes it easy to setup gitops
workflows in kubernetes.

Here is how you can setup a new kind cluster and install argocd into it using
helm, the kubernetes package manager.

``` bash
kind create cluster --name argocd

# your first time through you need to add the argocd repo
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update

# install argocd into the cluster
helm install argo argo/argo-cd --namespace argocd --create-namespace

# deploy the app of apps
kubectl apply -f apps/apps.yaml
```

If you want to add repos and apps to your cluster you can use the argo cli to
do that, but first you will need forward the argocd port and login.

``` bash
# Wait until Argo CD API server is available
echo "Waiting for Argo CD API server to be available..."
while ! kubectl wait --for=condition=available --timeout=60s deployment/argo-argocd-server -n argocd; do
  echo "Waiting for Argo CD API server to be ready..."
  sleep 10
done


kubectl port-forward svc/argo-argocd-server -n argocd 8080:443 &
argocd_admin_password=$(kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d)
argocd login localhost:8080 --insecure --username admin --password $argocd_admin_password
argocd repo add https://github.com/fokais-com/app.fokais.git --username waylonwalker --password ${GH_ARGO_PAT}
argocd app create app-fokais-local --repo https://github.com/fokais-com/app.fokais.git --path k8s/overlays/local --dest-server https://kubernetes.default.svc --sync-policy automated --sync-option Prune=true
```
