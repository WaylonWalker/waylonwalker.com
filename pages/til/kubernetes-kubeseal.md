---
date: 2024-03-27 20:02:57
templateKey: til
title: kubernetes kubeseal
published: true
tags:
  - k8s
  - kubernetes

---


In my homelab kubernetes cluster I am using kubeseal to encrypt secrets.  I
have been using it successfully for a few months now wtih great success. It
allows me to commit all of my secrets manifests to git with out risk of leaking
secrets.

You see kubeseal encrypts your secrets with a private key only stored in your
cluster, so only the cluster itself can decrypt them using the kubeseal
controller.

![cover](https://screenshots.waylonwalker.com/kubeseal-post.png)

## KubeSeal

[https://sealed-secrets.netlify.app/](https://sealed-secrets.netlify.app/){.hoverlink}

<a href='https://sealed-secrets.netlify.app/' >
<img
    src='https://shots.wayl.one/shot/?url=https://sealed-secrets.netlify.app/&height=450&width=800&scaled_width=800&scaled_height=450&selectors='
    alt='screenshot of https://sealed-secrets.netlify.app/'
    height='450'
    width='800'
/>
</a>

## installation

Installation happens in two steps.  You need the kubernetes controller and the
client side cli to create a sealed secret.

For a more complete instruction see the
[docs#installation](<https://github.com/bitnami-labs/sealed-secrets?tab=readme-ov-file#installation>]

## installation - controller

!!! warning
     **context**
     Make sure that you are in the right context before running any kubectl commands.

``` bash
kubectl config current-context
```

sealed-secrets is installed using the helm package manager.  To install
sealed-secrets run the following command.

``` bash
helm repo add sealed-secrets https://bitnami-labs.github.io/sealed-secrets
helm install sealed-secrets -n kube-system --set-string fullnameOverride=sealed-secrets-controller sealed-secrets/sealed-secrets
```

## installation - client

For the client you can check your OS package manager, brew, or the
[github-releases](https://github.com/bitnami-labs/sealed-secrets/releases/).
For me I found it in the main arch repos.

``` bash
paru -S kubeseal
# or
sudo pacman -S kubeseal
# or
brew install kubeseal
```

!!! note
     You will need to install kubeseal on every device that you will want to
     create sealed secrets on.

## Example

Most of these commands come straight from the docs.  From my experience I have
always specified the namespace, my projects go per namespace and I don't have
any reason that other namepsaces should see the secret, and if they do I deploy
another secret in that namespace.

``` bash
# Create a json/yaml-encoded Secret somehow:
# (note use of `--dry-run` - this is just a local file!)
echo -n bar | kubectl create secret generic mysecret --dry-run=client --from-file=foo=/dev/stdin -o yaml -n thenamespace > mysecret.yaml
```

> note that the key of the secret is `foo` and the value is `bar`

results

``` yaml
apiVersion: v1
data:
  foo: YmFy
kind: Secret
metadata:
  creationTimestamp: null
  name: mysecret
  namespace: thenamespace
```

!!! note
     The data is base64 encoded.

     ``` bash
     echo -n bar | base64
     # YmFy
     ```

``` bash
# This is the important bit:
kubeseal -f mysecret.yaml -w mysealedsecret.yaml

# At this point mysealedsecret.json is safe to upload to Github,
# post on Twitter, etc.

# Eventually:
kubectl create -f mysealedsecret.yaml -n thenamespace
# sealedsecret.bitnami.com/mysecret created

# Profit!
kubectl get secret mysecret
kubectl get secret mysecret -n thenamespace
# NAME       TYPE     DATA   AGE
# mysecret   Opaque   1      27s

cat mysealedsecret.yaml | kubeseal --validate

```

``` bash
echo -n bar | kubectl create secret generic mysecret --dry-run=client --from-file=foo=/dev/stdin -o yaml \
  | kubeseal -o yaml -n thenamespace > mysealedsecret.yaml
echo -n baz | kubectl create secret generic mysecret --dry-run=client --from-file=bar=/dev/stdin -o yaml \
  | kubeseal -o yaml -n thenamespace --merge-into mysealedsecret.yaml
```

Results

``` yaml
---
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  creationTimestamp: null
  name: mysecret
  namespace: thenamespace
spec:
  encryptedData:
    bar: AgBLkamltcLfH1dC1JxQ3qd8lJ8aBZF2ARoq3uo055hnzXOy8g2T5liTx5UPvyPV8yyWqABU8eOnwjNhDtzSATvYeBB3fGkucdOZziWEoiNsWTR9ZtFEkod7Ya6uGkzZOJwi3IkrHFVIT9oWZQUxxJZ6vFhPiFcx9Dorr8TNSzG4KOug25+PhWPPiHDgSup5N3CkWCZaYOF7dbZRVSA4nGP1fZxjFByHP4AsdjLCHptyVbkpLRKeiXTkLxfLX4K+JLZGM41S1On5bSP56mCfv1daTJx619kDXkRLw9l21Ot283/L0NMNAiw781AefYMVoO3aHmYgcT6wAtsQAKje9fyL7DQRHt8a5NZOWukp/P6XjdXRz/nfQasQlbSTrRkDpplKIM5/WdPcBoKi+yyoOL0rZ8x1X7YzUI3BggZmzWyEPD01BK1YAHGZnYIZbbCy1JSm8JCBvP+xWMg+i0Z/DCD8nclAhH1GX2Q7/NrNHF//589AJfuriymd2+mk7uaLA4RRsY0l5QeZD6HVAqSv5jWsVQQtSftWmI9vn9oL/Pno7sEUjSDpXPfF4nnsULhxsPEe2DFAMm1kZAjdF06ueF4/x2Fdy80ZQNyycaDx2CWm4z3b14A75WGyOXl2wJZQqxrFCz8el4hD2nH3zQFEzd6AIh49myqVAGuu2qGlYP4p94LJghVa+mQjztLD/2ZUZjY+anQ=
    foo: AgAducXW6iUCY900cPDdmRfuj7tKnh2hY4C1+2hFoAtjyvjepsKNWsiPJ81t8anaMfFPat4ta060l5VtTrceFE8oS/rViz1tvNWGPBjL+GwL/QjkGl6H8ju87vKERKQn5qw7B/V5j24VM8AxOd+/vJNt/IeRIHLubvFft4hyMq4b0xmIxaemBSTxchQX/5364T3VJH2kHaqpqd+JJgQnTbiTQe/XnyZokDX8GSxw4rAbJUJSRUtY9DB9ZDu2zC5VngX+GJjbwHGbv9EKs8LShJIPrD8xHqrDmlSXGkkP01D4A6268Qoi3x5S0H5aqDgtrgBiWsNkzdKwjfrTNx7pKecOi41lyFdffHOGUew4aPPMqjzWR2TEms9WNNQXwnBdDHKMkFsisocF52BolEkcjF8g/u5h2Af92abMu6k16VybJrB7TV1set5A9W7rqG1iXI4+1W6XQfFnpja8xL/zJBvZcyHgeYMNaxa3C3s6PANhPzAUVaXV9eedAkptGJLN13IZj4LujpoAxRKo6bEdydv/5P23R3fx5PgTOpVI7riECAOIg2PThFsEoVCUwStmKCvIx1I2+YixIlv/OiaUWo4lrI/3ve5WGp4ZnuiJPk34JoYAlRbR6+sX14d8Ek6viq/pJUUIfVpNIkNMboUL4u+KpT47eyQ/mWih/KFduQyX9II/vQ+/IJGzEEHIipxAhdmV+K4=
  template:
    metadata:
      creationTimestamp: null
      name: mysecret
      namespace: thenamespace
```

## backing up your sealing key

``` bash
kubectl get secret -n kube-system -l sealedsecrets.bitnami.com/sealed-secrets-key -o yaml >main.key
```

## converting .env files to a secret

Working with web applications .env is a common way to store credentials.  Let's
look at how we can convert these to secrets.

``` bash
kubectl create secret generic mysecret --from-env-file=.env -n thenamespace --dry-run=client -o yaml > mysecret.yaml
```

Now you have a secret that looks like this.

``` yaml
apiVersion: v1
data:
  foo: YmFy
kind: Secret
metadata:
  creationTimestamp: null
  name: mysecret
  namespace: thenamespace
```

Seal it up just like before.

``` bash
kubeseal -f mysecret.yaml -w mysealedsecret.yaml
```

## Using the secrets

I typically use the secrets in the container spec.

``` yaml
containers:
  - name: myapp
    envFrom:
      - secretRef:
          name: mysecret
    # You can still have other env vars
    env:
      - name: foo
        value: bar
```

Sometimes I want to mount the secret as a volume.

``` yaml
containers:
  - name: myapp
    volumeMounts:
      - name: mysecret
        mountPath: /mysecret
volumes:
  - name: mysecret
    secret:
      secretName: mysecret
```

## Image Pull Secrets

I also need to use imagePullSecrets.  Let's walk through the whole process.  Starting with the secret.

``` bash
kubectl create secret docker-registry regcred --docker-server=myprivateregistry.example.com --docker-username=foo --docker-password=bar --dry-run=client -o yaml
```

Generates the following secret.

``` yaml
apiVersion: v1
data:
  .dockerconfigjson: eyJhdXRocyI6eyJteXByaXZhdGVyZWdpc3RyeS5leGFtcGxlLmNvbSI6eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIiwiYXV0aCI6IlptOXZPbUpoY2c9PSJ9fX0=
kind: Secret
metadata:
  creationTimestamp: null
  name: regcred
type: kubernetes.io/dockerconfigjson

---
```

> the secret

Now we we can seal that secret.

``` bash
kubeseal -f regcred.yaml -w regcred-sealed.yaml
```

And that gives us the following sealed secret that we can deploy into our cluster.

``` yaml
---
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  creationTimestamp: null
  name: regcred
  namespace: default
spec:
  encryptedData:
    .dockerconfigjson: AgATYVEywkyYEaoErQbJo6xEZfOnRn1ydNTLkO3Jt/NF/UH+0o9lHpDecRpN0XnVu8xJUcdjkgD9q2XkwP8e6qQDS2mMPTiTNIN+8gbJx97WrD1YQDT0lXBuoyi9I/iwlXxx6MgH/6GY6CeGTz5SRlvoU0Xhlt4d11s7/xapdE8QMLsAReqPEv8oZHEyAxDRrjXX0V+tO8dV+G+GXjUDMBBceLael9rvGzSKIwDVXACVqQhLkB6FoP98M+yyBE46RBNnSnS0ShQM5PprL24HKpRZ43x4RM53KBrQ7R/MxeshafY+B6vUvrolmVox4sud8xngMOcjTO28LLOrck5V8ZiDabhN7ajHEf03IESr1o/ADGf5k9988Vv1txJtsZW0K2mpRu0D7/BLVL9KzbZ5ywULqIoD/Ur2GIGnZqMAKOq4laGp/GJtMKLrhmEvekT397wC/Gf/xdDKVhHf2p4ocsPu7LKFuS5H/Auel/Q5grdn8L5wwrO4VWRv3eJroKh/Hux7Qd7f64O7qdi0XthDocf+gmtjys+Gy72M7tyf8f/O+3oKbS4CWQVTj4ZThMc9znrFnHqt2q/7pAyytTQCpk51wlzOsNvOhCueJM/jmeahaL0LuBrqngqISpnd65sgVzBcZpwK9i2Fckyt0DrZLH+NoIuvaqNhzlF+OMbAft/ylWWKCH4WUP+FKG+1LXM7ud7AA3MMbGSBxHL0/WK/INa7MB56xZKMqqyvvLLQHFTQUROJjkgkzsumdOgwZTRgIFnAZ4+vOX3/1Rtt3mAs3vdoJhL4GuKUYCnEHt908eKkWEVEs7eMk5SdSRtIsbaXO2s0dtADwg==
  template:
    metadata:
      creationTimestamp: null
      name: regcred
      namespace: default
    type: kubernetes.io/dockerconfigjson
```

Now that we have our sealed registry secret, we can deploy it into our cluster.

``` bash
kubectl apply -f regcred-sealed.yaml
```

Now we can use it to pull images from our private registry.

``` yaml
containers:
  imagePullSecrets:
    - name: regcred
```

## Full example

Here is a full deployment example using all the secrets we have created.

* regcred
* mounting a secret
* envFrom secret

``` yaml
---
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    service: myservice
  name: myservice
  namespace: mynamespace
spec:
  replicas: 1
  selector:
    matchLabels:
      service: myservice
  strategy:
    type: Recreate
  template:
    metadata:
      creationTimestamp: null
      labels:
        service: myservice
    spec:
      containers:
        - envFrom:
            - secretRef:
                name: mysecret
          env:
            - name: foo
              value: bar
          image: private-registry.io/myimage:1.0.0
          name: myimage
          ports:
            - containerPort: 5000
              protocol: TCP
          resources: {}
          volumeMounts:
            - mountPath: /mysecret
              name: mysecret
      restartPolicy: Always
      volumes:
        - name: mysecret
          secret:
            secretName: mysecret
      imagePullSecrets:
        - name: regcred
```

## Downside

Now the main downside I see with kubeseal is that it does not provide a way to
store your secrets in a way that you can access outside of your cluster.  So
you need to make sure that you have another solution in place to store your
secrets so that you still have them if you ever were to take the cluster down
or move from k8s to something else.

Overall the likelyhood of you loosing a production cluster is pretty low, so
maybe it's ok to just trust it depending on what the secrets are.  Especially
for things you control and can rotate anyways its fine.
