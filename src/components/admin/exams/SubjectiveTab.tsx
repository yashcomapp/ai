'use client';

import React from 'react';
import { SubjectiveTabProps, extractAssignedSectionProps } from './types';
import { TodayTomorrowExamsTable } from './TodayTomorrowExamsTable';
import { AssignedExamsSection } from './AssignedExamsSection';

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
      <div id="subjective-templates-section" style={{ marginBottom: '24px' }}>
        <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
          📋 Subjective Exams Available for Assignment
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
                {filteredSubjectiveExams.filter(isSubjectiveAvailableForAssignment).length === 0 ? (
                  <tr>
                    <td colSpan={6} style={{ padding: '12px', textAlign: 'center', color: 'var(--text-muted)' }}>No subjective exams available for assignment.</td>
                  </tr>
                ) : (
                  filteredSubjectiveExams
                    .filter(isSubjectiveAvailableForAssignment)
                    .map(exam => (
                      <tr key={exam.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '4px 8px', fontWeight: 600 }}>{exam.name}</td>
                        <td style={{ padding: '4px 8px' }}>{exam.subjectName || exam.subjects?.[0] || '—'}</td>
                        <td style={{ padding: '4px 8px' }}>{(exam.topicCodes || []).join(', ') || '—'}</td>
                        <td style={{ padding: '4px 8px' }}>{exam.questionCount || exam.questions?.length || 0}</td>
                        <td style={{ padding: '4px 8px' }}>{exam.totalMarks || 0}</td>
                        <td style={{ padding: '4px 8px', textAlign: 'right' }}>
                          <div style={{ display: 'flex', gap: '4px', justifyContent: 'flex-end' }}>
                            <button className="btn btn-primary" style={{ padding: '2px 6px', fontSize: '10.5px' }} onClick={() => handleOpenAssign(exam, 'subjective')}>
                              📋 Assign
                            </button>
                            <button className="btn btn-secondary" style={{ padding: '2px 6px', fontSize: '10.5px', color: 'var(--danger)' }} onClick={() => handleDeleteExam(exam.id, exam.name, 'subjective')}>
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
