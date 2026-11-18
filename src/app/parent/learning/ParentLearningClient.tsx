'use client';

import React, { useEffect, useState, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import useSWR from 'swr';
import { fetchWithToken } from '@/lib/swrFetcher';
import { ParentPageShell } from '@/components/parent';
import { TabsSkeleton } from '@/components/common/Skeletons';
import { useToggleSet } from '@/hooks/useToggleSet';
import { formatDateOrFallback } from '@/lib/dateUtils';
import { getProgressColor } from '@/types/scorecard.types';
import { MASTERY_THRESHOLDS } from '@/lib/dashboardMetrics';
import { getCanonicalSubjectName } from '@/lib/questionTypes';

interface LearningTopicItem {
  topicCode: string;
  topicName: string;
  topicNumber: string;
  chapterCode: string;
  chapterName: string;
  chapterNumber: string;
  subjectCode: string;
  subjectName: string;
  mastery: number;
  confidence: number;
  priorityScore: number;
  lastAttempt: string | null;
  attempts: number;
  lastScore: number;
  state: string;
  practiceCount: number;
  targetQuestions?: number;
  totalQuestions?: number;
  isAbsentExam?: boolean;
}

interface LearningPathData {
  studentCode: string;
  needsAttention: LearningTopicItem[];
  continuePractice: LearningTopicItem[];
  revision: LearningTopicItem[];
  mastered: LearningTopicItem[];
}

export default function ParentLearningClient() {
  const { firebaseUser } = useAuth();
  const router = useRouter();

  // Child selection state
  const [children, setChildren] = useState<{ code: string; name: string }[]>([]);
  const [selectedChildCode, setSelectedChildCode] = useState<string>(() => {
    if (typeof window !== 'undefined') {
      const params = new URLSearchParams(window.location.search);
      return params.get('studentCode') || params.get('child') || '';
    }
    return '';
  });

  // Fetch parent dashboard to get children list
  useEffect(() => {
    let isMounted = true;
    async function loadParentProfile() {
      if (!firebaseUser) return;
      try {
        const idToken = await firebaseUser.getIdToken();
        const res = await fetch('/api/parent/dashboard', {
          headers: { 'Authorization': `Bearer ${idToken}` }
        });
        if (res.ok && isMounted) {
          const data = await res.json();
          const mapped = (data.children || []).map((c: any) => ({
            code: c.studentCode,
            name: c.name || c.studentCode
          }));
          setChildren(mapped);
          if (mapped.length > 0 && !selectedChildCode) {
            setSelectedChildCode(mapped[0].code);
          }
        }
      } catch (err) {
        console.warn('Failed to load children profiles:', err);
      }
    }
    loadParentProfile();
    return () => { isMounted = false; };
  }, [firebaseUser, selectedChildCode]);

  // Sync selectedChildCode with URL
  const handleSelectChild = (code: string) => {
    setSelectedChildCode(code);
    router.replace(`/parent/learning?studentCode=${encodeURIComponent(code)}`);
  };

  // Learning data fetcher
  const swrKey = firebaseUser && selectedChildCode 
    ? `/api/parent/learning?studentCode=${encodeURIComponent(selectedChildCode)}` 
    : null;

  const { data, error: swrError, isLoading } = useSWR<LearningPathData>(
    swrKey,
    async (url: string) => {
      const res = await fetchWithToken(url, firebaseUser);
      return res;
    },
    { revalidateOnFocus: false, dedupingInterval: 60000 }
  );

  const [activeTab, setActiveTab] = useState<'needsAttention' | 'continuePractice' | 'mastered'>('needsAttention');
  const [practiceSubFilter, setPracticeSubFilter] = useState<'all' | 'zero' | 'in_progress' | 'locked'>('all');
  const [searchTerm, setSearchTerm] = useState('');

  // Expand / collapse hooks
  const [expandedSubjects, toggleSubject, isSubjectExpanded, setExpandedSubjects] = useToggleSet();
  const [expandedChapters, toggleChapterSet, isChapterExpanded, setExpandedChapters] = useToggleSet();

  // Auto-expand first subject on load
  useEffect(() => {
    if (data && expandedSubjects.size === 0) {
      const firstSub = [
        ...data.needsAttention,
        ...data.continuePractice,
        ...data.revision,
        ...data.mastered
      ][0]?.subjectName;
      if (firstSub) {
        setExpandedSubjects(new Set([firstSub]));
      }
    }
  }, [data, expandedSubjects.size, setExpandedSubjects]);

  const toggleChapter = (subjName: string, chapterName: string) => {
    toggleChapterSet(`${subjName}||${chapterName}`);
  };

  // Sub-filter counts
  const practiceBreakdown = useMemo(() => {
    if (!data?.continuePractice) return { total: 0, zero: 0, inProgress: 0, locked: 0 };
    let zero = 0;
    let inProgress = 0;
    let locked = 0;
    for (const t of data.continuePractice) {
      const pCount = t.practiceCount || 0;
      if (pCount === 0) zero++;
      else if (pCount < 2) inProgress++;
      else locked++;
    }
    return { total: data.continuePractice.length, zero, inProgress, locked };
  }, [data?.continuePractice]);

  // Group topics for current tab
  const currentTabTopics = useMemo(() => {
    if (!data) return [];
    let list: LearningTopicItem[] = [];
    if (activeTab === 'needsAttention') list = data.needsAttention || [];
    else if (activeTab === 'continuePractice') {
      list = (data.continuePractice || []).filter(t => {
        const pCount = t.practiceCount || 0;
        if (practiceSubFilter === 'zero') return pCount === 0;
        if (practiceSubFilter === 'in_progress') return pCount > 0 && pCount < 2;
        if (practiceSubFilter === 'locked') return pCount >= 2;
        return true;
      });
    } else if (activeTab === 'mastered') list = data.mastered || [];

    if (searchTerm.trim()) {
      const q = searchTerm.toLowerCase();
      list = list.filter(t => 
        (t.topicName || '').toLowerCase().includes(q) ||
        (t.chapterName || '').toLowerCase().includes(q) ||
        (t.subjectName || '').toLowerCase().includes(q) ||
        (t.topicCode || '').toLowerCase().includes(q)
      );
    }
    return list;
  }, [data, activeTab, practiceSubFilter, searchTerm]);

  // Group by Subject -> Chapter
  const groupedData = useMemo(() => {
    const map = new Map<string, Map<string, LearningTopicItem[]>>();
    for (const t of currentTabTopics) {
      const subj = t.subjectName || getCanonicalSubjectName(t.subjectCode) || 'General';
      const chap = t.chapterName || `Chapter ${t.chapterNumber || 'General'}`;
      if (!map.has(subj)) map.set(subj, new Map());
      const subMap = map.get(subj)!;
      if (!subMap.has(chap)) subMap.set(chap, []);
      subMap.get(chap)!.push(t);
    }
    return map;
  }, [currentTabTopics]);

  const activeChildName = children.find(c => c.code === selectedChildCode)?.name || selectedChildCode;

  return (
    <ParentPageShell maxWidth="960px" backHref="/parent">
      <div style={{ maxWidth: '960px', margin: '0 auto', padding: '12px 14px 40px' }}>
        
        {/* Children Selector Pills (if multiple children linked) */}
        {children.length > 1 && (
          <div style={{ display: 'flex', gap: '8px', marginBottom: '14px', overflowX: 'auto', paddingBottom: '4px' }}>
            {children.map(child => (
              <button
                key={child.code}
                onClick={() => handleSelectChild(child.code)}
                style={{
                  padding: '5px 12px',
                  borderRadius: '16px',
                  fontSize: '12px',
                  fontWeight: 700,
                  whiteSpace: 'nowrap',
                  cursor: 'pointer',
                  border: selectedChildCode === child.code ? '1.5px solid var(--accent)' : '1px solid var(--border)',
                  background: selectedChildCode === child.code ? 'var(--accent)' : 'var(--surface-2)',
                  color: selectedChildCode === child.code ? '#ffffff' : 'var(--text)'
                }}
              >
                👤 {child.name}
              </button>
            ))}
          </div>
        )}

        {/* Page Subtitle & Selected Child Banner */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px', flexWrap: 'wrap', gap: '6px' }}>
          <div>
            <h2 style={{ fontSize: '18px', fontWeight: 800, margin: 0, color: 'var(--text)' }}>
              🧭 Learning OS (LOS) • {activeChildName}
            </h2>
            <div style={{ fontSize: '11.5px', color: 'var(--text-muted)' }}>
              Live topic mastery status, practice completion, and diagnostic guidance for your child.
            </div>
          </div>
          <span style={{
            fontSize: '11px',
            fontWeight: 700,
            padding: '2px 8px',
            borderRadius: '10px',
            background: 'rgba(59, 130, 246, 0.12)',
            color: 'var(--accent)'
          }}>
            Parent Portal View
          </span>
        </div>

        {/* Search Input */}
        <div style={{ marginBottom: '10px' }}>
          <input
            type="text"
            placeholder="Search subject, chapter or topic..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{
              width: '100%',
              padding: '7px 12px',
              borderRadius: 'var(--radius-sm)',
              border: '1px solid var(--border)',
              background: 'var(--surface)',
              color: 'var(--text)',
              fontSize: '13px'
            }}
          />
        </div>

        {/* Loading State */}
        {isLoading && (
          <div style={{ padding: '40px 0', textAlign: 'center', color: 'var(--text-muted)' }}>
            <TabsSkeleton />
            <div style={{ marginTop: '12px', fontSize: '13px' }}>Loading topic mastery data...</div>
          </div>
        )}

        {/* Error State */}
        {swrError && (
          <div className="card" style={{ padding: '20px', textAlign: 'center', background: 'var(--surface)', border: '1px solid var(--danger)', borderRadius: 'var(--radius)' }}>
            <div style={{ fontSize: '28px', marginBottom: '8px' }}>⚠️</div>
            <div style={{ fontSize: '14px', fontWeight: 700, color: 'var(--danger)', marginBottom: '4px' }}>
              Unable to load Learning OS
            </div>
            <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
              {swrError.message || 'Access restricted or network issue.'}
            </div>
          </div>
        )}

        {!isLoading && !swrError && data && (
          <>
            {/* Streamlined Single-Line Active Syllabus Coverage Status */}
            {(() => {
              const masteredCount = data.mastered?.length || 0;
              const practiceCount = data.continuePractice?.length || 0;
              const focusCount = data.needsAttention?.length || 0;
              const totalConducted = masteredCount + practiceCount + focusCount;
              const completionPercent = totalConducted > 0 ? Math.round((masteredCount / totalConducted) * 100) : 0;
              const isAllExhausted = totalConducted > 0 && practiceCount === 0 && focusCount === 0;

              return (
                <div style={{
                  background: isAllExhausted 
                    ? 'linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(56, 189, 248, 0.12))' 
                    : 'var(--surface)',
                  border: `1px solid ${isAllExhausted ? 'rgba(52, 211, 153, 0.4)' : 'var(--border-light)'}`,
                  borderRadius: 'var(--radius)',
                  padding: '8px 12px',
                  marginBottom: '10px',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  gap: '10px'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', fontWeight: 700, color: 'var(--text)', whiteSpace: 'nowrap' }}>
                    <span style={{ color: 'var(--text-muted)', fontWeight: 800 }}>Status:</span>
                    <span style={{ color: isAllExhausted ? 'var(--success)' : 'var(--accent)', fontWeight: 800 }}>
                      {masteredCount} / {totalConducted} Topics Done
                    </span>
                    <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>
                      ({completionPercent}%)
                    </span>
                  </div>
                  <div style={{ flex: '1', maxWidth: '140px', height: '6px', background: 'var(--surface-2)', borderRadius: '3px', overflow: 'hidden' }}>
                    <div style={{ width: `${completionPercent}%`, height: '100%', background: isAllExhausted ? 'var(--success)' : 'var(--accent)', transition: 'width 0.3s ease' }}></div>
                  </div>
                </div>
              );
            })()}

            {/* Tab Controls: Uniform 2-Line Symmetric Layout */}
            <div className="review-tabs" style={{ display: 'flex', gap: '6px', marginBottom: '10px', borderBottom: 'none' }}>
              <button
                className={`tab-btn ${activeTab === 'needsAttention' ? 'active' : ''}`}
                onClick={() => setActiveTab('needsAttention')}
                style={{
                  flex: 1,
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  padding: '8px 4px',
                  borderBottom: activeTab === 'needsAttention' ? '2px solid var(--accent)' : '2px solid transparent'
                }}
              >
                <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', whiteSpace: 'nowrap', fontSize: '13px', fontWeight: 700 }}>
                  <span>🚨</span><span>Focus</span>
                </span>
                <span className="tab-count" style={{ marginTop: '4px', marginInline: 'auto' }}>
                  {data ? data.needsAttention.length : 0}
                </span>
              </button>

              <button
                className={`tab-btn ${activeTab === 'continuePractice' ? 'active' : ''}`}
                onClick={() => setActiveTab('continuePractice')}
                style={{
                  flex: 1,
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  padding: '8px 4px',
                  borderBottom: activeTab === 'continuePractice' ? '2px solid var(--accent)' : '2px solid transparent'
                }}
              >
                <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', whiteSpace: 'nowrap', fontSize: '13px', fontWeight: 700 }}>
                  <span>🔄</span><span>Practice</span>
                </span>
                <span className="tab-count" style={{ marginTop: '4px', marginInline: 'auto' }}>
                  {data ? data.continuePractice.length : 0}
                </span>
              </button>

              <button
                className={`tab-btn ${activeTab === 'mastered' ? 'active' : ''}`}
                onClick={() => setActiveTab('mastered')}
                style={{
                  flex: 1,
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  padding: '8px 4px',
                  borderBottom: activeTab === 'mastered' ? '2px solid var(--accent)' : '2px solid transparent'
                }}
              >
                <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', whiteSpace: 'nowrap', fontSize: '13px', fontWeight: 700 }}>
                  <span>🏆</span><span>Mastered</span>
                </span>
                <span className="tab-count" style={{ marginTop: '4px', marginInline: 'auto' }}>
                  {data ? data.mastered.length : 0}
                </span>
              </button>
            </div>

            {/* Practice Sub-filters in ONE Line with Horizontal Touch Scroll */}
            {activeTab === 'continuePractice' && (
              <div style={{
                display: 'flex',
                gap: '6px',
                marginBottom: '12px',
                flexWrap: 'nowrap',
                overflowX: 'auto',
                alignItems: 'center',
                paddingBottom: '4px',
                WebkitOverflowScrolling: 'touch'
              }}>
                <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', marginRight: '2px', whiteSpace: 'nowrap' }}>
                  Filter:
                </span>
                <button
                  type="button"
                  onClick={() => setPracticeSubFilter('all')}
                  style={{
                    padding: '3px 9px',
                    borderRadius: '20px',
                    fontSize: '11px',
                    fontWeight: 700,
                    whiteSpace: 'nowrap',
                    border: '1px solid ' + (practiceSubFilter === 'all' ? 'var(--accent)' : 'var(--border-light)'),
                    background: practiceSubFilter === 'all' ? 'var(--accent)' : 'var(--bg-soft)',
                    color: practiceSubFilter === 'all' ? '#ffffff' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  All Practice ({practiceBreakdown.total})
                </button>
                <button
                  type="button"
                  onClick={() => setPracticeSubFilter('zero')}
                  style={{
                    padding: '3px 9px',
                    borderRadius: '20px',
                    fontSize: '11px',
                    fontWeight: 800,
                    whiteSpace: 'nowrap',
                    border: '1px solid ' + (practiceSubFilter === 'zero' ? '#ef4444' : 'var(--border-light)'),
                    background: practiceSubFilter === 'zero' ? 'rgba(239, 68, 68, 0.18)' : 'var(--bg-soft)',
                    color: practiceSubFilter === 'zero' ? '#ef4444' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  🔴 Zero Practice ({practiceBreakdown.zero})
                </button>
                <button
                  type="button"
                  onClick={() => setPracticeSubFilter('in_progress')}
                  style={{
                    padding: '3px 9px',
                    borderRadius: '20px',
                    fontSize: '11px',
                    fontWeight: 700,
                    whiteSpace: 'nowrap',
                    border: '1px solid ' + (practiceSubFilter === 'in_progress' ? '#f59e0b' : 'var(--border-light)'),
                    background: practiceSubFilter === 'in_progress' ? 'rgba(245, 158, 11, 0.18)' : 'var(--bg-soft)',
                    color: practiceSubFilter === 'in_progress' ? '#f59e0b' : 'var(--text-muted)',
                    cursor: 'pointer'
                  }}
                >
                  🟡 In Progress ({practiceBreakdown.inProgress})
                </button>
                {practiceBreakdown.locked > 0 && (
                  <button
                    type="button"
                    onClick={() => setPracticeSubFilter('locked')}
                    style={{
                      padding: '3px 9px',
                      borderRadius: '20px',
                      fontSize: '11px',
                      fontWeight: 700,
                      whiteSpace: 'nowrap',
                      border: '1px solid ' + (practiceSubFilter === 'locked' ? '#94a3b8' : 'var(--border-light)'),
                      background: practiceSubFilter === 'locked' ? 'rgba(148, 163, 184, 0.25)' : 'var(--bg-soft)',
                      color: practiceSubFilter === 'locked' ? 'var(--text)' : 'var(--text-muted)',
                      cursor: 'pointer'
                    }}
                  >
                    🔒 Quota Locked ({practiceBreakdown.locked})
                  </button>
                )}
              </div>
            )}

            {/* Empty state */}
            {currentTabTopics.length === 0 && (
              <div style={{ textAlign: 'center', padding: '40px 16px', background: 'var(--surface)', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)' }}>
                <div style={{ fontSize: '28px', marginBottom: '8px' }}>
                  {activeTab === 'mastered' ? '🏆' : (activeTab === 'needsAttention' ? '🎉' : '📖')}
                </div>
                <div style={{ fontSize: '14px', fontWeight: 700, color: 'var(--text)', marginBottom: '4px' }}>
                  {activeTab === 'needsAttention'
                    ? 'No topics currently in Focus. Everything tested is progressing solidly!'
                    : (activeTab === 'mastered' ? 'No topics fully mastered yet. Ongoing practice will certify topics.' : 'No topics currently in this practice filter.')}
                </div>
              </div>
            )}

            {/* Syllabus Accordion Lists */}
            {Array.from(groupedData.entries()).map(([subjName, chapters]) => {
              const isSubjExpanded = isSubjectExpanded(subjName);
              const allSubjTopics = Array.from(chapters.values()).flat();
              const subjectMastery = allSubjTopics.length > 0
                ? allSubjTopics.reduce((acc, t) => acc + (t.mastery || 0), 0) / allSubjTopics.length
                : 0;

              return (
                <div key={subjName} style={{ marginBottom: '10px', border: '1px solid var(--border)', borderRadius: 'var(--radius)', background: 'var(--surface)', overflow: 'hidden' }}>
                  <div
                    onClick={() => toggleSubject(subjName)}
                    style={{
                      padding: '10px 14px',
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                      cursor: 'pointer',
                      background: 'var(--surface-2)',
                      borderBottom: isSubjExpanded ? '1px solid var(--border)' : 'none'
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ fontSize: '15px' }}>📖</span>
                      <span style={{ fontWeight: 800, fontSize: '13.5px', color: 'var(--text)' }}>{subjName}</span>
                      <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>({allSubjTopics.length} topics)</span>
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text)' }}>{Math.round(subjectMastery)}%</span>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', transform: isSubjExpanded ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }}>▼</span>
                    </div>
                  </div>

                  {isSubjExpanded && (
                    <div style={{ padding: '8px 10px' }}>
                      {Array.from(chapters.entries()).map(([chapterName, topics]) => {
                        const chapterKey = `${subjName}||${chapterName}`;
                        const isChExpanded = expandedChapters.has(chapterKey);
                        const chMastery = topics.length > 0
                          ? topics.reduce((acc, t) => acc + (t.mastery || 0), 0) / topics.length
                          : 0;

                        return (
                          <div key={chapterName} style={{ marginBottom: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--bg-soft)', overflow: 'hidden' }}>
                            <div
                              onClick={() => toggleChapter(subjName, chapterName)}
                              style={{
                                padding: '8px 12px',
                                display: 'flex',
                                justifyContent: 'space-between',
                                alignItems: 'center',
                                cursor: 'pointer',
                                borderBottom: isChExpanded ? '1px solid var(--border-light)' : 'none'
                              }}
                            >
                              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                                <span style={{ fontSize: '9px', transform: isChExpanded ? 'rotate(90deg)' : 'none', transition: 'transform 0.15s' }}>▶</span>
                                <span style={{ fontWeight: 700, fontSize: '13px', color: 'var(--text)' }}>📘 {chapterName}</span>
                                <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>({topics.length})</span>
                              </div>
                              <span style={{ fontSize: '11.5px', fontWeight: 700, color: getProgressColor(chMastery) }}>{Math.round(chMastery)}%</span>
                            </div>

                            {isChExpanded && (
                              <div style={{ padding: '8px 10px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                                {topics.map(topic => {
                                  const mastery = Math.round(topic.mastery);
                                  const confidence = Math.round(topic.confidence);
                                  const attempts = Number(topic.attempts || topic.confidence || 0);
                                  const isAbsent = !!topic.isAbsentExam;
                                  const state = topic.state;
                                  const practiceCount = topic.practiceCount || 0;
                                  const isMasteredState = state === 'mastered';

                                  let statusBadgeColor = 'var(--text-muted)';
                                  let statusBadgeBg = 'rgba(148, 163, 184, 0.12)';
                                  let statusLabel = 'Needs Attention';
                                  let masteryBarColor = 'var(--danger)';

                                  if (isMasteredState) {
                                    statusBadgeColor = 'var(--success)';
                                    statusBadgeBg = 'rgba(16, 185, 129, 0.12)';
                                    statusLabel = 'Mastered';
                                    masteryBarColor = 'var(--success)';
                                  } else if (state === 'practicing' || state === 'continuePractice' || state === 'revision') {
                                    statusBadgeColor = 'var(--warning)';
                                    statusBadgeBg = 'rgba(245, 158, 11, 0.12)';
                                    statusLabel = 'Practicing';
                                    masteryBarColor = mastery >= 80 ? 'var(--warning)' : 'var(--danger)';
                                  } else {
                                    statusBadgeColor = 'var(--danger)';
                                    statusBadgeBg = 'rgba(239, 68, 68, 0.12)';
                                    statusLabel = 'Needs Attention';
                                    masteryBarColor = 'var(--danger)';
                                  }

                                  let expIcon = '⚪';
                                  let expColor = 'var(--text-muted)';
                                  let expText = '';

                                  if (state === 'needsAttention') {
                                    if (practiceCount >= 2) {
                                      expIcon = '🔒';
                                      expColor = 'var(--text-muted)';
                                      expText = `${practiceCount}/2 practices done (${mastery}% accuracy). Quota reached.`;
                                    } else if (isAbsent) {
                                      expIcon = '⚠️';
                                      expColor = 'var(--danger)';
                                      expText = 'Missed scheduled exam. Practice required to assess baseline.';
                                    } else if (attempts === 0) {
                                      expIcon = '⚪';
                                      expColor = 'var(--text-muted)';
                                      expText = 'Never practiced yet (0/2 sets). Pending 1st practice.';
                                    } else {
                                      expIcon = '🚨';
                                      expColor = 'var(--danger)';
                                      expText = `${practiceCount}/2 practices done (${mastery}% accuracy). Needs attention in weak concepts.`;
                                    }
                                  } else if (state === 'practicing' || state === 'continuePractice' || state === 'revision') {
                                    if (mastery >= MASTERY_THRESHOLDS.MASTERED_MIN && attempts < 12) {
                                      const needed = Math.max(1, 12 - attempts);
                                      expIcon = '📖';
                                      expColor = 'var(--accent)';
                                      expText = `High accuracy (${mastery}%), but needs ${needed} more verified question(s) for Certified Mastered.`;
                                    } else if (practiceCount >= 2) {
                                      expIcon = '🔒';
                                      expColor = 'var(--text-muted)';
                                      expText = `2/2 practices done (${mastery}% accuracy). Practice quota completed.`;
                                    } else {
                                      expIcon = '📈';
                                      expColor = 'var(--warning)';
                                      expText = `${practiceCount}/2 practices done (${mastery}% accuracy). On track toward Mastered.`;
                                    }
                                  } else if (state === 'mastered') {
                                    expIcon = '⭐';
                                    expColor = 'var(--success)';
                                    expText = `Mastered (${mastery}% accuracy across ${attempts} verified questions). Concept complete.`;
                                  } else {
                                    expIcon = '⚪';
                                    expColor = 'var(--text-muted)';
                                    expText = `${mastery}% accuracy across ${attempts} verified questions.`;
                                  }

                                  return (
                                    <div
                                      key={topic.topicCode}
                                      style={{
                                        background: 'var(--surface)',
                                        borderRadius: '8px',
                                        border: '1px solid var(--border-light)',
                                        padding: '10px 12px',
                                        display: 'flex',
                                        flexDirection: 'column',
                                        gap: '6px'
                                      }}
                                    >
                                      {/* Row 1: Topic Name & Status Badge */}
                                      <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: '8px' }}>
                                        <div style={{ fontWeight: 600, fontSize: '13px', color: 'var(--text)', lineHeight: 1.35, flex: 1 }}>
                                          📍 {topic.topicName || topic.topicCode}
                                        </div>
                                        <span style={{
                                          fontSize: '11px',
                                          fontWeight: 700,
                                          padding: '2px 8px',
                                          borderRadius: '12px',
                                          background: statusBadgeBg,
                                          color: statusBadgeColor,
                                          whiteSpace: 'nowrap',
                                          flexShrink: 0
                                        }}>
                                          {statusLabel} • {mastery}%
                                        </span>
                                      </div>

                                      {/* Row 2: Mastery Progress Bar */}
                                      <div style={{ width: '100%', height: '4px', background: 'rgba(148, 163, 184, 0.15)', borderRadius: '2px', overflow: 'hidden' }}>
                                        <div style={{ width: `${Math.min(100, Math.max(0, mastery))}%`, height: '100%', background: masteryBarColor, borderRadius: '2px' }} />
                                      </div>

                                      {/* Row 3: Metrics */}
                                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', fontSize: '11px', color: 'var(--text-muted)' }}>
                                        <span style={{ fontWeight: 600, color: practiceCount === 0 ? '#ef4444' : 'var(--text)' }}>
                                          🎯 {practiceCount}/2 Practices Done
                                        </span>
                                        <span>•</span>
                                        <span>📊 {confidence}% Confidence ({attempts}/12 Qs)</span>
                                        <span>•</span>
                                        <span>🕒 {formatDateOrFallback(topic.lastAttempt, 'Never')}</span>
                                      </div>

                                      {/* Row 4: Diagnostic Note (Rule 2F Parity) */}
                                      <div style={{ fontSize: '11.5px', color: expColor, lineHeight: 1.35 }}>
                                        <span>{expIcon}</span> {expText}
                                      </div>
                                    </div>
                                  );
                                })}
                              </div>
                            )}
                          </div>
                        );
                      })}
                    </div>
                  )}
                </div>
              );
            })}
          </>
        )}
      </div>
    </ParentPageShell>
  );
}
