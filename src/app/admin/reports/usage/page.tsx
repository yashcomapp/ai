'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import { useReports } from '@/hooks/useReports';
import dynamic from 'next/dynamic';
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });
// Client Firestore imports removed
export default function UsageReportPage() {
  const { firebaseUser, logout, user } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();
  const { getUsageReport } = useReports();

  const [loading, setLoading] = useState(true);
  const [evaluations, setEvaluations] = useState<any[]>([]);
  const [activeReviewsModal, setActiveReviewsModal] = useState<'parent' | 'student' | null>(null);
  const [studentMap, setStudentMap] = useState<{[key: string]: string}>({});
  const [usageStats, setUsageStats] = useState({
    totalUsers: 0,
    totalExams: 0,
    totalQuestions: 0,
    totalAttempts: 0,
    parentReviews: 0,
    studentReviews: 0
  });

  // Sorting and PDF export states
  const [sortField, setSortField] = useState<'submission' | 'studentName' | 'date'>('date');
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('desc');
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);

  useEffect(() => {
    const loadUsageStats = async () => {
      if (!firebaseUser) return;
      try {
        const idToken = await firebaseUser.getIdToken();
        
        // Fetch student names map
        try {
          const stuRes = await fetch('/api/admin/students', {
            headers: { 'Authorization': `Bearer ${idToken}` }
          });
          if (stuRes.ok) {
            const stuData = await stuRes.json();
            const map: {[key: string]: string} = {};
            if (Array.isArray(stuData.students)) {
              stuData.students.forEach((s: any) => {
                if (s.studentCode) {
                  map[s.studentCode] = s.name + (s.autonomous ? ' ⭐' : '');
                }
              });
            }
            setStudentMap(map);
          }
        } catch (e) {
          console.warn('Failed to load students for mapping:', e);
        }

        const data = await getUsageReport(idToken);
        if (data) {
          const evalsList = (data.evaluations || []).map((item: any) => ({
            ...item,
            dateStr: item.createdAt ? new Date(item.createdAt).toLocaleDateString('en-IN') : item.date ? new Date(item.date).toLocaleDateString('en-IN') : '-'
          }));

          setEvaluations(evalsList);
          setUsageStats(data.stats || {
            totalUsers: 0,
            totalExams: 0,
            totalQuestions: 0,
            totalAttempts: 0,
            parentReviews: 0,
            studentReviews: 0
          });
        }
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    loadUsageStats();
  }, [firebaseUser]);

  const handleSort = (field: 'submission' | 'studentName' | 'date') => {
    if (sortField === field) {
      setSortDir(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortField(field);
      setSortDir('desc');
    }
  };

  const getSortedEvaluations = (list: any[]) => {
    return [...list].sort((a, b) => {
      let comparison = 0;
      if (sortField === 'submission') {
        const valA = a.examName || a.examCode || a.name || 'Submission Review';
        const valB = b.examName || b.examCode || b.name || 'Submission Review';
        comparison = valA.localeCompare(valB);
      } else if (sortField === 'studentName') {
        const valA = studentMap[a.studentCode || a.childStudentCode || ''] || 'Student';
        const valB = studentMap[b.studentCode || b.childStudentCode || ''] || 'Student';
        comparison = valA.localeCompare(valB);
      } else {
        const timeA = a.createdAt ? new Date(a.createdAt).getTime() : (a.date ? new Date(a.date).getTime() : 0);
        const timeB = b.createdAt ? new Date(b.createdAt).getTime() : (b.date ? new Date(b.date).getTime() : 0);
        comparison = timeA - timeB;
      }
      return sortDir === 'asc' ? comparison : -comparison;
    });
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading system usage stats...
        </div>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <div className="page-header glass" style={{ padding: '8px 12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderRadius: '0', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left" style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
          <span className="brand" style={{ fontWeight: 800, fontSize: '1.2rem', color: 'var(--accent)', cursor: 'pointer' }} onClick={() => router.push('/admin')}>YASHCOM</span>
          <nav style={{ display: 'flex', gap: '15px' }}>
            <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer' }} onClick={() => router.push('/admin')}>Dashboard</span>
            <span style={{ fontSize: '13px', fontWeight: 700, color: 'var(--accent)', borderBottom: '2px solid var(--accent)', paddingBottom: '4px' }}>System Usage Analytics</span>
          </nav>
        </div>
        <div className="page-header-right" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span className="badge badge-info" id="usernameDisplay">{user?.name || 'Admin'}</span>
          
          <button className="btn btn-primary" style={{ padding: '6px 12px', fontSize: '12px' }} onClick={() => setPdfSelectorOpen(true)}>📄 Export PDF</button>
          <button className="btn btn-secondary logout-btn" onClick={logout} title="Logout" style={{ fontSize: '0.8rem', padding: '6px 12px' }}>🚪</button>
        </div>
      </div>

      {/* Main Workspace */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '900px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        
        <div id="usage-stats-section" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '16px' }}>
          <div className="card" style={{ padding: '20px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', textAlign: 'center' }}>
            <div style={{ fontSize: '28px', fontWeight: 800, color: 'var(--accent)' }}>{usageStats.totalUsers}</div>
            <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '4px' }}>Registered Users</div>
          </div>
          <div className="card" style={{ padding: '20px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', textAlign: 'center' }}>
            <div style={{ fontSize: '28px', fontWeight: 800, color: 'var(--success)' }}>{usageStats.totalExams}</div>
            <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '4px' }}>Compiled Exam Papers</div>
          </div>
          <div className="card" style={{ padding: '20px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', textAlign: 'center' }}>
            <div style={{ fontSize: '28px', fontWeight: 800, color: 'var(--accent)' }}>{usageStats.totalQuestions}</div>
            <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '4px' }}>Question Bank Pool</div>
          </div>
          <div className="card" style={{ padding: '20px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', textAlign: 'center' }}>
            <div style={{ fontSize: '28px', fontWeight: 800, color: 'var(--success)' }}>{usageStats.totalAttempts}</div>
            <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '4px' }}>Exam Answer Submissions</div>
          </div>
          <div className="card stats-interactive-card" onClick={() => setActiveReviewsModal('parent')} style={{ padding: '20px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', textAlign: 'center', cursor: 'pointer', transition: 'transform 0.2s, border-color 0.2s' }}>
            <div style={{ fontSize: '28px', fontWeight: 800, color: 'var(--accent)' }}>{usageStats.parentReviews}</div>
            <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '4px' }}>Parent Reviews Conducted 🔍</div>
          </div>
          <div className="card stats-interactive-card" onClick={() => setActiveReviewsModal('student')} style={{ padding: '20px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', textAlign: 'center', cursor: 'pointer', transition: 'transform 0.2s, border-color 0.2s' }}>
            <div style={{ fontSize: '28px', fontWeight: 800, color: 'var(--success)' }}>{usageStats.studentReviews}</div>
            <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '4px' }}>Student Reviews Conducted 🔍</div>
          </div>
        </div>

      </main>

      {/* Detailed Reviews List Modal */}
      {activeReviewsModal && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '650px', width: '100%', padding: '0', overflow: 'hidden' }}>
            <div className="modal-header" style={{ padding: '16px 24px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold' }}>
                📋 {activeReviewsModal === 'parent' ? 'Parent Reviews List' : 'Student Reviews List'}
              </h4>
              <button onClick={() => setActiveReviewsModal(null)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>
            <div id="usage-reviews-section" className="modal-body" style={{ padding: '24px', maxHeight: '400px', overflowY: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px' }}>
                <thead>
                  <tr style={{ borderBottom: '2px solid var(--border-light)', textAlign: 'left' }}>
                    <th onClick={() => handleSort('submission')} style={{ padding: '8px', color: 'var(--text-muted)', cursor: 'pointer', userSelect: 'none' }}>
                      Submission {sortField === 'submission' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th onClick={() => handleSort('studentName')} style={{ padding: '8px', color: 'var(--text-muted)', cursor: 'pointer', userSelect: 'none' }}>
                      Student Name {sortField === 'studentName' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th onClick={() => handleSort('date')} style={{ padding: '8px', color: 'var(--text-muted)', cursor: 'pointer', userSelect: 'none' }}>
                      Date {sortField === 'date' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {getSortedEvaluations(evaluations
                    .filter(e => {
                      if (activeReviewsModal === 'student') {
                        return e.reviewedByActor === 'student';
                      } else {
                        return e.reviewedByActor === 'parent' || (!e.reviewedByActor && e.evaluatorType === 'parent');
                      }
                    }))
                    .map((item, idx) => (
                      <tr key={item.id || idx} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '8px', fontWeight: 'bold' }}>{item.examName || item.examCode || item.name || 'Submission Review'}</td>
                        <td style={{ padding: '8px' }}>{studentMap[item.studentCode || item.childStudentCode || ''] || 'Student'}</td>
                        <td style={{ padding: '8px' }}>{item.dateStr}</td>
                      </tr>
                    ))}
                  {evaluations.filter(e => {
                    if (activeReviewsModal === 'student') {
                      return e.reviewedByActor === 'student';
                    } else {
                      return e.reviewedByActor === 'parent' || (!e.reviewedByActor && e.evaluatorType === 'parent');
                    }
                  }).length === 0 && (
                    <tr>
                      <td colSpan={3} style={{ textAlign: 'center', padding: '20px', color: 'var(--text-faint)' }}>No records found.</td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
            <div className="modal-footer" style={{ padding: '8px 12px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end' }}>
              <button className="btn btn-secondary" onClick={() => setActiveReviewsModal(null)}>Close</button>
            </div>
          </div>
        </div>
      )}
      <ExportPdfModal
        isOpen={pdfSelectorOpen}
        onClose={() => setPdfSelectorOpen(false)}
        title="System Usage Analytics Report"
        filename="Usage_Analytics_Report.pdf"
        sections={[
          { id: 'stats', name: 'Usage Counters Summary', elementId: 'usage-stats-section' },
          ...(activeReviewsModal ? [{ id: 'reviews', name: `Reviewed Submissions Table (${activeReviewsModal.toUpperCase()})`, elementId: 'usage-reviews-section' }] : [])
        ]}
      />
    </div>
  );
}
