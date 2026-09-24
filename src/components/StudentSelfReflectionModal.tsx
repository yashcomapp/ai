'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useMathRender } from '@/hooks/useMathRender';
import { preprocessMathText, parseAnswerList, resolveOptionDisplayText } from '@/lib/questionTypes';

interface StudentSelfReflectionModalProps {
  examId: string;
  examName?: string;
  onSuccess: () => void;
  onClose: () => void;
}

export default function StudentSelfReflectionModal({
  examId,
  examName,
  onSuccess,
  onClose
}: StudentSelfReflectionModalProps) {
  const { firebaseUser } = useAuth();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [reviewData, setReviewData] = useState<any>(null);
  const [wrongAnswers, setWrongAnswers] = useState<any[]>([]);
  const [unattemptedQuestions, setUnattemptedQuestions] = useState<any[]>([]);
  const [reviewedQuestions, setReviewedQuestions] = useState<Set<number>>(new Set());
  const [selectedReasons, setSelectedReasons] = useState<{ [key: number]: string }>({});
  const [filterTab, setFilterTab] = useState<'all' | 'incorrect' | 'unanswered'>('all');
  const [submitting, setSubmitting] = useState(false);

  useMathRender([reviewData, filterTab]);

  useEffect(() => {
    if (!examId || !firebaseUser) return;
    let isMounted = true;

    async function loadReflectionData() {
      setLoading(true);
      setError('');
      try {
        const idToken = await firebaseUser!.getIdToken();
        const res = await fetch(`/api/student/results?id=${encodeURIComponent(examId)}`, {
          headers: { 'Authorization': `Bearer ${idToken}` }
        });

        if (!res.ok) {
          throw new Error('Failed to load exam details for self-reflection.');
        }

        const data = await res.json();
        if (!isMounted) return;

        setReviewData(data);

        // Compile incorrect & unattempted items
        const wrongList: any[] = [];
        const unattemptedList: any[] = [];

        (data.questions || []).forEach((q: any, idx: number) => {
          const userAns = q.userAnswer;
          const isBlank = userAns === undefined || userAns === null || userAns === '' || userAns === '[]' || userAns === '[""]';
          if (isBlank) {
            unattemptedList.push({
              ...q,
              questionText: q.text || q.questionText,
              userAnswer: '',
              correctAnswer: q.correctAnswer || (q.correctAnswers ? q.correctAnswers.join(', ') : ''),
              type: 'unanswered',
              qIndex: idx
            });
          } else if (!q.isCorrect) {
            wrongList.push({
              ...q,
              questionText: q.text || q.questionText,
              userAnswer: q.userAnswer,
              correctAnswer: q.correctAnswer || (q.correctAnswers ? q.correctAnswers.join(', ') : ''),
              type: 'incorrect',
              qIndex: idx
            });
          }
        });

        setWrongAnswers(wrongList);
        setUnattemptedQuestions(unattemptedList);
      } catch (err: any) {
        if (isMounted) setError(err.message || 'Error loading reflection items');
      } finally {
        if (isMounted) setLoading(false);
      }
    }

    loadReflectionData();
    return () => { isMounted = false; };
  }, [examId, firebaseUser]);

  const questionsToReview = [
    ...wrongAnswers.map((w, idx) => ({ ...w, globalIdx: idx, type: 'incorrect' })),
    ...unattemptedQuestions.map((u, idx) => ({ ...u, globalIdx: wrongAnswers.length + idx, type: 'unanswered' }))
  ];

  const filteredQuestions = questionsToReview.filter(q => {
    if (filterTab === 'incorrect') return q.type === 'incorrect';
    if (filterTab === 'unanswered') return q.type === 'unanswered';
    return true;
  });

  const totalToReview = questionsToReview.length;
  const reviewedCount = reviewedQuestions.size;
  const isAllReviewed = totalToReview > 0 && reviewedCount === totalToReview;

  const handleSubmitReflection = async () => {
    if (!isAllReviewed || submitting || !firebaseUser) return;
    setSubmitting(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/student/exams', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          examId,
          wrongAnswerReasons: selectedReasons
        })
      });

      if (!res.ok) {
        const errJson = await res.json().catch(() => ({}));
        throw new Error(errJson.message || 'Failed to submit self-reflection');
      }

      onSuccess();
    } catch (err: any) {
      alert(`Error submitting self-reflection: ${err.message || err}`);
    } finally {
      setSubmitting(false);
    }
  };

  const getOptionText = (qItem: any, ansVal: any) => {
    return resolveOptionDisplayText(qItem.options || [], ansVal);
  };

  return (
    <div style={{
      position: 'fixed',
      inset: 0,
      background: 'rgba(0, 0, 0, 0.75)',
      backdropFilter: 'blur(6px)',
      WebkitBackdropFilter: 'blur(6px)',
      zIndex: 25000,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '20px'
    }}>
      <div style={{
        background: 'var(--surface)',
        border: '1px solid var(--border-light)',
        borderRadius: '16px',
        maxWidth: '820px',
        width: '100%',
        height: 'fit-content',
        maxHeight: '90vh',
        display: 'flex',
        flexDirection: 'column',
        overflowY: 'hidden',
        boxShadow: 'var(--shadow-xl)'
      }}>
        {/* Header */}
        <div style={{
          padding: '16px 24px',
          borderBottom: '1px solid var(--border-light)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          background: 'var(--surface-2)'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ fontSize: '20px' }}>📝</span>
            <div>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 800, color: 'var(--text)' }}>
                Exam Mistake Self-Reflection
              </h4>
              <p style={{ margin: 0, fontSize: '11px', color: 'var(--text-muted)' }}>
                Review and categorize your mistakes to unlock your next exams.
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            style={{
              background: 'transparent',
              border: 'none',
              fontSize: '18px',
              color: 'var(--text-muted)',
              cursor: 'pointer',
              padding: '4px 8px'
            }}
          >
            ✕
          </button>
        </div>

        {/* Modal Body */}
        <div style={{ padding: '20px 24px', overflowY: 'auto', flex: 1 }}>
          {loading ? (
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '50px 0', gap: '12px' }}>
              <div className="spinner"></div>
              <p style={{ fontSize: '13px', color: 'var(--text-muted)' }}>Loading mistake reflection set...</p>
            </div>
          ) : error ? (
            <div className="alert-box alert-box-danger" style={{ display: 'block', margin: '20px 0' }}>
              {error}
            </div>
          ) : totalToReview === 0 ? (
            <div style={{ textAlign: 'center', padding: '40px 20px', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '12px' }}>
              <div style={{ fontSize: '40px' }}>🎉</div>
              <h3 style={{ fontSize: '16px', fontWeight: 700, margin: 0, color: 'var(--text)' }}>No Mistakes Recorded!</h3>
              <p style={{ fontSize: '13px', color: 'var(--text-muted)', maxWidth: '400px', margin: 0 }}>
                You answered all questions correctly in this exam.
              </p>
              <button
                className="btn btn-primary"
                onClick={handleSubmitReflection}
                disabled={submitting}
                style={{ marginTop: '10px' }}
              >
                {submitting ? 'Submitting...' : '✓ Complete Sign-Off'}
              </button>
            </div>
          ) : (
            <>
              {/* Exam Info Summary Bar */}
              <div style={{
                background: 'var(--surface-2)',
                padding: '10px 16px',
                borderRadius: 'var(--radius)',
                display: 'flex',
                flexDirection: 'row',
                flexWrap: 'wrap',
                gap: '12px 20px',
                marginBottom: '16px',
                border: '1px solid var(--border-light)',
                color: 'var(--text)',
                fontSize: '11.5px'
              }}>
                <div><strong style={{ color: 'var(--text-muted)' }}>Exam:</strong> {reviewData?.examName || examName || examId}</div>
                <div><strong style={{ color: 'var(--text-muted)' }}>Score:</strong> {reviewData?.score} / {reviewData?.totalMarks} ({reviewData?.percentage}%)</div>
                <div><strong style={{ color: 'var(--text-muted)' }}>Mistakes to Reflect:</strong> <span style={{ color: 'var(--danger)', fontWeight: 700 }}>{totalToReview}</span></div>
              </div>

              {/* Filter Tabs Bar */}
              <div style={{ display: 'flex', gap: '8px', marginBottom: '14px', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px' }}>
                <button
                  onClick={() => setFilterTab('all')}
                  style={{
                    padding: '5px 12px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: filterTab === 'all' ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                    background: filterTab === 'all' ? 'var(--accent-soft)' : 'transparent',
                    color: filterTab === 'all' ? 'var(--accent)' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  All ({totalToReview})
                </button>
                <button
                  onClick={() => setFilterTab('incorrect')}
                  style={{
                    padding: '5px 12px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: filterTab === 'incorrect' ? '1px solid var(--danger)' : '1px solid var(--border-light)',
                    background: filterTab === 'incorrect' ? 'var(--danger-bg)' : 'transparent',
                    color: filterTab === 'incorrect' ? 'var(--danger)' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  Incorrect ({wrongAnswers.length})
                </button>
                <button
                  onClick={() => setFilterTab('unanswered')}
                  style={{
                    padding: '5px 12px',
                    fontSize: '11px',
                    fontWeight: 'bold',
                    borderRadius: 'var(--radius-sm)',
                    border: filterTab === 'unanswered' ? '1px solid var(--warning)' : '1px solid var(--border-light)',
                    background: filterTab === 'unanswered' ? 'var(--warning-bg)' : 'transparent',
                    color: filterTab === 'unanswered' ? 'var(--warning)' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  Unanswered ({unattemptedQuestions.length})
                </button>
              </div>

              {/* Reflection Questions List */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
                {filteredQuestions.length === 0 ? (
                  <div style={{ textAlign: 'center', padding: '20px 0', color: 'var(--text-muted)', fontSize: '12px' }}>
                    No questions in this filter tab.
                  </div>
                ) : (
                  filteredQuestions.map((qItem) => {
                    const isUnanswered = !qItem.userAnswer || qItem.userAnswer === 'UNANSWERED' || qItem.isUnanswered;
                    const isUnderstood = reviewedQuestions.has(qItem.globalIdx);
                    const explanation = qItem.explanation || qItem.solution || '';
                    const currentReason = selectedReasons[qItem.globalIdx];

                    return (
                      <div
                        key={qItem.globalIdx}
                        style={{
                          padding: '14px 16px',
                          borderRadius: 'var(--radius)',
                          border: isUnderstood ? '1px solid var(--success-border, rgba(46, 204, 113, 0.4))' : '1px solid var(--border-light)',
                          background: isUnderstood ? 'var(--success-bg, rgba(46, 204, 113, 0.04))' : 'var(--surface)',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '8px'
                        }}
                      >
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px', fontSize: '11px', color: 'var(--text-muted)' }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <span style={{ fontWeight: 700, color: 'var(--text)' }}>Question {qItem.qIndex !== undefined ? qItem.qIndex + 1 : qItem.globalIdx + 1}</span>
                            {currentReason && (
                              <span style={{ background: 'var(--warning-bg)', color: 'var(--warning)', padding: '2px 6px', borderRadius: '4px', fontSize: '9.5px', fontWeight: 'bold' }}>
                                ⚠️ Reason: {currentReason}
                              </span>
                            )}
                          </div>
                          <span style={{
                            fontWeight: 'bold',
                            fontSize: '10px',
                            padding: '2px 8px',
                            borderRadius: '12px',
                            background: isUnanswered ? 'var(--surface-3)' : 'var(--danger-bg)',
                            color: isUnanswered ? 'var(--text-muted)' : 'var(--danger)'
                          }}>
                            {isUnanswered ? 'UNANSWERED' : 'INCORRECT'}
                          </span>
                        </div>

                        {/* Question Text */}
                        <div
                          className="math-container"
                          style={{ fontSize: '13px', lineHeight: '1.5', color: 'var(--text)', fontWeight: 600 }}
                          dangerouslySetInnerHTML={{ __html: preprocessMathText(qItem.questionText || '') }}
                        />

                        {/* Options preview if available */}
                        {Array.isArray(qItem.options) && qItem.options.length > 0 && (
                          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '6px', margin: '4px 0' }}>
                            {qItem.options.map((opt: any, oi: number) => {
                              const optText = typeof opt === 'object' ? (opt.text || opt.code || '') : String(opt);
                              const isCorrectOpt = String(qItem.correctAnswer || '').includes(String.fromCharCode(65 + oi)) ||
                                String(qItem.correctAnswer || '').includes(optText);
                              const isUserOpt = String(qItem.userAnswer || '').includes(String.fromCharCode(65 + oi)) ||
                                String(qItem.userAnswer || '').includes(optText);

                              let border = '1px solid var(--border-light)';
                              let background = 'var(--surface)';
                              let color = 'var(--text-muted)';
                              let prefix = '';

                              if (isCorrectOpt) {
                                border = '1px solid var(--success-border, rgba(46, 204, 113, 0.6))';
                                background = 'var(--success-bg, rgba(46, 204, 113, 0.12))';
                                color = 'var(--success)';
                                prefix = '✓ ';
                              } else if (isUserOpt) {
                                border = '1px solid var(--danger-border, rgba(239, 68, 68, 0.6))';
                                background = 'var(--danger-bg, rgba(239, 68, 68, 0.12))';
                                color = 'var(--danger)';
                                prefix = '✗ ';
                              }

                              return (
                                <div
                                  key={oi}
                                  style={{
                                    display: 'flex',
                                    alignItems: 'center',
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
                                  {prefix && <span>{prefix}</span>}
                                  <span className="math-container" dangerouslySetInnerHTML={{ __html: preprocessMathText(optText) }} />
                                </div>
                              );
                            })}
                          </div>
                        )}

                        {/* Answers comparison */}
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', fontSize: '11.5px', background: 'var(--surface-2)', padding: '8px 10px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', margin: '4px 0' }}>
                          <div>
                            <strong style={{ color: 'var(--text-muted)', marginRight: '6px' }}>Your Answer:</strong>
                            <span className="math-container" style={{ color: 'var(--text)', fontWeight: 600 }}>
                              {isUnanswered ? '(blank)' : getOptionText(qItem, qItem.userAnswer)}
                            </span>
                          </div>
                          <div>
                            <strong style={{ color: 'var(--text-muted)', marginRight: '6px' }}>Correct Answer:</strong>
                            <span className="math-container" style={{ color: 'var(--success)', fontWeight: 'bold' }}>
                              {getOptionText(qItem, qItem.correctAnswer)}
                            </span>
                          </div>
                        </div>

                        {explanation && (
                          <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', borderTop: '1px dashed var(--border-light)', paddingTop: '6px' }}>
                            <strong style={{ color: 'var(--info)' }}>Solution Explanation:</strong>
                            <div className="math-container" style={{ margin: '3px 0 0 0', lineHeight: '1.4' }} dangerouslySetInnerHTML={{ __html: preprocessMathText(explanation) }} />
                          </div>
                        )}

                        {/* Error Reason Classification Box */}
                        <div style={{
                          marginTop: '6px',
                          border: '1px solid var(--border-light)',
                          borderRadius: 'var(--radius-sm)',
                          padding: '10px 12px',
                          background: 'var(--surface-2)'
                        }}>
                          <span style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '6px', color: 'var(--text)' }}>
                            Select your error reason:
                          </span>
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                            <div style={{ display: 'flex', gap: '6px' }}>
                              {['Reading Errors', 'Time Management', 'Over-Thinking'].map(reason => {
                                const isSelected = selectedReasons[qItem.globalIdx] === reason;
                                return (
                                  <button
                                    key={reason}
                                    type="button"
                                    onClick={() => setSelectedReasons(prev => ({ ...prev, [qItem.globalIdx]: reason }))}
                                    style={{
                                      flex: 1,
                                      padding: '6px 4px',
                                      fontSize: '10.5px',
                                      borderRadius: 'var(--radius-sm)',
                                      border: isSelected ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                                      background: isSelected ? 'var(--accent-soft)' : 'var(--surface)',
                                      color: isSelected ? 'var(--accent)' : 'var(--text-muted)',
                                      fontWeight: isSelected ? 700 : 500,
                                      cursor: 'pointer'
                                    }}
                                  >
                                    {reason}
                                  </button>
                                );
                              })}
                            </div>
                            <div style={{ display: 'flex', gap: '6px' }}>
                              {['Calculation / Slip', 'Need Concept Revision', 'Other'].map(reason => {
                                const isSelected = selectedReasons[qItem.globalIdx] === reason;
                                return (
                                  <button
                                    key={reason}
                                    type="button"
                                    onClick={() => setSelectedReasons(prev => ({ ...prev, [qItem.globalIdx]: reason }))}
                                    style={{
                                      flex: 1,
                                      padding: '6px 4px',
                                      fontSize: '10.5px',
                                      borderRadius: 'var(--radius-sm)',
                                      border: isSelected ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                                      background: isSelected ? 'var(--accent-soft)' : 'var(--surface)',
                                      color: isSelected ? 'var(--accent)' : 'var(--text-muted)',
                                      fontWeight: isSelected ? 700 : 500,
                                      cursor: 'pointer'
                                    }}
                                  >
                                    {reason}
                                  </button>
                                );
                              })}
                            </div>
                          </div>
                        </div>

                        {/* Confirmation Button */}
                        <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '4px' }}>
                          <button
                            type="button"
                            onClick={() => {
                              setReviewedQuestions(prev => {
                                const next = new Set(prev);
                                if (next.has(qItem.globalIdx)) {
                                  next.delete(qItem.globalIdx);
                                } else {
                                  next.add(qItem.globalIdx);
                                }
                                return next;
                              });
                            }}
                            style={{
                              display: 'inline-flex',
                              alignItems: 'center',
                              gap: '6px',
                              padding: '6px 14px',
                              fontSize: '11.5px',
                              fontWeight: 700,
                              borderRadius: 'var(--radius-sm)',
                              border: isUnderstood ? '1px solid var(--success)' : '1px solid var(--border-light)',
                              background: isUnderstood ? 'var(--success-bg)' : 'var(--surface)',
                              color: isUnderstood ? 'var(--success)' : 'var(--text-muted)',
                              cursor: 'pointer'
                            }}
                          >
                            <span>{isUnderstood ? '✓ Understood & Resolved' : 'Mark as Understood'}</span>
                          </button>
                        </div>
                      </div>
                    );
                  })
                )}
              </div>
            </>
          )}
        </div>

        {/* Footer & Submit Action */}
        {!loading && !error && totalToReview > 0 && (
          <div style={{ padding: '14px 24px', borderTop: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '8px', background: 'var(--surface-2)' }}>
            <div style={{
              padding: '8px 12px',
              fontSize: '12px',
              textAlign: 'center',
              borderRadius: 'var(--radius-sm)',
              background: isAllReviewed ? 'var(--success-bg)' : 'var(--warning-bg)',
              color: isAllReviewed ? 'var(--success)' : 'var(--warning)',
              border: isAllReviewed ? '1px solid var(--success-border)' : '1px solid var(--warning-border)',
              fontWeight: 'bold'
            }}>
              {isAllReviewed
                ? '✅ Excellent! All questions reviewed. Click below to submit & unlock your exams.'
                : `Reviewed: ${reviewedCount} / ${totalToReview} questions. Select a reason and click "I Understand" for each question above.`
              }
            </div>
            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
              <button
                className="btn btn-secondary"
                onClick={onClose}
                disabled={submitting}
                style={{ padding: '8px 16px', fontSize: '12px' }}
              >
                Close
              </button>
              <button
                className="btn btn-primary"
                disabled={!isAllReviewed || submitting}
                onClick={handleSubmitReflection}
                style={{
                  padding: '8px 20px',
                  fontSize: '12px',
                  fontWeight: 700,
                  background: isAllReviewed ? 'var(--success)' : 'var(--surface-3)',
                  color: 'var(--text-white)',
                  border: 'none',
                  borderRadius: '6px',
                  cursor: isAllReviewed ? 'pointer' : 'not-allowed'
                }}
              >
                {submitting ? 'Submitting...' : '🚀 Submit Reflection & Unlock Exams'}
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
