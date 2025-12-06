"""Environment for containerised GitLab deployments (Podman/Docker).

This class encapsulates operations for running backups, restores, upgrades and
service control on a GitLab instance running inside a container. It is
currently a stub.
"""

from __future__ import annotations

from .base import Environment


class ContainerPodman(Environment):
    """Operate against a GitLab container managed by Podman or Docker."""

    def backup(self) -> None:
        print("ContainerPodman.backup stub - will exec backup inside container.")

    def restore(self, backup_id: str) -> None:
        print(f"ContainerPodman.restore stub - will restore from backup {backup_id} inside container.")

    def restart_services(self) -> None:
        print("ContainerPodman.restart_services stub - will restart container.")

    def upgrade(self, target_version: str) -> None:
        print(f"ContainerPodman.upgrade stub - will pull new image {target_version}.")