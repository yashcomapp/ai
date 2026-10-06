'use client';

import React, { useEffect, useLayoutEffect, useRef, useState, useCallback, useMemo } from 'react';
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
   1. Universal Rich Math & SVG Diagram Renderer (Flicker-Free SSOT)
   ========================================================================= */

const useIsomorphicLayoutEffect = typeof window !== 'undefined' ? useLayoutEffect : useEffect;

export interface RichMathTextProps {
  content: any;
  className?: string;
  style?: React.CSSProperties;
  inline?: boolean;
  as?: 'div' | 'span' | 'p' | 'h2' | 'h3' | 'h4' | 'label';
  onClick?: (e: React.MouseEvent<HTMLElement>) => void;
  onDiagramClick?: (svgHtml: string) => void;
  title?: string;
}

export const RichMathText: React.FC<RichMathTextProps> = React.memo(({
  content,
  className = '',
  style,
  inline = false,
  as,
  onClick,
  onDiagramClick,
  title
}) => {
  const containerRef = useRef<HTMLElement | null>(null);
  const lastHtmlRef = useRef<string>('');
  const formattedHtml = useMemo(() => formatRichText(content || ''), [content]);

  useIsomorphicLayoutEffect(() => {
    const el = containerRef.current;
    if (!el) return;

    // If content has not changed and element already has rendered KaTeX, skip
    if (lastHtmlRef.current === formattedHtml && (el.dataset.rendered === 'true' || el.querySelector('.katex'))) {
      return;
    }

    lastHtmlRef.current = formattedHtml;
    el.innerHTML = formattedHtml;

    const win = typeof window !== 'undefined' ? (window as any) : null;
    if (win && win.renderMathInElement) {
      try {
        win.renderMathInElement(el, KATEX_AUTO_RENDER_OPTIONS);
        el.dataset.rendered = 'true';
      } catch (err) {
        console.warn('RichMathText renderMathInElement failed:', err);
      }
    } else {
      el.dataset.rendered = 'false';
    }
  }, [formattedHtml]);

  const handleClick = (e: React.MouseEvent<HTMLElement>) => {
    if (onClick) onClick(e);
    const target = e.target as HTMLElement | SVGElement | null;
    const diagramWrapper = target?.closest('.zoomable-diagram-wrapper');
    const svgEl = target?.closest('svg');
    if (diagramWrapper || svgEl) {
      const actualSvg = (diagramWrapper?.querySelector('svg') || svgEl) as SVGElement | null;
      if (actualSvg && onDiagramClick) {
        e.preventDefault();
        e.stopPropagation();
        onDiagramClick(actualSvg.outerHTML);
      }
    }
  };

  const Component = (as || (inline ? 'span' : 'div')) as any;
  const combinedClass = `math-container ${className}`.trim();

  return (
    <Component
      ref={containerRef}
      className={combinedClass}
      style={style}
      onClick={handleClick}
      title={title}
      suppressHydrationWarning
    />
  );
});
RichMathText.displayName = 'RichMathText';

/* =========================================================================
   1.5. Interactive Diagram & Image Zoom Lightbox Modal
   ========================================================================= */

export interface DiagramMedia {
  type: 'svg' | 'image';
  content: string;
  title?: string;
}

export interface DiagramZoomModalProps {
  isOpen: boolean;
  onClose: () => void;
  media: DiagramMedia | null;
}

export const DiagramZoomModal: React.FC<DiagramZoomModalProps> = ({
  isOpen,
  onClose,
  media
}) => {
  const [scale, setScale] = useState(1);
  const [pan, setPan] = useState({ x: 0, y: 0 });
  const [isDragging, setIsDragging] = useState(false);
  const [dragStart, setDragStart] = useState({ x: 0, y: 0 });
  const [touchDistance, setTouchDistance] = useState<number | null>(null);

  // Reset zoom and pan whenever modal opens or media changes
  useEffect(() => {
    if (isOpen) {
      setScale(1);
      setPan({ x: 0, y: 0 });
      setIsDragging(false);
      setTouchDistance(null);
      const originalOverflow = document.body.style.overflow;
      document.body.style.overflow = 'hidden';
      return () => {
        document.body.style.overflow = originalOverflow;
      };
    }
  }, [isOpen, media]);

  // Keyboard shortcut handler (Escape to close, +/-/0 to zoom)
  useEffect(() => {
    if (!isOpen) return;
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
      else if (e.key === '+' || e.key === '=') {
        setScale(s => Math.min(5, Math.round((s + 0.5) * 10) / 10));
      } else if (e.key === '-') {
        setScale(s => Math.max(0.6, Math.round((s - 0.5) * 10) / 10));
      } else if (e.key === '0') {
        setScale(1);
        setPan({ x: 0, y: 0 });
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen || !media) return null;

  const handleZoomIn = (e: React.MouseEvent) => {
    e.stopPropagation();
    setScale(s => Math.min(5, Math.round((s + 0.5) * 10) / 10));
  };

  const handleZoomOut = (e: React.MouseEvent) => {
    e.stopPropagation();
    setScale(s => Math.max(0.6, Math.round((s - 0.5) * 10) / 10));
  };

  const handleReset = (e: React.MouseEvent) => {
    e.stopPropagation();
    setScale(1);
    setPan({ x: 0, y: 0 });
  };

  const handleWheel = (e: React.WheelEvent) => {
    e.preventDefault();
    e.stopPropagation();
    const delta = e.deltaY > 0 ? -0.2 : 0.2;
    setScale(s => Math.max(0.6, Math.min(5, Math.round((s + delta) * 10) / 10)));
  };

  // Mouse pan drag
  const handleMouseDown = (e: React.MouseEvent) => {
    if (e.button !== 0) return; // Only left mouse button
    setIsDragging(true);
    setDragStart({ x: e.clientX - pan.x, y: e.clientY - pan.y });
  };

  const handleMouseMove = (e: React.MouseEvent) => {
    if (!isDragging) return;
    setPan({ x: e.clientX - dragStart.x, y: e.clientY - dragStart.y });
  };

  const handleMouseUp = () => setIsDragging(false);

  // Touch pan & pinch-to-zoom
  const handleTouchStart = (e: React.TouchEvent) => {
    if (e.touches.length === 1) {
      setIsDragging(true);
      setDragStart({ x: e.touches[0].clientX - pan.x, y: e.touches[0].clientY - pan.y });
    } else if (e.touches.length === 2) {
      setIsDragging(false);
      const dist = Math.hypot(
        e.touches[0].clientX - e.touches[1].clientX,
        e.touches[0].clientY - e.touches[1].clientY
      );
      setTouchDistance(dist);
    }
  };

  const handleTouchMove = (e: React.TouchEvent) => {
    if (e.touches.length === 1 && isDragging) {
      setPan({ x: e.touches[0].clientX - dragStart.x, y: e.touches[0].clientY - dragStart.y });
    } else if (e.touches.length === 2 && touchDistance !== null) {
      const dist = Math.hypot(
        e.touches[0].clientX - e.touches[1].clientX,
        e.touches[0].clientY - e.touches[1].clientY
      );
      const factor = dist / touchDistance;
      setScale(s => Math.max(0.6, Math.min(5, Math.round((s * factor) * 10) / 10)));
      setTouchDistance(dist);
    }
  };

  const handleTouchEnd = () => {
    setIsDragging(false);
    setTouchDistance(null);
  };

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-label="Figure Inspection Modal"
      onClick={onClose}
      style={{
        position: 'fixed',
        inset: 0,
        zIndex: 999999,
        background: 'rgba(10, 15, 29, 0.92)',
        backdropFilter: 'blur(8px)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '16px',
        userSelect: 'none'
      }}
    >
      {/* Top Controls Bar */}
      <div
        onClick={e => e.stopPropagation()}
        style={{
          width: '100%',
          maxWidth: '900px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: '12px',
          padding: '10px 16px',
          background: 'rgba(255, 255, 255, 0.08)',
          borderRadius: '12px',
          border: '1px solid rgba(255, 255, 255, 0.12)',
          color: '#ffffff'
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ fontSize: '18px' }}>📐</span>
          <div>
            <div style={{ fontWeight: 700, fontSize: '14px', letterSpacing: '0.2px' }}>
              {media.title || 'Figure Inspection'}
            </div>
            <div style={{ fontSize: '11px', color: 'rgba(255, 255, 255, 0.6)' }}>
              Zoom & pan to inspect fine markings & angles
            </div>
          </div>
        </div>

        {/* Zoom Controls */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <button
            type="button"
            onClick={handleZoomOut}
            disabled={scale <= 0.6}
            style={{
              background: 'rgba(255, 255, 255, 0.15)',
              border: '1px solid rgba(255, 255, 255, 0.2)',
              color: '#ffffff',
              borderRadius: '6px',
              width: '34px',
              height: '34px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '18px',
              fontWeight: 'bold',
              cursor: scale <= 0.6 ? 'not-allowed' : 'pointer',
              opacity: scale <= 0.6 ? 0.4 : 1
            }}
            title="Zoom Out (-)"
          >
            −
          </button>

          <span
            style={{
              minWidth: '54px',
              textAlign: 'center',
              fontSize: '13px',
              fontWeight: 700,
              padding: '6px 8px',
              background: 'rgba(255, 255, 255, 0.12)',
              borderRadius: '6px'
            }}
          >
            {Math.round(scale * 100)}%
          </span>

          <button
            type="button"
            onClick={handleZoomIn}
            disabled={scale >= 5}
            style={{
              background: 'rgba(255, 255, 255, 0.15)',
              border: '1px solid rgba(255, 255, 255, 0.2)',
              color: '#ffffff',
              borderRadius: '6px',
              width: '34px',
              height: '34px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '18px',
              fontWeight: 'bold',
              cursor: scale >= 5 ? 'not-allowed' : 'pointer',
              opacity: scale >= 5 ? 0.4 : 1
            }}
            title="Zoom In (+)"
          >
            +
          </button>

          <button
            type="button"
            onClick={handleReset}
            style={{
              background: 'rgba(255, 255, 255, 0.12)',
              border: '1px solid rgba(255, 255, 255, 0.18)',
              color: '#ffffff',
              borderRadius: '6px',
              padding: '6px 12px',
              fontSize: '12px',
              fontWeight: 600,
              cursor: 'pointer'
            }}
            title="Reset Zoom (0)"
          >
            ↺ Reset
          </button>

          <button
            type="button"
            onClick={onClose}
            style={{
              background: 'rgba(239, 68, 68, 0.25)',
              border: '1px solid rgba(239, 68, 68, 0.4)',
              color: '#fca5a5',
              borderRadius: '6px',
              padding: '6px 14px',
              fontSize: '13px',
              fontWeight: 700,
              cursor: 'pointer',
              marginLeft: '4px'
            }}
            title="Close (Esc)"
          >
            ✕ Close
          </button>
        </div>
      </div>

      {/* Main Pannable/Zoomable Viewport */}
      <div
        onWheel={handleWheel}
        onMouseDown={handleMouseDown}
        onMouseMove={handleMouseMove}
        onMouseUp={handleMouseUp}
        onMouseLeave={handleMouseUp}
        onTouchStart={handleTouchStart}
        onTouchMove={handleTouchMove}
        onTouchEnd={handleTouchEnd}
        onClick={e => e.stopPropagation()}
        style={{
          flex: 1,
          width: '100%',
          maxWidth: '1000px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          overflow: 'hidden',
          position: 'relative',
          cursor: isDragging ? 'grabbing' : (scale > 1 ? 'grab' : 'default'),
          touchAction: 'none'
        }}
      >
        <div
          style={{
            transform: `translate(${pan.x}px, ${pan.y}px) scale(${scale})`,
            transformOrigin: 'center center',
            transition: isDragging ? 'none' : 'transform 0.12s cubic-bezier(0.16, 1, 0.3, 1)',
            display: 'inline-flex',
            alignItems: 'center',
            justifyContent: 'center',
            background: '#ffffff',
            borderRadius: '14px',
            padding: '24px',
            boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.7)',
            maxWidth: '92vw',
            maxHeight: '75vh'
          }}
        >
          {media.type === 'svg' ? (
            <div
              style={{
                width: '100%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
              }}
              dangerouslySetInnerHTML={{ __html: media.content }}
            />
          ) : (
            <img
              src={media.content}
              alt={media.title || 'Enlarged figure'}
              style={{
                maxWidth: '85vw',
                maxHeight: '70vh',
                objectFit: 'contain',
                borderRadius: '8px'
              }}
              draggable={false}
            />
          )}
        </div>
      </div>

      {/* Bottom Hint Bar */}
      <div
        onClick={e => e.stopPropagation()}
        style={{
          fontSize: '12px',
          color: 'rgba(255, 255, 255, 0.65)',
          background: 'rgba(255, 255, 255, 0.05)',
          padding: '6px 16px',
          borderRadius: '20px',
          display: 'flex',
          alignItems: 'center',
          gap: '6px'
        }}
      >
        <span>💡</span>
        <span>Pinch or use <strong>+</strong> / <strong>−</strong> to zoom • Drag to pan • Tap <strong>✕</strong> or backdrop to close</span>
      </div>
    </div>
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

export const QuestionDisplay: React.FC<QuestionDisplayProps> = React.memo(({
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
  // Zoomable diagram & image modal state
  const [zoomedDiagram, setZoomedDiagram] = useState<DiagramMedia | null>(null);

  const handleDiagramClick = useCallback((svgHtml: string) => {
    setZoomedDiagram({
      type: 'svg',
      content: svgHtml,
      title: 'Figure Inspection'
    });
  }, []);

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
              <strong>Assertion (A):</strong> <RichMathText content={assertion} inline onDiagramClick={handleDiagramClick} />
            </div>
            <div>
              <strong>Reason (R):</strong> <RichMathText content={reason} inline onDiagramClick={handleDiagramClick} />
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
              <RichMathText content={combinedText} inline={!reactNodePrefix} onDiagramClick={handleDiagramClick} />
              {showQuestionCode && qCode && (
                <span className="badge badge-secondary" style={{ fontSize: '10px', marginLeft: '6px', opacity: 0.85 }}>
                  {qCode}
                </span>
              )}
            </div>
            {headerRight && <div style={{ flexShrink: 0 }}>{headerRight}</div>}
          </div>
        ) : (
          <RichMathText content={combinedText} onDiagramClick={handleDiagramClick} />
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
              <RichMathText content={stripOptionLabel(optText)} inline style={{ flex: 1 }} onDiagramClick={handleDiagramClick} />
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
              <RichMathText content={stripOptionLabel(optText)} inline style={{ flex: 1 }} onDiagramClick={handleDiagramClick} />
            </div>
          );
        })}

        {/* User Answer vs Correct Answer Summary Bar */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '3px', fontSize: '11.5px', background: 'var(--surface-3, #f1f5f9)', padding: '6px 10px', borderRadius: '6px', border: '1px solid var(--border-light, #e2e8f0)', marginTop: '4px' }}>
          <div>
            <strong style={{ color: 'var(--text-muted, #64748b)', marginRight: '6px' }}>Student Answer:</strong>
            <span style={{ color: effectiveIsCorrect ? 'var(--success, #16a34a)' : 'var(--danger, #dc2626)', fontWeight: 700 }}>
              {isUnanswered ? '(blank / unattempted)' : <RichMathText content={stripOptionLabel(String(qUserAnswer))} inline onDiagramClick={handleDiagramClick} />}
            </span>
          </div>
          <div>
            <strong style={{ color: 'var(--text-muted, #64748b)', marginRight: '6px' }}>Correct Answer:</strong>
            <span style={{ color: 'var(--success, #16a34a)', fontWeight: 'bold' }}>
              <RichMathText content={stripOptionLabel(Array.isArray(qCorrectAnswer) ? qCorrectAnswer.join(', ') : String(qCorrectAnswer))} inline onDiagramClick={handleDiagramClick} />
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
                  <RichMathText content={stripOptionLabel(optText)} inline style={{ flex: 1 }} onDiagramClick={handleDiagramClick} />
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
              ✅ Correct Answer: <RichMathText content={Array.isArray(qCorrectAnswer) ? qCorrectAnswer.join(', ') : String(qCorrectAnswer)} inline onDiagramClick={handleDiagramClick} />
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
              <RichMathText content={stripOptionLabel(optText)} inline style={{ flex: 1 }} onDiagramClick={handleDiagramClick} />
            </div>
          );
        })}

        {!resolvedOptions && qCorrectAnswer && (
          <div style={{ fontSize: '11.5px', marginTop: '4px', color: 'var(--success, #16a34a)', fontWeight: 600 }}>
            <strong>Correct Answer:</strong> <RichMathText content={Array.isArray(qCorrectAnswer) ? qCorrectAnswer.join(', ') : String(qCorrectAnswer)} inline onDiagramClick={handleDiagramClick} />
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
        <RichMathText content={qExplanation} onDiagramClick={handleDiagramClick} />
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

      {/* 2. Optional Image (Clickable Zoom Inspection) */}
      {qImage && (
        <div
          className="zoomable-image-wrapper"
          style={{ margin: '8px 0 12px', position: 'relative', display: 'inline-block', cursor: 'zoom-in' }}
          onClick={() => setZoomedDiagram({ type: 'image', content: qImage, title: 'Figure Inspection' })}
          title="Click or tap to zoom figure"
        >
          <div style={{ position: 'relative', display: 'inline-block' }}>
            <Image
              src={qImage}
              alt="Question illustration"
              width={320}
              height={200}
              style={{ objectFit: 'contain', borderRadius: '6px', border: '1px solid var(--border-light, #e2e8f0)' }}
            />
            <div style={{
              position: 'absolute',
              top: '6px',
              right: '6px',
              background: 'rgba(15,23,42,0.8)',
              color: '#ffffff',
              padding: '2px 8px',
              borderRadius: '4px',
              fontSize: '11px',
              fontWeight: 600,
              pointerEvents: 'none',
              display: 'inline-flex',
              alignItems: 'center',
              gap: '4px',
              backdropFilter: 'blur(4px)',
              boxShadow: '0 1px 3px rgba(0,0,0,0.3)',
              letterSpacing: '0.3px'
            }}>
              🔍 Zoom
            </div>
          </div>
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

      {/* 5. Diagram & Image Zoom Lightbox Modal */}
      <DiagramZoomModal
        isOpen={!!zoomedDiagram}
        onClose={() => setZoomedDiagram(null)}
        media={zoomedDiagram}
      />
    </div>
  );
});
QuestionDisplay.displayName = 'QuestionDisplay';

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
