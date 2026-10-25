'use client';

import React from 'react';
import { Exam, Assignment, ExamScheduleStatus, isExamAssigned } from './types';
import { TodayTomorrowExamsTable } from './TodayTomorrowExamsTable';
import { AssignedExamsSection } from './AssignedExamsSection';

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
            <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '12.5px' }}>
              <thead>
                <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '11.5px' }}>
                  <th style={{ padding: '4px 8px' }}>Exam Name</th>
                  <th style={{ padding: '4px 8px' }}>Subject</th>
                  <th style={{ padding: '4px 8px' }}>Topics</th>
                  <th style={{ padding: '4px 8px' }}>Questions</th>
                  <th style={{ padding: '4px 8px' }}>Marks</th>
                  <th style={{ padding: '4px 8px', textAlign: 'right' }}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {filteredObjectiveExams.filter(exam => !isExamAssigned(exam, assignments, attemptCounts)).length === 0 ? (
                  <tr>
                    <td colSpan={6} style={{ padding: '12px', textAlign: 'center', color: 'var(--text-muted)' }}>No exams available for assignment.</td>
                  </tr>
                ) : (
                  filteredObjectiveExams
                    .filter(exam => !isExamAssigned(exam, assignments, attemptCounts))
                    .map(exam => (
                      <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '4px 8px', fontWeight: 600 }}>{exam.name}</td>
                        <td style={{ padding: '4px 8px' }}>{exam.subjectName || exam.subjects?.[0] || '—'}</td>
                        <td style={{ padding: '4px 8px' }}>{(exam.topicCodes || []).join(', ') || '—'}</td>
                        <td style={{ padding: '4px 8px' }}>{exam.questionCount || exam.questions?.length || 0}</td>
                        <td style={{ padding: '4px 8px' }}>{exam.totalMarks || 0}</td>
                        <td style={{ padding: '4px 8px', textAlign: 'right' }}>
                          <div style={{ display: 'flex', gap: '4px', justifyContent: 'flex-end' }}>
                            <button className="btn btn-secondary" style={{ padding: '2px 6px', fontSize: '10.5px', background: 'var(--accent-tint)', color: 'var(--accent)', fontWeight: 600 }} onClick={() => router.push(`/admin/mock-exam?examId=${encodeURIComponent(exam.id)}`)}>
                              🧪 Mock Test
                            </button>
                            <button className="btn btn-primary" style={{ padding: '2px 6px', fontSize: '10.5px' }} onClick={() => handleOpenAssign(exam, 'objective')}>
                              📋 Assign
                            </button>
                            <button className="btn btn-secondary" style={{ padding: '2px 6px', fontSize: '10.5px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'objective')}>
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
      <TodayTomorrowExamsTable
        exams={filteredObjectiveExams}
        type="objective"
        assignments={assignments}
        attemptCounts={attemptCounts}
        getAssignedNames={getAssignedNames}
        getLatestAssignmentDate={getLatestAssignmentDate}
        toggleAssignmentStatus={toggleAssignmentStatus}
        handleOpenAssign={handleOpenAssign}
        handleOpenEdit={handleOpenEdit}
        handleDeleteExam={handleDeleteExam}
        isAlreadyAssigned={(exam) => isExamAssigned(exam, assignments, attemptCounts)}
        router={router}
      />

      {/* Section 2: Already Assigned */}
      <AssignedExamsSection
        assignedExamsList={filteredObjectiveExams.filter(exam => isExamAssigned(exam, assignments, attemptCounts))}
        type="objective"
        assignments={assignments}
        attemptCounts={attemptCounts}
        isAssignedSectionExpanded={isAssignedSectionExpanded}
        setIsAssignedSectionExpanded={setIsAssignedSectionExpanded}
        expandedClasses={expandedClasses}
        toggleClassExpanded={toggleClassExpanded}
        expandedSubjects={expandedSubjects}
        toggleSubjectExpanded={toggleSubjectExpanded}
        expandedChapters={expandedChapters}
        toggleChapterExpanded={toggleChapterExpanded}
        expandAllAssigned={expandAllAssigned}
        collapseAllAssigned={collapseAllAssigned}
        assignedSortField={assignedSortField}
        assignedSortDir={assignedSortDir}
        handleAssignedSort={handleAssignedSort}
        sortAssignedExams={sortAssignedExams}
        getGroupedClasses={getGroupedClasses}
        getExamClass={getExamClass}
        getExamSubject={getExamSubject}
        getExamChapter={getExamChapter}
        getAssignedNames={getAssignedNames}
        getLatestAssignmentDate={getLatestAssignmentDate}
        getExamScheduleStatus={getExamScheduleStatus}
        toggleAssignmentStatus={toggleAssignmentStatus}
        handleOpenAssign={handleOpenAssign}
        handleOpenEdit={handleOpenEdit}
        handleDeleteExam={handleDeleteExam}
        router={router}
      />
    </div>
  );
}
