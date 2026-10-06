'use client';

import React, { useEffect, useRef } from 'react';
import Image from 'next/image';
import {
  formatRichText,
  preprocessMathText,
  stripOptionLabel,
  isAssertionReasonType,
  extractAssertionAndReason,
  isMultipleChoiceType,
  isTrueFalseType,
  isNumericalType,
  isFillBlanksType,
  isSubjectiveType,
  normalizeOptionAnswer,
  getRawOptionKey,
  getRawOptionText,
  isOptionCorrect,
  isOptionSelectedByUser,
  KATEX_AUTO_RENDER_OPTIONS,
  DEFAULT_ASSERTION_REASON_OPTIONS
} from '@/lib/questionTypes';

/* =========================================================================
   1. Universal Rich Math & SVG Diagram Renderer
   ========================================================================= */

interface RichMathTextProps {
  content: any;
  className?: string;
  style?: React.CSSProperties;
  inline?: boolean;
  as?: 'div' | 'span' | 'p' | 'h2' | 'h3' | 'h4' | 'label';
  onClick?: (e: React.MouseEvent<HTMLElement>) => void;
  title?: string;
}

export const RichMathText: React.FC<RichMathTextProps> = ({
  content,
  className = '',
  style,
  inline = false,
  as,
  onClick,
  title
}) => {
  const containerRef = useRef<HTMLElement | null>(null);
  const formattedHtml = formatRichText(content || '');

  useEffect(() => {
    if (!containerRef.current) return;
    const win = typeof window !== 'undefined' ? (window as any) : null;
    if (win && win.renderMathInElement) {
      try {
        win.renderMathInElement(containerRef.current, KATEX_AUTO_RENDER_OPTIONS);
      } catch (err) {
        console.warn('RichMathText renderMathInElement failed:', err);
      }
    }
  }, [formattedHtml]);

  const Component = (as || (inline ? 'span' : 'div')) as any;
  const combinedClass = `math-container ${className}`.trim();

  return (
    <Component
      ref={containerRef}
      className={combinedClass}
      style={style}
      onClick={onClick}
      title={title}
      dangerouslySetInnerHTML={{ __html: formattedHtml }}
    />
  );
};

/* =========================================================================
   2. SSOT QuestionDisplay Props
   ========================================================================= */

export type QuestionDisplayMode =
  | 'stem-only'  // Only render the question stem (assertion/reason, formulas, SVG)
  | 'exam'       // Interactive student exam (radio, checkbox, input)
  | 'practice'   // Interactive student practice (submit feedback, highlights)
  | 'review'     // Review / audit mode (Scorecard, Parent review, Teacher review)
  | 'report'     // Exam report card with option vote distributions
  | 'bank'       // Question bank item display with correct answer marked
  | 'preview';   // Real-time preview for Create Question Bank

export interface QuestionData {
  text?: string;
  questionText?: string;
  type?: string;
  questionCode?: string;
  code?: string;
  options?: any[];
  correctAnswer?: any;
  correctAnswers?: any[];
  userAnswer?: any;
  answer?: any;
  solution?: string;
  explanation?: string;
  steps?: any[];
  imageUrl?: string;
  difficulty?: string;
  bloomLevel?: string;
  marks?: number;
  assertion?: string;
  reason?: string;
  isCorrect?: boolean;
}

export interface QuestionDisplayProps {
  /** The question object or dictionary containing text, options, answers, etc. */
  question?: QuestionData | any;

  /** Individual property overrides */
  text?: string;
  type?: string;
  options?: any[];
  correctAnswer?: any;
  correctAnswers?: any[];
  userAnswer?: any;
  solution?: string;
  explanation?: string;
  questionCode?: string;
  imageUrl?: string;

  /** Display mode determining interactivity, answer badges, and options layout */
  mode?: QuestionDisplayMode;

  /** Prefix before question (e.g. "Q1. ") */
  prefix?: React.ReactNode;

  /** Right-aligned header action or badge (e.g. "✏️ Edit Answer") */
  headerRight?: React.ReactNode;

  /** Whether to show internal question code badge */
  showQuestionCode?: boolean;

  /** Currently selected answer in exam / practice mode */
  selectedAnswer?: any;

  /** Interactivity callbacks */
  onSelectOption?: (optionKeyOrText: string) => void;
  onTextInput?: (text: string) => void;

  /** Exam report mode: votes per option { [optKey]: { count: number, students: [] } } */
  optionVotes?: { [key: string]: { count: number; students?: any[] } };
  onVoteClick?: (optKey: string, students: any[]) => void;

  /** Submission & review flags */
  isSubmitted?: boolean;
  isCorrect?: boolean;
  hideExplanation?: boolean;
  explanationLabel?: string;

  /** Optional nested children rendered between stem and options (e.g. stats bar) */
  children?: React.ReactNode;

  /** Container styling */
  className?: string;
  style?: React.CSSProperties;
}

/* =========================================================================
   3. Canonical SSOT QuestionDisplay Component
   ========================================================================= */

export const QuestionDisplay: React.FC<QuestionDisplayProps> = ({
  question,
  text,
  type,
  options,
  correctAnswer,
  correctAnswers,
  userAnswer,
  solution,
  explanation,
  questionCode,
  imageUrl,
  mode = 'stem-only',
  prefix,
  headerRight,
  showQuestionCode = false,
  selectedAnswer,
  onSelectOption,
  onTextInput,
  optionVotes,
  onVoteClick,
  isSubmitted = false,
  isCorrect,
  hideExplanation = false,
  explanationLabel,
  children,
  className = '',
  style
}) => {
  // Resolve properties with fallback hierarchy
  const qText = text ?? question?.text ?? question?.questionText ?? '';
  const qType = type ?? question?.type ?? '';
  const rawOptions = options ?? question?.options ?? null;
  const qCorrectAnswer = correctAnswer ?? question?.correctAnswer ?? question?.answer ?? question?.correct_answer ?? '';
  const qCorrectAnswers = correctAnswers ?? question?.correctAnswers ?? (Array.isArray(qCorrectAnswer) ? qCorrectAnswer : []);
  const qUserAnswer = userAnswer ?? selectedAnswer ?? question?.userAnswer ?? '';
  const qExplanation = explanation ?? solution ?? question?.explanation ?? question?.solution ?? '';
  const qCode = questionCode ?? question?.questionCode ?? question?.code ?? '';
  const qImage = imageUrl ?? question?.imageUrl ?? '';

  // Determine question structure
  const isAR = isAssertionReasonType(qType) || (typeof qText === 'string' && /(?:Assertion\s*\(A\)|Reason\s*\(R\))/i.test(qText));

  // Resolved options list
  let resolvedOptions: any[] | null = null;
  if (Array.isArray(rawOptions) && rawOptions.length > 0) {
    resolvedOptions = rawOptions;
  } else if (isAR) {
    resolvedOptions = DEFAULT_ASSERTION_REASON_OPTIONS;
  } else if (isTrueFalseType(qType)) {
    resolvedOptions = ['True', 'False'];
  }

  // Evaluate evaluation correctness if not explicitly supplied
  const effectiveIsCorrect = typeof isCorrect === 'boolean'
    ? isCorrect
    : (question?.isCorrect ?? (qUserAnswer && qCorrectAnswer && normalizeOptionAnswer(qUserAnswer, resolvedOptions || []) === normalizeOptionAnswer(qCorrectAnswer, resolvedOptions || [])));

  const isUnanswered = !qUserAnswer || String(qUserAnswer).trim() === '' || String(qUserAnswer).toLowerCase() === 'blank';

  /* -----------------------------------------------------------------------
     A. Render Question Stem (Assertion & Reason or Standard Text)
     ----------------------------------------------------------------------- */
  const renderStem = () => {
    if (isAR) {
      const { assertion, reason } = extractAssertionAndReason({ text: qText, type: qType, ...(typeof question === 'object' ? question : {}) });
      return (
        <div style={{ marginBottom: mode === 'stem-only' ? 0 : '14px' }}>
          {(prefix || headerRight || (showQuestionCode && qCode)) && (
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px', gap: '8px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                {prefix && <span style={{ fontWeight: 700 }}>{prefix}</span>}
                {showQuestionCode && qCode && (
                  <span className="badge badge-secondary" style={{ fontSize: '10px', opacity: 0.85 }}>
                    {qCode}
                  </span>
                )}
              </div>
              {headerRight}
            </div>
          )}
          <div style={{ background: 'var(--bg-soft, #f8fafc)', border: '1px solid var(--border-light, #e2e8f0)', borderRadius: '6px', padding: '10px 12px', display: 'flex', flexDirection: 'column', gap: '6px' }}>
            <div>
              <strong>Assertion (A):</strong> <RichMathText content={assertion} inline />
            </div>
            <div>
              <strong>Reason (R):</strong> <RichMathText content={reason} inline />
            </div>
          </div>
        </div>
      );
    }

    const rawPrefix = typeof prefix === 'string' ? prefix : '';
    const reactNodePrefix = typeof prefix !== 'string' ? prefix : null;
    const combinedText = rawPrefix ? `${rawPrefix}${qText || ''}` : (qText || '');

    return (
      <div style={{ marginBottom: mode === 'stem-only' ? 0 : '14px' }}>
        {(headerRight || (showQuestionCode && qCode) || reactNodePrefix) ? (
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '10px' }}>
            <div style={{ flex: 1, minWidth: 0 }}>
              {reactNodePrefix && <span style={{ fontWeight: 700, marginRight: '4px' }}>{reactNodePrefix}</span>}
              <RichMathText content={combinedText} inline={!reactNodePrefix} />
              {showQuestionCode && qCode && (
                <span className="badge badge-secondary" style={{ fontSize: '10px', marginLeft: '6px', opacity: 0.85 }}>
                  {qCode}
                </span>
              )}
            </div>
            {headerRight && <div style={{ flexShrink: 0 }}>{headerRight}</div>}
          </div>
        ) : (
          <RichMathText content={combinedText} />
        )}
      </div>
    );
  };

  /* -----------------------------------------------------------------------
     B. Render Interactive Options (mode='exam')
     ----------------------------------------------------------------------- */
  const renderExamOptions = () => {
    if (!resolvedOptions || resolvedOptions.length === 0) {
      if (isNumericalType(qType) || isFillBlanksType(qType)) {
        return (
          <div style={{ marginTop: '10px' }}>
            <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '6px' }}>
              {isNumericalType(qType) ? 'Enter Numerical Answer:' : 'Type Answer:'}
            </label>
            <input
              type={isNumericalType(qType) ? 'number' : 'text'}
              value={qUserAnswer}
              onChange={(e) => onTextInput?.(e.target.value)}
              placeholder="Type your answer here..."
              style={{ width: '100%', padding: '10px 12px', border: '1.5px solid var(--border-light, #e2e8f0)', borderRadius: '6px', fontSize: '14px', background: 'var(--surface, #fff)', color: 'var(--text)' }}
            />
          </div>
        );
      }
      if (isSubjectiveType(qType) || String(qType).startsWith('sub') || String(qType).includes('reasoning') || String(qType).includes('different')) {
        return (
          <div style={{ marginTop: '10px' }}>
            <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '6px' }}>
              Write Explanation:
            </label>
            <textarea
              value={qUserAnswer}
              onChange={(e) => onTextInput?.(e.target.value)}
              placeholder="Write your explanation or step-by-step answer here..."
              rows={4}
              style={{ width: '100%', padding: '10px 12px', border: '1.5px solid var(--border-light, #e2e8f0)', borderRadius: '6px', fontSize: '14px', background: 'var(--surface, #fff)', color: 'var(--text)', resize: 'vertical' }}
            />
          </div>
        );
      }
      return null;
    }

    const isMulti = isMultipleChoiceType(qType);

    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
        {resolvedOptions.map((opt: any, oi: number) => {
          const letter = String.fromCharCode(65 + oi);
          const optKey = getRawOptionKey(opt);
          const optText = getRawOptionText(opt);
          const isSelected = isMulti
            ? (Array.isArray(qUserAnswer) ? qUserAnswer.includes(letter) : String(qUserAnswer).includes(letter))
            : String(qUserAnswer).trim().toLowerCase() === String(letter).trim().toLowerCase() ||
              String(qUserAnswer).trim().toLowerCase() === String(optKey).trim().toLowerCase();

          return (
            <div
              key={oi}
              onClick={() => onSelectOption?.(letter)}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '12px',
                padding: '10px 14px',
                borderRadius: '8px',
                border: isSelected ? '1.5px solid var(--accent, #2563eb)' : '1px solid var(--border-light, #e2e8f0)',
                background: isSelected ? 'var(--accent-soft, rgba(37,99,235,0.08))' : 'var(--surface, #fff)',
                cursor: 'pointer',
                transition: 'border 0.15s, background 0.15s'
              }}
            >
              <input
                type={isMulti ? 'checkbox' : 'radio'}
                checked={isSelected}
                readOnly
                style={{ width: '17px', height: '17px', cursor: 'pointer' }}
              />
              <span style={{ fontWeight: 700, color: isSelected ? 'var(--accent, #2563eb)' : 'inherit' }}>
                ({letter})
              </span>
              <RichMathText content={stripOptionLabel(optText)} inline style={{ flex: 1 }} />
            </div>
          );
        })}
      </div>
    );
  };

  /* -----------------------------------------------------------------------
     C. Render Practice Mode Options (mode='practice')
     ----------------------------------------------------------------------- */
  const renderPracticeOptions = () => {
    if (!resolvedOptions || resolvedOptions.length === 0) return null;
    const isMulti = isMultipleChoiceType(qType);

    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
        {resolvedOptions.map((opt: any, oi: number) => {
          const letter = String.fromCharCode(65 + oi);
          const optText = getRawOptionText(opt);
          const isSelected = isMulti
            ? (Array.isArray(qUserAnswer) ? qUserAnswer.includes(letter) : String(qUserAnswer).includes(letter))
            : normalizeOptionAnswer(qUserAnswer, resolvedOptions!) === normalizeOptionAnswer(letter, resolvedOptions!);

          const isThisCorrect = normalizeOptionAnswer(letter, resolvedOptions!) === normalizeOptionAnswer(qCorrectAnswer, resolvedOptions!);

          let border = '1px solid var(--border-light, #e2e8f0)';
          let bg = 'var(--surface, #fff)';
          let badge = null;

          if (isSubmitted) {
            if (isSelected) {
              if (isThisCorrect) {
                border = '1.5px solid var(--success, #16a34a)';
                bg = 'rgba(22, 163, 74, 0.08)';
                badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success, #16a34a)', fontWeight: 700 }}>✓ Selected (Correct)</span>;
              } else {
                border = '1.5px solid var(--danger, #dc2626)';
                bg = 'rgba(220, 38, 38, 0.08)';
                badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--danger, #dc2626)', fontWeight: 700 }}>✗ Selected (Incorrect)</span>;
              }
            } else if (isThisCorrect) {
              border = '1.5px dashed var(--success, #16a34a)';
              bg = 'rgba(22, 163, 74, 0.05)';
              badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success, #16a34a)', fontWeight: 700 }}>✓ Correct Choice</span>;
            }
          } else if (isSelected) {
            border = '1.5px solid var(--accent, #2563eb)';
            bg = 'var(--accent-soft, rgba(37,99,235,0.08))';
          }

          return (
            <div
              key={oi}
              onClick={() => !isSubmitted && onSelectOption?.(letter)}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '12px',
                padding: '10px 14px',
                borderRadius: '8px',
                border,
                background: bg,
                cursor: isSubmitted ? 'default' : 'pointer'
              }}
            >
              <input
                type={isMulti ? 'checkbox' : 'radio'}
                checked={isSelected}
                disabled={isSubmitted}
                readOnly
                style={{ width: '17px', height: '17px' }}
              />
              <span style={{ fontWeight: 700 }}>({letter})</span>
              <RichMathText content={stripOptionLabel(optText)} inline style={{ flex: 1 }} />
              {badge}
            </div>
          );
        })}
      </div>
    );
  };

  /* -----------------------------------------------------------------------
     D. Render Review Mode Options & Comparison (mode='review')
     ----------------------------------------------------------------------- */
  const renderReviewOptions = () => {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', marginBottom: '10px' }}>
        {resolvedOptions && resolvedOptions.length > 0 && resolvedOptions.map((opt: any, oi: number) => {
          const letter = String.fromCharCode(65 + oi);
          const optKey = getRawOptionKey(opt);
          const optText = getRawOptionText(opt);

          const correctAns = (Array.isArray(qCorrectAnswers) && qCorrectAnswers.length > 0) ? qCorrectAnswers : qCorrectAnswer;
          let isCorrectOpt = isOptionCorrect(correctAns, optKey, oi, optText, resolvedOptions!);
          const isUserOpt = isOptionSelectedByUser(qUserAnswer, optKey, oi, optText, resolvedOptions!);

          // Failsafe
          if (effectiveIsCorrect && isUserOpt) {
            isCorrectOpt = true;
          }

          let border = '1px solid var(--border-light, #e2e8f0)';
          let background = 'var(--surface, #fff)';
          let color = 'var(--text)';
          let prefixIcon = '';

          if (isCorrectOpt) {
            border = '1.5px solid var(--success, #16a34a)';
            background = 'rgba(22, 163, 74, 0.08)';
            color = 'var(--success, #16a34a)';
            prefixIcon = isUserOpt ? '🎯 ' : '✅ ';
          } else if (isUserOpt) {
            border = '1.5px solid var(--danger, #dc2626)';
            background = 'rgba(220, 38, 38, 0.08)';
            color = 'var(--danger, #dc2626)';
            prefixIcon = '❌ ';
          }

          return (
            <div
              key={oi}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                padding: '7px 12px',
                borderRadius: '8px',
                border,
                background,
                color,
                fontSize: '12px',
                fontWeight: (isCorrectOpt || isUserOpt) ? 600 : 400
              }}
            >
              {prefixIcon && <span>{prefixIcon}</span>}
              <span style={{ fontWeight: 700 }}>({letter})</span>
              <RichMathText content={stripOptionLabel(optText)} inline style={{ flex: 1 }} />
            </div>
          );
        })}

        {/* User Answer vs Correct Answer Summary Bar */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '3px', fontSize: '11.5px', background: 'var(--surface-3, #f1f5f9)', padding: '6px 10px', borderRadius: '6px', border: '1px solid var(--border-light, #e2e8f0)', marginTop: '4px' }}>
          <div>
            <strong style={{ color: 'var(--text-muted, #64748b)', marginRight: '6px' }}>Student Answer:</strong>
            <span style={{ color: effectiveIsCorrect ? 'var(--success, #16a34a)' : 'var(--danger, #dc2626)', fontWeight: 700 }}>
              {isUnanswered ? '(blank / unattempted)' : <RichMathText content={stripOptionLabel(String(qUserAnswer))} inline />}
            </span>
          </div>
          <div>
            <strong style={{ color: 'var(--text-muted, #64748b)', marginRight: '6px' }}>Correct Answer:</strong>
            <span style={{ color: 'var(--success, #16a34a)', fontWeight: 'bold' }}>
              <RichMathText content={stripOptionLabel(Array.isArray(qCorrectAnswer) ? qCorrectAnswer.join(', ') : String(qCorrectAnswer))} inline />
            </span>
          </div>
        </div>
      </div>
    );
  };

  /* -----------------------------------------------------------------------
     E. Render Exam Report Card Mode (mode='report')
     ----------------------------------------------------------------------- */
  const renderReportOptions = () => {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', marginBottom: '10px' }}>
        {resolvedOptions && resolvedOptions.length > 0 ? (
          resolvedOptions.map((opt: any, oi: number) => {
            const letter = String.fromCharCode(65 + oi);
            const optKey = getRawOptionKey(opt);
            const optText = getRawOptionText(opt);
            const vote = (optionVotes && (optionVotes[optKey] || optionVotes[optText] || optionVotes[String(oi)] || optionVotes[letter])) || { count: 0, students: [] };
            const isCorrectOpt = Array.isArray(qCorrectAnswer)
              ? qCorrectAnswer.includes(optKey) || qCorrectAnswer.includes(letter)
              : qCorrectAnswer === optKey || qCorrectAnswer === letter;

            return (
              <div
                key={oi}
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  padding: '7px 12px',
                  borderRadius: '8px',
                  border: isCorrectOpt ? '1.5px solid var(--success, #16a34a)' : '1px solid var(--border-light, #e2e8f0)',
                  background: isCorrectOpt ? 'rgba(22, 163, 74, 0.08)' : 'var(--surface, #fff)',
                  fontSize: '12px'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flex: 1, minWidth: 0 }}>
                  <span style={{ fontWeight: 700, color: isCorrectOpt ? 'var(--success, #16a34a)' : 'inherit' }}>
                    {isCorrectOpt ? '✅ ' : ''}({letter})
                  </span>
                  <RichMathText content={stripOptionLabel(optText)} inline style={{ flex: 1 }} />
                </div>
                {typeof vote.count === 'number' && (
                  <span
                    className="pq-option-count"
                    onClick={() => onVoteClick?.(optKey, vote.students || [])}
                    style={{
                      background: 'var(--bg-soft, #f1f5f9)',
                      borderRadius: '12px',
                      padding: '2px 10px',
                      fontWeight: 700,
                      fontSize: '11px',
                      marginLeft: '8px',
                      cursor: onVoteClick ? 'pointer' : 'default'
                    }}
                  >
                    {vote.count}
                  </span>
                )}
              </div>
            );
          })
        ) : (
          qCorrectAnswer && (
            <div style={{ padding: '8px 12px', border: '1.5px solid var(--success, #16a34a)', borderRadius: '8px', background: 'rgba(22, 163, 74, 0.08)', fontSize: '12px', fontWeight: 600 }}>
              ✅ Correct Answer: <RichMathText content={Array.isArray(qCorrectAnswer) ? qCorrectAnswer.join(', ') : String(qCorrectAnswer)} inline />
            </div>
          )
        )}

        {/* Correct answer subtitle when options list is rendered */}
        {resolvedOptions && resolvedOptions.length > 0 && qCorrectAnswer && (
          <div style={{ fontSize: '12px', color: 'var(--success, #16a34a)', fontWeight: 700, marginTop: '4px' }}>
            ℹ️ Correct Answer: Option {Array.isArray(qCorrectAnswer) ? qCorrectAnswer.join(', ') : String(qCorrectAnswer)}
          </div>
        )}
      </div>
    );
  };

  /* -----------------------------------------------------------------------
     F. Render Bank / Preview Mode Options (mode='bank' | mode='preview')
     ----------------------------------------------------------------------- */
  const renderBankOptions = () => {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', marginBottom: '8px' }}>
        {resolvedOptions && resolvedOptions.length > 0 && resolvedOptions.map((opt: any, oi: number) => {
          const letter = String.fromCharCode(65 + oi);
          const optKey = getRawOptionKey(opt);
          const optText = getRawOptionText(opt);
          const isCorrectOpt = isOptionCorrect(qCorrectAnswer, optKey, oi, optText, resolvedOptions);

          return (
            <div
              key={oi}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                padding: '6px 12px',
                borderRadius: '6px',
                border: isCorrectOpt ? '1.5px solid var(--success, #16a34a)' : '1px solid var(--border-light, #e2e8f0)',
                background: isCorrectOpt ? 'rgba(22, 163, 74, 0.08)' : 'var(--surface, #fff)',
                fontSize: '12px'
              }}
            >
              <span style={{ fontWeight: 700, color: isCorrectOpt ? 'var(--success, #16a34a)' : 'inherit' }}>
                {isCorrectOpt ? '✅ ' : ''}({letter})
              </span>
              <RichMathText content={stripOptionLabel(optText)} inline style={{ flex: 1 }} />
            </div>
          );
        })}

        {!resolvedOptions && qCorrectAnswer && (
          <div style={{ fontSize: '11.5px', marginTop: '4px', color: 'var(--success, #16a34a)', fontWeight: 600 }}>
            <strong>Correct Answer:</strong> <RichMathText content={Array.isArray(qCorrectAnswer) ? qCorrectAnswer.join(', ') : String(qCorrectAnswer)} inline />
          </div>
        )}
      </div>
    );
  };

  /* -----------------------------------------------------------------------
     G. Render Solution / Step-by-Step Explanation
     ----------------------------------------------------------------------- */
  const renderExplanation = () => {
    if (hideExplanation || !qExplanation) return null;
    const label = explanationLabel || (mode === 'review' ? '💡 Step-by-Step Solution & Concept:' : '💡 Explanation:');

    return (
      <div
        className="pq-explanation"
        style={{
          marginTop: '8px',
          padding: '8px 12px',
          background: 'var(--bg-soft, #f8fafc)',
          borderRadius: '6px',
          borderTop: '1px dashed var(--border-light, #e2e8f0)',
          fontSize: '11.5px',
          lineHeight: '1.45',
          color: 'var(--text-muted, #64748b)'
        }}
      >
        <div style={{ fontWeight: 700, color: 'var(--text, #0f172a)', marginBottom: '4px' }}>
          {label}
        </div>
        <RichMathText content={qExplanation} />
      </div>
    );
  };

  /* -----------------------------------------------------------------------
     Master Layout Assembler
     ----------------------------------------------------------------------- */
  return (
    <div className={`question-display-root ${className}`.trim()} style={{ width: '100%', ...style }}>
      {/* 1. Stem */}
      {renderStem()}

      {/* 2. Optional Image */}
      {qImage && (
        <div style={{ margin: '8px 0 12px' }}>
          <Image
            src={qImage}
            alt="Question illustration"
            width={320}
            height={200}
            style={{ objectFit: 'contain', borderRadius: '6px', border: '1px solid var(--border-light, #e2e8f0)' }}
          />
        </div>
      )}

      {/* 3. Middle / Custom Content (e.g. progress bar, stats) */}
      {children}

      {/* 4. Options by Mode */}
      {mode === 'exam' && renderExamOptions()}
      {mode === 'practice' && renderPracticeOptions()}
      {mode === 'review' && renderReviewOptions()}
      {mode === 'report' && renderReportOptions()}
      {(mode === 'bank' || mode === 'preview') && renderBankOptions()}

      {/* 4. Explanation / Solution */}
      {(mode === 'review' || mode === 'report' || mode === 'bank' || mode === 'preview' || (mode === 'practice' && isSubmitted)) && renderExplanation()}
    </div>
  );
};

/* =========================================================================
   Compatibility Sub-Component Exports (Aliases to Single Method)
   ========================================================================= */

export const QuestionStemDisplay: React.FC<QuestionDisplayProps> = (props) => (
  <QuestionDisplay {...props} mode="stem-only" />
);

export const QuestionExplanationDisplay: React.FC<{ explanation: any; label?: string; style?: React.CSSProperties; className?: string }> = ({
  explanation,
  label = '💡 Explanation:',
  style,
  className
}) => {
  if (!explanation) return null;
  return (
    <div
      className={`pq-explanation ${className || ''}`.trim()}
      style={{
        marginTop: '8px',
        padding: '8px 12px',
        background: 'var(--bg-soft, #f8fafc)',
        borderRadius: '6px',
        borderTop: '1px dashed var(--border-light, #e2e8f0)',
        fontSize: '11.5px',
        lineHeight: '1.45',
        color: 'var(--text-muted, #64748b)',
        ...style
      }}
    >
      <div style={{ fontWeight: 700, color: 'var(--text, #0f172a)', marginBottom: '4px' }}>
        {label}
      </div>
      <RichMathText content={explanation} />
    </div>
  );
};

export const QuestionOptionRow: React.FC<{
  index: number;
  label?: string;
  text: any;
  isCorrect?: boolean;
  isSelected?: boolean;
  voteCount?: number;
  onVoteClick?: () => void;
  onClick?: () => void;
  style?: React.CSSProperties;
}> = ({
  index,
  label,
  text,
  isCorrect,
  isSelected,
  voteCount,
  onVoteClick,
  onClick,
  style
}) => {
  const optLetter = label || String.fromCharCode(65 + index);
  const cleanText = stripOptionLabel(text);

  let border = '1px solid var(--border-light, #e2e8f0)';
  let bg = 'var(--surface, #ffffff)';
  if (isCorrect) {
    border = '1.5px solid var(--success, #16a34a)';
    bg = 'rgba(22, 163, 74, 0.08)';
  } else if (isSelected) {
    border = '1.5px solid var(--accent, #2563eb)';
    bg = 'rgba(37, 99, 235, 0.08)';
  }

  return (
    <div
      onClick={onClick}
      style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '7px 12px',
        borderRadius: '8px',
        border,
        background: bg,
        fontSize: '12px',
        lineHeight: '1.4',
        cursor: onClick ? 'pointer' : 'default',
        ...style
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flex: 1, minWidth: 0 }}>
        <span style={{ fontWeight: 700, flexShrink: 0, color: isCorrect ? 'var(--success, #16a34a)' : 'inherit' }}>
          {isCorrect ? '✅ ' : ''}({optLetter})
        </span>
        <RichMathText content={cleanText} inline style={{ flex: 1 }} />
      </div>
      {typeof voteCount === 'number' && (
        <span
          className="pq-option-count"
          onClick={(e) => {
            if (onVoteClick) {
              e.stopPropagation();
              onVoteClick();
            }
          }}
          style={{
            background: 'var(--bg-soft, #f1f5f9)',
            borderRadius: '12px',
            padding: '2px 10px',
            fontWeight: 700,
            fontSize: '11px',
            marginLeft: '8px',
            cursor: onVoteClick ? 'pointer' : 'default'
          }}
        >
          {voteCount}
        </span>
      )}
    </div>
  );
};

export default QuestionDisplay;
