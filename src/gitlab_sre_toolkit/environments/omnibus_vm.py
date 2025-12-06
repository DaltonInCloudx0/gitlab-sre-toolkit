"""Environment for GitLab Omnibus installations on VMs or bare metal.

This class encapsulates operations for running backups, restores, upgrades and
service control on an Omnibus GitLab installation. It is currently a stub.
"""

from __future__ import annotations

from .base import Environment


class OmnibusVM(Environment):
    """Operate against an Omnibus GitLab instance on a VM or bare metal host."""

    def backup(self) -> None:
        print("OmnibusVM.backup stub - will create backup using gitlab-backup.")

    def restore(self, backup_id: str) -> None:
        print(f"OmnibusVM.restore stub - will restore from backup {backup_id}.")

    def restart_services(self) -> None:
        print("OmnibusVM.restart_services stub - will call gitlab-ctl restart.")

    def upgrade(self, target_version: str) -> None:
        print(f"OmnibusVM.upgrade stub - will upgrade to {target_version}.")