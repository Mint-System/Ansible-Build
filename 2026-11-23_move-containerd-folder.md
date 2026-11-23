---
commit_ref: ae3249735cd3195b9345bc2b32fda6c97210c234
title: "Move containerd folder"
author: "Janik von Rotz <login@janikvonrotz.ch>"
session_id: 01a209ff-3907-73a8-b847-b1d786380f8d
action: execute
state: completed
date_completed: 2025-11-23
harness: pi
provider: mistral
model: deepseek-v4-1-flash-1017
input_tokens: 16063
output_tokens: 5238
---

# Move containerd folder

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read the `AGENTS.md` to get an understanding of the project
- Read task section and prepare a list of todos
- Update the todo list while working on task

@Clanker When task is completed set frontmatter state to review. If you have access to session info add token count and session id. Prompt the author to verify the results.

## Task

On most server I moved the Docker data dir to an external disk. Now I found this:

```
/var/lib/containerd# sudo du -hs ./* | sort -h
4.0K	./io.containerd.sandbox.controller.v1.shim
4.0K	./io.containerd.snapshotter.v1.blockfile
4.0K	./io.containerd.snapshotter.v1.btrfs
4.0K	./io.containerd.snapshotter.v1.erofs
4.0K	./tmpmounts
8.0K	./io.containerd.grpc.v1.introspection
8.0K	./io.containerd.snapshotter.v1.native
44K	./io.containerd.runtime.v2.task
1.7M	./io.containerd.metadata.v1.bolt
1.6G	./io.containerd.content.v1.content
5.6G	./io.containerd.snapshotter.v1.overlayfs
```

Is this the application folder? What is the `overlayfs` in this context?

What would it mean to move it to a mounted folder (similar to Docker data)?

## Worklog

Answer to the questions (analysis task, no role changes).

### Is `/var/lib/containerd` the application folder?

No. It is **containerd's internal state directory** (the "root"), not application data.
It holds the image store, unpacked image layers and runtime state. Containers never read
their application files from there directly — the overlay mount is only the merged root
filesystem they see at runtime. Application data belongs in Docker volumes or bind mounts.

| Folder | Content |
| --- | --- |
| `io.containerd.content.v1.content` | Content-addressable blob store (1.6G). Every image layer, manifest and config stored once by digest. |
| `io.containerd.snapshotter.v1.overlayfs` | Unpacked, mutable image layers used by the overlayfs snapshotter (5.6G). |
| `io.containerd.metadata.v1.bolt` | BoltDB metadata: namespaces, image refs, snapshots, leases, containers. |
| `io.containerd.runtime.v2.task` | Runtime (runc) state per task: bundles, `config.json`, pid files. |
| `io.containerd.snapshotter.v1.native/btrfs/erofs/blockfile` | Alternative snapshotter state, unused while overlayfs is active. |
| `tmpmounts`, `io.containerd.grpc.v1.introspection`, `io.containerd.sandbox.controller.v1.shim` | Runtime helpers and introspection mounts. |

### What is `overlayfs` here?

OverlayFS is the Linux union filesystem. Each image layer is stored as a *snapshot* of
extracted files. A container's root filesystem is assembled from `lowerdir` (stacked,
immutable image layers) + `upperdir` (the container's writable layer) + `workdir`, merged
into one directory. `io.containerd.snapshotter.v1.overlayfs` holds that: snapshots of image
layers plus the writable layers of containers. It grows with every image pulled *and* every
container created.

Docker does not keep a second copy: `/var/lib/docker` (`data-root`) already contains
`overlay2/`, i.e. the same data in a different layout. Moving the Docker data dir moved the
image layers with it.

### Moving it to a mounted folder

Possible, with these consequences:

1. **Docker usually does not use this directory.** The `docker` role sets
   `"data-root": "{{ docker_data_dir }}"` in `/etc/docker/daemon.json`, so Docker keeps its own
   image/content/snapshot store under that path. `/var/lib/containerd` then mostly holds state
   from other consumers (crictl, k3s, podman, dind) or start-ordering leftovers. Verify with
   `docker info -f '{{.DockerRootDir}}'` before relocating.
2. **Containerd must be reconfigured, not just moved.** There is no `daemon.json` equivalent for
   the root; it is set by the systemd unit:
   `ExecStart=/usr/bin/containerd --root /var/lib/containerd --state /run/containerd`.
   Relocation needs a drop-in `/etc/systemd/system/containerd.service.d/override.conf` changing
   `--root` (keep `--state` on local disk).
3. **Images are migrated, not referenced.** Stop `containerd` and `docker`, then `rsync -aHAX`,
   or accept re-pulling all images. A partially migrated content store causes digest/manifest
   mismatches.
4. **Mount ordering and filesystem.** The disk must be mounted before containerd starts: use
   `RequiresMountsFor=` in the drop-in and avoid relying on `nofail`. OverlayFS on network
   storage is unsupported; a local block device is required.
5. **Removing the old tree** requires both `containerd` and `docker` stopped, otherwise bind
   mounts under `tmpmounts` keep inodes busy.
6. **Monitoring.** `cadvisor`, `alloy` and `promtail` mount `docker_data_dir` read-only, not the
   containerd root. A relocated containerd root is invisible to `write-docker-volume-metric`;
   add a disk-usage metric for that mount if the ~7G matters.

**Recommendation:** keep `/var/lib/containerd` on the system disk while Docker uses its own
`data-root` — it holds no application data and is only a few GB. Relocate only if a second
runtime actually populates it, and then via a systemd drop-in with the external disk mounted
first.

Changelog: no changes, analysis task only.

Author confirmed the results. No files outside `prompt.md` were modified.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info update token count. Finally, update the changelog with the most important changes.
