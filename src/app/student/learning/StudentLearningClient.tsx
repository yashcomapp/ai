'use client';

import { getStudentMode } from '@/types/user.types';

import React, { useEffect, useState, useMemo, useDeferredValue } from 'react';
import { useAuth } from '@/context/AuthContext';
import useSWR from 'swr';
import { fetchWithToken, FetchError, createTokenFetcher } from '@/lib/swrFetcher';
import { getProgressColor } from '@/types/scorecard.types';
import { TabsSkeleton } from '@/components/common/Skeletons';
import { useToggleSet } from '@/hooks/useToggleSet';
import { useRouter } from 'next/navigation';
import dynamic from 'next/dynamic';

import { formatDateOrFallback } from '@/lib/dateUtils';
import { getCanonicalSubjectName } from '@/lib/questionTypes';
import { MASTERY_THRESHOLDS } from '@/lib/dashboardMetrics';
import { LearningTopicItem, StudentLearningTopicItem, LearningPathData } from '@/types/learning.types';
import { LearningStatusBar, LearningTabControls, LearningPracticeFilterBar } from '@/components/learning';

const getMaxTopicPractices = (_topic?: any): number => {
  // Single Source of Truth (SSOT): All topics have strictly 2 practice sets assigned (Target: 12 Qs)
  return 2;
};

export default function StudentLearning({ initialData }: { initialData?: LearningPathData }) {
  const { firebaseUser, user } = useAuth();
  const router = useRouter();

  const [localCache, setLocalCache] = useState<LearningPathData | null>(null);

  useEffect(() => {
    if (getStudentMode(user) === 'limited') {
      router.replace('/student');
    }
  }, [user, router]);

  useEffect(() => {
    try {
      const cached = localStorage.getItem('yc_student_learning_cache');
      if (cached) {
        setLocalCache(JSON.parse(cached));
      }
    } catch (e) {
      console.warn('Failed to load cached learning data:', e);
    }
  }, []);

  const fetcher = async (url: string) => {
    try {
      const data = await fetchWithToken(url, firebaseUser);
      if (data) {
        try {
          localStorage.setItem('yc_student_learning_cache', JSON.stringify(data));
        } catch (e) {
          console.warn('Failed to save learning cache:', e);
        }
      }
      return data;
    } catch (err: any) {
      if (err instanceof FetchError && err.status === 403) {
        throw new FetchError(
          '⛔ Permission Denied: Learning OS access is restricted for Autonomous Student accounts.',
          403,
          err.info
        );
      }
      throw err;
    }
  };

  const { data, error: swrError, isLoading } = useSWR<LearningPathData>(
    firebaseUser ? '/api/student/learning' : null,
    fetcher,
    {
      fallbackData: initialData || localCache || undefined,
      revalidateOnFocus: false,
      revalidateOnMount: !initialData,
      revalidateIfStale: false,
      dedupingInterval: 300000
    }
  );

  const error = swrError?.message || '';
  const loading = isLoading && !data;

  // Auto-expand first subject by default on data load (keep chapters collapsed to prevent clutter)
  const [expandedSubjects, toggleSubject, isSubjectExpanded, setExpandedSubjects] = useToggleSet();
  const [expandedChapters, toggleChapterSet, isChapterExpanded, setExpandedChapters] = useToggleSet();

  const [activeTab, setActiveTab] = useState<'all' | 'needsAttention' | 'continuePractice' | 'mastered'>('needsAttention');

  useEffect(() => {
    if (data && expandedSubjects.size === 0) {
      const firstSub = [
        ...data.needsAttention,
        ...data.continuePractice,
        ...data.mastered
      ].map(t => t.subjectName || getCanonicalSubjectName(t.subjectCode, t.topicCode, t.chapterName)).filter(Boolean)[0];
      if (firstSub) {
        setExpandedSubjects(new Set([firstSub]));
      }

      // Smart tab defaulting: If focus (needsAttention) has 0 topics, switch to practice or all
      if ((data.needsAttention || []).length === 0) {
        if ((data.continuePractice || []).length > 0) {
          setActiveTab('continuePractice');
        } else if ((data.mastered || []).length > 0) {
          setActiveTab('all');
        }
      }
    }
  }, [data]);
  const [practiceSubFilter, setPracticeSubFilter] = useState<'all' | 'zero' | 'in_progress' | 'locked'>('all');
  const [searchTerm, setSearchTerm] = useState('');
  const [alertMsg, setAlertMsg] = useState<{ text: string; isError: boolean } | null>(null);

  // Sorting and PDF export states
  const [sortField, setSortField] = useState<'topicName' | 'mastery' | 'attempts' | 'lastAttempt'>('mastery');
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('asc');
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);

  const handleSort = (field: 'topicName' | 'mastery' | 'attempts' | 'lastAttempt') => {
    if (sortField === field) {
      setSortDir(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortField(field);
      setSortDir('asc');
    }
  };

  const getSortedTopics = (list: StudentLearningTopicItem[]) => {
    return [...list].sort((a, b) => {
      let comparison = 0;
      if (sortField === 'topicName') {
        comparison = (a.topicName || '').localeCompare(b.topicName || '');
      } else if (sortField === 'mastery') {
        comparison = (a.mastery || 0) - (b.mastery || 0);
      } else if (sortField === 'attempts') {
        comparison = (a.attempts || 0) - (b.attempts || 0);
      } else {
        const timeA = a.lastAttempt ? new Date(a.lastAttempt).getTime() : 0;
        const timeB = b.lastAttempt ? new Date(b.lastAttempt).getTime() : 0;
        comparison = timeA - timeB;
      }
      return sortDir === 'asc' ? comparison : -comparison;
    });
  };

  const getActionText = (state: string) => {
    if (state === 'mastered') return 'Mastered';
    return 'Practice';
  };

  const getMasteryClass = (mastery: number) => {
    if (mastery < MASTERY_THRESHOLDS.PRACTICING_MIN) return 'low';
    if (mastery < MASTERY_THRESHOLDS.MASTERED_MIN) return 'medium';
    return 'high';
  };

  const getProgressColor = (mastery: number) => {
    if (mastery < MASTERY_THRESHOLDS.PRACTICING_MIN) return 'var(--danger)';
    if (mastery < MASTERY_THRESHOLDS.MASTERED_MIN) return 'var(--warning)';
    return 'var(--success)';
  };

  const toggleChapter = (subjectName: string, chapterName: string) => {
    toggleChapterSet(`${subjectName}||${chapterName}`);
  };

    const practiceBreakdown = useMemo(() => {
    const list = data?.continuePractice || [];
    let zero = 0;
    let inProgress = 0;
    let locked = 0;
    list.forEach(t => {
      const maxP = getMaxTopicPractices(t);
      const pCount = t.practiceCount || 0;
      if (pCount === 0) zero++;
      else if (pCount >= maxP) locked++;
      else inProgress++;
    });
    return { zero, inProgress, locked, total: list.length };
  }, [data?.continuePractice]);

  const focusBreakdown = useMemo(() => {
    const list = data?.needsAttention || [];
    let zero = 0;
    let inProgress = 0;
    let locked = 0;
    list.forEach(t => {
      const maxP = getMaxTopicPractices(t);
      const pCount = t.practiceCount || 0;
      if (pCount === 0) zero++;
      else if (pCount >= maxP) locked++;
      else inProgress++;
    });
    return { zero, inProgress, locked, total: list.length };
  }, [data?.needsAttention]);

  const allTopicsList = useMemo(() => {
    if (!data) return [];
    return [
      ...(data.needsAttention || []),
      ...(data.continuePractice || []),
      ...(data.mastered || [])
    ];
  }, [data]);

  const practicedCount = useMemo(() => {
    if (data?.counts?.uniqueTopicsPracticed !== undefined) {
      return data.counts.uniqueTopicsPracticed;
    }
    return allTopicsList.filter(t => (t.practiceCount || 0) > 0 || (t.attempts || 0) > 0 || (t.confidence || 0) > 0).length;
  }, [data, allTopicsList]);

  const totalConductedCount = data?.counts?.totalAssignedCount || allTopicsList.length;

  const deferredSearchTerm = useDeferredValue(searchTerm);

  // Filter topics based on active tab and search query
  const { grouped, sortedSubjects, topicsList } = useMemo(() => {
    let list: StudentLearningTopicItem[] = [];
    if (data) {
      if (activeTab === 'all') {
        list = allTopicsList;
      } else if (activeTab === 'needsAttention') {
        list = data.needsAttention || [];
      } else if (activeTab === 'continuePractice') {
        list = data.continuePractice || [];
        if (practiceSubFilter !== 'all') {
          list = list.filter(t => {
            const maxP = getMaxTopicPractices(t);
            const pCount = t.practiceCount || 0;
            if (practiceSubFilter === 'zero') return pCount === 0;
            if (practiceSubFilter === 'in_progress') return pCount > 0 && pCount < maxP;
            if (practiceSubFilter === 'locked') return pCount >= maxP;
            return true;
          });
        }
      } else if (activeTab === 'mastered') {
        list = data.mastered || [];
      }
    }

    const query = deferredSearchTerm.toLowerCase().trim();
    if (query) {
      list = list.filter(t =>
        (t.topicName || '').toLowerCase().includes(query) ||
        (t.subjectName || '').toLowerCase().includes(query) ||
        (t.chapterName || '').toLowerCase().includes(query)
      );
    }

    // Group filtered topics by subject, then by chapter
    const grp = new Map<string, Map<string, StudentLearningTopicItem[]>>();
    list.forEach(topic => {
      const sName = topic.subjectName || getCanonicalSubjectName(topic.subjectCode, topic.topicCode, topic.chapterName);
      const cName = topic.chapterName || 'General';

      if (!grp.has(sName)) {
        grp.set(sName, new Map());
      }
      const chapters = grp.get(sName)!;
      if (!chapters.has(cName)) {
        chapters.set(cName, []);
      }
      chapters.get(cName)!.push(topic);
    });

    const getSubjMastery = (subjName: string) => {
      const chapters = grp.get(subjName);
      if (!chapters) return 0;
      const allSubjTopics = Array.from(chapters.values()).flat();
      if (allSubjTopics.length === 0) return 0;
      return allSubjTopics.reduce((acc, t) => acc + t.mastery, 0) / allSubjTopics.length;
    };

    const sortedSubjs = Array.from(grp.keys()).sort((a, b) => getSubjMastery(a) - getSubjMastery(b));

    return { grouped: grp, sortedSubjects: sortedSubjs, topicsList: list };
  }, [data, activeTab, practiceSubFilter, deferredSearchTerm]);

  if (user && (user as any).autonomous) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', padding: '20px' }}>
        <div style={{ maxWidth: '480px', width: '100%', textAlign: 'center', padding: '32px 24px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--warning)', boxShadow: 'var(--shadow-glass)' }}>
          <div style={{ fontSize: '3rem', marginBottom: '12px' }}>🔒</div>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--text)', marginBottom: '8px' }}>Access Restricted / पहुँच प्रतिबंधित</h3>
          <p style={{ fontSize: '13.5px', color: 'var(--text-muted)', lineHeight: '1.5', marginBottom: '20px' }}>
            Autonomous mode is active on your account. Self-directed practice from Learning OS is disabled.
          </p>
          <button className="btn btn-primary" onClick={() => router.push('/student')}>
            🏠 Back to Dashboard
          </button>
        </div>
      </div>
    );
  }

  const renderToolbarSkeleton = () => (
    <div style={{ display: 'flex', gap: '12px', marginBottom: '20px', flexWrap: 'wrap', alignItems: 'center' }} className="skeleton-blink">
      <div style={{ flex: 1, minWidth: '240px', height: '36px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)' }}></div>
    </div>
  );

  const renderTabsSkeleton = () => (
    <div style={{ display: 'flex', gap: '8px', marginBottom: '16px', overflowX: 'auto', paddingBottom: '4px' }} className="skeleton-blink">
      {[1, 2, 3, 4, 5].map(i => (
        <div key={i} style={{ width: '100px', height: '36px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: '20px', flexShrink: 0 }}></div>
      ))}
    </div>
  );

  const renderSubjectListSkeleton = () => {
    const cachedData = initialData || localCache;
    let subjectCount = 2;
    if (cachedData) {
      const allTopics = [
        ...cachedData.needsAttention,
        ...cachedData.continuePractice,
        ...cachedData.mastered
      ];
      const subjects = new Set(allTopics.map(t => t.subjectName).filter(Boolean));
      subjectCount = subjects.size;
    }
    const count = Math.max(1, subjectCount);

    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {Array.from({ length: count }).map((_, i) => (
          <div key={i} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', background: 'var(--surface)', overflow: 'hidden' }} className="skeleton-blink">
            <div style={{ padding: '16px 20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <div style={{ width: '18px', height: '18px', background: 'var(--border-light)', borderRadius: '4px' }}></div>
                <div style={{ width: '140px', height: '14px', background: 'var(--border-light)', borderRadius: '4px' }}></div>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                <div style={{ width: '80px', height: '6px', background: 'var(--border-light)', borderRadius: '3px' }}></div>
                <div style={{ width: '30px', height: '14px', background: 'var(--border-light)', borderRadius: '4px' }}></div>
              </div>
            </div>
          </div>
        ))}
      </div>
    );
  };

  if (error) {
    const isAutonomousBlock = error && error.includes('restricted');
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div className="alert-box alert-box-danger" style={{ display: 'block', maxWidth: '400px', textAlign: 'center' }}>
          {error || 'Could not load syllabus.'}
        </div>
        <button 
          className="btn btn-primary" 
          onClick={() => isAutonomousBlock ? router.push('/student') : window.location.reload()} 
          style={{ marginTop: '16px' }}
        >
          {isAutonomousBlock ? 'Back to Dashboard' : 'Retry'}
        </button>
      </div>
    );
  }

  return (
    <div className="page-wrapper">
      
      <style>{`
        .topic-row-hover {
          transition: background-color 0.15s ease;
        }
        .topic-row-hover:hover {
          background-color: var(--bg-soft) !important;
        }
        .topic-card-hover {
          transition: all 0.15s ease;
        }
        .topic-card-hover:hover {
          border-color: var(--accent) !important;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }
        @keyframes skeleton-blink {
          0% { opacity: 0.6; }
          50% { opacity: 1; }
          100% { opacity: 0.6; }
        }
        .skeleton-blink {
          animation: skeleton-blink 1.5s infinite ease-in-out;
        }
      `}</style>

      <div className="dashboard-container" style={{ maxWidth: '1000px', margin: '0 auto', padding: '10px 8px 30px 8px' }}>
        {loading ? (
          <>
            {renderToolbarSkeleton()}
            <TabsSkeleton />
            {renderSubjectListSkeleton()}
          </>
        ) : (
          <>
            {/* Search & Toolbars */}
            <div style={{ display: 'flex', gap: '8px', marginBottom: '10px', flexWrap: 'wrap', alignItems: 'center' }}>
              <input 
                type="text" 
                placeholder="Search subject, chapter or topic..." 
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                style={{ flex: 1, minWidth: '240px', padding: '6px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border)', background: 'var(--surface)', color: 'var(--text)', fontSize: '13px' }}
              />
            </div>

            {alertMsg && (
              <div className={`alert-box ${alertMsg.isError ? 'alert-box-danger' : 'alert-box-success'}`} style={{ display: 'block', marginBottom: '8px' }}>
                {alertMsg.text}
              </div>
            )}

            {/* Streamlined Active Syllabus Coverage Status */}
            {data && (
              <LearningStatusBar
                masteredCount={data.counts?.masteredCount ?? (data.mastered?.length || 0)}
                practicedCount={practicedCount}
                totalConducted={totalConductedCount}
              />
            )}

            {/* Tab Controls: Uniform 2-Line Symmetric Layout */}
            <LearningTabControls
              activeTab={activeTab}
              onSelectTab={setActiveTab}
              counts={{
                all: totalConductedCount,
                needsAttention: data ? data.needsAttention.length : 0,
                continuePractice: data ? data.continuePractice.length : 0,
                mastered: data ? data.mastered.length : 0
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
          </>
        )}

        {/* Syllabus Accordion Lists */}
        {!loading && (
          <>
            {/* P2: Start Here High-Impact Remediation Banner */}
            {activeTab === 'needsAttention' && data?.needsAttention && data.needsAttention.length > 0 && !searchTerm && (() => {
              const topTopic = data.needsAttention[0];
              const targetUrl = `/student/topic?topicCode=${encodeURIComponent(topTopic.topicCode)}&category=needsAttention`;
              const accuracy = Math.round(topTopic.mastery || 0);
              return (
                <div style={{
                  marginBottom: '12px',
                  padding: '12px 16px',
                  background: 'linear-gradient(135deg, rgba(239, 68, 68, 0.12) 0%, rgba(249, 115, 22, 0.08) 100%)',
                  border: '1px solid rgba(239, 68, 68, 0.35)',
                  borderRadius: 'var(--radius)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  gap: '12px',
                  flexWrap: 'wrap'
                }}>
                  <div style={{ flex: '1 1 300px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '11px', fontWeight: 700, color: 'var(--danger)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                      <span>🎯</span>
                      <span>Recommended Next Step • Highest Impact</span>
                    </div>
                    <div style={{ fontSize: '14px', fontWeight: 700, color: 'var(--text)', marginTop: '2px' }}>
                      Start here: {topTopic.topicName || topTopic.topicCode}
                    </div>
                    <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
                      {accuracy > 0
                        ? `You scored ${accuracy}% accuracy on recent assessments. Complete 1 practice set to build toward Mastered.`
                        : 'Unattempted concept baseline. Complete 1 practice set (6 Qs) to assess your understanding.'}
                    </div>
                  </div>
                  <button
                    onClick={() => router.push(targetUrl)}
                    className="btn btn-sm btn-primary"
                    style={{
                      display: 'inline-flex',
                      alignItems: 'center',
                      gap: '6px',
                      fontWeight: 700,
                      fontSize: '12px',
                      padding: '6px 14px',
                      borderRadius: '6px',
                      background: 'var(--accent)',
                      color: '#fff',
                      cursor: 'pointer',
                      whiteSpace: 'nowrap'
                    }}
                  >
                    <span>Start 1st Practice</span>
                    <span>→</span>
                  </button>
                </div>
              );
            })()}

          <div id="student-learning-pathway">
            {sortedSubjects.length === 0 ? (
              <div style={{ textAlign: 'center', padding: '32px 16px', background: 'var(--surface)', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', marginTop: '8px' }}>
                {searchTerm ? (
                  <div style={{ color: 'var(--text-muted)', fontSize: '13px' }}>🔍 No topics match "{searchTerm}".</div>
                ) : activeTab === 'needsAttention' ? (
                  <div>
                    <div style={{ fontSize: '28px', marginBottom: '6px' }}>🛡️</div>
                    <div style={{ fontWeight: 800, fontSize: '14px', color: 'var(--success)' }}>All Good — Zero Topics in Focus</div>
                    <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '2px' }}>
                      No topics currently need urgent remediation. Everything tested is progressing solidly!
                    </div>
                    <div style={{ marginTop: '14px', display: 'flex', justifyContent: 'center', gap: '8px', flexWrap: 'wrap' }}>
                      {(data?.continuePractice?.length || 0) > 0 && (
                        <button
                          type="button"
                          onClick={() => setActiveTab('continuePractice')}
                          className="btn btn-sm btn-primary"
                          style={{ fontSize: '12px', padding: '6px 14px', borderRadius: '20px' }}
                        >
                          🔄 View {data?.continuePractice?.length} Practice Topics
                        </button>
                      )}
                      <button
                        type="button"
                        onClick={() => setActiveTab('all')}
                        className="btn btn-sm"
                        style={{ fontSize: '12px', padding: '6px 14px', borderRadius: '20px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)' }}
                      >
                        📋 View All {totalConductedCount} Conducted Topics
                      </button>
                    </div>
                  </div>
                ) : activeTab === 'continuePractice' ? (
                  <div>
                    <div style={{ fontSize: '28px', marginBottom: '6px' }}>🎉</div>
                    <div style={{ fontWeight: 800, fontSize: '14px', color: 'var(--text)' }}>All Assigned Practice Completed!</div>
                    <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '4px', maxWidth: '460px', margin: '4px auto 0 auto', lineHeight: 1.4 }}>
                      You have completed all regular practice sets from exams conducted to date. Great work on completing all active practice workouts!
                    </div>
                    <div style={{ marginTop: '14px', display: 'flex', justifyContent: 'center', gap: '8px', flexWrap: 'wrap' }}>
                      {(data?.mastered?.length || 0) > 0 && (
                        <button
                          type="button"
                          onClick={() => setActiveTab('mastered')}
                          className="btn btn-sm btn-primary"
                          style={{ fontSize: '12px', padding: '6px 14px', borderRadius: '20px' }}
                        >
                          🏆 View {data?.mastered?.length} Mastered Topics
                        </button>
                      )}
                      <button
                        type="button"
                        onClick={() => setActiveTab('all')}
                        className="btn btn-sm"
                        style={{ fontSize: '12px', padding: '6px 14px', borderRadius: '20px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)' }}
                      >
                        📋 View All {totalConductedCount} Conducted Topics
                      </button>
                    </div>
                  </div>
                ) : (
                  <div style={{ color: 'var(--text-muted)', fontSize: '13px' }}>📚 No topics found in this category.</div>
                )}
              </div>
            ) : (
              sortedSubjects.map(subjName => {
                const chapters = grouped.get(subjName)!;
                const allSubjTopics = Array.from(chapters.values()).flat();
                const subjectMastery = allSubjTopics.reduce((acc, t) => acc + t.mastery, 0) / allSubjTopics.length;
                const isSubjExpanded = expandedSubjects.has(subjName);
                const subjProgressColor = getProgressColor(subjectMastery);

                // Helper to compute chapter average mastery
                const getChapterMastery = (topics: StudentLearningTopicItem[]) => {
                  if (topics.length === 0) return 0;
                  return topics.reduce((acc, t) => acc + t.mastery, 0) / topics.length;
                };

                // Sort chapters such that lowest mastery is on top
                const sortedChapters = Array.from(chapters.keys()).sort((a, b) => {
                  const aMast = getChapterMastery(chapters.get(a)!);
                  const bMast = getChapterMastery(chapters.get(b)!);
                  return aMast - bMast;
                });

                return (
                  <div key={subjName} className="subject-group" style={{ marginBottom: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)', background: 'var(--surface)', overflow: 'hidden' }}>
                    <div 
                      className="subject-header" 
                      onClick={() => toggleSubject(subjName)}
                      style={{ padding: '8px 12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isSubjExpanded ? '1px solid var(--border-light)' : 'none' }}
                    >
                      <div className="subject-title" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <span className="subject-icon" style={{ fontSize: '1.1rem' }}>📖</span>
                        <span className="subject-name" style={{ fontWeight: 'bold', fontSize: '13.5px' }}>{subjName}</span>
                        <span className="subject-stats" style={{ fontSize: '10.5px', color: 'var(--text-muted)' }}>({allSubjTopics.length} topics)</span>
                      </div>
                      <div className="subject-progress" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <div className="subject-progress-bar" style={{ width: '70px', height: '5px', background: 'var(--border-light)', borderRadius: '3px', overflow: 'hidden' }}>
                          <div className="subject-progress-fill" style={{ width: `${subjectMastery}%`, height: '100%', background: subjProgressColor }}></div>
                        </div>
                        <span className="subject-percent" style={{ fontSize: '11.5px', fontWeight: 600 }}>{Math.round(subjectMastery)}%</span>
                        <span className={`expand-icon ${isSubjExpanded ? 'expanded' : ''}`} style={{ fontSize: '9px', transition: 'transform 0.2s', transform: isSubjExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                      </div>
                    </div>

                    {isSubjExpanded && (
                      <div className="subject-content" style={{ padding: '6px 10px' }}>
                        {sortedChapters.map(chapterName => {
                          const topics = chapters.get(chapterName)!;
                          const chapterMastery = getChapterMastery(topics);
                          const chapterKey = `${subjName}||${chapterName}`;
                          const isChExpanded = expandedChapters.has(chapterKey);
                          const chProgressColor = getProgressColor(chapterMastery);

                          const sortedTopics = getSortedTopics(topics);

                          return (
                            <div key={chapterName} className="chapter-group" style={{ marginBottom: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--bg-soft)', overflow: 'hidden' }}>
                              <div 
                                className="chapter-header" 
                                onClick={() => toggleChapter(subjName, chapterName)}
                                style={{ padding: '6px 10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', cursor: 'pointer', borderBottom: isChExpanded ? '1px solid var(--border-light)' : 'none' }}
                              >
                                <div className="chapter-title" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                                  <span className="expand-icon" style={{ fontSize: '8px', transform: isChExpanded ? 'rotate(90deg)' : 'none', transition: 'transform 0.15s' }}>▶</span>
                                  <span className="chapter-name" style={{ fontWeight: 600, fontSize: '12.5px' }}>📘 {chapterName}</span>
                                  <span className="chapter-stats" style={{ fontSize: '9.5px', color: 'var(--text-muted)' }}>({topics.length} topics)</span>
                                </div>
                                <div className="chapter-progress" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                  <div className="chapter-progress-bar" style={{ width: '50px', height: '4px', background: 'var(--border-light)', borderRadius: '2px', overflow: 'hidden' }}>
                                    <div className="chapter-progress-fill" style={{ width: `${chapterMastery}%`, height: '100%', background: chProgressColor }}></div>
                                  </div>
                                  <span className="chapter-percent" style={{ fontSize: '10.5px', fontWeight: 600 }}>{Math.round(chapterMastery)}%</span>
                                </div>
                              </div>

                              {isChExpanded && (
                                <div className="topics-list" style={{ padding: '6px 4px 10px' }}>
                                  {/* Compact Sort Toolbar */}
                                  <div style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    justifyContent: 'space-between',
                                    padding: '4px 6px 8px',
                                    fontSize: '11px',
                                    color: 'var(--text-muted)',
                                    borderBottom: '1px solid var(--border-light)',
                                    marginBottom: '10px',
                                    flexWrap: 'wrap',
                                    gap: '6px'
                                  }}>
                                    <span style={{ fontWeight: 600 }}>{sortedTopics.length} Topic{sortedTopics.length !== 1 ? 's' : ''}</span>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                                      <span style={{ fontSize: '10.5px' }}>Sort:</span>
                                      <button
                                        type="button"
                                        onClick={() => handleSort('mastery')}
                                        style={{
                                          background: sortField === 'mastery' ? 'rgba(59, 130, 246, 0.12)' : 'transparent',
                                          color: sortField === 'mastery' ? 'var(--accent)' : 'var(--text-muted)',
                                          border: sortField === 'mastery' ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                                          padding: '2px 8px',
                                          borderRadius: '12px',
                                          fontSize: '10.5px',
                                          fontWeight: sortField === 'mastery' ? 700 : 500,
                                          cursor: 'pointer'
                                        }}
                                      >
                                        Mastery {sortField === 'mastery' ? (sortDir === 'asc' ? '▲' : '▼') : ''}
                                      </button>
                                      <button
                                        type="button"
                                        onClick={() => handleSort('topicName')}
                                        style={{
                                          background: sortField === 'topicName' ? 'rgba(59, 130, 246, 0.12)' : 'transparent',
                                          color: sortField === 'topicName' ? 'var(--accent)' : 'var(--text-muted)',
                                          border: sortField === 'topicName' ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                                          padding: '2px 8px',
                                          borderRadius: '12px',
                                          fontSize: '10.5px',
                                          fontWeight: sortField === 'topicName' ? 700 : 500,
                                          cursor: 'pointer'
                                        }}
                                      >
                                        Name {sortField === 'topicName' ? (sortDir === 'asc' ? '▲' : '▼') : ''}
                                      </button>
                                      <button
                                        type="button"
                                        onClick={() => handleSort('attempts')}
                                        style={{
                                          background: sortField === 'attempts' ? 'rgba(59, 130, 246, 0.12)' : 'transparent',
                                          color: sortField === 'attempts' ? 'var(--accent)' : 'var(--text-muted)',
                                          border: sortField === 'attempts' ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                                          padding: '2px 8px',
                                          borderRadius: '12px',
                                          fontSize: '10.5px',
                                          fontWeight: sortField === 'attempts' ? 700 : 500,
                                          cursor: 'pointer'
                                        }}
                                      >
                                        Practiced {sortField === 'attempts' ? (sortDir === 'asc' ? '▲' : '▼') : ''}
                                      </button>
                                    </div>
                                  </div>

                                  {/* List of Unified Topic Cells (One cell per topic) */}
                                  <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                                    {sortedTopics.map(topic => {
                                      const mastery = Math.round(topic.mastery);
                                      const confidence = Math.round(topic.confidence);
                                      const attempts = Number(topic.attempts || topic.confidence || topic.questionsAttempted || 0);
                                      const isAbsent = !!topic.isAbsentExam;
                                      const state = topic.state;
                                      const practiceCount = topic.practiceCount || 0;
                                      const maxPractices = 2; // Unified SSOT: exactly 2 practice sets assigned
                                      const reqMasteryQs = 12; // 2 sets * 6 questions = 12 Qs to Master
                                      const isLimitReached = practiceCount >= maxPractices;
                                      const isMasteredState = state === 'mastered';
                                      const targetUrl = `/student/topic?topicCode=${encodeURIComponent(topic.topicCode)}&category=${topic.state}`;

                                      // Status styling
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
                                        if (isLimitReached) {
                                          expIcon = '🔒';
                                          expColor = 'var(--text-muted)';
                                          expText = `${practiceCount}/${maxPractices} practices done (${mastery}% accuracy). Quota reached. Consult teacher for further guidance.`;
                                        } else if (isAbsent) {
                                          expIcon = '⚠️';
                                          expColor = 'var(--danger)';
                                          expText = 'Missed scheduled exam. Complete practice questions to recover concept understanding.';
                                        } else if (attempts === 0) {
                                          expIcon = '⚪';
                                          expColor = 'var(--text-muted)';
                                          expText = `Never practiced yet (0/${maxPractices} sets). Start 1st practice to assess concept baseline.`;
                                        } else {
                                          expIcon = '🚨';
                                          expColor = 'var(--danger)';
                                          expText = `${practiceCount}/${maxPractices} practices done (${mastery}% accuracy). ${Math.max(0, maxPractices - practiceCount)} practice set(s) left — focus on weak areas.`;
                                        }
                                      } else if (state === 'practicing' || state === 'continuePractice' || state === 'revision') {
                                        if (mastery >= MASTERY_THRESHOLDS.MASTERED_MIN && attempts < reqMasteryQs) {
                                          const needed = Math.max(1, reqMasteryQs - attempts);
                                          expIcon = '📖';
                                          expColor = 'var(--accent)';
                                          expText = `High accuracy (${mastery}%), but needs ${needed} more verified question(s) to reach full confidence for Mastered.`;
                                        } else if (isLimitReached) {
                                          expIcon = '🔒';
                                          expColor = 'var(--text-muted)';
                                          expText = `${practiceCount}/${maxPractices} practices done (${mastery}% accuracy). Practice quota completed.`;
                                        } else {
                                          expIcon = '📈';
                                          expColor = 'var(--warning)';
                                          expText = `${practiceCount}/${maxPractices} practices done (${mastery}% accuracy). Complete Practice Set ${practiceCount + 1} (6 Qs) to aim for 90%+ Mastered.`;
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

                                      let btnLabel = isLimitReached && !isMasteredState
                                        ? `🔒 Quota Used (${practiceCount}/${maxPractices})`
                                        : (practiceCount === 0 ? 'Start 1st Practice →' : `Practice Set ${practiceCount + 1} →`);

                                      return (
                                        <div
                                          key={topic.topicCode}
                                          onClick={() => {
                                            if (!isMasteredState && !isLimitReached) router.push(targetUrl);
                                          }}
                                          style={{
                                            background: 'var(--surface)',
                                            borderRadius: '8px',
                                            border: '1px solid var(--border-light)',
                                            padding: '12px 14px',
                                            display: 'flex',
                                            flexDirection: 'column',
                                            gap: '8px',
                                            cursor: isMasteredState || isLimitReached ? 'default' : 'pointer'
                                          }}
                                          className={isMasteredState || isLimitReached ? '' : 'topic-card-hover'}
                                        >
                                          {/* Row 1: Topic Name & Status Badge */}
                                          <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: '8px' }}>
                                            <div style={{ fontWeight: 600, fontSize: '13.5px', color: 'var(--text)', lineHeight: 1.35, flex: 1 }}>
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

                                          {/* Row 3: Metrics (Practiced, Confidence, Last Activity) */}
                                          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap', fontSize: '11.5px', color: 'var(--text-muted)' }}>
                                            <span style={{ fontWeight: 600, color: practiceCount === 0 ? '#ef4444' : 'var(--text)' }}>
                                              🎯 {practiceCount === 0 ? `0/${maxPractices} Sets (Never Practiced)` : `${practiceCount}/${maxPractices} Practices Done`}
                                            </span>
                                            <span>•</span>
                                            <span>📊 {confidence}% Confidence ({attempts}/{reqMasteryQs} Qs)</span>
                                            <span>•</span>
                                            <span>🕒 {formatDateOrFallback(topic.lastAttempt, 'Never')}</span>
                                          </div>

                                          {/* Row 4: Diagnostic Guidance Note */}
                                          <div style={{ fontSize: '11.5px', color: expColor, lineHeight: 1.4 }}>
                                            <span>{expIcon}</span> {expText}
                                          </div>

                                          {/* Row 5: Action Button / Completed Badge */}
                                          <div style={{ display: 'flex', justifyContent: 'flex-end', alignItems: 'center', paddingTop: '6px', borderTop: '1px dashed var(--border-light)' }}>
                                            {isMasteredState ? (
                                              <span style={{
                                                fontSize: '11.5px',
                                                fontWeight: 700,
                                                color: 'var(--success)',
                                                display: 'inline-flex',
                                                alignItems: 'center',
                                                gap: '4px',
                                                padding: '4px 8px'
                                              }}>
                                                ✓ Concept Certified Mastered
                                              </span>
                                            ) : isLimitReached ? (
                                              <span style={{
                                                padding: '4px 10px',
                                                borderRadius: '20px',
                                                fontSize: '10.5px',
                                                fontWeight: 600,
                                                background: 'rgba(148, 163, 184, 0.12)',
                                                color: 'var(--text-muted)',
                                                border: '1px solid var(--border-light)'
                                              }}>
                                                🔒 Locked ({practiceCount}/2)
                                              </span>
                                            ) : (
                                              <button
                                                type="button"
                                                onClick={(e) => {
                                                  e.stopPropagation();
                                                  router.push(targetUrl);
                                                }}
                                                className="btn btn-sm btn-primary"
                                                style={{
                                                  padding: '5px 14px',
                                                  borderRadius: '20px',
                                                  fontSize: '11.5px',
                                                  fontWeight: 600,
                                                  background: practiceCount === 0 ? 'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)' : 'var(--accent-grad)',
                                                  color: '#fff',
                                                  cursor: 'pointer',
                                                  border: 'none',
                                                  display: 'inline-flex',
                                                  alignItems: 'center',
                                                  gap: '4px'
                                                }}
                                              >
                                                <span>{btnLabel}</span>
                                              </button>
                                            )}
                                          </div>
                                        </div>
                                      );
                                    })}
                                  </div>
                                </div>
                              )}
                            </div>
                          );
                        })}
                      </div>
                    )}
                  </div>
                );
              })
            )}
          </div>
          </>
        )}
      </div>
    </div>
  );
}