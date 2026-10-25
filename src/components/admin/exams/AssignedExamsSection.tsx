'use client';

import React from 'react';
import { Exam, Assignment, ExamScheduleStatus, AssignedExamsSectionProps } from './types';
import { SubjectiveModeBadges } from './SubjectiveModeBadges';

export type { AssignedExamsSectionProps };

export function AssignedExamsSection({
  assignedExamsList,
  type,
  assignments,
  attemptCounts,
  isAssignedSectionExpanded = false,
  setIsAssignedSectionExpanded,
  expandedClasses,
  toggleClassExpanded,
  expandedSubjects,
  toggleSubjectExpanded,
  expandedChapters,
  toggleChapterExpanded,
  expandAllAssigned,
  collapseAllAssigned,
  assignedSortField,
  assignedSortDir,
  handleAssignedSort,
  sortAssignedExams,
  getGroupedClasses,
  getExamClass,
  getExamSubject,
  getExamChapter,
  getAssignedNames,
  getLatestAssignmentDate,
  getExamScheduleStatus,
  toggleAssignmentStatus,
  handleOpenAssign,
  handleOpenEdit,
  handleDeleteExam,
  triggerPeerReviewLottery,
  openPeerReviewStatus,
  openTruthTestReport,
  router
}: AssignedExamsSectionProps) {
  const collectionName = type === 'objective' ? 'batchAssignments' : 'subjectiveAssignments';

  return (
    <div id={`${type}-assignments-section`}>
      <div 
        onClick={() => setIsAssignedSectionExpanded?.(prev => !prev)}
        style={{ 
          display: 'flex', 
          alignItems: 'center', 
          justifyContent: 'space-between',
          padding: '12px 16px',
          background: 'var(--bg-soft)',
          border: '1px solid var(--border-light)',
          borderRadius: 'var(--radius-md)',
          marginBottom: isAssignedSectionExpanded ? '12px' : '0px',
          cursor: 'pointer',
          userSelect: 'none',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', margin: 0, display: 'flex', alignItems: 'center', gap: '6px' }}>
            📚 Exams Already Assigned
          </h3>
          <span style={{ fontSize: '12px', fontWeight: 700, padding: '2px 8px', borderRadius: '12px', background: 'var(--accent-tint)', color: 'var(--accent)' }}>
            {assignedExamsList.length} exams
          </span>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          {isAssignedSectionExpanded && (
            <div style={{ display: 'flex', gap: '6px' }} onClick={e => e.stopPropagation()}>
              <button
                type="button"
                className="btn btn-secondary"
                style={{ padding: '3px 8px', fontSize: '11px', fontWeight: 600 }}
                onClick={() => expandAllAssigned?.(type, assignedExamsList)}
                title="Expand all classes, subjects, and chapters"
              >
                ⊞ Expand All
              </button>
              <button
                type="button"
                className="btn btn-secondary"
                style={{ padding: '3px 8px', fontSize: '11px', fontWeight: 600 }}
                onClick={() => collapseAllAssigned?.(type)}
                title="Collapse all classes, subjects, and chapters"
              >
                ⊟ Collapse All
              </button>
            </div>
          )}
          <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '4px' }}>
            {isAssignedSectionExpanded ? 'Click to Collapse ▲' : 'Click to Expand ▼'}
          </span>
        </div>
      </div>

      {isAssignedSectionExpanded && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          {assignedExamsList.length === 0 ? (
            <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '30px', textAlign: 'center', color: 'var(--text-muted)' }}>
              No assigned exams found.
            </div>
          ) : (
            (() => {
              const classes = getGroupedClasses(assignedExamsList);
              return classes.map(cls => {
                const examsInClass = assignedExamsList.filter(exam => getExamClass(exam) === cls);
                const sortedExams = sortAssignedExams(examsInClass);
                const isExpanded = expandedClasses.has(`${type}||${cls}`);
                
                return (
                  <div key={cls} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', background: 'var(--surface)', overflow: 'hidden' }}>
                    <div 
                      onClick={() => toggleClassExpanded(`${type}||${cls}`)}
                      style={{ padding: '10px 14px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isExpanded ? '1px solid var(--border-light)' : 'none' }}
                    >
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <span style={{ fontWeight: 'bold', fontSize: '13px', color: 'var(--accent)' }}>🏫 Class {cls}</span>
                        <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>({examsInClass.length} exams)</span>
                      </div>
                      <span style={{ fontSize: '10px', transition: 'transform 0.2s', transform: isExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                    </div>
                    
                    {isExpanded && (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', padding: '8px' }}>
                        {(() => {
                          const subjectGroups = new Map<string, Exam[]>();
                          sortedExams.forEach(exam => {
                            const subj = getExamSubject(exam);
                            if (!subjectGroups.has(subj)) subjectGroups.set(subj, []);
                            subjectGroups.get(subj)!.push(exam);
                          });

                          return Array.from(subjectGroups.entries()).map(([subjName, subjExams]) => {
                            const subjKey = `subj||${type}||${cls}||${subjName}`;
                            const isSubjExpanded = expandedSubjects.has(subjKey);

                            const chapterGroups = new Map<string, Exam[]>();
                            subjExams.forEach(exam => {
                              const chap = getExamChapter(exam);
                              if (!chapterGroups.has(chap)) chapterGroups.set(chap, []);
                              chapterGroups.get(chap)!.push(exam);
                            });

                            return (
                              <div key={subjKey} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-md)', background: 'var(--surface)', overflow: 'hidden' }}>
                                <div 
                                  onClick={() => toggleSubjectExpanded(subjKey)}
                                  style={{ padding: '6px 10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isSubjExpanded ? '1px solid var(--border-light)' : 'none' }}
                                >
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <span style={{ fontWeight: 700, fontSize: '12px', color: 'var(--text)' }}>📚 {subjName}</span>
                                    <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>({subjExams.length} {subjExams.length === 1 ? 'exam' : 'exams'})</span>
                                  </div>
                                  <span style={{ fontSize: '9px', transition: 'transform 0.2s', transform: isSubjExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                                </div>

                                {isSubjExpanded && (
                                  <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', padding: '6px' }}>
                                    {Array.from(chapterGroups.entries()).map(([chapName, chapExams]) => {
                                      const chapKey = `chap||${type}||${cls}||${subjName}||${chapName}`;
                                      const isChapExpanded = expandedChapters.has(chapKey);

                                      return (
                                        <div key={chapKey} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', overflow: 'hidden' }}>
                                          <div 
                                            onClick={() => toggleChapterExpanded(chapKey)}
                                            style={{ padding: '4px 8px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isChapExpanded ? '1px solid var(--border-light)' : 'none' }}
                                          >
                                            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                              <span style={{ fontWeight: 700, fontSize: '11.5px', color: 'var(--accent)' }}>📘 {chapName}</span>
                                              <span style={{ fontSize: '10.5px', color: 'var(--text-muted)' }}>({chapExams.length} {chapExams.length === 1 ? 'exam' : 'exams'})</span>
                                            </div>
                                            <span style={{ fontSize: '9px', transition: 'transform 0.2s', transform: isChapExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                                          </div>

                                          {isChapExpanded && (
                                            <div style={{ overflowX: 'auto' }}>
                                              <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: type === 'subjective' ? '13px' : '12.5px' }}>
                                                <thead>
                                                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: type === 'subjective' ? '12px' : '11.5px' }}>
                                                    <th style={{ padding: '4px 8px', cursor: 'pointer', userSelect: 'none' }} onClick={() => handleAssignedSort('name')}>
                                                      Exam Name {assignedSortField === 'name' ? (assignedSortDir === 'asc' ? '🔼' : '🔽') : ''}
                                                    </th>
                                                    {type === 'subjective' && (
                                                      <>
                                                        <th style={{ padding: '4px 8px' }}>Mode</th>
                                                        <th style={{ padding: '4px 8px' }}>Peer Review</th>
                                                      </>
                                                    )}
                                                    <th style={{ padding: '4px 8px' }}>Assigned To</th>
                                                    <th style={{ padding: '4px 8px', cursor: 'pointer', userSelect: 'none' }} onClick={() => handleAssignedSort('date')}>
                                                      {type === 'subjective' ? 'Status / Starts' : 'Assigned Date'} {assignedSortField === 'date' ? (assignedSortDir === 'asc' ? '🔼' : '🔽') : ''}
                                                    </th>
                                                    {type === 'objective' && <th style={{ padding: '4px 8px' }}>Status / Starts</th>}
                                                    <th style={{ padding: '4px 8px', textAlign: 'right' }}>Actions</th>
                                                  </tr>
                                                </thead>
                                                <tbody>
                                                  {chapExams.map(exam => {
                                                    const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === collectionName);
                                                    const rawStatus = activeAssign?.status || 'active';
                                                    const scheduleStatus = getExamScheduleStatus(exam, activeAssign, type);
                                                    const mode = activeAssign?.examMode || (exam as any).mode || 'home';
                                                    const peerStatus = (exam as any).peerReviewStatus || 'not_started';
                                                    const count = attemptCounts[exam.id] || 0;

                                                    return (
                                                      <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                                                        <td style={{ padding: '4px 8px', fontWeight: 600 }}>{exam.name}</td>
                                                        {type === 'subjective' && (
                                                          <SubjectiveModeBadges mode={mode} peerStatus={peerStatus} />
                                                        )}
                                                        <td style={{ padding: '4px 8px', fontSize: '11px', color: 'var(--text-muted)' }}>
                                                          {getAssignedNames(exam.id, exam.batchId)}
                                                        </td>
                                                        <td style={{ padding: '4px 8px', fontSize: '11px', color: 'var(--text-muted)' }}>
                                                          {type === 'subjective' ? (
                                                            <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                                                              <div style={{ display: 'flex', gap: '6px', flexDirection: 'row', alignItems: 'center' }}>
                                                                <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: scheduleStatus.badgeBg, color: scheduleStatus.badgeColor, fontWeight: 700, whiteSpace: 'nowrap' }}>
                                                                  {scheduleStatus.badgeText}
                                                                </span>
                                                                {count > 0 && (
                                                                  <span style={{ fontSize: '11px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                                                                    ({count} starts)
                                                                  </span>
                                                                )}
                                                              </div>
                                                              <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                                                                Assigned: {getLatestAssignmentDate(exam.id, exam.assignedAt, exam)}
                                                              </div>
                                                            </div>
                                                          ) : (
                                                            getLatestAssignmentDate(exam.id, exam.assignedAt, exam)
                                                          )}
                                                        </td>
                                                        {type === 'objective' && (
                                                          <td style={{ padding: '4px 8px' }}>
                                                            <div style={{ display: 'flex', gap: '6px', flexDirection: 'row', alignItems: 'center' }}>
                                                              <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: scheduleStatus.badgeBg, color: scheduleStatus.badgeColor, fontWeight: 700, whiteSpace: 'nowrap' }}>
                                                                {scheduleStatus.badgeText}
                                                              </span>
                                                              {count > 0 && (
                                                                <span style={{ fontSize: '11px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                                                                  ({count} starts)
                                                                </span>
                                                              )}
                                                            </div>
                                                          </td>
                                                        )}
                                                        <td style={{ padding: '4px 8px', textAlign: 'right' }}>
                                                          <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                                                            {activeAssign && activeAssign.openMode !== 'scheduled' && (
                                                              <button 
                                                                type="button"
                                                                className={`btn ${rawStatus === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                                                style={{ padding: '3px 8px', fontSize: '10.5px', background: rawStatus === 'active' ? 'var(--danger)' : 'var(--success)', color: 'white', border: 'none' }} 
                                                                onClick={() => toggleAssignmentStatus(activeAssign.id, collectionName, rawStatus === 'active' ? 'disabled' : 'active')}
                                                              >
                                                                {rawStatus === 'active' ? '🛑 Stop' : '🟢 Start'}
                                                              </button>
                                                            )}
                                                            <button 
                                                              type="button"
                                                              className="btn btn-secondary" 
                                                              style={{ padding: '3px 8px', fontSize: '10.5px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} 
                                                              onClick={() => router.push(`/admin/mock-exam?examId=${encodeURIComponent(exam.id)}${type === 'subjective' ? '&type=subjective' : ''}`)}
                                                            >
                                                              🧪 Mock Test
                                                            </button>
                                                            <button 
                                                              type="button"
                                                              className="btn btn-primary" 
                                                              style={{ padding: '3px 8px', fontSize: '10.5px' }} 
                                                              onClick={() => handleOpenAssign(exam, type)}
                                                            >
                                                              📋 Assign Again
                                                            </button>
                                                            {type === 'objective' ? (
                                                              <button 
                                                                type="button"
                                                                className="btn btn-secondary" 
                                                                style={{ padding: '3px 8px', fontSize: '11px' }} 
                                                                onClick={() => router.push(`/admin/exam-report?examId=${encodeURIComponent(exam.id)}`)}
                                                              >
                                                                📊 Report
                                                              </button>
                                                            ) : (
                                                              <button 
                                                                type="button"
                                                                className="btn btn-secondary" 
                                                                style={{ padding: '3px 8px', fontSize: '10.5px' }} 
                                                                onClick={() => router.push(`/admin/teacher-final-review?examId=${exam.id}`)}
                                                              >
                                                                Grade
                                                              </button>
                                                            )}
                                                            {type === 'subjective' && mode === 'classroom' && (
                                                              <>
                                                                {peerStatus === 'not_started' && triggerPeerReviewLottery && (
                                                                  <button 
                                                                    type="button"
                                                                    className="btn btn-primary" 
                                                                    style={{ padding: '3px 8px', fontSize: '10.5px', background: 'var(--warning)', borderColor: 'var(--warning)' }} 
                                                                    onClick={() => triggerPeerReviewLottery(exam.id, exam.name)}
                                                                  >
                                                                    🎲 Lottery
                                                                  </button>
                                                                )}
                                                                {peerStatus === 'assigned' && openPeerReviewStatus && (
                                                                  <button 
                                                                    type="button"
                                                                    className="btn btn-secondary" 
                                                                    style={{ padding: '3px 8px', fontSize: '10.5px' }} 
                                                                    onClick={() => openPeerReviewStatus(exam.id, exam.name)}
                                                                  >
                                                                    📊 Status
                                                                  </button>
                                                                )}
                                                                {openTruthTestReport && (
                                                                  <button 
                                                                    type="button"
                                                                    className="btn btn-secondary" 
                                                                    style={{ padding: '3px 8px', fontSize: '10.5px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} 
                                                                    onClick={() => openTruthTestReport(exam.id, exam.name)}
                                                                  >
                                                                    ⚖️ Truth Test
                                                                  </button>
                                                                )}
                                                              </>
                                                            )}
                                                            <button 
                                                              type="button"
                                                              className="btn btn-secondary" 
                                                              style={{ 
                                                                padding: '3px 8px', 
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
                                                              style={{ padding: '3px 8px', fontSize: '10.5px', color: 'var(--danger)' }} 
                                                              onClick={() => handleDeleteExam(exam.id, exam.name, type)}
                                                            >
                                                              🗑️ Delete
                                                            </button>
                                                          </div>
                                                        </td>
                                                      </tr>
                                                    );
                                                  })}
                                                </tbody>
                                              </table>
                                            </div>
                                          )}
                                        </div>
                                      );
                                    })}
                                  </div>
                                )}
                              </div>
                            );
                          });
                        })()}
                      </div>
                    )}
                  </div>
                );
              });
            })()
          )}
        </div>
      )}
    </div>
  );
}
