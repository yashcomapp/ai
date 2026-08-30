'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import { formatDateDMY as formatDateStr, getDateKeyIST as getISTDateString } from '@/lib/dateUtils';
import dynamic from 'next/dynamic';
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });

interface StudentRecord {
  studentCode: string;
  name: string;
  email: string;
  status: 'present' | 'absent' | 'late' | 'leave' | 'half_day';
  remarks: string;
  isLeaveApproved: boolean;
  pendingLeave?: {
    id: string;
    startDate: string;
    endDate: string;
    remarks: string;
    status: string;
  } | null;
  selfMarked?: boolean;
  selfMarkedBy?: string | null;
  selfMarkedAt?: string | null;
}

interface Batch {
  id: string;
  name: string;
  classNum: string;
}

interface Leave {
  id: string;
  studentCode: string;
  studentName: string;
  startDate: string;
  endDate: string;
  type: string;
  remarks: string;
}

export default function AdminAttendancePage() {
  const { firebaseUser } = useAuth();
  const router = useRouter();

  // Tab View
  const [activeTab, setActiveTab] = useState<'classroom' | 'parent_sync'>('classroom');

  const todayStr = getISTDateString();
  const [selectedDate, setSelectedDate] = useState(todayStr);
  const [batches, setBatches] = useState<Batch[]>([]);
  const [selectedBatchId, setSelectedBatchId] = useState('');

  const [roster, setRoster] = useState<StudentRecord[]>([]);
  const [rosterLoading, setRosterLoading] = useState(false);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');
  const [successMsg, setSuccessMsg] = useState('');

  // Parent-Child 5-Min Sync Attendance State
  const [syncDate, setSyncDate] = useState(todayStr);
  const [syncBatchId, setSyncBatchId] = useState('all');
  const [syncData, setSyncData] = useState<{
    summary: { totalStudents: number; completedCount: number; pendingCount: number; syncPercentage: number };
    records: Array<{ studentCode: string; studentName: string; className: string; batchName: string; status: 'completed' | 'pending'; completedAt: string; reviewedBy: string; feedback: string }>;
  } | null>(null);
  const [syncLoading, setSyncLoading] = useState(false);
  const [pdfModalOpen, setPdfModalOpen] = useState(false);

  // Leaves management
  const [leaves, setLeaves] = useState<Leave[]>([]);
  const [declarations, setDeclarations] = useState<any[]>([]);
  const [showLeaveModal, setShowLeaveModal] = useState(false);
  const [newLeaveStudentCode, setNewLeaveStudentCode] = useState('');
  const [newLeaveStudentName, setNewLeaveStudentName] = useState('');
  const [newLeaveStart, setNewLeaveStart] = useState('');
  const [newLeaveEnd, setNewLeaveEnd] = useState('');
  const [newLeaveType, setNewLeaveType] = useState('sick');
  const [newLeaveRemarks, setNewLeaveRemarks] = useState('');
  const [leaveLoading, setLeaveLoading] = useState(false);

  // Fetch batches
  useEffect(() => {
    async function loadBatches() {
      if (!firebaseUser) return;
      try {
        const token = await firebaseUser.getIdToken();
        const res = await fetch('/api/admin/batches', {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        if (!res.ok) throw new Error('Failed to load batches');
        const resData = await res.json();
        setBatches(resData.batches || []);
        if (resData.batches?.length > 0) {
          setSelectedBatchId(resData.batches[0].id);
        }
      } catch (e: any) {
        setError(e.message);
      }
    }
    loadBatches();
  }, [firebaseUser]);

  // Fetch leaves list
  async function loadLeaves() {
    if (!firebaseUser) return;
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/attendance/leaves', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (!res.ok) throw new Error('Failed to load leave records');
      const resData = await res.json();
      setLeaves(resData.leaves || []);

      // Load multi-day declarations
      const resDecl = await fetch('/api/student/attendance/declare', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (resDecl.ok) {
        const declData = await resDecl.json();
        setDeclarations(declData.declarations || []);
      }
    } catch (e: any) {
      console.error(e);
    }
  }

  useEffect(() => {
    loadLeaves();
  }, [firebaseUser]);

  // Fetch Roster
  async function fetchRoster() {
    if (!firebaseUser || !selectedBatchId) return;
    setRosterLoading(true);
    setError('');
    setSuccessMsg('');
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch(`/api/admin/attendance?batchId=${selectedBatchId}&date=${selectedDate}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (!res.ok) throw new Error('Failed to load roster status');
      const resData = await res.json();
      setRoster(resData.roster || []);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setRosterLoading(false);
    }
  }

  useEffect(() => {
    if (activeTab === 'classroom') {
      fetchRoster();
    }
  }, [selectedBatchId, firebaseUser, selectedDate, activeTab]);

  // Fetch Parent-Child 5-Min Sync Attendance
  const fetchParentSyncAttendance = async () => {
    if (!firebaseUser) return;
    setSyncLoading(true);
    setError('');
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/attendance/parent-sync?date=${syncDate}&batchId=${syncBatchId}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (!res.ok) throw new Error('Failed to load parent sync attendance');
      const resData = await res.json();
      setSyncData(resData);
    } catch (e: any) {
      console.error('Parent sync attendance fetch error:', e);
      setError(e.message);
    } finally {
      setSyncLoading(false);
    }
  };

  useEffect(() => {
    if (activeTab === 'parent_sync') {
      fetchParentSyncAttendance();
    }
  }, [activeTab, syncDate, syncBatchId, firebaseUser]);

  const handleApproveLeave = async (leaveId: string) => {
    if (!firebaseUser) return;
    if (!confirm('Are you sure you want to approve this leave request?')) return;
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/attendance/leaves', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          action: 'approve',
          leaveId
        })
      });
      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.error || 'Failed to approve leave request');
      }
      alert('✅ Leave request approved successfully.');
      fetchRoster();
    } catch (e: any) {
      alert(e.message || 'Error approving leave.');
    }
  };

  const handleStatusChange = (studentCode: string, status: 'present' | 'absent' | 'late' | 'leave' | 'half_day') => {
    setRoster(prev =>
      prev.map(r => (r.studentCode === studentCode ? { ...r, status } : r))
    );
  };

  const handleRemarksChange = (studentCode: string, remarks: string) => {
    setRoster(prev =>
      prev.map(r => (r.studentCode === studentCode ? { ...r, remarks } : r))
    );
  };

  // Submit Roster
  const handleSaveAttendance = async () => {
    if (!selectedBatchId || roster.length === 0 || saving) return;
    setSaving(true);
    setError('');
    setSuccessMsg('');
    try {
      const token = await firebaseUser!.getIdToken();
      const recordsPayload: Record<string, { status: string; remarks: string }> = {};
      roster.forEach(r => {
        recordsPayload[r.studentCode] = {
          status: r.status,
          remarks: r.remarks
        };
      });

      const res = await fetch('/api/admin/attendance', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          batchId: selectedBatchId,
          date: selectedDate,
          records: recordsPayload
        })
      });

      const resData = await res.json();
      if (!res.ok) throw new Error(resData.error || 'Failed to save attendance');
      setSuccessMsg('Daily attendance saved successfully! Unexcused absences reported to parents.');
      fetchRoster();
    } catch (e: any) {
      setError(e.message);
    } finally {
      setSaving(false);
    }
  };

  // Submit Leave Approval
  const handleCreateLeave = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newLeaveStudentCode || !newLeaveStart || !newLeaveEnd) {
      alert('Please fill out student code, start and end dates.');
      return;
    }
    setLeaveLoading(true);
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/attendance/leaves', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          action: 'create',
          leaveData: {
            studentCode: newLeaveStudentCode.trim().toUpperCase(),
            studentName: newLeaveStudentName.trim(),
            startDate: newLeaveStart,
            endDate: newLeaveEnd,
            type: newLeaveType,
            remarks: newLeaveRemarks
          }
        })
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.error || 'Failed to approve leave');
      }

      setNewLeaveStudentCode('');
      setNewLeaveStudentName('');
      setNewLeaveRemarks('');
      setShowLeaveModal(false);
      loadLeaves();
      fetchRoster();
      alert('Long duration leave approved successfully!');
    } catch (err: any) {
      alert(err.message);
    } finally {
      setLeaveLoading(false);
    }
  };

  // Delete Leave approval
  const handleDeleteLeave = async (id: string) => {
    if (!confirm('Are you sure you want to delete this leave approval?')) return;
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/attendance/leaves', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          action: 'delete',
          leaveId: id
        })
      });
      if (!res.ok) throw new Error('Failed to delete leave record');
      loadLeaves();
      fetchRoster();
    } catch (err: any) {
      alert(err.message);
    }
  };

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', padding: '24px 12px' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>
        
        {/* Header Block */}
        <div className="card glass" style={{ padding: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <h2 style={{ fontSize: '1.5rem', fontWeight: 800, color: 'var(--accent)', margin: 0 }}>📅 Daily Attendance Sheet</h2>
          </div>
          <div style={{ display: 'flex', gap: '8px' }}>
            <button className="btn btn-secondary" onClick={() => setShowLeaveModal(true)}>
              🌴 Manage Long Leaves
            </button>
            <button className="btn btn-secondary" onClick={() => router.push('/admin')}>
              Back
            </button>
          </div>
        </div>

        {/* Top Tab Bar */}
        <div style={{ display: 'flex', gap: '8px', borderBottom: '1.5px solid var(--border-light)', paddingBottom: '8px' }}>
          <button
            onClick={() => setActiveTab('classroom')}
            style={{
              padding: '10px 18px',
              border: 'none',
              cursor: 'pointer',
              background: 'none',
              fontWeight: 700,
              fontSize: '14px',
              borderBottom: activeTab === 'classroom' ? '2.5px solid var(--accent)' : 'none',
              color: activeTab === 'classroom' ? 'var(--accent)' : 'var(--text-muted)',
              display: 'flex',
              alignItems: 'center',
              gap: '6px'
            }}
          >
            <span>📋 Classroom Attendance</span>
          </button>
          <button
            onClick={() => setActiveTab('parent_sync')}
            style={{
              padding: '10px 18px',
              border: 'none',
              cursor: 'pointer',
              background: 'none',
              fontWeight: 700,
              fontSize: '14px',
              borderBottom: activeTab === 'parent_sync' ? '2.5px solid #a855f7' : 'none',
              color: activeTab === 'parent_sync' ? '#a855f7' : 'var(--text-muted)',
              display: 'flex',
              alignItems: 'center',
              gap: '6px'
            }}
          >
            <span>🌙 Parent-Child 5-Min Sync Attendance</span>
            {syncData?.summary?.completedCount ? (
              <span style={{ fontSize: '11px', background: '#a855f7', color: '#fff', padding: '1px 6px', borderRadius: '10px', fontWeight: 800 }}>
                {syncData.summary.completedCount}
              </span>
            ) : null}
          </button>
        </div>

        {error && <div className="alert-box alert-box-danger">{error}</div>}
        {successMsg && <div className="alert-box alert-box-success">{successMsg}</div>}

        {/* VIEW 1: Classroom Attendance */}
        {activeTab === 'classroom' && (
          <>
            {/* Batch Selector & Target Date */}
            <div className="card" style={{ padding: '16px 20px', background: 'var(--surface)', display: 'flex', gap: '24px', alignItems: 'center', flexWrap: 'wrap', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)' }}>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '10px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Select Batch</label>
                <select
                  value={selectedBatchId}
                  onChange={(e) => setSelectedBatchId(e.target.value)}
                  style={{ padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontWeight: 600, outline: 'none' }}
                >
                  {batches.map(b => (
                    <option key={b.id} value={b.id}>{b.name} (Class {b.classNum})</option>
                  ))}
                </select>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '10px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Target Date</label>
                <input
                  type="date"
                  value={selectedDate}
                  max={todayStr}
                  onChange={(e) => setSelectedDate(e.target.value)}
                  style={{ padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontWeight: 600 }}
                />
              </div>
            </div>

            {/* Roster list */}
            <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', overflow: 'hidden' }}>
              <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)' }}>
                <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold' }}>Roster Listing</h3>
              </div>

              {rosterLoading ? (
                <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>Loading batch roster...</div>
              ) : roster.length === 0 ? (
                <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>No active students mapped to this batch.</div>
              ) : (
                <div style={{ overflowX: 'auto' }}>
                  <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                    <thead>
                      <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                        <th style={{ padding: '8px 12px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Name</th>
                        <th style={{ padding: '8px 12px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', width: '180px' }}>Mark Attendance</th>
                        <th style={{ padding: '8px 12px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Remarks</th>
                      </tr>
                    </thead>
                    <tbody>
                      {roster.map(student => (
                        <tr key={student.studentCode} style={{ borderBottom: '1px solid var(--border-light)' }}>
                          <td style={{ padding: '8px 12px', fontSize: '13px' }}>
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                {/* Declaration status indicators */}
                                {student.isLeaveApproved ? (
                                  <span style={{ fontSize: '14px', cursor: 'help', color: '#eab308', fontWeight: 'bold' }} title="Approved Leave">🌴</span>
                                ) : student.pendingLeave ? (
                                  <span style={{ fontSize: '14px', cursor: 'help' }} title="Pending Leave Request">⏳</span>
                                ) : student.selfMarked ? (
                                  <span style={{ fontSize: '16px', cursor: 'help', color: '#22c55e', fontWeight: 'bold' }} title={`Voluntary declaration: Self-marked by ${student.selfMarkedBy || 'student'} at ${student.selfMarkedAt ? new Date(student.selfMarkedAt).toLocaleTimeString() : ''}`}>✓</span>
                                ) : (
                                  <span style={{ fontSize: '14px', cursor: 'help' }} title="Not Declared">⚠️</span>
                                )}
                                <strong>{student.name}</strong>
                              </div>
                              {student.pendingLeave && (
                                <span style={{ fontSize: '10.5px', color: '#eab308', fontWeight: 600, marginLeft: '22px' }}>
                                  📅 Pending Leave: {formatDateStr(student.pendingLeave.startDate)} to {formatDateStr(student.pendingLeave.endDate)}
                                  {student.pendingLeave.remarks && ` (${student.pendingLeave.remarks})`}
                                </span>
                              )}
                            </div>
                          </td>
                          <td style={{ padding: '8px 12px' }}>
                            {student.isLeaveApproved ? (
                              <span className="badge badge-secondary" style={{ padding: '4px 8px', borderRadius: '4px', fontSize: '10.5px', fontWeight: 700 }}>
                                Excused Leave 🌴
                              </span>
                            ) : (
                              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                                {student.pendingLeave && (
                                  <div style={{ display: 'flex', gap: '6px', marginBottom: '4px' }}>
                                    <button
                                      onClick={() => handleApproveLeave(student.pendingLeave!.id)}
                                      className="btn"
                                      style={{
                                        padding: '4px 8px',
                                        fontSize: '10.5px',
                                        borderRadius: '4px',
                                        fontWeight: 'bold',
                                        background: '#2ecc71',
                                        border: 'none',
                                        color: '#fff',
                                        cursor: 'pointer'
                                      }}
                                    >
                                      Approve 🌴
                                    </button>
                                    <button
                                      onClick={() => handleDeleteLeave(student.pendingLeave!.id)}
                                      className="btn"
                                      style={{
                                        padding: '4px 8px',
                                        fontSize: '10.5px',
                                        borderRadius: '4px',
                                        fontWeight: 'bold',
                                        background: '#e74c3c',
                                        border: 'none',
                                        color: '#fff',
                                        cursor: 'pointer'
                                      }}
                                    >
                                      Decline ✖
                                    </button>
                                  </div>
                                )}
                                <div style={{ display: 'flex', gap: '4px' }}>
                                  <button
                                    onClick={() => handleStatusChange(student.studentCode, 'present')}
                                    style={{
                                      border: 'none',
                                      background: student.status === 'present' ? 'var(--success)' : 'var(--bg-soft)',
                                      color: student.status === 'present' ? '#fff' : 'var(--text-muted)',
                                      width: '26px',
                                      height: '26px',
                                      borderRadius: '50%',
                                      display: 'inline-flex',
                                      alignItems: 'center',
                                      justifyContent: 'center',
                                      cursor: 'pointer',
                                      fontWeight: 'bold'
                                    }}
                                    title="Present"
                                  >
                                    P
                                  </button>
                                  <button
                                    onClick={() => handleStatusChange(student.studentCode, 'absent')}
                                    style={{
                                      border: 'none',
                                      background: student.status === 'absent' ? 'var(--danger)' : 'var(--bg-soft)',
                                      color: student.status === 'absent' ? '#fff' : 'var(--text-muted)',
                                      width: '26px',
                                      height: '26px',
                                      borderRadius: '50%',
                                      display: 'inline-flex',
                                      alignItems: 'center',
                                      justifyContent: 'center',
                                      cursor: 'pointer',
                                      fontWeight: 'bold'
                                    }}
                                    title="Absent"
                                  >
                                    A
                                  </button>
                                  <button
                                    onClick={() => handleStatusChange(student.studentCode, 'late')}
                                    style={{
                                      border: 'none',
                                      background: student.status === 'late' ? '#f39c12' : 'var(--bg-soft)',
                                      color: student.status === 'late' ? '#fff' : 'var(--text-muted)',
                                      width: '26px',
                                      height: '26px',
                                      borderRadius: '50%',
                                      display: 'inline-flex',
                                      alignItems: 'center',
                                      justifyContent: 'center',
                                      cursor: 'pointer',
                                      fontWeight: 'bold'
                                    }}
                                    title="Late"
                                  >
                                    L
                                  </button>
                                  <button
                                    onClick={() => handleStatusChange(student.studentCode, 'leave')}
                                    style={{
                                      border: 'none',
                                      background: student.status === 'leave' ? '#3498db' : 'var(--bg-soft)',
                                      color: student.status === 'leave' ? '#fff' : 'var(--text-muted)',
                                      width: '26px',
                                      height: '26px',
                                      borderRadius: '50%',
                                      display: 'inline-flex',
                                      alignItems: 'center',
                                      justifyContent: 'center',
                                      cursor: 'pointer',
                                      fontWeight: 'bold'
                                    }}
                                    title="Leave"
                                  >
                                    🌴
                                  </button>
                                  <button
                                    onClick={() => handleStatusChange(student.studentCode, 'half_day')}
                                    style={{
                                      border: 'none',
                                      background: student.status === 'half_day' ? '#9b59b6' : 'var(--bg-soft)',
                                      color: student.status === 'half_day' ? '#fff' : 'var(--text-muted)',
                                      width: '26px',
                                      height: '26px',
                                      borderRadius: '50%',
                                      display: 'inline-flex',
                                      alignItems: 'center',
                                      justifyContent: 'center',
                                      cursor: 'pointer',
                                      fontWeight: 'bold'
                                    }}
                                    title="Half Day"
                                  >
                                    ½
                                  </button>
                                </div>
                              </div>
                            )}
                          </td>
                          <td style={{ padding: '8px 12px' }}>
                            <input
                              type="text"
                              value={student.remarks || ''}
                              onChange={(e) => handleRemarksChange(student.studentCode, e.target.value)}
                              placeholder="Add reason or note..."
                              style={{ width: '100%', padding: '6px 10px', fontSize: '12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                            />
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}

              <div style={{ padding: '16px 20px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end' }}>
                <button className="btn btn-primary" onClick={handleSaveAttendance} disabled={saving || roster.length === 0}>
                  {saving ? 'Saving...' : '💾 Save Daily Attendance'}
                </button>
              </div>
            </div>
          </>
        )}

        {/* VIEW 2: Daily Parent-Child 5-Min Sync Attendance */}
        {activeTab === 'parent_sync' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {/* Filter & Export Bar */}
            <div className="card" style={{ padding: '16px 20px', background: 'var(--surface)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)' }}>
              <div style={{ display: 'flex', gap: '20px', alignItems: 'center', flexWrap: 'wrap' }}>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <label style={{ fontSize: '10px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Select Batch</label>
                  <select
                    value={syncBatchId}
                    onChange={(e) => setSyncBatchId(e.target.value)}
                    style={{ padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontWeight: 600, outline: 'none' }}
                  >
                    <option value="all">All Batches</option>
                    {batches.map(b => (
                      <option key={b.id} value={b.id}>{b.name} (Class {b.classNum})</option>
                    ))}
                  </select>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <label style={{ fontSize: '10px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Target Date</label>
                  <input
                    type="date"
                    value={syncDate}
                    max={todayStr}
                    onChange={(e) => setSyncDate(e.target.value)}
                    style={{ padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontWeight: 600 }}
                  />
                </div>
              </div>

              <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
                <button 
                  className="btn btn-secondary btn-sm"
                  onClick={() => fetchParentSyncAttendance()}
                  disabled={syncLoading}
                >
                  🔄 Refresh
                </button>
                <button 
                  className="btn btn-primary btn-sm"
                  onClick={() => setPdfModalOpen(true)}
                  disabled={syncLoading || !syncData || syncData.records.length === 0}
                  style={{ background: 'linear-gradient(135deg, #a855f7, #6366f1)', border: 'none' }}
                >
                  📄 Export PDF (No Photos)
                </button>
              </div>
            </div>

            {/* Summary Statistics Card */}
            <div id="parent-sync-summary-section" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: '12px' }}>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
                <div style={{ fontSize: '20px', fontWeight: 800 }}>{syncData?.summary?.totalStudents ?? '—'}</div>
                <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '4px' }}>👥 Total Enrolled</div>
              </div>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
                <div style={{ fontSize: '20px', fontWeight: 800, color: 'var(--success)' }}>{syncData?.summary?.completedCount ?? '—'}</div>
                <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '4px' }}>🟢 Sync Completed</div>
              </div>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
                <div style={{ fontSize: '20px', fontWeight: 800, color: (syncData?.summary?.pendingCount || 0) > 0 ? 'var(--danger)' : 'var(--text)' }}>
                  {syncData?.summary?.pendingCount ?? '—'}
                </div>
                <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '4px' }}>🔴 Pending / Missed</div>
              </div>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
                <div style={{ fontSize: '20px', fontWeight: 800, color: '#a855f7' }}>{syncData?.summary?.syncPercentage ?? 0}%</div>
                <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '4px' }}>📊 Sincerity Rate</div>
              </div>
            </div>

            {/* Attendance Table (Clean - Zero Photos) */}
            <div id="parent-sync-table-section" className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', overflow: 'hidden' }}>
              <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold' }}>
                  Daily 5-Min Parent-Child Sync Register &mdash; {formatDateStr(syncDate)}
                </h3>
                <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                  {syncBatchId === 'all' ? 'All Batches' : batches.find(b => b.id === syncBatchId)?.name || 'Selected Batch'}
                </span>
              </div>

              {syncLoading ? (
                <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>Loading sync records...</div>
              ) : !syncData || syncData.records.length === 0 ? (
                <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>No student records found.</div>
              ) : (
                <div style={{ overflowX: 'auto' }}>
                  <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
                    <thead>
                      <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '11px', textTransform: 'uppercase' }}>
                        <th style={{ padding: '10px 14px', width: '40px' }}>#</th>
                        <th style={{ padding: '10px 14px' }}>Student</th>
                        <th style={{ padding: '10px 14px' }}>Class / Batch</th>
                        <th style={{ padding: '10px 14px' }}>Sync Status</th>
                        <th style={{ padding: '10px 14px' }}>Time (IST)</th>
                        <th style={{ padding: '10px 14px' }}>Reviewed By</th>
                        <th style={{ padding: '10px 14px' }}>Discussion Notes / Feedback</th>
                      </tr>
                    </thead>
                    <tbody>
                      {syncData.records.map((rec, idx) => (
                        <tr key={rec.studentCode} style={{ borderBottom: '1px solid var(--border-light)' }}>
                          <td style={{ padding: '10px 14px', color: 'var(--text-muted)', fontSize: '12px' }}>{idx + 1}</td>
                          <td style={{ padding: '10px 14px', fontWeight: 600 }}>👤 {rec.studentName}</td>
                          <td style={{ padding: '10px 14px', color: 'var(--text-muted)', fontSize: '12px' }}>{rec.batchName} ({rec.className})</td>
                          <td style={{ padding: '10px 14px' }}>
                            {rec.status === 'completed' ? (
                              <span style={{ background: 'rgba(34, 197, 94, 0.15)', color: '#16a34a', padding: '3px 8px', borderRadius: '6px', fontSize: '11px', fontWeight: 700 }}>
                                🟢 Verified
                              </span>
                            ) : (
                              <span style={{ background: 'rgba(239, 68, 68, 0.15)', color: '#dc2626', padding: '3px 8px', borderRadius: '6px', fontSize: '11px', fontWeight: 700 }}>
                                ⏳ Pending
                              </span>
                            )}
                          </td>
                          <td style={{ padding: '10px 14px', fontSize: '12px', color: 'var(--text-muted)' }}>{rec.completedAt}</td>
                          <td style={{ padding: '10px 14px', fontSize: '12px' }}>{rec.reviewedBy}</td>
                          <td style={{ padding: '10px 14px', fontSize: '12px', color: 'var(--text-muted)' }}>{rec.feedback}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </div>

            {/* Export PDF Modal */}
            <ExportPdfModal
              isOpen={pdfModalOpen}
              onClose={() => setPdfModalOpen(false)}
              filename={`Parent-Sync-Attendance-${syncDate}-${syncBatchId}`}
              title={`Daily Parent-Child 5-Min Sync Attendance — ${formatDateStr(syncDate)}`}
              sections={[
                { id: 'summary', name: 'Attendance Summary Metrics', elementId: 'parent-sync-summary-section' },
                { id: 'table', name: 'Student Sync Register (Without Photos)', elementId: 'parent-sync-table-section' }
              ]}
            />
          </div>
        )}
      </div>

      {/* Leaves Modal */}
      {showLeaveModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.5)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
          <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '800px', width: '100%', maxHeight: '90vh', display: 'flex', flexDirection: 'column', boxShadow: 'var(--shadow-lg)' }}>
            
            <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold' }}>🌴 Long Duration Leave approvals</h3>
              <button style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }} onClick={() => setShowLeaveModal(false)}>×</button>
            </div>

            <div style={{ padding: '20px', overflowY: 'auto', display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', flex: 1 }}>
              
              {/* Form to approve leave */}
              <form onSubmit={handleCreateLeave} style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                <h4 style={{ margin: 0, fontSize: '12px', textTransform: 'uppercase', color: 'var(--text-muted)' }}>Approve New Leave</h4>
                
                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <label style={{ fontSize: '11px', fontWeight: 600 }}>Student Code</label>
                  <input
                    type="text"
                    required
                    value={newLeaveStudentCode}
                    onChange={(e) => setNewLeaveStudentCode(e.target.value)}
                    placeholder="e.g. ST-2026-000050"
                    style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                  />
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <label style={{ fontSize: '11px', fontWeight: 600 }}>Student Name</label>
                  <input
                    type="text"
                    value={newLeaveStudentName}
                    onChange={(e) => setNewLeaveStudentName(e.target.value)}
                    placeholder="Vrujesh Bhutada"
                    style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                  />
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px' }}>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                    <label style={{ fontSize: '11px', fontWeight: 600 }}>Start Date</label>
                    <input
                      type="date"
                      required
                      value={newLeaveStart}
                      onChange={(e) => setNewLeaveStart(e.target.value)}
                      style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                    />
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                    <label style={{ fontSize: '11px', fontWeight: 600 }}>End Date</label>
                    <input
                      type="date"
                      required
                      value={newLeaveEnd}
                      onChange={(e) => setNewLeaveEnd(e.target.value)}
                      style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                    />
                  </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <label style={{ fontSize: '11px', fontWeight: 600 }}>Type</label>
                  <select
                    value={newLeaveType}
                    onChange={(e) => setNewLeaveType(e.target.value)}
                    style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                  >
                    <option value="sick">Sick Leave</option>
                    <option value="planned">Planned Personal Leave</option>
                  </select>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <label style={{ fontSize: '11px', fontWeight: 600 }}>Remarks</label>
                  <textarea
                    value={newLeaveRemarks}
                    onChange={(e) => setNewLeaveRemarks(e.target.value)}
                    placeholder="Sickness recovery leave"
                    style={{ padding: '8px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', resize: 'none', height: '60px' }}
                  />
                </div>

                <button type="submit" className="btn btn-primary" style={{ marginTop: '8px' }} disabled={leaveLoading}>
                  {leaveLoading ? 'Processing...' : 'Approve Leave'}
                </button>
              </form>

              {/* List of active approved leaves */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <h4 style={{ margin: 0, fontSize: '12px', textTransform: 'uppercase', color: 'var(--text-muted)' }}>Approved Leave Register</h4>
                {leaves.length === 0 ? (
                  <div style={{ color: 'var(--text-faint)', fontSize: '12px', textAlign: 'center', padding: '20px 0' }}>No active approved leaves.</div>
                ) : (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '350px', overflowY: 'auto' }}>
                    {leaves.map(l => (
                      <div key={l.id} className="card" style={{ padding: '10px 12px', background: 'var(--bg-soft)', border: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <div style={{ fontSize: '12px' }}>
                          <div><strong>{l.studentName}</strong></div>
                          <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>
                            📅 {formatDateStr(l.startDate)} to {formatDateStr(l.endDate)}
                          </div>
                          {l.remarks && <div style={{ fontSize: '11px', fontStyle: 'italic', color: 'var(--text-muted)', marginTop: '2px' }}>"{l.remarks}"</div>}
                        </div>
                        <button
                          onClick={() => handleDeleteLeave(l.id)}
                          style={{ border: 'none', background: 'transparent', color: 'var(--danger)', cursor: 'pointer', fontSize: '1.1rem' }}
                          title="Delete Leave"
                        >
                          🗑️
                        </button>
                      </div>
                    ))}
                  </div>
                )}
              </div>

              {/* Student/Parent Multi-Day Declarations Section */}
              <div style={{ marginTop: '20px', borderTop: '1px solid var(--border-light)', paddingTop: '20px', gridColumn: 'span 2' }}>
                <h4 style={{ margin: '0 0 10px 0', fontSize: '12.5px', fontWeight: 'bold', textTransform: 'uppercase', color: 'var(--text-muted)' }}>📢 Student / Parent Multi-Day Declarations</h4>
                {declarations.length === 0 ? (
                  <div style={{ color: 'var(--text-faint)', fontSize: '12px', textAlign: 'center', padding: '20px 0' }}>No multi-day declarations submitted yet.</div>
                ) : (
                  <div style={{ overflowX: 'auto', maxHeight: '250px' }}>
                    <table style={{ width: '100%', fontSize: '12px', borderCollapse: 'collapse', textAlign: 'left' }}>
                      <thead>
                        <tr style={{ borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', background: 'var(--bg-soft)' }}>
                          <th style={{ padding: '8px 10px' }}>Student</th>
                          <th style={{ padding: '8px 10px' }}>Status</th>
                          <th style={{ padding: '8px 10px' }}>Date Range</th>
                          <th style={{ padding: '8px 10px' }}>Declared By</th>
                          <th style={{ padding: '8px 10px' }}>Remarks</th>
                          <th style={{ padding: '8px 10px' }}>Submitted At</th>
                        </tr>
                      </thead>
                      <tbody>
                        {declarations.map((decl: any) => (
                          <tr key={decl.declarationId} style={{ borderBottom: '1px solid var(--border-light)' }}>
                            <td style={{ padding: '8px 10px', fontWeight: 600 }}>{decl.studentName}</td>
                            <td style={{ padding: '8px 10px' }}>
                              <span className={`badge ${decl.status === 'present' ? 'badge-success' : 'badge-warning'}`} style={{ fontSize: '10px', padding: '2px 6px', borderRadius: '4px' }}>
                                {decl.status === 'present' ? '🟢 Present' : 'Excused Leave'}
                              </span>
                            </td>
                            <td style={{ padding: '8px 10px', fontWeight: 600 }}>{formatDateStr(decl.startDate)} to {formatDateStr(decl.endDate)}</td>
                            <td style={{ padding: '8px 10px', textTransform: 'capitalize' }}>{decl.declaredBy}</td>
                            <td style={{ padding: '8px 10px', color: 'var(--text-muted)' }}>{decl.remarks || '—'}</td>
                            <td style={{ padding: '8px 10px', color: 'var(--text-faint)', fontSize: '10px' }}>{formatDateStr(decl.createdAt)}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </div>

            </div>

          </div>
        </div>
      )}

    </div>
  );
}
