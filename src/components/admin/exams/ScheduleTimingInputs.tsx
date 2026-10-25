'use client';

import React from 'react';
import DateTimeInputDMY from '@/components/DateTimeInputDMY';
import { calculateEndDatetime } from '@/lib/dateUtils';

export interface ScheduleTimingModalState {
  openMode: 'immediate' | 'scheduled';
  startAtStr: string;
  endAtStr: string;
  isMorningTest?: boolean;
  isEveningTest?: boolean;
  lateEntryRestriction?: boolean;
  [key: string]: any;
}

export interface ScheduleTimingInputsProps<T extends ScheduleTimingModalState> {
  state: T;
  setState: React.Dispatch<React.SetStateAction<T>>;
  getDuration: (state: T) => number;
  radioNamePrefix?: string;
}

export function ScheduleTimingInputs<T extends ScheduleTimingModalState>({
  state,
  setState,
  getDuration,
  radioNamePrefix = ''
}: ScheduleTimingInputsProps<T>) {
  if (state.openMode !== 'scheduled') return null;

  const radioName = `${radioNamePrefix}lateEntryRestriction`;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
      <div style={{ display: 'flex', gap: '10px' }}>
        <div style={{ flex: 1 }}>
          <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>Start Datetime</label>
          <DateTimeInputDMY 
            value={state.startAtStr}
            disabled={state.isMorningTest || state.isEveningTest}
            onChange={(val) => {
              const is6or9 = /T(06|21):/.test(val) || val.includes('06:00') || val.includes('21:00');
              setState(prev => {
                const dur = getDuration(prev);
                return { 
                  ...prev, 
                  startAtStr: val, 
                  endAtStr: calculateEndDatetime(val, dur),
                  lateEntryRestriction: is6or9 ? true : prev.lateEntryRestriction
                };
              });
            }}
          />
        </div>
        <div style={{ flex: 1 }}>
          <label style={{ display: 'block', fontSize: '10px', color: 'var(--text-muted)' }}>End Datetime</label>
          <DateTimeInputDMY 
            value={state.endAtStr}
            disabled={state.isMorningTest || state.isEveningTest}
            onChange={(val) => setState(prev => ({ ...prev, endAtStr: val }))}
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
              name={radioName} 
              checked={state.lateEntryRestriction === true} 
              onChange={() => setState(prev => ({ ...prev, lateEntryRestriction: true }))} 
              style={{ cursor: 'pointer' }}
            /> Enforce 5-minute limit
          </label>
          <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer' }}>
            <input 
              type="radio" 
              name={radioName} 
              checked={state.lateEntryRestriction === false} 
              onChange={() => setState(prev => ({ ...prev, lateEntryRestriction: false }))} 
              style={{ cursor: 'pointer' }}
            /> Allow late entry
          </label>
        </div>
      </div>
    </div>
  );
}

export default ScheduleTimingInputs;
