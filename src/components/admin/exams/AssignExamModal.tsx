'use client';

import React from 'react';
import DateTimeInputDMY from '@/components/DateTimeInputDMY';
import { calculateEndDatetime, toLocalISOString } from '@/lib/dateUtils';
import { Batch } from '@/types/batch.types';
import TargetPicker from './TargetPicker';
import ScheduleTimingInputs from './ScheduleTimingInputs';
import { AttemptDurationControls } from './AttemptDurationControls';

export interface AssignModalState {
  show: boolean;
  examId: string;
  examName: string;
  type: 'objective' | 'subjective';
  targetType: 'batch' | 'student' | 'mixed';
  selectedBatches: Set<string>;
  selectedStudents: Set<string>;
  openMode: 'immediate' | 'scheduled';
  startAtStr: string;
  endAtStr: string;
  attemptLimit: number;
  examDuration?: number;
  normDuration?: number;
  overrideDuration?: boolean;
  isMorningTest?: boolean;
  isEveningTest?: boolean;
  examMode?: 'home' | 'classroom';
  classroomDuration?: number;
  classroomTimePerQ?: number;
  lateEntryRestriction?: boolean;
}

interface AssignExamModalProps {
  assignModal: AssignModalState;
  setAssignModal: React.Dispatch<React.SetStateAction<AssignModalState>>;
  batches: Batch[];
  getStudentsGroupedByBatch: () => {
    grouped: { [batchId: string]: { batchName: string; list: any[] } };
    unassigned: any[];
  };
  handleToggleBatchAssign: (id: string) => void;
  handleToggleStudentAssign: (code: string) => void;
  getMorningTestTimes: (dur: number) => { startStr: string; endStr: string };
  getEveningTestTimes: (dur: number) => { startStr: string; endStr: string };
  handleSaveAssignment: () => void;
  assigning: boolean;
}

function getModalDuration(modal: AssignModalState): number {
  if (modal.type === 'objective') {
    return Number(modal.overrideDuration ? modal.examDuration : modal.normDuration) || 30;
  }
  if (modal.examMode === 'classroom') {
    return Number(modal.classroomDuration) || 45;
  }
  return Number(modal.normDuration) || 60;
}

export function AssignExamModal({
  assignModal,
  setAssignModal,
  batches,
  getStudentsGroupedByBatch,
  handleToggleBatchAssign,
  handleToggleStudentAssign,
  getMorningTestTimes,
  getEveningTestTimes,
  handleSaveAssignment,
  assigning
}: AssignExamModalProps) {
  if (!assignModal.show) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '620px', width: '94%', maxHeight: '90vh', overflowY: 'auto', padding: '20px 24px', display: 'flex', flexDirection: 'column', gap: '12px', boxShadow: 'var(--shadow-lg)' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '12px' }}>
          <div>
            <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0, color: 'var(--text)' }}>
              📋 Assign {assignModal.type === 'objective' ? 'Objective' : 'Subjective'} Exam
            </h3>
            <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '2px', wordBreak: 'break-word', lineHeight: '1.4' }}>
              {assignModal.examName}
            </div>
          </div>
          <button 
            onClick={() => setAssignModal(prev => ({ ...prev, show: false }))} 
            disabled={assigning}
            style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', fontSize: '18px', padding: '2px 6px', borderRadius: '4px' }}
          >
            ✕
          </button>
        </div>

        {assignModal.type === 'subjective' && (
          <div>
            <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '4px' }}>Subjective Exam Mode</label>
            <div style={{ display: 'flex', gap: '15px' }}>
              <label style={{ fontSize: '12px', cursor: 'pointer' }}>
                <input 
                  type="radio" 
                  name="examMode" 
                  checked={assignModal.examMode === 'home'} 
                  onChange={() => setAssignModal(prev => {
                    const dur = Number(prev.normDuration) || 60;
                    return {
                      ...prev,
                      examMode: 'home',
                      endAtStr: prev.startAtStr ? calculateEndDatetime(prev.startAtStr, dur) : prev.endAtStr
                    };
                  })} 
                /> 🏠 Home Mode (Parent review)
              </label>
              <label style={{ fontSize: '12px', cursor: 'pointer' }}>
                <input 
                  type="radio" 
                  name="examMode" 
                  checked={assignModal.examMode === 'classroom'} 
                  onChange={() => setAssignModal(prev => {
                    const dur = Number(prev.classroomDuration) || 45;
                    return {
                      ...prev,
                      examMode: 'classroom',
                      endAtStr: prev.startAtStr ? calculateEndDatetime(prev.startAtStr, dur) : prev.endAtStr
                    };
                  })} 
                /> 🏫 Classroom Mode (Peer Lottery)
              </label>
            </div>
          </div>
        )}

        {assignModal.type === 'subjective' && assignModal.examMode === 'classroom' && (
          <div style={{ background: 'var(--bg-soft)', padding: '8px 12px', borderRadius: 'var(--radius-sm)', borderLeft: '3px solid var(--warning)', fontSize: '11px', display: 'flex', flexDirection: 'column', gap: '6px' }}>
            <strong>Classroom Peer Lottery Settings:</strong>
            <div style={{ display: 'flex', gap: '10px' }}>
              <div>
                <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Duration (mins)</label>
                <input 
                  type="number" 
                  value={assignModal.classroomDuration === undefined || assignModal.classroomDuration === null ? '' : assignModal.classroomDuration} 
                  onChange={(e) => {
                    const raw = e.target.value;
                    if (raw === '') {
                      setAssignModal(prev => ({ ...prev, classroomDuration: '' as any }));
                      return;
                    }
                    const dur = Number(raw);
                    setAssignModal(prev => {
                      let updates: any = { classroomDuration: isNaN(dur) ? '' : dur };
                      if (prev.startAtStr && !isNaN(dur) && dur > 0) {
                        updates.endAtStr = calculateEndDatetime(prev.startAtStr, dur);
                      }
                      return { ...prev, ...updates };
                    });
                  }}
                  onBlur={() => {
                    setAssignModal(prev => {
                      if (!prev.classroomDuration || isNaN(Number(prev.classroomDuration))) {
                        const fallback = 45;
                        return {
                          ...prev,
                          classroomDuration: fallback,
                          endAtStr: prev.startAtStr ? calculateEndDatetime(prev.startAtStr, fallback) : prev.endAtStr
                        };
                      }
                      return prev;
                    });
                  }}
                  style={{ width: '80px', padding: '4px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                />
              </div>
              <div>
                <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Mins per Q</label>
                <input 
                  type="number" 
                  value={assignModal.classroomTimePerQ === undefined || assignModal.classroomTimePerQ === null ? '' : assignModal.classroomTimePerQ} 
                  onChange={(e) => {
                    const raw = e.target.value;
                    setAssignModal(prev => ({ ...prev, classroomTimePerQ: raw === '' ? ('' as any) : Number(raw) }));
                  }}
                  onBlur={() => {
                    if (!assignModal.classroomTimePerQ || isNaN(Number(assignModal.classroomTimePerQ))) {
                      setAssignModal(prev => ({ ...prev, classroomTimePerQ: 3 }));
                    }
                  }}
                  style={{ width: '80px', padding: '4px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                />
              </div>
            </div>
          </div>
        )}

        <div style={{ background: 'var(--surface-sunken)', padding: '10px 12px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
          <TargetPicker
            targetType={assignModal.targetType}
            onChangeTargetType={(type) => setAssignModal(prev => ({ ...prev, targetType: type }))}
            batches={batches}
            selectedBatches={assignModal.selectedBatches}
            onToggleBatch={handleToggleBatchAssign}
            selectedStudents={assignModal.selectedStudents}
            onToggleStudent={handleToggleStudentAssign}
            getStudentsGroupedByBatch={getStudentsGroupedByBatch}
          />
        </div>

        <div>
          <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Availability Slot</label>
          <div style={{ display: 'flex', alignItems: 'center', gap: '15px', marginBottom: '8px', flexWrap: 'wrap' }}>
            <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
              <input 
                type="radio" 
                name="openMode" 
                checked={assignModal.openMode === 'immediate'} 
                onChange={() => setAssignModal(prev => ({ ...prev, openMode: 'immediate', isMorningTest: false, isEveningTest: false }))} 
              /> Immediate
            </label>
            <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap' }}>
              <input 
                type="radio" 
                name="openMode" 
                checked={assignModal.openMode === 'scheduled' && !assignModal.isMorningTest && !assignModal.isEveningTest} 
                onChange={() => setAssignModal(prev => {
                  const dur = getModalDuration(prev);
                  const start = prev.startAtStr || toLocalISOString(new Date());
                  const end = calculateEndDatetime(start, dur);
                  return {
                    ...prev,
                    openMode: 'scheduled',
                    isMorningTest: false,
                    isEveningTest: false,
                    startAtStr: start,
                    endAtStr: end
                  };
                })} 
              /> Scheduled
            </label>
            <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap', background: assignModal.isMorningTest ? 'rgba(52, 152, 219, 0.2)' : 'rgba(52, 152, 219, 0.08)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(52, 152, 219, 0.25)' }}>
              <input 
                type="checkbox" 
                checked={!!assignModal.isMorningTest} 
                onChange={(e) => {
                  const checked = e.target.checked;
                  setAssignModal(prev => {
                    let updates: any = { isMorningTest: checked, isEveningTest: false };
                    if (checked) {
                      updates.openMode = 'scheduled';
                      updates.lateEntryRestriction = true;
                      const duration = (prev.type === 'objective' ? prev.examDuration : (prev.examMode === 'classroom' ? prev.classroomDuration : 60)) || 30;
                      const times = getMorningTestTimes(duration);
                      updates.startAtStr = times.startStr;
                      updates.endAtStr = times.endStr;
                    }
                    return { ...prev, ...updates };
                  });
                }} 
              /> ☀️ 6 AM Test
            </label>
            <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', whiteSpace: 'nowrap', background: assignModal.isEveningTest ? 'rgba(168, 85, 247, 0.2)' : 'rgba(168, 85, 247, 0.08)', padding: '2px 8px', borderRadius: '4px', border: '1px solid rgba(168, 85, 247, 0.25)' }}>
              <input 
                type="checkbox" 
                checked={!!assignModal.isEveningTest} 
                onChange={(e) => {
                  const checked = e.target.checked;
                  setAssignModal(prev => {
                    let updates: any = { isEveningTest: checked, isMorningTest: false };
                    if (checked) {
                      updates.openMode = 'scheduled';
                      updates.lateEntryRestriction = true;
                      const duration = (prev.type === 'objective' ? prev.examDuration : (prev.examMode === 'classroom' ? prev.classroomDuration : 60)) || 30;
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

          <ScheduleTimingInputs
            state={assignModal}
            setState={setAssignModal}
            getDuration={getModalDuration}
            radioNamePrefix="assign"
          />
        </div>

        <AttemptDurationControls
          maxAttempts={assignModal.attemptLimit}
          onChangeMaxAttempts={(val) => setAssignModal(prev => ({ ...prev, attemptLimit: val }))}
          showDuration={assignModal.type === 'objective'}
          overrideDuration={assignModal.overrideDuration}
          examDuration={assignModal.examDuration}
          onChangeOverrideDuration={(checked) => {
            setAssignModal(prev => {
              const dur = checked ? (Number(prev.examDuration) || prev.normDuration || 30) : (prev.normDuration || 30);
              let updates: any = { overrideDuration: checked, examDuration: dur };
              if (prev.startAtStr && dur && dur > 0) {
                updates.endAtStr = calculateEndDatetime(prev.startAtStr, dur);
              }
              return { ...prev, ...updates };
            });
          }}
          onChangeExamDuration={(dur) => {
            setAssignModal(prev => {
              let updates: any = { examDuration: dur };
              if (prev.startAtStr && typeof dur === 'number' && dur > 0) {
                updates.endAtStr = calculateEndDatetime(prev.startAtStr, dur);
              }
              return { ...prev, ...updates };
            });
          }}
          onBlurExamDuration={() => {
            setAssignModal(prev => {
              if (!prev.examDuration || Number(prev.examDuration) < 1) {
                const fallback = prev.normDuration || 30;
                return {
                  ...prev,
                  examDuration: fallback,
                  endAtStr: prev.startAtStr ? calculateEndDatetime(prev.startAtStr, fallback) : prev.endAtStr
                };
              }
              return prev;
            });
          }}
          durationHelperText={!assignModal.overrideDuration && (
            <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>
              Auto-calculated from questions ({assignModal.normDuration} mins standard norm).
            </div>
          )}
        />

        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '6px' }}>
          <button className="btn btn-secondary" onClick={() => setAssignModal(prev => ({ ...prev, show: false }))} disabled={assigning}>Cancel</button>
          <button className="btn btn-primary" onClick={handleSaveAssignment} disabled={assigning}>
            {assigning ? '⏳ Assigning Exam...' : 'Assign Exam'}
          </button>
        </div>
      </div>
    </div>
  );
}

export default AssignExamModal;
