'use client';

import React from 'react';

interface SubjectiveModeBadgesProps {
  mode: string;
  peerStatus: string;
}

export function SubjectiveModeBadges({ mode, peerStatus }: SubjectiveModeBadgesProps) {
  return (
    <>
      <td style={{ padding: '6px 8px', whiteSpace: 'nowrap' }}>
        {mode === 'home' ? (
          <span className="badge badge-info" style={{ fontSize: '10px', whiteSpace: 'nowrap' }}>🏠 Home</span>
        ) : (
          <span className="badge badge-warning" style={{ fontSize: '10px', whiteSpace: 'nowrap' }}>🏫 Classroom</span>
        )}
      </td>
      <td style={{ padding: '6px 8px', textTransform: 'capitalize', fontSize: '12px', whiteSpace: 'nowrap' }}>
        {mode === 'classroom' ? (
          peerStatus === 'not_started' ? (
            <span style={{ color: 'var(--warning)', whiteSpace: 'nowrap' }}>⏳ Waiting</span>
          ) : peerStatus === 'assigned' ? (
            <span style={{ color: 'var(--accent)', whiteSpace: 'nowrap' }}>🔄 In Progress</span>
          ) : (
            <span style={{ color: 'var(--success)', whiteSpace: 'nowrap' }}>✅ Finished</span>
          )
        ) : (
          '—'
        )}
      </td>
    </>
  );
}
