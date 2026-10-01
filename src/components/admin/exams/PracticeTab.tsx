'use client';

import React from 'react';
import { Batch, Student } from './types';

interface PracticeTabProps {
  batches: Batch[];
  pracBatchFilter: string;
  setPracBatchFilter: (val: string) => void;
  pracSearchName: string;
  setPracSearchName: (val: string) => void;
  loadingPracticeTracks: boolean;
  filteredPracticeBatches: Array<{
    batch: Batch;
    batchStudents: Student[];
    sortedStudents: Student[];
  }>;
  pracSortField: string | null;
  pracSortDir: 'asc' | 'desc';
  handlePracSort: (field: string) => void;
  practiceStats: {
    [studentCode: string]: {
      totalSessions: number;
      questionsAttempted: number;
      avgScore: number;
      lastActive: string | null;
    };
  };
  masteryStats: {
    [studentCode: string]: {
      avgMastery: number;
      avgQuality?: number;
      mastered: number;
      practicing: number;
      needsAttention: number;
    };
  };
  handleRowClick: (student: Student) => void;
  openTopicStatusModal: (
    student: Student,
    filterType: 'mastered' | 'practicing' | 'needsAttention',
    e: React.MouseEvent
  ) => void;
  formatDateDMY: (dateStr: string) => string;
}

export default function PracticeTab({
  batches,
  pracBatchFilter,
  setPracBatchFilter,
  pracSearchName,
  setPracSearchName,
  loadingPracticeTracks,
  filteredPracticeBatches,
  pracSortField,
  pracSortDir,
  handlePracSort,
  practiceStats,
  masteryStats,
  handleRowClick,
  openTopicStatusModal,
  formatDateDMY
}: PracticeTabProps) {
  const renderSortIndicator = (field: string) => {
    if (pracSortField !== field) return <span style={{ color: 'var(--text-faint)', marginLeft: '4px' }}>⇅</span>;
    return pracSortDir === 'asc' ? <span style={{ color: 'var(--accent)', marginLeft: '4px' }}>↑</span> : <span style={{ color: 'var(--accent)', marginLeft: '4px' }}>↓</span>;
  };

  return (
    <div id="practice-tracks-section" style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
      {/* Filters Bar */}
      <div className="card" style={{ padding: '16px 20px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexWrap: 'wrap', gap: '8px', alignItems: 'center' }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', minWidth: '200px' }}>
          <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Filter by Batch</label>
          <select 
            value={pracBatchFilter}
            onChange={(e) => setPracBatchFilter(e.target.value)}
            style={{ padding: '8px 12px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '13px' }}
          >
            <option value="all">All Batches</option>
            {batches.map(b => (
              <option key={b.id} value={b.id}>{b.name}</option>
            ))}
          </select>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', flex: 1, minWidth: '240px' }}>
          <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Search Student</label>
          <input 
            type="text" 
            placeholder="Filter by student name..."
            value={pracSearchName}
            onChange={(e) => setPracSearchName(e.target.value)}
            style={{ padding: '8px 12px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '13px' }}
          />
        </div>
      </div>

      {/* Batches & Student Lists */}
      {loadingPracticeTracks ? (
        <div className="card" style={{ padding: '60px 20px', textAlign: 'center', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
          <div className="spinner" style={{ margin: '0 auto 12px' }}></div>
          <div style={{ color: 'var(--text-muted)', fontSize: '13px', fontWeight: 600 }}>Loading practice tracks and topic mastery...</div>
        </div>
      ) : filteredPracticeBatches.map(({ batch, batchStudents, sortedStudents }) => {
        return (
          <div key={batch.id} className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden', marginBottom: '16px' }}>
            <div style={{ background: 'var(--bg-soft)', padding: '12px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ fontSize: '13px', fontWeight: 'bold', margin: 0, color: 'var(--text)' }}>
                📦 {batch.name} — <span style={{ color: 'var(--accent)' }}>{batchStudents.length} students</span>
              </h4>
            </div>

            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', fontSize: '13px', borderCollapse: 'collapse', textAlign: 'left' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                    <th onClick={() => handlePracSort('student')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                      STUDENT {renderSortIndicator('student')}
                    </th>
                    <th onClick={() => handlePracSort('sessions')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                      SESSIONS {renderSortIndicator('sessions')}
                    </th>
                    <th onClick={() => handlePracSort('questions')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                      QUESTIONS {renderSortIndicator('questions')}
                    </th>
                    <th onClick={() => handlePracSort('score')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                      AVG SCORE {renderSortIndicator('score')}
                    </th>
                    <th onClick={() => handlePracSort('avgMastery')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                      AVG MASTERY {renderSortIndicator('avgMastery')}
                    </th>
                    <th onClick={() => handlePracSort('avgQuality')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                      QUALITY {renderSortIndicator('avgQuality')}
                    </th>
                    <th onClick={() => handlePracSort('masteryStats')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                      STATUS {renderSortIndicator('masteryStats')}
                    </th>
                    <th onClick={() => handlePracSort('active')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                      LAST SEEN {renderSortIndicator('active')}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {sortedStudents.length === 0 ? (
                    <tr>
                      <td colSpan={8} style={{ padding: '24px', textAlign: 'center', color: 'var(--text-muted)' }}>No students found in this batch.</td>
                    </tr>
                  ) : (
                    sortedStudents.map(student => {
                      const stats = practiceStats[student.studentCode] || { totalSessions: 0, questionsAttempted: 0, avgScore: 0, lastActive: null };
                      const mastery = masteryStats[student.studentCode] || { avgMastery: 0, avgQuality: 100, mastered: 0, practicing: 0, needsAttention: 0 };
                      const quality = mastery.avgQuality ?? 100;
                      return (
                        <tr 
                          key={student.studentCode} 
                          onClick={() => handleRowClick(student)}
                          className="hover-row"
                          style={{ borderBottom: '1px solid var(--border-light)', cursor: 'pointer', transition: 'background 0.2s' }}
                        >
                          <td style={{ padding: '12px 16px', fontWeight: 'bold' }}>{student.name}</td>
                          <td style={{ padding: '12px 16px', textAlign: 'center' }}>{stats.totalSessions}</td>
                          <td style={{ padding: '12px 16px', textAlign: 'center' }}>{stats.questionsAttempted}</td>
                          <td style={{ padding: '12px 16px', fontWeight: 'bold', color: stats.totalSessions > 0 ? 'var(--accent)' : 'inherit' }}>
                            {stats.totalSessions > 0 ? `${stats.avgScore}%` : '—'}
                          </td>
                          <td style={{ padding: '12px 16px', fontWeight: 'bold' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                              <span style={{ width: '28px' }}>{mastery.avgMastery}%</span>
                              <div style={{ width: '40px', height: '6px', background: 'var(--bg-soft)', borderRadius: '3px', overflow: 'hidden' }}>
                                <div style={{
                                  width: `${mastery.avgMastery}%`,
                                  height: '100%',
                                  background: mastery.avgMastery >= 90 ? 'var(--success)' : mastery.avgMastery >= 50 ? 'var(--warning)' : 'var(--danger)'
                                }} />
                              </div>
                            </div>
                          </td>
                          <td style={{ padding: '12px 16px', fontWeight: 'bold' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                              <span style={{ width: '28px' }}>{quality}%</span>
                              <div style={{ width: '40px', height: '6px', background: 'var(--bg-soft)', borderRadius: '3px', overflow: 'hidden' }}>
                                <div style={{
                                  width: `${quality}%`,
                                  height: '100%',
                                  background: quality >= 80 ? 'var(--success)' : quality >= 50 ? 'var(--warning)' : 'var(--danger)'
                                }} />
                              </div>
                            </div>
                          </td>
                          <td style={{ padding: '12px 16px', whiteSpace: 'nowrap' }}>
                            <span 
                              onClick={(e) => openTopicStatusModal(student, 'mastered', e)} 
                              style={{ color: 'var(--success)', fontWeight: 700, cursor: 'pointer', padding: '3px 8px', borderRadius: '6px', background: 'rgba(16,185,129,0.12)', border: '1px solid rgba(16,185,129,0.25)', transition: 'all 0.15s' }} 
                              title="Click to view Mastered Topics (>=90% accuracy & target confidence)"
                            >
                              🟢 {mastery.mastered}
                            </span>
                            <span 
                              onClick={(e) => openTopicStatusModal(student, 'practicing', e)} 
                              style={{ color: 'var(--warning)', fontWeight: 700, marginLeft: '6px', cursor: 'pointer', padding: '3px 8px', borderRadius: '6px', background: 'rgba(245,158,11,0.12)', border: '1px solid rgba(245,158,11,0.25)', transition: 'all 0.15s' }} 
                              title="Click to view Practicing / In Progress Topics (50-89% or low confidence)"
                            >
                              🟡 {mastery.practicing}
                            </span>
                            <span 
                              onClick={(e) => openTopicStatusModal(student, 'needsAttention', e)} 
                              style={{ color: 'var(--danger)', fontWeight: 700, marginLeft: '6px', cursor: 'pointer', padding: '3px 8px', borderRadius: '6px', background: 'rgba(239,68,68,0.12)', border: '1px solid rgba(239,68,68,0.25)', transition: 'all 0.15s' }} 
                              title="Click to view Needs Care / Focus Topics (<50%)"
                            >
                              🔴 {mastery.needsAttention}
                            </span>
                          </td>
                          <td style={{ padding: '12px 16px', color: 'var(--text-muted)' }}>
                            {stats.lastActive ? formatDateDMY(stats.lastActive) : 'Never'}
                          </td>
                        </tr>
                      );
                    })
                  )}
                </tbody>
              </table>
            </div>
          </div>
        );
      })}
    </div>
  );
}
