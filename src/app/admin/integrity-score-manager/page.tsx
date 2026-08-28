'use client';

import React, { useEffect, useState, useMemo, useDeferredValue } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import { useReports } from '@/hooks/useReports';
import dynamic from 'next/dynamic';
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });
// Client Firestore imports removed
interface Student {
  id: string;
  name: string;
  email: string;
  studentCode?: string;
  rollNumber?: string;
  class?: string;
}

interface ScoreRecord {
  id: string;
  week: number;
  year: number;
  score: number;
  level: string;
  totalSessions: number;
  tabViolations?: number;
  noFaceCount?: number;
  multipleFacesCount?: number;
}

export default function AdminIntegrityScoreManagerPage() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();
  const { getIntegrityReport } = useReports();

  const [loading, setLoading] = useState(true);
  const [students, setStudents] = useState<Student[]>([]);
  const [filteredStudents, setFilteredStudents] = useState<Student[]>([]);
  
  // Stats
  const [stats, setStats] = useState({ totalScores: 0, reviewCount: 0, avgScore: 0 });
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedClass, setSelectedClass] = useState('all');

  // Sorting
  const [sortField, setSortField] = useState<'name' | 'class'>('name');
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('asc');
  const [histSortField, setHistSortField] = useState<'week' | 'year' | 'score' | 'totalSessions'>('week');
  const [histSortDir, setHistSortDir] = useState<'asc' | 'desc'>('desc');
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);

  // Roster checks
  const [checkedIds, setCheckedIds] = useState<Set<string>>(new Set());
  
  // Selected student details
  const [selectedStudent, setSelectedStudent] = useState<Student | null>(null);
  const [history, setHistory] = useState<ScoreRecord[]>([]);
  const [loadingHistory, setLoadingHistory] = useState(false);

  // Score override reset fields
  const [resetWeek, setResetWeek] = useState<number | string>(1);
  const [resetYear, setResetYear] = useState<number | string>(2026);
  const [resetReason, setResetReason] = useState('');
  const [processingOverride, setProcessingOverride] = useState(false);

  // Operations Log Console
  const [logs, setLogs] = useState<string[]>(['[System] Ready. Select a student to manage proctoring logs...']);

  const addLog = (text: string) => {
    setLogs(prev => [...prev, `[${new Date().toLocaleTimeString()}] ${text}`]);
  };

  const fetchStatsAndStudents = async () => {
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const statsData = await getIntegrityReport(idToken);
      if (statsData) {
        setStats({
          totalScores: statsData.totalScores || 0,
          reviewCount: statsData.reviewCount || 0,
          avgScore: statsData.avgScore || 100
        });

        const studentList = statsData.students || [];
        setStudents(studentList);
        setFilteredStudents(studentList);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStatsAndStudents();
  }, [firebaseUser]);

  // Filters & Sorting
  const handleSort = (field: 'name' | 'class') => {
    if (sortField === field) {
      setSortDir(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortField(field);
      setSortDir('asc');
    }
  };

  const handleHistSort = (field: 'week' | 'year' | 'score' | 'totalSessions') => {
    if (histSortField === field) {
      setHistSortDir(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setHistSortField(field);
      setHistSortDir('desc');
    }
  };

  const deferredSearch = useDeferredValue(searchQuery);

  const sortedFilteredStudents = useMemo(() => {
    const q = deferredSearch.toLowerCase().trim();
    const list = students.filter(s => {
      if (selectedClass !== 'all' && s.class !== selectedClass) return false;
      if (q) {
        const code = s.rollNumber || s.studentCode || '';
        return s.name.toLowerCase().includes(q) || code.toLowerCase().includes(q);
      }
      return true;
    });

    return [...list].sort((a, b) => {
      const valA = a[sortField] || '';
      const valB = b[sortField] || '';
      return sortDir === 'asc' ? valA.localeCompare(valB) : valB.localeCompare(valA);
    });
  }, [students, selectedClass, deferredSearch, sortField, sortDir]);

  const sortedHistory = useMemo(() => {
    return [...history].sort((a, b) => {
      const valA = Number(a[histSortField] ?? 0);
      const valB = Number(b[histSortField] ?? 0);
      return histSortDir === 'asc' ? valA - valB : valB - valA;
    });
  }, [history, histSortField, histSortDir]);

  const handleSelectStudent = async (s: Student) => {
    setSelectedStudent(s);
    setLoadingHistory(true);
    addLog(`Fetching score history for ${s.name}...`);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const code = s.studentCode || s.rollNumber || '';
      const res = await fetch(`/api/admin/integrity?studentCode=${code}`, {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (!res.ok) throw new Error('Failed history query.');
      const data = await res.json();
      setHistory(data.history || []);
      addLog(`Loaded ${data.history?.length || 0} integrity scorecards for ${s.name}.`);
    } catch (err: any) {
      addLog(`❌ Error loading history: ${err.message}`);
    } finally {
      setLoadingHistory(false);
    }
  };

  const handleToggleSelectAll = () => {
    if (checkedIds.size === filteredStudents.length) {
      setCheckedIds(new Set());
    } else {
      setCheckedIds(new Set(filteredStudents.map(s => s.id)));
    }
  };

  const handleToggleCheck = (id: string) => {
    setCheckedIds(prev => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  // Generate scorecards for checked students
  const handleGenerateBatch = async () => {
    if (checkedIds.size === 0) {
      alert('Please select at least one student.');
      return;
    }
    addLog(`Initiating scorecard compilation for ${checkedIds.size} students...`);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const targetCodes = students
        .filter(s => checkedIds.has(s.id))
        .map(s => s.studentCode || s.rollNumber)
        .filter(Boolean);

      const res = await fetch('/api/admin/integrity', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ studentCodes: targetCodes })
      });
      if (!res.ok) throw new Error('Generation failed.');
      addLog(`✅ Successfully compiled scorecards for ${checkedIds.size} students.`);
      setCheckedIds(new Set());
      await fetchStatsAndStudents();
      if (selectedStudent) {
        await handleSelectStudent(selectedStudent);
      }
    } catch (err: any) {
      addLog(`❌ Batch generation error: ${err.message}`);
    }
  };

  const handleResetWeek = async () => {
    if (!selectedStudent || processingOverride) return;
    setProcessingOverride(true);
    addLog(`Overriding week ${resetWeek} score for ${selectedStudent.name}...`);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/integrity', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'resetWeek',
          studentCode: selectedStudent.studentCode || selectedStudent.rollNumber,
          week: resetWeek,
          year: resetYear,
          reason: resetReason
        })
      });
      if (!res.ok) throw new Error('Override failed.');
      addLog(`✅ Integrity overridden for week ${resetWeek}.`);
      setResetReason('');
      await handleSelectStudent(selectedStudent);
      await fetchStatsAndStudents();
    } catch (err: any) {
      addLog(`❌ Override error: ${err.message}`);
    } finally {
      setProcessingOverride(false);
    }
  };

  const handleResetAll = async () => {
    if (!selectedStudent) return;
    if (!confirm(`Purge all integrity metrics for ${selectedStudent.name}? This resets their records.`)) return;

    addLog(`Purging all scorecard records for ${selectedStudent.name}...`);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/integrity', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'resetAll',
          studentCode: selectedStudent.studentCode || selectedStudent.rollNumber
        })
      });
      if (!res.ok) throw new Error('Purge failed.');
      addLog(`✅ Successfully purged scorecards for ${selectedStudent.name}.`);
      await handleSelectStudent(selectedStudent);
      await fetchStatsAndStudents();
    } catch (err: any) {
      addLog(`❌ Purge error: ${err.message}`);
    }
  };

  const uniqueClasses = Array.from(new Set(students.map(s => s.class).filter(Boolean)));

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading proctor logs...
        </div>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800, cursor: 'pointer' }} onClick={() => router.push('/admin')}>YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Integrity Score Manager</h1>
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Proctor violation logging and score card aggregators</div>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          
          <button className="btn btn-primary" style={{ padding: '6px 12px', fontSize: '12px' }} onClick={() => setPdfSelectorOpen(true)}>📄 Export PDF</button>
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      {/* Main Container */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1000px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>
        
        {/* Statistics summary */}
        <div id="integrity-stats-section" className="stats-row" style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px' }}>
          <div className="card card-stat" style={{ textAlign: 'center', padding: '16px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)' }}>
            <div className="stat-number" style={{ fontSize: '20px', fontWeight: 800 }}>{stats.totalScores}</div>
            <div className="stat-label" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Weekly Scores</div>
          </div>
          <div className="card card-stat" style={{ textAlign: 'center', padding: '16px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)' }}>
            <div className="stat-number" style={{ fontSize: '20px', fontWeight: 800, color: 'var(--danger)' }}>{stats.reviewCount}</div>
            <div className="stat-label" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Need Review</div>
          </div>
          <div className="card card-stat" style={{ textAlign: 'center', padding: '16px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)' }}>
            <div className="stat-number" style={{ fontSize: '20px', fontWeight: 800, color: 'var(--success)' }}>{stats.avgScore}%</div>
            <div className="stat-label" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Avg Classroom Score</div>
          </div>
        </div>

        {/* Workspace Columns */}
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '16px', alignItems: 'start' }}>
          
          {/* Left: Students Check Roster */}
          <div id="integrity-roster-section" className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
            <h3 style={{ fontSize: '12px', fontWeight: 800, margin: '0 0 10px' }}>👥 Student Roster</h3>
            
            <div style={{ display: 'flex', gap: '6px', marginBottom: '10px' }}>
              <input 
                type="text" 
                className="form-input" 
                placeholder="🔍 Search name..." 
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                style={{ fontSize: '11px', padding: '5px 8px' }}
              />
              <select 
                className="form-input" 
                value={selectedClass} 
                onChange={(e) => setSelectedClass(e.target.value)}
                style={{ fontSize: '11px', padding: '5px 8px', width: '90px' }}
              >
                <option value="all">Class</option>
                {uniqueClasses.map(c => <option key={c} value={c}>{c}</option>)}
              </select>
            </div>

            <div style={{ maxHeight: '300px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: '4px' }}>
              <table style={{ width: '100%', fontSize: '11px', textAlign: 'left', borderCollapse: 'collapse' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                    <th style={{ padding: '6px 10px', width: '30px' }}>
                      <input 
                        type="checkbox" 
                        checked={checkedIds.size === filteredStudents.length && filteredStudents.length > 0} 
                        onChange={handleToggleSelectAll} 
                      />
                    </th>
                    <th style={{ padding: '6px 10px', cursor: 'pointer', userSelect: 'none' }} onClick={() => handleSort('name')}>
                      Student {sortField === 'name' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th style={{ padding: '6px 10px', width: '50px', cursor: 'pointer', userSelect: 'none' }} onClick={() => handleSort('class')}>
                      Class {sortField === 'class' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {sortedFilteredStudents.map(s => (
                    <tr key={s.id} style={{ borderBottom: '1px solid var(--border-light)', cursor: 'pointer' }} onClick={() => handleSelectStudent(s)}>
                      <td style={{ padding: '8px 10px' }} onClick={(e) => e.stopPropagation()}>
                        <input 
                          type="checkbox" 
                          checked={checkedIds.has(s.id)} 
                          onChange={() => handleToggleCheck(s.id)} 
                        />
                      </td>
                      <td style={{ padding: '8px 10px', fontWeight: selectedStudent?.id === s.id ? 700 : 500, color: selectedStudent?.id === s.id ? 'var(--accent)' : 'inherit' }}>
                        {s.name}
                      </td>
                      <td style={{ padding: '8px 10px' }}>{s.class || '—'}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <button 
              className="btn btn-primary" 
              onClick={handleGenerateBatch}
              style={{ width: '100%', padding: '10px', fontSize: '11px', marginTop: '12px' }}
            >
              ⚙️ Generate Selected ({checkedIds.size})
            </button>
          </div>

          {/* Right: Scores aggregator details */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {selectedStudent ? (
              <div id="integrity-history-section" className="card" style={{ background: 'var(--surface)', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
                <h3 style={{ borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '15px', fontSize: '14px', fontWeight: 800 }}>
                  👤 Student: {selectedStudent.name}
                </h3>

                {loadingHistory ? (
                  <div style={{ textAlign: 'center', padding: '20px' }}>Loading score history...</div>
                ) : (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                    {/* Scorecards History Table */}
                    <div>
                      <h4 style={{ fontSize: '12px', fontWeight: 700, marginBottom: '6px' }}>📊 Score history cards</h4>
                      <div style={{ overflowX: 'auto', border: '1px solid var(--border-light)', borderRadius: '4px' }}>
                        <table style={{ width: '100%', fontSize: '11px', textAlign: 'left', borderCollapse: 'collapse' }}>
                          <thead>
                            <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                              <th onClick={() => handleHistSort('week')} style={{ padding: '8px 12px', cursor: 'pointer', userSelect: 'none' }}>
                                Week {histSortField === 'week' ? (histSortDir === 'asc' ? '▲' : '▼') : '⇅'}
                              </th>
                              <th onClick={() => handleHistSort('year')} style={{ padding: '8px 12px', cursor: 'pointer', userSelect: 'none' }}>
                                Year {histSortField === 'year' ? (histSortDir === 'asc' ? '▲' : '▼') : '⇅'}
                              </th>
                              <th onClick={() => handleHistSort('score')} style={{ padding: '8px 12px', cursor: 'pointer', userSelect: 'none' }}>
                                Score {histSortField === 'score' ? (histSortDir === 'asc' ? '▲' : '▼') : '⇅'}
                              </th>
                              <th style={{ padding: '8px 12px' }}>Status</th>
                              <th onClick={() => handleHistSort('totalSessions')} style={{ padding: '8px 12px', cursor: 'pointer', userSelect: 'none' }}>
                                Sessions {histSortField === 'totalSessions' ? (histSortDir === 'asc' ? '▲' : '▼') : '⇅'}
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            {sortedHistory.length === 0 ? (
                              <tr>
                                <td colSpan={5} style={{ padding: '20px', textAlign: 'center', color: 'var(--text-muted)' }}>No integrity scores calculated for this student.</td>
                              </tr>
                            ) : (
                              sortedHistory.map(h => (
                                <tr key={h.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                                  <td style={{ padding: '8px 12px' }}>W{h.week}</td>
                                  <td style={{ padding: '8px 12px' }}>{h.year}</td>
                                  <td style={{ padding: '8px 12px', fontWeight: 700 }}>{h.score}%</td>
                                  <td style={{ padding: '8px 12px' }}>
                                    <span style={{
                                      fontSize: '9px',
                                      padding: '2px 6px',
                                      borderRadius: '4px',
                                      background: h.score >= 75 ? '#dbf3e1' : (h.score >= 60 ? '#fef3c7' : '#fee2e2'),
                                      color: h.score >= 75 ? '#1aa54e' : (h.score >= 60 ? '#d97706' : '#dc2626'),
                                      fontWeight: 700
                                    }}>{h.level.toUpperCase()}</span>
                                  </td>
                                  <td style={{ padding: '8px 12px' }}>{h.totalSessions}</td>
                                </tr>
                              ))
                            )}
                          </tbody>
                        </table>
                      </div>
                    </div>

                    {/* Reset Panels */}
                    <div style={{ background: '#fef2f2', border: '1px solid #fee2e2', borderRadius: 'var(--radius)', padding: '15px' }}>
                      <h4 style={{ fontSize: '11px', fontWeight: 800, color: 'var(--danger)', margin: '0 0 10px' }}>⚠️ Integrity Score Overrides</h4>
                      
                      <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                        <input 
                          type="number" 
                          className="form-input" 
                          placeholder="Week" 
                          min={1} 
                          max={53} 
                          value={resetWeek} 
                          onChange={(e) => {
                            const raw = e.target.value;
                            setResetWeek(raw === '' ? '' : parseInt(raw, 10) || '');
                          }}
                          onBlur={() => {
                            if (!resetWeek || Number(resetWeek) < 1) setResetWeek(1);
                          }}
                          style={{ width: '70px', fontSize: '11px', padding: '6px' }}
                        />
                        <input 
                          type="number" 
                          className="form-input" 
                          placeholder="Year" 
                          value={resetYear} 
                          onChange={(e) => {
                            const raw = e.target.value;
                            setResetYear(raw === '' ? '' : parseInt(raw, 10) || '');
                          }}
                          onBlur={() => {
                            if (!resetYear || Number(resetYear) < 2020) setResetYear(new Date().getFullYear());
                          }}
                          style={{ width: '80px', fontSize: '11px', padding: '6px' }}
                        />
                        <input 
                          type="text" 
                          className="form-input" 
                          placeholder="Reason..." 
                          value={resetReason} 
                          onChange={(e) => setResetReason(e.target.value)}
                          style={{ flex: 1, minWidth: '120px', fontSize: '11px', padding: '6px' }}
                        />
                        <button 
                          className="btn btn-primary" 
                          onClick={handleResetWeek} 
                          disabled={processingOverride}
                          style={{ fontSize: '11px', padding: '6px 12px', background: 'var(--warning)', border: 'none' }}
                        >
                          Override Week
                        </button>
                      </div>

                      <button 
                        className="btn btn-danger" 
                        onClick={handleResetAll}
                        style={{ width: '100%', fontSize: '11px', padding: '8px', marginTop: '12px' }}
                      >
                        Reset ALL Weeks Scorecards
                      </button>
                    </div>

                  </div>
                )}
              </div>
            ) : (
              <div className="card" style={{ padding: '50px 20px', textAlign: 'center', color: 'var(--text-muted)', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)' }}>
                👉 Select a student from the left side panel to review integrity score sheets.
              </div>
            )}

            {/* Operations Console Log */}
            <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px', marginBottom: '8px' }}>
                <span style={{ fontSize: '11px', fontWeight: 800 }}>💻 Operations Console Log</span>
                <button className="btn btn-secondary btn-sm" style={{ padding: '2px 6px', fontSize: '9px' }} onClick={() => setLogs(['[System] Log cleared.'])}>Clear</button>
              </div>
              <div style={{
                background: 'black',
                color: '#00ff00',
                padding: '10px',
                fontFamily: 'monospace',
                fontSize: '10px',
                borderRadius: '4px',
                maxHeight: '130px',
                overflowY: 'auto',
                lineHeight: 1.4
              }}>
                {logs.map((log, idx) => <div key={idx}>{log}</div>)}
              </div>
            </div>

          </div>

        </div>

      </main>
      <ExportPdfModal
        isOpen={pdfSelectorOpen}
        onClose={() => setPdfSelectorOpen(false)}
        title="Classroom Integrity Performance Audit Report"
        filename="Integrity_Classroom_Audit.pdf"
        sections={[
          { id: 'stats', name: 'Integrity Statistics Summary', elementId: 'integrity-stats-section' },
          { id: 'roster', name: 'Student Accounts Roster', elementId: 'integrity-roster-section' },
          ...(selectedStudent ? [{ id: 'history', name: `Weekly Score Sheet: ${selectedStudent.name}`, elementId: 'integrity-history-section' }] : [])
        ]}
      />
    </div>
  );
}
