'use client';

import React from 'react';
import { renderSortHeader } from '@/lib/feesUtils';

export interface FeeTemplate {
  templateId: string;
  name: string;
  classNum: string;
  totalPackageAmount: number;
  installments: { installmentNo: number; amount: number; dueDate?: string; dueDateOffsetDays?: number }[];
}

interface FeesTemplatesTabProps {
  templates: FeeTemplate[];
  tmplSortField: string;
  tmplSortDir: 'asc' | 'desc';
  handleTmplSort: (field: any) => void;
  massApplying: boolean;
  handleMassApplyTemplate: (templateId: string, classNum: string, overrideCustom: boolean) => Promise<void>;
  onCreateTemplate: () => void;
  onEditTemplate: (template: FeeTemplate) => void;
  onDeleteTemplate: (templateId: string) => Promise<void>;
}

export default function FeesTemplatesTab({
  templates,
  tmplSortField,
  tmplSortDir,
  handleTmplSort,
  massApplying,
  handleMassApplyTemplate,
  onCreateTemplate,
  onEditTemplate,
  onDeleteTemplate
}: FeesTemplatesTabProps) {
  const sortedTemplates = [...templates].sort((a, b) => {
    let valA: any = '';
    let valB: any = '';
    if (tmplSortField === 'name') {
      valA = (a.name || '').toLowerCase();
      valB = (b.name || '').toLowerCase();
    } else if (tmplSortField === 'classNum') {
      valA = Number(a.classNum) || 0;
      valB = Number(b.classNum) || 0;
    } else if (tmplSortField === 'totalPackageAmount') {
      valA = Number(a.totalPackageAmount) || 0;
      valB = Number(b.totalPackageAmount) || 0;
    } else if (tmplSortField === 'splits') {
      valA = a.installments?.length || 0;
      valB = b.installments?.length || 0;
    }
    if (valA < valB) return tmplSortDir === 'asc' ? -1 : 1;
    if (valA > valB) return tmplSortDir === 'asc' ? 1 : -1;
    return 0;
  });

  return (
    <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', overflow: 'hidden' }}>
      <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold' }}>Blanket Templates Configurations</h3>
        <button
          className="btn btn-primary"
          onClick={onCreateTemplate}
          style={{ padding: '6px 12px', fontSize: '12px' }}
        >
          ➕ Create Template
        </button>
      </div>

      {templates.length === 0 ? (
        <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>No templates found. Click create to get started.</div>
      ) : (
        <div style={{ overflowX: 'auto' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
            <thead>
              <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                {renderSortHeader('Template Name', 'name', tmplSortField, tmplSortDir, handleTmplSort)}
                {renderSortHeader('Class', 'classNum', tmplSortField, tmplSortDir, handleTmplSort)}
                {renderSortHeader('Package Fee', 'totalPackageAmount', tmplSortField, tmplSortDir, handleTmplSort)}
                {renderSortHeader('Splits', 'splits', tmplSortField, tmplSortDir, handleTmplSort)}
                <th style={{ padding: '12px 16px', fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', textAlign: 'right' }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {sortedTemplates.map(t => (
                <tr key={t.templateId} style={{ borderBottom: '1px solid var(--border-light)' }}>
                  <td style={{ padding: '14px 16px', fontSize: '13px', fontWeight: 'bold' }}>{t.name}</td>
                  <td style={{ padding: '14px 16px', fontSize: '13px' }}>Class {t.classNum}</td>
                  <td style={{ padding: '14px 16px', fontSize: '13px', fontWeight: 700 }}>₹{t.totalPackageAmount}</td>
                  <td style={{ padding: '14px 16px', fontSize: '13px' }}>{t.installments?.length || 0} Splits</td>
                  <td style={{ padding: '14px 16px', textAlign: 'right' }}>
                    <button
                      onClick={() => handleMassApplyTemplate(t.templateId, t.classNum, false)}
                      disabled={massApplying}
                      className="btn btn-primary"
                      style={{ padding: '4px 10px', fontSize: '11px', fontWeight: 700, marginRight: '8px', borderRadius: '4px' }}
                      title={`Apply ${t.name} to all active Class ${t.classNum} students`}
                    >
                      ⚡ Apply to Class {t.classNum}
                    </button>
                    <button
                      onClick={() => onEditTemplate(t)}
                      className="btn btn-secondary"
                      style={{ padding: '4px 8px', fontSize: '11px', marginRight: '8px' }}
                    >
                      ✏️ Edit
                    </button>
                    <button
                      onClick={() => onDeleteTemplate(t.templateId)}
                      style={{ border: 'none', background: 'transparent', color: 'var(--danger)', cursor: 'pointer', fontSize: '1rem' }}
                      title="Delete template"
                    >
                      🗑️
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
