'use client';

import React from 'react';
import { formatDateTimeIST } from '@/lib/dateUtils';
import { sanitizeNoticeHtml } from '@/lib/sanitize';
import { ParentNotice } from './types';
import NoticeOverlayModal from '@/components/notices/NoticeOverlayModal';

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
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold' }}>🔔 Push Notification History / नोटिफिकेशन इतिहास</h4>
              <button className="close-modal" onClick={onCloseNotificationHistory} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>
            
            <div className="modal-body" style={{ padding: '24px', overflowY: 'auto', flex: 1 }}>
              {loadingHistory ? (
                <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
                  <div className="spinner" style={{ margin: '0 auto 10px' }}></div> Loading history... / लोड हो रहा है...
                </div>
              ) : notificationHistory.length === 0 ? (
                <div style={{ textAlign: 'center', padding: '30px 0', color: 'var(--text-muted)', fontSize: '13px' }}>
                  No notification history found. / कोई सूचना इतिहास नहीं मिला।
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
              <button className="btn btn-secondary" onClick={onCloseNotificationHistory}>Close / बंद करें</button>
            </div>
          </div>
        </div>
      )}

      {/* Announcements Modal */}
      {isNoticesModalOpen && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '600px', width: '100%', maxHeight: '80vh', display: 'flex', flexDirection: 'column', padding: '0', overflow: 'hidden' }}>
            <div className="modal-header" style={{ padding: '16px 24px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold' }}>📢 Announcements / सूचनाएं</h4>
              <button className="close-modal" onClick={onCloseNoticesModal} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>
            
            <div className="modal-body" style={{ padding: '24px', overflowY: 'auto', flex: 1 }}>
              {visibleNotices.length === 0 && !showSeenNotices ? (
                <div style={{ textAlign: 'center', padding: '30px 0', color: 'var(--text-muted)' }}>
                  <span style={{ fontSize: '13px' }}>All caught up! ✅ No new announcements / कोई नई सूचना नहीं है।</span>
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
                      Show read announcements / पढ़ी गई सूचनाएं देखें
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
                {showSeenNotices ? 'Show unread only / केवल अपठित दिखाएं' : 'Show read announcements / पढ़ी गई सूचनाएं दिखाएं'}
              </button>
              <button className="btn btn-secondary" onClick={onCloseNoticesModal}>Close / बंद करें</button>
            </div>
          </div>
        </div>
      )}

      {/* Important Notices Fullscreen Overlay */}
      <NoticeOverlayModal
        notice={activeOverlayNotice}
        onDismiss={onDismissOverlayNotice}
        role="parent"
        absenceReason={absenceReason}
        setAbsenceReason={setAbsenceReason}
        absenceRemarks={absenceRemarks}
        setAbsenceRemarks={setAbsenceRemarks}
      />
    </>
  );
});
