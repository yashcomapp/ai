'use client';

import React from 'react';
import { useRouter } from 'next/navigation';
import { formatDateIST, formatDurationHM } from '@/lib/dateUtils';
import { ParentDashboardData, ActivityItem } from './types';

interface ParentSnapshotModalsProps {
  activeModal: string | null;
  onCloseModal: () => void;
  snapshot?: ParentDashboardData['snapshot'];
  childInfo?: ParentDashboardData['childInfo'];
  selectedActivity: ActivityItem | null;
  showAlert: boolean;
  alertTitle: string;
  alertMsg: string;
  onCloseAlert: () => void;
  hasOverdueInstallment?: boolean;
  outstandingAmount?: number;
  dismissedOverdue: boolean;
  onDismissOverdue: () => void;
  selectedChildCode: string;
}

export const ParentSnapshotModals = React.memo(function ParentSnapshotModals({
  activeModal,
  onCloseModal,
  snapshot,
  childInfo,
  selectedActivity,
  showAlert,
  alertTitle,
  alertMsg,
  onCloseAlert,
  hasOverdueInstallment,
  outstandingAmount,
  dismissedOverdue,
  onDismissOverdue,
  selectedChildCode
}: ParentSnapshotModalsProps) {
  const router = useRouter();
  const fmtTime = formatDurationHM;

  const isSnapshotModal = activeModal === 'time' || activeModal === 'streak' || activeModal === 'score' || activeModal === 'integrity' || (activeModal === 'activity' && selectedActivity);

  return (
    <>
      {/* Snapshot Details Modal */}
      {isSnapshotModal && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '500px', width: '100%', overflow: 'hidden' }}>
            <div className="modal-header" style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold' }}>
                {activeModal === 'time' && '⏱️ Screen Time Analysis'}
                {activeModal === 'streak' && '🔥 Consistent Study Streak'}
                {activeModal === 'score' && '📊 Overall Exam Performance'}
                {activeModal === 'integrity' && '🛡️ Proctor & Integrity Diagnostics'}
                {activeModal === 'activity' && (selectedActivity?.type === 'exam' ? '📝 Exam Details' : '🏋️ Practice Details')}
              </h4>
              <button onClick={onCloseModal} style={{ background: 'transparent', border: 'none', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>
            
            <div className="modal-body" style={{ padding: '20px', fontSize: '13px' }}>
              {activeModal === 'time' && snapshot && (
                <div>
                  <div style={{ background: 'var(--surface-2)', borderLeft: '4px solid var(--accent)', padding: '10px 14px', borderRadius: '4px', fontSize: '11.5px', color: 'var(--text)', marginBottom: '16px', lineHeight: 1.5 }}>
                    💡 <strong>Smart Active Time Monitoring:</strong> Only active, visible screen time is counted. Idle time (&gt;60s inactivity), tab switches, and minimized windows are automatically excluded.
                  </div>

                  <h5 style={{ fontSize: '13px', fontWeight: 'bold', margin: '0 0 10px 0', color: 'var(--text)' }}>
                    ⏱️ Today&apos;s Active Time: <span style={{ color: 'var(--accent)' }}>{fmtTime(snapshot.todaySeconds)}</span>
                  </h5>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', marginBottom: '20px' }}>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>📝 EXAMS TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--accent)' }}>{fmtTime((snapshot as any).todayExamSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>🏋️ PRACTICE TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--success)' }}>{fmtTime((snapshot as any).todayPracticeSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>📊 REVIEW TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--warning)' }}>{fmtTime((snapshot as any).todayReviewSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>🖥️ OS & GENERAL TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--text)' }}>{fmtTime((snapshot as any).todayGeneralSeconds || 0)}</strong>
                    </div>
                  </div>

                  <h5 style={{ fontSize: '13px', fontWeight: 'bold', margin: '0 0 10px 0', color: 'var(--text)' }}>
                    📅 This Week Active Time (7 Days): <span style={{ color: 'var(--accent)' }}>{fmtTime(snapshot.weekSeconds)}</span>
                  </h5>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>📝 EXAMS TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--accent)' }}>{fmtTime((snapshot as any).weekExamSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>🏋️ PRACTICE TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--success)' }}>{fmtTime((snapshot as any).weekPracticeSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>📊 REVIEW TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--warning)' }}>{fmtTime((snapshot as any).weekReviewSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>🖥️ OS & GENERAL TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--text)' }}>{fmtTime((snapshot as any).weekGeneralSeconds || 0)}</strong>
                    </div>
                  </div>
                </div>
              )}

              {activeModal === 'streak' && snapshot && (
                <div>
                  <p style={{ color: 'var(--text-muted)', marginBottom: '12px' }}>Consecutive days of online practice:</p>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <span style={{ fontSize: '2rem' }}>🔥</span>
                    <span style={{ fontSize: '1.8rem', fontWeight: 800 }}>{snapshot.streakDays} Days In a Row!</span>
                  </div>
                  <p style={{ marginTop: '12px', fontSize: '12px', color: 'var(--text-faint)' }}>Help your child maintain this streak by practicing every single day!</p>
                </div>
              )}

              {activeModal === 'score' && snapshot && (
                <div>
                  <p style={{ color: 'var(--text-muted)', marginBottom: '12px' }}>Aggregated results of all examinations and exercises:</p>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                    <div style={{ textAlign: 'center', padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)' }}>
                      <div style={{ fontSize: '20px', fontWeight: 'bold', color: 'var(--accent)' }}>{snapshot.avgScore}%</div>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Average Grade</div>
                    </div>
                    <div style={{ textAlign: 'center', padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)' }}>
                      <div style={{ fontSize: '20px', fontWeight: 'bold', color: 'var(--success)' }}>{snapshot.totalSessions}</div>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Sessions Completed</div>
                    </div>
                  </div>
                </div>
              )}

              {activeModal === 'integrity' && snapshot && (
                <div>
                  <p style={{ color: 'var(--text-muted)', marginBottom: '12px' }}>Calculated based on exam room proctor logs (tab switches, webcam detections):</p>
                  <div style={{ padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                    <span>Integrity Index Score:</span>
                    <span style={{ fontWeight: 'bold', color: 'var(--accent)' }}>{snapshot.integrityScore}%</span>
                  </div>
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '12px' }}>
                    {snapshot.integrityScore >= 90 ? (
                      <span style={{ color: 'var(--success)' }}>✅ Studied with excellent honesty. No severe anomalies reported.</span>
                    ) : snapshot.integrityScore >= 75 ? (
                      <span style={{ color: 'var(--warning)' }}>⚠️ Minor issues found (e.g. accidental tab changes). Warn child to pay attention.</span>
                    ) : (
                      <span style={{ color: 'var(--danger)' }}>🚨 Multi-violations logged. Please discuss code rules and guidelines with the child.</span>
                    )}
                  </div>
                </div>
              )}

              {activeModal === 'activity' && selectedActivity && (
                <div>
                  <div style={{ padding: '16px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', lineHeight: 1.6, whiteSpace: 'pre-line' }}>
                    {selectedActivity.type === 'exam' ? (
                      `📝 ${childInfo?.name || 'Child'}'s Exam
                      ─────────────────────
                      📌 Name: ${selectedActivity.name}
                      📅 Date: ${formatDateIST(selectedActivity.date)}
                      📊 Score: ${selectedActivity.score}%
                      🏁 Status: ${selectedActivity.status}
                      ─────────────────────`
                    ) : (
                      `🏋️ ${childInfo?.name || 'Child'}'s Practice
                      ─────────────────────
                      📌 Name: ${selectedActivity.name}
                      📅 Date: ${formatDateIST(selectedActivity.date)}
                      📊 Score: ${selectedActivity.score}%
                      ─────────────────────`
                    )}
                  </div>
                </div>
              )}
            </div>
            
            <div className="modal-footer" style={{ padding: '12px 16px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end' }}>
              <button className="btn btn-secondary" onClick={onCloseModal}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Themed Custom Alert Modal */}
      {showAlert && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 30000 }}>
          <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '440px', width: '90%', display: 'flex', flexDirection: 'column', gap: '16px', boxShadow: '0 10px 25px rgba(0,0,0,0.2)' }}>
            <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 'bold', color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '8px' }}>
              🔔 {alertTitle || 'Notice'}
            </h3>
            <p style={{ margin: 0, fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.5' }}>
              {alertMsg}
            </p>
            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '4px' }}>
              <button 
                type="button" 
                className="btn btn-primary" 
                onClick={onCloseAlert}
              >
                OK
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Dismissible Overdue Fees Overlay */}
      {hasOverdueInstallment && !dismissedOverdue && (
        <div style={{
          position: 'fixed',
          inset: 0,
          background: 'rgba(0, 0, 0, 0.45)',
          backdropFilter: 'blur(8px)',
          WebkitBackdropFilter: 'blur(8px)',
          zIndex: 99999,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '20px'
        }}>
          <div className="card" style={{
            background: 'var(--surface-popover)',
            border: '1px solid var(--border-popover)',
            borderRadius: 'var(--radius-lg)',
            padding: '28px',
            maxWidth: '500px',
            width: '100%',
            textAlign: 'center',
            boxShadow: 'var(--shadow-lg)'
          }}>
            <span style={{ fontSize: '3rem', display: 'block', marginBottom: '16px' }}>💳</span>
            <h2 style={{ fontSize: '1.45rem', fontWeight: 800, color: 'var(--danger)', margin: '0 0 10px 0' }}>
              Fee Installment Overdue
            </h2>
            <p style={{ fontSize: '13px', color: 'var(--text)', lineHeight: '1.6', margin: '0 0 20px 0' }}>
              Your child&apos;s account has an outstanding overdue balance of <strong>₹{outstandingAmount || 0}</strong>. Please check the dues schedule and complete payment.
            </p>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <button 
                className="btn btn-primary" 
                onClick={() => {
                  router.push(`/parent/fees?studentCode=${selectedChildCode}`);
                  onDismissOverdue();
                }}
                style={{ width: '100%' }}
              >
                View Fees & Invoices
              </button>
              <button 
                className="btn btn-secondary" 
                onClick={onDismissOverdue}
                style={{ width: '100%' }}
              >
                Dismiss
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
});
