"""Repository-wide exception hierarchy."""

from __future__ import annotations


class AevixError(Exception):
    """Base class for all AEVIX-specific exceptions."""


class ConfigurationError(AevixError):
    """Raised when configuration loading or validation fails."""


class LoggingConfigurationError(AevixError):
    """Raised when logging setup fails."""


class RegistryError(AevixError):
    """Raised when registry operations fail."""


class CheckpointError(AevixError):
    """Raised when checkpoint persistence fails."""


class ValidationError(AevixError):
    """Raised when object validation fails."""
