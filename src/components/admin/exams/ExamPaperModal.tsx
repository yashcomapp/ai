'use client';

import React, { useEffect, useState, useMemo, useCallback } from 'react';
import { useAuth } from '@/context/AuthContext';
import { Exam } from '@/types/exam.types';
import { RichMathText } from '@/components/QuestionDisplay';
import { preprocessMathText } from '@/lib/questionTypes';

interface ExamPaperModalProps {
  show: boolean;
  onClose: () => void;
  exam: Exam | null;
  examType?: 'objective' | 'subjective';
  onExamUpdated?: () => void;
}

export default function ExamPaperModal({
  show,
  onClose,
  exam,
  examType = 'objective',
  onExamUpdated
}: ExamPaperModalProps) {
  const { firebaseUser, loading: authLoading } = useAuth();
  const [currentExam, setCurrentExam] = useState<Exam | null>(exam);
  const [loading, setLoading] = useState(false);
  const [questions, setQuestions] = useState<any[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [balancing, setBalancing] = useState(false);
  const [balanceMessage, setBalanceMessage] = useState<string | null>(null);

  const fetchExamPaper = useCallback(async (isRetry = false) => {
    if (!exam) return;
    setLoading(true);
    setError(null);

    try {
      let currentUser = firebaseUser;
      if (!currentUser && typeof window !== 'undefined') {
        const { auth } = await import('@/lib/firebase/client');
        currentUser = auth.currentUser;
      }
      
      let idToken = currentUser ? await currentUser.getIdToken(isRetry) : '';
      if (!idToken && typeof window !== 'undefined') {
        // Wait briefly if auth state was restoring
        await new Promise(r => setTimeout(r, 400));
        const { auth } = await import('@/lib/firebase/client');
        currentUser = auth.currentUser || firebaseUser;
        idToken = currentUser ? await currentUser.getIdToken(isRetry) : '';
      }

      const headers: Record<string, string> = {};
      if (idToken) {
        headers['Authorization'] = `Bearer ${idToken}`;
      }

      const res = await fetch(`/api/admin/exams?action=getExamPaper&id=${encodeURIComponent(exam.id)}&type=${examType}`, {
        headers
      });
      if (!res.ok) {
        if (res.status === 403 && !isRetry && currentUser) {
          // Stale claims or token expired: retry with forced refresh
          return fetchExamPaper(true);
        }
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.message || 'Failed to load exam paper details.');
      }
      const data = await res.json();
      setQuestions(data.questions || []);
      if (data.exam) {
        setCurrentExam(prev => ({ ...(prev || exam), ...data.exam }));
      }
    } catch (err: any) {
      setError(err.message || 'Error fetching exam questions.');
    } finally {
      setLoading(false);
    }
  }, [exam, examType, firebaseUser]);

  // Load questions whenever modal opens or exam changes
  useEffect(() => {
    if (!show || !exam) {
      setQuestions([]);
      setError(null);
      setBalanceMessage(null);
      setCurrentExam(null);
      return;
    }

    setCurrentExam(exam);
    fetchExamPaper();
  }, [show, exam, fetchExamPaper]);

  // Calculate answer distribution across questions
  const distribution = useMemo(() => {
    const counts: Record<string, number> = { A: 0, B: 0, C: 0, D: 0, Other: 0 };
    let objectiveCount = 0;

    questions.forEach(q => {
      const type = String(q.type || '').toUpperCase();
      if (type.startsWith('S') || type.includes('SUBJECTIVE') || type.includes('NUMERICAL_SHORT') || type.includes('NUMERICAL_LONG')) {
        return;
      }
      objectiveCount++;
      const ans = String(q.correctAnswer || '').trim().toUpperCase();
      if (['A', 'B', 'C', 'D'].includes(ans)) {
        counts[ans] = (counts[ans] || 0) + 1;
      } else {
        counts.Other = (counts.Other || 0) + 1;
      }
    });

    const isBiased = objectiveCount > 4 && Object.entries(counts).some(([k, v]) => k !== 'Other' && (v / objectiveCount) > 0.40);
    return { counts, objectiveCount, isBiased };
  }, [questions]);

  // Balance & Shuffle Options handler
  const handleBalanceOptions = async () => {
    if (!exam) return;
    setBalancing(true);
    setBalanceMessage(null);
    try {
      const idToken = firebaseUser ? await firebaseUser.getIdToken() : '';
      const headers: Record<string, string> = { 'Content-Type': 'application/json' };
      if (idToken) {
        headers['Authorization'] = `Bearer ${idToken}`;
      }

      const res = await fetch('/api/admin/exams', {
        method: 'POST',
        headers,
        body: JSON.stringify({
          action: 'balanceExamOptions',
          examId: exam.id,
          examType
        })
      });
      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.message || 'Failed to balance options.');
      }
      setQuestions(data.questions || []);
      setBalanceMessage('✅ Successfully balanced and shuffled options across all questions! Correct answers are now evenly distributed.');
      onExamUpdated?.();
    } catch (err: any) {
      alert(err.message || 'Error balancing exam options.');
    } finally {
      setBalancing(false);
    }
  };

  if (!show || !exam) return null;

  return (
    <div 
      className="modal-backdrop" 
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.75)',
        zIndex: 9999,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '16px'
      }}
      onClick={onClose}
    >
      <div 
        className="modal-content"
        style={{
          background: 'var(--surface, #1e293b)',
          color: 'var(--text, #f8fafc)',
          borderRadius: '12px',
          width: '100%',
          maxWidth: '960px',
          maxHeight: '90vh',
          display: 'flex',
          flexDirection: 'column',
          boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.5)',
          border: '1px solid var(--border-light, #334155)',
          overflow: 'hidden'
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div style={{
          padding: '16px 20px',
          borderBottom: '1px solid var(--border-light, #334155)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          background: 'var(--surface-header, #0f172a)'
        }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
              <span style={{ fontSize: '18px', fontWeight: 700 }}>📄 {exam.name || exam.title || exam.id}</span>
              <span style={{ fontSize: '12px', padding: '2px 8px', borderRadius: '4px', background: '#3b82f6', color: '#fff', fontWeight: 600 }}>
                Class {exam.class}
              </span>
              <span style={{ fontSize: '12px', padding: '2px 8px', borderRadius: '4px', background: '#10b981', color: '#fff', fontWeight: 600 }}>
                {currentExam?.subject || exam.subject || (exam as any).subjectCode || 'General'}
              </span>
              <span style={{ fontSize: '12px', padding: '2px 8px', borderRadius: '4px', background: '#6366f1', color: '#fff', fontWeight: 600 }}>
                {examType === 'subjective' ? 'Subjective' : 'Objective'}
              </span>
            </div>
            <div style={{ fontSize: '13px', color: '#94a3b8', marginTop: '4px' }}>
              {currentExam?.chapter || exam.chapter ? `Chapter: ${currentExam?.chapter || exam.chapter}` : ''} • Duration: {currentExam?.duration || exam.duration || 30} mins • Total Questions: {questions.length || (Array.isArray(currentExam?.questionCodes || exam.questionCodes) ? (currentExam?.questionCodes || exam.questionCodes)!.length : 0)} • Total Marks: {currentExam?.totalMarks || exam.totalMarks || ((questions.length || (Array.isArray(currentExam?.questionCodes || exam.questionCodes) ? (currentExam?.questionCodes || exam.questionCodes)!.length : 0)) * 4)}
            </div>
          </div>
          <button 
            onClick={onClose}
            style={{
              background: 'transparent',
              border: 'none',
              fontSize: '24px',
              color: '#94a3b8',
              cursor: 'pointer',
              padding: '4px 8px'
            }}
          >
            ✕
          </button>
        </div>

        {/* Answer Distribution & Integrity Bar (Objective only) */}
        {examType !== 'subjective' && distribution.objectiveCount > 0 && (
          <div style={{
            padding: '12px 20px',
            background: distribution.isBiased ? 'rgba(239, 68, 68, 0.12)' : 'rgba(16, 185, 129, 0.08)',
            borderBottom: '1px solid var(--border-light, #334155)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            flexWrap: 'wrap',
            gap: '12px'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px', flexWrap: 'wrap' }}>
              <span style={{ fontWeight: 600, fontSize: '13px' }}>
                {distribution.isBiased ? '⚠️ Option Bias Warning:' : '✅ Answer Key Distribution:'}
              </span>
              <div style={{ display: 'flex', gap: '8px', fontSize: '12px' }}>
                <span style={{ padding: '2px 8px', borderRadius: '4px', background: 'rgba(255,255,255,0.08)', fontWeight: 600 }}>
                  A: {distribution.counts.A} ({Math.round((distribution.counts.A / distribution.objectiveCount) * 100)}%)
                </span>
                <span style={{ padding: '2px 8px', borderRadius: '4px', background: 'rgba(255,255,255,0.08)', fontWeight: 600 }}>
                  B: {distribution.counts.B} ({Math.round((distribution.counts.B / distribution.objectiveCount) * 100)}%)
                </span>
                <span style={{ padding: '2px 8px', borderRadius: '4px', background: 'rgba(255,255,255,0.08)', fontWeight: 600 }}>
                  C: {distribution.counts.C} ({Math.round((distribution.counts.C / distribution.objectiveCount) * 100)}%)
                </span>
                <span style={{ padding: '2px 8px', borderRadius: '4px', background: 'rgba(255,255,255,0.08)', fontWeight: 600 }}>
                  D: {distribution.counts.D} ({Math.round((distribution.counts.D / distribution.objectiveCount) * 100)}%)
                </span>
                {distribution.counts.Other > 0 && (
                  <span style={{ padding: '2px 8px', borderRadius: '4px', background: 'rgba(148,163,184,0.18)', fontWeight: 600, color: '#cbd5e1' }}>
                    Other: {distribution.counts.Other} ({Math.round((distribution.counts.Other / distribution.objectiveCount) * 100)}%)
                  </span>
                )}
              </div>
            </div>

            <button
              onClick={handleBalanceOptions}
              disabled={balancing}
              style={{
                background: distribution.isBiased ? '#ef4444' : '#3b82f6',
                color: '#fff',
                border: 'none',
                borderRadius: '6px',
                padding: '6px 14px',
                fontSize: '12px',
                fontWeight: 600,
                cursor: balancing ? 'not-allowed' : 'pointer',
                display: 'inline-flex',
                alignItems: 'center',
                gap: '6px'
              }}
            >
              {balancing ? '⏳ Shuffling...' : '🔀 Re-Shuffle & Balance Options'}
            </button>
          </div>
        )}

        {balanceMessage && (
          <div style={{ padding: '10px 20px', background: 'rgba(16, 185, 129, 0.15)', color: '#10b981', fontSize: '13px', fontWeight: 600 }}>
            {balanceMessage}
          </div>
        )}

        {/* Question Body List */}
        <div style={{ flex: 1, overflowY: 'auto', padding: '20px' }}>
          {loading ? (
            <div style={{ textAlign: 'center', padding: '40px', color: '#94a3b8' }}>
              <div style={{ fontSize: '24px', marginBottom: '8px' }}>⏳</div>
              <div>Loading exam questions and answer keys...</div>
            </div>
          ) : error ? (
            <div style={{ textAlign: 'center', padding: '30px', color: '#ef4444' }}>
              <p>⚠️ {error}</p>
              <button 
                className="btn btn-secondary" 
                onClick={() => fetchExamPaper(true)} 
                style={{ marginTop: '10px' }}
              >
                Retry
              </button>
            </div>
          ) : questions.length === 0 ? (
            <div style={{ textAlign: 'center', padding: '40px', color: '#94a3b8' }}>
              No question documents found for this exam.
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
              {questions.map((q, qIdx) => {
                const options = Array.isArray(q.options) ? q.options : [];
                const normAns = String(q.correctAnswer || '').trim().toUpperCase();

                return (
                  <div
                    key={q.id || q.questionCode || qIdx}
                    style={{
                      background: 'rgba(255, 255, 255, 0.03)',
                      border: '1px solid var(--border-light, #334155)',
                      borderRadius: '8px',
                      padding: '16px'
                    }}
                  >
                    {/* Question Header */}
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                        <span style={{ fontWeight: 700, fontSize: '15px', color: '#38bdf8' }}>
                          Q{qIdx + 1}.
                        </span>
                        <span style={{ fontSize: '11px', fontFamily: 'monospace', padding: '2px 6px', borderRadius: '4px', background: 'rgba(255,255,255,0.06)' }}>
                          {q.questionCode || q.id}
                        </span>
                        <span style={{ fontSize: '11px', padding: '2px 6px', borderRadius: '4px', background: 'rgba(99, 102, 241, 0.2)', color: '#818cf8', fontWeight: 600 }}>
                          {q.type || 'OSC'}
                        </span>
                        <span style={{ 
                          fontSize: '11px', 
                          padding: '2px 6px', 
                          borderRadius: '4px', 
                          fontWeight: 600,
                          background: q.difficulty === 'hard' ? 'rgba(239, 68, 68, 0.2)' : q.difficulty === 'medium' ? 'rgba(245, 158, 11, 0.2)' : 'rgba(16, 185, 129, 0.2)',
                          color: q.difficulty === 'hard' ? '#f87171' : q.difficulty === 'medium' ? '#fbbf24' : '#34d399'
                        }}>
                          {q.difficulty || 'medium'}
                        </span>
                        <span style={{ fontSize: '11px', padding: '2px 6px', borderRadius: '4px', background: 'rgba(255,255,255,0.06)' }}>
                          {q.marks || 4} Marks
                        </span>
                      </div>
                    </div>

                    {/* Question Stem */}
                    <div style={{ fontSize: '14px', lineHeight: '1.6', marginBottom: '14px' }}>
                      <RichMathText content={preprocessMathText(q.text || q.questionText || '')} inline={false} />
                    </div>

                    {/* Options (for Objective) */}
                    {options.length > 0 && (
                      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '8px', marginBottom: '12px' }}>
                        {options.map((opt: any, oi: number) => {
                          const letter = String.fromCharCode(65 + oi);
                          const isObj = typeof opt === 'object' && opt !== null;
                          const optText = isObj ? opt.text : String(opt);
                          const isCorrect = isObj 
                            ? opt.isCorrect === true 
                            : (letter === normAns || optText === q.correctAnswer);

                          return (
                            <div
                              key={oi}
                              style={{
                                display: 'flex',
                                alignItems: 'flex-start',
                                gap: '8px',
                                padding: '8px 12px',
                                borderRadius: '6px',
                                border: isCorrect ? '1.5px solid #10b981' : '1px solid var(--border-light, #334155)',
                                background: isCorrect ? 'rgba(16, 185, 129, 0.12)' : 'rgba(255, 255, 255, 0.02)',
                                color: isCorrect ? '#34d399' : 'inherit'
                              }}
                            >
                              <span style={{ fontWeight: 700, fontSize: '13px' }}>
                                {isCorrect ? '✅ ' : ''}({letter})
                              </span>
                              <div style={{ flex: 1, fontSize: '13px' }}>
                                <RichMathText content={preprocessMathText(optText)} inline />
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    )}

                    {/* Solution / Explanation */}
                    {(q.solution || q.explanation) && (
                      <div style={{
                        marginTop: '10px',
                        padding: '10px 14px',
                        borderRadius: '6px',
                        background: 'rgba(255, 255, 255, 0.03)',
                        borderLeft: '3px solid #38bdf8',
                        fontSize: '13px',
                        color: '#cbd5e1'
                      }}>
                        <div style={{ fontWeight: 600, color: '#38bdf8', marginBottom: '4px' }}>💡 Solution:</div>
                        <RichMathText content={preprocessMathText(q.solution || q.explanation)} inline={false} />
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          )}
        </div>

        {/* Footer */}
        <div style={{
          padding: '12px 20px',
          borderTop: '1px solid var(--border-light, #334155)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          background: 'var(--surface-header, #0f172a)'
        }}>
          <div style={{ fontSize: '12px', color: '#94a3b8' }}>
            YASHCOM Learning OS • Exam Paper Inspector
          </div>
          <div style={{ display: 'flex', gap: '10px' }}>
            <button 
              className="btn btn-secondary" 
              onClick={() => window.print()}
              style={{
                padding: '6px 14px',
                borderRadius: '6px',
                border: '1px solid var(--border-light, #334155)',
                background: 'transparent',
                color: 'inherit',
                cursor: 'pointer',
                fontSize: '13px'
              }}
            >
              🖨️ Print Paper
            </button>
            <button 
              className="btn btn-primary" 
              onClick={onClose}
              style={{
                padding: '6px 16px',
                borderRadius: '6px',
                background: '#3b82f6',
                color: '#fff',
                border: 'none',
                cursor: 'pointer',
                fontWeight: 600,
                fontSize: '13px'
              }}
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
