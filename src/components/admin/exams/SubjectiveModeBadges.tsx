'use client';

import React from 'react';

interface SubjectiveModeBadgesProps {
  mode: string;
  peerStatus: string;
}

export function SubjectiveModeBadges({ mode, peerStatus }: SubjectiveModeBadgesProps) {
  return (
    <>
      <td style={{ padding: '4px 8px' }}>
        {mode === 'home' ? (
          <span className="badge badge-info" style={{ fontSize: '10px' }}>🏠 Home</span>
        ) : (
          <span className="badge badge-warning" style={{ fontSize: '10px' }}>🏫 Classroom</span>
        )}
      </td>
      <td style={{ padding: '4px 8px', textTransform: 'capitalize', fontSize: '12px' }}>
        {mode === 'classroom' ? (
          peerStatus === 'not_started' ? (
            <span style={{ color: 'var(--warning)' }}>⏳ Waiting</span>
          ) : peerStatus === 'assigned' ? (
            <span style={{ color: 'var(--accent)' }}>🔄 In Progress</span>
          ) : (
            <span style={{ color: 'var(--success)' }}>✅ Finished</span>
          )
        ) : (
          '—'
        )}
      </td>
    </>
  );
}
