---
date: 2025-07-01 12:46:33
templateKey: blog-post
title: just fucking use kubernetes
tags:
  - kubernetes
  - satire
published: True

---

You want to run containers?

**JUST FUCKING USE KUBERNETES.**

!!! tip "Obvious satire"
    If you don't like harsh language this is not the post for you.  Obviously
    ripping off [motherfuckingwebsite](https://motherfuckingwebsite.com/).

!!! warning "ThIs is AI SLoP"
    If you don't like if you can fuck off to the next post, I'm having fun here,
    but satire is not my strong suit and needed some help.

---

## "But it’s complicated!"

Shut up.  Close twitter and fucking do something.  Life is complicated. You know what else is complicated? Email. DNS. Life.
Kubernetes is the least painful way to orchestrate containers at scale.
**Docker Compose is for your laptop.**

* Swarm is dead.
* Nomad is just sad.
* Systemd units? Get out of here.

---

## "But my app is small!"

**SO IS YOUR AMBITION.**
You *could* write a bunch of bash scripts and hope they work on prod.
You *could* SSH into servers and handcraft your infra like it's 2011.
Or you could **just fucking use Kubernetes** and sleep at night.

---

## I can just throw my script in crontab

Tell that to your boss when your cronjob failed 16 times in the last week
without anyone noticing. **kubernete** makes it fucking simple, want retry ask
for it.  Hanging script, activeDeadlineSeconds that bitch.  Connecting to six
other services in your shitty ass infrastructure this shit retries automatically.

---

## "I don’t need autoscaling!"

Cool. Tell that to your boss when the CEO tweets your link and the site goes
down harder than your last date.

---

## "But YAML is ugly!"

So is your Terraform, your Ansible, your Prometheus config, your custom CI/CD
scripts written in Bash, and the spaghetti you called a monolith before you
went microservices and made it worse.

---

## "Kubernetes is too heavy!"

Compared to what?

Your handcrafted, artisanal, single-node LXC setup running on an Intel NUC from 2014?

---

## "What if it’s overkill?"

What if YOU are underkill?

---

## "How do I do zero-downtime deploys?"

Probes my dude, you fucking probe your shit.  Rolling out a new deployment
kubernets won't cut over to your broke ass release if that shit don't pass. No
more writing janky scripts that SSH into prod and run git pull while praying to
the CI/CD gods.

## "What if I still fuck it up - How do I roll back?"

`k9s` is your best friend, pop that shit open find your broke ass deployment,
jump owner to the replicaset and roll that bitch back to the working shit.

## I need to scale

This shit is built in, add a goddamn replica or 6 for fuck sake, need
autoscaling use the HPA.  This aint your granpas hand fucking crafted pet
server, its fucking cattle.  Load balancing just fucking happens, don't think
about it just use it, and it will work for your six goddamn friends that
actually use your shit.

## I want gitops

---

## USE KUBERNETES

* It fucking works.
* Everyone else is using it.
* There are like 500 open-source projects built just to make it easier.
* It runs on your laptop, your server, the cloud, and inside your dreams.
* It *will* make your resume better.
* It even has a goddamn **dashboard** now.

---

## Not convinced?

Here’s your alternative stack:

1. A bash script that restarts Docker when it dies.
2. A Makefile that deploys via SCP.
3. A cron job that prays to the log gods.
4. A wiki page explaining how to debug your hand-rolled bullshit.
5. You. Crying.

---

## So yeah

Save yourself.
Save your team.
Save your infrastructure.

## JUST

## FUCKING

## USE

## KUBERNETES

*(or don’t, and become a DevOps cautionary tale)*

!!! seealso

    * [motherfuckingwebsite](https://motherfuckingwebsite.com/)
    * [justfuckingcode](https://www.justfuckingcode.com/)
    * [justfuckingusereact](https://justfuckingusereact.com/)
