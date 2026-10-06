'use client';

import React, { useState, useEffect, useRef, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useMathRender } from '@/hooks/useMathRender';
import { 
  preprocessMathText, 
  isOptionSelectedByUser, 
  isOptionCorrect,
  getQuestionCorrectAnswer,
  extractAssertionAndReason,
  isBlank, 
  getReasonForQuestion, 
  getRawOptionKey, 
  getRawOptionText, 
  parseAnswerList,
  formatUserAnswerSummary,
  isAssertionReasonType,
  isObjectiveType,
  DEFAULT_ASSERTION_REASON_OPTIONS
} from '@/lib/questionTypes';
import QuestionDisplay, { RichMathText } from '@/components/QuestionDisplay';
import { formatDateTimeIST, parseDateInput } from '@/lib/dateUtils';

interface QuestionDetailsItem {
  id: string;
  questionCode: string;
  qNumber?: number | null;
  text: string;
  type: string;
  options: any[];
  assertion?: string;
  reason?: string;
  solution?: string;
  difficulty: string;
  bloomLevel: string;
  userAnswer: string;
  isCorrect: boolean;
  correctAnswer: string;
  correctAnswers: string[];
  marks?: number;
  timeSpent?: number;
  durationSpent?: number;
  steps?: any[];
  evaluations?: any[];
  subjectCode?: string;
  topicCode?: string;
  chapterNumber?: string | number;
}

export interface DetailedScorecard {
  id: string;
  examId?: string;
  studentCode?: string;
  examCode: string;
  examName: string;
  examType: string;
  score: number;
  totalMarks: number;
  percentage: number;
  durationSpent: number;
  submittedAt: string | null;
  tabViolations: number;
  proctoringViolations: {
    noFace?: number;
    multipleFaces?: number;
    lookingAway?: number;
  };
  integrityScore: number;
  status: string;
  wrongAnswerReasons?: string[];
  questions: QuestionDetailsItem[];
  subject?: string;
  chapter?: string;
  topicName?: string;
  topicCode?: string;
  practiceNumber?: number | null;
  violations?: {
    screenshots?: string[];
  };
}

interface ScorecardModalProps {
  scorecard: DetailedScorecard | null;
  loading: boolean;
  onClose: () => void;
  actionButton?: React.ReactNode;
}

export default function ScorecardModal({ scorecard, loading, onClose, actionButton }: ScorecardModalProps) {
  const { user, firebaseUser } = useAuth();
  
  // View mode: Flashcard (default) vs Full List
  const [viewMode, setViewMode] = useState<'flashcard' | 'list'>('flashcard');
  const [questionFilterTab, setQuestionFilterTab] = useState<'needs_review' | 'incorrect' | 'unanswered' | 'correct' | 'all'>('needs_review');
  const [cardIndex, setCardIndex] = useState<number>(0);

  // Bookmarks State
  const [bookmarkedCodes, setBookmarkedCodes] = useState<Set<string>>(new Set());
  const [bookmarkLoading, setBookmarkLoading] = useState<string | null>(null);

  // 30-Second Partnership Sign-Off State (Pills)
  const [teachBackRating, setTeachBackRating] = useState<'confident' | 'good' | 'needs_help' | null>(null);
  const [notebooksChecked, setNotebooksChecked] = useState<boolean>(false);
  const [bagReady, setBagReady] = useState<boolean>(false);
  const [parentNote, setParentNote] = useState<string>('');

  // Interactive Review & 60-Minute Accountability State
  const isOfficialExam = scorecard?.examType !== 'practice' && scorecard?.examType !== 'entrance';
  const [reviewedQuestionIds, setReviewedQuestionIds] = useState<Set<string>>(new Set());
  const [challenges, setChallenges] = useState<Record<string, any>>({});
  const [reviewSubmitting, setReviewSubmitting] = useState<boolean>(false);
  const [reviewSubmittedSuccess, setReviewSubmittedSuccess] = useState<string | null>(null);

  // Time elapsed since exam submission
  const [elapsedMinutes, setElapsedMinutes] = useState<number>(0);
  const startTimeRef = useRef<number>(Date.now());

  // Challenge Dialog Modal
  const [challengeTargetQ, setChallengeTargetQ] = useState<QuestionDetailsItem | null>(null);
  const [challengeReason, setChallengeReason] = useState<string>('wrong_key');
  const [challengeSuggestedAnswer, setChallengeSuggestedAnswer] = useState<string>('B');
  const [challengeNotes, setChallengeNotes] = useState<string>('');

  // Questions needing review (strictly incorrect + unanswered)
  const questionsNeedingReview = useMemo(() => {
    return scorecard?.questions?.filter(q => !q.isCorrect || isBlank(q.userAnswer)) || [];
  }, [scorecard]);

  // Adjust default filter tab based on mistakes existence
  useEffect(() => {
    if (scorecard) {
      if (questionsNeedingReview.length > 0) {
        setQuestionFilterTab('needs_review');
      } else {
        setQuestionFilterTab('all');
      }
      setCardIndex(0);
    }
  }, [scorecard?.id, questionsNeedingReview.length]);

  // Fetch initial bookmarks for this student
  useEffect(() => {
    const fetchBookmarks = async () => {
      if (!firebaseUser) return;
      try {
        const token = await firebaseUser.getIdToken();
        const sCode = user?.studentCode || scorecard?.studentCode || '';
        const res = await fetch(`/api/student/bookmarks${sCode ? `?studentCode=${encodeURIComponent(sCode)}` : ''}`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        if (res.ok) {
          const data = await res.json();
          if (Array.isArray(data.bookmarks)) {
            const set = new Set<string>(data.bookmarks.map((b: any) => String(b.questionCode)));
            setBookmarkedCodes(set);
          }
        }
      } catch (err) {
        console.warn('Failed to fetch bookmarks:', err);
      }
    };
    fetchBookmarks();
  }, [firebaseUser, user?.studentCode, scorecard?.studentCode]);

  // Reading pacing timer (minimum reading seconds based on number of mistakes)
  const [reviewSecondsRemaining, setReviewSecondsRemaining] = useState<number>(0);

  useEffect(() => {
    if (!scorecard || questionsNeedingReview.length === 0) {
      setReviewSecondsRemaining(0);
      return;
    }
    const targetSeconds = Math.min(45, Math.max(10, questionsNeedingReview.length * 6));
    setReviewSecondsRemaining(targetSeconds);

    const interval = setInterval(() => {
      setReviewSecondsRemaining(prev => {
        if (prev <= 1) {
          clearInterval(interval);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [scorecard?.id, questionsNeedingReview.length]);

  useEffect(() => {
    if (scorecard?.submittedAt) {
      const compDate = parseDateInput(scorecard.submittedAt);
      if (compDate) {
        const diffM = Math.floor((Date.now() - compDate.getTime()) / 60000);
        setElapsedMinutes(Math.max(0, diffM));
      }
    }
  }, [scorecard]);

  // Dynamically load KaTeX and auto-render math expressions when scorecard changes or card changes
  useMathRender([scorecard, questionFilterTab, cardIndex, viewMode, challengeTargetQ]);

  const formatDate = (dateStr: string | null) => {
    return formatDateTimeIST(dateStr) || '-';
  };

  const formatDuration = (seconds: number) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m}m ${s}s`;
  };

  if (!scorecard && !loading) return null;

  const correctCount = scorecard?.questions && scorecard.questions.length > 0
    ? scorecard.questions.filter(q => q.isCorrect && !isBlank(q.userAnswer)).length
    : (scorecard?.score || 0);
  const incorrectCount = scorecard?.questions && scorecard.questions.length > 0
    ? scorecard.questions.filter(q => !q.isCorrect && !isBlank(q.userAnswer)).length
    : Math.max(0, (scorecard?.totalMarks || 0) - (scorecard?.score || 0));
  const unansweredCount = scorecard?.questions && scorecard.questions.length > 0
    ? scorecard.questions.filter(q => !q.isCorrect && isBlank(q.userAnswer)).length
    : 0;

  const filteredQuestions = scorecard?.questions?.filter(q => {
    const blank = isBlank(q.userAnswer);
    if (questionFilterTab === 'needs_review') return !q.isCorrect || blank;
    if (questionFilterTab === 'correct') return q.isCorrect && !blank;
    if (questionFilterTab === 'incorrect') return !q.isCorrect && !blank;
    if (questionFilterTab === 'unanswered') return !q.isCorrect && blank;
    return true;
  }) || [];

  const reviewedMistakesCount = questionsNeedingReview.filter(q => {
    const qId = q.questionCode || q.id;
    return reviewedQuestionIds.has(qId) || !!challenges[qId];
  }).length;

  const isReviewComplete = questionsNeedingReview.length === 0 || reviewedMistakesCount >= questionsNeedingReview.length;
  const canSubmitReview = isReviewComplete && reviewSecondsRemaining === 0;

  const remainingMins = Math.max(0, 60 - elapsedMinutes);
  const isWithin60Min = elapsedMinutes <= 60;

  // Toggle mark question as understood
  const toggleUnderstood = (qId: string) => {
    setReviewedQuestionIds(prev => {
      const next = new Set(prev);
      if (next.has(qId)) next.delete(qId);
      else next.add(qId);
      return next;
    });
  };

  // Toggle Bookmark
  const handleToggleBookmark = async (q: QuestionDetailsItem) => {
    const qCode = q.questionCode || q.id;
    if (!qCode || !firebaseUser) return;
    setBookmarkLoading(qCode);
    try {
      const token = await firebaseUser.getIdToken();
      const isCurrentlyBookmarked = bookmarkedCodes.has(qCode);
      
      // Optimistic update
      setBookmarkedCodes(prev => {
        const next = new Set(prev);
        if (isCurrentlyBookmarked) next.delete(qCode);
        else next.add(qCode);
        return next;
      });

      const res = await fetch('/api/student/bookmarks', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
          questionCode: qCode,
          questionText: q.text,
          subjectCode: q.subjectCode || scorecard?.subject,
          topicCode: q.topicCode || scorecard?.topicCode,
          chapterNumber: q.chapterNumber || scorecard?.chapter,
          examId: scorecard?.id,
          action: 'toggle'
        })
      });

      if (!res.ok) {
        // Revert on failure
        setBookmarkedCodes(prev => {
          const next = new Set(prev);
          if (isCurrentlyBookmarked) next.add(qCode);
          else next.delete(qCode);
          return next;
        });
      }
    } catch (err) {
      console.error('Bookmark toggle error:', err);
    } finally {
      setBookmarkLoading(null);
    }
  };

  // Submit challenge
  const handleSaveChallenge = () => {
    if (!challengeTargetQ) return;
    const qId = challengeTargetQ.questionCode || challengeTargetQ.id;
    setChallenges(prev => ({
      ...prev,
      [qId]: {
        questionId: qId,
        questionCode: challengeTargetQ.questionCode || qId,
        questionText: challengeTargetQ.text || '',
        reason: challengeReason,
        suggestedAnswer: challengeSuggestedAnswer,
        notes: challengeNotes
      }
    }));
    setReviewedQuestionIds(prev => new Set(prev).add(qId));
    setChallengeTargetQ(null);
  };

  // Submit full review
  const handleSubmitReview = async () => {
    if (!firebaseUser || !scorecard || !user) return;
    setReviewSubmitting(true);
    setReviewSubmittedSuccess(null);
    try {
      const token = await firebaseUser.getIdToken();
      const timeSpentSecs = Math.max(12, Math.floor((Date.now() - startTimeRef.current) / 1000));
      const sCode = (user.studentCode || scorecard.studentCode || '').trim().toUpperCase();
      let examId = scorecard.examId || scorecard.examCode || scorecard.id;
      if (examId && sCode && examId.toUpperCase().endsWith(`_${sCode}`)) {
        examId = examId.slice(0, examId.length - (sCode.length + 1));
      }

      const challengeList = Object.values(challenges);

      const res = await fetch('/api/student/exam-review', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
          examId,
          examName: scorecard.examName,
          reviewedQuestionIds: Array.from(reviewedQuestionIds),
          challenges: challengeList,
          timeSpentSeconds: timeSpentSecs,
          partnershipLog: {
            teachBackRating,
            notebooksChecked,
            bagReady,
            parentNote
          }
        })
      });

      const data = await res.json();
      if (res.ok) {
        setReviewSubmittedSuccess(
          data.message || (challengeList.length > 0 
            ? `✅ Verified review submitted with ${challengeList.length} question challenge(s)!` 
            : '✅ Verified review submitted successfully!')
        );
        if (scorecard) {
          scorecard.status = 'approved';
        }
      } else {
        alert('Error submitting review: ' + (data.message || 'Failed to submit review'));
      }
    } catch (err: any) {
      alert('Error submitting review: ' + err.message);
    } finally {
      setReviewSubmitting(false);
    }
  };



  // Total cards in Flashcard Mode: filtered questions + 1 final sign-off card
  const totalCards = filteredQuestions.length + 1;
  const isFinalCard = cardIndex === filteredQuestions.length;
  const currentQ = !isFinalCard && filteredQuestions[cardIndex] ? filteredQuestions[cardIndex] : null;

  return (
    <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.55)', backdropFilter: 'blur(5px)', WebkitBackdropFilter: 'blur(5px)', zIndex: 35000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '10px 8px' }}>
      <div className="modal-content" style={{ background: 'var(--surface-popover, #ffffff)', border: '1px solid var(--border-popover, #cbd5e1)', borderRadius: 'var(--radius-lg, 14px)', maxWidth: '920px', width: '100%', height: 'fit-content', maxHeight: '95vh', display: 'flex', flexDirection: 'column', overflowY: 'hidden', boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25)' }}>
        
        {/* Header */}
        <div className="modal-header" style={{ padding: '12px 18px', borderBottom: '1px solid var(--border-light, #e2e8f0)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft, #f8fafc)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
            <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 800, color: 'var(--text, #0f172a)' }}>
              📊 {scorecard?.examType === 'practice' ? 'Practice Review' : 'Exam Review & Reflection'}
            </h4>
            {scorecard?.examType === 'practice' && scorecard?.practiceNumber && (
              <span style={{ background: 'var(--accent, #4f46e5)', color: '#ffffff', fontSize: '11px', fontWeight: 800, padding: '3px 10px', borderRadius: '12px' }}>
                Practice #{scorecard.practiceNumber}
              </span>
            )}
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            {/* View Mode Toggle */}
            <div style={{ display: 'inline-flex', background: 'var(--bg, #f1f5f9)', padding: '2px', borderRadius: '8px', border: '1px solid var(--border-light, #cbd5e1)' }}>
              <button
                type="button"
                onClick={() => setViewMode('flashcard')}
                style={{
                  padding: '4px 10px',
                  fontSize: '11px',
                  fontWeight: 800,
                  borderRadius: '6px',
                  border: 'none',
                  cursor: 'pointer',
                  background: viewMode === 'flashcard' ? 'var(--accent, #4f46e5)' : 'transparent',
                  color: viewMode === 'flashcard' ? '#ffffff' : 'var(--text-muted, #64748b)',
                  transition: 'all 0.15s ease'
                }}
              >
                🗂️ Flashcard View
              </button>
              <button
                type="button"
                onClick={() => setViewMode('list')}
                style={{
                  padding: '4px 10px',
                  fontSize: '11px',
                  fontWeight: 800,
                  borderRadius: '6px',
                  border: 'none',
                  cursor: 'pointer',
                  background: viewMode === 'list' ? 'var(--accent, #4f46e5)' : 'transparent',
                  color: viewMode === 'list' ? '#ffffff' : 'var(--text-muted, #64748b)',
                  transition: 'all 0.15s ease'
                }}
              >
                📜 Full List
              </button>
            </div>

            <button className="close-modal" onClick={onClose} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.4rem', color: 'var(--text-muted, #64748b)', padding: '0 4px', lineHeight: 1 }}>✕</button>
          </div>
        </div>

        <div id="scorecard-details-section" className="modal-body math-container" style={{ padding: '14px 18px', overflowY: 'auto', flex: 1 }}>
          {loading && (
            <div style={{ textAlign: 'center', padding: '30px 0' }}>
              <div className="spinner" style={{ margin: '0 auto 12px' }}></div> Loading review scorecard...
            </div>
          )}

          {!loading && scorecard && (
            <div>
              {/* 60-Minute Accountability Banner for Official Exams */}
              {isOfficialExam && user?.role === 'student' && (
                <div style={{
                  background: isWithin60Min ? 'var(--warning-bg, #fefce8)' : 'var(--danger-bg, #fef2f2)',
                  border: `1px solid ${isWithin60Min ? 'var(--warning-border, #fde047)' : 'var(--danger-border, #fecaca)'}`,
                  borderRadius: 'var(--radius, 8px)',
                  padding: '8px 14px',
                  marginBottom: '12px',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  flexWrap: 'wrap',
                  gap: '6px'
                }}>
                  <div style={{ fontSize: '12px', color: isWithin60Min ? 'var(--text, #1e293b)' : 'var(--danger, #dc2626)', fontWeight: 600 }}>
                    {isWithin60Min ? (
                      <span>⏱️ <strong>60-Min Review Window:</strong> {remainingMins}m remaining to verify mistakes without being flagged in Fault Register!</span>
                    ) : (
                      <span>⚠️ <strong>Review Window Expired:</strong> {elapsedMinutes}m elapsed since exam. Review will be recorded as Late.</span>
                    )}
                  </div>
                  <div style={{ fontSize: '11px', color: 'var(--warning, #d97706)', fontWeight: 700 }}>
                    🏆 Spot question/key errors to earn +2 Diligence points!
                  </div>
                </div>
              )}

              {reviewSubmittedSuccess && (
                <div style={{ background: 'var(--success-bg, #f0fdf4)', color: 'var(--success, #16a34a)', border: '1px solid var(--success-border, #bbf7d0)', padding: '10px 14px', borderRadius: 'var(--radius, 8px)', fontSize: '13px', fontWeight: 700, marginBottom: '12px' }}>
                  {reviewSubmittedSuccess}
                </div>
              )}

              {/* Compact Summary Header Bar */}
              <div style={{ 
                background: 'var(--bg-soft, #f8fafc)', 
                padding: '10px 14px', 
                borderRadius: 'var(--radius, 8px)', 
                display: 'flex', 
                flexDirection: 'row', 
                flexWrap: 'wrap', 
                gap: '8px 18px', 
                marginBottom: '12px',
                border: '1px solid var(--border-light, #e2e8f0)'
              }}>
                {scorecard.subject && (
                  <div style={{ fontSize: '12px', lineHeight: '1.3' }}>
                    <strong style={{ color: 'var(--text-muted, #64748b)' }}>Subject:</strong>{' '}
                    <span style={{ fontWeight: 700 }}>{scorecard.subject}</span>
                  </div>
                )}
                {scorecard.chapter && (
                  <div style={{ fontSize: '12px', lineHeight: '1.3' }}>
                    <strong style={{ color: 'var(--text-muted, #64748b)' }}>Chapter:</strong>{' '}
                    <span style={{ fontWeight: 700 }}>{scorecard.chapter}</span>
                  </div>
                )}
                <div style={{ fontSize: '12px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted, #64748b)' }}>Score:</strong>{' '}
                  <span style={{ fontWeight: 800, color: scorecard.percentage >= 80 ? 'var(--success, #16a34a)' : scorecard.percentage >= 50 ? 'var(--warning, #d97706)' : 'var(--danger, #dc2626)' }}>
                    {scorecard.score} / {scorecard.totalMarks} ({scorecard.percentage}%)
                  </span>
                </div>
                <div style={{ fontSize: '12px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted, #64748b)' }}>Time Spent:</strong>{' '}
                  <span style={{ fontWeight: 700 }}>{formatDuration(scorecard.durationSpent)}</span>
                </div>
                <div style={{ fontSize: '12px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted, #64748b)' }}>Integrity:</strong>{' '}
                  <span style={{ fontWeight: 700, color: scorecard.integrityScore < 70 ? 'var(--danger, #dc2626)' : 'var(--success, #16a34a)' }}>
                    {scorecard.integrityScore} / 100
                  </span>
                </div>
              </div>

              {/* Filter Tabs Bar */}
              <div className="outcome-tabs" style={{ display: 'flex', gap: '6px', marginBottom: '12px', borderBottom: '1px solid var(--border-light, #e2e8f0)', paddingBottom: '8px', flexWrap: 'wrap', alignItems: 'center' }}>
                <button 
                  type="button"
                  onClick={() => { setQuestionFilterTab('needs_review'); setCardIndex(0); }} 
                  style={{
                    padding: '5px 12px',
                    fontSize: '12px',
                    fontWeight: 800,
                    borderRadius: '20px',
                    border: questionFilterTab === 'needs_review' ? '2px solid var(--warning, #d97706)' : '1px solid var(--border-light, #cbd5e1)',
                    background: questionFilterTab === 'needs_review' ? 'var(--warning-bg, #fefce8)' : 'transparent',
                    color: questionFilterTab === 'needs_review' ? 'var(--warning, #b45309)' : 'var(--text-muted, #64748b)',
                    cursor: 'pointer'
                  }}
                >
                  ⚠️ Mistakes Only ({questionsNeedingReview.length})
                </button>
                <button 
                  type="button"
                  onClick={() => { setQuestionFilterTab('incorrect'); setCardIndex(0); }} 
                  style={{
                    padding: '5px 12px',
                    fontSize: '12px',
                    fontWeight: 700,
                    borderRadius: '20px',
                    border: questionFilterTab === 'incorrect' ? '2px solid var(--danger, #dc2626)' : '1px solid var(--border-light, #cbd5e1)',
                    background: questionFilterTab === 'incorrect' ? 'var(--danger-bg, #fef2f2)' : 'transparent',
                    color: questionFilterTab === 'incorrect' ? 'var(--danger, #dc2626)' : 'var(--text-muted, #64748b)',
                    cursor: 'pointer'
                  }}
                >
                  Incorrect ({incorrectCount})
                </button>
                <button 
                  type="button"
                  onClick={() => { setQuestionFilterTab('correct'); setCardIndex(0); }} 
                  style={{
                    padding: '5px 12px',
                    fontSize: '12px',
                    fontWeight: 700,
                    borderRadius: '20px',
                    border: questionFilterTab === 'correct' ? '2px solid var(--success, #16a34a)' : '1px solid var(--border-light, #cbd5e1)',
                    background: questionFilterTab === 'correct' ? 'var(--success-bg, #f0fdf4)' : 'transparent',
                    color: questionFilterTab === 'correct' ? 'var(--success, #16a34a)' : 'var(--text-muted, #64748b)',
                    cursor: 'pointer'
                  }}
                >
                  Correct ({correctCount})
                </button>
                <button 
                  type="button"
                  onClick={() => { setQuestionFilterTab('all'); setCardIndex(0); }} 
                  style={{
                    padding: '5px 12px',
                    fontSize: '12px',
                    fontWeight: 700,
                    borderRadius: '20px',
                    border: questionFilterTab === 'all' ? '2px solid var(--accent, #4f46e5)' : '1px solid var(--border-light, #cbd5e1)',
                    background: questionFilterTab === 'all' ? 'var(--accent-soft, #eef2ff)' : 'transparent',
                    color: questionFilterTab === 'all' ? 'var(--accent, #4f46e5)' : 'var(--text-muted, #64748b)',
                    cursor: 'pointer'
                  }}
                >
                  All Questions ({scorecard.questions.length})
                </button>
              </div>

              {/* ============================================================ */}
              {/* MODE A: FLASHCARD SYSTEM (1 Question at a Time)               */}
              {/* ============================================================ */}
              {viewMode === 'flashcard' && (
                <div>
                  {/* Top Question Stepper Palette */}
                  <div style={{ display: 'flex', gap: '6px', overflowX: 'auto', paddingBottom: '10px', marginBottom: '12px', alignItems: 'center' }}>
                    {filteredQuestions.map((q, idx) => {
                      const isUnans = isBlank(q.userAnswer);
                      const isCur = cardIndex === idx;
                      const isUnderstood = reviewedQuestionIds.has(q.questionCode || q.id);

                      return (
                        <button
                          key={`step_${q.id || idx}_${idx}`}
                          type="button"
                          onClick={() => setCardIndex(idx)}
                          style={{
                            padding: '6px 12px',
                            borderRadius: '16px',
                            fontSize: '11.5px',
                            fontWeight: 800,
                            cursor: 'pointer',
                            display: 'flex',
                            alignItems: 'center',
                            gap: '4px',
                            flexShrink: 0,
                            border: isCur ? '2px solid var(--accent, #4f46e5)' : '1px solid var(--border-light, #cbd5e1)',
                            background: isCur 
                              ? 'var(--accent, #4f46e5)' 
                              : isUnans 
                                ? 'var(--bg-soft, #f8fafc)' 
                                : q.isCorrect 
                                  ? 'var(--success-bg, #f0fdf4)' 
                                  : 'var(--danger-bg, #fef2f2)',
                            color: isCur 
                              ? '#ffffff' 
                              : isUnans 
                                ? 'var(--text-muted, #64748b)' 
                                : q.isCorrect 
                                  ? 'var(--success, #16a34a)' 
                                  : 'var(--danger, #dc2626)',
                            transform: isCur ? 'scale(1.05)' : 'scale(1)',
                            transition: 'all 0.15s ease'
                          }}
                        >
                          <span>{isUnans ? '⚪' : q.isCorrect ? '🟢' : '🔴'}</span>
                          <span>Q{scorecard.questions.indexOf(q) !== -1 ? scorecard.questions.indexOf(q) + 1 : idx + 1}</span>
                          {isUnderstood && <span style={{ fontSize: '10px' }}>✓</span>}
                        </button>
                      );
                    })}

                    {/* Final Finish & Sign-off Step Pill */}
                    <button
                      type="button"
                      onClick={() => setCardIndex(filteredQuestions.length)}
                      style={{
                        padding: '6px 14px',
                        borderRadius: '16px',
                        fontSize: '11.5px',
                        fontWeight: 800,
                        cursor: 'pointer',
                        flexShrink: 0,
                        border: isFinalCard ? '2px solid var(--accent, #4f46e5)' : '1px solid var(--border-light, #cbd5e1)',
                        background: isFinalCard ? 'var(--accent, #4f46e5)' : 'var(--bg-soft, #f8fafc)',
                        color: isFinalCard ? '#ffffff' : 'var(--text, #1e293b)',
                        transform: isFinalCard ? 'scale(1.05)' : 'scale(1)',
                        transition: 'all 0.15s ease'
                      }}
                    >
                      🏁 Summary & Sign-off
                    </button>
                  </div>

                  {/* FLASHCARD BODY: Question Card OR Final Summary Card */}
                  {!isFinalCard && currentQ ? (() => {
                    const q = currentQ;
                    const isUnanswered = isBlank(q.userAnswer);
                    const qId = q.questionCode || q.id;
                    const isUnderstood = reviewedQuestionIds.has(qId);
                    const challenge = challenges[qId];
                    const isBookmarked = bookmarkedCodes.has(qId);
                    const timeSpentOnQ = q.timeSpent || q.durationSpent || 0;

                    // Telemetry Behavioral Clues
                    const isRushed = timeSpentOnQ > 0 && timeSpentOnQ < 8 && !q.isCorrect;
                    const isStruggled = timeSpentOnQ > 150;
                    const isFastFluency = q.isCorrect && timeSpentOnQ > 0 && timeSpentOnQ < 12;

                    return (
                      <div style={{
                        background: 'var(--surface, #ffffff)',
                        border: '2px solid var(--border-light, #e2e8f0)',
                        borderRadius: 'var(--radius-lg, 12px)',
                        padding: '16px 20px',
                        boxShadow: '0 4px 12px rgba(0, 0, 0, 0.05)',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '12px'
                      }}>
                        {/* Top Card Bar */}
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light, #e2e8f0)', paddingBottom: '10px', flexWrap: 'wrap', gap: '8px' }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <span style={{ fontSize: '13px', fontWeight: 800, color: 'var(--text, #0f172a)' }}>
                              Card {cardIndex + 1} of {filteredQuestions.length}
                            </span>
                            <span style={{ fontSize: '11px', color: 'var(--text-muted, #64748b)', background: 'var(--bg-soft, #f1f5f9)', padding: '2px 8px', borderRadius: '6px', fontWeight: 600 }}>
                              Q{scorecard.questions.indexOf(q) !== -1 ? scorecard.questions.indexOf(q) + 1 : cardIndex + 1} • {(q.difficulty || 'MEDIUM').toUpperCase()}
                            </span>
                            {/* Behavioral Telemetry Tag */}
                            {isRushed && (
                              <span style={{ background: 'var(--warning-bg, #fefce8)', color: 'var(--warning, #b45309)', border: '1px solid var(--warning-border, #fde047)', fontSize: '11px', fontWeight: 700, padding: '2px 8px', borderRadius: '12px' }}>
                                ⚡ Solved Fast ({timeSpentOnQ}s) — Possible Rush
                              </span>
                            )}
                            {isStruggled && (
                              <span style={{ background: 'var(--accent-soft, #eef2ff)', color: 'var(--accent, #4f46e5)', border: '1px solid var(--border-light, #c7d2fe)', fontSize: '11px', fontWeight: 700, padding: '2px 8px', borderRadius: '12px' }}>
                                ⏳ Spent {formatDuration(timeSpentOnQ)} — Deep Struggle
                              </span>
                            )}
                            {isFastFluency && (
                              <span style={{ background: 'var(--success-bg, #f0fdf4)', color: 'var(--success, #16a34a)', border: '1px solid var(--success-border, #bbf7d0)', fontSize: '11px', fontWeight: 700, padding: '2px 8px', borderRadius: '12px' }}>
                                🎯 Fast Fluency ({timeSpentOnQ}s)
                              </span>
                            )}
                          </div>

                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            {/* 1-Tap Bookmark Button */}
                            <button
                              type="button"
                              onClick={() => handleToggleBookmark(q)}
                              disabled={bookmarkLoading === qId}
                              style={{
                                display: 'flex',
                                alignItems: 'center',
                                gap: '4px',
                                padding: '4px 10px',
                                borderRadius: '16px',
                                fontSize: '11.5px',
                                fontWeight: 700,
                                cursor: 'pointer',
                                border: isBookmarked ? '1.5px solid #eab308' : '1px solid var(--border-light, #cbd5e1)',
                                background: isBookmarked ? '#fefce8' : 'var(--bg-soft, #f8fafc)',
                                color: isBookmarked ? '#a16207' : 'var(--text-muted, #64748b)',
                                transition: 'all 0.15s ease'
                              }}
                            >
                              <span>{isBookmarked ? '⭐' : '☆'}</span>
                              <span>{isBookmarked ? 'In Tricky Vault' : 'Bookmark'}</span>
                            </button>

                            {/* Status Badge */}
                            <span style={{ 
                              fontWeight: 800, 
                              fontSize: '11px',
                              padding: '3px 10px',
                              borderRadius: '12px',
                              background: isUnanswered ? 'var(--bg-soft, #f1f5f9)' : (q.isCorrect ? 'var(--success-bg, #f0fdf4)' : 'var(--danger-bg, #fef2f2)'),
                              color: isUnanswered ? 'var(--text-muted, #64748b)' : (q.isCorrect ? 'var(--success, #16a34a)' : 'var(--danger, #dc2626)') 
                            }}>
                              {isUnanswered ? '⚪ Unattempted' : (q.isCorrect ? '🟢 Correct' : '🔴 Incorrect')}
                            </span>
                          </div>
                        </div>

                        {/* Question Details via SSOT QuestionDisplay */}
                        <QuestionDisplay
                          mode="review"
                          question={q}
                          isCorrect={q.isCorrect}
                          userAnswer={isUnanswered ? '' : q.userAnswer}
                          correctAnswer={getQuestionCorrectAnswer(q)}
                          explanation={q.solution}
                          explanationLabel="💡 Step-by-Step Solution & Concept:"
                        />

                        {/* Bottom Question Controls & Challenge Button */}
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', paddingTop: '10px', borderTop: '1px solid var(--border-light, #e2e8f0)' }}>
                          <div style={{ display: 'flex', gap: '8px' }}>
                            <button
                              type="button"
                              onClick={() => toggleUnderstood(qId)}
                              style={{
                                padding: '5px 12px',
                                borderRadius: '16px',
                                fontSize: '11.5px',
                                fontWeight: 700,
                                border: isUnderstood ? '1.5px solid var(--success, #16a34a)' : '1px solid var(--border-light, #cbd5e1)',
                                background: isUnderstood ? 'var(--success-bg, #f0fdf4)' : 'transparent',
                                color: isUnderstood ? 'var(--success, #16a34a)' : 'var(--text-muted, #64748b)',
                                cursor: 'pointer'
                              }}
                            >
                              {isUnderstood ? '✓ Discussed & Understood' : 'Mark as Understood'}
                            </button>

                            {isOfficialExam && user?.role === 'student' && (
                              <button
                                type="button"
                                onClick={() => {
                                  setChallengeTargetQ(q);
                                  setChallengeReason('wrong_key');
                                  setChallengeSuggestedAnswer('B');
                                  setChallengeNotes('');
                                }}
                                style={{
                                  padding: '5px 12px',
                                  borderRadius: '16px',
                                  fontSize: '11.5px',
                                  fontWeight: 700,
                                  border: challenge ? '1.5px solid var(--warning-border, #fde047)' : '1px solid var(--border-light, #cbd5e1)',
                                  background: challenge ? 'var(--warning-bg, #fefce8)' : 'transparent',
                                  color: challenge ? 'var(--warning, #b45309)' : 'var(--text-muted, #64748b)',
                                  cursor: 'pointer'
                                }}
                              >
                                {challenge ? '⚠️ Challenged' : '⚠️ Challenge Key / Error'}
                              </button>
                            )}
                          </div>

                          {/* Next / Prev Buttons */}
                          <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                            <button
                              type="button"
                              className="btn btn-secondary btn-sm"
                              onClick={() => setCardIndex(prev => Math.max(0, prev - 1))}
                              disabled={cardIndex === 0}
                              style={{ fontWeight: 700, padding: '5px 12px' }}
                            >
                              ← Prev
                            </button>
                            <button
                              type="button"
                              className="btn btn-primary btn-sm"
                              onClick={() => setCardIndex(prev => Math.min(filteredQuestions.length, prev + 1))}
                              style={{ fontWeight: 700, padding: '5px 14px' }}
                            >
                              {cardIndex === filteredQuestions.length - 1 ? 'Go to Summary 🏁 →' : 'Next →'}
                            </button>
                          </div>
                        </div>

                      </div>
                    );
                  })() : (
                    /* ============================================================ */
                    /* FINAL COMPLETION & 30-SECOND PARTNERSHIP SIGN-OFF CARD       */
                    /* ============================================================ */
                    <div style={{
                      background: 'var(--surface, #ffffff)',
                      border: '2px solid var(--accent, #4f46e5)',
                      borderRadius: 'var(--radius-lg, 12px)',
                      padding: '20px 24px',
                      boxShadow: '0 8px 24px rgba(79, 70, 229, 0.12)',
                      display: 'flex',
                      flexDirection: 'column',
                      gap: '16px'
                    }}>
                      <div style={{ textAlign: 'center', borderBottom: '1px solid var(--border-light, #e2e8f0)', paddingBottom: '12px' }}>
                        <div style={{ fontSize: '32px', marginBottom: '4px' }}>🏁</div>
                        <h3 style={{ margin: '0 0 4px', fontSize: '18px', fontWeight: 800, color: 'var(--text, #0f172a)' }}>
                          Review Complete!
                        </h3>
                        <p style={{ margin: 0, fontSize: '12px', color: 'var(--text-muted, #64748b)' }}>
                          Score: <strong>{scorecard.score}/{scorecard.totalMarks} ({scorecard.percentage}%)</strong> • Time: <strong>{formatDuration(scorecard.durationSpent)}</strong> • Integrity: <strong>{scorecard.integrityScore}/100</strong>
                        </p>
                      </div>

                      {/* 30-Second Partnership Section */}
                      <div style={{ background: 'var(--bg-soft, #f8fafc)', borderRadius: 'var(--radius, 10px)', padding: '14px 16px', border: '1px solid var(--border-light, #e2e8f0)', display: 'flex', flexDirection: 'column', gap: '12px' }}>
                        <div style={{ fontSize: '13px', fontWeight: 800, color: 'var(--text, #0f172a)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                          🤝 30-Second Parent-Kid Partnership Touchpoint
                        </div>

                        {/* Pillar 1: Teach-Back Check */}
                        <div>
                          <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted, #64748b)', marginBottom: '6px' }}>
                            🗣️ आज काय शिकला / आज क्या पढ़ा? (Child Explained Concept):
                          </div>
                          <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                            {[
                              { key: 'confident', label: '🌟 Confident / स्पष्ट सांगितले' },
                              { key: 'good', label: '👍 Good / ठीक-ठाक' },
                              { key: 'needs_help', label: '⚠️ Needs Revision / रिव्हिजन हवे' }
                            ].map(item => {
                              const isSel = teachBackRating === item.key;
                              return (
                                <button
                                  key={item.key}
                                  type="button"
                                  onClick={() => setTeachBackRating(item.key as any)}
                                  style={{
                                    padding: '6px 14px',
                                    borderRadius: '20px',
                                    fontSize: '12px',
                                    fontWeight: 700,
                                    cursor: 'pointer',
                                    border: isSel ? '2px solid var(--accent, #4f46e5)' : '1px solid var(--border-light, #cbd5e1)',
                                    background: isSel ? 'var(--accent, #4f46e5)' : '#ffffff',
                                    color: isSel ? '#ffffff' : 'var(--text, #1e293b)',
                                    transition: 'all 0.15s ease'
                                  }}
                                >
                                  {item.label}
                                </button>
                              );
                            })}
                          </div>
                        </div>

                        {/* Pillar 2 & 3: Routine Check (Notebooks & Bag) */}
                        <div>
                          <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted, #64748b)', marginBottom: '6px' }}>
                            📋 Routine & Readiness Check:
                          </div>
                          <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                            <button
                              type="button"
                              onClick={() => setNotebooksChecked(prev => !prev)}
                              style={{
                                padding: '6px 14px',
                                borderRadius: '20px',
                                fontSize: '12px',
                                fontWeight: 700,
                                cursor: 'pointer',
                                border: notebooksChecked ? '2px solid var(--success, #16a34a)' : '1px solid var(--border-light, #cbd5e1)',
                                background: notebooksChecked ? 'var(--success-bg, #f0fdf4)' : '#ffffff',
                                color: notebooksChecked ? 'var(--success, #16a34a)' : 'var(--text-muted, #64748b)',
                                transition: 'all 0.15s ease'
                              }}
                            >
                              📚 Notebooks Checked {notebooksChecked ? '✓' : ''}
                            </button>

                            <button
                              type="button"
                              onClick={() => setBagReady(prev => !prev)}
                              style={{
                                padding: '6px 14px',
                                borderRadius: '20px',
                                fontSize: '12px',
                                fontWeight: 700,
                                cursor: 'pointer',
                                border: bagReady ? '2px solid var(--success, #16a34a)' : '1px solid var(--border-light, #cbd5e1)',
                                background: bagReady ? 'var(--success-bg, #f0fdf4)' : '#ffffff',
                                color: bagReady ? 'var(--success, #16a34a)' : 'var(--text-muted, #64748b)',
                                transition: 'all 0.15s ease'
                              }}
                            >
                              🎒 Bag & Timetable Ready {bagReady ? '✓' : ''}
                            </button>
                          </div>
                        </div>

                        {/* Pillar 4: Optional Note */}
                        <div>
                          <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted, #64748b)', marginBottom: '4px' }}>
                            💬 Note for Teacher (Optional):
                          </div>
                          <input
                            type="text"
                            value={parentNote}
                            onChange={(e) => setParentNote(e.target.value)}
                            placeholder="e.g. Understood chapter 13 well; excited about geometry."
                            style={{ width: '100%', padding: '8px 12px', fontSize: '12px', borderRadius: '6px', border: '1px solid var(--border-light, #cbd5e1)', background: '#ffffff' }}
                          />
                        </div>
                      </div>

                      {/* Navigation & Action Footer for Final Card */}
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', paddingTop: '10px' }}>
                        <button
                          type="button"
                          className="btn btn-secondary btn-sm"
                          onClick={() => setCardIndex(filteredQuestions.length - 1)}
                          style={{ fontWeight: 700 }}
                        >
                          ← Back to Questions
                        </button>

                        <div style={{ display: 'flex', gap: '10px' }}>
                          {actionButton}
                        </div>
                      </div>

                    </div>
                  )}
                </div>
              )}

              {/* ============================================================ */}
              {/* MODE B: CLASSIC FULL LIST VIEW (Scrollable)                  */}
              {/* ============================================================ */}
              {viewMode === 'list' && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  {filteredQuestions.length === 0 ? (
                    <div style={{ textAlign: 'center', padding: '24px 0', color: 'var(--text-faint, #94a3b8)', fontSize: '13px' }}>📭 No questions match this filter.</div>
                  ) : (
                    filteredQuestions.map((q, idx) => {
                      const isUnanswered = isBlank(q.userAnswer);
                      const qId = q.questionCode || q.id;
                      const isUnderstood = reviewedQuestionIds.has(qId);
                      const challenge = challenges[qId];
                      const isBookmarked = bookmarkedCodes.has(qId);

                      return (
                        <div 
                          key={`${q.id || idx}_${idx}`} 
                          style={{
                            width: '100%',
                            padding: '12px 16px',
                            borderRadius: 'var(--radius, 8px)',
                            border: isUnderstood ? '1.5px solid var(--accent, #4f46e5)' : '1.5px solid var(--border-light, #e2e8f0)',
                            background: 'var(--surface, #ffffff)',
                            display: 'flex',
                            flexDirection: 'column',
                            gap: '8px'
                          }}
                        >
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light, #e2e8f0)', paddingBottom: '6px', fontSize: '12px', color: 'var(--text-muted, #64748b)' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                              <span style={{ fontWeight: 700 }}>
                                Q{scorecard.questions.indexOf(q) !== -1 ? scorecard.questions.indexOf(q) + 1 : idx + 1}{' '}
                                ({(q.difficulty || 'MEDIUM').toUpperCase()} • {q.bloomLevel || 'Understand'})
                              </span>
                            </div>

                            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                              <button
                                type="button"
                                onClick={() => handleToggleBookmark(q)}
                                style={{
                                  padding: '2px 8px',
                                  borderRadius: '12px',
                                  fontSize: '11px',
                                  fontWeight: 700,
                                  cursor: 'pointer',
                                  border: isBookmarked ? '1px solid #eab308' : '1px solid var(--border-light, #cbd5e1)',
                                  background: isBookmarked ? '#fefce8' : 'transparent',
                                  color: isBookmarked ? '#a16207' : 'var(--text-muted, #64748b)'
                                }}
                              >
                                {isBookmarked ? '⭐ Saved' : '☆ Bookmark'}
                              </button>

                              <span style={{ 
                                fontWeight: 800, 
                                fontSize: '11px',
                                padding: '2px 8px',
                                borderRadius: '10px',
                                background: isUnanswered ? 'var(--bg-soft, #f1f5f9)' : (q.isCorrect ? 'var(--success-bg, #f0fdf4)' : 'var(--danger-bg, #fef2f2)'),
                                color: isUnanswered ? 'var(--text-muted, #64748b)' : (q.isCorrect ? 'var(--success, #16a34a)' : 'var(--danger, #dc2626)') 
                              }}>
                                {isUnanswered ? 'Unattempted' : (q.isCorrect ? 'Correct' : 'Incorrect')}
                              </span>
                            </div>
                          </div>

                          {/* Question Details via SSOT QuestionDisplay */}
                          <QuestionDisplay
                            mode="review"
                            question={q}
                            isCorrect={q.isCorrect}
                            userAnswer={isUnanswered ? '' : q.userAnswer}
                            correctAnswer={getQuestionCorrectAnswer(q)}
                            explanation={q.solution}
                            explanationLabel="💡 Step-by-Step Solution & Concept:"
                          />

                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '6px', marginTop: '6px', paddingTop: '6px', borderTop: '1px solid var(--border-light, #e2e8f0)' }}>
                            <button
                              type="button"
                              onClick={() => toggleUnderstood(qId)}
                              style={{
                                padding: '4px 10px',
                                borderRadius: '12px',
                                fontSize: '11px',
                                fontWeight: 700,
                                border: isUnderstood ? '1px solid var(--success, #16a34a)' : '1px solid var(--border-light, #cbd5e1)',
                                background: isUnderstood ? 'var(--success-bg, #f0fdf4)' : 'transparent',
                                color: isUnderstood ? 'var(--success, #16a34a)' : 'var(--text-muted, #64748b)',
                                cursor: 'pointer'
                              }}
                            >
                              {isUnderstood ? '✓ Understood' : 'Mark as Understood'}
                            </button>
                          </div>
                        </div>
                      );
                    })
                  )}
                </div>
              )}

            </div>
          )}
        </div>

        {/* Footer */}
        <div className="modal-footer" style={{ padding: '12px 20px', borderTop: '1px solid var(--border-light, #e2e8f0)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', background: 'var(--bg-soft, #f8fafc)' }}>
          <div>
            {isOfficialExam && user?.role === 'student' && (
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                {reviewSecondsRemaining > 0 && (
                  <span style={{ fontSize: '11.5px', color: 'var(--warning, #b45309)', fontWeight: 700, padding: '4px 10px', background: 'var(--warning-bg, #fefce8)', borderRadius: '6px', border: '1px solid var(--warning-border, #fde047)' }}>
                    ⏳ Reviewing reflection ({reviewSecondsRemaining}s)
                  </span>
                )}
                <button
                  type="button"
                  className="btn btn-primary btn-sm"
                  onClick={handleSubmitReview}
                  disabled={reviewSubmitting || !canSubmitReview || scorecard?.status === 'approved'}
                  style={{ fontWeight: 800, fontSize: '12px', padding: '6px 16px' }}
                >
                  {reviewSubmitting 
                    ? 'Submitting...' 
                    : reviewSecondsRemaining > 0
                      ? `⏳ Reading & Reflection (${reviewSecondsRemaining}s)`
                      : !isReviewComplete
                        ? `🔍 Verify Mistakes (${reviewedMistakesCount}/${questionsNeedingReview.length})`
                        : scorecard?.status === 'approved'
                          ? '✅ Review Verified & Approved'
                          : `🚀 Complete Verified Review (${reviewedMistakesCount}/${questionsNeedingReview.length})`
                  }
                </button>
              </div>
            )}
          </div>

          <div style={{ display: 'flex', gap: '10px' }}>
            <button className="btn btn-secondary btn-sm" onClick={onClose} style={{ fontWeight: 700 }}>Close</button>
            {actionButton}
          </div>
        </div>

      </div>

      {/* Challenge Question Dialog */}
      {challengeTargetQ && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.6)', zIndex: 40000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '12px' }}>
          <div className="modal-content" style={{ background: 'var(--surface, #ffffff)', border: '1px solid var(--border-light, #cbd5e1)', borderRadius: 'var(--radius-lg, 12px)', maxWidth: '460px', width: '100%', padding: '20px' }}>
            <h4 style={{ margin: '0 0 6px', fontSize: '14px', fontWeight: 800 }}>
              ⚠️ Challenge Question / Answer Key
            </h4>
            <p style={{ margin: '0 0 10px', fontSize: '11px', color: 'var(--text-muted, #64748b)' }}>
              Question: <strong>{challengeTargetQ.questionCode || challengeTargetQ.id}</strong>
            </p>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--text-muted, #64748b)', marginBottom: '3px' }}>Issue Type</label>
                <select
                  value={challengeReason}
                  onChange={(e) => setChallengeReason(e.target.value)}
                  style={{ width: '100%', padding: '6px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--border-light, #cbd5e1)', background: 'var(--surface, #ffffff)', color: 'var(--text, #0f172a)' }}
                >
                  <option value="wrong_key">Wrong Answer Key (Key given is incorrect)</option>
                  <option value="typo">Typo / Ambiguity in Question Text</option>
                  <option value="no_correct_option">None of the Options are Correct</option>
                  <option value="math_error">Math / Equation Rendering Defect</option>
                  <option value="ambiguous">Multiple Correct Options</option>
                </select>
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--text-muted, #64748b)', marginBottom: '3px' }}>Your Suggested Correct Option / Answer</label>
                <input
                  type="text"
                  value={challengeSuggestedAnswer}
                  onChange={(e) => setChallengeSuggestedAnswer(e.target.value)}
                  placeholder="e.g. B or Option (C)"
                  style={{ width: '100%', padding: '6px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--border-light, #cbd5e1)', background: 'var(--surface, #ffffff)', color: 'var(--text, #0f172a)' }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--text-muted, #64748b)', marginBottom: '3px' }}>Your Explanation / Proof</label>
                <textarea
                  rows={2}
                  value={challengeNotes}
                  onChange={(e) => setChallengeNotes(e.target.value)}
                  placeholder="e.g. As per NCERT Chapter 5 pg 42, force is mass x acceleration..."
                  style={{ width: '100%', padding: '6px', fontSize: '11px', borderRadius: '4px', border: '1px solid var(--border-light, #cbd5e1)', background: 'var(--bg, #f8fafc)', color: 'var(--text, #0f172a)' }}
                />
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '8px' }}>
                <button
                  type="button"
                  className="btn btn-secondary btn-sm"
                  onClick={() => setChallengeTargetQ(null)}
                >
                  Cancel
                </button>
                <button
                  type="button"
                  className="btn btn-primary btn-sm"
                  onClick={handleSaveChallenge}
                  style={{ fontWeight: 700 }}
                >
                  Save Challenge
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}
