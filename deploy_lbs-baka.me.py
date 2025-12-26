#!/data/data/com.termux/files/usr/bin/python

import os
import subprocess
from datetime import datetime
import sys

# Absolute path to your website directory
PROJECT_DIR = "/storage/emulated/0/Download/Termux-Directory/Web-Server/LbsLightX"

def run(cmd, allow_fail=False):
    print("➜", " ".join(cmd))
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        if allow_fail:
            return
        print("✖ Command failed:", " ".join(cmd))
        sys.exit(1)

def main():
    if not os.path.isdir(PROJECT_DIR):
        print("✖ Project directory not found:")
        print(PROJECT_DIR)
        sys.exit(1)

    os.chdir(PROJECT_DIR)
    print("✔ Working directory:", PROJECT_DIR)

    # Pull latest changes first (important)
    run(["git", "pull", "origin", "main"])

    # Stage everything
    run(["git", "add", "."])

    # Check if there is anything to commit
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )

    if not status.stdout.strip():
        print("✔ No changes to commit")
        return

    # Ask for commit message
    user_message = input("📝 Enter commit message (press Enter for default): ").strip()

    if user_message:
        commit_message = user_message
    else:
        commit_message = f"Update & Fixes: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    # Commit
    run(["git", "commit", "-m", commit_message])

    # Push (NO force)
    run(["git", "push", "origin", "main"])

    print("✔ Deployment complete")

if __name__ == "__main__":
    main()
    
