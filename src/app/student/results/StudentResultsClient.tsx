'use client';

import React, { useEffect, useState, Suspense } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import useSWR from 'swr';
import { fetchWithToken } from '@/lib/swrFetcher';
import { t } from '@/lib/i18n';
import { useRouter } from 'next/navigation';
import dynamic from 'next/dynamic';
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });
const ScorecardModal = dynamic(() => import('@/components/ScorecardModal'), { ssr: false });
import { useMathRender } from '@/hooks/useMathRender';
import { useScorecard } from '@/hooks/useScorecard';
import { useToggleSet } from '@/hooks/useToggleSet';
import { stripOptionLabel, preprocessMathText, parseAnswerList, isOptionSelectedByUser, isBlank, getReasonForQuestion, getRawOptionKey, getRawOptionText, formatUserAnswerSummary } from '@/lib/questionTypes';
import { formatDateTimeIST } from '@/lib/dateUtils';

interface ResultSummaryItem {
  id: string;
  examCode: string;
  examName: string;
  examType: string;
  score: number;
  totalQuestions: number;
  totalMarks: number;
  percentage: number;
  durationSpent: number;
  submittedAt: string | null;
  status: string;
  suspiciousLevel: string;
  subject?: string;
  chapter?: string;
  topicName?: string;
  practiceNumber?: number | null;
}

interface QuestionDetailsItem {
  id: string;
  questionCode: string;
  qNumber?: number | null;
  text: string;
  type: string;
  options: any[];
  assertion?: string;
  reason?: string;
  solution?: string;
  difficulty: string;
  bloomLevel: string;
  userAnswer: string;
  isCorrect: boolean;
  correctAnswer: string;
  correctAnswers: string[];
}

interface DetailedScorecard {
  id: string;
  examCode: string;
  examName: string;
  examType: string;
  score: number;
  totalMarks: number;
  percentage: number;
  durationSpent: number;
  submittedAt: string | null;
  tabViolations: number;
  proctoringViolations: {
    noFace?: number;
    multipleFaces?: number;
    lookingAway?: number;
  };
  integrityScore: number;
  status: string;
  wrongAnswerReasons?: string[];
  questions: QuestionDetailsItem[];
  subject?: string;
  chapter?: string;
  topicName?: string;
}

export default function StudentResults({ initialData }: { initialData?: { results: ResultSummaryItem[] } }) {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  // Cache loading
  const [localCache, setLocalCache] = useState<{ results: ResultSummaryItem[] } | null>(null);

  useEffect(() => {
    try {
      const cached = localStorage.getItem('yc_student_results_cache');
      if (cached) {
        setLocalCache(JSON.parse(cached));
      }
    } catch (e) {
      console.warn('Failed to load results cache:', e);
    }
  }, []);

  const fetcher = async (url: string) => {
    const data = await fetchWithToken(url, firebaseUser);
    if (data) {
      try {
        localStorage.setItem('yc_student_results_cache', JSON.stringify(data));
      } catch (e) {
        console.warn('Failed to save results cache:', e);
      }
    }
    return data;
  };

  const { data, error: swrError, isLoading } = useSWR<{ results: ResultSummaryItem[] }>(
    firebaseUser ? '/api/student/results' : null,
    fetcher,
    {
      fallbackData: initialData || localCache || undefined,
      revalidateOnFocus: false,
      dedupingInterval: 5000
    }
  );

  const resultsList = data?.results || [];
  const error = swrError?.message || '';
  const loading = isLoading && !resultsList.length;

  const [activeTab, setActiveTab] = useState<'exams' | 'practice'>('exams');
  const [expandedSubjects, toggleSubject, isSubjectExpanded, setExpandedSubjects] = useToggleSet();
  const [expandedChapters, toggleChapterSet, isChapterExpanded, setExpandedChapters] = useToggleSet();

  const renderWidgetsSkeleton = () => (
    <div className="mobile-responsive-grid skeleton-blink">
      {[1, 2, 3, 4].map(i => (
        <div key={i} className="card mobile-responsive-card" style={{ background: 'var(--surface)', padding: '12px 8px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', minHeight: '64px' }}>
          <div style={{ width: '40px', height: '20px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
          <div style={{ width: '70px', height: '10px', background: 'var(--bg-soft)', borderRadius: '2px', marginTop: '6px' }}></div>
        </div>
      ))}
    </div>
  );

  const renderTabsSkeleton = () => (
    <div className="review-tabs skeleton-blink" style={{ display: 'flex', gap: '8px', marginBottom: '16px', alignItems: 'center', height: '36px' }}>
      <div style={{ flex: 1, height: '100%', background: 'var(--bg-soft)', borderRadius: '8px' }}></div>
      <div style={{ flex: 1, height: '100%', background: 'var(--bg-soft)', borderRadius: '8px' }}></div>
    </div>
  );

  const renderAccordionSkeleton = () => {
    const cachedResults = initialData?.results || localCache?.results;
    let subjectCount = 3;
    if (cachedResults && Array.isArray(cachedResults)) {
      const subjects = new Set(cachedResults.map(r => r.subject || 'General'));
      subjectCount = subjects.size;
    }
    const count = Math.max(1, subjectCount);

    return (
      <div className="skeleton-blink" style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {Array.from({ length: count }).map((_, i) => (
          <div key={i} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', background: 'var(--surface)', overflow: 'hidden' }}>
            <div style={{ padding: '16px 20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <div style={{ width: '18px', height: '18px', background: 'var(--border-light)', borderRadius: '50%' }}></div>
                <div style={{ width: '120px', height: '16px', background: 'var(--border-light)', borderRadius: '4px' }}></div>
                <div style={{ width: '60px', height: '12px', background: 'var(--border-light)', borderRadius: '4px' }}></div>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                <div style={{ width: '80px', height: '6px', background: 'var(--border-light)', borderRadius: '3px' }}></div>
                <div style={{ width: '30px', height: '14px', background: 'var(--border-light)', borderRadius: '4px' }}></div>
                <div style={{ width: '12px', height: '12px', background: 'var(--border-light)', borderRadius: '2px' }}></div>
              </div>
            </div>
          </div>
        ))}
      </div>
    );
  };

  // Scorecard modal state
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const { scorecard, loading: modalLoading, loadScorecard: fetchScorecard, setScorecard } = useScorecard();

  // Sorting and PDF export states
  const [sortField, setSortField] = useState<'submittedAt' | 'durationSpent' | 'percentage'>('submittedAt');
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('desc');
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);
  useMathRender([activeTab, resultsList, selectedId, scorecard]);

  // Lock body scroll when modal is open
  useEffect(() => {
    if (selectedId) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
    };
  }, [selectedId]);

  const handleSort = (field: 'submittedAt' | 'durationSpent' | 'percentage') => {
    if (sortField === field) {
      setSortDir(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortField(field);
      setSortDir('desc');
    }
  };

  const getSortedAttempts = (list: ResultSummaryItem[]) => {
    return [...list].sort((a, b) => {
      let comparison = 0;
      if (sortField === 'submittedAt') {
        const da = a.submittedAt ? new Date(a.submittedAt).getTime() : 0;
        const db = b.submittedAt ? new Date(b.submittedAt).getTime() : 0;
        comparison = da - db;
      } else if (sortField === 'durationSpent') {
        comparison = (a.durationSpent || 0) - (b.durationSpent || 0);
      } else {
        comparison = (a.percentage || 0) - (b.percentage || 0);
      }
      return sortDir === 'asc' ? comparison : -comparison;
    });
  };

  const loadScorecard = async (id: string) => {
    setSelectedId(id);
    try {
      await fetchScorecard(id);
    } catch (err) {
      setSelectedId(null);
    }
  };

  const formatDate = (dateStr: string | null) => {
    if (!dateStr) return '-';
    return formatDateTimeIST(dateStr) || '-';
  };

  const formatDuration = (seconds: number) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m}m ${s}s`;
  };

  const getScoreClass = (pct: number) => {
    if (pct < 40) return 'score-low';
    if (pct < 75) return 'score-medium';
    return 'score-high';
  };

  const getSuspiciousClass = (level: string) => {
    if (level === 'red') return 'badge-danger';
    if (level === 'yellow') return 'badge-warning';
    return 'badge-success';
  };



  if (error) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div className="alert-box alert-box-danger" style={{ display: 'block', maxWidth: '400px', textAlign: 'center' }}>
          {error}
        </div>
        <button className="btn btn-primary" onClick={() => window.location.reload()} style={{ marginTop: '16px' }}>Retry</button>
      </div>
    );
  }

  // Filter list by tab
  const examsList = resultsList.filter(r => r.examType !== 'practice');
  const practiceList = resultsList.filter(r => r.examType === 'practice');

  const avgExamScore = examsList.length
    ? Math.round(examsList.reduce((acc, r) => acc + r.percentage, 0) / examsList.length)
    : 0;

  const avgPracticeScore = practiceList.length
    ? Math.round(practiceList.reduce((acc, r) => acc + r.percentage, 0) / practiceList.length)
    : 0;

  // Helper to group items by subject and chapter
  const getGroupedItems = (items: ResultSummaryItem[]) => {
    const grouped = new Map<string, Map<string, ResultSummaryItem[]>>();
    items.forEach(item => {
      const sName = item.subject || 'General';
      const cName = item.chapter || 'General Chapter';
      if (!grouped.has(sName)) {
        grouped.set(sName, new Map<string, ResultSummaryItem[]>());
      }
      const chapters = grouped.get(sName)!;
      if (!chapters.has(cName)) {
        chapters.set(cName, []);
      }
      chapters.get(cName)!.push(item);
    });
    return grouped;
  };

  const getProgressColor = (pct: number) => {
    if (pct < 40) return '#f44336';
    if (pct < 70) return '#ff9800';
    return '#4caf50';
  };

  const toggleChapter = (subjectName: string, chapterName: string) => {
    toggleChapterSet(`${subjectName}||${chapterName}`);
  };

  const activeGrouped = getGroupedItems(activeTab === 'exams' ? examsList : practiceList);
  const sortedSubjects = Array.from(activeGrouped.keys()).sort();

  return (
    <div className="page-wrapper" style={{ display: 'flex', flexDirection: 'column' }}>

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
        .mobile-responsive-grid {
          display: grid;
          grid-template-columns: repeat(4, 1fr) !important;
          gap: 8px;
          margin-bottom: 24px;
        }
        @media (max-width: 640px) {
          .mobile-responsive-grid {
            grid-template-columns: repeat(2, 1fr) !important;
            gap: 10px;
          }
        }
      `}</style>

      <div className="dashboard-container" style={{ maxWidth: '1000px', width: '100%', margin: '0 auto', padding: '24px 12px' }}>
        {loading ? (
          <>
            {renderWidgetsSkeleton()}
            {renderTabsSkeleton()}
            {renderAccordionSkeleton()}
          </>
        ) : (
          <>
            {/* Statistics Widgets */}
            <div className="mobile-responsive-grid">
              <div className="card mobile-responsive-card" style={{ background: 'var(--surface)', padding: '12px 8px', borderRadius: 'var(--radius-lg)', textAlign: 'center', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', minHeight: '64px' }}>
                <div style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--accent)' }}>{examsList.length}</div>
                <div style={{ fontSize: '9px', color: 'var(--text-muted)', textTransform: 'uppercase', marginTop: '4px', lineHeight: '1.2' }}>Exams Submitted</div>
              </div>
              <div className="card mobile-responsive-card" style={{ background: 'var(--surface)', padding: '12px 8px', borderRadius: 'var(--radius-lg)', textAlign: 'center', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', minHeight: '64px' }}>
                <div style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--success)' }}>{avgExamScore}%</div>
                <div style={{ fontSize: '9px', color: 'var(--text-muted)', textTransform: 'uppercase', marginTop: '4px', lineHeight: '1.2' }}>Average Exam Score</div>
              </div>
              <div className="card mobile-responsive-card" style={{ background: 'var(--surface)', padding: '12px 8px', borderRadius: 'var(--radius-lg)', textAlign: 'center', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', minHeight: '64px' }}>
                <div style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--accent-light-bg)' }}>{practiceList.length}</div>
                <div style={{ fontSize: '9px', color: 'var(--text-muted)', textTransform: 'uppercase', marginTop: '4px', lineHeight: '1.2' }}>Practice Sets Done</div>
              </div>
              <div className="card mobile-responsive-card" style={{ background: 'var(--surface)', padding: '12px 8px', borderRadius: 'var(--radius-lg)', textAlign: 'center', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', minHeight: '64px' }}>
                <div style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--success)' }}>{avgPracticeScore}%</div>
                <div style={{ fontSize: '9px', color: 'var(--text-muted)', textTransform: 'uppercase', marginTop: '4px', lineHeight: '1.2' }}>Average Practice Score</div>
              </div>
            </div>

            {/* Tab Controls */}
            <div className="review-tabs" style={{ display: 'flex', gap: '8px', marginBottom: '16px', alignItems: 'center' }}>
              <button className={`tab-btn ${activeTab === 'exams' ? 'active' : ''}`} onClick={() => setActiveTab('exams')} style={{ flex: 1 }}>
                📝 Formal Exams
              </button>
              <button className={`tab-btn ${activeTab === 'practice' ? 'active' : ''}`} onClick={() => setActiveTab('practice')} style={{ flex: 1 }}>
                📚 Topic Practice
              </button>
            </div>

            {/* Accordion Lists */}
            <div id="results-accordion-section">
              {sortedSubjects.length === 0 ? (
                <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '40px 0', textAlign: 'center', color: 'var(--text-faint)' }}>
                  📭 No submissions found in this category.
                </div>
              ) : (
                sortedSubjects.map(subjName => {
              const chapters = activeGrouped.get(subjName)!;
              const allSubjItems = Array.from(chapters.values()).flat();
              const subjectAvgScore = allSubjItems.reduce((acc, t) => acc + t.percentage, 0) / allSubjItems.length;
              const isSubjExpanded = expandedSubjects.has(subjName);
              const subjProgressColor = getProgressColor(subjectAvgScore);

              const sortedChapters = Array.from(chapters.keys()).sort();

              return (
                <div key={subjName} className="subject-group" style={{ marginBottom: '16px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', background: 'var(--surface)', overflow: 'hidden' }}>
                  <div 
                    className="subject-header" 
                    onClick={() => toggleSubject(subjName)}
                    style={{ padding: '16px 20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)', cursor: 'pointer', borderBottom: isSubjExpanded ? '1px solid var(--border-light)' : 'none' }}
                  >
                    <div className="subject-title" style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                      <span className="subject-icon" style={{ fontSize: '1.2rem' }}>📖</span>
                      <span className="subject-name" style={{ fontWeight: 'bold', fontSize: '14px' }}>{subjName}</span>
                      <span className="subject-stats" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>({allSubjItems.length} attempts)</span>
                    </div>
                    <div className="subject-progress" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                      <div className="subject-progress-bar" style={{ width: '80px', height: '6px', background: 'var(--border-light)', borderRadius: '3px', overflow: 'hidden' }}>
                        <div className="subject-progress-fill" style={{ width: `${subjectAvgScore}%`, height: '100%', background: subjProgressColor }}></div>
                      </div>
                      <span className="subject-percent" style={{ fontSize: '12px', fontWeight: 600 }}>{Math.round(subjectAvgScore)}%</span>
                      <span className={`expand-icon ${isSubjExpanded ? 'expanded' : ''}`} style={{ fontSize: '10px', transition: 'transform 0.2s', transform: isSubjExpanded ? 'rotate(180deg)' : 'none' }}>▼</span>
                    </div>
                  </div>

                  {isSubjExpanded && (
                    <div className="subject-content" style={{ padding: '12px 20px' }}>
                      {sortedChapters.map(chapterName => {
                        const items = chapters.get(chapterName)!;
                        const chapterAvgScore = items.reduce((acc, t) => acc + t.percentage, 0) / items.length;
                        const chapterKey = `${subjName}||${chapterName}`;
                        const isChExpanded = expandedChapters.has(chapterKey);
                        const chProgressColor = getProgressColor(chapterAvgScore);

                        const sortedAttempts = getSortedAttempts(items);

                        return (
                          <div key={chapterName} className="chapter-group" style={{ marginBottom: '12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)', background: 'var(--bg-soft)', overflow: 'hidden' }}>
                            <div 
                              className="chapter-header" 
                              onClick={() => toggleChapter(subjName, chapterName)}
                              style={{ padding: '12px 16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', cursor: 'pointer', borderBottom: isChExpanded ? '1px solid var(--border-light)' : 'none' }}
                            >
                              <div className="chapter-title" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                <span className="expand-icon" style={{ fontSize: '9px', transform: isChExpanded ? 'rotate(90deg)' : 'none', transition: 'transform 0.15s' }}>▶</span>
                                <span className="chapter-name" style={{ fontWeight: 600, fontSize: '13px' }}>📘 {chapterName}</span>
                                <span className="chapter-stats" style={{ fontSize: '10px', color: 'var(--text-muted)' }}>({items.length} attempts)</span>
                              </div>
                              <div className="chapter-progress" style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                                <div className="chapter-progress-bar" style={{ width: '60px', height: '4px', background: 'var(--border-light)', borderRadius: '2px', overflow: 'hidden' }}>
                                  <div className="chapter-progress-fill" style={{ width: `${chapterAvgScore}%`, height: '100%', background: chProgressColor }}></div>
                                </div>
                                <span className="chapter-percent" style={{ fontSize: '11px', fontWeight: 600 }}>{Math.round(chapterAvgScore)}%</span>
                              </div>
                            </div>

                            {isChExpanded && (
                              <div className="topics-list" style={{ padding: '8px 12px' }}>
                                <div style={{ width: '100%', overflowX: 'auto', WebkitOverflowScrolling: 'touch', display: 'block' }}>
                                  <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px', minWidth: '600px' }}>
                                    <thead>
                                      <tr style={{ borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '10px', textTransform: 'uppercase', height: '30px' }}>
                                        <th style={{ padding: '6px 8px', textAlign: 'center', minWidth: '180px', whiteSpace: 'nowrap' }}>Topic(s)</th>
                                        <th onClick={() => handleSort('submittedAt')} style={{ padding: '6px 8px', textAlign: 'center', width: '130px', minWidth: '120px', whiteSpace: 'nowrap', cursor: 'pointer', userSelect: 'none' }}>
                                          Submitted At {sortField === 'submittedAt' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                                        </th>
                                        <th onClick={() => handleSort('durationSpent')} style={{ padding: '6px 8px', textAlign: 'center', width: '90px', minWidth: '90px', whiteSpace: 'nowrap', cursor: 'pointer', userSelect: 'none' }}>
                                          Time Spent {sortField === 'durationSpent' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                                        </th>
                                        <th style={{ padding: '6px 8px', textAlign: 'center', width: '100px', minWidth: '100px', whiteSpace: 'nowrap' }}>Integrity</th>
                                        <th onClick={() => handleSort('percentage')} style={{ padding: '6px 8px', textAlign: 'center', width: '90px', minWidth: '80px', whiteSpace: 'nowrap', cursor: 'pointer', userSelect: 'none' }}>
                                          Score {sortField === 'percentage' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                                        </th>
                                      </tr>
                                    </thead>
                                    <tbody>
                                      {sortedAttempts.map(item => (
                                        <tr 
                                          key={item.id} 
                                          className="topic-row-hover"
                                          onClick={() => loadScorecard(item.id)}
                                          style={{ borderBottom: '1px solid var(--border-light)', height: '38px', cursor: 'pointer' }}
                                        >
                                          <td style={{ padding: '6px 8px', fontWeight: 600, textAlign: 'center' }}>
                                            {activeTab === 'exams' 
                                              ? `📝 ${item.topicName || item.examName}` 
                                              : `📚 Practice Test #${item.practiceNumber || '?'}: ${item.topicName || item.examName}`}
                                          </td>
                                          <td style={{ padding: '6px 8px', textAlign: 'center', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>{formatDate(item.submittedAt)}</td>
                                          <td style={{ padding: '6px 8px', textAlign: 'center', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>{formatDuration(item.durationSpent)}</td>
                                          <td style={{ padding: '6px 8px', textAlign: 'center', whiteSpace: 'nowrap' }}>
                                            <span className={`badge ${getSuspiciousClass(item.suspiciousLevel)}`} style={{ fontSize: '9px' }}>
                                              {item.suspiciousLevel.toUpperCase()}
                                            </span>
                                          </td>
                                          <td style={{ padding: '6px 8px', textAlign: 'center', fontWeight: 'bold', whiteSpace: 'nowrap' }}>
                                            <div>{item.score}/{activeTab === 'exams' ? item.totalMarks : item.totalQuestions}</div>
                                            <div style={{ fontSize: '9px', color: 'var(--text-muted)', fontWeight: 'normal' }}>{item.percentage}%</div>
                                          </td>
                                        </tr>
                                      ))}
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
          </>
        )}
      </div>

      <ScorecardModal 
        scorecard={scorecard as any}
        loading={modalLoading}
        onClose={() => {
          setSelectedId(null);
          setScorecard(null);
        }}
      />
    </div>
  );
}
