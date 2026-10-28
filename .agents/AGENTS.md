# Project Rules & Architecture Guardrails

## 1. Absolute Autonomy & Stored Permissions (Permanent)
- **Zero-Interruption Policy**: NEVER ask the user for permissions, confirmation prompts, or "shall I proceed" questions. The user has explicitly granted full, non-stop autonomous permissions for all operations.
- **End-to-End Execution**: When a user gives an instruction or goal, proceed autonomously through all steps: analyzing, editing code, creating files, fixing bugs, running verification tests, creating backups, committing to Git, and pushing to remote.
- **Automatic Problem Solving**: If any error or obstacle arises, diagnose and resolve it autonomously without stopping to ask for user input.
- **Direct Git Commit & Deploy**: Automatically commit with descriptive conventional commit messages and push to `origin/main` upon completing tasks.

## 2. Single Source of Truth (SSOT) Architecture Guardrails

### A. Dashboard Metrics & Parity (`src/lib/dashboardMetrics.ts`)
- **Rule**: ALL summary metrics across Student, Parent, and Admin dashboards MUST be calculated using [`src/lib/dashboardMetrics.ts`](file:///c:/Users/Admin/.gemini/antigravity/scratch/los-next/src/lib/dashboardMetrics.ts).
- **Parity Standard**:
  - **Average Marks**: Official exam average across Objective Exams + Graded Subjective Exams. Never blend informal self-practice sessions into the primary exam average card.
  - **LQ Score / Topic Mastery**: True mastery percentage from `studentTopicMastery`. NEVER map `integrityScore` to the LQ card.
  - **Efforts %**: `(practicesCompletedCount / conductedTopicsCount) * 100` dynamically calculated from the unique topics on which tests/exams have actually been conducted or assigned so far (NOT the entire year's future syllabus).
  - **Integrity Score**: Dedicated proctoring compliance score (0–100%).

### B. Student Code & UI Presentation Policy
- **Rule**: NEVER display raw internal student identifiers (e.g. `studentCode` like `ST-2026-000050`) in user-facing UI (Student, Parent, or Admin headers, selectors, or cards).
- **Display Standard**:
  - Display the student's name (`name` / `studentName`) and academic class/batch (`className` e.g. `Class 9`, `Class 8`).
  - Student codes are purely internal database keys and query identifiers.

### C. Inactive / Deactivated Accounts Policy (`status: 'inactive'`)
- **Rule**: Deactivated student accounts (`status: 'inactive'`) and parents linked solely to deactivated students MUST be excluded from all active loops:
  - **Student Registry (`/admin/students`)**: Must default to `Active Only`.
  - **Chat & Communications (`/api/chat`)**: Excluded from active DM lists, class batch group participant arrays, and the "Start DM" selection drawer.
  - **Attendance Rosters**: Excluded from active class marking.
  - **Live Exam Monitoring / Notifications**: Excluded from active student loops.

### D. User Query Resolution (`role === 'student'`)
- **Rule**: When querying user documents by `studentCode`, ALWAYS include `.where('role', '==', 'student')` and verify `data.role === 'student'`.
- **Rationale**: Both student and parent profiles share the `studentCode` field in Firestore. Omitting the role check causes parent records to overwrite student records (e.g. parent name appearing on absent notices).
- **Absent Notifications**: Attendance alerts MUST always use the student's name (e.g. `Adhira Sumit Warge`), never the parent's name.

### E. Chat & Communication SSOT (`src/app/api/chat/route.ts`)
- **Rule**:
  - **Direct Messages**: The sidebar under Direct Messages MUST list **only existent communications** (channels that have actual message exchanges with a valid `lastMessage`). Never list 0-message empty placeholders.
  - **Sorting**: All conversations (Class Groups and DMs) MUST be sorted with the **latest communication on top** (`lastMessage.timestamp` descending).
  - **Unread Notification**: Unread message counts MUST be rendered with a high-visibility badge counter bubble.

### F. Topic Mastery & Diagnostic Breakdown (`src/lib/studentDb.ts`)
- **Rule**: Topic mastery categorization and explanation logic must remain completely synchronized across Student, Parent, and Admin views:
  - 🟢 **Mastered**: Mastery $\ge 90\%$ AND Confidence $\ge \text{requiredConfidence}$ (Minor/Micro: 12, Medium/Conceptual: 18, Major/HOTS: 24 questions; computed via `getRequiredConfidence`).
  - 🟡 **In Progress / Practicing**: Mastery between $50\%$ and $89\%$ (or $\ge 90\%$ with confidence $< \text{requiredConfidence}$).
  - 🔴 **Needs Attention**: Mastery $< 50\%$ or missed scheduled exam unattempted.
  - Status dot badges (`🟢`, `🟡`, `🔴`) clicked by an admin MUST open a breakdown modal showing the exact same diagnostic guidance and explanation string displayed on the student's dashboard.

### G. Attendance & Leave Calculation (`src/lib/attendanceUtils.ts`)
- **Rule**: ALL attendance stats (total days, effective present days, leaves, late arrivals, percentage) MUST be computed via `calculateAttendanceSummary` in [`src/lib/attendanceUtils.ts`](file:///c:/Users/Admin/.gemini/antigravity/scratch/los-next/src/lib/attendanceUtils.ts).
- Never implement ad-hoc attendance loops in individual route files.

### H. Proctoring & Integrity Scoring (`src/lib/proctoring.ts`)
- **Rule**: ALL integrity penalty calculations MUST use `calculateProctoringIntegrityScore` in [`src/lib/proctoring.ts`](file:///c:/Users/Admin/.gemini/antigravity/scratch/los-next/src/lib/proctoring.ts).
- Penalties: Tab switch (-10 pts), Multiple faces (-15 pts), No face (-10 pts), Gaze away (-5 pts), Head movement (-5 pts).

### I. Date & Time Standardization (`src/lib/dateUtils.ts`)
- **Rule**: All scheduling, attendance dates, daily exams, and streak keys MUST use Asia/Kolkata (IST) via `getDateKeyIST` or `formatDateIST` in [`src/lib/dateUtils.ts`](file:///c:/Users/Admin/.gemini/antigravity/scratch/los-next/src/lib/dateUtils.ts).
- Never use raw UTC `toISOString().split('T')[0]` for India-scheduled dates (causes midnight shift bugs).

### J. Question Bank & Exam Deduplication (`src/lib/questionSimilarity.ts`)
- **Rule**: Automated question generation and lottery algorithms MUST utilize `isNearDuplicateQuestion` in [`src/lib/questionSimilarity.ts`](file:///c:/Users/Admin/.gemini/antigravity/scratch/los-next/src/lib/questionSimilarity.ts) to prevent questions that differ by only 1–2 filler words from being duplicated.

### K. Question Code & Type Standards (`src/lib/questionTypes.ts`)
- **Rule**: ALL questions in the Question Bank MUST follow the standard naming convention:
  `${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}-${typeCode}-${sequence}`
  *(e.g., `CBSE-8-MGP1-3-3.1-OMC-001`, `MH-10-SCIT1-1-1.1-OSC-031`)*.
- **Canonical Question Type Codes**:
  - **Objective Types**:
    - `OSC`: Single Choice MCQ (default 4 marks)
    - `OMC`: Multiple Choice MCQ (default 4 marks)
    - `OTF`: True / False (default 4 marks)
    - `OAR`: Assertion & Reason (default 4 marks, valid options `A`, `B`, `C`, `D`)
    - `OFB`: Fill in the Blanks (default 4 marks)
    - `ONE`: Numerical Objective (default 4 marks, $\pm 0.05$ tolerance)
  - **Subjective Types**:
    - `SDF`: Definition (1 mark)
    - `SLP`: Laws & Principles (1 mark)
    - `SSA`: Short Answer (2 marks)
    - `SSR`: Scientific Reasoning / Short Notes (2 marks)
    - `SSN`: Numerical Short (2 marks)
    - `SLA`: Long Answer (4 marks)
    - `SLN`: Numerical Long (4 marks)
- **Mathematical Text & KaTeX Standard**:
  - ALL mathematical expressions, formulas, and symbols MUST use `preprocessMathText` and `formatRichText` in [`src/lib/questionTypes.ts`](file:///c:/Users/Admin/.gemini/antigravity/scratch/los-next/src/lib/questionTypes.ts).
  - Delimiters: Inline `\(...\)`, Display `\[...\]`. Never raw un-escaped double backslashes or corrupted fractions.

### L. Syllabus & Topic Hierarchy SSOT (`syllabus` & `syllabusTopicIndex`)
- **Rule**: All syllabus chapters, topics, and subtopics across CBSE and Maharashtra Board MUST strictly follow official textbook curricula (NCERT NCF-SE for CBSE Classes 8–10; Balbharti for Maharashtra Board Classes 8–10).
- **Canonical Board & Subject Code Standards**:
  - **CBSE Class 8**: `CBSE-8-MGP1` (*Ganit Prakash 1*), `CBSE-8-CURI` (*Curiosity*)
  - **CBSE Class 9**: `CBSE-9-MGM` (*Mathematics - Ganita Manjari*), `CBSE-9-SCIE` (*Science - Exploration*)
  - **CBSE Class 10**: `CBSE-10-MATH` (*Mathematics*), `CBSE-10-SCI` (*Science*)
  - **MH Class 8**: `MH-8-SCI` (*General Science*)
  - **MH Class 9**: `MH-9-MTH1` (*Algebra*), `MH-9-MTH2` (*Geometry*), `MH-9-SCIT` (*Science & Technology*)
  - **MH Class 10**: `MH-10-MTH1` (*Algebra*), `MH-10-MTH2` (*Geometry*), `MH-10-SCIT1` (*Science & Tech Part 1*), `MH-10-SCIT2` (*Science & Tech Part 2*)
- **Topic Code Standard**: `${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}` (e.g. `CBSE-8-MGP1-3-3.1`, `MH-10-SCIT1-1-1.1`).
- **Question Bank Linking & 100% Mapping**:
  - ALL question documents in the `questions` collection MUST store a canonical `topicCode` matching an indexed document in `syllabusTopicIndex`.
  - Any addition or modification to the `syllabus` collection MUST be followed by an index rebuild (`/api/admin/syllabus/rebuild`) to maintain zero orphaned or unmapped questions across practice and exam modules.

### M. Exam Architecture & Evaluation Standards (`src/services/attempt.service.ts`)
- **Rule**:
  - **Objective Exams**: Evaluated synchronously via `AttemptService.submitAttempt` against `evaluateQuestionAnswer`. Disputed/quarantined questions are excluded pro-rata without penalizing student score or topic mastery.
  - **Subjective Exams**: Evaluated via teacher final review or structured peer review with model answers (`solution` or `answerLines`).
  - **Proctoring Penalties**: Computed only via `calculateProctoringIntegrityScore`.

### N. Adaptive Practice & Mastery Engine (`src/services/practice.service.ts`)
- **Rule**:
  - **Adaptive Difficulty Selection**:
    - Mastery $< 30\%$: 70% Easy, 30% Medium
    - Mastery $30–59\%$: 50% Easy, 50% Medium
    - Mastery $60–84\%$: 20% Easy, 50% Medium, 30% Hard
    - Mastery $\ge 85\%$: 10% Easy, 40% Medium, 50% Hard
    - High-flyer rule: Mastery $\ge 80\%$ with $< 15$ attempts triggers 100% Hard mode.
  - **Mastery Criteria**: Requires verified attempts $\ge \text{requiredConfidence}$ (Minor: 6, Medium: 10, Major: 15) and $\ge 90\%$ accuracy for Green Mastered status.
  - **Option Integrity**: All MCQs served in practice sessions MUST have $\ge 2$ valid options. Corrupted entries with missing options must be automatically filtered out.

### O. Scorecard & Review Modal Question Hydration (`src/components/ScorecardModal.tsx` & `/api/student/results`)
- **Rule**:
  - **Question Text Display**: Scorecards MUST ALWAYS render the full question text (`text` / `questionText`) formatted with `preprocessMathText`. The question code must only appear as a subtle badge/subtitle — NEVER as a replacement for the question text.
  - **Question Hydration Pipeline**:
    - Objective Exams: Hydrate questions from the `exams` collection, `questions` collection (querying by document IDs AND `questionCode`), and `reviewData.questionDetails`.
    - Practice Sessions: `PracticeService.submitPracticeGrade` MUST store full `questionDetails` and `questions` in `parentReviews`. When loading practice scorecards, fallback dynamically to `practiceSubmissions` if `parentReviews` lacks question details.
  - **Options & Answers Mapping**:
    - Always display option-matched text for both student answers and correct answers (translating letters/indices to option strings).
    - Always render the question explanation/solution (`solution` / `explanation`) if present.

### P. Live Syllabus Synchronization with Question Bank & Exam Generator (`/api/admin/exams/generate` & `/api/admin/syllabus`)
- **Rule**: ALL subject cascading and selector hierarchies across **Create Question Bank** (`/admin/create-qb`), **Exam Generator** (`/admin/exam-generator`), **Create Exam** (`/admin/create-exam`), and **Question Bank** (`/admin/question-bank`) MUST be dynamically constructed in real-time from the live `syllabus` collection in Firestore.
- **Zero-Lag Availability**:
  - Whenever a new subject or curriculum hierarchy is added in **Syllabus Manager** (`/admin/syllabus`), it MUST immediately appear in all subject selection checkboxes in Create Question Bank and Exam Generator without requiring manual re-indexing or static file rebuilds.
  - `/api/admin/exams/generate` MUST dynamically aggregate subjects and board/subject code maps directly from `adminDb.collection('syllabus').get()`.
  - All subject mutation endpoints (`POST`, `PUT`, `DELETE` in `/api/admin/syllabus/route.ts`) MUST automatically sync `config/syllabusSubjects`, `config/boardCodes`, and `config/subjectCodes` on write.

### Q. Mandatory Pre-Mutation Automated Snapshot Engine (`src/lib/backupUtils.ts`)
- **Rule**: NO maintenance script, migration, data harmonizer, bulk deletion, or bulk update may execute without first creating an atomic point-in-time snapshot of targeted collections via `createPreMutationSnapshot(...)`.
- **Requirements**:
  - All snapshots must be saved to `backups/snapshots/` with timestamp, reason, collection document counts, and logged in `_systemBackups`.
  - Every destructive or bulk database modification MUST be reversible via `restoreSnapshot(...)` / `node scripts/db-restore.js`.

### R. Strict Single Source of Truth (SSOT) Canonical Entity Invariants
- **Rule**: Every core entity MUST have ONE AND ONLY ONE canonical identifier format across the entire codebase:
  - **`studentCode`**: Strictly `ST-YYYY-XXXXXX` (e.g. `ST-2026-000001`).
  - **`topicCode`**: Strictly `${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}` (e.g. `MH-8-MTH1-3-3.1`, `CBSE-8-MGP1-1-1.1`).
  - **`questionCode`**: Strictly `${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}-${typeCode}-${sequence}` (e.g. `MH-8-MTH1-3-3.1-OSC-001`).
  - **`boardCode`**: Strictly `CBSE` or `MH` (never full string variations like `MAHARASHTRA BOARD` in database keys).
  - **`subjectCode`**: Strictly official curriculum codes (`MGP1`, `CURI`, `MGM`, `SCIE`, `MATH`, `SCI`, `MTH1`, `MTH2`, `SCIT1`, `SCIT2`, `SCIT`).
- **Single Method Invariant**: Never implement parallel, competing, or alternate query methods for the same business logic. All components must consume the single canonical SSOT utility.

### S. Proctoring Interruption Coalescing & Mobile Lifecycle SSOT (`src/hooks/useLiveExam.ts`)
- **Rule**: All tab switch, window blur, and fullscreen exit event tracking MUST be exclusively owned and debounced by `useLiveExam.ts`.
- **Interruption Coalescing**:
  - A single incoming phone call, OS notification, or heads-up dialer interruption MUST count as only **1 violation incident**.
  - `isCurrentlyAwayRef` must prevent duplicate increments while the student is continuous away.
  - A 10-second coalescing window and 5-second post-return stabilization buffer must be strictly maintained.
  - `useProctoring.ts` must NEVER duplicate `setTabViolations` calls in its `onViolation` callback.

### T. Topic Practice Quotas & Dynamic UI Presentation
- **Rule**: Practice set limits MUST dynamically reflect the topic's true scope:
  - **Minor / Micro Topics**: Max 2 Practice Sets ($2 \times 6 = 12$ Qs max, target: 12 Qs).
  - **Medium / Conceptual Topics**: Max 3 Practice Sets ($3 \times 6 = 18$ Qs max, target: 18 Qs).
  - **Major / HOTS Topics**: Max 4 Practice Sets ($4 \times 6 = 24$ Qs max, target: 24 Qs).
- **UI Copy Standard**: NEVER display hardcoded `/5 practices` or `5/5 practices done` in any UI component, diagnostic badge, or explanation banner. Always render dynamic targets `${practiceCount}/${maxPractices} practices`.




### U. Strict Zero-Cost Cloud & Network Egress Invariants (`src/lib/costGuard.ts`)
- **Rule**: Total Google Cloud and Firestore network egress MUST strictly remain within Google Cloud's **10 GB/month 100% Free Tier** ($₹0.00$ cost invariant).
- **No Heavy Blobs in Real-Time Collections**:
  - NEVER store base64 images, audio/video data URLs, or raw binary blobs in real-time collections (`liveExamSessions`, `chatMessages`, `notifications`).
  - Real-time Firestore listeners (`onSnapshot`) re-transmit the entire document on every single update. Storing media in real-time documents causes exponential egress multiplication ($> 20\text{ GB/month}$), triggering `Cloud Firestore Internet Data Transfer Out from APAC to APAC` bills under the App Engine parent category.
- **Segregated On-Demand Evidence Collection (`liveExamEvidence`)**:
  - Real-time session documents MUST contain ONLY lightweight metadata and numeric counters (`proctoringSnapshotCount: number`, `manualCaptureCount: number`).
  - Heavy evidence, photos, and manual captures MUST be written to the segregated `liveExamEvidence` collection and loaded strictly on-demand via single `getDoc` calls when an admin explicitly opens the Evidence modal.
- **Proctoring Image Compression Standard**:
  - All automated camera snapshots MUST use `captureCameraSnapshot(videoEl, 160, 0.22)` in [`src/hooks/useProctoring.ts`](file:///c:/Users/Admin/.gemini/antigravity/scratch/los-next/src/hooks/useProctoring.ts).
  - Payloads must never exceed $12\text{ KB}$ per image.
- **Automated Evidence Purge (`src/lib/purgeUtils.ts`)**:
  - Expired `liveExamEvidence` documents must be purged automatically at midnight via `purgeExpiredProctoringSnapshots` so evidence never accumulates long-term storage or egress costs.
- **No Paid Crons in Vercel**:
  - Vercel paid cron jobs (`vercel.json`) are strictly forbidden. All maintenance sweeps must be opportunistic or triggered via manual admin action.

### V. Automated Cost & Egress Early Warning System (`src/lib/costGuard.ts`)
- **Rule**: All real-time Firestore mutations MUST be guarded by `sanitizeRealTimePayload` and `inspectPayloadCostSafety`.
- **Payload Inspection Ceiling**:
  - Maximum allowable payload for real-time streamed documents is **$30\text{ KB}$**.
  - Any document write exceeding $30\text{ KB}$ triggers an immediate `[COST GUARD WARNING]` and dispatches an `app:cost-warning` browser event.
- **Active Interception**:
  - `sanitizeRealTimePayload` automatically strips rogue `proctoringSnapshots` or `manualCaptures` arrays if accidentally passed to `createLiveSession` or `updateLiveSession`, converting them to numeric counts to safeguard the project from unexpected billing.
- **Google Cloud Budget Alert**:
  - A budget alert threshold at **$₹100$** with email notifications MUST remain active on Google Cloud Billing account `010A2C-9022DA-A6231A` to proactively alert administrators of any unauthorized cloud spending.

### W. Deduplication & Zero Dead Export Invariants
- **Rule**:
  - Zero duplicate types across schemas and views. Canonical types MUST be imported from `@/types/`.
  - Zero unused or dead exports in `src/lib/`, `src/services/`, and `src/hooks/`.
  - Static, batch, and syllabus lookups MUST consume in-memory caches (`getCachedBatches`, `getCachedSyllabusByClass`) to eliminate redundant Firestore document reads.

### X. On-Demand Proctoring & Zero Idle Streaming Invariant (`useLiveExam.ts` & `live-exam-monitor`)
- **Rule**: Live exam session document updates MUST be strictly gated by active admin presence (`proctorPresence` in Firebase Realtime Database):
  - **Zero Idle Syncing**: If NO admin is actively viewing `/admin/live-exam-monitor`, student exam clients MUST NEVER write periodic heartbeats, away-time ticks, or question progression metrics to `liveExamSessions`.
  - **Local In-Memory Tracking**: Violations, time-away, and exam metrics are tracked locally in React client memory and submitted once at exam completion via `submitAttempt`.
  - **Automatic Visibility Disconnection**: When an admin minimizes or switches away from the Live Exam Monitor tab, the Firestore `onSnapshot` listener and RTDB presence MUST immediately disconnect via `document.addEventListener('visibilitychange')`.
  - **On-Demand Activation**: When an admin opens or views the monitor, student clients immediately detect presence, flush their current state, and stream live metrics only for the duration of the admin's active session.
  - **Evidence Segregation**: Camera snapshots are compressed to $\le 12\text{ KB}$ and saved strictly to `liveExamEvidence`, completely decoupled from real-time session documents.
