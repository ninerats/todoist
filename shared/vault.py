"""
Utilities for securely storing and retrieving tokens using the system keyring.

This module uses the `keyring` library to interface with the operating system's
secure credential store. Tokens are stored per service/key pair and are not
written to disk or exposed in plain text.
"""

import keyring

SERVICE_NAME = "my-dev-utils"
"""
The name used to namespace stored credentials in the system keyring.
Customize this per application or project.
"""


def set_token(key: str, value: str) -> None:
    """
    Store a token securely in the system keyring.

    Args:
        key: The identifier for the token (e.g., "todoist", "api_key").
        value: The token or secret value to store.
    """
    keyring.set_password(SERVICE_NAME, key, value)


def get_token(key: str) -> str | None:
    """
    Retrieve a stored token from the system keyring.

    Args:
        key: The identifier used when storing the token.

    Returns:
        The stored token if found, or None if not found.
    """
    return keyring.get_password(SERVICE_NAME, key)


def delete_token(key: str) -> None:
    """
    Delete a stored token from the system keyring.

    Args:
        key: The identifier of the token to remove.
    """
    keyring.delete_password(SERVICE_NAME, key)
