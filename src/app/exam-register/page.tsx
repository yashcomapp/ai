'use client';

import React, { useEffect, Suspense } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { fetchWithToken } from '@/lib/swrFetcher';
import { useRouter, useSearchParams } from 'next/navigation';
import useSWR from 'swr';

import dynamic from 'next/dynamic';
const ScorecardModal = dynamic(() => import('@/components/ScorecardModal'), { ssr: false });
import { useScorecard } from '@/hooks/useScorecard';

interface ExamRecord {
  examId: string;
  name: string;
  date: string;
  maxMarks: number;
  score: number;
  percentage: number;
  status: 'present' | 'absent';
  chapterName?: string;
  topicName?: string;
  absenceReason?: string;
}

interface RegisterData {
  studentName: string;
  studentCode: string;
  batchName: string;
  exams: ExamRecord[];
  summary: {
    total: number;
    present: number;
    absent: number;
    averagePercentage: number;
  };
}

function ExamRegisterContent() {
  const { user, firebaseUser, loading: authLoading } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const router = useRouter();
  const searchParams = useSearchParams();
  const studentCodeParam = searchParams.get('studentCode');
  const { scorecard, loading: scorecardLoading, loadScorecard, setScorecard } = useScorecard();

  const fetcher = async (url: string) => {
    return fetchWithToken(url, firebaseUser);
  };

  // If student role is logged in, default to their own student code if param not provided
  const targetCode = studentCodeParam || (user?.role === 'student' ? user?.studentCode : '');

  const { data, error, isLoading } = useSWR<RegisterData>(
    user && targetCode ? `/api/student/exam-register?studentCode=${targetCode}` : null,
    fetcher,
    { revalidateOnFocus: false, dedupingInterval: 60000 }
  );

  useEffect(() => {
    if (!authLoading && !user) {
      router.push('/register'); // Redirect to login/register if not authenticated
    }
  }, [user, authLoading, router]);

  if (authLoading || !user) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', background: 'var(--bg)', color: 'var(--text-muted)' }}>
        <span>Verifying credentials...</span>
      </div>
    );
  }

  // Helper to color-code score percentages
  const getPercentageStyle = (record: ExamRecord) => {
    if (record.status === 'absent') {
      return {
        color: '#ef4444',
        background: 'rgba(239, 68, 68, 0.1)',
        padding: '3px 8px',
        borderRadius: '12px',
        fontWeight: 700,
        fontSize: '11px',
        border: '1px solid rgba(239, 68, 68, 0.2)'
      };
    }
    
    const pct = record.percentage;
    if (pct >= 75) {
      return {
        color: '#10b981',
        background: 'rgba(16, 185, 129, 0.1)',
        padding: '3px 8px',
        borderRadius: '12px',
        fontWeight: 700,
        fontSize: '11px',
        border: '1px solid rgba(16, 185, 129, 0.2)'
      };
    } else if (pct >= 50) {
      return {
        color: '#f59e0b',
        background: 'rgba(245, 158, 11, 0.1)',
        padding: '3px 8px',
        borderRadius: '12px',
        fontWeight: 700,
        fontSize: '11px',
        border: '1px solid rgba(245, 158, 11, 0.2)'
      };
    } else {
      return {
        color: '#f97316',
        background: 'rgba(249, 115, 22, 0.1)',
        padding: '3px 8px',
        borderRadius: '12px',
        fontWeight: 700,
        fontSize: '11px',
        border: '1px solid rgba(249, 115, 22, 0.2)'
      };
    }
  };

  // Sort exams descending by date (latest first)
  const sortedExams = [...(data?.exams || [])].sort((a, b) => {
    const dateA = a.date ? new Date(a.date).getTime() : 0;
    const dateB = b.date ? new Date(b.date).getTime() : 0;
    return dateB - dateA;
  });

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      
      <style dangerouslySetInnerHTML={{ __html: ".summary-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; width: 100%; } .summary-card { padding: 16px; border-radius: var(--radius); background: var(--surface); border: 1px solid var(--border-light); display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; gap: 8px; } .exam-name-cell { max-width: 220px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; } @media (max-width: 768px) { .summary-grid { grid-template-columns: repeat(2, 1fr) !important; } .exam-name-cell { max-width: 140px !important; } }" }} />

      {/* Main Roster Body */}
      <div className="dashboard-container" style={{ maxWidth: '900px', width: '100%', margin: '0 auto', padding: '16px', flex: 1, display: 'flex', flexDirection: 'column', gap: '14px' }}>
        
        {/* Navigation & Header */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '10px' }}>
          <button
            onClick={() => {
              if (user?.role === 'parent') {
                router.push('/parent');
              } else if (user?.role === 'admin') {
                router.push('/admin');
              } else {
                router.push('/student');
              }
            }}
            className="btn btn-secondary"
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              padding: '8px 14px',
              borderRadius: 'var(--radius)',
              fontSize: '13px',
              fontWeight: 600,
              cursor: 'pointer',
              background: 'var(--surface)',
              border: '1px solid var(--border-light)',
              color: 'var(--text)'
            }}
          >
            <span>←</span> Back to Dashboard
          </button>

          {data && (
            <div style={{ textAlign: 'right' }}>
              <div style={{ fontSize: '14px', fontWeight: 700, color: 'var(--text)' }}>
                📋 Exam Attendance & Performance Register
              </div>
              <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '2px' }}>
                {data.studentName} ({data.studentCode}) • {data.batchName || 'Registered Student'}
              </div>
            </div>
          )}
        </div>

        {/* Loading and Error Handling States */}
        {isLoading && (
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '100px 0', color: 'var(--text-muted)' }}>
            <span>Retrieving exam registers...</span>
          </div>
        )}

        {error && (
          <div className="alert-box alert-box-danger" style={{ display: 'block', padding: '16px', borderRadius: 'var(--radius-lg)' }}>
            ⚠️ Error loading exam register records. Please try again or verify permissions.
          </div>
        )}

        {/* Register Details and Table */}
        {!isLoading && !error && data && (
          <>
            {/* Exams Table */}
            <div className="card glass" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
              <div style={{ overflowX: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px', textAlign: 'left' }}>
                  <thead>
                    <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                      <th style={{ padding: '12px 16px' }}>Date</th>
                      <th style={{ padding: '12px 16px' }}>Exam Name</th>
                      <th style={{ padding: '12px 16px', textAlign: 'center' }}>Percentage</th>
                      <th style={{ padding: '12px 16px', textAlign: 'left' }}>Absence Reason</th>
                    </tr>
                  </thead>
                  <tbody>
                    {sortedExams.length === 0 ? (
                      <tr>
                        <td colSpan={4} style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
                          📭 No completed or missed exams recorded for this batch.
                        </td>
                      </tr>
                    ) : (
                      sortedExams.map((record) => {
                        const isAbsent = record.status === 'absent';
                        const displayName = record.name && record.name !== '—'
                          ? record.name
                          : (record.chapterName && record.topicName
                              ? `${record.chapterName} — ${record.topicName}`
                              : record.chapterName || 'Exam');

                        return (
                          <tr 
                            key={record.examId} 
                            style={{ 
                              borderBottom: '1px solid var(--border-light)',
                              background: isAbsent ? 'rgba(239, 68, 68, 0.02)' : 'transparent'
                            }}
                          >
                            <td style={{ padding: '12px 16px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                              {record.date || '—'}
                            </td>
                            <td style={{ padding: '12px 16px', fontWeight: 600, color: 'var(--text)' }}>
                              <div 
                                className="exam-name-cell" 
                                title={isAbsent ? `${displayName} (Absent - No Scorecard)` : displayName}
                                onClick={() => {
                                  if (isAbsent) {
                                    alert(`⚠️ No Scorecard: The student was absent for "${displayName}". You can practice this topic in the Focus / Practice tab.`);
                                    return;
                                  }
                                  if (record.examId) {
                                    loadScorecard(record.examId, targetCode);
                                  }
                                }}
                                style={{
                                  cursor: !isAbsent && record.examId ? 'pointer' : 'default',
                                  color: !isAbsent && record.examId ? 'var(--accent)' : 'var(--text)',
                                  display: 'inline-flex',
                                  alignItems: 'center',
                                  gap: '4px'
                                }}
                              >
                                <span>{displayName}</span>
                                {!isAbsent && <span style={{ fontSize: '10px', opacity: 0.8 }}>🔍</span>}
                              </div>
                            </td>
                            <td style={{ padding: '12px 16px', textAlign: 'center' }}>
                              <span style={getPercentageStyle(record)}>
                                {isAbsent ? 'Absent' : `${record.percentage}%`}
                              </span>
                            </td>
                            <td style={{ padding: '12px 16px', textAlign: 'left' }}>
                              {isAbsent ? (
                                record.absenceReason ? (
                                  <span style={{ fontSize: '11.5px', color: 'var(--text)', fontWeight: 600, background: 'var(--bg-soft)', padding: '2px 8px', borderRadius: '8px', border: '1px solid var(--border-light)' }}>
                                    {record.absenceReason}
                                  </span>
                                ) : (
                                  <span style={{ color: '#ef4444', fontSize: '11.5px', fontWeight: 600 }}>Absent</span>
                                )
                              ) : (
                                <span style={{ color: 'var(--text-muted)', fontSize: '11px' }}>—</span>
                              )}
                            </td>
                          </tr>
                        );
                      })
                    )}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Summary Cards Footer */}
            <div className="summary-grid">
              
              {/* Card 1: Total Exams */}
              <div className="card glass summary-card">
                <span style={{ fontSize: '1.8rem', lineHeight: 1 }}>📅</span>
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                  <div style={{ fontSize: '9px', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600 }}>Total Exams</div>
                  <div style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--text)' }}>{data.summary.total}</div>
                </div>
              </div>

              {/* Card 2: Attended */}
              <div className="card glass summary-card">
                <span style={{ fontSize: '1.8rem', lineHeight: 1 }}>✅</span>
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                  <div style={{ fontSize: '9px', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600 }}>Present</div>
                  <div style={{ fontSize: '1.2rem', fontWeight: 800, color: '#10b981' }}>{data.summary.present}</div>
                </div>
              </div>

              {/* Card 3: Absent */}
              <div className="card glass summary-card">
                <span style={{ fontSize: '1.8rem', lineHeight: 1 }}>❌</span>
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                  <div style={{ fontSize: '9px', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600 }}>Absent</div>
                  <div style={{ fontSize: '1.2rem', fontWeight: 800, color: '#ef4444' }}>{data.summary.absent}</div>
                </div>
              </div>

              {/* Card 4: Average Grade */}
              <div className="card glass summary-card">
                <span style={{ fontSize: '1.8rem', lineHeight: 1 }}>📊</span>
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                  <div style={{ fontSize: '9px', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600 }}>Average Grade</div>
                  <div style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--accent)' }}>{data.summary.present > 0 ? `${data.summary.averagePercentage}%` : '—'}</div>
                </div>
              </div>

            </div>
          </>
        )}

      {/* Result Scorecard Details Modal */}
      {scorecard && (
        <ScorecardModal 
          scorecard={scorecard} 
          loading={scorecardLoading}
          onClose={() => setScorecard(null)} 
        />
      )}
      </div>
    </div>
  );
}

export default function ExamRegisterPage() {
  return (
    <Suspense fallback={
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', background: 'var(--bg)', color: 'var(--text-muted)' }}>
        <span>Loading exam register...</span>
      </div>
    }>
      <ExamRegisterContent />
    </Suspense>
  );
}
