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

        <QuestionDisplay
          mode="practice"
          question={question}
          userAnswer={userAnswer}
          isSubmitted={isQSubmitted}
          isCorrect={feedbackCorrect}
          onSelectOption={(letter) => {
            if (isMultipleChoiceType(question.type)) {
              onCheckboxChange(letter);
            } else {
              onRadioChange(letter);
            }
          }}
          onTextInput={(text) => onTextAnswerChange(text)}
        />
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
