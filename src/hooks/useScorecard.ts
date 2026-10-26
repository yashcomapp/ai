import { useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { DetailedScorecard } from '@/types/scorecard.types';

export type { DetailedScorecard };

export function useScorecard() {
  const { firebaseUser } = useAuth();
  const [scorecard, setScorecard] = useState<DetailedScorecard | null>(null);
  const [selectedScorecardId, setSelectedScorecardId] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const loadScorecard = async (id: string, studentCode?: string) => {
    if (!firebaseUser) return;
    setSelectedScorecardId(id);
    setLoading(true);
    setScorecard(null);
    try {
      const idToken = await firebaseUser.getIdToken();
      let url = `/api/student/results?id=${encodeURIComponent(id)}`;
      if (studentCode) {
        url += `&studentCode=${encodeURIComponent(studentCode)}`;
      }
      const res = await fetch(url, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        throw new Error('Failed to load scorecard details');
      }
      const scoreData: DetailedScorecard = await res.json();
      setScorecard(scoreData);
      return scoreData;
    } catch (err: any) {
      setSelectedScorecardId(null);
      alert(err.message || 'Could not load detail review');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const clearScorecard = () => {
    setScorecard(null);
    setSelectedScorecardId(null);
  };

  return {
    scorecard,
    setScorecard,
    selectedScorecardId,
    setSelectedScorecardId,
    clearScorecard,
    loading,
    loadScorecard
  };
}
