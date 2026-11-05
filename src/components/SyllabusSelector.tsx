import React from 'react';
import { isSameTopic } from '@/lib/syllabusUtils';
import { Topic, Chapter } from '@/types/syllabus.types';

export type { Topic, Chapter };

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
  singleTopicSelect?: boolean;
  
  onCreateQBTopic?: (topic: T) => void;
  onCreateQBChapter?: (chapter: Chapter) => void;
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
  topicPlaceholder = 'Select at least one chapter first.',
  singleTopicSelect = false,
  onCreateQBTopic,
  onCreateQBChapter
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
    return selectedTopics.some(s => isSameTopic(s, top));
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
      {/* Subjects Selection */}
      {availableSubjects.length > 0 && (
        <div>
          <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '3px' }}>
            Select Subjects
          </label>
          <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap', padding: '2px 0' }}>
            {availableSubjects.map(s => {
              const isChecked = isSubjectChecked(s);
              return (
                <label
                  key={s}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '5px',
                    padding: '3px 7px',
                    background: isChecked ? 'var(--accent-soft)' : 'var(--surface)',
                    border: isChecked ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    fontSize: '11.5px',
                    color: 'var(--text)',
                    whiteSpace: 'nowrap',
                    transition: 'all 0.15s ease'
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
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          {/* Chapters selection */}
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
              <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>
                Chapters ({selectedChapters.size} selected)
              </label>
              <div style={{ display: 'flex', gap: '6px' }}>
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
            <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap', maxHeight: '180px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '6px 8px', background: 'var(--bg-soft)' }}>
              {availableChapters.map((ch, idx) => {
                const isChecked = selectedChapters.has(idx);
                return (
                  <label
                    key={idx}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: '5px',
                      padding: '3px 7px',
                      background: isChecked ? 'var(--accent-soft)' : 'var(--surface)',
                      border: isChecked ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                      borderRadius: 'var(--radius-sm)',
                      cursor: 'pointer',
                      fontSize: '11.5px',
                      color: 'var(--text)',
                      whiteSpace: 'nowrap',
                      transition: 'all 0.15s ease'
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
                        fontSize: '9.5px',
                        fontWeight: 700,
                        marginLeft: '3px',
                        padding: '1px 5px',
                        borderRadius: '4px',
                        background: isChecked ? 'var(--accent-ring)' : 'var(--border-light, rgba(255,255,255,0.08))',
                        border: '1px solid var(--border-light, rgba(255,255,255,0.1))',
                        display: 'inline-flex',
                        alignItems: 'center',
                        gap: '2px'
                      }}
                      title={`Objective Questions: ${ch.objectiveCount ?? ch.chapter?.objectiveCount ?? 0} | Subjective Questions: ${ch.subjectiveCount ?? ch.chapter?.subjectiveCount ?? 0}`}
                    >
                      <span style={{ color: 'var(--accent)' }}>O: {ch.objectiveCount ?? ch.chapter?.objectiveCount ?? 0}</span>
                      <span style={{ opacity: 0.4 }}>|</span>
                      <span style={{ color: 'var(--accent)' }}>S: {ch.subjectiveCount ?? ch.chapter?.subjectiveCount ?? 0}</span>
                    </span>
                    {(() => {
                      const condTopics = ch.conductedTopicsCount ?? ch.chapter?.conductedTopicsCount ?? 0;
                      const totTopics = ch.totalTopicsCount ?? ch.chapter?.totalTopicsCount ?? (Array.isArray(ch.chapter?.topics) ? ch.chapter.topics.length : 0);
                      const exStatus = ch.examStatus ?? ch.chapter?.examStatus ?? (condTopics > 0 && condTopics >= totTopics ? 'all_conducted' : condTopics > 0 ? 'partial_conducted' : 'unconducted');

                      if (exStatus === 'all_conducted' || (condTopics > 0 && condTopics >= totTopics)) {
                        return (
                          <span
                            style={{
                              fontSize: '9px',
                              fontWeight: 700,
                              marginLeft: '3px',
                              padding: '1px 5px',
                              borderRadius: '4px',
                              background: 'rgba(16, 185, 129, 0.18)',
                              color: '#34d399',
                              border: '1px solid rgba(16, 185, 129, 0.4)',
                              display: 'inline-flex',
                              alignItems: 'center',
                              gap: '3px'
                            }}
                            title={`All ${totTopics} topics in this chapter tested`}
                          >
                            <span>🟢</span>
                            <span>All Tested (${condTopics}/${totTopics})</span>
                          </span>
                        );
                      }
                      if (exStatus === 'partial_conducted' || condTopics > 0) {
                        return (
                          <span
                            style={{
                              fontSize: '9px',
                              fontWeight: 700,
                              marginLeft: '3px',
                              padding: '1px 5px',
                              borderRadius: '4px',
                              background: 'rgba(245, 158, 11, 0.18)',
                              color: '#fbbf24',
                              border: '1px solid rgba(245, 158, 11, 0.4)',
                              display: 'inline-flex',
                              alignItems: 'center',
                              gap: '3px'
                            }}
                            title={`${condTopics} of ${totTopics} topics tested in this chapter`}
                          >
                            <span>🟡</span>
                            <span>${condTopics}/${totTopics} Tested</span>
                          </span>
                        );
                      }
                      return (
                        <span
                          style={{
                            fontSize: '9px',
                            fontWeight: 600,
                            marginLeft: '3px',
                            padding: '1px 5px',
                            borderRadius: '4px',
                            background: 'rgba(148, 163, 184, 0.08)',
                            color: 'var(--text-muted, #94a3b8)',
                            border: '1px solid rgba(148, 163, 184, 0.18)',
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '3px'
                          }}
                          title="No exams conducted on any topic in this chapter yet"
                        >
                          <span>⚪</span>
                          <span>Untested{totTopics > 0 ? ` (0/${totTopics})` : ''}</span>
                        </span>
                      );
                    })()}
                    {onCreateQBChapter && (
                      <button
                        type="button"
                        onClick={(e) => {
                          e.preventDefault();
                          e.stopPropagation();
                          onCreateQBChapter(ch);
                        }}
                        style={{
                          marginLeft: '3px',
                          fontSize: '9px',
                          fontWeight: 800,
                          padding: '1px 5px',
                          borderRadius: '4px',
                          background: ((ch.objectiveCount ?? ch.chapter?.objectiveCount ?? 0) === 0) ? 'rgba(239, 68, 68, 0.15)' : 'rgba(59, 130, 246, 0.12)',
                          color: ((ch.objectiveCount ?? ch.chapter?.objectiveCount ?? 0) === 0) ? '#f87171' : 'var(--accent)',
                          border: ((ch.objectiveCount ?? ch.chapter?.objectiveCount ?? 0) === 0) ? '1px solid rgba(239, 68, 68, 0.35)' : '1px solid rgba(59, 130, 246, 0.25)',
                          cursor: 'pointer',
                          display: 'inline-flex',
                          alignItems: 'center',
                          gap: '2px'
                        }}
                        title={`Open Create Question Bank (AI) for Chapter ${ch.chapterNumber}`}
                      >
                        <span>✨</span>
                        <span>+QB</span>
                      </button>
                    )}
                  </label>
                );
              })}
            </div>
          </div>

          {/* Topics selection */}
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
              <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>
                {singleTopicSelect ? `Select Topic (1 Topic at a time for Question Bank generation)` : `Topics (${selectedTopics.length} selected)`}
              </label>
              {!singleTopicSelect && (
                <div style={{ display: 'flex', gap: '6px' }}>
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
              )}
            </div>
            <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap', maxHeight: '180px', overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '6px 8px', background: 'var(--bg-soft)' }}>
              {availableTopics.length === 0 ? (
                <div style={{ width: '100%', textAlign: 'center', padding: '14px', color: 'var(--text-muted)', fontSize: '11px' }}>
                  {topicPlaceholder}
                </div>
              ) : (
                availableTopics.map((top, idx) => {
                  const hasSubtopics = !!(top as any).hasSubtopics;
                  const isChecked = isTopicChecked(top);
                  const childSubtopics = hasSubtopics ? availableTopics.filter(t => {
                    const tCh = String((t as any).chapterNumber || '').trim();
                    const tNum = String((t as any).topicNumber || '').trim();
                    const topNum = String((top as any).topicNumber || '').trim();
                    return tCh === String((top as any).chapterNumber || '').trim() && tNum.startsWith(`${topNum}.`);
                  }) : [];
                  const areAllSubtopicsSelected = hasSubtopics && childSubtopics.length > 0 && childSubtopics.every(cs => selectedTopics.some(s => isSameTopic(s, cs)));
                  const isPartiallySelected = hasSubtopics && !areAllSubtopicsSelected && childSubtopics.some(cs => selectedTopics.some(s => isSameTopic(s, cs)));
                  return (
                    <label
                      key={idx}
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: '5px',
                        padding: '3px 7px',
                        background: hasSubtopics 
                          ? 'var(--bg-soft)' 
                          : (isChecked ? 'rgba(59, 130, 246, 0.1)' : 'var(--surface)'),
                        border: (hasSubtopics ? (areAllSubtopicsSelected || isPartiallySelected) : isChecked)
                          ? '1.5px solid var(--accent)'
                          : ((((top as any).testsCount ?? 0) > 0) ? '1px solid rgba(16, 185, 129, 0.35)' : (hasSubtopics ? '1px dashed var(--border-light)' : '1px solid var(--border-light)')),
                        borderRadius: 'var(--radius-sm)',
                        cursor: 'pointer',
                        fontSize: '11.5px',
                        color: (hasSubtopics ? (areAllSubtopicsSelected || isPartiallySelected) : isChecked) ? 'var(--accent)' : 'var(--text)',
                        fontWeight: hasSubtopics ? 700 : (isChecked ? 700 : 400),
                        opacity: 1,
                        whiteSpace: 'nowrap',
                        transition: 'all 0.15s ease'
                      }}
                      title={hasSubtopics ? 'Click to select / deselect all subtopics under this topic' : undefined}
                    >
                      <input
                        type={singleTopicSelect ? "radio" : "checkbox"}
                        name={singleTopicSelect ? "qb_single_topic_selection" : undefined}
                        checked={hasSubtopics ? areAllSubtopicsSelected : isChecked}
                        ref={el => { if (el) el.indeterminate = isPartiallySelected; }}
                        onChange={() => onToggleTopic(top)}
                      />
                      <span>{top.topic}</span>
                      {hasSubtopics && (
                        <span style={{ fontSize: '9px', fontWeight: 600, color: 'var(--accent)', background: 'rgba(59, 130, 246, 0.12)', padding: '1px 5px', borderRadius: '4px', marginLeft: '2px' }}>
                          (Has Subtopics)
                        </span>
                      )}
                      <span
                        style={{
                          fontSize: '9.5px',
                          fontWeight: 700,
                          marginLeft: '3px',
                          padding: '1px 5px',
                          borderRadius: '4px',
                          background: isChecked ? 'var(--accent-soft)' : 'var(--surface-2)',
                          border: '1px solid var(--border-light)',
                          display: 'inline-flex',
                          alignItems: 'center',
                          gap: '2px'
                        }}
                        title={`Objective Questions: ${(top as any).objectiveCount ?? 0} | Subjective Questions: ${(top as any).subjectiveCount ?? 0}`}
                      >
                        <span style={{ color: 'var(--info)' }}>O: {(top as any).objectiveCount ?? 0}</span>
                        <span style={{ opacity: 0.4 }}>|</span>
                        <span style={{ color: 'var(--purple)' }}>S: {(top as any).subjectiveCount ?? 0}</span>
                      </span>

                      {(() => {
                        const tTests = (top as any).testsCount ?? 0;
                        if (tTests > 0) {
                          return (
                            <span
                              style={{
                                marginLeft: '3px',
                                fontSize: '9px',
                                fontWeight: 700,
                                padding: '1px 5px',
                                borderRadius: '4px',
                                background: 'rgba(16, 185, 129, 0.16)',
                                color: '#10b981',
                                border: '1px solid rgba(16, 185, 129, 0.35)',
                                display: 'inline-flex',
                                alignItems: 'center',
                                gap: '2px'
                              }}
                              title={`Exam conducted on this topic (${tTests} test${tTests > 1 ? 's' : ''})`}
                            >
                              <span>✓</span>
                              <span>{tTests} Exam{tTests > 1 ? 's' : ''}</span>
                            </span>
                          );
                        }
                        return (
                          <span
                            style={{
                              marginLeft: '3px',
                              fontSize: '9px',
                              fontWeight: 600,
                              padding: '1px 5px',
                              borderRadius: '4px',
                              background: 'rgba(148, 163, 184, 0.08)',
                              color: 'var(--text-muted, #94a3b8)',
                              border: '1px solid rgba(148, 163, 184, 0.18)',
                              display: 'inline-flex',
                              alignItems: 'center',
                              gap: '2px'
                            }}
                            title="No exams conducted on this topic yet"
                          >
                            <span>○</span>
                            <span>Untested</span>
                          </span>
                        );
                      })()}
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
