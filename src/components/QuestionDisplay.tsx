'use client';

import React, { useEffect, useRef } from 'react';
import {
  formatRichText,
  preprocessMathText,
  stripOptionLabel,
  isAssertionReasonType,
  extractAssertionAndReason,
  KATEX_AUTO_RENDER_OPTIONS
} from '@/lib/questionTypes';

interface RichMathTextProps {
  content: any;
  className?: string;
  style?: React.CSSProperties;
  inline?: boolean;
  as?: 'div' | 'span' | 'p' | 'h2' | 'h3' | 'h4' | 'label';
  onClick?: (e: React.MouseEvent<HTMLElement>) => void;
  title?: string;
}

/**
 * Universal SSOT renderer for KaTeX math formulas, markdown formatting,
 * and embedded SVG vector diagrams across the entire platform.
 */
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

interface QuestionStemDisplayProps {
  text: any;
  type?: string;
  prefix?: React.ReactNode;
  questionCode?: string;
  showQuestionCode?: boolean;
  className?: string;
  style?: React.CSSProperties;
  headerRight?: React.ReactNode;
}

/**
 * SSOT Question Stem Renderer.
 * Automatically handles:
 * 1. Assertion & Reason questions (splits and renders Assertion (A) & Reason (R) cleanly).
 * 2. Normal question text with embedded KaTeX math and visual SVG diagrams.
 * 3. Optional question code badge (Rule 2.O standard).
 * 4. Custom header prefixes (e.g. Q1. ) and right-aligned action buttons (e.g. Edit Answer).
 */
export const QuestionStemDisplay: React.FC<QuestionStemDisplayProps> = ({
  text,
  type,
  prefix,
  questionCode,
  showQuestionCode = false,
  className = '',
  style,
  headerRight
}) => {
  const isAR = isAssertionReasonType(type) || (typeof text === 'string' && /(?:Assertion\s*\(A\)|Reason\s*\(R\))/i.test(text));

  if (isAR) {
    const { assertion, reason } = extractAssertionAndReason({ text, type });
    return (
      <div className={`question-stem-ar ${className}`.trim()} style={{ width: '100%', ...style }}>
        {(prefix || headerRight || (showQuestionCode && questionCode)) && (
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px', gap: '8px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              {prefix && <span style={{ fontWeight: 700 }}>{prefix}</span>}
              {showQuestionCode && questionCode && (
                <span className="badge badge-secondary" style={{ fontSize: '10.5px', opacity: 0.85 }}>
                  {questionCode}
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

  // Normal question stem
  const rawPrefix = typeof prefix === 'string' ? prefix : '';
  const reactNodePrefix = typeof prefix !== 'string' ? prefix : null;
  const combinedText = rawPrefix ? `${rawPrefix}${text || ''}` : (text || '');

  return (
    <div className={`question-stem-normal ${className}`.trim()} style={{ width: '100%', ...style }}>
      {(headerRight || (showQuestionCode && questionCode) || reactNodePrefix) ? (
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '10px' }}>
          <div style={{ flex: 1, minWidth: 0 }}>
            {reactNodePrefix && <span style={{ fontWeight: 700, marginRight: '4px' }}>{reactNodePrefix}</span>}
            <RichMathText content={combinedText} inline={!reactNodePrefix} />
            {showQuestionCode && questionCode && (
              <span className="badge badge-secondary" style={{ fontSize: '10px', marginLeft: '6px', opacity: 0.85 }}>
                {questionCode}
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

interface QuestionExplanationDisplayProps {
  explanation: any;
  label?: string;
  className?: string;
  style?: React.CSSProperties;
}

/**
 * SSOT Question Solution / Explanation Renderer.
 * Properly renders KaTeX math formulas, steps, and SVG diagrams in solutions.
 */
export const QuestionExplanationDisplay: React.FC<QuestionExplanationDisplayProps> = ({
  explanation,
  label = '💡 Explanation:',
  className = '',
  style
}) => {
  if (!explanation) return null;

  return (
    <div
      className={`pq-explanation ${className}`.trim()}
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

interface QuestionOptionRowProps {
  index: number;
  label?: string;
  text: any;
  isCorrect?: boolean;
  isSelected?: boolean;
  voteCount?: number;
  onVoteClick?: () => void;
  onClick?: () => void;
  style?: React.CSSProperties;
}

/**
 * SSOT Question Option Row.
 * Uniformly renders options across Practice, Exam, Review, and Report screens.
 */
export const QuestionOptionRow: React.FC<QuestionOptionRowProps> = ({
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
    bg = 'var(--success-bg, rgba(22, 163, 74, 0.08))';
  } else if (isSelected) {
    border = '1.5px solid var(--accent, #2563eb)';
    bg = 'var(--accent-soft, rgba(37, 99, 235, 0.08))';
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
      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '8px', flex: 1, minWidth: 0 }}>
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
