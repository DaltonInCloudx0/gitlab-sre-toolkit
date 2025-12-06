#!/bin/bash
# Wrapper around Podman or Docker commands for managing a GitLab container.
#
# This script provides a uniform interface for starting, stopping and restarting
# a GitLab container. It is currently a placeholder and will be implemented in
# a future milestone.

CMD=$1
CONTAINER_NAME=${2:-gitlab}

case "${CMD}" in
  start|stop|restart|status)
    echo "container_ctl.sh: ${CMD} on container ${CONTAINER_NAME} would be executed here."
    ;;
  *)
    echo "Usage: $0 {start|stop|restart|status} [container_name]"
    exit 1
    ;;
esac