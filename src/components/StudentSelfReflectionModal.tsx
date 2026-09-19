'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useMathRender } from '@/hooks/useMathRender';
import { preprocessMathText, parseAnswerList } from '@/lib/questionTypes';

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
    const list = parseAnswerList(ansVal);
    if (list.length === 0) return '(blank)';
    const opts = qItem.options || [];
    if (!Array.isArray(opts) || opts.length === 0) return list.join(', ');

    const matchedTexts: string[] = [];
    list.forEach(item => {
      let foundText = '';
      if (item.length === 1 && item.toUpperCase() >= 'A' && item.toUpperCase() <= 'Z') {
        const codeIndex = item.toUpperCase().charCodeAt(0) - 65;
        if (codeIndex >= 0 && codeIndex < opts.length) {
          const optVal = opts[codeIndex];
          foundText = (optVal && typeof optVal === 'object') ? (optVal.text || optVal.code || item) : String(optVal);
        }
      }
      if (!foundText && /^\d+$/.test(item)) {
        const codeIndex = parseInt(item, 10);
        if (codeIndex >= 0 && codeIndex < opts.length) {
          const optVal = opts[codeIndex];
          foundText = (optVal && typeof optVal === 'object') ? (optVal.text || optVal.code || item) : String(optVal);
        }
      }
      if (!foundText) {
        const opt = opts.find((o: any) => {
          if (o && typeof o === 'object') return o.code === item || o.text === item;
          return String(o) === item;
        });
        if (opt) {
          foundText = (opt && typeof opt === 'object') ? (opt.text || opt.code || item) : String(opt);
        }
      }
      matchedTexts.push(foundText || item);
    });

    return matchedTexts.join(', ');
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
        background: 'var(--surface-popover, #1e293b)',
        border: '1px solid var(--border-popover, #334155)',
        borderRadius: '16px',
        maxWidth: '820px',
        width: '100%',
        height: 'fit-content',
        maxHeight: '90vh',
        display: 'flex',
        flexDirection: 'column',
        overflowY: 'hidden',
        boxShadow: 'var(--shadow-xl, 0 20px 25px -5px rgba(0, 0, 0, 0.5))'
      }}>
        {/* Header */}
        <div style={{
          padding: '16px 24px',
          borderBottom: '1px solid var(--border-light, #334155)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          background: 'var(--surface, #0f172a)'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ fontSize: '20px' }}>📝</span>
            <div>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 800, color: 'var(--text, #f8fafc)' }}>
                Exam Mistake Self-Reflection
              </h4>
              <p style={{ margin: 0, fontSize: '11px', color: 'var(--text-muted, #94a3b8)' }}>
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
              color: 'var(--text-muted, #94a3b8)',
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
              <p style={{ fontSize: '13px', color: 'var(--text-muted, #94a3b8)' }}>Loading mistake reflection set...</p>
            </div>
          ) : error ? (
            <div className="alert-box alert-box-danger" style={{ display: 'block', margin: '20px 0' }}>
              {error}
            </div>
          ) : totalToReview === 0 ? (
            <div style={{ textAlign: 'center', padding: '40px 20px', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '12px' }}>
              <div style={{ fontSize: '40px' }}>🎉</div>
              <h3 style={{ fontSize: '16px', fontWeight: 700, margin: 0, color: 'var(--text, #f8fafc)' }}>No Mistakes Recorded!</h3>
              <p style={{ fontSize: '13px', color: 'var(--text-muted, #94a3b8)', maxWidth: '400px', margin: 0 }}>
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
                background: 'var(--bg-soft, #1e293b)',
                padding: '10px 16px',
                borderRadius: 'var(--radius, 8px)',
                display: 'flex',
                flexDirection: 'row',
                flexWrap: 'wrap',
                gap: '12px 20px',
                marginBottom: '16px',
                border: '1px solid var(--border-light, #334155)',
                color: 'var(--text, #f8fafc)',
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
                    borderRadius: 'var(--radius-sm, 6px)',
                    border: filterTab === 'incorrect' ? '1px solid #ef4444' : '1px solid var(--border-light, #334155)',
                    background: filterTab === 'incorrect' ? 'rgba(239, 68, 68, 0.15)' : 'transparent',
                    color: filterTab === 'incorrect' ? '#f87171' : 'var(--text-muted, #94a3b8)',
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
                    borderRadius: 'var(--radius-sm, 6px)',
                    border: filterTab === 'unanswered' ? '1px solid #f59e0b' : '1px solid var(--border-light, #334155)',
                    background: filterTab === 'unanswered' ? 'rgba(245, 158, 11, 0.15)' : 'transparent',
                    color: filterTab === 'unanswered' ? '#fbbf24' : 'var(--text-muted, #94a3b8)',
                    cursor: 'pointer'
                  }}
                >
                  Unanswered ({unattemptedQuestions.length})
                </button>
              </div>

              {/* Reflection Questions List */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
                {filteredQuestions.length === 0 ? (
                  <div style={{ textAlign: 'center', padding: '20px 0', color: 'var(--text-muted, #94a3b8)', fontSize: '12px' }}>
                    📭 No questions in this filter.
                  </div>
                ) : (
                  filteredQuestions.map(qItem => {
                    const isUnanswered = qItem.type === 'unanswered';
                    const isUnderstood = reviewedQuestions.has(qItem.globalIdx);
                    const explanation = qItem.solution || qItem.explanation || '';
                    const currentReason = selectedReasons[qItem.globalIdx];

                    return (
                      <div
                        key={qItem.globalIdx}
                        style={{
                          padding: '14px 16px',
                          borderRadius: 'var(--radius, 8px)',
                          border: isUnderstood ? '1px solid rgba(46, 204, 113, 0.4)' : '1px solid var(--border-light, #334155)',
                          background: isUnderstood ? 'rgba(46, 204, 113, 0.04)' : 'var(--surface, #0f172a)',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '8px'
                        }}
                      >
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light, #334155)', paddingBottom: '6px', fontSize: '11px', color: 'var(--text-muted, #94a3b8)' }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <span style={{ fontWeight: 700, color: 'var(--text, #f8fafc)' }}>Question {qItem.qIndex !== undefined ? qItem.qIndex + 1 : qItem.globalIdx + 1}</span>
                            {currentReason && (
                              <span style={{ background: 'rgba(230, 126, 34, 0.15)', color: '#fb923c', padding: '2px 6px', borderRadius: '4px', fontSize: '9.5px', fontWeight: 'bold' }}>
                                ⚠️ Reason: {currentReason}
                              </span>
                            )}
                          </div>
                          <span style={{
                            fontWeight: 'bold',
                            fontSize: '10px',
                            padding: '2px 8px',
                            borderRadius: '12px',
                            background: isUnanswered ? 'rgba(149, 165, 166, 0.15)' : 'rgba(239, 68, 68, 0.15)',
                            color: isUnanswered ? '#94a3b8' : '#f87171'
                          }}>
                            {isUnanswered ? 'UNANSWERED' : 'INCORRECT'}
                          </span>
                        </div>

                        {/* Question Text */}
                        <div
                          className="math-container"
                          style={{ fontSize: '13px', lineHeight: '1.5', color: 'var(--text, #f8fafc)', fontWeight: 600 }}
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

                              let border = '1px solid var(--border-light, #334155)';
                              let background = 'var(--surface, #1e293b)';
                              let color = 'var(--text-muted, #94a3b8)';
                              let prefix = '';

                              if (isCorrectOpt) {
                                border = '1px solid rgba(46, 204, 113, 0.6)';
                                background = 'rgba(46, 204, 113, 0.12)';
                                color = '#4ade80';
                                prefix = '✓ ';
                              } else if (isUserOpt) {
                                border = '1px solid rgba(239, 68, 68, 0.6)';
                                background = 'rgba(239, 68, 68, 0.12)';
                                color = '#f87171';
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
                                    borderRadius: 'var(--radius-sm, 6px)',
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
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', fontSize: '11.5px', background: 'var(--surface-3, rgba(15, 23, 42, 0.7))', padding: '8px 10px', borderRadius: 'var(--radius-sm, 6px)', border: '1px solid var(--border-light, #334155)', margin: '4px 0' }}>
                          <div>
                            <strong style={{ color: 'var(--text-muted, #94a3b8)', marginRight: '6px' }}>Your Answer:</strong>
                            <span className="math-container" style={{ color: 'var(--text, #f8fafc)', fontWeight: 600 }}>
                              {isUnanswered ? '(blank)' : getOptionText(qItem, qItem.userAnswer)}
                            </span>
                          </div>
                          <div>
                            <strong style={{ color: 'var(--text-muted, #94a3b8)', marginRight: '6px' }}>Correct Answer:</strong>
                            <span className="math-container" style={{ color: '#4ade80', fontWeight: 'bold' }}>
                              {getOptionText(qItem, qItem.correctAnswer)}
                            </span>
                          </div>
                        </div>

                        {explanation && (
                          <div style={{ fontSize: '11.5px', color: 'var(--text-muted, #94a3b8)', borderTop: '1px dashed var(--border-light, #334155)', paddingTop: '6px' }}>
                            <strong style={{ color: '#93c5fd' }}>Solution Explanation:</strong>
                            <div className="math-container" style={{ margin: '3px 0 0 0', lineHeight: '1.4' }} dangerouslySetInnerHTML={{ __html: preprocessMathText(explanation) }} />
                          </div>
                        )}

                        {/* Error Reason Classification Box */}
                        <div style={{
                          marginTop: '6px',
                          border: '1px solid var(--border-light, #334155)',
                          borderRadius: 'var(--radius-sm, 6px)',
                          padding: '10px 12px',
                          background: 'var(--bg-soft, #1e293b)'
                        }}>
                          <span style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '6px', color: 'var(--text, #f8fafc)' }}>
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
                                    onClick={() => {
                                      if (!isUnderstood) {
                                        setSelectedReasons(prev => ({ ...prev, [qItem.globalIdx]: reason }));
                                      }
                                    }}
                                    disabled={isUnderstood}
                                    className="btn btn-sm"
                                    style={{
                                      fontSize: '10px',
                                      padding: '4px 8px',
                                      flex: 1,
                                      border: isSelected ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                                      background: isSelected ? 'var(--accent)' : 'var(--surface-2)',
                                      color: isSelected ? 'var(--text-on-accent)' : 'var(--text)',
                                      cursor: isUnderstood ? 'not-allowed' : 'pointer',
                                      whiteSpace: 'nowrap'
                                    }}
                                  >
                                    {reason}
                                  </button>
                                );
                              })}
                            </div>
                            <div style={{ display: 'flex', gap: '6px' }}>
                              {['Silly Mistake', 'Concept'].map(reason => {
                                const isSelected = selectedReasons[qItem.globalIdx] === reason;
                                return (
                                  <button
                                    key={reason}
                                    type="button"
                                    onClick={() => {
                                      if (!isUnderstood) {
                                        setSelectedReasons(prev => ({ ...prev, [qItem.globalIdx]: reason }));
                                      }
                                    }}
                                    disabled={isUnderstood}
                                    className="btn btn-sm"
                                    style={{
                                      fontSize: '10px',
                                      padding: '4px 8px',
                                      flex: 1,
                                      border: isSelected ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                                      background: isSelected ? 'var(--accent)' : 'var(--surface-2)',
                                      color: isSelected ? 'var(--text-on-accent)' : 'var(--text)',
                                      cursor: isUnderstood ? 'not-allowed' : 'pointer',
                                      whiteSpace: 'nowrap'
                                    }}
                                  >
                                    {reason}
                                  </button>
                                );
                              })}
                            </div>
                          </div>
                        </div>

                        <button
                          className="btn btn-sm"
                          disabled={isUnderstood || !selectedReasons[qItem.globalIdx]}
                          onClick={() => {
                            setReviewedQuestions(prev => {
                              const next = new Set(prev);
                              next.add(qItem.globalIdx);
                              return next;
                            });
                          }}
                          style={{
                            fontSize: '11px',
                            padding: '5px 14px',
                            alignSelf: 'flex-start',
                            marginTop: '6px',
                            background: isUnderstood ? 'var(--success-bg)' : selectedReasons[qItem.globalIdx] ? 'var(--accent)' : 'var(--surface-3)',
                            color: isUnderstood ? 'var(--success)' : (selectedReasons[qItem.globalIdx] ? 'var(--text-on-accent)' : 'var(--text-muted)'),
                            border: isUnderstood ? '1px solid rgba(52, 211, 153, 0.3)' : 'none',
                            borderRadius: '6px',
                            cursor: (isUnderstood || !selectedReasons[qItem.globalIdx]) ? 'default' : 'pointer'
                          }}
                        >
                          {isUnderstood ? '✓ Understood' : '🔘 I Understand'}
                        </button>
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
          <div style={{ padding: '14px 24px', borderTop: '1px solid var(--border-light, #334155)', display: 'flex', flexDirection: 'column', gap: '8px', background: 'var(--surface, #0f172a)' }}>
            <div style={{
              padding: '8px 12px',
              fontSize: '12px',
              textAlign: 'center',
              borderRadius: 'var(--radius-sm, 6px)',
              background: isAllReviewed ? 'rgba(46, 204, 113, 0.15)' : 'rgba(245, 158, 11, 0.15)',
              color: isAllReviewed ? '#4ade80' : '#fbbf24',
              border: isAllReviewed ? '1px solid #4ade80' : '1px solid #fbbf24',
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
                  background: isAllReviewed ? '#10b981' : '#475569',
                  color: '#ffffff',
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
