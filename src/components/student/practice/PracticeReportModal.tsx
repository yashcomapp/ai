'use client';

import React from 'react';

interface PracticeReportModalProps {
  isOpen: boolean;
  reportReason: string;
  setReportReason: (reason: string) => void;
  reportNotes: string;
  setReportNotes: (notes: string) => void;
  isSubmittingReport: boolean;
  onClose: () => void;
  onSubmitReport: () => void;
}

export function PracticeReportModal({
  isOpen,
  reportReason,
  setReportReason,
  reportNotes,
  setReportNotes,
  isSubmittingReport,
  onClose,
  onSubmitReport
}: PracticeReportModalProps) {
  if (!isOpen) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.6)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 25000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
      <div style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', padding: '24px', maxWidth: '480px', width: '100%', boxShadow: 'var(--shadow-lg)' }}>
        <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--text)', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '8px' }}>
          🚩 Report Question &amp; Skip
        </h3>
        <p style={{ fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.4', marginBottom: '16px' }}>
          If there is an error with this question (missing options, broken symbols, incomplete text), you can report it. An automated screenshot proof will be sent to your teacher, and this question will be <strong>excluded from your score and mastery calculations with zero penalty</strong>.
        </p>

        <div style={{ marginBottom: '14px' }}>
          <label style={{ display: 'block', fontSize: '12px', fontWeight: 700, marginBottom: '6px', color: 'var(--text)' }}>
            Issue Category:
          </label>
          <select 
            value={reportReason}
            onChange={(e) => setReportReason(e.target.value)}
            style={{ width: '100%', padding: '10px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', fontSize: '13px' }}
          >
            <option value="missing_options">Missing Options / No Choices</option>
            <option value="broken_formula">Broken Formula / LaTeX / Image</option>
            <option value="incorrect_text">Incomplete or Incorrect Question Text</option>
            <option value="duplicate_options">Duplicate / Confusing Options</option>
            <option value="other">Other Issue</option>
          </select>
        </div>

        <div style={{ marginBottom: '16px' }}>
          <label style={{ display: 'block', fontSize: '12px', fontWeight: 700, marginBottom: '6px', color: 'var(--text)' }}>
            Additional Notes (Optional):
          </label>
          <textarea 
            value={reportNotes}
            onChange={(e) => setReportNotes(e.target.value)}
            placeholder="Describe what looks wrong..."
            rows={2}
            style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', fontSize: '13px', resize: 'none' }}
          />
        </div>

        <div style={{ background: 'rgba(16, 185, 129, 0.08)', border: '1px solid rgba(16, 185, 129, 0.2)', borderRadius: 'var(--radius-sm)', padding: '10px 12px', fontSize: '11.5px', color: 'var(--success)', marginBottom: '18px' }}>
          📷 <strong>Automated Proof:</strong> A clean visual snapshot of this question card will be captured and attached automatically for teacher review.
        </div>

        <div style={{ display: 'flex', gap: '10px' }}>
          <button 
            type="button"
            className="btn btn-secondary" 
            onClick={onClose}
            disabled={isSubmittingReport}
            style={{ flex: 1 }}
          >
            Cancel
          </button>
          <button 
            type="button"
            className="btn btn-primary" 
            onClick={onSubmitReport}
            disabled={isSubmittingReport}
            style={{ flex: 1, background: 'var(--danger)', borderColor: 'var(--danger)' }}
          >
            {isSubmittingReport ? 'Reporting...' : 'Bypass & Report'}
          </button>
        </div>
      </div>
    </div>
  );
}
