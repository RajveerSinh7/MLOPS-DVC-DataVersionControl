# 🧠 DVC Version Control Workflow (with Local Remote)

This guide explains how to set up **Data Version Control (DVC)** for your project — including initializing DVC, adding data, versioning, pushing updates, and rolling back to older versions.

---

## 🧩 Step 1: Create and Clone a Git Repository

```bash
# Create a new Git repository (on GitHub)
# Then clone it locally
git clone <your_repo_url>
cd <your_repo_name>
```

---

## 📝 Step 2: Create a Python Script

Create `mycode.py` that saves a CSV file into a new `data` folder.

```bash
mkdir data
touch mycode.py
```

Example content for `mycode.py`:

```python
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

df = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Score": [85, 90]
})

df.to_csv("data/sample.csv", index=False)
print("✅ CSV saved to data/sample.csv")
```

Run the script:
```bash
python mycode.py
```

---

## 🧾 Step 3: Commit Initial Code to Git

```bash
git add .
git commit -m "Initial commit with data and mycode.py"
git push origin main
```

---

## ⚙️ Step 4: Initialize DVC

Install and initialize DVC:

```bash
pip install dvc
dvc init
```

This creates `.dvc/` and `.dvcignore` files.

---

## 🗄️ Step 5: Define DVC Storage (Local Folder)

We’ll simulate S3 by using a local folder named `S3`:

```bash
mkdir S3
```

---

## 🔗 Step 6: Set Remote Storage for DVC

```bash
dvc remote add -d myremote S3
```

Here:
- `myremote` → nickname for your remote
- `S3` → path to local remote folder (could also be an S3 URL)

---

## 📦 Step 7: Make DVC Track the Data Folder

```bash
dvc add data/
```

This will:
- Generate `data.dvc`
- Add `data/` to `.gitignore`

---

## 🧩 Step 8: Resolve Git Ignore Issue (Optional)

If Git was already tracking the folder, remove it from Git tracking:

```bash
git rm -r --cached data
```

Then re-add everything:
```bash
git add .
git commit -m "Make DVC start tracking data folder"
```

---

## ☁️ Step 9: Push Data to Remote (First Version)

```bash
dvc commit
dvc push
```

✅ DVC uploads the current dataset from `data/` to `S3/` and begins versioning.

---

## 🔄 Step 10: Modify Data (Version 2)

Append a new row in your data file using Python or manually.

Then check changes:
```bash
dvc status
```

Commit and push new version:
```bash
dvc commit
dvc push
```

---

## 🔁 Step 11: Add Another Row (Version 3)

Repeat the modification step again — append a new row and save.
Then run:
```bash
dvc status
dvc commit
dvc push
```

---

## ⏪ Step 12: Rollback Between Versions

To restore an older dataset version:

1. **Check Git history:**
   ```bash
   git log --oneline
   ```

2. **Checkout an earlier commit** (for the version you want):
   ```bash
   git checkout <old_commit_hash>
   ```

3. **Pull data from DVC remote:**
   ```bash
   dvc pull
   ```

✅ This restores the exact dataset version that existed at that commit.

To return to the latest version:
```bash
git checkout main
dvc pull
```

---

## 🧹 Summary of Commands

| Task | Command |
|------|----------|
| Initialize DVC | `dvc init` |
| Add data for tracking | `dvc add data/` |
| Commit DVC metadata | `dvc commit` |
| Push data to remote | `dvc push` |
| Check version status | `dvc status` |
| Rollback (old commit) | `git checkout <hash> && dvc pull` |
