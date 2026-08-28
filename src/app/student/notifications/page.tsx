'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';

interface Notice {
  id: string;
  title: string;
  body: string;
  createdAt: string | null;
  type?: string;
  noticeDate?: string | null;
}

export default function StudentSeenNotificationsPage() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();
  const [loading, setLoading] = useState(true);
  const [notices, setNotices] = useState<Notice[]>([]);
  const [seenNoticeIds, setSeenNoticeIds] = useState<string[]>([]);
  const [error, setError] = useState('');

  const renderListSkeleton = () => (
    <div className="skeleton-blink" style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
      {[1, 2, 3].map(i => (
        <div 
          key={i} 
          className="card" 
          style={{ 
            background: 'var(--surface)', 
            borderRadius: 'var(--radius-lg)', 
            border: '1px solid var(--border-light)', 
            padding: '16px',
            display: 'flex',
            flexDirection: 'column',
            gap: '10px'
          }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
              <div style={{ width: '180px', height: '14px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
              <div style={{ width: '120px', height: '10px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
            </div>
            <div style={{ display: 'flex', gap: '6px' }}>
              <div style={{ width: '50px', height: '18px', background: 'var(--bg-soft)', borderRadius: '12px' }}></div>
              <div style={{ width: '60px', height: '18px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
            </div>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', marginTop: '4px' }}>
            <div style={{ width: '100%', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
            <div style={{ width: '90%', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
          </div>
        </div>
      ))}
    </div>
  );

  const loadNotificationsData = async () => {
    if (!firebaseUser) return;
    setLoading(true);
    try {
      // 1. Load seen IDs from localStorage
      const stored = localStorage.getItem('yc_seenNotices');
      let seenIds: string[] = [];
      if (stored) {
        seenIds = JSON.parse(stored);
        setSeenNoticeIds(seenIds);
      }

      // 2. Fetch all notices matching student from API
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/notices', {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        throw new Error('Failed to load announcements data.');
      }
      const data = await res.json();
      const fetchedNotices: Notice[] = data.notices || [];

      // 3. Set all notices directly
      setNotices(fetchedNotices);

      // 4. Synchronize seen status from server
      const serverSeenIds = fetchedNotices.filter((n: any) => n.seen).map((n: any) => n.id);
      const mergedSeen = Array.from(new Set([...seenIds, ...serverSeenIds]));
      const validSeenIds = mergedSeen.filter(id => fetchedNotices.some(n => n.id === id));

      localStorage.setItem('yc_seenNotices', JSON.stringify(validSeenIds));
      setSeenNoticeIds(validSeenIds);
      window.dispatchEvent(new Event('yc_seen_notices_changed'));
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error loading notifications.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (firebaseUser) {
      loadNotificationsData();
    }
  }, [firebaseUser]);

  const handleMarkAsSeen = (id: string) => {
    try {
      const updated = [...seenNoticeIds, id];
      setSeenNoticeIds(updated);
      localStorage.setItem('yc_seenNotices', JSON.stringify(updated));
      window.dispatchEvent(new Event('yc_seen_notices_changed'));

      firebaseUser?.getIdToken().then(idToken => {
        fetch('/api/notices/seen', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
          },
          body: JSON.stringify({ noticeId: id })
        }).catch(err => console.warn('Failed to report notice seen status:', err));
      });
    } catch (e) {
      console.warn('Failed to mark notice as seen:', e);
    }
  };

  const handleMarkAsUnseen = (id: string) => {
    try {
      const updated = seenNoticeIds.filter(noticeId => noticeId !== id);
      setSeenNoticeIds(updated);
      localStorage.setItem('yc_seenNotices', JSON.stringify(updated));
      window.dispatchEvent(new Event('yc_seen_notices_changed'));
      
      // Proactively notify the seen endpoint of status removal
      firebaseUser?.getIdToken().then(idToken => {
        fetch('/api/notices/seen', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
          },
          body: JSON.stringify({ noticeId: id, remove: true })
        }).catch(err => console.warn('Failed to report notice unseen status:', err));
      });
    } catch (e) {
      console.warn('Failed to mark notice as unseen:', e);
    }
  };

  const handleClearAllSeen = () => {
    if (!confirm('Are you sure you want to clear all seen notification records from this device?')) return;
    try {
      localStorage.setItem('yc_seenNotices', JSON.stringify([]));
      setSeenNoticeIds([]);
      window.dispatchEvent(new Event('yc_seen_notices_changed'));
    } catch (e) {
      console.warn('Failed to clear seen notifications:', e);
    }
  };

  const unreadNotices = notices.filter(n => !seenNoticeIds.includes(n.id));
  const readNotices = notices.filter(n => seenNoticeIds.includes(n.id));

  const renderNoticeCard = (notice: Notice, isSeen: boolean) => {
    const nType = notice.type || 'general';
    const config = 
      nType === 'schedule' 
        ? { border: '4px solid var(--accent)', badgeBg: 'var(--accent-soft)', badgeColor: 'var(--accent)', label: '📅 Schedule' }
        : nType === 'fees'
        ? { border: '4px solid #f59e0b', badgeBg: 'rgba(245, 158, 11, 0.1)', badgeColor: '#f59e0b', label: '💰 Fees' }
        : { border: '4px solid #94a3b8', badgeBg: 'rgba(148, 163, 184, 0.1)', badgeColor: '#64748b', label: '📢 Announcement' };

    return (
      <div 
        key={notice.id} 
        className="card" 
        style={{ 
          background: 'var(--surface)', 
          borderRadius: 'var(--radius-lg)', 
          border: '1px solid var(--border-light)', 
          borderLeft: config.border,
          padding: '16px',
          display: 'flex',
          flexDirection: 'column',
          gap: '10px',
          position: 'relative',
          opacity: isSeen ? 0.75 : 1
        }}
      >
        {/* Notice Header */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '10px', flexWrap: 'wrap' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
              <h3 style={{ margin: 0, fontSize: '17px', fontWeight: 800, color: 'var(--text)' }}>
                {notice.title}
              </h3>
              <span style={{ fontSize: '9px', fontWeight: 800, background: config.badgeBg, color: config.badgeColor, padding: '2px 8px', borderRadius: '12px' }}>
                {config.label}
              </span>
            </div>
            <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '4px' }}>
              📅 Posted: {notice.createdAt ? new Date(notice.createdAt).toLocaleString('en-IN') : 'N/A'}
            </div>
          </div>
          
          <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
            {isSeen ? (
              <>
                <span 
                  style={{ 
                    fontSize: '9.5px', 
                    fontWeight: 700, 
                    background: 'rgba(16, 185, 129, 0.1)', 
                    color: 'var(--success)', 
                    padding: '2px 8px', 
                    borderRadius: '12px',
                    border: '1px solid rgba(16, 185, 129, 0.2)'
                  }}
                >
                  Read
                </span>
                <button
                  onClick={() => handleMarkAsUnseen(notice.id)}
                  style={{
                    background: 'var(--bg-soft)',
                    border: '1px solid var(--border-light)',
                    borderRadius: 'var(--radius-sm)',
                    padding: '2px 8px',
                    fontSize: '10px',
                    fontWeight: 600,
                    cursor: 'pointer',
                    color: 'var(--text-muted)',
                    transition: 'background 0.2s'
                  }}
                  title="Mark as Unread"
                >
                  ↩ Unread
                </button>
              </>
            ) : (
              <button
                onClick={() => handleMarkAsSeen(notice.id)}
                style={{
                  background: 'var(--accent)',
                  border: '1px solid var(--accent-light)',
                  borderRadius: 'var(--radius-sm)',
                  padding: '4px 10px',
                  fontSize: '11px',
                  fontWeight: 700,
                  cursor: 'pointer',
                  color: '#ffffff',
                  transition: 'background 0.2s'
                }}
              >
                ✓ Mark as Read
              </button>
            )}
          </div>
        </div>

        {/* Schedule date details */}
        {nType === 'schedule' && notice.noticeDate && (
          <div style={{
            fontSize: '12.5px',
            fontWeight: 700,
            color: 'var(--accent)',
            background: 'var(--accent-soft)',
            padding: '6px 10px',
            borderRadius: '4px',
            display: 'inline-flex',
            alignItems: 'center',
            gap: '4px',
            alignSelf: 'flex-start',
            border: '1px solid var(--accent-ring)'
          }}>
            📅 Scheduled Date: {(() => {
              const d = new Date(notice.noticeDate);
              if (isNaN(d.getTime())) return notice.noticeDate;
              const day = String(d.getDate()).padStart(2, '0');
              const month = String(d.getMonth() + 1).padStart(2, '0');
              return `${day}/${month}/${d.getFullYear()}`;
            })()}
          </div>
        )}

        {/* Notice Body */}
        <div 
          style={{ 
            margin: 0, 
            fontSize: '14.5px', 
            color: 'var(--text)', 
            lineHeight: '1.25' 
          }}
          dangerouslySetInnerHTML={{
            __html: (notice.body || '')
              .replace(/(<\/div>|<\/p>|<\/li>)\s*\r?\n/gi, '$1')
              .replace(/\r?\n\s*(<div[^>]*>|<p[^>]*>|<ul[^>]*>|<ol[^>]*>|<li[^>]*>)/gi, '$1')
              .replace(/\r?\n/g, '<br/>')
          }}
        />
      </div>
    );
  };

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Top Header Bar matching Review Page */}
      <div className="page-header glass" style={{ padding: '8px 16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderRadius: '0', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <button 
            onClick={() => router.push('/student')}
            style={{
              background: 'transparent',
              border: 'none',
              color: 'var(--text)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              padding: '6px',
              borderRadius: '50%',
              transition: 'background 0.2s'
            }}
            title="Back to Dashboard"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>
          </button>
          <span className="brand" style={{ fontWeight: 800, fontSize: '1.1rem', color: 'var(--accent)', cursor: 'pointer' }} onClick={() => router.push('/student')}>YASHCOM</span>
        </div>
        <div className="page-header-right" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          
          <button className="btn btn-secondary logout-btn" onClick={() => logout()} style={{ fontSize: '1rem', padding: '6px 10px', display: 'flex', alignItems: 'center', justifyContent: 'center' }} title="Logout">🚪</button>
        </div>
      </div>

      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '800px', width: '100%', margin: '0 auto' }}>
      <style>{`
        @keyframes skeleton-blink {
          0% { opacity: 0.6; }
          50% { opacity: 1; }
          100% { opacity: 0.6; }
        }
        .skeleton-blink {
          animation: skeleton-blink 1.5s infinite ease-in-out;
        }
      `}</style>

      {error && (
        <div className="alert-box alert-box-danger" style={{ display: 'block', marginBottom: '20px' }}>
          {error}
        </div>
      )}

      <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
        
        {/* Page Header */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px', borderBottom: '1px solid var(--border-light)', paddingBottom: '14px' }}>
          <div>
            <h2 style={{ margin: 0, fontSize: '1.4rem', fontWeight: 800, color: 'var(--text)' }}>
              📢 Student Notice Board
            </h2>
            <p style={{ margin: '4px 0 0 0', fontSize: '11.5px', color: 'var(--text-muted)' }}>
              Stay updated with the latest schedules, announcements, and reminders.
            </p>
          </div>
          {!loading && readNotices.length > 0 && (
            <button 
              className="btn btn-secondary btn-sm"
              onClick={handleClearAllSeen}
              style={{ fontSize: '11px', fontWeight: 700, padding: '6px 14px', background: '#fee2e2', color: '#b91c1c', border: '1px solid #fca5a5' }}
            >
              🗑️ Clear Read Archive
            </button>
          )}
        </div>

        {/* Notifications List */}
        {loading ? (
          renderListSkeleton()
        ) : notices.length === 0 ? (
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '40px 20px', textAlign: 'center' }}>
            <div style={{ fontSize: '2.5rem', marginBottom: '12px' }}>📭</div>
            <h4 style={{ margin: '0 0 4px 0', fontSize: '14px', fontWeight: 700, color: 'var(--text)' }}>No Announcements</h4>
            <p style={{ margin: 0, fontSize: '11px', color: 'var(--text-muted)' }}>
              There are no announcements currently published.
            </p>
            <button 
              className="btn btn-primary btn-sm" 
              onClick={() => router.push('/student')} 
              style={{ marginTop: '16px', fontSize: '12px', fontWeight: 700 }}
            >
              🏠 Go to Dashboard
            </button>
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
            {/* 1. Unread section */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <h4 style={{ margin: '0 0 4px 0', fontSize: '13px', fontWeight: 800, color: 'var(--accent)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                New Announcements ({unreadNotices.length})
              </h4>
              {unreadNotices.length === 0 ? (
                <div className="card" style={{ background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)', padding: '16px', textAlign: 'center', border: '1px dashed var(--border-light)', fontSize: '12px', color: 'var(--text-muted)' }}>
                  🎉 You have read all notifications.
                </div>
              ) : (
                unreadNotices.map(notice => renderNoticeCard(notice, false))
              )}
            </div>

            {/* 2. Read Archive section */}
            {readNotices.length > 0 && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', borderTop: '1px dashed var(--border-light)', paddingTop: '20px' }}>
                <h4 style={{ margin: '0 0 4px 0', fontSize: '13px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                  Read History Archive ({readNotices.length})
                </h4>
                {readNotices.map(notice => renderNoticeCard(notice, true))}
              </div>
            )}
          </div>
        )}
      </div>
    </main>
    </div>
  );
}
