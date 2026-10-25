'use client';

import React from 'react';

export interface ModalShellProps {
  isOpen: boolean;
  onClose?: () => void;
  children: React.ReactNode;
  maxWidth?: string | number;
  width?: string;
  zIndex?: number;
  align?: 'center' | 'flex-start';
  padding?: string;
  backdropBlur?: string;
  className?: string;
  cardStyle?: React.CSSProperties;
}

export function ModalShell({
  isOpen,
  onClose,
  children,
  maxWidth = '450px',
  width = '90%',
  zIndex = 10000,
  align = 'center',
  padding = '16px',
  backdropBlur = '4px',
  className = '',
  cardStyle,
}: ModalShellProps) {
  if (!isOpen) return null;

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        background: 'rgba(0, 0, 0, 0.65)',
        backdropFilter: `blur(${backdropBlur})`,
        WebkitBackdropFilter: `blur(${backdropBlur})`,
        display: 'flex',
        alignItems: align,
        justifyContent: 'center',
        zIndex,
        padding,
        overflowY: 'auto',
      }}
      onClick={(e) => {
        if (e.target === e.currentTarget && onClose) {
          onClose();
        }
      }}
    >
      <div
        className={className}
        style={{
          background: 'var(--surface-popover)',
          border: '1px solid var(--border)',
          borderRadius: '12px',
          padding: '20px',
          maxWidth: typeof maxWidth === 'number' ? `${maxWidth}px` : maxWidth,
          width,
          boxShadow: 'var(--shadow-lg)',
          margin: align === 'flex-start' ? '0 auto' : undefined,
          ...cardStyle,
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {children}
      </div>
    </div>
  );
}

export default ModalShell;
