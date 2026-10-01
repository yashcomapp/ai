'use client';

import React from 'react';

export interface NewGroupModalProps {
  showGroupModal: boolean;
  setShowGroupModal: (show: boolean) => void;
  batchesList: { id: string; name: string }[];
  selectedBatchId: string;
  setSelectedBatchId: (id: string) => void;
  groupName: string;
  setGroupName: (name: string) => void;
  handleCreateGroup: (e: React.FormEvent) => void;
}

export function NewGroupModal({
  showGroupModal,
  setShowGroupModal,
  batchesList,
  selectedBatchId,
  setSelectedBatchId,
  groupName,
  setGroupName,
  handleCreateGroup,
}: NewGroupModalProps) {
  if (!showGroupModal) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.6)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
      <div style={{ background: 'var(--surface-popover)', border: '1px solid var(--border)', borderRadius: '12px', maxWidth: '480px', width: '100%', boxShadow: '0 4px 24px rgba(0,0,0,0.3)', color: 'var(--text)' }}>
        
        <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 700, color: 'var(--text)' }}>👥 Setup Batch Group Chat</h3>
          <button style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.5rem', color: 'var(--text-muted)', lineHeight: 1 }} onClick={() => setShowGroupModal(false)}>×</button>
        </div>

        <form onSubmit={handleCreateGroup} style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '14px' }}>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
            <label style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)' }}>Select Batch</label>
            <select
              value={selectedBatchId}
              onChange={(e) => {
                setSelectedBatchId(e.target.value);
                const bName = batchesList.find(b => b.id === e.target.value)?.name || '';
                setGroupName(`${bName} Chat Group`);
              }}
              style={{ padding: '8px 10px', borderRadius: '6px', border: '1px solid var(--border)', background: 'var(--surface)', color: 'var(--text)', fontSize: '16px', outline: 'none' }}
            >
              {batchesList.map(b => (
                <option key={b.id} value={b.id}>{b.name}</option>
              ))}
            </select>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
            <label style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)' }}>Group Name</label>
            <input
              type="text"
              required
              value={groupName}
              onChange={(e) => setGroupName(e.target.value)}
              style={{ padding: '8px 10px', borderRadius: '6px', border: '1px solid var(--border)', background: 'var(--surface)', color: 'var(--text)', fontSize: '16px', outline: 'none' }}
            />
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
              boxShadow: '0 2px 8px rgba(79, 70, 229, 0.45)',
              transition: 'transform 0.1s'
            }}
            onMouseDown={(e) => e.currentTarget.style.transform = 'scale(0.98)'}
            onMouseUp={(e) => e.currentTarget.style.transform = 'scale(1)'}
          >
            Create Group Chat
          </button>

        </form>
      </div>
    </div>
  );
}

export default NewGroupModal;
