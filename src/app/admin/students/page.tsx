'use client';

import React, { useEffect, useState, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import dynamic from 'next/dynamic';
import { formatToDDMMYYYY, formatToYYYYMMDD } from '@/lib/dateUtils';
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });

interface Student {
  id: string;
  name: string;
  email: string;
  studentCode?: string;
  rollNumber?: string;
  tempId?: string;
  batchIds?: string[];
  status?: string;
  feeStatus?: string;
  dob?: string;
  parentEmail?: string;
  overallMastery?: number;
  autonomous?: boolean;
  curfewBypass?: boolean;
  lastActiveAt?: any;
  currentPage?: string;
  currentPagePath?: string;
  presenceState?: string;
}

import { formatLastActiveIST as formatLastActive } from '@/lib/dateUtils';

interface Batch {
  id: string;
  name: string;
}

export default function AdminStudentsPage() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [students, setStudents] = useState<Student[]>([]);
  const [batches, setBatches] = useState<Batch[]>([]);
  const [error, setError] = useState('');

  // Filtering / Sorting State
  const [searchQuery, setSearchQuery] = useState('');
  const [batchFilter, setBatchFilter] = useState('all');
  const [statusFilter, setStatusFilter] = useState('active');
  const [sortColumn, setSortColumn] = useState<keyof Student>('name');
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc');

  // Modals state
  const [selectedStudent, setSelectedStudent] = useState<Student | null>(null);
  const [viewModalOpen, setViewModalOpen] = useState(false);
  const [editModalOpen, setEditModalOpen] = useState(false);
  const [editFormData, setEditFormData] = useState({
    name: '',
    dob: '',
    parentEmail: '',
    batchIds: [] as string[],
    autonomous: false,
    curfewBypass: false
  });
  const [savingEdit, setSavingEdit] = useState(false);
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);
  const [honestyAlerts, setHonestyAlerts] = useState<any[]>([]);
  const [loadingAlerts, setLoadingAlerts] = useState(false);

  // Password Reset Modal states
  const [resetModalOpen, setResetModalOpen] = useState(false);
  const [resetTargetStudent, setResetTargetStudent] = useState<Student | null>(null);
  const [resetSelection, setResetSelection] = useState<'student' | 'parent' | 'both'>('student');

  const fetchStudents = async () => {
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/students', {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) throw new Error('Failed to load students roster.');
      const data = await res.json();
      setStudents(data.students || []);
      setBatches(data.batches || []);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error fetching records.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStudents();
  }, [firebaseUser]);

  const handleToggleStatus = async (studentId: string, currentStatus: string) => {
    const nextStatus = currentStatus === 'active' ? 'inactive' : 'active';
    if (!confirm(`Are you sure you want to change student status to ${nextStatus}?`)) return;

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/students', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          studentId,
          updateData: { status: nextStatus }
        })
      });
      if (!res.ok) throw new Error('Failed to update status.');
      await fetchStudents();
    } catch (err: any) {
      alert(err.message || 'Status update failed.');
    }
  };

  const handleOpenResetModal = (student: Student) => {
    setResetTargetStudent(student);
    setResetSelection('student');
    setResetModalOpen(true);
  };

  const handleSendResetEmail = async () => {
    if (!resetTargetStudent) return;
    
    const targets: string[] = [];
    if (resetSelection === 'student' || resetSelection === 'both') {
      if (resetTargetStudent.email) targets.push(resetTargetStudent.email);
    }
    if (resetSelection === 'parent' || resetSelection === 'both') {
      if (resetTargetStudent.parentEmail) {
        targets.push(resetTargetStudent.parentEmail);
      }
    }

    if (targets.length === 0) {
      alert('❌ No valid email address selected.');
      return;
    }

    try {
      const { auth } = await import('@/lib/firebase/client');
      const { sendPasswordResetEmail } = await import('firebase/auth');
      
      for (const email of targets) {
        await sendPasswordResetEmail(auth, email);
      }
      
      alert(`✅ Password reset link successfully sent to: ${targets.join(', ')}`);
      setResetModalOpen(false);
      setResetTargetStudent(null);
    } catch (err: any) {
      alert(`❌ Reset failed: ${err.message}`);
    }
  };

  const handleDeleteStudent = async (studentId: string, name: string, studentCode?: string) => {
    if (!confirm(`⚠️ Delete student "${name}"? This cannot be undone.\nThis cascade deletes their dashboard metrics, mastery tracks, and exam attempts.`)) return;

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch(`/api/admin/students?studentId=${studentId}&studentCode=${studentCode || ''}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) throw new Error('Failed to execute deletion.');
      alert('✅ Student record successfully deleted.');
      await fetchStudents();
    } catch (err: any) {
      alert(err.message || 'Deletion failed.');
    }
  };

  const handleOpenViewModal = async (student: Student) => {
    setSelectedStudent(student);
    setViewModalOpen(true);
    setHonestyAlerts([]);
    if (student.studentCode && firebaseUser) {
      setLoadingAlerts(true);
      try {
        const idToken = await firebaseUser.getIdToken();
        const res = await fetch(`/api/admin/students?studentCode=${student.studentCode}`, {
          headers: {
            'Authorization': `Bearer ${idToken}`
          }
        });
        const data = await res.json();
        setHonestyAlerts(data.alerts || []);
      } catch (err) {
        console.error("Failed to load honesty alerts:", err);
      } finally {
        setLoadingAlerts(false);
      }
    }
  };

  const handleOpenEditModal = (student: Student) => {
    setSelectedStudent(student);
    setEditFormData({
      name: student.name || '',
      dob: formatToDDMMYYYY(student.dob) || '',
      parentEmail: student.parentEmail || '',
      batchIds: student.batchIds || [],
      autonomous: student.autonomous || false,
      curfewBypass: student.curfewBypass || false
    });
    setEditModalOpen(true);
  };

  const handleSaveEdit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedStudent || savingEdit) return;
    setSavingEdit(true);

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/students', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          studentId: selectedStudent.id,
          updateData: editFormData
        })
      });
      if (!res.ok) throw new Error('Save edits failed.');
      alert('✅ Student profile updated successfully.');
      setEditModalOpen(false);
      await fetchStudents();
    } catch (err: any) {
      alert(err.message || 'Error saving changes.');
    } finally {
      setSavingEdit(false);
    }
  };

  // Sort and filter logic
  const handleSort = (col: keyof Student) => {
    if (sortColumn === col) {
      setSortDirection(prev => prev === 'asc' ? 'desc' : 'asc');
    } else {
      setSortColumn(col);
      setSortDirection('asc');
    }
  };

  const getSortVal = (s: Student, col: keyof Student) => {
    const val = s[col];
    if (typeof val === 'string') return val.toLowerCase();
    if (Array.isArray(val)) return val.length;
    return val || '';
  };

  const filtered = useMemo(() => {
    return students
      .filter(s => {
        if (batchFilter !== 'all' && !(s.batchIds || []).includes(batchFilter)) return false;
        const studentStatus = s.status || 'active';
        if (statusFilter !== 'all' && studentStatus !== statusFilter) return false;
        if (searchQuery) {
          const query = searchQuery.toLowerCase();
          const code = s.studentCode || s.rollNumber || s.tempId || '';
          return (
            (s.name || '').toLowerCase().includes(query) ||
            (s.email || '').toLowerCase().includes(query) ||
            code.toLowerCase().includes(query)
          );
        }
        return true;
      })
      .sort((a, b) => {
        const aVal = getSortVal(a, sortColumn);
        const bVal = getSortVal(b, sortColumn);
        if (aVal < bVal) return sortDirection === 'asc' ? -1 : 1;
        if (aVal > bVal) return sortDirection === 'asc' ? 1 : -1;
        return 0;
      });
  }, [students, batchFilter, statusFilter, searchQuery, sortColumn, sortDirection]);

  const renderFiltersSkeleton = () => (
    <div className="card skeleton-blink" style={{ background: 'var(--surface)', padding: '15px 20px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', gap: '10px', flexWrap: 'wrap', height: '62px' }}>
    </div>
  );

  const renderTableSkeleton = () => (
    <div className="card skeleton-blink" style={{ background: 'var(--surface)', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
      <div style={{ background: 'var(--bg-soft)', height: '45px', borderBottom: '1px solid var(--border-light)' }}></div>
      <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {[1, 2, 3].map(i => (
          <div key={i} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '12px', borderBottom: '1px solid var(--border-light)' }}>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
              <div style={{ width: '180px', height: '14px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
              <div style={{ width: '220px', height: '10px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
            </div>
            <div style={{ width: '80px', height: '24px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
          </div>
        ))}
      </div>
    </div>
  );

  if (error) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div className="alert-box alert-box-danger" style={{ display: 'block', maxWidth: '400px', textAlign: 'center' }}>
          {error}
        </div>
        <button className="btn btn-primary" onClick={() => window.location.reload()} style={{ marginTop: '16px' }}>Retry</button>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <style dangerouslySetInnerHTML={{__html: `
        @keyframes skeleton-blink {
          0% { opacity: 0.6; }
          50% { opacity: 1; }
          100% { opacity: 0.6; }
        }
        .skeleton-blink {
          animation: skeleton-blink 1.5s infinite ease-in-out;
        }
      `}} />
      {/* Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800, cursor: 'pointer' }} onClick={() => router.push('/admin')}>YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Students</h1>
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Classroom student registry & credentials database</div>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          
          <button className="btn btn-primary" style={{ padding: '6px 12px', fontSize: '12px' }} onClick={() => setPdfSelectorOpen(true)}>📄 Export PDF</button>
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      {/* Main Workspace */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1000px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {loading ? (
          <>
            {renderFiltersSkeleton()}
            {renderTableSkeleton()}
          </>
        ) : (
          <>
            {/* Filters */}
            <div className="card" style={{ background: 'var(--surface)', padding: '15px 20px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <input 
            type="text" 
            className="form-input" 
            placeholder="🔍 Search name, email, roll number..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{ flex: 1, minWidth: '200px' }}
          />

          <select 
            className="form-input" 
            value={batchFilter} 
            onChange={(e) => setBatchFilter(e.target.value)}
            style={{ width: '160px' }}
          >
            <option value="all">All Batches</option>
            {batches.map(b => (
              <option key={b.id} value={b.id}>{b.name}</option>
            ))}
          </select>

          <select 
            className="form-input" 
            value={statusFilter} 
            onChange={(e) => setStatusFilter(e.target.value)}
            style={{ width: '140px' }}
          >
            <option value="active">Active Only</option>
            <option value="all">All Statuses</option>
            <option value="inactive">Inactive</option>
          </select>
        </div>

        {/* Student Grid */}
        <div id="students-roster-section" className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
          <div style={{ overflowX: 'auto' }}>
            <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px', textAlign: 'left' }}>
              <thead>
                <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                  <th onClick={() => handleSort('name')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                    Name {sortColumn === 'name' ? (sortDirection === 'asc' ? '▲' : '▼') : '⇅'}
                  </th>
                  <th onClick={() => handleSort('email')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                    Email {sortColumn === 'email' ? (sortDirection === 'asc' ? '▲' : '▼') : '⇅'}
                  </th>
                  <th style={{ padding: '12px 16px' }}>Batches</th>
                  <th onClick={() => handleSort('status')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                    Status {sortColumn === 'status' ? (sortDirection === 'asc' ? '▲' : '▼') : '⇅'}
                  </th>
                  <th style={{ padding: '12px 16px', textAlign: 'right' }}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {filtered.length === 0 ? (
                  <tr>
                    <td colSpan={5} style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>📭 No students found matching filters.</td>
                  </tr>
                ) : (
                  filtered.map(s => {
                    const isActive = s.status === 'active';
                    return (
                      <tr key={s.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '12px 16px', fontWeight: 600, whiteSpace: 'nowrap' }}>
                          <button 
                            onClick={() => router.push(`/exam-register?studentCode=${s.studentCode}`)}
                            style={{ background: 'none', border: 'none', color: 'var(--accent)', fontWeight: 700, padding: 0, cursor: 'pointer', textAlign: 'left' }}
                          >
                            {s.autonomous ? '🔒 ' : ''}{s.name || '—'}
                          </button>
                        </td>
                        <td style={{ padding: '12px 16px' }}>{s.email || '—'}</td>
                        <td style={{ padding: '12px 16px' }}>
                          <div style={{ display: 'flex', gap: '4px', flexWrap: 'wrap' }}>
                            {(s.batchIds || []).map(bId => {
                              const bName = batches.find(b => b.id === bId)?.name || bId;
                              return (
                                <span key={bId} style={{ fontSize: '10px', padding: '1px 6px', background: 'var(--bg-soft)', borderRadius: '4px', border: '1px solid var(--border-light)', whiteSpace: 'nowrap' }}>
                                  {bName}
                                </span>
                              );
                            })}
                          </div>
                        </td>
                        <td style={{ padding: '12px 16px' }}>
                          <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: isActive ? '#dbf3e1' : '#eee', color: isActive ? '#1aa54e' : '#888', fontWeight: 700 }}>
                            {isActive ? 'Active' : 'Inactive'}
                          </span>
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'right' }}>
                          <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end' }}>
                            <button className="btn btn-secondary btn-sm" style={{ padding: '3px 8px', fontSize: '11px' }} onClick={() => handleOpenEditModal(s)} title="Edit Student Profile">✏️</button>
                            <button className="btn btn-secondary btn-sm" style={{ padding: '3px 8px', fontSize: '11px' }} onClick={() => handleOpenResetModal(s)} title="Send Password Reset Link">🔑</button>
                            <button className="btn btn-secondary btn-sm" style={{ padding: '3px 8px', fontSize: '11px' }} onClick={() => handleToggleStatus(s.id, s.status || 'inactive')} title={isActive ? 'Deactivate' : 'Activate'}>
                              {isActive ? '🔴' : '🟢'}
                            </button>
                            <button className="btn btn-secondary btn-sm" style={{ padding: '3px 8px', fontSize: '11px', color: 'var(--danger)' }} onClick={() => handleDeleteStudent(s.id, s.name, s.studentCode)} title="Delete Student Record">🗑️</button>
                          </div>
                        </td>
                      </tr>
                    );
                  })
                )}
              </tbody>
            </table>
          </div>
        </div>
          </>
        )}
      </main>

      {/* View Student Modal */}
      {viewModalOpen && selectedStudent && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 20000, padding: '20px' }}>
          <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '460px', width: '90%', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '15px' }}>👤 Student Information</h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', fontSize: '13px' }}>
              <div><strong>Full Name:</strong> {selectedStudent.name}</div>
              <div><strong>Email Address:</strong> {selectedStudent.email}</div>
              <div><strong>Date of Birth:</strong> {formatToDDMMYYYY(selectedStudent.dob) || '—'}</div>
              <div><strong>Parent Email:</strong> {selectedStudent.parentEmail || '—'}</div>
              <div><strong>Fee Status:</strong> <span className="badge badge-info">{selectedStudent.feeStatus || 'pending'}</span></div>
              <div><strong>Overall Mastery Index:</strong> {selectedStudent.overallMastery !== undefined ? `${Math.round(selectedStudent.overallMastery)}%` : '—'}</div>
              <div><strong>Autonomous Mode:</strong> {selectedStudent.autonomous ? '✅ Yes' : '❌ No'}</div>
              <div><strong>Sleep Curfew Bypass:</strong> {selectedStudent.curfewBypass ? '🟢 Bypassed' : '🔴 Normal Curfew (Default)'}</div>
              <div><strong>Presence State:</strong> {selectedStudent.presenceState ? (selectedStudent.presenceState === 'active' ? '🟢 Active' : '⚪ Idle/Away') : '—'}</div>
              <div><strong>Last Activity Time:</strong> {selectedStudent.lastActiveAt ? new Date(selectedStudent.lastActiveAt.seconds ? selectedStudent.lastActiveAt.seconds * 1000 : selectedStudent.lastActiveAt).toLocaleString() : '—'}</div>
              <div><strong>Current Active Page:</strong> {selectedStudent.currentPage ? `📄 ${selectedStudent.currentPage} (${selectedStudent.currentPagePath})` : '—'}</div>
            </div>
            
            {/* Practice Guard / Curfew Alerts Section */}
            <div style={{ marginTop: '16px', borderTop: '1px solid var(--border-light)', paddingTop: '16px' }}>
              <h4 style={{ fontSize: '12px', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '6px', color: 'var(--text)', marginBottom: '8px' }}>
                ⚠️ Practice Honesty Alerts
              </h4>
              {loadingAlerts ? (
                <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Loading safety alerts...</div>
              ) : honestyAlerts.length === 0 ? (
                <div style={{ fontSize: '11px', color: 'var(--success)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                  🟢 No suspected grinding or curfew issues logged.
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '150px', overflowY: 'auto', paddingRight: '4px' }}>
                  {honestyAlerts.map((topicAlert: any, idx: number) => (
                    <div key={idx} style={{ background: 'rgba(239, 68, 68, 0.08)', border: '1px solid rgba(239, 68, 68, 0.2)', borderRadius: '6px', padding: '8px 10px', fontSize: '11px' }}>
                      <div style={{ fontWeight: 700, color: 'var(--danger)', marginBottom: '3px' }}>
                        {topicAlert.chapterName || 'General'} - {topicAlert.topicName}
                      </div>
                      {topicAlert.alerts.map((al: any, aIdx: number) => (
                        <div key={aIdx} style={{ marginTop: '4px', borderTop: '1px dashed rgba(239, 68, 68, 0.15)', paddingTop: '4px', color: 'var(--text-muted)' }}>
                          • <strong>Suspected Grinding Alert</strong> (Confirm study clicked but no improvement)
                          <div style={{ fontSize: '10px', marginTop: '2px' }}>
                            Time: {new Date(al.timestamp).toLocaleString()} | Attempt Qs: {al.questionsAttempted} | Mastery: {Math.round(al.masteryBefore || 0)}% → {Math.round(al.masteryAfter || 0)}%
                          </div>
                        </div>
                      ))}
                    </div>
                  ))}
                </div>
              )}
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '20px' }}>
              <button className="btn btn-secondary" onClick={() => setViewModalOpen(false)}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Edit Student Modal */}
      {editModalOpen && selectedStudent && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 20000, padding: '12px' }}>
          <form onSubmit={handleSaveEdit} className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', padding: '16px 20px', borderRadius: 'var(--radius-lg)', maxWidth: '560px', width: '95%', maxHeight: '92vh', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '10px', boxShadow: 'var(--shadow-lg)' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px', margin: 0 }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800 }}>✏️ Edit Profile: {selectedStudent.name}</h3>
              <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontFamily: 'monospace' }}>{selectedStudent.studentCode || ''}</span>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '10px' }}>
              <div className="form-group" style={{ margin: 0 }}>
                <label style={{ fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', color: 'var(--text-muted)' }}>Student Name</label>
                <input 
                  type="text" 
                  className="form-input" 
                  value={editFormData.name} 
                  onChange={(e) => setEditFormData(prev => ({ ...prev, name: e.target.value }))}
                  style={{ padding: '6px 10px', fontSize: '13px' }}
                  required
                />
              </div>

              <div className="form-group" style={{ margin: 0 }}>
                <label style={{ fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', color: 'var(--text-muted)' }}>Date of Birth (DD/MM/YYYY)</label>
                <div style={{ position: 'relative', display: 'flex', alignItems: 'center' }}>
                  <input 
                    type="text" 
                    className="form-input" 
                    placeholder="DD/MM/YYYY (e.g. 05/03/2012)"
                    value={editFormData.dob} 
                    onChange={(e) => setEditFormData(prev => ({ ...prev, dob: e.target.value }))}
                    style={{ padding: '6px 32px 6px 10px', fontSize: '13px', width: '100%' }}
                  />
                  <input 
                    type="date"
                    tabIndex={-1}
                    value={formatToYYYYMMDD(editFormData.dob)}
                    onChange={(e) => {
                      if (e.target.value) {
                        setEditFormData(prev => ({ ...prev, dob: formatToDDMMYYYY(e.target.value) }));
                      }
                    }}
                    style={{
                      position: 'absolute',
                      right: '6px',
                      width: '24px',
                      height: '24px',
                      opacity: 0,
                      cursor: 'pointer',
                      zIndex: 2
                    }}
                  />
                  <span style={{ position: 'absolute', right: '8px', pointerEvents: 'none', fontSize: '14px', opacity: 0.7 }}>
                    📅
                  </span>
                </div>
              </div>
            </div>

            <div className="form-group" style={{ margin: 0 }}>
              <label style={{ fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', color: 'var(--text-muted)' }}>Parent Email Address</label>
              <input 
                type="email" 
                className="form-input" 
                value={editFormData.parentEmail} 
                onChange={(e) => setEditFormData(prev => ({ ...prev, parentEmail: e.target.value }))}
                style={{ padding: '6px 10px', fontSize: '13px' }}
              />
            </div>

            <div className="form-group" style={{ margin: 0 }}>
              <label style={{ fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', color: 'var(--text-muted)' }}>Batches (Select Multiple)</label>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', border: '1px solid var(--border-light)', padding: '6px 10px', borderRadius: 'var(--radius-sm)', background: 'var(--bg-soft)', maxHeight: '90px', overflowY: 'auto' }}>
                {batches.map(b => {
                  const checked = editFormData.batchIds.includes(b.id);
                  return (
                    <label key={b.id} style={{ display: 'inline-flex', alignItems: 'center', gap: '5px', fontSize: '11px', fontWeight: 600, padding: '3px 8px', borderRadius: '4px', background: checked ? 'rgba(59, 130, 246, 0.2)' : 'transparent', border: checked ? '1px solid #3b82f6' : '1px solid transparent', cursor: 'pointer' }}>
                      <input 
                        type="checkbox" 
                        checked={checked}
                        onChange={() => {
                          setEditFormData(prev => {
                            const nextIds = checked 
                              ? prev.batchIds.filter(id => id !== b.id)
                              : [...prev.batchIds, b.id];
                            return { ...prev, batchIds: nextIds };
                          });
                        }}
                      />
                      {b.name}
                    </label>
                  );
                })}
              </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '10px', background: 'var(--bg-soft)', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
              <div className="form-group" style={{ margin: 0 }}>
                <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px', fontWeight: 800, cursor: 'pointer' }}>
                  <input 
                    type="checkbox" 
                    checked={editFormData.autonomous}
                    onChange={(e) => setEditFormData(prev => ({ ...prev, autonomous: e.target.checked }))}
                  />
                  Autonomous Student Mode
                </label>
                <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginLeft: '18px', lineHeight: 1.2 }}>
                  Restricts subjective exams, blocks parent login.
                </div>
              </div>

              <div className="form-group" style={{ margin: 0 }}>
                <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px', fontWeight: 800, cursor: 'pointer' }}>
                  <input 
                    type="checkbox" 
                    checked={editFormData.curfewBypass}
                    onChange={(e) => setEditFormData(prev => ({ ...prev, curfewBypass: e.target.checked }))}
                  />
                  Bypass Sleep Curfew
                </label>
                <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginLeft: '18px', lineHeight: 1.2 }}>
                  Allows login during curfew (10:30 PM - 5:00 AM).
                </div>
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', paddingTop: '4px' }}>
              <button type="button" className="btn btn-secondary" style={{ padding: '6px 14px', fontSize: '12px' }} onClick={() => setEditModalOpen(false)}>Cancel</button>
              <button type="submit" className="btn btn-primary" style={{ padding: '6px 16px', fontSize: '12px', fontWeight: 700 }} disabled={savingEdit}>
                {savingEdit ? 'Saving...' : 'Save Changes'}
              </button>
            </div>
          </form>
        </div>
      )}
      {/* Password Reset Email Target Modal */}
      {resetModalOpen && resetTargetStudent && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 20000, padding: '20px' }}>
          <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '440px', width: '90%', display: 'flex', flexDirection: 'column', gap: '16px', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold', color: 'var(--text)', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px' }}>
              🔑 Send Reset Password Link
            </h3>
            
            <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
              Choose recipient(s) to receive the password reset link for student <strong>{resetTargetStudent.name}</strong>:
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '4px' }}>
              <label style={{ display: 'flex', alignItems: 'center', gap: '10px', padding: '10px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', cursor: 'pointer', border: resetSelection === 'student' ? '2px solid var(--accent)' : '2px solid transparent' }}>
                <input 
                  type="radio" 
                  name="resetTarget" 
                  value="student" 
                  checked={resetSelection === 'student'} 
                  onChange={() => setResetSelection('student')}
                />
                <div>
                  <strong style={{ display: 'block', fontSize: '13px' }}>Student Email</strong>
                  <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>{resetTargetStudent.email}</span>
                </div>
              </label>

              <label 
                style={{ 
                  display: 'flex', 
                  alignItems: 'center', 
                  gap: '10px', 
                  padding: '10px', 
                  background: resetTargetStudent.parentEmail ? 'var(--bg-soft)' : '#fee2e2', 
                  borderRadius: 'var(--radius-sm)', 
                  cursor: resetTargetStudent.parentEmail ? 'pointer' : 'not-allowed', 
                  border: resetSelection === 'parent' ? '2px solid var(--accent)' : '2px solid transparent',
                  opacity: resetTargetStudent.parentEmail ? 1 : 0.6
                }}
              >
                <input 
                  type="radio" 
                  name="resetTarget" 
                  value="parent" 
                  disabled={!resetTargetStudent.parentEmail}
                  checked={resetSelection === 'parent'} 
                  onChange={() => setResetSelection('parent')}
                />
                <div>
                  <strong style={{ display: 'block', fontSize: '13px' }}>Parent Email</strong>
                  <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                    {resetTargetStudent.parentEmail || 'Not registered'}
                  </span>
                </div>
              </label>

              <label 
                style={{ 
                  display: 'flex', 
                  alignItems: 'center', 
                  gap: '10px', 
                  padding: '10px', 
                  background: resetTargetStudent.parentEmail ? 'var(--bg-soft)' : '#fee2e2', 
                  borderRadius: 'var(--radius-sm)', 
                  cursor: resetTargetStudent.parentEmail ? 'pointer' : 'not-allowed', 
                  border: resetSelection === 'both' ? '2px solid var(--accent)' : '2px solid transparent',
                  opacity: resetTargetStudent.parentEmail ? 1 : 0.6
                }}
              >
                <input 
                  type="radio" 
                  name="resetTarget" 
                  value="both" 
                  disabled={!resetTargetStudent.parentEmail}
                  checked={resetSelection === 'both'} 
                  onChange={() => setResetSelection('both')}
                />
                <div>
                  <strong style={{ display: 'block', fontSize: '13px' }}>Both Emails</strong>
                  <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                    {resetTargetStudent.parentEmail ? `${resetTargetStudent.email} & ${resetTargetStudent.parentEmail}` : 'Parent email not registered'}
                  </span>
                </div>
              </label>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '12px' }}>
              <button 
                type="button" 
                className="btn btn-secondary" 
                onClick={() => {
                  setResetModalOpen(false);
                  setResetTargetStudent(null);
                }}
              >
                Cancel
              </button>
              <button 
                type="button" 
                className="btn btn-primary" 
                onClick={handleSendResetEmail}
                style={{ background: 'var(--accent-grad)', color: '#fff', border: 'none', fontWeight: 'bold' }}
              >
                Send Reset Link
              </button>
            </div>
          </div>
        </div>
      )}

      <ExportPdfModal
        isOpen={pdfSelectorOpen}
        onClose={() => setPdfSelectorOpen(false)}
        title="YASHCOM Student Accounts Registry"
        filename="Students_Registry.pdf"
        sections={[
          { id: 'roster', name: 'Student Accounts Roster Table', elementId: 'students-roster-section' }
        ]}
      />
    </div>
  );
}
