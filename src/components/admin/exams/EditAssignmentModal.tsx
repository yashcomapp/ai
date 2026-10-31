'use client';

import React from 'react';
import DateTimeInputDMY from '@/components/DateTimeInputDMY';
import { calculateEndDatetime, toLocalISOString, getDateKeyIST } from '@/lib/dateUtils';
import { Batch } from '@/types/batch.types';
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
  handleSaveEditedAssignment: () => void;
}

export function EditAssignmentModal({
  editModal,
  setEditModal,
  batches,
  getStudentsGroupedByBatch,
  handleToggleBatchEdit,
  handleToggleStudentEdit,
  getMorningTestTimes,
  getEveningTestTimes,
  handleSaveEditedAssignment
}: EditAssignmentModalProps) {
  if (!editModal.show) return null;

  return (
    <ModalShell
      isOpen={editModal.show}
      onClose={() => setEditModal(prev => ({ ...prev, show: false }))}
      maxWidth="620px"
      zIndex={20000}
      cardStyle={ASSIGNMENT_MODAL_CARD_STYLE}
    >
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '12px' }}>
          <div>
            <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0, color: 'var(--text)' }}>
              ✏️ Edit Assignment Schedule
            </h3>
            <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '2px', wordBreak: 'break-word', lineHeight: '1.4' }}>
              {editModal.examName}
            </div>
          </div>
          <button 
            onClick={() => setEditModal(prev => ({ ...prev, show: false }))} 
            style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', fontSize: '18px', padding: '2px 6px', borderRadius: '4px' }}
          >
            ✕
          </button>
        </div>

        {/* Target Audience Section */}
        <div style={{ background: 'var(--surface-sunken)', padding: '10px 12px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
          <TargetPicker
            targetType={editModal.targetType}
            onChangeTargetType={(type) => setEditModal(prev => ({ ...prev, targetType: type }))}
            batches={batches}
            selectedBatches={editModal.selectedBatches}
            onToggleBatch={handleToggleBatchEdit}
            selectedStudents={editModal.selectedStudents}
            onToggleStudent={handleToggleStudentEdit}
            getStudentsGroupedByBatch={getStudentsGroupedByBatch}
          />
        </div>

        <div>
          <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Availability Slot</label>
          <div style={{ display: 'flex', alignItems: 'center', gap: '15px', marginBottom: '8px', flexWrap: 'wrap' }}>
            <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
              <input 
                type="radio" 
                name="editOpenMode" 
                checked={editModal.openMode === 'immediate'} 
                onChange={() => setEditModal(prev => ({ ...prev, openMode: 'immediate', isMorningTest: false, isEveningTest: false }))} 
              /> Immediate
            </label>
            <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
              <input 
                type="radio" 
                name="editOpenMode" 
                checked={editModal.openMode === 'scheduled' && !editModal.isMorningTest && !editModal.isEveningTest} 
                onChange={() => setEditModal(prev => {
                  const dur = Number(prev.examDuration) || prev.normDuration || 30;
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
            <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap', background: editModal.isMorningTest ? 'rgba(52, 152, 219, 0.2)' : 'rgba(52, 152, 219, 0.08)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(52, 152, 219, 0.25)' }}>
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
                      const times = getMorningTestTimes(prev.examDuration || 30);
                      updates.startAtStr = times.startStr;
                      updates.endAtStr = times.endStr;
                    }
                    return { ...prev, ...updates };
                  });
                }} 
              /> ☀️ 6 AM Test
            </label>
            <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap', background: editModal.isEveningTest ? 'rgba(168, 85, 247, 0.2)' : 'rgba(168, 85, 247, 0.08)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(168, 85, 247, 0.25)' }}>
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
                      const times = getEveningTestTimes(prev.examDuration || 30);
                      updates.startAtStr = times.startStr;
                      updates.endAtStr = times.endStr;
                    }
                    return { ...prev, ...updates };
                  });
                }} 
              /> 🌙 9 PM Test
            </label>
            <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap', background: editModal.isTodaySlot ? 'rgba(16, 185, 129, 0.2)' : 'rgba(16, 185, 129, 0.08)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(16, 185, 129, 0.25)' }}>
              <input 
                type="checkbox" 
                checked={!!editModal.isTodaySlot} 
                onChange={(e) => {
                  const checked = e.target.checked;
                  setEditModal(prev => {
                    let updates: any = { isTodaySlot: checked, isMorningTest: false, isEveningTest: false };
                    if (checked) {
                      updates.openMode = 'scheduled';
                      updates.lateEntryRestriction = false;
                      const todayStr = getDateKeyIST();
                      updates.startAtStr = `${todayStr}T06:20`;
                      updates.endAtStr = `${todayStr}T23:59`;
                    }
                    return { ...prev, ...updates };
                  });
                }} 
              /> 📅 Today Slot (06:20 AM – 11:59 PM)
            </label>
          </div>

          <ScheduleTimingInputs
            state={editModal}
            setState={setEditModal}
            getDuration={(prev) => Number(prev.examDuration) || prev.normDuration || 30}
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
              return { ...prev, overrideDuration: checked, examDuration: dur };
            });
          }}
          onChangeExamDuration={(dur) => {
            setEditModal(prev => ({ ...prev, examDuration: dur === '' ? ('' as any) : Number(dur) }));
          }}
          onBlurExamDuration={() => {
            if (!editModal.examDuration || Number(editModal.examDuration) < 1) {
              const fallbackDur = editModal.normDuration || 30;
              setEditModal(prev => ({
                ...prev,
                examDuration: fallbackDur
              }));
            }
          }}
          durationHelperText={!editModal.overrideDuration && (
            <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>
              Auto-calculated from questions ({editModal.normDuration} mins standard norm).
            </div>
          )}
        />

        {editModal.startsCount && editModal.startsCount > 0 ? (
          <div style={{ background: 'rgba(239, 68, 68, 0.08)', border: '1px solid rgba(239, 68, 68, 0.25)', padding: '10px 12px', borderRadius: 'var(--radius-sm)', fontSize: '12px' }}>
            <label style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer', color: '#ef4444', fontWeight: 600 }}>
              <input 
                type="checkbox" 
                checked={!!editModal.resetAttempts} 
                onChange={(e) => setEditModal(prev => ({ ...prev, resetAttempts: e.target.checked }))} 
              />
              🔄 Reset existing {editModal.startsCount} student attempt(s) on reschedule
            </label>
            <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '4px' }}>
              Checked by default: allows students who already started or took the test to re-attempt in the new window.
            </div>
          </div>
        ) : null}

        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '6px' }}>
          <button className="btn btn-secondary" onClick={() => setEditModal(prev => ({ ...prev, show: false }))}>Cancel</button>
          <button className="btn btn-primary" onClick={handleSaveEditedAssignment}>Save Changes</button>
        </div>
    </ModalShell>
  );
}

export default EditAssignmentModal;
