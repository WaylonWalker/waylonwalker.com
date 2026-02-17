---
title: '💭 kv - Command | Vault | HashiCorp Developer'
date: 2023-11-05T03:26:51
templateKey: link
link: https://developer.hashicorp.com/vault/docs/commands/kv
tags:
  - cli
published: true

---

> hashi vault lets you manage secrets right from your cli.

``` bash
# set your vault url
export VAULT_ADDR=https://myvault.mydomain
vault login

# get a secret
vault kv get secret/hvac

# put a secret
vault kv put -mount=secret creds passcode=my-long-passcode

# get it
vault kv get secret/creds

# == Secret Path ==
# secret/data/creds
# 
# ======= Metadata =======
# Key                Value
# ---                -----
# created_time       2023-11-05T02:53:40.978120001Z
# custom_metadata    <nil>
# deletion_time      n/a
# destroyed          false
# version            3
# 
# ====== Data ======
# Key         Value
# ---         -----
# bar         baz
# passcode    my-long-passcode

# get one field
vault kv get -field=passcode secret/creds

# my-long-passcode
vault kv put -mount=secret creds bar=baz

# set more keys
vault kv put -mount=secret creds passcode=my-long-passcode bar=baz

# 
# == Secret Path ==
# secret/data/creds
# 
# ======= Metadata =======
# Key                Value
# ---                -----
# created_time       2023-11-05T03:24:14.65958906Z
# custom_metadata    <nil>
# deletion_time      n/a
# destroyed          false
# version            4

vault kv get secret/creds

# == Secret Path ==
# secret/data/creds
# 
# ======= Metadata =======
# Key                Value
# ---                -----
# created_time       2023-11-05T02:53:40.978120001Z
# custom_metadata    <nil>
# deletion_time      n/a
# destroyed          false
# version            4
# 
# ====== Data ======
# Key         Value
# ---         -----
# bar         baz
# passcode    my-long-passcode

```

[Original thought](https://developer.hashicorp.com/vault/docs/commands/kv)
