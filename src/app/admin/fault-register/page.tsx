'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import { getDateKeyIST, formatDateDMY } from '@/lib/dateUtils';
import { useAdminBatches } from '@/hooks/useAdminReferenceData';
import DateInputDMY from '@/components/DateInputDMY';
import { FaultCategory, StudentFaultEntry } from '@/services/fault.service';

export default function AdminFaultRegisterPage() {
  const { user, firebaseUser, loading: authLoading } = useAuth();
  const router = useRouter();

  const [date, setDate] = useState<string>(() => getDateKeyIST());
  const [selectedBatchId, setSelectedBatchId] = useState<string>('all');
  const [batches, setBatches] = useState<Array<{ id: string; name: string }>>([]);
  const [searchTerm, setSearchTerm] = useState<string>('');

  const [categories, setCategories] = useState<FaultCategory[]>([]);
  const [students, setStudents] = useState<StudentFaultEntry[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [saveStatus, setSaveStatus] = useState<'idle' | 'saving' | 'saved' | 'error'>('idle');
  const [lastSavedTime, setLastSavedTime] = useState<string | null>(null);

  // Client crash reports telemetry tab
  const [activeRegisterTab, setActiveRegisterTab] = useState<'discipline' | 'crashes'>('discipline');
  // View mode within discipline: 'quick' (Fast Pill Logger) vs 'matrix' (Full Table Matrix)
  const [disciplineViewMode, setDisciplineViewMode] = useState<'quick' | 'matrix'>('quick');
  const [selectedFaultId, setSelectedFaultId] = useState<string>('no_homework');
  const [clientCrashes, setClientCrashes] = useState<any[]>([]);
  const [loadingCrashes, setLoadingCrashes] = useState<boolean>(false);

  const fetchClientCrashes = useCallback(async () => {
    if (!firebaseUser) return;
    try {
      setLoadingCrashes(true);
      const token = await firebaseUser.getIdToken();
      const res = await fetch('/api/system/client-error?limit=50', {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setClientCrashes(data.faults || []);
      }
    } catch (e) {
      console.error('Failed to load client crashes:', e);
    } finally {
      setLoadingCrashes(false);
    }
  }, [firebaseUser]);

  useEffect(() => {
    if (activeRegisterTab === 'crashes') {
      fetchClientCrashes();
    }
  }, [activeRegisterTab, fetchClientCrashes]);

  // Auto-save debounce and queue refs
  const pendingSavesRef = React.useRef<Map<string, { faults: Record<string, boolean>; notes: Record<string, string> }>>(new Map());
  const debounceTimerRef = React.useRef<NodeJS.Timeout | null>(null);
  const dateRef = React.useRef<string>(date);
  dateRef.current = date;

  // Flush pending auto-saves
  const flushPendingSaves = useCallback(async () => {
    if (debounceTimerRef.current) {
      clearTimeout(debounceTimerRef.current);
      debounceTimerRef.current = null;
    }
    if (pendingSavesRef.current.size === 0 || !firebaseUser) return;

    const entries = Array.from(pendingSavesRef.current.entries()).map(([sCode, data]) => {
      const student = students.find(s => s.studentCode === sCode);
      return {
        date: dateRef.current,
        studentCode: sCode,
        studentName: student?.studentName || '',
        batchId: student?.batchId || '',
        faults: data.faults,
        notes: data.notes
      };
    });

    pendingSavesRef.current.clear();
    setSaveStatus('saving');

    try {
      const token = await firebaseUser.getIdToken();
      const payload = entries.length === 1 ? entries[0] : { bulk: entries };
      const res = await fetch('/api/admin/fault-register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify(payload)
      });

      if (res.ok) {
        setSaveStatus('saved');
        const timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
        setLastSavedTime(timeStr);
      } else {
        setSaveStatus('error');
      }
    } catch (err) {
      console.error('Auto-save error:', err);
      setSaveStatus('error');
    }
  }, [firebaseUser]);

  // Queue a student for auto-saving
  const queueAutoSave = useCallback((studentCode: string, faults: Record<string, boolean>, notes: Record<string, string>, immediate: boolean = false) => {
    pendingSavesRef.current.set(studentCode, { faults, notes });
    setSaveStatus('saving');

    if (debounceTimerRef.current) {
      clearTimeout(debounceTimerRef.current);
    }

    if (immediate) {
      flushPendingSaves();
    } else {
      debounceTimerRef.current = setTimeout(() => {
        flushPendingSaves();
      }, 350);
    }
  }, [flushPendingSaves]);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (pendingSavesRef.current.size > 0) {
        flushPendingSaves();
      }
    };
  }, [flushPendingSaves]);

  // Category Manager Modal
  const [categoryModalOpen, setCategoryModalOpen] = useState<boolean>(false);
  const [newCatName, setNewCatName] = useState<string>('');
  const [newCatTarget, setNewCatTarget] = useState<'student' | 'parent' | 'shared'>('student');
  const [newCatCategory, setNewCatCategory] = useState<string>('academic');
  const [newCatIcon, setNewCatIcon] = useState<string>('📌');

  // Student Timeline Detail Drawer
  const [selectedStudent, setSelectedStudent] = useState<StudentFaultEntry | null>(null);
  const [studentTimeline, setStudentTimeline] = useState<any>(null);
  const [loadingTimeline, setLoadingTimeline] = useState<boolean>(false);

  // Note Modal
  const [activeNoteStudent, setActiveNoteStudent] = useState<string | null>(null);
  const [activeNoteCatId, setActiveNoteCatId] = useState<string | null>(null);
  const [tempNoteText, setTempNoteText] = useState<string>('');

  // 1. Shared SWR Batches
  const { batches: swrBatches } = useAdminBatches();

  useEffect(() => {
    if (swrBatches && swrBatches.length > 0) {
      setBatches(swrBatches);
    }
  }, [swrBatches]);

  // 2. Fetch Matrix Data
  const loadMatrix = useCallback(async () => {
    if (!firebaseUser) return;
    // Flush any pending saves before reloading matrix
    if (pendingSavesRef.current.size > 0) {
      await flushPendingSaves();
    }
    setLoading(true);
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/fault-register?date=${date}&batchId=${selectedBatchId}`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setCategories(data.categories || []);
        setStudents(data.students || []);
        setSaveStatus('idle');
      }
    } catch (err) {
      console.error('Failed to load fault register matrix:', err);
    } finally {
      setLoading(false);
    }
  }, [firebaseUser, date, selectedBatchId, flushPendingSaves]);

  useEffect(() => {
    if (user && user.role === 'admin') {
      loadMatrix();
    }
  }, [user, loadMatrix]);

  // Toggle fault checkbox with real-time auto-save
  const handleToggleFault = (studentCode: string, catId: string) => {
    setStudents(prev => {
      let targetStudent: StudentFaultEntry | undefined;
      const updated = prev.map(s => {
        if (s.studentCode === studentCode) {
          const currentVal = !!s.faults[catId];
          const updatedFaults = {
            ...s.faults,
            [catId]: !currentVal
          };
          targetStudent = {
            ...s,
            faults: updatedFaults
          };
          return targetStudent;
        }
        return s;
      });

      if (targetStudent) {
        queueAutoSave(targetStudent.studentCode, targetStudent.faults, targetStudent.notes);
      }
      return updated;
    });
  };

  // Open note modal
  const openNoteModal = (studentCode: string, catId: string) => {
    const student = students.find(s => s.studentCode === studentCode);
    const existing = student?.notes?.[catId] || '';
    setActiveNoteStudent(studentCode);
    setActiveNoteCatId(catId);
    setTempNoteText(existing);
  };

  const saveNote = () => {
    if (!activeNoteStudent || !activeNoteCatId) return;
    const noteText = tempNoteText.trim();
    setStudents(prev => {
      let targetStudent: StudentFaultEntry | undefined;
      const updated = prev.map(s => {
        if (s.studentCode === activeNoteStudent) {
          const updatedNotes = {
            ...s.notes,
            [activeNoteCatId]: noteText
          };
          targetStudent = {
            ...s,
            notes: updatedNotes
          };
          return targetStudent;
        }
        return s;
      });

      if (targetStudent) {
        queueAutoSave(targetStudent.studentCode, targetStudent.faults, targetStudent.notes, true);
      }
      return updated;
    });
    setActiveNoteStudent(null);
    setActiveNoteCatId(null);
  };

  // Add custom category
  const handleAddCategory = async () => {
    if (!newCatName.trim() || !firebaseUser) return;
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/fault-register/categories', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
          name: newCatName.trim(),
          target: newCatTarget,
          category: newCatCategory,
          icon: newCatIcon || '📌'
        })
      });
      if (res.ok) {
        const data = await res.json();
        setCategories(data.categories || []);
        setNewCatName('');
        setCategoryModalOpen(false);
        loadMatrix();
      }
    } catch (err: any) {
      alert('Failed to add category: ' + err.message);
    }
  };

  // Delete category
  const handleDeleteCategory = async (catId: string) => {
    if (!confirm('Are you sure you want to remove this fault type?') || !firebaseUser) return;
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/fault-register/categories?id=${catId}`, {
        method: 'DELETE',
        headers: { Authorization: `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setCategories(data.categories || []);
        loadMatrix();
      }
    } catch (err: any) {
      alert('Failed to delete category: ' + err.message);
    }
  };

  // Filter students
  const filteredStudents = students.filter(s => {
    if (!searchTerm.trim()) return true;
    const term = searchTerm.toLowerCase();
    return s.studentName.toLowerCase().includes(term) || s.studentCode.toLowerCase().includes(term);
  });

  if (authLoading || !user) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', background: 'var(--bg)' }}>
        <span>Loading Fault Register...</span>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', flex: 1, padding: '16px 12px' }}>
      <div style={{ maxWidth: '1440px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '14px' }}>

        {/* Header Bar */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px', background: 'var(--surface)', padding: '14px 18px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <h2 style={{ margin: 0, fontSize: '18px', fontWeight: 800, color: 'var(--text)' }}>
                📋 Fault & Accountability Register
              </h2>
              <span className="badge" style={{ background: 'var(--accent-soft)', color: 'var(--accent)', border: '1px solid var(--accent-ring)', fontSize: '10px', fontWeight: 700, padding: '2px 8px', borderRadius: '12px' }}>
                Date-Wise Matrix
              </span>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
            <button
              type="button"
              className="btn btn-secondary btn-sm"
              onClick={() => setCategoryModalOpen(true)}
              style={{ fontSize: '12px', padding: '6px 12px', display: 'flex', alignItems: 'center', gap: '6px' }}
            >
              ⚙️ Manage Fault Types
            </button>
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '7px',
                fontSize: '12px',
                fontWeight: 700,
                padding: '6px 14px',
                borderRadius: 'var(--radius-sm)',
                background: saveStatus === 'saving'
                  ? 'var(--accent-soft)'
                  : saveStatus === 'error'
                    ? 'rgba(239, 68, 68, 0.15)'
                    : saveStatus === 'saved'
                      ? 'rgba(34, 197, 94, 0.12)'
                      : 'var(--surface-2)',
                color: saveStatus === 'saving'
                  ? 'var(--accent)'
                  : saveStatus === 'error'
                    ? 'var(--danger)'
                    : saveStatus === 'saved'
                      ? 'var(--success)'
                      : 'var(--text-muted)',
                border: saveStatus === 'saving'
                  ? '1px solid var(--accent-ring)'
                  : saveStatus === 'error'
                    ? '1px solid var(--danger)'
                    : saveStatus === 'saved'
                      ? '1px solid rgba(34, 197, 94, 0.3)'
                      : '1px solid var(--border-light)'
              }}
            >
              {saveStatus === 'saving' ? (
                <>
                  <span
                    style={{
                      display: 'inline-block',
                      width: '11px',
                      height: '11px',
                      border: '2px solid var(--accent)',
                      borderTopColor: 'transparent',
                      borderRadius: '50%',
                      animation: 'spin 0.7s linear infinite'
                    }}
                  />
                  <span>Saving...</span>
                </>
              ) : saveStatus === 'error' ? (
                <>
                  <span>⚠️ Save Error</span>
                  <button
                    type="button"
                    onClick={() => flushPendingSaves()}
                    style={{
                      background: 'var(--danger)',
                      color: '#fff',
                      border: 'none',
                      borderRadius: '4px',
                      padding: '2px 7px',
                      fontSize: '10px',
                      cursor: 'pointer',
                      fontWeight: 700
                    }}
                  >
                    Retry
                  </button>
                </>
              ) : (
                <>
                  <span
                    style={{
                      width: '8px',
                      height: '8px',
                      borderRadius: '50%',
                      background: saveStatus === 'saved' ? 'var(--success)' : 'var(--text-muted)',
                      boxShadow: saveStatus === 'saved' ? '0 0 6px var(--success)' : 'none'
                    }}
                  />
                  <span>{lastSavedTime ? `Auto-saved (${lastSavedTime})` : '⚡ Auto-save Ready'}</span>
                </>
              )}
            </div>
          </div>
        </div>

        {/* Tab Switcher: Student Conduct vs Client Crashes */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px' }}>
          <div style={{ display: 'flex', gap: '8px' }}>
            <button
              type="button"
              onClick={() => setActiveRegisterTab('discipline')}
              style={{
                padding: '6px 14px',
                borderRadius: '6px',
                border: 'none',
                background: activeRegisterTab === 'discipline' ? 'var(--accent)' : 'var(--surface-2)',
                color: activeRegisterTab === 'discipline' ? '#fff' : 'var(--text-muted)',
                fontWeight: 700,
                fontSize: '12px',
                cursor: 'pointer'
              }}
            >
              📋 Student Fault Register
            </button>
            <button
              type="button"
              onClick={() => setActiveRegisterTab('crashes')}
              style={{
                padding: '6px 14px',
                borderRadius: '6px',
                border: 'none',
                background: activeRegisterTab === 'crashes' ? 'var(--danger)' : 'var(--surface-2)',
                color: activeRegisterTab === 'crashes' ? '#fff' : 'var(--text-muted)',
                fontWeight: 700,
                fontSize: '12px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '6px'
              }}
            >
              🚨 Client Crashes & Faults
              {clientCrashes.length > 0 && (
                <span style={{
                  background: 'rgba(255,255,255,0.25)',
                  color: '#fff',
                  fontSize: '10px',
                  padding: '1px 6px',
                  borderRadius: '10px'
                }}>
                  {clientCrashes.length}
                </span>
              )}
            </button>
          </div>

          {activeRegisterTab === 'discipline' && (
            <div style={{ display: 'flex', background: 'var(--surface-2)', padding: '3px', borderRadius: '8px', border: '1px solid var(--border-light)' }}>
              <button
                type="button"
                onClick={() => setDisciplineViewMode('quick')}
                style={{
                  padding: '4px 12px',
                  borderRadius: '6px',
                  border: 'none',
                  background: disciplineViewMode === 'quick' ? 'var(--surface)' : 'transparent',
                  color: disciplineViewMode === 'quick' ? 'var(--accent)' : 'var(--text-muted)',
                  fontWeight: disciplineViewMode === 'quick' ? 800 : 600,
                  fontSize: '12px',
                  cursor: 'pointer',
                  boxShadow: disciplineViewMode === 'quick' ? 'var(--shadow-sm)' : 'none',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '5px'
                }}
              >
                ⚡ Quick Fault Logger (Pills)
              </button>
              <button
                type="button"
                onClick={() => setDisciplineViewMode('matrix')}
                style={{
                  padding: '4px 12px',
                  borderRadius: '6px',
                  border: 'none',
                  background: disciplineViewMode === 'matrix' ? 'var(--surface)' : 'transparent',
                  color: disciplineViewMode === 'matrix' ? 'var(--accent)' : 'var(--text-muted)',
                  fontWeight: disciplineViewMode === 'matrix' ? 800 : 600,
                  fontSize: '12px',
                  cursor: 'pointer',
                  boxShadow: disciplineViewMode === 'matrix' ? 'var(--shadow-sm)' : 'none',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '5px'
                }}
              >
                📊 Full Conduct Matrix
              </button>
            </div>
          )}
        </div>

        {activeRegisterTab === 'crashes' ? (
          /* Real-Time Client Crash Log */
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '16px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px', flexWrap: 'wrap', gap: '10px' }}>
              <div>
                <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800, color: 'var(--text)' }}>
                  🚨 Real-Time Client Crash Log (`systemFaults`)
                </h3>
                <p style={{ margin: '2px 0 0', fontSize: '12px', color: 'var(--text-muted)' }}>
                  Captured by ExamErrorBoundary from student phones & browsers.
                </p>
              </div>
              <button
                type="button"
                className="btn btn-secondary btn-sm"
                onClick={fetchClientCrashes}
                disabled={loadingCrashes}
                style={{ fontSize: '11px', display: 'flex', alignItems: 'center', gap: '6px' }}
              >
                🔄 Refresh Logs
              </button>
            </div>

            {loadingCrashes ? (
              <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
                <div className="spinner" style={{ margin: '0 auto 10px' }}></div> Loading client crash logs...
              </div>
            ) : clientCrashes.length === 0 ? (
              <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--success)' }}>
                <div style={{ fontSize: '2rem', marginBottom: '8px' }}>✅</div>
                <strong>Zero client crashes reported!</strong>
                <p style={{ fontSize: '12px', color: 'var(--text-muted)', margin: '4px 0 0' }}>
                  No error boundary exceptions or runtime crashes have been reported from student devices.
                </p>
              </div>
            ) : (
              <div style={{ overflowX: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px', textAlign: 'left' }}>
                  <thead>
                    <tr style={{ background: 'var(--surface-light)', borderBottom: '2px solid var(--border-light)' }}>
                      <th style={{ padding: '8px 10px' }}>Time (IST)</th>
                      <th style={{ padding: '8px 10px' }}>Student</th>
                      <th style={{ padding: '8px 10px' }}>Exam ID</th>
                      <th style={{ padding: '8px 10px' }}>Error & Message</th>
                      <th style={{ padding: '8px 10px' }}>Device / URL</th>
                    </tr>
                  </thead>
                  <tbody>
                    {clientCrashes.map(crash => (
                      <tr key={crash.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '8px 10px', whiteSpace: 'nowrap', verticalAlign: 'top', color: 'var(--text-muted)' }}>
                          {crash.timestamp ? formatDateDMY(crash.timestamp) + ' ' + new Date(crash.timestamp).toLocaleTimeString('en-IN') : 'N/A'}
                        </td>
                        <td style={{ padding: '8px 10px', verticalAlign: 'top' }}>
                          <div style={{ fontWeight: 700, color: 'var(--text)' }}>
                            {crash.context?.studentName || crash.context?.studentCode || 'Anonymous'}
                          </div>
                          {crash.context?.studentCode && (
                            <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>{crash.context.studentCode}</span>
                          )}
                        </td>
                        <td style={{ padding: '8px 10px', verticalAlign: 'top', whiteSpace: 'nowrap' }}>
                          <span className="badge" style={{ fontSize: '10px' }}>{crash.context?.examId || 'General'}</span>
                        </td>
                        <td style={{ padding: '8px 10px', verticalAlign: 'top', maxWidth: '380px' }}>
                          <div style={{ fontWeight: 700, color: 'var(--danger)', wordBreak: 'break-word' }}>
                            {crash.message}
                          </div>
                          {(crash.stack || crash.componentStack) && (
                            <details style={{ marginTop: '4px', fontSize: '11px', color: 'var(--text-muted)' }}>
                              <summary style={{ cursor: 'pointer', color: 'var(--accent)' }}>View Stack Trace</summary>
                              <pre style={{ margin: '4px 0 0', padding: '6px', background: 'var(--bg)', borderRadius: '4px', fontSize: '10px', overflowX: 'auto', whiteSpace: 'pre-wrap', maxHeight: '160px' }}>
                                {crash.stack}
                                {crash.componentStack ? `\n\nComponent Stack:\n${crash.componentStack}` : ''}
                              </pre>
                            </details>
                          )}
                        </td>
                        <td style={{ padding: '8px 10px', verticalAlign: 'top', fontSize: '11px', color: 'var(--text-muted)', maxWidth: '240px', wordBreak: 'break-word' }}>
                          <div>{crash.url}</div>
                          <div style={{ fontSize: '10px', opacity: 0.7, marginTop: '2px' }}>{crash.userAgent?.slice(0, 80)}...</div>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        ) : (
          <>
            {/* Filters and Batch Bar */}
        <div style={{ display: 'flex', gap: '12px', alignItems: 'center', flexWrap: 'wrap', background: 'var(--surface-light)', padding: '10px 14px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <label style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)' }}>📅 Date:</label>
            <DateInputDMY
              value={date}
              onChange={(val) => setDate(val)}
              style={{ width: '130px' }}
              inputStyle={{ height: '30px', padding: '4px 26px 4px 8px', fontSize: '12px' }}
            />
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <label style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)' }}>🏫 Batch:</label>
            <select
              value={selectedBatchId}
              onChange={(e) => setSelectedBatchId(e.target.value)}
              style={{ padding: '4px 8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', height: '30px', minWidth: '160px' }}
            >
              <option value="all">All Batches</option>
              {batches.map(b => (
                <option key={b.id} value={b.id}>{b.name}</option>
              ))}
            </select>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flex: 1, minWidth: '200px' }}>
            <input
              type="text"
              placeholder="🔍 Search student name or code..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              style={{ width: '100%', padding: '4px 10px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', height: '30px' }}
            />
          </div>

          <button
            type="button"
            className="btn btn-secondary btn-sm"
            onClick={loadMatrix}
            disabled={loading}
            style={{ fontSize: '11px', height: '30px', padding: '0 10px' }}
          >
            🔄 Refresh
          </button>
        </div>

        {/* -------------------- QUICK FAULT LOGGER (PILL VIEW) -------------------- */}
        {disciplineViewMode === 'quick' ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
            {/* Step 1: Grouped Fault Categories */}
            <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '16px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                <div>
                  <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 800, color: 'var(--text)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                    1️⃣ Select Fault to Assign
                  </h4>
                  <p style={{ margin: '2px 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>
                    Pick a fault below, then tap students to immediately tag or untag them.
                  </p>
                </div>
              </div>

              {/* Group faults by category: Academic, Conduct, Punctuality/Absence, Review */}
              {(() => {
                const groupConfig: Record<string, { label: string; icon: string }> = {
                  academic: { label: 'Academic & Homework', icon: '📚' },
                  conduct: { label: 'Conduct & Classroom', icon: '🗣️' },
                  punctuality: { label: 'Attendance & Absence', icon: '⏰' },
                  review: { label: 'Exams & Reviews', icon: '⏱️' },
                  custom: { label: 'Custom & Other', icon: '📌' },
                };

                const groupedCats: Record<string, FaultCategory[]> = {};
                categories.forEach(cat => {
                  const grp = cat.category || 'custom';
                  if (!groupedCats[grp]) groupedCats[grp] = [];
                  groupedCats[grp].push(cat);
                });

                // Set effective selected category if not set
                const activeCatId = categories.some(c => c.id === selectedFaultId)
                  ? selectedFaultId
                  : (categories[0]?.id || '');

                return (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                    {Object.entries(groupedCats).map(([grpKey, grpCats]) => {
                      const cfg = groupConfig[grpKey] || { label: grpKey, icon: '📌' };
                      return (
                        <div key={grpKey} style={{ background: 'var(--surface-light)', borderRadius: '8px', padding: '10px 12px', border: '1px solid var(--border-light)' }}>
                          <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '5px' }}>
                            <span>{cfg.icon}</span>
                            <span>{cfg.label}</span>
                          </div>
                          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
                            {grpCats.map(cat => {
                              const isSelected = cat.id === activeCatId;
                              // Count how many students currently have this fault
                              const taggedCount = students.filter(s => !!s.faults[cat.id]).length;

                              return (
                                <button
                                  key={cat.id}
                                  type="button"
                                  onClick={() => setSelectedFaultId(cat.id)}
                                  style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    gap: '7px',
                                    padding: '7px 12px',
                                    borderRadius: '20px',
                                    border: isSelected ? '2px solid var(--accent)' : '1px solid var(--border-light)',
                                    background: isSelected ? 'var(--accent-soft)' : 'var(--surface)',
                                    color: isSelected ? 'var(--accent)' : 'var(--text)',
                                    fontWeight: isSelected ? 800 : 600,
                                    fontSize: '12px',
                                    cursor: 'pointer',
                                    boxShadow: isSelected ? '0 0 0 1px var(--accent-ring)' : 'none',
                                    transition: 'all 0.15s ease'
                                  }}
                                >
                                  <span>{cat.icon || '📌'}</span>
                                  <span>{cat.name}</span>
                                  <span
                                    style={{
                                      fontSize: '10px',
                                      fontWeight: 800,
                                      padding: '1px 6px',
                                      borderRadius: '10px',
                                      background: taggedCount > 0
                                        ? (isSelected ? 'var(--accent)' : 'var(--danger-bg)')
                                        : 'var(--surface-2)',
                                      color: taggedCount > 0
                                        ? (isSelected ? '#fff' : 'var(--danger)')
                                        : 'var(--text-muted)',
                                      border: taggedCount > 0 && !isSelected ? '1px solid rgba(239, 68, 68, 0.25)' : 'none'
                                    }}
                                  >
                                    {taggedCount}
                                  </span>
                                </button>
                              );
                            })}
                          </div>
                        </div>
                      );
                    })}
                  </div>
                );
              })()}
            </div>

            {/* Step 2: Interactive Student Pill Cloud */}
            {(() => {
              const activeCat = categories.find(c => c.id === selectedFaultId) || categories[0];
              if (!activeCat) return null;
              const taggedStudents = filteredStudents.filter(s => !!s.faults[activeCat.id]);

              return (
                <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '16px' }}>
                  {/* Action Banner */}
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px', paddingBottom: '12px', borderBottom: '1px solid var(--border-light)', marginBottom: '14px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                      <div style={{ fontSize: '24px', background: 'var(--accent-soft)', width: '42px', height: '42px', borderRadius: '10px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                        {activeCat.icon || '📌'}
                      </div>
                      <div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 800, color: 'var(--text)' }}>
                            {activeCat.name}
                          </h4>
                          <span style={{ fontSize: '10px', color: activeCat.target === 'parent' ? 'var(--warning)' : 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 700, background: 'var(--surface-2)', padding: '2px 6px', borderRadius: '4px' }}>
                            Target: {activeCat.target}
                          </span>
                        </div>
                        <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>
                          <strong>{taggedStudents.length}</strong> of {filteredStudents.length} students tagged for {formatDateDMY(date)}
                        </div>
                      </div>
                    </div>

                    {/* Quick batch select / clear for this fault */}
                    <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                      {taggedStudents.length > 0 && (
                        <button
                          type="button"
                          className="btn btn-secondary btn-sm"
                          onClick={() => {
                            if (!confirm(`Clear '${activeCat.name}' for all ${taggedStudents.length} tagged students?`)) return;
                            taggedStudents.forEach(s => {
                              handleToggleFault(s.studentCode, activeCat.id);
                            });
                          }}
                          style={{ fontSize: '11px', padding: '4px 10px', color: 'var(--danger)' }}
                        >
                          ✕ Clear All Tagged ({taggedStudents.length})
                        </button>
                      )}
                    </div>
                  </div>

                  {loading ? (
                    <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
                      <div className="spinner" style={{ margin: '0 auto 10px' }}></div> Loading student roster...
                    </div>
                  ) : filteredStudents.length === 0 ? (
                    <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)', fontSize: '13px' }}>
                      No active students found matching the batch/search filter.
                    </div>
                  ) : (
                    <div>
                      {/* Active Tagged Section (if any) */}
                      {taggedStudents.length > 0 && (
                        <div style={{ marginBottom: '16px' }}>
                          <div style={{ fontSize: '11px', fontWeight: 800, color: 'var(--danger)', textTransform: 'uppercase', letterSpacing: '0.5px', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                            <span>🚨 Tagged Students ({taggedStudents.length})</span>
                            <span style={{ fontSize: '10px', color: 'var(--text-muted)', fontWeight: 500, textTransform: 'none' }}>— Click pill to untag</span>
                          </div>
                          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
                            {taggedStudents.map(s => {
                              const isAuto = !!s.autoSuggested?.[activeCat.id];
                              const note = s.notes?.[activeCat.id] || '';
                              return (
                                <div
                                  key={s.studentCode}
                                  style={{
                                    display: 'inline-flex',
                                    alignItems: 'center',
                                    gap: '6px',
                                    background: 'rgba(239, 68, 68, 0.12)',
                                    border: '1px solid rgba(239, 68, 68, 0.35)',
                                    borderRadius: '24px',
                                    padding: '5px 10px 5px 12px',
                                    boxShadow: 'var(--shadow-xs)'
                                  }}
                                >
                                  <button
                                    type="button"
                                    onClick={() => handleToggleFault(s.studentCode, activeCat.id)}
                                    style={{
                                      background: 'none',
                                      border: 'none',
                                      padding: 0,
                                      cursor: 'pointer',
                                      display: 'flex',
                                      alignItems: 'center',
                                      gap: '6px',
                                      color: 'var(--danger)',
                                      fontWeight: 800,
                                      fontSize: '12px'
                                    }}
                                    title="Click to remove fault"
                                  >
                                    <span>✓</span>
                                    <span>{s.studentName}</span>
                                    <span style={{ fontSize: '10px', fontWeight: 600, opacity: 0.8, color: 'var(--text-muted)' }}>
                                      ({s.classNum ? `Cl ${s.classNum}` : s.batchName})
                                    </span>
                                  </button>

                                  {isAuto && (
                                    <span style={{ fontSize: '9px', fontWeight: 800, background: 'var(--warning-soft)', color: 'var(--warning)', padding: '1px 5px', borderRadius: '8px' }} title={note}>
                                      ⚡ Auto
                                    </span>
                                  )}

                                  <button
                                    type="button"
                                    onClick={(e) => {
                                      e.stopPropagation();
                                      openNoteModal(s.studentCode, activeCat.id);
                                    }}
                                    style={{
                                      border: 'none',
                                      background: note ? 'var(--accent)' : 'rgba(0,0,0,0.06)',
                                      color: note ? '#fff' : 'var(--text-muted)',
                                      borderRadius: '12px',
                                      padding: '2px 6px',
                                      fontSize: '10px',
                                      fontWeight: 700,
                                      cursor: 'pointer'
                                    }}
                                    title={note || 'Add specific note'}
                                  >
                                    {note ? '📝' : '+📝'}
                                  </button>
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      )}

                      {/* Untagged Students Cloud */}
                      <div>
                        <div style={{ fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.5px', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                          <span>👥 Untagged Students ({filteredStudents.length - taggedStudents.length})</span>
                          <span style={{ fontSize: '10px', color: 'var(--text-muted)', fontWeight: 500, textTransform: 'none' }}>— Click to tag with '{activeCat.name}'</span>
                        </div>
                        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
                          {filteredStudents
                            .filter(s => !s.faults[activeCat.id])
                            .map(s => (
                              <button
                                key={s.studentCode}
                                type="button"
                                onClick={() => handleToggleFault(s.studentCode, activeCat.id)}
                                style={{
                                  display: 'inline-flex',
                                  alignItems: 'center',
                                  gap: '6px',
                                  background: 'var(--surface-light)',
                                  border: '1px solid var(--border-light)',
                                  borderRadius: '24px',
                                  padding: '5px 12px',
                                  fontSize: '12px',
                                  fontWeight: 600,
                                  color: 'var(--text)',
                                  cursor: 'pointer',
                                  transition: 'all 0.12s ease'
                                }}
                                onMouseEnter={(e) => {
                                  e.currentTarget.style.borderColor = 'var(--accent)';
                                  e.currentTarget.style.background = 'var(--accent-soft)';
                                  e.currentTarget.style.color = 'var(--accent)';
                                }}
                                onMouseLeave={(e) => {
                                  e.currentTarget.style.borderColor = 'var(--border-light)';
                                  e.currentTarget.style.background = 'var(--surface-light)';
                                  e.currentTarget.style.color = 'var(--text)';
                                }}
                              >
                                <span style={{ opacity: 0.5, fontSize: '13px' }}>+</span>
                                <span>{s.studentName}</span>
                                <span style={{ fontSize: '10px', opacity: 0.6, color: 'var(--text-muted)' }}>
                                  ({s.classNum ? `Cl ${s.classNum}` : s.batchName})
                                </span>
                              </button>
                            ))}
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              );
            })()}
          </div>
        ) : (
          /* -------------------- FULL CONDUCT MATRIX VIEW -------------------- */
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '0', overflow: 'hidden' }}>
            {loading ? (
              <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
                <div className="spinner" style={{ margin: '0 auto 10px' }}></div> Loading fault register matrix for {date}...
              </div>
            ) : filteredStudents.length === 0 ? (
              <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)', fontSize: '13px' }}>
                No active students found for the selected batch.
              </div>
            ) : (
              <div style={{ overflowX: 'auto', maxHeight: '72vh' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px', textAlign: 'left' }}>
                  <thead style={{ position: 'sticky', top: 0, background: 'var(--surface-light)', zIndex: 10, borderBottom: '2px solid var(--border-light)' }}>
                    <tr>
                      <th style={{ padding: '10px 12px', width: '220px', minWidth: '180px', position: 'sticky', left: 0, background: 'var(--surface-light)', zIndex: 11 }}>
                        Student Name
                      </th>
                      {categories.map(cat => (
                        <th
                          key={cat.id}
                          style={{
                            padding: '8px 10px',
                            textAlign: 'center',
                            minWidth: '110px',
                            borderLeft: '1px solid var(--border-light)',
                            verticalAlign: 'bottom'
                          }}
                        >
                          <div style={{ fontSize: '15px', marginBottom: '2px' }}>{cat.icon || '📌'}</div>
                          <div style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text)', whiteSpace: 'normal', lineHeight: '1.2' }}>
                            {cat.name}
                          </div>
                          <span style={{ fontSize: '8px', color: cat.target === 'parent' ? 'var(--warning)' : 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600 }}>
                            [{cat.target}]
                          </span>
                        </th>
                      ))}
                      <th style={{ padding: '10px 12px', textAlign: 'center', width: '70px', borderLeft: '1px solid var(--border-light)' }}>
                        Faults
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    {filteredStudents.map((s, idx) => {
                      const activeCount = Object.values(s.faults).filter(Boolean).length;
                      return (
                        <tr
                          key={s.studentCode}
                          style={{
                            borderBottom: '1px solid var(--border-light)',
                            background: idx % 2 === 0 ? 'var(--surface)' : 'var(--surface-light)',
                            transition: 'background 0.15s'
                          }}
                        >
                          {/* Student Name Cell */}
                          <td
                            style={{
                              padding: '10px 12px',
                              position: 'sticky',
                              left: 0,
                              background: idx % 2 === 0 ? 'var(--surface)' : 'var(--surface-light)',
                              zIndex: 5,
                              borderRight: '1px solid var(--border-light)'
                            }}
                          >
                            <div style={{ fontWeight: 700, color: 'var(--text)' }}>
                              {s.studentName}
                            </div>
                            <div style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'flex', gap: '6px', alignItems: 'center' }}>
                              <span>{s.classNum ? `Class ${s.classNum}` : s.batchName}</span>
                              {s.parentPhone && <span>• 📞 {s.parentPhone}</span>}
                            </div>
                          </td>

                          {/* Checkbox Cells */}
                          {categories.map(cat => {
                            const isChecked = !!s.faults[cat.id];
                            const isAuto = !!s.autoSuggested?.[cat.id];
                            const note = s.notes?.[cat.id] || '';

                            return (
                              <td
                                key={cat.id}
                                style={{
                                  padding: '6px 8px',
                                  textAlign: 'center',
                                  borderLeft: '1px solid var(--border-light)',
                                  background: isChecked
                                    ? 'rgba(239, 68, 68, 0.08)'
                                    : 'transparent'
                                }}
                              >
                                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '3px' }}>
                                  <input
                                    type="checkbox"
                                    checked={isChecked}
                                    onChange={() => handleToggleFault(s.studentCode, cat.id)}
                                    style={{
                                      width: '16px',
                                      height: '16px',
                                      cursor: 'pointer',
                                      accentColor: 'var(--danger)'
                                    }}
                                  />
                                  {isAuto && (
                                    <span style={{ fontSize: '8px', color: 'var(--warning)', fontWeight: 800, textTransform: 'uppercase' }} title={note}>
                                      ⚡ Auto
                                    </span>
                                  )}
                                  <button
                                    type="button"
                                    onClick={() => openNoteModal(s.studentCode, cat.id)}
                                    style={{
                                      border: 'none',
                                      background: 'transparent',
                                      fontSize: '9px',
                                      color: note ? 'var(--accent)' : 'var(--text-muted)',
                                      cursor: 'pointer',
                                      padding: 0
                                    }}
                                    title={note || 'Add specific note'}
                                  >
                                    {note ? '📝 Note' : '➕ Note'}
                                  </button>
                                </div>
                              </td>
                            );
                          })}

                          {/* Total Count Cell */}
                          <td style={{ padding: '8px 10px', textAlign: 'center', borderLeft: '1px solid var(--border-light)' }}>
                            <span
                              className="badge"
                              style={{
                                background: activeCount > 0 ? 'var(--danger-bg)' : 'var(--surface-2)',
                                color: activeCount > 0 ? 'var(--danger)' : 'var(--text-muted)',
                                border: activeCount > 0 ? '1px solid rgba(239, 68, 68, 0.3)' : '1px solid var(--border-light)',
                                fontWeight: 800,
                                fontSize: '11px',
                                padding: '2px 8px',
                                borderRadius: '10px'
                              }}
                            >
                              {activeCount}
                            </span>
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        )}
        </>
        )}


      </div>

      {/* Note Modal */}
      {activeNoteStudent && activeNoteCatId && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.5)', zIndex: 40000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '12px' }}>
          <div className="modal-content" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', maxWidth: '420px', width: '100%', padding: '16px' }}>
            <h4 style={{ margin: '0 0 8px', fontSize: '14px', fontWeight: 800 }}>
              📝 Add Specific Note
            </h4>
            <p style={{ margin: '0 0 10px', fontSize: '11px', color: 'var(--text-muted)' }}>
              Category: <strong>{categories.find(c => c.id === activeNoteCatId)?.name}</strong>
            </p>
            <textarea
              rows={3}
              value={tempNoteText}
              onChange={(e) => setTempNoteText(e.target.value)}
              placeholder="e.g. Incomplete exercise 5.2 questions 1-4..."
              style={{ width: '100%', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--bg)', color: 'var(--text)', fontSize: '12px', resize: 'vertical' }}
            />
            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '12px' }}>
              <button
                type="button"
                className="btn btn-secondary btn-sm"
                onClick={() => { setActiveNoteStudent(null); setActiveNoteCatId(null); }}
              >
                Cancel
              </button>
              <button
                type="button"
                className="btn btn-primary btn-sm"
                onClick={saveNote}
              >
                Save Note
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Category Manager Modal */}
      {categoryModalOpen && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.5)', zIndex: 40000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '12px' }}>
          <div className="modal-content" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', maxWidth: '540px', width: '100%', padding: '18px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 800 }}>⚙️ Manage Fault Types</h4>
              <button className="close-modal" onClick={() => setCategoryModalOpen(false)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>

            {/* List of Current Categories */}
            <div style={{ maxHeight: '200px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '6px 10px', marginBottom: '14px', background: 'var(--bg)' }}>
              {categories.map(c => (
                <div key={c.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '5px 0', borderBottom: '1px solid var(--border-light)', fontSize: '12px' }}>
                  <span>{c.icon} <strong>{c.name}</strong> <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>({c.target})</span></span>
                  {!c.isDefault && (
                    <button
                      type="button"
                      onClick={() => handleDeleteCategory(c.id)}
                      style={{ border: 'none', background: 'transparent', color: 'var(--danger)', cursor: 'pointer', fontSize: '12px' }}
                    >
                      ✕ Remove
                    </button>
                  )}
                </div>
              ))}
            </div>

            {/* Add New Category Form */}
            <div style={{ background: 'var(--surface-light)', padding: '12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
              <h5 style={{ margin: '0 0 8px', fontSize: '12px', fontWeight: 700 }}>+ Add Custom Fault Type</h5>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px', marginBottom: '8px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '10px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '2px' }}>Name</label>
                  <input
                    type="text"
                    placeholder="e.g. Uniform Incomplete"
                    value={newCatName}
                    onChange={(e) => setNewCatName(e.target.value)}
                    style={{ width: '100%', padding: '4px 6px', fontSize: '11px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '10px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '2px' }}>Target Stakeholder</label>
                  <select
                    value={newCatTarget}
                    onChange={(e) => setNewCatTarget(e.target.value as any)}
                    style={{ width: '100%', padding: '4px 6px', fontSize: '11px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)' }}
                  >
                    <option value="student">Student</option>
                    <option value="parent">Parent</option>
                    <option value="shared">Shared</option>
                  </select>
                </div>
              </div>
              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
                <button
                  type="button"
                  className="btn btn-primary btn-sm"
                  onClick={handleAddCategory}
                  style={{ fontSize: '11px' }}
                >
                  Add Fault Type
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
