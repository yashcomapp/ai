# LOS-Next — Audit Completion & Continuity Record
**Repo:** yashcomapp/ai | **Branch:** main | **Latest commit:** 4ebb479
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

## What's verified as working
- 50/50 business invariants pass on real code
- 9/9 Phase 1 invariants pass
- npm run build: exit 0 across all 61 routes
- Firestore rules deployed live to project ai-yashcom
- Estimated reads: ~600/student/day (down from ~1,745)
- Supports 2,000 students for <$15/month

## Open items (Phase 2) — in priority order

### P0 — Verify before declaring done
1. ✅ DONE: 'status' allowlist removal (verified in 4ebb479)
2. ✅ DONE: S22 test migration (real functions now tested)

### P1 — Security + structural (~1 day)
3. R3/R4: peerAssignments existence check in subjectiveReviews/evaluations create rules
   - Risk: student can create fake peer review for any peer
   - Fix: add exists() check on peerAssignments/{revieweeCode}_{studentCode}
4. R6: attendanceDeclarations daily cap (5/day) + reject startDate < today
   - Risk: spam + retroactive leave declarations
5. P7: pre-submit "take your time" warning at 15s/Q
   - Reduces rushed session voidance, pairs with 30-min cooldown
6. Verify QuotientService.calculateBulkQuotients is batched
   - If per-student: ~1,500 reads per practiceTracks call
   - Fix: chunkArray(studentCodes, 30) + .where('studentCode', 'in', chunk)
7. Verify PracticeLockPrompt receives full question objects (text, options, solution)
   - LaTeX rendering depends on this; if only IDs sent, UI is broken

### P2 — Refinements (~1 day)
8. Dedupe practiceSubmissions (mirror of parentReviews — 50% fewer practice writes)
9. Debounce live-exam-monitor listener detach (2-5 min)
10. Add chatRooms message cache in ChatContext
11. Cache classifyAssignedTopics result in loadStudentCoreData
12. Migrate studentCode write-on-read to one-time script

### P3 — Pedagogical depth (backlog)
13. Lever 3: conceptTags on questions + cross-topic diagnosis
14. Lever 2: Set 2 targets Set 1 misses (isomorphic transfer)
15. Gap 4: pre-exam warm-up set
16. Memory health card (SRS visible)

## Verification protocol for new AI sessions
- AI cannot fetch URLs, GitHub, or local files
- Paste code INLINE in message body (not attachment)
- Use format: ## FILE: path \n ```lang \n content \n ```
- Always paste from deployed source (firebase firestore:rules:get or git show commit:path)
- Local working copies may be stale — never trust them
- Scope one item per turn

## The most important learnings from this audit
1. Immediate retry on identical questions tests echo, not comprehension
   (Illusion of Competence — rejected P1 in favor of generative reflection)
2. Test copies of functions, not real code → real bugs pass (S22 fix)
3. CRLF vs LF on rules pastes caused two false-positives (always paste from deployed)
4. Mode-aware design: Regular has parent review, Autonomous needs system gate,
   Limited has no LOS access. One-size-fits-all pedagogy fails all three.
5. The dashboard (not learning page) was the biggest remaining read leak
   after C1/C3 — because C2 hadn't shipped yet at that time.
