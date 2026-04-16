# 📘 Beginner-Friendly Collaboration & Commit Guide

Welcome to the **Biometric Forensic Identification Platform**! If this is your first time collaborating on a big project using Git and GitHub, **do not worry!** This guide is built to help you contribute safely. 

Git can feel intimidating, but as long as you follow these rules, **you cannot physically break the main project!** Let's get started.

---

## 🛑 The "Golden Rules" of the Project
1. **Never commit passwords, API keys, or database URLs.** These go in your local `.env` file!
2. **Never type `git push -f` (Force Push).** If git tells you to force push, ask for help instead!
3. **Never work directly on the `main` branch.** Treat `main` like a glass display case. You don't build inside the case; you build in your workshop (a "branch") and then ask permission to put it in the case.

---

## 🐣 Step 1: Getting the Code on Your Computer
If you haven't downloaded the project yet, do the following:

1. Open your terminal.
2. Clone (download) the repository to your computer:
   ```bash
   git clone https://github.com/HarshVerma2705/identity.git
   ```
3. Navigate into the folder:
   ```bash
   cd identity
   ```
*(Note: Because this project uses Node and React, make sure to run `npm install` inside the `frontend` and `backend` folders to download all the local packages).*

---

## 🎯 Step 2: Finding Something to Work On (Issues)
We use the **Issues** tab on GitHub like a To-Do list.
1. Browse open issues on GitHub.
2. Comment: *"I would like to work on this!"* to claim it. 
3. **Why?** This prevents two people from accidentally wasting time building the same exact feature!

---

## 🔀 Step 3: Making Your Safe Workspace (Branching)
Now that you know what to build, you need a safe bubble to build it in. This is called a **Branch**.

```bash
# 1. ALWAYS make sure your local computer's main branch is up-to-date!
git checkout main
git pull origin main

# 2. Create and switch to your isolated feature branch
# Convention: Use 'feature/' for new code, or 'bugfix/' for errors
git checkout -b feature/login-screen
```
*You are now in your bubble! Write all the code you want here. Even if nothing works, it won't affect anyone else.*

---

## 💾 Step 4: Saving Your Checkpoints (Committing)
As you write code, save "checkpoints". We call these commits. 

```bash
# Check what files you have modified
git status

# Stage the file(s) you want to save to your checkpoint
git add frontend/src/components/Login.jsx
# (Or use `git add .` to save everything you've changed)

# Label your checkpoint with a very clear, descriptive message
git commit -m "feat: add user authentication form to Login component"
```

**What labeling prefix should you use?**
- `feat:` for a brand new feature or file.
- `fix:` for squashing a bug.
- `style:` for CSS updates.
- `docs:` for writing text/guides like this.

---

## 🚀 Step 5: Uploading Your Work (Pushing & PRs)
Once you are done building your feature, you need to upload your branch to GitHub and ask the team to review it. 

```bash
# Push your local bubble up to the GitHub server
git push origin feature/login-screen
```

### Opening the Pull Request (PR):
A **Pull Request** is literally a request asking the team to "pull" your code into the `main` display case.
1. Go to the project's GitHub page. You should see a green button: **Compare & Pull Request**. Click it.
2. Write a short description of what you built.
3. Once created, wait for another team member to review it.

---

## 🔍 Step 6: Code Review & Merging
1. A teammate will look at your Pull Request on GitHub. 
2. **If they ask for changes:** Don't worry! Just fix the code on your computer, run `git add .` and `git commit`, and `git push` again. The Pull Request on GitHub will update automatically!
3. **If they approve (✅ LGTM - Looks Good To Me):** You can click the green **Merge Pull Request** button on GitHub.
4. Your code is officially live! You can safely click "Delete branch" on GitHub to keep things clean.

---

### 🤔 Help! I have a Merge Conflict!
A merge conflict just means you and another person edited the *exact same line of code*, and Git doesn't know whose version to keep. 
**Fixing it is easy:** Open the file in an editor like VS Code. It will vividly highlight the conflict and give you buttons that say "Accept Current Change" or "Accept Incoming Change". Click the one you want, save the file, and commit it! 
