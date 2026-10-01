'use client';

import React from 'react';

export interface PollCreationModalProps {
  showPollModal: boolean;
  setShowPollModal: (show: boolean) => void;
  pollQuestion: string;
  setPollQuestion: (question: string) => void;
  pollOptionsInput: string[];
  setPollOptionsInput: React.Dispatch<React.SetStateAction<string[]>>;
  handleCreatePoll: (e: React.FormEvent) => void;
}

export function PollCreationModal({
  showPollModal,
  setShowPollModal,
  pollQuestion,
  setPollQuestion,
  pollOptionsInput,
  setPollOptionsInput,
  handleCreatePoll,
}: PollCreationModalProps) {
  if (!showPollModal) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.6)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
      <div style={{ background: 'var(--surface-popover)', border: '1px solid var(--border)', borderRadius: '12px', maxWidth: '400px', width: '100%', boxShadow: '0 4px 24px rgba(0,0,0,0.3)', color: 'var(--text)', display: 'flex', flexDirection: 'column' }}>
        <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 700, color: 'var(--text)' }}>📊 Create Interactive Poll</h3>
          <button style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.5rem', color: 'var(--text-muted)', lineHeight: 1 }} onClick={() => setShowPollModal(false)}>×</button>
        </div>
        <form onSubmit={handleCreatePoll} style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '14px' }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
            <label style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)' }}>Poll Question / Title</label>
            <input
              type="text"
              required
              value={pollQuestion}
              onChange={(e) => setPollQuestion(e.target.value)}
              placeholder="e.g. Schedule extra revision class?"
              style={{ padding: '8px 10px', borderRadius: '6px', border: '1px solid var(--border)', background: 'var(--surface)', color: 'var(--text)', fontSize: '16px', outline: 'none' }}
            />
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <label style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)' }}>Options (at least 2)</label>
            {pollOptionsInput.map((opt, idx) => (
              <div key={idx} style={{ display: 'flex', gap: '6px' }}>
                <input
                  type="text"
                  required={idx < 2}
                  value={opt}
                  onChange={(e) => {
                    const updated = [...pollOptionsInput];
                    updated[idx] = e.target.value;
                    setPollOptionsInput(updated);
                  }}
                  placeholder={`Option ${idx + 1}`}
                  style={{ flex: 1, padding: '8px 10px', borderRadius: '6px', border: '1px solid var(--border)', background: 'var(--surface)', color: 'var(--text)', fontSize: '16px', outline: 'none' }}
                />
                {pollOptionsInput.length > 2 && (
                  <button
                    type="button"
                    onClick={() => {
                      setPollOptionsInput(prev => prev.filter((_, i) => i !== idx));
                    }}
                    style={{ background: 'rgba(239, 68, 68, 0.15)', border: '1px solid rgba(239, 68, 68, 0.4)', color: 'var(--danger)', borderRadius: '6px', padding: '0 8px', cursor: 'pointer' }}
                  >
                    ✕
                  </button>
                )}
              </div>
            ))}
            {pollOptionsInput.length < 5 && (
              <button
                type="button"
                onClick={() => setPollOptionsInput(prev => [...prev, ''])}
                style={{ alignSelf: 'flex-start', background: 'transparent', border: 'none', color: 'var(--accent)', fontSize: '11px', fontWeight: 600, cursor: 'pointer', padding: '4px 0' }}
              >
                + Add Option
              </button>
            )}
          </div>
          <button 
            type="submit" 
            style={{ 
              marginTop: '8px', 
              padding: '10px', 
              background: 'var(--accent)', 
              border: 'none', 
              color: 'var(--text-white)', 
              fontSize: '13px', 
              fontWeight: 600, 
              borderRadius: '6px', 
              cursor: 'pointer',
              boxShadow: '0 2px 8px rgba(79, 70, 229, 0.45)'
            }}
          >
            Send Poll to Chat
          </button>
        </form>
      </div>
    </div>
  );
}

export default PollCreationModal;
