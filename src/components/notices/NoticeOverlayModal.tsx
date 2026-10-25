'use client';

import React from 'react';
import { sanitizeNoticeHtml } from '@/lib/sanitize';

export interface NoticeOverlayData {
  id: string;
  title: string;
  body: string;
  type?: string;
  noticeDate?: string | null;
  [key: string]: any;
}

export interface NoticeOverlayModalProps {
  notice: NoticeOverlayData | null;
  onDismiss: (noticeId: string, reason?: string, remarks?: string) => void;
  role?: 'student' | 'parent';
  absenceReason?: string;
  setAbsenceReason?: (reason: string) => void;
  absenceRemarks?: string;
  setAbsenceRemarks?: (remarks: string) => void;
}

export default function NoticeOverlayModal({
  notice,
  onDismiss,
  role = 'student',
  absenceReason = '',
  setAbsenceReason,
  absenceRemarks = '',
  setAbsenceRemarks
}: NoticeOverlayModalProps) {
  if (!notice) return null;

  const type = notice.type || 'general';
  const typeConfig = 
    type === 'schedule' 
      ? { title: '📅 CLASS SCHEDULE UPDATE', color: 'var(--accent)', bg: 'var(--accent-soft)', text: 'var(--accent)', icon: '📅' }
      : type === 'fees'
      ? { title: '💰 FEES REMINDER', color: 'var(--warning)', bg: 'var(--warning-bg)', text: 'var(--warning)', icon: '💰' }
      : type === 'exam_absent'
      ? { title: '🚨 EXAM ABSENCE ALERT', color: 'var(--danger)', bg: 'var(--danger-bg)', text: 'var(--danger-muted)', icon: '🚨' }
      : type === 'exam_excellent'
      ? { title: '🏆 EXCELLENT EXAM RESULT', color: 'var(--success)', bg: 'var(--success-bg)', text: 'var(--success)', icon: '🏆' }
      : type === 'exam_good'
      ? { title: '🌟 EXAM RESULT ANNOUNCEMENT', color: 'var(--accent)', bg: 'var(--accent-soft)', text: 'var(--accent)', icon: '🌟' }
      : type === 'exam_needs_improvement'
      ? { title: '⚠️ EXAM RESULT - ATTENTION', color: 'var(--warning)', bg: 'var(--warning-bg)', text: 'var(--warning)', icon: '⚠️' }
      : { title: '📢 IMPORTANT ANNOUNCEMENT', color: 'var(--danger)', bg: 'var(--danger-bg)', text: 'var(--danger-muted)', icon: '📢' };

  const isAbsentNotice = type === 'exam_absent' && role === 'parent';

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
            {notice.title}
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
          {type === 'schedule' && notice.noticeDate && (
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
                const d = new Date(notice.noticeDate);
                if (isNaN(d.getTime())) return notice.noticeDate;
                const day = String(d.getDate()).padStart(2, '0');
                const month = String(d.getMonth() + 1).padStart(2, '0');
                return `${day}/${month}/${d.getFullYear()}`;
              })()}</span>
            </div>
          )}
          <div 
            style={{ lineHeight: '1.25', margin: '4px 0' }}
            dangerouslySetInnerHTML={{ __html: sanitizeNoticeHtml(notice.body || '') }}
          />

          {/* Interactive Absence Reason Form for Parent */}
          {isAbsentNotice && setAbsenceReason && (
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
              {(absenceReason === '📝 Other Reason / अन्य कारण' || absenceReason === '📝 Other Reason' || absenceReason === 'other') && setAbsenceRemarks && (
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
                alert('Please select a reason for absence before submitting. / कृपया आगे बढ़ने से पहले अनुपस्थिति का कारण चुनें।');
                return;
              }
              onDismiss(notice.id, absenceReason, absenceRemarks);
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
            {isAbsentNotice 
              ? 'कारण सबमिट करें और आगे बढ़ें / Submit Reason & Proceed' 
              : role === 'parent'
              ? 'I Understand & Dismiss / समझ गया एवं बंद करें'
              : 'I Understand & Dismiss'}
          </button>
        </div>
      </div>
    </div>
  );
}
