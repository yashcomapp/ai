'use client';

import React from 'react';
import { Exam, Assignment, ExamScheduleStatus } from './types';

interface SubjectiveTabProps {
  filteredSubjectiveExams: Exam[];
  assignments: Assignment[];
  attemptCounts: { [key: string]: number };
  subjFilterName: string;
  setSubjFilterName: (val: string) => void;
  subjFilterTopic: string;
  setSubjFilterTopic: (val: string) => void;
  isSubjectiveAvailableForAssignment: (exam: Exam) => boolean;
  isSubjectiveAlreadyAssigned: (exam: Exam) => boolean;
  isTodayOrTomorrow: (exam: Exam, type: 'objective' | 'subjective') => boolean;
  getExamSortTimestamp: (exam: Exam, type: 'objective' | 'subjective') => number;
  getExamClass: (exam: any) => string;
  getExamSubject: (exam: any) => string;
  getExamChapter: (exam: any) => string;
  getAssignedNames: (examId: string, directBatchId?: string | null) => string;
  getLatestAssignmentDate: (examId: string, assignedAt?: string | null, exam?: Exam) => string;
  getExamScheduleStatus: (exam: Exam, activeAssign?: Assignment, examType?: 'objective' | 'subjective') => ExamScheduleStatus;
  isAssignedSectionExpanded?: boolean;
  setIsAssignedSectionExpanded?: React.Dispatch<React.SetStateAction<boolean>>;
  expandedClasses: Set<string>;
  toggleClassExpanded: (clsKey: string) => void;
  expandedSubjects: Set<string>;
  toggleSubjectExpanded: (key: string) => void;
  expandedChapters: Set<string>;
  toggleChapterExpanded: (key: string) => void;
  expandAllAssigned?: (type: 'objective' | 'subjective', list: Exam[]) => void;
  collapseAllAssigned?: (type: 'objective' | 'subjective') => void;
  assignedSortField: 'name' | 'date';
  assignedSortDir: 'asc' | 'desc';
  handleAssignedSort: (field: 'name' | 'date') => void;
  sortAssignedExams: (examsList: Exam[]) => Exam[];
  getGroupedClasses: (examsList: Exam[]) => string[];
  handleOpenAssign: (exam: Exam, type: 'objective' | 'subjective') => void;
  handleDeleteExam: (examId: string, examName: string, type: 'objective' | 'subjective') => void;
  toggleAssignmentStatus: (assignmentId: string, collection: string, newStatus: string) => void;
  exportUniversalExamPDF: (exam: any, questions: any[]) => void;
  handleOpenEdit: (examId: string, examName: string, collection: string) => void;
  triggerPeerReviewLottery: (examId: string, examName: string) => void;
  openPeerReviewStatus: (examId: string, examName: string) => void;
  openTruthTestReport: (examId: string, examName: string) => void;
  router: any;
}

export default function SubjectiveTab({
  filteredSubjectiveExams,
  assignments,
  attemptCounts,
  subjFilterName,
  setSubjFilterName,
  subjFilterTopic,
  setSubjFilterTopic,
  isSubjectiveAvailableForAssignment,
  isSubjectiveAlreadyAssigned,
  isTodayOrTomorrow,
  getExamSortTimestamp,
  getExamClass,
  getExamSubject,
  getExamChapter,
  getAssignedNames,
  getLatestAssignmentDate,
  getExamScheduleStatus,
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
  handleOpenAssign,
  handleDeleteExam,
  toggleAssignmentStatus,
  exportUniversalExamPDF,
  handleOpenEdit,
  triggerPeerReviewLottery,
  openPeerReviewStatus,
  openTruthTestReport,
  router
}: SubjectiveTabProps) {
  return (
    <div>
      <div className="filter-row" style={{ display: 'flex', gap: '10px', marginBottom: '16px', flexWrap: 'wrap' }}>
        <input 
          type="text" 
          value={subjFilterName}
          placeholder="🔍 Filter by exam name..." 
          onChange={(e) => setSubjFilterName(e.target.value)}
          style={{ flex: 1, minWidth: '220px', padding: '8px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
        />
        <input 
          type="text" 
          value={subjFilterTopic}
          placeholder="🔍 Filter by topic code..." 
          onChange={(e) => setSubjFilterTopic(e.target.value)}
          style={{ flex: 1, minWidth: '220px', padding: '8px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
        />
        <button 
          className="btn btn-secondary" 
          onClick={() => { setSubjFilterName(''); setSubjFilterTopic(''); }}
        >
          Clear
        </button>
      </div>

      {/* Section 1: Available for Assignment */}
      <div id="subjective-templates-section" style={{ marginBottom: '24px' }}>
        <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
          📋 Subjective Exams Available for Assignment
        </h3>
        <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
          <div style={{ overflowX: 'auto' }}>
            <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
              <thead>
                <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                  <th style={{ padding: '4px 8px' }}>Exam Name</th>
                  <th style={{ padding: '4px 8px' }}>Subject</th>
                  <th style={{ padding: '4px 8px' }}>Topics</th>
                  <th style={{ padding: '4px 8px' }}>Mode</th>
                  <th style={{ padding: '4px 8px' }}>Marks</th>
                  <th style={{ padding: '4px 8px', textAlign: 'right' }}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {filteredSubjectiveExams.filter(isSubjectiveAvailableForAssignment).length === 0 ? (
                  <tr>
                    <td colSpan={6} style={{ padding: '16px', textAlign: 'center', color: 'var(--text-muted)' }}>No subjective exams available for assignment.</td>
                  </tr>
                ) : (
                  filteredSubjectiveExams
                    .filter(isSubjectiveAvailableForAssignment)
                    .map(exam => (
                      <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '4px 8px', fontWeight: 600 }}>{exam.name}</td>
                        <td style={{ padding: '4px 8px' }}>{exam.subjectName || exam.subjects?.[0] || '—'}</td>
                        <td style={{ padding: '4px 8px' }}>{(exam.topicCodes || []).join(', ') || '—'}</td>
                        <td style={{ padding: '4px 8px' }}>
                          <span className="badge badge-info" style={{ fontSize: '10px' }}>🏠 Home</span>
                        </td>
                        <td style={{ padding: '4px 8px' }}>{exam.totalMarks || 0}</td>
                        <td style={{ padding: '4px 8px', textAlign: 'right' }}>
                          <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end' }}>
                            <button className="btn btn-primary" style={{ padding: '3px 8px', fontSize: '10.5px' }} onClick={() => handleOpenAssign(exam, 'subjective')}>
                              📋 Assign
                            </button>
                            <button className="btn btn-secondary" style={{ padding: '3px 8px', fontSize: '10.5px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'subjective')}>
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

      {/* Section 1b: Today's & Tomorrow's Subjective Exams */}
      <div id="subjective-today-tomorrow-section" style={{ marginBottom: '24px' }}>
        <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
          📅 Today's & Tomorrow's Subjective Exams
        </h3>
        <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
          <div style={{ overflowX: 'auto' }}>
            <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
              <thead>
                <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                  <th style={{ padding: '4px 8px' }}>Exam Name</th>
                  <th style={{ padding: '4px 8px' }}>Mode</th>
                  <th style={{ padding: '4px 8px' }}>Peer Review</th>
                  <th style={{ padding: '4px 8px' }}>Assigned To</th>
                  <th style={{ padding: '4px 8px' }}>Status / Starts</th>
                  <th style={{ padding: '4px 8px', textAlign: 'right' }}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {(() => {
                  const todayTomorrowExams = filteredSubjectiveExams.filter(exam => 
                    isSubjectiveAlreadyAssigned(exam) &&
                    isTodayOrTomorrow(exam, 'subjective')
                  );
                  
                  const sortedTodayTomorrowExams = [...todayTomorrowExams].sort((a, b) => {
                    const timeA = getExamSortTimestamp(a, 'subjective');
                    const timeB = getExamSortTimestamp(b, 'subjective');
                    if (timeA !== timeB) return timeA - timeB;
                    
                    const classA = parseInt(getExamClass(a)) || 0;
                    const classB = parseInt(getExamClass(b)) || 0;
                    return classA - classB;
                  });

                  if (sortedTodayTomorrowExams.length === 0) {
                    return (
                      <tr>
                        <td colSpan={6} style={{ padding: '16px', textAlign: 'center', color: 'var(--text-muted)' }}>No subjective exams scheduled for today or tomorrow.</td>
                      </tr>
                    );
                  }
                  
                  return sortedTodayTomorrowExams.map(exam => {
                    const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === 'subjectiveAssignments') || assignments.find(a => a.examId === exam.id);
                    const rawStatus = activeAssign?.status || 'active';
                    const scheduleStatus = getExamScheduleStatus(exam, activeAssign, 'subjective');
                    const mode = activeAssign?.examMode || exam.mode || 'home';
                    const peerStatus = exam.peerReviewStatus || 'not_started';
                    const count = attemptCounts[exam.id] || 0;
                    return (
                      <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '4px 8px', fontWeight: 600 }}>
                          {exam.name}
                        </td>
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
                        <td style={{ padding: '4px 8px', fontSize: '11px', color: 'var(--text-muted)' }}>{getAssignedNames(exam.id, exam.batchId)}</td>
                        <td style={{ padding: '4px 8px' }}>
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
                        </td>
                        <td style={{ padding: '4px 8px', textAlign: 'right' }}>
                          <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                            {activeAssign && activeAssign.openMode !== 'scheduled' && (
                              <button 
                                className={`btn ${rawStatus === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                style={{ padding: '3px 8px', fontSize: '10.5px', background: rawStatus === 'active' ? 'var(--danger)' : 'var(--success)', color: 'white', border: 'none' }} 
                                onClick={() => toggleAssignmentStatus(activeAssign.id, 'subjectiveAssignments', rawStatus === 'active' ? 'disabled' : 'active')}
                              >
                                {rawStatus === 'active' ? '🛑 Stop' : '🟢 Start'}
                              </button>
                            )}
                            <button className="btn btn-secondary" style={{ padding: '3px 8px', fontSize: '10.5px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} onClick={() => exportUniversalExamPDF(exam, exam.questions || (exam as any).questionDetails || (exam as any).questionCodes || (exam as any).questionIds || [])}>
                              📄 PDF
                            </button>
                            <button className="btn btn-primary" style={{ padding: '3px 8px', fontSize: '10.5px' }} onClick={() => handleOpenAssign(exam, 'subjective')}>
                              📋 Assign Again
                            </button>
                            <button 
                              className="btn btn-secondary" 
                              style={{ 
                                padding: '3px 8px', 
                                fontSize: '10.5px', 
                                opacity: count > 0 ? 0.5 : 1, 
                                cursor: count > 0 ? 'not-allowed' : 'pointer' 
                              }} 
                              disabled={count > 0}
                              onClick={() => handleOpenEdit(exam.id, exam.name, 'subjectiveAssignments')}
                            >
                              ✏️ Edit
                            </button>
                            <button className="btn btn-secondary" style={{ padding: '3px 8px', fontSize: '10.5px' }} onClick={() => router.push(`/admin/teacher-final-review?examId=${exam.id}`)}>
                              Grade
                            </button>
                            <button className="btn btn-secondary" style={{ padding: '3px 8px', fontSize: '10.5px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'subjective')}>
                              🗑️ Delete
                            </button>
                          </div>
                        </td>
                      </tr>
                    );
                  });
                })()}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {/* Section 2: Already Assigned */}
      <div id="subjective-assignments-section">
        {(() => {
          const assignedExamsList = filteredSubjectiveExams.filter(isSubjectiveAlreadyAssigned);
          return (
            <>
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
                    📚 Subjective Exams Already Assigned
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
                        onClick={() => expandAllAssigned?.('subjective', assignedExamsList)}
                        title="Expand all classes, subjects, and chapters"
                      >
                        ⊞ Expand All
                      </button>
                      <button
                        type="button"
                        className="btn btn-secondary"
                        style={{ padding: '3px 8px', fontSize: '11px', fontWeight: 600 }}
                        onClick={() => collapseAllAssigned?.('subjective')}
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
                      No assigned subjective exams found.
                    </div>
                  ) : (
                    (() => {
                      const classes = getGroupedClasses(assignedExamsList);
                      return classes.map(cls => {
                        const examsInClass = assignedExamsList.filter(exam => getExamClass(exam) === cls);
                        const sortedExams = sortAssignedExams(examsInClass);
                        const isExpanded = expandedClasses.has(`subjective||${cls}`);
                        
                        return (
                          <div key={cls} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', background: 'var(--surface)', overflow: 'hidden' }}>
                            <div 
                              onClick={() => toggleClassExpanded(`subjective||${cls}`)}
                              style={{ padding: '10px 14px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isExpanded ? '1px solid var(--border-light)' : 'none' }}
                            >
                              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                <span style={{ fontWeight: 'bold', fontSize: '13px', color: 'var(--accent)' }}>🏫 Class {cls}</span>
                                <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>({examsInClass.length} subjective exams)</span>
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
                                    const subjKey = `subj||subjective||${cls}||${subjName}`;
                                    const isSubjExpanded = expandedSubjects.has(subjKey);

                                    const chapterGroups = new Map<string, Exam[]>();
                                    subjExams.forEach(exam => {
                                      const chap = getExamChapter(exam);
                                      if (!chapterGroups.has(chap)) chapterGroups.set(chap, []);
                                      chapterGroups.get(chap)!.push(exam);
                                    });

                                    return (
                                      <div key={subjKey} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-md)', background: 'var(--surface-popover)', overflow: 'hidden' }}>
                                        {/* Subject Line with count */}
                                        <div 
                                          onClick={() => toggleSubjectExpanded(subjKey)}
                                          style={{ padding: '8px 12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isSubjExpanded ? '1px solid var(--border-light)' : 'none' }}
                                        >
                                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                            <span style={{ fontWeight: 800, fontSize: '12.5px', color: 'var(--text)' }}>📖 {subjName}</span>
                                            <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>({subjExams.length} {subjExams.length === 1 ? 'exam' : 'exams'})</span>
                                          </div>
                                          <span style={{ fontSize: '10px', transition: 'transform 0.2s', transform: isSubjExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                                        </div>

                                        {/* Chapter hierarchy */}
                                        {isSubjExpanded && (
                                          <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', padding: '8px' }}>
                                            {Array.from(chapterGroups.entries()).map(([chapName, chapExams]) => {
                                              const chapKey = `chap||subjective||${cls}||${subjName}||${chapName}`;
                                              const isChapExpanded = expandedChapters.has(chapKey);

                                              return (
                                                <div key={chapKey} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', overflow: 'hidden' }}>
                                                  {/* Chapter Line with count */}
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

                                        {/* Exam Table */}
                                        {isChapExpanded && (
                                          <div style={{ overflowX: 'auto' }}>
                                            <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
                                              <thead>
                                                <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                                                  <th style={{ padding: '4px 8px', cursor: 'pointer', userSelect: 'none' }} onClick={() => handleAssignedSort('name')}>
                                                    Exam Name {assignedSortField === 'name' ? (assignedSortDir === 'asc' ? '🔼' : '🔽') : ''}
                                                  </th>
                                                  <th style={{ padding: '4px 8px' }}>Mode</th>
                                                  <th style={{ padding: '4px 8px' }}>Peer Review</th>
                                                  <th style={{ padding: '4px 8px' }}>Assigned To</th>
                                                  <th style={{ padding: '4px 8px', cursor: 'pointer', userSelect: 'none' }} onClick={() => handleAssignedSort('date')}>
                                                    Status / Starts {assignedSortField === 'date' ? (assignedSortDir === 'asc' ? '🔼' : '🔽') : ''}
                                                  </th>
                                                  <th style={{ padding: '4px 8px', textAlign: 'right' }}>Actions</th>
                                                </tr>
                                              </thead>
                                              <tbody>
                                                {chapExams.map(exam => {
                                                  const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === 'subjectiveAssignments');
                                                  const rawStatus = activeAssign?.status || 'active';
                                                  const scheduleStatus = getExamScheduleStatus(exam, activeAssign, 'subjective');
                                                  const mode = activeAssign?.examMode || exam.mode || 'home';
                                                  const peerStatus = exam.peerReviewStatus || 'not_started';
                                                  const count = attemptCounts[exam.id] || 0;
                                                  
                                                  return (
                                                    <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                                                      <td style={{ padding: '4px 8px', fontWeight: 600 }}>{exam.name}</td>
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
                                                      <td style={{ padding: '4px 8px', fontSize: '11px', color: 'var(--text-muted)' }}>{getAssignedNames(exam.id, exam.batchId)}</td>
                                                      <td style={{ padding: '4px 8px' }}>
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
                                                        </div>
                                                      </td>
                                                      <td style={{ padding: '4px 8px', textAlign: 'right' }}>
                                                        <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                                                          {activeAssign && activeAssign.openMode !== 'scheduled' && (
                                                            <button 
                                                              className={`btn ${rawStatus === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                                              style={{ padding: '3px 8px', fontSize: '10.5px', background: rawStatus === 'active' ? 'var(--danger)' : 'var(--success)', color: 'white', border: 'none' }} 
                                                              onClick={() => toggleAssignmentStatus(activeAssign.id, 'subjectiveAssignments', rawStatus === 'active' ? 'disabled' : 'active')}
                                                            >
                                                              {rawStatus === 'active' ? '🛑 Stop' : '🟢 Start'}
                                                            </button>
                                                          )}
                                                          <button className="btn btn-secondary" style={{ padding: '3px 8px', fontSize: '10.5px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} onClick={() => exportUniversalExamPDF(exam, exam.questions || (exam as any).questionDetails || (exam as any).questionCodes || (exam as any).questionIds || [])}>
                                                            📄 PDF
                                                          </button>
                                                          <button className="btn btn-primary" style={{ padding: '3px 8px', fontSize: '10.5px' }} onClick={() => handleOpenAssign(exam, 'subjective')}>
                                                            📋 Assign Again
                                                          </button>
                                                          <button 
                                                            className="btn btn-secondary" 
                                                            style={{ 
                                                              padding: '3px 8px', 
                                                              fontSize: '10.5px', 
                                                              opacity: count > 0 ? 0.5 : 1, 
                                                              cursor: count > 0 ? 'not-allowed' : 'pointer' 
                                                            }} 
                                                            disabled={count > 0}
                                                            onClick={() => handleOpenEdit(exam.id, exam.name, 'subjectiveAssignments')}
                                                          >
                                                            ✏️ Edit
                                                          </button>
                                                          <button className="btn btn-secondary" style={{ padding: '3px 8px', fontSize: '10.5px' }} onClick={() => router.push(`/admin/teacher-final-review?examId=${exam.id}`)}>
                                                            Grade
                                                          </button>
                                                          {mode === 'classroom' && (
                                                            <>
                                                              {peerStatus === 'not_started' && (
                                                                <button className="btn btn-primary" style={{ padding: '3px 8px', fontSize: '10.5px', background: 'var(--warning)', borderColor: 'var(--warning)' }} onClick={() => triggerPeerReviewLottery(exam.id, exam.name)}>
                                                                  🎲 Lottery
                                                                </button>
                                                              )}
                                                              {peerStatus === 'assigned' && (
                                                                <button className="btn btn-secondary" style={{ padding: '3px 8px', fontSize: '10.5px' }} onClick={() => openPeerReviewStatus(exam.id, exam.name)}>
                                                                  📊 Status
                                                                </button>
                                                              )}
                                                              <button 
                                                                className="btn btn-secondary" 
                                                                style={{ padding: '3px 8px', fontSize: '10.5px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} 
                                                                onClick={() => openTruthTestReport(exam.id, exam.name)}
                                                              >
                                                                ⚖️ Truth Test
                                                              </button>
                                                            </>
                                                          )}
                                                          <button className="btn btn-secondary" style={{ padding: '3px 8px', fontSize: '10.5px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'subjective')}>
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
            </>
          );
        })()}
      </div>
    </div>
  );
}
