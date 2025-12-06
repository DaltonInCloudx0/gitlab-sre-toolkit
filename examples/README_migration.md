# Migration example: local VM to new host

This document describes how to migrate a GitLab instance from a local VM to a
new host using the GitLab SRE Toolkit. Migration is essentially a backup and
restore operation.

1. Ensure your source instance is running the same version as the target.
2. Run `gitlab-sre backup` on the source. This generates a backup archive in
   the configured `backup_dir`.
3. Transfer the backup archive to the new host (e.g. via `scp`).
4. Install the same GitLab version on the new host and configure it.
5. Run `gitlab-sre restore --backup-id <archive>` on the new host.

In future milestones the `migrate` command will automate these steps for you.