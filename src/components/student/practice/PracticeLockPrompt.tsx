'use client';

import React from 'react';
import { useRouter } from 'next/navigation';

interface PracticeLockPromptProps {
  type: 'autonomous' | 'textbook';
  topicCode: string;
  category: string;
  textbookStudyMessage?: string;
  lockType?: 'initial' | 'cooldown' | 'daily' | 'quota_reached' | null;
  textbookConfirmedCheck?: boolean;
  setTextbookConfirmedCheck?: (checked: boolean) => void;
  confirmingTextbook?: boolean;
  onConfirmTextbook?: () => void;
}

export function PracticeLockPrompt({
  type,
  textbookStudyMessage,
  lockType,
  textbookConfirmedCheck = false,
  setTextbookConfirmedCheck,
  confirmingTextbook = false,
  onConfirmTextbook
}: PracticeLockPromptProps) {
  const router = useRouter();

  if (type === 'autonomous') {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', padding: '20px' }}>
        <div style={{ maxWidth: '480px', width: '100%', textAlign: 'center', padding: '32px 24px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--warning)', boxShadow: 'var(--shadow-glass)' }}>
          <div style={{ fontSize: '3rem', marginBottom: '12px' }}>🔒</div>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--text)', marginBottom: '8px' }}>Practice Restricted / अभ्यास प्रतिबंधित</h3>
          <p style={{ fontSize: '13.5px', color: 'var(--text-muted)', lineHeight: '1.5', marginBottom: '20px' }}>
            Autonomous mode is active on your account. Self-directed topic practice is disabled.
          </p>
          <button className="btn btn-primary" onClick={() => router.push('/student')}>
            🏠 Back to Dashboard
          </button>
        </div>
      </div>
    );
  }

  if (type === 'textbook') {
    const isQuota = lockType === 'quota_reached';
    const isLockedState = lockType === 'cooldown' || lockType === 'daily' || isQuota;
    const icon = lockType === 'cooldown' ? '⏳' : lockType === 'daily' ? '🔒' : isQuota ? '🎓' : '📖';
    const heading = lockType === 'cooldown' 
      ? 'Deliberation Cooldown Active / विश्राम अवधि ⏳' 
      : lockType === 'daily' 
        ? 'Daily Limit Reached / दैनिक अभ्यास सीमा 🔒' 
        : isQuota 
          ? 'Practice Quota Completed / अभ्यास कोटा पूर्ण 🎓'
          : 'Time to hit the textbook! / पाठ्यपुस्तक पढ़ें 📚';

    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', padding: '20px' }}>
        <div style={{ 
          maxWidth: '520px', 
          width: '100%', 
          textAlign: 'center', 
          padding: '40px 30px', 
          background: 'var(--surface)', 
          borderRadius: 'var(--radius-lg)', 
          border: isQuota ? '1px solid var(--accent)' : '1px solid var(--warning)', 
          boxShadow: 'var(--shadow-glass)',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center'
        }}>
          <div style={{ fontSize: '3.5rem', marginBottom: '16px' }}>{icon}</div>
          <h3 style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--text)', marginBottom: '12px' }}>
            {heading}
          </h3>
          <p style={{ fontSize: '14px', color: 'var(--text-muted)', lineHeight: '1.6', marginBottom: '24px' }}>
            {textbookStudyMessage || "Let's take a break from tests. Please read your textbook and review your class notes for this chapter before trying again."}
          </p>
          
          {!isLockedState && (
            <label style={{ 
              display: 'flex', 
              alignItems: 'center', 
              gap: '10px', 
              fontSize: '13px', 
              color: 'var(--text)', 
              cursor: 'pointer',
              padding: '12px 16px',
              background: 'var(--bg)',
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--border-light)',
              width: '100%',
              marginBottom: '24px',
              boxSizing: 'border-box'
            }}>
              <input 
                type="checkbox" 
                checked={textbookConfirmedCheck} 
                onChange={(e) => setTextbookConfirmedCheck?.(e.target.checked)}
                style={{ width: '18px', height: '18px', cursor: 'pointer' }}
              />
              <span style={{ textAlign: 'left' }}>I confirm that I have reviewed this concept in my textbook/notes.</span>
            </label>
          )}

          <div style={{ display: 'flex', gap: '12px', width: '100%' }}>
            <button 
              className="btn btn-secondary" 
              onClick={() => router.push('/student')}
              style={{ flex: 1 }}
            >
              🏠 Back to Dashboard
            </button>
            {!isLockedState && (
              <button 
                className="btn btn-primary" 
                disabled={!textbookConfirmedCheck || confirmingTextbook}
                onClick={onConfirmTextbook}
                style={{ flex: 1 }}
              >
                {confirmingTextbook ? 'Updating...' : '⚡ Unlock & Resume'}
              </button>
            )}
          </div>
        </div>
      </div>
    );
  }

  return null;
}
