import { useState } from 'react';

export function usePractice() {
  const [loading, setLoading] = useState(false);
  const [questions, setQuestions] = useState<any[]>([]);
  const [masteryAtStart, setMasteryAtStart] = useState(0);
  const [idealTimeSeconds, setIdealTimeSeconds] = useState(0);
  const [needRequest, setNeedRequest] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const startSession = async (params: {
    topicCode: string;
    category: string;
    size: number;
    idToken: string;
    examCategory?: string;
    mode?: string;
  }) => {
    setLoading(true);
    setError(null);
    try {
      const examCatQuery = params.examCategory ? `&examCategory=${params.examCategory}` : '';
      const modeQuery = params.mode ? `&mode=${params.mode}` : '';
      const res = await fetch(`/api/student/practice?topicCode=${params.topicCode}&category=${params.category}&size=${params.size}${examCatQuery}${modeQuery}`, {
        headers: { 'Authorization': `Bearer ${params.idToken}` }
      });
      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        if (errData.requireRecoveryMode || errData.allowRecovery) {
          return { requireRecoveryMode: true, allowRecovery: true, message: errData.message };
        }
        if (errData.requireTextbookStudy) {
          return { requireTextbookStudy: true, message: errData.message, lockType: errData.lockType };
        }
        throw new Error(errData.message || 'Failed to start practice session.');
      }
      const data = await res.json();
      setQuestions(data.questions || []);
      setMasteryAtStart(data.masteryAtStart || 0);
      setIdealTimeSeconds(data.idealTimeSeconds || 0);
      setNeedRequest(data.needRequest || false);
      return data;
    } catch (err: any) {
      setError(err.message || 'Failed to load practice questions.');
      throw err; // Re-throw to propagate to component state
    } finally {
      setLoading(false);
    }
  };

  const submitGrading = async (params: {
    topicCode: string;
    category: string;
    answers: any[];
    violations?: any;
    idToken: string;
    mode?: string;
    isRecoveryMode?: boolean;
  }) => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch('/api/student/practice', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${params.idToken}`
        },
        body: JSON.stringify({
          topicCode: params.topicCode,
          category: params.category,
          answers: params.answers,
          violations: params.violations,
          mode: params.mode,
          isRecoveryMode: params.isRecoveryMode || params.mode === 'recovery'
        })
      });
      if (!res.ok) throw new Error('Submission grading failed.');
      const data = await res.json();
      return data;
    } catch (err: any) {
      setError(err.message || 'Submission grading failed.');
      return null;
    } finally {
      setLoading(false);
    }
  };

  return {
    loading,
    error,
    questions,
    masteryAtStart,
    idealTimeSeconds,
    needRequest,
    startSession,
    submitGrading
  };
}
