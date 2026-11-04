# LOS-Next — Audit Completion & Continuity Record
**Repo:** yashcomapp/ai | **Branch:** main | **Latest commit:** d6a267e
**Stack:** Next.js 14 + TypeScript + Firebase Firestore + Vercel
**Product:** Learning OS for CBSE/MH students (Classes 8-10)
**Modes:** Regular (parent review) | Autonomous (reflection gate) | Limited (no LOS)

## The Two Goals (in order)
1. Reduce Firebase read cost (was approaching 10 GB/month free tier)
2. Improve pedagogical value (especially for Autonomous students)

## What's been shipped and verified

### Phase 0 — Cost + Security (DONE)
- C7: practiceTracks bounded by batchId/date range, 30-day window
- C8: verifyAnyRole custom-claims fast-path (0 reads for admin/parent)
- C3: parent dashboard queries bounded (.limit(100), scheduledDate >=)
- C1: student learning queries bounded (.limit(100), dropped subjectiveAttempts)
- R1/R2: liveExamSessions/liveExamEvidence field allowlists (server-only integrity)
- R7: FCM tokens removed from client-writable users allowlist
- P2/P4: "Start Here" banner + micro progress bars on student learning page
- 5 new composite indexes added

### Phase 1 — Structural Pipeline Sharing (DONE)
- C2: loadStudentCoreData shared 60s cache (12 queries → 1 cache hit)
- C4: assignment docs now carry topicCode/topicCodes/title/subject/chapter
- C5: ReportCacheManager L1+L2 scorecard cache (180s TTL)
- C9: getAssignmentsForBatches .select() projection (~40% egress)
- Lever 1: Autonomous reflection gate
  - Detects wrongCount > 0 && scorePercent < 80
  - Flags parentReviews with reflectionRequiredByGate
  - Gates next practice set on reflection completion
  - Tier 2 validation: 25-350 chars, banned phrases, repetitive char check
  - 6 categories: conceptual_misunderstanding, calculation_error, misread_question,
    silly_mistake, over_thinking, guessed
  - PracticeLockPrompt.tsx with LaTeX + category pills + char counter

### P1.5 — Verification & Polish (DONE)
- 'status' removed from student allowlists on BOTH reviews and parentReviews
  (was the highest-risk security item — students cannot bypass parent review)
- Mode-isolated cache key: student_core_${code}_${isLimited ? 'lim' : 'full'}
- deriveStudentBatchIds(userData) SSOT helper used by both callers
- getAssignmentsForBatches projection expanded (subject, chapter, chapterName)
- Parent reflection actionableSummary (0 extra reads, piggybacks on parentReviews)
- S22: tests now import REAL functions (not copies) via scripts/ts-loader.js
  - 50/50 invariants test the actual production code

### Phase 2 (P1) & In-Depth Audit Fixes (DONE — `d6a267e`)
- Live Proctoring Rules Allowlist Expanded:
  `['lastActive', 'lastHeartbeat', 'currentQuestionIndex', 'answeredCount', 'violations', 'awaySeconds', 'awayTimeTotal', 'proctoringSnapshotCount', 'manualCaptureCount', 'proctoringSnapshotsExpiresAt', 'proctoringSnapshotsPurgedAt', 'updatedAt', 'status']`.
- Leave-Declaration Guard Restored:
  Regular mode students blocked from self-declaring leave via HTTP 403.
- Rate-Limit Query Resilience:
  Wrapped in try/catch to avoid 500 errors.
- 3 Missing Composite Indexes Deployed to Production:
  - `attendanceDeclarations`: `studentCode` ASC, `createdAt` ASC
  - `parentReviews`: `studentCode` ASC, `topicCode` ASC, `type` ASC, `createdAt` DESC
  - `subjectiveAttempts`: `studentCode` ASC, `submittedAt` DESC
- Hardcoded Password Removed:
  Default `Yashcom@26` removed from registration client form; `/api/register` makes password optional and derives securely from DOB.
- Canonical SSOT Mode Helper:
  `src/app/api/student/handlers/practice.ts:132` migrated to `getStudentMode(student.userData) === 'autonomous'`.
- Projection Hardening:
  `lateEntryRestriction`, `createdBy`, and `updatedAt` added to `getAssignmentsForBatches` `.select(...)`.
- Anti-Rushing Guard (P7):
  Client deliberation warning modal at <15s/Q; server fluency check voids only if <18s/Q AND score <50%.
- Gitignore Sanitized:
  `audit-*`, `*.snapshot`, and full codebase txt files ignored.

## What's verified as working
- 50/50 business invariants pass on real code
- 9/9 Phase 1 invariants pass
- npm run build: exit 0 across all 61 routes
- Firebase deploy: Rules & Indexes deployed to default database (`ai-yashcom`)

## Scale viability
- Reads per student per day: ~600
- 2,000 students < $15/month
- Real-time egress < 30 KB ceiling (Rule 2.U & 2.V)
