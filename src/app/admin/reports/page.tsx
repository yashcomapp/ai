'use client';

import React from 'react';
import { useRouter } from 'next/navigation';

interface ReportCard {
  title: string;
  description: string;
  path: string;
  icon: string;
  badge?: string;
}

const REPORT_SECTIONS: ReportCard[] = [
  {
    title: 'Learning Quotient (LQ) Reports',
    description: 'Comprehensive 5-pillar student quotients, continuous observations, multi-component metrics and WhatsApp card dispatch.',
    path: '/admin/reports/learning-quotient',
    icon: '📊',
    badge: 'Core Analytics'
  },
  {
    title: 'Daily Practice Reports',
    description: 'Real-time practice sets completion, accuracy percentages, autonomous activity, and topic mastery locks.',
    path: '/admin/reports/daily-practice',
    icon: '📝',
    badge: 'Daily Activity'
  },
  {
    title: 'Login & Presence Register',
    description: 'Daily audit trail of student and parent session logins, device disconnects, and cumulative usage times.',
    path: '/admin/reports/login-register',
    icon: '🕒',
    badge: 'Presence Audit'
  },
  {
    title: 'Parent Pending Action Reports',
    description: 'Track outstanding parent homework reviews, pending confirmations, and signature requirements.',
    path: '/admin/reports/parent-pending',
    icon: '👨‍👩‍👧',
    badge: 'Engagement'
  },
  {
    title: 'System Usage & Time Logs',
    description: 'Detailed breakdown of active session durations, device platform analytics, and student time distribution.',
    path: '/admin/reports/usage',
    icon: '📈',
    badge: 'Telemetry'
  }
];

export default function AdminReportsHubPage() {
  const router = useRouter();

  return (
    <div style={{ background: 'var(--bg)', flex: 1, display: 'flex', flexDirection: 'column' }}>

      {/* Main Container */}
      <main style={{ flex: 1, padding: '24px 16px', maxWidth: '1100px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>
        <div>
          <h2 style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text)', margin: '0 0 4px' }}>
            Analytics & Management Reports
          </h2>
          <p style={{ fontSize: '13px', color: 'var(--text-muted)', margin: 0 }}>
            Select a report section below to view metrics, analyze performance, or export PDF summaries.
          </p>
        </div>

        {/* Report Cards Grid */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))',
          gap: '16px'
        }}>
          {REPORT_SECTIONS.map((report) => (
            <div
              key={report.path}
              onClick={() => router.push(report.path)}
              className="card"
              style={{
                background: 'var(--surface)',
                border: '1px solid var(--border-light)',
                borderRadius: 'var(--radius, 12px)',
                padding: '20px',
                cursor: 'pointer',
                transition: 'all 0.2s ease',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                boxShadow: 'var(--shadow-sm)'
              }}
              onMouseOver={(e) => {
                e.currentTarget.style.borderColor = 'var(--accent)';
                e.currentTarget.style.transform = 'translateY(-2px)';
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.borderColor = 'var(--border-light)';
                e.currentTarget.style.transform = 'translateY(0)';
              }}
            >
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                  <span style={{ fontSize: '28px' }}>{report.icon}</span>
                  {report.badge && (
                    <span style={{
                      fontSize: '11px',
                      fontWeight: 700,
                      padding: '3px 8px',
                      borderRadius: 'var(--radius-sm, 6px)',
                      background: 'var(--accent-soft, rgba(217, 123, 56, 0.12))',
                      color: 'var(--accent)'
                    }}>
                      {report.badge}
                    </span>
                  )}
                </div>
                <h3 style={{ fontSize: '15px', fontWeight: 800, color: 'var(--text)', margin: '0 0 6px' }}>
                  {report.title}
                </h3>
                <p style={{ fontSize: '12.5px', color: 'var(--text-muted)', lineHeight: 1.5, margin: 0 }}>
                  {report.description}
                </p>
              </div>

              <div style={{ marginTop: '16px', display: 'flex', alignItems: 'center', gap: '6px', fontSize: '13px', fontWeight: 700, color: 'var(--accent)' }}>
                <span>Open Report</span>
                <span>→</span>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}
