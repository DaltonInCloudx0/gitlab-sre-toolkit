"""Services command implementation.

This module provides functions to manage GitLab services. Only the restart
operation is currently stubbed out; start/stop/status commands can be added
later.
"""

from __future__ import annotations

from typing import Any, Dict


def run_restart(config: Dict[str, Any]) -> None:
    """Restart all GitLab services.

    This helper delegates to a wrapper script appropriate for the deployment
    type.  For a bare‑metal or VM Omnibus installation we invoke
    ``gitlab_ctl_wrapper.sh`` with the ``restart`` command.  For a
    containerised deployment (e.g. Podman or Docker) we call ``container_ctl.sh``.

    Parameters
    ----------
    config: Dict[str, Any]
        Parsed configuration dictionary that must include a ``deployment_type`` key
        set to either ``omnibus_vm`` or ``container_podman``.
    """
    import subprocess
    from pathlib import Path

    deployment_type = config.get("deployment_type", "omnibus_vm")
    print(f"[SERVICES] Restart requested for deployment_type={deployment_type}")

    project_root = Path(__file__).resolve().parents[2]

    if deployment_type == "omnibus_vm":
        script = project_root / "scripts" / "gitlab_ctl_wrapper.sh"
        cmd = [str(script), "restart"]
    elif deployment_type == "container_podman":
        # Use container name from config or default to "gitlab"
        container_name = config.get("container_name", "gitlab")
        script = project_root / "scripts" / "container_ctl.sh"
        cmd = [str(script), "restart", container_name]
    else:
        print(f"[SERVICES] Unknown deployment type '{deployment_type}'. Cannot restart services.")
        return

    print(f"[SERVICES] Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        print(result.stdout)
        if result.returncode != 0:
            print("[SERVICES] ERROR: restart command exited with non-zero status")
            print(result.stderr)
        else:
            print("[SERVICES] Services restarted successfully.")
    except FileNotFoundError:
        print(f"[SERVICES] Wrapper script {script} not found. Ensure the scripts directory is present and executable.")