'use client';

import React from 'react';
import {
  stripOptionLabel,
  isMultipleChoiceType,
  normalizeOptionAnswer,
  parseAnswerList,
  isOptionMatch
} from '@/lib/questionTypes';
import { RichMathText } from '@/components/QuestionDisplay';
import { ModalShell } from '@/components/common/ModalShell';

interface PracticeFeedbackModalProps {
  isOpen: boolean;
  isCorrect: boolean;
  question: any;
  explanationTimer: number;
  isSubmittingPractice: boolean;
  selectedErrorReason?: string;
  onSelectErrorReason?: (reason: string) => void;
  onNext: () => void;
}

export function PracticeFeedbackModal({
  isOpen,
  isCorrect,
  question,
  explanationTimer,
  isSubmittingPractice,
  selectedErrorReason,
  onSelectErrorReason,
  onNext
}: PracticeFeedbackModalProps) {
  if (!isOpen || !question) return null;

  const getCorrectOptionText = (qItem: any) => {
    const isMultiple = isMultipleChoiceType(qItem.type);
    const rawAnswers = isMultiple
      ? (Array.isArray(qItem.correctAnswers) && qItem.correctAnswers.length > 0 ? qItem.correctAnswers : parseAnswerList(qItem.correctAnswer))
      : [qItem.correctAnswer || (Array.isArray(qItem.correctAnswers) ? qItem.correctAnswers[0] : '')];

    if (!qItem.options || qItem.options.length === 0) {
      return rawAnswers.filter(Boolean).join(', ') || 'Correct option';
    }

    const matchedTexts: string[] = [];
    rawAnswers.forEach((ans: any) => {
      if (!ans) return;
      const normLetter = normalizeOptionAnswer(ans, qItem.options);
      if (normLetter && /^[A-Z]$/.test(normLetter)) {
        const idx = normLetter.charCodeAt(0) - 65;
        if (idx >= 0 && idx < qItem.options.length) {
          const opt = qItem.options[idx];
          const text = typeof opt === 'object' && opt ? (opt.text || opt.value || '') : String(opt);
          matchedTexts.push(`(${normLetter}) ${stripOptionLabel(text)}`);
          return;
        }
      }
      const match = qItem.options.find((o: any) => isOptionMatch(o, ans));
      if (match) {
        const idx = qItem.options.indexOf(match);
        const code = String.fromCharCode(65 + idx);
        const text = typeof match === 'object' ? (match.text || match.value) : String(match);
        matchedTexts.push(`(${code}) ${stripOptionLabel(text)}`);
      } else {
        matchedTexts.push(String(ans));
      }
    });

    if (matchedTexts.length > 0) {
      return Array.from(new Set(matchedTexts)).join(', ');
    }

    const correctOpts = qItem.options.filter((o: any) => o && typeof o === 'object' && (o.isCorrect || o.correct));
    if (correctOpts.length > 0) {
      return correctOpts.map((o: any) => {
        const idx = qItem.options.indexOf(o);
        const code = String.fromCharCode(65 + idx);
        return `(${code}) ${stripOptionLabel(o.text || o.value)}`;
      }).join(', ');
    }

    return 'Correct option';
  };

  return (
    <ModalShell
      isOpen={isOpen && !!question}
      maxWidth="640px"
      zIndex={20000}
      cardStyle={{
        background: 'var(--surface-popover)',
        border: '1px solid var(--border-popover)',
        borderRadius: 'var(--radius-lg)',
        padding: '32px 28px',
        borderTop: `6px solid ${isCorrect ? 'var(--success)' : 'var(--danger)'}`,
        boxShadow: 'var(--shadow-lg)'
      }}
    >
      <h2 style={{ color: isCorrect ? 'var(--success)' : 'var(--danger)', fontSize: '2rem', fontWeight: 800, margin: '0 0 16px 0' }}>
        {isCorrect ? '🎉 Correct!' : '❌ Incorrect'}
      </h2>
      <div style={{ margin: '16px 0 24px 0', fontSize: '15px', color: 'var(--text)', display: 'flex', flexDirection: 'column', gap: '14px' }}>
        {!isCorrect && (
          <div style={{ background: 'rgba(239, 68, 68, 0.08)', padding: '14px 18px', borderRadius: 'var(--radius-sm)', border: '1px solid rgba(239, 68, 68, 0.2)' }}>
            <strong style={{ color: 'var(--danger)', fontSize: '16px' }}>Correct Answer: </strong>
            <RichMathText content={getCorrectOptionText(question)} inline style={{ fontWeight: 700, fontSize: '16px' }} />
          </div>
        )}
        {!isCorrect && (
          <div style={{ background: 'var(--bg-soft)', padding: '16px 18px', borderRadius: 'var(--radius-sm)', overflowY: 'auto', maxHeight: '240px', border: '1px solid var(--border-light)', textAlign: 'left' }}>
            <strong style={{ color: 'var(--accent)', display: 'block', marginBottom: '8px', fontSize: '15px' }}>💡 Detailed Explanation &amp; Solution:</strong>
            {question.solution || question.explanation ? (
              <RichMathText 
                content={question.solution || question.explanation}
                style={{ lineHeight: '1.6', fontSize: '14.5px', color: 'var(--text)' }}
              />
            ) : (
              <div style={{ lineHeight: '1.6', fontSize: '14.5px', color: 'var(--text)' }}>
                Analyze the key concepts: The correct choice is <strong>{getCorrectOptionText(question)}</strong>. Review topic definitions and core principles to reinforce this concept.
              </div>
            )}
          </div>
        )}
        {!isCorrect && (
          <div style={{ 
            background: 'var(--bg-soft)', 
            padding: '14px 18px', 
            borderRadius: 'var(--radius-sm)', 
            border: '1px solid var(--border-light)',
            textAlign: 'left' 
          }}>
            <strong style={{ fontSize: '13px', display: 'block', marginBottom: '8px', color: 'var(--text)' }}>
              Why did you miss this question? <span style={{ color: 'var(--danger)' }}>*</span>
            </strong>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
              {['Reading Errors', 'Silly Mistake', 'Calculation Error', 'Over-Thinking', 'Concept Gap', 'Guessed / Fluke'].map(reason => {
                const isSelected = selectedErrorReason === reason;
                return (
                  <button
                    key={reason}
                    type="button"
                    onClick={() => onSelectErrorReason && onSelectErrorReason(reason)}
                    className={`btn btn-sm ${isSelected ? 'btn-primary' : 'btn-secondary'}`}
                    style={{ 
                      fontSize: '11px', 
                      padding: '6px 12px',
                      borderRadius: 'var(--radius-sm)',
                      border: isSelected ? '1px solid var(--accent)' : '1px solid var(--border)',
                      background: isSelected ? 'var(--accent-grad)' : 'var(--surface)',
                      color: isSelected ? 'var(--text-white)' : 'var(--text)',
                      cursor: 'pointer'
                    }}
                  >
                    {reason}
                  </button>
                );
              })}
            </div>
          </div>
        )}
        {isCorrect && (
          <div style={{ background: 'rgba(16, 185, 129, 0.08)', padding: '18px 20px', borderRadius: 'var(--radius-sm)', border: '1px solid rgba(16, 185, 129, 0.2)' }}>
            <p style={{ margin: 0, fontWeight: 700, fontSize: '16px', color: 'var(--success)' }}>🎉 Well done! You evaluated this statement correctly.</p>
            {(question.solution || question.explanation) && (
              <div style={{ marginTop: '12px', fontSize: '14.5px', lineHeight: '1.6', color: 'var(--text)', textAlign: 'left' }}>
                <strong style={{ color: 'var(--text-muted)' }}>Solution Note: </strong>
                <RichMathText content={question.solution || question.explanation} inline />
              </div>
            )}
          </div>
        )}
      </div>
      <button 
        className="btn btn-primary" 
        onClick={onNext} 
        disabled={isSubmittingPractice || (!isCorrect && (explanationTimer > 0 || !selectedErrorReason))}
        style={{ width: '100%', padding: '14px', fontSize: '16px', fontWeight: 800, borderRadius: 'var(--radius-sm)' }}
      >
        {isSubmittingPractice
          ? 'Submitting Practice...'
          : (isCorrect 
            ? 'Continue →' 
            : (explanationTimer > 0 
                ? `Read Explanation (${explanationTimer}s)` 
                : (!selectedErrorReason ? '⚠️ Select Error Reason Above to Proceed' : '✓ I Understand')))}
      </button>
    </ModalShell>
  );
}
