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
            <p style={{ margin: '3px 0 0', fontSize: '12px', color: 'var(--text-muted)' }}>
              1-Click discipline tracking for students & parents with auto-detection for missed 60m exam reviews, exam absences & communication gaps.
            </p>
          </div>

          <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
            <button
              type="button"
              className="btn btn-secondary btn-sm"
              onClick={() => router.push('/admin/disputes')}
              style={{ fontSize: '12px', padding: '6px 12px', display: 'flex', alignItems: 'center', gap: '6px' }}
            >
              ⚖️ Exam Disputes Hub
            </button>
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
        <div style={{ display: 'flex', gap: '8px', borderBottom: '1px solid var(--border-light)', paddingBottom: '4px' }}>
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
            📋 Student Conduct Matrix
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

        {/* Main Matrix Table */}
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
