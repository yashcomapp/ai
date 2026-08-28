'use client';

import React from 'react';

interface Topic {
  topic: string;
  subject?: string;
  topicNumber?: string;
  [key: string]: any;
}

interface Chapter {
  chapterNumber: string | number;
  chapterName: string;
  [key: string]: any;
}

interface SyllabusSelectorProps<T extends { topic: string; subject?: string }> {
  availableSubjects: string[];
  selectedSubjects: Set<string> | Record<string, any>;
  onToggleSubject: (subject: string) => void;
  
  availableChapters: Chapter[];
  selectedChapters: Set<number>;
  onToggleChapter: (index: number) => void;
  onSelectAllChapters: () => void;
  onDeselectAllChapters: () => void;
  
  availableTopics: T[];
  selectedTopics: T[];
  onToggleTopic: (topic: T) => void;
  onSelectAllTopics: () => void;
  onDeselectAllTopics: () => void;
  
  topicPlaceholder?: string;
}

export function SyllabusSelector<T extends { topic: string; subject?: string }>({
  availableSubjects,
  selectedSubjects,
  onToggleSubject,
  availableChapters,
  selectedChapters,
  onToggleChapter,
  onSelectAllChapters,
  onDeselectAllChapters,
  availableTopics,
  selectedTopics,
  onToggleTopic,
  onSelectAllTopics,
  onDeselectAllTopics,
  topicPlaceholder = 'Select at least one chapter first.'
}: SyllabusSelectorProps<T>) {
  
  const isSubjectChecked = (s: string) => {
    if (selectedSubjects instanceof Set) {
      return selectedSubjects.has(s);
    }
    if (typeof selectedSubjects === 'object' && selectedSubjects !== null) {
      const val = (selectedSubjects as Record<string, any>)[s];
      if (val && typeof val === 'object') {
        return !!val.selected;
      }
      return !!val;
    }
    return false;
  };

  const isTopicChecked = (top: T) => {
    return selectedTopics.some(s => s.topic === top.topic && s.subject === top.subject);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
      {/* Subjects Selection */}
      {availableSubjects.length > 0 && (
        <div>
          <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>
            📖 Select Subjects
          </label>
          <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap', padding: '6px 0' }}>
            {availableSubjects.map(s => {
              const isChecked = isSubjectChecked(s);
              return (
                <label
                  key={s}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px',
                    padding: '4px 8px',
                    background: isChecked ? 'var(--accent-soft)' : 'var(--surface)',
                    border: isChecked ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    fontSize: '12px',
                    color: 'var(--text)',
                    whiteSpace: 'nowrap',
                    transition: 'all 0.2s ease'
                  }}
                >
                  <input
                    type="checkbox"
                    checked={isChecked}
                    onChange={() => onToggleSubject(s)}
                  />
                  <span>{s}</span>
                </label>
              );
            })}
          </div>
        </div>
      )}

      {/* Chapters & Topics Layout */}
      {availableChapters.length > 0 && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {/* Chapters selection */}
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
              <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>
                Chapters ({selectedChapters.size} selected)
              </label>
              <div style={{ display: 'flex', gap: '8px' }}>
                <button
                  type="button"
                  className="btn btn-secondary"
                  style={{ padding: '2px 6px', fontSize: '10px' }}
                  onClick={onSelectAllChapters}
                >
                  Select All
                </button>
                <button
                  type="button"
                  className="btn btn-secondary"
                  style={{ padding: '2px 6px', fontSize: '10px' }}
                  onClick={onDeselectAllChapters}
                >
                  Deselect All
                </button>
              </div>
            </div>
            <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', maxHeight: '250px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '10px', background: 'var(--bg-soft)' }}>
              {availableChapters.map((ch, idx) => {
                const isChecked = selectedChapters.has(idx);
                return (
                  <label
                    key={idx}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: '6px',
                      padding: '4px 8px',
                      background: isChecked ? 'var(--accent-soft)' : 'var(--surface)',
                      border: isChecked ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                      borderRadius: 'var(--radius-sm)',
                      cursor: 'pointer',
                      fontSize: '12px',
                      color: 'var(--text)',
                      whiteSpace: 'nowrap',
                      transition: 'all 0.2s ease'
                    }}
                  >
                    <input
                      type="checkbox"
                      checked={isChecked}
                      onChange={() => onToggleChapter(idx)}
                    />
                    <span>Ch.{ch.chapterNumber}: {ch.chapterName}</span>
                    <span
                      style={{
                        fontSize: '10px',
                        fontWeight: 700,
                        marginLeft: '4px',
                        padding: '1px 6px',
                        borderRadius: '6px',
                        background: isChecked ? 'var(--accent-ring)' : 'var(--border-light, rgba(255,255,255,0.08))',
                        border: '1px solid var(--border-light, rgba(255,255,255,0.1))',
                        display: 'inline-flex',
                        alignItems: 'center',
                        gap: '3px'
                      }}
                      title={`Objective Questions: ${ch.objectiveCount ?? ch.chapter?.objectiveCount ?? 0} | Subjective Questions: ${ch.subjectiveCount ?? ch.chapter?.subjectiveCount ?? 0}`}
                    >
                      <span style={{ color: 'var(--accent)' }}>O: {ch.objectiveCount ?? ch.chapter?.objectiveCount ?? 0}</span>
                      <span style={{ opacity: 0.4 }}>|</span>
                      <span style={{ color: 'var(--accent)' }}>S: {ch.subjectiveCount ?? ch.chapter?.subjectiveCount ?? 0}</span>
                    </span>
                  </label>
                );
              })}
            </div>
          </div>

          {/* Topics selection */}
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
              <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>
                Topics ({selectedTopics.length} selected)
              </label>
              <div style={{ display: 'flex', gap: '8px' }}>
                <button
                  type="button"
                  className="btn btn-secondary"
                  style={{ padding: '2px 6px', fontSize: '10px' }}
                  onClick={onSelectAllTopics}
                >
                  Select All
                </button>
                <button
                  type="button"
                  className="btn btn-secondary"
                  style={{ padding: '2px 6px', fontSize: '10px' }}
                  onClick={onDeselectAllTopics}
                >
                  Deselect All
                </button>
              </div>
            </div>
            <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', maxHeight: '250px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '10px', background: 'var(--bg-soft)' }}>
              {availableTopics.length === 0 ? (
                <div style={{ width: '100%', textAlign: 'center', padding: '20px', color: 'var(--text-muted)', fontSize: '11px' }}>
                  {topicPlaceholder}
                </div>
              ) : (
                availableTopics.map((top, idx) => {
                  const hasSubtopics = !!(top as any).hasSubtopics;
                  const isChecked = isTopicChecked(top);
                  return (
                    <label
                      key={idx}
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: '6px',
                        padding: '4px 8px',
                        background: hasSubtopics 
                          ? 'var(--bg-soft)' 
                          : (isChecked ? 'rgba(59, 130, 246, 0.1)' : 'var(--surface)'),
                        border: hasSubtopics
                          ? '1px dashed var(--border-light)'
                          : (isChecked ? '1px solid var(--accent)' : '1px solid var(--border-light)'),
                        borderRadius: 'var(--radius-sm)',
                        cursor: hasSubtopics ? 'not-allowed' : 'pointer',
                        fontSize: '12px',
                        color: hasSubtopics ? 'var(--text-muted)' : 'var(--text)',
                        fontWeight: hasSubtopics ? 700 : 400,
                        opacity: hasSubtopics ? 0.75 : 1,
                        whiteSpace: 'nowrap',
                        transition: 'all 0.2s ease'
                      }}
                      title={hasSubtopics ? 'This topic contains subtopics. Please select specific subtopics below.' : undefined}
                    >
                      <input
                        type="checkbox"
                        checked={!hasSubtopics && isChecked}
                        disabled={hasSubtopics}
                        onChange={() => {
                          if (!hasSubtopics) onToggleTopic(top);
                        }}
                      />
                      <span>{top.topic}</span>
                      {hasSubtopics && (
                        <span style={{ fontSize: '9px', fontWeight: 600, color: 'var(--accent)', background: 'rgba(59, 130, 246, 0.12)', padding: '1px 5px', borderRadius: '4px', marginLeft: '2px' }}>
                          (Has Subtopics)
                        </span>
                      )}
                      <span
                        style={{
                          fontSize: '10px',
                          fontWeight: 700,
                          marginLeft: '4px',
                          padding: '1px 6px',
                          borderRadius: '6px',
                          background: isChecked ? 'rgba(59, 130, 246, 0.25)' : 'var(--border-light, rgba(255,255,255,0.08))',
                          border: '1px solid var(--border-light, rgba(255,255,255,0.1))',
                          display: 'inline-flex',
                          alignItems: 'center',
                          gap: '3px'
                        }}
                        title={`Objective Questions: ${(top as any).objectiveCount ?? 0} | Subjective Questions: ${(top as any).subjectiveCount ?? 0}`}
                      >
                        <span style={{ color: '#38bdf8' }}>O: {(top as any).objectiveCount ?? 0}</span>
                        <span style={{ opacity: 0.4 }}>|</span>
                        <span style={{ color: '#c084fc' }}>S: {(top as any).subjectiveCount ?? 0}</span>
                      </span>
                    </label>
                  );
                })
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
