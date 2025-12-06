# src/gitlab_sre_toolkit/cli.py
import click
from . import config as cfg
from .commands import backup, restore, services, upgrade, migrate
from .plugins import loader as plugin_loader

@click.group()
@click.option("--config", "-c", default="config.yaml",
              help="Path to gitlab-sre config file.")
@click.pass_context
def cli(ctx, config):
    ctx.obj = {}
    ctx.obj["config"] = cfg.load_config(config)

@cli.command()
@click.pass_context
def init_config(ctx):
    """Create an example config file for this environment."""
    cfg.init_example_config()

@cli.command()
@click.pass_context
def backup_cmd(ctx):
    """Create a full GitLab backup using gitlab-backup."""
    backup.run(ctx.obj["config"])

@cli.command()
@click.option("--backup-id", required=True, help="Backup ID or filename.")
@click.pass_context
def restore_cmd(ctx, backup_id):
    """Restore GitLab from a backup (rehydrate instance)."""
    restore.run(ctx.obj["config"], backup_id)

@cli.group()
def services():
    """Manage GitLab services (start/stop/restart/status)."""
    pass

@services.command("restart")
@click.pass_context
def services_restart(ctx):
    services.run_restart(ctx.obj["config"])

@cli.command()
@click.option("--to", "target_version", required=True,
              help="Target GitLab version (e.g. 16.9.2).")
@click.pass_context
def upgrade_cmd(ctx, target_version):
    """Upgrade GitLab to the target version with backup + safety checks."""
    upgrade.run(ctx.obj["config"], target_version)

@cli.command()
@click.option("--to-host", required=True,
              help="Hostname of new target GitLab instance.")
@click.pass_context
def migrate_cmd(ctx, to_host):
    """Migrate (rehydrate) GitLab to a new host."""
    migrate.run(ctx.obj["config"], to_host)

@cli.group()
def plugins():
    """Manage gitlab-sre plugins."""
    pass

@plugins.command("list")
def plugins_list():
    plugin_loader.list_plugins()
