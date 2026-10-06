'use client';

import {
  preprocessMathText,
  stripOptionLabel,
  extractAssertionAndReason,
  isMultipleChoiceType,
  isTrueFalseType,
  isAssertionReasonType,
  isNumericalType,
  isFillBlanksType,
  normalizeOptionAnswer,
  parseAnswerList,
  isOptionMatch
} from '@/lib/questionTypes';
import { QuestionStemDisplay, RichMathText } from '@/components/QuestionDisplay';

interface PracticeQuestionCardProps {
  question: any;
  currentQIndex: number;
  totalQuestions: number;
  userAnswer: string;
  isQSubmitted: boolean;
  isDisputed?: boolean;
  isSubmittingPractice: boolean;
  feedbackCorrect: boolean;
  explanationTimer: number;
  questionContainerRef: React.RefObject<HTMLDivElement | null>;
  onOpenReportModal?: () => void;
  onCheckboxChange: (letter: string) => void;
  onRadioChange: (choice: string) => void;
  onTextAnswerChange: (text: string) => void;
  onBack: () => void;
  onSubmitQuestion: () => void;
  onNext: () => void;
}

export function PracticeQuestionCard({
  question,
  currentQIndex,
  totalQuestions,
  userAnswer,
  isQSubmitted,
  isSubmittingPractice,
  feedbackCorrect,
  explanationTimer,
  questionContainerRef,
  onCheckboxChange,
  onRadioChange,
  onTextAnswerChange,
  onBack,
  onSubmitQuestion,
  onNext
}: PracticeQuestionCardProps) {
  if (!question) return null;

  return (
    <div 
      className="card" 
      ref={questionContainerRef as any} 
      style={{ 
        background: 'var(--surface)', 
        padding: '24px', 
        borderRadius: 'var(--radius-lg)', 
        border: '1px solid var(--border-light)', 
        flex: 1, 
        display: 'flex', 
        flexDirection: 'column', 
        justifyContent: 'space-between' 
      }}
    >
      <div>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
          <span className="badge badge-info" style={{ textTransform: 'uppercase', fontSize: '10px' }}>
            Q {currentQIndex + 1} of {totalQuestions}
          </span>
          <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
            <span className="badge badge-secondary" style={{ textTransform: 'uppercase', fontSize: '10px' }}>
              {question.difficulty} • {question.bloomLevel}
            </span>
          </div>
        </div>

        <QuestionStemDisplay
          text={question.text || ''}
          type={question.type}
          style={{ fontSize: '16px', fontWeight: 700, margin: '15px 0 20px', lineHeight: '1.5' }}
        />

        {/* Options Selector Layout */}
        <div className="options-container" style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '16px' }}>
          {/* 1. Multiple MCQ */}
          {isMultipleChoiceType(question.type) && Array.isArray(question.options) && question.options.length > 0 && (
            question.options.map((opt: any, oIdx: number) => {
              const letter = String.fromCharCode(65 + oIdx);
              let isChecked = false;
              try { isChecked = JSON.parse(userAnswer || '[]').includes(letter); } catch {}
              const optionText = typeof opt === 'object' && opt ? (opt.text || opt.value || '') : String(opt);
              const correctList = Array.isArray(question.correctAnswers) && question.correctAnswers.length > 0
                ? question.correctAnswers
                : parseAnswerList(question.correctAnswer);
              const correctLetters = correctList.map((c: any) => normalizeOptionAnswer(c, question.options));
              const isThisCorrect = correctLetters.includes(letter);

              let itemBorder = isChecked ? '2px solid var(--accent)' : '1px solid var(--border-light)';
              let itemBg = isChecked ? 'var(--accent-light)' : 'var(--surface)';
              let badge = null;

              if (isQSubmitted) {
                if (isChecked) {
                  if (isThisCorrect) {
                    itemBorder = '2px solid var(--success)';
                    itemBg = 'rgba(16, 185, 129, 0.12)';
                    badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Selected (Correct)</span>;
                  } else {
                    itemBorder = '2px solid var(--danger)';
                    itemBg = 'rgba(239, 68, 68, 0.12)';
                    badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--danger)', fontWeight: 700 }}>✗ Selected (Incorrect)</span>;
                  }
                } else if (isThisCorrect) {
                  itemBorder = '2px dashed var(--success)';
                  itemBg = 'rgba(16, 185, 129, 0.06)';
                  badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Correct Choice</span>;
                }
              }

              return (
                <div 
                  key={`${question.id}-${oIdx}`} 
                  onClick={() => !isQSubmitted && onCheckboxChange(letter)}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '12px',
                    padding: '12px 16px',
                    borderRadius: 'var(--radius-sm)',
                    border: itemBorder,
                    background: itemBg,
                    cursor: isQSubmitted ? 'not-allowed' : 'pointer',
                    transition: 'border 0.15s, background 0.15s'
                  }}
                >
                  <input 
                    type="checkbox" 
                    checked={isChecked}
                    onChange={() => {}}
                    disabled={isQSubmitted}
                  />
                  <div className="math-container" style={{ fontSize: '13px', color: 'var(--text)' }}>
                    <strong>{letter}.</strong> {preprocessMathText(stripOptionLabel(optionText))}
                  </div>
                  {badge}
                </div>
              );
            })
          )}

          {/* 2. True/False */}
          {isTrueFalseType(question.type) && (
            ['True', 'False'].map((val) => {
              const selected = userAnswer.toLowerCase() === val.toLowerCase();
              const correctVal = String(question.correctAnswer || (Array.isArray(question.correctAnswers) ? question.correctAnswers[0] : '')).trim().toLowerCase();
              const isThisCorrect = val.toLowerCase() === correctVal;

              let itemBorder = selected ? '2px solid var(--accent)' : '1px solid var(--border-light)';
              let itemBg = selected ? 'var(--accent-light)' : 'var(--surface)';
              let badge = null;

              if (isQSubmitted) {
                if (selected) {
                  if (isThisCorrect) {
                    itemBorder = '2px solid var(--success)';
                    itemBg = 'rgba(16, 185, 129, 0.12)';
                    badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Selected (Correct)</span>;
                  } else {
                    itemBorder = '2px solid var(--danger)';
                    itemBg = 'rgba(239, 68, 68, 0.12)';
                    badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--danger)', fontWeight: 700 }}>✗ Selected (Incorrect)</span>;
                  }
                } else if (isThisCorrect) {
                  itemBorder = '2px dashed var(--success)';
                  itemBg = 'rgba(16, 185, 129, 0.06)';
                  badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Correct Choice</span>;
                }
              }

              return (
                <div 
                  key={`${question.id}-${val}`} 
                  onClick={() => !isQSubmitted && onRadioChange(val)}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '12px',
                    padding: '12px 16px',
                    borderRadius: 'var(--radius-sm)',
                    border: itemBorder,
                    background: itemBg,
                    cursor: isQSubmitted ? 'not-allowed' : 'pointer',
                    transition: 'border 0.15s, background 0.15s'
                  }}
                >
                  <input 
                    type="radio" 
                    name={`q-${currentQIndex}`} 
                    checked={selected}
                    onChange={() => {}}
                    disabled={isQSubmitted}
                  />
                  <div className="math-container" style={{ fontSize: '13px', color: 'var(--text)' }}>{val}</div>
                  {badge}
                </div>
              );
            })
          )}

          {/* 3. Assertion & Reason */}
          {isAssertionReasonType(question.type) && (() => {
            const defaultArOptions = [
              { code: 'A', text: 'Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).' },
              { code: 'B', text: 'Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).' },
              { code: 'C', text: 'Assertion (A) is true, but Reason (R) is false.' },
              { code: 'D', text: 'Assertion (A) is false, but Reason (R) is true.' }
            ];

            let optionsToRender = defaultArOptions;
            if (Array.isArray(question.options) && question.options.length > 0) {
              optionsToRender = question.options.map((opt: any, oIdx: number) => {
                const letter = String.fromCharCode(65 + oIdx);
                if (typeof opt === 'string') {
                  return { code: letter, text: opt };
                }
                if (opt && typeof opt === 'object') {
                  return {
                    code: opt.code || opt.value || letter,
                    text: opt.text || opt.value || opt.label || String(opt)
                  };
                }
                return { code: letter, text: String(opt) };
              });
            }

            const rawCorrect = question.correctAnswer || (Array.isArray(question.correctAnswers) ? question.correctAnswers[0] : '');
            const correctCode = (typeof rawCorrect === 'string' && rawCorrect.length === 1 && /[A-D]/i.test(rawCorrect))
              ? rawCorrect.toUpperCase()
              : 'A';

            return optionsToRender.map((opt: any) => {
              const code = opt.code;
              const selected = userAnswer === code;
              const optionText = opt.text;
              const isThisCorrect = code.toUpperCase() === correctCode;

              let itemBorder = selected ? '2px solid var(--accent)' : '1px solid var(--border-light)';
              let itemBg = selected ? 'var(--accent-light)' : 'var(--surface)';
              let badge = null;

              if (isQSubmitted) {
                if (selected) {
                  if (isThisCorrect) {
                    itemBorder = '2px solid var(--success)';
                    itemBg = 'rgba(16, 185, 129, 0.12)';
                    badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Selected (Correct)</span>;
                  } else {
                    itemBorder = '2px solid var(--danger)';
                    itemBg = 'rgba(239, 68, 68, 0.12)';
                    badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--danger)', fontWeight: 700 }}>✗ Selected (Incorrect)</span>;
                  }
                } else if (isThisCorrect) {
                  itemBorder = '2px dashed var(--success)';
                  itemBg = 'rgba(16, 185, 129, 0.06)';
                  badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Correct Choice</span>;
                }
              }

              return (
                <div 
                  key={`${question.id}-${code}`} 
                  onClick={() => !isQSubmitted && onRadioChange(code)}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '12px',
                    padding: '12px 16px',
                    borderRadius: 'var(--radius-sm)',
                    border: itemBorder,
                    background: itemBg,
                    cursor: isQSubmitted ? 'not-allowed' : 'pointer',
                    transition: 'border 0.15s, background 0.15s'
                  }}
                >
                  <input 
                    type="radio" 
                    name={`q-${currentQIndex}`} 
                    checked={selected}
                    onChange={() => {}}
                    disabled={isQSubmitted}
                  />
                  <div className="math-container" style={{ fontSize: '13px', color: 'var(--text)' }}>
                    <strong>{code}.</strong> {preprocessMathText(stripOptionLabel(optionText))}
                  </div>
                  {badge}
                </div>
              );
            });
          })()}

          {/* 4. Single MCQ / Any Question Type with Options */}
          {!isMultipleChoiceType(question.type) && !isTrueFalseType(question.type) && !isAssertionReasonType(question.type) && Array.isArray(question.options) && question.options.length > 0 && (
            question.options.map((opt: any, oIdx: number) => {
              const letter = String.fromCharCode(65 + oIdx);
              const selected = userAnswer === letter;
              const optionText = typeof opt === 'object' && opt ? (opt.text || opt.value || '') : String(opt);
              const resolvedCorrect = question.correctAnswer || (Array.isArray(question.correctAnswers) ? question.correctAnswers[0] : '');
              const isThisCorrect = normalizeOptionAnswer(letter, question.options) === normalizeOptionAnswer(resolvedCorrect, question.options);

              let itemBorder = selected ? '2px solid var(--accent)' : '1px solid var(--border-light)';
              let itemBg = selected ? 'var(--accent-light)' : 'var(--surface)';
              let badge = null;

              if (isQSubmitted) {
                if (selected) {
                  if (isThisCorrect) {
                    itemBorder = '2px solid var(--success)';
                    itemBg = 'rgba(16, 185, 129, 0.12)';
                    badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Selected (Correct)</span>;
                  } else {
                    itemBorder = '2px solid var(--danger)';
                    itemBg = 'rgba(239, 68, 68, 0.12)';
                    badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--danger)', fontWeight: 700 }}>✗ Selected (Incorrect)</span>;
                  }
                } else if (isThisCorrect) {
                  itemBorder = '2px dashed var(--success)';
                  itemBg = 'rgba(16, 185, 129, 0.06)';
                  badge = <span style={{ marginLeft: 'auto', fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>✓ Correct Choice</span>;
                }
              }

              return (
                <div 
                  key={`${question.id}-${oIdx}`} 
                  onClick={() => !isQSubmitted && onRadioChange(letter)}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '12px',
                    padding: '12px 16px',
                    borderRadius: 'var(--radius-sm)',
                    border: itemBorder,
                    background: itemBg,
                    cursor: isQSubmitted ? 'not-allowed' : 'pointer',
                    transition: 'border 0.15s, background 0.15s'
                  }}
                >
                  <input 
                    type="radio" 
                    name={`q-${currentQIndex}`} 
                    checked={selected}
                    onChange={() => {}}
                    disabled={isQSubmitted}
                  />
                  <div className="math-container" style={{ fontSize: '13px', color: 'var(--text)' }}>
                    <strong>{letter}.</strong> {preprocessMathText(stripOptionLabel(optionText))}
                  </div>
                  {badge}
                </div>
              );
            })
          )}

          {/* 5. Direct Numerical Input */}
          {isNumericalType(question.type) && (!Array.isArray(question.options) || question.options.length === 0) && (
            <div>
              <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '6px' }}>Type Numerical Value:</label>
              <input 
                type="number" 
                value={userAnswer}
                onChange={(e) => onTextAnswerChange(e.target.value)}
                disabled={isQSubmitted}
                placeholder="Enter numerical answer..."
                style={{ width: '100%', padding: '12px', border: '1.5px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '14px', background: 'var(--surface)', color: 'var(--text)' }}
              />
            </div>
          )}

          {/* 6. Fill in the Blanks Input */}
          {isFillBlanksType(question.type) && (!Array.isArray(question.options) || question.options.length === 0) && (
            <div>
              <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '6px' }}>Type Missing Word:</label>
              <input 
                type="text" 
                value={userAnswer}
                onChange={(e) => onTextAnswerChange(e.target.value)}
                disabled={isQSubmitted}
                placeholder="Type your answer here..."
                style={{ width: '100%', padding: '12px', border: '1.5px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '14px', background: 'var(--surface)', color: 'var(--text)' }}
              />
            </div>
          )}

          {/* 7. General Text Input Fallback */}
          {!isTrueFalseType(question.type) && !isAssertionReasonType(question.type) && !isNumericalType(question.type) && !isFillBlanksType(question.type) && (!Array.isArray(question.options) || question.options.length === 0) && (
            <div>
              <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '6px' }}>Type Your Answer:</label>
              <input 
                type="text" 
                value={userAnswer}
                onChange={(e) => onTextAnswerChange(e.target.value)}
                disabled={isQSubmitted}
                placeholder="Type your answer or option..."
                style={{ width: '100%', padding: '12px', border: '1.5px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '14px', background: 'var(--surface)', color: 'var(--text)' }}
              />
            </div>
          )}
        </div>
      </div>

      {/* Navigation buttons */}
      <div style={{ display: 'flex', justifyContent: 'space-between', gap: '15px', marginTop: '30px' }}>
        <button 
          className="btn btn-secondary" 
          onClick={onBack}
          disabled={currentQIndex === 0 || isQSubmitted}
          style={{ width: '100px' }}
        >
          ← Back
        </button>

        {!isQSubmitted ? (
          <button 
            className="btn btn-primary" 
            onClick={onSubmitQuestion}
            disabled={!userAnswer}
            style={{ width: '160px' }}
          >
            Submit &amp; Check
          </button>
        ) : (
          <button 
            className="btn btn-primary" 
            onClick={onNext}
            disabled={isSubmittingPractice || (!feedbackCorrect && explanationTimer > 0)}
            style={{ width: '160px' }}
          >
            {isSubmittingPractice
              ? 'Submitting...'
              : (!feedbackCorrect && explanationTimer > 0 
                ? `Wait (${explanationTimer}s)` 
                : (currentQIndex === totalQuestions - 1 ? 'Finish Set →' : 'Next Question →'))}
          </button>
        )}
      </div>
    </div>
  );
}
