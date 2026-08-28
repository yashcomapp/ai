'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import Link from 'next/link';
import dynamic from 'next/dynamic';
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });

interface Registration {
  id: string;
  studentName: string;
  studentEmail: string;
  studentMobile: string;
  dob: string;
  gender: string;
  bloodGroup: string;
  address: string;
  parentName: string;
  parentEmail: string;
  parentMobile: string;
  parentRelation: string;
  parentOccupation?: string;
  batchId: string;
  batchName: string;
  tempId: string;
  status: 'pending' | 'approved' | 'rejected';
  createdAt: string;
}

export default function RegistrationsPage() {
  const { firebaseUser, logout, user } = useAuth();
  const { toggleTheme } = useTheme();

  const [registrations, setRegistrations] = useState<Registration[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  
  // Search & Filter
  const [search, setSearch] = useState('');
  const [statusFilter, setStatusFilter] = useState('all');

  // Sorting and PDF export states
  const [sortField, setSortField] = useState<'tempId' | 'studentName' | 'createdAt' | 'batchName' | 'status'>('createdAt');
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('desc');
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);

  // Modals state
  const [selectedReg, setSelectedReg] = useState<Registration | null>(null);
  const [viewModalOpen, setViewModalOpen] = useState(false);
  const [editModalOpen, setEditModalOpen] = useState(false);

  // Edit fields
  const [editFields, setEditFields] = useState({
    studentName: '',
    studentEmail: '',
    studentMobile: '',
    dob: '',
    gender: '',
    bloodGroup: '',
    address: '',
    parentName: '',
    parentEmail: '',
    parentMobile: '',
    parentRelation: '',
    status: 'pending' as 'pending' | 'approved' | 'rejected',
    password: ''
  });

  const fetchRegistrations = async () => {
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/registrations', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (!res.ok) {
        throw new Error('Failed to load registrations');
      }
      const resData = await res.json();
      setRegistrations(resData.registrations || []);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Access Denied');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRegistrations();
  }, [firebaseUser]);

  const handleApprove = async (id: string) => {
    if (!confirm('Approve this registration? This will create student and parent accounts.')) return;
    
    setLoading(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/registrations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ id, action: 'approve' })
      });

      const resData = await res.json();
      if (!res.ok) {
        throw new Error(resData.message || 'Approval failed.');
      }

      alert(resData.message || 'Approved successfully!');
      fetchRegistrations();
    } catch (err: any) {
      alert(err.message);
      setLoading(false);
    }
  };

  const handleReject = async (id: string) => {
    if (!confirm('Reject this registration?')) return;
    
    setLoading(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/registrations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ id, action: 'reject' })
      });

      if (!res.ok) {
        const resData = await res.json();
        throw new Error(resData.message || 'Rejection failed.');
      }

      alert('Registration rejected.');
      fetchRegistrations();
    } catch (err: any) {
      alert(err.message);
      setLoading(false);
    }
  };

  const handleDelete = async (id: string) => {
    if (!confirm('⚠️ Permanently delete this registration? This cannot be undone.')) return;
    
    setLoading(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch(`/api/admin/registrations?id=${id}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${idToken}` }
      });

      if (!res.ok) {
        const resData = await res.json();
        throw new Error(resData.message || 'Deletion failed.');
      }

      alert('Registration deleted.');
      fetchRegistrations();
    } catch (err: any) {
      alert(err.message);
      setLoading(false);
    }
  };

  const handleOpenEdit = (reg: Registration) => {
    setSelectedReg(reg);
    setEditFields({
      studentName: reg.studentName || '',
      studentEmail: reg.studentEmail || '',
      studentMobile: reg.studentMobile || '',
      dob: reg.dob || '',
      gender: reg.gender || '',
      bloodGroup: reg.bloodGroup || '',
      address: reg.address || '',
      parentName: reg.parentName || '',
      parentEmail: reg.parentEmail || '',
      parentMobile: reg.parentMobile || '',
      parentRelation: reg.parentRelation || '',
      status: reg.status || 'pending',
      password: ''
    });
    setEditModalOpen(true);
  };

  const handleSaveEdit = async () => {
    if (!selectedReg) return;
    
    setLoading(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/registrations', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ id: selectedReg.id, updates: editFields })
      });

      if (!res.ok) {
        const resData = await res.json();
        throw new Error(resData.message || 'Failed to update registration.');
      }

      setEditModalOpen(false);
      setSelectedReg(null);
      alert('Registration updated successfully!');
      fetchRegistrations();
    } catch (err: any) {
      alert(err.message);
      setLoading(false);
    }
  };

  const filtered = registrations.filter(r => {
    const matchStatus = statusFilter === 'all' || r.status === statusFilter;
    const matchSearch = !search || [r.studentName, r.studentEmail, r.parentName, r.batchName, r.tempId]
      .some(v => v && v.toLowerCase().includes(search.toLowerCase()));
    return matchStatus && matchSearch;
  });

  const handleSort = (field: 'tempId' | 'studentName' | 'createdAt' | 'batchName' | 'status') => {
    if (sortField === field) {
      setSortDir(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortField(field);
      setSortDir('desc');
    }
  };

  const sortedFiltered = [...filtered].sort((a, b) => {
    let comparison = 0;
    if (sortField === 'tempId') {
      comparison = (a.tempId || '').localeCompare(b.tempId || '');
    } else if (sortField === 'studentName') {
      comparison = (a.studentName || '').localeCompare(b.studentName || '');
    } else if (sortField === 'batchName') {
      comparison = (a.batchName || '').localeCompare(b.batchName || '');
    } else if (sortField === 'status') {
      comparison = (a.status || '').localeCompare(b.status || '');
    } else {
      const dateA = a.createdAt ? new Date(a.createdAt).getTime() : 0;
      const dateB = b.createdAt ? new Date(b.createdAt).getTime() : 0;
      comparison = dateA - dateB;
    }
    return sortDir === 'asc' ? comparison : -comparison;
  });

  if (loading && registrations.length === 0) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading Registrations...
        </div>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh' }}>
      {/* Page Header */}
      <div className="page-header glass" style={{ padding: '8px 12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderRadius: '0', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <Link href="/admin" style={{ textDecoration: 'none' }}>
            <span className="brand" style={{ fontWeight: 800, fontSize: '1.2rem', color: 'var(--accent)', cursor: 'pointer' }}>YASHCOM</span>
          </Link>
          <div><h1 style={{ fontSize: '1.4rem', margin: '0' }}><Link href="/admin" style={{ color: 'inherit' }}>Admin Dashboard</Link> &gt; Registrations</h1></div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span className="badge badge-info">{user?.name || 'Admin'}</span>
          
          <button className="btn btn-primary" style={{ padding: '6px 12px', fontSize: '12px' }} onClick={() => setPdfSelectorOpen(true)}>📄 Export PDF</button>
          <button className="btn btn-secondary" onClick={logout} title="Logout" style={{ fontSize: '0.8rem', padding: '6px 12px' }}>🚪</button>
        </div>
      </div>

      <div className="main-content" style={{ maxWidth: '1300px', margin: '0 auto', padding: '24px 12px' }}>
        {/* Toolbar */}
        <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', alignItems: 'center', marginBottom: '20px' }}>
          <input 
            type="text" 
            placeholder="🔍 Search name, email, batch..." 
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            style={{ flex: 1, minWidth: '200px', padding: '8px 16px', border: '1px solid var(--border)', borderRadius: 'var(--radius-pill)', background: 'var(--surface)', color: 'var(--text)', fontSize: '13px' }}
          />
          <select 
            value={statusFilter} 
            onChange={(e) => setStatusFilter(e.target.value)}
            style={{ padding: '8px 12px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '13px' }}
          >
            <option value="all">All Status</option>
            <option value="pending">⏳ Pending</option>
            <option value="approved">✅ Approved</option>
            <option value="rejected">❌ Rejected</option>
          </select>
          <span className="count-chip" style={{ fontSize: '11px', color: 'var(--text-muted)', padding: '4px 12px', background: 'var(--surface-2)', borderRadius: '20px' }}>
            {filtered.length} records
          </span>
        </div>

        {error && (
          <div className="alert-box alert-box-danger" style={{ display: 'block', marginBottom: '20px' }}>
            {error}
          </div>
        )}

        {filtered.length === 0 ? (
          <div className="empty-state" style={{ padding: '40px', textAlign: 'center', color: 'var(--text-faint)' }}>📭 No registrations found.</div>
        ) : (
          <div id="registrations-roster-section" className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflowX: 'auto' }}>
            <table className="reg-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px' }}>
              <thead>
                <tr style={{ background: 'var(--surface-2)', borderBottom: '2px solid var(--border)' }}>
                  <th onClick={() => handleSort('tempId')} style={{ padding: '12px 10px', textAlign: 'left', color: 'var(--text-muted)', cursor: 'pointer', userSelect: 'none' }}>
                    Temp ID {sortField === 'tempId' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                  </th>
                  <th onClick={() => handleSort('studentName')} style={{ padding: '12px 10px', textAlign: 'left', color: 'var(--text-muted)', cursor: 'pointer', userSelect: 'none' }}>
                    Student Details {sortField === 'studentName' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                  </th>
                  <th onClick={() => handleSort('batchName')} style={{ padding: '12px 10px', textAlign: 'left', color: 'var(--text-muted)', cursor: 'pointer', userSelect: 'none' }}>
                    Batch Name {sortField === 'batchName' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                  </th>
                  <th style={{ padding: '12px 10px', textAlign: 'left', color: 'var(--text-muted)' }}>Parent Details</th>
                  <th onClick={() => handleSort('createdAt')} style={{ padding: '12px 10px', textAlign: 'left', color: 'var(--text-muted)', cursor: 'pointer', userSelect: 'none' }}>
                    Submitted Date {sortField === 'createdAt' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                  </th>
                  <th onClick={() => handleSort('status')} style={{ padding: '12px 10px', textAlign: 'left', color: 'var(--text-muted)', cursor: 'pointer', userSelect: 'none' }}>
                    Status {sortField === 'status' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                  </th>
                  <th style={{ padding: '12px 10px', textAlign: 'left', color: 'var(--text-muted)' }}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {sortedFiltered.map((reg) => (
                  <tr key={reg.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                    <td style={{ padding: '10px' }}><code>{reg.tempId || '-'}</code></td>
                    <td style={{ padding: '10px' }}>
                      <strong>{reg.studentName}</strong>
                      <div style={{ color: 'var(--text-muted)', fontSize: '10px' }}>{reg.studentEmail}</div>
                    </td>
                    <td style={{ padding: '10px' }}>{reg.batchName}</td>
                    <td style={{ padding: '10px' }}>
                      {reg.parentName}
                      <div style={{ color: 'var(--text-muted)', fontSize: '10px' }}>{reg.parentEmail}</div>
                    </td>
                    <td style={{ padding: '10px' }}>{new Date(reg.createdAt).toLocaleDateString('en-IN')}</td>
                    <td style={{ padding: '10px' }}>
                      <span className={`badge ${reg.status === 'approved' ? 'badge-success' : reg.status === 'rejected' ? 'badge-danger' : 'badge-warning'}`}>
                        {reg.status === 'approved' ? '✅ Approved' : reg.status === 'rejected' ? '❌ Rejected' : '⏳ Pending'}
                      </span>
                    </td>
                    <td style={{ padding: '10px' }}>
                      <div style={{ display: 'flex', gap: '6px' }}>
                        <button className="btn btn-secondary" style={{ fontSize: '10px', padding: '4px 8px' }} onClick={() => { setSelectedReg(reg); setViewModalOpen(true); }} title="View">👁</button>
                        <button className="btn btn-primary" style={{ fontSize: '10px', padding: '4px 8px' }} onClick={() => handleOpenEdit(reg)} title="Edit">✏️</button>
                        {reg.status === 'pending' && (
                          <>
                            <button className="btn btn-success" style={{ fontSize: '10px', padding: '4px 8px' }} onClick={() => handleApprove(reg.id)} title="Approve">✅</button>
                            <button className="btn btn-danger" style={{ fontSize: '10px', padding: '4px 8px' }} onClick={() => handleReject(reg.id)} title="Reject">❌</button>
                          </>
                        )}
                        <button className="btn btn-danger" style={{ fontSize: '10px', padding: '4px 8px' }} onClick={() => handleDelete(reg.id)} title="Delete">🗑</button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* View Details Modal */}
      {viewModalOpen && selectedReg && (
        <div className="modal show" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'rgba(0,0,0,0.5)', zIndex: 9999 }}>
          <div className="modal-content" style={{ maxWidth: '560px', margin: 'auto' }}>
            <div className="modal-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 16px', borderBottom: '1px solid var(--border-light)' }}>
              <h4>📋 Registration Details</h4>
              <button onClick={() => { setViewModalOpen(false); setSelectedReg(null); }} style={{ background: 'transparent', border: 'none', cursor: 'pointer', fontSize: '1.2rem' }}>✕</button>
            </div>
            <div className="modal-body" style={{ padding: '20px' }}>
              <div className="detail-grid" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px 20px', fontSize: '13px' }}>
                <div style={{ gridColumn: '1/-1', fontWeight: 'bold', color: 'var(--accent)', borderBottom: '1px solid var(--border-light)', paddingBottom: '4px' }}>👨‍🎓 STUDENT</div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Name</label><span>{selectedReg.studentName}</span></div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Temp ID</label><span style={{ color: 'var(--accent)', fontWeight: 'bold' }}>{selectedReg.tempId}</span></div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Email</label><span>{selectedReg.studentEmail}</span></div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Mobile</label><span>{selectedReg.studentMobile}</span></div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>DOB</label><span>{selectedReg.dob}</span></div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Gender</label><span>{selectedReg.gender}</span></div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Blood Group</label><span>{selectedReg.bloodGroup}</span></div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Batch</label><span>{selectedReg.batchName}</span></div>
                <div style={{ gridColumn: '1/-1' }}><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Address</label><span>{selectedReg.address}</span></div>
                
                <div style={{ gridColumn: '1/-1', fontWeight: 'bold', color: 'var(--accent)', borderBottom: '1px solid var(--border-light)', paddingBottom: '4px', marginTop: '12px' }}>👨‍👩‍👧 PARENT</div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Name</label><span>{selectedReg.parentName}</span></div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Relation</label><span>{selectedReg.parentRelation}</span></div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Email</label><span>{selectedReg.parentEmail}</span></div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Mobile</label><span>{selectedReg.parentMobile}</span></div>
                {selectedReg.parentOccupation && <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Occupation</label><span>{selectedReg.parentOccupation}</span></div>}

                <div style={{ gridColumn: '1/-1', fontWeight: 'bold', color: 'var(--accent)', borderBottom: '1px solid var(--border-light)', paddingBottom: '4px', marginTop: '12px' }}>📋 STATUS</div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Status</label><span>{selectedReg.status}</span></div>
                <div><label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Submitted</label><span>{new Date(selectedReg.createdAt).toLocaleString('en-IN')}</span></div>
              </div>
            </div>
            <div className="modal-footer" style={{ display: 'flex', gap: '8px', padding: '12px 16px', borderTop: '1px solid var(--border-light)', justifyContent: 'flex-end' }}>
              {selectedReg.status === 'pending' && (
                <>
                  <button className="btn btn-success" onClick={() => { handleApprove(selectedReg.id); setViewModalOpen(false); }}>Approve</button>
                  <button className="btn btn-danger" onClick={() => { handleReject(selectedReg.id); setViewModalOpen(false); }}>Reject</button>
                </>
              )}
              <button className="btn btn-secondary" onClick={() => { setViewModalOpen(false); setSelectedReg(null); }}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Edit Registration Modal */}
      {editModalOpen && selectedReg && (
        <div className="modal show" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 9999 }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', maxWidth: '540px', margin: 'auto' }}>
            <div className="modal-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 16px', borderBottom: '1px solid var(--border-light)' }}>
              <h4>✏️ Edit Registration</h4>
              <button onClick={() => { setEditModalOpen(false); setSelectedReg(null); }} style={{ background: 'transparent', border: 'none', cursor: 'pointer', fontSize: '1.2rem' }}>✕</button>
            </div>
            <div className="modal-body" style={{ padding: '20px' }}>
              <div className="edit-grid" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 12px', fontSize: '13px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>Student Name</label>
                  <input 
                    type="text" 
                    value={editFields.studentName}
                    onChange={(e) => setEditFields(prev => ({ ...prev, studentName: e.target.value }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>Student Email</label>
                  <input 
                    type="email" 
                    value={editFields.studentEmail}
                    onChange={(e) => setEditFields(prev => ({ ...prev, studentEmail: e.target.value }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>Student Mobile</label>
                  <input 
                    type="text" 
                    value={editFields.studentMobile}
                    onChange={(e) => setEditFields(prev => ({ ...prev, studentMobile: e.target.value }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>DOB</label>
                  <input 
                    type="date" 
                    value={editFields.dob}
                    onChange={(e) => setEditFields(prev => ({ ...prev, dob: e.target.value }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>Gender</label>
                  <select 
                    value={editFields.gender}
                    onChange={(e) => setEditFields(prev => ({ ...prev, gender: e.target.value }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  >
                    <option value="">-</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                  </select>
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>Blood Group</label>
                  <select 
                    value={editFields.bloodGroup}
                    onChange={(e) => setEditFields(prev => ({ ...prev, bloodGroup: e.target.value }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  >
                    <option value="">-</option>
                    <option value="A+">A+</option><option value="A-">A-</option>
                    <option value="B+">B+</option><option value="B-">B-</option>
                    <option value="O+">O+</option><option value="O-">O-</option>
                    <option value="AB+">AB+</option><option value="AB-">AB-</option>
                  </select>
                </div>
                <div style={{ gridColumn: '1/-1' }}>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>Address</label>
                  <input 
                    type="text" 
                    value={editFields.address}
                    onChange={(e) => setEditFields(prev => ({ ...prev, address: e.target.value }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>Parent Name</label>
                  <input 
                    type="text" 
                    value={editFields.parentName}
                    onChange={(e) => setEditFields(prev => ({ ...prev, parentName: e.target.value }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>Parent Email</label>
                  <input 
                    type="email" 
                    value={editFields.parentEmail}
                    onChange={(e) => setEditFields(prev => ({ ...prev, parentEmail: e.target.value }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>Parent Mobile</label>
                  <input 
                    type="text" 
                    value={editFields.parentMobile}
                    onChange={(e) => setEditFields(prev => ({ ...prev, parentMobile: e.target.value }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>Parent Relation</label>
                  <select 
                    value={editFields.parentRelation}
                    onChange={(e) => setEditFields(prev => ({ ...prev, parentRelation: e.target.value }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  >
                    <option value="">-</option>
                    <option value="Father">Father</option>
                    <option value="Mother">Mother</option>
                    <option value="Guardian">Guardian</option>
                  </select>
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>Status</label>
                  <select 
                    value={editFields.status}
                    onChange={(e) => setEditFields(prev => ({ ...prev, status: e.target.value as any }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  >
                    <option value="pending">⏳ Pending</option>
                    <option value="approved">✅ Approved</option>
                    <option value="rejected">❌ Rejected</option>
                  </select>
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)' }}>Password</label>
                  <input 
                    type="text" 
                    placeholder="Leave blank to keep existing"
                    value={editFields.password}
                    onChange={(e) => setEditFields(prev => ({ ...prev, password: e.target.value }))}
                    style={{ width: '100%', padding: '6px 10px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                </div>
              </div>
            </div>
            <div className="modal-footer" style={{ display: 'flex', gap: '8px', padding: '12px 16px', borderTop: '1px solid var(--border-light)', justifyContent: 'flex-end' }}>
              <button className="btn btn-primary" onClick={handleSaveEdit}>💾 Save Changes</button>
              <button className="btn btn-secondary" onClick={() => { setEditModalOpen(false); setSelectedReg(null); }}>Cancel</button>
            </div>
          </div>
        </div>
      )}
      <ExportPdfModal
        isOpen={pdfSelectorOpen}
        onClose={() => setPdfSelectorOpen(false)}
        title="Pending Admissions Registration Audits"
        filename="Registrations_Report.pdf"
        sections={[
          { id: 'roster', name: 'Pending Registrations Roster Table', elementId: 'registrations-roster-section' }
        ]}
      />
    </div>
  );
}
