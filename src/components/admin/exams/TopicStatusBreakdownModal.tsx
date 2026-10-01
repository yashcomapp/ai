'use client';

import React from 'react';

export interface TopicStatusBreakdownState {
  show: boolean;
  student: any;
  data: {
    mastered: any[];
    practicing: any[];
    needsAttention: any[];
  } | null;
  activeTab: 'all' | 'mastered' | 'practicing' | 'needsAttention';
  searchText: string;
  loading: boolean;
}

export interface TopicStatusBreakdownModalProps {
  topicStatusModal: TopicStatusBreakdownState;
  setTopicStatusModal: React.Dispatch<React.SetStateAction<TopicStatusBreakdownState>>;
}

export default function TopicStatusBreakdownModal({
  topicStatusModal,
  setTopicStatusModal,
}: TopicStatusBreakdownModalProps) {
  if (!topicStatusModal.show) return null;

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
      <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '800px', width: '100%', maxHeight: '88vh', overflowY: 'auto', padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px', boxShadow: 'var(--shadow-lg)' }}>
        
        {/* Modal Header */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '14px' }}>
          <div>
            <h3 style={{ fontSize: '16px', fontWeight: 800, margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
              {topicStatusModal.activeTab === 'mastered' ? '🟢 Mastered Topics' : 
               topicStatusModal.activeTab === 'practicing' ? '🟡 In Progress Topics' :
               topicStatusModal.activeTab === 'needsAttention' ? '🔴 Needs Attention Topics' : '🎯 All Topic Mastery'}: {topicStatusModal.student?.name}
            </h3>
            <span style={{ fontSize: '11.5px', color: 'var(--text-muted)' }}>
              Real-time Diagnostic Status
            </span>
          </div>
          <button 
            onClick={() => setTopicStatusModal(prev => ({ ...prev, show: false }))} 
            style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.3rem', color: 'var(--text-muted)' }}
          >
            ✕
          </button>
        </div>

        {/* Filter Tabs & Search Bar */}
        {topicStatusModal.data && (
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
            <div style={{ display: 'flex', gap: '6px', background: 'var(--bg-soft)', padding: '4px', borderRadius: '10px', border: '1px solid var(--border-light)' }}>
              <button
                onClick={() => setTopicStatusModal(prev => ({ ...prev, activeTab: 'all' }))}
                style={{
                  padding: '5px 12px',
                  borderRadius: '8px',
                  fontSize: '11px',
                  fontWeight: topicStatusModal.activeTab === 'all' ? 700 : 500,
                  border: 'none',
                  cursor: 'pointer',
                  background: topicStatusModal.activeTab === 'all' ? 'var(--surface)' : 'transparent',
                  color: topicStatusModal.activeTab === 'all' ? 'var(--text)' : 'var(--text-muted)',
                  boxShadow: topicStatusModal.activeTab === 'all' ? 'var(--shadow-sm)' : 'none'
                }}
              >
                All ({(topicStatusModal.data.mastered.length + topicStatusModal.data.practicing.length + topicStatusModal.data.needsAttention.length)})
              </button>
              <button
                onClick={() => setTopicStatusModal(prev => ({ ...prev, activeTab: 'mastered' }))}
                style={{
                  padding: '5px 12px',
                  borderRadius: '8px',
                  fontSize: '11px',
                  fontWeight: topicStatusModal.activeTab === 'mastered' ? 700 : 500,
                  border: 'none',
                  cursor: 'pointer',
                  background: topicStatusModal.activeTab === 'mastered' ? 'rgba(16,185,129,0.15)' : 'transparent',
                  color: topicStatusModal.activeTab === 'mastered' ? 'var(--success)' : 'var(--text-muted)',
                  boxShadow: topicStatusModal.activeTab === 'mastered' ? 'var(--shadow-sm)' : 'none'
                }}
              >
                🟢 Mastered ({topicStatusModal.data.mastered.length})
              </button>
              <button
                onClick={() => setTopicStatusModal(prev => ({ ...prev, activeTab: 'practicing' }))}
                style={{
                  padding: '5px 12px',
                  borderRadius: '8px',
                  fontSize: '11px',
                  fontWeight: topicStatusModal.activeTab === 'practicing' ? 700 : 500,
                  border: 'none',
                  cursor: 'pointer',
                  background: topicStatusModal.activeTab === 'practicing' ? 'rgba(245,158,11,0.15)' : 'transparent',
                  color: topicStatusModal.activeTab === 'practicing' ? 'var(--warning)' : 'var(--text-muted)',
                  boxShadow: topicStatusModal.activeTab === 'practicing' ? 'var(--shadow-sm)' : 'none'
                }}
              >
                🟡 In Progress ({topicStatusModal.data.practicing.length})
              </button>
              <button
                onClick={() => setTopicStatusModal(prev => ({ ...prev, activeTab: 'needsAttention' }))}
                style={{
                  padding: '5px 12px',
                  borderRadius: '8px',
                  fontSize: '11px',
                  fontWeight: topicStatusModal.activeTab === 'needsAttention' ? 700 : 500,
                  border: 'none',
                  cursor: 'pointer',
                  background: topicStatusModal.activeTab === 'needsAttention' ? 'rgba(239,68,68,0.15)' : 'transparent',
                  color: topicStatusModal.activeTab === 'needsAttention' ? 'var(--danger)' : 'var(--text-muted)',
                  boxShadow: topicStatusModal.activeTab === 'needsAttention' ? 'var(--shadow-sm)' : 'none'
                }}
              >
                🔴 Needs Care ({topicStatusModal.data.needsAttention.length})
              </button>
            </div>

            <input 
              type="text"
              placeholder="Search topic or chapter..."
              value={topicStatusModal.searchText}
              onChange={(e) => setTopicStatusModal(prev => ({ ...prev, searchText: e.target.value }))}
              style={{
                padding: '6px 12px',
                fontSize: '11.5px',
                borderRadius: '8px',
                border: '1px solid var(--border-light)',
                background: 'var(--bg-soft)',
                color: 'var(--text)',
                minWidth: '180px'
              }}
            />
          </div>
        )}

        {/* Modal Body */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', minHeight: '150px' }}>
          {topicStatusModal.loading ? (
            <div style={{ textAlign: 'center', padding: '40px 20px' }}>
              <div className="spinner" style={{ margin: '0 auto 12px' }}></div>
              <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>Loading student topic breakdown & learning explanations...</div>
            </div>
          ) : !topicStatusModal.data ? (
            <div style={{ textAlign: 'center', padding: '30px', color: 'var(--text-faint)' }}>
              Failed to load topic status data.
            </div>
          ) : (() => {
            let list = topicStatusModal.activeTab === 'mastered' 
              ? topicStatusModal.data.mastered 
              : topicStatusModal.activeTab === 'practicing'
              ? topicStatusModal.data.practicing
              : topicStatusModal.activeTab === 'needsAttention'
              ? topicStatusModal.data.needsAttention
              : [
                  ...topicStatusModal.data.needsAttention,
                  ...topicStatusModal.data.practicing,
                  ...topicStatusModal.data.mastered
                ];

            if (topicStatusModal.searchText.trim()) {
              const q = topicStatusModal.searchText.toLowerCase();
              list = list.filter(t => 
                (t.topicName || '').toLowerCase().includes(q) ||
                (t.chapterName || '').toLowerCase().includes(q) ||
                (t.subjectName || '').toLowerCase().includes(q) ||
                (t.topicCode || '').toLowerCase().includes(q)
              );
            }

            if (list.length === 0) {
              return (
                <div style={{ textAlign: 'center', padding: '36px', color: 'var(--text-muted)' }}>
                  📭 No topics found under this status filter.
                </div>
              );
            }

            return (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {list.map((t, idx) => {
                  const isMastered = t.state === 'mastered';
                  const isPracticing = t.state === 'continuePractice' || t.state === 'revision';
                  const statusColor = isMastered ? 'var(--success)' : isPracticing ? 'var(--warning)' : 'var(--danger)';
                  const statusBg = isMastered ? 'rgba(16,185,129,0.06)' : isPracticing ? 'rgba(245,158,11,0.06)' : 'rgba(239,68,68,0.06)';
                  const statusBorder = isMastered ? 'rgba(16,185,129,0.25)' : isPracticing ? 'rgba(245,158,11,0.25)' : 'rgba(239,68,68,0.25)';

                  return (
                    <div 
                      key={t.topicCode || idx}
                      style={{
                        border: `1px solid ${statusBorder}`,
                        borderRadius: 'var(--radius)',
                        background: statusBg,
                        padding: '14px 16px',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '8px',
                        transition: 'transform 0.15s, box-shadow 0.15s'
                      }}
                    >
                      {/* Top row: Subject / Chapter badge & Mastery Pill */}
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '6px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
                          <span style={{ fontSize: '10px', fontWeight: 700, padding: '2px 7px', borderRadius: '4px', background: 'var(--surface)', border: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                            📘 {t.subjectName} • {t.chapterName}
                          </span>
                          <span style={{ fontSize: '10px', color: 'var(--text-faint)' }}>
                            Code: {t.topicCode}
                          </span>
                        </div>

                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span style={{
                            fontSize: '11px',
                            fontWeight: 800,
                            color: statusColor,
                            background: 'var(--surface)',
                            padding: '2px 8px',
                            borderRadius: '6px',
                            border: `1px solid ${statusBorder}`
                          }}>
                            {t.mastery}% Accuracy
                          </span>
                          <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>
                            {t.practiceCount}/{t.topicClassification === 'minor' || t.topicClassification === 'micro' ? 2 : 3} Practices ({t.attempts} Qs)
                          </span>
                        </div>
                      </div>

                      {/* Topic Name */}
                      <div style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--text)' }}>
                        📍 {t.topicName}
                      </div>

                      {/* Student Explanation Banner */}
                      <div style={{
                        display: 'flex',
                        alignItems: 'flex-start',
                        gap: '8px',
                        padding: '8px 12px',
                        borderRadius: '8px',
                        background: 'var(--surface)',
                        border: `1px solid var(--border-light)`,
                        fontSize: '11.5px',
                        color: t.expColor || statusColor,
                        lineHeight: 1.5
                      }}>
                        <span style={{ fontSize: '14px', flexShrink: 0 }}>{t.expIcon}</span>
                        <div>
                          <strong style={{ display: 'block', fontSize: '10.5px', textTransform: 'uppercase', letterSpacing: '0.5px', opacity: 0.8, marginBottom: '1px' }}>
                            Explanation shown to student:
                          </strong>
                          {t.expText}
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            );
          })()}
        </div>

        {/* Modal Footer */}
        <div style={{ display: 'flex', justifyContent: 'flex-end', borderTop: '1px solid var(--border-light)', paddingTop: '14px', marginTop: '4px' }}>
          <button 
            className="btn btn-secondary" 
            onClick={() => setTopicStatusModal(prev => ({ ...prev, show: false }))}
          >
            Close
          </button>
        </div>

      </div>
    </div>
  );
}
