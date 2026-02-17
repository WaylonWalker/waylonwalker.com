---
title: '💭 How an empty S3 bucket can make your AWS bill explode | by Mac...'
date: 2024-05-01T02:31:56
templateKey: link
link: https://medium.com/@maciej.pocwierz/how-an-empty-s3-bucket-can-make-your-aws-bill-explode-934a383cb8b1
tags:
  - aws
published: true

---

> Imagine waking up to a $1,300 for running an example project!  That sounds like peanuts for a cloud bill but for an individual trying to learn that hits my monthly budget real hard.

That's what happened to Marciej, make sure you check out the full article and give them a 👏 on Medium if you have an account.

The more I see things come out about aws, the more it makes me sick, and confirm my feelings that I cannot possibly use them for a side project without some real $$ planning to come out of it.

> Yes, S3 charges for unauthorized requests (4xx) as well[1]. That’s expected behavior.

They offer no DDOS protection against 4xx or 5xx requests against your bucket.  Absolutely bonkers that you have ZERO control over this.

---

This response just feels absolutely gross.

> I notified the AWS security team. I suggested that they restrict the unfortunate S3 bucket name to protect their customers from unexpected charges, and to protect the impacted companies from data leaks. But they were unwilling to address misconfigurations of third-party products.

It sounds like this guy followed some default instructions for an example site, HOW MANY OTHERS have done this or will do this? And AWS has no response other than to take thier money.

After contacting them he was able to get it cancelled, but this is no guarantee.  We've seen other cloud vendors stick users like this with a few thousand dollar bills after cutting their bill to 5% of the original.

> AWS was kind enough to cancel my S3 bill. However, they emphasized that this was done as an exception.

2024 is wild on the cloud hosting front, own your shit or be careful.

[Original thought](https://medium.com/@maciej.pocwierz/how-an-empty-s3-bucket-can-make-your-aws-bill-explode-934a383cb8b1)
