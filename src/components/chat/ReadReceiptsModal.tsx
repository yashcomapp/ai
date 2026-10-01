'use client';

import React from 'react';

export interface ReadReceiptsModalProps {
  receiptsModalMessage: any;
  setReceiptsModalMessage: (msg: any) => void;
  participantNames: Record<string, string>;
  studentsList: any[];
  firebaseUser: any;
}

export function ReadReceiptsModal({
  receiptsModalMessage,
  setReceiptsModalMessage,
  participantNames,
  studentsList,
  firebaseUser,
}: ReadReceiptsModalProps) {
  if (!receiptsModalMessage) return null;

  const parseReadReceiptTime = (timeVal: any): string => {
    if (!timeVal) return '—';
    let dateObj: Date | null = null;
    
    if (typeof timeVal === 'string') {
      dateObj = new Date(timeVal);
    } else if (typeof timeVal === 'object') {
      if (typeof timeVal.seconds === 'number') {
        dateObj = new Date(timeVal.seconds * 1000);
      } else {
        let currentVal = timeVal;
        while (currentVal && typeof currentVal === 'object' && !Array.isArray(currentVal)) {
          if (typeof currentVal.seconds === 'number') {
            dateObj = new Date(currentVal.seconds * 1000);
            break;
          }
          const keys = Object.keys(currentVal);
          if (keys.length === 0) break;
          currentVal = currentVal[keys[0]];
        }
        if (typeof currentVal === 'string') {
          dateObj = new Date(currentVal);
        }
      }
    }
    
    if (!dateObj || isNaN(dateObj.getTime())) {
      return '—';
    }
    
    const day = String(dateObj.getDate()).padStart(2, '0');
    const month = String(dateObj.getMonth() + 1).padStart(2, '0');
    const datePart = `${day}/${month}/${dateObj.getFullYear()}`;
    return dateObj.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) + ' ' + datePart;
  };

  const readBy = receiptsModalMessage.readBy || {};
  const details: Array<{ name: string; role: string; time: string }> = [];

  Object.entries(readBy).forEach(([uid, timeStr]) => {
    if (uid === receiptsModalMessage.senderId) return;
    let name = participantNames[uid] || uid;
    let role = 'student';
    
    if (uid.toLowerCase() === 'admin' || uid === firebaseUser?.uid) {
      name = participantNames['admin'] || 'Admin';
      role = 'admin';
    } else if (uid.startsWith('PR-')) {
      role = 'parent';
      const emailOrId = uid.substring(3).toLowerCase().trim();
      let student = studentsList.find((s: any) => s.parentEmail?.toLowerCase().trim() === emailOrId);
      if (!student) {
        student = studentsList.find((s: any) => s.studentCode === emailOrId);
      }
      if (student) {
        name = `${student.name} (Parent)`;
      } else if (name === uid || name.includes('@')) {
        name = 'Parent (P)';
      }
    } else {
      const student = studentsList.find((s: any) => s.studentCode === uid);
      if (student) {
        name = student.name;
      } else if (name === uid || name.includes('@') || /^ST-\d{4}-\d+$/i.test(name)) {
        name = 'Student';
      }
    }

    details.push({
      name,
      role,
      time: parseReadReceiptTime(timeStr)
    });
  });

  return (
    <div style={{
      position: 'fixed',
      inset: 0,
      background: 'rgba(0, 0, 0, 0.6)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 10000,
      backdropFilter: 'blur(4px)',
      padding: '16px'
    }}>
      <div style={{
        background: 'var(--surface-popover)',
        border: '1px solid var(--border)',
        borderRadius: '12px',
        padding: '20px',
        width: '340px',
        display: 'flex',
        flexDirection: 'column',
        gap: '12px',
        maxHeight: '80%',
        overflowY: 'auto'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h4 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold', color: 'var(--text)' }}>✔️ Message Info (Read Receipts)</h4>
          <button 
            onClick={() => setReceiptsModalMessage(null)}
            style={{ background: 'transparent', border: 'none', color: 'var(--text-muted)', fontSize: '16px', cursor: 'pointer' }}
          >
            ×
          </button>
        </div>
        
        <div style={{ padding: '10px', background: 'var(--surface-2)', borderRadius: '8px', fontSize: '12.5px', border: '1px solid var(--border)' }}>
          <div style={{ color: 'var(--text-muted)', fontSize: '10px', textTransform: 'uppercase', marginBottom: '4px', fontWeight: 'bold' }}>Message Text</div>
          <div style={{ wordBreak: 'break-word', color: 'var(--text)' }}>{receiptsModalMessage.text}</div>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginTop: '4px' }}>
          <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 'bold', textTransform: 'uppercase' }}>Read By</span>
          
          {details.length === 0 ? (
            <div style={{ fontSize: '12px', color: 'var(--text-muted)', fontStyle: 'italic', textAlign: 'center', padding: '10px 0' }}>No one has read this message yet.</div>
          ) : (
            details.map((reader, index) => (
              <div key={index} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '6px 0', borderBottom: '1px solid var(--border)' }}>
                <div style={{ display: 'flex', flexDirection: 'column' }}>
                  <span style={{ fontSize: '12.5px', fontWeight: 600, color: 'var(--text)' }}>{reader.name}</span>
                  <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>{reader.role.toUpperCase()}</span>
                </div>
                <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>{reader.time}</span>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default ReadReceiptsModal;
