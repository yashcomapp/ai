'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import dynamic from 'next/dynamic';
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });

interface Member {
  id: string;
  name: string;
  email: string;
  role: 'student' | 'parent';
  studentCode?: string;
  linkedStudentName?: string;
  lastActiveAt?: any;
  presenceState: 'active' | 'inactive';
  currentPage?: string;
  currentPagePath?: string;
}

interface BatchGroup {
  batchId: string;
  batchName: string;
  members: Member[];
}

import { formatLastActiveIST as formatLastActive, getDateKeyIST } from '@/lib/dateUtils';

interface LoginLogoutLog {
  id: string;
  uid: string;
  name: string;
  email: string;
  role: 'student' | 'parent';
  batchIds: string[];
  type: 'login' | 'logout';
  timestamp: string | null;
}

export default function LoginRegisterReportPage() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [batches, setBatches] = useState<BatchGroup[]>([]);
  const [logs, setLogs] = useState<LoginLogoutLog[]>([]);
  const [activeTab, setActiveTab] = useState<'roster' | 'register'>('register');
  const [selectedDate, setSelectedDate] = useState(getDateKeyIST());
  const [error, setError] = useState('');

  // Filtering & Sorting State
  const [searchQuery, setSearchQuery] = useState('');
  const [roleFilter, setRoleFilter] = useState<'all' | 'student' | 'parent'>('all');
  const [sortBy, setSortBy] = useState<'name' | 'lastActive' | 'status'>('lastActive');
  const [sortDesc, setSortDesc] = useState(true);
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);

  const fetchReportData = async () => {
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/reports/login-register?date=${selectedDate}`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) throw new Error('Failed to load login register report.');
      const data = await res.json();
      setBatches(data.batches || []);
      setLogs(data.logs || []);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error fetching report records.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchReportData();
  }, [firebaseUser, selectedDate]);

  const handleSortToggle = (field: typeof sortBy) => {
    if (sortBy === field) {
      setSortDesc(prev => !prev);
    } else {
      setSortBy(field);
      setSortDesc(field === 'name' ? false : true);
    }
  };

  const getSortVal = (m: Member, col: typeof sortBy) => {
    if (col === 'name') return m.name.toLowerCase();
    if (col === 'status') return m.presenceState === 'active' ? 1 : 0;
    if (col === 'lastActive') {
      if (!m.lastActiveAt) return 0;
      return m.lastActiveAt.seconds 
        ? m.lastActiveAt.seconds * 1000 
        : new Date(m.lastActiveAt).getTime();
    }
    return 0;
  };

  // Process data locally inside each batch for display
  const processedBatches = batches.map(b => {
    // Filter
    const filteredMembers = b.members.filter(m => {
      // Role filter
      if (roleFilter !== 'all' && m.role !== roleFilter) return false;
      
      // Search query
      if (searchQuery) {
        const query = searchQuery.toLowerCase();
        const studentCodeVal = m.studentCode || '';
        const linkedName = m.linkedStudentName || '';
        return (
          m.name.toLowerCase().includes(query) ||
          m.email.toLowerCase().includes(query) ||
          studentCodeVal.toLowerCase().includes(query) ||
          linkedName.toLowerCase().includes(query)
        );
      }
      return true;
    });

    // Sort
    const sortedMembers = [...filteredMembers].sort((a, b) => {
      const aVal = getSortVal(a, sortBy);
      const bVal = getSortVal(b, sortBy);
      
      if (aVal < bVal) return sortDesc ? 1 : -1;
      if (aVal > bVal) return sortDesc ? -1 : 1;
      return 0;
    });

    return {
      ...b,
      members: sortedMembers
    };
  }).filter(b => b.members.length > 0); // Hide empty batches from view if filtered

  const getGroupedLogs = () => {
    // 1. Map parent logs to their children's batches
    const enrichedLogs = logs.map(log => {
      let logBatches = [...(log.batchIds || [])];
      
      if (log.role === 'parent') {
        const parentUser = batches.flatMap(b => b.members).find(m => m.id === log.uid);
        if (parentUser && parentUser.linkedStudentName) {
          const childStudent = batches.flatMap(b => b.members).find(m => m.role === 'student' && m.name === parentUser.linkedStudentName);
          if (childStudent) {
            batches.forEach(b => {
              if (b.members.some(m => m.id === childStudent.id) && !logBatches.includes(b.batchId)) {
                logBatches.push(b.batchId);
              }
            });
          }
        }
      }
      return {
        ...log,
        batchIds: logBatches
      };
    });

    // 2. Filter logs based on search query, role filter, etc.
    const filteredLogs = enrichedLogs.filter(log => {
      if (roleFilter !== 'all' && log.role !== roleFilter) return false;
      if (searchQuery) {
        const query = searchQuery.toLowerCase();
        return (
          log.name.toLowerCase().includes(query) ||
          log.email.toLowerCase().includes(query)
        );
      }
      return true;
    });

    // 3. Group by batch
    const grouped: { [batchId: string]: LoginLogoutLog[] } = {};
    batches.forEach(b => {
      grouped[b.batchId] = [];
    });
    const unassigned: LoginLogoutLog[] = [];

    filteredLogs.forEach(log => {
      if (log.batchIds && log.batchIds.length > 0) {
        log.batchIds.forEach(bId => {
          if (grouped[bId]) {
            grouped[bId].push(log);
          } else {
            if (!unassigned.some(existing => existing.id === log.id)) {
              unassigned.push(log);
            }
          }
        });
      } else {
        if (!unassigned.some(existing => existing.id === log.id)) {
          unassigned.push(log);
        }
      }
    });

    // 4. Sort each group's logs by timestamp
    const sortLogs = (list: LoginLogoutLog[]) => {
      return [...list].sort((a, b) => {
        const timeA = a.timestamp 
          ? ((a.timestamp as any).seconds ? (a.timestamp as any).seconds * 1000 : new Date(a.timestamp).getTime())
          : 0;
        const timeB = b.timestamp 
          ? ((b.timestamp as any).seconds ? (b.timestamp as any).seconds * 1000 : new Date(b.timestamp).getTime())
          : 0;
        return sortDesc ? timeB - timeA : timeA - timeB;
      });
    };

    const result = batches.map(b => ({
      batchId: b.batchId,
      batchName: b.batchName,
      logs: sortLogs(grouped[b.batchId])
    })).filter(b => b.logs.length > 0);

    if (unassigned.length > 0) {
      result.push({
        batchId: 'unassigned',
        batchName: 'Unassigned Logins & Logouts',
        logs: sortLogs(unassigned)
      });
    }

    return result;
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading Login &amp; Presence Register...
        </div>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <button 
            className="btn btn-secondary" 
            style={{ padding: '4px 10px', fontSize: '12px' }} 
            onClick={() => router.push('/admin')}
          >
            ← Dashboard
          </button>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Login Activity Register</h1>
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Student &amp; Parent login presence and page tracking grouped by batch</div>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          
          <button className="btn btn-primary" style={{ padding: '6px 12px', fontSize: '12px' }} onClick={() => setPdfSelectorOpen(true)}>📄 Export PDF</button>
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      {/* Main Workspace */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1000px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {error && (
          <div style={{ background: '#fee2e2', border: '1px solid #fecaca', padding: '12px', borderRadius: '4px', color: '#b91c1c', fontSize: '12px' }}>
            {error}
          </div>
        )}

        {/* Filters */}
        <div className="card" style={{ background: 'var(--surface)', padding: '15px 20px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', gap: '10px', flexWrap: 'wrap', alignItems: 'center' }}>
          <input 
            type="text" 
            className="form-input" 
            placeholder="🔍 Search name, email, student code..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{ flex: 1, minWidth: '200px' }}
          />

          <select 
            className="form-input" 
            value={roleFilter} 
            onChange={(e) => setRoleFilter(e.target.value as any)}
            style={{ width: '150px' }}
          >
            <option value="all">All Roles</option>
            <option value="student">Students Only</option>
            <option value="parent">Parents Only</option>
          </select>

          <input 
            type="date"
            className="form-input"
            value={selectedDate}
            onChange={(e) => setSelectedDate(e.target.value)}
            style={{ width: '150px' }}
            title="Select log date"
          />

          <div style={{ display: 'flex', gap: '6px', fontSize: '12px', color: 'var(--text-muted)' }}>
            <span style={{ alignSelf: 'center' }}>Sort by:</span>
            <button 
              onClick={() => handleSortToggle('lastActive')}
              className={`btn btn-sm ${sortBy === 'lastActive' ? 'btn-primary' : 'btn-secondary'}`}
              style={{ padding: '3px 8px', fontSize: '11px' }}
            >
              Time {sortBy === 'lastActive' ? (sortDesc ? '▼' : '▲') : ''}
            </button>
            <button 
              onClick={() => handleSortToggle('name')}
              className={`btn btn-sm ${sortBy === 'name' ? 'btn-primary' : 'btn-secondary'}`}
              style={{ padding: '3px 8px', fontSize: '11px' }}
            >
              Name {sortBy === 'name' ? (sortDesc ? '▼' : '▲') : ''}
            </button>
            <button 
              onClick={() => handleSortToggle('status')}
              className={`btn btn-sm ${sortBy === 'status' ? 'btn-primary' : 'btn-secondary'}`}
              style={{ padding: '3px 8px', fontSize: '11px' }}
            >
              Status {sortBy === 'status' ? (sortDesc ? '▼' : '▲') : ''}
            </button>
          </div>
        </div>

        {/* Tab Selection */}
        <div style={{ display: 'flex', gap: '8px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '10px' }}>
          <button 
            onClick={() => setActiveTab('register')}
            style={{
              background: activeTab === 'register' ? 'var(--accent)' : 'none',
              color: activeTab === 'register' ? '#fff' : 'var(--text)',
              border: activeTab === 'register' ? 'none' : '1px solid var(--border-light)',
              padding: '8px 16px',
              borderRadius: 'var(--radius)',
              cursor: 'pointer',
              fontWeight: 600,
              fontSize: '13px'
            }}
          >
            📋 Today's Login/Logout Register
          </button>
          <button 
            onClick={() => setActiveTab('roster')}
            style={{
              background: activeTab === 'roster' ? 'var(--accent)' : 'none',
              color: activeTab === 'roster' ? '#fff' : 'var(--text)',
              border: activeTab === 'roster' ? 'none' : '1px solid var(--border-light)',
              padding: '8px 16px',
              borderRadius: 'var(--radius)',
              cursor: 'pointer',
              fontWeight: 600,
              fontSize: '13px'
            }}
          >
            🟢 Active Presence Snap
          </button>
        </div>

        {/* Grouped Lists (Either Roster or Register Timeline) */}
        <div id="login-register-roster-section" style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {activeTab === 'roster' ? (
            processedBatches.length === 0 ? (
              <div className="card" style={{ background: 'var(--surface)', padding: '40px', textAlign: 'center', color: 'var(--text-muted)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
                📭 No active login presence records match your filters.
              </div>
            ) : (
              processedBatches.map(b => (
                <div key={b.batchId} className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '16px 20px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--accent)', margin: 0, borderBottom: '1px solid var(--border-light)', paddingBottom: '6px', display: 'flex', justifyContent: 'space-between' }}>
                    <span>📦 {b.batchName}</span>
                    <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>{b.members.length} members</span>
                  </h3>
                  
                  <div style={{ overflowX: 'auto' }}>
                    <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px', textAlign: 'left' }}>
                      <thead>
                        <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                          <th style={{ padding: '8px 12px' }}>User Name</th>
                          <th style={{ padding: '8px 12px' }}>Role</th>
                          <th style={{ padding: '8px 12px' }}>Email</th>
                          <th style={{ padding: '8px 12px' }}>Last Active presence</th>
                          <th style={{ padding: '8px 12px' }}>Active Page</th>
                        </tr>
                      </thead>
                      <tbody>
                        {b.members.map(m => {
                          const isStudent = m.role === 'student';
                          const activeTime = m.lastActiveAt ? new Date((m.lastActiveAt as any).seconds ? (m.lastActiveAt as any).seconds * 1000 : m.lastActiveAt).getTime() : 0;
                          const isOnline = m.presenceState === 'active' && activeTime > 0 && (Date.now() - activeTime) < 300000;
                          
                          return (
                            <tr key={m.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                              <td style={{ padding: '10px 12px', fontWeight: 600 }}>
                                <div style={{ display: 'flex', flexDirection: 'column' }}>
                                  <span>{m.name}</span>
                                  {m.role === 'parent' && m.linkedStudentName && (
                                    <span style={{ fontSize: '10px', color: 'var(--text-muted)', fontWeight: 'normal' }}>
                                      Parent of: {m.linkedStudentName}
                                    </span>
                                  )}
                                </div>
                              </td>
                              <td style={{ padding: '10px 12px' }}>
                                <span style={{ 
                                  fontSize: '10px', 
                                  padding: '2px 8px', 
                                  borderRadius: '4px', 
                                  background: isStudent ? 'rgba(59, 130, 246, 0.15)' : 'rgba(168, 85, 247, 0.15)', 
                                  color: isStudent ? '#3b82f6' : '#a855f7',
                                  fontWeight: 700 
                                }}>
                                  {isStudent ? 'Student' : 'Parent'}
                                </span>
                              </td>
                              <td style={{ padding: '10px 12px' }}>{m.email}</td>
                              <td style={{ padding: '10px 12px' }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                                  <span style={{ 
                                    width: '8px', 
                                    height: '8px', 
                                    borderRadius: '50%', 
                                    background: isOnline ? '#1aa54e' : '#888' 
                                  }} />
                                  <span>{formatLastActive(m.lastActiveAt)}</span>
                                </div>
                              </td>
                              <td style={{ padding: '10px 12px', color: 'var(--text-muted)', fontSize: '12px' }}>
                                {m.currentPage ? (
                                  <span title={m.currentPagePath || ''}>
                                    📄 {m.currentPage}
                                  </span>
                                ) : (
                                  '—'
                                )}
                              </td>
                            </tr>
                          );
                        })}
                      </tbody>
                    </table>
                  </div>
                </div>
              ))
            )
          ) : (
            getGroupedLogs().length === 0 ? (
              <div className="card" style={{ background: 'var(--surface)', padding: '40px', textAlign: 'center', color: 'var(--text-muted)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
                📭 No login/logout records since 12 AM today match your filters.
              </div>
            ) : (
              getGroupedLogs().map(b => (
                <div key={b.batchId} className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '16px 20px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--accent)', margin: 0, borderBottom: '1px solid var(--border-light)', paddingBottom: '6px', display: 'flex', justifyContent: 'space-between' }}>
                    <span>📦 {b.batchName}</span>
                    <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>{b.logs.length} events today</span>
                  </h3>
                  
                  <div style={{ overflowX: 'auto' }}>
                    <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px', textAlign: 'left' }}>
                      <thead>
                        <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                          <th style={{ padding: '8px 12px' }}>Time</th>
                          <th style={{ padding: '8px 12px' }}>User Name</th>
                          <th style={{ padding: '8px 12px' }}>Role</th>
                          <th style={{ padding: '8px 12px' }}>Email</th>
                          <th style={{ padding: '8px 12px' }}>Action</th>
                        </tr>
                      </thead>
                      <tbody>
                        {b.logs.map(log => {
                          const isStudent = log.role === 'student';
                          const isLogin = log.type === 'login';
                          const timeStr = log.timestamp 
                            ? new Date((log.timestamp as any).seconds ? (log.timestamp as any).seconds * 1000 : log.timestamp).toLocaleTimeString('en-IN', {
                                hour: '2-digit',
                                minute: '2-digit',
                                second: '2-digit',
                                hour12: true
                              })
                            : '—';
                          
                          return (
                            <tr key={log.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                              <td style={{ padding: '10px 12px', fontWeight: 600 }}>{timeStr}</td>
                              <td style={{ padding: '10px 12px', fontWeight: 600 }}>{log.name}</td>
                              <td style={{ padding: '10px 12px' }}>
                                <span style={{ 
                                  fontSize: '10px', 
                                  padding: '2px 8px', 
                                  borderRadius: '4px', 
                                  background: isStudent ? 'rgba(59, 130, 246, 0.15)' : 'rgba(168, 85, 247, 0.15)', 
                                  color: isStudent ? '#3b82f6' : '#a855f7',
                                  fontWeight: 700 
                                }}>
                                  {isStudent ? 'Student' : 'Parent'}
                                </span>
                              </td>
                              <td style={{ padding: '10px 12px' }}>{log.email}</td>
                              <td style={{ padding: '10px 12px' }}>
                                <span style={{ 
                                  fontSize: '10px', 
                                  padding: '2px 8px', 
                                  borderRadius: '4px', 
                                  background: isLogin ? 'rgba(26, 165, 78, 0.15)' : 'rgba(239, 68, 68, 0.15)', 
                                  color: isLogin ? '#1aa54e' : '#ef4444',
                                  fontWeight: 700 
                                }}>
                                  {isLogin ? '🔑 LOGIN' : '🚪 LOGOUT'}
                                </span>
                              </td>
                            </tr>
                          );
                        })}
                      </tbody>
                    </table>
                  </div>
                </div>
              ))
            )
          )}
        </div>
      </main>

      <ExportPdfModal
        isOpen={pdfSelectorOpen}
        onClose={() => setPdfSelectorOpen(false)}
        title="YASHCOM User Logins &amp; Presence Register"
        filename="User_Login_Presence_Register.pdf"
        sections={[
          { id: 'register', name: 'User Presence &amp; Active Logins', elementId: 'login-register-roster-section' }
        ]}
      />
    </div>
  );
}
