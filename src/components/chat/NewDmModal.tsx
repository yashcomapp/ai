'use client';

import React from 'react';

export interface UserProfile {
  studentCode: string;
  name: string;
  role: string;
  email: string;
  parentEmail?: string;
  parentName?: string;
  parentPhone?: string;
  status?: string;
  batchId?: string;
  class?: string | number;
}

export interface NewDmModalProps {
  showDmModal: boolean;
  setShowDmModal: (show: boolean) => void;
  searchQuery: string;
  setSearchQuery: (query: string) => void;
  filteredStudents: UserProfile[];
  handleStartDM: (studentCode: string, name: string) => void;
}

export function NewDmModal({
  showDmModal,
  setShowDmModal,
  searchQuery,
  setSearchQuery,
  filteredStudents,
  handleStartDM,
}: NewDmModalProps) {
  if (!showDmModal) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.6)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
      <div style={{ background: 'var(--surface-popover)', border: '1px solid var(--border)', borderRadius: '12px', maxWidth: '480px', width: '100%', maxHeight: '80vh', display: 'flex', flexDirection: 'column', boxShadow: '0 4px 24px rgba(0,0,0,0.3)', color: 'var(--text)' }}>
        
        <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 700, color: 'var(--text)' }}>💬 Start Private Direct Message</h3>
          <button style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.5rem', color: 'var(--text-muted)', lineHeight: 1 }} onClick={() => setShowDmModal(false)}>×</button>
        </div>

        <div style={{ padding: '12px 20px', borderBottom: '1px solid var(--border)' }}>
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search student code or name..."
            style={{ width: '100%', padding: '9px 12px', borderRadius: '8px', border: '1px solid var(--border)', background: 'var(--surface)', color: 'var(--text)', fontSize: '16px', outline: 'none' }}
          />
        </div>

        <div style={{ flex: 1, overflowY: 'auto', padding: '10px' }}>
          {filteredStudents.length === 0 ? (
            <div style={{ color: 'var(--text-muted)', fontSize: '13px', padding: '20px', textAlign: 'center' }}>No matches found.</div>
          ) : (
            filteredStudents.map(student => (
              <div
                key={student.studentCode}
                onClick={() => handleStartDM(student.studentCode, student.name)}
                style={{
                  padding: '10px 14px',
                  borderRadius: '8px',
                  cursor: 'pointer',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  transition: 'background 0.2s',
                  marginBottom: '4px'
                }}
                onMouseEnter={(e) => e.currentTarget.style.background = 'var(--surface-2)'}
                onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
              >
                <div>
                  <div style={{ fontSize: '13.5px', fontWeight: 600, color: 'var(--text)' }}>{student.name}</div>
                  <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>Student</div>
                </div>
                <span style={{ fontSize: '12px', color: 'var(--accent)', fontWeight: 600 }}>Chat →</span>
              </div>
            ))
          )}
        </div>

      </div>
    </div>
  );
}

export default NewDmModal;
