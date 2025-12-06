"""Upgrade command implementation.

This module contains the ``run`` function which performs a GitLab upgrade to
a specified version. Currently the implementation is a stub.
"""

from __future__ import annotations

from typing import Any, Dict


def run(config: Dict[str, Any], target_version: str) -> None:
    """Upgrade GitLab to the given version.

    Parameters
    ----------
    config:
        Parsed configuration dictionary.
    target_version:
        Target GitLab version, e.g. ``16.9.2``.
    """
    # TODO: implement upgrade logic including backup and upgrade steps.
    print("Upgrade command invoked.")
    print(f"Would upgrade to version '{target_version}' with configuration: {config}")