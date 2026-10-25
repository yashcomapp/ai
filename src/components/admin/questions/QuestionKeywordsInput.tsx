'use client';

import React from 'react';

interface QuestionKeywordsInputProps {
  keywords?: string[] | string;
  onChange: (keywords: string[]) => void;
}

export function QuestionKeywordsInput({ keywords, onChange }: QuestionKeywordsInputProps) {
  const value = Array.isArray(keywords) ? keywords.join(', ') : (keywords || '');

  return (
    <div>
      <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--accent)', marginBottom: '4px' }}>
        🏷️ Essential Keywords / Key Phrases for Subject (Comma-Separated):
      </label>
      <input 
        type="text"
        className="form-input"
        placeholder="e.g. centripetal force, directed towards center, gravitational force"
        value={value}
        onChange={(e) => {
          const kwList = e.target.value.split(',').map((s) => s.trim()).filter(Boolean);
          onChange(kwList);
        }}
        style={{ width: '100%', fontSize: '12px' }}
      />
    </div>
  );
}
