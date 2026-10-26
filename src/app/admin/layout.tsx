'use client';

import React, { useState, useEffect, useRef } from 'react';
import Image from 'next/image';
import { useRouter, usePathname } from 'next/navigation';
import { Bell, MessageSquare, Settings, LogOut } from 'lucide-react';
import { useAuth } from '@/context/AuthContext';
import TopBarTimeTracker from '@/components/TopBarTimeTracker';
import TopBarChatButton from '@/components/chat/TopBarChatButton';
import { useUnreadChatCount } from '@/hooks/useUnreadChatCount';
import { triggerNavStart } from '@/components/NavigationProgressBar';

const getAdminPageTitle = (pathname: string): string => {
  if (pathname === '/admin') return 'Dashboard';
  if (pathname.startsWith('/admin/exam-generator')) return 'Exam Generator';
  if (pathname.startsWith('/admin/exam-report')) return 'Exam Report';
  if (pathname.startsWith('/admin/classroom-test')) return 'Classroom Test & Suites';
  if (pathname.startsWith('/admin/live-exam-monitor')) return 'Live Monitor';
  if (pathname.startsWith('/admin/exams')) return 'Manage Exams';
  if (pathname.startsWith('/admin/create-qb')) return 'Create Question Bank';
  if (pathname.startsWith('/admin/question-bank')) return 'Question Bank';
  if (pathname.startsWith('/admin/syllabus')) return 'Syllabus Manager';
  if (pathname.startsWith('/admin/students')) return 'Students & Batches';
  if (pathname.startsWith('/admin/batches')) return 'Batches';
  if (pathname.startsWith('/admin/registrations')) return 'Student Registrations';
  if (pathname.startsWith('/admin/attendance')) return 'Daily Attendance Sheet';
  if (pathname.startsWith('/admin/fees')) return 'Fees Manager';
  if (pathname.startsWith('/admin/notices')) return 'Notices & Announcements';
  if (pathname.startsWith('/admin/chat')) return 'Live Chat Workspace';
  if (pathname === '/admin/reports') return 'Reports & Analytics Hub';
  if (pathname.startsWith('/admin/reports/learning-quotient')) return 'Learning Quotient (LQ)';
  if (pathname.startsWith('/admin/reports/daily-practice')) return 'Daily Practice Summary';
  if (pathname.startsWith('/admin/reports/parent-pending')) return 'Parent Reviews & Sincerity';
  if (pathname.startsWith('/admin/reports/usage')) return 'System Usage Analytics';
  if (pathname.startsWith('/admin/reports/login-register')) return 'Login Activity Register';
  if (pathname.startsWith('/admin/integrity-score-manager')) return 'Integrity Score Manager';
  if (pathname.startsWith('/admin/teacher-final-review')) return 'Teacher Final Review';
  if (pathname.startsWith('/admin/settings')) return 'System Settings';
  if (pathname.startsWith('/admin/fault-register')) return 'Fault Register';
  return 'Admin';
};

interface SubmenuItem {
  icon: string;
  en: string;
  url: string;
  action?: string;
}

const ADMIN_SUBMENUS: { [key: string]: SubmenuItem[] } = {
  exams: [
    { icon: '📝', en: 'Create Exam', url: '/admin/exam-generator' },
    { icon: '📚', en: 'All Exams', url: '/admin/exams' },
    { icon: '🔴', en: 'Live Monitor', url: '/admin/live-exam-monitor' },
    { icon: '🏫', en: 'Classroom Test', url: '/admin/classroom-test' }
  ],
  qb: [
    { icon: '📒', en: 'QB', url: '/admin/question-bank' },
    { icon: '🤖', en: 'Create QB (AI)', url: '/admin/create-qb' },
    { icon: '📖', en: 'Syllabus Manager', url: '/admin/syllabus' }
  ],
  manage: [
    { icon: '📢', en: 'Notices Manager', url: '/admin/notices' },
    { icon: '💬', en: 'Live Chat Workspace', url: '/admin/chat' },
    { icon: '📅', en: 'Attendance Sheet', url: '/admin/attendance' },
    { icon: '📋', en: 'Fault Register', url: '/admin/fault-register' },
    { icon: '🪙', en: 'Fees Manager', url: '/admin/fees' },
    { icon: '👥', en: 'Students & Batches', url: '/admin/students' }
  ],
  reports: [
    { icon: '📊', en: 'Learning Quotient (LQ)', url: '/admin/reports/learning-quotient' },
    { icon: '✍️', en: 'Daily Practice Summary', url: '/admin/reports/daily-practice' },
    { icon: '📈', en: 'System Usage Analytics', url: '/admin/reports/usage' },
    { icon: '👥', en: 'Parent Reviews', url: '/admin/reports/parent-pending' },
    { icon: '🔑', en: 'Login Activity Register', url: '/admin/reports/login-register' }
  ],
  settings: [
    { icon: '🛡️', en: 'Integrity Scores', url: '/admin/integrity-score-manager' },
    { icon: '⚙️', en: 'Settings Dashboard', url: '/admin/settings' }
  ]
};

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const pathname = usePathname() || '';
  const { logout } = useAuth();
  const unreadChatCount = useUnreadChatCount('admin', pathname);

  const [panelOpen, setPanelOpen] = useState(false);
  const [activeSubmenu, setActiveSubmenu] = useState<string | null>(null);
  const dropdownRef = useRef<HTMLDivElement | null>(null);

  const panelRef = useRef<HTMLDivElement | null>(null);
  const hamburgerRef = useRef<HTMLButtonElement | null>(null);

  // Close menus when clicking outside
  useEffect(() => {
    function handleOutsideClick(e: MouseEvent) {
      if (
        panelRef.current && 
        !panelRef.current.contains(e.target as Node) &&
        hamburgerRef.current &&
        !hamburgerRef.current.contains(e.target as Node)
      ) {
        setPanelOpen(false);
        setActiveSubmenu(null);
      }
    }
    document.addEventListener('click', handleOutsideClick);
    return () => document.removeEventListener('click', handleOutsideClick);
  }, []);

  // Dynamically position dropdown next to active chip matching legacy admin-nav.js
  useEffect(() => {
    if (activeSubmenu && dropdownRef.current && panelOpen) {
      const btn = document.querySelector(`[data-chip-id="${activeSubmenu}"]`);
      if (btn) {
        const r = btn.getBoundingClientRect();
        const rightVal = window.innerWidth - r.left + 6;
        let topVal = r.top;
        const dropdownHeight = dropdownRef.current.offsetHeight;
        const maxTop = window.innerHeight - dropdownHeight - 8;
        if (topVal > maxTop) {
          topVal = Math.max(8, maxTop);
        }
        dropdownRef.current.style.right = `${rightVal}px`;
        dropdownRef.current.style.top = `${topVal}px`;
        dropdownRef.current.style.visibility = 'visible';
      }
    }
  }, [activeSubmenu, panelOpen]);

  useEffect(() => {
    if (panelOpen) {
      // Warm up admin routes in the background
      Object.values(ADMIN_SUBMENUS).flat().forEach(item => {
        if (item.url && item.url !== '#') {
          router.prefetch(item.url);
        }
      });
    }
  }, [panelOpen, router]);

  const handleChipClick = (e: React.MouseEvent, chipId: string) => {
    e.stopPropagation();

    const matchedChip = chips.find(c => c.id === chipId);
    if (matchedChip?.url) {
      triggerNavStart();
      router.push(matchedChip.url);
      setPanelOpen(false);
      setActiveSubmenu(null);
      return;
    }

    if (activeSubmenu === chipId) {
      setActiveSubmenu(null);
      return;
    }
    
    setActiveSubmenu(chipId);
  };

  const handleSubmenuItemClick = (item: SubmenuItem) => {
    if (item.url && item.url !== '#') {
      triggerNavStart();
      router.push(item.url);
    } else {
      alert(`Feature "${item.en}" is legacy or placeholder.`);
    }
    setPanelOpen(false);
    setActiveSubmenu(null);
  };

  const chips: Array<{ id: string; icon: string; en: string; url?: string }> = [
    { id: 'exams', icon: '📚', en: 'Exams' },
    { id: 'qb', icon: '📒', en: 'QB' },
    { id: 'manage', icon: '👥', en: 'Manage' },
    { id: 'faults', icon: '📋', en: 'Faults', url: '/admin/fault-register' },
    { id: 'reports', icon: '📈', en: 'Reports' },
    { id: 'settings', icon: '⚙️', en: 'Settings' }
  ];

  return (
    <div className="page-wrapper" style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      {/* Injecting Legacy styling exact layout */}
      <style>{`
        /* Floating Hamburger */
        .nav-hamburger-btn {
          position: fixed;
          bottom: 16px;
          right: 16px;
          width: 48px;
          height: 48px;
          border-radius: 50%;
          background: var(--surface-popover);
          color: var(--text);
          border: 1.5px solid var(--border-glass);
          box-shadow: var(--shadow-lg);
          font-size: 20px;
          z-index: 10000;
          cursor: pointer;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: background 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
        }
        .nav-hamburger-btn:hover {
          background: var(--surface-3);
          border-color: var(--border-popover);
          color: var(--primary);
          transform: scale(1.05);
        }
        .nav-hamburger-btn .hb-icon {
          display: inline-block;
          transition: transform .2s ease;
        }
        .nav-hamburger-btn.open .hb-icon {
          transform: rotate(90deg);
        }

        /* Panel layout */
        .nav-chip-panel {
          position: fixed;
          bottom: 74px;
          right: 16px;
          left: auto;
          width: max-content;
          min-width: 150px;
          max-width: 200px;
          display: none;
          flex-direction: column;
          gap: 2px;
          padding: 5px;
          z-index: 10000;
          background: var(--surface-popover);
          border: 1px solid var(--border-popover);
          border-radius: var(--radius);
          box-shadow: var(--shadow-lg);
        }
        .nav-chip-panel.show {
          display: flex;
        }

        /* Nav Item Styles */
        .nav-item {
          display: flex;
          flex-direction: row;
          align-items: center;
          gap: 8px;
          padding: 7px 10px;
          border-radius: 4px;
          cursor: pointer;
          color: var(--text);
          background: transparent;
          border: none;
          white-space: nowrap;
          width: 100%;
          text-align: left;
          font-family: inherit;
        }
        .nav-item:hover {
          background: var(--bg-soft);
          color: var(--accent);
        }
        .nav-item.active {
          background: var(--accent);
          color: var(--text-white);
        }
        .nav-icon {
          font-size: 16px;
          width: 18px;
          text-align: center;
        }
        .nav-label {
          font-size: 13px;
          font-weight: 500;
        }

        /* Flyout Dropdown Menu */
        .dropdown-menu-flyout {
          position: fixed;
          z-index: 10001;
          background: var(--surface-popover);
          border: 1px solid var(--border-popover);
          border-radius: var(--radius-sm);
          box-shadow: var(--shadow-lg);
          padding: 4px;
          display: flex;
          flex-direction: column;
          gap: 2px;
          min-width: 140px;
          visibility: hidden;
        }
        .dropdown-item-flyout {
          display: flex;
          align-items: center;
          gap: 8px;
          padding: 6px 12px;
          font-size: 12px;
          font-weight: 500;
          cursor: pointer;
          border-radius: 3px;
          color: var(--text);
        }
        .dropdown-item-flyout:hover {
          background: var(--bg-soft);
          color: var(--accent);
        }

        @media (max-width: 580px) {
          .hide-mobile {
            display: none !important;
          }
        }

      `}</style>

      {/* Universal Top Header Bar for all Admin Pages */}
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
        position: 'sticky',
        top: 0,
        zIndex: 100
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexShrink: 0, minWidth: 0 }}>
          <div 
            onClick={() => { triggerNavStart(); router.push('/admin'); }}
            onMouseEnter={() => router.prefetch('/admin')}
            style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer', flexShrink: 0 }}
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

          {pathname !== '/admin' && (
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', minWidth: 0 }}>
              <span style={{ color: 'var(--border-popover)', fontSize: '14px', flexShrink: 0 }}>/</span>
              <span 
                className="hide-mobile"
                style={{ 
                  fontWeight: 700, 
                  fontSize: '0.95rem', 
                  color: 'var(--text)', 
                  whiteSpace: 'nowrap', 
                  overflow: 'hidden', 
                  textOverflow: 'ellipsis' 
                }}
              >
                {getAdminPageTitle(pathname)}
              </span>
            </div>
          )}
        </div>

        <div className="page-header-actions" style={{ display: 'flex', alignItems: 'center', gap: '8px', flexShrink: 0 }}>
          <TopBarTimeTracker />

          {/* Notices */}
          <button 
            className="page-header-btn" 
            onClick={() => { triggerNavStart(); router.push('/admin/notices'); }}
            onMouseEnter={() => router.prefetch('/admin/notices')}
            title="Notices & Announcements"
            style={{ 
              background: pathname === '/admin/notices' ? 'var(--warning-bg)' : 'rgba(255,255,255,0.05)', 
              border: pathname === '/admin/notices' ? '1px solid var(--warning)' : '1px solid var(--border)', 
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
            <Bell size={16} color="var(--warning)" />
          </button>

          {/* Live Chat with Unread Badge Counter */}
          <TopBarChatButton role="admin" chatUrl="/admin/chat" count={unreadChatCount} />

          {/* Settings */}
          <button 
            className="page-header-btn" 
            onClick={() => { triggerNavStart(); router.push('/admin/settings'); }}
            onMouseEnter={() => router.prefetch('/admin/settings')}
            title="Admin Settings"
            style={{ 
              background: pathname === '/admin/settings' ? 'var(--surface-3)' : 'rgba(255,255,255,0.05)', 
              border: pathname === '/admin/settings' ? '1px solid var(--accent)' : '1px solid var(--border)', 
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
            <Settings size={16} color="var(--text-muted)" />
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
              color: 'var(--danger)', 
              cursor: 'pointer',
              flexShrink: 0
            }} 
            title="Logout"
          >
            <LogOut size={16} />
          </button>
        </div>
      </header>

      {/* Main Administrative Pages Workspace */}
      <div style={{ 
        flex: 1,
        display: 'flex',
        flexDirection: 'column',
        paddingBottom: pathname === '/admin/chat' ? '0' : '80px',
        overflow: pathname === '/admin/chat' ? 'hidden' : undefined
      }}>
        {children}
      </div>

      {/* Floating Hamburger Menu Trigger */}
      {pathname !== '/admin/chat' && (
        <button 
          ref={hamburgerRef}
          className={`nav-hamburger-btn ${panelOpen ? 'open' : ''}`}
          onClick={() => { setPanelOpen(!panelOpen); setActiveSubmenu(null); }}
          aria-label="Toggle Menu"
        >
          <span className="hb-icon">☰</span>
        </button>
      )}

      {/* Menu Panel */}
      <div 
        ref={panelRef}
        className={`nav-chip-panel ${panelOpen ? 'show' : ''}`}
      >
        {chips.map(c => {
          const isCurrentActive = activeSubmenu === c.id;
          const hasChatUnread = c.id === 'manage' && unreadChatCount > 0;
          return (
            <button 
              key={c.id}
              data-chip-id={c.id}
              className={`nav-item ${isCurrentActive ? 'active' : ''}`}
              onClick={(e) => handleChipClick(e, c.id)}
              onMouseEnter={() => {
                if (c.url) router.prefetch(c.url);
                ADMIN_SUBMENUS[c.id]?.forEach(s => {
                  if (s.url && s.url !== '#') router.prefetch(s.url);
                });
              }}
              style={{ position: 'relative' }}
            >
              <span className="nav-icon">{c.icon}</span>
              <span className="nav-label">{c.en}</span>
              {hasChatUnread && (
                <span 
                  style={{
                    position: 'absolute',
                    top: '4px',
                    right: '6px',
                    background: '#ef4444',
                    color: '#fff',
                    fontSize: '9px',
                    fontWeight: 800,
                    padding: '1px 5px',
                    borderRadius: '8px',
                    lineHeight: 1
                  }}
                >
                  {unreadChatCount > 99 ? '99+' : unreadChatCount}
                </span>
              )}
            </button>
          );
        })}
      </div>

      {/* Flyout Submenu Dropdown */}
      {panelOpen && activeSubmenu && (
        <div 
          ref={dropdownRef}
          className="dropdown-menu-flyout"
        >
          {ADMIN_SUBMENUS[activeSubmenu]?.map((item, idx) => (
            <div 
              key={idx}
              className="dropdown-item-flyout"
              onClick={() => handleSubmenuItemClick(item)}
              onMouseEnter={() => {
                if (item.url && item.url !== '#') router.prefetch(item.url);
              }}
              style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span>{item.icon}</span>
                <span>{item.en}</span>
              </div>
              {item.url === '/admin/chat' && unreadChatCount > 0 && (
                <span 
                  style={{
                    background: '#ef4444',
                    color: '#ffffff',
                    fontSize: '10px',
                    fontWeight: 800,
                    padding: '2px 6px',
                    borderRadius: '8px',
                    lineHeight: 1,
                    marginLeft: '8px'
                  }}
                >
                  {unreadChatCount > 99 ? '99+' : unreadChatCount}
                </span>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
