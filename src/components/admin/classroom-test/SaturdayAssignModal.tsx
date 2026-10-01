'use client';

import React from 'react';

export interface SaturdayAssignModalState {
  show: boolean;
  examId: string;
  examName: string;
  batchId: string;
  startAtStr: string;
  endAtStr: string;
  examDuration: number | string;
  assignmentId?: string;
}

export interface SaturdayAssignModalProps {
  saturdayAssignModal: SaturdayAssignModalState;
  setSaturdayAssignModal: React.Dispatch<React.SetStateAction<SaturdayAssignModalState>>;
  batches: { id: string; name: string }[];
  handleSaveSaturdayAssignment: () => void;
}

export function SaturdayAssignModal({
  saturdayAssignModal,
  setSaturdayAssignModal,
  batches,
  handleSaveSaturdayAssignment,
}: SaturdayAssignModalProps) {
  if (!saturdayAssignModal.show) return null;

  return (
    <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.6)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 10000, padding: '16px' }}>
      <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', width: '100%', maxWidth: '480px', border: '1px solid var(--border-light)', overflow: 'hidden', padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px' }}>
          <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800, color: 'var(--accent)' }}>
            🏫 {saturdayAssignModal.assignmentId ? 'Modify Saturday Test Timing' : 'Set Saturday Test Timing & Activate'}
          </h3>
          <button style={{ background: 'none', border: 'none', cursor: 'pointer', fontSize: '16px', color: 'var(--text-muted)' }} onClick={() => setSaturdayAssignModal(prev => ({ ...prev, show: false }))}>✕</button>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
          <div>
            <strong style={{ fontSize: '11px', color: 'var(--text-muted)', textTransform: 'uppercase' }}>Exam Name:</strong>
            <div style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text)', marginTop: '2px' }}>{saturdayAssignModal.examName}</div>
          </div>

          <div className="form-group">
            <label style={{ fontSize: '11px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>Target Batch</label>
            <select 
              className="form-input" 
              value={saturdayAssignModal.batchId} 
              onChange={(e) => setSaturdayAssignModal(prev => ({ ...prev, batchId: e.target.value }))}
              disabled={!!saturdayAssignModal.assignmentId}
            >
              <option value="">-- Select Batch --</option>
              {batches.map(b => <option key={b.id} value={b.id}>{b.name}</option>)}
            </select>
          </div>

          <div className="form-group">
            <label style={{ fontSize: '11px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>Start Datetime (local)</label>
            <input 
              type="datetime-local" 
              className="form-input"
              value={saturdayAssignModal.startAtStr}
              onChange={(e) => setSaturdayAssignModal(prev => ({ ...prev, startAtStr: e.target.value }))}
            />
          </div>

          <div className="form-group">
            <label style={{ fontSize: '11px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>End Datetime (local)</label>
            <input 
              type="datetime-local" 
              className="form-input"
              value={saturdayAssignModal.endAtStr}
              onChange={(e) => setSaturdayAssignModal(prev => ({ ...prev, endAtStr: e.target.value }))}
            />
          </div>

          <div className="form-group">
            <label style={{ fontSize: '11px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>Exam Duration (minutes)</label>
            <input 
              type="number" 
              className="form-input"
              min={5}
              max={300}
              value={saturdayAssignModal.examDuration}
              onChange={(e) => {
                const raw = e.target.value;
                if (raw === '') {
                  setSaturdayAssignModal(prev => ({ ...prev, examDuration: '' as any }));
                } else {
                  const val = parseInt(raw, 10);
                  setSaturdayAssignModal(prev => ({ ...prev, examDuration: isNaN(val) ? '' as any : Math.max(5, Math.min(300, val)) }));
                }
              }}
              onBlur={() => {
                if (!saturdayAssignModal.examDuration || Number(saturdayAssignModal.examDuration) < 5) {
                  setSaturdayAssignModal(prev => ({ ...prev, examDuration: 60 }));
                }
              }}
            />
          </div>
        </div>

        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', borderTop: '1px solid var(--border-light)', paddingTop: '14px', marginTop: '4px' }}>
          <button className="btn btn-secondary btn-sm" onClick={() => setSaturdayAssignModal(prev => ({ ...prev, show: false }))}>Cancel</button>
          <button className="btn btn-primary btn-sm" onClick={handleSaveSaturdayAssignment}>
            {saturdayAssignModal.assignmentId ? 'Save Changes' : 'Activate Exam'}
          </button>
        </div>

      </div>
    </div>
  );
}

export default SaturdayAssignModal;
