'use client';

import React from 'react';
import type { Exam } from '@/types/exam.types';
import { getExamClass, getClassBadgeStyle } from './examAdminUtils';

interface UnassignedExamsTableProps {
  exams: Exam[];
  type: 'objective' | 'subjective';
  onAssign: (exam: Exam, type: 'objective' | 'subjective') => void;
  onDelete: (id: string, name: string, type: 'objective' | 'subjective') => void;
  onMockExam?: (examId: string) => void;
  onOpenExamPaper?: (exam: Exam, type: 'objective' | 'subjective') => void;
}

export function UnassignedExamsTable({
  exams,
  type,
  onAssign,
  onDelete,
  onMockExam,
  onOpenExamPaper,
}: UnassignedExamsTableProps) {
  const isSubjective = type === 'subjective';
  const sectionId = isSubjective ? 'subjective-templates-section' : 'objective-templates-section';
  const title = isSubjective
    ? '📋 Subjective Exams Available for Assignment'
    : '📋 Exams Available for Assignment';
  const emptyMessage = isSubjective
    ? 'No subjective exams available for assignment.'
    : 'No exams available for assignment.';

  return (
    <div id={sectionId} style={{ marginBottom: '24px' }}>
      <h3
        style={{
          fontSize: '14px',
          fontWeight: 800,
          color: 'var(--text)',
          marginBottom: '10px',
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
        }}
      >
        {title}
      </h3>
      <div
        className="card"
        style={{
          background: 'var(--surface)',
          borderRadius: 'var(--radius-lg)',
          border: '1px solid var(--border-light)',
          overflow: 'hidden',
        }}
      >
        <div className="no-scrollbar" style={{ overflowX: 'auto', WebkitOverflowScrolling: 'touch', scrollbarWidth: 'none', msOverflowStyle: 'none' }}>
          <table
            className="reviews-table"
            style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '12px', whiteSpace: 'nowrap' }}
          >
            <thead>
              <tr
                style={{
                  background: 'var(--bg-soft)',
                  borderBottom: '1px solid var(--border-light)',
                  color: 'var(--text-muted)',
                  fontSize: '11.5px',
                  whiteSpace: 'nowrap'
                }}
              >
                <th style={{ padding: '5px 6px', whiteSpace: 'nowrap' }}>Exam Name</th>
                <th style={{ padding: '5px 6px', whiteSpace: 'nowrap' }}>Subject</th>
                <th style={{ padding: '5px 6px', whiteSpace: 'nowrap' }}>Topics</th>
                <th style={{ padding: '5px 6px', whiteSpace: 'nowrap' }}>Questions</th>
                <th style={{ padding: '5px 6px', whiteSpace: 'nowrap' }}>Marks</th>
                <th style={{ padding: '5px 6px', textAlign: 'right', whiteSpace: 'nowrap' }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {exams.length === 0 ? (
                <tr>
                  <td colSpan={6} style={{ padding: '12px', textAlign: 'center', color: 'var(--text-muted)' }}>
                    {emptyMessage}
                  </td>
                </tr>
              ) : (
                exams.map((exam) => {
                  const examClass = getExamClass(exam);
                  const badgeStyle = getClassBadgeStyle(examClass);

                  return (
                    <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)', whiteSpace: 'nowrap', verticalAlign: 'middle' }}>
                      <td style={{ padding: '4px 6px', fontWeight: 600, whiteSpace: 'nowrap' }}>
                        <button
                          type="button"
                          onClick={() => onOpenExamPaper?.(exam, type)}
                          style={{
                            background: 'none',
                            border: 'none',
                            padding: 0,
                            fontWeight: 600,
                            color: 'var(--primary, #3b82f6)',
                            cursor: 'pointer',
                            textAlign: 'left',
                            textDecoration: 'none',
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '6px',
                            whiteSpace: 'nowrap'
                          }}
                          title="Click to view exam paper questions and answer keys"
                        >
                          <span
                            style={{
                              display: 'inline-flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                              width: '22px',
                              height: '22px',
                              minWidth: '22px',
                              borderRadius: '5px',
                              background: badgeStyle.bg,
                              color: badgeStyle.color,
                              border: `1px solid ${badgeStyle.border}`,
                              fontWeight: 900,
                              fontSize: examClass.length > 2 ? '10.5px' : '12px',
                              lineHeight: 1,
                              flexShrink: 0,
                              userSelect: 'none'
                            }}
                            title={`Class ${examClass}`}
                          >
                            {examClass !== 'General' ? examClass : '—'}
                          </span>
                          <span style={{ whiteSpace: 'nowrap' }}>{exam.name}</span>
                        </button>
                      </td>
                      <td style={{ padding: '4px 6px', whiteSpace: 'nowrap' }}>{exam.subjectName || exam.subjects?.[0] || '—'}</td>
                      <td style={{ padding: '4px 6px', whiteSpace: 'nowrap' }}>{(exam.topicCodes || []).join(', ') || '—'}</td>
                      <td style={{ padding: '4px 6px', whiteSpace: 'nowrap' }}>{exam.questionCount || exam.questions?.length || 0}</td>
                      <td style={{ padding: '4px 6px', whiteSpace: 'nowrap' }}>{exam.totalMarks || 0}</td>
                      <td style={{ padding: '4px 6px', textAlign: 'right', whiteSpace: 'nowrap' }}>
                        <div style={{ display: 'flex', gap: '4px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                        {onMockExam && (
                          <button
                            className="btn btn-secondary"
                            style={{
                              padding: '2px 6px',
                              fontSize: '10.5px',
                              background: 'var(--accent-tint)',
                              color: 'var(--accent)',
                              fontWeight: 600,
                            }}
                            onClick={() => onMockExam(exam.id)}
                          >
                            🧪 Mock Test
                          </button>
                        )}
                        <button
                          className="btn btn-primary"
                          style={{ padding: '2px 6px', fontSize: '10.5px' }}
                          onClick={() => onAssign(exam, type)}
                        >
                          📋 Assign
                        </button>
                        <button
                          className="btn btn-secondary"
                          style={{ padding: '2px 6px', fontSize: '10.5px', color: 'var(--danger)' }}
                          onClick={() => onDelete(exam.id, exam.name, type)}
                        >
                          🗑️ Delete
                        </button>
                      </div>
                    </td>
                  </tr>
                );
              })
            )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
