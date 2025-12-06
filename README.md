# GitLab SRE Toolkit

This repository provides a plug‑and‑play automation toolkit for managing GitLab
Community Edition (CE) installations across a variety of deployment types.

The goal of this project is to automate common site reliability engineering
tasks such as creating backups, restoring instances on new hosts, safely
performing version upgrades with rollback support, and managing the lifecycle of
GitLab services. The toolkit is designed to work against bare‑metal or VM
installations, containerised setups (e.g. Podman or Docker), and cloud VMs on
providers such as AWS.

## Features

* **Configuration abstraction** – define your environment and desired GitLab
  version in a single YAML file.
* **Backup & restore** – easily create full backups of your GitLab instance and
  rehydrate a new instance from those backups.
* **Service control** – start, stop, restart and check the status of GitLab
  services uniformly across different installation types.
* **Upgrade manager** – automate GitLab upgrades with pre‑upgrade backups and a
  clear rollback path.
* **Extensible architecture** – plugin interface to add custom commands such as
  monitoring integrations (e.g. Prometheus/Grafana).

This repository is a work in progress. The initial commit includes a skeleton
for the Python package, basic CLI wiring, example configuration files and
placeholder Ansible playbooks. Subsequent commits will flesh out each command,
implement the Ansible roles and provide real logic behind backup, restore and
upgrade workflows.

## Getting started

To begin using the toolkit locally you need Python 3.9+ installed. We recommend
using a virtual environment.

```bash
git clone <this repository>
cd gitlab-sre-toolkit
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

After installation you can run the `gitlab-sre` CLI. To bootstrap your first
configuration file run:

```bash
gitlab-sre init-config
```

This will create a `config.yaml` file in the current directory. Edit this file
to point at your GitLab instance (host, SSH user, deployment type etc.) and
then explore other commands:

```bash
gitlab-sre backup      # create a full backup of GitLab
gitlab-sre restore --backup-id <file>  # restore from a backup
gitlab-sre services restart            # restart services
gitlab-sre upgrade --to <version>      # upgrade to a target version
```

Refer to the in‑code documentation for details on each command and supported
configuration options.

## Contributing

We welcome contributions! Please open issues or pull requests to propose
features, report bugs or discuss improvements.