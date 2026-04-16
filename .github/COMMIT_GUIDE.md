# 📘 Team Collaboration & Commit Guide

Welcome! To ensure our **Biometric Forensic Identification Platform** scales cleanly without losing data or stepping on each other's toes, we strictly follow a Git/GitHub workflow. 

This guide serves as your crash course on how to claim tasks, branch out code, write commits, and securely merge your work into the main project.

---

## 1. 🎯 Step 1: Claiming an Issue
Before you write any code, you need to know *what* you are building!
1. Navigate to the **Issues** tab on GitHub.
2. Browse the open tasks. When you find one you want to tackle, comment on it: *"I'd like to take this on!"*
3. Wait for the project maintainer to formally **Assign** the issue to you.
4. **Why?** This prevents two developers from accidentally building the exact same feature at the same time.

---

## 2. 🔀 Step 2: Branching Strategy
We **never** commit code directly to the `main` branch. Every feature or bug fix requires its own isolated branch.

Once the issue is assigned to you, open your local terminal and run:

```bash
# 1. ALWAYS make sure your main branch is up-to-date!
git checkout main
git pull origin main

# 2. Create your isolated feature branch
# Convention: Use 'feature/' for new additions, or 'bugfix/' for errors
git checkout -b feature/login-screen
```
*You are now working in a safe bubble. Nothing you do here will break the `main` application.*

---

## 3. 💾 Step 3: Writing Commits
As you write code, you should save checkpoints of your work. We use small, frequent, and descriptively named commits.

```bash
# Check what files you have modified
git status

# Stage the files you want to save
git add frontend/src/components/Login.jsx

# Commit the files with a very clear, descriptive message
git commit -m "feat: add user authentication form to Login component"
```

**Commit Name Best Practices:**
- Use prefixes: `feat:` (New feature), `fix:` (Bug fix), `docs:` (Documentation), `style:` (CSS/UI styling).
- Keep the message active and short. (e.g., `fix: resolve auth crash` instead of ~~`fixed that crash issue from yesterday`~~).

---

## 4. 🔄 Step 4: Syncing up
If you have been working on your branch for a few days, other people might have merged their code into `main`. You don't want your branch to fall behind!

```bash
# While still inside your feature branch, pull in updates from main
git pull origin main
```
If there are any **Merge Conflicts** at this stage, VS Code will highlight them. Discuss with the other developer if you are unsure which code to keep!

---

## 5. 🚀 Step 5: Pushing and Pull Requests (PRs)
You finished the feature! Now you need to push your local bubble up to GitHub and request to merge it into `main`.

```bash
# Push your branch up to the GitHub server
git push origin feature/login-screen
```

### Opening the Pull Request:
1. Go to the project's GitHub page. You should see a green button: **Compare & Pull Request**. Click it.
2. In the description box, explain what you did.
   - *Tip: If your PR solves Issue #5, write `Closes #5` in the description. GitHub will magically close the issue for you when the PR merges!*
3. Once created, request a review from **at least one** team member.

---

## 6. 🔍 Step 6: Code Review & Merging
1. Your reviewer will look at your code on GitHub. They might leave comments asking for small changes.
2. If changes are requested: Make the fixes on your local machine, run `git add` and `git commit`, and push again. The PR will update automatically!
3. Once the reviewer approves with a **✅ LGTM (Looks Good To Me)**, you can click the green **Merge Pull Request** button on GitHub.
4. **Delete your branch** on GitHub after merging to keep the repository clean.

---

🎉 **Congratulations! Your code is now live on the main application!**
