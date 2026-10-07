'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import { formatDuration, formatDateTimeIST } from '@/lib/dateUtils';
import {
  preprocessMathText,
  extractAssertionAndReason,
  isMultipleChoiceType,
  isAssertionReasonType,
  parseAnswerList,
  isOptionMatch
} from '@/lib/questionTypes';

interface PracticeCompletionViewProps {
  finalResult: {
    score: number;
    totalQuestions: number;
    mastery: number;
    confidence: number;
    practiceNumber?: number;
    topicCode?: string;
    topicName?: string;
    completedAt?: string;
    questions: any[];
  };
  topicData: {
    topicCode: string;
    topicName?: string;
    masteryAtStart: number;
    idealTimeSeconds: number;
    currentSetNumber?: number;
    questions: any[];
  };
  totalSeconds: number;
  totalAwaySeconds: number;
  tabViolations: number;
  noFaceCount: number;
  multipleFacesCount: number;
  lookingAwayCount: number;
  userAnswers: string[];
  questionResults: (boolean | null)[];
}

export function PracticeCompletionView({
  finalResult,
  topicData,
  totalSeconds,
  totalAwaySeconds,
  tabViolations,
  noFaceCount,
  multipleFacesCount,
  lookingAwayCount,
  userAnswers,
  questionResults
}: PracticeCompletionViewProps) {
  const router = useRouter();
  const [showReviewList, setShowReviewList] = useState(false);
  const [reviewTab, setReviewTab] = useState<'all' | 'correct' | 'incorrect'>('all');

  const getIntegrityLevel = () => {
    const totalIssues = tabViolations + noFaceCount + multipleFacesCount + lookingAwayCount;
    if (totalIssues === 0) return { level: 'green', text: '🟢 Excellent Integrity', class: 'integrity-green' };
    if (totalIssues <= 5) return { level: 'yellow', text: '🟡 Good Integrity', class: 'integrity-yellow' };
    return { level: 'red', text: '🔴 Integrity Warning', class: 'integrity-red' };
  };

  const integrity = getIntegrityLevel();
  const masteryChange = finalResult.mastery - topicData.masteryAtStart;
  const efficiency = topicData.idealTimeSeconds > 0 ? Math.round((topicData.idealTimeSeconds / totalSeconds) * 100) : 0;
  const percentTimeAway = totalSeconds > 0 ? Math.round((totalAwaySeconds / totalSeconds) * 100) : 0;
  const practiceNum = finalResult.practiceNumber || topicData.currentSetNumber || 1;
  const practiceTopicName = finalResult.topicName || topicData.topicName || topicData.topicCode;
  const completedTimestampIST = formatDateTimeIST(finalResult.completedAt || new Date()) || '-';

  const evalQuestions = finalResult.questions && finalResult.questions.length > 0 
    ? finalResult.questions 
    : topicData.questions.map((q, idx) => ({
        ...q,
        userAnswer: userAnswers[idx] || '',
        isCorrect: questionResults[idx] === true
      }));

  const filteredReviewQuestions = evalQuestions.filter(q => {
    if (reviewTab === 'correct') return q.isCorrect;
    if (reviewTab === 'incorrect') return !q.isCorrect;
    return true;
  });

  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', padding: '20px', background: 'var(--bg)' }}>
      <div className="card results-card" style={{ maxWidth: '680px', width: '100%', textAlign: 'center', padding: '28px 24px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
        
        {/* Header Badge with Practice Number and IST Date/Time */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', marginBottom: '16px', borderBottom: '1px solid var(--border-light)', paddingBottom: '12px' }}>
          <span style={{ background: 'var(--accent)', color: 'var(--text-on-accent)', fontSize: '12px', fontWeight: 800, padding: '4px 10px', borderRadius: '14px' }}>
            📚 Practice Set #{practiceNum}
          </span>
          <span style={{ fontSize: '12px', color: 'var(--text-muted)', fontWeight: 600 }}>
            🗓️ {completedTimestampIST}
          </span>
        </div>

        <h2 style={{ fontSize: '1.4rem', fontWeight: 800, marginBottom: '6px' }}>Practice Complete!</h2>
        <div style={{ fontSize: '13px', color: 'var(--accent)', fontWeight: 700, marginBottom: '16px' }}>
          {practiceTopicName} <span style={{ opacity: 0.7, fontWeight: 500 }}>({topicData.topicCode})</span>
        </div>

        <div className="score-big" style={{ fontSize: '3.5rem', fontWeight: 900, color: 'var(--accent)', margin: '10px 0', lineHeight: '1.1' }}>
          {finalResult.score}/{finalResult.totalQuestions}
        </div>
        <p style={{ fontSize: '20px', fontWeight: 'bold', margin: '4px 0 12px 0' }}>
          {Math.round((finalResult.score / finalResult.totalQuestions) * 100)}% Accuracy
        </p>
        <p style={{ margin: '8px 0', fontSize: '14px' }}>
          Mastery: {topicData.masteryAtStart}% → {finalResult.mastery}% ({masteryChange >= 0 ? `+${masteryChange}` : masteryChange}%)
        </p>
        <p style={{ margin: '4px 0', fontSize: '13px', color: 'var(--text-muted)' }}>
          ⏱️ Time: {formatDuration(totalSeconds)} / Ideal: {formatDuration(topicData.idealTimeSeconds)} ({efficiency}% efficiency)
        </p>

        <div style={{ background: 'var(--bg-soft)', borderRadius: 'var(--radius)', padding: '14px', margin: '16px 0', textAlign: 'left' }}>
          <div className={`integrity-level`} style={{ fontWeight: 'bold', fontSize: '13px', marginBottom: '6px' }}>{integrity.text}</div>
          {integrity.level !== 'green' && (
            <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
              {tabViolations > 0 && <p style={{ margin: '2px 0' }}>• Tab switches: {tabViolations} times</p>}
              {totalAwaySeconds > 0 && <p style={{ margin: '2px 0' }}>• Time away: {formatDuration(totalAwaySeconds)} ({percentTimeAway}% of total)</p>}
              {noFaceCount > 0 && <p style={{ margin: '2px 0' }}>• Face not detected: {noFaceCount} checks</p>}
              {lookingAwayCount > 0 && <p style={{ margin: '2px 0' }}>• Gaze violations: {lookingAwayCount} checks</p>}
            </div>
          )}
        </div>

        {/* Toggle Full Question Review */}
        <div style={{ margin: '16px 0' }}>
          <button 
            className="btn btn-secondary" 
            onClick={() => setShowReviewList(!showReviewList)} 
            style={{ width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px', padding: '10px', fontSize: '13px', fontWeight: 700 }}
          >
            <span>{showReviewList ? '▲ Hide Detailed Review' : '▼ Review All Practice Questions & Solutions'}</span>
          </button>
        </div>

        {showReviewList && (
          <div style={{ textAlign: 'left', marginTop: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius)', padding: '16px', border: '1px solid var(--border-light)' }}>
            <div style={{ display: 'flex', gap: '8px', marginBottom: '14px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px' }}>
              <button 
                onClick={() => setReviewTab('all')} 
                style={{
                  padding: '4px 10px',
                  fontSize: '11px',
                  fontWeight: 'bold',
                  borderRadius: 'var(--radius-sm)',
                  border: reviewTab === 'all' ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                  background: reviewTab === 'all' ? 'var(--accent-soft)' : 'transparent',
                  color: reviewTab === 'all' ? 'var(--accent)' : 'var(--text-muted)',
                  cursor: 'pointer'
                }}
              >
                All ({evalQuestions.length})
              </button>
              <button 
                onClick={() => setReviewTab('correct')} 
                style={{
                  padding: '4px 10px',
                  fontSize: '11px',
                  fontWeight: 'bold',
                  borderRadius: 'var(--radius-sm)',
                  border: reviewTab === 'correct' ? '1px solid var(--success)' : '1px solid var(--border-light)',
                  background: reviewTab === 'correct' ? 'var(--success-bg)' : 'transparent',
                  color: reviewTab === 'correct' ? 'var(--success)' : 'var(--text-muted)',
                  cursor: 'pointer'
                }}
              >
                Correct ({evalQuestions.filter((q: any) => q.isCorrect).length})
              </button>
              <button 
                onClick={() => setReviewTab('incorrect')} 
                style={{
                  padding: '4px 10px',
                  fontSize: '11px',
                  fontWeight: 'bold',
                  borderRadius: 'var(--radius-sm)',
                  border: reviewTab === 'incorrect' ? '1px solid var(--danger)' : '1px solid var(--border-light)',
                  background: reviewTab === 'incorrect' ? 'var(--danger-soft)' : 'transparent',
                  color: reviewTab === 'incorrect' ? 'var(--danger)' : 'var(--text-muted)',
                  cursor: 'pointer'
                }}
              >
                Incorrect ({evalQuestions.filter((q: any) => !q.isCorrect).length})
              </button>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px', maxHeight: '420px', overflowY: 'auto', paddingRight: '4px' }}>
              {filteredReviewQuestions.map((qItem: any, idx: number) => {
                const isMulti = isMultipleChoiceType(qItem.type);
                const parsedUserAns = isMulti 
                  ? (Array.isArray(qItem.userAnswer) ? qItem.userAnswer : parseAnswerList(qItem.userAnswer))
                  : [qItem.userAnswer];
                const parsedCorrectAns = isMulti
                  ? (Array.isArray(qItem.correctAnswers) && qItem.correctAnswers.length > 0 ? qItem.correctAnswers : (Array.isArray(qItem.correctAnswer) ? qItem.correctAnswer : parseAnswerList(qItem.correctAnswer)))
                  : [qItem.correctAnswer || (Array.isArray(qItem.correctAnswers) ? qItem.correctAnswers[0] : '')];

                return (
                  <div key={idx} style={{ background: 'var(--surface)', padding: '12px', borderRadius: 'var(--radius-sm)', border: `1px solid ${qItem.isCorrect ? 'var(--success)' : 'var(--danger)'}` }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                      <span style={{ fontWeight: 800, fontSize: '12px' }}>Q#{idx + 1} {qItem.questionCode ? `• ${qItem.questionCode}` : ''}</span>
                      <span style={{ fontSize: '11px', fontWeight: 700, padding: '2px 8px', borderRadius: '4px', background: qItem.isCorrect ? 'var(--success-bg)' : 'var(--danger-soft)', color: qItem.isCorrect ? 'var(--success)' : 'var(--danger)' }}>
                        {qItem.isCorrect ? '✓ Correct' : '✕ Incorrect'}
                      </span>
                    </div>
                    {isAssertionReasonType(qItem.type) ? (() => {
                      const { assertion, reason } = extractAssertionAndReason(qItem);
                      return (
                        <div style={{ margin: '6px 0 10px', display: 'flex', flexDirection: 'column', gap: '4px', fontSize: '13px' }}>
                          <p style={{ margin: 0 }}><strong>Assertion (A):</strong> <span className="math-container" dangerouslySetInnerHTML={{ __html: preprocessMathText(assertion) }} /></p>
                          <p style={{ margin: 0 }}><strong>Reason (R):</strong> <span className="math-container" dangerouslySetInnerHTML={{ __html: preprocessMathText(reason) }} /></p>
                        </div>
                      );
                    })() : (
                      <div className="math-container" style={{ fontSize: '13px', lineHeight: '1.5', marginBottom: '8px', fontWeight: 500 }} dangerouslySetInnerHTML={{ __html: preprocessMathText(qItem.text || qItem.assertion || '') }} />
                    )}
                    
                    {qItem.options && Array.isArray(qItem.options) && qItem.options.length > 0 && (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', marginBottom: '8px' }}>
                        {qItem.options.map((opt: any, optIdx: number) => {
                          const optText = typeof opt === 'string' ? opt : (opt.text || opt.value || '');
                          const optKey = typeof opt === 'string' ? String.fromCharCode(65 + optIdx) : (opt.key || String.fromCharCode(65 + optIdx));
                          const isSelected = parsedUserAns.some((a: string) => isOptionMatch(optText, a) || isOptionMatch(optKey, a));
                          const isRight = parsedCorrectAns.some((a: string) => isOptionMatch(optText, a) || isOptionMatch(optKey, a));

                          let optBg = 'transparent';
                          let optBorder = 'var(--border-light)';
                          let optColor = 'inherit';
                          if (isRight) {
                            optBg = 'var(--success-bg)';
                            optBorder = 'var(--success)';
                            optColor = 'var(--success)';
                          } else if (isSelected && !isRight) {
                            optBg = 'var(--danger-soft)';
                            optBorder = 'var(--danger)';
                            optColor = 'var(--danger)';
                          }

                          return (
                            <div key={optIdx} style={{ padding: '6px 10px', fontSize: '12px', borderRadius: '4px', background: optBg, border: `1px solid ${optBorder}`, color: optColor, display: 'flex', gap: '6px' }}>
                              <span style={{ fontWeight: 700 }}>({optKey})</span>
                              <span className="math-container" dangerouslySetInnerHTML={{ __html: preprocessMathText(optText) }} />
                              {isSelected && <span style={{ marginLeft: 'auto', fontWeight: 700, fontSize: '11px' }}>[Your Answer]</span>}
                              {isRight && <span style={{ marginLeft: isSelected ? '4px' : 'auto', fontWeight: 700, fontSize: '11px' }}>[Correct]</span>}
                            </div>
                          );
                        })}
                      </div>
                    )}

                    {qItem.solution && (
                      <div style={{ marginTop: '8px', padding: '8px 10px', background: 'var(--bg-soft)', borderRadius: '4px', fontSize: '12px', borderLeft: '3px solid var(--accent)' }}>
                        <strong style={{ color: 'var(--accent)' }}>Explanation:</strong>{' '}
                        <span className="math-container" dangerouslySetInnerHTML={{ __html: preprocessMathText(qItem.solution) }} />
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        )}

        <div style={{ display: 'flex', gap: '12px', justifyContent: 'center', marginTop: '24px' }}>
          <button className="btn btn-primary" onClick={() => router.push('/student')} style={{ flex: 1 }}>Dashboard</button>
          <button className="btn btn-secondary" onClick={() => window.location.reload()} style={{ flex: 1 }}>Practice Again</button>
        </div>
      </div>
    </div>
  );
}
