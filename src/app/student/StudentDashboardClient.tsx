'use client';

import React, { useState, useEffect, useRef, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { t } from '@/lib/i18n';
import { useRouter } from 'next/navigation';
import useSWR from 'swr';
import { fetchWithToken, createTokenFetcher } from '@/lib/swrFetcher';
import { triggerNavStart } from '@/components/NavigationProgressBar';
import TopBarTimeTracker from '@/components/TopBarTimeTracker';
import NoticeOverlayModal from '@/components/notices/NoticeOverlayModal';
import OverdueFeeModal from '@/components/fees/OverdueFeeModal';
import { 
  TrendingUp, 
  AlertTriangle, 
  CheckCircle, 
  CheckCircle2,
  Dumbbell, 
  Calendar, 
  ClipboardList, 
  MessageSquare, 
  Play, 
  LogOut, 
  Sun, 
  Moon, 
  Rocket, 
  BookOpen, 
  GraduationCap,
  Brain,
  Award,
  Sparkles,
  FileText,
  CheckSquare,
  Edit3,
  Clock,
  RotateCcw,
  CreditCard
} from 'lucide-react';
import { getScoreColor } from '@/lib/dashboardMetrics';
import StudentSelfReflectionModal from '@/components/StudentSelfReflectionModal';
import { useNotices } from '@/hooks/useNotices';
import { getGreeting } from '@/lib/dateUtils';

interface ExamItem {
  id: string;
  name: string;
  subject: string;
  questionsCount: number;
  duration?: number;
  totalTime?: number;
  totalMarks: number;
  chapterNumber?: number;
  chapter?: string;
  topicCode?: string;
  mode?: string;
  startAt?: string;
  endAt?: string;
  lateEntryRestriction?: boolean;
}

interface DashboardData {
  profile: {
    overallMastery: number;
    masteredTopics: number;
    needsAttentionTopics: number;
    name: string;
    studentCode: string;
    autonomous?: boolean;
  };
  resultsSummary: {
    examCount: number;
    averageScore: number;
    bestScore: number;
    pendingReviewCount: number;
  };
  peerReviews: {
    count: number;
    firstExamId: string | null;
  };
  exams: {
    pendingObjectiveExams: ExamItem[];
    scheduledObjectiveExams: ExamItem[];
    pendingSubjectiveExams: ExamItem[];
    scheduledSubjectiveExams: ExamItem[];
    pendingEntranceExams?: ExamItem[];
    scheduledEntranceExams?: ExamItem[];
    dailyHomePractices?: any[];
    studyChips?: any[];
  };
  zoomClass?: {
    meetingNumber: string;
    passcode: string;
    title: string;
    active: boolean;
  };
}

export default function StudentDashboardClient({ initialData }: { initialData: DashboardData | null }) {
  const { user, firebaseUser, logout } = useAuth();
  const router = useRouter();

  const [examTab, setExamTab] = useState<'objective' | 'subjective' | 'mock'>('objective');
  const [timeFilter, setTimeFilter] = useState<'overall' | 'month' | 'week'>('overall');
  const [isAnnouncementsExpanded, setIsAnnouncementsExpanded] = useState(false);
  const [activeReflectionExam, setActiveReflectionExam] = useState<{ examId: string; examName?: string } | null>(null);

  const {
    notices,
    seenNoticeIds,
    visibleNotices,
    showSeenNotices,
    setShowSeenNotices,
    activeOverlayNotice,
    handleDismissOverlayNotice,
    handleMarkNoticeAsSeen
  } = useNotices({ role: 'student', firebaseUser });

  useEffect(() => {
    if ((user as any)?.autonomous && examTab !== 'objective') {
      setExamTab('objective');
    }
  }, [user, examTab]);



  const fetcher = createTokenFetcher(firebaseUser);

  const [localCache, setLocalCache] = useState<DashboardData | undefined>(undefined);

  useEffect(() => {
    try {
      const cached = localStorage.getItem('yc_student_dashboard_cache');
      if (cached) {
        setLocalCache(JSON.parse(cached));
      }
    } catch (e) {
      console.warn('Failed to load cached dashboard data:', e);
    }
  }, []);

  const { data, error, isLoading, mutate } = useSWR<DashboardData>(
    firebaseUser ? '/api/student/dashboard' : null,
    fetcher,
    {
      revalidateOnFocus: false,
      revalidateOnMount: !initialData,
      revalidateIfStale: !initialData,
      dedupingInterval: 60000,
      keepPreviousData: true,
      fallbackData: initialData || localCache
    }
  );

  // Live Clock Ticker: dynamically updates when scheduled exams reach startAt or late limits
  const [nowMs, setNowMs] = useState<number>(Date.now());
  useEffect(() => {
    const raw = (data || initialData || localCache)?.exams;
    if (!raw) return;

    const allExams = [
      ...(raw.scheduledObjectiveExams || []),
      ...(raw.scheduledSubjectiveExams || []),
      ...(raw.scheduledEntranceExams || []),
      ...(raw.pendingObjectiveExams || []),
      ...(raw.pendingSubjectiveExams || [])
    ];

    const currentNow = Date.now();
    let nextBoundaryMs: number | null = null;
    let hasNearActiveCountdown = false;

    for (const exam of allExams) {
      const startMs = exam.startAt ? new Date(exam.startAt).getTime() : 0;
      if (startMs > currentNow) {
        if (!nextBoundaryMs || startMs < nextBoundaryMs) {
          nextBoundaryMs = startMs;
        }
        if (startMs - currentNow <= 60000) {
          hasNearActiveCountdown = true;
        }
      }
      if (exam.lateEntryRestriction === true && startMs > 0) {
        const lateLimitMs = startMs + (5 * 60 * 1000);
        if (lateLimitMs > currentNow) {
          if (!nextBoundaryMs || lateLimitMs < nextBoundaryMs) {
            nextBoundaryMs = lateLimitMs;
          }
          if (lateLimitMs - currentNow <= 60000) {
            hasNearActiveCountdown = true;
          }
        }
      }
    }

    // If an exam is within 60s of starting or late lock closing, tick every second for precision
    if (hasNearActiveCountdown) {
      const timer = setInterval(() => setNowMs(Date.now()), 1000);
      return () => clearInterval(timer);
    }

    // Otherwise, sleep until the exact next boundary, or check every 30s as a gentle fallback
    const delay = nextBoundaryMs ? Math.min(Math.max(500, nextBoundaryMs - currentNow + 100), 30000) : 30000;
    const timeout = setTimeout(() => setNowMs(Date.now()), delay);
    return () => clearTimeout(timeout);
  }, [data, initialData, localCache]);

  const [dismissedOverdue, setDismissedOverdue] = useState(false);

  const needAttentionTopics: any[] = (data as any)?.needsAttention || [];
  const srsDueTopics: any[] = (data as any)?.srsDueTopics || [];
  const attendanceRate = (data as any)?.profile?.attendanceRate !== undefined 
    ? `${(data as any).profile.attendanceRate}%` 
    : ((data as any)?.stats?.attendanceRate !== undefined ? `${(data as any).stats.attendanceRate}%` : '100%');
  const unreadChatsCount = (data as any)?.profile?.unreadChatsCount || (data as any)?.unreadChatsCount || 0;
  const feeRecord = (data as any)?.profile?.feeRecord || (data as any)?.feeRecord || null;

  useEffect(() => {
    if (data) {
      try {
        localStorage.setItem('yc_student_dashboard_cache', JSON.stringify(data));
      } catch (e) {
        console.warn('Failed to cache dashboard data:', e);
      }
    }
  }, [data]);

  const [mounted, setMounted] = useState(false);
  useEffect(() => {
    setMounted(true);
    // Warm up high-frequency subroutes in idle background time
    const routes = ['/student/learning', '/student/results', '/student/attendance', '/student/fees', '/student/chat', '/exam-register'];
    const timer = setTimeout(() => {
      routes.forEach(r => router.prefetch(r));
    }, 1200);
    return () => clearTimeout(timer);
  }, [router]);

  const handleStartExam = (examId: string, isSubjective: boolean) => {
    triggerNavStart();
    if (isSubjective) {
      router.push(`/student/take-subjective-exam?examId=${encodeURIComponent(examId)}`);
    } else {
      router.push(`/student/take-exam?examId=${encodeURIComponent(examId)}`);
    }
  };

  const handleGoToPeerReview = (examId: string | null) => {
    if (examId) {
      triggerNavStart();
      router.push(`/student/take-subjective-exam?mode=peer-review&examId=${encodeURIComponent(examId)}`);
    }
  };

  const renderStatsSkeleton = () => (
    <div style={{
      background: 'var(--surface)',
      border: '1px solid var(--border)',
      borderRadius: 'var(--radius)',
      padding: '16px 20px',
      marginBottom: '12px',
      boxShadow: 'var(--shadow-sm)'
    }} className="skeleton-blink">
      {/* Glance Card Header Skeleton */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
        <div style={{ width: '100px', height: '18px', background: 'var(--surface-3)', borderRadius: '4px' }}></div>
        <div style={{ width: '100px', height: '24px', background: 'var(--surface-2)', borderRadius: 'var(--radius-pill)' }}></div>
      </div>
      {/* 3 Stats Grid Skeleton */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '12px' }}>
        {[1, 2, 3].map(i => (
          <div key={i} style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
            <div style={{ width: '60px', height: '28px', background: 'var(--surface-3)', borderRadius: '6px' }}></div>
            <div style={{ width: '80px', height: '12px', background: 'var(--surface-2)', borderRadius: '4px' }}></div>
          </div>
        ))}
      </div>
    </div>
  );

  const renderSectionSkeleton = () => {
    const cachedExams = initialData?.exams || localCache?.exams;
    let pendingCount = 2;
    if (cachedExams) {
      if (examTab === 'objective') {
        pendingCount = (cachedExams.pendingObjectiveExams?.length || 0) + (cachedExams.scheduledObjectiveExams?.length || 0);
      } else if (examTab === 'mock') {
        pendingCount = (cachedExams.pendingEntranceExams?.length || 0) + (cachedExams.scheduledEntranceExams?.length || 0);
      } else {
        pendingCount = (cachedExams.pendingSubjectiveExams?.length || 0) + (cachedExams.scheduledSubjectiveExams?.length || 0);
      }
    }
    const rowCount = Math.max(1, pendingCount);

    return (
      <div style={{
        background: 'var(--surface)',
        border: '1px solid var(--border)',
        borderRadius: 'var(--radius)',
        padding: '16px 20px',
        marginBottom: '16px',
        boxShadow: 'var(--shadow-sm)'
      }} className="skeleton-blink">
        {/* Header skeleton */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
          <div style={{ width: '140px', height: '18px', background: 'var(--surface-3)', borderRadius: '4px' }}></div>
          <div style={{ width: '70px', height: '20px', background: 'var(--surface-2)', borderRadius: 'var(--radius-pill)' }}></div>
        </div>
        {/* Items list skeleton */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          {Array.from({ length: rowCount }).map((_, i) => (
            <div key={i} style={{ height: '56px', background: 'var(--surface-2)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)' }}></div>
          ))}
        </div>
      </div>
    );
  };

  const activeData = data || initialData || localCache;
  const profile = activeData?.profile;
  const resultsSummary = activeData?.resultsSummary;
  const peerReviews = activeData?.peerReviews || { count: 0, firstExamId: null };
  const pendingSelfReviews: any[] = (activeData as any)?.pendingSelfReviews || [];
  const pendingAbsences: any[] = (activeData as any)?.pendingAbsences || [];
  const activeSrsDue: any[] = (activeData as any)?.srsDueTopics || [];
  const rawExams = activeData?.exams || { pendingObjectiveExams: [], scheduledObjectiveExams: [], pendingSubjectiveExams: [], scheduledSubjectiveExams: [], dailyHomePractices: [], studyChips: [] };
  
  // Real-time dynamic promotion: If client clock has reached startAt, immediately unlock exam with Start button without waiting for manual refresh
  const exams = useMemo(() => {
    const pendingObj = [...(rawExams.pendingObjectiveExams || [])];
    const scheduledObj: ExamItem[] = [];

    (rawExams.scheduledObjectiveExams || []).forEach(exam => {
      const startMs = exam.startAt ? new Date(exam.startAt).getTime() : 0;
      if (startMs > 0 && nowMs >= startMs) {
        // Automatically promoted to active pending exam with Start button!
        pendingObj.push(exam);
      } else {
        scheduledObj.push(exam);
      }
    });

    const pendingSub = [...(rawExams.pendingSubjectiveExams || [])];
    const scheduledSub: ExamItem[] = [];

    (rawExams.scheduledSubjectiveExams || []).forEach(exam => {
      const startMs = exam.startAt ? new Date(exam.startAt).getTime() : 0;
      if (startMs > 0 && nowMs >= startMs) {
        pendingSub.push(exam);
      } else {
        scheduledSub.push(exam);
      }
    });

    const pendingEnt = [...(rawExams.pendingEntranceExams || [])];
    const scheduledEnt: ExamItem[] = [];

    (rawExams.scheduledEntranceExams || []).forEach(exam => {
      const startMs = exam.startAt ? new Date(exam.startAt).getTime() : 0;
      if (startMs > 0 && nowMs >= startMs) {
        pendingEnt.push(exam);
      } else {
        scheduledEnt.push(exam);
      }
    });

    return {
      ...rawExams,
      pendingObjectiveExams: pendingObj,
      scheduledObjectiveExams: scheduledObj,
      pendingSubjectiveExams: pendingSub,
      scheduledSubjectiveExams: scheduledSub,
      pendingEntranceExams: pendingEnt,
      scheduledEntranceExams: scheduledEnt
    };
  }, [rawExams, nowMs]);

  if (error) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div className="alert-box alert-box-danger" style={{ display: 'block', maxWidth: '400px', textAlign: 'center' }}>
          {error?.message || 'Could not load student dashboard profile.'}
        </div>
        <button className="btn btn-primary" onClick={() => window.location.reload()} style={{ marginTop: '16px' }}>Retry</button>
      </div>
    );
  }
  const greeting = getGreeting(mounted);
  const firstName = profile?.name ? profile.name.split(' ')[0] : '';
  const hasActionItems = Boolean(
    pendingSelfReviews.length ||
    pendingAbsences.length ||
    needAttentionTopics.length ||
    activeSrsDue.length ||
    peerReviews.count
  );
  const totalActionCount =
    pendingSelfReviews.length +
    pendingAbsences.length +
    (peerReviews.count ? 1 : 0) +
    needAttentionTopics.length +
    activeSrsDue.length;

  return (
    <div className="page-wrapper" style={{ background: 'var(--bg)', minHeight: '100vh' }}>
      <div className="dashboard-container" style={{ maxWidth: '1000px', margin: '0 auto', padding: '4px 8px 30px 8px' }}>
        {(!activeData && isLoading) || !profile ? (
          <>
            {renderStatsSkeleton()}
            {renderSectionSkeleton()}
          </>
        ) : (
          <>
            {/* CARD 1: Glance (Soothing Matte Card) */}
            <div className="card card-blue" style={{
              borderRadius: 'var(--radius)',
              padding: '10px 12px',
              marginBottom: '8px',
              boxShadow: 'var(--shadow-sm)',
              position: 'relative'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px', flexWrap: 'nowrap', gap: '6px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <TrendingUp size={18} color="var(--info)" />
                  <h3 style={{ fontSize: '14px', fontWeight: 800, margin: 0, color: 'var(--text)', lineHeight: 1.2, whiteSpace: 'nowrap' }}>Glance</h3>
                </div>
                {/* Interactive Time Range Filter Dropdown */}
                <select
                  className="glance-period-select"
                  value={timeFilter}
                  onChange={(e: any) => setTimeFilter(e.target.value)}
                  style={{
                    background: 'var(--surface-2)',
                    color: 'var(--text)',
                    fontSize: '11px',
                    fontWeight: 600,
                    padding: '3px 8px',
                    borderRadius: 'var(--radius-pill)',
                    border: '1px solid var(--border)',
                    outline: 'none',
                    cursor: 'pointer',
                    width: 'auto',
                    minWidth: '90px',
                    maxWidth: '110px',
                    flexShrink: 0
                  }}
                >
                  <option value="overall">Overall</option>
                  <option value="month">This Month</option>
                  <option value="week">This Week</option>
                </select>
              </div>

              {/* 3 Stats Grid */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px', alignItems: 'center' }}>
                {/* Stat 1: Avg Exam Marks (Click opens results page) */}
                <div 
                  onClick={() => router.push('/student/results')}
                  style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', justifyContent: 'center', gap: '2px', cursor: 'pointer', background: 'var(--surface-2)', padding: '8px 4px', borderRadius: '10px', border: '1px solid var(--border)', transition: 'all 0.2s', boxShadow: 'var(--shadow-sm)' }}
                  title="Click to view detailed exam results"
                >
                  <div style={{ fontSize: '1.55rem', fontWeight: 800, color: 'var(--info)', lineHeight: 1 }}>
                    {resultsSummary?.examCount ? Math.round(resultsSummary.averageScore) : 0}%
                  </div>
                  <div style={{ fontSize: '11px', color: 'var(--text-secondary)', fontWeight: 700 }}>
                    Average Marks
                  </div>
                </div>

                {/* Stat 2: LQ Score */}
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', justifyContent: 'center', gap: '2px', background: 'var(--surface-2)', padding: '8px 4px', borderRadius: '10px', border: '1px solid var(--border)', boxShadow: 'var(--shadow-sm)' }}>
                  <div style={{ fontSize: '1.55rem', fontWeight: 800, color: 'var(--success)', lineHeight: 1 }}>
                    {Math.round((profile as any)?.lqScore ?? profile?.overallMastery ?? 0)}%
                  </div>
                  <div style={{ fontSize: '11px', color: 'var(--text-secondary)', fontWeight: 700 }}>
                    LQ Score
                  </div>
                  {Boolean((profile as any)?.srsEnabled) ? (
                    <div style={{ fontSize: '9.5px', color: 'var(--text-secondary)', fontWeight: 600 }}>
                      🧠 {(profile as any)?.averageRetention ?? 0}% Retention
                    </div>
                  ) : (
                    <div style={{ fontSize: '9.5px', color: 'var(--text-secondary)', fontWeight: 600 }}>
                      Mastery Index
                    </div>
                  )}
                </div>

                {/* Stat 3: Efforts % */}
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', justifyContent: 'center', gap: '2px', background: 'var(--surface-2)', padding: '8px 4px', borderRadius: '10px', border: '1px solid var(--border)', boxShadow: 'var(--shadow-sm)' }}>
                  <div style={{ fontSize: '1.55rem', fontWeight: 800, color: 'var(--warning)', lineHeight: 1 }}>
                    {Math.round((profile as any)?.effortsPercent ?? Math.min(100, Math.round((((profile as any)?.practicesCompletedCount || 0) / Math.max(1, (profile as any)?.totalTopicsCount || 24)) * 100)))}%
                  </div>
                  <div style={{ fontSize: '11px', color: 'var(--text-secondary)', fontWeight: 700 }}>
                    Efforts %
                  </div>
                </div>
              </div>
            </div>

            {/* CARD 2: Action Needed / All Clear Ledger */}
            <div className={hasActionItems ? "card card-amber" : "card card-emerald"} style={{
              borderRadius: 'var(--radius)',
              padding: '10px 12px',
              marginBottom: '8px',
              display: 'flex',
              flexDirection: 'column',
              gap: '6px'
            }}>
              {/* Compact Header */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                {hasActionItems ? (
                  <AlertTriangle size={18} color="var(--warning)" style={{ flexShrink: 0 }} />
                ) : (
                  <CheckCircle2 size={18} color="var(--success)" style={{ flexShrink: 0 }} />
                )}
                <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.2 }}>
                  {hasActionItems 
                    ? `${totalActionCount} Action Item(s) Need Attention` 
                    : 'All Clear! You are fully on track!'}
                </h3>
              </div>

              {/* 1. Pending Self-Reflection Reviews (Highest Priority Action Item) */}
              {pendingSelfReviews.length > 0 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                  {pendingSelfReviews.map((r: any) => (
                    <div key={r.id || r.examId} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', background: 'var(--danger-bg)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--danger-border)', gap: '8px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flex: 1 }}>
                        <span style={{ fontSize: '18px' }}>📝</span>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                          <div style={{ fontWeight: 800, fontSize: '12px', color: 'var(--danger)' }}>
                            Exam Self-Reflection Required: {r.examName || r.examId}
                          </div>
                          <div style={{ fontSize: '10.5px', color: 'var(--text-secondary)' }}>
                            Score: {r.score}/{r.totalMarks} ({r.percentage}%) • Complete mistake review to unblock exams
                          </div>
                        </div>
                      </div>
                      <button 
                        className="btn btn-primary" 
                        style={{ padding: '4px 12px', fontSize: '11px', borderRadius: 'var(--radius-sm)', fontWeight: 800, whiteSpace: 'nowrap', background: 'var(--danger)', color: 'var(--text-white)', border: 'none' }}
                        onClick={() => setActiveReflectionExam({ examId: r.examId, examName: r.examName })}
                      >
                        Reflect & Unlock
                      </button>
                    </div>
                  ))}
                </div>
              )}

              {/* 2. Missed Exam Absences Pending Parent Sign-Off */}
              {pendingAbsences.length > 0 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                  {pendingAbsences.map((a: any) => (
                    <div key={a.id || a.examId} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', background: 'var(--warning-bg)', borderRadius: 'var(--radius-sm)', border: '1px solid rgba(251, 191, 36, 0.25)', gap: '8px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flex: 1 }}>
                        <span style={{ fontSize: '18px' }}>⚠️</span>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                          <div style={{ fontWeight: 800, fontSize: '12px', color: 'var(--warning)' }}>
                            Missed Exam: Parent Acknowledgment Pending
                          </div>
                          <div style={{ fontSize: '10.5px', color: 'var(--text-secondary)' }}>
                            {a.name} ({a.subject || 'General'}) • Parent must acknowledge absence in Parent Portal to unlock exams
                          </div>
                        </div>
                      </div>
                      <span style={{ padding: '3px 8px', fontSize: '10px', borderRadius: '4px', background: 'var(--surface-2)', color: 'var(--warning)', border: '1px solid rgba(251, 191, 36, 0.3)', fontWeight: 700, whiteSpace: 'nowrap' }}>
                        Sign-off Pending
                      </span>
                    </div>
                  ))}
                </div>
              )}

              {/* 3. Peer Review Alert */}
              {peerReviews.count > 0 && (
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '6px 10px', background: 'var(--surface-2)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border)' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <ClipboardList size={16} color="var(--warning)" />
                    <div style={{ fontWeight: 700, fontSize: '12px', color: 'var(--text)' }}>Peer Paper Review Pending</div>
                  </div>
                  <button 
                    className="btn btn-primary" 
                    style={{ padding: '4px 10px', fontSize: '11px', borderRadius: 'var(--radius-sm)', fontWeight: 700 }}
                    onClick={() => handleGoToPeerReview(peerReviews.firstExamId)}
                  >
                    Grade Paper
                  </button>
                </div>
              )}

              {/* 3.5. Spaced Repetition Due (Mastered Topics Ready for Micro-Refresher) */}
              {Boolean((profile as any)?.srsEnabled) && activeSrsDue.length > 0 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  {activeSrsDue.slice(0, 3).map((t: any) => (
                    <div key={t.topicCode} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 10px', background: 'var(--surface-2)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border)', borderLeft: '3.5px solid var(--info)', gap: '8px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flex: 1 }}>
                        <span style={{ fontSize: '18px' }}>🧠</span>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                          <div style={{ fontWeight: 800, fontSize: '12px', color: 'var(--info)' }}>
                            Memory Refresher Due: {t.topicName}
                          </div>
                          <div style={{ fontSize: '10.5px', color: 'var(--text-secondary)' }}>
                            {t.subjectName || 'General'} • {t.srsSchedule?.stageLabel || 'Interval Refresher'} • {t.srsSchedule?.estimatedRetention || 75}% Retention
                          </div>
                        </div>
                      </div>
                      <button 
                        className="btn btn-primary" 
                        style={{ padding: '4px 10px', fontSize: '11px', borderRadius: 'var(--radius-sm)', fontWeight: 800, whiteSpace: 'nowrap', background: 'var(--accent)', color: 'var(--text-on-accent)', border: 'none' }}
                        onClick={() => router.push(`/student/topic?topicCode=${encodeURIComponent(t.topicCode)}&category=revision`)}
                      >
                        Start Workout
                      </button>
                    </div>
                  ))}
                </div>
              )}

              {/* 4. Need Attention Topics List */}
              {needAttentionTopics.length > 0 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  {needAttentionTopics.slice(0, 4).map((t: any) => (
                    <div key={t.topicCode} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '6px 10px', background: 'var(--surface-2)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border)', gap: '8px' }}>
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '1px', flex: 1 }}>
                        <div style={{ fontWeight: 700, fontSize: '12px', color: 'var(--text)' }}>{t.topicName}</div>
                        <div style={{ fontSize: '10.5px', color: 'var(--text-secondary)', display: 'flex', alignItems: 'center', gap: '4px', flexWrap: 'wrap' }}>
                          <span>{t.subjectName || 'General'}</span>
                          <span>•</span>
                          {t.isAbsentExam ? (
                            <span style={{ color: 'var(--danger)', fontWeight: 700 }}>Missed Exam</span>
                          ) : (
                            <span style={{ color: 'var(--warning)', fontWeight: 700 }}>{t.mastery || 0}% Mastery</span>
                          )}
                          {t.topicClassification && (
                            <>
                              <span>•</span>
                              <span style={{
                                fontSize: '9.5px',
                                fontWeight: 700,
                                padding: '1px 6px',
                                borderRadius: '4px',
                                background: (t.topicClassification === 'minor' || t.topicClassification === 'micro') ? 'var(--success-bg)' : (t.topicClassification === 'major' || t.topicClassification === 'calculative' || t.topicClassification === 'hots') ? 'var(--danger-bg)' : 'var(--info-bg)',
                                color: (t.topicClassification === 'minor' || t.topicClassification === 'micro') ? 'var(--success)' : (t.topicClassification === 'major' || t.topicClassification === 'calculative' || t.topicClassification === 'hots') ? 'var(--danger)' : 'var(--info)',
                                border: `1px solid ${(t.topicClassification === 'minor' || t.topicClassification === 'micro') ? 'rgba(52, 211, 153, 0.25)' : (t.topicClassification === 'major' || t.topicClassification === 'calculative' || t.topicClassification === 'hots') ? 'rgba(248, 113, 113, 0.25)' : 'rgba(56, 189, 248, 0.25)'}`
                              }}>
                                {(t.topicClassification === 'minor' || t.topicClassification === 'micro') && '📘 Minor (6 Qs to Master • Max 2 Sets)'}
                                {(t.topicClassification === 'medium' || t.topicClassification === 'moderate' || t.topicClassification === 'conceptual') && '📙 Medium (10 Qs to Master • Max 3 Sets)'}
                                {(t.topicClassification === 'major' || t.topicClassification === 'calculative' || t.topicClassification === 'hots') && '📕 Major (15 Qs to Master • Max 3 Sets)'}
                              </span>
                            </>
                          )}
                        </div>
                      </div>
                      <button 
                        className="btn btn-secondary btn-sm"
                        style={{ padding: '3px 8px', fontSize: '10.5px', fontWeight: 700 }}
                        onClick={() => router.push(`/student/topic?topicCode=${encodeURIComponent(t.topicCode)}&category=needsAttention`)}
                      >
                        Practice
                      </button>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* CARD 3: Quick Navigation Hotspot Grid */}
            <div className="card card-purple" style={{
              borderRadius: 'var(--radius)',
              padding: '10px 12px',
              marginBottom: '8px',
              boxShadow: 'var(--shadow-sm)',
              display: 'flex',
              flexDirection: 'column',
              gap: '8px'
            }}>
              <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 800, color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Rocket size={18} color="var(--accent)" /> Quick Navigation
              </h3>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(70px, 1fr))', gap: '6px' }}>
                {/* Hotspot 1: Learn OS */}
                <div 
                  onClick={() => { triggerNavStart(); router.push('/student/learning'); }}
                  onMouseEnter={(e) => { router.prefetch('/student/learning'); e.currentTarget.style.borderColor = 'var(--accent)'; e.currentTarget.style.transform = 'translateY(-2px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    padding: '8px 4px',
                    background: 'var(--surface-2)',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    textAlign: 'center',
                    gap: '4px',
                    transition: 'all 0.2s ease',
                    boxShadow: 'var(--shadow-sm)'
                  }}
                >
                  <GraduationCap size={24} color="var(--accent)" />
                  <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text)' }}>Learn OS</span>
                </div>

                {/* Hotspot 2: Attendance showing % */}
                <div 
                  onClick={() => { triggerNavStart(); router.push('/student/attendance'); }}
                  onMouseEnter={(e) => { router.prefetch('/student/attendance'); e.currentTarget.style.borderColor = 'var(--success)'; e.currentTarget.style.transform = 'translateY(-2px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    padding: '8px 4px',
                    background: 'var(--surface-2)',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    textAlign: 'center',
                    gap: '4px',
                    transition: 'all 0.2s ease',
                    boxShadow: 'var(--shadow-sm)'
                  }}
                >
                  <Calendar size={24} color="var(--success)" />
                  <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text)' }}>
                    Attendance ({attendanceRate})
                  </span>
                </div>

                {/* Hotspot 3: Exam Register */}
                <div 
                  onClick={() => { triggerNavStart(); router.push('/exam-register'); }}
                  onMouseEnter={(e) => { router.prefetch('/exam-register'); e.currentTarget.style.borderColor = 'var(--warning)'; e.currentTarget.style.transform = 'translateY(-2px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    padding: '8px 4px',
                    background: 'var(--surface-2)',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    textAlign: 'center',
                    gap: '4px',
                    transition: 'all 0.2s ease',
                    boxShadow: 'var(--shadow-sm)'
                  }}
                >
                  <ClipboardList size={24} color="var(--warning)" />
                  <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text)' }}>Exam Register</span>
                </div>

                {/* Hotspot 4: Fees & Ledger */}
                <div 
                  onClick={() => { triggerNavStart(); router.push('/student/fees'); }}
                  onMouseEnter={(e) => { router.prefetch('/student/fees'); e.currentTarget.style.borderColor = 'var(--primary)'; e.currentTarget.style.transform = 'translateY(-2px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    padding: '8px 4px',
                    background: 'var(--surface-2)',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    textAlign: 'center',
                    gap: '4px',
                    transition: 'all 0.2s ease',
                    boxShadow: 'var(--shadow-sm)'
                  }}
                >
                  <CreditCard size={24} color="var(--primary)" />
                  <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text)' }}>Fees & Dues</span>
                </div>

                {/* Hotspot 5: Live Chat */}
                <div 
                  onClick={() => { triggerNavStart(); router.push('/student/chat'); }}
                  onMouseEnter={(e) => { router.prefetch('/student/chat'); e.currentTarget.style.borderColor = 'var(--info)'; e.currentTarget.style.transform = 'translateY(-2px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                  style={{
                    position: 'relative',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    padding: '8px 4px',
                    background: 'var(--surface-2)',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    textAlign: 'center',
                    gap: '4px',
                    transition: 'all 0.2s ease',
                    boxShadow: 'var(--shadow-sm)'
                  }}
                >
                  <MessageSquare size={24} color="var(--info)" />
                  <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text)' }}>Live Chat</span>
                  {unreadChatsCount > 0 && (
                    <span style={{
                      position: 'absolute',
                      top: '4px',
                      right: '6px',
                      background: 'var(--danger)',
                      color: 'var(--text-white)',
                      fontSize: '9px',
                      fontWeight: 800,
                      borderRadius: '10px',
                      padding: '1px 5px',
                      lineHeight: '1.1'
                    }}>
                      {unreadChatsCount}
                    </span>
                  )}
                </div>
              </div>
            </div>

        {/* ROW 2: Exams & Review Card (Full Width) */}
        <div className="card card-academic" style={{ borderRadius: 'var(--radius)', overflow: 'hidden', marginBottom: '8px', boxShadow: 'var(--shadow-sm)' }}>
          <div className="exams-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 12px', borderBottom: '1px solid var(--border)' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <FileText size={18} color="var(--primary)" />
              <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)', margin: 0 }}>Exams & Review</h3>
            </div>
            <div className="review-badge" style={{ background: 'var(--primary)', color: 'white', padding: '2px 8px', borderRadius: '20px', fontSize: '11px', fontWeight: 800, cursor: 'pointer' }}>
              Pending: {resultsSummary?.pendingReviewCount || 0}
            </div>
          </div>

          {/* Peer Review Container */}
          {peerReviews.count > 0 && (
            <div className="peer-review-link-container" style={{ display: 'block', padding: '6px 12px', borderBottom: '1px solid var(--border)', background: 'var(--success-bg)' }}>
              <a className="peer-review-link" onClick={() => handleGoToPeerReview(peerReviews.firstExamId)} style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', color: 'var(--success)', fontSize: '12px', fontWeight: 700, textDecoration: 'none', cursor: 'pointer' }}>
                <RotateCcw size={14} color="var(--success)" />
                <span>Peer Review Pending</span>
                <span className="badge" style={{ background: 'var(--danger)', color: 'white', borderRadius: '50%', padding: '1px 5px', fontSize: '9.5px', marginLeft: '4px' }}>{peerReviews.count}</span>
              </a>
              <span className="peer-review-sub" style={{ fontSize: '11px', color: 'var(--text-muted)', marginLeft: '6px' }}>Review your classmate's paper</span>
            </div>
          )}

          {/* Exam Tabs (Obj, Sub, Mock) */}
          {(user as any)?.autonomous !== true ? (
            <div className="exam-tabs" style={{ display: 'flex', borderBottom: '1px solid var(--border)', background: 'var(--surface-2)', padding: '6px 8px', gap: '6px' }}>
              <div 
                className={`exam-tab ${examTab === 'objective' ? 'active' : ''}`} 
                onClick={() => setExamTab('objective')}
                style={{ flex: 1, textAlign: 'center', padding: '6px 0', fontSize: '12px', fontWeight: 800, cursor: 'pointer', borderRadius: '6px', background: examTab === 'objective' ? 'var(--surface)' : 'transparent', color: examTab === 'objective' ? 'var(--primary)' : 'var(--text-muted)', boxShadow: examTab === 'objective' ? 'var(--shadow-sm)' : 'none', border: examTab === 'objective' ? '2px solid var(--primary)' : '1px solid var(--border)', transition: 'all 0.18s ease' }}
              >
                Obj <span className="tab-count" style={{ background: examTab === 'objective' ? 'var(--primary)' : 'var(--surface-3, var(--border))', color: 'var(--text-white)', borderRadius: '8px', padding: '1px 5px', fontSize: '10px', fontWeight: 800, marginLeft: '3px' }}>{exams.pendingObjectiveExams.length + exams.scheduledObjectiveExams.length}</span>
              </div>
              <div 
                className={`exam-tab ${examTab === 'subjective' ? 'active' : ''}`} 
                onClick={() => setExamTab('subjective')}
                style={{ flex: 1, textAlign: 'center', padding: '6px 0', fontSize: '12px', fontWeight: 800, cursor: 'pointer', borderRadius: '6px', background: examTab === 'subjective' ? 'var(--surface)' : 'transparent', color: examTab === 'subjective' ? 'var(--secondary)' : 'var(--text-muted)', boxShadow: examTab === 'subjective' ? 'var(--shadow-sm)' : 'none', border: examTab === 'subjective' ? '2px solid var(--secondary)' : '1px solid var(--border)', transition: 'all 0.18s ease' }}
              >
                Sub <span className="tab-count" style={{ background: examTab === 'subjective' ? 'var(--secondary)' : 'var(--surface-3)', color: 'var(--text-white)', borderRadius: '8px', padding: '1px 5px', fontSize: '10px', fontWeight: 800, marginLeft: '3px' }}>{exams.pendingSubjectiveExams.length + exams.scheduledSubjectiveExams.length}</span>
              </div>
              <div 
                className={`exam-tab ${examTab === 'mock' ? 'active' : ''}`} 
                onClick={() => setExamTab('mock')}
                style={{ flex: 1, textAlign: 'center', padding: '6px 0', fontSize: '12px', fontWeight: 800, cursor: 'pointer', borderRadius: '6px', background: examTab === 'mock' ? 'var(--surface)' : 'transparent', color: examTab === 'mock' ? 'var(--warning)' : 'var(--text-muted)', boxShadow: examTab === 'mock' ? 'var(--shadow-sm)' : 'none', border: examTab === 'mock' ? '2px solid var(--warning)' : '1px solid var(--border)', transition: 'all 0.18s ease' }}
              >
                Mock <span className="tab-count" style={{ background: examTab === 'mock' ? 'var(--warning)' : 'var(--surface-3, var(--border))', color: 'var(--text-white)', borderRadius: '8px', padding: '1px 5px', fontSize: '10px', fontWeight: 800, marginLeft: '3px' }}>{(exams.pendingEntranceExams?.length || 0) + (exams.scheduledEntranceExams?.length || 0)}</span>
              </div>
            </div>
          ) : null}

          {/* Objective Exams List */}
          {examTab === 'objective' && (
            <div className="pending-exams-flex-list" style={{ display: 'flex', flexDirection: 'column', padding: '8px 10px', maxHeight: '350px', overflowY: 'auto', gap: '6px' }}>
              {exams.pendingObjectiveExams.length === 0 && exams.scheduledObjectiveExams.length === 0 ? (
                <div className="no-exams" style={{ textAlign: 'center', color: 'var(--text-faint)', padding: '16px 0', fontSize: '12.5px' }}>No pending objective exams</div>
              ) : (
                <>
                  {exams.pendingObjectiveExams.map((exam) => {
                    const startMs = exam.startAt ? new Date(exam.startAt).getTime() : 0;
                    const lateLimitMs = (startMs > 0 && exam.lateEntryRestriction === true) ? startMs + (5 * 60 * 1000) : 0;
                    const isLateLocked = lateLimitMs > 0 && nowMs > lateLimitMs;
                    const secondsLeftToJoin = lateLimitMs > 0 ? Math.max(0, Math.floor((lateLimitMs - nowMs) / 1000)) : 0;
                    const minsLeft = Math.floor(secondsLeftToJoin / 60);
                    const secsLeft = secondsLeftToJoin % 60;

                    return (
                      <div key={exam.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 10px', background: 'var(--surface-2)', borderRadius: '8px', border: isLateLocked ? '1px solid var(--danger-border, rgba(239, 68, 68, 0.4))' : '1px solid var(--border)', boxShadow: 'var(--shadow-sm)' }}>
                        <div style={{ flex: 1, minWidth: 0, paddingRight: '8px' }}>
                          <div className="pending-exam-name" style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }} title={exam.name}>{exam.name}</div>
                          <div className="pending-exam-details" style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '1px' }}>
                            {exam.subject} • {exam.questionsCount} Qs • {exam.duration} mins • {exam.totalMarks} Marks
                            {isLateLocked ? (
                              <div style={{ marginTop: '2px', color: 'var(--danger)', fontWeight: 700, fontSize: '10.5px', display: 'flex', alignItems: 'center', gap: '3px' }}>
                                <AlertTriangle size={11} color="var(--danger)" />
                                <span>⛔ Entry Closed (Late entry allowed only within 5 mins)</span>
                              </div>
                            ) : lateLimitMs > 0 ? (
                              <div style={{ marginTop: '2px', color: 'var(--success)', fontWeight: 700, fontSize: '10.5px', display: 'flex', alignItems: 'center', gap: '3px' }}>
                                <Clock size={11} color="var(--success)" />
                                <span>🟢 LIVE • Entry closes in: {minsLeft}m {String(secsLeft).padStart(2, '0')}s</span>
                              </div>
                            ) : null}
                          </div>
                        </div>
                        {isLateLocked ? (
                          <button className="btn btn-secondary btn-sm" style={{ padding: '4px 8px', fontSize: '10.5px', opacity: 0.6, cursor: 'not-allowed', background: 'var(--surface-3)', color: 'var(--danger)' }} disabled>
                            Closed
                          </button>
                        ) : (
                          <button className="btn btn-primary btn-sm" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => handleStartExam(exam.id, false)}>
                            Start
                          </button>
                        )}
                      </div>
                    );
                  })}
                  {exams.scheduledObjectiveExams.map((exam) => {
                    const startMs = exam.startAt ? new Date(exam.startAt).getTime() : 0;
                    const secondsUntilStart = startMs > 0 ? Math.max(0, Math.floor((startMs - nowMs) / 1000)) : 0;
                    const minsUntil = Math.floor(secondsUntilStart / 60);
                    const secsUntil = secondsUntilStart % 60;

                    return (
                      <div key={exam.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 10px', background: 'var(--surface-2)', borderRadius: '8px', border: '1px solid var(--border)', opacity: 0.85 }}>
                        <div style={{ flex: 1, minWidth: 0, paddingRight: '8px' }}>
                          <div className="pending-exam-name" style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }} title={exam.name}>{exam.name}</div>
                          <div className="pending-exam-details" style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '1px' }}>
                            {exam.subject} • {exam.questionsCount} Qs • {exam.duration} mins • {exam.totalMarks} Marks
                            <div style={{ marginTop: '2px', color: 'var(--warning)', fontWeight: 700, fontSize: '10.5px', display: 'flex', alignItems: 'center', gap: '3px' }}>
                              <Clock size={11} color="var(--warning)" />
                              <span>
                                Starts: {exam.startAt ? new Date(exam.startAt).toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' }) : '—'}
                                {secondsUntilStart > 0 && secondsUntilStart < 3600 ? ` (in ${minsUntil}m ${String(secsUntil).padStart(2, '0')}s)` : ''}
                              </span>
                            </div>
                          </div>
                        </div>
                        <button className="btn btn-secondary btn-sm" style={{ padding: '4px 8px', fontSize: '10.5px' }} disabled>
                          Locked
                        </button>
                      </div>
                    );
                  })}
                </>
              )}
            </div>
          )}

          {/* Subjective Exams List */}
          {examTab === 'subjective' && (
            <div className="pending-exams-flex-list" style={{ display: 'flex', flexDirection: 'column', padding: '8px 10px', maxHeight: '350px', overflowY: 'auto', gap: '6px' }}>
              {exams.pendingSubjectiveExams.length === 0 && exams.scheduledSubjectiveExams.length === 0 ? (
                <div className="no-exams" style={{ textAlign: 'center', color: 'var(--text-faint)', padding: '16px 0', fontSize: '12.5px' }}>No pending subjective exams</div>
              ) : (
                <>
                  {exams.pendingSubjectiveExams.map((exam) => {
                    const startMs = exam.startAt ? new Date(exam.startAt).getTime() : 0;
                    const lateLimitMs = (startMs > 0 && exam.lateEntryRestriction === true) ? startMs + (5 * 60 * 1000) : 0;
                    const isLateLocked = lateLimitMs > 0 && nowMs > lateLimitMs;
                    const secondsLeftToJoin = lateLimitMs > 0 ? Math.max(0, Math.floor((lateLimitMs - nowMs) / 1000)) : 0;
                    const minsLeft = Math.floor(secondsLeftToJoin / 60);
                    const secsLeft = secondsLeftToJoin % 60;

                    return (
                      <div key={exam.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 10px', background: 'var(--surface-2)', borderRadius: '8px', border: isLateLocked ? '1px solid var(--danger-border, rgba(239, 68, 68, 0.4))' : '1px solid var(--border)', boxShadow: 'var(--shadow-sm)' }}>
                        <div style={{ flex: 1, minWidth: 0, paddingRight: '8px' }}>
                          <div className="pending-exam-name" style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }} title={exam.name}>{exam.name}</div>
                          <div className="pending-exam-details" style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '1px' }}>
                            {exam.subject} • {exam.questionsCount} Qs • {exam.totalTime} mins • {exam.totalMarks} Marks • Mode: {exam.mode}
                            {isLateLocked ? (
                              <div style={{ marginTop: '2px', color: 'var(--danger)', fontWeight: 700, fontSize: '10.5px', display: 'flex', alignItems: 'center', gap: '3px' }}>
                                <AlertTriangle size={11} color="var(--danger)" />
                                <span>⛔ Entry Closed (Late entry allowed only within 5 mins)</span>
                              </div>
                            ) : lateLimitMs > 0 ? (
                              <div style={{ marginTop: '2px', color: 'var(--success)', fontWeight: 700, fontSize: '10.5px', display: 'flex', alignItems: 'center', gap: '3px' }}>
                                <Clock size={11} color="var(--success)" />
                                <span>🟢 LIVE • Entry closes in: {minsLeft}m {String(secsLeft).padStart(2, '0')}s</span>
                              </div>
                            ) : null}
                          </div>
                        </div>
                        {isLateLocked ? (
                          <button className="btn btn-secondary btn-sm" style={{ padding: '4px 8px', fontSize: '10.5px', opacity: 0.6, cursor: 'not-allowed' }} disabled>
                            Closed
                          </button>
                        ) : (
                          <button className="btn btn-primary btn-sm" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => handleStartExam(exam.id, true)}>
                            Start
                          </button>
                        )}
                      </div>
                    );
                  })}
                  {exams.scheduledSubjectiveExams.map((exam) => {
                    const startMs = exam.startAt ? new Date(exam.startAt).getTime() : 0;
                    const secondsUntilStart = startMs > 0 ? Math.max(0, Math.floor((startMs - nowMs) / 1000)) : 0;
                    const minsUntil = Math.floor(secondsUntilStart / 60);
                    const secsUntil = secondsUntilStart % 60;

                    return (
                      <div key={exam.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 10px', background: 'var(--surface-2)', borderRadius: '8px', border: '1px solid var(--border)', opacity: 0.85 }}>
                        <div style={{ flex: 1, minWidth: 0, paddingRight: '8px' }}>
                          <div className="pending-exam-name" style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }} title={exam.name}>{exam.name}</div>
                          <div className="pending-exam-details" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                            {exam.subject} • {exam.questionsCount} Qs • {exam.totalTime} mins • {exam.totalMarks} Marks • Mode: {exam.mode}
                            <div style={{ marginTop: '2px', color: 'var(--warning)', fontWeight: 600, fontSize: '10.5px', display: 'flex', alignItems: 'center', gap: '3px' }}>
                              <Clock size={11} color="var(--warning)" />
                              <span>
                                Starts: {exam.startAt ? new Date(exam.startAt).toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' }) : '—'}
                                {secondsUntilStart > 0 && secondsUntilStart < 3600 ? ` (in ${minsUntil}m ${String(secsUntil).padStart(2, '0')}s)` : ''}
                              </span>
                            </div>
                          </div>
                        </div>
                        <button className="start-exam-small subjective" disabled style={{ background: 'var(--text-faint)', color: 'var(--text-muted)', border: 'none', padding: '4px 10px', borderRadius: '20px', fontSize: '10.5px', fontWeight: 600, cursor: 'not-allowed', flexShrink: 0 }}>
                          Locked
                        </button>
                      </div>
                    );
                  })}
                </>
              )}
            </div>
          )}

          {/* Mock Exams List */}
          {examTab === 'mock' && (
            <div className="pending-exams-flex-list" style={{ display: 'flex', flexDirection: 'column', padding: '8px 10px', maxHeight: '350px', overflowY: 'auto', gap: '6px' }}>
              {(exams.pendingEntranceExams?.length || 0) === 0 && (exams.scheduledEntranceExams?.length || 0) === 0 ? (
                <div className="no-exams" style={{ textAlign: 'center', color: 'var(--text-faint)', padding: '16px 0', fontSize: '12.5px' }}>No pending mock exams</div>
              ) : (
                <>
                  {(exams.pendingEntranceExams || []).map((exam) => (
                    <div key={exam.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 10px', background: 'var(--bg-soft)', borderRadius: '8px', border: '1px solid var(--border-light)' }}>
                      <div style={{ flex: 1, minWidth: 0, paddingRight: '8px' }}>
                        <div className="pending-exam-name" style={{ fontSize: '13px', fontWeight: 'bold', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }} title={exam.name}>{exam.name}</div>
                        <div className="pending-exam-details" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                          {exam.subject} • {exam.questionsCount} Qs • {exam.duration} mins • {exam.totalMarks} Marks
                        </div>
                      </div>
                      <button className="start-exam-small" onClick={() => handleStartExam(exam.id, false)} style={{ background: 'var(--accent-grad)', color: 'white', border: 'none', padding: '4px 10px', borderRadius: '20px', fontSize: '10.5px', fontWeight: 600, cursor: 'pointer', flexShrink: 0 }}>
                        Start
                      </button>
                    </div>
                  ))}
                  {(exams.scheduledEntranceExams || []).map((exam) => (
                    <div key={exam.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 10px', background: 'var(--bg-soft)', borderRadius: '8px', border: '1px solid var(--border-light)', opacity: 0.8 }}>
                      <div style={{ flex: 1, minWidth: 0, paddingRight: '8px' }}>
                        <div className="pending-exam-name" style={{ fontSize: '13px', fontWeight: 'bold', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }} title={exam.name}>{exam.name}</div>
                        <div className="pending-exam-details" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                          {exam.subject} • {exam.questionsCount} Qs • {exam.duration} mins • {exam.totalMarks} Marks
                          <div style={{ marginTop: '2px', color: 'var(--warning)', fontWeight: 600, fontSize: '10.5px', display: 'flex', alignItems: 'center', gap: '3px' }}>
                            <Clock size={11} color="var(--warning)" />
                            <span>Starts: {exam.startAt ? new Date(exam.startAt).toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' }) : '—'}</span>
                          </div>
                        </div>
                      </div>
                      <button className="start-exam-small" disabled style={{ background: 'var(--text-faint)', color: 'var(--text-muted)', border: 'none', padding: '4px 10px', borderRadius: '20px', fontSize: '10.5px', fontWeight: 600, cursor: 'not-allowed', flexShrink: 0 }}>
                        Locked
                      </button>
                    </div>
                  ))}
                </>
              )}
            </div>
          )}
        </div>

        {/* Today's Study & Practice (Combined Card) */}
        {((exams.studyChips && exams.studyChips.length > 0) || (exams.dailyHomePractices && exams.dailyHomePractices.length > 0)) && (
          <div className="card card-cyan" style={{ 
            borderRadius: 'var(--radius)', 
            padding: '10px 12px', 
            marginBottom: '8px',
            boxShadow: 'var(--shadow-sm)'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <BookOpen size={18} color="var(--accent)" />
                <h3 style={{ fontSize: '14px', fontWeight: 800, margin: 0, color: 'var(--text)', whiteSpace: 'nowrap' }}>Today's Study & Practice</h3>
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              {/* Part 1: Learning Material */}
              {exams.studyChips && exams.studyChips.map((chip: any) => (
                <div key={chip.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', paddingBottom: exams.dailyHomePractices?.length ? '8px' : '0', borderBottom: exams.dailyHomePractices?.length ? '1px dashed var(--border-light)' : 'none' }}>
                  <div style={{ flex: '1 1 240px' }}>
                    <div style={{ fontWeight: 800, fontSize: '12.5px', lineHeight: 1.3, color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                      <BookOpen size={15} color="var(--accent)" style={{ flexShrink: 0 }} />
                      <span>{chip.isTomorrow ? "Tomorrow's Study Sheet" : (chip.dayName ? `${chip.dayName} Study Sheet` : "Today's Study Sheet")} — {chip.topics && chip.topics.length > 0 ? chip.topics.join(', ') : chip.chapterName}</span>
                    </div>
                    <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '1px' }}>
                      {chip.subject} • <strong>{chip.totalQuestions} Questions</strong>
                      {chip.isTomorrow && (
                        <span className="badge" style={{ background: 'var(--success-bg)', color: 'var(--success)', border: '1px solid rgba(52, 211, 153, 0.3)', marginLeft: '6px', padding: '1px 5px', borderRadius: '4px', fontSize: '9px', fontWeight: 700 }}>Early Access</span>
                      )}
                    </div>
                  </div>
                  <button 
                    className="btn btn-primary btn-sm"
                    onClick={() => router.push('/student/learning')}
                    style={{ padding: '4px 10px', fontSize: '10.5px', fontWeight: 700, whiteSpace: 'nowrap' }}
                  >
                    📖 Open Study Sheet
                  </button>
                </div>
              ))}

              {/* Part 2: Practice Test */}
              {exams.dailyHomePractices && exams.dailyHomePractices.map((hp: any) => {
                const isMathHP = /math|algebra|geometry|ganit/i.test(hp.subject || '');
                const unlockTimeStr = isMathHP ? "5:00 AM" : "8:30 PM";
                return (
                  <div key={hp.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                    <div style={{ flex: '1 1 240px' }}>
                      <div style={{ fontWeight: 800, fontSize: '12.5px', lineHeight: 1.3, color: 'var(--text)' }}>
                        ✍️ {hp.dayName ? `${hp.dayName} Practice Sheet` : "Daily Practice Sheet"} {!hp.isActive && (
                          hp.isExpired ? (
                            <span style={{ color: 'var(--text-muted)', fontSize: '9.5px', fontWeight: 'normal', marginLeft: '4px' }}>⏳ (Closed)</span>
                          ) : (
                            <span style={{ color: 'var(--warning)', fontSize: '9.5px', fontWeight: 'normal', marginLeft: '4px' }}>⏳ (Starts at {unlockTimeStr})</span>
                          )
                        )}
                      </div>
                      <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '1px' }}>
                        {hp.subject} • <strong>{hp.totalMarks} Marks</strong> ({hp.totalQuestions} Questions)
                      </div>
                    </div>

                    {hp.isActive ? (
                      <button 
                        className="btn btn-primary btn-sm"
                        onClick={() => router.push(`/student/take-subjective-exam?examId=${encodeURIComponent(hp.id)}`)}
                        style={{ padding: '4px 10px', fontSize: '10.5px', fontWeight: 700, whiteSpace: 'nowrap' }}
                      >
                        Start Test
                      </button>
                    ) : (
                      <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                        {hp.isExpired ? (
                          <>
                            <span className="badge" style={{ background: 'var(--text-faint)', color: 'var(--text-muted)', padding: '2px 6px', borderRadius: '4px', fontSize: '9.5px', fontWeight: 700 }}>Closed</span>
                            <button 
                              className="btn btn-secondary btn-sm"
                              disabled
                              style={{ padding: '4px 8px', fontSize: '10.5px', fontWeight: 700, cursor: 'not-allowed', opacity: 0.6, whiteSpace: 'nowrap' }}
                            >
                              🔒 Closed
                            </button>
                          </>
                        ) : (
                          <>
                            <span className="badge" style={{ background: 'var(--warning)', color: 'white', padding: '2px 6px', borderRadius: '4px', fontSize: '9.5px', fontWeight: 700 }}>Upcoming</span>
                            <button 
                              className="btn btn-secondary btn-sm"
                              disabled
                              style={{ padding: '4px 8px', fontSize: '10.5px', fontWeight: 700, cursor: 'not-allowed', opacity: 0.6, whiteSpace: 'nowrap' }}
                            >
                              🔒 Unlocks at {unlockTimeStr}
                            </button>
                          </>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        )}

            {/* Student Dashboard Footer with Account Status & Log Out */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '14px 16px',
              marginTop: '16px',
              borderTop: '1px solid var(--border-light)',
              borderRadius: 'var(--radius)',
              background: 'var(--surface-2)',
              gap: '12px',
              flexWrap: 'wrap'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '12.5px', color: 'var(--text-muted)' }}>
                <span>Signed in as <strong style={{ color: 'var(--text)' }}>{profile?.name || user?.name || 'Student'}</strong></span>
              </div>
              <button
                onClick={logout}
                className="btn btn-secondary"
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  fontSize: '12px',
                  fontWeight: 600,
                  color: 'var(--danger)',
                  borderColor: 'var(--danger-border, rgba(239, 68, 68, 0.3))',
                  padding: '6px 14px'
                }}
              >
                <LogOut size={14} />
                <span>Log Out</span>
              </button>
            </div>

          </>
        )}
      </div>
      {/* Dismissible Overdue Fees Overlay */}
      <OverdueFeeModal
        isOpen={Boolean(feeRecord?.hasOverdueInstallment && !dismissedOverdue)}
        onDismiss={() => setDismissedOverdue(true)}
        outstandingAmount={feeRecord?.outstandingAmount || 0}
        role="student"
      />

      {/* Important Notices Fullscreen Overlay */}
      <NoticeOverlayModal
        notice={activeOverlayNotice}
        onDismiss={handleDismissOverlayNotice}
        role="student"
      />

      {activeReflectionExam && (
        <StudentSelfReflectionModal
          examId={activeReflectionExam.examId}
          examName={activeReflectionExam.examName}
          onClose={() => setActiveReflectionExam(null)}
          onSuccess={() => {
            setActiveReflectionExam(null);
            if (typeof window !== 'undefined') {
              window.location.reload();
            }
          }}
        />
      )}
    </div>
  );
}
