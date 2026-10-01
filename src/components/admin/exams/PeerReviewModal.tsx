'use client';

import React from 'react';

export interface LotteryModalState {
  show: boolean;
  examId: string;
  examName: string;
  loading: boolean;
  statusData: any;
}

interface PeerReviewModalProps {
  lotteryModal: LotteryModalState;
  setLotteryModal: React.Dispatch<React.SetStateAction<LotteryModalState>>;
}

export function PeerReviewModal({ lotteryModal, setLotteryModal }: PeerReviewModalProps) {
  if (!lotteryModal.show) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '500px', width: '90%', padding: '24px', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0 }}>
            📊 Peer Review Status: {lotteryModal.examName}
          </h3>
          <button onClick={() => setLotteryModal(prev => ({ ...prev, show: false }))} style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', fontSize: '16px' }}>✕</button>
        </div>

        {lotteryModal.loading ? (
          <div style={{ padding: '30px', textAlign: 'center' }}>
            <div className="spinner"></div> Fetching pairings...
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', fontSize: '12px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', background: 'var(--bg-soft)', padding: '8px 12px', borderRadius: 'var(--radius-sm)' }}>
              <span>Completed: <strong>{lotteryModal.statusData?.completedCount || 0}</strong></span>
              <span>Pending: <strong>{lotteryModal.statusData?.pendingCount || 0}</strong></span>
            </div>

            <div style={{ maxHeight: '250px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '6px' }}>
              {lotteryModal.statusData?.pendingAssignments?.map((a: any, idx: number) => (
                <div key={`p_${idx}`} style={{ padding: '6px 10px', background: 'rgba(255,152,0,0.1)', color: 'var(--warning)', borderRadius: 'var(--radius-sm)', borderLeft: '3px solid var(--warning)' }}>
                  👤 {a.reviewerName} → 📝 {a.revieweeName} (Pending)
                </div>
              ))}
              {lotteryModal.statusData?.completedAssignments?.map((a: any, idx: number) => (
                <div key={`c_${idx}`} style={{ padding: '6px 10px', background: 'rgba(76,175,80,0.1)', color: 'var(--success)', borderRadius: 'var(--radius-sm)', borderLeft: '3px solid var(--success)' }}>
                  ✅ {a.reviewerName} → 📝 {a.revieweeName} (Completed)
                </div>
              ))}
            </div>
          </div>
        )}

        <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '10px' }}>
          <button className="btn btn-secondary" onClick={() => setLotteryModal(prev => ({ ...prev, show: false }))}>Close</button>
        </div>
      </div>
    </div>
  );
}

export default PeerReviewModal;

