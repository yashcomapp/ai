'use client';

import React from 'react';

interface ClassFilterSelectProps {
  value: string;
  onChange: (val: string) => void;
  classes: (string | number)[];
  label?: string;
}

export default function ClassFilterSelect({
  value,
  onChange,
  classes,
  label = 'Class'
}: ClassFilterSelectProps) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
      <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>{label}</label>
      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        style={{ padding: '7px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '12px' }}
      >
        <option value="ALL">All Classes</option>
        {classes.map(cls => (
          <option key={cls} value={cls}>Class {cls}</option>
        ))}
      </select>
    </div>
  );
}
