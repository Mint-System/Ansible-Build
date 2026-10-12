---
commit_ref: 126f358ae1ba3c9e0ecbac419143182077e5ff82
title: "Fix test project ci"
author: "Janik von Rotz <login@janikvonrotz.ch>"
state: completed
date_completed: 2026-10-12
model: moonshotai/Kimi-K2.6
input_tokens: 29851
output_tokens: 13795
---

# Fix test project ci

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

My ci workflow `test-project` fails with this message:

``
TEST: Test docker volume scripts
postgres01
Make sure to stop the container postgres01 before creating a backup.
Run backup for Docker volume postgres01.
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
4e07a0f12b2c: Pulling fs layer
06ad70e463aa: Pulling fs layer
06ad70e463aa: Verifying Checksum
06ad70e463aa: Download complete
4e07a0f12b2c: Verifying Checksum
4e07a0f12b2c: Download complete
4e07a0f12b2c: Pull complete
06ad70e463aa: Pull complete
Digest: sha256:f144425ff09be612d6d9ad965196e9cdc23dae1f42110a8a11a3e9a8198759f7
Status: Downloaded newer image for ubuntu:latest
tar: Removing leading `/' from member names
Docker volume backup has finished: /var/tmp/postgres01/{postgres01}.tar
Make sure to stop the container postgres01 before creating a backup.
Run backup for Docker volume postgres0148a7c0a486a14eb0de22215a3659962dff79cbdfd84b26724c31058f388d5550.
tar: Removing leading `/' from member names
Docker volume backup has finished: /var/tmp/postgres01/{postgres0148a7c0a486a14eb0de22215a3659962dff79cbdfd84b26724c31058f388d5550}.tar
postgres01
postgres01
Make sure to stop the attached containers before running the restore.
Run restore /var/tmp/postgres01/postgres01.tar to Docker volume postgres01 ...
tar: /restore/postgres01.tar: Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
Error: Process completed with exit code 2.
```

Check the `docker-volume-backup` and `docker-volume-restore` scripts.

## Worklog

Fixed the `test-project` CI failure by addressing bugs in the docker volume scripts:

### `roles/docker_volume/files/docker-volume-backup`
- The `docker inspect` Go template `{{ range .Mounts }}{{ .Name }}{{ end }}` concatenated all mount names without separators, causing multiple volume names to be merged into a single invalid filename (e.g. `postgres01<hash>`).
- Fixed by filtering for `Type == "volume"` and outputting each name on a separate line with `{{ "\n" }}`.
- Replaced the broken manual array conversion (`printf -v volumes ...` + `volume_list=($(echo ... | tr ',' '\n'))`) with proper Bash array handling using `mapfile -t` for `-a` and `IFS=',' read -r -a` for `-v`.

### `roles/docker_volume/files/docker-volume-restore`
- The tar command inside `docker run ... bash -c "..."` was vulnerable to word splitting if `$filename` contained spaces, because the outer shell expanded the variable before the inner shell parsed the command string.
- Fixed by passing the filename via the `-e RESTORE_FILE` environment variable and using single quotes around the `bash -c` argument so the inner shell performs the variable expansion safely.

@Clanker Set frontmatter state to completed and update date and model. If you have access to session info also add token count.
