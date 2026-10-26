'use client';

import React, { useState } from 'react';
import { Batch, Student } from './types';
import { formatReportStudentName, exportBatchPracticeTracksImage, computeBatchMaxTopics } from '@/lib/lqCardExport';
import { getDateKeyIST } from '@/lib/dateUtils';

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
      examAvg?: number;
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
      efforts?: number;
      totalAssigned?: number;
    };
  };
  weeklyStats?: Record<string, {
    days: Record<string, { questionsCount: number; sessionsCount: number; avgScore: number; correctCount: number }>;
    totalQuestions: number;
    totalSessions: number;
    activeDays: number;
    avgScore: number;
    activeDates: string[];
  }>;
  weekDays?: Array<{ dateKey: string; label: string; shortLabel: string; dayName: string; isToday: boolean }>;
  handleRowClick: (student: Student) => void;
  openTopicStatusModal: (
    student: Student,
    filterType: 'mastered' | 'practicing' | 'needsAttention' | 'all',
    e: React.MouseEvent
  ) => void;
  formatDateDMY: (dateStr: string) => string;
  onSelectDuration?: (options?: {
    days?: number;
    startDate?: string;
    endDate?: string;
  }) => Promise<void> | void;
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
  weeklyStats = {},
  weekDays = [],
  handleRowClick,
  openTopicStatusModal,
  formatDateDMY,
  onSelectDuration
}: PracticeTabProps) {
  const [exportingBatchId, setExportingBatchId] = useState<string | null>(null);
  const [viewMode, setViewMode] = useState<'weekly' | 'cumulative'>('weekly');
  const [durationPreset, setDurationPreset] = useState<'7d' | '14d' | '30d' | 'thisMonth' | 'custom' | 'cumulative'>('7d');
  const [customStartDate, setCustomStartDate] = useState(() => {
    const d = new Date();
    d.setDate(d.getDate() - 6);
    return getDateKeyIST(d);
  });
  const [customEndDate, setCustomEndDate] = useState(() => getDateKeyIST(new Date()));

  const handlePresetChange = (preset: '7d' | '14d' | '30d' | 'thisMonth' | 'custom' | 'cumulative') => {
    setDurationPreset(preset);
    if (preset === 'cumulative') {
      setViewMode('cumulative');
      return;
    }

    setViewMode('weekly');

    if (preset === '7d') {
      onSelectDuration?.({ days: 7 });
    } else if (preset === '14d') {
      onSelectDuration?.({ days: 14 });
    } else if (preset === '30d') {
      onSelectDuration?.({ days: 30 });
    } else if (preset === 'thisMonth') {
      const now = new Date();
      const firstDay = new Date(now.getFullYear(), now.getMonth(), 1);
      const startKey = getDateKeyIST(firstDay);
      const endKey = getDateKeyIST(now);
      onSelectDuration?.({ startDate: startKey, endDate: endKey });
    } else if (preset === 'custom') {
      if (customStartDate && customEndDate) {
        onSelectDuration?.({ startDate: customStartDate, endDate: customEndDate });
      }
    }
  };

  const handleApplyCustomRange = () => {
    if (!customStartDate || !customEndDate) {
      alert('Please select both from and to dates.');
      return;
    }
    if (customStartDate > customEndDate) {
      alert('Start date must be before or equal to end date.');
      return;
    }
    setViewMode('weekly');
    onSelectDuration?.({ startDate: customStartDate, endDate: customEndDate });
  };

  const getPresetBtnStyle = (isActive: boolean) => ({
    padding: '6px 12px',
    fontSize: '12px',
    fontWeight: 700,
    borderRadius: '4px',
    border: 'none',
    cursor: 'pointer',
    background: isActive ? 'var(--primary)' : 'transparent',
    color: isActive ? '#ffffff' : 'var(--text-muted)',
    transition: 'all 0.2s'
  });

  const renderSortIndicator = (field: string) => {
    if (pracSortField !== field) return <span style={{ color: 'var(--text-faint)', marginLeft: '4px' }}>⇅</span>;
    return pracSortDir === 'asc' ? <span style={{ color: 'var(--accent)', marginLeft: '4px' }}>↑</span> : <span style={{ color: 'var(--accent)', marginLeft: '4px' }}>↓</span>;
  };

  return (
    <div id="practice-tracks-section" style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
      {/* Filters & Duration Bar */}
      <div className="card" style={{ padding: '16px 20px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '14px' }}>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '12px', alignItems: 'center' }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', minWidth: '180px' }}>
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

          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', flex: 1, minWidth: '220px' }}>
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

        {/* View Mode & Flexible Duration Switcher */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', borderTop: '1px solid var(--border-light)', paddingTop: '12px' }}>
          <div style={{ display: 'flex', flexWrap: 'wrap', alignItems: 'center', justifyContent: 'space-between', gap: '8px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
              <span style={{ fontSize: '11.5px', fontWeight: 700, color: 'var(--text-muted)', marginRight: '2px' }}>
                DURATION / VIEW:
              </span>
              <div style={{ display: 'inline-flex', flexWrap: 'wrap', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', padding: '3px', border: '1px solid var(--border)', gap: '2px' }}>
                <button
                  type="button"
                  onClick={() => handlePresetChange('7d')}
                  style={getPresetBtnStyle(durationPreset === '7d')}
                >
                  📅 Last 7 Days
                </button>
                <button
                  type="button"
                  onClick={() => handlePresetChange('14d')}
                  style={getPresetBtnStyle(durationPreset === '14d')}
                >
                  📅 Last 14 Days
                </button>
                <button
                  type="button"
                  onClick={() => handlePresetChange('30d')}
                  style={getPresetBtnStyle(durationPreset === '30d')}
                >
                  📅 Last 30 Days
                </button>
                <button
                  type="button"
                  onClick={() => handlePresetChange('thisMonth')}
                  style={getPresetBtnStyle(durationPreset === 'thisMonth')}
                >
                  🗓️ This Month
                </button>
                <button
                  type="button"
                  onClick={() => handlePresetChange('custom')}
                  style={getPresetBtnStyle(durationPreset === 'custom')}
                >
                  ⚙️ Custom Range
                </button>
                <button
                  type="button"
                  onClick={() => handlePresetChange('cumulative')}
                  style={getPresetBtnStyle(durationPreset === 'cumulative')}
                >
                  📊 All-Time Cumulative
                </button>
              </div>
            </div>

            {/* Active Range Chip */}
            {durationPreset !== 'cumulative' && weekDays.length > 0 && (
              <div style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: '6px',
                background: 'rgba(56, 189, 248, 0.08)',
                color: 'var(--accent)',
                border: '1px solid rgba(56, 189, 248, 0.25)',
                padding: '4px 10px',
                borderRadius: '6px',
                fontSize: '11.5px',
                fontWeight: 700
              }}>
                <span>📅</span>
                <span>{weekDays[0].label} – {weekDays[weekDays.length - 1].label}</span>
                <span style={{ background: 'var(--accent)', color: '#fff', borderRadius: '10px', padding: '1px 7px', fontSize: '10.5px' }}>
                  {weekDays.length} Days
                </span>
              </div>
            )}
          </div>

          {/* Custom Date Range Selector (displayed when 'custom' is selected) */}
          {durationPreset === 'custom' && (
            <div style={{
              display: 'flex',
              alignItems: 'center',
              flexWrap: 'wrap',
              gap: '10px',
              padding: '10px 14px',
              background: 'var(--bg-soft)',
              borderRadius: 'var(--radius-sm)',
              border: '1px dashed var(--border)',
              marginTop: '4px'
            }}>
              <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text)' }}>🗓️ Select Custom Date Range:</span>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>From:</label>
                <input
                  type="date"
                  value={customStartDate}
                  onChange={(e) => setCustomStartDate(e.target.value)}
                  style={{
                    padding: '5px 8px',
                    border: '1px solid var(--border)',
                    borderRadius: '4px',
                    background: 'var(--surface)',
                    color: 'var(--text)',
                    fontSize: '12px'
                  }}
                />
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>To:</label>
                <input
                  type="date"
                  value={customEndDate}
                  onChange={(e) => setCustomEndDate(e.target.value)}
                  style={{
                    padding: '5px 8px',
                    border: '1px solid var(--border)',
                    borderRadius: '4px',
                    background: 'var(--surface)',
                    color: 'var(--text)',
                    fontSize: '12px'
                  }}
                />
              </div>
              <button
                type="button"
                onClick={handleApplyCustomRange}
                disabled={loadingPracticeTracks}
                style={{
                  padding: '5px 14px',
                  background: 'var(--primary)',
                  color: '#ffffff',
                  border: 'none',
                  borderRadius: '4px',
                  fontSize: '12px',
                  fontWeight: 700,
                  cursor: 'pointer'
                }}
              >
                {loadingPracticeTracks ? '⏳ Loading...' : 'Apply Range'}
              </button>
            </div>
          )}
        </div>
      </div>

      {/* Batches & Student Lists */}
      {loadingPracticeTracks ? (
        <div className="card" style={{ padding: '60px 20px', textAlign: 'center', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
          <div className="spinner" style={{ margin: '0 auto 12px' }}></div>
          <div style={{ color: 'var(--text-muted)', fontSize: '13px', fontWeight: 600 }}>Loading practice tracks and topic mastery...</div>
        </div>
      ) : filteredPracticeBatches.map(({ batch, batchStudents, sortedStudents }) => {
        // Find the batch-level conducted/assigned topic count across all batch students
        const batchMaxTopics = computeBatchMaxTopics(batchStudents, masteryStats);

        return (
          <div key={batch.id} className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden', marginBottom: '16px' }}>
            <div style={{ background: 'var(--bg-soft)', padding: '10px 14px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ fontSize: '13px', fontWeight: 'bold', margin: 0, color: 'var(--text)' }}>
                📦 {batch.name} — <span style={{ color: 'var(--accent)' }}>{batchStudents.length} students</span>
                {viewMode === 'weekly' && weekDays.length > 0 && (
                  <span style={{ fontSize: '11.5px', color: 'var(--text-muted)', fontWeight: 600, marginLeft: '8px' }}>
                    ({weekDays[0].label} – {weekDays[weekDays.length - 1].label}) • {weekDays.length} Days
                  </span>
                )}
              </h4>
              <button
                onClick={async (e) => {
                  e.stopPropagation();
                  setExportingBatchId(batch.id);
                  try {
                    await exportBatchPracticeTracksImage({
                      batchName: batch.name,
                      students: sortedStudents,
                      practiceStats,
                      masteryStats,
                      weeklyStats: viewMode === 'weekly' ? weeklyStats : undefined,
                      weekDays: viewMode === 'weekly' ? weekDays : undefined,
                      formatDateDMY
                    });
                  } catch (err: any) {
                    console.error('Batch practice export failed:', err);
                  } finally {
                    setExportingBatchId(null);
                  }
                }}
                disabled={exportingBatchId === batch.id || sortedStudents.length === 0}
                className="btn btn-secondary btn-sm"
                style={{
                  padding: '5px 14px',
                  fontSize: '12px',
                  fontWeight: 700,
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '6px',
                  background: 'var(--surface)',
                  border: '1px solid var(--border)',
                  cursor: 'pointer',
                  borderRadius: '6px'
                }}
                title={viewMode === 'weekly' ? `Export ${weekDays.length}-day day-wise practice report image for WhatsApp` : "Export cumulative practice dossier for WhatsApp"}
              >
                {exportingBatchId === batch.id ? '⏳ Exporting...' : (viewMode === 'weekly' ? `📸 Export ${weekDays.length}D Report (WhatsApp)` : '📸 Export WhatsApp')}
              </button>
            </div>

            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', fontSize: '13px', borderCollapse: 'collapse', textAlign: 'left' }}>
                <thead>
                  {viewMode === 'weekly' ? (
                    <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                      <th onClick={() => handlePracSort('student')} style={{ padding: '8px 10px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        STUDENT {renderSortIndicator('student')}
                      </th>
                      {weekDays.map(wd => (
                        <th key={wd.dateKey} style={{ padding: '8px 4px', textAlign: 'center', whiteSpace: 'nowrap', minWidth: '50px', background: wd.isToday ? 'rgba(56, 189, 248, 0.1)' : undefined }}>
                          <div style={{ fontSize: '11px', fontWeight: 800, color: wd.isToday ? 'var(--accent)' : 'inherit' }}>{wd.shortLabel}</div>
                          <div style={{ fontSize: '10px', fontWeight: 600, color: 'var(--text-muted)' }}>{wd.label.split(' ')[1] || ''}</div>
                        </th>
                      ))}
                      <th onClick={() => handlePracSort('weeklyQuestions')} style={{ padding: '8px 8px', textAlign: 'center', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        {weekDays.length}D TOTAL {renderSortIndicator('weeklyQuestions')}
                      </th>
                      <th onClick={() => handlePracSort('weeklyActive')} style={{ padding: '8px 8px', textAlign: 'center', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        ACTIVE ({weekDays.length}d) {renderSortIndicator('weeklyActive')}
                      </th>
                      <th onClick={() => handlePracSort('weeklyScore')} style={{ padding: '8px 8px', textAlign: 'center', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        ACCURACY {renderSortIndicator('weeklyScore')}
                      </th>
                      <th onClick={() => handlePracSort('masteryStats')} style={{ padding: '8px 10px', textAlign: 'center', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        TOPIC STATUS {renderSortIndicator('masteryStats')}
                      </th>
                      <th style={{ padding: '8px 10px', textAlign: 'center', whiteSpace: 'nowrap' }}>
                        ACTION
                      </th>
                    </tr>
                  ) : (
                    <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                      <th onClick={() => handlePracSort('student')} style={{ padding: '6px 10px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        STUDENT {renderSortIndicator('student')}
                      </th>
                      <th onClick={() => handlePracSort('sessions')} style={{ padding: '6px 10px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        SESSIONS {renderSortIndicator('sessions')}
                      </th>
                      <th onClick={() => handlePracSort('questions')} style={{ padding: '6px 10px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        QUESTIONS {renderSortIndicator('questions')}
                      </th>
                      <th onClick={() => handlePracSort('score')} style={{ padding: '6px 10px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        PRACTICE AVG {renderSortIndicator('score')}
                      </th>
                      <th onClick={() => handlePracSort('avgMastery')} style={{ padding: '6px 10px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        AVG MASTERY {renderSortIndicator('avgMastery')}
                      </th>
                      <th onClick={() => handlePracSort('efforts')} style={{ padding: '6px 10px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        EFFORTS {renderSortIndicator('efforts')}
                      </th>
                      <th onClick={() => handlePracSort('avgQuality')} style={{ padding: '6px 10px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        QUALITY {renderSortIndicator('avgQuality')}
                      </th>
                      <th onClick={() => handlePracSort('masteryStats')} style={{ padding: '6px 10px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        STATUS {renderSortIndicator('masteryStats')}
                      </th>
                      <th onClick={() => handlePracSort('active')} style={{ padding: '6px 10px', cursor: 'pointer', userSelect: 'none', whiteSpace: 'nowrap' }}>
                        LAST SEEN {renderSortIndicator('active')}
                      </th>
                      <th style={{ padding: '6px 10px', textAlign: 'center', whiteSpace: 'nowrap' }}>
                        ACTION
                      </th>
                    </tr>
                  )}
                </thead>
                <tbody>
                  {sortedStudents.length === 0 ? (
                    <tr>
                      <td colSpan={viewMode === 'weekly' ? (weekDays.length + 5) : 10} style={{ padding: '16px', textAlign: 'center', color: 'var(--text-muted)' }}>No students found in this batch.</td>
                    </tr>
                  ) : (
                    sortedStudents.map(student => {
                      const stats = practiceStats[student.studentCode] || { totalSessions: 0, questionsAttempted: 0, avgScore: 0, lastActive: null };
                      const mastery = masteryStats[student.studentCode] || { avgMastery: 0, avgQuality: 100, mastered: 0, practicing: 0, needsAttention: 0 };
                      const rawAssigned = (mastery.mastered + mastery.practicing + mastery.needsAttention);
                      const targetTotal = mastery.totalAssigned || (batchMaxTopics > 0 ? batchMaxTopics : rawAssigned);
                      const adjustedNeedsAttention = mastery.needsAttention;
                      const efforts = mastery.efforts ?? (targetTotal > 0 ? Math.min(100, Math.round((stats.totalSessions / targetTotal) * 100)) : 0);
                      const quality = mastery.avgQuality ?? 100;
                      const formattedName = formatReportStudentName(student.name);

                      if (viewMode === 'weekly') {
                        const w = weeklyStats[student.studentCode] || { days: {}, totalQuestions: 0, totalSessions: 0, activeDays: 0, avgScore: 0 };

                        return (
                          <tr 
                            key={student.studentCode} 
                            onClick={() => handleRowClick(student)}
                            className="hover-row"
                            style={{ borderBottom: '1px solid var(--border-light)', cursor: 'pointer', transition: 'background 0.2s', height: '46px' }}
                          >
                            <td style={{ padding: '6px 10px' }}>
                              <div style={{ fontWeight: 800, fontSize: '13px', color: 'var(--text)' }}>{formattedName}</div>
                              <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', fontWeight: 600 }}>
                                {student.className || student.class || 'Batch'} {student.rollNumber ? `• Roll ${student.rollNumber}` : ''}
                              </div>
                            </td>
                            {weekDays.map(wd => {
                              const dayData = w.days?.[wd.dateKey];
                              const hasPrac = dayData && dayData.sessionsCount > 0;
                              return (
                                <td key={wd.dateKey} style={{ padding: '4px 6px', textAlign: 'center', background: wd.isToday ? 'rgba(56, 189, 248, 0.05)' : undefined }}>
                                  {hasPrac ? (
                                    <div>
                                      <div style={{ fontWeight: 800, fontSize: '12px', color: 'var(--text)' }}>
                                        {dayData.questionsCount} <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>Qs</span>
                                      </div>
                                      <div style={{
                                        fontSize: '10px',
                                        fontWeight: 800,
                                        color: dayData.avgScore >= 80 ? 'var(--success)' : dayData.avgScore >= 50 ? 'var(--warning)' : 'var(--danger)'
                                      }}>
                                        {dayData.avgScore}%
                                      </div>
                                    </div>
                                  ) : (
                                    <span style={{ color: 'var(--text-faint)', fontWeight: 700 }}>—</span>
                                  )}
                                </td>
                              );
                            })}
                            <td style={{ padding: '6px 8px', textAlign: 'center', background: 'var(--bg-soft)' }}>
                              <div style={{ fontWeight: 900, fontSize: '13px', color: 'var(--accent)' }}>
                                {w.totalQuestions} <span style={{ fontSize: '10.5px', fontWeight: 600 }}>Qs</span>
                              </div>
                              <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', fontWeight: 600 }}>
                                {w.totalSessions} sess
                              </div>
                            </td>
                            <td style={{ padding: '6px 8px', textAlign: 'center' }}>
                              <div style={{
                                fontWeight: 800,
                                fontSize: '12px',
                                color: w.activeDays >= Math.ceil(weekDays.length * 0.7) ? 'var(--success)' : w.activeDays >= Math.ceil(weekDays.length * 0.4) ? 'var(--warning)' : 'var(--text-muted)'
                              }}>
                                {w.activeDays} / {weekDays.length} d
                              </div>
                              {weekDays.length <= 14 ? (
                                <div style={{ fontSize: '8px', letterSpacing: '0.5px', marginTop: '2px' }}>
                                  {weekDays.map(wd => (w.days?.[wd.dateKey]?.sessionsCount || 0) > 0 ? '🟢' : '⚪').join('')}
                                </div>
                              ) : (
                                <div style={{ fontSize: '10px', fontWeight: 600, color: 'var(--text-muted)', marginTop: '2px' }}>
                                  {Math.round((w.activeDays / (weekDays.length || 1)) * 100)}% active
                                </div>
                              )}
                            </td>
                            <td style={{ padding: '6px 8px', textAlign: 'center' }}>
                              <div style={{ fontWeight: 800, fontSize: '12.5px', color: w.totalQuestions > 0 ? (w.avgScore >= 80 ? 'var(--success)' : w.avgScore >= 50 ? 'var(--warning)' : 'var(--danger)') : 'var(--text-muted)' }}>
                                {w.totalQuestions > 0 ? `${w.avgScore}%` : '—'}
                              </div>
                              <div style={{ fontSize: '9.5px', fontWeight: 700, color: 'var(--text-muted)' }}>
                                {w.avgScore >= 85 ? '⭐ उत्तम' : w.avgScore >= 65 ? 'मध्यम' : w.totalQuestions > 0 ? 'सुधारणा हवी' : 'सराव नाही'}
                              </div>
                            </td>
                            <td style={{ padding: '6px 10px', textAlign: 'center', whiteSpace: 'nowrap' }}>
                              <div style={{ display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
                                <span 
                                  onClick={(e) => openTopicStatusModal(student, 'mastered', e)} 
                                  style={{ color: 'var(--success)', fontWeight: 700, cursor: 'pointer', padding: '1px 5px', borderRadius: '5px', background: 'rgba(16,185,129,0.12)', border: '1px solid rgba(16,185,129,0.25)' }} 
                                  title="Mastered Topics"
                                >
                                  🟢 {mastery.mastered}
                                </span>
                                <span 
                                  onClick={(e) => openTopicStatusModal(student, 'practicing', e)} 
                                  style={{ color: 'var(--warning)', fontWeight: 700, cursor: 'pointer', padding: '1px 5px', borderRadius: '5px', background: 'rgba(245,158,11,0.12)', border: '1px solid rgba(245,158,11,0.25)' }} 
                                  title="Practicing Topics"
                                >
                                  🟡 {mastery.practicing}
                                </span>
                                <span 
                                  onClick={(e) => openTopicStatusModal(student, 'needsAttention', e)} 
                                  style={{ color: 'var(--danger)', fontWeight: 700, cursor: 'pointer', padding: '1px 5px', borderRadius: '5px', background: 'rgba(239,68,68,0.12)', border: '1px solid rgba(239,68,68,0.25)' }} 
                                  title="Needs Attention Topics"
                                >
                                  🔴 {adjustedNeedsAttention}
                                </span>
                              </div>
                              <div style={{ fontSize: '10px', fontWeight: 600, color: 'var(--text-muted)', marginTop: '2px' }}>
                                एकूण: <strong>{targetTotal}</strong> घटक
                              </div>
                            </td>
                            <td style={{ padding: '6px 10px', textAlign: 'center', whiteSpace: 'nowrap' }} onClick={(e) => e.stopPropagation()}>
                              <button
                                onClick={(e) => openTopicStatusModal(student, 'all', e)}
                                className="btn btn-secondary btn-sm"
                                style={{
                                  padding: '3px 8px',
                                  fontSize: '11px',
                                  fontWeight: 700,
                                  borderRadius: '5px',
                                  display: 'inline-flex',
                                  alignItems: 'center',
                                  gap: '4px',
                                  cursor: 'pointer',
                                  background: 'var(--surface)',
                                  border: '1px solid var(--border-light)'
                                }}
                                title="Open topic breakdown and export individual WhatsApp report card"
                              >
                                📸 WhatsApp
                              </button>
                            </td>
                          </tr>
                        );
                      }

                      // Cumulative View Row
                      return (
                        <tr 
                          key={student.studentCode} 
                          onClick={() => handleRowClick(student)}
                          className="hover-row"
                          style={{ borderBottom: '1px solid var(--border-light)', cursor: 'pointer', transition: 'background 0.2s' }}
                        >
                          <td style={{ padding: '6px 10px', fontWeight: 'bold' }}>{formattedName}</td>
                          <td style={{ padding: '6px 10px', textAlign: 'center' }}>{stats.totalSessions}</td>
                          <td style={{ padding: '6px 10px', textAlign: 'center' }}>{stats.questionsAttempted}</td>
                          <td style={{ padding: '6px 10px' }}>
                            <div style={{ fontWeight: 'bold', color: stats.totalSessions > 0 ? 'var(--accent)' : 'inherit' }}>
                              {stats.totalSessions > 0 ? `${stats.avgScore}%` : '—'}
                            </div>
                            {typeof stats.examAvg === 'number' && (
                              <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', fontWeight: 600 }}>
                                Exam: {stats.examAvg}%
                              </div>
                            )}
                          </td>
                          <td style={{ padding: '6px 10px', fontWeight: 'bold' }}>
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
                          <td style={{ padding: '6px 10px', fontWeight: 'bold' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                              <span style={{ width: '28px' }}>{efforts}%</span>
                              <div style={{ width: '40px', height: '6px', background: 'var(--bg-soft)', borderRadius: '3px', overflow: 'hidden' }}>
                                <div style={{
                                  width: `${efforts}%`,
                                  height: '100%',
                                  background: efforts >= 80 ? 'var(--success)' : efforts >= 50 ? 'var(--warning)' : 'var(--danger)'
                                }} />
                              </div>
                            </div>
                          </td>
                          <td style={{ padding: '6px 10px', fontWeight: 'bold' }}>
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
                          <td style={{ padding: '6px 10px', whiteSpace: 'nowrap' }}>
                            <span 
                              onClick={(e) => openTopicStatusModal(student, 'mastered', e)} 
                              style={{ color: 'var(--success)', fontWeight: 700, cursor: 'pointer', padding: '2px 6px', borderRadius: '6px', background: 'rgba(16,185,129,0.12)', border: '1px solid rgba(16,185,129,0.25)', transition: 'all 0.15s' }} 
                              title="Click to view Mastered Topics (>=90% accuracy & target confidence)"
                            >
                              🟢 {mastery.mastered}
                            </span>
                            <span 
                              onClick={(e) => openTopicStatusModal(student, 'practicing', e)} 
                              style={{ color: 'var(--warning)', fontWeight: 700, marginLeft: '6px', cursor: 'pointer', padding: '2px 6px', borderRadius: '6px', background: 'rgba(245,158,11,0.12)', border: '1px solid rgba(245,158,11,0.25)', transition: 'all 0.15s' }} 
                              title="Click to view Practicing / In Progress Topics (50-89% or low confidence)"
                            >
                              🟡 {mastery.practicing}
                            </span>
                            <span 
                              onClick={(e) => openTopicStatusModal(student, 'needsAttention', e)} 
                              style={{ color: 'var(--danger)', fontWeight: 700, marginLeft: '6px', cursor: 'pointer', padding: '2px 6px', borderRadius: '6px', background: 'rgba(239,68,68,0.12)', border: '1px solid rgba(239,68,68,0.25)', transition: 'all 0.15s' }} 
                              title="Click to view Needs Care / Focus Topics (<50% or unattempted)"
                            >
                              🔴 {adjustedNeedsAttention}
                            </span>
                          </td>
                          <td style={{ padding: '6px 10px', color: 'var(--text-muted)' }}>
                            {stats.lastActive ? formatDateDMY(stats.lastActive) : 'Never'}
                          </td>
                          <td style={{ padding: '6px 10px', textAlign: 'center', whiteSpace: 'nowrap' }} onClick={(e) => e.stopPropagation()}>
                            <button
                              onClick={(e) => openTopicStatusModal(student, 'all', e)}
                              className="btn btn-secondary btn-sm"
                              style={{
                                padding: '3px 8px',
                                fontSize: '11px',
                                fontWeight: 700,
                                borderRadius: '5px',
                                display: 'inline-flex',
                                alignItems: 'center',
                                gap: '4px',
                                cursor: 'pointer',
                                background: 'var(--surface)',
                                border: '1px solid var(--border-light)'
                              }}
                              title="Open topic breakdown and export individual WhatsApp report card"
                            >
                              📸 WhatsApp
                            </button>
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
