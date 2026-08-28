'use client';

import React, { useState } from 'react';
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
  formatUserAnswerSummary
} from '@/lib/questionTypes';
import { formatDateTimeIST } from '@/lib/dateUtils';

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
  const [questionFilterTab, setQuestionFilterTab] = useState<'all' | 'correct' | 'incorrect' | 'unanswered'>('all');

  // Dynamically load KaTeX and auto-render math expressions when scorecard changes or tab changes
  useMathRender([scorecard, questionFilterTab]);

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

  return (
    <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 35000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '10px 8px' }}>
      <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '850px', width: '100%', height: 'fit-content', maxHeight: '92vh', display: 'flex', flexDirection: 'column', overflowY: 'hidden' }}>
        
        <div className="modal-header" style={{ padding: '12px 16px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h4 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold' }}>
            📊 {scorecard?.examType === 'practice' ? 'Practice Review Scorecard' : 'Exam Review Scorecard'}
          </h4>
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
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>{scorecard.examType === 'practice' ? 'Topic' : 'Exam ID'}:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{scorecard.examType === 'practice' ? scorecard.topicName || scorecard.examName : scorecard.examName}</span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Date:</strong>{' '}
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
                  <span style={{ fontWeight: 600, color: scorecard.integrityScore < 70 ? '#f44336' : scorecard.integrityScore < 90 ? '#ff9800' : '#4caf50' }}>
                    {scorecard.integrityScore} / 100
                  </span>
                </div>
                <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                  <strong style={{ color: 'var(--text-muted)' }}>Tab Out:</strong>{' '}
                  <span style={{ fontWeight: 600 }}>{scorecard.tabViolations} times</span>
                </div>
                {scorecard.proctoringViolations && (
                  <>
                    <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                      <strong style={{ color: 'var(--text-muted)' }}>Gaze:</strong>{' '}
                      <span style={{ fontWeight: 600 }}>{scorecard.proctoringViolations.lookingAway || 0} times</span>
                    </div>
                    <div style={{ fontSize: '11px', lineHeight: '1.3' }}>
                      <strong style={{ color: 'var(--text-muted)' }}>No Face:</strong>{' '}
                      <span style={{ fontWeight: 600 }}>{scorecard.proctoringViolations.noFace || 0} times</span>
                    </div>
                  </>
                )}
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
              <h5 style={{ fontSize: '12px', fontWeight: 'bold', marginBottom: '8px', paddingBottom: '2px' }}>🔍 Question-by-Question Audit</h5>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {filteredQuestions.length === 0 ? (
                  <div style={{ textAlign: 'center', padding: '20px 0', color: 'var(--text-faint)', fontSize: '12px' }}>📭 No questions match this filter.</div>
                ) : (
                  filteredQuestions.map((q, idx) => {
                    const isUnanswered = isBlank(q.userAnswer);
                    
                    // Find option text for correct choice if it exists
                    let correctOptionsToRender: { label: string; text: string }[] = [];
                    if (q.options && q.options.length > 0) {
                      q.options.forEach((opt: any, optIdx: number) => {
                        const label = String.fromCharCode(65 + optIdx);
                        const isCorrectOpt = q.correctAnswers ? q.correctAnswers.includes(label) : (q.correctAnswer === label);
                        if (isCorrectOpt) {
                          correctOptionsToRender.push({
                            label,
                            text: opt.text || opt
                          });
                        }
                      });
                    }

                    return (
                      <div 
                        key={`${q.id || idx}_${idx}`} 
                        style={{
                          width: '100%',
                          padding: '10px 12px',
                          borderRadius: 'var(--radius-sm)',
                          border: '1.5px solid var(--review-card-border)',
                          background: 'var(--review-card-bg)',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '6px'
                        }}
                      >
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '4px', fontSize: '11px', color: 'var(--text-muted)' }}>
                          <div style={{ display: 'flex', alignItems: 'center' }}>
                            <span style={{ fontWeight: 600 }}>
                              Q{scorecard.questions.indexOf(q) !== -1 ? scorecard.questions.indexOf(q) + 1 : idx + 1}{' '}
                              ({(q.difficulty || 'MEDIUM').toUpperCase()} • {q.bloomLevel || 'Understand'})
                            </span>
                            {(() => {
                              const reason = getReasonForQuestion(q, scorecard);
                              if (!reason) return null;
                              return (
                                <span style={{ background: 'rgba(230,126,34,0.12)', color: '#d35400', padding: '1px 5px', borderRadius: '4px', fontSize: '9px', fontWeight: 'bold', marginLeft: '6px' }}>
                                  ⚠️ Reason: {reason}
                                </span>
                              );
                            })()}
                          </div>
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

                        {q.type === 'assertion_reason' ? (() => {
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
                        {q.options && q.options.length > 0 ? (
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', marginBottom: '8px' }}>
                            {q.options.map((opt: any, oi: number) => {
                              const optKey = getRawOptionKey(opt);
                              const optText = getRawOptionText(opt);
                              const correctAns = getQuestionCorrectAnswer(q);
                              
                              let isCorrectOpt = isOptionCorrect(correctAns, optKey, oi, optText);
                              const isUserOpt = isOptionSelectedByUser(q.userAnswer, optKey, oi, optText);

                              // Failsafe: if the question is overall evaluated as correct and user selected this option, it IS correct!
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
                                  {prefix && <span style={{ marginRight: '2px' }}>{prefix}</span>}
                                  <span className="math-container">{preprocessMathText(optText)}</span>
                                </div>
                              );
                            })}
                          </div>
                        ) : null}

                        {(() => {
                          const isObjective = (q.options && q.options.length > 0) || 
                            ['single_mcq', 'multiple_mcq', 'true_false', 'assertion_reason', 'fill_blanks', 'fill_blank', 'numerical', 'numerical_short', 'numerical_long'].includes(q.type);
                          
                          const correctDisplay = Array.isArray(q.correctAnswer)
                            ? q.correctAnswer.map((ca: any) => formatUserAnswerSummary(q.options, ca)).join(', ')
                            : (Array.isArray(q.correctAnswers) && q.correctAnswers.length > 0
                                ? q.correctAnswers.map((ca: any) => formatUserAnswerSummary(q.options, ca)).join(', ')
                                : (q.correctAnswer ? formatUserAnswerSummary(q.options, q.correctAnswer) : 'N/A'));

                          return isObjective ? (
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', fontSize: '11.5px', background: 'var(--surface-3)', padding: '6px 8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                              <div style={{ lineHeight: '1.3' }}>
                                <strong style={{ color: 'var(--text-muted)', marginRight: '6px' }}>Student Answer:</strong>
                                <span className="math-container" style={{ color: 'var(--text)', fontWeight: 600 }}>
                                  {preprocessMathText(
                                    isUnanswered
                                      ? '(blank)'
                                      : (q.options && q.options.length > 0
                                          ? formatUserAnswerSummary(q.options, q.userAnswer)
                                          : (q.userAnswer || '(blank)'))
                                  )}
                                </span>
                              </div>
                              <div style={{ lineHeight: '1.3' }}>
                                <strong style={{ color: 'var(--text-muted)', marginRight: '6px' }}>Correct Answer:</strong>
                                <span className="math-container" style={{ color: 'var(--success)', fontWeight: 'bold' }}>
                                  {preprocessMathText(correctDisplay)}
                                </span>
                              </div>
                            </div>
                          ) : (
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', fontSize: '12px', background: 'var(--surface-3)', padding: '12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                              <div style={{ fontWeight: 600, color: 'var(--text)' }}>
                                Total Marks: <span style={{ color: 'var(--accent)' }}>{(q as any).marks || 0}</span>
                              </div>
                              {(q as any).evaluations && (q as any).evaluations.length > 0 ? (
                                (q as any).evaluations.map((ev: any, ei: number) => (
                                  <div key={ei} style={{ borderTop: ei > 0 ? '1px dashed var(--border-light)' : 'none', paddingTop: ei > 0 ? '10px' : '0' }}>
                                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                                      <span style={{ fontWeight: 700, color: 'var(--text-muted)', textTransform: 'capitalize' }}>
                                        Evaluator: {ev.evaluatorType} {ev.evaluatorName ? `(${ev.evaluatorName})` : ''}
                                      </span>
                                      <span style={{ fontWeight: 800, color: 'var(--success)', fontSize: '13px' }}>
                                        Score: {ev.marksAwarded} / {ev.maxMarks}
                                      </span>
                                    </div>
                                    {ev.stepMarks && ev.stepMarks.length > 0 && (
                                      <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', margin: '6px 0', paddingLeft: '8px', borderLeft: '2px solid var(--accent)' }}>
                                        {ev.stepMarks.map((sm: any, smi: number) => {
                                          const stepDesc = (q as any).steps?.[sm.stepNo - 1]?.description || `Step ${sm.stepNo}`;
                                          return (
                                            <div key={smi} style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-muted)' }}>
                                              <span>{stepDesc}</span>
                                              <span style={{ fontWeight: 600 }}>{sm.awarded} marks</span>
                                            </div>
                                          );
                                        })}
                                      </div>
                                    )}
                                    {ev.feedback && (
                                      <div style={{ fontStyle: 'italic', color: 'var(--text)', background: 'var(--bg-soft)', padding: '6px 8px', borderRadius: '4px', marginTop: '6px' }}>
                                        💬 {ev.feedback}
                                      </div>
                                    )}
                                  </div>
                                ))
                              ) : (
                                <div style={{ fontStyle: 'italic', color: 'var(--text-muted)' }}>No grading evaluation available yet.</div>
                              )}
                            </div>
                          );
                        })()}

                        {q.solution && (
                          <div style={{ marginTop: '6px', fontSize: '11.5px', color: 'var(--text-muted)', borderTop: '1px dashed var(--border-light)', paddingTop: '6px' }}>
                            <strong>Solution Explanation:</strong>
                            <p className="math-container" style={{ margin: '2px 0 0 0', lineHeight: '1.35' }}>{preprocessMathText(q.solution)}</p>
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

        <div className="modal-footer" style={{ padding: '16px 24px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
          <button className="btn btn-secondary" onClick={onClose}>Close</button>
          {actionButton}
        </div>

      </div>
    </div>
  );
}
