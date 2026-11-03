import { getStudentMode } from '@/types/user.types';
import React from 'react';
import { Batch } from '@/types/batch.types';

export interface TargetPickerProps {
  targetType: 'batch' | 'student' | 'mixed';
  onChangeTargetType: (type: 'batch' | 'student' | 'mixed') => void;
  batches: Batch[];
  selectedBatches: Set<string>;
  onToggleBatch: (batchId: string) => void;
  selectedStudents: Set<string>;
  onToggleStudent: (studentCode: string) => void;
  getStudentsGroupedByBatch: () => {
    grouped: { [batchId: string]: { batchName: string; list: any[] } };
    unassigned: any[];
  };
}

export default function TargetPicker({
  targetType,
  onChangeTargetType,
  batches,
  selectedBatches,
  onToggleBatch,
  selectedStudents,
  onToggleStudent,
  getStudentsGroupedByBatch
}: TargetPickerProps) {
  const { grouped, unassigned } = getStudentsGroupedByBatch();
  const allStudents = [
    ...Object.values(grouped).flatMap(g => g.list),
    ...unassigned
  ];
  // Deduplicate by studentCode
  const uniqueStudents = Array.from(new Map(allStudents.map(s => [s.studentCode, s])).values());
  const limitedStudents = uniqueStudents.filter(s => getStudentMode(s) === 'limited');
  const allLimitedSelected = limitedStudents.length > 0 && limitedStudents.every(s => selectedStudents.has(s.studentCode));

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
        <div>
          <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '4px' }}>
            Assign Target
          </label>
          <div style={{ display: 'flex', gap: '15px' }}>
            <label style={{ fontSize: '12px', cursor: 'pointer' }}>
              <input 
                type="radio" 
                name="targetTypePicker" 
                checked={targetType === 'batch'} 
                onChange={() => onChangeTargetType('batch')} 
              /> 📦 Entire Batches
            </label>
            <label style={{ fontSize: '12px', cursor: 'pointer' }}>
              <input 
                type="radio" 
                name="targetTypePicker" 
                checked={targetType === 'student'} 
                onChange={() => onChangeTargetType('student')} 
              /> 👤 Individual Students
            </label>
            <label style={{ fontSize: '12px', cursor: 'pointer' }}>
              <input 
                type="radio" 
                name="targetTypePicker" 
                checked={targetType === 'mixed'} 
                onChange={() => onChangeTargetType('mixed')} 
              /> 🔀 Mixed (Batches + Students)
            </label>
          </div>
        </div>

        {/* Single Button to Target Mode 3 (Limited) Students */}
        {limitedStudents.length > 0 && (
          <button
            type="button"
            className="btn btn-sm"
            onClick={() => {
              if (targetType === 'batch') {
                onChangeTargetType('student');
              }
              const shouldSelect = !allLimitedSelected;
              limitedStudents.forEach(s => {
                if (shouldSelect) {
                  if (!selectedStudents.has(s.studentCode)) onToggleStudent(s.studentCode);
                } else {
                  if (selectedStudents.has(s.studentCode)) onToggleStudent(s.studentCode);
                }
              });
            }}
            style={{
              padding: '4px 10px',
              fontSize: '11px',
              fontWeight: 800,
              borderRadius: '6px',
              background: allLimitedSelected ? 'var(--warning)' : 'rgba(245, 158, 11, 0.14)',
              color: allLimitedSelected ? '#ffffff' : 'var(--warning, #d97706)',
              border: '1px solid rgba(245, 158, 11, 0.45)',
              cursor: 'pointer',
              display: 'inline-flex',
              alignItems: 'center',
              gap: '4px'
            }}
            title={allLimitedSelected ? 'Deselect all Mode 3 (Limited) students' : 'Select all Mode 3 (Limited) students'}
          >
            <span>◇</span>
            <span>{allLimitedSelected ? 'Deselect' : 'Select'} Mode 3 Students ({limitedStudents.length})</span>
          </button>
        )}
      </div>

      {/* Batches selections */}
      {(targetType === 'batch' || targetType === 'mixed') && (
        <div>
          <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '4px' }}>
            Select Target Batches:
          </label>
          <div style={{ maxHeight: '110px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '6px 8px', display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(180px, 1fr))', gap: '4px' }}>
            {batches.map(b => (
              <label key={b.id} style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px', padding: '2px 0', cursor: 'pointer' }}>
                <input 
                  type="checkbox" 
                  checked={selectedBatches.has(b.id)} 
                  onChange={() => onToggleBatch(b.id)} 
                /> 📦 {b.name}
              </label>
            ))}
          </div>
        </div>
      )}

      {/* Student selections grouped by batch */}
      {(targetType === 'student' || targetType === 'mixed') && (
        <div style={{ marginTop: '6px' }}>
          <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '3px' }}>
            Select Target Students (Grouped by Batch):
          </label>
          <div style={{ maxHeight: '150px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '5px' }}>
            {(() => {
              const elements: React.ReactNode[] = [];

              Object.entries(grouped).forEach(([bid, group]) => {
                if (group.list.length === 0) return;
                elements.push(
                  <div key={`group-hdr-${bid}`} style={{ fontWeight: 'bold', fontSize: '11px', color: 'var(--accent)', marginTop: '6px', paddingBottom: '2px', borderBottom: '1px dashed var(--border-light)' }}>
                    📦 {group.batchName}
                  </div>
                );
                group.list.forEach(s => {
                  const sMode = getStudentMode(s);
                  const modePrefix = sMode === 'autonomous' ? '* ' : (sMode === 'limited' ? '◇ ' : '');
                  elements.push(
                    <label key={`${bid}-${s.studentCode}`} style={{ display: 'block', fontSize: '12px', padding: '2px 0', marginLeft: '12px', cursor: 'pointer' }}>
                      <input 
                        type="checkbox" 
                        checked={selectedStudents.has(s.studentCode)} 
                        onChange={() => onToggleStudent(s.studentCode)} 
                      /> 👤 {modePrefix}{s.name}
                    </label>
                  );
                });
              });

              if (unassigned.length > 0) {
                elements.push(
                  <div key="group-hdr-unassigned" style={{ fontWeight: 'bold', fontSize: '11px', color: 'var(--text-muted)', marginTop: '6px', paddingBottom: '2px', borderBottom: '1px dashed var(--border-light)' }}>
                    👤 Unassigned / No Batch
                  </div>
                );
                unassigned.forEach(s => {
                  const sMode = getStudentMode(s);
                  const modePrefix = sMode === 'autonomous' ? '* ' : (sMode === 'limited' ? '◇ ' : '');
                  elements.push(
                    <label key={`unassigned-${s.studentCode}`} style={{ display: 'block', fontSize: '12px', padding: '2px 0', marginLeft: '12px', cursor: 'pointer' }}>
                      <input 
                        type="checkbox" 
                        checked={selectedStudents.has(s.studentCode)} 
                        onChange={() => onToggleStudent(s.studentCode)} 
                      /> 👤 {modePrefix}{s.name}
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
  );
}
