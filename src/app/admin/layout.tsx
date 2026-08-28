'use client';

import React, { useState, useEffect, useRef } from 'react';
import { useRouter, usePathname } from 'next/navigation';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';

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
    { icon: '🪙', en: 'Fees Manager', url: '/admin/fees' },
    { icon: '📝', en: 'Registrations', url: '/admin/registrations' },
    { icon: '👥', en: 'Students', url: '/admin/students' },
    { icon: '📦', en: 'Batches', url: '/admin/batches' }
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
  const pathname = usePathname();
  const { toggleTheme } = useTheme();

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

  const handleChipClick = (e: React.MouseEvent, chipId: string) => {
    e.stopPropagation();

    if (activeSubmenu === chipId) {
      setActiveSubmenu(null);
      return;
    }
    
    setActiveSubmenu(chipId);
  };

  const handleSubmenuItemClick = (item: SubmenuItem) => {
    if (item.url && item.url !== '#') {
      router.push(item.url);
    } else {
      alert(`Feature "${item.en}" is legacy or placeholder.`);
    }
    setPanelOpen(false);
    setActiveSubmenu(null);
  };

  const chips = [
    { id: 'exams', icon: '📚', en: 'Exams' },
    { id: 'qb', icon: '📒', en: 'QB' },
    { id: 'manage', icon: '👥', en: 'Manage' },
    { id: 'reports', icon: '📈', en: 'Reports' },
    { id: 'settings', icon: '⚙️', en: 'Settings' }
  ];

  return (
    <div className="page-wrapper">
      {/* Injecting Legacy styling exact layout */}
      <style>{`
        /* Floating Hamburger */
        .nav-hamburger-btn {
          position: fixed;
          bottom: 16px;
          right: 16px;
          width: 52px;
          height: 52px;
          border-radius: 50%;
          background: var(--accent-grad);
          color: #ffffff;
          border: none;
          box-shadow: var(--shadow-lg);
          font-size: 24px;
          z-index: 10000;
          cursor: pointer;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: transform 0.2s ease;
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
          color: #ffffff;
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

        /* Edge Sliver */
        .nav-dashboard-sliver {
          position: fixed;
          top: 0;
          right: 0;
          width: 6px;
          height: 100vh;
          border: none;
          background: var(--accent);
          opacity: .25;
          cursor: pointer;
          z-index: 9999;
          padding: 0;
          transition: opacity .15s ease, width .15s ease;
        }
        .nav-dashboard-sliver:hover {
          opacity: .8;
          width: 10px;
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
      `}</style>

      {/* Main Administrative Pages Workspace */}
      <div style={{ paddingBottom: pathname === '/admin/chat' ? '0' : '80px' }}>
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
          return (
            <button 
              key={c.id}
              data-chip-id={c.id}
              className={`nav-item ${isCurrentActive ? 'active' : ''}`}
              onClick={(e) => handleChipClick(e, c.id)}
            >
              <span className="nav-icon">{c.icon}</span>
              <span className="nav-label">{c.en}</span>
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
            >
              <span>{item.icon}</span>
              <span>{item.en}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
