# Project Rules & Architecture Guardrails

## 1. Command Permissions
- The agent has permanent permission to run `npm run build` directly. Always run this command with `run_command` without asking for user approval.

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
  - 🟢 **Mastered**: Mastery $\ge 90\%$ AND Confidence $\ge 20$ questions (or `isRecoveryMastered === true`).
  - 🟡 **In Progress / Practicing**: Mastery between $50\%$ and $89\%$ (or $\ge 90\%$ with confidence $< 20$).
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
  - **Mastery Criteria**: Requires $\ge 20$ attempts and $\ge 90\%$ accuracy for Green Mastered status.
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
  - Every destructive or bulk database modification MUST be reversible via `restoreSnapshot(...)` / `npm run db:restore`.

### R. Strict Single Source of Truth (SSOT) Canonical Entity Invariants
- **Rule**: Every core entity MUST have ONE AND ONLY ONE canonical identifier format across the entire codebase:
  - **`studentCode`**: Strictly `ST-YYYY-XXXXXX` (e.g. `ST-2026-000001`).
  - **`topicCode`**: Strictly `${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}` (e.g. `MH-8-MTH1-3-3.1`, `CBSE-8-MGP1-1-1.1`).
  - **`questionCode`**: Strictly `${boardCode}-${class}-${subjectCode}-${chapterNumber}-${topicNumber}-${typeCode}-${sequence}` (e.g. `MH-8-MTH1-3-3.1-OSC-001`).
  - **`boardCode`**: Strictly `CBSE` or `MH` (never full string variations like `MAHARASHTRA BOARD` in database keys).
  - **`subjectCode`**: Strictly official curriculum codes (`MGP1`, `CURI`, `MGM`, `SCIE`, `MATH`, `SCI`, `MTH1`, `MTH2`, `SCIT1`, `SCIT2`, `SCIT`).
- **Single Method Invariant**: Never implement parallel, competing, or alternate query methods for the same business logic. All components must consume the single canonical SSOT utility.



