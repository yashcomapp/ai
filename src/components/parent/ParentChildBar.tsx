'use client';

import React from 'react';
import { User, GraduationCap, ChevronDown } from 'lucide-react';
import { Child } from './types';

interface ParentChildBarProps {
  isLoading: boolean;
  userName?: string | null;
  userDisplayName?: string | null;
  greeting: string;
  childrenList: Child[];
  selectedChildCode: string;
  onSelectChild: (studentCode: string) => void;
}

export const ParentChildBar = React.memo(function ParentChildBar({
  isLoading,
  userName,
  userDisplayName,
  greeting,
  childrenList,
  selectedChildCode,
  onSelectChild
}: ParentChildBarProps) {
  if (isLoading) {
    return (
      <div className="card skeleton-blink" style={{
        background: 'var(--surface)',
        border: '1px solid var(--border-light)',
        borderRadius: 'var(--radius)',
        padding: '8px 12px',
        marginBottom: '8px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <div style={{ width: '32px', height: '32px', borderRadius: '50%', background: 'var(--surface-2)' }}></div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
            <div style={{ width: '70px', height: '10px', background: 'var(--surface-3)', borderRadius: '3px' }}></div>
            <div style={{ width: '100px', height: '14px', background: 'var(--surface-2)', borderRadius: '4px' }}></div>
          </div>
        </div>
        <div style={{ width: '130px', height: '32px', background: 'var(--surface-2)', borderRadius: 'var(--radius-sm)' }}></div>
      </div>
    );
  }

  if (!childrenList || childrenList.length === 0) return null;

  const parentName = (userName || userDisplayName || 'Parent').replace(/\s*ji$/i, '') + ' ji';
  const active = childrenList.find(c => c.studentCode === selectedChildCode) || childrenList[0];
  const classLabel = (() => {
    if (active?.className && active.className.trim()) {
      return active.className.startsWith('Class') ? active.className : `Class ${active.className}`;
    }
    if ((active as any)?.class) {
      return String((active as any).class).startsWith('Class') ? String((active as any).class) : `Class ${(active as any).class}`;
    }
    return 'Student';
  })();

  return (
    <div className="card" style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      gap: '8px',
      marginBottom: '8px',
      padding: '8px 12px',
      borderRadius: 'var(--radius)',
      border: '1px solid var(--border-light)',
      background: 'var(--surface)',
      boxShadow: 'var(--shadow-sm)',
      flexWrap: 'nowrap'
    }}>
      {/* Left: Parent Greeting */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', minWidth: 0 }}>
        <div style={{
          width: '32px',
          height: '32px',
          borderRadius: '50%',
          background: 'var(--accent-soft)',
          border: '1px solid var(--accent-ring)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          flexShrink: 0
        }}>
          <User size={16} color="var(--accent)" />
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', minWidth: 0 }}>
          <span suppressHydrationWarning style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', lineHeight: 1.1 }}>
            {greeting}
          </span>
          <span style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.2, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
            {parentName}
          </span>
        </div>
      </div>

      {/* Right: Child Selector */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        background: 'var(--bg-soft)',
        border: '1px solid var(--border-light)',
        borderRadius: 'var(--radius-sm)',
        padding: '4px 8px',
        gap: '6px',
        position: 'relative'
      }}>
        <div style={{
          width: '24px',
          height: '24px',
          borderRadius: '50%',
          background: 'var(--accent-soft)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          flexShrink: 0
        }}>
          <GraduationCap size={14} color="var(--accent)" />
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', minWidth: 0 }}>
          <div style={{ display: 'flex', alignItems: 'center', position: 'relative' }}>
            <select 
              value={selectedChildCode}
              onChange={(e) => onSelectChild(e.target.value)}
              style={{ 
                background: 'transparent', 
                border: 'none', 
                color: 'var(--text)', 
                fontSize: '13px', 
                fontWeight: 800, 
                outline: 'none', 
                cursor: 'pointer',
                paddingRight: '14px',
                appearance: 'none',
                WebkitAppearance: 'none'
              }}
            >
              {childrenList.map(c => (
                <option key={c.studentCode} value={c.studentCode} style={{ background: 'var(--surface)', color: 'var(--text)' }}>
                  {c.name}
                </option>
              ))}
            </select>
            <ChevronDown size={12} color="var(--text-muted)" style={{ position: 'absolute', right: 0, pointerEvents: 'none' }} />
          </div>
          <span style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '-1px', fontWeight: 600 }}>
            {classLabel}
          </span>
        </div>
      </div>
    </div>
  );
});
