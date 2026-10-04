'use client';

import React from 'react';
import { preprocessMathText } from '@/lib/questionTypes';
import { highlightModelAnswerKeywords } from '@/lib/pdfExport';

interface InPlaceAiGeneratorProps {
  title: string;
  subtitle: string;
  buttonLabel: string;
  onGeneratePrompt: () => void;
  qbPrompt: string;
  setQbPrompt: (val: string) => void;
  qbPasteJson: string;
  setQbPasteJson: (val: string) => void;
  qbStatus: string;
  onParseQuestions: () => void;
  previewQuestions: any[];
  setPreviewQuestions: React.Dispatch<React.SetStateAction<any[]>>;
  selectedSubjects: string[];
  onSaveValidatedQuestions: () => void;
  qbSaving: boolean;
  showPyqInfo?: boolean;
}

export default function InPlaceAiGenerator({
  title,
  subtitle,
  buttonLabel,
  onGeneratePrompt,
  qbPrompt,
  setQbPrompt,
  qbPasteJson,
  setQbPasteJson,
  qbStatus,
  onParseQuestions,
  previewQuestions,
  setPreviewQuestions,
  selectedSubjects,
  onSaveValidatedQuestions,
  qbSaving,
  showPyqInfo = false
}: InPlaceAiGeneratorProps) {
  return (
    <div style={{ border: '2px solid var(--accent)', borderRadius: 'var(--radius)', padding: '16px', background: 'var(--surface)', display: 'flex', flexDirection: 'column', gap: '12px', marginTop: '10px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
        <div>
          <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 800, color: 'var(--accent)' }}>
            {title}
          </h4>
          <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>
            {subtitle}
          </div>
        </div>
        <button 
          className="btn btn-secondary btn-sm"
          onClick={onGeneratePrompt}
          style={{ fontSize: '11px', fontWeight: 700, padding: '6px 14px', background: 'var(--purple)', color: 'var(--text-white)', border: 'none' }}
        >
          {buttonLabel}
        </button>
      </div>

      {/* Status Banner with Anchor ID */}
      {qbStatus && (
        <div 
          id="qb-status-banner"
          style={{ 
            padding: '8px 12px', 
            background: qbStatus.startsWith('❌') ? 'var(--danger-bg)' : 'var(--success-bg)', 
            border: `1px solid ${qbStatus.startsWith('❌') ? 'var(--danger-border)' : 'var(--success-border)'}`, 
            borderRadius: '4px', 
            fontSize: '11px', 
            color: qbStatus.startsWith('❌') ? 'var(--danger)' : 'var(--success)', 
            fontWeight: 600, 
            whiteSpace: 'pre-line' 
          }}
        >
          {qbStatus}
        </div>
      )}

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '12px' }}>
        <div className="form-group">
          <label style={{ fontSize: '11px', fontWeight: 700 }}>📋 Generated AI Prompt</label>
          <textarea 
            className="form-input" 
            rows={5} 
            value={qbPrompt} 
            onChange={(e) => setQbPrompt(e.target.value)}
            placeholder="Click generate prompt button above to populate prompt..."
            style={{ fontSize: '11px', fontFamily: 'monospace' }}
          />
        </div>

        <div className="form-group">
          <label style={{ fontSize: '11px', fontWeight: 700 }}>📥 Paste AI Response (JSON)</label>
          <textarea 
            className="form-input" 
            rows={5} 
            value={qbPasteJson} 
            onChange={(e) => setQbPasteJson(e.target.value)}
            placeholder="Paste JSON array response from Gemini or ChatGPT here..."
            style={{ fontSize: '11px', fontFamily: 'monospace' }}
          />
        </div>
      </div>

      <button 
        className="btn btn-primary btn-sm"
        onClick={onParseQuestions}
        disabled={!qbPasteJson.trim()}
        style={{ alignSelf: 'flex-end', padding: '8px 18px', fontSize: '12px', fontWeight: 700 }}
      >
        ⚡ Parse & Preview Questions for Review
      </button>

      {/* Interactive Question Preview & Review Cards with Standard KaTeX Rendering */}
      {previewQuestions.length > 0 && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginTop: '10px', borderTop: '1px dashed var(--border-light)', paddingTop: '14px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 800, color: 'var(--accent)' }}>
              🔍 Review & Edit Parsed Questions ({previewQuestions.length} Qs)
            </h4>
            <button 
              className="btn btn-secondary btn-sm"
              onClick={() => setPreviewQuestions([])}
              style={{ fontSize: '10px', padding: '2px 8px' }}
            >
              ✕ Clear Preview
            </button>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', maxHeight: '450px', overflowY: 'auto' }}>
            {previewQuestions.map((q, idx) => (
              <div key={idx} className="math-container" style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '12px', background: 'var(--bg-soft)', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '11px' }}>
                  <span style={{ fontWeight: 800, color: 'var(--accent)' }}>
                    Q{idx + 1} • Topic: {q.topicName || 'General'}
                  </span>
                  <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                    <span className="badge" style={{ background: 'var(--surface-3)', color: 'var(--text)', padding: '2px 8px', borderRadius: '4px', fontSize: '10px' }}>
                      {q.marks} Mark{q.marks > 1 ? 's' : ''} ({q.type})
                    </span>
                    <button 
                      className="btn btn-secondary btn-sm" 
                      onClick={() => setPreviewQuestions(prev => prev.filter((_, i) => i !== idx))}
                      style={{ background: 'var(--danger-bg)', color: 'var(--danger)', border: '1px solid var(--danger-border)', fontSize: '10px', padding: '2px 6px' }}
                    >
                      🗑️ Delete
                    </button>
                  </div>
                </div>

                {/* Editable Question Text */}
                <div className="form-group">
                  <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)' }}>Question Text:</label>
                  <textarea 
                    className="form-input" 
                    rows={2} 
                    value={q.text} 
                    onChange={(e) => {
                      const val = e.target.value;
                      setPreviewQuestions(prev => {
                        const next = [...prev];
                        next[idx] = { ...next[idx], text: val };
                        return next;
                      });
                    }}
                    style={{ fontSize: '11px' }}
                  />
                  {/* Live Math & Diagram Render Preview */}
                  <div 
                    className="math-container" 
                    style={{ fontSize: '11px', color: 'var(--text)', marginTop: '4px', padding: '6px 10px', background: 'var(--surface)', border: '1px dashed var(--border-light)', borderRadius: '4px', minHeight: '18px', whiteSpace: 'pre-line' }}
                    dangerouslySetInnerHTML={{ __html: preprocessMathText(q.text || '') }}
                  />
                </div>

                {/* Editable Model Answer */}
                <div className="form-group">
                  <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)' }}>Model Answer:</label>
                  <textarea 
                    className="form-input" 
                    rows={3} 
                    value={q.solution} 
                    onChange={(e) => {
                      const val = e.target.value;
                      setPreviewQuestions(prev => {
                        const next = [...prev];
                        next[idx] = { ...next[idx], solution: val };
                        return next;
                      });
                    }}
                    style={{ fontSize: '11px' }}
                  />
                </div>

                {/* Editable Keywords with Smooth Unbound Text State */}
                <div className="form-group">
                  <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--accent)' }}>🏷️ Key Words / Phrases (Comma Separated):</label>
                  <input 
                    type="text" 
                    className="form-input" 
                    value={q.keywordsText ?? (Array.isArray(q.keywords) ? q.keywords.join(', ') : '')} 
                    onChange={(e) => {
                      const val = e.target.value;
                      const kwArr = val.split(',').map(s => s.trim()).filter(Boolean);
                      setPreviewQuestions(prev => {
                        const next = [...prev];
                        next[idx] = { ...next[idx], keywordsText: val, keywords: kwArr };
                        return next;
                      });
                    }}
                    style={{ fontSize: '11px' }}
                  />
                </div>

                {/* PYQ Info Reference (If enabled or present) */}
                {showPyqInfo && (
                  <div className="form-group">
                    <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--accent)' }}>🎓 PYQ Info / Board Year Reference (Optional):</label>
                    <input 
                      type="text" 
                      className="form-input" 
                      value={q.pyqInfo || ''} 
                      onChange={(e) => {
                        const val = e.target.value;
                        setPreviewQuestions(prev => {
                          const next = [...prev];
                          next[idx] = { ...next[idx], pyqInfo: val };
                          return next;
                        });
                      }}
                      placeholder="e.g. CBSE Board 2020 or PYQ Style Practice"
                      style={{ fontSize: '11px' }}
                    />
                  </div>
                )}

                {/* Textbook Practice Set Reference (For Math) */}
                {selectedSubjects.some(subj => /math|algebra|geometry|ganit/i.test(subj)) && (
                  <div className="form-group">
                    <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--accent)' }}>📖 Textbook Practice Set Reference (Optional):</label>
                    <input 
                      type="text" 
                      className="form-input" 
                      value={q.textbookPracticeSet || ''} 
                      onChange={(e) => {
                        const val = e.target.value;
                        setPreviewQuestions(prev => {
                          const next = [...prev];
                          next[idx] = { ...next[idx], textbookPracticeSet: val };
                          return next;
                        });
                      }}
                      placeholder="e.g. Practice Set 1.2: Q1 to Q5"
                      style={{ fontSize: '11px' }}
                    />
                  </div>
                )}

                {/* Live Standard KaTeX Highlight Preview */}
                <div className="math-container" style={{ background: 'var(--surface)', padding: '8px 12px', borderRadius: '4px', border: '1px solid var(--border-light)', fontSize: '11px', lineHeight: 1.5, whiteSpace: 'pre-line' }}>
                  <strong style={{ color: 'var(--success)', fontSize: '10px', display: 'block', marginBottom: '2px' }}>💡 Live KaTeX Model Answer Highlight Preview:</strong>
                  <div 
                    dangerouslySetInnerHTML={{ 
                      __html: preprocessMathText(highlightModelAnswerKeywords(q.solution, q.keywords)) 
                    }} 
                  />
                </div>
              </div>
            ))}
          </div>

          <button 
            className="btn btn-primary"
            onClick={onSaveValidatedQuestions}
            disabled={qbSaving}
            style={{ padding: '10px', fontSize: '12px', fontWeight: 800, marginTop: '8px' }}
          >
            {qbSaving ? '⏳ Saving Validated Questions...' : `💾 Save ${previewQuestions.length} Validated Questions to Question Bank`}
          </button>
        </div>
      )}
    </div>
  );
}
