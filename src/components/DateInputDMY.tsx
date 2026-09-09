'use client';

import React, { useRef, useState, useEffect } from 'react';
import { formatToDDMMYYYY, formatToYYYYMMDD } from '@/lib/dateUtils';

interface DateInputDMYProps {
  value?: string; // Standard YYYY-MM-DD or DD/MM/YYYY
  onChange: (isoDate: string) => void;
  onKeyDown?: (e: React.KeyboardEvent<HTMLInputElement>) => void;
  inputRef?: React.Ref<HTMLInputElement>;
  placeholder?: string;
  disabled?: boolean;
  required?: boolean;
  className?: string;
  style?: React.CSSProperties;
}

/**
 * SSOT Date Input Component
 * Enforces DD/MM/YYYY display format everywhere across all browsers and locales,
 * while maintaining YYYY-MM-DD ISO data storage under the hood.
 */
export default function DateInputDMY({
  value,
  onChange,
  onKeyDown,
  inputRef,
  placeholder = 'DD/MM/YYYY',
  disabled = false,
  required = false,
  className,
  style
}: DateInputDMYProps) {
  const datePickerRef = useRef<HTMLInputElement>(null);
  
  // Format incoming ISO or raw value to DD/MM/YYYY for text display
  const [displayText, setDisplayText] = useState<string>(() => formatToDDMMYYYY(value || ''));

  useEffect(() => {
    setDisplayText(formatToDDMMYYYY(value || ''));
  }, [value]);

  // Convert current value to YYYY-MM-DD for native hidden datepicker
  const isoValue = formatToYYYYMMDD(value || '');

  const handleTextChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    let raw = e.target.value.replace(/[^0-9/]/g, '');
    
    // Auto-insert slashes if typing numbers continuously
    if (raw.length === 2 && !raw.includes('/')) {
      raw = raw + '/';
    } else if (raw.length === 5 && (raw.match(/\//g) || []).length === 1) {
      raw = raw + '/';
    }
    
    setDisplayText(raw);

    // If matches complete DD/MM/YYYY
    if (/^\d{2}\/\d{2}\/\d{4}$/.test(raw)) {
      const [d, m, y] = raw.split('/');
      const day = parseInt(d, 10);
      const month = parseInt(m, 10);
      const year = parseInt(y, 10);

      if (month >= 1 && month <= 12 && day >= 1 && day <= 31 && year >= 1900 && year <= 2100) {
        const iso = `${year}-${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
        onChange(iso);
      }
    } else if (raw === '') {
      onChange('');
    }
  };

  const handlePickerChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const pickedIso = e.target.value; // YYYY-MM-DD
    if (pickedIso) {
      onChange(pickedIso);
      setDisplayText(formatToDDMMYYYY(pickedIso));
    }
  };

  const openCalendar = () => {
    if (disabled) return;
    try {
      if (datePickerRef.current) {
        if (typeof (datePickerRef.current as any).showPicker === 'function') {
          (datePickerRef.current as any).showPicker();
        } else {
          datePickerRef.current.focus();
          datePickerRef.current.click();
        }
      }
    } catch (err) {
      datePickerRef.current?.click();
    }
  };

  return (
    <div
      style={{
        position: 'relative',
        display: 'inline-flex',
        alignItems: 'center',
        boxSizing: 'border-box',
        ...style
      }}
      className={className}
    >
      <input
        ref={inputRef}
        type="text"
        value={displayText}
        onChange={handleTextChange}
        onKeyDown={onKeyDown}
        placeholder={placeholder}
        disabled={disabled}
        required={required}
        maxLength={10}
        style={{
          width: '100%',
          boxSizing: 'border-box',
          padding: '6px 28px 6px 8px',
          borderRadius: '4px',
          border: '1px solid var(--border-light)',
          background: 'var(--surface)',
          color: 'var(--text)',
          fontSize: '11px',
          fontFamily: 'monospace, inherit',
          letterSpacing: '0.3px',
          ...style
        }}
      />

      {/* Hidden native date picker triggered by the icon */}
      <input
        ref={datePickerRef}
        type="date"
        value={isoValue}
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
        onClick={openCalendar}
        disabled={disabled}
        tabIndex={-1}
        title="Pick date (DD/MM/YYYY)"
        style={{
          position: 'absolute',
          right: '4px',
          background: 'transparent',
          border: 'none',
          cursor: disabled ? 'not-allowed' : 'pointer',
          padding: '2px 4px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '12px',
          color: 'var(--text-muted)'
        }}
      >
        📅
      </button>
    </div>
  );
}
