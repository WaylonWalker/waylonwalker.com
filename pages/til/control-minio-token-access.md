---
date: 2024-04-24 17:03:34
templateKey: til
title: control minio token access
published: true
tags:
  - python

---

To allow access only to the <bucket>, you can pass add the Resource field  to
the User Policy when you create a new token.

``` json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "admin:*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "kms:*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:*"
      ],
      "Resource": [
        "arn:aws:s3:::<bucket>",
        "arn:aws:s3:::<bucket>/*"
      ]
    }
  ]
}
```
