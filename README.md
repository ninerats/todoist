# 📝 Follow-Up Todoist Utility

This is a simple Python command-line script that lets you create follow-up tasks in [Todoist](https://todoist.com/) directly from a file path. It's designed to help you track files you need to revisit or act on later by creating a task with a direct link to the file.

## 🚀 Features

- Creates a Todoist task using the file's name as the task content.
- Optionally adds the task to a specific project (default is the Inbox).
- Attaches a comment to the task with a clickable `file://` link to open the file directly.
- Designed to be used as a right-click context menu action or via shell command.

## 🛠 Usage

```bash
python follow_up_todoist.py <path_to_file>
```

Example:
```bash
python follow_up_todoist.py "C:\Users\you\Documents\ImportantFile.docx"
```

## ⚙️ Setup

1. **Get your Todoist API token**:
   - Visit https://todoist.com/prefs/integrations to find your personal token.
   - Replace the value of `TODOIST_API_TOKEN` in the script with your token.

2. **(Optional)** Set a default project ID:
   - If you want all tasks to go into a specific project instead of the Inbox, set the `TODOIST_PROJECT_ID`.

3. **File link support**:
   - The comment added to the task will contain a `file://` URL for the selected file, making it easy to open.

## 🔐 Security Warning

Do **not** commit your Todoist API token to version control! This script is for personal use and should be stored securely.

## ✅ Example Output

```
🚀 Script is running...
✅ Task created for 'ImportantFile.docx' with file link.
```

## 🧪 Notes

- Requires `requests` Python package:
  ```bash
  pip install requests
  ```

- Ideal for use with file explorer shell integrations, custom keyboard shortcuts, or productivity automation tools.

## 📄 License

MIT (or add your preferred license here)
