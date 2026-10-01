'use client';

import React from 'react';

export interface PracticeHistoryStudent {
  studentCode: string;
  name: string;
}

export interface PracticeHistoryModalProps {
  selectedPracStudent: any;
  setSelectedPracStudent: (student: any) => void;
  loadingPracHistory: boolean;
  pracHistory: any[];
  modalExpandedSubjects: Set<string>;
  setModalExpandedSubjects: React.Dispatch<React.SetStateAction<Set<string>>>;
  modalExpandedChapters: Set<string>;
  setModalExpandedChapters: React.Dispatch<React.SetStateAction<Set<string>>>;
  modalSortKey: 'name' | 'score' | 'date' | 'integrity';
  modalSortDirection: 'asc' | 'desc';
  handleModalSort: (key: 'name' | 'score' | 'date' | 'integrity') => void;
  loadScorecard: (examId: string, studentCode: string) => void;
  formatDateDMY: (date: any) => string;
}

export default function PracticeHistoryModal({
  selectedPracStudent,
  setSelectedPracStudent,
  loadingPracHistory,
  pracHistory,
  modalExpandedSubjects,
  setModalExpandedSubjects,
  modalExpandedChapters,
  setModalExpandedChapters,
  modalSortKey,
  modalSortDirection,
  handleModalSort,
  loadScorecard,
  formatDateDMY,
}: PracticeHistoryModalProps) {
  if (!selectedPracStudent) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
      <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '750px', width: '100%', maxHeight: '85vh', overflowY: 'auto', padding: '24px', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '12px' }}>
          <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0 }}>
            📚 Practice History: {selectedPracStudent.name}
          </h3>
          <button onClick={() => setSelectedPracStudent(null)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          {loadingPracHistory ? (
            <div style={{ textAlign: 'center', padding: '20px' }}>
              <div className="spinner" style={{ margin: '0 auto 10px' }}></div> Loading history details...
            </div>
          ) : pracHistory.length === 0 ? (
            <div style={{ textAlign: 'center', padding: '20px', color: 'var(--text-faint)' }}>
              📭 No practice logs found for this student.
            </div>
          ) : (() => {
            const groupedPrac = new Map<string, Map<string, any[]>>();
            pracHistory.forEach(h => {
              const sName = h.subject || 'Other Subjects';
              const cName = h.chapter || 'General';
              if (!groupedPrac.has(sName)) {
                groupedPrac.set(sName, new Map());
              }
              const chapters = groupedPrac.get(sName)!;
              if (!chapters.has(cName)) {
                chapters.set(cName, []);
              }
              chapters.get(cName)!.push(h);
            });

            const sortedSubjs = Array.from(groupedPrac.keys());

            const getSubjAvg = (sName: string) => {
              const chapters = groupedPrac.get(sName)!;
              const topics = Array.from(chapters.values()).flat();
              if (topics.length === 0) return 0;
              return topics.reduce((acc, t) => acc + (t.scorePercent || 0), 0) / topics.length;
            };

            const getChapAvg = (topics: any[]) => {
              if (topics.length === 0) return 0;
              return topics.reduce((acc, t) => acc + (t.scorePercent || 0), 0) / topics.length;
            };

            const getProgressCol = (pct: number) => {
              if (pct < 40) return 'var(--danger)';
              if (pct < 70) return 'var(--warning)';
              return 'var(--success)';
            };

            const toggleModalSubject = (subjName: string) => {
              const next = new Set(modalExpandedSubjects);
              if (next.has(subjName)) next.delete(subjName);
              else next.add(subjName);
              setModalExpandedSubjects(next);
            };

            const toggleModalChapter = (subjName: string, chapterName: string) => {
              const key = `${subjName}||${chapterName}`;
              const next = new Set(modalExpandedChapters);
              if (next.has(key)) next.delete(key);
              else next.add(key);
              setModalExpandedChapters(next);
            };

            return (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                {sortedSubjs.map(subjName => {
                  const chapters = groupedPrac.get(subjName)!;
                  const allSubjTopics = Array.from(chapters.values()).flat();
                  const subjectMastery = getSubjAvg(subjName);
                  const isSubjExpanded = modalExpandedSubjects.has(subjName);
                  const subjProgressColor = getProgressCol(subjectMastery);

                  const sortedChapters = Array.from(chapters.keys());

                  return (
                    <div key={subjName} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius)', background: 'var(--surface)', overflow: 'hidden' }}>
                      <div 
                        onClick={() => toggleModalSubject(subjName)}
                        style={{ padding: '12px 16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isSubjExpanded ? '1px solid var(--border-light)' : 'none' }}
                      >
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span style={{ fontWeight: 'bold', fontSize: '13px' }}>📖 {subjName}</span>
                          <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>({allSubjTopics.length} sessions)</span>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                          <div style={{ width: '60px', height: '5px', background: 'var(--border-light)', borderRadius: '3px', overflow: 'hidden' }}>
                            <div style={{ width: `${subjectMastery}%`, height: '100%', background: subjProgressColor }}></div>
                          </div>
                          <span style={{ fontSize: '11px', fontWeight: 600 }}>{Math.round(subjectMastery)}%</span>
                          <span style={{ fontSize: '9px', transform: isSubjExpanded ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }}>▼</span>
                        </div>
                      </div>

                      {isSubjExpanded && (
                        <div style={{ padding: '10px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
                          {sortedChapters.map(chapterName => {
                            const topics = chapters.get(chapterName)!;
                            const chapterMastery = getChapAvg(topics);
                            const chapterKey = `${subjName}||${chapterName}`;
                            const isChExpanded = modalExpandedChapters.has(chapterKey);
                            const chProgressColor = getProgressCol(chapterMastery);

                            return (
                              <div key={chapterName} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--bg-soft)', overflow: 'hidden' }}>
                                <div 
                                  onClick={() => toggleModalChapter(subjName, chapterName)}
                                  style={{ padding: '10px 12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', cursor: 'pointer', borderBottom: isChExpanded ? '1px solid var(--border-light)' : 'none' }}
                                >
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                                    <span style={{ fontSize: '8px', transform: isChExpanded ? 'rotate(90deg)' : 'none', transition: 'transform 0.15s' }}>▶</span>
                                    <span style={{ fontWeight: 600, fontSize: '12px' }}>📘 {chapterName}</span>
                                    <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>({topics.length})</span>
                                  </div>
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <div style={{ width: '50px', height: '4px', background: 'var(--border-light)', borderRadius: '2px', overflow: 'hidden' }}>
                                      <div style={{ width: `${chapterMastery}%`, height: '100%', background: chProgressColor }}></div>
                                    </div>
                                    <span style={{ fontSize: '10px', fontWeight: 600 }}>{Math.round(chapterMastery)}%</span>
                                  </div>
                                </div>

                                {isChExpanded && (() => {
                                  const sortedTopics = [...topics].sort((a, b) => {
                                    let cmp = 0;
                                    if (modalSortKey === 'name') {
                                      cmp = (a.name || a.topicName || '').localeCompare(b.name || b.topicName || '', undefined, { numeric: true, sensitivity: 'base' });
                                    } else if (modalSortKey === 'score') {
                                      cmp = (a.scorePercent || 0) - (b.scorePercent || 0);
                                    } else if (modalSortKey === 'date') {
                                      const da = a.date ? new Date(a.date).getTime() : (a.createdAt ? (a.createdAt.toDate ? a.createdAt.toDate().getTime() : new Date(a.createdAt).getTime()) : 0);
                                      const db = b.date ? new Date(b.date).getTime() : (b.createdAt ? (b.createdAt.toDate ? b.createdAt.toDate().getTime() : new Date(b.createdAt).getTime()) : 0);
                                      cmp = da - db;
                                    } else if (modalSortKey === 'integrity') {
                                      const getRank = (item: any) => {
                                        if (typeof item.integrityScore === 'number') return item.integrityScore;
                                        const lvl = item.suspiciousLevel || 'green';
                                        return lvl === 'green' ? 100 : (lvl === 'yellow' ? 50 : 0);
                                      };
                                      cmp = getRank(a) - getRank(b);
                                    }
                                    return modalSortDirection === 'asc' ? cmp : -cmp;
                                  });

                                  return (
                                    <div style={{ padding: '8px' }}>
                                      <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '11px' }}>
                                        <thead>
                                          <tr style={{ borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', textTransform: 'uppercase', height: '28px' }}>
                                            <th 
                                              onClick={() => handleModalSort('name')}
                                              title="Click to sort by Topic / Practice Name"
                                              style={{ padding: '4px 6px', textAlign: 'left', cursor: 'pointer', userSelect: 'none' }}
                                            >
                                              <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', color: modalSortKey === 'name' ? 'var(--primary)' : 'inherit' }}>
                                                Topic / Practice Name
                                                <span style={{ fontSize: '10px', opacity: modalSortKey === 'name' ? 1 : 0.35 }}>
                                                  {modalSortKey === 'name' ? (modalSortDirection === 'asc' ? '▲' : '▼') : '⇅'}
                                                </span>
                                              </span>
                                            </th>
                                            <th 
                                              onClick={() => handleModalSort('score')}
                                              title="Click to sort by Score"
                                              style={{ padding: '4px 6px', textAlign: 'center', width: '65px', cursor: 'pointer', userSelect: 'none' }}
                                            >
                                              <span style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: '4px', color: modalSortKey === 'score' ? 'var(--primary)' : 'inherit' }}>
                                                Score
                                                <span style={{ fontSize: '10px', opacity: modalSortKey === 'score' ? 1 : 0.35 }}>
                                                  {modalSortKey === 'score' ? (modalSortDirection === 'asc' ? '▲' : '▼') : '⇅'}
                                                </span>
                                              </span>
                                            </th>
                                            <th 
                                              onClick={() => handleModalSort('date')}
                                              title="Click to sort by Date"
                                              style={{ padding: '4px 6px', textAlign: 'center', width: '85px', cursor: 'pointer', userSelect: 'none' }}
                                            >
                                              <span style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: '4px', color: modalSortKey === 'date' ? 'var(--primary)' : 'inherit' }}>
                                                Date
                                                <span style={{ fontSize: '10px', opacity: modalSortKey === 'date' ? 1 : 0.35 }}>
                                                  {modalSortKey === 'date' ? (modalSortDirection === 'asc' ? '▲' : '▼') : '⇅'}
                                                </span>
                                              </span>
                                            </th>
                                            <th 
                                              onClick={() => handleModalSort('integrity')}
                                              title="Click to sort by Integrity Level"
                                              style={{ padding: '4px 6px', textAlign: 'center', width: '65px', cursor: 'pointer', userSelect: 'none' }}
                                            >
                                              <span style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: '4px', color: modalSortKey === 'integrity' ? 'var(--primary)' : 'inherit' }}>
                                                Integrity
                                                <span style={{ fontSize: '10px', opacity: modalSortKey === 'integrity' ? 1 : 0.35 }}>
                                                  {modalSortKey === 'integrity' ? (modalSortDirection === 'asc' ? '▲' : '▼') : '⇅'}
                                                </span>
                                              </span>
                                            </th>
                                            <th style={{ padding: '4px 6px', textAlign: 'right', width: '80px', userSelect: 'none' }}>Action</th>
                                          </tr>
                                        </thead>
                                        <tbody>
                                          {sortedTopics.map((h, hIdx) => {
                                            const score = Math.round(h.scorePercent || 0);
                                            const level = h.suspiciousLevel || 'green';
                                            const dotCol = level === 'red' ? 'var(--danger)' : (level === 'yellow' ? 'var(--warning)' : 'var(--success)');

                                            return (
                                              <tr key={h.id || hIdx} style={{ borderBottom: '1px solid var(--border-light)', height: '36px' }}>
                                                <td style={{ padding: '4px 6px', fontWeight: 600 }}>
                                                  📍 {h.name}
                                                </td>
                                                <td style={{ padding: '4px 6px', textAlign: 'center', fontWeight: 'bold' }}>
                                                  <span style={{
                                                    color: score < 40 ? 'var(--danger)' : (score < 70 ? 'var(--warning)' : 'var(--success)'),
                                                    background: score < 40 ? 'rgba(239,68,68,0.1)' : (score < 70 ? 'rgba(245,158,11,0.1)' : 'rgba(16,185,129,0.1)'),
                                                    padding: '2px 6px',
                                                    borderRadius: '4px'
                                                  }}>
                                                    {score}%
                                                  </span>
                                                </td>
                                                <td style={{ padding: '4px 6px', textAlign: 'center', color: 'var(--text-muted)' }}>
                                                  {h.date ? formatDateDMY(h.date) : '-'}
                                                </td>
                                                <td style={{ padding: '4px 6px', textAlign: 'center' }}>
                                                  <span style={{ display: 'inline-block', width: '8px', height: '8px', borderRadius: '50%', background: dotCol }} title={`Integrity level: ${level}`} />
                                                </td>
                                                <td style={{ padding: '4px 6px', textAlign: 'right' }}>
                                                  <button 
                                                    onClick={() => loadScorecard(h.id, selectedPracStudent.studentCode)}
                                                    style={{ padding: '3px 10px', borderRadius: '20px', fontSize: '9px', fontWeight: 600, border: 'none', background: 'var(--accent-grad)', color: 'white', cursor: 'pointer' }}
                                                  >
                                                    Scorecard
                                                  </button>
                                                </td>
                                              </tr>
                                            );
                                          })}
                                        </tbody>
                                      </table>
                                    </div>
                                  );
                                })()}
                              </div>
                            );
                          })}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            );
          })()}
        </div>

        <div style={{ display: 'flex', justifyContent: 'flex-end', borderTop: '1px solid var(--border-light)', paddingTop: '12px', marginTop: '8px' }}>
          <button className="btn btn-secondary" onClick={() => setSelectedPracStudent(null)}>Close</button>
        </div>
      </div>
    </div>
  );
}
