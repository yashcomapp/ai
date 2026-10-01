'use client';

import React from 'react';
import { getDateKeyIST } from '@/lib/dateUtils';

export interface ScheduledSuitesManagerModalProps {
  showManagerModal: boolean;
  setShowManagerModal: (show: boolean) => void;
  loadingScheduled: boolean;
  scheduledExamsList: any[];
  assignments: any[];
  isCompletedSectionExpanded: boolean;
  setIsCompletedSectionExpanded: (expanded: boolean) => void;
  printPlannerForSuite: (chapName: string, dailyTests: any[], saturdayTest?: any) => void;
  handleDeleteSuiteGroup: (ids: string[]) => void;
  openSaturdayAssign: (item: any) => void;
  toISTString: (val: any) => string;
}

export function ScheduledSuitesManagerModal({
  showManagerModal,
  setShowManagerModal,
  loadingScheduled,
  scheduledExamsList,
  assignments,
  isCompletedSectionExpanded,
  setIsCompletedSectionExpanded,
  printPlannerForSuite,
  handleDeleteSuiteGroup,
  openSaturdayAssign,
  toISTString,
}: ScheduledSuitesManagerModalProps) {
  if (!showManagerModal) return null;

  return (
    <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.6)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
      <div style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', width: '100%', maxWidth: '950px', maxHeight: '90vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-light)', overflow: 'hidden', boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.3)' }}>
        
        <div style={{ padding: '14px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)' }}>
          <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800, color: 'var(--text)' }}>
            📅 Scheduled Home Practices & Classroom Tests
          </h3>
          <button className="btn btn-secondary btn-sm" onClick={() => setShowManagerModal(false)}>✕ Close</button>
        </div>

        <div style={{ padding: '20px', overflowY: 'auto', flex: 1 }}>
          {loadingScheduled ? (
            <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
              Loading scheduled exams...
            </div>
          ) : scheduledExamsList.length === 0 ? (
            <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>No scheduled exams found.</div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
              {(() => {
                const getWeekRange = (dateStr: string) => {
                  if (!dateStr) return 'Unknown Week';
                  const parts = dateStr.split('-');
                  if (parts.length !== 3) return 'Unknown Week';
                  
                  const year = Number(parts[0]);
                  const month = Number(parts[1]) - 1;
                  const dayVal = Number(parts[2]);
                  
                  const tempDate = new Date(year, month, dayVal);
                  const dayOfWeek = tempDate.getDay();
                  
                  const mondayOffset = dayOfWeek === 0 ? -6 : 1 - dayOfWeek;
                  const monday = new Date(year, month, dayVal + mondayOffset);
                  const saturday = new Date(monday.getFullYear(), monday.getMonth(), monday.getDate() + 5);
                  
                  const fmt = (d: Date) => {
                    const m = d.toLocaleString('en-US', { month: 'short' });
                    return `${m} ${d.getDate()}, ${d.getFullYear()}`;
                  };
                  return `Week of ${fmt(monday)} – ${fmt(saturday)}`;
                };

                const sortedExams = [...scheduledExamsList].sort((a: any, b: any) => {
                  return (a.scheduledDate || '').localeCompare(b.scheduledDate || '');
                });

                const groups: Record<string, any[]> = {};
                sortedExams.forEach((exam: any) => {
                  const weekKey = getWeekRange(exam.scheduledDate);
                  if (!groups[weekKey]) groups[weekKey] = [];
                  groups[weekKey].push(exam);
                });

                const todayStr = getDateKeyIST();

                const ongoingGroups: [string, any[]][] = [];
                const completedGroups: [string, any[]][] = [];

                Object.entries(groups).forEach(([weekRange, groupItems]) => {
                  const dates = groupItems.map((item: any) => item.scheduledDate || '');
                  const maxDate = dates.reduce((a: string, b: string) => a > b ? a : b, '');
                  if (maxDate >= todayStr) {
                    ongoingGroups.push([weekRange, groupItems]);
                  } else {
                    completedGroups.push([weekRange, groupItems]);
                  }
                });

                const renderGroup = ([weekRange, groupItems]: [string, any[]]) => {
                  const allGroupIds = groupItems.map((item: any) => item.id);
                  const dailyTests = groupItems.filter((item: any) => item.type === 'home_practice');
                  const saturdayTest = groupItems.find((item: any) => item.type === 'classroom_test');
                  const chapName = groupItems[0]?.chapterName || 'General';

                  return (
                    <div key={weekRange} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', background: 'var(--bg-soft)', overflow: 'hidden', marginBottom: '16px' }}>
                      <div style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span style={{ fontSize: '15px' }}>📅</span>
                          <strong style={{ fontSize: '13px', color: 'var(--text)' }}>{weekRange}</strong>
                          <span style={{ fontSize: '11px', color: 'var(--text-muted)', background: 'var(--bg-main)', padding: '2px 8px', borderRadius: '12px', fontWeight: 600 }}>
                            {groupItems.length} Tests
                          </span>
                        </div>
                        
                        <div style={{ display: 'flex', gap: '8px' }}>
                          <button 
                            className="btn btn-secondary btn-sm"
                            onClick={() => printPlannerForSuite(chapName, dailyTests, saturdayTest)}
                            style={{ fontSize: '11px', padding: '4px 10px', display: 'flex', alignItems: 'center', gap: '4px' }}
                          >
                            🖨️ Print Planner
                          </button>
                          <button 
                            className="btn btn-secondary btn-sm"
                            onClick={() => handleDeleteSuiteGroup(allGroupIds)}
                            style={{ background: 'var(--danger-bg)', color: 'var(--danger)', border: '1px solid var(--danger-border)', fontSize: '11px', padding: '4px 10px' }}
                          >
                            🗑️ Delete Entire Week
                          </button>
                        </div>
                      </div>

                      <div style={{ overflowX: 'auto', background: 'var(--surface)' }}>
                        <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '12px' }}>
                          <thead>
                            <tr style={{ borderBottom: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text-muted)', fontWeight: 600 }}>
                              <th style={{ padding: '10px 14px' }}>Date & Day</th>
                              <th style={{ padding: '10px 14px' }}>Type</th>
                              <th style={{ padding: '10px 14px' }}>Subject & Topics Covered</th>
                              <th style={{ padding: '10px 14px' }}>Questions / Marks</th>
                              <th style={{ padding: '10px 14px' }}>Saturday Status & Setup</th>
                              <th style={{ padding: '10px 14px', textAlign: 'center' }}>Actions</th>
                            </tr>
                          </thead>
                          <tbody>
                            {groupItems.map((item: any) => {
                              const dateParts = (item.scheduledDate || '').split('-');
                              const dateLabel = dateParts.length === 3 ? `${dateParts[1]}/${dateParts[2]}` : item.scheduledDate || '';
                              const dayLabel = item.dayName ? `(${item.dayName.substring(0, 3)})` : '';
                              
                              const topicNames = Array.from(new Set(item.questions?.map((q: any) => q.topicName || q.topic).filter(Boolean)));
                              const chapterNumLabel = item.chapterNumber ? `Ch ${item.chapterNumber}: ` : '';
                              const topicsDisplay = topicNames.length > 0 ? topicNames.join(', ') : (item.chapterName || 'General Practice');

                              const isSat = item.type === 'classroom_test';
                              const satAssign = isSat ? assignments.find((a: any) => a.examId === item.id) : null;

                              return (
                                <tr key={item.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                                  <td style={{ padding: '12px 14px', whiteSpace: 'nowrap', fontWeight: 600, color: 'var(--text)' }}>
                                    {dateLabel} {dayLabel}
                                  </td>
                                  
                                  <td style={{ padding: '12px 14px' }}>
                                    {isSat ? (
                                      <span style={{ background: 'var(--accent-bg)', color: 'var(--accent)', padding: '2px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700, border: '1px solid var(--border)' }}>
                                        🏫 Classroom Test
                                      </span>
                                    ) : (
                                      <span style={{ background: 'var(--info-bg)', color: 'var(--info)', padding: '2px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700, border: '1px solid var(--border)' }}>
                                        🏠 Home Practice
                                      </span>
                                    )}
                                  </td>

                                  <td style={{ padding: '12px 14px', maxWidth: '300px' }}>
                                    <div style={{ fontWeight: 600, color: 'var(--text-muted)', fontSize: '11px', textTransform: 'uppercase' }}>
                                      {item.subject}
                                    </div>
                                    <div style={{ marginTop: '2px', fontSize: '11px', color: 'var(--text)', lineHeight: '1.4' }}>
                                      <strong>{chapterNumLabel}</strong>{topicsDisplay}
                                    </div>
                                  </td>

                                  <td style={{ padding: '12px 14px', whiteSpace: 'nowrap', color: 'var(--text-muted)' }}>
                                    <strong>{item.totalQuestions || 0}</strong> Qs / <strong>{item.totalMarks || 0}</strong> Marks
                                  </td>

                                  <td style={{ padding: '12px 14px' }}>
                                    {isSat ? (
                                      <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', alignItems: 'flex-start' }}>
                                        {satAssign ? (
                                          <span style={{ background: 'var(--success-bg)', color: 'var(--success)', fontSize: '10px', padding: '2px 6px', borderRadius: '4px', fontWeight: 800 }}>
                                            Active: {toISTString(satAssign.startAt).replace('T', ' ')} to {toISTString(satAssign.endAt).split('T')[1]}
                                          </span>
                                        ) : (
                                          <span style={{ background: 'var(--warning-bg)', color: 'var(--warning)', fontSize: '10px', padding: '2px 6px', borderRadius: '4px', fontWeight: 800 }}>
                                            Pending Activation
                                          </span>
                                        )}
                                        <button 
                                          className="btn btn-primary btn-sm"
                                          style={{ padding: '2px 6px', fontSize: '10px', height: 'auto', lineHeight: 1 }}
                                          onClick={() => openSaturdayAssign(item)}
                                        >
                                          ⚙️ {satAssign ? 'Modify' : 'Activate'}
                                        </button>
                                      </div>
                                    ) : (
                                      <span style={{ color: 'var(--text-muted)', fontSize: '11px' }}>—</span>
                                    )}
                                  </td>

                                  <td style={{ padding: '12px 14px', textAlign: 'center' }}>
                                    <button
                                      onClick={() => handleDeleteSuiteGroup([item.id])}
                                      style={{ background: 'none', border: 'none', color: 'var(--danger)', cursor: 'pointer', fontSize: '14px', padding: '4px' }}
                                      title="Delete this test"
                                    >
                                      🗑️
                                    </button>
                                  </td>
                                </tr>
                              );
                            })}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  );
                };

                return (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                    <div>
                      <h4 style={{ margin: '0 0 12px 0', fontSize: '13px', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.5px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <span>🚀 Ongoing Weekly Suites</span>
                        <span style={{ background: 'var(--info-bg)', color: 'var(--info)', padding: '2px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700 }}>
                          {ongoingGroups.length}
                        </span>
                      </h4>
                      {ongoingGroups.length === 0 ? (
                        <div style={{ padding: '20px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-lg)', border: '1px dashed var(--border-light)', color: 'var(--text-faint)', fontSize: '12px', textAlign: 'center' }}>
                          No ongoing weekly suites.
                        </div>
                      ) : (
                        ongoingGroups.map(renderGroup)
                      )}
                    </div>

                    <div style={{ borderTop: '1px solid var(--border-light)', paddingTop: '20px', marginTop: '10px' }}>
                      <button
                        onClick={() => setIsCompletedSectionExpanded(!isCompletedSectionExpanded)}
                        style={{
                          width: '100%',
                          background: 'var(--bg-soft)',
                          border: '1px solid var(--border-light)',
                          borderRadius: 'var(--radius-md)',
                          padding: '10px 16px',
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center',
                          cursor: 'pointer',
                          color: 'var(--text)',
                          fontSize: '12.5px',
                          fontWeight: 700,
                          outline: 'none',
                          textAlign: 'left'
                        }}
                      >
                        <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span>✅ Completed Weekly Suites</span>
                          <span style={{ background: 'var(--border-light)', color: 'var(--text-muted)', padding: '2px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700 }}>
                            {completedGroups.length}
                          </span>
                        </span>
                        <span style={{ color: 'var(--text-muted)', fontSize: '11px', fontWeight: 600 }}>
                          {isCompletedSectionExpanded ? 'Hide completed suites ▲' : 'Show completed suites ▼'}
                        </span>
                      </button>

                      {isCompletedSectionExpanded && (
                        <div style={{ marginTop: '16px' }}>
                          {completedGroups.length === 0 ? (
                            <div style={{ padding: '20px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-lg)', border: '1px dashed var(--border-light)', color: 'var(--text-faint)', fontSize: '12px', textAlign: 'center' }}>
                              No completed weekly suites.
                            </div>
                          ) : (
                            completedGroups.map(renderGroup)
                          )}
                        </div>
                      )}
                    </div>
                  </div>
                );
              })()}
            </div>
          )}
        </div>

      </div>
    </div>
  );
}

export default ScheduledSuitesManagerModal;
