"""Base class for deployment environments.

Concrete environment classes should implement methods to run backups,
restores, upgrades and service control commands appropriate for the
installation type.
"""

from __future__ import annotations

from typing import Any, Dict


class Environment:
    """Base environment class.

    A concrete subclass should implement the methods defined here to perform
    operations on a GitLab instance.
    """

    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    def backup(self) -> None:
        raise NotImplementedError

    def restore(self, backup_id: str) -> None:
        raise NotImplementedError

    def restart_services(self) -> None:
        raise NotImplementedError

    def upgrade(self, target_version: str) -> None:
        raise NotImplementedError