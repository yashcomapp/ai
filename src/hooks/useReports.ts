import { useState } from 'react';

export function useReports() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchReport = async (url: string, idToken: string) => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(url, {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (!res.ok) throw new Error(`Report fetch failed: ${res.statusText}`);
      const data = await res.json();
      return data;
    } catch (err: any) {
      setError(err.message || 'Failed to load report.');
      console.error(err);
      return null;
    } finally {
      setLoading(false);
    }
  };



  const getUsageReport = async (idToken: string) => {
    return fetchReport('/api/admin/reports/usage', idToken);
  };

  const getIntegrityReport = async (idToken: string) => {
    return fetchReport('/api/admin/integrity', idToken);
  };



  const getParentPendingReport = async (idToken: string) => {
    return fetchReport('/api/admin/reports/parent-pending', idToken);
  };

  const getQuotientReport = async (idToken: string, studentCode?: string, duration?: string) => {
    let url = '/api/admin/reports/learning-quotient';
    const params = new URLSearchParams();
    if (studentCode) params.set('studentCode', studentCode);
    if (duration) params.set('duration', duration);
    const qs = params.toString();
    if (qs) url += `?${qs}`;
    return fetchReport(url, idToken);
  };

  const saveClassObservation = async (
    idToken: string, 
    data: { studentCode: string; activeParticipation: number; sincerity: number; timelyWork: number }
  ) => {
    setLoading(true);
    try {
      const res = await fetch('/api/admin/reports/learning-quotient', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${idToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      if (!res.ok) throw new Error('Failed to save classroom observation.');
      return await res.json();
    } catch (err: any) {
      setError(err.message || 'Failed to save observation.');
      return null;
    } finally {
      setLoading(false);
    }
  };

  const saveQuotientParameter = async (idToken: string, name: string, parameterId?: string) => {
    setLoading(true);
    try {
      const res = await fetch('/api/admin/reports/learning-quotient', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${idToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ action: 'saveParameter', name, parameterId })
      });
      if (!res.ok) throw new Error('Failed to save parameter');
      return await res.json();
    } catch (err: any) {
      setError(err.message || 'Failed to save parameter');
      return null;
    } finally {
      setLoading(false);
    }
  };

  const deleteQuotientParameter = async (idToken: string, parameterId: string) => {
    setLoading(true);
    try {
      const res = await fetch('/api/admin/reports/learning-quotient', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${idToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ action: 'deleteParameter', parameterId })
      });
      if (!res.ok) throw new Error('Failed to delete parameter');
      return await res.json();
    } catch (err: any) {
      setError(err.message || 'Failed to delete parameter');
      return null;
    } finally {
      setLoading(false);
    }
  };

  const batchAwardObservations = async (idToken: string, payload: { studentCodes: string[]; parameterId: string; score: number }) => {
    setLoading(true);
    try {
      const res = await fetch('/api/admin/reports/learning-quotient', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${idToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ action: 'batchAward', ...payload })
      });
      if (!res.ok) throw new Error('Failed to batch award observations');
      return await res.json();
    } catch (err: any) {
      setError(err.message || 'Failed to batch award');
      return null;
    } finally {
      setLoading(false);
    }
  };

  const logSingleObservation = async (idToken: string, studentCode: string, scores: Record<string, number>) => {
    setLoading(true);
    try {
      const res = await fetch('/api/admin/reports/learning-quotient', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${idToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ action: 'logSingleObservation', studentCode, scores })
      });
      if (!res.ok) throw new Error('Failed to save student observations');
      return await res.json();
    } catch (err: any) {
      setError(err.message || 'Failed to save student observations');
      return null;
    } finally {
      setLoading(false);
    }
  };

  const getExamAttendanceReport = async (idToken: string) => {
    return fetchReport('/api/admin/reports/exam-attendance', idToken);
  };

  return {
    loading,
    error,
    getUsageReport,
    getIntegrityReport,
    getParentPendingReport,
    getQuotientReport,
    getExamAttendanceReport,
    saveClassObservation,
    saveQuotientParameter,
    deleteQuotientParameter,
    batchAwardObservations,
    logSingleObservation
  };
}
