'use client';

import React from 'react';
import { Moon, CheckCircle2, Video } from 'lucide-react';

interface ParentDailySyncBannerProps {
  isLoading: boolean;
  dailySyncDoneToday: boolean;
  isSyncTimeSlot: boolean;
  onStartSync: () => void;
}

export const ParentDailySyncBanner = React.memo(function ParentDailySyncBanner({
  isLoading,
  dailySyncDoneToday,
  isSyncTimeSlot,
  onStartSync
}: ParentDailySyncBannerProps) {
  if (isLoading) {
    return (
      <div className="card skeleton-blink" style={{
        background: 'var(--surface)',
        border: '1px solid var(--border-light)',
        borderRadius: 'var(--radius)',
        padding: '10px 12px',
        marginBottom: '8px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
          <div style={{ width: '18px', height: '18px', borderRadius: '50%', background: 'var(--surface-2)' }}></div>
          <div style={{ width: '150px', height: '14px', background: 'var(--surface-2)', borderRadius: '4px' }}></div>
        </div>
        <div style={{ width: '120px', height: '28px', background: 'var(--surface-2)', borderRadius: '8px' }}></div>
      </div>
    );
  }

  return (
    <div className="card card-accent" style={{
      borderRadius: 'var(--radius)',
      padding: '10px 12px',
      marginBottom: '8px',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      gap: '8px',
      boxShadow: 'var(--shadow-sm)'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
        <Moon size={18} color="var(--accent)" />
        <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.2 }}>
          Daily 5-Min Parent-Kid Sync
        </h3>
      </div>

      <div>
        {dailySyncDoneToday ? (
          <div style={{ display: 'flex', alignItems: 'center', gap: '4px', background: 'var(--success-bg)', border: '1px solid rgba(52, 211, 153, 0.3)', padding: '6px 10px', borderRadius: 'var(--radius)', color: 'var(--success)', fontWeight: 700, fontSize: '11px' }}>
            <CheckCircle2 size={14} color="var(--success)" />
            <span>Verified for Today!</span>
          </div>
        ) : (
          <button 
            className="btn"
            disabled={!isSyncTimeSlot}
            onClick={onStartSync}
            style={{
              background: isSyncTimeSlot ? 'var(--accent)' : 'var(--surface-2)',
              color: isSyncTimeSlot ? 'var(--text-on-accent)' : 'var(--text-muted)',
              fontWeight: 700,
              fontSize: '12px',
              padding: '6px 12px',
              borderRadius: '8px',
              border: '1px solid var(--border)',
              cursor: isSyncTimeSlot ? 'pointer' : 'not-allowed',
              opacity: isSyncTimeSlot ? 1 : 0.85,
              boxShadow: isSyncTimeSlot ? 'var(--shadow-sm)' : 'none',
              display: 'flex',
              alignItems: 'center',
              gap: '5px'
            }}
            title={isSyncTimeSlot ? 'Start live 5-minute sync with photo verification' : 'Parent-Child Sync starts at 9:30 PM IST'}
          >
            {isSyncTimeSlot ? (
              <>
                <Video size={14} color="var(--text-white)" />
                <span>Start 5-Min Sync</span>
              </>
            ) : (
              <span>Starts at 9:30 PM IST</span>
            )}
          </button>
        )}
      </div>
    </div>
  );
});
