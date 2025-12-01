---
date: 2025-02-02 19:18:05
templateKey: blog-post
title: Make MinIO Access Key
tags:
  - homelab
  - minio
published: True

---

Today in my homelab I wanted to setup a new service that needed a MinIO access
key. So I created a new user and a new access key with the MinIO CLI rather
than poking through the ui like I have before.

![screenshot-2025-02-03T02-13-38-628Z.png](https://dropper.wayl.one/api/file/2f706c5d-c591-4465-8d2b-eb18ce26aeca.png){.more-cinematic}

## Global Level vs User Level

The MinIO CLI has two levels of access, global and user level. Most of the
commands in this post will have several ways to do similar tasks that would
potentially work.  We are going to prefer to use the user level commands for
more control.  For some commands such as listing Keys it is handy to use the
global level.

## The Policy

First we are going to make a new policy file named `mypages_rw_policy.json`.

```bash
{
"Version": "2012-10-17",
"Statement": [
    {
    "Action": [
        "s3:GetBucketLocation",
        "s3:ListBucket"
    ],
    "Effect": "Allow",
    "Resource": [
        "arn:aws:s3:::mybucket"
    ]
    },
    {
    "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListMultipartUploadParts",
        "s3:AbortMultipartUpload"
    ],
    "Effect": "Allow",
    "Resource": [
        "arn:aws:s3:::mybucket/*"
    ]
    }
]
}
```

## Set the Minio Alias

Before we can create new access keys we will need to start by settin up an
alias in minio that has admin rights to the minio server.

``` bash
# default values
export MINIO_ACCESS_KEY=minioadmin
export MINIO_SECRET_KEY=minioadmin

mc alias set myminio https://myminio.example.com $MINIO_ACCESS_KEY $MINIO_SECRET_KEY
```

Check to see if your alias exists.

``` bash
mc alias list
```

## The Script

Now we are going to pick a SECRETKEY and a NEWUSERNAME, create the policy,
create the user, attach the policy to the user and add the user to the alias.

``` bash
#!/bin/bash
NEWUSERNAME=MYPAGESUSER
NEWPASSWORD=mysupersecretkey
echo USERNAME: $NEWUSERNAME
echo PASSWORD: $NEWPASSWORD

# create a new policy for read/write to the bucket
mc admin policy create myminio mybucket-readwrite mypages_rw_policy.json

# create a new user
mc admin user add myminio $NEWUSERNAME $NEWPASSWORD

# attach the policy to the user, giving them read/write to the bucket
mc admin policy attach myminio mybucket-readwrite --user $NEWUSERNAME

# add the user to the alias
mc config host add myminio https://minio.wayl.one $NEWUSERNAME $NEWPASSWORD

# create a new access key for the user with thier permissions
mc admin user svcacct add                       \
myminio MYPAGESUSER                     \
--name mypagesRWKey                       \
--description "MYPAGESUSER Key for myminio" \
--expiry 2025-03-01
```

``` bash
NEWSECRETKEY
3e11************************************************************
Access Key: IL4*****************
Secret Key: M3D*************************************
Expiration: 2025-03-01 06:00:00 +0000 UTC
```

!!! Attention
    * This is the secret key, do not share it with anyone.
    * This secret key will only be displayed once here, make sure you copy it
      to a secure location now.

## Give it a test

Now we can test that it works, by creating a file and copying it into the
bucket.

``` bash
# set up to work with the aws cli
export AWS_DEFAULT_REGION=us-east-1
export AWS_ACCESS_KEY_ID=IL4*****************
export AWS_SECRET_ACCESS_KEY=M3D*************************************
export AWS_ENDPOINT_URL=https://myminio.example.com

# create a test file
echo "You How" > hi-hello.txt
# upload the file
aws s3 cp hi-hello.txt s3://mybucket/hi-hello.txt
# test the file exists
aws s3 ls s3://mybucket
# output
# 2025-02-02 19:25:02          8 hi-hello.txt
```

!!! note
    I am using the aws cli to test, I installed it with pip.

    ``` bash
    pipx install awscli
    ```

## Managing Access Keys

You can list all of the access keys for a user, or all users.

``` bash
# for one user
mc admin accesskey ls myminio/ MYPAGESUSER

# for all users
mc admin accesskey ls myminio/ --all
```

The output will show you all of the access keys for each user.

``` bash
User: MYPAGESUSER
  Access Keys:
    IL4*****************, expires: 3 weeks from now, sts: false
```

You can also get a list of the service accounts for a user with this command.

``` bash
mc admin user svcacct ls myminio/ MYPAGESUSER
```

``` bash
   Access Key        | Expiry
IL4***************** | 2025-03-01 06:00:00 +0000 UTC
````

!!! Note
    You cannot see all of these keys from the web ui, the cli seems to be the
    only way to display all access keys, including access keys for other users.

## Creating an RO Access Key

I ran into errors when trying to create a new key with exactly the same
permissions as the user, I'm not sure if adding a policy that does not match
the user is allowed or not.

I made a new policy that has read only access to the bucket as `mypages_ro_policy.json`

``` json
{
"Version": "2012-10-17",
"Statement": [
    {
    "Action": [
        "s3:GetBucketLocation",
        "s3:ListBucket"
    ],
    "Effect": "Allow",
    "Resource": [
        "arn:aws:s3:::mypages"
    ]
    },
    {
    "Action": [
        "s3:GetObject",
        "s3:ListMultipartUploadParts"
    ],
    "Effect": "Allow",
    "Resource": [
        "arn:aws:s3:::mypages/*"
    ]
    }
]
}
```

This command will use the above policy to create a new read only access key.

``` bash
mc admin user svcacct add \
  myminio MYPAGESUSER \
  --name mypagesRWKey \
  --description "MYPAGESUSER READ ONLY Key for myminio" \
  --expiry 2025-03-01 \
  --policy mypages_ro_policy.json
```

The output will show you the access key and secret key.

``` bash
Access Key: KDM*****************
Secret Key: 8Ww*************************************
Expiration: 2025-03-01 06:00:00 +0000 UTC
```

!!! Attention
    * This is the secret key, do not share it with anyone.
    * This secret key will only be displayed once here, make sure you copy it
      to a secure location now.

## Removing a service account

If you want to remove a service account, you can use the `rm` command to remove
the Access Key, by alias and Access Key.

``` bash
mc admin user svcacct rm myminio/ QH6*****************
```

## Getting info

You can get the info for a user or service accounts using the `info`
subcommands.

``` bash
⬢ [devtainer] ❯ mc admin user info minio-wayl-one/ MYPAGESUSER
AccessKey: MYPAGESUSER
Status: enabled
PolicyName: mypages-readwrite
MemberOf: []

⬢ [devtainer] ❯ mc admin user svcacct ls minio-wayl-one/ MYPAGESUSER
   Access Key        | Expiry
KDM***************** | 2025-03-01 06:00:00 +0000 UTC
IL4***************** | 2025-03-01 06:00:00 +0000 UTC

⬢ [devtainer] ❯ mc admin user svcacct info myminio/ IL4*****************
AccessKey: IL4*****************
ParentUser: MYPAGESUSER
Status: on
Name: mypagesRWKey
Description: MYPAGESUSER Key for myminio
Policy: implied
Expiration: 3 weeks from now

⬢ [devtainer] ❯ mc admin user svcacct info myminio/ KDM*****************
AccessKey: KDM*****************
ParentUser: MYPAGESUSER
Status: on
Name: mypagesRWKey
Description: MYPAGESUSER READ ONLY Key for myminio
Policy: embedded
Expiration: 3 weeks from now
```
