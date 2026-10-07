'use client';

import React, { useRef, useState, useEffect } from 'react';

interface DateTimeInputDMYProps {
  value?: string; // Standard YYYY-MM-DDTHH:mm
  onChange: (isoDateTime: string) => void;
  disabled?: boolean;
  required?: boolean;
  className?: string;
  style?: React.CSSProperties;
  inputStyle?: React.CSSProperties;
  min?: string;
  max?: string;
}

/**
 * Converts YYYY-MM-DDTHH:mm to DD/MM/YYYY hh:mm AM/PM
 */
function formatToDDMMYYYYTime(isoStr?: string | null): string {
  if (!isoStr) return '';
  const clean = String(isoStr).trim();
  const [datePart, timePart] = clean.split('T');
  if (!datePart || !timePart) return clean;

  const dateParts = datePart.split('-');
  if (dateParts.length !== 3) return clean;
  const [y, m, d] = dateParts;

  const [hStr, minStr] = timePart.split(':');
  if (hStr === undefined || minStr === undefined) return `${d}/${m}/${y}`;

  const h = parseInt(hStr, 10);
  const isPM = h >= 12;
  const h12 = h % 12 === 0 ? 12 : h % 12;
  const ampm = isPM ? 'PM' : 'AM';
  const paddedH12 = String(h12).padStart(2, '0');
  const paddedMin = String(minStr).padStart(2, '0');

  return `${d}/${m}/${y} ${paddedH12}:${paddedMin} ${ampm}`;
}

/**
 * SSOT Date & Time Input Component
 * Enforces DD/MM/YYYY hh:mm AM/PM display format everywhere across all browsers and locales,
 * while maintaining YYYY-MM-DDTHH:mm ISO data format under the hood.
 */
export default function DateTimeInputDMY({
  value,
  onChange,
  disabled = false,
  required = false,
  className,
  style,
  inputStyle,
  min,
  max
}: DateTimeInputDMYProps) {
  const pickerRef = useRef<HTMLInputElement>(null);
  const [displayText, setDisplayText] = useState<string>(() => formatToDDMMYYYYTime(value || ''));

  useEffect(() => {
    setDisplayText(formatToDDMMYYYYTime(value || ''));
  }, [value]);

  const isoValue = value || '';

  const handlePickerChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const picked = e.target.value; // YYYY-MM-DDTHH:mm
    if (picked) {
      onChange(picked);
      setDisplayText(formatToDDMMYYYYTime(picked));
    } else {
      onChange('');
      setDisplayText('');
    }
  };

  const openPicker = () => {
    if (disabled) return;
    try {
      if (pickerRef.current) {
        if (typeof (pickerRef.current as any).showPicker === 'function') {
          (pickerRef.current as any).showPicker();
        } else {
          pickerRef.current.focus();
          pickerRef.current.click();
        }
      }
    } catch {
      pickerRef.current?.click();
    }
  };

  return (
    <div
      style={{
        position: 'relative',
        display: 'inline-flex',
        alignItems: 'center',
        boxSizing: 'border-box',
        width: '100%',
        ...style
      }}
      className={className}
    >
      <input
        type="text"
        value={displayText}
        readOnly
        onClick={openPicker}
        placeholder="DD/MM/YYYY HH:MM AM/PM"
        disabled={disabled}
        required={required}
        style={{
          width: '100%',
          boxSizing: 'border-box',
          height: '34px',
          padding: '5px 32px 5px 8px',
          borderRadius: 'var(--radius-sm)',
          border: '1px solid var(--border-light)',
          background: disabled ? 'var(--surface-2)' : 'var(--surface)',
          color: disabled ? 'var(--text-muted)' : 'var(--text)',
          fontSize: '12px',
          fontWeight: 600,
          fontFamily: 'monospace, inherit',
          letterSpacing: '0.2px',
          cursor: disabled ? 'not-allowed' : 'pointer',
          outline: 'none',
          ...inputStyle
        }}
      />

      {/* Hidden native datetime-local picker */}
      <input
        ref={pickerRef}
        type="datetime-local"
        value={isoValue}
        min={min}
        max={max}
        onChange={handlePickerChange}
        tabIndex={-1}
        aria-hidden="true"
        style={{
          position: 'absolute',
          opacity: 0,
          pointerEvents: 'none',
          width: 0,
          height: 0,
          right: 0,
          bottom: 0
        }}
      />

      <button
        type="button"
        onClick={openPicker}
        disabled={disabled}
        tabIndex={-1}
        title="Pick Date & Time (DD/MM/YYYY)"
        style={{
          position: 'absolute',
          right: '6px',
          background: 'transparent',
          border: 'none',
          cursor: disabled ? 'not-allowed' : 'pointer',
          padding: '2px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '13px',
          color: 'var(--text-muted)'
        }}
      >
        📅
      </button>
    </div>
  );
}
