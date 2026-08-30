'use client';

import React, { useEffect, useState } from 'react';
import Image from 'next/image';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import { Bell, MessageSquare, Settings, LogOut } from 'lucide-react';
import StudentActivityTable from '@/components/StudentActivityTable';
import TopBarTimeTracker from '@/components/TopBarTimeTracker';

import useSWR from 'swr';
import { fetchWithToken } from '@/lib/swrFetcher';

interface AdminStats {
  totalStudents: number;
  totalBatches: number;
  cumulativePractice: number;
  activeExams: number;
  todayAttendanceRate: number | null;
  overdueFeesCount: number;
  unreadChatsCount: number;
}

interface RecentRegistration {
  id: string;
  studentName: string;
  studentEmail: string;
  batchName: string;
  createdAt: string;
}

interface AdminDashboardData {
  stats: AdminStats;
  recentRegistrations: RecentRegistration[];
}

export default function AdminDashboard() {
  const { firebaseUser, logout, user } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const renderStatsSkeleton = () => (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '12px', marginBottom: '20px' }} className="skeleton-blink">
      {/* Card 1 Skeleton */}
      <div className="card" style={{ background: 'var(--surface)', padding: '12px 14px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '8px' }}>
        {[1, 2, 3].map(i => (
          <div key={i} style={{ width: '100%', height: '34px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)' }}></div>
        ))}
      </div>
      {/* Card 2 Skeleton */}
      <div className="card" style={{ background: 'var(--surface)', padding: '12px 14px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '8px' }}>
        {[1, 2].map(i => (
          <div key={i} style={{ width: '100%', height: '34px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)' }}></div>
        ))}
      </div>
    </div>
  );

  const renderQuickActionsSkeleton = () => (
    <div className="card skeleton-blink" style={{ background: 'var(--surface)', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', marginBottom: '32px' }}>
      <div style={{ width: '120px', height: '14px', background: 'var(--bg-soft)', borderRadius: '4px', marginBottom: '16px' }}></div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '8px' }}>
        {[1, 2, 3, 4, 5, 6, 7, 8].map(i => (
          <div key={i} style={{ width: '100%', height: '36px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)' }}></div>
        ))}
        <div style={{ width: '100%', height: '36px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', gridColumn: 'span 2' }}></div>
      </div>
    </div>
  );

  const renderTableSkeleton = () => (
    <div className="card skeleton-blink" style={{ background: 'var(--surface)', padding: '24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
      <div style={{ width: '180px', height: '16px', background: 'var(--bg-soft)', borderRadius: '4px', marginBottom: '16px' }}></div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {[1, 2, 3, 4].map(i => (
          <div key={i} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', height: '32px', borderBottom: '1px solid var(--border-light)' }}>
            <div style={{ width: '140px', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
            <div style={{ width: '80px', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
          </div>
        ))}
      </div>
    </div>
  );

  const [localCache, setLocalCache] = useState<AdminDashboardData | undefined>(undefined);

  useEffect(() => {
    try {
      const cached = localStorage.getItem('yc_admin_dashboard_cache');
      if (cached) {
        setLocalCache(JSON.parse(cached));
      }
    } catch (e) {
      console.warn('Failed to load cached admin dashboard data:', e);
    }
  }, []);

  const fetcher = async (url: string) => {
    const resData = await fetchWithToken(url, firebaseUser);
    if (resData) {
      try {
        localStorage.setItem('yc_admin_dashboard_cache', JSON.stringify(resData));
      } catch (e) {}
    }
    return resData;
  };

  const { data, error, isLoading } = useSWR<AdminDashboardData>(
    firebaseUser ? '/api/admin/dashboard' : null,
    fetcher,
    {
      revalidateOnFocus: true,
      dedupingInterval: 10000,
      keepPreviousData: true,
      fallbackData: localCache
    }
  );

  const loading = isLoading && !data;

  if (error && !data) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div className="alert-box alert-box-danger" style={{ display: 'block', maxWidth: '400px', textAlign: 'center' }}>
          {error?.message || 'Could not load admin dashboard profile.'}
        </div>
        <button className="btn btn-primary" onClick={() => window.location.reload()} style={{ marginTop: '16px' }}>Retry</button>
      </div>
    );
  }

  const stats = data?.stats || { totalStudents: 0, totalBatches: 0, cumulativePractice: 0, activeExams: 0, todayAttendanceRate: null, overdueFeesCount: 0, unreadChatsCount: 0 };

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh' }}>
      <style>{`
        @media (max-width: 580px) {
          .hide-mobile {
            display: none !important;
          }
        }
        @keyframes skeleton-blink {
          0% { opacity: 0.6; }
          50% { opacity: 1; }
          100% { opacity: 0.6; }
        }
        .skeleton-blink {
          animation: skeleton-blink 1.5s infinite ease-in-out;
        }
      `}</style>
      {/* Page Header */}
      <header className="page-header glass" style={{ 
        padding: '10px 16px', 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center', 
        borderRadius: '0',
        borderBottom: '1px solid var(--border)',
        background: 'var(--surface-glass)',
        backdropFilter: 'blur(16px)',
        WebkitBackdropFilter: 'blur(16px)',
        zIndex: 100
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexShrink: 0 }}>
          <div 
            onClick={() => router.push('/admin')} 
            style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer' }}
          >
            <Image 
              src="/logo.png" 
              alt="YASHCOM Logo" 
              width={24} 
              height={24} 
              style={{ borderRadius: '50%', objectFit: 'cover' }} 
              priority
            />
            <span className="page-header-logo-text" style={{ fontWeight: 900, fontSize: '1.15rem', letterSpacing: '0.5px', color: 'var(--text)' }}>
              YASHCOM
            </span>
          </div>
        </div>

        <div className="page-header-actions" style={{ display: 'flex', alignItems: 'center', gap: '8px', flexShrink: 0 }}>
          <TopBarTimeTracker />

          {/* Notices */}
          <button 
            className="page-header-btn" 
            onClick={() => router.push('/admin/notices')} 
            title="Notices & Announcements"
            style={{ 
              background: 'rgba(255,255,255,0.05)', 
              border: '1px solid var(--border)', 
              borderRadius: '50%', 
              width: '36px', 
              height: '36px', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center', 
              cursor: 'pointer',
              color: 'var(--text)',
              flexShrink: 0
            }}
          >
            <Bell size={16} color="#fbbf24" />
          </button>

          {/* Live Chat */}
          <button 
            className="page-header-btn" 
            onClick={() => router.push('/admin/chat')} 
            title="Live Chat Workspace"
            style={{ 
              background: 'rgba(255,255,255,0.05)', 
              border: '1px solid var(--border)', 
              borderRadius: '50%', 
              width: '36px', 
              height: '36px', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center', 
              cursor: 'pointer',
              color: 'var(--text)',
              flexShrink: 0
            }}
          >
            <MessageSquare size={16} color="#38bdf8" />
          </button>

          {/* Settings */}
          <button 
            className="page-header-btn" 
            onClick={() => router.push('/admin/settings')} 
            title="Admin Settings"
            style={{ 
              background: 'rgba(255,255,255,0.05)', 
              border: '1px solid var(--border)', 
              borderRadius: '50%', 
              width: '36px', 
              height: '36px', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center', 
              cursor: 'pointer',
              color: 'var(--text)',
              flexShrink: 0
            }}
          >
            <Settings size={16} color="#94a3b8" />
          </button>

          {/* Logout Button */}
          <button 
            className="page-header-btn"
            onClick={logout} 
            style={{ 
              background: 'rgba(255,255,255,0.05)', 
              border: '1px solid var(--border)', 
              borderRadius: '50%', 
              width: '36px', 
              height: '36px', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center', 
              color: '#f87171', 
              cursor: 'pointer',
              flexShrink: 0
            }}
            title="Logout"
          >
            <LogOut size={16} />
          </button>
        </div>
      </header>

      <div className="dashboard-container" style={{ maxWidth: '1300px', margin: '0 auto', padding: '10px 8px 30px 8px' }}>

        {loading ? (
          <>
            {renderStatsSkeleton()}
            {renderQuickActionsSkeleton()}
            {renderTableSkeleton()}
          </>
        ) : (
          <>
            {/* Bento-style Statistics Cards */}
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
              gap: '8px',
              marginBottom: '10px'
            }}>
              {/* Card 1: Academic & Attendance Stats */}
              <div className="card" style={{
                background: '#ffffff',
                padding: '8px 10px',
                borderRadius: 'var(--radius)',
                border: '1px solid var(--border)',
                boxShadow: 'var(--shadow-sm)',
                display: 'flex',
                flexDirection: 'column',
                gap: '6px',
                justifyContent: 'center'
              }}>
                {/* Chip 1: Batches (Students) */}
                <div 
                  onClick={() => router.push('/admin/batches')}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '6px 10px',
                    background: 'var(--surface-2)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    transition: 'all 0.18s ease',
                    border: '1px solid var(--border)'
                  }}
                  onMouseEnter={(e) => { e.currentTarget.style.borderColor = '#cbd5e1'; e.currentTarget.style.transform = 'translateY(-1px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                >
                  <span style={{ fontSize: '11.5px', fontWeight: 600, color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    Batches (Students)
                  </span>
                  <span style={{ fontSize: '12.5px', fontWeight: 800, color: '#7c3aed' }}>
                    {stats.totalBatches} ({stats.totalStudents})
                  </span>
                </div>

                {/* Chip 2: Exams - Practice */}
                <div 
                  onClick={() => router.push('/admin/exams')}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '6px 10px',
                    background: 'var(--surface-2)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    transition: 'all 0.18s ease',
                    border: '1px solid var(--border)'
                  }}
                  onMouseEnter={(e) => { e.currentTarget.style.borderColor = '#cbd5e1'; e.currentTarget.style.transform = 'translateY(-1px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                >
                  <span style={{ fontSize: '11.5px', fontWeight: 600, color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    Exams - Practice
                  </span>
                  <span style={{ fontSize: '12.5px', fontWeight: 800, color: '#0d9488' }}>
                    {stats.activeExams} - {stats.cumulativePractice}
                  </span>
                </div>

                {/* Chip 3: Attendance */}
                <div 
                  onClick={() => router.push('/admin/attendance')}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '6px 10px',
                    background: 'var(--surface-2)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    transition: 'all 0.18s ease',
                    border: '1px solid var(--border)'
                  }}
                  onMouseEnter={(e) => { e.currentTarget.style.borderColor = '#cbd5e1'; e.currentTarget.style.transform = 'translateY(-1px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                >
                  <span style={{ fontSize: '11.5px', fontWeight: 600, color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    Attendance
                  </span>
                  <span style={{ fontSize: '12.5px', fontWeight: 800, color: '#2563eb' }}>
                    {stats.todayAttendanceRate !== null ? `${stats.todayAttendanceRate}%` : '--'}
                  </span>
                </div>
              </div>

              {/* Card 2: Communication & Accounts Stats */}
              <div className="card" style={{
                background: '#ffffff',
                padding: '8px 10px',
                borderRadius: 'var(--radius)',
                border: '1px solid var(--border)',
                boxShadow: 'var(--shadow-sm)',
                display: 'flex',
                flexDirection: 'column',
                gap: '6px',
                justifyContent: 'center'
              }}>
                {/* Chip 1: Chat */}
                <div 
                  onClick={() => router.push('/admin/chat')}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '6px 10px',
                    background: 'var(--surface-2)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    transition: 'all 0.18s ease',
                    border: '1px solid var(--border)'
                  }}
                  onMouseEnter={(e) => { e.currentTarget.style.borderColor = '#cbd5e1'; e.currentTarget.style.transform = 'translateY(-1px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                >
                  <span style={{ fontSize: '11.5px', fontWeight: 600, color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    Chat
                  </span>
                  <span style={{ fontSize: '12.5px', fontWeight: 800, color: stats.unreadChatsCount > 0 ? '#dc2626' : 'var(--text-muted)' }}>
                    {stats.unreadChatsCount} Rooms
                  </span>
                </div>

                {/* Chip 2: Fees Pending */}
                <div 
                  onClick={() => router.push('/admin/fees')}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '6px 10px',
                    background: 'var(--surface-2)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    transition: 'all 0.18s ease',
                    border: '1px solid var(--border)'
                  }}
                  onMouseEnter={(e) => { e.currentTarget.style.borderColor = '#cbd5e1'; e.currentTarget.style.transform = 'translateY(-1px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                >
                  <span style={{ fontSize: '11.5px', fontWeight: 600, color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    Fees Pending
                  </span>
                  <span style={{ fontSize: '12.5px', fontWeight: 800, color: stats.overdueFeesCount > 0 ? '#dc2626' : '#059669' }}>
                    {stats.overdueFeesCount} Accounts
                  </span>
                </div>
              </div>
            </div>

            {/* Quick Actions Panel */}
            <div className="card" style={{ background: '#ffffff', padding: '10px 12px', borderRadius: 'var(--radius)', border: '1px solid var(--border)', marginBottom: '10px', boxShadow: 'var(--shadow-sm)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '4px', marginBottom: '8px' }}>
                <h3 style={{ fontSize: '14px', fontWeight: 800, margin: 0, color: 'var(--text)' }}>Quick Actions</h3>
              </div>
              <div className="admin-quick-actions-grid">
                <button className="btn btn-secondary" style={{ width: '100%', fontSize: '11.5px', fontWeight: 600, padding: '6px 8px', whiteSpace: 'nowrap', borderRadius: 'var(--radius-sm)' }} onClick={() => router.push('/admin/exams')}>Exams Scheduler</button>
                <button className="btn btn-secondary" style={{ width: '100%', fontSize: '11.5px', fontWeight: 600, padding: '6px 8px', whiteSpace: 'nowrap', borderRadius: 'var(--radius-sm)' }} onClick={() => router.push('/admin/exam-generator')}>Exam Generator</button>
                <button className="btn btn-secondary" style={{ width: '100%', fontSize: '11.5px', fontWeight: 600, padding: '6px 8px', whiteSpace: 'nowrap', borderRadius: 'var(--radius-sm)' }} onClick={() => router.push('/admin/question-bank')}>Question Bank</button>
                <button className="btn btn-secondary" style={{ width: '100%', fontSize: '11.5px', fontWeight: 600, padding: '6px 8px', whiteSpace: 'nowrap', borderRadius: 'var(--radius-sm)' }} onClick={() => router.push('/admin/syllabus')}>Syllabus Manager</button>
                <button className="btn btn-secondary" style={{ width: '100%', fontSize: '11.5px', fontWeight: 600, padding: '6px 8px', whiteSpace: 'nowrap', borderRadius: 'var(--radius-sm)' }} onClick={() => router.push('/admin/live-exam-monitor')}>Live Monitor</button>
                <button className="btn btn-secondary" style={{ width: '100%', fontSize: '11.5px', fontWeight: 600, padding: '6px 8px', whiteSpace: 'nowrap', borderRadius: 'var(--radius-sm)' }} onClick={() => router.push('/admin/notices')}>Notices Manager</button>
                <button className="btn btn-secondary" style={{ width: '100%', fontSize: '11.5px', fontWeight: 600, padding: '6px 8px', whiteSpace: 'nowrap', borderRadius: 'var(--radius-sm)' }} onClick={() => router.push('/admin/attendance')}>Attendance Sheet</button>
                <button className="btn btn-secondary" style={{ width: '100%', fontSize: '11.5px', fontWeight: 600, padding: '6px 8px', whiteSpace: 'nowrap', borderRadius: 'var(--radius-sm)' }} onClick={() => router.push('/admin/fees')}>Fees Manager</button>
                <button className="btn btn-secondary" style={{ width: '100%', fontSize: '11.5px', fontWeight: 600, padding: '6px 8px', whiteSpace: 'nowrap', borderRadius: 'var(--radius-sm)' }} onClick={() => router.push('/admin/chat')}>Live Chat Center</button>
                <button className="btn btn-secondary" style={{ width: '100%', fontSize: '11.5px', fontWeight: 600, padding: '6px 8px', whiteSpace: 'nowrap', borderRadius: 'var(--radius-sm)' }} onClick={() => router.push('/admin/batches')}>Batches & Students</button>
              </div>
            </div>

            {/* Student Live Activity presence table */}
            <StudentActivityTable />
          </>
        )}
      </div>
    </div>
  );
}
