'use client';

import React from 'react';

export interface StepItem {
  stepNumber?: number;
  text?: string;
  marks: number;
  awarded?: number;
}

export interface StepAnswerInputProps {
  questionIndex: number;
  steps?: StepItem[];
  questionMarks: number;
  reviewAnswers: Record<string, any>;
  setReviewAnswers: React.Dispatch<React.SetStateAction<Record<string, any>>>;
  disabled?: boolean;
}

export default function StepAnswerInput({
  questionIndex,
  steps,
  questionMarks,
  reviewAnswers,
  setReviewAnswers,
  disabled = false
}: StepAnswerInputProps) {
  const hasSteps = Array.isArray(steps) && steps.length > 0;

  if (hasSteps) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginBottom: '10px' }}>
        {steps.map((step, si) => {
          const key = `ps_${questionIndex}_${si}`;
          return (
            <div 
              key={key} 
              style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                padding: '8px 12px',
                background: 'var(--surface-2)',
                border: '1.5px solid var(--border)',
                borderRadius: 'var(--radius-sm)',
                color: 'var(--text)'
              }}
            >
              <div style={{ display: 'flex', flexDirection: 'column', gap: '2px', maxWidth: '75%' }}>
                <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--accent)' }}>
                  Step {step.stepNumber || si + 1}
                </span>
                {step.text && (
                  <span style={{ fontSize: '11px', color: 'var(--text-muted)', lineHeight: '1.3' }}>
                    {step.text}
                  </span>
                )}
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Max: {step.marks}</span>
                <input 
                  type="number" 
                  min="0" 
                  max={step.marks} 
                  step="0.5" 
                  disabled={disabled}
                  value={reviewAnswers[key] ?? ''}
                  onChange={(e) => {
                    const raw = e.target.value;
                    if (raw === '') {
                      setReviewAnswers(prev => {
                        const copy = { ...prev };
                        delete copy[key];
                        return copy;
                      });
                    } else {
                      const val = Math.min(step.marks, Math.max(0, parseFloat(raw) || 0));
                      setReviewAnswers(prev => ({ ...prev, [key]: val }));
                    }
                  }}
                  style={{
                    width: '70px',
                    padding: '6px',
                    border: '2px solid var(--accent)',
                    borderRadius: '6px',
                    textAlign: 'center',
                    background: 'var(--surface-2)',
                    color: 'var(--text)',
                    fontWeight: 800,
                    fontSize: '14px',
                    outline: 'none'
                  }}
                />
              </div>
            </div>
          );
        })}
      </div>
    );
  }

  const key = `ps_${questionIndex}_0`;
  return (
    <div 
      style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '8px 12px',
        background: 'var(--surface-2)',
        border: '1.5px solid var(--border)',
        borderRadius: 'var(--radius-sm)',
        color: 'var(--text)',
        marginBottom: '10px'
      }}
    >
      <span style={{ fontSize: '12px', fontWeight: 600 }}>Overall Score</span>
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Max: {questionMarks}</span>
        <input 
          type="number" 
          min="0" 
          max={questionMarks} 
          step="0.5" 
          disabled={disabled}
          value={reviewAnswers[key] ?? ''}
          onChange={(e) => {
            const raw = e.target.value;
            if (raw === '') {
              setReviewAnswers(prev => {
                const copy = { ...prev };
                delete copy[key];
                return copy;
              });
            } else {
              const val = Math.min(questionMarks, Math.max(0, parseFloat(raw) || 0));
              setReviewAnswers(prev => ({ ...prev, [key]: val }));
            }
          }}
          style={{
            width: '70px',
            padding: '6px',
            border: '2px solid var(--accent)',
            borderRadius: '6px',
            textAlign: 'center',
            background: 'var(--surface-2)',
            color: 'var(--text)',
            fontWeight: 800,
            fontSize: '14px',
            outline: 'none'
          }}
        />
      </div>
    </div>
  );
}
