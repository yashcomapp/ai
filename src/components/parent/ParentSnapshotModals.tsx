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
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '520px', width: '100%', overflow: 'hidden' }}>
            <div className="modal-header" style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '14.5px', fontWeight: 'bold' }}>
                {activeModal === 'time' && '⏱️ Screen Time Analysis / स्क्रीन समय विश्लेषण'}
                {activeModal === 'streak' && '🔥 Consistent Study Streak / निरंतर अध्ययन स्ट्रीक'}
                {activeModal === 'score' && '📊 Overall Exam Performance / कुल परीक्षा प्रदर्शन'}
                {activeModal === 'integrity' && '🛡️ Proctor & Integrity / सत्यनिष्ठा व निगरानी'}
                {activeModal === 'activity' && (selectedActivity?.type === 'exam' ? '📝 Exam Details / परीक्षा विवरण' : '🏋️ Practice Details / अभ्यास विवरण')}
              </h4>
              <button onClick={onCloseModal} style={{ background: 'transparent', border: 'none', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>
            
            <div className="modal-body" style={{ padding: '20px', fontSize: '13px' }}>
              {activeModal === 'time' && snapshot && (
                <div>
                  <div style={{ background: 'var(--surface-2)', borderLeft: '4px solid var(--accent)', padding: '10px 14px', borderRadius: '4px', fontSize: '11.5px', color: 'var(--text)', marginBottom: '16px', lineHeight: 1.5 }}>
                    <div>💡 <strong>Smart Active Time Monitoring:</strong> Only active, visible screen time is counted. Idle time (&gt;60s inactivity), tab switches, and minimized windows are automatically excluded.</div>
                    <div style={{ marginTop: '4px', color: 'var(--text-muted)' }}>💡 <strong>सक्रिय स्क्रीन समय निगरानी:</strong> केवल वास्तविक पढ़ाई का समय गिना जाता है। 60 सेकंड से अधिक निष्क्रियता, टैब स्विच व स्क्रीन मिनिमाइज समय को हटा दिया जाता है।</div>
                  </div>

                  <h5 style={{ fontSize: '13px', fontWeight: 'bold', margin: '0 0 10px 0', color: 'var(--text)' }}>
                    ⏱️ Today&apos;s Active Time / आज का सक्रिय समय: <span style={{ color: 'var(--accent)' }}>{fmtTime(snapshot.todaySeconds)}</span>
                  </h5>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', marginBottom: '20px' }}>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>📝 EXAMS / परीक्षा</span>
                      <strong style={{ fontSize: '14px', color: 'var(--accent)' }}>{fmtTime((snapshot as any).todayExamSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>🏋️ PRACTICE / अभ्यास</span>
                      <strong style={{ fontSize: '14px', color: 'var(--success)' }}>{fmtTime((snapshot as any).todayPracticeSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>📊 REVIEW / समीक्षा</span>
                      <strong style={{ fontSize: '14px', color: 'var(--warning)' }}>{fmtTime((snapshot as any).todayReviewSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>🖥️ GENERAL / सामान्य</span>
                      <strong style={{ fontSize: '14px', color: 'var(--text)' }}>{fmtTime((snapshot as any).todayGeneralSeconds || 0)}</strong>
                    </div>
                  </div>

                  <h5 style={{ fontSize: '13px', fontWeight: 'bold', margin: '0 0 10px 0', color: 'var(--text)' }}>
                    📅 This Week Active Time (7 Days) / इस सप्ताह (7 दिन): <span style={{ color: 'var(--accent)' }}>{fmtTime(snapshot.weekSeconds)}</span>
                  </h5>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>📝 EXAMS / परीक्षा</span>
                      <strong style={{ fontSize: '14px', color: 'var(--accent)' }}>{fmtTime((snapshot as any).weekExamSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>🏋️ PRACTICE / अभ्यास</span>
                      <strong style={{ fontSize: '14px', color: 'var(--success)' }}>{fmtTime((snapshot as any).weekPracticeSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>📊 REVIEW / समीक्षा</span>
                      <strong style={{ fontSize: '14px', color: 'var(--warning)' }}>{fmtTime((snapshot as any).weekReviewSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>🖥️ GENERAL / सामान्य</span>
                      <strong style={{ fontSize: '14px', color: 'var(--text)' }}>{fmtTime((snapshot as any).weekGeneralSeconds || 0)}</strong>
                    </div>
                  </div>
                </div>
              )}

              {activeModal === 'streak' && snapshot && (
                <div>
                  <p style={{ color: 'var(--text-muted)', marginBottom: '12px' }}>Consecutive days of online practice / ऑनलाइन अभ्यास के लगातार दिन:</p>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <span style={{ fontSize: '2rem' }}>🔥</span>
                    <span style={{ fontSize: '1.6rem', fontWeight: 800 }}>{snapshot.streakDays} Days In a Row! / लगातार {snapshot.streakDays} दिन!</span>
                  </div>
                  <p style={{ marginTop: '12px', fontSize: '12px', color: 'var(--text-faint)' }}>Help your child maintain this streak by practicing every single day! / हर दिन अभ्यास कराकर बच्चे की यह निरंतरता बनाए रखने में मदद करें।</p>
                </div>
              )}

              {activeModal === 'score' && snapshot && (
                <div>
                  <p style={{ color: 'var(--text-muted)', marginBottom: '12px' }}>Aggregated results of all examinations and exercises / सभी परीक्षाओं और अभ्यासों का कुल परिणाम:</p>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                    <div style={{ textAlign: 'center', padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)' }}>
                      <div style={{ fontSize: '20px', fontWeight: 'bold', color: 'var(--accent)' }}>{snapshot.avgScore}%</div>
                      <div style={{ fontSize: '11px', color: 'var(--text)' }}>Average Grade</div>
                      <div style={{ fontSize: '10px', color: 'var(--text-muted)' }}>औसत ग्रेड</div>
                    </div>
                    <div style={{ textAlign: 'center', padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)' }}>
                      <div style={{ fontSize: '20px', fontWeight: 'bold', color: 'var(--success)' }}>{snapshot.totalSessions}</div>
                      <div style={{ fontSize: '11px', color: 'var(--text)' }}>Sessions Completed</div>
                      <div style={{ fontSize: '10px', color: 'var(--text-muted)' }}>पूर्ण सत्र</div>
                    </div>
                  </div>
                </div>
              )}

              {activeModal === 'integrity' && snapshot && (
                <div>
                  <p style={{ color: 'var(--text-muted)', marginBottom: '12px' }}>Calculated based on exam room proctor logs (tab switches, webcam detections) / परीक्षा कक्ष निगरानी (टैब स्विच, कैमरा जांच) के आधार पर:</p>
                  <div style={{ padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                    <span>Integrity Score / सत्यनिष्ठा स्कोर:</span>
                    <span style={{ fontWeight: 'bold', color: 'var(--accent)' }}>{snapshot.integrityScore}%</span>
                  </div>
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '12px', lineHeight: 1.5 }}>
                    {snapshot.integrityScore >= 90 ? (
                      <span style={{ color: 'var(--success)' }}>✅ Studied with excellent honesty. No severe anomalies reported. / पूर्ण ईमानदारी से अध्ययन किया। कोई असामान्यता नहीं मिली।</span>
                    ) : snapshot.integrityScore >= 75 ? (
                      <span style={{ color: 'var(--warning)' }}>⚠️ Minor issues found (e.g. accidental tab changes). Warn child to pay attention. / कुछ छोटी त्रुटियां मिलीं (जैसे गलती से टैब बदलना)। बच्चे को ध्यान देने कहें।</span>
                    ) : (
                      <span style={{ color: 'var(--danger)' }}>🚨 Multi-violations logged. Please discuss code rules and guidelines with the child. / कई नियम उल्लंघन दर्ज हुए। कृपया बच्चे से नियमों का पालन करने को कहें।</span>
                    )}
                  </div>
                </div>
              )}

              {activeModal === 'activity' && selectedActivity && (
                <div>
                  <div style={{ padding: '16px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', lineHeight: 1.6, whiteSpace: 'pre-line' }}>
                    {selectedActivity.type === 'exam' ? (
                      `📝 ${childInfo?.name || 'Child'}'s Exam / परीक्षा
                      ─────────────────────
                      📌 Name / नाम: ${selectedActivity.name}
                      📅 Date / तारीख: ${formatDateIST(selectedActivity.date)}
                      📊 Score / स्कोर: ${selectedActivity.score}%
                      🏁 Status / स्थिति: ${selectedActivity.status}
                      ─────────────────────`
                    ) : (
                      `🏋️ ${childInfo?.name || 'Child'}'s Practice / अभ्यास
                      ─────────────────────
                      📌 Name / नाम: ${selectedActivity.name}
                      📅 Date / तारीख: ${formatDateIST(selectedActivity.date)}
                      📊 Score / स्कोर: ${selectedActivity.score}%
                      ─────────────────────`
                    )}
                  </div>
                </div>
              )}
            </div>
            
            <div className="modal-footer" style={{ padding: '12px 16px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end' }}>
              <button className="btn btn-secondary" onClick={onCloseModal}>Close / बंद करें</button>
            </div>
          </div>
        </div>
      )}

      {/* Themed Custom Alert Modal */}
      {showAlert && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 30000 }}>
          <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '440px', width: '90%', display: 'flex', flexDirection: 'column', gap: '16px', boxShadow: '0 10px 25px rgba(0,0,0,0.2)' }}>
            <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold', color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '8px' }}>
              🔔 {alertTitle || 'Notice / सूचना'}
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
                OK / ठीक है
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
            <h2 style={{ fontSize: '1.35rem', fontWeight: 800, color: 'var(--danger)', margin: '0 0 10px 0' }}>
              Fee Installment Overdue<br />
              <span style={{ fontSize: '1rem', fontWeight: 700 }}>किश्त की अंतिम तारीख निकल चुकी है</span>
            </h2>
            <p style={{ fontSize: '13px', color: 'var(--text)', lineHeight: '1.6', margin: '0 0 20px 0' }}>
              Your child&apos;s account has an outstanding overdue balance of <strong>₹{outstandingAmount || 0}</strong>. Please check the dues schedule and complete payment.<br />
              <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>आपके बच्चे के खाते में <strong>₹{outstandingAmount || 0}</strong> की बकाया फीस देय है। कृपया फीस विवरण देखकर भुगतान पूरा करें।</span>
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
                View Fees &amp; Invoices / फीस और रसीद देखें
              </button>
              <button 
                className="btn btn-secondary" 
                onClick={onDismissOverdue}
                style={{ width: '100%' }}
              >
                Dismiss / बंद करें
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
});
