#!/data/data/com.termux/files/usr/bin/python

import os
import subprocess
from datetime import datetime

# Your website directory
project_dir = "/storage/emulated/0/Download/Termux-Directory/Web-Server/LbsLightX"

# Go to the project directory
os.chdir(project_dir)

# Stage all changes
subprocess.run(["git", "add", "."], check=True)

# Create a commit message with timestamp
commit_message = f"Update & Fixes: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
subprocess.run(["git", "commit", "-m", commit_message], check=False)  # skip error if nothing to commit

# Push to GitHub
subprocess.run(["git", "push", "--force", "origin", "main"], check=True)
