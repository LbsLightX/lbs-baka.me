import os
import subprocess

# --- CONFIG ---
GITHUB_USERNAME = "LbsLightX"
GITHUB_TOKEN = "token_here"  # 🔐 Replace with your real token
REPO = "lbs-baka.me"
BRANCH = "main"  # ✅ use 'main' not 'master'
REPO_PATH = "/storage/emulated/0/Download/Termux-Directory/Web-Server/LbsLightX"
# --------------

def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr and "nothing to commit" not in result.stderr:
        print(result.stderr.strip())
    return result

def main():
    os.chdir(REPO_PATH)
    print("📁 In repo:", REPO_PATH)

    print("🔄 Switching to 'main' branch...")
    run("git checkout main")

    print("📥 Staging changes...")
    run("git add .")

    print("📝 Committing...")
    commit = run("git commit -m '🔄 Auto-update via Termux script'")
    if "nothing to commit" in commit.stderr:
        print("✅ No changes to commit.")
        return

    print("🔗 Updating remote URL...")
    remote_url = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO}.git"
    run(f"git remote set-url origin {remote_url}")

    print("🚀 Pushing to GitHub Pages (`main`)...")
    run(f"git push origin {BRANCH}")

    print("✅ Done! Website should be updated at:")
    print(f"🌐 https://{GITHUB_USERNAME}.github.io/{REPO}/")

if __name__ == "__main__":
    main()
