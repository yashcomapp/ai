'use client';

import React from 'react';
import DateTimeInputDMY from '@/components/DateTimeInputDMY';

interface Batch {
  id: string;
  name: string;
}

interface Student {
  studentCode: string;
  name: string;
  batchId?: string | null;
  batchIds?: string[];
  rollNumber?: string;
}

export interface EditModalState {
  show: boolean;
  assignmentId: string;
  examId: string;
  examName: string;
  collection: 'batchAssignments' | 'subjectiveAssignments';
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
  lateEntryRestriction?: boolean;
}

interface EditAssignmentModalProps {
  editModal: EditModalState;
  setEditModal: React.Dispatch<React.SetStateAction<EditModalState>>;
  batches: Batch[];
  getStudentsGroupedByBatch: () => {
    grouped: { [batchId: string]: { batchName: string; list: any[] } };
    unassigned: any[];
  };
  handleToggleBatchEdit: (id: string) => void;
  handleToggleStudentEdit: (code: string) => void;
  getMorningTestTimes: (dur: number) => { startStr: string; endStr: string };
  getEveningTestTimes: (dur: number) => { startStr: string; endStr: string };
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
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '620px', width: '94%', maxHeight: '90vh', overflowY: 'auto', padding: '20px 24px', display: 'flex', flexDirection: 'column', gap: '12px', boxShadow: 'var(--shadow-lg)' }}>
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
          <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>Target Audience</label>
          
          <div style={{ display: 'flex', gap: '15px', marginBottom: '8px' }}>
            <label style={{ fontSize: '12px', cursor: 'pointer' }}>
              <input 
                type="radio" 
                name="editTargetType" 
                checked={editModal.targetType === 'batch'} 
                onChange={() => setEditModal(prev => ({ ...prev, targetType: 'batch' }))} 
              /> Batches Only
            </label>
            <label style={{ fontSize: '12px', cursor: 'pointer' }}>
              <input 
                type="radio" 
                name="editTargetType" 
                checked={editModal.targetType === 'student'} 
                onChange={() => setEditModal(prev => ({ ...prev, targetType: 'student' }))} 
              /> Students Only
            </label>
            <label style={{ fontSize: '12px', cursor: 'pointer' }}>
              <input 
                type="radio" 
                name="editTargetType" 
                checked={editModal.targetType === 'mixed'} 
                onChange={() => setEditModal(prev => ({ ...prev, targetType: 'mixed' }))} 
              /> Mixed Audience
            </label>
          </div>

          {/* Batches selections */}
          {(editModal.targetType === 'batch' || editModal.targetType === 'mixed') && (
            <div>
              <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '4px' }}>Select Target Batches:</label>
              <div style={{ maxHeight: '110px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '6px 8px', display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(180px, 1fr))', gap: '4px' }}>
                {batches.map(b => (
                  <label key={b.id} style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px', padding: '2px 0', cursor: 'pointer' }}>
                    <input 
                      type="checkbox" 
                      checked={editModal.selectedBatches.has(b.id)} 
                      onChange={() => handleToggleBatchEdit(b.id)} 
                    /> 📦 {b.name}
                  </label>
                ))}
              </div>
            </div>
          )}

          {/* Student selections grouped by batch */}
          {(editModal.targetType === 'student' || editModal.targetType === 'mixed') && (
            <div style={{ marginTop: '6px' }}>
              <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '3px' }}>Select Target Students (Grouped by Batch):</label>
              <div style={{ maxHeight: '150px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '5px' }}>
                {(() => {
                  const { grouped, unassigned } = getStudentsGroupedByBatch();
                  const elements: React.ReactNode[] = [];

                  Object.entries(grouped).forEach(([bid, group]) => {
                    if (group.list.length === 0) return;
                    elements.push(
                      <div key={`edit-group-hdr-${bid}`} style={{ fontWeight: 'bold', fontSize: '11px', color: 'var(--accent)', marginTop: '6px', paddingBottom: '2px', borderBottom: '1px dashed var(--border-light)' }}>
                        📦 {group.batchName}
                      </div>
                    );
                    group.list.forEach(s => {
                      elements.push(
                        <label key={`edit-${bid}-${s.studentCode}`} style={{ display: 'block', fontSize: '12px', padding: '2px 0', marginLeft: '12px' }}>
                          <input 
                            type="checkbox" 
                            checked={editModal.selectedStudents.has(s.studentCode)} 
                            onChange={() => handleToggleStudentEdit(s.studentCode)} 
                          /> 👤 {s.name}
                        </label>
                      );
                    });
                  });

                  if (unassigned.length > 0) {
                    elements.push(
                      <div key="edit-group-hdr-unassigned" style={{ fontWeight: 'bold', fontSize: '11px', color: 'var(--text-muted)', marginTop: '6px', paddingBottom: '2px', borderBottom: '1px dashed var(--border-light)' }}>
                        👤 Unassigned / No Batch
                      </div>
                    );
                    unassigned.forEach(s => {
                      elements.push(
                        <label key={`edit-unassigned-${s.studentCode}`} style={{ display: 'block', fontSize: '12px', padding: '2px 0', marginLeft: '12px' }}>
                          <input 
                            type="checkbox" 
                            checked={editModal.selectedStudents.has(s.studentCode)} 
                            onChange={() => handleToggleStudentEdit(s.studentCode)} 
                          /> 👤 {s.name}
                        </label>
                      );
                    });
                  }

                  return elements.length > 0 ? elements : <div style={{ fontSize: '11px', color: 'var(--text-muted)', padding: '8px 0' }}>No students found.</div>;
                })()}
              </div>
            </div>
          )}
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
                onChange={() => setEditModal(prev => ({ ...prev, openMode: 'scheduled', isMorningTest: false, isEveningTest: false }))} 
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
          </div>

          {editModal.openMode === 'scheduled' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
              <div style={{ display: 'flex', gap: '10px' }}>
                <div style={{ flex: 1 }}>
                  <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Start Datetime</label>
                  <DateTimeInputDMY 
                    value={editModal.startAtStr}
                    disabled={editModal.isMorningTest || editModal.isEveningTest}
                    onChange={(val) => {
                      const is6or9 = /T(06|21):/.test(val) || val.includes('06:00') || val.includes('21:00');
                      setEditModal(prev => ({ 
                        ...prev, 
                        startAtStr: val, 
                        endAtStr: val,
                        lateEntryRestriction: is6or9 ? true : prev.lateEntryRestriction
                      }));
                    }}
                  />
                </div>
                <div style={{ flex: 1 }}>
                  <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>End Datetime</label>
                  <DateTimeInputDMY 
                    value={editModal.endAtStr}
                    disabled={editModal.isMorningTest || editModal.isEveningTest}
                    onChange={(val) => setEditModal(prev => ({ ...prev, endAtStr: val }))}
                  />
                </div>
              </div>
              {/* Late Entry Restriction Options */}
              <div style={{ marginTop: '2px' }}>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '3px' }}>Late Entry Restriction</label>
                <div style={{ display: 'flex', gap: '15px' }}>
                  <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer' }}>
                    <input 
                      type="radio" 
                      name="editLateEntryRestriction" 
                      checked={editModal.lateEntryRestriction === true} 
                      onChange={() => setEditModal(prev => ({ ...prev, lateEntryRestriction: true }))} 
                      style={{ cursor: 'pointer' }}
                    /> Enforce 5-minute limit
                  </label>
                  <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer' }}>
                    <input 
                      type="radio" 
                      name="editLateEntryRestriction" 
                      checked={editModal.lateEntryRestriction === false} 
                      onChange={() => setEditModal(prev => ({ ...prev, lateEntryRestriction: false }))} 
                      style={{ cursor: 'pointer' }}
                    /> Allow late entry
                  </label>
                </div>
              </div>
            </div>
          )}
        </div>

        <div style={{ display: 'flex', gap: '15px' }}>
          <div style={{ flex: 1 }}>
            <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '4px' }}>Attempt Limit</label>
            <select 
              value={editModal.attemptLimit} 
              onChange={(e) => setEditModal(prev => ({ ...prev, attemptLimit: Number(e.target.value) }))}
              style={{ width: '100%', padding: '5px 6px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)' }}
            >
              <option value={1}>1 Attempt</option>
              <option value={2}>2 Attempts</option>
              <option value={3}>3 Attempts</option>
              <option value={-1}>Unlimited</option>
            </select>
          </div>
          {editModal.collection === 'batchAssignments' && (
            <div style={{ flex: 1 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>
                  Duration (Minutes)
                </label>
                <label style={{ fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', color: editModal.overrideDuration ? 'var(--primary)' : 'var(--text-muted)' }}>
                  <input 
                    type="checkbox" 
                    checked={editModal.overrideDuration} 
                    onChange={(e) => {
                      const checked = e.target.checked;
                      setEditModal(prev => {
                        const dur = checked ? prev.examDuration : prev.normDuration;
                        let updates: any = { overrideDuration: checked, examDuration: dur };
                        if ((prev.isMorningTest || prev.isEveningTest) && prev.startAtStr && dur && dur > 0) {
                          const startDate = new Date(prev.startAtStr);
                          const endDate = new Date(startDate.getTime() + dur * 60000);
                          const endYear = endDate.getFullYear();
                          const endMonth = String(endDate.getMonth() + 1).padStart(2, '0');
                          const endDateStr = String(endDate.getDate()).padStart(2, '0');
                          const endHours = String(endDate.getHours()).padStart(2, '0');
                          const endMinutes = String(endDate.getMinutes()).padStart(2, '0');
                          updates.endAtStr = `${endYear}-${endMonth}-${endDateStr}T${endHours}:${endMinutes}`;
                        }
                        return { ...prev, ...updates };
                      });
                    }}
                    style={{ cursor: 'pointer' }}
                  />
                  <span>Override</span>
                </label>
              </div>
              <input 
                type="number" 
                value={editModal.examDuration === undefined || editModal.examDuration === null ? '' : editModal.examDuration} 
                disabled={!editModal.overrideDuration}
                onChange={(e) => {
                  const raw = e.target.value;
                  if (raw === '') {
                    setEditModal(prev => ({ ...prev, examDuration: '' as any }));
                    return;
                  }
                  const dur = Number(raw);
                  setEditModal(prev => {
                    let updates: any = { examDuration: isNaN(dur) ? '' : dur };
                    if ((prev.isMorningTest || prev.isEveningTest) && prev.startAtStr && !isNaN(dur) && dur > 0) {
                      const startDate = new Date(prev.startAtStr);
                      const endDate = new Date(startDate.getTime() + dur * 60000);
                      const endYear = endDate.getFullYear();
                      const endMonth = String(endDate.getMonth() + 1).padStart(2, '0');
                      const endDateStr = String(endDate.getDate()).padStart(2, '0');
                      const endHours = String(endDate.getHours()).padStart(2, '0');
                      const endMinutes = String(endDate.getMinutes()).padStart(2, '0');
                      updates.endAtStr = `${endYear}-${endMonth}-${endDateStr}T${endHours}:${endMinutes}`;
                    }
                    return { ...prev, ...updates };
                  });
                }}
                onBlur={() => {
                  if (!editModal.examDuration || Number(editModal.examDuration) < 1) {
                    setEditModal(prev => ({ ...prev, examDuration: prev.normDuration || 30 }));
                  }
                }}
                style={{ 
                  width: '100%', 
                  padding: '5px 6px', 
                  background: editModal.overrideDuration ? 'var(--surface)' : 'var(--surface-muted, rgba(255, 255, 255, 0.05))', 
                  color: editModal.overrideDuration ? 'var(--text)' : 'var(--text-muted)', 
                  border: '1px solid var(--border-light)', 
                  borderRadius: 'var(--radius-sm)',
                  cursor: editModal.overrideDuration ? 'text' : 'not-allowed',
                  opacity: editModal.overrideDuration ? 1 : 0.8
                }}
              />
              {!editModal.overrideDuration && (
                <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>
                  Auto-calculated from questions ({editModal.normDuration} mins standard norm).
                </div>
              )}
            </div>
          )}
        </div>

        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '6px' }}>
          <button className="btn btn-secondary" onClick={() => setEditModal(prev => ({ ...prev, show: false }))}>Cancel</button>
          <button className="btn btn-primary" onClick={handleSaveEditedAssignment}>Save Changes</button>
        </div>
      </div>
    </div>
  );
}

export default EditAssignmentModal;
