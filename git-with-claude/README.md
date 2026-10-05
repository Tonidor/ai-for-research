# Why Use Git with Claude

## You stay in control
- You can see every change Claude makes and undo anything you don't like.
- Commits are save points, so trying things out never puts your work at risk.
- Before you accept a change, `git diff` shows you exactly what's different.

## Claude understands your project better
- It can look through your history to figure out why the code is the way it is.
- It keeps new work on its own branch, so your working code stays untouched.
- Its commit messages actually explain what changed and why.

## It saves you time
- Claude can open pull requests, reply to review comments, and fix broken builds.
- When something breaks, it can dig through past changes to find the cause fast.
- Boring jobs like merges and changelogs can just be handed off.

## Run several Claudes at once
- You can have multiple Claude sessions working in parallel, each on its own branch.
- One can fix a bug while another builds a feature, and they don't step on each other.
- Git keeps their work separate, and you merge it together when you're ready.

## The short version
Git makes working with Claude safe and easy to follow: you can always see what
happened, roll it back, and even have a few Claudes working side by side without
any mess.

---

# GitHub CLI (`gh`) Setup

## 1. Install

**macOS**
```bash
brew install gh
```

**Linux**
- Debian/Ubuntu: `sudo apt install gh` (via [official repo](https://github.com/cli/cli/blob/trunk/docs/install_linux.md))
- Fedora/RHEL: `sudo dnf install gh`
- openSUSE: `sudo zypper install gh`
- Arch: `sudo pacman -S github-cli`
- Any distro: `brew install gh`, `sudo snap install gh`, or a [release binary](https://github.com/cli/cli/releases)

## 2. Authenticate
```bash
gh auth login
```
Choose: GitHub.com, then HTTPS, then authenticate Git, then **Login with a web browser** (`gh` creates and stores the token).

## 3. Verify
```bash
gh auth status
gh repo list --limit 5
```

## Note
The browser login handles the token automatically on both macOS and Linux,
so no manual personal access token is needed on a normal desktop with a browser.
