'use client';

import React, { useState, useEffect, useRef } from 'react';
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
  stripOptionLabel,
  DEFAULT_ASSERTION_REASON_OPTIONS
} from '@/lib/questionTypes';
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
  steps?: any[];
  evaluations?: any[];
}

export interface DetailedScorecard {
  id: string;
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
  const [questionFilterTab, setQuestionFilterTab] = useState<'all' | 'correct' | 'incorrect' | 'unanswered'>('all');

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

  useEffect(() => {
    if (scorecard?.submittedAt) {
      const compDate = parseDateInput(scorecard.submittedAt);
      if (compDate) {
        const diffM = Math.floor((Date.now() - compDate.getTime()) / 60000);
        setElapsedMinutes(Math.max(0, diffM));
      }
    }
  }, [scorecard]);

  // Dynamically load KaTeX and auto-render math expressions when scorecard changes or tab changes
  useMathRender([scorecard, questionFilterTab, challengeTargetQ]);

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
    ? scorecard.questions.filter(q => q.isCorrect).length
    : (scorecard?.score || 0);
  const incorrectCount = scorecard?.questions && scorecard.questions.length > 0
    ? scorecard.questions.filter(q => !q.isCorrect && !isBlank(q.userAnswer)).length
    : Math.max(0, (scorecard?.totalMarks || 0) - (scorecard?.score || 0));
  const unansweredCount = scorecard?.questions && scorecard.questions.length > 0
    ? scorecard.questions.filter(q => !q.isCorrect && isBlank(q.userAnswer)).length
    : 0;

  const filteredQuestions = scorecard?.questions?.filter(q => {
    const blank = isBlank(q.userAnswer);
    if (questionFilterTab === 'correct') return q.isCorrect;
    if (questionFilterTab === 'incorrect') return !q.isCorrect && !blank;
    if (questionFilterTab === 'unanswered') return !q.isCorrect && blank;
    return true;
  }) || [];

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
    // Also mark as reviewed
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
      const timeSpentSecs = Math.max(10, Math.floor((Date.now() - startTimeRef.current) / 1000));
      const examId = scorecard.id || scorecard.examCode;

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
          challenges: Object.values(challenges),
          timeSpentSeconds: timeSpentSecs
        })
      });

      const data = await res.json();
      if (res.ok) {
        setReviewSubmittedSuccess(data.message || '✅ Verified review submitted successfully!');
      } else {
        alert('Error submitting review: ' + data.message);
      }
    } catch (err: any) {
      alert('Error: ' + err.message);
    } finally {
      setReviewSubmitting(false);
    }
  };

  return (
    <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 35000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '10px 8px' }}>
      <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '880px', width: '100%', height: 'fit-content', maxHeight: '94vh', display: 'flex', flexDirection: 'column', overflowY: 'hidden' }}>
        
        {/* Header */}
        <div className="modal-header" style={{ padding: '12px 16px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <h4 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold' }}>
              📊 {scorecard?.examType === 'practice' ? 'Practice Review Scorecard' : 'Exam Review & Verification Scorecard'}
            </h4>
            {scorecard?.examType === 'practice' && scorecard?.practiceNumber && (
              <span style={{ background: 'var(--accent)', color: 'var(--text-on-accent)', fontSize: '11px', fontWeight: 700, padding: '2px 8px', borderRadius: '12px' }}>
                Practice #{scorecard.practiceNumber}
              </span>
            )}
          </div>
          <button className="close-modal" onClick={onClose} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
        </div>

        <div id="scorecard-details-section" className="modal-body math-container" style={{ padding: '12px 14px', overflowY: 'auto', flex: 1 }}>
          {loading && (
            <div style={{ textAlign: 'center', padding: '24px 0' }}>
              <div className="spinner" style={{ margin: '0 auto 10px' }}></div> Loading details...
            </div>
          )}

          {!loading && scorecard && (
            <div>
              {/* 60-Minute Accountability Banner for Official Exams */}
              {isOfficialExam && user?.role === 'student' && (
                <div style={{
                  background: isWithin60Min ? 'var(--warning-bg)' : 'var(--danger-bg)',
                  border: `1px solid ${isWithin60Min ? 'var(--warning-border)' : 'var(--danger-border)'}`,
                  borderRadius: 'var(--radius-sm)',
                  padding: '8px 12px',
                  marginBottom: '10px',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  flexWrap: 'wrap',
                  gap: '6px'
                }}>
                  <div style={{ fontSize: '11.5px', color: isWithin60Min ? 'var(--text)' : 'var(--danger)', fontWeight: 600 }}>
                    {isWithin60Min ? (
                      <span>⏱️ <strong>60-Min Review Window:</strong> {remainingMins}m remaining to verify mistakes without being flagged in Fault Register!</span>
                    ) : (
                      <span>⚠️ <strong>Review Window Expired:</strong> {elapsedMinutes}m elapsed since exam. Review will be recorded as Late.</span>
                    )}
                  </div>
                  <div style={{ fontSize: '10.5px', color: 'var(--warning)', fontWeight: 700 }}>
                    🏆 First 3 to spot genuine question/key errors earn +2 Diligence points!
                  </div>
                </div>
              )}

              {reviewSubmittedSuccess && (
                <div style={{ background: 'var(--success-bg)', color: 'var(--success)', border: '1px solid var(--success-border)', padding: '8px 12px', borderRadius: 'var(--radius-sm)', fontSize: '12px', fontWeight: 700, marginBottom: '10px' }}>
                  {reviewSubmittedSuccess}
                </div>
              )}

              {/* Compact Horizontal Summary Bar */}
              <div style={{ 
                background: 'var(--bg-soft)', 
                padding: '8px 12px', 
                borderRadius: 'var(--radius-sm)', 
                display: 'flex', 
                flexDirection: 'row', 
                flexWrap: 'wrap', 
                gap: '8px 16px', 
                marginBottom: '10px',
                border: '1px solid var(--border-light)'
              }}>
                {scorecard.subject && scorecard.subject !== 'General' && (
                  <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                    <strong style={{ color: 'var(--text-muted)' }}>Subject:</strong>{' '}
                    <span style={{ fontWeight: 600 }}>{scorecard.subject}</span>
                  </div>
                )}
                {scorecard.chapter && scorecard.chapter !== 'General' && scorecard.chapter !== 'General Chapter' && (
                  <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                    <strong style={{ color: 'var(--text-muted)' }}>Chapter:</strong>{' '}
                    <span style={{ fontWeight: 600 }}>{scorecard.chapter}</span>
                  </div>
                )}
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>{scorecard.examType === 'practice' ? 'Topic' : 'Exam ID'}:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>
                    {scorecard.examType === 'practice' ? (scorecard.topicName || scorecard.examName) : scorecard.examName}
                    {scorecard.examType === 'practice' && scorecard.topicCode && scorecard.topicCode !== (scorecard.topicName || scorecard.examName) ? ` (${scorecard.topicCode})` : ''}
                  </span>
                </div>
                {scorecard.examType === 'practice' && (scorecard.practiceNumber !== undefined && scorecard.practiceNumber !== null) && (
                  <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                    <strong style={{ color: 'var(--text-muted)' }}>Practice Set:</strong>{' '}
                    <span style={{ fontWeight: 700, color: 'var(--accent)' }}>Practice #{scorecard.practiceNumber}</span>
                  </div>
                )}
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Date & Time:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{formatDate(scorecard.submittedAt)}</span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Time Spent:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{formatDuration(scorecard.durationSpent)}</span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Score:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{scorecard.score} / {scorecard.totalMarks} ({scorecard.percentage}%)</span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Integrity:</strong>{' '}
                  <span style={{ fontWeight: 600, color: scorecard.integrityScore < 70 ? 'var(--danger)' : scorecard.integrityScore < 90 ? 'var(--warning)' : 'var(--success)' }}>
                    {scorecard.integrityScore} / 100
                  </span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Tab Out:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{scorecard.tabViolations} times</span>
                </div>
              </div>

              {/* Filter Tabs Bar */}
              <div className="outcome-tabs" style={{ display: 'flex', gap: '6px', marginBottom: '10px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px' }}>
                <button 
                  onClick={() => setQuestionFilterTab('all')} 
                  style={{
                    padding: '4px 10px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: questionFilterTab === 'all' ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                    background: questionFilterTab === 'all' ? 'var(--accent-soft)' : 'transparent',
                    color: questionFilterTab === 'all' ? 'var(--accent)' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  All ({scorecard.questions.length})
                </button>
                <button 
                  onClick={() => setQuestionFilterTab('correct')} 
                  style={{
                    padding: '4px 10px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: questionFilterTab === 'correct' ? '1px solid var(--success)' : '1px solid var(--border-light)',
                    background: questionFilterTab === 'correct' ? 'var(--success-bg)' : 'transparent',
                    color: questionFilterTab === 'correct' ? 'var(--success)' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  Correct ({correctCount})
                </button>
                <button 
                  onClick={() => setQuestionFilterTab('incorrect')} 
                  style={{
                    padding: '4px 10px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: questionFilterTab === 'incorrect' ? '1px solid var(--danger)' : '1px solid var(--border-light)',
                    background: questionFilterTab === 'incorrect' ? 'var(--danger-bg)' : 'transparent',
                    color: questionFilterTab === 'incorrect' ? 'var(--danger)' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  Incorrect ({incorrectCount})
                </button>
                <button 
                  onClick={() => setQuestionFilterTab('unanswered')} 
                  style={{
                    padding: '4px 10px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: questionFilterTab === 'unanswered' ? '1px solid var(--text-muted)' : '1px solid var(--border-light)',
                    background: questionFilterTab === 'unanswered' ? 'var(--bg-soft)' : 'transparent',
                    color: 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  Unanswered ({unansweredCount})
                </button>
              </div>

              {/* Question Cards */}
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                <h5 style={{ fontSize: '12px', fontWeight: 'bold', margin: 0 }}>🔍 Question-by-Question Audit</h5>
                {isOfficialExam && user?.role === 'student' && (
                  <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                    Verified: <strong>{reviewedQuestionIds.size}</strong> / {scorecard.questions.length}
                  </span>
                )}
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {filteredQuestions.length === 0 ? (
                  <div style={{ textAlign: 'center', padding: '20px 0', color: 'var(--text-faint)', fontSize: '12px' }}>📭 No questions match this filter.</div>
                ) : (
                  filteredQuestions.map((q, idx) => {
                    const isUnanswered = isBlank(q.userAnswer);
                    const qId = q.questionCode || q.id;
                    const isUnderstood = reviewedQuestionIds.has(qId);
                    const challenge = challenges[qId];

                    return (
                      <div 
                        key={`${q.id || idx}_${idx}`} 
                        style={{
                          width: '100%',
                          padding: '10px 12px',
                          borderRadius: 'var(--radius-sm)',
                          border: isUnderstood ? '1.5px solid var(--accent)' : '1.5px solid var(--review-card-border)',
                          background: 'var(--review-card-bg)',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '6px'
                        }}
                      >
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '4px', fontSize: '11px', color: 'var(--text-muted)' }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                            <span style={{ fontWeight: 600 }}>
                              Q{scorecard.questions.indexOf(q) !== -1 ? scorecard.questions.indexOf(q) + 1 : idx + 1}{' '}
                              ({(q.difficulty || 'MEDIUM').toUpperCase()} • {q.bloomLevel || 'Understand'})
                            </span>
                            {(() => {
                              const reason = getReasonForQuestion(q, scorecard);
                              if (!reason) return null;
                              return (
                                <span style={{ background: 'var(--warning-bg)', color: 'var(--warning)', border: '1px solid rgba(251, 191, 36, 0.25)', padding: '1px 5px', borderRadius: '4px', fontSize: '9px', fontWeight: 'bold' }}>
                                  ⚠️ Reason: {reason}
                                </span>
                              );
                            })()}
                          </div>

                          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                            <span style={{ 
                              fontWeight: 'bold', 
                              fontSize: '10px',
                              padding: '1px 6px',
                              borderRadius: '10px',
                              background: isUnanswered ? 'var(--bg-soft)' : (q.isCorrect ? 'var(--success-bg)' : 'var(--danger-bg)'),
                              color: isUnanswered ? 'var(--text-muted)' : (q.isCorrect ? 'var(--success)' : 'var(--danger)') 
                            }}>
                              {isUnanswered ? 'Unattempted' : (q.isCorrect ? 'Correct' : 'Incorrect')}
                            </span>
                          </div>
                        </div>

                        {isAssertionReasonType(q.type) ? (() => {
                          const { assertion, reason } = extractAssertionAndReason(q);
                          return (
                            <div style={{ marginBottom: '8px', fontSize: '12.5px' }}>
                              <p style={{ margin: '2px 0' }}><strong>Assertion (A):</strong> <span className="math-container" dangerouslySetInnerHTML={{ __html: preprocessMathText(assertion) }} /></p>
                              <p style={{ margin: '2px 0' }}><strong>Reason (R):</strong> <span className="math-container" dangerouslySetInnerHTML={{ __html: preprocessMathText(reason) }} /></p>
                            </div>
                          );
                        })() : (
                          <p className="math-container" style={{ fontSize: '12.5px', margin: '0 0 6px 0', fontWeight: 'bold', lineHeight: '1.35', color: 'var(--text)' }} dangerouslySetInnerHTML={{ __html: preprocessMathText(q.text || '') }} />
                        )}

                        {/* Options List breakdown */}
                        {(() => {
                          const isAssertionReason = isAssertionReasonType(q.type);
                          const optionsToRender = (q.options && q.options.length > 0)
                            ? q.options
                            : (isAssertionReason ? DEFAULT_ASSERTION_REASON_OPTIONS : []);

                          if (optionsToRender.length > 0) {
                            return (
                              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', marginBottom: '8px' }}>
                                {optionsToRender.map((opt: any, oi: number) => {
                                  const optKey = getRawOptionKey(opt);
                                  const optText = getRawOptionText(opt);
                                  const correctAns = getQuestionCorrectAnswer(q);
                                  
                                  let isCorrectOpt = isOptionCorrect(correctAns, optKey, oi, optText, optionsToRender);
                                  const isUserOpt = isOptionSelectedByUser(q.userAnswer, optKey, oi, optText, optionsToRender);

                                  if (q.isCorrect && isUserOpt) {
                                    isCorrectOpt = true;
                                  }

                                  let border = '1px solid var(--review-option-border)';
                                  let background = 'var(--review-option-bg)';
                                  let color = 'var(--text)';
                                  let prefix = '';

                                  if (isCorrectOpt) {
                                    border = '1.5px solid var(--success)';
                                    background = 'var(--success-bg)';
                                    color = 'var(--success)';
                                    prefix = isUserOpt ? '🎯 ' : '✅ ';
                                  } else if (isUserOpt) {
                                    border = '1.5px solid var(--danger)';
                                    background = 'rgba(220, 38, 38, 0.08)';
                                    color = 'var(--danger)';
                                    prefix = '❌ ';
                                  }

                                  const letterLabel = String.fromCharCode(65 + oi);

                                  return (
                                    <div 
                                      key={oi} 
                                      style={{ 
                                        display: 'flex', 
                                        alignItems: 'flex-start', 
                                        gap: '6px',
                                        padding: '6px 10px', 
                                        border, 
                                        borderRadius: 'var(--radius-sm)', 
                                        background,
                                        color,
                                        fontSize: '11.5px',
                                        fontWeight: (isCorrectOpt || isUserOpt) ? 600 : 400
                                      }}
                                    >
                                      <span style={{ fontWeight: 'bold', minWidth: '24px', flexShrink: 0 }}>
                                        {prefix ? `${prefix}(${letterLabel})` : `(${letterLabel})`}
                                      </span>
                                      <span className="math-container" style={{ flex: 1 }}>{preprocessMathText(stripOptionLabel(optText))}</span>
                                    </div>
                                  );
                                })}
                              </div>
                            );
                          }

                          // Non-option question fallback (e.g. Numerical or Fill in Blank without options)
                          return (
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', fontSize: '11.5px', background: 'var(--surface-3, rgba(0,0,0,0.03))', padding: '6px 10px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', marginBottom: '8px' }}>
                              <div>
                                <strong style={{ color: 'var(--text-muted)', marginRight: '6px' }}>Your Answer:</strong>
                                <span className="math-container" style={{ color: isUnanswered ? 'var(--text-muted)' : (q.isCorrect ? 'var(--success)' : 'var(--danger)'), fontWeight: 600 }}>
                                  {isUnanswered ? '(blank)' : preprocessMathText(formatUserAnswerSummary(q.userAnswer))}
                                </span>
                              </div>
                              <div>
                                <strong style={{ color: 'var(--text-muted)', marginRight: '6px' }}>Correct Answer:</strong>
                                <span className="math-container" style={{ color: 'var(--success)', fontWeight: 600 }}>
                                  {preprocessMathText(formatUserAnswerSummary(getQuestionCorrectAnswer(q)))}
                                </span>
                              </div>
                            </div>
                          );
                        })()}

                        {/* Solution & Explanation */}
                        {q.solution && (
                          <div style={{ marginTop: '4px', fontSize: '11.5px', color: 'var(--text-muted)', borderTop: '1px dashed var(--border-light)', paddingTop: '6px' }}>
                            <strong>Solution Explanation:</strong>
                            <p className="math-container" style={{ margin: '2px 0 0 0', lineHeight: '1.35' }}>{preprocessMathText(q.solution)}</p>
                          </div>
                        )}

                        {/* Interactive Verification & Challenge Buttons (Student Exam Review) */}
                        {isOfficialExam && user?.role === 'student' && (
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '6px', marginTop: '6px', paddingTop: '6px', borderTop: '1px solid var(--border-light)' }}>
                            <div style={{ display: 'flex', gap: '6px' }}>
                              <button
                                type="button"
                                onClick={() => toggleUnderstood(qId)}
                                style={{
                                  padding: '3px 8px',
                                  borderRadius: '12px',
                                  fontSize: '10.5px',
                                  fontWeight: 700,
                                  border: isUnderstood ? '1px solid var(--success)' : '1px solid var(--border-light)',
                                  background: isUnderstood ? 'var(--success-bg)' : 'transparent',
                                  color: isUnderstood ? 'var(--success)' : 'var(--text-muted)',
                                  cursor: 'pointer'
                                }}
                              >
                                {isUnderstood ? '✓ Understood' : 'Mark as Understood'}
                              </button>

                              <button
                                type="button"
                                onClick={() => {
                                  setChallengeTargetQ(q);
                                  setChallengeReason('wrong_key');
                                  setChallengeSuggestedAnswer('B');
                                  setChallengeNotes('');
                                }}
                                style={{
                                  padding: '3px 8px',
                                  borderRadius: '12px',
                                  fontSize: '10.5px',
                                  fontWeight: 700,
                                  border: challenge ? '1px solid var(--warning-border)' : '1px solid var(--border-light)',
                                  background: challenge ? 'var(--warning-bg)' : 'transparent',
                                  color: challenge ? 'var(--warning)' : 'var(--text-muted)',
                                  cursor: 'pointer'
                                }}
                              >
                                {challenge ? '⚠️ Challenged' : '⚠️ Challenge Key / Error'}
                              </button>
                            </div>

                            {challenge && (
                              <span style={{ fontSize: '10px', color: 'var(--warning)', fontWeight: 600 }}>
                                Flagged: {challenge.reason} ({challenge.suggestedAnswer})
                              </span>
                            )}
                          </div>
                        )}

                      </div>
                    );
                  })
                )}
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="modal-footer" style={{ padding: '12px 18px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
          <div>
            {isOfficialExam && user?.role === 'student' && (
              <button
                type="button"
                className="btn btn-primary btn-sm"
                onClick={handleSubmitReview}
                disabled={reviewSubmitting || reviewedQuestionIds.size === 0}
                style={{ fontWeight: 700, fontSize: '12px', padding: '6px 14px' }}
              >
                {reviewSubmitting ? 'Submitting...' : `🚀 Complete Verified Review (${reviewedQuestionIds.size}/${scorecard?.questions.length || 0})`}
              </button>
            )}
          </div>

          <div style={{ display: 'flex', gap: '8px' }}>
            <button className="btn btn-secondary btn-sm" onClick={onClose}>Close</button>
            {actionButton}
          </div>
        </div>

      </div>

      {/* Challenge Question Dialog */}
      {challengeTargetQ && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.6)', zIndex: 40000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '12px' }}>
          <div className="modal-content" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', maxWidth: '460px', width: '100%', padding: '18px' }}>
            <h4 style={{ margin: '0 0 6px', fontSize: '14px', fontWeight: 800 }}>
              ⚠️ Challenge Question / Answer Key
            </h4>
            <p style={{ margin: '0 0 10px', fontSize: '11px', color: 'var(--text-muted)' }}>
              Question: <strong>{challengeTargetQ.questionCode || challengeTargetQ.id}</strong>
            </p>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>Issue Type</label>
                <select
                  value={challengeReason}
                  onChange={(e) => setChallengeReason(e.target.value)}
                  style={{ width: '100%', padding: '6px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)' }}
                >
                  <option value="wrong_key">Wrong Answer Key (Key given is incorrect)</option>
                  <option value="typo">Typo / Ambiguity in Question Text</option>
                  <option value="no_correct_option">None of the Options are Correct</option>
                  <option value="math_error">Math / Equation Rendering Defect</option>
                  <option value="ambiguous">Multiple Correct Options</option>
                </select>
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>Your Suggested Correct Option / Answer</label>
                <input
                  type="text"
                  value={challengeSuggestedAnswer}
                  onChange={(e) => setChallengeSuggestedAnswer(e.target.value)}
                  placeholder="e.g. B or Option (C)"
                  style={{ width: '100%', padding: '6px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)' }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>Your Explanation / Proof</label>
                <textarea
                  rows={2}
                  value={challengeNotes}
                  onChange={(e) => setChallengeNotes(e.target.value)}
                  placeholder="e.g. As per NCERT Chapter 5 pg 42, force is mass x acceleration..."
                  style={{ width: '100%', padding: '6px', fontSize: '11px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg)', color: 'var(--text)' }}
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
