---
date: 2023-10-01 20:11:51
templateKey: til
title: Set up minio bucket entrypoint
status: "published"
tags:
  - data
---

I recently se tup minio object storage in my homelab for litestream sqlite
backups. The litestream quickstart made it easy to get everything up and
running on localhost, but I hit a wall when dns was involved to pull it from a
different machine.

## Here is what I got to work

First I had to configure the Key ID and Secret Access Key generated in the
minio ui.

```bash
❯ aws configure
AWS Access Key ID [****************VZnD]:
AWS Secret Access Key [****************xAm8]:
Default region name [us-east-1]:
Default output format [None]:
```

Then set the the s3 signature_version to s3v4.

```bash
aws configure set default.s3.signature_version s3v4
```

Now when I have minio running on <https://my-minio-endpoint.com> I can use the
aws cli to access the bucket.

> Note that `https://my-minio-endpoint.com` resolves to the bucket endpoint
> (default 9000) not the ui (default 9001).

```bash
aws --endpoint-url https://my-minio-endpoint.com s3 ls my_bucket
```

## Now Configuring Litestream

Litestream also accepts the `endpoint` argument via config. I could not get it
to work just with the ui.

> Note the `aws configure` step above is not required for litestream, only the
> aws cli.

```yaml
dbs:
  - path: /path/to/database.db
    replicas:
      - url: s3://my_bucket/
        endpoint: https://my-minio-endpoint.com
        region: us-east-1
        access-key-id: ****************VZnD
        secret-access-key: ************************************xAm8
```

Now run a litestream replication.

```bash
litestream replicate -config litestream.yml
# or put the config in /etc/litestream.yml and just run replicate
litestream replicate
```
