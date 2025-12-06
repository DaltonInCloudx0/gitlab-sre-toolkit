"""Configuration utilities for the GitLab SRE Toolkit.

This module contains helpers to load configuration from YAML files and to
generate example configuration files. The configuration is used by the CLI to
determine how to connect to a GitLab instance and which deployment type to
operate against.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import yaml


def load_config(path: str) -> Dict[str, Any]:
    """Load a YAML configuration file.

    Parameters
    ----------
    path:
        Path to the YAML file.

    Returns
    -------
    dict
        Parsed configuration dictionary. If the file does not exist an empty
        dictionary is returned.
    """
    cfg_path = Path(path)
    if not cfg_path.exists():
        return {}
    with cfg_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data


def init_example_config(path: str = "config.yaml") -> None:
    """Create an example configuration file.

    The example configuration contains the minimal set of keys required by the
    toolkit. It is safe to overwrite an existing file; the user can then edit
    the values to suit their environment.

    Parameters
    ----------
    path:
        Destination file name for the configuration.
    """
    sample_config: Dict[str, Any] = {
        # The type of deployment: omnibus_vm for bare-metal or VM, container_podman for Podman/Docker
        "deployment_type": "omnibus_vm",
        # Address of the GitLab instance (host or IP)
        "host": "gitlab.example.com",
        # SSH user used to connect to the host
        "ssh_user": "gitlab",
        # Directory where backups should be stored
        "backup_dir": "./backups",
        # Target GitLab version for upgrades
        "target_version": "15.9.0",
    }
    cfg_path = Path(path)
    with cfg_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(sample_config, f, sort_keys=False)
    print(f"Created example configuration at {cfg_path.resolve()}")