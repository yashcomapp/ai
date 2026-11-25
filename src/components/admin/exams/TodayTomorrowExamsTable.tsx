'use client';

import React from 'react';
import { Exam, Assignment, Batch } from './types';
import {
  getExamSortTimestamp,
  getExamClass,
  getClassBadgeStyle,
  getExamScheduleStatus,
  isTodayOrTomorrow
} from './examAdminUtils';
import { SubjectiveModeBadges } from './SubjectiveModeBadges';

export interface TodayTomorrowExamsTableProps {
  exams: Exam[];
  type: 'objective' | 'subjective';
  assignments: Assignment[];
  batches?: Batch[];
  attemptCounts: { [key: string]: number };
  getAssignedNames: (examId: string, directBatchId?: string | null) => string;
  getLatestAssignmentDate: (examId: string, assignedAt?: string | null, exam?: Exam) => string;
  toggleAssignmentStatus: (assignmentId: string, collection: string, newStatus: string) => void;
  handleOpenAssign: (exam: Exam, type: 'objective' | 'subjective') => void;
  handleOpenEdit: (examId: string, examName: string, collection: string) => void;
  handleDeleteExam: (examId: string, examName: string, type: 'objective' | 'subjective') => void;
  handleOpenExamPaper?: (exam: Exam, type: 'objective' | 'subjective') => void;
  isAlreadyAssigned: (exam: Exam) => boolean;
  router: any;
}

export function TodayTomorrowExamsTable({
  exams,
  type,
  assignments,
  batches,
  attemptCounts,
  getAssignedNames,
  getLatestAssignmentDate,
  toggleAssignmentStatus,
  handleOpenAssign,
  handleOpenEdit,
  handleDeleteExam,
  handleOpenExamPaper,
  isAlreadyAssigned,
  router
}: TodayTomorrowExamsTableProps) {
  const collectionName = type === 'objective' ? 'batchAssignments' : 'subjectiveAssignments';

  const todayTomorrowExams = exams.filter(exam =>
    isAlreadyAssigned(exam) &&
    isTodayOrTomorrow(exam, type, assignments)
  );

  const sortedTodayTomorrowExams = [...todayTomorrowExams].sort((a, b) => {
    const timeA = getExamSortTimestamp(a, type, assignments);
    const timeB = getExamSortTimestamp(b, type, assignments);
    if (timeA !== timeB) return timeA - timeB;

    const classA = parseInt(getExamClass(a, assignments, batches)) || 0;
    const classB = parseInt(getExamClass(b, assignments, batches)) || 0;
    return classA - classB;
  });

  return (
    <div id={`${type}-today-tomorrow-section`} style={{ marginBottom: '24px' }}>
      <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
        📅 Today's & Tomorrow's {type === 'subjective' ? 'Subjective ' : ''}Exams
      </h3>
      <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
        <div className="no-scrollbar" style={{ overflowX: 'auto', WebkitOverflowScrolling: 'touch', scrollbarWidth: 'none', msOverflowStyle: 'none' }}>
          <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: type === 'subjective' ? '12.5px' : '12px', whiteSpace: 'nowrap' }}>
            <thead>
              <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: type === 'subjective' ? '11.5px' : '11px', whiteSpace: 'nowrap' }}>
                <th style={{ padding: '5px 6px', whiteSpace: 'nowrap' }}>Exam Name</th>
                {type === 'subjective' && (
                  <>
                    <th style={{ padding: '5px 6px', whiteSpace: 'nowrap' }}>Mode</th>
                    <th style={{ padding: '5px 6px', whiteSpace: 'nowrap' }}>Peer Review</th>
                  </>
                )}
                <th style={{ padding: '5px 6px', whiteSpace: 'nowrap' }}>Assigned To</th>
                <th style={{ padding: '5px 6px', whiteSpace: 'nowrap' }}>Assigned Date</th>
                <th style={{ padding: '5px 6px', whiteSpace: 'nowrap' }}>Status / Starts</th>
                <th style={{ padding: '5px 6px', textAlign: 'right', whiteSpace: 'nowrap' }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {sortedTodayTomorrowExams.length === 0 ? (
                <tr>
                  <td colSpan={type === 'subjective' ? 7 : 5} style={{ padding: '16px', textAlign: 'center', color: 'var(--text-muted)' }}>
                    No {type === 'subjective' ? 'subjective ' : ''}exams scheduled for today or tomorrow.
                  </td>
                </tr>
              ) : (
                sortedTodayTomorrowExams.map(exam => {
                  const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === collectionName) || assignments.find(a => a.examId === exam.id);
                  const rawStatus = activeAssign?.status || 'active';
                  const scheduleStatus = getExamScheduleStatus(exam, activeAssign, type);
                  const count = attemptCounts[exam.id] || 0;
                  const mode = activeAssign?.examMode || (exam as any).mode || 'home';
                  const peerStatus = (exam as any).peerReviewStatus || 'not_started';
                  const examClass = getExamClass(exam, assignments, batches);
                  const badgeStyle = getClassBadgeStyle(examClass);

                  return (
                    <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)', whiteSpace: 'nowrap', verticalAlign: 'middle' }}>
                      <td style={{ padding: '4px 6px', fontWeight: 600, whiteSpace: 'nowrap' }}>
                        <button
                          type="button"
                          onClick={() => handleOpenExamPaper?.(exam, type)}
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
                      {type === 'subjective' && (
                        <SubjectiveModeBadges mode={mode} peerStatus={peerStatus} />
                      )}
                      <td style={{ padding: '4px 6px', fontSize: '11px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                        {getAssignedNames(exam.id, exam.batchId)}
                      </td>
                      <td style={{ padding: '4px 6px', fontSize: '11px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                        {getLatestAssignmentDate(exam.id, exam.assignedAt, exam)}
                      </td>
                      <td style={{ padding: '4px 6px', whiteSpace: 'nowrap' }}>
                        <div style={{ display: 'flex', gap: '5px', flexDirection: 'row', alignItems: 'center', whiteSpace: 'nowrap' }}>
                          <span style={{ fontSize: '10px', padding: '1px 6px', borderRadius: '10px', background: scheduleStatus.badgeBg, color: scheduleStatus.badgeColor, fontWeight: 700, whiteSpace: 'nowrap' }}>
                            {scheduleStatus.badgeText}
                          </span>
                          {count > 0 && (
                            <span style={{ fontSize: '10.5px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                              ({count} starts)
                            </span>
                          )}
                        </div>
                      </td>
                      <td style={{ padding: '4px 6px', textAlign: 'right', whiteSpace: 'nowrap' }}>
                        <div style={{ display: 'flex', gap: '3px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                          {activeAssign && (activeAssign.openMode !== 'scheduled' || rawStatus === 'disabled') && (
                            <button
                              type="button"
                              className={`btn ${rawStatus === 'active' ? 'btn-secondary' : 'btn-primary'}`}
                              style={{ padding: '2px 5px', fontSize: '10.5px', background: rawStatus === 'active' ? 'var(--danger)' : 'var(--success)', color: 'white', border: 'none', whiteSpace: 'nowrap' }}
                              onClick={() => toggleAssignmentStatus(activeAssign.id, collectionName, rawStatus === 'active' ? 'disabled' : 'active')}
                            >
                              {rawStatus === 'active' ? '🛑 Stop' : '🟢 Start'}
                            </button>
                          )}
                          <button
                            type="button"
                            className="btn btn-secondary"
                            style={{ padding: '2px 5px', fontSize: '10.5px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600, whiteSpace: 'nowrap' }}
                            onClick={() => router.push(`/admin/mock-exam?examId=${encodeURIComponent(exam.id)}${type === 'subjective' ? '&type=subjective' : ''}`)}
                          >
                            🧪 Mock Test
                          </button>
                          <button
                            type="button"
                            className="btn btn-primary"
                            style={{ padding: '2px 5px', fontSize: '10.5px', whiteSpace: 'nowrap' }}
                            onClick={() => handleOpenAssign(exam, type)}
                          >
                            📋 Re-Assign
                          </button>
                          {type === 'objective' ? (
                            <button
                              type="button"
                              className="btn btn-secondary"
                              style={{ padding: '2px 5px', fontSize: '10.5px', whiteSpace: 'nowrap' }}
                              onClick={() => router.push(`/admin/exam-report?examId=${exam.id}`)}
                            >
                              📊 Report
                            </button>
                          ) : (
                            <button
                              type="button"
                              className="btn btn-secondary"
                              style={{ padding: '2px 5px', fontSize: '10.5px', whiteSpace: 'nowrap' }}
                              onClick={() => router.push(`/admin/teacher-final-review?examId=${exam.id}`)}
                            >
                              Grade
                            </button>
                          )}
                          <button
                            type="button"
                            className="btn btn-secondary"
                            style={{
                              padding: '2px 5px',
                              fontSize: '10.5px',
                              opacity: count > 0 ? 0.5 : 1,
                              cursor: count > 0 ? 'not-allowed' : 'pointer',
                              whiteSpace: 'nowrap'
                            }}
                            disabled={count > 0}
                            onClick={() => handleOpenEdit(exam.id, exam.name, collectionName)}
                          >
                            ✏️ Edit
                          </button>
                          <button
                            type="button"
                            className="btn btn-secondary"
                            style={{ padding: '2px 5px', fontSize: '10.5px', color: 'var(--danger)', whiteSpace: 'nowrap' }}
                            onClick={() => handleDeleteExam(exam.id, exam.name, type)}
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
