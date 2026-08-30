'use client';

import React, { useEffect, useState, useMemo, useDeferredValue } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import useSWR from 'swr';
import { fetchWithToken } from '@/lib/swrFetcher';
import { useToggleSet } from '@/hooks/useToggleSet';
import { useRouter } from 'next/navigation';
import dynamic from 'next/dynamic';
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });
import { formatDateIST } from '@/lib/dateUtils';
import { getCanonicalSubjectName } from '@/lib/questionTypes';

interface TopicItem {
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
  isRecoveryMastered?: boolean;
}

interface LearningPathData {
  studentCode: string;
  needsAttention: TopicItem[];
  continuePractice: TopicItem[];
  revision: TopicItem[];
  mastered: TopicItem[];
}

export default function StudentLearning({ initialData }: { initialData?: LearningPathData }) {
  const { firebaseUser, user } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const [localCache, setLocalCache] = useState<LearningPathData | null>(null);

  useEffect(() => {
    try {
      const cached = localStorage.getItem('yc_student_learning_cache');
      if (cached) {
        setLocalCache(JSON.parse(cached));
      }
    } catch (e) {
      console.warn('Failed to load learning cache:', e);
    }
  }, []);

  const fetcher = async (url: string) => {
    try {
      const data = await fetchWithToken(url, firebaseUser);
      if (data) {
        localStorage.setItem('yc_student_learning_cache', JSON.stringify(data));
      }
      return data;
    } catch (err: any) {
      throw new Error('⛔ Permission Denied: Learning OS access is restricted for Autonomous Student accounts.');
    }
  };

  const { data, error: swrError, isLoading } = useSWR<LearningPathData>(
    firebaseUser ? '/api/student/learning' : null,
    fetcher,
    {
      fallbackData: initialData || localCache || undefined,
      revalidateOnFocus: false,
      dedupingInterval: 5000
    }
  );

  const error = swrError?.message || '';
  const loading = isLoading && !data;

  // Auto-expand first subject by default on data load
  const [expandedSubjects, toggleSubject, isSubjectExpanded, setExpandedSubjects] = useToggleSet();
  const [expandedChapters, toggleChapterSet, isChapterExpanded, setExpandedChapters] = useToggleSet();

  useEffect(() => {
    if (data && expandedSubjects.size === 0) {
      const firstSub = [
        ...data.needsAttention,
        ...data.continuePractice,
        ...data.revision,
        ...data.mastered
      ].map(t => t.subjectName).filter(Boolean)[0];
      if (firstSub) {
        setExpandedSubjects(new Set([firstSub]));
      }
    }
  }, [data]);

  const [activeTab, setActiveTab] = useState<'needsAttention' | 'continuePractice' | 'revision' | 'mastered'>('needsAttention');
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

  const getSortedTopics = (list: TopicItem[]) => {
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
    if (state === 'mastered') return 'Review';
    if (state === 'revision') return 'Revise';
    if (state === 'continuePractice' || state === 'needsAttention') return 'Practice';
    return 'Learn';
  };

  const getMasteryClass = (mastery: number) => {
    if (mastery < 40) return 'low';
    if (mastery < 70) return 'medium';
    return 'high';
  };

  const getProgressColor = (mastery: number) => {
    if (mastery < 40) return '#f44336';
    if (mastery < 70) return '#ff9800';
    return '#4caf50';
  };

  const toggleChapter = (subjectName: string, chapterName: string) => {
    toggleChapterSet(`${subjectName}||${chapterName}`);
  };

  const formatDate = (dateStr: string | null) => {
    if (!dateStr) return 'Never';
    return formatDateIST(dateStr) || 'Never';
  };

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
        ...cachedData.revision,
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

  const deferredSearchTerm = useDeferredValue(searchTerm);

  // Filter topics based on active tab and search query
  const { grouped, sortedSubjects, topicsList } = useMemo(() => {
    let list: TopicItem[] = [];
    if (data) {
      if (activeTab === 'needsAttention') {
        list = data.needsAttention || [];
      } else if (activeTab === 'continuePractice') {
        list = data.continuePractice || [];
      } else if (activeTab === 'revision') {
        list = data.revision || [];
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
    const grp = new Map<string, Map<string, TopicItem[]>>();
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
  }, [data, activeTab, deferredSearchTerm]);

  return (
    <div className="page-wrapper">
      
      <style>{`
        .topic-row-hover {
          transition: background-color 0.15s ease;
        }
        .topic-row-hover:hover {
          background-color: var(--bg-soft) !important;
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
            {renderTabsSkeleton()}
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

            {/* Tab Controls (Focus is fully restored) */}
            <div className="review-tabs" style={{ display: 'flex', gap: '6px', marginBottom: '10px', overflowX: 'auto', paddingBottom: '2px' }}>
              <button className={`tab-btn ${activeTab === 'needsAttention' ? 'active' : ''}`} onClick={() => setActiveTab('needsAttention')}>
                🚨 Focus <span className="tab-count">{data ? data.needsAttention.length : 0}</span>
              </button>
              <button className={`tab-btn ${activeTab === 'continuePractice' ? 'active' : ''}`} onClick={() => setActiveTab('continuePractice')}>
                🔄 Practice <span className="tab-count">{data ? data.continuePractice.length : 0}</span>
              </button>
              <button className={`tab-btn ${activeTab === 'revision' ? 'active' : ''}`} onClick={() => setActiveTab('revision')}>
                📚 Revise <span className="tab-count">{data ? data.revision.length : 0}</span>
              </button>
              <button className={`tab-btn ${activeTab === 'mastered' ? 'active' : ''}`} onClick={() => setActiveTab('mastered')}>
                🏆 Mastered <span className="tab-count">{data ? data.mastered.length : 0}</span>
              </button>
            </div>
          </>
        )}

        {/* Syllabus Accordion Lists */}
        {!loading && (
          <div id="student-learning-pathway">
            {sortedSubjects.length === 0 ? (
              <div className="empty-state" style={{ textAlign: 'center', padding: '24px 0', color: 'var(--text-faint)' }}>📭 No topics found in this category.</div>
            ) : (
              sortedSubjects.map(subjName => {
                const chapters = grouped.get(subjName)!;
                const allSubjTopics = Array.from(chapters.values()).flat();
                const subjectMastery = allSubjTopics.reduce((acc, t) => acc + t.mastery, 0) / allSubjTopics.length;
                const isSubjExpanded = expandedSubjects.has(subjName);
                const subjProgressColor = getProgressColor(subjectMastery);

                // Helper to compute chapter average mastery
                const getChapterMastery = (topics: TopicItem[]) => {
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
                                <div className="topics-list" style={{ padding: '4px 6px' }}>
                                  <div style={{ overflowX: 'auto', WebkitOverflowScrolling: 'touch' }}>
                                    <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px', minWidth: '550px' }}>
                                      <thead>
                                        <tr style={{ borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '10px', textTransform: 'uppercase', height: '30px' }}>
                                          <th onClick={() => handleSort('topicName')} style={{ padding: '6px 8px', textAlign: 'left', cursor: 'pointer', userSelect: 'none' }}>
                                            Topic Name {sortField === 'topicName' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                                          </th>
                                          <th onClick={() => handleSort('mastery')} style={{ padding: '6px 8px', textAlign: 'center', width: '70px', cursor: 'pointer', userSelect: 'none' }}>
                                            Mastery {sortField === 'mastery' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                                          </th>
                                          <th style={{ padding: '6px 8px', textAlign: 'center', width: '80px' }}>Confidence</th>
                                          <th onClick={() => handleSort('attempts')} style={{ padding: '6px 8px', textAlign: 'center', width: '110px', cursor: 'pointer', userSelect: 'none' }}>
                                            Practiced {sortField === 'attempts' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                                          </th>
                                          <th onClick={() => handleSort('lastAttempt')} style={{ padding: '6px 8px', textAlign: 'center', width: '100px', cursor: 'pointer', userSelect: 'none' }}>
                                            Last Practice {sortField === 'lastAttempt' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                                          </th>
                                          <th style={{ padding: '6px 8px', textAlign: 'right', width: '90px' }}>Action</th>
                                        </tr>
                                      </thead>
                                      <tbody>
                                        {sortedTopics.map(topic => {
                                          const mastery = Math.round(topic.mastery);
                                          const confidence = Math.round(topic.confidence);
                                          const masteryClass = getMasteryClass(mastery);
                                          const actionText = getActionText(topic.state);
                                          const attempts = topic.attempts || 0;
                                          const isAbsent = !!topic.isAbsentExam;
                                          const isRecovery = !!topic.isRecoveryMastered;
                                          const state = topic.state;

                                          let expIcon = '⚪';
                                          let expColor = 'var(--text-muted)';
                                          let expText = '';
                                          const practiceCount = topic.practiceCount || 0;
                                          const isLimitReached = practiceCount >= 5;

                                          if (state === 'needsAttention') {
                                            if (isLimitReached) {
                                              expIcon = '⚡';
                                              expColor = 'var(--accent)';
                                              expText = `5/5 practices done (${mastery}% accuracy). Take the Recovery Quiz (Fresh + Missed Qs) to achieve Mastered!`;
                                            } else if (isAbsent) {
                                              expIcon = '⚠️';
                                              expColor = '#ef4444';
                                              expText = 'Missed scheduled exam. Practice questions to recover concept understanding.';
                                            } else if (attempts === 0) {
                                              expIcon = '⚪';
                                              expColor = 'var(--text-muted)';
                                              expText = 'Not attempted yet. Start 1st practice to assess concept baseline.';
                                            } else {
                                              expIcon = '🚨';
                                              expColor = '#ef4444';
                                              expText = `${practiceCount}/5 practices done (${mastery}% accuracy). ${5 - practiceCount} practice(s) left — focus on weak areas.`;
                                            }
                                          } else if (state === 'continuePractice') {
                                            if (isLimitReached) {
                                              expIcon = '⚡';
                                              expColor = 'var(--accent)';
                                              expText = `5/5 practices done (${mastery}% accuracy). Take the Recovery Quiz (Fresh + Missed Qs) to achieve Mastered!`;
                                            } else {
                                              expIcon = '📈';
                                              expColor = '#f59e0b';
                                              expText = `${practiceCount}/5 practices done (${mastery}% accuracy). ${5 - practiceCount} practice(s) left to aim for 90%+ Mastered.`;
                                            }
                                          } else if (state === 'revision') {
                                            const needed = Math.max(1, 20 - attempts);
                                            expIcon = '📖';
                                            expColor = 'var(--accent)';
                                            expText = `High accuracy (${mastery}%), but needs ${needed} more attempts to reach 20-question Confidence threshold for Mastered.`;
                                          } else {
                                            if (isRecovery) {
                                              expIcon = '⚡';
                                              expColor = 'var(--accent)';
                                              expText = `Mastered via Recovery Diagnostic (Passed fresh unseen + remediated question assessment).`;
                                            } else {
                                              expIcon = '⭐';
                                              expColor = '#10b981';
                                              expText = `Mastered on 1st attempt (${mastery}% accuracy across ${attempts} verified questions).`;
                                            }
                                          }

                                          const isRecoveryAction = isLimitReached && state !== 'mastered';
                                          const targetUrl = isRecoveryAction
                                            ? `/student/topic?topicCode=${topic.topicCode}&category=${topic.state}&mode=recovery`
                                            : `/student/topic?topicCode=${topic.topicCode}&category=${topic.state}`;

                                          return (
                                            <tr 
                                              key={topic.topicCode}
                                              onClick={() => router.push(targetUrl)}
                                              style={{ borderBottom: '1px solid var(--border-light)', cursor: 'pointer', height: '48px' }}
                                              className="topic-row-hover"
                                            >
                                              <td style={{ padding: '8px', fontWeight: 600, color: 'var(--text)' }}>
                                                <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
                                                  <span>📍 {topic.topicName || topic.topicCode}</span>
                                                  {isAbsent && (
                                                    <span style={{ fontSize: '9px', fontWeight: 700, padding: '1px 5px', borderRadius: '4px', background: 'rgba(239, 68, 68, 0.15)', color: '#ef4444', border: '1px solid rgba(239, 68, 68, 0.3)' }}>
                                                      Missed Exam
                                                    </span>
                                                  )}
                                                  {state === 'mastered' && (
                                                    isRecovery ? (
                                                      <span style={{ fontSize: '9px', fontWeight: 700, padding: '1px 6px', borderRadius: '10px', background: 'var(--accent-soft)', color: 'var(--accent)', border: '1px solid var(--accent-ring)' }}>
                                                        ⚡ Recovery Mastered
                                                      </span>
                                                    ) : (
                                                      <span style={{ fontSize: '9px', fontWeight: 700, padding: '1px 6px', borderRadius: '10px', background: 'linear-gradient(135deg, rgba(16,185,129,0.15), rgba(5,150,105,0.15))', color: '#10b981', border: '1px solid rgba(16,185,129,0.3)' }}>
                                                        🌟 Certified Mastered
                                                      </span>
                                                    )
                                                  )}
                                                </div>
                                                <div style={{ fontSize: '10.5px', fontWeight: 400, color: expColor, marginTop: '2px', display: 'flex', alignItems: 'center', gap: '4px' }}>
                                                  <span>{expIcon}</span>
                                                  <span>{expText}</span>
                                                </div>
                                              </td>
                                              <td style={{ padding: '6px 8px', textAlign: 'center' }}>
                                                <span className={`badge badge-${masteryClass}`} style={{ fontSize: '10px', fontWeight: 'bold', padding: '2px 6px', borderRadius: '4px' }}>
                                                  {mastery}%
                                                </span>
                                              </td>
                                              <td style={{ padding: '6px 8px', textAlign: 'center', color: 'var(--text-muted)' }}>
                                                {confidence}%
                                              </td>
                                              <td style={{ padding: '6px 8px', textAlign: 'center', color: 'var(--text)' }}>
                                                 {topic.practiceCount}/5 practices
                                                 <div style={{ fontSize: '10px', color: 'var(--text-muted)' }}>({topic.attempts} / {topic.totalQuestions || topic.targetQuestions || 30} Qs max)</div>
                                               </td>
                                              <td style={{ padding: '6px 8px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '11px' }}>
                                                {formatDate(topic.lastAttempt)}
                                              </td>
                                              <td style={{ padding: '6px 8px', textAlign: 'right' }} onClick={(e) => e.stopPropagation()}>
                                                <button 
                                                  onClick={() => router.push(targetUrl)}
                                                  style={{ 
                                                    padding: '4px 12px', 
                                                    borderRadius: '30px', 
                                                    fontSize: '10px', 
                                                    fontWeight: 600, 
                                                    border: 'none', 
                                                    background: isRecoveryAction ? 'var(--accent-grad)' : 'var(--accent-grad)', 
                                                    color: 'white', 
                                                    cursor: 'pointer' 
                                                  }}
                                                >
                                                  {isRecoveryAction ? '⚡ Recovery Quiz' : actionText}
                                                </button>
                                              </td>
                                            </tr>
                                          );
                                        })}
                                      </tbody>
                                    </table>
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
        )}
      </div>
    </div>
  );
}
