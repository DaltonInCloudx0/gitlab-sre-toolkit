#!/bin/bash
# Wrapper around gitlab-ctl commands.
#
# This script provides a uniform interface for starting, stopping and
# restarting GitLab services on an Omnibus installation. It is currently a
# placeholder and will be fleshed out in a future milestone.

CMD=$1
case "${CMD}" in
  start|stop|restart|status)
    echo "gitlab_ctl_wrapper.sh: ${CMD} would be executed here."
    ;;
  *)
    echo "Usage: $0 {start|stop|restart|status}"
    exit 1
    ;;
esac