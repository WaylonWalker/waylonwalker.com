---
date: 2024-09-15 16:57:41
templateKey: til
title: k3s config after first install
published: true
tags:
  - k8s
  - k3s
  - kubernetes

---

After first setting up a new k3s instance your kubeconfig file will be located
in /etc/rancher/k3s/k3s.yaml.

You cans use it from here by setting $KUBECONFIG to that file.

```bash
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

Or you can copy it to `~/.kube/config`

``` bash
cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
```

If you have installed k3s on a remote server and need the config on your local
machine then you will need to modify the server address to reflect the remote
server.

``` bash
scp user@<server-ip>:/etc/rancher/k3s/k3s.yaml ~/.kube/config
```

!!! warning
  only do this if you don't already have a ~/.kube/config file, otherwise copy
  it to a new file and set your $KUBECONFIG env variable to use it.

Now you will need to open that file and change the server address, making sure
to keep the port number.

``` yaml
apiVersion: v1
clusters:
  - cluster:
      certificate-authority-data: ****
      server: https://<server-ip>:6443
    name: default
```
