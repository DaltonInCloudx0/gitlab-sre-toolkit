"""Backup command implementation.

This module provides a ``run`` function which the CLI calls when the user
invokes ``gitlab-sre backup``. In later milestones this function will
execute an Ansible playbook or shell commands to create a full backup of
the GitLab instance as configured.
"""

from __future__ import annotations

from typing import Any, Dict


def run(config: Dict[str, Any]) -> None:
    """Perform a backup of the GitLab instance.

    The backup command orchestrates the creation of a full GitLab backup.  In
    its simplest form this function creates a timestamped backup directory
    locally and shells out to an Ansible playbook or shell script that runs
    GitLab's own backup utilities.  Future improvements will detect the
    environment (VM vs container) and use the appropriate wrapper.

    Parameters
    ----------
    config: Dict[str, Any]
        Parsed configuration dictionary loaded from a YAML config file.
    """
    from datetime import datetime
    import subprocess
    from pathlib import Path

    # Determine where to place backups.  Allow override via config, defaulting
    # to a local ``backups`` directory relative to the project root.
    backup_dir = Path(config.get("backup_dir", "backups")).resolve()
    backup_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    print(f"[BACKUP] Starting backup at {timestamp}…")
    print(f"[BACKUP] Using backup directory: {backup_dir}")

    # Construct ansible-playbook invocation.  For now we assume the inventory
    # and playbook live in the top-level ``ansible`` directory.  In a future
    # version this could be parameterised via config.
    playbook = Path(__file__).resolve().parents[2] / "ansible" / "playbooks" / "backup.yml"
    inventory = Path(__file__).resolve().parents[2] / "ansible" / "inventory" / "example_local.ini"
    cmd = [
        "ansible-playbook",
        "-i",
        str(inventory),
        str(playbook),
    ]

    print(f"[BACKUP] Executing playbook: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        print(result.stdout)
        if result.returncode != 0:
            print("[BACKUP] ERROR: ansible-playbook exited with non-zero status")
            print(result.stderr)
        else:
            print("[BACKUP] Backup playbook completed successfully.")
    except FileNotFoundError:
        # ansible-playbook not installed; fall back to a simple message.
        print("[BACKUP] ansible-playbook not found. Please install Ansible or implement your own backup mechanism.")

    print("[BACKUP] Backup process finished.")