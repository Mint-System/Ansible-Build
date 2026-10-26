---
title: "Loki log retention"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: review
date_completed: YYYY-MM-DD
harness: pi
model: moonshotai/Kimi-K2.6
input_tokens:
output_tokens:
---

# Loki log retention

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

On my server `atlas` the loki server stores log data:

```
root@atlas:/mnt/sdb/docker/volumes/loki01/_data# du -hs ./* | sort -h
4.0K	./compactor
4.0K	./rules
4.0K	./rules-temp
884K	./tsdb-shipper-active
1.7M	./tsdb-shipper-cache
47M	./wal
36G	./chunks
```

Check if the retention policies of loki are configured correctly.

You are allowed to access the atlas host, but only to read stuff.

Share the analysis in this file and I will decide what to do.


@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

### Findings

**Retention period configured**: `14d` via `loki_retention_period` (`roles/loki/defaults/main.yml`). This is NOT overridden in `inventories/mint_system/host_vars/atlas/vars.yml`.

**Critical issue**: The `local-config.yml` template (`roles/loki/templates/local-config.yml`) defines `limits_config.retention_period: 14d` but **omits the `compactor` section entirely**.

In Loki 3.x with TSDB + filesystem storage, `limits_config.retention_period` only restricts query range. The actual deletion of expired chunks is performed by the compactor which requires `retention_enabled: true`. Without it, old chunks accumulate indefinitely even though they cannot be queried beyond 14 days.

**Evidence from atlas** (provided by author):
- `./chunks` = 36G
- `./compactor` = 4.0K (inactive)

This distribution strongly suggests the compactor is NOT removing old chunks.

### Recommendation

Add the following section to `roles/loki/templates/local-config.yml`:

```yaml
compactor:
  retention_enabled: true
```

Then redeploy the Loki role to atlas (`task play ... -t loki -l atlas`). After the container restarts with the new config, the compactor will begin deleting chunks older than 14 days. Disk usage should drop automatically over the next compaction cycle.

### Note

Direct SSH to atlas was not possible from this environment due to missing authorized key, so the analysis is based entirely on the repository configuration and the author's `du` output.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness and model. If you have access to session info also add token count.
