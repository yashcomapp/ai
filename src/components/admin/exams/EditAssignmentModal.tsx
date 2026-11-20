'use client';

import React from 'react';
import { calculateEndDatetime, toLocalISOString } from '@/lib/dateUtils';
import TargetPicker from './TargetPicker';
import ScheduleTimingInputs from './ScheduleTimingInputs';
import { AttemptDurationControls } from './AttemptDurationControls';
import { ModalShell } from '@/components/common/ModalShell';
import { BaseAssignmentModalState, AssignmentModalCommonProps, ASSIGNMENT_MODAL_CARD_STYLE } from './types';

export interface EditModalState extends BaseAssignmentModalState {
  assignmentId: string;
  collection: 'batchAssignments' | 'subjectiveAssignments';
}

interface EditAssignmentModalProps extends AssignmentModalCommonProps {
  editModal: EditModalState;
  setEditModal: React.Dispatch<React.SetStateAction<EditModalState>>;
  handleToggleBatchEdit: (id: string) => void;
  handleToggleStudentEdit: (code: string) => void;
  handleSelectStudentsEdit?: (codes: string[], select: boolean) => void;
  handleSaveEditedAssignment: () => void;
}

export function EditAssignmentModal({
  editModal,
  setEditModal,
  batches,
  getStudentsGroupedByBatch,
  handleToggleBatchEdit,
  handleToggleStudentEdit,
  handleSelectStudentsEdit,
  getMorningTestTimes,
  getEveningTestTimes,
  handleSaveEditedAssignment
}: EditAssignmentModalProps) {
  if (!editModal.show) return null;

  const getDuration = (prev: EditModalState) => {
    return Number(prev.overrideDuration && prev.examDuration ? prev.examDuration : prev.normDuration) || 30;
  };

  return (
    <ModalShell
      isOpen={editModal.show}
      onClose={() => setEditModal(prev => ({ ...prev, show: false }))}
      maxWidth="660px"
      zIndex={20000}
      cardStyle={ASSIGNMENT_MODAL_CARD_STYLE}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '8px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
          <h3 style={{ fontSize: '14px', fontWeight: 800, margin: 0, color: 'var(--text)' }}>
            ✏️ Edit Assignment Schedule
          </h3>
          <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 500, wordBreak: 'break-all' }}>
            ({editModal.examName})
          </span>
        </div>
        <button 
          onClick={() => setEditModal(prev => ({ ...prev, show: false }))} 
          style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', fontSize: '16px', padding: '1px 4px', borderRadius: '4px' }}
        >
          ✕
        </button>
      </div>

      {/* Target Audience Section */}
      <div style={{ background: 'var(--surface-sunken)', padding: '6px 10px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
        <TargetPicker
          targetType={editModal.targetType}
          onChangeTargetType={(type) => setEditModal(prev => ({ ...prev, targetType: type }))}
          batches={batches}
          selectedBatches={editModal.selectedBatches}
          onToggleBatch={handleToggleBatchEdit}
          selectedStudents={editModal.selectedStudents}
          onToggleStudent={handleToggleStudentEdit}
          onSelectStudents={handleSelectStudentsEdit}
          getStudentsGroupedByBatch={getStudentsGroupedByBatch}
        />
      </div>

      <div>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '4px', flexWrap: 'wrap', gap: '6px' }}>
          <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Availability Slot</label>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
            <label style={{ fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
              <input 
                type="radio" 
                name="editOpenMode" 
                checked={editModal.openMode === 'immediate'} 
                onChange={() => setEditModal(prev => ({ ...prev, openMode: 'immediate', isMorningTest: false, isEveningTest: false }))} 
              /> Immediate
            </label>
            <label style={{ fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
              <input 
                type="radio" 
                name="editOpenMode" 
                checked={editModal.openMode === 'scheduled' && !editModal.isMorningTest && !editModal.isEveningTest} 
                onChange={() => setEditModal(prev => {
                  const dur = getDuration(prev);
                  const start = prev.startAtStr || toLocalISOString(new Date());
                  return {
                    ...prev,
                    openMode: 'scheduled',
                    isMorningTest: false,
                    isEveningTest: false,
                    startAtStr: start,
                    endAtStr: calculateEndDatetime(start, dur)
                  };
                })} 
              /> Scheduled
            </label>
            <label style={{ fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap', background: editModal.isMorningTest ? 'rgba(52, 152, 219, 0.2)' : 'rgba(52, 152, 219, 0.08)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(52, 152, 219, 0.25)' }}>
              <input 
                type="checkbox" 
                checked={!!editModal.isMorningTest} 
                onChange={(e) => {
                  const checked = e.target.checked;
                  setEditModal(prev => {
                    let updates: any = { isMorningTest: checked, isEveningTest: false };
                    if (checked) {
                      updates.openMode = 'scheduled';
                      updates.lateEntryRestriction = true;
                      const duration = getDuration(prev);
                      const times = getMorningTestTimes(duration);
                      updates.startAtStr = times.startStr;
                      updates.endAtStr = times.endStr;
                    }
                    return { ...prev, ...updates };
                  });
                }} 
              /> ☀️ 6 AM Test
            </label>
            <label style={{ fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap', background: editModal.isEveningTest ? 'rgba(168, 85, 247, 0.2)' : 'rgba(168, 85, 247, 0.08)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(168, 85, 247, 0.25)' }}>
              <input 
                type="checkbox" 
                checked={!!editModal.isEveningTest} 
                onChange={(e) => {
                  const checked = e.target.checked;
                  setEditModal(prev => {
                    let updates: any = { isEveningTest: checked, isMorningTest: false };
                    if (checked) {
                      updates.openMode = 'scheduled';
                      updates.lateEntryRestriction = true;
                      const duration = getDuration(prev);
                      const times = getEveningTestTimes(duration);
                      updates.startAtStr = times.startStr;
                      updates.endAtStr = times.endStr;
                    }
                    return { ...prev, ...updates };
                  });
                }} 
              /> 🌙 9 PM Test
            </label>
          </div>
        </div>

        <ScheduleTimingInputs
          state={editModal}
          setState={setEditModal}
          getDuration={getDuration}
          radioNamePrefix="edit"
        />
      </div>

      <AttemptDurationControls
        maxAttempts={editModal.attemptLimit}
        onChangeMaxAttempts={(val) => setEditModal(prev => ({ ...prev, attemptLimit: val }))}
        showDuration={editModal.collection === 'batchAssignments'}
        overrideDuration={editModal.overrideDuration}
        examDuration={editModal.examDuration}
        onChangeOverrideDuration={(checked) => {
          setEditModal(prev => {
            const dur = checked ? (Number(prev.examDuration) || prev.normDuration || 30) : (prev.normDuration || 30);
            let updates: any = { overrideDuration: checked, examDuration: dur };
            if (prev.startAtStr && dur > 0) {
              updates.endAtStr = calculateEndDatetime(prev.startAtStr, dur);
            }
            return { ...prev, ...updates };
          });
        }}
        onChangeExamDuration={(dur) => {
          setEditModal(prev => {
            const numDur = dur === '' ? ('' as any) : Number(dur);
            let updates: any = { examDuration: numDur, overrideDuration: true };
            if (prev.startAtStr && typeof numDur === 'number' && !isNaN(numDur) && numDur > 0) {
              updates.endAtStr = calculateEndDatetime(prev.startAtStr, numDur);
            }
            return { ...prev, ...updates };
          });
        }}
        onBlurExamDuration={() => {
          setEditModal(prev => {
            if (!prev.examDuration || Number(prev.examDuration) < 1) {
              const fallbackDur = prev.normDuration || 30;
              return {
                ...prev,
                examDuration: fallbackDur,
                endAtStr: prev.startAtStr ? calculateEndDatetime(prev.startAtStr, fallbackDur) : prev.endAtStr
              };
            }
            return prev;
          });
        }}
        durationHelperText={!editModal.overrideDuration && (
          <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>
            Auto-calculated from questions ({editModal.normDuration} mins standard norm).
          </div>
        )}
      />

      {editModal.startsCount && editModal.startsCount > 0 ? (
        <div style={{ background: 'rgba(239, 68, 68, 0.08)', border: '1px solid rgba(239, 68, 68, 0.25)', padding: '6px 10px', borderRadius: 'var(--radius-sm)', fontSize: '11px' }}>
          <label style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer', color: '#ef4444', fontWeight: 600 }}>
            <input 
              type="checkbox" 
              checked={!!editModal.resetAttempts} 
              onChange={(e) => setEditModal(prev => ({ ...prev, resetAttempts: e.target.checked }))} 
            />
            🔄 Reset existing {editModal.startsCount} student attempt(s) on reschedule
          </label>
          <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>
            Checked by default: allows students who already started or took the test to re-attempt in the new window.
          </div>
        </div>
      ) : null}

      <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '4px' }}>
        <button className="btn btn-secondary" onClick={() => setEditModal(prev => ({ ...prev, show: false }))}>Cancel</button>
        <button className="btn btn-primary" onClick={handleSaveEditedAssignment}>Save Changes</button>
      </div>
    </ModalShell>
  );
}

export default EditAssignmentModal;
