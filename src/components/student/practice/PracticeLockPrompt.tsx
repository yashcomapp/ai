'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import { RichMathText } from '@/components/QuestionDisplay';

interface PracticeLockPromptProps {
  type: 'autonomous' | 'textbook';
  topicCode: string;
  category: string;
  textbookStudyMessage?: string;
  lockType?: 'initial' | 'cooldown' | 'daily' | 'quota_reached' | 'reflection_required' | null;
  textbookConfirmedCheck?: boolean;
  setTextbookConfirmedCheck?: (checked: boolean) => void;
  confirmingTextbook?: boolean;
  onConfirmTextbook?: () => void;
  firebaseUser?: any;
  reflectionReviewId?: string;
  reflectionQuestions?: any[];
  onReflectionComplete?: () => void;
}

const REFLECTION_CATEGORIES = [
  { key: 'conceptual_misunderstanding', label: '🧠 Concept Gap' },
  { key: 'calculation_error', label: '🔢 Calculation Error' },
  { key: 'misread_question', label: '📖 Misread Question' },
  { key: 'silly_mistake', label: '⚡ Silly Mistake' },
  { key: 'over_thinking', label: '🤔 Over-Thinking' },
  { key: 'guessed', label: '🎲 Guessed / Fluke' }
];

export function PracticeLockPrompt({
  type,
  topicCode,
  textbookStudyMessage,
  lockType,
  textbookConfirmedCheck = false,
  setTextbookConfirmedCheck,
  confirmingTextbook = false,
  onConfirmTextbook,
  firebaseUser,
  reflectionReviewId,
  reflectionQuestions = [],
  onReflectionComplete
}: PracticeLockPromptProps) {
  const router = useRouter();

  // Lever 1: Reflection Gate State
  const [reflections, setReflections] = useState<Record<string, { category: string; explanation: string }>>({});
  const [submittingReflection, setSubmittingReflection] = useState(false);
  const [reflectionError, setReflectionError] = useState<string | null>(null);

  if (type === 'autonomous') {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', padding: '20px' }}>
        <div style={{ maxWidth: '480px', width: '100%', textAlign: 'center', padding: '32px 24px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--warning)', boxShadow: 'var(--shadow-glass)' }}>
          <div style={{ fontSize: '3rem', marginBottom: '12px' }}>🔒</div>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--text)', marginBottom: '8px' }}>Practice Restricted / अभ्यास प्रतिबंधित</h3>
          <p style={{ fontSize: '13.5px', color: 'var(--text-muted)', lineHeight: '1.5', marginBottom: '20px' }}>
            Autonomous mode is active on your account. Self-directed topic practice is disabled.
          </p>
          <button className="btn btn-primary" onClick={() => router.push('/student')}>
            🏠 Back to Dashboard
          </button>
        </div>
      </div>
    );
  }

  // Lever 1: Generative Reflection Gate Interface
  if (lockType === 'reflection_required') {
    const questionsToReflect = reflectionQuestions.length > 0
      ? reflectionQuestions
      : [{ questionCode: topicCode, text: 'Review core concepts for this topic.' }];

    const allValid = questionsToReflect.every((q, idx) => {
      const key = q.questionCode || q.id || `q_${idx}`;
      const entry = reflections[key];
      return entry && entry.category && entry.explanation && entry.explanation.trim().length >= 25;
    });

    const handleReflectionSubmit = async () => {
      if (!reflectionReviewId || !firebaseUser || !allValid || submittingReflection) return;
      setSubmittingReflection(true);
      setReflectionError(null);

      try {
        const idToken = await firebaseUser.getIdToken();
        const payload = {
          reviewId: reflectionReviewId,
          reflections: questionsToReflect.map((q, idx) => {
            const key = q.questionCode || q.id || `q_${idx}`;
            const entry = reflections[key] || { category: 'conceptual_misunderstanding', explanation: '' };
            return {
              questionCode: q.questionCode || q.id || topicCode,
              category: entry.category,
              studentExplanation: entry.explanation.trim()
            };
          })
        };

        const res = await fetch('/api/student/practice/reflect', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
          },
          body: JSON.stringify(payload)
        });

        const data = await res.json();
        if (!res.ok) {
          throw new Error(data.message || 'Failed to submit reflection');
        }

        onReflectionComplete?.();
      } catch (err: any) {
        setReflectionError(err.message || 'Error submitting reflection');
      } finally {
        setSubmittingReflection(false);
      }
    };

    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', padding: '24px 16px' }}>
        <div style={{
          maxWidth: '680px',
          width: '100%',
          padding: '36px 28px',
          background: 'var(--surface)',
          borderRadius: 'var(--radius-lg)',
          border: '1px solid var(--accent)',
          boxShadow: 'var(--shadow-glass)',
          display: 'flex',
          flexDirection: 'column',
          gap: '20px'
        }}>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '3rem', marginBottom: '12px' }}>💡</div>
            <h3 style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--text)', marginBottom: '8px' }}>
              Mistake Reflection Required / चुकांचे विश्लेषण
            </h3>
            <p style={{ fontSize: '14px', color: 'var(--text-muted)', lineHeight: '1.6', margin: 0 }}>
              As an Autonomous Learner, reflecting on your mistakes builds true concept mastery.
              Before starting your next practice set, explain what went wrong in your own words.
            </p>
          </div>

          {reflectionError && (
            <div className="alert-box alert-box-danger" style={{ display: 'block', fontSize: '13.5px' }}>
              {reflectionError}
            </div>
          )}

          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px', maxHeight: '55vh', overflowY: 'auto', paddingRight: '4px' }}>
            {questionsToReflect.map((q, idx) => {
              const key = q.questionCode || q.id || `q_${idx}`;
              const entry = reflections[key] || { category: 'conceptual_misunderstanding', explanation: '' };
              const charCount = entry.explanation.length;
              const isLongEnough = charCount >= 25;

              return (
                <div key={key} style={{
                  background: 'var(--bg-soft)',
                  borderRadius: 'var(--radius-md)',
                  padding: '18px 20px',
                  border: '1px solid var(--border-light)',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '12px'
                }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <span style={{ fontSize: '12.5px', fontWeight: 700, color: 'var(--text-muted)' }}>
                      Question {idx + 1} {q.questionCode ? `• ${q.questionCode}` : ''}
                    </span>
                    <span style={{ fontSize: '11px', color: 'var(--danger)', fontWeight: 600 }}>Missed</span>
                  </div>

                  {q.text && (
                    <div style={{ fontSize: '14px', color: 'var(--text)', lineHeight: '1.5' }}>
                      <RichMathText content={q.text} />
                    </div>
                  )}

                  {q.correctAnswer && (
                    <div style={{ fontSize: '13px', color: 'var(--success)', background: 'rgba(16, 185, 129, 0.08)', padding: '8px 12px', borderRadius: 'var(--radius-sm)' }}>
                      <strong>Correct Answer:</strong> {String(q.correctAnswer)}
                    </div>
                  )}

                  {q.solution && (
                    <div style={{ fontSize: '12.5px', color: 'var(--text-muted)', lineHeight: '1.5', background: 'var(--bg)', padding: '10px 12px', borderRadius: 'var(--radius-sm)' }}>
                      <strong>Solution Note:</strong> <RichMathText content={q.solution} inline />
                    </div>
                  )}

                  <div>
                    <label style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)', display: 'block', marginBottom: '6px' }}>
                      Why did you miss this question?
                    </label>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                      {REFLECTION_CATEGORIES.map(cat => {
                        const isSelected = entry.category === cat.key;
                        return (
                          <button
                            key={cat.key}
                            type="button"
                            onClick={() => setReflections(prev => ({
                              ...prev,
                              [key]: { ...entry, category: cat.key }
                            }))}
                            className={`btn btn-sm ${isSelected ? 'btn-primary' : 'btn-secondary'}`}
                            style={{
                              fontSize: '11px',
                              padding: '5px 10px',
                              borderRadius: 'var(--radius-sm)',
                              border: isSelected ? '1px solid var(--accent)' : '1px solid var(--border)',
                              background: isSelected ? 'var(--accent-grad)' : 'var(--surface)',
                              color: isSelected ? 'var(--text-white)' : 'var(--text)',
                              cursor: 'pointer'
                            }}
                          >
                            {cat.label}
                          </button>
                        );
                      })}
                    </div>
                  </div>

                  <div>
                    <label style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)', display: 'block', marginBottom: '6px' }}>
                      Explain your error &amp; what the correct approach is:
                    </label>
                    <textarea
                      value={entry.explanation}
                      onChange={(e) => {
                        const val = e.target.value.slice(0, 350);
                        setReflections(prev => ({
                          ...prev,
                          [key]: { ...entry, explanation: val }
                        }));
                      }}
                      placeholder="Explain in your own words what concept was misunderstood or where the error occurred (min 25 characters)..."
                      rows={3}
                      style={{
                        width: '100%',
                        padding: '10px 12px',
                        fontSize: '13px',
                        borderRadius: 'var(--radius-sm)',
                        border: isLongEnough ? '1px solid var(--border)' : '1px solid var(--danger)',
                        background: 'var(--surface)',
                        color: 'var(--text)',
                        resize: 'vertical',
                        boxSizing: 'border-box'
                      }}
                    />
                    <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '4px', fontSize: '11.5px' }}>
                      <span style={{ color: isLongEnough ? 'var(--success)' : 'var(--danger)' }}>
                        {isLongEnough ? '✓ Minimum length satisfied' : `Needs at least ${25 - charCount} more characters`}
                      </span>
                      <span style={{ color: 'var(--text-muted)' }}>{charCount}/350</span>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          <div style={{ display: 'flex', gap: '12px', width: '100%' }}>
            <button
              className="btn btn-secondary"
              onClick={() => router.push('/student')}
              style={{ flex: 1 }}
            >
              🏠 Dashboard
            </button>
            <button
              className="btn btn-primary"
              disabled={!allValid || submittingReflection}
              onClick={handleReflectionSubmit}
              style={{ flex: 2, fontWeight: 700 }}
            >
              {submittingReflection ? 'Saving Reflection...' : '✓ Submit Reflection & Unlock Next Set'}
            </button>
          </div>
        </div>
      </div>
    );
  }

  if (type === 'textbook') {
    const isQuota = lockType === 'quota_reached';
    const isLockedState = lockType === 'cooldown' || lockType === 'daily';
    const icon = lockType === 'cooldown' ? '⏳' : lockType === 'daily' ? '🔒' : isQuota ? '🎓' : '📖';
    const heading = lockType === 'cooldown' 
      ? 'Deliberation Cooldown Active / विश्राम अवधि ⏳' 
      : lockType === 'daily' 
        ? 'Daily Limit Reached / दैनिक अभ्यास सीमा 🔒' 
        : isQuota 
          ? 'Practice Quota Completed / अभ्यास कोटा पूर्ण 🎓'
          : 'Time to hit the textbook! / पाठ्यपुस्तक पढ़ें 📚';

    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', padding: '20px' }}>
        <div style={{ 
          maxWidth: '520px', 
          width: '100%', 
          textAlign: 'center', 
          padding: '40px 30px', 
          background: 'var(--surface)', 
          borderRadius: 'var(--radius-lg)', 
          border: isQuota ? '1px solid var(--accent)' : '1px solid var(--warning)', 
          boxShadow: 'var(--shadow-glass)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center'
        }}>
          <div style={{ fontSize: '3.5rem', marginBottom: '16px' }}>{icon}</div>
          <h3 style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--text)', marginBottom: '12px' }}>
            {heading}
          </h3>
          <p style={{ fontSize: '14px', color: 'var(--text-muted)', lineHeight: '1.6', marginBottom: '24px' }}>
            {textbookStudyMessage || "Let's take a break from tests. Please read your textbook and review your class notes for this chapter before trying again."}
          </p>
          
          {!isLockedState && (
            <label style={{ 
              display: 'flex', 
              alignItems: 'center', 
              gap: '10px', 
              fontSize: '13px', 
              color: 'var(--text)', 
              cursor: 'pointer',
              padding: '12px 16px',
              background: 'var(--bg)',
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--border-light)',
              width: '100%',
              marginBottom: '24px',
              boxSizing: 'border-box'
            }}>
              <input 
                type="checkbox" 
                checked={textbookConfirmedCheck} 
                onChange={(e) => setTextbookConfirmedCheck?.(e.target.checked)}
                style={{ width: '18px', height: '18px', cursor: 'pointer' }}
              />
              <span style={{ textAlign: 'left' }}>I confirm that I have reviewed this concept in my textbook/notes.</span>
            </label>
          )}

          <div style={{ display: 'flex', gap: '12px', width: '100%' }}>
            <button 
              className="btn btn-secondary" 
              onClick={() => router.push('/student')}
              style={{ flex: 1 }}
            >
              🏠 Back to Dashboard
            </button>
            {!isLockedState && (
              <button 
                className="btn btn-primary" 
                disabled={!textbookConfirmedCheck || confirmingTextbook}
                onClick={onConfirmTextbook}
                style={{ flex: 1 }}
              >
                {confirmingTextbook ? 'Updating...' : '⚡ Unlock & Resume'}
              </button>
            )}
          </div>
        </div>
      </div>
    );
  }

  return null;
}
