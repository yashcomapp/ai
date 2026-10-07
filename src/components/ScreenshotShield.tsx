'use client';

import React, { useMemo } from 'react';
import { useScreenshotGuard } from '@/hooks/useScreenshotGuard';

interface ScreenshotShieldProps {
  children: React.ReactNode;
  enabled?: boolean;
  watermarkEnabled?: boolean;
  blurOnFocusLoss?: boolean;
  clearClipboardOnPrint?: boolean;
  studentName?: string;
  studentBatch?: string;
  examTitle?: string;
  onViolation?: (reason: string) => void;
  className?: string;
}

export function ScreenshotShield({
  children,
  enabled = true,
  watermarkEnabled = true,
  blurOnFocusLoss = true,
  clearClipboardOnPrint = true,
  studentName,
  studentBatch,
  examTitle,
  onViolation,
  className = ''
}: ScreenshotShieldProps) {
  const { isObscured, alertMessage, dismissAlert } = useScreenshotGuard({
    enabled,
    blurOnFocusLoss,
    clearClipboardOnPrint,
    onViolation
  });

  // Generate watermark pattern string
  const watermarkText = useMemo(() => {
    const parts = [
      studentName || 'Student',
      studentBatch || 'Class',
      examTitle || 'Proctored Exam'
    ].filter(Boolean);
    return parts.join(' • ');
  }, [studentName, studentBatch, examTitle]);

  // Create an array of watermark grid items
  const watermarkTiles = useMemo(() => {
    return Array.from({ length: 24 });
  }, []);

  return (
    <div className={`relative min-h-screen select-none ${className}`}>
      {/* 1. Global Print CSS Blocker */}
      {enabled && (
        <style dangerouslySetInnerHTML={{ __html: `
          @media print {
            body, html {
              display: none !important;
              visibility: hidden !important;
            }
          }
          ::selection {
            background: transparent !important;
            color: inherit !important;
          }
        ` }} />
      )}

      {/* 2. Repeating Forensic Background Watermark */}
      {enabled && watermarkEnabled && (
        <div
          aria-hidden="true"
          className="pointer-events-none fixed inset-0 z-10 overflow-hidden opacity-[0.035] dark:opacity-[0.05] select-none flex flex-wrap justify-around items-center content-around p-4"
        >
          {watermarkTiles.map((_, idx) => (
            <div
              key={idx}
              className="transform -rotate-12 whitespace-nowrap text-xs md:text-sm font-mono font-bold tracking-wider text-slate-800 dark:text-slate-100 m-6"
            >
              {watermarkText}
            </div>
          ))}
        </div>
      )}

      {/* 3. Main Exam Interface Content */}
      <div className={`relative z-0 transition duration-150 ${isObscured ? 'filter blur-xl pointer-events-none select-none' : ''}`}>
        {children}
      </div>

      {/* 4. Anti-Snipping / Window Loss Shield Curtain */}
      {enabled && blurOnFocusLoss && isObscured && (
        <div className="fixed inset-0 z-50 flex flex-col items-center justify-center bg-slate-900/80 backdrop-blur-md text-white p-6 text-center animate-fade-in">
          <div className="w-16 h-16 rounded-full bg-amber-500/20 border border-amber-500/40 flex items-center justify-center mb-4 text-amber-400 text-3xl shadow-lg">
            🛡️
          </div>
          <h2 className="text-xl md:text-2xl font-bold tracking-tight mb-2">
            Exam Content Shielded
          </h2>
          <p className="text-sm md:text-base text-slate-300 max-w-md mb-6 leading-relaxed">
            The exam window lost focus or a screen capture utility was detected. Please click below to return to your exam.
          </p>
          <button
            onClick={() => {
              window.focus();
            }}
            className="px-6 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 active:scale-95 text-slate-950 font-semibold text-sm transition shadow-lg shadow-amber-500/20"
          >
            Click to Resume Exam
          </button>
        </div>
      )}

      {/* 5. Security Interception Alert Toast */}
      {alertMessage && (
        <div className="fixed bottom-6 left-1/2 transform -translate-x-1/2 z-[100] max-w-md w-11/12 bg-rose-950 border border-rose-500/50 text-rose-200 px-4 py-3 rounded-2xl shadow-2xl flex items-center justify-between gap-3 animate-bounce-once">
          <div className="flex items-center gap-3">
            <span className="text-lg">🚫</span>
            <span className="text-xs md:text-sm font-medium">{alertMessage}</span>
          </div>
          <button
            onClick={dismissAlert}
            className="text-rose-400 hover:text-rose-100 text-sm font-bold px-2 py-1"
          >
            ✕
          </button>
        </div>
      )}
    </div>
  );
}
export default ScreenshotShield;
