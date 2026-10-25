'use client';

import React from 'react';
import { isExamAssigned, ObjectiveTabProps, extractAssignedSectionProps } from './types';
import { TodayTomorrowExamsTable } from './TodayTomorrowExamsTable';
import { AssignedExamsSection } from './AssignedExamsSection';
import { UnassignedExamsTable } from './UnassignedExamsTable';

export type { ObjectiveTabProps };

export default function ObjectiveTab(props: ObjectiveTabProps) {
  const {
    filteredObjectiveExams,
    assignments,
    attemptCounts,
    objFilterName,
    setObjFilterName,
    objFilterTopic,
    setObjFilterTopic,
    getAssignedNames,
    getLatestAssignmentDate,
    toggleAssignmentStatus,
    handleOpenAssign,
    handleOpenEdit,
    handleDeleteExam,
    router
  } = props;

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
      <UnassignedExamsTable
        exams={filteredObjectiveExams.filter(exam => !isExamAssigned(exam, assignments, attemptCounts))}
        type="objective"
        onAssign={handleOpenAssign}
        onDelete={handleDeleteExam}
        onMockExam={(examId) => router.push(`/admin/mock-exam?examId=${encodeURIComponent(examId)}`)}
      />

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
        {...extractAssignedSectionProps(
          props,
          filteredObjectiveExams.filter(exam => isExamAssigned(exam, assignments, attemptCounts)),
          'objective'
        )}
      />
    </div>
  );
}
