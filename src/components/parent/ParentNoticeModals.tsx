'use client';

import React from 'react';
import { formatDateTimeIST } from '@/lib/dateUtils';
import { ParentNotice } from './types';

interface ParentNoticeModalsProps {
  // Push Notification History Modal
  isNotificationHistoryOpen: boolean;
  onCloseNotificationHistory: () => void;
  notificationHistory: any[];
  loadingHistory: boolean;

  // Announcements Modal
  isNoticesModalOpen: boolean;
  onCloseNoticesModal: () => void;
  notices: ParentNotice[];
  visibleNotices: ParentNotice[];
  seenNoticeIds: string[];
  showSeenNotices: boolean;
  onToggleShowSeenNotices: () => void;
  onMarkNoticeAsSeen: (id: string) => void;

  // Fullscreen Important Notice / Overlay Notice
  activeOverlayNotice: ParentNotice | null;
  onDismissOverlayNotice: (noticeId: string, reason?: string, remarks?: string) => void;
  absenceReason: string;
  setAbsenceReason: (reason: string) => void;
  absenceRemarks: string;
  setAbsenceRemarks: (remarks: string) => void;
}

export const ParentNoticeModals = React.memo(function ParentNoticeModals({
  isNotificationHistoryOpen,
  onCloseNotificationHistory,
  notificationHistory,
  loadingHistory,
  isNoticesModalOpen,
  onCloseNoticesModal,
  notices,
  visibleNotices,
  seenNoticeIds,
  showSeenNotices,
  onToggleShowSeenNotices,
  onMarkNoticeAsSeen,
  activeOverlayNotice,
  onDismissOverlayNotice,
  absenceReason,
  setAbsenceReason,
  absenceRemarks,
  setAbsenceRemarks
}: ParentNoticeModalsProps) {
  return (
    <>
      {/* Push Notification History Modal */}
      {isNotificationHistoryOpen && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '600px', width: '100%', maxHeight: '80vh', display: 'flex', flexDirection: 'column', padding: '0', overflow: 'hidden' }}>
            <div className="modal-header" style={{ padding: '16px 24px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold' }}>🔔 Push Notification History</h4>
              <button className="close-modal" onClick={onCloseNotificationHistory} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>
            
            <div className="modal-body" style={{ padding: '24px', overflowY: 'auto', flex: 1 }}>
              {loadingHistory ? (
                <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
                  <div className="spinner" style={{ margin: '0 auto 10px' }}></div> Loading history...
                </div>
              ) : notificationHistory.length === 0 ? (
                <div style={{ textAlign: 'center', padding: '30px 0', color: 'var(--text-muted)', fontSize: '13px' }}>
                  No notification history found.
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  {notificationHistory.map((notif) => (
                    <div key={notif.id} style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '6px' }}>
                        <strong style={{ fontSize: '13px', color: 'var(--text)' }}>{notif.title}</strong>
                        <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>{formatDateTimeIST(notif.sentAt)}</span>
                      </div>
                      <p style={{ margin: 0, fontSize: '12px', color: 'var(--text-muted)', lineHeight: '1.4' }}>{notif.body}</p>
                    </div>
                  ))}
                </div>
              )}
            </div>
            
            <div className="modal-footer" style={{ padding: '12px 24px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end' }}>
              <button className="btn btn-secondary" onClick={onCloseNotificationHistory}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Announcements Modal */}
      {isNoticesModalOpen && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '600px', width: '100%', maxHeight: '80vh', display: 'flex', flexDirection: 'column', padding: '0', overflow: 'hidden' }}>
            <div className="modal-header" style={{ padding: '16px 24px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold' }}>📢 Announcements</h4>
              <button className="close-modal" onClick={onCloseNoticesModal} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>
            
            <div className="modal-body" style={{ padding: '24px', overflowY: 'auto', flex: 1 }}>
              {visibleNotices.length === 0 && !showSeenNotices ? (
                <div style={{ textAlign: 'center', padding: '30px 0', color: 'var(--text-muted)' }}>
                  <span style={{ fontSize: '13px' }}>All caught up! ✅ No new announcements.</span>
                  <div style={{ marginTop: '16px' }}>
                    <button
                      onClick={onToggleShowSeenNotices}
                      style={{
                        background: 'none',
                        border: 'none',
                        color: 'var(--text-accent)',
                        textDecoration: 'underline',
                        cursor: 'pointer',
                        fontSize: '12px',
                        fontWeight: 600
                      }}
                    >
                      Show read announcements
                    </button>
                  </div>
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  {(showSeenNotices ? notices : visibleNotices).map(notice => {
                    const isSeen = seenNoticeIds.includes(notice.id);
                    const nType = notice.type || 'general';
                    const config = 
                      nType === 'schedule' 
                        ? { border: '4px solid var(--accent)', badgeBg: 'var(--accent-soft)', badgeColor: 'var(--accent)', label: '📅 Schedule' }
                        : nType === 'fees'
                        ? { border: '4px solid var(--warning)', badgeBg: 'var(--warning-bg)', badgeColor: 'var(--warning)', label: '💳 Fees' }
                        : { border: '4px solid var(--danger)', badgeBg: 'var(--danger-bg)', badgeColor: 'var(--danger)', label: '📢 Announcement' };

                    return (
                      <div key={notice.id} style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', borderLeft: config.border, opacity: isSeen ? 0.75 : 1, position: 'relative' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '6px', flexWrap: 'wrap', gap: '8px' }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                            <strong style={{ fontSize: '17px', color: 'var(--text)' }}>{notice.title}</strong>
                            <span style={{ fontSize: '10px', fontWeight: 800, background: config.badgeBg, color: config.badgeColor, padding: '2px 8px', borderRadius: '12px' }}>
                              {config.label}
                            </span>
                          </div>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                            <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>
                              {notice.createdAt ? (() => {
                                const d = new Date(notice.createdAt);
                                if (isNaN(d.getTime())) return '';
                                const day = String(d.getDate()).padStart(2, '0');
                                const month = String(d.getMonth() + 1).padStart(2, '0');
                                return `${day}/${month}/${d.getFullYear()}`;
                              })() : ''}
                            </span>
                            {isSeen ? (
                              <span style={{ fontSize: '10px', color: 'var(--success)', fontWeight: 700 }}>
                                ✓ Read
                              </span>
                            ) : (
                              <button 
                                onClick={() => onMarkNoticeAsSeen(notice.id)}
                                style={{
                                  background: 'var(--danger)',
                                  border: '1px solid var(--danger-border)',
                                  borderRadius: 'var(--radius-sm)',
                                  padding: '2px 8px',
                                  fontSize: '10px',
                                  fontWeight: 600,
                                  cursor: 'pointer',
                                  color: 'var(--text-white)'
                                }}
                              >
                                Read
                              </button>
                            )}
                          </div>
                        </div>
                        {nType === 'schedule' && notice.noticeDate && (
                          <div style={{
                            fontSize: '12px',
                            fontWeight: 700,
                            color: 'var(--accent)',
                            background: 'var(--accent-soft)',
                            padding: '6px 10px',
                            borderRadius: '4px',
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '4px',
                            marginBottom: '8px',
                            border: '1px solid var(--accent-ring)'
                          }}>
                            📅 Scheduled Date: {(() => {
                              const d = new Date(notice.noticeDate);
                              if (isNaN(d.getTime())) return notice.noticeDate;
                              const day = String(d.getDate()).padStart(2, '0');
                              const month = String(d.getMonth() + 1).padStart(2, '0');
                              return `${day}/${month}/${d.getFullYear()}`;
                            })()}
                          </div>
                        )}
                        <p style={{ margin: 0, fontSize: '15px', color: 'var(--text-muted)', whiteSpace: 'pre-line', lineHeight: '1.5' }}>
                          {notice.body}
                        </p>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
            
            <div className="modal-footer" style={{ padding: '12px 24px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <button
                onClick={onToggleShowSeenNotices}
                style={{
                  background: 'none',
                  border: 'none',
                  color: 'var(--text-accent)',
                  cursor: 'pointer',
                  fontSize: '11px',
                  fontWeight: 600
                }}
              >
                {showSeenNotices ? 'Show unread only' : 'Show read announcements'}
              </button>
              <button className="btn btn-secondary" onClick={onCloseNoticesModal}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Important Notices Fullscreen Overlay */}
      {activeOverlayNotice && (() => {
        const type = activeOverlayNotice.type || 'general';
        const typeConfig = 
          type === 'schedule' 
            ? { title: '📅 CLASS SCHEDULE UPDATE', color: 'var(--accent)', bg: 'var(--accent-soft)', text: 'var(--accent)', icon: '📅' }
            : type === 'fees'
            ? { title: '💳 FEES REMINDER', color: 'var(--warning)', bg: 'var(--warning-bg)', text: 'var(--warning)', icon: '💳' }
            : type === 'exam_absent'
            ? { title: '🚨 EXAM ABSENCE ALERT', color: 'var(--danger)', bg: 'var(--danger-bg)', text: 'var(--danger-muted)', icon: '🚨' }
            : type === 'exam_excellent'
            ? { title: '🌟 EXCELLENT EXAM RESULT', color: 'var(--success)', bg: 'var(--success-bg)', text: 'var(--success)', icon: '🌟' }
            : type === 'exam_good'
            ? { title: '👏 EXAM RESULT ANNOUNCEMENT', color: 'var(--accent)', bg: 'var(--accent-soft)', text: 'var(--accent)', icon: '👏' }
            : type === 'exam_needs_improvement'
            ? { title: '⚠️ EXAM RESULT - ATTENTION', color: 'var(--warning)', bg: 'var(--warning-bg)', text: 'var(--warning)', icon: '⚠️' }
            : { title: '📢 IMPORTANT ANNOUNCEMENT', color: 'var(--danger)', bg: 'var(--danger-bg)', text: 'var(--danger-muted)', icon: '📢' };
        
        const isAbsentNotice = type === 'exam_absent';

        return (
          <div style={{
            position: 'fixed',
            inset: 0,
            background: 'rgba(0, 0, 0, 0.5)',
            backdropFilter: 'blur(8px)',
            WebkitBackdropFilter: 'blur(8px)',
            zIndex: 999999,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '20px'
          }}>
            <div className="card" style={{
              background: 'var(--surface-popover)',
              border: `2px solid ${typeConfig.color}`,
              borderRadius: 'var(--radius-lg)',
              padding: '28px',
              maxWidth: '520px',
              width: '100%',
              maxHeight: '95%',
              display: 'flex',
              flexDirection: 'column',
              gap: '16px',
              boxShadow: 'var(--shadow-lg)',
              overflow: 'hidden'
            }}>
              <div style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '16px' }}>
                <span style={{ fontSize: '48px', margin: '4px 0 12px 0', display: 'block', lineHeight: 1 }}>
                  {typeConfig.icon}
                </span>
                <span style={{
                  fontSize: '11px',
                  background: typeConfig.bg,
                  color: typeConfig.text,
                  padding: '4px 10px',
                  borderRadius: '20px',
                  fontWeight: 800,
                  letterSpacing: '0.5px',
                  display: 'inline-block',
                  marginBottom: '12px'
                }}>
                  {typeConfig.title.replace(/^[^\s]+\s*/, '')}
                </span>
                <h2 style={{ fontSize: '1.75rem', fontWeight: 800, color: 'var(--text)', margin: 0, lineHeight: '1.3' }}>
                  {activeOverlayNotice.title}
                </h2>
              </div>
              
              <div style={{
                flex: 1,
                overflowY: 'auto',
                fontSize: '17px',
                lineHeight: '1.6',
                color: 'var(--text)',
                padding: '4px 8px 4px 0',
                whiteSpace: 'pre-line',
                wordBreak: 'break-word'
              }}>
                {type === 'schedule' && activeOverlayNotice.noticeDate && (
                  <div style={{
                    fontSize: '17px',
                    fontWeight: 700,
                    color: 'var(--accent)',
                    background: 'var(--accent-soft)',
                    padding: '8px 12px',
                    borderRadius: '6px',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    marginBottom: '14px',
                    border: '1px solid var(--accent-ring)'
                  }}>
                    <span>{(() => {
                      const d = new Date(activeOverlayNotice.noticeDate);
                      if (isNaN(d.getTime())) return activeOverlayNotice.noticeDate;
                      const day = String(d.getDate()).padStart(2, '0');
                      const month = String(d.getMonth() + 1).padStart(2, '0');
                      return `${day}/${month}/${d.getFullYear()}`;
                    })()}</span>
                  </div>
                )}
                <div 
                  style={{ lineHeight: '1.25', margin: '4px 0' }}
                  dangerouslySetInnerHTML={{ __html: (activeOverlayNotice.body || '').replace(/(<\/div>|<\/p>|<\/li>)\s*\r?\n/gi, '$1').replace(/\r?\n\s*(<div[^>]*>|<p[^>]*>|<ul[^>]*>|<ol[^>]*>|<li[^>]*>)/gi, '$1').replace(/\r?\n/g, '<br/>') }}
                />

                {/* Interactive Absence Reason Form for Parent with Firm Hindi Advisory */}
                {isAbsentNotice && (
                  <div style={{
                    marginTop: '16px',
                    padding: '14px',
                    background: 'rgba(239, 68, 68, 0.08)',
                    borderRadius: '8px',
                    border: '1.5px solid rgba(239, 68, 68, 0.35)',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '12px'
                  }}>
                    {/* Polite & Firm Parental Advisory in Hindi */}
                    <div style={{
                      padding: '12px 14px',
                      background: 'var(--danger-bg)',
                      borderRadius: '8px',
                      borderLeft: '4px solid var(--danger)',
                      color: 'var(--text)',
                      fontSize: '13px',
                      lineHeight: '1.6'
                    }}>
                      <div style={{ fontWeight: 800, color: 'var(--danger)', marginBottom: '6px', fontSize: '13.5px' }}>
                        ⚠️ अभिभावक परामर्श (Parental Advisory):
                      </div>
                      <div>
                        आदरणीय अभिभावक, कृपया ध्यान दें कि नियमित अभ्यास और परीक्षाओं में उपस्थिति ही विद्यार्थी की मजबूत तैयारी सुनिश्चित करती है। कृपया परीक्षा में अनुपस्थिति का कारण दर्ज करें।
                      </div>
                    </div>

                    <div style={{ fontWeight: 800, fontSize: '13px', color: 'var(--danger)' }}>
                      📌 अनुपस्थिति का कारण चुनें (Select reason for absence):
                    </div>
                    {[
                      '⏰ Got up Late / देर से सोकर उठे',
                      '🩺 Health / Medical Issue / स्वास्थ्य समस्या',
                      '🚨 Family Emergency / पारिवारिक आपातकाल',
                      '📝 Other Reason / अन्य कारण'
                    ].map((reasonOption) => (
                      <label key={reasonOption} style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', cursor: 'pointer', fontWeight: 600 }}>
                        <input 
                          type="radio" 
                          name="absenceReason" 
                          value={reasonOption} 
                          checked={absenceReason === reasonOption} 
                          onChange={() => setAbsenceReason(reasonOption)} 
                        />
                        {reasonOption}
                      </label>
                    ))}
                    {(absenceReason === '📝 Other Reason / अन्य कारण' || absenceReason === '📝 Other Reason' || absenceReason === 'other') && (
                      <input 
                        type="text" 
                        placeholder="कृपया विवरण दर्ज करें (Please specify details)..." 
                        value={absenceRemarks} 
                        onChange={(e) => setAbsenceRemarks(e.target.value)} 
                        style={{
                          width: '100%',
                          padding: '8px 10px',
                          borderRadius: '6px',
                          border: '1px solid var(--border-light)',
                          background: 'var(--surface)',
                          color: 'var(--text)',
                          fontSize: '12px',
                          marginTop: '4px'
                        }} 
                      />
                    )}
                  </div>
                )}
              </div>

              <div style={{ borderTop: '1px solid var(--border-light)', paddingTop: '16px', marginTop: '4px' }}>
                <button 
                  className="btn btn-primary" 
                  onClick={() => {
                    if (isAbsentNotice && !absenceReason) {
                      alert('Please select a reason for absence before submitting.');
                      return;
                    }
                    onDismissOverlayNotice(activeOverlayNotice.id, absenceReason, absenceRemarks);
                  }}
                  style={{
                    width: '100%',
                    padding: '12px',
                    borderRadius: 'var(--radius-md)',
                    fontWeight: 'bold',
                    fontSize: '14px',
                    background: typeConfig.color,
                    color: 'var(--text-white)',
                    border: 'none',
                    cursor: 'pointer'
                  }}
                >
                  {isAbsentNotice ? 'कारण सबमिट करें और आगे बढ़ें' : 'I Understand & Dismiss'}
                </button>
              </div>
            </div>
          </div>
        );
      })()}
    </>
  );
});
