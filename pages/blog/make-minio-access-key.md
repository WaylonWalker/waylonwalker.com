---
date: 2025-02-02 19:18:05
templateKey: blog-post
title: Make MinIO Access Key
tags:
  - homelab
published: True

---

Today in my homelab I wanted to setup a new service that needed a MinIO access
key. So I created a new user and a new access key with the MinIO CLI rather
than poking through the ui like I have before.

![screenshot-2025-02-03T02-13-38-628Z.png](/api/file/2f706c5d-c591-4465-8d2b-eb18ce26aeca.png){.cinematic}

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
NEWSECRETKEY=mysupersecretkey
echo NEWSECRETKEY
echo $NEWSECRETKEY

mc admin policy create myminio mybucket-readwrite mypages_rw_policy.json
mc admin user add myminio $NEWUSERNAME $NEWSECRETKEY
mc admin policy attach myminio mybucket-readwrite --user $NEWUSERNAME
mc config host add myminio https://minio.wayl.one $NEWUSERNAME $NEWSECRETKEY
```

## Give it a test

Now we can test that it works, by creating a file and copying it into the
bucket.

``` bash
# set up to work with the aws cli
export AWS_DEFAULT_REGION=us-east-1
export AWS_ACCESS_KEY_ID=$NEWUSERNAME
export AWS_SECRET_ACCESS_KEY=$NEWSECRETKEY
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
