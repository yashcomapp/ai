'use client';

import React, { useState, useEffect, useCallback } from 'react';
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
import QuestionDisplay from '@/components/QuestionDisplay';

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

export const PracticeQuestionCard = React.memo(function PracticeQuestionCard({
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
  const [readingTimer, setReadingTimer] = useState<number>(20);
  const [correctAssimilationTimer, setCorrectAssimilationTimer] = useState<number>(0);

  const handleSelectOption = useCallback((letter: string) => {
    if (isMultipleChoiceType(question?.type)) {
      onCheckboxChange(letter);
    } else {
      onRadioChange(letter);
    }
  }, [question?.type, onCheckboxChange, onRadioChange]);

  const handleTextInput = useCallback((text: string) => {
    onTextAnswerChange(text);
  }, [onTextAnswerChange]);

  useEffect(() => {
    if (isQSubmitted) {
      setReadingTimer(0);
      return;
    }
    const qType = String(question?.type || '').toLowerCase();
    const qText = String(question?.text || question?.assertion || '');
    const isNumerical = qType.includes('numerical') || qType === 'one' || qType === 'ssn' || qType === 'sln';
    const isConceptual = qType === 'oar' || qType === 'assertion_reason' || qType === 'omc' || qType === 'multiple_mcq' || qText.length > 100;
    
    // Front-door deliberation timer: 45s for numericals, 30s for complex conceptual, 20s for standard factual
    const initialSeconds = isNumerical ? 45 : (isConceptual ? 30 : 20);
    setReadingTimer(initialSeconds);

    const interval = setInterval(() => {
      setReadingTimer(prev => {
        if (prev <= 1) {
          clearInterval(interval);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [currentQIndex, isQSubmitted, question]);

  useEffect(() => {
    if (isQSubmitted && feedbackCorrect) {
      setCorrectAssimilationTimer(4);
      const interval = setInterval(() => {
        setCorrectAssimilationTimer(prev => {
          if (prev <= 1) {
            clearInterval(interval);
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
      return () => clearInterval(interval);
    } else {
      setCorrectAssimilationTimer(0);
    }
  }, [isQSubmitted, feedbackCorrect, currentQIndex]);

  if (!question) return null;

  return (
    <div 
      className="card practice-question-card" 
      ref={questionContainerRef as any} 
      style={{ 
        background: 'var(--surface)', 
        borderRadius: 'var(--radius-lg)', 
        border: '1px solid var(--border-light)', 
        flex: 1, 
        display: 'flex', 
        flexDirection: 'column', 
        justifyContent: 'space-between' 
      }}
    >
      <style>{`
        .practice-question-card {
          padding: 24px;
        }
        .practice-nav-row {
          display: flex;
          justify-content: space-between;
          align-items: center;
          gap: 15px;
          margin-top: 24px;
        }
        @media (max-width: 640px) {
          .practice-question-card {
            padding: 14px 10px !important;
          }
          .practice-nav-row {
            margin-top: 14px !important;
            gap: 8px !important;
          }
        }
      `}</style>
      <div>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
          <span className="badge badge-info" style={{ textTransform: 'uppercase', fontSize: '10px' }}>
            Q {currentQIndex + 1} of {totalQuestions}
          </span>
          <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
            {readingTimer > 0 && !isQSubmitted && (
              <span className="badge badge-warning" style={{ fontSize: '10px', fontWeight: 700 }}>
                ⏱️ Deliberation Gate: {readingTimer}s
              </span>
            )}
            <span className="badge badge-secondary" style={{ textTransform: 'uppercase', fontSize: '10px' }}>
              {question.difficulty} • {question.bloomLevel}
            </span>
          </div>
        </div>

        <QuestionDisplay
          mode="practice"
          question={question}
          userAnswer={userAnswer}
          isSubmitted={isQSubmitted}
          isCorrect={feedbackCorrect}
          onSelectOption={handleSelectOption}
          onTextInput={handleTextInput}
        />
      </div>

      {/* Navigation buttons */}
      <div className="practice-nav-row">
        <button 
          className="btn btn-secondary" 
          onClick={onBack}
          disabled={currentQIndex === 0 || isQSubmitted}
          style={{ width: '100px' }}
        >
          ← Back
        </button>

        {!isQSubmitted ? (
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <button 
              className="btn btn-primary" 
              onClick={onSubmitQuestion}
              disabled={!userAnswer || readingTimer > 0}
              style={{ minWidth: '160px' }}
            >
              {readingTimer > 0 ? `⏱️ Deliberate (${readingTimer}s)` : 'Submit & Check'}
            </button>
          </div>
        ) : (
          <button 
            className="btn btn-primary" 
            onClick={onNext} 
            disabled={isSubmittingPractice || (!feedbackCorrect && explanationTimer > 0) || (feedbackCorrect && correctAssimilationTimer > 0)}
            style={{ minWidth: '160px' }}
          >
            {isSubmittingPractice
              ? 'Submitting...'
              : (!feedbackCorrect && explanationTimer > 0 
                ? `Review Solution (${explanationTimer}s)` 
                : (feedbackCorrect && correctAssimilationTimer > 0
                  ? `Assimilate (${correctAssimilationTimer}s)`
                  : (currentQIndex === totalQuestions - 1 ? 'Finish Set →' : 'Next Question →')))}
          </button>
        )}
      </div>
    </div>
  );
});
