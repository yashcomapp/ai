'use client';

import React from 'react';
import { Exam, Assignment } from './types';
import {
  getExamSortTimestamp,
  getExamClass,
  getExamScheduleStatus,
  isTodayOrTomorrow
} from './examAdminUtils';

export interface TodayTomorrowExamsTableProps {
  exams: Exam[];
  type: 'objective' | 'subjective';
  assignments: Assignment[];
  attemptCounts: { [key: string]: number };
  getAssignedNames: (examId: string, directBatchId?: string | null) => string;
  getLatestAssignmentDate: (examId: string, assignedAt?: string | null, exam?: Exam) => string;
  toggleAssignmentStatus: (assignmentId: string, collection: string, newStatus: string) => void;
  handleOpenAssign: (exam: Exam, type: 'objective' | 'subjective') => void;
  handleOpenEdit: (examId: string, examName: string, collection: string) => void;
  handleDeleteExam: (examId: string, examName: string, type: 'objective' | 'subjective') => void;
  isAlreadyAssigned: (exam: Exam) => boolean;
  router: any;
}

export function TodayTomorrowExamsTable({
  exams,
  type,
  assignments,
  attemptCounts,
  getAssignedNames,
  getLatestAssignmentDate,
  toggleAssignmentStatus,
  handleOpenAssign,
  handleOpenEdit,
  handleDeleteExam,
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

    const classA = parseInt(getExamClass(a)) || 0;
    const classB = parseInt(getExamClass(b)) || 0;
    return classA - classB;
  });

  return (
    <div id={`${type}-today-tomorrow-section`} style={{ marginBottom: '24px' }}>
      <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
        📅 Today's & Tomorrow's {type === 'subjective' ? 'Subjective ' : ''}Exams
      </h3>
      <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
        <div style={{ overflowX: 'auto' }}>
          <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: type === 'subjective' ? '13px' : '12.5px' }}>
            <thead>
              <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: type === 'subjective' ? '12px' : '11.5px' }}>
                <th style={{ padding: '4px 8px' }}>Exam Name</th>
                {type === 'subjective' && (
                  <>
                    <th style={{ padding: '4px 8px' }}>Mode</th>
                    <th style={{ padding: '4px 8px' }}>Peer Review</th>
                  </>
                )}
                <th style={{ padding: '4px 8px' }}>Assigned To</th>
                {type === 'objective' && <th style={{ padding: '4px 8px' }}>Assigned Date</th>}
                <th style={{ padding: '4px 8px' }}>Status / Starts</th>
                <th style={{ padding: '4px 8px', textAlign: 'right' }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {sortedTodayTomorrowExams.length === 0 ? (
                <tr>
                  <td colSpan={type === 'subjective' ? 6 : 5} style={{ padding: '16px', textAlign: 'center', color: 'var(--text-muted)' }}>
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

                  return (
                    <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                      <td style={{ padding: '4px 8px', fontWeight: 600 }}>{exam.name}</td>
                      {type === 'subjective' && (
                        <>
                          <td style={{ padding: '4px 8px' }}>
                            {mode === 'home' ? (
                              <span className="badge badge-info" style={{ fontSize: '10px' }}>🏠 Home</span>
                            ) : (
                              <span className="badge badge-warning" style={{ fontSize: '10px' }}>🏫 Classroom</span>
                            )}
                          </td>
                          <td style={{ padding: '4px 8px', textTransform: 'capitalize', fontSize: '12px' }}>
                            {mode === 'classroom' ? (
                              peerStatus === 'not_started' ? (
                                <span style={{ color: 'var(--warning)' }}>⏳ Waiting</span>
                              ) : peerStatus === 'assigned' ? (
                                <span style={{ color: 'var(--accent)' }}>🔄 In Progress</span>
                              ) : (
                                <span style={{ color: 'var(--success)' }}>✅ Finished</span>
                              )
                            ) : '—'}
                          </td>
                        </>
                      )}
                      <td style={{ padding: '4px 8px', fontSize: '11px', color: 'var(--text-muted)' }}>
                        {getAssignedNames(exam.id, exam.batchId)}
                      </td>
                      {type === 'objective' && (
                        <td style={{ padding: '4px 8px', fontSize: '11px', color: 'var(--text-muted)' }}>
                          {getLatestAssignmentDate(exam.id, exam.assignedAt, exam)}
                        </td>
                      )}
                      <td style={{ padding: '4px 8px' }}>
                        <div style={{ display: 'flex', flexDirection: type === 'subjective' ? 'column' : 'row', gap: type === 'subjective' ? '4px' : '6px', alignItems: type === 'subjective' ? 'flex-start' : 'center' }}>
                          <div style={{ display: 'flex', gap: '6px', flexDirection: 'row', alignItems: 'center' }}>
                            <span style={{ fontSize: '10px', padding: '1px 6px', borderRadius: '10px', background: scheduleStatus.badgeBg, color: scheduleStatus.badgeColor, fontWeight: 700, whiteSpace: 'nowrap' }}>
                              {scheduleStatus.badgeText}
                            </span>
                            {count > 0 && (
                              <span style={{ fontSize: '11px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                                ({count} starts)
                              </span>
                            )}
                          </div>
                          {type === 'subjective' && (
                            <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                              Assigned: {getLatestAssignmentDate(exam.id, exam.assignedAt, exam)}
                            </div>
                          )}
                        </div>
                      </td>
                      <td style={{ padding: '4px 8px', textAlign: 'right' }}>
                        <div style={{ display: 'flex', gap: '4px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                          {activeAssign && activeAssign.openMode !== 'scheduled' && (
                            <button
                              type="button"
                              className={`btn ${rawStatus === 'active' ? 'btn-secondary' : 'btn-primary'}`}
                              style={{ padding: '2px 6px', fontSize: '10.5px', background: rawStatus === 'active' ? 'var(--danger)' : 'var(--success)', color: 'white', border: 'none' }}
                              onClick={() => toggleAssignmentStatus(activeAssign.id, collectionName, rawStatus === 'active' ? 'disabled' : 'active')}
                            >
                              {rawStatus === 'active' ? '🛑 Stop' : '🟢 Start'}
                            </button>
                          )}
                          <button
                            type="button"
                            className="btn btn-secondary"
                            style={{ padding: '2px 6px', fontSize: '10.5px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }}
                            onClick={() => router.push(`/admin/mock-exam?examId=${encodeURIComponent(exam.id)}${type === 'subjective' ? '&type=subjective' : ''}`)}
                          >
                            🧪 Mock Test
                          </button>
                          <button
                            type="button"
                            className="btn btn-primary"
                            style={{ padding: '2px 6px', fontSize: '10.5px' }}
                            onClick={() => handleOpenAssign(exam, type)}
                          >
                            📋 Assign Again
                          </button>
                          {type === 'objective' ? (
                            <button
                              type="button"
                              className="btn btn-secondary"
                              style={{ padding: '2px 6px', fontSize: '10.5px' }}
                              onClick={() => router.push(`/admin/exam-report?examId=${exam.id}`)}
                            >
                              📊 Report
                            </button>
                          ) : (
                            <button
                              type="button"
                              className="btn btn-secondary"
                              style={{ padding: '2px 6px', fontSize: '10.5px' }}
                              onClick={() => router.push(`/admin/teacher-final-review?examId=${exam.id}`)}
                            >
                              Grade
                            </button>
                          )}
                          <button
                            type="button"
                            className="btn btn-secondary"
                            style={{
                              padding: '2px 6px',
                              fontSize: '10.5px',
                              opacity: count > 0 ? 0.5 : 1,
                              cursor: count > 0 ? 'not-allowed' : 'pointer'
                            }}
                            disabled={count > 0}
                            onClick={() => handleOpenEdit(exam.id, exam.name, collectionName)}
                          >
                            ✏️ Edit
                          </button>
                          <button
                            type="button"
                            className="btn btn-secondary"
                            style={{ padding: '2px 6px', fontSize: '10.5px', color: 'var(--danger)' }}
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
