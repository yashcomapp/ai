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
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
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
              const { grouped, unassigned } = getStudentsGroupedByBatch();
              const elements: React.ReactNode[] = [];

              Object.entries(grouped).forEach(([bid, group]) => {
                if (group.list.length === 0) return;
                elements.push(
                  <div key={`group-hdr-${bid}`} style={{ fontWeight: 'bold', fontSize: '11px', color: 'var(--accent)', marginTop: '6px', paddingBottom: '2px', borderBottom: '1px dashed var(--border-light)' }}>
                    📦 {group.batchName}
                  </div>
                );
                group.list.forEach(s => {
                  elements.push(
                    <label key={`${bid}-${s.studentCode}`} style={{ display: 'block', fontSize: '12px', padding: '2px 0', marginLeft: '12px', cursor: 'pointer' }}>
                      <input 
                        type="checkbox" 
                        checked={selectedStudents.has(s.studentCode)} 
                        onChange={() => onToggleStudent(s.studentCode)} 
                      /> 👤 {s.name}
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
                  elements.push(
                    <label key={`unassigned-${s.studentCode}`} style={{ display: 'block', fontSize: '12px', padding: '2px 0', marginLeft: '12px', cursor: 'pointer' }}>
                      <input 
                        type="checkbox" 
                        checked={selectedStudents.has(s.studentCode)} 
                        onChange={() => onToggleStudent(s.studentCode)} 
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
  );
}
