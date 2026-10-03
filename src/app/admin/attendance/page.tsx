'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import { formatDateDMY as formatDateStr, getDateKeyIST as getISTDateString } from '@/lib/dateUtils';
import { useAdminBatches } from '@/hooks/useAdminReferenceData';

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

  const todayStr = getISTDateString();
  const [selectedDate, setSelectedDate] = useState(todayStr);
  const [batches, setBatches] = useState<Batch[]>([]);
  const [selectedBatchId, setSelectedBatchId] = useState('');

  const [roster, setRoster] = useState<StudentRecord[]>([]);
  const [rosterLoading, setRosterLoading] = useState(false);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');
  const [successMsg, setSuccessMsg] = useState('');

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

  // Shared SWR Batches
  const { batches: swrBatches } = useAdminBatches();

  useEffect(() => {
    if (swrBatches && swrBatches.length > 0) {
      setBatches(swrBatches);
      setSelectedBatchId(prev => prev || swrBatches[0].id);
    }
  }, [swrBatches]);

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
    fetchRoster();
  }, [selectedBatchId, firebaseUser, selectedDate]);

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
      setSuccessMsg('✅ Daily attendance saved successfully! Unexcused absences reported to parents.');
      setSaving(false);
      // Refresh roster asynchronously in background without keeping button locked in Saving state
      fetchRoster();
    } catch (e: any) {
      setError(e.message);
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
      <div style={{ maxWidth: '1200px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        
        {/* Back to Dashboard Link on Top */}
        <div style={{ display: 'flex', justifyContent: 'flex-start' }}>
          <button 
            onClick={() => router.push('/admin')} 
            style={{
              background: 'none',
              border: 'none',
              color: 'var(--accent)',
              cursor: 'pointer',
              fontSize: '13px',
              fontWeight: 600,
              display: 'flex',
              alignItems: 'center',
              gap: '4px',
              padding: 0
            }}
          >
            ← Back to Dashboard
          </button>
        </div>

        {/* Header Block */}
        <div className="card glass" style={{ padding: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <h2 style={{ fontSize: '1.5rem', fontWeight: 800, color: 'var(--accent)', margin: 0 }}>Daily Attendance Sheet</h2>
          </div>
          <div style={{ display: 'flex', gap: '8px' }}>
            <button className="btn btn-secondary" onClick={() => setShowLeaveModal(true)}>
              Manage Long Leaves
            </button>
          </div>
        </div>


        {error && <div className="alert-box alert-box-danger">{error}</div>}
        {successMsg && <div className="alert-box alert-box-success">{successMsg}</div>}

        {/* Classroom Attendance */}
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
                                  <span style={{ fontSize: '14px', cursor: 'help', color: 'var(--warning)', fontWeight: 'bold' }} title="Approved Leave">🌴</span>
                                ) : student.pendingLeave ? (
                                  <span style={{ fontSize: '14px', cursor: 'help' }} title="Pending Leave Request">⏳</span>
                                ) : student.selfMarked ? (
                                  <span style={{ fontSize: '16px', cursor: 'help', color: 'var(--success)', fontWeight: 'bold' }} title={`Voluntary declaration: Self-marked by ${student.selfMarkedBy || 'student'} at ${student.selfMarkedAt ? new Date(student.selfMarkedAt).toLocaleTimeString() : ''}`}>✓</span>
                                ) : (
                                  <span style={{ fontSize: '14px', cursor: 'help' }} title="Not Declared">⚠️</span>
                                )}
                                <strong>{student.name}</strong>
                              </div>
                              {student.pendingLeave && (
                                <span style={{ fontSize: '10.5px', color: 'var(--warning)', fontWeight: 600, marginLeft: '22px' }}>
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
                                        background: 'var(--success)',
                                        border: 'none',
                                        color: 'var(--text-white)',
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
                                        background: 'var(--danger)',
                                        border: 'none',
                                        color: 'var(--text-white)',
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
                                      color: student.status === 'present' ? 'var(--text-white)' : 'var(--text-muted)',
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
                                      color: student.status === 'absent' ? 'var(--text-white)' : 'var(--text-muted)',
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
                                      background: student.status === 'late' ? 'var(--warning)' : 'var(--bg-soft)',
                                      color: student.status === 'late' ? 'var(--text-white)' : 'var(--text-muted)',
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
                                      background: student.status === 'leave' ? 'var(--accent)' : 'var(--bg-soft)',
                                      color: student.status === 'leave' ? 'var(--text-white)' : 'var(--text-muted)',
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
                                      background: student.status === 'half_day' ? 'var(--purple)' : 'var(--bg-soft)',
                                      color: student.status === 'half_day' ? 'var(--text-white)' : 'var(--text-muted)',
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
