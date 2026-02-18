---
title: Create new write Docker metrics scripts
---

Read the `AGENTS.md` to get a general understanding of the project.

Have a look at `roles/node_exporter/templates/write-docker-volume-metric`. I want you to create three new scripts:

- write-docker-up-metric / container_last_seen
- write-docker-memory-metric / container_memory_usage_bytes
- write-docker-cpu-metric / container_cpu_user_seconds_total

Each of these scripts write the respective metric for all running Docker containers.

The metrics are replicated from cAdvsior.

Here are samples of each cAdvsior metric.

- container_last_seen

```
container_last_seen{container_label_description="Database odoo03",container_label_maintainer="",container_label_org_opencontainers_image_authors="",container_label_org_opencontainers_image_description="",container_label_org_opencontainers_image_documentation="",container_label_org_opencontainers_image_licenses="",container_label_org_opencontainers_image_ref_name="",container_label_org_opencontainers_image_revision="",container_label_org_opencontainers_image_source="",container_label_org_opencontainers_image_title="",container_label_org_opencontainers_image_url="",container_label_org_opencontainers_image_version="",id="/docker/385bf1fb28167256f49e36ce89d6eaf76bafe9d08c2f901ffd827520e34c096f",image="postgres:14-alpine",name="postgres04"} 1.765537702e+09 1765537702016
```

- container_memory_usage_bytes

```
container_memory_usage_bytes{container_label_description="Database odoo03",container_label_maintainer="",container_label_org_opencontainers_image_authors="",container_label_org_opencontainers_image_description="",container_label_org_opencontainers_image_documentation="",container_label_org_opencontainers_image_licenses="",container_label_org_opencontainers_image_ref_name="",container_label_org_opencontainers_image_revision="",container_label_org_opencontainers_image_source="",container_label_org_opencontainers_image_title="",container_label_org_opencontainers_image_url="",container_label_org_opencontainers_image_version="",id="/docker/385bf1fb28167256f49e36ce89d6eaf76bafe9d08c2f901ffd827520e34c096f",image="postgres:14-alpine",name="postgres04"} 1.1266048e+08 1765537679897
```

- container_cpu_user_seconds_total

```
container_cpu_user_seconds_total{container_label_description="Database odoo03",container_label_maintainer="",container_label_org_opencontainers_image_authors="",container_label_org_opencontainers_image_description="",container_label_org_opencontainers_image_documentation="",container_label_org_opencontainers_image_licenses="",container_label_org_opencontainers_image_ref_name="",container_label_org_opencontainers_image_revision="",container_label_org_opencontainers_image_source="",container_label_org_opencontainers_image_title="",container_label_org_opencontainers_image_url="",container_label_org_opencontainers_image_version="",id="/docker/385bf1fb28167256f49e36ce89d6eaf76bafe9d08c2f901ffd827520e34c096f",image="postgres:14-alpine",name="postgres04"} 3174.76 1765537679897
```

As you can see there are a log of labels. The new scripts should only write these labels:

- image
- name
- id

To test the script you can use the local Docker setup.