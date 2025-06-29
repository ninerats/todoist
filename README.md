# Python Template

Starter repo for Python projects with:

- `.venv`-based local environment
- Runtime vs dev dependencies split
- Pre-wired VS Code settings
- Idempotent setup script (`init_project.ps1`)

---

## 🚀 How to Create a New Project from This Template

### 🧱 Step 1: Clone your template repo

```bash
git clone https://github.com/ninerats/python-template.git my-new-project
cd my-new-project
```

Or manually copy the folder if not using GitHub.

---

### 🧼 Step 2: Clean Git (if cloned)

If you cloned the repo and want a fresh Git history:

```bash
rm -r .git -force
git init
git add .
git commit -m "Initial commit from template"
```

---

### ⚙️ Step 3: Initialize the environment

```powershell
.\init_project.ps1
```

This sets up `.venv`, installs packages, and ensures `.gitignore` includes `.venv`.

---

### 🧪 Step 4: Start coding!

- Your entry point: `src/main.py`
- Run or test via VS Code or command line
- Add packages via `pip install packagename`

---

### 📝 Step 5: Manage requirements

If you add runtime packages:

```bash
pip freeze > requirements.txt
```

Or add them manually to `requirements.txt` and re-run:

```bash
pip install -r requirements.txt
```

---
