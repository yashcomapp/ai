'use client';

import React, { useState, useEffect, useRef } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { t } from '@/lib/i18n';
import { useRouter } from 'next/navigation';
import useSWR from 'swr';
import { fetchWithToken } from '@/lib/swrFetcher';
import { collection, query, orderBy, limit, onSnapshot } from 'firebase/firestore';
import { db } from '@/lib/firebase/firestore';
import TopBarTimeTracker from '@/components/TopBarTimeTracker';
import { 
  TrendingUp, 
  AlertTriangle, 
  CheckCircle, 
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
  Award,
  Sparkles
} from 'lucide-react';
import { getScoreColor } from '@/lib/dashboardMetrics';

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
  const { theme, toggleTheme } = useTheme();
  const router = useRouter();

  const [examTab, setExamTab] = useState<'objective' | 'subjective' | 'mock'>('objective');
  const [timeFilter, setTimeFilter] = useState<'overall' | 'month' | 'week'>('overall');
  const [notices, setNotices] = useState<{ id: string; title: string; body: string; createdAt: string | null; isOverlay?: boolean; type?: string; noticeDate?: string | null }[]>([]);
  const [seenNoticeIds, setSeenNoticeIds] = useState<string[]>([]);
  const [showSeenNotices, setShowSeenNotices] = useState(false);
  const [isAnnouncementsExpanded, setIsAnnouncementsExpanded] = useState(false);
  const [activeOverlayNotice, setActiveOverlayNotice] = useState<any | null>(null);

  const handleDismissOverlayNotice = async (noticeId: string) => {
    const userId = firebaseUser?.uid || 'student';
    const dismissedStored = localStorage.getItem(`yc_dismissed_overlays_${userId}`);
    let dismissedIds: string[] = [];
    if (dismissedStored) {
      try {
        dismissedIds = JSON.parse(dismissedStored);
      } catch (e) {}
    }
    if (!dismissedIds.includes(noticeId)) {
      dismissedIds.push(noticeId);
      localStorage.setItem(`yc_dismissed_overlays_${userId}`, JSON.stringify(dismissedIds));
    }
    
    // Mark as seen locally
    if (!seenNoticeIds.includes(noticeId)) {
      const updated = [...seenNoticeIds, noticeId];
      setSeenNoticeIds(updated);
      localStorage.setItem('yc_seenNotices', JSON.stringify(updated));
      window.dispatchEvent(new Event('yc_seen_notices_changed'));
    }
    
    // Call the seen API
    try {
      const token = await firebaseUser!.getIdToken();
      await fetch('/api/notices/seen', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ noticeId })
      });
    } catch (err) {
      console.warn('Failed to report notice seen status:', err);
    }
    
    // Check if there are other unread overlay notices and display them sequentially
    const nextOverlay = notices.find((n: any) => n.isOverlay && n.id !== noticeId && !dismissedIds.includes(n.id));
    if (nextOverlay) {
      setActiveOverlayNotice(nextOverlay);
    } else {
      setActiveOverlayNotice(null);
    }
  };

  useEffect(() => {
    try {
      const stored = localStorage.getItem('yc_seenNotices');
      if (stored) {
        setSeenNoticeIds(JSON.parse(stored));
      }
    } catch (e) {
      console.warn('Failed to load seen notices:', e);
    }
  }, []);

  useEffect(() => {
    if ((user as any)?.autonomous && examTab !== 'objective') {
      setExamTab('objective');
    }
  }, [user, examTab]);

  const handleMarkNoticeAsSeen = async (id: string) => {
    try {
      const updated = [...seenNoticeIds, id];
      setSeenNoticeIds(updated);
      localStorage.setItem('yc_seenNotices', JSON.stringify(updated));

      // Post to database seen logs
      if (firebaseUser) {
        const idToken = await firebaseUser.getIdToken();
        fetch('/api/notices/seen', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
          },
          body: JSON.stringify({ noticeId: id })
        }).catch(err => console.warn('Failed to report notice seen status:', err));
      }
    } catch (e) {
      console.warn('Failed to save seen notices:', e);
    }
  };

  const visibleNotices = notices.filter(n => !seenNoticeIds.includes(n.id));



  const fetcher = async (url: string) => {
    return fetchWithToken(url, firebaseUser);
  };

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

  const { data, error, isLoading } = useSWR<DashboardData>(
    firebaseUser ? '/api/student/dashboard' : null,
    fetcher,
    {
      revalidateOnFocus: false,
      dedupingInterval: 60000,
      keepPreviousData: true,
      fallbackData: initialData || localCache
    }
  );

  const { data: feesData } = useSWR<any>(
    firebaseUser ? '/api/student/fees' : null,
    fetcher
  );

  const { data: chatRoomsData } = useSWR<any>(
    firebaseUser ? '/api/chat' : null,
    fetcher,
    {
      revalidateOnFocus: false,
      dedupingInterval: 60000
    }
  );

  const { data: attendanceData } = useSWR<any>(
    firebaseUser ? '/api/student/attendance' : null,
    fetcher
  );

  const { data: learningData } = useSWR<any>(
    firebaseUser && !(user as any)?.autonomous ? '/api/student/learning' : null,
    fetcher,
    { revalidateOnFocus: false, dedupingInterval: 30000 }
  );

  const needAttentionTopics = learningData?.needsAttention || [];

  const [dismissedOverdue, setDismissedOverdue] = useState(false);

  useEffect(() => {
    if (data) {
      try {
        localStorage.setItem('yc_student_dashboard_cache', JSON.stringify(data));
      } catch (e) {
        console.warn('Failed to cache dashboard data:', e);
      }
    }
  }, [data]);

  useEffect(() => {
    if (!firebaseUser) return;

    let isMounted = true;
    const loadNotices = async () => {
      try {
        const token = await firebaseUser.getIdToken();
        const res = await fetch('/api/notices', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        if (res.ok) {
          const resData = await res.json();
          if (isMounted) {
            const filtered = resData.notices || [];
            setNotices(filtered);

            const userId = firebaseUser?.uid || 'student';
            const serverSeenIds = filtered.filter((n: any) => n.seen).map((n: any) => n.id);

            // Synchronize seen status from server
            const stored = localStorage.getItem('yc_seenNotices');
            let seenIds: string[] = [];
            if (stored) {
              try {
                seenIds = JSON.parse(stored);
              } catch (e) {}
            }
            const mergedSeen = Array.from(new Set([...seenIds, ...serverSeenIds]));
            const validSeenIds = mergedSeen.filter((id: string) => filtered.some((n: any) => n.id === id));
            localStorage.setItem('yc_seenNotices', JSON.stringify(validSeenIds));
            setSeenNoticeIds(validSeenIds);
            window.dispatchEvent(new Event('yc_seen_notices_changed'));

            // Check for overlay notices that are not dismissed yet
            const dismissedStored = localStorage.getItem(`yc_dismissed_overlays_${userId}`);
            let dismissedIds: string[] = [];
            if (dismissedStored) {
              try {
                dismissedIds = JSON.parse(dismissedStored);
              } catch (e) {}
            }
            // If seen on server, it should be dismissed in overlays as well
            const mergedDismissed = Array.from(new Set([...dismissedIds, ...serverSeenIds]));
            localStorage.setItem(`yc_dismissed_overlays_${userId}`, JSON.stringify(mergedDismissed));

            const activeOverlay = filtered.find((n: any) => n.isOverlay && !mergedDismissed.includes(n.id));
            if (activeOverlay) {
              setActiveOverlayNotice(activeOverlay);
            }
          }
        }
      } catch (err) {
        console.warn('Failed to fetch notices via API:', err);
      }
    };

    loadNotices();

    const handleSeenChange = () => {
      const stored = localStorage.getItem('yc_seenNotices');
      if (stored) {
        try {
          setSeenNoticeIds(JSON.parse(stored));
        } catch (e) {}
      }
    };
    window.addEventListener('yc_seen_notices_changed', handleSeenChange);

    return () => {
      isMounted = false;
      window.removeEventListener('yc_seen_notices_changed', handleSeenChange);
    };
  }, [firebaseUser]);

  const [mounted, setMounted] = useState(false);
  useEffect(() => {
    setMounted(true);
  }, []);

  const getGreeting = () => {
    if (!mounted) return 'Good Morning';
    const hour = new Date().getHours();
    if (hour < 12) return 'Good Morning';
    if (hour < 17) return 'Good Afternoon';
    return 'Good Evening';
  };

  const handleStartExam = (examId: string, isSubjective: boolean) => {
    if (isSubjective) {
      router.push(`/student/take-subjective-exam?examId=${examId}`);
    } else {
      router.push(`/student/take-exam?examId=${examId}`);
    }
  };

  const handleGoToPeerReview = (examId: string | null) => {
    if (examId) {
      router.push(`/student/take-subjective-exam?mode=peer-review&examId=${examId}`);
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

  const activeData = data || initialData || localCache;
  const profile = activeData?.profile;
  const resultsSummary = activeData?.resultsSummary;
  const peerReviews = activeData?.peerReviews || { count: 0, firstExamId: null };
  const exams = activeData?.exams || { pendingObjectiveExams: [], scheduledObjectiveExams: [], pendingSubjectiveExams: [], scheduledSubjectiveExams: [], dailyHomePractices: [], studyChips: [] };
  const greeting = getGreeting();
  const firstName = profile?.name ? profile.name.split(' ')[0] : '';

  return (
    <div className="page-wrapper" style={{
      background: 'var(--bg)',
      minHeight: '100vh'
    }}>
      <div className="dashboard-container" style={{ maxWidth: '1000px', margin: '0 auto', padding: '6px 12px 60px 12px' }}>
        {(!activeData && isLoading) || !profile ? (
          <>
            {renderStatsSkeleton()}
            {renderSectionSkeleton()}
          </>
        ) : (
          <>
            {/* CARD 1: Glance (Clean Minimal Card) */}
            <div className="card" style={{
              background: 'var(--surface)',
              border: '1px solid var(--border)',
              borderRadius: 'var(--radius)',
              padding: '16px 20px',
              marginBottom: '12px',
              boxShadow: 'var(--shadow-sm)',
              position: 'relative'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '14px', flexWrap: 'nowrap', gap: '8px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px', minWidth: '0', flexShrink: 0 }}>
                  <TrendingUp size={16} color="var(--accent)" />
                  <strong style={{ fontSize: '14px', color: 'var(--text)', fontWeight: 800, letterSpacing: '0.2px', whiteSpace: 'nowrap' }}>Glance</strong>
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
                    padding: '4px 10px',
                    borderRadius: 'var(--radius-pill)',
                    border: '1px solid var(--border)',
                    outline: 'none',
                    cursor: 'pointer',
                    width: 'auto',
                    minWidth: '95px',
                    maxWidth: '115px',
                    flexShrink: 0
                  }}
                >
                  <option value="overall" style={{ background: 'var(--surface-2)', color: 'var(--text)' }}>Overall</option>
                  <option value="month" style={{ background: 'var(--surface-2)', color: 'var(--text)' }}>This Month</option>
                  <option value="week" style={{ background: 'var(--surface-2)', color: 'var(--text)' }}>This Week</option>
                </select>
              </div>

              {/* 3 Stats Grid */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px', alignItems: 'center' }}>
                {/* Stat 1: Avg Exam Marks (Click opens results page) */}
                <div 
                  onClick={() => router.push('/student/results')}
                  style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', justifyContent: 'center', gap: '4px', cursor: 'pointer', transition: 'opacity 0.2s' }}
                  title="Click to view detailed exam results"
                >
                  <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--text)', lineHeight: 1 }}>
                    {resultsSummary?.examCount ? Math.round(resultsSummary.averageScore) : 0}%
                  </div>
                  <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', fontWeight: 600 }}>
                    Average Marks
                  </div>
                </div>

                {/* Stat 2: LQ Score */}
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', justifyContent: 'center', gap: '4px', borderLeft: '1px solid var(--border)', paddingLeft: '8px' }}>
                  <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--text)', lineHeight: 1 }}>
                    {Math.round(profile?.overallMastery || 0)}%
                  </div>
                  <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', fontWeight: 600 }}>
                    LQ Score
                  </div>
                </div>

                {/* Stat 3: Efforts % */}
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', justifyContent: 'center', gap: '4px', borderLeft: '1px solid var(--border)', paddingLeft: '8px' }}>
                  <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--text)', lineHeight: 1 }}>
                    {Math.round((profile as any)?.effortsPercent ?? Math.min(100, Math.round((((profile as any)?.practicesCompletedCount || 0) / Math.max(1, (profile as any)?.totalTopicsCount || 24)) * 100)))}%
                  </div>
                  <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', fontWeight: 600 }}>
                    Efforts %
                  </div>
                </div>
              </div>
            </div>

            {/* CARD 2: Compact Action Needed / All Clear Ledger */}
            <div style={{
              background: (needAttentionTopics.length > 0 || peerReviews.count > 0) ? 'var(--danger-bg)' : 'var(--success-bg)',
              border: (needAttentionTopics.length > 0 || peerReviews.count > 0) ? '1px solid rgba(239, 68, 68, 0.25)' : '1px solid rgba(16, 185, 129, 0.25)',
              borderRadius: 'var(--radius)',
              padding: '12px 16px',
              marginBottom: '12px',
              display: 'flex',
              flexDirection: 'column',
              gap: '10px'
            }}>
              {/* Compact Header */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <div style={{
                  width: '28px',
                  height: '28px',
                  borderRadius: '50%',
                  background: (needAttentionTopics.length > 0 || peerReviews.count > 0) ? 'rgba(239, 68, 68, 0.2)' : 'rgba(16, 185, 129, 0.2)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  color: (needAttentionTopics.length > 0 || peerReviews.count > 0) ? 'var(--danger)' : '#10b981',
                  flexShrink: 0
                }}>
                  {(needAttentionTopics.length > 0 || peerReviews.count > 0) ? <AlertTriangle size={15} /> : <CheckCircle size={15} color="#10b981" />}
                </div>
                <h3 style={{ margin: 0, fontSize: '13.5px', fontWeight: 700, color: 'var(--text)' }}>
                  {(needAttentionTopics.length > 0 || peerReviews.count > 0) 
                    ? `${needAttentionTopics.length + (peerReviews.count > 0 ? 1 : 0)} Action Item(s) Need Attention` 
                    : 'All Clear!'}
                </h3>
              </div>

              {/* Peer Review Alert */}
              {peerReviews.count > 0 && (
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', background: 'var(--surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border)' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <ClipboardList size={16} color="var(--danger)" />
                    <div style={{ fontWeight: 600, fontSize: '12.5px', color: 'var(--text)' }}>Peer Paper Review Pending</div>
                  </div>
                  <button 
                    className="btn btn-primary" 
                    style={{ padding: '4px 12px', fontSize: '11px', borderRadius: 'var(--radius-sm)' }}
                    onClick={() => handleGoToPeerReview(peerReviews.firstExamId)}
                  >
                    Grade Paper
                  </button>
                </div>
              )}

              {/* Need Attention Topics List */}
              {needAttentionTopics.length > 0 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                  {needAttentionTopics.slice(0, 4).map((t: any) => (
                    <div key={t.topicCode} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', background: 'var(--surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border)', gap: '10px' }}>
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '2px', flex: 1 }}>
                        <div style={{ fontWeight: 600, fontSize: '12.5px', color: 'var(--text)' }}>{t.topicName}</div>
                        <div style={{ fontSize: '11px', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                          <span>{t.subjectName || 'General'}</span>
                          <span>•</span>
                          {t.isAbsentExam ? (
                            <span style={{ color: 'var(--danger)', fontWeight: 600 }}>Missed Exam</span>
                          ) : (
                            <span style={{ color: 'var(--warning)', fontWeight: 600 }}>{t.mastery || 0}% Mastery</span>
                          )}
                        </div>
                      </div>
                      <button 
                        className="btn btn-primary" 
                        style={{ padding: '4px 12px', fontSize: '11px', fontWeight: 600, borderRadius: 'var(--radius-sm)' }}
                        onClick={() => router.push(`/student/topic?topicCode=${t.topicCode}&category=needsAttention`)}
                      >
                        Start Practice
                      </button>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* CARD 3: Quick Navigation Hotspot Grid (Clean Professional Colorful Grid) */}
            <div className="card" style={{
              background: 'var(--surface)',
              border: '1px solid var(--border)',
              borderRadius: 'var(--radius)',
              padding: '16px 20px',
              marginBottom: '16px',
              boxShadow: 'var(--shadow-sm)',
              display: 'flex',
              flexDirection: 'column',
              gap: '12px'
            }}>
              <h3 style={{ margin: 0, fontSize: '13.5px', fontWeight: 700, color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Rocket size={16} color="#f472b6" /> Quick Navigation
              </h3>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '10px' }}>
                {/* Hotspot 1: Learn OS */}
                <div 
                  onClick={() => router.push('/student/learning')}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    padding: '14px 8px',
                    background: 'var(--surface-2)',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    textAlign: 'center',
                    gap: '8px',
                    transition: 'all 0.2s ease'
                  }}
                  onMouseEnter={(e) => { e.currentTarget.style.borderColor = '#818cf8'; e.currentTarget.style.transform = 'translateY(-1px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                >
                  <div style={{ width: '40px', height: '40px', borderRadius: '12px', background: 'rgba(99, 102, 241, 0.15)', border: '1px solid rgba(99, 102, 241, 0.35)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    <Dumbbell size={20} color="#818cf8" />
                  </div>
                  <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text)' }}>Learn OS</span>
                </div>

                {/* Hotspot 2: Attendance showing % */}
                <div 
                  onClick={() => router.push('/student/attendance')}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    padding: '14px 8px',
                    background: 'var(--surface-2)',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    textAlign: 'center',
                    gap: '8px',
                    transition: 'all 0.2s ease'
                  }}
                  onMouseEnter={(e) => { e.currentTarget.style.borderColor = '#34d399'; e.currentTarget.style.transform = 'translateY(-1px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                >
                  <div style={{ width: '40px', height: '40px', borderRadius: '12px', background: 'rgba(16, 185, 129, 0.15)', border: '1px solid rgba(16, 185, 129, 0.35)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    <Calendar size={20} color="#34d399" />
                  </div>
                  <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text)' }}>
                    Attendance ({attendanceData?.stats?.attendanceRate !== undefined ? `${attendanceData.stats.attendanceRate}%` : '100%'})
                  </span>
                </div>

                {/* Hotspot 3: Exam Register */}
                <div 
                  onClick={() => router.push('/exam-register')}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    padding: '14px 8px',
                    background: 'var(--surface-2)',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    textAlign: 'center',
                    gap: '8px',
                    transition: 'all 0.2s ease'
                  }}
                  onMouseEnter={(e) => { e.currentTarget.style.borderColor = '#fbbf24'; e.currentTarget.style.transform = 'translateY(-1px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                >
                  <div style={{ width: '40px', height: '40px', borderRadius: '12px', background: 'rgba(245, 158, 11, 0.15)', border: '1px solid rgba(245, 158, 11, 0.35)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    <ClipboardList size={20} color="#fbbf24" />
                  </div>
                  <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text)' }}>Exam Register</span>
                </div>

                {/* Hotspot 4: Live Chat */}
                <div 
                  onClick={() => router.push('/student/chat')}
                  style={{
                    position: 'relative',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    padding: '14px 8px',
                    background: 'var(--surface-2)',
                    border: '1px solid var(--border)',
                    borderRadius: 'var(--radius-sm)',
                    cursor: 'pointer',
                    textAlign: 'center',
                    gap: '8px',
                    transition: 'all 0.2s ease'
                  }}
                  onMouseEnter={(e) => { e.currentTarget.style.borderColor = '#22d3ee'; e.currentTarget.style.transform = 'translateY(-1px)'; }}
                  onMouseLeave={(e) => { e.currentTarget.style.borderColor = 'var(--border)'; e.currentTarget.style.transform = 'translateY(0)'; }}
                >
                  <div style={{ width: '40px', height: '40px', borderRadius: '12px', background: 'rgba(6, 182, 212, 0.15)', border: '1px solid rgba(6, 182, 212, 0.35)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    <MessageSquare size={20} color="#22d3ee" />
                  </div>
                  <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text)' }}>
                    Live Chat
                  </span>
                  {((chatRoomsData?.rooms || []).reduce((sum: number, r: any) => sum + (r.unreadCounts?.[(user as any)?.studentCode || ''] || 0), 0)) > 0 && (
                    <span style={{ position: 'absolute', top: '6px', right: '6px', background: 'var(--danger)', color: '#fff', fontSize: '10px', fontWeight: 700, padding: '2px 6px', borderRadius: '10px' }}>
                      {(chatRoomsData?.rooms || []).reduce((sum: number, r: any) => sum + (r.unreadCounts?.[(user as any)?.studentCode || ''] || 0), 0)}
                    </span>
                  )}
                </div>
              </div>
            </div>
        {/* ROW 2: Exams & Review Card (Full Width) */}
        <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden', marginBottom: '16px', minHeight: '240px' }}>
          <div className="exams-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 16px', borderBottom: '1px solid var(--border-light)' }}>
            <h3 style={{ fontSize: '14px', fontWeight: 'bold', color: 'var(--text)' }}>📝 Exams & Review</h3>
            <div className="review-badge" style={{ background: 'var(--danger)', color: 'white', padding: '2px 8px', borderRadius: '30px', fontSize: '11px', fontWeight: 700, cursor: 'pointer' }}>
              Pending: {resultsSummary?.pendingReviewCount || 0}
            </div>
          </div>

          {/* Peer Review Container */}
          {peerReviews.count > 0 && (
            <div className="peer-review-link-container" style={{ display: 'block', padding: '8px 16px', borderBottom: '1px solid var(--border-light)', background: 'var(--success-bg)' }}>
              <a className="peer-review-link" onClick={() => handleGoToPeerReview(peerReviews.firstExamId)} style={{ display: 'inline-block', color: 'var(--success)', fontSize: '12px', fontWeight: 600, textDecoration: 'none', cursor: 'pointer' }}>
                🔄 Peer Review Pending <span className="badge" style={{ background: 'var(--danger)', color: 'white', borderRadius: '50%', padding: '2px 6px', fontSize: '10px', marginLeft: '6px' }}>{peerReviews.count}</span>
              </a>
              <span className="peer-review-sub" style={{ fontSize: '11px', color: 'var(--text-muted)', marginLeft: '8px' }}>Review your classmate's paper</span>
            </div>
          )}

          {/* Exam Tabs */}
          {(user as any)?.autonomous !== true ? (
            <div className="exam-tabs" style={{ display: 'flex', borderBottom: '1px solid var(--border-light)', background: 'var(--bg-soft)' }}>
              <div 
                className={`exam-tab ${examTab === 'objective' ? 'active' : ''}`} 
                onClick={() => setExamTab('objective')}
                style={{ flex: 1, textAlign: 'center', padding: '10px 0', fontSize: '12.5px', fontWeight: 700, cursor: 'pointer', borderBottom: examTab === 'objective' ? '2.5px solid #38bdf8' : 'none', color: examTab === 'objective' ? 'var(--text)' : 'var(--text-muted)' }}
              >
                📋 Objective <span className="tab-count" style={{ background: examTab === 'objective' ? '#0284c7' : 'var(--surface-3)', color: 'white', borderRadius: '10px', padding: '2px 7px', fontSize: '10.5px', fontWeight: 700, marginLeft: '4px' }}>{exams.pendingObjectiveExams.length + exams.scheduledObjectiveExams.length}</span>
              </div>
              <div 
                className={`exam-tab ${examTab === 'subjective' ? 'active' : ''}`} 
                onClick={() => setExamTab('subjective')}
                style={{ flex: 1, textAlign: 'center', padding: '10px 0', fontSize: '12.5px', fontWeight: 700, cursor: 'pointer', borderBottom: examTab === 'subjective' ? '2.5px solid #a78bfa' : 'none', color: examTab === 'subjective' ? 'var(--text)' : 'var(--text-muted)' }}
              >
                📝 Subjective <span className="tab-count" style={{ background: examTab === 'subjective' ? '#7c3aed' : 'var(--surface-3)', color: 'white', borderRadius: '10px', padding: '2px 7px', fontSize: '10.5px', fontWeight: 700, marginLeft: '4px' }}>{exams.pendingSubjectiveExams.length + exams.scheduledSubjectiveExams.length}</span>
              </div>
              <div 
                className={`exam-tab ${examTab === 'mock' ? 'active' : ''}`} 
                onClick={() => setExamTab('mock')}
                style={{ flex: 1, textAlign: 'center', padding: '10px 0', fontSize: '12.5px', fontWeight: 700, cursor: 'pointer', borderBottom: examTab === 'mock' ? '2.5px solid #fbbf24' : 'none', color: examTab === 'mock' ? 'var(--text)' : 'var(--text-muted)' }}
              >
                🏆 Mock <span className="tab-count" style={{ background: examTab === 'mock' ? '#d97706' : 'var(--surface-3)', color: 'white', borderRadius: '10px', padding: '2px 7px', fontSize: '10.5px', fontWeight: 700, marginLeft: '4px' }}>{(exams.pendingEntranceExams?.length || 0) + (exams.scheduledEntranceExams?.length || 0)}</span>
              </div>
            </div>
          ) : null}

          {/* Objective Exams List */}
          {examTab === 'objective' && (
            <div className="pending-exams-flex-list" style={{ display: 'flex', flexDirection: 'column', padding: '10px 16px', maxHeight: '350px', overflowY: 'auto', gap: '6px' }}>
              {exams.pendingObjectiveExams.length === 0 && exams.scheduledObjectiveExams.length === 0 ? (
                <div className="no-exams" style={{ textAlign: 'center', color: 'var(--text-faint)', padding: '20px 0' }}>No pending objective exams</div>
              ) : (
                <>
                  {exams.pendingObjectiveExams.map((exam) => (
                    <div key={exam.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 12px', background: 'var(--bg-soft)', borderRadius: '8px', border: '1px solid var(--border-light)' }}>
                      <div style={{ flex: 1, minWidth: 0, paddingRight: '12px' }}>
                        <div className="pending-exam-name" style={{ fontSize: '13px', fontWeight: 'bold', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }} title={exam.name}>{exam.name}</div>
                        <div className="pending-exam-details" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                          {exam.subject} • {exam.questionsCount} Qs • {exam.duration} mins • {exam.totalMarks} Marks
                        </div>
                      </div>
                      <button className="start-exam-small" onClick={() => handleStartExam(exam.id, false)} style={{ background: 'var(--accent-grad)', color: 'white', border: 'none', padding: '6px 14px', borderRadius: '30px', fontSize: '11px', fontWeight: 600, cursor: 'pointer', flexShrink: 0 }}>
                        Start
                      </button>
                    </div>
                  ))}
                  {exams.scheduledObjectiveExams.map((exam) => (
                    <div key={exam.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 12px', background: 'var(--bg-soft)', borderRadius: '8px', border: '1px solid var(--border-light)', opacity: 0.8 }}>
                      <div style={{ flex: 1, minWidth: 0, paddingRight: '12px' }}>
                        <div className="pending-exam-name" style={{ fontSize: '13px', fontWeight: 'bold', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }} title={exam.name}>{exam.name}</div>
                        <div className="pending-exam-details" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                          {exam.subject} • {exam.questionsCount} Qs • {exam.duration} mins • {exam.totalMarks} Marks
                          <div style={{ marginTop: '3px', color: 'var(--warning)', fontWeight: 600, fontSize: '10px' }}>
                            📅 Starts: {exam.startAt ? new Date(exam.startAt).toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' }) : '—'}
                          </div>
                        </div>
                      </div>
                      <button className="start-exam-small" disabled style={{ background: 'var(--text-faint)', color: 'var(--text-muted)', border: 'none', padding: '6px 14px', borderRadius: '30px', fontSize: '11px', fontWeight: 600, cursor: 'not-allowed', flexShrink: 0 }}>
                        Locked
                      </button>
                    </div>
                  ))}
                </>
              )}
            </div>
          )}

          {/* Subjective Exams List */}
          {examTab === 'subjective' && (
            <div className="pending-exams-flex-list" style={{ display: 'flex', flexDirection: 'column', padding: '10px 16px', maxHeight: '350px', overflowY: 'auto', gap: '6px' }}>
              {exams.pendingSubjectiveExams.length === 0 && exams.scheduledSubjectiveExams.length === 0 ? (
                <div className="no-exams" style={{ textAlign: 'center', color: 'var(--text-faint)', padding: '20px 0' }}>No pending subjective exams</div>
              ) : (
                <>
                  {exams.pendingSubjectiveExams.map((exam) => (
                    <div key={exam.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 12px', background: 'var(--bg-soft)', borderRadius: '8px', border: '1px solid var(--border-light)' }}>
                      <div style={{ flex: 1, minWidth: 0, paddingRight: '12px' }}>
                        <div className="pending-exam-name" style={{ fontSize: '13px', fontWeight: 'bold', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }} title={exam.name}>{exam.name}</div>
                        <div className="pending-exam-details" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                          {exam.subject} • {exam.questionsCount} Qs • {exam.totalTime} mins • {exam.totalMarks} Marks • Mode: {exam.mode}
                        </div>
                      </div>
                      <button className="start-exam-small subjective" onClick={() => handleStartExam(exam.id, true)} style={{ background: 'var(--accent-grad)', color: 'white', border: 'none', padding: '6px 14px', borderRadius: '30px', fontSize: '11px', fontWeight: 600, cursor: 'pointer', flexShrink: 0 }}>
                        Start
                      </button>
                    </div>
                  ))}
                  {exams.scheduledSubjectiveExams.map((exam) => (
                    <div key={exam.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 12px', background: 'var(--bg-soft)', borderRadius: '8px', border: '1px solid var(--border-light)', opacity: 0.8 }}>
                      <div style={{ flex: 1, minWidth: 0, paddingRight: '12px' }}>
                        <div className="pending-exam-name" style={{ fontSize: '13px', fontWeight: 'bold', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }} title={exam.name}>{exam.name}</div>
                        <div className="pending-exam-details" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                          {exam.subject} • {exam.questionsCount} Qs • {exam.totalTime} mins • {exam.totalMarks} Marks • Mode: {exam.mode}
                          <div style={{ marginTop: '3px', color: 'var(--warning)', fontWeight: 600, fontSize: '10px' }}>
                            📅 Starts: {exam.startAt ? new Date(exam.startAt).toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' }) : '—'}
                          </div>
                        </div>
                      </div>
                      <button className="start-exam-small subjective" disabled style={{ background: 'var(--text-faint)', color: 'var(--text-muted)', border: 'none', padding: '6px 14px', borderRadius: '30px', fontSize: '11px', fontWeight: 600, cursor: 'not-allowed', flexShrink: 0 }}>
                        Locked
                      </button>
                    </div>
                  ))}
                </>
              )}
            </div>
          )}

          {/* Mock Exams List */}
          {examTab === 'mock' && (
            <div className="pending-exams-flex-list" style={{ display: 'flex', flexDirection: 'column', padding: '10px 16px', maxHeight: '350px', overflowY: 'auto', gap: '6px' }}>
              {(exams.pendingEntranceExams?.length || 0) === 0 && (exams.scheduledEntranceExams?.length || 0) === 0 ? (
                <div className="no-exams" style={{ textAlign: 'center', color: 'var(--text-faint)', padding: '20px 0' }}>No pending mock exams</div>
              ) : (
                <>
                  {(exams.pendingEntranceExams || []).map((exam) => (
                    <div key={exam.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 12px', background: 'var(--bg-soft)', borderRadius: '8px', border: '1px solid var(--border-light)' }}>
                      <div style={{ flex: 1, minWidth: 0, paddingRight: '12px' }}>
                        <div className="pending-exam-name" style={{ fontSize: '13px', fontWeight: 'bold', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }} title={exam.name}>{exam.name}</div>
                        <div className="pending-exam-details" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                          {exam.subject} • {exam.questionsCount} Qs • {exam.duration} mins • {exam.totalMarks} Marks
                        </div>
                      </div>
                      <button className="start-exam-small" onClick={() => handleStartExam(exam.id, false)} style={{ background: 'var(--accent-grad)', color: 'white', border: 'none', padding: '6px 14px', borderRadius: '30px', fontSize: '11px', fontWeight: 600, cursor: 'pointer', flexShrink: 0 }}>
                        Start
                      </button>
                    </div>
                  ))}
                  {(exams.scheduledEntranceExams || []).map((exam) => (
                    <div key={exam.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 12px', background: 'var(--bg-soft)', borderRadius: '8px', border: '1px solid var(--border-light)', opacity: 0.8 }}>
                      <div style={{ flex: 1, minWidth: 0, paddingRight: '12px' }}>
                        <div className="pending-exam-name" style={{ fontSize: '13px', fontWeight: 'bold', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }} title={exam.name}>{exam.name}</div>
                        <div className="pending-exam-details" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                          {exam.subject} • {exam.questionsCount} Qs • {exam.duration} mins • {exam.totalMarks} Marks
                          <div style={{ marginTop: '3px', color: 'var(--warning)', fontWeight: 600, fontSize: '10px' }}>
                            📅 Starts: {exam.startAt ? new Date(exam.startAt).toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' }) : '—'}
                          </div>
                        </div>
                      </div>
                      <button className="start-exam-small" disabled style={{ background: 'var(--text-faint)', color: 'var(--text-muted)', border: 'none', padding: '6px 14px', borderRadius: '30px', fontSize: '11px', fontWeight: 600, cursor: 'not-allowed', flexShrink: 0 }}>
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
          <div className="card" style={{ 
            background: 'var(--surface)', 
            borderRadius: 'var(--radius-lg)', 
            border: '2px solid var(--accent)', 
            padding: '12px 16px', 
            marginBottom: '16px',
            boxShadow: 'var(--shadow-sm)'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px' }}>
              <div>
                <h3 style={{ fontSize: '14px', fontWeight: 800, margin: 0, color: 'var(--accent)', whiteSpace: 'nowrap' }}>📚 Today's Study & Practice</h3>
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {/* Part 1: Learning Material */}
              {exams.studyChips && exams.studyChips.map((chip: any) => (
                <div key={chip.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px', paddingBottom: exams.dailyHomePractices?.length ? '12px' : '0', borderBottom: exams.dailyHomePractices?.length ? '1px dashed var(--border-light)' : 'none' }}>
                  <div style={{ flex: '1 1 280px' }}>
                    <div style={{ fontWeight: 800, fontSize: '13px', lineHeight: 1.3, color: 'var(--text)' }}>
                      📖 {chip.isTomorrow ? "Tomorrow's Study Sheet" : (chip.dayName ? `${chip.dayName} Study Sheet` : "Today's Study Sheet")} — {chip.topics && chip.topics.length > 0 ? chip.topics.join(', ') : chip.chapterName}
                    </div>
                    <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>
                      {chip.subject} • <strong>{chip.totalQuestions} Questions</strong>
                      {chip.isTomorrow && (
                        <span className="badge" style={{ background: '#22c55e', color: 'white', marginLeft: '8px', padding: '2px 6px', borderRadius: '4px', fontSize: '9px', fontWeight: 700 }}>Early Access</span>
                      )}
                    </div>
                  </div>
                  <button 
                    className="btn btn-success btn-sm"
                    onClick={async () => {
                      const customChip = {
                        ...chip,
                        name: `${chip.isTomorrow ? "Tomorrow's Study Sheet" : (chip.dayName ? `${chip.dayName} Study Sheet` : "Daily Study Sheet")} — ${chip.topics && chip.topics.length > 0 ? chip.topics.join(', ') : chip.chapterName}`,
                        chapterName: chip.topics && chip.topics.length > 0 ? chip.topics.join(', ') : chip.chapterName
                      };
                      try {
                        const { exportPasswordProtectedLearningPDF } = await import('@/lib/pdfExport');
                        await exportPasswordProtectedLearningPDF(customChip, chip.questions);
                      } catch (err: any) {
                        alert('Failed to generate protected PDF: ' + err.message);
                      }
                    }}
                    style={{ padding: '5px 12px', fontSize: '11px', fontWeight: 700, whiteSpace: 'nowrap' }}
                  >
                    🔒 Download PDF
                  </button>
                </div>
              ))}

              {/* Part 2: Practice Test */}
              {exams.dailyHomePractices && exams.dailyHomePractices.map((hp: any) => {
                const isMathHP = /math|algebra|geometry|ganit/i.test(hp.subject || '');
                const unlockTimeStr = isMathHP ? "5:00 AM" : "8:30 PM";
                return (
                  <div key={hp.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
                    <div style={{ flex: '1 1 280px' }}>
                      <div style={{ fontWeight: 800, fontSize: '13px', lineHeight: 1.3, color: 'var(--text)' }}>
                        ✍️ {hp.dayName ? `${hp.dayName} Practice Sheet` : "Daily Practice Sheet"} {!hp.isActive && (
                          hp.isExpired ? (
                            <span style={{ color: 'var(--text-muted)', fontSize: '10px', fontWeight: 'normal', marginLeft: '4px' }}>⏳ (Closed)</span>
                          ) : (
                            <span style={{ color: 'var(--warning)', fontSize: '10px', fontWeight: 'normal', marginLeft: '4px' }}>⏳ (Starts at {unlockTimeStr})</span>
                          )
                        )}
                      </div>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>
                        {hp.subject} • <strong>{hp.totalMarks} Marks</strong> ({hp.totalQuestions} Questions)
                      </div>
                    </div>

                    {hp.isActive ? (
                      <button 
                        className="btn btn-primary btn-sm"
                        onClick={() => router.push(`/student/take-subjective-exam?examId=${hp.id}`)}
                        style={{ padding: '5px 12px', fontSize: '11px', fontWeight: 700, whiteSpace: 'nowrap' }}
                      >
                        Start Test
                      </button>
                    ) : (
                      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                        {hp.isExpired ? (
                          <>
                            <span className="badge" style={{ background: 'var(--text-faint)', color: 'var(--text-muted)', padding: '4px 8px', borderRadius: '4px', fontSize: '10px', fontWeight: 700 }}>Closed</span>
                            <button 
                              className="btn btn-secondary btn-sm"
                              disabled
                              style={{ padding: '5px 12px', fontSize: '11px', fontWeight: 700, cursor: 'not-allowed', opacity: 0.6, whiteSpace: 'nowrap' }}
                            >
                              🔒 Closed
                            </button>
                          </>
                        ) : (
                          <>
                            <span className="badge" style={{ background: 'var(--warning)', color: 'white', padding: '4px 8px', borderRadius: '4px', fontSize: '10px', fontWeight: 700 }}>Upcoming</span>
                            <button 
                              className="btn btn-secondary btn-sm"
                              disabled
                              style={{ padding: '5px 12px', fontSize: '11px', fontWeight: 700, cursor: 'not-allowed', opacity: 0.6, whiteSpace: 'nowrap' }}
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


          </>
        )}
      </div>
      {/* Dismissible Overdue Fees Overlay */}
      {feesData?.feeRecord?.hasOverdueInstallment && !dismissedOverdue && (
        <div style={{
          position: 'fixed',
          inset: 0,
          background: 'rgba(0, 0, 0, 0.45)',
          backdropFilter: 'blur(8px)',
          WebkitBackdropFilter: 'blur(8px)',
          zIndex: 99999,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '20px'
        }}>
          <div className="card" style={{
            background: 'var(--surface-popover)',
            border: '1px solid var(--border-popover)',
            borderRadius: 'var(--radius-lg)',
            padding: '28px',
            maxWidth: '500px',
            width: '100%',
            textAlign: 'center',
            boxShadow: 'var(--shadow-lg)'
          }}>
            <span style={{ fontSize: '3rem', display: 'block', marginBottom: '16px' }}>🪙</span>
            <h2 style={{ fontSize: '1.45rem', fontWeight: 800, color: 'var(--danger)', margin: '0 0 10px 0' }}>
              Fee Installment Overdue
            </h2>
            <p style={{ fontSize: '13px', color: 'var(--text)', lineHeight: '1.6', margin: '0 0 20px 0' }}>
              Your account has an outstanding overdue balance of <strong>₹{feesData?.feeRecord?.outstandingAmount}</strong>. Please check your dues schedule and complete payment.
            </p>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <button 
                className="btn btn-primary" 
                onClick={() => {
                  router.push('/student/fees');
                  setDismissedOverdue(true);
                }}
                style={{ width: '100%' }}
              >
                View Fees & Invoices
              </button>
              <button 
                className="btn btn-secondary" 
                onClick={() => setDismissedOverdue(true)}
                style={{ width: '100%' }}
              >
                Dismiss
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Important Notices Fullscreen Overlay */}
      {activeOverlayNotice && (() => {
        const type = activeOverlayNotice.type || 'general';
        const typeConfig = 
          type === 'schedule' 
            ? { title: '📅 CLASS SCHEDULE UPDATE', color: 'var(--accent)', bg: 'var(--accent-soft)', text: 'var(--accent)', icon: '📅' }
            : type === 'fees'
            ? { title: '💰 FEES REMINDER', color: '#f59e0b', bg: 'rgba(245, 158, 11, 0.15)', text: '#fbbf24', icon: '💰' }
            : type === 'exam_absent'
            ? { title: '🚨 EXAM ABSENCE ALERT', color: '#ef4444', bg: 'rgba(239, 68, 68, 0.15)', text: '#f87171', icon: '🚨' }
            : type === 'exam_excellent'
            ? { title: '🏆 EXCELLENT EXAM RESULT', color: '#10b981', bg: 'rgba(16, 185, 129, 0.15)', text: '#34d399', icon: '🏆' }
            : type === 'exam_good'
            ? { title: '🌟 EXAM RESULT ANNOUNCEMENT', color: 'var(--accent)', bg: 'var(--accent-soft)', text: 'var(--accent)', icon: '🌟' }
            : type === 'exam_needs_improvement'
            ? { title: '⚠️ EXAM RESULT - ATTENTION', color: '#f59e0b', bg: 'rgba(245, 158, 11, 0.15)', text: '#fbbf24', icon: '⚠️' }
            : { title: '📢 IMPORTANT ANNOUNCEMENT', color: '#ef4444', bg: 'rgba(239, 68, 68, 0.15)', text: '#f87171', icon: '📢' };
        
        return (
          <div style={{
            position: 'fixed',
            inset: 0,
            background: 'rgba(0, 0, 0, 0.5)',
            backdropFilter: 'blur(8px)',
            WebkitBackdropFilter: 'blur(8px)',
            zIndex: 999999,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '20px'
          }}>
            <div className="card" style={{
              background: 'var(--surface-popover)',
              border: `2px solid ${typeConfig.color}`,
              borderRadius: 'var(--radius-lg)',
              padding: '28px',
              maxWidth: '520px',
              width: '100%',
              maxHeight: '95%',
              display: 'flex',
              flexDirection: 'column',
              gap: '16px',
              boxShadow: 'var(--shadow-lg)',
              overflow: 'hidden'
            }}>
              <div style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '16px' }}>
                <span style={{ fontSize: '48px', margin: '4px 0 12px 0', display: 'block', lineHeight: 1 }}>
                  {typeConfig.icon}
                </span>
                <span style={{
                  fontSize: '11px',
                  background: typeConfig.bg,
                  color: typeConfig.text,
                  padding: '4px 10px',
                  borderRadius: '20px',
                  fontWeight: 800,
                  letterSpacing: '0.5px',
                  display: 'inline-block',
                  marginBottom: '12px'
                }}>
                  {typeConfig.title.replace(/^[^\s]+\s*/, '')}
                </span>
                <h2 style={{ fontSize: '1.75rem', fontWeight: 800, color: 'var(--text)', margin: 0, lineHeight: '1.3' }}>
                  {activeOverlayNotice.title}
                </h2>
              </div>
              
              <div style={{
                flex: 1,
                overflowY: 'auto',
                fontSize: '17px',
                lineHeight: '1.6',
                color: 'var(--text)',
                padding: '4px 8px 4px 0',
                whiteSpace: 'pre-line',
                wordBreak: 'break-word'
              }}>
                {type === 'schedule' && activeOverlayNotice.noticeDate && (
                  <div style={{
                    fontSize: '17px',
                    fontWeight: 700,
                    color: 'var(--accent)',
                    background: 'var(--accent-soft)',
                    padding: '8px 12px',
                    borderRadius: '6px',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    marginBottom: '14px',
                    border: '1px solid var(--accent-ring)'
                  }}>
                    <span>{(() => {
                      const d = new Date(activeOverlayNotice.noticeDate);
                      if (isNaN(d.getTime())) return activeOverlayNotice.noticeDate;
                      const day = String(d.getDate()).padStart(2, '0');
                      const month = String(d.getMonth() + 1).padStart(2, '0');
                      return `${day}/${month}/${d.getFullYear()}`;
                    })()}</span>
                  </div>
                )}
                <div 
                  style={{ lineHeight: '1.25', margin: '4px 0' }}
                  dangerouslySetInnerHTML={{
                    __html: (activeOverlayNotice.body || '')
                      .replace(/(<\/div>|<\/p>|<\/li>)\s*\r?\n/gi, '$1')
                      .replace(/\r?\n\s*(<div[^>]*>|<p[^>]*>|<ul[^>]*>|<ol[^>]*>|<li[^>]*>)/gi, '$1')
                      .replace(/\r?\n/g, '<br/>')
                  }}
                />
              </div>

              <div style={{ borderTop: '1px solid var(--border-light)', paddingTop: '16px', marginTop: '4px' }}>
                <button 
                  className="btn btn-primary" 
                  onClick={() => handleDismissOverlayNotice(activeOverlayNotice.id)}
                  style={{
                    width: '100%',
                    padding: '12px',
                    borderRadius: 'var(--radius-md)',
                    fontWeight: 'bold',
                    fontSize: '14px',
                    background: typeConfig.color,
                    color: '#ffffff',
                    border: 'none',
                    cursor: 'pointer'
                  }}
                >
                  I Understand & Dismiss
                </button>
              </div>
            </div>
          </div>
        );
      })()}
    </div>
  );
}
