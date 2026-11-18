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
import { LearningTopicItem, LearningPathData } from '@/types/learning.types';
import { LearningStatusBar, LearningTabControls, LearningPracticeFilterBar } from '@/components/learning';

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
            <LearningStatusBar
              masteredCount={data.mastered?.length || 0}
              totalConducted={(data.mastered?.length || 0) + (data.continuePractice?.length || 0) + (data.needsAttention?.length || 0)}
            />

            {/* Tab Controls: Uniform 2-Line Symmetric Layout */}
            <LearningTabControls
              activeTab={activeTab}
              onSelectTab={setActiveTab}
              counts={{
                needsAttention: data.needsAttention?.length || 0,
                continuePractice: data.continuePractice?.length || 0,
                mastered: data.mastered?.length || 0
              }}
            />

            {/* Practice Sub-filters in ONE Line with Horizontal Touch Scroll */}
            {activeTab === 'continuePractice' && (
              <LearningPracticeFilterBar
                activeFilter={practiceSubFilter}
                onSelectFilter={setPracticeSubFilter}
                breakdown={practiceBreakdown}
              />
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
