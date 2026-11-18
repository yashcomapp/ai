'use client';

import React from 'react';

// ==============================================================================
// 1. Learning Status Bar (SSOT Single-Line Status)
// ==============================================================================
export interface LearningStatusBarProps {
  masteredCount: number;
  practicedCount?: number;
  totalConducted: number;
}

export const LearningStatusBar: React.FC<LearningStatusBarProps> = React.memo(({
  masteredCount,
  practicedCount,
  totalConducted
}) => {
  const completionPercent = totalConducted > 0 ? Math.round((masteredCount / totalConducted) * 100) : 0;
  const practicedPercent = totalConducted > 0 && practicedCount !== undefined ? Math.round((practicedCount / totalConducted) * 100) : 0;
  const isAllExhausted = totalConducted > 0 && masteredCount === totalConducted;

  return (
    <div style={{
      background: isAllExhausted 
        ? 'linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(56, 189, 248, 0.12))' 
        : 'var(--surface)',
      border: `1px solid ${isAllExhausted ? 'rgba(52, 211, 153, 0.4)' : 'var(--border-light)'}`,
      borderRadius: 'var(--radius)',
      padding: '10px 14px',
      marginBottom: '12px',
      display: 'flex',
      flexWrap: 'wrap',
      justifyContent: 'space-between',
      alignItems: 'center',
      gap: '12px'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '14px', flexWrap: 'wrap' }}>
        {practicedCount !== undefined ? (
          <>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12.5px', fontWeight: 700, color: 'var(--text)', whiteSpace: 'nowrap' }}>
              <span style={{ color: 'var(--text-muted)' }}>🔄 Practiced:</span>
              <span style={{ color: 'var(--text)', fontWeight: 800 }}>
                {practicedCount} / {totalConducted}
              </span>
              <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>
                ({practicedPercent}%)
              </span>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12.5px', fontWeight: 700, color: 'var(--text)', whiteSpace: 'nowrap' }}>
              <span style={{ color: 'var(--text-muted)' }}>🏆 Mastered:</span>
              <span style={{ color: isAllExhausted ? 'var(--success)' : 'var(--accent)', fontWeight: 800 }}>
                {masteredCount} / {totalConducted}
              </span>
              <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>
                ({completionPercent}%)
              </span>
            </div>
          </>
        ) : (
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', fontWeight: 700, color: 'var(--text)', whiteSpace: 'nowrap' }}>
            <span style={{ color: 'var(--text-muted)', fontWeight: 800 }}>Status:</span>
            <span style={{ color: isAllExhausted ? 'var(--success)' : 'var(--accent)', fontWeight: 800 }}>
              {masteredCount} / {totalConducted} Topics Done
            </span>
            <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>
              ({completionPercent}%)
            </span>
          </div>
        )}
      </div>

      <div style={{ flex: '1', minWidth: '120px', maxWidth: '200px', display: 'flex', alignItems: 'center', gap: '8px' }}>
        <div style={{ flex: '1', height: '7px', background: 'var(--surface-2)', borderRadius: '4px', overflow: 'hidden', position: 'relative' }}>
          {practicedCount !== undefined && (
            <div 
              style={{ 
                position: 'absolute', 
                top: 0, 
                left: 0, 
                width: `${practicedPercent}%`, 
                height: '100%', 
                background: 'rgba(59, 130, 246, 0.4)', 
                borderRadius: '4px',
                transition: 'width 0.3s ease'
              }} 
              title={`Practiced: ${practicedPercent}%`} 
            />
          )}
          <div 
            style={{ 
              position: 'absolute', 
              top: 0, 
              left: 0, 
              width: `${completionPercent}%`, 
              height: '100%', 
              background: isAllExhausted ? 'var(--success)' : 'var(--accent)', 
              borderRadius: '4px', 
              transition: 'width 0.3s ease' 
            }} 
            title={`Mastered: ${completionPercent}%`} 
          />
        </div>
      </div>
    </div>
  );
});

LearningStatusBar.displayName = 'LearningStatusBar';

// ==============================================================================
// 2. Learning Tab Controls (SSOT Symmetric 2-Line Tab Layout)
// ==============================================================================
export interface LearningTabControlsProps {
  activeTab: 'needsAttention' | 'continuePractice' | 'mastered';
  onSelectTab: (tab: 'needsAttention' | 'continuePractice' | 'mastered') => void;
  counts: {
    needsAttention: number;
    continuePractice: number;
    mastered: number;
  };
}

export const LearningTabControls: React.FC<LearningTabControlsProps> = React.memo(({
  activeTab,
  onSelectTab,
  counts
}) => {
  return (
    <div className="review-tabs" style={{ display: 'flex', gap: '6px', marginBottom: '10px', borderBottom: 'none' }}>
      <button 
        className={`tab-btn ${activeTab === 'needsAttention' ? 'active' : ''}`} 
        onClick={() => onSelectTab('needsAttention')}
        style={{
          flex: 1,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '8px 4px',
          borderBottom: activeTab === 'needsAttention' ? '2px solid var(--accent)' : '2px solid transparent'
        }}
      >
        <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', whiteSpace: 'nowrap', fontSize: '13px', fontWeight: 700 }}>
          <span>🚨</span><span>Focus</span>
        </span>
        <span className="tab-count" style={{ marginTop: '4px', marginInline: 'auto' }}>
          {counts.needsAttention}
        </span>
      </button>

      <button 
        className={`tab-btn ${activeTab === 'continuePractice' ? 'active' : ''}`} 
        onClick={() => onSelectTab('continuePractice')}
        style={{
          flex: 1,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '8px 4px',
          borderBottom: activeTab === 'continuePractice' ? '2px solid var(--accent)' : '2px solid transparent'
        }}
      >
        <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', whiteSpace: 'nowrap', fontSize: '13px', fontWeight: 700 }}>
          <span>🔄</span><span>Practice</span>
        </span>
        <span className="tab-count" style={{ marginTop: '4px', marginInline: 'auto' }}>
          {counts.continuePractice}
        </span>
      </button>

      <button 
        className={`tab-btn ${activeTab === 'mastered' ? 'active' : ''}`} 
        onClick={() => onSelectTab('mastered')}
        style={{
          flex: 1,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '8px 4px',
          borderBottom: activeTab === 'mastered' ? '2px solid var(--accent)' : '2px solid transparent'
        }}
      >
        <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', whiteSpace: 'nowrap', fontSize: '13px', fontWeight: 700 }}>
          <span>🏆</span><span>Mastered</span>
        </span>
        <span className="tab-count" style={{ marginTop: '4px', marginInline: 'auto' }}>
          {counts.mastered}
        </span>
      </button>
    </div>
  );
});

LearningTabControls.displayName = 'LearningTabControls';

// ==============================================================================
// 3. Learning Practice Filter Bar (SSOT 1-Line Filter Controls)
// ==============================================================================
export interface LearningPracticeFilterBarProps {
  activeFilter: 'all' | 'zero' | 'in_progress' | 'locked';
  onSelectFilter: (filter: 'all' | 'zero' | 'in_progress' | 'locked') => void;
  breakdown: {
    total: number;
    zero: number;
    inProgress: number;
    locked: number;
  };
}

export const LearningPracticeFilterBar: React.FC<LearningPracticeFilterBarProps> = React.memo(({
  activeFilter,
  onSelectFilter,
  breakdown
}) => {
  return (
    <div style={{
      display: 'flex',
      gap: '6px',
      marginBottom: '12px',
      flexWrap: 'nowrap',
      overflowX: 'auto',
      alignItems: 'center',
      paddingBottom: '4px',
      WebkitOverflowScrolling: 'touch'
    }}>
      <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', marginRight: '2px', whiteSpace: 'nowrap' }}>
        Filter:
      </span>
      <button
        type="button"
        onClick={() => onSelectFilter('all')}
        style={{
          padding: '3px 9px',
          borderRadius: '20px',
          fontSize: '11px',
          fontWeight: 700,
          whiteSpace: 'nowrap',
          border: '1px solid ' + (activeFilter === 'all' ? 'var(--accent)' : 'var(--border-light)'),
          background: activeFilter === 'all' ? 'var(--accent)' : 'var(--bg-soft)',
          color: activeFilter === 'all' ? '#ffffff' : 'var(--text-muted)',
          cursor: 'pointer'
        }}
      >
        All Practice ({breakdown.total})
      </button>
      <button
        type="button"
        onClick={() => onSelectFilter('zero')}
        style={{
          padding: '3px 9px',
          borderRadius: '20px',
          fontSize: '11px',
          fontWeight: 800,
          whiteSpace: 'nowrap',
          border: '1px solid ' + (activeFilter === 'zero' ? '#ef4444' : 'var(--border-light)'),
          background: activeFilter === 'zero' ? 'rgba(239, 68, 68, 0.18)' : 'var(--bg-soft)',
          color: activeFilter === 'zero' ? '#ef4444' : 'var(--text-muted)',
          cursor: 'pointer'
        }}
      >
        🔴 Zero Practice ({breakdown.zero})
      </button>
      <button
        type="button"
        onClick={() => onSelectFilter('in_progress')}
        style={{
          padding: '3px 9px',
          borderRadius: '20px',
          fontSize: '11px',
          fontWeight: 700,
          whiteSpace: 'nowrap',
          border: '1px solid ' + (activeFilter === 'in_progress' ? '#f59e0b' : 'var(--border-light)'),
          background: activeFilter === 'in_progress' ? 'rgba(245, 158, 11, 0.18)' : 'var(--bg-soft)',
          color: activeFilter === 'in_progress' ? '#f59e0b' : 'var(--text-muted)',
          cursor: 'pointer'
        }}
      >
        🟡 In Progress ({breakdown.inProgress})
      </button>
      {breakdown.locked > 0 && (
        <button
          type="button"
          onClick={() => onSelectFilter('locked')}
          style={{
            padding: '3px 9px',
            borderRadius: '20px',
            fontSize: '11px',
            fontWeight: 700,
            whiteSpace: 'nowrap',
            border: '1px solid ' + (activeFilter === 'locked' ? '#94a3b8' : 'var(--border-light)'),
            background: activeFilter === 'locked' ? 'rgba(148, 163, 184, 0.25)' : 'var(--bg-soft)',
            color: activeFilter === 'locked' ? 'var(--text)' : 'var(--text-muted)',
            cursor: 'pointer'
          }}
        >
          🔒 Quota Locked ({breakdown.locked})
        </button>
      )}
    </div>
  );
});

LearningPracticeFilterBar.displayName = 'LearningPracticeFilterBar';
