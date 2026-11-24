'use client';

import React, { useEffect, useState, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import { useReports } from '@/hooks/useReports';

export default function SystemHealthAuditPage() {
  const { firebaseUser } = useAuth();
  const router = useRouter();
  const { getUsageReport } = useReports();

  const [loading, setLoading] = useState(true);
  const [data, setData] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);
  const [auditSearch, setAuditSearch] = useState('');

  useEffect(() => {
    if (!firebaseUser) return;
    let isMounted = true;

    async function loadData() {
      try {
        setLoading(true);
        const idToken = await firebaseUser!.getIdToken();
        const res = await getUsageReport(idToken);
        if (isMounted) {
          setData(res);
        }
      } catch (err: any) {
        if (isMounted) {
          setError(err.message || 'Failed to load system health metrics.');
        }
      } finally {
        if (isMounted) setLoading(false);
      }
    }

    loadData();
    return () => { isMounted = false; };
  }, [firebaseUser, getUsageReport]);

  const usageStats = data?.stats || data?.usageStats || {
    totalUsers: 0,
    totalExams: 0,
    totalQuestions: 0,
    totalAttempts: 0,
    totalEvaluations: 0,
    parentReviews: 0,
    studentReviews: 0
  };

  const evaluations: any[] = data?.evaluations || [];

  // Filtered audit logs
  const filteredAuditLogs = useMemo(() => {
    if (!evaluations) return [];
    if (!auditSearch.trim()) return evaluations.slice(0, 50);
    const q = auditSearch.toLowerCase();
    return evaluations.filter((item: any) => {
      const studentName = (item.studentName || item.studentCode || '').toLowerCase();
      const examTitle = (item.examTitle || item.title || item.examId || '').toLowerCase();
      const actor = (item.reviewedByActor || item.evaluatorType || '').toLowerCase();
      return studentName.includes(q) || examTitle.includes(q) || actor.includes(q);
    }).slice(0, 50);
  }, [evaluations, auditSearch]);

  return (
    <div style={{ background: 'var(--bg)', flex: 1, display: 'flex', flexDirection: 'column' }}>

      {/* Reports Hub Sub-Navigation Bar */}
      <div style={{ maxWidth: '1280px', width: '100%', margin: '0 auto', padding: '8px 16px 0 16px' }}>
        <nav style={{ display: 'flex', gap: '14px', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px', overflowX: 'auto' }}>
          <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports')}>
            ⚡ Classroom Remediation Hub
          </span>
          <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/daily-practice')}>
            📝 Practice Track Report
          </span>
          <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/remediation')}>
            🎯 Topic Remediation Tracker
          </span>
          <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/learning-quotient')}>
            📊 Student Learning Profiles (LQ)
          </span>
          <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--accent)', borderBottom: '2px solid var(--accent)', paddingBottom: '4px', whiteSpace: 'nowrap' }}>
            🛡️ System Health & Audit
          </span>
        </nav>
      </div>

      {/* Main Workspace */}
      <main style={{ flex: 1, padding: '10px 14px', maxWidth: '1280px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '10px' }}>
        
        {/* Header Title */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <h2 style={{ fontSize: '17px', fontWeight: 800, color: 'var(--text)', margin: 0 }}>
                🛡️ System Health & Audit
              </h2>
              <span style={{
                fontSize: '10px',
                fontWeight: 700,
                padding: '1px 6px',
                borderRadius: '6px',
                background: 'rgba(34, 197, 94, 0.12)',
                color: 'var(--success, #22c55e)'
              }}>
                Telemetry & Invariants
              </span>
            </div>
            <p style={{ fontSize: '11.5px', color: 'var(--text-muted)', margin: '2px 0 0 0' }}>
              Real-time infrastructure health, cost guard status, and forensic exam submission audit trail.
            </p>
          </div>
        </div>

        {loading ? (
          <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
            <div style={{ fontSize: '24px', marginBottom: '6px' }}>⏳</div>
            <div style={{ fontSize: '13px', fontWeight: 600 }}>Loading system telemetry & health metrics...</div>
          </div>
        ) : error ? (
          <div style={{
            background: 'rgba(239, 68, 68, 0.1)',
            border: '1px solid rgba(239, 68, 68, 0.3)',
            color: 'var(--danger, #ef4444)',
            padding: '12px',
            borderRadius: '8px',
            fontSize: '12.5px',
            fontWeight: 600
          }}>
            ⚠️ {error}
          </div>
        ) : (
          <>
            {/* 4 Health Metric Cards */}
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
              gap: '10px'
            }}>
              {/* Card 1: Registered Accounts */}
              <div style={{
                background: 'var(--surface)',
                border: '1px solid var(--border-light)',
                borderRadius: '8px',
                padding: '10px 12px'
              }}>
                <div style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '2px' }}>
                  Registered Profiles
                </div>
                <div style={{ fontSize: '20px', fontWeight: 800, color: 'var(--accent)' }}>
                  {Number(usageStats.totalUsers || 0).toLocaleString()}
                </div>
                <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
                  Active students and linked accounts
                </div>
              </div>

              {/* Card 2: Question Pool */}
              <div style={{
                background: 'var(--surface)',
                border: '1px solid var(--border-light)',
                borderRadius: '8px',
                padding: '10px 12px'
              }}>
                <div style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '2px' }}>
                  Question Bank Pool
                </div>
                <div style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text)' }}>
                  {Number(usageStats.totalQuestions || 0).toLocaleString()}
                </div>
                <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
                  Curriculum-mapped items
                </div>
              </div>

              {/* Card 3: Conducted Exams */}
              <div style={{
                background: 'var(--surface)',
                border: '1px solid var(--border-light)',
                borderRadius: '8px',
                padding: '10px 12px'
              }}>
                <div style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '2px' }}>
                  Conducted Exams
                </div>
                <div style={{ fontSize: '20px', fontWeight: 800, color: '#38bdf8' }}>
                  {Number(usageStats.totalExams || 0).toLocaleString()}
                </div>
                <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
                  Curriculum & benchmark tests
                </div>
              </div>

              {/* Card 4: Evaluated Submissions */}
              <div style={{
                background: 'var(--surface)',
                border: '1px solid var(--border-light)',
                borderRadius: '8px',
                padding: '10px 12px'
              }}>
                <div style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '2px' }}>
                  Evaluated Submissions
                </div>
                <div style={{ fontSize: '20px', fontWeight: 800, color: 'var(--success)' }}>
                  {Number((usageStats.totalEvaluations || usageStats.totalAttempts) || 0).toLocaleString()}
                </div>
                <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
                  Total graded exam & practice reviews
                </div>
              </div>
            </div>

            {/* Google Cloud Infrastructure & Live Billing Notice */}
            <div style={{
              background: 'var(--surface)',
              border: '1px solid var(--border-light)',
              borderLeft: '4px solid #38bdf8',
              borderRadius: '8px',
              padding: '10px 14px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              flexWrap: 'wrap',
              gap: '10px'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '18px' }}>☁️</span>
                <div>
                  <div style={{ fontSize: '12.5px', fontWeight: 800, color: 'var(--text)' }}>
                    Google Cloud Infrastructure & Billing
                  </div>
                  <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                    Project: <strong style={{ color: 'var(--text)' }}>ai-yashcom</strong> • Live Cloud Run compute, Artifact Registry image storage, and Firestore egress costs must be monitored directly in Google Cloud Console.
                  </div>
                </div>
              </div>
              <a
                href="https://console.cloud.google.com/billing"
                target="_blank"
                rel="noopener noreferrer"
                style={{
                  fontSize: '11px',
                  fontWeight: 800,
                  color: '#ffffff',
                  background: 'var(--accent, #3b82f6)',
                  padding: '5px 12px',
                  borderRadius: '6px',
                  textDecoration: 'none',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '5px'
                }}
              >
                Open Google Cloud Billing ↗
              </a>
            </div>

            {/* Forensic Submission Audit Trail */}
            <div style={{
              background: 'var(--surface)',
              border: '1px solid var(--border-light)',
              borderRadius: '8px',
              padding: '12px 14px',
              display: 'flex',
              flexDirection: 'column',
              gap: '10px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                <div>
                  <h3 style={{ fontSize: '13.5px', fontWeight: 800, color: 'var(--text)', margin: 0 }}>
                    🔍 Forensic Submission & Evaluation Audit Trail
                  </h3>
                  <p style={{ fontSize: '11px', color: 'var(--text-muted)', margin: '1px 0 0 0' }}>
                    Real-time audit log of evaluations, autonomous sweeps, and submissions.
                  </p>
                </div>

                <input
                  type="text"
                  placeholder="Search student or exam..."
                  value={auditSearch}
                  onChange={(e) => setAuditSearch(e.target.value)}
                  style={{
                    background: 'var(--bg)',
                    border: '1px solid var(--border)',
                    borderRadius: '6px',
                    padding: '5px 10px',
                    fontSize: '11.5px',
                    color: 'var(--text)',
                    minWidth: '200px'
                  }}
                />
              </div>

              {filteredAuditLogs.length === 0 ? (
                <div style={{ textAlign: 'center', padding: '24px', color: 'var(--text-muted)', fontSize: '12px' }}>
                  No audit records match your query.
                </div>
              ) : (
                <div style={{ overflowX: 'auto' }}>
                  <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '11.5px' }}>
                    <thead>
                      <tr style={{ borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                        <th style={{ padding: '6px 8px', fontWeight: 700 }}>Student</th>
                        <th style={{ padding: '6px 8px', fontWeight: 700 }}>Exam / Activity</th>
                        <th style={{ padding: '6px 8px', fontWeight: 700 }}>Evaluator</th>
                        <th style={{ padding: '6px 8px', fontWeight: 700 }}>Score</th>
                        <th style={{ padding: '6px 8px', fontWeight: 700 }}>Timestamp</th>
                      </tr>
                    </thead>
                    <tbody>
                      {filteredAuditLogs.map((log: any, idx: number) => (
                        <tr key={log.id || idx} style={{ borderBottom: '1px solid var(--border-light)' }}>
                          <td style={{ padding: '6px 8px', fontWeight: 600, color: 'var(--text)' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                              <span>
                                {log.studentName && !log.studentName.startsWith('ST-') 
                                  ? log.studentName 
                                  : (log.rollNumber ? `Roll #${log.rollNumber}` : (log.studentCode ? `Roll #${parseInt(log.studentCode.replace(/[^0-9]/g, '').slice(-3) || '0', 10) || '—'}` : 'Student'))}
                              </span>
                              {log.rollNumber && (
                                <span style={{ fontSize: '9.5px', color: 'var(--text-muted)', background: 'var(--bg-soft, rgba(255,255,255,0.06))', padding: '1px 5px', borderRadius: '4px' }}>
                                  #{log.rollNumber}
                                </span>
                              )}
                            </div>
                          </td>
                          <td style={{ padding: '6px 8px', color: 'var(--text-muted)' }}>
                            {log.examTitle || log.title || log.examId || 'Practice Attempt'}
                          </td>
                          <td style={{ padding: '6px 8px' }}>
                            <span style={{
                              fontSize: '10.5px',
                              padding: '2px 6px',
                              borderRadius: '4px',
                              background: 'var(--bg-soft, rgba(255,255,255,0.05))',
                              color: log.reviewedByActor === '⚡ System Auto' ? 'var(--accent)' : 'var(--text-muted)',
                              fontWeight: 600
                            }}>
                              {log.reviewedByActor || log.evaluatorType || '⚡ System Auto'}
                            </span>
                          </td>
                          <td style={{ padding: '6px 8px', fontWeight: 700, color: 'var(--accent)' }}>
                            {log.percentage != null ? `${log.percentage}%` : (log.score != null ? `${log.score} pts` : '—')}
                          </td>
                          <td style={{ padding: '6px 8px', color: 'var(--text-muted)', fontSize: '11px' }}>
                            {log.createdAt ? new Date(log.createdAt).toLocaleString([], { dateStyle: 'short', timeStyle: 'short' }) : '—'}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          </>
        )}

      </main>
    </div>
  );
}
