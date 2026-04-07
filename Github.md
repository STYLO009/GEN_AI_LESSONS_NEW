# 🚀 Complete GitHub Commands Guide

## 🧱 1. Initial Setup (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --list
```

---

## 📁 2. Create / Initialize Repository

### Start a new repo

```bash
git init
```

### Clone existing repo

```bash
git clone https://github.com/username/repo.git
```

---

## 📦 3. Basic Workflow

```bash
git status
git add .
git commit -m "your message"
```

---

## 🌐 4. Connect to GitHub

```bash
git remote add origin https://github.com/username/repo.git
git remote -v
```

---

## 🚀 5. Push Code

### First push

```bash
git branch -M main
git push -u origin main
```

### Next pushes

```bash
git push
```

---

## ⬇️ 6. Pull Latest Code

```bash
git pull origin main
```

### Recommended

```bash
git pull origin main --rebase
```

---

## 🔄 7. Daily Workflow (Best Practice)

```bash
git pull origin main --rebase
git add .
git commit -m "update"
git push
```

---

## 🌿 8. Branching

```bash
git branch feature-branch
git checkout feature-branch
```

### Create + switch

```bash
git checkout -b feature-branch
```

### Modern way

```bash
git switch feature-branch
```

---

## 🔀 9. Merge Branch

```bash
git checkout main
git merge feature-branch
```

---

## ❌ 10. Undo Changes

### Unstage file

```bash
git reset file.py
```

### Undo last commit (keep changes)

```bash
git reset --soft HEAD~1
```

### Undo last commit (delete changes)

```bash
git reset --hard HEAD~1
```

---

## ⚠️ 11. Force Push

```bash
git push origin main --force
```

---

## 🔍 12. View Logs

```bash
git log
git log --oneline
```

---

## 📂 13. Remove Files

```bash
git rm file.py
git commit -m "removed file"
```

---

## 🧹 14. .gitignore Example

```
.env
venv/
__pycache__/
node_modules/
models/
```

---

## 🔗 15. Fix Common Errors

### Rejected push

```bash
git pull origin main --rebase
git push
```

### Change remote URL

```bash
git remote remove origin
git remote add origin NEW_URL
```

---

## 🧠 16. Advanced Commands

### Stash changes

```bash
git stash
git stash pop
```

### Check differences

```bash
git diff
```

---

## 🎯 Quick Cheat Sheet

```bash
git pull origin main --rebase
git add .
git commit -m "update"
git push
```
