'use client';

import React, { useEffect, useState, useMemo, useDeferredValue } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';

interface StudentSummary {
  studentCode: string;
  name: string;
  batchIds: string[];
  className: string;
  isAutonomous: boolean;
  activeLocks: string[];
  sessionsCount: number;
  avgAccuracy: number;
  avgHonesty: number; // Stored in backend as avgHonesty
  avgMastery: number;
  totalQuestions: number;
  totalTimeSpent: number;
}

export default function DailyPracticeSummaryPage() {
  const { firebaseUser, logout, user } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [students, setStudents] = useState<StudentSummary[]>([]);
  const [batches, setBatches] = useState<{ id: string; name: string }[]>([]);
  const [selectedBatchId, setSelectedBatchId] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState<string>('');
  
  // Format current date in IST timezone as YYYY-MM-DD
  const getTodayISTStr = () => {
    return new Date().toLocaleDateString('en-CA', { timeZone: 'Asia/Kolkata' });
  };
  const [selectedDate, setSelectedDate] = useState<string>(getTodayISTStr());

  // Sorting state
  const [sortField, setSortField] = useState<keyof StudentSummary>('name');
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc');

  // Client-side authentication check
  useEffect(() => {
    if (user && (user as any).role !== 'admin') {
      router.replace('/student');
    }
  }, [user, router]);

  const loadData = async (dateVal: string) => {
    setLoading(true);
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/reports/daily-practice?date=${dateVal}`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (res.ok) {
        const data = await res.json();
        setStudents(data.students || []);
        setBatches(data.batches || []);
      }
    } catch (e) {
      console.error('Error loading daily practice summary:', e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (firebaseUser) {
      loadData(selectedDate);
    }
  }, [firebaseUser, selectedDate]);

  const handleSort = (field: keyof StudentSummary) => {
    if (sortField === field) {
      setSortDirection(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortField(field);
      setSortDirection(field === 'name' ? 'asc' : 'desc');
    }
  };

  const handlePrint = () => {
    window.print();
  };

  const formatTimeSpent = (totalSeconds: number) => {
    if (!totalSeconds || totalSeconds <= 0) return '0s';
    if (totalSeconds < 60) return `${totalSeconds}s`;
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    if (mins < 60) {
      return `${mins}m ${secs}s`;
    }
    const hrs = Math.floor(mins / 60);
    const remMins = mins % 60;
    return `${hrs}h ${remMins}m`;
  };

  const deferredSearch = useDeferredValue(searchQuery);

  // Filter students by selected batch and search query
  const filteredStudents = useMemo(() => {
    const qLower = deferredSearch.toLowerCase().trim();
    return students.filter(student => {
      const matchesBatch = selectedBatchId === 'all' || student.batchIds?.includes(selectedBatchId);
      if (!matchesBatch) return false;
      if (!qLower) return true;
      return student.name.toLowerCase().includes(qLower) || 
             student.studentCode.toLowerCase().includes(qLower);
    });
  }, [students, selectedBatchId, deferredSearch]);

  // Separate active (completed >= 1 session) vs. inactive (0 sessions, did not practice) students
  const activeList = useMemo(() => filteredStudents.filter(s => s.sessionsCount > 0), [filteredStudents]);
  const inactiveList = useMemo(() => filteredStudents.filter(s => s.sessionsCount === 0), [filteredStudents]);

  // Sort only the active list for display
  const sortedActiveStudents = useMemo(() => {
    return [...activeList].sort((a, b) => {
      let aVal = a[sortField];
      let bVal = b[sortField];

      if (typeof aVal === 'string' && typeof bVal === 'string') {
        return sortDirection === 'asc' 
          ? aVal.localeCompare(bVal) 
          : bVal.localeCompare(aVal);
      }

      // Number sorting
      const numA = Number(aVal || 0);
      const numB = Number(bVal || 0);
      return sortDirection === 'asc' ? numA - numB : numB - numA;
    });
  }, [activeList, sortField, sortDirection]);

  // Aggregate stats of current filtered selection
  const totalPracticedCount = activeList.length;
  const totalSessionsCount = activeList.reduce((sum, s) => sum + s.sessionsCount, 0);
  
  const sumAccuracy = activeList.reduce((sum, s) => sum + s.avgAccuracy, 0);
  const avgBatchAccuracy = totalPracticedCount > 0 ? parseFloat((sumAccuracy / totalPracticedCount).toFixed(1)) : 0;

  const sumHonesty = activeList.reduce((sum, s) => sum + s.avgHonesty, 0);
  const avgBatchIntegrity = totalPracticedCount > 0 ? parseFloat((sumHonesty / totalPracticedCount).toFixed(1)) : 100;

  const selectedBatchName = selectedBatchId === 'all' 
    ? 'All Batches' 
    : batches.find(b => b.id === selectedBatchId)?.name || 'Selected Batch';

  // Format date nicely for display
  const formatDisplayDate = (dateStr: string) => {
    try {
      const dateObj = new Date(dateStr + 'T00:00:00');
      return dateObj.toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });
    } catch {
      return dateStr;
    }
  };

  const getLockTag = (student: StudentSummary) => {
    if (student.isAutonomous) {
      return <span style={{ color: 'var(--warning)', fontSize: '11px', fontWeight: 800 }}>🤖 Autonomous</span>;
    }
    if (student.activeLocks.length > 0) {
      // Find clean code of first lock
      const lock = student.activeLocks[0];
      const code = lock.split(':')[0] || 'Topic';
      const type = lock.includes('Daily') ? 'Daily' : 'Cooldown';
      return (
        <span style={{ color: 'var(--error)', fontSize: '11px', fontWeight: 800 }} title={student.activeLocks.join(', ')}>
          🔒 {type} ({code})
        </span>
      );
    }
    return null;
  };

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      
      {/* Printable CSS Override Block */}
      <style jsx global>{`
        @media print {
          body {
            background: white !important;
            color: black !important;
            font-size: 11px !important;
          }
          .no-print, nav, header, select, button, .theme-toggle, .page-header, .sidebar, .card:not(.print-table-card) {
            display: none !important;
          }
          .print-header-info {
            display: block !important;
            margin-bottom: 20px !important;
          }
          .print-table-card {
            border: none !important;
            box-shadow: none !important;
            background: transparent !important;
            padding: 0 !important;
            margin: 0 !important;
          }
          table {
            width: 100% !important;
            border-collapse: collapse !important;
            margin-top: 15px !important;
          }
          th, td {
            border: 1px solid #ddd !important;
            padding: 6px 8px !important;
            text-align: left !important;
          }
          th {
            background-color: #f5f5f5 !important;
            color: #333 !important;
            font-weight: 700 !important;
          }
        }
        .print-header-info {
          display: none;
        }
        .sortable-th {
          cursor: pointer;
          user-select: none;
          transition: background-color 0.2s ease;
        }
        .sortable-th:hover {
          background-color: var(--bg-hover) !important;
        }
      `}</style>

      {/* Page Header (Hidden on Print) */}
      <div className="page-header glass no-print" style={{ padding: '8px 12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left" style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
          <span className="brand" style={{ fontWeight: 800, fontSize: '1.2rem', color: 'var(--accent)', cursor: 'pointer' }} onClick={() => router.push('/admin')}>YASHCOM</span>
          <nav style={{ display: 'flex', gap: '15px' }}>
            <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer' }} onClick={() => router.push('/admin/reports/learning-quotient')}>Learning Quotient (LQ)</span>
            <span style={{ fontSize: '13px', fontWeight: 700, color: 'var(--accent)', borderBottom: '2px solid var(--accent)', paddingBottom: '4px' }}>Daily Practice Summary ✍️</span>
            <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer' }} onClick={() => router.push('/admin/reports/parent-pending')}>Parent Pending</span>
            <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer' }} onClick={() => router.push('/admin/reports/usage')}>System Usage</span>
            <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer' }} onClick={() => router.push('/admin/reports/login-register')}>Login Register</span>
          </nav>
        </div>
        <div className="page-header-right" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span className="badge badge-info">{user?.name || 'Admin'}</span>
          
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </div>

      {/* Header Info Block (Only visible on Print) */}
      <div className="print-header-info">
        <h2 style={{ margin: '0 0 5px 0', color: '#1a1a1a' }}>Yashcom Foundation - Daily Practice Summary</h2>
        <div style={{ fontSize: '12px', color: '#555', borderBottom: '2px solid #333', paddingBottom: '10px' }}>
          <strong>Batch:</strong> {selectedBatchName} | <strong>Date:</strong> {formatDisplayDate(selectedDate)} | <strong>Exported:</strong> {new Date().toLocaleTimeString('en-IN')}
        </div>
        <div style={{ display: 'flex', gap: '20px', marginTop: '10px', fontSize: '11px' }}>
          <span><strong>Total Students Practiced:</strong> {totalPracticedCount}</span>
          <span><strong>Total Practice Sessions:</strong> {totalSessionsCount}</span>
          <span><strong>Avg Accuracy:</strong> {avgBatchAccuracy}%</span>
          <span><strong>Avg Integrity:</strong> {avgBatchIntegrity}%</span>
        </div>
      </div>

      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1400px', width: '100%', margin: '0 auto' }}>
        
        {/* Toolbar Controls (Hidden on Print) */}
        <div className="card glass no-print" style={{ padding: '16px 20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '15px', marginBottom: '20px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '15px', flexWrap: 'wrap' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text-muted)' }}>Batch:</span>
              <select
                value={selectedBatchId}
                onChange={(e) => setSelectedBatchId(e.target.value)}
                style={{
                  padding: '8px 14px',
                  borderRadius: 'var(--radius-sm)',
                  border: '1px solid var(--border-light)',
                  background: 'var(--bg-soft)',
                  color: 'var(--text)',
                  fontSize: '12px',
                  fontWeight: 700,
                  cursor: 'pointer'
                }}
              >
                <option value="all">🌐 All Batches</option>
                {batches.map(b => (
                  <option key={b.id} value={b.id}>📦 {b.name}</option>
                ))}
              </select>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text-muted)' }}>Date:</span>
              <input
                type="date"
                value={selectedDate}
                onChange={(e) => setSelectedDate(e.target.value)}
                style={{
                  padding: '7px 12px',
                  borderRadius: 'var(--radius-sm)',
                  border: '1px solid var(--border-light)',
                  background: 'var(--bg-soft)',
                  color: 'var(--text)',
                  fontSize: '12px',
                  fontWeight: 700,
                  cursor: 'pointer'
                }}
              />
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text-muted)' }}>Search:</span>
              <input
                type="text"
                placeholder="Search student..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                style={{
                  padding: '7px 12px',
                  borderRadius: 'var(--radius-sm)',
                  border: '1px solid var(--border-light)',
                  background: 'var(--bg-soft)',
                  color: 'var(--text)',
                  fontSize: '12px',
                  width: '180px'
                }}
              />
            </div>
          </div>

          <div>
            <button 
              className="btn btn-primary"
              onClick={handlePrint}
              style={{ display: 'flex', alignItems: 'center', gap: '6px', padding: '8px 16px', fontWeight: 700 }}
            >
              🖨️ Print Daily Summary PDF
            </button>
          </div>
        </div>

        {/* Stats Cards Row (Hidden on Print) */}
        <div className="no-print" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '16px', marginBottom: '20px' }}>
          <div className="card glass" style={{ padding: '16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Students Active</div>
            <div style={{ fontSize: '1.8rem', fontWeight: 800, color: 'var(--accent)', marginTop: '4px' }}>{totalPracticedCount}</div>
          </div>
          <div className="card glass" style={{ padding: '16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Sessions Done</div>
            <div style={{ fontSize: '1.8rem', fontWeight: 800, color: 'var(--accent)', marginTop: '4px' }}>{totalSessionsCount}</div>
          </div>
          <div className="card glass" style={{ padding: '16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Avg Accuracy</div>
            <div style={{ fontSize: '1.8rem', fontWeight: 800, color: 'var(--success)', marginTop: '4px' }}>{avgBatchAccuracy}%</div>
          </div>
          <div className="card glass" style={{ padding: '16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Avg Integrity</div>
            <div style={{ fontSize: '1.8rem', fontWeight: 800, color: avgBatchIntegrity < 85 ? 'var(--warning)' : 'var(--accent)', marginTop: '4px' }}>{avgBatchIntegrity}%</div>
          </div>
        </div>

        {/* Data Table */}
        <div className="card glass print-table-card" style={{ borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
          {loading ? (
            <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '60px 0' }}>
              <div className="spinner"></div>
              <span style={{ marginLeft: '10px', fontWeight: 600, color: 'var(--text-muted)' }}>Loading summary data...</span>
            </div>
          ) : filteredStudents.length === 0 ? (
            <div style={{ textAlign: 'center', padding: '60px 20px', color: 'var(--text-muted)' }}>
              📭 No student practice data found for {selectedBatchName} on {formatDisplayDate(selectedDate)}.
            </div>
          ) : (
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                    <th 
                      onClick={() => handleSort('name')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'left', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Student Name {sortField === 'name' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('sessionsCount')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      No. of Sessions {sortField === 'sessionsCount' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('totalQuestions')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Questions Solved {sortField === 'totalQuestions' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('avgAccuracy')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Accuracy {sortField === 'avgAccuracy' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('avgHonesty')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Integrity {sortField === 'avgHonesty' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('avgMastery')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Mastery {sortField === 'avgMastery' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('totalTimeSpent')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Time Spent {sortField === 'totalTimeSpent' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {/* Absent / Did Not Practice Section (Pinned to top, matching objective exam layout) */}
                  {inactiveList.length > 0 && (
                    <tr style={{ borderBottom: '1px solid var(--border-light)', background: 'rgba(239, 68, 68, 0.08)' }}>
                      <td colSpan={7} style={{ padding: '14px 16px', color: '#dc2626' }}>
                        <div style={{ textAlign: 'center', fontWeight: 800, fontSize: '14px', marginBottom: '10px', color: '#dc2626' }}>
                          🔴 Did Not Practice Today ({inactiveList.length})
                        </div>
                        <div style={{ 
                          display: 'grid', 
                          gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', 
                          gap: '8px 16px',
                          fontSize: '13px',
                          fontWeight: 700,
                          color: '#dc2626'
                        }}>
                          {[...inactiveList]
                            .sort((a, b) => a.name.localeCompare(b.name))
                            .map(a => (
                              <div key={a.studentCode} style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', color: '#dc2626', fontWeight: 700, fontSize: '13px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                                <span>• {a.name}</span>
                                {getLockTag(a)}
                              </div>
                            ))
                          }
                        </div>
                      </td>
                    </tr>
                  )}

                  {/* Active Practice Attempts List */}
                  {sortedActiveStudents.length === 0 ? (
                    <tr>
                      <td colSpan={7} style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
                        📭 No active practice sessions completed today.
                      </td>
                    </tr>
                  ) : (
                    sortedActiveStudents.map((row, idx) => (
                      <tr 
                        key={row.studentCode} 
                        style={{ 
                          borderBottom: idx === sortedActiveStudents.length - 1 ? 'none' : '1px solid var(--border-light)',
                          background: idx % 2 === 1 ? 'var(--bg-soft-even)' : 'transparent'
                        }}
                      >
                        <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <span>{row.name}</span>
                            {getLockTag(row)}
                          </div>
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700 }}>
                          {row.sessionsCount}
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--accent)' }}>
                          {row.totalQuestions}
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'center' }}>
                          <span style={{ color: 'var(--success)', fontWeight: 700 }}>{row.avgAccuracy}%</span>
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'center' }}>
                          <span style={{ 
                            color: row.avgHonesty < 70 ? 'var(--error)' : (row.avgHonesty < 90 ? 'var(--warning)' : 'var(--success)'),
                            fontWeight: 700
                          }}>
                            {row.avgHonesty}%
                          </span>
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'center' }}>
                          <span style={{ color: 'var(--accent)', fontWeight: 700 }}>{row.avgMastery}%</span>
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'center' }}>
                          {formatTimeSpent(row.totalTimeSpent)}
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
