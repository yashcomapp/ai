'use client';

import React from 'react';
import { Exam, Assignment, ExamScheduleStatus, isExamAssigned } from './types';

interface ObjectiveTabProps {
  filteredObjectiveExams: Exam[];
  assignments: Assignment[];
  attemptCounts: { [key: string]: number };
  objFilterName: string;
  setObjFilterName: (val: string) => void;
  objFilterTopic: string;
  setObjFilterTopic: (val: string) => void;
  isTodayOrTomorrow: (exam: Exam, type: 'objective' | 'subjective') => boolean;
  getExamSortTimestamp: (exam: Exam, type: 'objective' | 'subjective') => number;
  getExamClass: (exam: any) => string;
  getExamSubject: (exam: any) => string;
  getExamChapter: (exam: any) => string;
  getAssignedNames: (examId: string, directBatchId?: string | null) => string;
  getLatestAssignmentDate: (examId: string, assignedAt?: string | null, exam?: Exam) => string;
  getExamScheduleStatus: (exam: Exam, activeAssign?: Assignment, examType?: 'objective' | 'subjective') => ExamScheduleStatus;
  expandedClasses: Set<string>;
  toggleClassExpanded: (clsKey: string) => void;
  collapsedSubjects: Set<string>;
  toggleSubjectCollapsed: (key: string) => void;
  collapsedChapters: Set<string>;
  toggleChapterCollapsed: (key: string) => void;
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
  router: any;
}

export default function ObjectiveTab({
  filteredObjectiveExams,
  assignments,
  attemptCounts,
  objFilterName,
  setObjFilterName,
  objFilterTopic,
  setObjFilterTopic,
  isTodayOrTomorrow,
  getExamSortTimestamp,
  getExamClass,
  getExamSubject,
  getExamChapter,
  getAssignedNames,
  getLatestAssignmentDate,
  getExamScheduleStatus,
  expandedClasses,
  toggleClassExpanded,
  collapsedSubjects,
  toggleSubjectCollapsed,
  collapsedChapters,
  toggleChapterCollapsed,
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
  router
}: ObjectiveTabProps) {
  return (
    <div>
      <div className="filter-row" style={{ display: 'flex', gap: '10px', marginBottom: '16px', flexWrap: 'wrap' }}>
        <input 
          type="text" 
          value={objFilterName}
          placeholder="🔍 Filter by exam name..." 
          onChange={(e) => setObjFilterName(e.target.value)}
          style={{ flex: 1, minWidth: '220px', padding: '8px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
        />
        <input 
          type="text" 
          value={objFilterTopic}
          placeholder="🔍 Filter by topic code..." 
          onChange={(e) => setObjFilterTopic(e.target.value)}
          style={{ flex: 1, minWidth: '220px', padding: '8px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)' }}
        />
        <button 
          className="btn btn-secondary" 
          onClick={() => { setObjFilterName(''); setObjFilterTopic(''); }}
        >
          Clear
        </button>
      </div>

      {/* Section 1: Available for Assignment */}
      <div id="objective-templates-section" style={{ marginBottom: '24px' }}>
        <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
          📋 Exams Available for Assignment
        </h3>
        <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
          <div style={{ overflowX: 'auto' }}>
            <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
              <thead>
                <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                  <th style={{ padding: '12px 16px' }}>Exam Name</th>
                  <th style={{ padding: '12px 16px' }}>Subject</th>
                  <th style={{ padding: '12px 16px' }}>Topics</th>
                  <th style={{ padding: '12px 16px' }}>Questions</th>
                  <th style={{ padding: '12px 16px' }}>Marks</th>
                  <th style={{ padding: '12px 16px', textAlign: 'right' }}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {filteredObjectiveExams.filter(exam => !isExamAssigned(exam, assignments, attemptCounts)).length === 0 ? (
                  <tr>
                    <td colSpan={6} style={{ padding: '30px', textAlign: 'center', color: 'var(--text-muted)' }}>No exams available for assignment.</td>
                  </tr>
                ) : (
                  filteredObjectiveExams
                    .filter(exam => !isExamAssigned(exam, assignments, attemptCounts))
                    .map(exam => (
                      <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '12px 16px', fontWeight: 600 }}>{exam.name}</td>
                        <td style={{ padding: '12px 16px' }}>{exam.subjectName || exam.subjects?.[0] || '—'}</td>
                        <td style={{ padding: '12px 16px' }}>{(exam.topicCodes || []).join(', ') || '—'}</td>
                        <td style={{ padding: '12px 16px' }}>{exam.questionCount || exam.questions?.length || 0}</td>
                        <td style={{ padding: '12px 16px' }}>{exam.totalMarks || 0}</td>
                        <td style={{ padding: '12px 16px', textAlign: 'right' }}>
                          <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end' }}>
                            <button className="btn btn-primary" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => handleOpenAssign(exam, 'objective')}>
                              📋 Assign
                            </button>
                            <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'objective')}>
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

      {/* Section 1b: Today's & Tomorrow's Exams */}
      <div id="objective-today-tomorrow-section" style={{ marginBottom: '24px' }}>
        <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
          📅 Today's & Tomorrow's Exams
        </h3>
        <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
          <div style={{ overflowX: 'auto' }}>
            <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
              <thead>
                <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                  <th style={{ padding: '12px 16px' }}>Exam Name</th>
                  <th style={{ padding: '12px 16px' }}>Assigned To</th>
                  <th style={{ padding: '12px 16px' }}>Assigned Date</th>
                  <th style={{ padding: '12px 16px' }}>Status / Starts</th>
                  <th style={{ padding: '12px 16px', textAlign: 'right' }}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {(() => {
                  const todayTomorrowExams = filteredObjectiveExams.filter(exam => 
                    isExamAssigned(exam, assignments, attemptCounts) &&
                    isTodayOrTomorrow(exam, 'objective')
                  );
                  
                  const sortedTodayTomorrowExams = [...todayTomorrowExams].sort((a, b) => {
                    const timeA = getExamSortTimestamp(a, 'objective');
                    const timeB = getExamSortTimestamp(b, 'objective');
                    if (timeA !== timeB) return timeA - timeB;
                    
                    const classA = parseInt(getExamClass(a)) || 0;
                    const classB = parseInt(getExamClass(b)) || 0;
                    return classA - classB;
                  });

                  if (sortedTodayTomorrowExams.length === 0) {
                    return (
                      <tr>
                        <td colSpan={5} style={{ padding: '24px', textAlign: 'center', color: 'var(--text-muted)' }}>No exams scheduled for today or tomorrow.</td>
                      </tr>
                    );
                  }
                  
                  return sortedTodayTomorrowExams.map(exam => {
                    const count = attemptCounts[exam.id] || 0;
                    const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === 'batchAssignments') || assignments.find(a => a.examId === exam.id);
                    const rawStatus = activeAssign?.status || 'active';
                    const scheduleStatus = getExamScheduleStatus(exam, activeAssign, 'objective');
                    return (
                      <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                          {exam.name}
                          <span style={{ marginLeft: '8px', fontSize: '9px', fontWeight: 700, background: 'rgba(59, 130, 246, 0.1)', color: 'var(--accent)', padding: '2px 6px', borderRadius: '4px' }}>
                            Class {getExamClass(exam)}
                          </span>
                        </td>
                        <td style={{ padding: '12px 16px', fontSize: '11px', color: 'var(--text-muted)' }}>{getAssignedNames(exam.id, exam.batchId)}</td>
                        <td style={{ padding: '12px 16px', fontSize: '11px', color: 'var(--text-muted)' }}>{getLatestAssignmentDate(exam.id, exam.assignedAt, exam)}</td>
                        <td style={{ padding: '12px 16px' }}>
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
                        <td style={{ padding: '12px 16px', textAlign: 'right' }}>
                          <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                            {activeAssign && activeAssign.openMode !== 'scheduled' && (
                              <button 
                                className={`btn ${rawStatus === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                style={{ padding: '4px 10px', fontSize: '11px', background: rawStatus === 'active' ? 'var(--danger)' : 'var(--success)', color: 'white', border: 'none' }} 
                                onClick={() => toggleAssignmentStatus(activeAssign.id, activeAssign.collection || 'batchAssignments', rawStatus === 'active' ? 'disabled' : 'active')}
                              >
                                {rawStatus === 'active' ? '🛑 Stop' : '🟢 Start'}
                              </button>
                            )}
                            <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} onClick={() => exportUniversalExamPDF(exam, exam.questions || (exam as any).questionDetails || (exam as any).questionCodes || (exam as any).questionIds || [])}>
                              📄 PDF
                            </button>
                            <button className="btn btn-primary" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => handleOpenAssign(exam, 'objective')}>
                              📋 Assign Again
                            </button>
                            <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => router.push(`/admin/exam-report?examId=${exam.id}`)}>
                              📊 Report
                            </button>
                            <button 
                              className="btn btn-secondary" 
                              style={{ 
                                padding: '4px 10px', 
                                fontSize: '11px', 
                                opacity: count > 0 ? 0.5 : 1, 
                                cursor: count > 0 ? 'not-allowed' : 'pointer' 
                              }} 
                              disabled={count > 0}
                              onClick={() => handleOpenEdit(exam.id, exam.name, activeAssign?.collection || 'batchAssignments')}
                            >
                              ✏️ Edit
                            </button>
                            <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'objective')}>
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
      <div id="objective-assignments-section">
        <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
          📚 Exams Already Assigned
        </h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          {(() => {
            const assignedExamsList = filteredObjectiveExams.filter(exam => isExamAssigned(exam, assignments, attemptCounts));
            if (assignedExamsList.length === 0) {
              return (
                <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '30px', textAlign: 'center', color: 'var(--text-muted)' }}>
                  No assigned exams found.
                </div>
              );
            }
            
            const classes = getGroupedClasses(assignedExamsList);
            return classes.map(cls => {
              const examsInClass = assignedExamsList.filter(exam => getExamClass(exam) === cls);
              const sortedExams = sortAssignedExams(examsInClass);
              const isExpanded = expandedClasses.has(`objective||${cls}`);
              
              return (
                <div key={cls} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', background: 'var(--surface)', overflow: 'hidden' }}>
                  <div 
                    onClick={() => toggleClassExpanded(`objective||${cls}`)}
                    style={{ padding: '14px 18px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isExpanded ? '1px solid var(--border-light)' : 'none' }}
                  >
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ fontWeight: 'bold', fontSize: '13.5px', color: 'var(--accent)' }}>🏫 Class {cls}</span>
                      <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>({examsInClass.length} exams)</span>
                    </div>
                    <span style={{ fontSize: '10px', transition: 'transform 0.2s', transform: isExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                  </div>
                  
                  {isExpanded && (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', padding: '12px' }}>
                      {(() => {
                        const subjectGroups = new Map<string, Exam[]>();
                        sortedExams.forEach(exam => {
                          const subj = getExamSubject(exam);
                          if (!subjectGroups.has(subj)) subjectGroups.set(subj, []);
                          subjectGroups.get(subj)!.push(exam);
                        });

                        return Array.from(subjectGroups.entries()).map(([subjName, subjExams]) => {
                          const subjKey = `subj||objective||${cls}||${subjName}`;
                          const isSubjExpanded = !collapsedSubjects.has(subjKey);

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
                                onClick={() => toggleSubjectCollapsed(subjKey)}
                                style={{ padding: '10px 14px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isSubjExpanded ? '1px solid var(--border-light)' : 'none' }}
                              >
                                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                  <span style={{ fontWeight: 800, fontSize: '13px', color: 'var(--text)' }}>📖 {subjName}</span>
                                  <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>({subjExams.length} {subjExams.length === 1 ? 'exam' : 'exams'})</span>
                                </div>
                                <span style={{ fontSize: '10px', transition: 'transform 0.2s', transform: isSubjExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                              </div>

                              {/* Chapter hierarchy */}
                              {isSubjExpanded && (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', padding: '10px' }}>
                                  {Array.from(chapterGroups.entries()).map(([chapName, chapExams]) => {
                                    const chapKey = `chap||objective||${cls}||${subjName}||${chapName}`;
                                    const isChapExpanded = !collapsedChapters.has(chapKey);

                                    return (
                                      <div key={chapKey} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', overflow: 'hidden' }}>
                                        {/* Chapter Line with count */}
                                        <div 
                                          onClick={() => toggleChapterCollapsed(chapKey)}
                                          style={{ padding: '8px 12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isChapExpanded ? '1px solid var(--border-light)' : 'none' }}
                                        >
                                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                            <span style={{ fontWeight: 700, fontSize: '12px', color: 'var(--accent)' }}>📘 {chapName}</span>
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
                                                  <th style={{ padding: '10px 14px', cursor: 'pointer', userSelect: 'none' }} onClick={() => handleAssignedSort('name')}>
                                                    Exam Name {assignedSortField === 'name' ? (assignedSortDir === 'asc' ? '🔼' : '🔽') : ''}
                                                  </th>
                                                  <th style={{ padding: '10px 14px' }}>Assigned To</th>
                                                  <th style={{ padding: '10px 14px', cursor: 'pointer', userSelect: 'none' }} onClick={() => handleAssignedSort('date')}>
                                                    Assigned Date {assignedSortField === 'date' ? (assignedSortDir === 'asc' ? '🔼' : '🔽') : ''}
                                                  </th>
                                                  <th style={{ padding: '10px 14px' }}>Status / Starts</th>
                                                  <th style={{ padding: '10px 14px', textAlign: 'right' }}>Actions</th>
                                                </tr>
                                              </thead>
                                              <tbody>
                                                {chapExams.map(exam => {
                                                  const count = attemptCounts[exam.id] || 0;
                                                  const activeAssign = assignments.find(a => a.examId === exam.id && a.collection === 'batchAssignments');
                                                  const rawStatus = activeAssign?.status || 'active';
                                                  const scheduleStatus = getExamScheduleStatus(exam, activeAssign, 'objective');
                                                  
                                                  return (
                                                    <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                                                      <td style={{ padding: '10px 14px', fontWeight: 600 }}>{exam.name}</td>
                                                      <td style={{ padding: '10px 14px', fontSize: '11px', color: 'var(--text-muted)' }}>{getAssignedNames(exam.id, exam.batchId)}</td>
                                                      <td style={{ padding: '10px 14px', fontSize: '11px', color: 'var(--text-muted)' }}>{getLatestAssignmentDate(exam.id, exam.assignedAt, exam)}</td>
                                                      <td style={{ padding: '10px 14px' }}>
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
                                                      <td style={{ padding: '10px 14px', textAlign: 'right' }}>
                                                        <div style={{ display: 'flex', gap: '6px', justifyContent: 'flex-end', flexWrap: 'nowrap', whiteSpace: 'nowrap' }}>
                                                          {activeAssign && activeAssign.openMode !== 'scheduled' && (
                                                            <button 
                                                              className={`btn ${rawStatus === 'active' ? 'btn-secondary' : 'btn-primary'}`} 
                                                              style={{ padding: '4px 10px', fontSize: '11px', background: rawStatus === 'active' ? 'var(--danger)' : 'var(--success)', color: 'white', border: 'none' }} 
                                                              onClick={() => toggleAssignmentStatus(activeAssign.id, 'batchAssignments', rawStatus === 'active' ? 'disabled' : 'active')}
                                                            >
                                                              {rawStatus === 'active' ? '🛑 Stop' : '🟢 Start'}
                                                            </button>
                                                          )}
                                                          <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} onClick={() => exportUniversalExamPDF(exam, exam.questions || (exam as any).questionDetails || (exam as any).questionCodes || (exam as any).questionIds || [])}>
                                                            📄 PDF
                                                          </button>
                                                          <button className="btn btn-primary" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => handleOpenAssign(exam, 'objective')}>
                                                            📋 Assign Again
                                                          </button>
                                                          <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => router.push(`/admin/exam-report?examId=${encodeURIComponent(exam.id)}`)}>
                                                            📊 Report
                                                          </button>
                                                          <button 
                                                            className="btn btn-secondary" 
                                                            style={{ 
                                                              padding: '4px 10px', 
                                                              fontSize: '11px', 
                                                              opacity: count > 0 ? 0.5 : 1, 
                                                              cursor: count > 0 ? 'not-allowed' : 'pointer' 
                                                            }} 
                                                            disabled={count > 0}
                                                            onClick={() => handleOpenEdit(exam.id, exam.name, 'batchAssignments')}
                                                          >
                                                            ✏️ Edit
                                                          </button>
                                                          <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'objective')}>
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
          })()}
        </div>
      </div>
    </div>
  );
}
