"""Submodules implementing individual CLI commands.

Each command in the CLI corresponds to a module in this package which exposes
a top-level ``run(...)`` function (and any additional helpers). These
functions receive the loaded configuration dictionary and any extra arguments
from the CLI.

At this stage the implementations are placeholders. Future milestones will
replace the stubs with real logic calling out to Ansible playbooks, SSH
commands, container runtimes, etc.
"""

from . import backup  # noqa: F401
from . import restore  # noqa: F401
from . import services  # noqa: F401
from . import upgrade  # noqa: F401
from . import migrate  # noqa: F401

__all__ = ["backup", "restore", "services", "upgrade", "migrate"]