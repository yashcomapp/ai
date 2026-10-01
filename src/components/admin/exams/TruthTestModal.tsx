'use client';

import React, { useState } from 'react';

export interface TruthTestModalState {
  show: boolean;
  examId: string;
  examName: string;
  loading: boolean;
  data: any;
}

interface TruthTestModalProps {
  truthTestModal: TruthTestModalState;
  setTruthTestModal: React.Dispatch<React.SetStateAction<TruthTestModalState>>;
}

export function TruthTestModal({ truthTestModal, setTruthTestModal }: TruthTestModalProps) {
  const [truthSearchText, setTruthSearchText] = useState('');

  if (!truthTestModal.show) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
      <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '900px', width: '100%', maxHeight: '85vh', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)', overflow: 'hidden' }}>
        {/* Header */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', padding: '16px 24px' }}>
          <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
            ⚖️ Truth Test Report: {truthTestModal.examName}
          </h3>
          <button onClick={() => setTruthTestModal(prev => ({ ...prev, show: false }))} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
        </div>

        {truthTestModal.loading ? (
          <div style={{ padding: '40px', textAlign: 'center', flex: 1 }}>
            <div className="spinner" style={{ margin: '0 auto 10px' }}></div> Analyzing evaluations...
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '15px', padding: '0 24px 24px', overflowY: 'auto', flex: 1 }}>
            
            {/* Metrics Grid */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '12px' }}>
              <div className="card glass" style={{ padding: '12px 16px', display: 'flex', flexDirection: 'column', gap: '4px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>TRUTH ALIGNMENT RATE</span>
                <span style={{ fontSize: '20px', fontWeight: 800, color: truthTestModal.data?.metrics?.alignmentRate >= 75 ? 'var(--success)' : (truthTestModal.data?.metrics?.alignmentRate >= 50 ? 'var(--warning)' : 'var(--danger)') }}>
                  {truthTestModal.data?.metrics?.alignmentRate || 0}%
                </span>
              </div>
              <div className="card glass" style={{ padding: '12px 16px', display: 'flex', flexDirection: 'column', gap: '4px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>AVG PARENT OVERESTIMATE</span>
                <span style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text)' }}>
                  +{truthTestModal.data?.metrics?.avgParentOverestimate || 0} pts
                </span>
              </div>
              <div className="card glass" style={{ padding: '12px 16px', display: 'flex', flexDirection: 'column', gap: '4px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>ANALYZED QUESTION PAIRS</span>
                <span style={{ fontSize: '20px', fontWeight: 800, color: 'var(--accent)' }}>
                  {truthTestModal.data?.metrics?.totalQuestionsAnalyzed || 0}
                </span>
              </div>
              <div className="card glass" style={{ padding: '12px 16px', display: 'flex', flexDirection: 'column', gap: '4px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>PARENT HIGHER FLAGS</span>
                <span style={{ fontSize: '20px', fontWeight: 800, color: truthTestModal.data?.metrics?.parentHigherCount > 0 ? 'var(--danger)' : 'var(--success)' }}>
                  {truthTestModal.data?.metrics?.parentHigherCount || 0}
                </span>
              </div>
            </div>

            {/* Search Bar */}
            <div style={{ display: 'flex', gap: '10px' }}>
              <input
                type="text"
                className="form-control"
                placeholder="🔍 Search by student name or question content..."
                value={truthSearchText}
                onChange={(e) => setTruthSearchText(e.target.value)}
                style={{ flex: 1, padding: '8px 12px', fontSize: '12px', background: 'var(--bg-soft)', color: 'var(--text)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)' }}
              />
            </div>

            {/* Table */}
            <div className="table-responsive" style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-md)', maxHeight: '350px', overflowY: 'auto' }}>
              <table className="table" style={{ width: '100%', fontSize: '12px', borderCollapse: 'collapse', textAlign: 'left' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                    <th style={{ padding: '10px 14px', fontWeight: 700 }}>Student Name</th>
                    <th style={{ padding: '10px 14px', fontWeight: 700 }}>Question Prompt</th>
                    <th style={{ padding: '10px 14px', fontWeight: 700, textAlign: 'center' }}>Home (Parent)</th>
                    <th style={{ padding: '10px 14px', fontWeight: 700, textAlign: 'center' }}>Classroom (Peer)</th>
                    <th style={{ padding: '10px 14px', fontWeight: 700, textAlign: 'center' }}>Variance (Δ)</th>
                    <th style={{ padding: '10px 14px', fontWeight: 700, textAlign: 'center' }}>Truth Status</th>
                  </tr>
                </thead>
                <tbody>
                  {(() => {
                    const filteredItems = (truthTestModal.data?.items || []).filter((item: any) => {
                      if (!truthSearchText) return true;
                      const s = truthSearchText.toLowerCase();
                      return (
                        item.studentName.toLowerCase().includes(s) ||
                        item.questionText.toLowerCase().includes(s)
                      );
                    });

                    if (filteredItems.length === 0) {
                      return (
                        <tr>
                          <td colSpan={6} style={{ padding: '24px', textAlign: 'center', color: 'var(--text-faint)' }}>
                            📭 No matching question pairs found for this search.
                          </td>
                        </tr>
                      );
                    }

                    return filteredItems.map((item: any) => (
                      <tr key={item.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '10px 14px', fontWeight: 600 }}>{item.studentName}</td>
                        <td style={{ padding: '10px 14px', color: 'var(--text-muted)', maxWidth: '280px', wordBreak: 'break-word', whiteSpace: 'pre-line' }}>{item.questionText}</td>
                        <td style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 600 }}>{item.parentMarks} / {item.maxMarks}</td>
                        <td style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 600 }}>{item.peerMarks} / {item.maxMarks}</td>
                        <td style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 700, color: item.variance > 0.5 ? 'var(--danger)' : (item.variance < -0.5 ? 'var(--accent)' : 'var(--success)') }}>
                          {item.variance > 0 ? `+${item.variance}` : item.variance}
                        </td>
                        <td style={{ padding: '10px 14px', textAlign: 'center' }}>
                          {item.status === 'aligned' && (
                            <span style={{ padding: '3px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700, background: 'rgba(16, 185, 129, 0.15)', color: 'var(--success)', border: '1px solid rgba(16, 185, 129, 0.3)' }}>
                              Aligned
                            </span>
                          )}
                          {item.status === 'parent_higher' && (
                            <span style={{ padding: '3px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700, background: 'rgba(239, 68, 68, 0.15)', color: 'var(--danger)', border: '1px solid rgba(239, 68, 68, 0.3)' }}>
                              Parent Higher ⚠️
                            </span>
                          )}
                          {item.status === 'peer_higher' && (
                            <span style={{ padding: '3px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700, background: 'rgba(59, 130, 246, 0.15)', color: 'var(--accent)', border: '1px solid rgba(59, 130, 246, 0.3)' }}>
                              Classroom Higher
                            </span>
                          )}
                        </td>
                      </tr>
                    ));
                  })()}
                </tbody>
              </table>
            </div>

          </div>
        )}

        {/* Footer */}
        <div style={{ display: 'flex', justifyContent: 'flex-end', padding: '16px 24px', borderTop: '1px solid var(--border-light)', background: 'var(--bg-soft)' }}>
          <button className="btn btn-secondary" onClick={() => setTruthTestModal(prev => ({ ...prev, show: false }))}>Close</button>
        </div>
      </div>
    </div>
  );
}

export default TruthTestModal;

