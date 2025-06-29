"""
Integration test to verify connectivity to the Todoist API using a securely stored API token.

This test retrieves the token from the system keyring via `vault`, makes a
simple authenticated request to the Todoist REST API, and passes if a valid response
is received.

Requirements:
- The `requests` package must be installed.
- The token must be stored using `set_token("todoist", "<your-token>")`.

Usage:
    pytest test_todoist_connection.py
"""

from pytest import CaptureFixture
import requests
import logging
from shared.vault import get_token

TODOIST_API_ROOT = "https://api.todoist.com/rest/v2"
TOKEN_KEY = "todoist"


logger = logging.getLogger(__name__)


def test_can_connect_to_todoist():
    """Ensure the Todoist API responds with a valid status and data."""
    token = get_token(TOKEN_KEY)
    assert token is not None, "Todoist API token is missing in keyring"

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{TODOIST_API_ROOT}/projects", headers=headers, timeout=10
    )

    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"
    assert isinstance(
        response.json(), list
    ), "Expected a list of projects in response"


def test_create_and_delete_task(capfd: CaptureFixture[str]):
    """Test creating and deleting a Todoist task."""

    token = get_token(TOKEN_KEY)
    assert token is not None, "Todoist API token is missing in keyring"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    # Step 1: Create a task
    task_data = {"content": "Test task from pytest"}
    create_resp = requests.post(
        f"{TODOIST_API_ROOT}/tasks",
        json=task_data,
        headers=headers,
        timeout=10,
    )
    assert create_resp.status_code == 200, f"Create failed: {create_resp.text}"
    task = create_resp.json()
    task_id = task.get("id")
    assert task_id, "No task ID returned"

    # Step 2: Dump task ID to test output
    logger.info("\n...created Task ID: %s", task_id)

    # Step 3: Delete the task
    delete_url = f"{TODOIST_API_ROOT}/tasks/{task_id}"
    delete_resp = requests.delete(delete_url, headers=headers, timeout=10)
    assert (
        delete_resp.status_code == 204
    ), f"Delete failed: {delete_resp.status_code} {delete_resp.text}"
    logger.info("\nDeleted Task ID: %s", task_id)
