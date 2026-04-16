# Biometric App - Contributor Roles & Task Division

Welcome to the Biometric Forensic Identification Platform! To make collaboration easier, the work can be divided across the following user roles/teams based on the existing folder structure.

## 1. Frontend Team (UI/UX)
**Working Directory:** `frontend/`
**Tech Stack:** React, Vite, CSS/SCSS

**Responsibilities:**
- **UI Components:** Build reusable, responsive components (buttons, input fields, navigation bars) inside `frontend/src/components/`.
- **Pages & Routing:** Wire up the UI flows for `LoginPage`, `UploadVictim`, `ViewVictims` and `MatchResult`.
- **API Integration:** Connect the React interface with backend APIs through the functions in `frontend/src/services/` (authService, victimService, etc.).
- **Auth State:** Implement protected routing so only authenticated forensic/admin users can view dashboard items.

## 2. Backend Team (Core API)
**Working Directory:** `backend/`
**Tech Stack:** Node.js, Express (or FastAPI)

**Responsibilities:**
- **Auth System:** Finish writing secure authentication using JWT, handling the login, registration, and logout flows. Include proper error handling `try/catch`.
- **Victim & Missing Person APIs:** Create CRUD endpoints to receive uploads of victim biometrics and store them.
- **Data Validation:** Validate incoming API payloads to ensure high data integrity.
- **Integration:** Expose endpoints for the frontend team to consume.

## 3. Database & Architecture Team
**Working Directory:** `database/`
**Tech Stack:** PostgreSQL, MongoDB

**Responsibilities:**
- **Schema Design:** Define the database models for Users, Victims, Missing Persons, and Match Logs.
- **Migrations & Seeding:** Maintain migration scripts so developers can easily sync their local database structures.
- **Optimization:** Create indexes for fast lookup (especially important when comparing multiple biometric signatures).

## 4. Notifications & Communication Team
**Working Directory:** `notifications/`
**Tech Stack:** Node.js Mailer (e.g., Nodemailer)

**Responsibilities:**
- **Email Service:** Implement `emailService.js` to dispatch emails securely using environment variables for the mail server/API keys.
- **Templates:** Design and refine the HTML templates like `matchFound.html` and `updateStatus.html` with responsive styles.
- **Event Triggers:** Connect this service to the Backend API so emails are automatically sent to family members or handlers when a biometric match hits a high confidence threshold.

---

### Best Practices for Git Workflow

To ensure no code conflicts occur when multiple contributors are working simultaneously:

1. **Never commit directly to `main` or `master`.**
2. **Feature Branches:** Have contributors create their own branch according to their task, for example: `git checkout -b feature/frontend-login`.
3. **Pull Requests (PRs):** Once their feature is done, push up their branch (`git push origin feature/frontend-login`) and open a Pull Request for exactly one or two other users to review.
4. **Frequent Commits:** Commit code in small logical chunks.
