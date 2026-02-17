---
title: '💭 Creating k8s jobs with python'
date: 2023-10-28T00:52:24
templateKey: link
link: https://thoughts.waylonwalker.com/post-og/152
tags:
  - homelab
  - k3s
  - containers
published: true

---

> I was looking to add running kubernetes jobs to a python cli I am creating, and I found this solution, mostly thanks to `ollama run mistral:7b-instruct-q4_K_M ` and my loose understanding of what the yaml syntax is supposed to look like for a kubernetes job.  This will let me create a job in the cluster, choose the image that runs, the command that is called, and how long until the job expires and is cleaned up.  While the job still exists I can go in and look at the logs, but once its ttl has expired they are gone.


``` python
from kubernetes import client, config

# Load the default kubeconfig
config.load_kube_config()

# Define the API client for batch jobs
api_instance = client.BatchV1Api()

# Create a new job object
job = client.V1Job(
    api_version="batch/v1",
    kind="Job",
    metadata=client.V1ObjectMeta(name="myjob"),
    spec=client.V1JobSpec(
        ttl_seconds_after_finished=100,
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "myjob"}),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="myjobcontainer",
                        image="busybox",
                        command=["ls", "/"],
                    ),
                ],
                restart_policy="Never",
            ),
        ),
        backoff_limit=1,
    ),
)

# Call the Kubernetes API to create the job
api_instance.create_namespaced_job(namespace="default", body=job)
```

[Original thought](https://thoughts.waylonwalker.com/post-og/152)
