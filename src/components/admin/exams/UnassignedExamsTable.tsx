'use client';

import React from 'react';
import type { Exam } from '@/types/exam.types';

interface UnassignedExamsTableProps {
  exams: Exam[];
  type: 'objective' | 'subjective';
  onAssign: (exam: Exam, type: 'objective' | 'subjective') => void;
  onDelete: (id: string, name: string, type: 'objective' | 'subjective') => void;
  onMockExam?: (examId: string) => void;
}

export function UnassignedExamsTable({
  exams,
  type,
  onAssign,
  onDelete,
  onMockExam,
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
        <div style={{ overflowX: 'auto' }}>
          <table
            className="reviews-table"
            style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '12.5px' }}
          >
            <thead>
              <tr
                style={{
                  background: 'var(--bg-soft)',
                  borderBottom: '1px solid var(--border-light)',
                  color: 'var(--text-muted)',
                  fontSize: '11.5px',
                }}
              >
                <th style={{ padding: '4px 8px' }}>Exam Name</th>
                <th style={{ padding: '4px 8px' }}>Subject</th>
                <th style={{ padding: '4px 8px' }}>Topics</th>
                <th style={{ padding: '4px 8px' }}>Questions</th>
                <th style={{ padding: '4px 8px' }}>Marks</th>
                <th style={{ padding: '4px 8px', textAlign: 'right' }}>Actions</th>
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
                exams.map((exam) => (
                  <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                    <td style={{ padding: '4px 8px', fontWeight: 600 }}>{exam.name}</td>
                    <td style={{ padding: '4px 8px' }}>{exam.subjectName || exam.subjects?.[0] || '—'}</td>
                    <td style={{ padding: '4px 8px' }}>{(exam.topicCodes || []).join(', ') || '—'}</td>
                    <td style={{ padding: '4px 8px' }}>{exam.questionCount || exam.questions?.length || 0}</td>
                    <td style={{ padding: '4px 8px' }}>{exam.totalMarks || 0}</td>
                    <td style={{ padding: '4px 8px', textAlign: 'right' }}>
                      <div style={{ display: 'flex', gap: '4px', justifyContent: 'flex-end' }}>
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
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
