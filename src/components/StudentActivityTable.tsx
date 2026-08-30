'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { formatDurationHM, formatDateTimeIST } from '@/lib/dateUtils';

interface StudentActivity {
  uid: string;
  name: string;
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
  const [activities, setActivities] = useState<StudentActivity[]>([]);
  const [filteredActivities, setFilteredActivities] = useState<StudentActivity[]>([]);
  const [loading, setLoading] = useState(true);
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
      console.warn('Failed to fetch student activity data:', e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchActivity();
  }, [firebaseUser]);

  // Handle sorting and searching
  useEffect(() => {
    let result = [...activities];

    // Filter by search term
    if (searchTerm.trim()) {
      const term = searchTerm.toLowerCase();
      result = result.filter(
        a =>
          a.name.toLowerCase().includes(term) ||
          a.studentCode.toLowerCase().includes(term) ||
          a.email.toLowerCase().includes(term)
      );
    }

    // Sort
    result.sort((a, b) => {
      let comparison = 0;
      if (sortBy === 'loginTime') {
        const aTime = a.lastLoginAt ? new Date(a.lastLoginAt).getTime() : 0;
        const bTime = b.lastLoginAt ? new Date(b.lastLoginAt).getTime() : 0;
        comparison = bTime - aTime;
      } else if (sortBy === 'cumulativeTime') {
        comparison = b.cumulativeSeconds - a.cumulativeSeconds;
      } else if (sortBy === 'name') {
        comparison = a.name.localeCompare(b.name);
      }
      
      if (sortBy === 'name') {
        return sortDesc ? -comparison : comparison;
      } else {
        return sortDesc ? comparison : -comparison;
      }
    });

    setFilteredActivities(result);
  }, [activities, searchTerm, sortBy, sortDesc]);

  const formatTime = formatDurationHM;
  const formatDateTime = (dateStr: string | null) => dateStr ? formatDateTimeIST(dateStr) : 'Never';

  if (loading) {
    return (
      <div className="card" style={{ padding: '32px', display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '150px' }}>
        <div className="spinner"></div> Loading Activity Logs...
      </div>
    );
  }

  return (
    <div className="card" style={{
      background: 'var(--surface)',
      padding: '12px 14px',
      borderRadius: 'var(--radius)',
      border: '1px solid var(--border-light)',
      marginTop: '10px',
      boxShadow: 'var(--shadow-sm)'
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px', marginBottom: '12px' }}>
        <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', margin: 0 }}>
          🟢 Live Student Activity & Presence Monitor
        </h3>
        
        <div style={{ display: 'flex', gap: '12px', alignItems: 'center', flexWrap: 'wrap' }}>
          {/* Refresh Button */}
          <button 
            onClick={fetchActivity}
            style={{
              padding: '6px 14px',
              fontSize: '13px',
              fontWeight: 600,
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--border-light)',
              background: 'var(--bg-soft)',
              color: 'var(--text)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
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
            placeholder="Search by name or code..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{
              padding: '6px 12px',
              fontSize: '13px',
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--border-light)',
              background: 'var(--bg-soft)',
              color: 'var(--text)',
              width: '200px'
            }}
          />

          {/* Removed duplicate Sort Select */}
        </div>
      </div>

      {filteredActivities.length === 0 ? (
        <div style={{ padding: '24px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>
          No active student logs found matching search.
        </div>
      ) : (
        <div style={{ overflowX: 'auto' }}>
          <table className="data-table" style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13.5px' }}>
            <thead>
              <tr style={{ borderBottom: '1px solid var(--border-light)' }}>
                <th 
                  onClick={() => toggleSort('name')}
                  style={{ padding: '12px 8px', color: sortBy === 'name' ? 'var(--accent)' : 'var(--text-muted)', cursor: 'pointer', userSelect: 'none', textAlign: 'left' }}
                  title="Click to sort by name"
                >
                  Student {sortBy === 'name' ? (sortDesc ? '▼' : '▲') : '⇅'}
                </th>
                <th 
                  onClick={() => toggleSort('loginTime')}
                  style={{ padding: '12px 8px', color: sortBy === 'loginTime' ? 'var(--accent)' : 'var(--text-muted)', cursor: 'pointer', userSelect: 'none', textAlign: 'center' }}
                  title="Click to sort by latest login"
                >
                  Last Login {sortBy === 'loginTime' ? (sortDesc ? '▼' : '▲') : '⇅'}
                </th>
                <th 
                  onClick={() => toggleSort('cumulativeTime')}
                  style={{ padding: '12px 8px', color: sortBy === 'cumulativeTime' ? 'var(--accent)' : 'var(--text-muted)', cursor: 'pointer', userSelect: 'none', textAlign: 'center' }}
                  title="Click to sort by total spent"
                >
                  Total Spent {sortBy === 'cumulativeTime' ? (sortDesc ? '▼' : '▲') : '⇅'}
                </th>
                <th style={{ padding: '12px 8px', color: 'var(--text-muted)', textAlign: 'center' }}>Current Status</th>
              </tr>
            </thead>
            <tbody>
              {filteredActivities.map((a) => {
                // If page open timestamp is within last 1 minute, show live green glow!
                const isLive = a.currentPageAt && (Date.now() - new Date(a.currentPageAt).getTime() < 60000);
                return (
                  <tr key={a.uid} style={{ borderBottom: '1px solid var(--border-light)' }}>
                    <td style={{ padding: '12px 8px', textAlign: 'left' }}>
                      <div style={{ fontWeight: 700, color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                        {isLive && <span style={{ fontSize: '12px' }}>🟢</span>}
                        <span>{a.name}</span>
                      </div>
                    </td>
                    <td style={{ padding: '12px 8px', color: 'var(--text)', textAlign: 'center' }}>
                      {formatDateTime(a.lastLoginAt)}
                    </td>
                    <td style={{ padding: '12px 8px', fontWeight: 700, color: 'var(--accent)', textAlign: 'center' }}>
                      {formatTime(a.cumulativeSeconds)}
                    </td>
                    <td style={{ padding: '12px 8px', textAlign: 'center' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', justifyContent: 'center' }}>
                        <span 
                          style={{
                            width: '8px',
                            height: '8px',
                            borderRadius: '50%',
                            background: isLive ? '#10b981' : '#d1d5db',
                            boxShadow: isLive ? '0 0 8px #10b981' : 'none',
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
