import { useState } from 'react';

export function useReports() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchReport = async (url: string, idToken: string) => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(url, {
        headers: { 'Authorization': `Bearer ${idToken}` },
        cache: 'no-store'
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



  const getInterventionQueue = async (idToken: string, forceRefresh?: boolean) => {
    const url = forceRefresh ? '/api/admin/reports/interventions?refresh=true' : '/api/admin/reports/interventions';
    return fetchReport(url, idToken);
  };

  const getUsageReport = async (idToken: string) => {
    return fetchReport('/api/admin/reports/usage', idToken);
  };

  const getIntegrityReport = async (idToken: string, forceRefresh?: boolean) => {
    const url = forceRefresh ? '/api/admin/integrity?refresh=true' : '/api/admin/integrity';
    return fetchReport(url, idToken);
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

  return {
    loading,
    error,
    getInterventionQueue,
    getUsageReport,
    getIntegrityReport,
    getQuotientReport
  };
}
