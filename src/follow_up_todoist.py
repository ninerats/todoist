import sys
import os
import requests

# === TODO: Replace with your personal Todoist API token ===
TODOIST_API_TOKEN = "2069791e69e4e6ec96b6a5e2bb71465db69b34fb"

# Optional: specify a default project ID (None = Inbox)
TODOIST_PROJECT_ID = "6VWM3frp978CJ2Cc"

# === 1. Get the file path from the command line ===
if len(sys.argv) < 2:
    print("❌ Error: No file path provided.")
    print("Usage: follow_up_todoist.py <path_to_file>")
    sys.exit(1)

file_path = sys.argv[1]
file_name = os.path.basename(file_path)

# Create a file:// link for use in the task comment
FILE_LINK = f"file:///{file_path.replace(' ', '%20')}"

# === 2. Create the Todoist task ===
headers = {
    "Authorization": f"Bearer {TODOIST_API_TOKEN}"
}

task_data = {
    "content": f"Follow up on {file_name}"
}
if TODOIST_PROJECT_ID:
    task_data["project_id"] = TODOIST_PROJECT_ID

task_response = requests.post(
    "https://api.todoist.com/rest/v2/tasks",
    headers=headers,
    json=task_data
)

if task_response.status_code != 200 and task_response.status_code != 204:
    print(f"❌ Failed to create task: {task_response.status_code} {task_response.text}")
    sys.exit(1)

task_id = task_response.json()["id"]

# === 3. Add a comment with the file link ===
comment_data = {
    "task_id": task_id,
    "content": f"[Open file]({FILE_LINK})"
}

comment_response = requests.post(
    "https://api.todoist.com/rest/v2/comments",
    headers=headers,
    json=comment_data,
    timeout=10
)

if comment_response.status_code not in (200, 204):
    print(f"⚠️ Task created, but failed to add comment: {comment_response.status_code} {comment_response.text}")
else:
    print(f"✅ Task created for '{file_name}' with file link.")
