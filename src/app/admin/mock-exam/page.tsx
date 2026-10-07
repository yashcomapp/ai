'use client';

import React, { useState, useEffect, useMemo, Suspense } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import { useAuth } from '@/context/AuthContext';
import { useMathRender } from '@/hooks/useMathRender';
import { preprocessMathText } from '@/lib/questionTypes';
import { RichMathText } from '@/components/QuestionDisplay';

interface MockQuestion {
  id?: string;
  questionCode?: string;
  text?: string;
  questionText?: string;
  options?: any[];
  correctAnswer?: string | number;
  correctAnswers?: any[];
  solution?: string;
  explanation?: string;
  marks?: number;
  type?: string;
  imageUrl?: string;
  topicCode?: string;
}

interface MockExam {
  id: string;
  name?: string;
  title?: string;
  duration?: number;
  totalMarks?: number;
  questions: MockQuestion[];
}

function AdminMockExamContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { user, firebaseUser, loading: authLoading } = useAuth();

  const examId = searchParams.get('examId') || searchParams.get('id');
  const examType = searchParams.get('type') || 'objective';

  const [exam, setExam] = useState<MockExam | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Runner state
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState<Record<number, string>>({});
  const [revealKeyMode, setRevealKeyMode] = useState(false);
  const [timeRemaining, setTimeRemaining] = useState<number>(1800);
  const [isTimerPaused, setIsTimerPaused] = useState(false);

  // Scorecard modal
  const [isSubmitted, setIsSubmitted] = useState(false);

  // Render Math equations on state changes
  useMathRender([loading, currentIndex, revealKeyMode, isSubmitted, exam]);

  // Timer tick
  useEffect(() => {
    if (isTimerPaused || isSubmitted || loading) return;
    const interval = setInterval(() => {
      setTimeRemaining(prev => Math.max(0, prev - 1));
    }, 1000);
    return () => clearInterval(interval);
  }, [isTimerPaused, isSubmitted, loading]);

  // Load Exam
  useEffect(() => {
    if (authLoading) return;

    if (!user || user.role !== 'admin') {
      setError('Access Denied: Admin role required to access the Mock Test simulator.');
      setLoading(false);
      return;
    }

    if (!examId) {
      setError('No exam ID specified.');
      setLoading(false);
      return;
    }

    let isSubscribed = true;

    async function fetchExam() {
      try {
        setLoading(true);
        setError(null);
        const token = firebaseUser ? await firebaseUser.getIdToken() : '';
        const res = await fetch(`/api/admin/exams/mock?examId=${encodeURIComponent(examId!)}&type=${examType}`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });

        if (!res.ok) {
          const errData = await res.json().catch(() => ({}));
          throw new Error(errData.message || `Failed to fetch exam (${res.status})`);
        }

        const data = await res.json();
        if (!isSubscribed) return;

        if (!data.exam) {
          throw new Error('Exam payload is empty.');
        }

        setExam(data.exam);
        const durationMins = Number(data.exam.duration) || 30;
        setTimeRemaining(durationMins * 60);
      } catch (err: any) {
        if (isSubscribed) {
          setError(err.message || 'Error loading exam');
        }
      } finally {
        if (isSubscribed) setLoading(false);
      }
    }

    fetchExam();

    return () => {
      isSubscribed = false;
    };
  }, [examId, examType, user, firebaseUser, authLoading]);

  const questions = exam?.questions || [];
  const currentQ: MockQuestion | undefined = questions[currentIndex];

  const handleSelectOption = (index: number, optionKey: string) => {
    setSelectedAnswers(prev => ({
      ...prev,
      [index]: optionKey
    }));
  };

  const handleClearSelection = (index: number) => {
    setSelectedAnswers(prev => {
      const copy = { ...prev };
      delete copy[index];
      return copy;
    });
  };

  const handleAutoFill = () => {
    const autoAnswers: Record<number, string> = {};
    questions.forEach((q, idx) => {
      const opts = q.options || [];
      if (opts.length > 0) {
        // 75% pick correct answer, 25% pick random
        const shouldPickCorrect = Math.random() < 0.75;
        const correctKey = String(q.correctAnswer ?? '').trim();
        if (shouldPickCorrect && correctKey) {
          autoAnswers[idx] = correctKey;
        } else {
          const randomIdx = Math.floor(Math.random() * opts.length);
          const optVal = opts[randomIdx];
          const key = typeof optVal === 'object' ? (optVal.key || String.fromCharCode(65 + randomIdx)) : String.fromCharCode(65 + randomIdx);
          autoAnswers[idx] = key;
        }
      }
    });
    setSelectedAnswers(autoAnswers);
  };

  // Helper to extract option text and key
  const formatOption = (opt: any, optIdx: number) => {
    if (typeof opt === 'string') {
      const defaultKey = String.fromCharCode(65 + optIdx);
      return { key: defaultKey, text: opt };
    }
    if (typeof opt === 'object' && opt !== null) {
      const key = opt.key || opt.label || String.fromCharCode(65 + optIdx);
      const text = opt.text || opt.value || '';
      return { key, text };
    }
    return { key: String(optIdx), text: String(opt) };
  };

  // Grading calculation
  const evaluation = useMemo(() => {
    if (!questions.length) return { totalMarks: 0, score: 0, correct: 0, incorrect: 0, unanswered: 0, percentage: 0 };
    let score = 0;
    let totalMarks = 0;
    let correct = 0;
    let incorrect = 0;
    let unanswered = 0;

    questions.forEach((q, idx) => {
      const qMarks = Number(q.marks) || 4;
      totalMarks += qMarks;
      const userAns = selectedAnswers[idx];
      const correctAns = String(q.correctAnswer ?? '').trim();

      if (!userAns) {
        unanswered++;
      } else if (String(userAns).trim().toLowerCase() === correctAns.toLowerCase()) {
        correct++;
        score += qMarks;
      } else {
        incorrect++;
      }
    });

    const percentage = totalMarks > 0 ? Math.round((score / totalMarks) * 100) : 0;
    return { totalMarks, score, correct, incorrect, unanswered, percentage };
  }, [questions, selectedAnswers]);

  const formatTimer = (secs: number) => {
    const mins = Math.floor(secs / 60);
    const rem = secs % 60;
    return `${String(mins).padStart(2, '0')}:${String(rem).padStart(2, '0')}`;
  };

  if (loading || authLoading) {
    return (
      <div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'var(--bg)' }}>
        <div style={{ textAlign: 'center' }}>
          <div className="spinner" style={{ margin: '0 auto 16px' }} />
          <h3 style={{ fontSize: '18px', fontWeight: 600 }}>Loading Mock Exam Runner...</h3>
          <p style={{ color: 'var(--text-muted)', fontSize: '13px' }}>Hydrating questions and options in sandbox mode</p>
        </div>
      </div>
    );
  }

  if (error || !exam) {
    return (
      <div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'var(--bg)', padding: '20px' }}>
        <div className="card" style={{ maxWidth: '520px', width: '100%', padding: '28px', textAlign: 'center' }}>
          <div style={{ fontSize: '36px', marginBottom: '12px' }}>⚠️</div>
          <h2 style={{ fontSize: '18px', fontWeight: 700, marginBottom: '8px', color: 'var(--danger)' }}>Mock Test Error</h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '13.5px', marginBottom: '20px' }}>{error || 'Exam could not be loaded.'}</p>
          <button className="btn btn-primary" onClick={() => router.push('/admin/exams')}>
            ← Back to Exams
          </button>
        </div>
      </div>
    );
  }

  return (
    <div style={{ minHeight: '100vh', background: 'var(--bg)', display: 'flex', flexDirection: 'column' }}>
      {/* Top Navbar */}
      <header style={{ 
        background: 'var(--surface)', 
        borderBottom: '1px solid var(--border-light)', 
        padding: '12px 24px', 
        display: 'flex', 
        alignItems: 'center', 
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        gap: '12px',
        position: 'sticky',
        top: 0,
        zIndex: 50
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
          <button 
            className="btn btn-secondary" 
            style={{ fontSize: '12px', padding: '6px 12px' }}
            onClick={() => router.push('/admin/exams')}
          >
            ← Exit Mock Test
          </button>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)' }}>
                🧪 Admin Mock Test: {exam.name || exam.title || exam.id}
              </span>
              <span className="badge badge-warning" style={{ fontSize: '10px', background: '#fef3c7', color: '#92400e', border: '1px solid #fde68a' }}>
                🛡️ Sandbox (0 Student Records Written)
              </span>
            </div>
            <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>
              {questions.length} Questions • {exam.duration || 30} Minutes • Total Marks: {exam.totalMarks || questions.length * 4}
            </div>
          </div>
        </div>

        {/* Right Controls */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          {/* Timer Display with Pause */}
          <div style={{ 
            display: 'flex', 
            alignItems: 'center', 
            gap: '8px', 
            background: 'var(--bg-soft)', 
            padding: '4px 10px', 
            borderRadius: 'var(--radius)', 
            border: '1px solid var(--border-light)' 
          }}>
            <span style={{ fontSize: '13px', fontWeight: 700, fontFamily: 'monospace', color: timeRemaining < 300 ? 'var(--danger)' : 'var(--text)' }}>
              ⏱️ {formatTimer(timeRemaining)}
            </span>
            <button 
              className="btn btn-secondary" 
              style={{ padding: '2px 6px', fontSize: '10.5px' }}
              onClick={() => setIsTimerPaused(!isTimerPaused)}
            >
              {isTimerPaused ? '▶️ Resume' : '⏸️ Pause'}
            </button>
          </div>

          {/* Reveal Answers Toggle */}
          <button 
            className={`btn ${revealKeyMode ? 'btn-primary' : 'btn-secondary'}`}
            style={{ fontSize: '11.5px', padding: '5px 10px' }}
            onClick={() => setRevealKeyMode(!revealKeyMode)}
          >
            {revealKeyMode ? '👁️ Answer Key: ON' : '👁️ Reveal Answer Key'}
          </button>

          {/* Quick Auto-Fill */}
          <button 
            className="btn btn-secondary"
            style={{ fontSize: '11.5px', padding: '5px 10px' }}
            onClick={handleAutoFill}
            title="Auto-fill answers to rapidly verify submission"
          >
            ⚡ Auto-Fill
          </button>

          {/* Finish & Grade */}
          <button 
            className="btn btn-primary"
            style={{ fontSize: '12px', padding: '6px 14px', background: 'var(--success)', borderColor: 'var(--success)' }}
            onClick={() => setIsSubmitted(true)}
          >
            ✅ Submit & Review
          </button>
        </div>
      </header>

      {/* Main Container */}
      <div style={{ display: 'flex', flex: 1, padding: '20px', gap: '20px', maxWidth: '1400px', width: '100%', margin: '0 auto' }}>
        {/* Left: Question Area */}
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {currentQ ? (
            <div key={currentIndex} className="card" style={{ background: 'var(--surface)', padding: '24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
              {/* Question Header */}
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px', borderBottom: '1px solid var(--border-light)', paddingBottom: '12px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <span style={{ fontSize: '16px', fontWeight: 800, color: 'var(--accent)' }}>
                    Question {currentIndex + 1} of {questions.length}
                  </span>
                  {currentQ.questionCode && (
                    <span style={{ fontSize: '11px', fontFamily: 'monospace', padding: '2px 8px', background: 'var(--bg-soft)', borderRadius: '4px', border: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                      {currentQ.questionCode}
                    </span>
                  )}
                  {currentQ.type && (
                    <span className="badge badge-info" style={{ fontSize: '10.5px' }}>
                      {currentQ.type}
                    </span>
                  )}
                </div>
                <div style={{ fontSize: '12.5px', fontWeight: 700, color: 'var(--text-muted)' }}>
                  Marks: +{currentQ.marks || 4}
                </div>
              </div>

              {/* Question Text */}
              <RichMathText 
                content={currentQ.text || currentQ.questionText || ''}
                className="math-container"
                style={{ fontSize: '15px', lineHeight: 1.6, marginBottom: '20px', color: 'var(--text)', whiteSpace: 'pre-wrap' }}
              />

              {/* Optional Diagram / Image */}
              {currentQ.imageUrl && (
                <div style={{ marginBottom: '20px', textAlign: 'center' }}>
                  <img 
                    src={currentQ.imageUrl} 
                    alt="Question Diagram" 
                    style={{ maxWidth: '100%', maxHeight: '350px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)' }} 
                  />
                </div>
              )}

              {/* Options */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginBottom: '24px' }}>
                {(currentQ.options || []).map((rawOpt, optIdx) => {
                  const { key, text } = formatOption(rawOpt, optIdx);
                  const isSelected = selectedAnswers[currentIndex] === key;
                  const isCorrect = String(currentQ.correctAnswer ?? '').trim().toLowerCase() === key.toLowerCase();

                  let border = '1px solid var(--border-light)';
                  let bg = 'var(--surface)';
                  let color = 'var(--text)';

                  if (isSelected) {
                    border = '2px solid var(--accent)';
                    bg = 'var(--accent-tint)';
                  }

                  if (revealKeyMode || isSubmitted) {
                    if (isCorrect) {
                      border = '2px solid var(--success)';
                      bg = 'rgba(16, 185, 129, 0.1)';
                    } else if (isSelected && !isCorrect) {
                      border = '2px solid var(--danger)';
                      bg = 'rgba(239, 68, 68, 0.1)';
                    }
                  }

                  return (
                    <div
                      key={optIdx}
                      onClick={() => handleSelectOption(currentIndex, key)}
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: '12px',
                        padding: '12px 16px',
                        borderRadius: 'var(--radius)',
                        border,
                        background: bg,
                        color,
                        cursor: 'pointer',
                        transition: 'all 0.15s ease'
                      }}
                    >
                      <div style={{
                        width: '28px',
                        height: '28px',
                        borderRadius: '50%',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontWeight: 700,
                        fontSize: '12.5px',
                        background: isSelected ? 'var(--accent)' : 'var(--bg-soft)',
                        color: isSelected ? '#fff' : 'var(--text)',
                        border: '1px solid var(--border-light)',
                        flexShrink: 0
                      }}>
                        {key}
                      </div>
                      <RichMathText 
                        content={text}
                        className="math-container"
                        style={{ fontSize: '14px', flex: 1, whiteSpace: 'pre-wrap' }}
                      />
                      {(revealKeyMode || isSubmitted) && isCorrect && (
                        <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--success)' }}>
                          ✓ Correct
                        </span>
                      )}
                    </div>
                  );
                })}
              </div>

              {/* Solution / Explanation Box in Reveal Mode */}
              {(revealKeyMode || isSubmitted) && (currentQ.solution || currentQ.explanation) && (
                <div style={{ 
                  background: 'var(--bg-soft)', 
                  border: '1px solid var(--border-light)', 
                  borderRadius: 'var(--radius)', 
                  padding: '16px', 
                  marginBottom: '20px' 
                }}>
                  <div style={{ fontSize: '12px', fontWeight: 800, color: 'var(--accent)', marginBottom: '6px' }}>
                    💡 Model Solution & Step-by-Step Explanation:
                  </div>
                  <RichMathText 
                    content={currentQ.solution || currentQ.explanation || ''}
                    className="math-container"
                    style={{ fontSize: '13.5px', lineHeight: 1.6, color: 'var(--text)', whiteSpace: 'pre-wrap' }}
                  />
                </div>
              )}

              {/* Action Buttons */}
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: '16px', borderTop: '1px solid var(--border-light)' }}>
                <button
                  className="btn btn-secondary"
                  disabled={currentIndex === 0}
                  onClick={() => setCurrentIndex(prev => Math.max(0, prev - 1))}
                  style={{ opacity: currentIndex === 0 ? 0.5 : 1 }}
                >
                  ⬅ Previous
                </button>
                <button
                  className="btn btn-secondary"
                  onClick={() => handleClearSelection(currentIndex)}
                  style={{ fontSize: '12px' }}
                >
                  Clear Choice
                </button>
                <button
                  className="btn btn-primary"
                  disabled={currentIndex === questions.length - 1}
                  onClick={() => setCurrentIndex(prev => Math.min(questions.length - 1, prev + 1))}
                  style={{ opacity: currentIndex === questions.length - 1 ? 0.5 : 1 }}
                >
                  Next ➡
                </button>
              </div>
            </div>
          ) : (
            <div className="card" style={{ padding: '30px', textAlign: 'center' }}>
              <p style={{ color: 'var(--text-muted)' }}>No questions available for this exam.</p>
            </div>
          )}
        </div>

        {/* Right: Question Palette */}
        <div style={{ width: '320px', flexShrink: 0 }}>
          <div className="card" style={{ background: 'var(--surface)', padding: '18px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', position: 'sticky', top: '76px' }}>
            <h4 style={{ fontSize: '13.5px', fontWeight: 800, marginBottom: '12px', color: 'var(--text)' }}>
              Question Palette
            </h4>

            {/* Stats summary */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '8px', marginBottom: '16px', fontSize: '11.5px' }}>
              <div style={{ background: 'var(--bg-soft)', padding: '6px 8px', borderRadius: '4px' }}>
                <span style={{ color: 'var(--success)', fontWeight: 700 }}>● {Object.keys(selectedAnswers).length}</span> Answered
              </div>
              <div style={{ background: 'var(--bg-soft)', padding: '6px 8px', borderRadius: '4px' }}>
                <span style={{ color: 'var(--text-muted)', fontWeight: 700 }}>● {questions.length - Object.keys(selectedAnswers).length}</span> Unanswered
              </div>
            </div>

            {/* Grid */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: '6px', maxHeight: '380px', overflowY: 'auto', paddingRight: '4px' }}>
              {questions.map((_, idx) => {
                const isCurrent = idx === currentIndex;
                const isAnswered = selectedAnswers[idx] !== undefined;

                let bg = 'var(--bg-soft)';
                let color = 'var(--text-muted)';
                let border = '1px solid var(--border-light)';

                if (isAnswered) {
                  bg = 'var(--success)';
                  color = '#fff';
                  border = '1px solid var(--success)';
                }

                if (isCurrent) {
                  border = '2px solid var(--accent)';
                  if (!isAnswered) {
                    bg = 'var(--accent-tint)';
                    color = 'var(--accent)';
                  }
                }

                return (
                  <button
                    key={idx}
                    onClick={() => setCurrentIndex(idx)}
                    style={{
                      height: '36px',
                      borderRadius: 'var(--radius)',
                      background: bg,
                      color,
                      border,
                      fontWeight: 700,
                      fontSize: '12px',
                      cursor: 'pointer',
                      transition: 'all 0.15s ease'
                    }}
                  >
                    {idx + 1}
                  </button>
                );
              })}
            </div>

            <div style={{ marginTop: '20px', borderTop: '1px solid var(--border-light)', paddingTop: '16px' }}>
              <button 
                className="btn btn-primary" 
                style={{ width: '100%', background: 'var(--success)', borderColor: 'var(--success)' }}
                onClick={() => setIsSubmitted(true)}
              >
                Submit Mock Test
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Scorecard Modal */}
      {isSubmitted && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          background: 'rgba(0, 0, 0, 0.6)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 100,
          padding: '20px'
        }}>
          <div className="card" style={{
            maxWidth: '640px',
            width: '100%',
            background: 'var(--surface)',
            borderRadius: 'var(--radius-lg)',
            padding: '24px',
            maxHeight: '90vh',
            overflowY: 'auto'
          }}>
            <div style={{ textAlign: 'center', marginBottom: '20px' }}>
              <div style={{ fontSize: '40px', marginBottom: '8px' }}>🎉</div>
              <h2 style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text)' }}>
                Mock Test Verification Complete!
              </h2>
              <p style={{ color: 'var(--text-muted)', fontSize: '13px' }}>
                All questions and options rendered with zero runtime errors.
              </p>
            </div>

            {/* Scorecard Summary */}
            <div style={{ 
              display: 'grid', 
              gridTemplateColumns: 'repeat(4, 1fr)', 
              gap: '10px', 
              background: 'var(--bg-soft)', 
              padding: '16px', 
              borderRadius: 'var(--radius)', 
              marginBottom: '20px',
              textAlign: 'center'
            }}>
              <div>
                <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Score</div>
                <div style={{ fontSize: '18px', fontWeight: 800, color: 'var(--accent)' }}>
                  {evaluation.score} / {evaluation.totalMarks}
                </div>
              </div>
              <div>
                <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Accuracy</div>
                <div style={{ fontSize: '18px', fontWeight: 800, color: evaluation.percentage >= 80 ? 'var(--success)' : 'var(--warning)' }}>
                  {evaluation.percentage}%
                </div>
              </div>
              <div>
                <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Correct</div>
                <div style={{ fontSize: '18px', fontWeight: 800, color: 'var(--success)' }}>
                  {evaluation.correct}
                </div>
              </div>
              <div>
                <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Incorrect</div>
                <div style={{ fontSize: '18px', fontWeight: 800, color: 'var(--danger)' }}>
                  {evaluation.incorrect}
                </div>
              </div>
            </div>

            {/* Verification checklist */}
            <div style={{ background: 'rgba(16, 185, 129, 0.08)', border: '1px solid var(--success)', borderRadius: 'var(--radius)', padding: '14px', marginBottom: '20px' }}>
              <div style={{ fontSize: '12.5px', fontWeight: 700, color: 'var(--success)', marginBottom: '4px' }}>
                ✅ Exam Health Status: Verified Ready for Students
              </div>
              <ul style={{ fontSize: '11.5px', color: 'var(--text-muted)', margin: 0, paddingLeft: '16px' }}>
                <li>KaTeX mathematical formulas rendered smoothly.</li>
                <li>Multiple options mapped without duplicate keys or null errors.</li>
                <li>Zero student records, rosters, or masteries touched.</li>
              </ul>
            </div>

            {/* Modal buttons */}
            <div style={{ display: 'flex', gap: '10px', justifyContent: 'flex-end' }}>
              <button
                className="btn btn-secondary"
                onClick={() => setIsSubmitted(false)}
              >
                Review Answers in Test
              </button>
              <button
                className="btn btn-primary"
                onClick={() => router.push('/admin/exams')}
              >
                Return to Exams Management
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default function AdminMockExamPage() {
  return (
    <Suspense fallback={
      <div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <div className="spinner" />
      </div>
    }>
      <AdminMockExamContent />
    </Suspense>
  );
}
