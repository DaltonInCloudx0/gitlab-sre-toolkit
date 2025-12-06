"""Command line interface for the GitLab SRE Toolkit.

This CLI is built using the `click` library to provide a user friendly
experience. Each command delegates its work to a corresponding module in
``gitlab_sre_toolkit.commands``. This file does not contain the business
logic itself.
"""

from __future__ import annotations

import click

from . import config as cfg
from .commands import (
    backup as backup_module,
    restore as restore_module,
    services as svc_module,
    upgrade as upgrade_module,
    migrate as migrate_module,
)


@click.group()
@click.option(
    "--config",
    "-c",
    default="config.yaml",
    help="Path to the GitLab SRE Toolkit configuration file.",
    show_default=True,
)
@click.pass_context
def cli(ctx: click.Context, config: str) -> None:
    """GitLab SRE Toolkit.

    This command group serves as the entry point for all subcommands. The
    configuration file is loaded lazily by subcommands as needed.
    """
    ctx.ensure_object(dict)
    ctx.obj["config_path"] = config


@cli.command(name="init-config")
@click.pass_context
def init_config(ctx: click.Context) -> None:
    """Create an example configuration file.

    This will write a sample configuration to the path specified by ``--config``.
    """
    cfg.init_example_config(ctx.obj["config_path"])


@cli.command(name="backup")
@click.pass_context
def backup_cmd(ctx: click.Context) -> None:
    """Create a full GitLab backup.

    Reads the configuration and calls the backup module's run function.
    """
    conf = cfg.load_config(ctx.obj["config_path"])
    backup_module.run(conf)


@cli.command(name="restore")
@click.option(
    "--backup-id",
    required=True,
    help="Backup filename or identifier to restore from.",
)
@click.pass_context
def restore_cmd(ctx: click.Context, backup_id: str) -> None:
    """Restore GitLab from a backup.

    You must specify the backup file name or ID via ``--backup-id``.
    """
    conf = cfg.load_config(ctx.obj["config_path"])
    restore_module.run(conf, backup_id)


@cli.group(name="services")
@click.pass_context
def services_group(ctx: click.Context) -> None:
    """Manage GitLab services (start/stop/restart/status)."""


@services_group.command(name="restart")
@click.pass_context
def services_restart(ctx: click.Context) -> None:
    """Restart all GitLab services."""
    conf = cfg.load_config(ctx.obj["config_path"])
    svc_module.run_restart(conf)


@cli.command(name="upgrade")
@click.option(
    "--to",
    "target_version",
    required=True,
    help="Target GitLab version to upgrade to (e.g. 16.9.2).",
)
@click.pass_context
def upgrade_cmd(ctx: click.Context, target_version: str) -> None:
    """Upgrade GitLab to the specified version.

    The upgrade command will perform a backup first, then apply the upgrade.
    """
    conf = cfg.load_config(ctx.obj["config_path"])
    upgrade_module.run(conf, target_version)


@cli.command(name="migrate")
@click.option(
    "--to-host",
    required=True,
    help="Hostname or IP address of the new GitLab instance to migrate to.",
)
@click.pass_context
def migrate_cmd(ctx: click.Context, to_host: str) -> None:
    """Migrate (rehydrate) GitLab to a new host.

    This command orchestrates a backup on the source, copies the backup to the
    target and restores it there.
    """
    conf = cfg.load_config(ctx.obj["config_path"])
    migrate_module.run(conf, to_host)


@cli.group(name="plugins")
def plugins_group() -> None:
    """Manage optional plugins."""
    # Plugin commands will be added here in future milestones.