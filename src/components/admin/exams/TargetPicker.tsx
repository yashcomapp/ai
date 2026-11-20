import { getStudentMode } from '@/types/user.types';
import React, { useState } from 'react';
import { Batch } from '@/types/batch.types';

export interface TargetPickerProps {
  targetType: 'batch' | 'student' | 'mixed';
  onChangeTargetType: (type: 'batch' | 'student' | 'mixed') => void;
  batches: Batch[];
  selectedBatches: Set<string>;
  onToggleBatch: (batchId: string) => void;
  selectedStudents: Set<string>;
  onToggleStudent: (studentCode: string) => void;
  onSelectStudents?: (studentCodes: string[], select: boolean) => void;
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
  onSelectStudents,
  getStudentsGroupedByBatch
}: TargetPickerProps) {
  const [onlyMode3, setOnlyMode3] = useState(true);
  const { grouped, unassigned } = getStudentsGroupedByBatch();

  // If batches are selected, only consider groups from those batches
  const relevantBatches = selectedBatches.size > 0
    ? Object.entries(grouped).filter(([bid]) => selectedBatches.has(bid))
    : Object.entries(grouped);

  const candidateStudents = relevantBatches.flatMap(([_, g]) => g.list);
  const limitedStudents = candidateStudents.filter(s => getStudentMode(s) === 'limited');
  const allLimitedSelected = limitedStudents.length > 0 && limitedStudents.every(s => selectedStudents.has(s.studentCode));

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '6px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', flexWrap: 'wrap' }}>
          <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>
            Assign Target:
          </label>
          <div style={{ display: 'flex', gap: '12px' }}>
            <label style={{ fontSize: '12px', cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
              <input 
                type="radio" 
                name="targetTypePicker" 
                checked={targetType === 'batch'} 
                onChange={() => onChangeTargetType('batch')} 
              /> 📦 Entire Batches
            </label>
            <label style={{ fontSize: '12px', cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
              <input 
                type="radio" 
                name="targetTypePicker" 
                checked={targetType === 'student'} 
                onChange={() => onChangeTargetType('student')} 
              /> 👤 Individual Students
            </label>
            <label style={{ fontSize: '12px', cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
              <input 
                type="radio" 
                name="targetTypePicker" 
                checked={targetType === 'mixed'} 
                onChange={() => onChangeTargetType('mixed')} 
              /> 🔀 Mixed (Batches + Students)
            </label>
          </div>
        </div>

        {/* Single Button to Target Mode 3 (Limited) Students in Selected Batch */}
        {limitedStudents.length > 0 && (
          <button
            type="button"
            className="btn btn-sm"
            onClick={() => {
              if (targetType === 'batch') {
                onChangeTargetType('student');
              }
              const shouldSelect = !allLimitedSelected;
              const codes = limitedStudents.map(s => s.studentCode);
              if (onSelectStudents) {
                onSelectStudents(codes, shouldSelect);
              } else {
                codes.forEach(c => {
                  if (shouldSelect) {
                    if (!selectedStudents.has(c)) onToggleStudent(c);
                  } else {
                    if (selectedStudents.has(c)) onToggleStudent(c);
                  }
                });
              }
            }}
            style={{
              padding: '3px 8px',
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
            title={allLimitedSelected ? 'Deselect Mode 3 (Limited) students in selected batch' : 'Select Mode 3 (Limited) students in selected batch'}
          >
            <span>◇</span>
            <span>{allLimitedSelected ? 'Deselect' : 'Select'} Mode 3 Students ({limitedStudents.length})</span>
          </button>
        )}
      </div>

      {/* Batches selections */}
      <div>
        <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)', marginBottom: '3px' }}>
          {targetType === 'student' ? 'Select Target Batch (to filter students):' : 'Select Target Batches:'}
        </label>
        <div 
          className="no-scrollbar"
          style={{ 
            maxHeight: '68px', 
            overflowY: 'auto', 
            border: '1px solid var(--border-light)', 
            borderRadius: 'var(--radius-sm)', 
            padding: '4px 6px', 
            display: 'grid', 
            gridTemplateColumns: 'repeat(auto-fill, minmax(180px, 1fr))', 
            gap: '2px',
            scrollbarWidth: 'none',
            msOverflowStyle: 'none'
          }}
        >
          {batches.map(b => (
            <label key={b.id} style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '11px', padding: '1px 0', cursor: 'pointer' }}>
              <input 
                type="checkbox" 
                checked={selectedBatches.has(b.id)} 
                onChange={() => onToggleBatch(b.id)} 
              /> 📦 {b.name}
            </label>
          ))}
        </div>
      </div>

      {/* Student selections grouped by selected batch */}
      {(targetType === 'student' || targetType === 'mixed') && (
        <div>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '3px' }}>
            <label style={{ fontSize: '10px', color: 'var(--text-muted)', fontWeight: 600 }}>
              Select Target Students {selectedBatches.size > 0 ? '(Selected Batches Only)' : '(Grouped by Batch)'}:
            </label>
            <label style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', fontSize: '11px', color: 'var(--warning, #d97706)', cursor: 'pointer', fontWeight: 700 }}>
              <input 
                type="checkbox" 
                checked={onlyMode3} 
                onChange={(e) => setOnlyMode3(e.target.checked)} 
              />
              <span>◇ Mode 3 (Limited) Only</span>
            </label>
          </div>

          <div 
            className="no-scrollbar"
            style={{ 
              maxHeight: '110px', 
              overflowY: 'auto', 
              border: '1px solid var(--border-light)', 
              borderRadius: 'var(--radius-sm)', 
              padding: '4px 6px',
              scrollbarWidth: 'none',
              msOverflowStyle: 'none'
            }}
          >
            {(() => {
              if (selectedBatches.size === 0 && batches.length > 0) {
                return (
                  <div style={{ fontSize: '11px', color: 'var(--text-muted)', padding: '8px', textAlign: 'center', fontStyle: 'italic' }}>
                    👈 Select a target batch above to view its Mode 3 students.
                  </div>
                );
              }

              const elements: React.ReactNode[] = [];

              relevantBatches.forEach(([bid, group]) => {
                const list = onlyMode3 ? group.list.filter(s => getStudentMode(s) === 'limited') : group.list;
                const listCodes = list.map((st: any) => st.studentCode);
                const allInListSelected = listCodes.length > 0 && listCodes.every((c: string) => selectedStudents.has(c));

                elements.push(
                  <div key={`group-hdr-${bid}`} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontWeight: 'bold', fontSize: '11px', color: 'var(--accent)', marginTop: '4px', paddingBottom: '2px', borderBottom: '1px dashed var(--border-light)' }}>
                    <span>📦 {group.batchName} ({list.length} student{list.length !== 1 ? 's' : ''})</span>
                    {list.length > 0 && (
                      <button
                        type="button"
                        onClick={() => {
                          if (onSelectStudents) {
                            onSelectStudents(listCodes, !allInListSelected);
                          } else {
                            listCodes.forEach((c: string) => {
                              if (!allInListSelected && !selectedStudents.has(c)) onToggleStudent(c);
                              else if (allInListSelected && selectedStudents.has(c)) onToggleStudent(c);
                            });
                          }
                        }}
                        style={{
                          background: 'none',
                          border: 'none',
                          color: 'var(--primary)',
                          fontSize: '10px',
                          fontWeight: 600,
                          cursor: 'pointer',
                          padding: '0 4px',
                          textDecoration: 'underline'
                        }}
                      >
                        {allInListSelected ? 'Deselect All' : 'Select All'}
                      </button>
                    )}
                  </div>
                );

                if (list.length === 0) {
                  elements.push(
                    <div key={`empty-${bid}`} style={{ fontSize: '11px', color: 'var(--text-muted)', marginLeft: '12px', padding: '2px 0', fontStyle: 'italic' }}>
                      No {onlyMode3 ? 'Mode 3 (Limited)' : ''} students in this batch.
                    </div>
                  );
                } else {
                  list.forEach(s => {
                    const sMode = getStudentMode(s);
                    const modePrefix = sMode === 'autonomous' ? '* ' : (sMode === 'limited' ? '◇ ' : '');
                    elements.push(
                      <label key={`${bid}-${s.studentCode}`} style={{ display: 'block', fontSize: '11px', padding: '1px 0', marginLeft: '12px', cursor: 'pointer' }}>
                        <input 
                          type="checkbox" 
                          checked={selectedStudents.has(s.studentCode)} 
                          onChange={() => onToggleStudent(s.studentCode)} 
                        /> 👤 {modePrefix}{s.name}
                      </label>
                    );
                  });
                }
              });

              if (selectedBatches.size === 0 && unassigned.length > 0) {
                const unassignedList = onlyMode3 ? unassigned.filter(s => getStudentMode(s) === 'limited') : unassigned;
                if (unassignedList.length > 0) {
                  elements.push(
                    <div key="group-hdr-unassigned" style={{ fontWeight: 'bold', fontSize: '11px', color: 'var(--text-muted)', marginTop: '4px', paddingBottom: '2px', borderBottom: '1px dashed var(--border-light)' }}>
                      👤 Unassigned / No Batch ({unassignedList.length})
                    </div>
                  );
                  unassignedList.forEach(s => {
                    const sMode = getStudentMode(s);
                    const modePrefix = sMode === 'autonomous' ? '* ' : (sMode === 'limited' ? '◇ ' : '');
                    elements.push(
                      <label key={`unassigned-${s.studentCode}`} style={{ display: 'block', fontSize: '11px', padding: '1px 0', marginLeft: '12px', cursor: 'pointer' }}>
                        <input 
                          type="checkbox" 
                          checked={selectedStudents.has(s.studentCode)} 
                          onChange={() => onToggleStudent(s.studentCode)} 
                        /> 👤 {modePrefix}{s.name}
                      </label>
                    );
                  });
                }
              }

              return elements.length > 0 ? elements : <div style={{ fontSize: '11px', color: 'var(--text-muted)', padding: '6px 0' }}>No students found.</div>;
            })()}
          </div>
        </div>
      )}
    </div>
  );
}
