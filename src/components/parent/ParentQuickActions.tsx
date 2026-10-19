'use client';

import React from 'react';
import { useRouter } from 'next/navigation';
import { Rocket, Calendar, ClipboardList, Receipt, MessageSquare } from 'lucide-react';
import { ParentDashboardData } from './types';

interface ParentQuickActionsProps {
  selectedChildCode: string;
  data?: ParentDashboardData | null;
  childData?: ParentDashboardData | null;
}

export const ParentQuickActions = React.memo(function ParentQuickActions({
  selectedChildCode,
  data,
  childData
}: ParentQuickActionsProps) {
  const router = useRouter();

  const attendanceRate = (data as any)?.stats?.attendanceRate !== undefined 
    ? `${(data as any).stats.attendanceRate}%` 
    : ((data as any)?.profile?.attendanceRate !== undefined 
      ? `${(data as any).profile.attendanceRate}%` 
      : '100%');

  const absentCount = childData?.snapshot?.absentExamsCount || data?.snapshot?.absentExamsCount || 0;

  return (
    <div className="card card-purple" style={{
      borderRadius: 'var(--radius)',
      padding: '10px 12px',
      marginBottom: '8px',
      boxShadow: 'var(--shadow-sm)'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '8px' }}>
        <Rocket size={18} color="var(--primary)" />
        <h3 style={{ margin: 0, fontSize: '13.5px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.2 }}>
          Quick Actions / त्वरित कार्य
        </h3>
      </div>
      {/* Bento Grid: 4 Action Modules in 1 Single Line */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(4, 1fr)',
        gap: '6px',
        alignItems: 'stretch'
      }}>
        {/* Bento Item 1: Attendance */}
        <div
          onClick={() => router.push(`/parent/attendance?studentCode=${selectedChildCode}`)}
          style={{
            background: 'var(--surface-2)',
            border: '1.5px solid var(--border)',
            borderRadius: 'var(--radius-sm)',
            padding: '8px 3px',
            cursor: 'pointer',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            textAlign: 'center',
            gap: '3px',
            transition: 'all 0.2s ease',
            boxShadow: 'var(--shadow-sm)'
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.borderColor = 'var(--success)';
            e.currentTarget.style.transform = 'translateY(-2px)';
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.borderColor = 'var(--border)';
            e.currentTarget.style.transform = 'translateY(0)';
          }}
        >
          <Calendar size={22} color="var(--success)" />
          <div style={{ fontSize: '10px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.15, whiteSpace: 'nowrap' }}>
            Attendance
          </div>
          <div style={{ fontSize: '9px', color: 'var(--text-muted)', lineHeight: 1 }}>
            उपस्थिति
          </div>
          <div style={{ fontSize: '9.5px', color: 'var(--success)', fontWeight: 800, whiteSpace: 'nowrap', marginTop: '1px' }}>
            {attendanceRate}
          </div>
        </div>

        {/* Bento Item 2: Exam Register */}
        <div
          onClick={() => router.push(`/exam-register?studentCode=${selectedChildCode}`)}
          style={{
            background: 'var(--surface-2)',
            border: '1.5px solid var(--border)',
            borderRadius: 'var(--radius-sm)',
            padding: '8px 3px',
            cursor: 'pointer',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            textAlign: 'center',
            gap: '3px',
            transition: 'all 0.2s ease',
            boxShadow: 'var(--shadow-sm)'
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.borderColor = 'var(--primary)';
            e.currentTarget.style.transform = 'translateY(-2px)';
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.borderColor = 'var(--border)';
            e.currentTarget.style.transform = 'translateY(0)';
          }}
        >
          <ClipboardList size={22} color="var(--primary)" />
          <div style={{ fontSize: '10px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.15, whiteSpace: 'nowrap' }}>
            Exam Register
          </div>
          <div style={{ fontSize: '9px', color: 'var(--text-muted)', lineHeight: 1 }}>
            परीक्षा रजिस्टर
          </div>
          <div style={{ fontSize: '9.5px', color: absentCount > 0 ? 'var(--danger)' : 'var(--primary)', fontWeight: 800, whiteSpace: 'nowrap', marginTop: '1px' }}>
            {absentCount > 0 ? `${absentCount} Absent` : 'Active / सक्रिय'}
          </div>
        </div>

        {/* Bento Item 3: Fees & Dues */}
        <div
          onClick={() => router.push(`/parent/fees?studentCode=${selectedChildCode}`)}
          style={{
            background: 'var(--surface-2)',
            border: '1.5px solid var(--border)',
            borderRadius: 'var(--radius-sm)',
            padding: '8px 3px',
            cursor: 'pointer',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            textAlign: 'center',
            gap: '3px',
            transition: 'all 0.2s ease',
            boxShadow: 'var(--shadow-sm)'
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.borderColor = 'var(--warning)';
            e.currentTarget.style.transform = 'translateY(-2px)';
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.borderColor = 'var(--border)';
            e.currentTarget.style.transform = 'translateY(0)';
          }}
        >
          <Receipt size={22} color="var(--warning)" />
          <div style={{ fontSize: '10px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.15, whiteSpace: 'nowrap' }}>
            Fees &amp; Dues
          </div>
          <div style={{ fontSize: '9px', color: 'var(--text-muted)', lineHeight: 1 }}>
            फीस विवरण
          </div>
          <div style={{ fontSize: '9.5px', color: 'var(--warning)', fontWeight: 800, whiteSpace: 'nowrap', marginTop: '1px' }}>
            Receipts / रसीद
          </div>
        </div>

        {/* Bento Item 4: Chat */}
        <div
          onClick={() => router.push('/parent/chat')}
          style={{
            background: 'var(--surface-2)',
            border: '1.5px solid var(--border)',
            borderRadius: 'var(--radius-sm)',
            padding: '8px 3px',
            cursor: 'pointer',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            textAlign: 'center',
            gap: '3px',
            transition: 'all 0.2s ease',
            boxShadow: 'var(--shadow-sm)'
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.borderColor = 'var(--info)';
            e.currentTarget.style.transform = 'translateY(-2px)';
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.borderColor = 'var(--border)';
            e.currentTarget.style.transform = 'translateY(0)';
          }}
        >
          <MessageSquare size={22} color="var(--info)" />
          <div style={{ fontSize: '10px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.15, whiteSpace: 'nowrap' }}>
            Chat Desk
          </div>
          <div style={{ fontSize: '9px', color: 'var(--text-muted)', lineHeight: 1 }}>
            शिक्षक संवाद
          </div>
          <div style={{ fontSize: '9.5px', color: 'var(--info)', fontWeight: 800, whiteSpace: 'nowrap', marginTop: '1px' }}>
            Messages / चैट
          </div>
        </div>
      </div>
    </div>
  );
});
