'use client';

import React, { useEffect, useState, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { formatDurationHM, formatDateTimeIST } from '@/lib/dateUtils';

interface UserActivity {
  uid: string;
  role: 'student' | 'parent';
  name: string;
  isAutonomous?: boolean;
  email: string;
  studentCode: string;
  lastLoginAt: string | null;
  currentPage: string;
  currentPagePath: string;
  currentPageAt: string | null;
  cumulativeSeconds: number;
}

export default function StudentActivityTable() {
  const { firebaseUser } = useAuth();
  const [activities, setActivities] = useState<UserActivity[]>([]);
  const [loading, setLoading] = useState(true);
  const [roleFilter, setRoleFilter] = useState<'student' | 'parent' | 'all'>('student');
  const [searchTerm, setSearchTerm] = useState('');
  const [sortBy, setSortBy] = useState<'loginTime' | 'cumulativeTime' | 'name'>('loginTime');
  const [sortDesc, setSortDesc] = useState(true);

  const toggleSort = (field: 'loginTime' | 'cumulativeTime' | 'name') => {
    if (sortBy === field) {
      setSortDesc(prev => !prev);
    } else {
      setSortBy(field);
      setSortDesc(field === 'name' ? false : true); // default asc for name, desc for times
    }
  };

  const fetchActivity = async () => {
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/student-activity', {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (res.ok) {
        const data = await res.json();
        setActivities(data.studentsActivity || []);
      }
    } catch (e) {
      console.warn('Failed to fetch user activity data:', e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchActivity();
  }, [firebaseUser]);

  const studentCount = useMemo(() => activities.filter(a => a.role === 'student').length, [activities]);
  const parentCount = useMemo(() => activities.filter(a => a.role === 'parent').length, [activities]);

  // Handle sorting, filtering and searching
  const filteredActivities = useMemo(() => {
    let result = activities;

    // Filter by role
    if (roleFilter !== 'all') {
      result = result.filter(a => a.role === roleFilter);
    }

    // Filter by search term
    if (searchTerm.trim()) {
      const term = searchTerm.toLowerCase();
      result = result.filter(
        a =>
          (a.name || '').toLowerCase().includes(term) ||
          (a.studentCode || '').toLowerCase().includes(term) ||
          (a.email || '').toLowerCase().includes(term)
      );
    }

    // Sort
    const sorted = [...result];
    sorted.sort((a, b) => {
      let comparison = 0;
      if (sortBy === 'loginTime') {
        const aTime = a.lastLoginAt ? new Date(a.lastLoginAt).getTime() : 0;
        const bTime = b.lastLoginAt ? new Date(b.lastLoginAt).getTime() : 0;
        comparison = bTime - aTime;
      } else if (sortBy === 'cumulativeTime') {
        comparison = b.cumulativeSeconds - a.cumulativeSeconds;
      } else if (sortBy === 'name') {
        comparison = (a.name || '').localeCompare(b.name || '');
      }
      
      if (sortBy === 'name') {
        return sortDesc ? -comparison : comparison;
      } else {
        return sortDesc ? comparison : -comparison;
      }
    });

    return sorted;
  }, [activities, roleFilter, searchTerm, sortBy, sortDesc]);

  const formatTime = formatDurationHM;
  const formatDateTime = (dateStr: string | null) => dateStr ? formatDateTimeIST(dateStr) : 'Never';

  if (loading) {
    return (
      <div className="card" style={{ padding: '32px', display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '150px' }}>
        <div className="spinner"></div> Loading Activity Logs...
      </div>
    );
  }

  const columnTitle = roleFilter === 'student' ? 'Student' : roleFilter === 'parent' ? 'Parent' : 'User';

  return (
    <div className="card" style={{
      background: 'var(--surface)',
      padding: '14px 16px',
      borderRadius: 'var(--radius)',
      border: '1px solid var(--border-light)',
      marginTop: '12px',
      boxShadow: 'var(--shadow-sm)'
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '12px', marginBottom: '14px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
          <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', margin: 0, display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span>🟢</span> Live Presence & Activity Monitor
          </h3>

          {/* Role Filter Tabs */}
          <div style={{
            display: 'flex',
            background: 'var(--bg-soft)',
            padding: '3px',
            borderRadius: 'var(--radius-md)',
            border: '1px solid var(--border-light)',
            gap: '2px'
          }}>
            <button
              onClick={() => setRoleFilter('student')}
              style={{
                padding: '4px 10px',
                fontSize: '12px',
                fontWeight: roleFilter === 'student' ? 700 : 500,
                borderRadius: 'var(--radius-sm)',
                border: 'none',
                background: roleFilter === 'student' ? 'var(--accent)' : 'transparent',
                color: roleFilter === 'student' ? '#fff' : 'var(--text-muted)',
                cursor: 'pointer',
                transition: 'all 0.15s ease'
              }}
            >
              👨‍🎓 Students ({studentCount})
            </button>
            <button
              onClick={() => setRoleFilter('parent')}
              style={{
                padding: '4px 10px',
                fontSize: '12px',
                fontWeight: roleFilter === 'parent' ? 700 : 500,
                borderRadius: 'var(--radius-sm)',
                border: 'none',
                background: roleFilter === 'parent' ? 'var(--accent)' : 'transparent',
                color: roleFilter === 'parent' ? '#fff' : 'var(--text-muted)',
                cursor: 'pointer',
                transition: 'all 0.15s ease'
              }}
            >
              👨‍👩‍👧 Parents ({parentCount})
            </button>
            <button
              onClick={() => setRoleFilter('all')}
              style={{
                padding: '4px 10px',
                fontSize: '12px',
                fontWeight: roleFilter === 'all' ? 700 : 500,
                borderRadius: 'var(--radius-sm)',
                border: 'none',
                background: roleFilter === 'all' ? 'var(--accent)' : 'transparent',
                color: roleFilter === 'all' ? '#fff' : 'var(--text-muted)',
                cursor: 'pointer',
                transition: 'all 0.15s ease'
              }}
            >
              👥 All ({activities.length})
            </button>
          </div>
        </div>
        
        <div style={{ display: 'flex', gap: '10px', alignItems: 'center', flexWrap: 'wrap' }}>
          {/* Refresh Button */}
          <button 
            onClick={fetchActivity}
            style={{
              padding: '6px 12px',
              fontSize: '12.5px',
              fontWeight: 600,
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--border-light)',
              background: 'var(--bg-soft)',
              color: 'var(--text)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '5px',
              transition: 'background 0.2s'
            }}
            onMouseOver={(e) => e.currentTarget.style.background = 'var(--border-light)'}
            onMouseOut={(e) => e.currentTarget.style.background = 'var(--bg-soft)'}
          >
            🔄 Refresh
          </button>

          {/* Search Field */}
          <input
            type="text"
            placeholder={`Search ${roleFilter === 'student' ? 'students' : roleFilter === 'parent' ? 'parents' : 'users'}...`}
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{
              padding: '6px 12px',
              fontSize: '12.5px',
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--border-light)',
              background: 'var(--bg-soft)',
              color: 'var(--text)',
              width: '190px'
            }}
          />
        </div>
      </div>

      {filteredActivities.length === 0 ? (
        <div style={{ padding: '28px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>
          No active {roleFilter === 'student' ? 'students' : roleFilter === 'parent' ? 'parents' : 'users'} found{searchTerm ? ' matching search.' : '.'}
        </div>
      ) : (
        <div style={{ overflowX: 'auto' }}>
          <table className="data-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13.5px' }}>
            <thead>
              <tr style={{ borderBottom: '1px solid var(--border-light)' }}>
                <th 
                  onClick={() => toggleSort('name')}
                  style={{ padding: '12px 10px', color: sortBy === 'name' ? 'var(--accent)' : 'var(--text-muted)', cursor: 'pointer', userSelect: 'none', textAlign: 'left' }}
                  title={`Click to sort by ${columnTitle.toLowerCase()}`}
                >
                  {columnTitle.toUpperCase()} {sortBy === 'name' ? (sortDesc ? '▼' : '▲') : '⇅'}
                </th>
                <th 
                  onClick={() => toggleSort('loginTime')}
                  style={{ padding: '12px 10px', color: sortBy === 'loginTime' ? 'var(--accent)' : 'var(--text-muted)', cursor: 'pointer', userSelect: 'none', textAlign: 'center' }}
                  title="Click to sort by latest login"
                >
                  LAST LOGIN {sortBy === 'loginTime' ? (sortDesc ? '▼' : '▲') : '⇅'}
                </th>
                <th 
                  onClick={() => toggleSort('cumulativeTime')}
                  style={{ padding: '12px 10px', color: sortBy === 'cumulativeTime' ? 'var(--accent)' : 'var(--text-muted)', cursor: 'pointer', userSelect: 'none', textAlign: 'center' }}
                  title="Click to sort by total spent"
                >
                  TOTAL SPENT {sortBy === 'cumulativeTime' ? (sortDesc ? '▼' : '▲') : '⇅'}
                </th>
                <th style={{ padding: '12px 10px', color: 'var(--text-muted)', textAlign: 'center' }}>CURRENT STATUS</th>
              </tr>
            </thead>
            <tbody>
              {filteredActivities.map((a) => {
                // If page open timestamp is within last 1 minute, show live green glow!
                const isLive = a.currentPageAt && (Date.now() - new Date(a.currentPageAt).getTime() < 60000);
                return (
                  <tr key={a.uid} style={{ borderBottom: '1px solid var(--border-light)' }}>
                    <td style={{ padding: '12px 10px', textAlign: 'left' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                        {isLive && <span style={{ fontSize: '12px' }}>🟢</span>}
                        <span style={{ fontWeight: 700, color: 'var(--text)' }}>{a.name}</span>
                        {a.role === 'student' && a.isAutonomous && (
                          <span 
                            title="Autonomous Student" 
                            style={{ 
                              fontSize: '10.5px', 
                              padding: '1px 6px', 
                              borderRadius: '10px', 
                              background: 'rgba(234, 179, 8, 0.15)', 
                              color: '#ca8a04',
                              fontWeight: 700 
                            }}
                          >
                            ⭐ Auto
                          </span>
                        )}
                        {roleFilter === 'all' && (
                          <span style={{
                            fontSize: '10px',
                            fontWeight: 700,
                            padding: '1px 6px',
                            borderRadius: '4px',
                            textTransform: 'uppercase',
                            background: a.role === 'student' ? 'rgba(59, 130, 246, 0.12)' : 'rgba(168, 85, 247, 0.12)',
                            color: a.role === 'student' ? 'var(--accent)' : '#a855f7',
                            border: `1px solid ${a.role === 'student' ? 'rgba(59, 130, 246, 0.25)' : 'rgba(168, 85, 247, 0.25)'}`
                          }}>
                            {a.role}
                          </span>
                        )}
                      </div>
                    </td>
                    <td style={{ padding: '12px 10px', color: 'var(--text)', textAlign: 'center' }}>
                      {formatDateTime(a.lastLoginAt)}
                    </td>
                    <td style={{ padding: '12px 10px', fontWeight: 700, color: 'var(--accent)', textAlign: 'center' }}>
                      {formatTime(a.cumulativeSeconds)}
                    </td>
                    <td style={{ padding: '12px 10px', textAlign: 'center' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', justifyContent: 'center' }}>
                        <span 
                          style={{
                            width: '8px',
                            height: '8px',
                            borderRadius: '50%',
                            background: isLive ? 'var(--success)' : 'var(--text-muted)',
                            boxShadow: isLive ? '0 0 8px var(--success)' : 'none',
                            display: 'inline-block'
                          }}
                        />
                        <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap', justifyContent: 'center' }}>
                          <span style={{ fontWeight: 600, color: isLive ? 'var(--text)' : 'var(--text-muted)' }}>
                            {(a.currentPage || '').replace(/^YASHCOM Learning OS\s*-\s*/i, '').trim()}
                          </span>
                          {a.currentPageAt && (
                            <span style={{ fontSize: '11px', color: 'var(--text-faint)' }}>
                              ({formatDateTime(a.currentPageAt)})
                            </span>
                          )}
                        </div>
                      </div>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
