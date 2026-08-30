'use client';

import React, { useState, useEffect, useRef } from 'react';
import { usePathname, useRouter } from 'next/navigation';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import TopBarTimeTracker from '@/components/TopBarTimeTracker';
import { db } from '@/lib/firebase/firestore';
import { doc, onSnapshot } from 'firebase/firestore';

import { Sun, Moon, LogOut, Bell, Settings } from 'lucide-react';
import Image from 'next/image';

export default function StudentLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname() || '';
  const router = useRouter();
  const { theme, toggleTheme } = useTheme();
  const { user, logout } = useAuth();
  const [curfewActive, setCurfewActive] = useState(false);
  const [maintenance, setMaintenance] = useState<{ active: boolean; message: string } | null>(null);

  useEffect(() => {
    const unsub = onSnapshot(doc(db, 'config', 'systemAccess'), (snapshot) => {
      const email = (user?.email || '').toLowerCase();
      const isBypassed = email === 's@c.com' || email === 'p@c.com' || email === 'a@c.com' || !!user?.maintenanceBypass || !!user?.curfewBypass;

      if (snapshot.exists()) {
        const data = snapshot.data();
        if (!isBypassed && data.maintenanceMode && data.blockedRoles?.includes('student')) {
          setMaintenance({
            active: true,
            message: data.message || 'The system is undergoing scheduled maintenance. Access will be restored shortly.'
          });
        } else {
          setMaintenance(null);
        }
      } else {
        setMaintenance(null);
      }
    }, () => {});
    return () => unsub();
  }, [user]);

  useEffect(() => {
    const getOfficialTime = () => {
      const serverTimeStr = sessionStorage.getItem('yc_serverTime');
      const loadPerfStr = sessionStorage.getItem('yc_loadPerformanceTime');
      if (serverTimeStr && loadPerfStr) {
        const serverTime = parseInt(serverTimeStr);
        const loadPerf = parseFloat(loadPerfStr);
        const elapsed = performance.now() - loadPerf;
        return serverTime + elapsed;
      }
      return Date.now();
    };

    const checkCurfew = () => {
      const email = (user?.email || '').toLowerCase();
      const curfewBypassEmail = (process.env.NEXT_PUBLIC_CURFEW_BYPASS_EMAIL || '').toLowerCase();
      if (email === 's@c.com' || email === 'p@c.com' || email === 'a@c.com' || email === curfewBypassEmail || user?.curfewBypass || user?.maintenanceBypass) {
        setCurfewActive(false);
        return;
      }
      const actualTime = getOfficialTime();
      const istDate = new Date(actualTime + 5.5 * 60 * 60 * 1000);
      const hours = istDate.getUTCHours();
      const minutes = istDate.getUTCMinutes();
      const isCurfew = hours > 22 || (hours === 22 && minutes >= 30) || hours < 5;
      setCurfewActive(isCurfew);
    };

    checkCurfew();
    const interval = setInterval(checkCurfew, 15000);
    return () => clearInterval(interval);
  }, [user]);

  // Hide the menu entirely during active exam taking or proctored practice sessions
  const isTakingExam = pathname.includes('/take-exam') || pathname.includes('/take-subjective-exam') || pathname.includes('/student/topic');

  if (isTakingExam) {
    return <>{children}</>;
  }

  if (maintenance?.active) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '24px' }}>
        <div className="card glass" style={{ maxWidth: '480px', width: '100%', padding: '32px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center', display: 'flex', flexDirection: 'column', gap: '20px', background: 'var(--surface)' }}>
          <span style={{ fontSize: '3rem' }}>🛠️</span>
          <h2 style={{ margin: 0, fontSize: '20px', fontWeight: 800, color: 'var(--accent)' }}>System Under Maintenance</h2>
          <p style={{ margin: 0, fontSize: '14px', lineHeight: '1.6', color: 'var(--text)' }}>
            {maintenance.message}
          </p>
          <button className="btn btn-secondary" onClick={logout} style={{ marginTop: '10px', height: '40px', fontWeight: 700 }}>
            Sign Out
          </button>
        </div>
      </div>
    );
  }

  if (curfewActive) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '24px' }}>
        <div className="card glass" style={{ maxWidth: '480px', width: '100%', padding: '32px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center', display: 'flex', flexDirection: 'column', gap: '20px', background: 'var(--surface)' }}>
          <span style={{ fontSize: '3rem' }}>🌙</span>
          <h2 style={{ margin: 0, fontSize: '20px', fontWeight: 800, color: 'var(--accent)' }}>Night Curfew Active</h2>
          <p style={{ margin: 0, fontSize: '14px', lineHeight: '1.6', color: 'var(--text)' }}>
            The platform is closed for students between <strong>10:30 PM</strong> and <strong>5:00 AM IST</strong> to promote healthy sleep habits. Please rest well and return tomorrow!
          </p>
          <button className="btn btn-secondary" onClick={logout} style={{ marginTop: '10px', height: '40px', fontWeight: 700 }}>
            Sign Out
          </button>
        </div>
      </div>
    );
  }

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column', background: 'var(--bg)' }}>
      <style>{`
        @media (max-width: 580px) {
          .hide-mobile {
            display: none !important;
          }
        }
        @media (max-width: 480px) {
          .page-header {
            padding: 8px 10px !important;
          }
          .page-header-logo-text {
            font-size: 1rem !important;
          }
          .page-header-actions {
            gap: 6px !important;
          }
          .page-header-btn {
            width: 32px !important;
            height: 32px !important;
          }
        }
      `}</style>

      {/* Universal Top Header Bar (Single top bar for all student pages) */}
      <header className="page-header glass" style={{ 
        padding: '10px 16px', 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center', 
        borderBottom: '1px solid var(--border)',
        background: 'var(--surface-glass)',
        backdropFilter: 'blur(16px)',
        WebkitBackdropFilter: 'blur(16px)',
        zIndex: 100
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexShrink: 0 }}>
          <div 
            onClick={() => router.push('/student')} 
            style={{ display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer' }}
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

          {/* Notifications Button */}
          <button 
            className="page-header-btn" 
            onClick={() => router.push('/student/notifications')} 
            title="Notifications"
            style={{ 
              background: pathname === '/student/notifications' ? 'var(--accent-soft)' : (theme === 'dark' ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.05)'), 
              border: theme === 'dark' ? '1px solid rgba(255,255,255,0.15)' : '1px solid var(--border)', 
              borderRadius: '50%', 
              width: '36px', 
              height: '36px', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center', 
              cursor: 'pointer',
              color: pathname === '/student/notifications' ? 'var(--accent)' : 'var(--text)',
              flexShrink: 0
            }}
          >
            <Bell size={16} />
          </button>

          {/* Settings Button */}
          <button 
            className="page-header-btn" 
            onClick={() => router.push('/student/settings')} 
            title="Profile & Settings"
            style={{ 
              background: pathname === '/student/settings' ? 'var(--accent-soft)' : (theme === 'dark' ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.05)'), 
              border: theme === 'dark' ? '1px solid rgba(255,255,255,0.15)' : '1px solid var(--border)', 
              borderRadius: '50%', 
              width: '36px', 
              height: '36px', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center', 
              cursor: 'pointer',
              color: pathname === '/student/settings' ? 'var(--accent)' : 'var(--text)',
              flexShrink: 0
            }}
          >
            <Settings size={16} />
          </button>

          {/* Logout Button */}
          <button 
            className="page-header-btn"
            onClick={logout} 
            style={{ 
              background: 'rgba(255,255,255,0.08)', 
              border: '1px solid rgba(255,255,255,0.15)', 
              borderRadius: '50%', 
              width: '36px', 
              height: '36px', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center', 
              color: '#ef4444', 
              cursor: 'pointer',
              flexShrink: 0
            }}
            title="Logout"
          >
            <LogOut size={16} />
          </button>
        </div>
      </header>

      {/* Children workspace content */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', paddingBottom: '40px' }}>
        {children}
      </div>
    </div>
  );
}
