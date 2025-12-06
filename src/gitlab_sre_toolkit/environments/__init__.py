"""Deployment environment abstractions.

This package defines base classes and concrete implementations for operating
against different GitLab deployment types. In this initial skeleton the
implementations are stubs.
"""

from .base import Environment  # noqa: F401

__all__ = ["Environment"]