'use client';

import React from 'react';
import { SubjectiveTabProps, extractAssignedSectionProps } from './types';
import { TodayTomorrowExamsTable } from './TodayTomorrowExamsTable';
import { AssignedExamsSection } from './AssignedExamsSection';
import { UnassignedExamsTable } from './UnassignedExamsTable';

export type { SubjectiveTabProps };

export default function SubjectiveTab(props: SubjectiveTabProps) {
  const {
    filteredSubjectiveExams,
    assignments,
    attemptCounts,
    subjFilterName,
    setSubjFilterName,
    subjFilterTopic,
    setSubjFilterTopic,
    isSubjectiveAvailableForAssignment,
    isSubjectiveAlreadyAssigned,
    getAssignedNames,
    getLatestAssignmentDate,
    toggleAssignmentStatus,
    handleOpenAssign,
    handleOpenEdit,
    handleDeleteExam,
    triggerPeerReviewLottery,
    openPeerReviewStatus,
    openTruthTestReport,
    router
  } = props;

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
      <UnassignedExamsTable
        exams={filteredSubjectiveExams.filter(isSubjectiveAvailableForAssignment)}
        type="subjective"
        onAssign={handleOpenAssign}
        onDelete={handleDeleteExam}
      />

      {/* Section 1b: Today's & Tomorrow's Subjective Exams */}
      <TodayTomorrowExamsTable
        exams={filteredSubjectiveExams}
        type="subjective"
        assignments={assignments}
        attemptCounts={attemptCounts}
        getAssignedNames={getAssignedNames}
        getLatestAssignmentDate={getLatestAssignmentDate}
        toggleAssignmentStatus={toggleAssignmentStatus}
        handleOpenAssign={handleOpenAssign}
        handleOpenEdit={handleOpenEdit}
        handleDeleteExam={handleDeleteExam}
        isAlreadyAssigned={isSubjectiveAlreadyAssigned}
        router={router}
      />

      {/* Section 2: Already Assigned */}
      <AssignedExamsSection
        {...extractAssignedSectionProps(
          props,
          filteredSubjectiveExams.filter(isSubjectiveAlreadyAssigned),
          'subjective',
          { triggerPeerReviewLottery, openPeerReviewStatus, openTruthTestReport }
        )}
      />
    </div>
  );
}
