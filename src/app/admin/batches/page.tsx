'use client';

import React, { useEffect, useState, useMemo, useDeferredValue } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';

interface Batch {
  id: string;
  name: string;
  desc?: string;
  board?: string;
  class?: string;
  subjects?: string;
  rollPrefix?: string;
  academicYear?: string;
  zoomMeetingNumber?: string;
  zoomMeetingPasscode?: string;
  zoomMeetingActive?: boolean;
}

interface Student {
  id: string;
  name: string;
  email: string;
  studentCode?: string;
  rollNumber?: string;
  feeStatus?: string;
  batchIds: string[];
}

export default function AdminBatchesPage() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [batches, setBatches] = useState<Batch[]>([]);
  const [students, setStudents] = useState<Student[]>([]);
  const [error, setError] = useState('');

  const [searchQuery, setSearchQuery] = useState('');
  const [classFilter, setClassFilter] = useState('all');

  // Modals state
  const [selectedBatch, setSelectedBatch] = useState<Batch | null>(null);
  const [batchModalOpen, setBatchModalOpen] = useState(false);
  const [batchFormData, setBatchFormData] = useState({
    name: '',
    desc: '',
    board: '',
    class: '',
    subjects: '',
    rollPrefix: '',
    academicYear: '',
    zoomMeetingNumber: '',
    zoomMeetingPasscode: '',
    zoomMeetingActive: false
  });

  const [rosterModalOpen, setRosterModalOpen] = useState(false);
  const [rosterSearch, setRosterSearch] = useState('');
  const [addEmail, setAddEmail] = useState('');
  const [addingStudent, setAddingStudent] = useState(false);

  const [rollModalOpen, setRollModalOpen] = useState(false);
  const [rollStudent, setRollStudent] = useState<Student | null>(null);
  const [rollNumber, setRollNumber] = useState('');
  const [feeStatus, setFeeStatus] = useState('pending');
  const [savingRoll, setSavingRoll] = useState(false);

  const fetchBatches = async () => {
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/batches', {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) throw new Error('Failed to fetch batches list.');
      const data = await res.json();
      setBatches(data.batches || []);
      setStudents(data.students || []);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error loading batches.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchBatches();
  }, [firebaseUser]);

  // Open Batch Modal (Create/Edit)
  const handleOpenBatchModal = (batch?: Batch) => {
    if (batch) {
      setSelectedBatch(batch);
      setBatchFormData({
        name: batch.name || '',
        desc: batch.desc || '',
        board: batch.board || '',
        class: batch.class || '',
        subjects: batch.subjects || '',
        rollPrefix: batch.rollPrefix || '',
        academicYear: batch.academicYear || '',
        zoomMeetingNumber: batch.zoomMeetingNumber || '',
        zoomMeetingPasscode: batch.zoomMeetingPasscode || '',
        zoomMeetingActive: batch.zoomMeetingActive || false
      });
    } else {
      setSelectedBatch(null);
      setBatchFormData({
        name: '',
        desc: '',
        board: '',
        class: '',
        subjects: '',
        rollPrefix: '',
        academicYear: '',
        zoomMeetingNumber: '',
        zoomMeetingPasscode: '',
        zoomMeetingActive: false
      });
    }
    setBatchModalOpen(true);
  };

  const handleSaveBatch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!batchFormData.name.trim()) {
      alert('Batch Name is required.');
      return;
    }

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/batches', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'saveBatch',
          batchId: selectedBatch?.id || null,
          batchData: batchFormData
        })
      });
      if (!res.ok) throw new Error('Failed to save batch details.');
      setBatchModalOpen(false);
      await fetchBatches();
    } catch (err: any) {
      alert(err.message || 'Error saving batch.');
    }
  };

  const handleDeleteBatch = async (batchId: string, name: string) => {
    if (!confirm(`Are you sure you want to delete batch "${name}"? This unmaps all student members.`)) return;

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch(`/api/admin/batches?batchId=${batchId}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) throw new Error('Delete batch failed.');
      await fetchBatches();
    } catch (err: any) {
      alert(err.message || 'Deletion failed.');
    }
  };

  // Open Roster Modal (Manage Students in Batch)
  const handleOpenRosterModal = (batch: Batch) => {
    setSelectedBatch(batch);
    setRosterModalOpen(true);
    setAddEmail('');
    setRosterSearch('');
  };

  const handleAddStudent = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!addEmail.trim() || !selectedBatch) return;
    setAddingStudent(true);

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/batches', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'addStudent',
          batchId: selectedBatch.id,
          studentEmail: addEmail.trim()
        })
      });
      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.error || 'Failed to add student.');
      }
      setAddEmail('');
      await fetchBatches();
    } catch (err: any) {
      alert(err.message);
    } finally {
      setAddingStudent(false);
    }
  };

  const handleRemoveStudent = async (studentId: string) => {
    if (!selectedBatch) return;
    if (!confirm('Remove student from this batch?')) return;

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/batches', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'removeStudent',
          batchId: selectedBatch.id,
          studentId
        })
      });
      if (!res.ok) throw new Error('Failed to remove student.');
      await fetchBatches();
    } catch (err: any) {
      alert(err.message || 'Error removing student.');
    }
  };

  // Open Roll Modal (Assign Roll & Fee)
  const handleOpenRollModal = (student: Student) => {
    setRollStudent(student);
    setRollNumber(student.rollNumber || '');
    setFeeStatus(student.feeStatus || 'pending');
    setRollModalOpen(true);
  };

  const handleSaveRoll = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!rollStudent) return;
    setSavingRoll(true);

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/batches', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'updateRollAndFee',
          studentId: rollStudent.id,
          rollNumber,
          feeStatus
        })
      });
      if (!res.ok) throw new Error('Failed to update credentials.');
      setRollModalOpen(false);
      await fetchBatches();
    } catch (err: any) {
      alert(err.message || 'Update credentials failed.');
    } finally {
      setSavingRoll(false);
    }
  };

  const deferredSearch = useDeferredValue(searchQuery);
  const deferredRosterSearch = useDeferredValue(rosterSearch);

  // Filters
  const uniqueClasses = useMemo(() => Array.from(new Set(batches.map(b => b.class).filter(Boolean))), [batches]);
  
  const filteredBatches = useMemo(() => {
    const q = deferredSearch.toLowerCase().trim();
    return batches.filter(b => {
      if (classFilter !== 'all' && b.class !== classFilter) return false;
      if (q) {
        return (
          (b.name || '').toLowerCase().includes(q) ||
          (b.board || '').toLowerCase().includes(q) ||
          (b.class || '').toLowerCase().includes(q)
        );
      }
      return true;
    });
  }, [batches, classFilter, deferredSearch]);

  const filteredRoster = useMemo(() => {
    if (!selectedBatch) return [];
    const activeRoster = students.filter(s => s.batchIds?.includes(selectedBatch.id));
    const q = deferredRosterSearch.toLowerCase().trim();
    if (!q) return activeRoster;
    return activeRoster.filter(s => {
      const code = s.rollNumber || s.studentCode || '';
      return (
        s.name.toLowerCase().includes(q) ||
        s.email.toLowerCase().includes(q) ||
        code.toLowerCase().includes(q)
      );
    });
  }, [students, selectedBatch, deferredRosterSearch]);

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading course batches...
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
            <h1 style={{ fontSize: '16px', margin: 0 }}>Batches</h1>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          
          <button className="btn btn-primary" onClick={() => handleOpenBatchModal()}>+ New Batch</button>
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      {/* Main Container */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1000px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {/* Search */}
        <div className="card" style={{ background: 'var(--surface)', padding: '15px 20px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <input 
            type="text" 
            className="form-input" 
            placeholder="🔍 Search batch name, board, academic year..." 
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{ flex: 1, minWidth: '200px' }}
          />
          <div style={{ display: 'flex', gap: '6px' }}>
            <button 
              className={`btn ${classFilter === 'all' ? 'btn-primary' : 'btn-secondary'}`} 
              onClick={() => setClassFilter('all')}
              style={{ padding: '6px 12px', fontSize: '12px' }}
            >
              All
            </button>
            {uniqueClasses.map(c => (
              <button 
                key={c}
                className={`btn ${classFilter === c ? 'btn-primary' : 'btn-secondary'}`} 
                onClick={() => setClassFilter(c!)}
                style={{ padding: '6px 12px', fontSize: '12px' }}
              >
                Class {c}
              </button>
            ))}
          </div>
        </div>

        {/* Batches List Grid */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '16px' }}>
          {filteredBatches.length === 0 ? (
            <div className="card" style={{ padding: '40px', gridColumn: '1 / -1', textAlign: 'center', color: 'var(--text-muted)' }}>
              📭 No batches found matching active filters.
            </div>
          ) : (
            filteredBatches.map(b => {
              const members = students.filter(s => s.batchIds.includes(b.id));
              const paid = members.filter(s => s.feeStatus === 'paid').length;
              const pending = members.length - paid;

              return (
                <div key={b.id} className="card" style={{ background: 'var(--surface)', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '8px' }}>
                  <div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '8px' }}>
                      <span style={{ fontSize: '11px', background: 'var(--bg-soft)', border: '1px solid var(--border-light)', padding: '2px 8px', borderRadius: '10px', color: 'var(--accent)', fontWeight: 700 }}>
                        Class {b.class || '—'} • {b.board || 'CBSE'}
                      </span>
                      <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>{b.academicYear || '—'}</span>
                    </div>

                    <h3 style={{ fontSize: '14px', fontWeight: 800, margin: '4px 0' }}>{b.name}</h3>
                    {b.desc && <p style={{ fontSize: '12px', color: 'var(--text-muted)', lineHeight: 1.4, margin: '4px 0' }}>{b.desc}</p>}
                    
                    {b.subjects && (
                      <div style={{ marginTop: '8px', fontSize: '11px', color: 'var(--text-muted)' }}>
                        <strong>Subjects:</strong> {b.subjects}
                      </div>
                    )}
                    {b.rollPrefix && (
                      <div style={{ marginTop: '4px', fontSize: '11px', color: 'var(--text-muted)' }}>
                        <strong>Prefix:</strong> <code style={{ background: 'var(--bg-soft)', padding: '1px 4px', borderRadius: '3px' }}>{b.rollPrefix}</code>
                      </div>
                    )}
                  </div>

                  <div style={{ borderTop: '1px solid var(--border-light)', paddingTop: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                      <strong>{members.length}</strong> students ({paid} paid, {pending} pending)
                    </div>
                    <div style={{ display: 'flex', gap: '4px' }}>
                      <button className="btn btn-secondary btn-sm" style={{ padding: '4px 8px', fontSize: '11px' }} onClick={() => handleOpenRosterModal(b)}>👥 Roster</button>
                      <button className="btn btn-secondary btn-sm" style={{ padding: '4px 8px', fontSize: '11px' }} onClick={() => handleOpenBatchModal(b)}>✏️ Edit</button>
                      <button className="btn btn-secondary btn-sm" style={{ padding: '4px 8px', fontSize: '11px', color: 'var(--danger)' }} onClick={() => handleDeleteBatch(b.id, b.name)}>🗑️</button>
                    </div>
                  </div>
                </div>
              );
            })
          )}
        </div>
      </main>

      {/* Batch Edit/Create Modal */}
      {batchModalOpen && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 20000 }}>
          <form onSubmit={handleSaveBatch} className="card" style={{ 
            background: 'var(--surface)', 
            padding: '24px', 
            borderRadius: 'var(--radius-lg)', 
            maxWidth: '480px', 
            width: '90%', 
            maxHeight: '90vh',
            overflowY: 'auto',
            border: '1px solid var(--border-light)' 
          }}>
            <h3 style={{ borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '15px' }}>
              {selectedBatch ? '✏️ Edit Batch' : '➕ New Batch'}
            </h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <div className="form-group">
                <label style={{ fontSize: '12px', fontWeight: 600 }}>Batch Name *</label>
                <input 
                  type="text" 
                  className="form-input" 
                  value={batchFormData.name} 
                  onChange={(e) => setBatchFormData(prev => ({ ...prev, name: e.target.value }))}
                  required
                  placeholder="e.g., Class 10 - Mathematics (2024-25)"
                />
              </div>
              <div className="form-group">
                <label style={{ fontSize: '12px', fontWeight: 600 }}>Description</label>
                <textarea 
                  className="form-input" 
                  value={batchFormData.desc} 
                  onChange={(e) => setBatchFormData(prev => ({ ...prev, desc: e.target.value }))}
                  rows={2}
                  placeholder="Brief description of the batch..."
                />
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                <div className="form-group">
                  <label style={{ fontSize: '12px', fontWeight: 600 }}>Board</label>
                  <input 
                    type="text" 
                    className="form-input" 
                    value={batchFormData.board} 
                    onChange={(e) => setBatchFormData(prev => ({ ...prev, board: e.target.value }))}
                    placeholder="e.g., CBSE"
                  />
                </div>
                <div className="form-group">
                  <label style={{ fontSize: '12px', fontWeight: 600 }}>Class</label>
                  <input 
                    type="text" 
                    className="form-input" 
                    value={batchFormData.class} 
                    onChange={(e) => setBatchFormData(prev => ({ ...prev, class: e.target.value }))}
                    placeholder="e.g., 10"
                  />
                </div>
              </div>
              <div className="form-group">
                <label style={{ fontSize: '12px', fontWeight: 600 }}>Subjects (comma separated)</label>
                <input 
                  type="text" 
                  className="form-input" 
                  value={batchFormData.subjects} 
                  onChange={(e) => setBatchFormData(prev => ({ ...prev, subjects: e.target.value }))}
                  placeholder="e.g., Mathematics, Science"
                />
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                <div className="form-group">
                  <label style={{ fontSize: '12px', fontWeight: 600 }}>Roll Number Prefix</label>
                  <input 
                    type="text" 
                    className="form-input" 
                    value={batchFormData.rollPrefix} 
                    onChange={(e) => setBatchFormData(prev => ({ ...prev, rollPrefix: e.target.value }))}
                    placeholder="e.g., 10-"
                  />
                </div>
                <div className="form-group">
                  <label style={{ fontSize: '12px', fontWeight: 600 }}>Academic Year</label>
                  <input 
                    type="text" 
                    className="form-input" 
                    value={batchFormData.academicYear} 
                    onChange={(e) => setBatchFormData(prev => ({ ...prev, academicYear: e.target.value }))}
                    placeholder="e.g., 2024-25"
                  />
                </div>
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', borderTop: '1px dashed var(--border-light)', paddingTop: '10px', marginTop: '10px' }}>
                <div className="form-group">
                  <label style={{ fontSize: '12px', fontWeight: 600, color: 'var(--accent)' }}>Zoom Meeting Number</label>
                  <input 
                    type="text" 
                    className="form-input" 
                    value={batchFormData.zoomMeetingNumber} 
                    onChange={(e) => setBatchFormData(prev => ({ ...prev, zoomMeetingNumber: e.target.value }))}
                    placeholder="e.g., 89216852281"
                  />
                </div>
                <div className="form-group">
                  <label style={{ fontSize: '12px', fontWeight: 600, color: 'var(--accent)' }}>Zoom Passcode</label>
                  <input 
                    type="text" 
                    className="form-input" 
                    value={batchFormData.zoomMeetingPasscode} 
                    onChange={(e) => setBatchFormData(prev => ({ ...prev, zoomMeetingPasscode: e.target.value }))}
                    placeholder="e.g., yashcom"
                  />
                </div>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginTop: '12px', background: 'var(--bg-soft)', padding: '10px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)' }}>
                <input 
                  type="checkbox" 
                  id="zoomMeetingActive"
                  checked={batchFormData.zoomMeetingActive}
                  onChange={(e) => setBatchFormData(prev => ({ ...prev, zoomMeetingActive: e.target.checked }))}
                  style={{ width: '16px', height: '16px', cursor: 'pointer' }}
                />
                <label htmlFor="zoomMeetingActive" style={{ fontSize: '12px', fontWeight: 700, color: 'var(--success)', cursor: 'pointer', userSelect: 'none' }}>
                  🟢 Live Class is Running (Students can join)
                </label>
              </div>
            </div>
            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '20px' }}>
              <button type="button" className="btn btn-secondary" onClick={() => setBatchModalOpen(false)}>Cancel</button>
              <button type="submit" className="btn btn-primary">Save Batch</button>
            </div>
          </form>
        </div>
      )}

      {/* Manage Students Roster Modal */}
      {rosterModalOpen && selectedBatch && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 20000 }}>
          <div className="card" style={{ background: 'var(--surface)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '520px', width: '90%', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '15px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px' }}>
              <h3 style={{ margin: 0 }}>👥 Roster: {selectedBatch.name}</h3>
              <button className="btn btn-secondary btn-sm" onClick={() => setRosterModalOpen(false)}>✕</button>
            </div>

            {/* Add student row */}
            <form onSubmit={handleAddStudent} style={{ display: 'flex', gap: '8px' }}>
              <input 
                type="email" 
                className="form-input" 
                placeholder="Enter student email to add..." 
                value={addEmail}
                onChange={(e) => setAddEmail(e.target.value)}
                required
                style={{ flex: 1 }}
              />
              <button type="submit" className="btn btn-primary" disabled={addingStudent}>
                {addingStudent ? 'Adding...' : '+ Add'}
              </button>
            </form>

            <input 
              type="text" 
              className="form-input" 
              placeholder="🔍 Filter student members..." 
              value={rosterSearch}
              onChange={(e) => setRosterSearch(e.target.value)}
            />

            {/* Roster list */}
            <div style={{ maxHeight: '200px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: '4px', background: 'var(--bg-soft)' }}>
              {filteredRoster.length === 0 ? (
                <div style={{ padding: '24px', textAlign: 'center', color: 'var(--text-muted)' }}>No student members found.</div>
              ) : (
                filteredRoster.map(s => (
                  <div key={s.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 15px', borderBottom: '1px solid var(--border-light)' }}>
                    <div>
                      <div style={{ fontWeight: 600, fontSize: '13px' }}>{s.name}</div>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)', display: 'flex', gap: '8px', marginTop: '2px' }}>
                        <span>{s.email}</span>
                        {s.rollNumber && <span style={{ fontWeight: 700, color: 'var(--accent)' }}>• ID: {s.rollNumber}</span>}
                        <span style={{ fontSize: '10px', padding: '1px 5px', borderRadius: '4px', background: s.feeStatus === 'paid' ? '#dbf3e1' : '#eee', color: s.feeStatus === 'paid' ? '#1aa54e' : '#888' }}>
                          {s.feeStatus || 'pending'}
                        </span>
                      </div>
                    </div>
                    <div style={{ display: 'flex', gap: '4px' }}>
                      <button className="btn btn-secondary btn-sm" style={{ padding: '3px 8px', fontSize: '10px' }} onClick={() => handleOpenRollModal(s)}>🎫 ID / Fee</button>
                      <button className="btn btn-secondary btn-sm" style={{ padding: '3px 8px', fontSize: '10px', color: 'var(--danger)' }} onClick={() => handleRemoveStudent(s.id)}>Remove</button>
                    </div>
                  </div>
                ))
              )}
            </div>
          </div>
        </div>
      )}

      {/* Assign Roll Number and Fee Status Modal */}
      {rollModalOpen && rollStudent && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 21000 }}>
          <form onSubmit={handleSaveRoll} className="card" style={{ background: 'var(--surface)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '400px', width: '90%', border: '1px solid var(--border-light)' }}>
            <h3 style={{ borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '15px' }}>🎫 Student Credentials</h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <div><strong>Student Name:</strong> {rollStudent.name}</div>
              <div className="form-group">
                <label style={{ fontSize: '12px', fontWeight: 600 }}>Permanent Roll Number</label>
                <input 
                  type="text" 
                  className="form-input" 
                  value={rollNumber} 
                  onChange={(e) => setRollNumber(e.target.value)}
                  placeholder="e.g., 10-001"
                />
              </div>
              <div className="form-group">
                <label style={{ fontSize: '12px', fontWeight: 600 }}>Fee Payment Status</label>
                <select 
                  className="form-input" 
                  value={feeStatus}
                  onChange={(e) => setFeeStatus(e.target.value)}
                >
                  <option value="pending">Pending</option>
                  <option value="paid">Paid</option>
                  <option value="partial">Partial</option>
                </select>
              </div>
            </div>
            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '20px' }}>
              <button type="button" className="btn btn-secondary" onClick={() => setRollModalOpen(false)}>Cancel</button>
              <button type="submit" className="btn btn-primary" disabled={savingRoll}>
                {savingRoll ? 'Saving...' : 'Save & Update'}
              </button>
            </div>
          </form>
        </div>
      )}
    </div>
  );
}
