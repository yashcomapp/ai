'use client';

import React, { useEffect, useState } from 'react';

interface Toast {
  id: string;
  message: string;
  type: 'success' | 'error' | 'info';
}

export default function ToastContainer() {
  const [toasts, setToasts] = useState<Toast[]>([]);

  useEffect(() => {
    if (typeof window === 'undefined') return;

    const originalAlert = window.alert;

    window.alert = (message: any) => {
      const msgStr = String(message);
      const isError = msgStr.includes('❌') || msgStr.toLowerCase().includes('error') || msgStr.toLowerCase().includes('fail') || msgStr.includes('issue') || msgStr.toLowerCase().includes('invalid');
      const isSuccess = msgStr.includes('✅') || msgStr.toLowerCase().includes('success') || msgStr.toLowerCase().includes('approved');
      const type = isError ? 'error' : (isSuccess ? 'success' : 'info');

      // Strip off the leading emoji if any (since we show custom styled emojis in the toast)
      const cleanMsg = msgStr.replace(/^[❌✅⚠️💡]\s*/, '');

      const newToast: Toast = {
        id: Math.random().toString(36).substring(2, 9),
        message: cleanMsg,
        type
      };

      setToasts(prev => [...prev, newToast]);

      // Remove after 4 seconds
      setTimeout(() => {
        setToasts(prev => prev.filter(t => t.id !== newToast.id));
      }, 4000);
    };

    return () => {
      window.alert = originalAlert;
    };
  }, []);

  const removeToast = (id: string) => {
    setToasts(prev => prev.filter(t => t.id !== id));
  };

  return (
    <div className="app-toast-container">
      {toasts.map(toast => {
        let bg = 'rgba(0, 0, 0, 0.9)'; // Dark slate glass
        let border = '1px solid rgba(255, 255, 255, 0.08)';
        let icon = 'ℹ️';
        let color = 'var(--text)';

        if (toast.type === 'success') {
          bg = 'rgba(22, 163, 74, 0.95)'; // Success green glass
          border = '1px solid rgba(34, 197, 94, 0.25)';
          icon = '✅';
          color = '#ffffff';
        } else if (toast.type === 'error') {
          bg = 'rgba(220, 38, 38, 0.95)'; // Error red glass
          border = '1px solid rgba(239, 68, 68, 0.25)';
          icon = '❌';
          color = '#ffffff';
        }

        return (
          <div
            key={toast.id}
            className="app-toast-item"
            onClick={() => removeToast(toast.id)}
            style={{
              background: bg,
              border,
              color
            }}
          >
            <span style={{ fontSize: '16px' }}>{icon}</span>
            <span style={{ flex: 1 }}>{toast.message}</span>
            <span style={{ opacity: 0.5, fontSize: '11px', paddingLeft: '8px' }}>✕</span>
          </div>
        );
      })}
    </div>
  );
}
