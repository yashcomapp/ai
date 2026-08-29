'use client';

import React, { useEffect, useState, useRef } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import TopBarTimeTracker from '@/components/TopBarTimeTracker';
import useSWR from 'swr';
import { fetchWithToken } from '@/lib/swrFetcher';
import { collection, query, orderBy, limit, onSnapshot } from 'firebase/firestore';
import { db } from '@/lib/firebase/firestore';
import { useRouter } from 'next/navigation';
import { formatDateIST, formatDateTimeIST, formatDurationHM } from '@/lib/dateUtils';
import { usePushNotifications } from '@/hooks/usePushNotifications';
import { useLiveExam } from '@/hooks/useLiveExam';
import Image from 'next/image';
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
  Bell,
  Users,
  User,
  Check,
  ChevronRight,
  ShieldCheck,
  Sparkles,
  BarChart2
} from 'lucide-react';
import { getScoreColor } from '@/lib/dashboardMetrics';

interface Child {
  studentCode: string;
  name: string;
  uid: string;
  className?: string;
  batchName?: string;
}

interface ActivityItem {
  type: 'exam' | 'practice';
  id: string;
  name: string;
  score: number;
  date: string;
  subject: string;
  status: string;
}

interface ParentDashboardData {
  childInfo?: {
    uid: string;
    studentCode: string;
    name: string;
  };
  todayStats?: {
    todayMinutes: number;
    todayPracticeMinutes: number;
    todayExamMinutes: number;
    todaySessionsCount: number;
    todayQuestionsCount: number;
    todayAverageScore: number;
    streakDays: number;
  };
  topicDiagnostics?: {
    needsAttentionYesterdayCount: number;
    needsAttentionYesterdayTopics: string[];
    practicedTodayCount: number;
    practicedTodayTopics: string[];
    recoveredTodayCount: number;
    recoveredTodayTopics: string[];
    needsAttentionRemainingCount: number;
    needsAttentionRemainingTopics: string[];
  };
  snapshot?: {
    todaySeconds: number;
    weekSeconds: number;
    streakDays: number;
    avgScore: number;
    overallExamAverage?: number;
    objectiveAvgScore?: number;
    subjectiveAvgScore?: number;
    practiceAvgScore?: number;
    overallMastery?: number;
    lqScore?: number;
    effortsPercent?: number;
    practicesCompletedCount?: number;
    totalTopicsCount?: number;
    totalQuestionsPracticed?: number;
    totalSessions: number;
    integrityScore: number;
    needsAttentionCount: number;
    masteredTopicsCount?: number;
    absentExamsCount?: number;
  };
  recentActivity?: ActivityItem[];
  children: Child[];
  chartData?: any[];
  entranceResults?: any[];
}

interface ReviewItem {
  id: string;
  examId?: string;
  practiceId?: string;
  name: string;
  examName?: string;
  subject?: string;
  type: 'objective' | 'practice' | 'subjective' | 'entrance';
  date: string;
  scorePercent?: number;
  percentage?: number;
  status: 'pending' | 'approved';
  wrongCount?: number;
  unansweredCount?: number;
  correctCount?: number;
  durationSpent?: number;
  topicsCovered?: string[];
  submittedAt?: string;
  reviewedByActor?: string;
}

export default function ParentDashboardClient({ initialData: serverInitialData }: { initialData?: ParentDashboardData }) {
  const { user, firebaseUser, logout } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const router = useRouter();
  const { initFCM } = usePushNotifications();
  const [syncingPush, setSyncingPush] = useState(false);

  const defaultChildCode = serverInitialData?.childInfo?.studentCode || serverInitialData?.children?.[0]?.studentCode || '';
  const [selectedChildCode, setSelectedChildCode] = useState<string>(defaultChildCode);
  const [activeTab, setActiveTab] = useState<'pending' | 'approved'>('pending');
  const [activeModal, setActiveModal] = useState<string | null>(null);
  const [selectedReview, setSelectedReview] = useState<ReviewItem | null>(null);

  const [notices, setNotices] = useState<any[]>([]);
  const [seenNoticeIds, setSeenNoticeIds] = useState<string[]>([]);
  const [activeOverlayNotice, setActiveOverlayNotice] = useState<any | null>(null);
  const [absenceReason, setAbsenceReason] = useState<string>('');
  const [absenceRemarks, setAbsenceRemarks] = useState<string>('');
  const [timeFilter, setTimeFilter] = useState<'overall' | 'month' | 'week'>('overall');

  // Multi-actor verification selection
  const [actorPromptOpen, setActorPromptOpen] = useState(false);
  const [chosenActor, setChosenActor] = useState<'parent' | 'student'>('parent');
  const [approving, setApproving] = useState(false);

  // Themed Custom Dialogs
  const [showAlert, setShowAlert] = useState(false);
  const [alertTitle, setAlertTitle] = useState('');
  const [alertMsg, setAlertMsg] = useState('');
  
  const triggerAlert = (title: string, msg: string) => {
    setAlertTitle(title);
    setAlertMsg(msg);
    setShowAlert(true);
  };

  // Daily 5-Min Sync Ritual States
  const SYNC_TOTAL_SECONDS = 300; // 5 minutes mandatory
  const [dailySyncOpen, setDailySyncOpen] = useState(false);
  const [syncSecondsRemaining, setSyncSecondsRemaining] = useState<number>(SYNC_TOTAL_SECONDS);
  const [dailySyncStep, setDailySyncStep] = useState<1 | 2 | 3>(1);
  const [dailySyncFeedback, setDailySyncFeedback] = useState<'excellent' | 'good' | 'needs_attention'>('excellent');
  const [dailySyncCapturing, setDailySyncCapturing] = useState(false);
  const [dailySyncPhoto, setDailySyncPhoto] = useState<string | null>(null);
  const [dailySyncSubmitting, setDailySyncSubmitting] = useState(false);
  const [dailySyncDoneToday, setDailySyncDoneToday] = useState(false);

  // 5-minute mandatory countdown timer
  useEffect(() => {
    let interval: NodeJS.Timeout | null = null;
    if (dailySyncOpen && syncSecondsRemaining > 0) {
      interval = setInterval(() => {
        setSyncSecondsRemaining(prev => Math.max(0, prev - 1));
      }, 1000);
    }
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [dailySyncOpen, syncSecondsRemaining]);

  // Prevent browser window/tab close or reload during mandatory 5-min sync
  useEffect(() => {
    const handleBeforeUnload = (e: BeforeUnloadEvent) => {
      if (dailySyncOpen && syncSecondsRemaining > 0) {
        e.preventDefault();
        e.returnValue = 'A mandatory 5-minute Parent-Child Sync is in progress. Please complete the full 5 minutes before leaving.';
        return e.returnValue;
      }
    };
    window.addEventListener('beforeunload', handleBeforeUnload);
    return () => window.removeEventListener('beforeunload', handleBeforeUnload);
  }, [dailySyncOpen, syncSecondsRemaining]);

  const formatSyncTimer = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  };

  // Check if current IST time is in 9:30 PM - 10:30 PM slot
  const isSyncTimeSlot = () => {
    try {
      const nowIST = new Date(new Date().toLocaleString('en-US', { timeZone: 'Asia/Kolkata' }));
      const mins = nowIST.getHours() * 60 + nowIST.getMinutes();
      const start = 21 * 60 + 30; // 9:30 PM = 1290 mins
      const end = 22 * 60 + 30;   // 10:30 PM = 1350 mins
      return mins >= start && mins <= end;
    } catch (e) {
      return false;
    }
  };

  const syncVideoRef = useRef<HTMLVideoElement | null>(null);

  const effectiveSyncChildCode = selectedChildCode || (serverInitialData?.children && serverInitialData.children[0]?.studentCode) || serverInitialData?.childInfo?.studentCode || '';
  const activeSyncChild = (serverInitialData?.children || []).find((c: any) => c.studentCode === effectiveSyncChildCode)
    || serverInitialData?.childInfo;
  const syncStudentName = activeSyncChild?.name || 'Child';

  const {
    startCameraStream: startSyncLiveExam,
    stopCameraStream: stopSyncLiveExam,
    cameraStream: syncLiveStream,
    cameraStatus: syncCameraStatus
  } = useLiveExam({
    examId: `daily-sync-${effectiveSyncChildCode || 'child'}`,
    examName: `Daily 5-Min Parent-Child Sync (${syncStudentName})`,
    studentCode: effectiveSyncChildCode,
    studentName: syncStudentName,
    examType: 'sync' as any,
    totalQuestions: 3,
    currentQuestionIndex: dailySyncStep,
    answeredCount: dailySyncStep,
    cameraVideoRef: syncVideoRef,
    started: dailySyncOpen
  });

  // Automatically start live camera and broadcasting when sync container opens
  useEffect(() => {
    if (dailySyncOpen) {
      startSyncLiveExam().catch(err => console.warn('Failed to start sync live camera:', err));
    } else {
      stopSyncLiveExam();
    }
  }, [dailySyncOpen]);

  // Keep sync video element attached to live camera stream
  useEffect(() => {
    if (syncVideoRef.current && syncLiveStream && syncVideoRef.current.srcObject !== syncLiveStream) {
      syncVideoRef.current.srcObject = syncLiveStream;
      syncVideoRef.current.play().catch(() => {});
    }
  }, [syncLiveStream, dailySyncOpen]);

  const captureSyncSnapshot = async (): Promise<string | null> => {
    try {
      if (syncVideoRef.current && syncVideoRef.current.videoWidth) {
        const canvas = document.createElement('canvas');
        canvas.width = 320;
        canvas.height = 240;
        const ctx = canvas.getContext('2d');
        if (ctx) {
          ctx.drawImage(syncVideoRef.current, 0, 0, 320, 240);
          const dataUrl = canvas.toDataURL('image/jpeg', 0.65);
          setDailySyncPhoto(dataUrl);
          return dataUrl;
        }
      }

      if (typeof navigator === 'undefined' || !navigator.mediaDevices?.getUserMedia) return null;
      setDailySyncCapturing(true);
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { width: { ideal: 320 }, height: { ideal: 240 }, facingMode: 'user' },
        audio: false
      });
      const video = document.createElement('video');
      video.playsInline = true;
      video.muted = true;
      video.srcObject = stream;
      await video.play();

      await new Promise(res => setTimeout(res, 350));

      const canvas = document.createElement('canvas');
      canvas.width = 320;
      canvas.height = 240;
      const ctx = canvas.getContext('2d');
      if (ctx) {
        ctx.drawImage(video, 0, 0, 320, 240);
      }
      const dataUrl = canvas.toDataURL('image/jpeg', 0.65);
      stream.getTracks().forEach(t => t.stop());
      setDailySyncPhoto(dataUrl);
      setDailySyncCapturing(false);
      return dataUrl;
    } catch (e) {
      console.warn('Sync snapshot skipped:', e);
      setDailySyncCapturing(false);
      return null;
    }
  };

  const handleCompleteDailySync = async () => {
    if (!firebaseUser || !selectedChildCode || dailySyncSubmitting) return;
    setDailySyncSubmitting(true);
    try {
      let photo = dailySyncPhoto;
      if (!photo) {
        photo = await captureSyncSnapshot();
      }

      const idToken = await firebaseUser.getIdToken();
      await fetch('/api/parent/review', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          type: 'daily_5min_sync',
          reviewId: `daily-sync-${Date.now()}`,
          childStudentCode: selectedChildCode,
          reviewedByActor: 'parent',
          photoThumbnail: photo
        })
      });

      setDailySyncDoneToday(true);
      setDailySyncOpen(false);
      triggerAlert('🎉 Daily 5-Min Sync Completed!', 'Your daily parent-child review has been verified and recorded with photo proof.');
    } catch (err: any) {
      triggerAlert('Error', err.message || 'Failed to record daily sync');
    } finally {
      setDailySyncSubmitting(false);
    }
  };

  const renderChildSelectorSkeleton = () => (
    <div className="card skeleton-blink" style={{
      background: 'var(--surface)',
      border: '1px solid var(--border-light)',
      borderRadius: 'var(--radius)',
      padding: '12px 18px',
      marginBottom: '18px',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center'
    }}>
      <div style={{ width: '140px', height: '18px', background: 'var(--surface-2)', borderRadius: '4px' }}></div>
      <div style={{ width: '160px', height: '36px', background: 'var(--surface-2)', borderRadius: '24px' }}></div>
    </div>
  );

  const renderDailySyncSkeleton = () => (
    <div className="card skeleton-blink" style={{
      background: 'var(--surface)',
      border: '1px solid var(--border)',
      borderRadius: 'var(--radius)',
      padding: '14px 18px',
      marginBottom: '16px',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
        <div style={{ width: '38px', height: '38px', borderRadius: '50%', background: 'var(--surface-2)' }}></div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
          <div style={{ width: '180px', height: '14px', background: 'var(--surface-2)', borderRadius: '4px' }}></div>
          <div style={{ width: '120px', height: '10px', background: 'var(--surface-3)', borderRadius: '4px' }}></div>
        </div>
      </div>
      <div style={{ width: '140px', height: '36px', background: 'var(--surface-2)', borderRadius: 'var(--radius)' }}></div>
    </div>
  );

  const renderSnapshotGridSkeleton = () => (
    <div className="card skeleton-blink" style={{
      background: 'var(--surface)',
      border: '1px solid var(--border)',
      borderRadius: 'var(--radius)',
      padding: '16px 20px',
      marginBottom: '12px'
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
        <div style={{ width: '130px', height: '14px', background: 'var(--surface-2)', borderRadius: '4px' }}></div>
        <div style={{ width: '70px', height: '18px', background: 'var(--surface-2)', borderRadius: 'var(--radius-pill)' }}></div>
      </div>
      {/* 3 Stats Grid matching Child at a Glance */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px' }}>
        {[1, 2, 3].map(i => (
          <div key={i} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: '8px', padding: '10px 0' }}>
            <div style={{ width: '60px', height: '32px', background: 'var(--surface-2)', borderRadius: '6px' }}></div>
            <div style={{ width: '80px', height: '12px', background: 'var(--surface-3)', borderRadius: '4px' }}></div>
          </div>
        ))}
      </div>
    </div>
  );

  const renderReviewsSkeleton = () => {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginTop: '12px' }} className="skeleton-blink">
        <div className="card" style={{
          background: 'var(--surface)',
          border: '1px solid var(--border)',
          borderRadius: 'var(--radius)',
          padding: '16px 20px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
            <div style={{ width: '42px', height: '42px', borderRadius: '50%', background: 'var(--surface-2)' }}></div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
              <div style={{ width: '160px', height: '14px', background: 'var(--surface-2)', borderRadius: '4px' }}></div>
              <div style={{ width: '100px', height: '10px', background: 'var(--surface-3)', borderRadius: '4px' }}></div>
            </div>
          </div>
          <div style={{ width: '110px', height: '32px', background: 'var(--surface-2)', borderRadius: 'var(--radius)' }}></div>
        </div>
      </div>
    );
  };

  const renderChartSkeleton = () => (
    <div className="card skeleton-blink" style={{
      background: 'var(--surface)',
      border: '1px solid var(--border)',
      borderRadius: 'var(--radius)',
      padding: '16px 20px',
      marginBottom: '12px',
      minHeight: '160px'
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
        <div style={{ width: '140px', height: '14px', background: 'var(--surface-2)', borderRadius: '4px' }}></div>
        <div style={{ width: '80px', height: '18px', background: 'var(--surface-2)', borderRadius: 'var(--radius-pill)' }}></div>
      </div>
      <div style={{ height: '90px', background: 'var(--surface-2)', borderRadius: 'var(--radius-sm)' }}></div>
    </div>
  );

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

  const getParentFirstName = () => {
    const fullName = user?.name || user?.displayName || '';
    if (fullName) {
      return fullName.split(' ')[0];
    }
    if (user?.email) {
      return user.email.split('@')[0];
    }
    return 'Parent';
  };

  const [notificationPermission, setNotificationPermission] = useState<string>('default');
  const [notificationsSupported, setNotificationsSupported] = useState<boolean>(true);

  const [notificationHistory, setNotificationHistory] = useState<any[]>([]);
  const [loadingHistory, setLoadingHistory] = useState(false);

  const fetchNotificationHistory = async () => {
    setLoadingHistory(true);
    setActiveModal('notificationHistory');
    try {
      const idToken = firebaseUser ? await firebaseUser.getIdToken() : null;
      if (!idToken) return;
      const res = await fetch('/api/parent/notification-history', {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (res.ok) {
        const data = await res.json();
        setNotificationHistory(data.history || []);
      }
    } catch (err) {
      console.error('Error fetching notification history:', err);
    } finally {
      setLoadingHistory(false);
    }
  };

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const supported = 'Notification' in window;
      setNotificationsSupported(supported);
      if (supported) {
        setNotificationPermission(Notification.permission);
      }
    }
  }, []);

  const handleSyncPush = async () => {
    setSyncingPush(true);
    try {
      if (typeof window !== 'undefined' && 'Notification' in window) {
        const permission = await Notification.requestPermission();
        setNotificationPermission(permission);
        if (permission === 'granted') {
          await initFCM();
          const idToken = firebaseUser ? await firebaseUser.getIdToken() : null;
          if (idToken) {
            const res = await fetch('/api/auth/session', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${idToken}`
              },
              body: JSON.stringify({ action: 'get_profile' })
            });
            if (res.ok) {
              window.location.reload();
            }
          }
        }
      }
    } catch (err: any) {
      console.error('Manual push sync error:', err);
    } finally {
      setSyncingPush(false);
    }
  };

  // Modals & Reviews extra state
  const [selectedActivity, setSelectedActivity] = useState<ActivityItem | null>(null);
  const [showSeenNotices, setShowSeenNotices] = useState(false);
  const [isNoticesModalOpen, setIsNoticesModalOpen] = useState(false);

  const handleDismissOverlayNotice = async (noticeId: string, reason?: string, remarks?: string) => {
    const userId = firebaseUser?.uid || 'parent';
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
        body: JSON.stringify({ noticeId, reason, remarks })
      });
    } catch (err) {
      console.warn('Failed to report notice seen status:', err);
    }

    // Reset absence form state
    setAbsenceReason('');
    setAbsenceRemarks('');
    
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

  const [localCache, setLocalCache] = useState<ParentDashboardData | null>(null);
  const [localReviewsCache, setLocalReviewsCache] = useState<{
    objectiveReviews: ReviewItem[];
    practiceReviews: ReviewItem[];
    subjectiveReviews: ReviewItem[];
    entranceReviews: ReviewItem[];
  } | null>(null);

  useEffect(() => {
    if (!selectedChildCode) return;
    try {
      const cached = localStorage.getItem(`yc_parent_dashboard_cache_${selectedChildCode}`);
      if (cached) {
        setLocalCache(JSON.parse(cached));
      } else {
        setLocalCache(null);
      }
      const cachedReviews = localStorage.getItem(`yc_parent_reviews_cache_${selectedChildCode}`);
      if (cachedReviews) {
        setLocalReviewsCache(JSON.parse(cachedReviews));
      } else {
        setLocalReviewsCache(null);
      }
    } catch (e) {
      console.warn('Failed to load parent dashboard cache:', e);
    }
  }, [selectedChildCode]);

  // 1. Fetch parent dashboard initial (children list)
  const { data: initialData, error: initialError, isLoading: initialLoading } = useSWR<ParentDashboardData>(
    firebaseUser ? '/api/parent/dashboard' : null,
    fetcher,
    { 
      fallbackData: serverInitialData || undefined,
      revalidateOnFocus: false, 
      dedupingInterval: 60000 
    }
  );

  // Auto-select first child on load
  useEffect(() => {
    if (initialData?.children && initialData.children.length > 0 && !selectedChildCode) {
      setSelectedChildCode(initialData.children[0].studentCode);
    }
  }, [initialData, selectedChildCode]);

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

            const userId = firebaseUser?.uid || 'parent';
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
        console.warn('Failed to fetch parent notices via API:', err);
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

  const childFetcher = async (url: string) => {
    const resData = await fetcher(url);
    if (resData && selectedChildCode) {
      try {
        localStorage.setItem(`yc_parent_dashboard_cache_${selectedChildCode}`, JSON.stringify(resData));
      } catch (e) {
        console.warn('Failed to save parent dashboard cache:', e);
      }
    }
    return resData;
  };

  // 2. Fetch selected child stats
  const { data: childData, error: childError, isLoading: childLoading } = useSWR<ParentDashboardData>(
    firebaseUser && selectedChildCode ? `/api/parent/dashboard?studentCode=${selectedChildCode}` : null,
    childFetcher,
    { 
      fallbackData: selectedChildCode === defaultChildCode ? serverInitialData : (localCache || undefined),
      revalidateOnFocus: false, 
      keepPreviousData: true,
      dedupingInterval: 60000 
    }
  );

  const reviewsFetcher = async (url: string) => {
    const resData = await fetcher(url);
    if (resData && selectedChildCode) {
      try {
        localStorage.setItem(`yc_parent_reviews_cache_${selectedChildCode}`, JSON.stringify(resData));
      } catch (e) {
        console.warn('Failed to save parent reviews cache:', e);
      }
    }
    return resData;
  };

  // 3. Fetch reviews list
  const { data: reviewsData, error: reviewsError, isLoading: reviewsLoading, mutate: mutateReviews } = useSWR<{
    objectiveReviews: ReviewItem[];
    practiceReviews: ReviewItem[];
    subjectiveReviews: ReviewItem[];
    entranceReviews: ReviewItem[];
  }>(
    firebaseUser && selectedChildCode ? `/api/parent/review?studentCode=${selectedChildCode}` : null,
    reviewsFetcher,
    { 
      fallbackData: selectedChildCode === defaultChildCode ? (localReviewsCache || undefined) : undefined,
      revalidateOnFocus: false,
      dedupingInterval: 2000 
    }
  );

  const { data: feesData } = useSWR<any>(
    firebaseUser && selectedChildCode ? `/api/student/fees?studentCode=${selectedChildCode}` : null,
    fetcher,
    { revalidateOnFocus: false, dedupingInterval: 60000 }
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
    firebaseUser && selectedChildCode ? `/api/student/attendance?studentCode=${selectedChildCode}` : null,
    fetcher,
    { revalidateOnFocus: false, dedupingInterval: 60000 }
  );

  const [dismissedOverdue, setDismissedOverdue] = useState(false);

  const children = initialData?.children || [];
  const initialMatchesChild = initialData?.childInfo?.studentCode === selectedChildCode || (!selectedChildCode && initialData?.children?.length);
  const data = childData || (initialMatchesChild && initialData?.snapshot ? initialData : null) || (selectedChildCode === defaultChildCode ? localCache : null) || null;
  const objectiveReviews = reviewsData?.objectiveReviews || (selectedChildCode === defaultChildCode ? localReviewsCache?.objectiveReviews : []) || [];
  const practiceReviews = reviewsData?.practiceReviews || (selectedChildCode === defaultChildCode ? localReviewsCache?.practiceReviews : []) || [];
  const subjectiveReviews = reviewsData?.subjectiveReviews || (selectedChildCode === defaultChildCode ? localReviewsCache?.subjectiveReviews : []) || [];
  const entranceReviews = reviewsData?.entranceReviews || (selectedChildCode === defaultChildCode ? localReviewsCache?.entranceReviews : []) || [];

  const loading = (initialLoading && !initialData && !localCache) || (!selectedChildCode && children.length > 0 && !data);
  const loadingChild = childLoading && !localCache && !data;
  const error = initialError?.message || childError?.message || reviewsError?.message || '';

  const handleApprove = async () => {
    if (!firebaseUser || !selectedReview || approving) return;
    
    setApproving(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/parent/review', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          reviewId: selectedReview.id,
          type: selectedReview.type,
          childStudentCode: selectedChildCode,
          reviewedByActor: chosenActor
        })
      });

      if (!res.ok) {
        throw new Error('Failed to submit approval review');
      }

      triggerAlert('Success', '✅ Review successfully approved!');
      setSelectedReview(null);
      setActorPromptOpen(false);
      
      // Reload reviews using SWR mutation
      mutateReviews();
    } catch (err: any) {
      console.error(err);
      triggerAlert('Error', '❌ Error approving review: ' + (err.message || 'Unknown error'));
    } finally {
      setApproving(false);
    }
  };

  const handleBulkApprovePractice = async (reviewIds: string[]) => {
    if (!firebaseUser || reviewIds.length === 0 || approving) return;
    
    setApproving(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/parent/review', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          reviewIds,
          type: 'bulk_practice',
          childStudentCode: selectedChildCode,
          reviewedByActor: 'parent'
        })
      });

      if (!res.ok) {
        throw new Error('Failed to submit bulk approval review');
      }

      triggerAlert('Success', '✅ All pending practice sessions successfully approved!');
      mutateReviews();
    } catch (err: any) {
      console.error(err);
      triggerAlert('Error', '❌ Error approving practice reviews: ' + (err.message || 'Unknown error'));
    } finally {
      setApproving(false);
    }
  };

  const fmtTime = formatDurationHM;

  const getIntegrityLabel = (score: number) => {
    if (score >= 90) return { cls: 'good', label: 'Excellent' };
    if (score >= 75) return { cls: 'good', label: 'Good' };
    if (score >= 60) return { cls: 'warn', label: 'Caution' };
    return { cls: 'danger', label: 'Concerning' };
  };



  if (error) {
    const isAutonomousError = error.toLowerCase().includes('autonomous') || error.toLowerCase().includes('disabled');
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div style={{ maxWidth: '480px', width: '100%', textAlign: 'center', padding: '32px 24px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: `1px solid ${isAutonomousError ? 'var(--danger)' : 'var(--border-light)'}`, boxShadow: 'var(--shadow-glass)' }}>
          <div style={{ fontSize: '3rem', marginBottom: '12px' }}>🔒</div>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--danger)', marginBottom: '8px' }}>
            {isAutonomousError ? 'Login Denied / एक्सेस अस्वीकृत' : 'Notice'}
          </h3>
          <p style={{ fontSize: '13.5px', color: 'var(--text)', lineHeight: '1.5', marginBottom: '20px' }}>
            {error}
          </p>
          <button 
            className="btn btn-primary" 
            onClick={logout} 
            style={{ background: 'var(--danger)', color: '#ffffff', border: 'none', padding: '10px 20px', borderRadius: 'var(--radius-md)', fontWeight: 'bold', cursor: 'pointer' }}
          >
            🚪 Back to Login
          </button>
        </div>
      </div>
    );
  }

  const child = data?.childInfo;
  const activeChildName = child?.name || 'Child';
  const snapshot = data?.snapshot;
  const recentActivity = data?.recentActivity || [];

  // Calculation of weekly progress vs historical beginning average
  const progressMetrics = (() => {
    if (!data || !snapshot) return null;

    const sevenDaysAgo = new Date();
    sevenDaysAgo.setDate(sevenDaysAgo.getDate() - 7);

    // 1. Exam Performance Comparison
    const completedExams = (data.chartData || []).filter((item: any) => item.status === 'completed');
    const currentWeekExams = completedExams.filter((item: any) => new Date(item.date) >= sevenDaysAgo);
    const previousWeekExams = completedExams.filter((item: any) => new Date(item.date) < sevenDaysAgo);

    const currentExamAvg = currentWeekExams.length 
      ? currentWeekExams.reduce((sum: number, item: any) => sum + (item.marks || 0), 0) / currentWeekExams.length 
      : null;
    const previousExamAvg = previousWeekExams.length 
      ? previousWeekExams.reduce((sum: number, item: any) => sum + (item.marks || 0), 0) / previousWeekExams.length 
      : null;

    let examDiff = 0;
    let examStatus: 'up' | 'down' | 'neutral' = 'neutral';
    if (currentExamAvg !== null && previousExamAvg !== null) {
      examDiff = currentExamAvg - previousExamAvg;
      examStatus = examDiff > 0 ? 'up' : examDiff < 0 ? 'down' : 'neutral';
    }

    // 2. Practice Count & Practice Performance Comparison
    const completedPractices = (reviewsData?.practiceReviews || localReviewsCache?.practiceReviews || [])
      .filter((p: any) => p.date);
    
    const currentWeekPractices = completedPractices.filter((p: any) => new Date(p.date) >= sevenDaysAgo);
    const previousWeekPractices = completedPractices.filter((p: any) => new Date(p.date) < sevenDaysAgo);

    // Practice Performance average scorePercent
    const currentPracticePerfAvg = currentWeekPractices.length
      ? currentWeekPractices.reduce((sum: number, p: any) => sum + (p.scorePercent || p.percentage || 0), 0) / currentWeekPractices.length
      : null;
    const previousPracticePerfAvg = previousWeekPractices.length
      ? previousWeekPractices.reduce((sum: number, p: any) => sum + (p.scorePercent || p.percentage || 0), 0) / previousWeekPractices.length
      : null;

    let practicePerfDiff = 0;
    let practicePerfStatus: 'up' | 'down' | 'neutral' = 'neutral';
    if (currentPracticePerfAvg !== null && previousPracticePerfAvg !== null) {
      practicePerfDiff = currentPracticePerfAvg - previousPracticePerfAvg;
      practicePerfStatus = practicePerfDiff > 0 ? 'up' : practicePerfDiff < 0 ? 'down' : 'neutral';
    }

    // Practice Count:
    // Current week count = currentWeekPractices.length
    // Previous average weekly count:
    // First, find the duration of the previous period in weeks.
    // If there are previous practices, find the earliest practice date.
    // Else, default to 1 week.
    let previousWeeklyPracticeAvg = 0;
    if (previousWeekPractices.length > 0) {
      const dates = previousWeekPractices.map((p: any) => new Date(p.date).getTime());
      const earliestDate = Math.min(...dates);
      const msDiff = sevenDaysAgo.getTime() - earliestDate;
      const daysDiff = Math.max(1, msDiff / (1000 * 60 * 60 * 24));
      const weeksDiff = daysDiff / 7;
      previousWeeklyPracticeAvg = previousWeekPractices.length / weeksDiff;
    }

    const currentPracticeCount = currentWeekPractices.length;
    let practiceCountDiffPercent = 0;
    let practiceCountStatus: 'up' | 'down' | 'neutral' = 'neutral';
    if (previousWeeklyPracticeAvg > 0) {
      practiceCountDiffPercent = ((currentPracticeCount - previousWeeklyPracticeAvg) / previousWeeklyPracticeAvg) * 100;
      practiceCountStatus = practiceCountDiffPercent > 0 ? 'up' : practiceCountDiffPercent < 0 ? 'down' : 'neutral';
    } else if (currentPracticeCount > 0) {
      practiceCountDiffPercent = 100; // 100% increase
      practiceCountStatus = 'up';
    }

    return {
      exam: {
        current: currentExamAvg,
        previous: previousExamAvg,
        diff: examDiff,
        status: examStatus
      },
      practiceCount: {
        current: currentPracticeCount,
        previous: previousWeeklyPracticeAvg,
        diffPercent: practiceCountDiffPercent,
        status: practiceCountStatus
      },
      practicePerf: {
        current: currentPracticePerfAvg,
        previous: previousPracticePerfAvg,
        diff: practicePerfDiff,
        status: practicePerfStatus
      }
    };
  })();

  const formatDateStr = (dateStr: string | null) => {
    if (!dateStr) return '-';
    return formatDateIST(dateStr) || '-';
  };

  const allReviews = [
    ...objectiveReviews,
    ...practiceReviews,
    ...subjectiveReviews
  ];

  const sortedReviews = allReviews.sort((a, b) => {
    const da = a.date ? new Date(a.date).getTime() : 0;
    const db = b.date ? new Date(b.date).getTime() : 0;
    return db - da;
  });

  const pendingReviews = sortedReviews.filter(r => r.status === 'pending');
  const pendingExams = pendingReviews.filter(r => r.type !== 'practice');
  const pendingPractices = pendingReviews.filter(r => r.type === 'practice');
  const pendingMocks = entranceReviews.filter(r => r.status === 'pending');
  const approvedReviews = sortedReviews.filter(r => r.status === 'approved');

  const parentApprovedCount = approvedReviews.filter(r => r.reviewedByActor === 'parent' || (!r.reviewedByActor && r.status === 'approved')).length;
  const studentApprovedCount = approvedReviews.filter(r => r.reviewedByActor === 'student').length;

  return (
    <div className="page-wrapper" style={{
      background: 'var(--bg)',
      minHeight: '100vh'
    }}>
      {/* Page Header Header Bar */}
      <div className="page-header glass" style={{ 
        padding: '12px 20px', 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center', 
        borderBottom: '1px solid var(--border)',
        background: 'var(--surface-glass)',
        backdropFilter: 'blur(16px)',
        WebkitBackdropFilter: 'blur(16px)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <div 
            onClick={() => router.push('/parent')} 
            style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer' }}
          >
            <Image 
              src="/logo.png" 
              alt="YASHCOM Logo" 
              width={28}
              height={28}
              style={{ borderRadius: '50%', objectFit: 'cover' }} 
              priority
            />
            <span style={{ fontWeight: 900, fontSize: '1.2rem', letterSpacing: '0.5px', color: 'var(--text)' }}>
              YASHCOM
            </span>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
          {/* Notifications Bell Icon Button */}
          <button 
            onClick={fetchNotificationHistory}
            style={{ 
              position: 'relative', 
              background: 'rgba(255,255,255,0.05)', 
              border: '1px solid var(--border-light)', 
              borderRadius: '50%', 
              width: '38px', 
              height: '38px', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center', 
              color: 'var(--text)', 
              cursor: 'pointer'
            }}
            title="Notifications"
          >
            <Bell size={18} />
            {pendingReviews.length > 0 && (
              <span style={{
                position: 'absolute',
                top: '-2px',
                right: '-2px',
                background: '#ef4444',
                color: '#ffffff',
                fontSize: '10px',
                fontWeight: 800,
                width: '18px',
                height: '18px',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                border: '2px solid var(--surface-popover)'
              }}>
                {pendingReviews.length}
              </span>
            )}
          </button>

          {/* User Profile / Logout */}
          <button 
            onClick={logout} 
            style={{ 
              background: 'rgba(255,255,255,0.05)', 
              border: '1px solid var(--border-light)', 
              borderRadius: '50%', 
              width: '38px', 
              height: '38px', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center', 
              color: '#ef4444', 
              cursor: 'pointer'
            }}
            title="Logout"
          >
            <LogOut size={18} />
          </button>
        </div>
      </div>

      {/* Main Dashboard Container */}
      <div className="dashboard-container" style={{ maxWidth: '1000px', width: '100%', margin: '0 auto', padding: '16px 14px 80px 14px' }}>

        {/* ROW 1: Parent Greeting & Child Selector in ONE single line */}
        {initialLoading ? (
          renderChildSelectorSkeleton()
        ) : children.length > 0 ? (
          <div style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: '12px',
            marginBottom: '18px',
            flexWrap: 'nowrap'
          }}>
            <div>
              <h1 suppressHydrationWarning style={{ margin: 0, fontSize: '1rem', fontWeight: 700, color: 'var(--text)', lineHeight: '1.2' }}>
                {getGreeting()}, Parent 👋
              </h1>
            </div>

            {/* Child Selector Pill Container */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '10px',
              background: 'var(--surface)',
              border: '1px solid var(--border-light)',
              borderRadius: '24px',
              padding: '6px 14px',
              boxShadow: 'var(--shadow-sm)'
            }}>
              <div style={{
                width: '32px',
                height: '32px',
                borderRadius: '50%',
                background: 'var(--accent-grad)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '16px',
                color: '#ffffff',
                fontWeight: 700
              }}>
                👦
              </div>
              <div style={{ display: 'flex', flexDirection: 'column' }}>
                <select 
                  value={selectedChildCode}
                  onChange={(e) => setSelectedChildCode(e.target.value)}
                  style={{ 
                    background: 'transparent', 
                    border: 'none', 
                    color: 'var(--text)', 
                    fontSize: '13px', 
                    fontWeight: 700, 
                    outline: 'none', 
                    cursor: 'pointer',
                    paddingRight: '12px'
                  }}
                >
                  {children.map(c => (
                    <option key={c.studentCode} value={c.studentCode} style={{ background: '#171a1f', color: '#ffffff' }}>
                      {c.name}
                    </option>
                  ))}
                </select>
                <span style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '-2px' }}>
                  {(() => {
                    const active = children.find(c => c.studentCode === selectedChildCode) || children[0];
                    if (active?.className && active.className.trim()) {
                      return active.className.startsWith('Class') ? active.className : `Class ${active.className}`;
                    }
                    if ((active as any)?.class) {
                      return String((active as any).class).startsWith('Class') ? String((active as any).class) : `Class ${(active as any).class}`;
                    }
                    return 'Student';
                  })()}
                </span>
              </div>
            </div>
          </div>
        ) : null}

        {initialLoading || loadingChild ? (
          <>
            {renderDailySyncSkeleton()}
            {renderSnapshotGridSkeleton()}
            {renderReviewsSkeleton()}
            {renderChartSkeleton()}
          </>
        ) : children.length === 0 ? (
          <div className="alert-box alert-box-warning" style={{ display: 'block', textAlign: 'center' }}>
            No children profiles linked to this parent account. Please contact administrator.
          </div>
        ) : (
          <>
            {/* DAILY 5-MIN PARENT-CHILD SYNC BANNER */}
            <div className="card" style={{
              background: 'var(--surface)',
              border: '1px solid var(--border)',
              borderRadius: 'var(--radius)',
              padding: '14px 18px',
              marginBottom: '16px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              flexWrap: 'wrap',
              gap: '12px',
              boxShadow: 'var(--shadow-sm)'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                <div style={{
                  width: '38px',
                  height: '38px',
                  borderRadius: '50%',
                  background: 'var(--accent-soft)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: '18px',
                  color: 'var(--accent)',
                  flexShrink: 0
                }}>
                  🌙
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                  <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 800, color: 'var(--text)' }}>
                    Daily 5-Min Parent-Kid Sync
                  </h3>
                  <span style={{
                    fontSize: '10px',
                    fontWeight: 700,
                    padding: '2px 8px',
                    borderRadius: 'var(--radius-pill)',
                    background: isSyncTimeSlot() ? 'var(--success-bg)' : 'var(--surface-2)',
                    color: isSyncTimeSlot() ? 'var(--success)' : 'var(--text-muted)',
                    border: isSyncTimeSlot() ? '1px solid rgba(16, 185, 129, 0.3)' : '1px solid var(--border)'
                  }}>
                    {isSyncTimeSlot() ? '✨ 9:30–10:30 PM IST (Active Now)' : '⏰ 9:30 PM – 10:30 PM IST Slot'}
                  </span>
                </div>
              </div>

              <div>
                {dailySyncDoneToday ? (
                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px', background: 'rgba(34, 197, 94, 0.15)', border: '1px solid rgba(34, 197, 94, 0.3)', padding: '8px 14px', borderRadius: 'var(--radius)', color: '#4ade80', fontWeight: 700, fontSize: '12px' }}>
                    <span>✅ Verified for Today!</span>
                  </div>
                ) : (
                  <button 
                    className="btn"
                    disabled={!isSyncTimeSlot()}
                    onClick={() => {
                      if (!isSyncTimeSlot()) {
                        triggerAlert('Slot Closed', 'The Daily 5-Min Parent-Child Sync is strictly accessible during the 9:30 PM – 10:30 PM IST window.');
                        return;
                      }
                      setDailySyncStep(1);
                      setDailySyncPhoto(null);
                      setSyncSecondsRemaining(300);
                      setDailySyncOpen(true);
                    }}
                    style={{
                      background: isSyncTimeSlot() ? 'var(--accent-grad)' : 'var(--surface-2)',
                      color: isSyncTimeSlot() ? '#ffffff' : 'var(--text-muted)',
                      fontWeight: 700,
                      fontSize: '13px',
                      padding: '10px 18px',
                      borderRadius: 'var(--radius)',
                      border: isSyncTimeSlot() ? 'none' : '1px solid var(--border)',
                      cursor: isSyncTimeSlot() ? 'pointer' : 'not-allowed',
                      opacity: isSyncTimeSlot() ? 1 : 0.65,
                      boxShadow: isSyncTimeSlot() ? '0 4px 12px rgba(56, 189, 248, 0.3)' : 'none',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '6px'
                    }}
                    title={isSyncTimeSlot() ? 'Start live 5-minute sync with photo verification' : 'Parent-Child Sync opens only between 9:30 PM and 10:30 PM IST'}
                  >
                    {isSyncTimeSlot() ? (
                      <span>✨ Start 5-Min Sync (Live Video)</span>
                    ) : (
                      <span>🔒 Slot Opens at 9:30 PM IST</span>
                    )}
                  </button>
                )}
              </div>
            </div>

            {/* CARD 1: Child at a Glance (Clean Minimal Card matching Student Dashboard) */}
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
                  <strong style={{ fontSize: '14px', color: 'var(--text)', fontWeight: 800, letterSpacing: '0.2px', whiteSpace: 'nowrap' }}>Child at a Glance</strong>
                </div>
                <span style={{
                  background: 'var(--surface-2)',
                  color: 'var(--text-muted)',
                  fontSize: '11px',
                  fontWeight: 600,
                  padding: '4px 10px',
                  borderRadius: 'var(--radius-pill)',
                  border: '1px solid var(--border)',
                  whiteSpace: 'nowrap'
                }}>
                  This Month
                </span>
              </div>

              {/* 3 Stats Grid */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px', alignItems: 'center' }}>
                {/* Stat 1: Avg Exam Marks */}
                <div 
                  onClick={() => router.push(`/parent/review?child=${selectedChildCode}`)}
                  style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', justifyContent: 'center', gap: '4px', cursor: 'pointer', transition: 'opacity 0.2s' }}
                  title="Click to view detailed exam reviews"
                >
                  <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--text)', lineHeight: 1 }}>
                    {snapshot ? Math.round(snapshot.avgScore || 0) : 0}%
                  </div>
                  <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', fontWeight: 600 }}>
                    Average Marks
                  </div>
                </div>

                {/* Stat 2: LQ Score */}
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', justifyContent: 'center', gap: '4px', borderLeft: '1px solid var(--border)', paddingLeft: '8px' }}>
                  <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--text)', lineHeight: 1 }}>
                    {snapshot ? Math.round(snapshot.lqScore ?? snapshot.overallMastery ?? 0) : 0}%
                  </div>
                  <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', fontWeight: 600 }}>
                    LQ Score
                  </div>
                </div>

                {/* Stat 3: Efforts % */}
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', justifyContent: 'center', gap: '4px', borderLeft: '1px solid var(--border)', paddingLeft: '8px' }}>
                  <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--text)', lineHeight: 1 }}>
                    {snapshot ? Math.round(snapshot.effortsPercent ?? Math.min(100, Math.round(((snapshot as any)?.practicesCompletedCount || 0) / Math.max(1, (snapshot as any)?.totalTopicsCount || 24) * 100))) : 0}%
                  </div>
                  <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', fontWeight: 600 }}>
                    Efforts %
                  </div>
                </div>
              </div>
            </div>

            {/* CARD 2: Pending Reviews / Action Ledger */}
            <div style={{
              background: pendingReviews.length > 0 
                ? 'linear-gradient(135deg, rgba(239, 68, 68, 0.18), rgba(153, 27, 27, 0.12))' 
                : 'linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(6, 78, 59, 0.12))',
              border: pendingReviews.length > 0 
                ? '1px solid rgba(239, 68, 68, 0.4)' 
                : '1px solid rgba(16, 185, 129, 0.3)',
              borderRadius: 'var(--radius)',
              padding: '16px 20px',
              marginBottom: '16px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              flexWrap: 'wrap',
              gap: '12px'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
                <div style={{
                  width: '42px',
                  height: '42px',
                  borderRadius: '50%',
                  background: pendingReviews.length > 0 ? 'rgba(239, 68, 68, 0.25)' : 'rgba(16, 185, 129, 0.25)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: '20px',
                  color: pendingReviews.length > 0 ? '#ef4444' : '#10b981',
                  flexShrink: 0
                }}>
                  {pendingReviews.length > 0 ? '❗️' : '✅'}
                </div>
                <div>
                  <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 800, color: 'var(--text)' }}>
                    {pendingReviews.length > 0 
                      ? `${pendingReviews.length} thing(s) need your attention` 
                      : 'All Clear!'}
                  </h3>
                  <p style={{ margin: '2px 0 0 0', fontSize: '12px', color: 'var(--text-muted)' }}>
                    {pendingReviews.length > 0 
                      ? `Submission pending for review • ${pendingReviews[0]?.subject || 'Mathematics'} • Submitted today` 
                      : 'All exam paper reviews are completed and up to date.'}
                  </p>
                </div>
              </div>

              <div>
                {pendingReviews.length > 0 ? (
                  <button
                    className="btn"
                    onClick={() => router.push(`/parent/review?child=${selectedChildCode}${pendingReviews[0]?.id ? `&select=${pendingReviews[0].id}` : ''}`)}
                    style={{
                      background: 'rgba(239, 68, 68, 0.2)',
                      border: '1px solid #ef4444',
                      color: '#ffffff',
                      padding: '8px 18px',
                      borderRadius: '20px',
                      fontSize: '12px',
                      fontWeight: 800,
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '6px'
                    }}
                  >
                    <span>Review Now</span>
                    <span>→</span>
                  </button>
                ) : (
                  <button
                    className="btn btn-secondary"
                    onClick={() => router.push(`/parent/review?child=${selectedChildCode}`)}
                    style={{ padding: '6px 14px', fontSize: '12px', borderRadius: '20px', fontWeight: 700 }}
                  >
                    View History →
                  </button>
                )}
              </div>
            </div>

            {/* CARD 3: Compact 1-Line Quick Actions Bento Card */}
            <div className="card" style={{
              background: 'var(--surface)',
              border: '1px solid var(--border)',
              borderRadius: 'var(--radius)',
              padding: '12px 14px',
              marginBottom: '18px',
              boxShadow: 'var(--shadow-sm)'
            }}>
              {/* Bento Grid: 4 Action Modules in 1 Single Line */}
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(4, 1fr)',
                gap: '8px',
                alignItems: 'stretch'
              }}>
                {/* Bento Item 1: Attendance */}
                <div
                  onClick={() => router.push(`/parent/attendance?studentCode=${selectedChildCode}`)}
                  style={{
                    background: 'rgba(255, 255, 255, 0.03)',
                    border: '1px solid rgba(255, 255, 255, 0.08)',
                    borderRadius: 'var(--radius)',
                    padding: '8px 4px',
                    cursor: 'pointer',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    textAlign: 'center',
                    gap: '4px',
                    transition: 'all 0.2s ease',
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'rgba(52, 211, 153, 0.1)';
                    e.currentTarget.style.borderColor = 'rgba(52, 211, 153, 0.35)';
                    e.currentTarget.style.transform = 'translateY(-2px)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'rgba(255, 255, 255, 0.03)';
                    e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.08)';
                    e.currentTarget.style.transform = 'translateY(0)';
                  }}
                >
                  <div style={{
                    width: '30px',
                    height: '30px',
                    borderRadius: '8px',
                    background: 'rgba(52, 211, 153, 0.15)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    color: '#34d399',
                    flexShrink: 0
                  }}>
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                  </div>
                  <div style={{ fontSize: '11px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.2, whiteSpace: 'nowrap' }}>
                    Attendance
                  </div>
                  <div style={{ fontSize: '10px', color: '#34d399', fontWeight: 700, whiteSpace: 'nowrap' }}>
                    {attendanceData?.stats?.attendanceRate !== undefined ? `${attendanceData.stats.attendanceRate}%` : '100%'}
                  </div>
                </div>

                {/* Bento Item 2: Exam Register */}
                <div
                  onClick={() => router.push(`/exam-register?studentCode=${selectedChildCode}`)}
                  style={{
                    background: 'rgba(255, 255, 255, 0.03)',
                    border: '1px solid rgba(255, 255, 255, 0.08)',
                    borderRadius: 'var(--radius)',
                    padding: '8px 4px',
                    cursor: 'pointer',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    textAlign: 'center',
                    gap: '4px',
                    transition: 'all 0.2s ease',
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'rgba(192, 132, 252, 0.1)';
                    e.currentTarget.style.borderColor = 'rgba(192, 132, 252, 0.35)';
                    e.currentTarget.style.transform = 'translateY(-2px)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'rgba(255, 255, 255, 0.03)';
                    e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.08)';
                    e.currentTarget.style.transform = 'translateY(0)';
                  }}
                >
                  <div style={{
                    width: '30px',
                    height: '30px',
                    borderRadius: '8px',
                    background: 'rgba(192, 132, 252, 0.15)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    color: '#c084fc',
                    flexShrink: 0
                  }}>
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                  </div>
                  <div style={{ fontSize: '11px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.2, whiteSpace: 'nowrap' }}>
                    Exam Register
                  </div>
                  <div style={{ fontSize: '10px', color: (childData?.snapshot?.absentExamsCount || data?.snapshot?.absentExamsCount || 0) > 0 ? '#f87171' : '#c084fc', fontWeight: 700, whiteSpace: 'nowrap' }}>
                    {(childData?.snapshot?.absentExamsCount || data?.snapshot?.absentExamsCount || 0) > 0 ? `${childData?.snapshot?.absentExamsCount || data?.snapshot?.absentExamsCount} Absent` : 'Active'}
                  </div>
                </div>

                {/* Bento Item 3: Fees & Dues */}
                <div
                  onClick={() => router.push(`/parent/fees?studentCode=${selectedChildCode}`)}
                  style={{
                    background: 'rgba(255, 255, 255, 0.03)',
                    border: '1px solid rgba(255, 255, 255, 0.08)',
                    borderRadius: 'var(--radius)',
                    padding: '8px 4px',
                    cursor: 'pointer',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    textAlign: 'center',
                    gap: '4px',
                    transition: 'all 0.2s ease',
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'rgba(251, 191, 36, 0.1)';
                    e.currentTarget.style.borderColor = 'rgba(251, 191, 36, 0.35)';
                    e.currentTarget.style.transform = 'translateY(-2px)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'rgba(255, 255, 255, 0.03)';
                    e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.08)';
                    e.currentTarget.style.transform = 'translateY(0)';
                  }}
                >
                  <div style={{
                    width: '30px',
                    height: '30px',
                    borderRadius: '8px',
                    background: 'rgba(251, 191, 36, 0.15)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    color: '#fbbf24',
                    flexShrink: 0
                  }}>
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg>
                  </div>
                  <div style={{ fontSize: '11px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.2, whiteSpace: 'nowrap' }}>
                    Fees & Dues
                  </div>
                  <div style={{ fontSize: '10px', color: '#fbbf24', fontWeight: 700, whiteSpace: 'nowrap' }}>
                    Receipts
                  </div>
                </div>

                {/* Bento Item 4: Chat */}
                <div
                  onClick={() => router.push('/parent/chat')}
                  style={{
                    background: 'rgba(255, 255, 255, 0.03)',
                    border: '1px solid rgba(255, 255, 255, 0.08)',
                    borderRadius: 'var(--radius)',
                    padding: '8px 4px',
                    cursor: 'pointer',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    textAlign: 'center',
                    gap: '4px',
                    transition: 'all 0.2s ease',
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'rgba(96, 165, 250, 0.1)';
                    e.currentTarget.style.borderColor = 'rgba(96, 165, 250, 0.35)';
                    e.currentTarget.style.transform = 'translateY(-2px)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'rgba(255, 255, 255, 0.03)';
                    e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.08)';
                    e.currentTarget.style.transform = 'translateY(0)';
                  }}
                >
                  <div style={{
                    width: '30px',
                    height: '30px',
                    borderRadius: '8px',
                    background: 'rgba(96, 165, 250, 0.15)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    color: '#60a5fa',
                    flexShrink: 0
                  }}>
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                  </div>
                  <div style={{ fontSize: '11px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.2, whiteSpace: 'nowrap' }}>
                    Chat Desk
                  </div>
                  <div style={{ fontSize: '10px', color: '#60a5fa', fontWeight: 700, whiteSpace: 'nowrap' }}>
                    Messages
                  </div>
                </div>
              </div>
            </div>
          </>
        )}
      </div>

      {activeModal && (
        <div className="modal show" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 9999 }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', maxWidth: '480px', margin: 'auto' }}>
            <div className="modal-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 16px', borderBottom: '1px solid var(--border-light)' }}>
              <h4 style={{ margin: '0' }}>
                {activeModal === 'time' && '⏱️ Time Analysis'}
                {activeModal === 'streak' && '🔥 Study Streak'}
                {activeModal === 'score' && '📊 Score Details'}
                {activeModal === 'integrity' && '🛡️ Integrity Details'}
                {activeModal === 'activity' && selectedActivity && `${selectedActivity.type === 'exam' ? '📝 Exam' : '📚 Practice'} Review`}
              </h4>
              <button onClick={() => { setActiveModal(null); setSelectedActivity(null); }} style={{ background: 'transparent', border: 'none', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>
            
            <div className="modal-body" style={{ padding: '20px', fontSize: '13px' }}>
              {activeModal === 'time' && snapshot && (
                <div>
                  <div style={{ background: '#eef8ff', borderLeft: '4px solid var(--accent)', padding: '10px 14px', borderRadius: '4px', fontSize: '11.5px', color: '#1d4ed8', marginBottom: '16px', lineHeight: 1.5 }}>
                    💡 <strong>Smart Active Time Monitoring:</strong> Only active, visible screen time is counted. Idle time (&gt;60s inactivity), tab switches, and minimized windows are automatically excluded.
                  </div>

                  <h5 style={{ fontSize: '13px', fontWeight: 'bold', margin: '0 0 10px 0', color: 'var(--text)' }}>
                    ⏱️ Today's Active Time: <span style={{ color: 'var(--accent)' }}>{fmtTime(snapshot.todaySeconds)}</span>
                  </h5>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', marginBottom: '20px' }}>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>📝 EXAMS TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--accent)' }}>{fmtTime((snapshot as any).todayExamSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>🏋️ PRACTICE TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--success)' }}>{fmtTime((snapshot as any).todayPracticeSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>📊 REVIEW TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--warning)' }}>{fmtTime((snapshot as any).todayReviewSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>🌐 OS & GENERAL TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--text)' }}>{fmtTime((snapshot as any).todayGeneralSeconds || 0)}</strong>
                    </div>
                  </div>

                  <h5 style={{ fontSize: '13px', fontWeight: 'bold', margin: '0 0 10px 0', color: 'var(--text)' }}>
                    📅 This Week Active Time (7 Days): <span style={{ color: 'var(--accent)' }}>{fmtTime(snapshot.weekSeconds)}</span>
                  </h5>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>📝 EXAMS TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--accent)' }}>{fmtTime((snapshot as any).weekExamSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>🏋️ PRACTICE TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--success)' }}>{fmtTime((snapshot as any).weekPracticeSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>📊 REVIEW TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--warning)' }}>{fmtTime((snapshot as any).weekReviewSeconds || 0)}</strong>
                    </div>
                    <div style={{ padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>🌐 OS & GENERAL TIME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--text)' }}>{fmtTime((snapshot as any).weekGeneralSeconds || 0)}</strong>
                    </div>
                  </div>
                </div>
              )}

              {activeModal === 'streak' && snapshot && (
                <div>
                  <p style={{ color: 'var(--text-muted)', marginBottom: '12px' }}>Consecutive days of online practice:</p>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <span style={{ fontSize: '2rem' }}>🔥</span>
                    <span style={{ fontSize: '1.8rem', fontWeight: 800 }}>{snapshot.streakDays} Days In a Row!</span>
                  </div>
                  <p style={{ marginTop: '12px', fontSize: '12px', color: 'var(--text-faint)' }}>Help your child maintain this streak by practicing every single day!</p>
                </div>
              )}

              {activeModal === 'score' && snapshot && (
                <div>
                  <p style={{ color: 'var(--text-muted)', marginBottom: '12px' }}>Aggregated results of all examinations and exercises:</p>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                    <div style={{ textAlign: 'center', padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)' }}>
                      <div style={{ fontSize: '20px', fontWeight: 'bold', color: 'var(--accent)' }}>{snapshot.avgScore}%</div>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Average Grade</div>
                    </div>
                    <div style={{ textAlign: 'center', padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)' }}>
                      <div style={{ fontSize: '20px', fontWeight: 'bold', color: 'var(--success)' }}>{snapshot.totalSessions}</div>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Sessions Completed</div>
                    </div>
                  </div>
                </div>
              )}

              {activeModal === 'integrity' && snapshot && (
                <div>
                  <p style={{ color: 'var(--text-muted)', marginBottom: '12px' }}>Calculated based on exam room proctor logs (tab switches, webcam detections):</p>
                  <div style={{ padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                    <span>Integrity Index Score:</span>
                    <span style={{ fontWeight: 'bold', color: 'var(--accent)' }}>{snapshot.integrityScore}%</span>
                  </div>
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '12px' }}>
                    {snapshot.integrityScore >= 90 ? (
                      <span style={{ color: 'var(--success)' }}>✅ Studied with excellent honesty. No severe anomalies reported.</span>
                    ) : snapshot.integrityScore >= 75 ? (
                      <span style={{ color: 'var(--warning)' }}>⚠️ Minor issues found (e.g. accidental tab changes). Warn child to pay attention.</span>
                    ) : (
                      <span style={{ color: 'var(--danger)' }}>🔴 Multi-violations logged. Please discuss code rules and guidelines with the child.</span>
                    )}
                  </div>
                </div>
              )}

              {activeModal === 'activity' && selectedActivity && (
                <div>
                  <div style={{ padding: '16px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', lineHeight: 1.6, whiteSpace: 'pre-line' }}>
                    {selectedActivity.type === 'exam' ? (
                      `📢 ${child?.name}'s Exam
                      ━━━━━━━━━━━━━━━━━━━━━
                      📝 Name: ${selectedActivity.name}
                      📅 Date: ${formatDateIST(selectedActivity.date)}
                      📊 Score: ${selectedActivity.score}%
                      ⏳ Status: ${selectedActivity.status}
                      ━━━━━━━━━━━━━━━━━━━━━`
                    ) : (
                      `📢 ${child?.name}'s Practice
                      ━━━━━━━━━━━━━━━━━━━━━
                      📚 Name: ${selectedActivity.name}
                      📅 Date: ${formatDateIST(selectedActivity.date)}
                      📊 Score: ${selectedActivity.score}%
                      ━━━━━━━━━━━━━━━━━━━━━`
                    )}
                  </div>
                </div>
              )}
            </div>
            
            <div className="modal-footer" style={{ padding: '12px 16px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end' }}>
              <button className="btn btn-secondary" onClick={() => { setActiveModal(null); setSelectedActivity(null); }}>Close</button>
            </div>
          </div>
        </div>
      )}


      {/* Push Notification History Modal */}
      {activeModal === 'notificationHistory' && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '600px', width: '100%', maxHeight: '80vh', display: 'flex', flexDirection: 'column', padding: '0', overflow: 'hidden' }}>
            <div className="modal-header" style={{ padding: '16px 24px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold' }}>📜 Push Notification History</h4>
              <button className="close-modal" onClick={() => setActiveModal(null)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>
            
            <div className="modal-body" style={{ padding: '24px', overflowY: 'auto', flex: 1 }}>
              {loadingHistory ? (
                <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
                  <div className="spinner" style={{ margin: '0 auto 10px' }}></div> Loading history...
                </div>
              ) : notificationHistory.length === 0 ? (
                <div style={{ textAlign: 'center', padding: '30px 0', color: 'var(--text-muted)', fontSize: '13px' }}>
                  No notification history found.
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  {notificationHistory.map((notif) => (
                    <div key={notif.id} style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '6px' }}>
                        <strong style={{ fontSize: '13px', color: 'var(--text)' }}>{notif.title}</strong>
                        <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>{formatDateTimeIST(notif.sentAt)}</span>
                      </div>
                      <p style={{ margin: 0, fontSize: '12px', color: 'var(--text-muted)', lineHeight: '1.4' }}>{notif.body}</p>
                    </div>
                  ))}
                </div>
              )}
            </div>
            
            <div className="modal-footer" style={{ padding: '12px 24px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end' }}>
              <button className="btn btn-secondary" onClick={() => setActiveModal(null)}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Announcements Modal */}
      {isNoticesModalOpen && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '600px', width: '100%', maxHeight: '80vh', display: 'flex', flexDirection: 'column', padding: '0', overflow: 'hidden' }}>
            <div className="modal-header" style={{ padding: '16px 24px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold' }}>📢 Announcements</h4>
              <button className="close-modal" onClick={() => setIsNoticesModalOpen(false)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>
            
            <div className="modal-body" style={{ padding: '24px', overflowY: 'auto', flex: 1 }}>
              {visibleNotices.length === 0 && !showSeenNotices ? (
                <div style={{ textAlign: 'center', padding: '30px 0', color: 'var(--text-muted)' }}>
                  <span style={{ fontSize: '13px' }}>All caught up! 🎉 No new announcements.</span>
                  <div style={{ marginTop: '16px' }}>
                    <button
                      onClick={() => setShowSeenNotices(true)}
                      style={{
                        background: 'none',
                        border: 'none',
                        color: 'var(--text-accent)',
                        textDecoration: 'underline',
                        cursor: 'pointer',
                        fontSize: '12px',
                        fontWeight: 600
                      }}
                    >
                      Show read announcements
                    </button>
                  </div>
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  {(showSeenNotices ? notices : visibleNotices).map(notice => {
                    const isSeen = seenNoticeIds.includes(notice.id);
                    const nType = notice.type || 'general';
                    const config = 
                      nType === 'schedule' 
                        ? { border: '4px solid var(--accent)', badgeBg: 'var(--accent-soft)', badgeColor: 'var(--accent)', label: '📅 Schedule' }
                        : nType === 'fees'
                        ? { border: '4px solid #f59e0b', badgeBg: 'rgba(245, 158, 11, 0.1)', badgeColor: '#f59e0b', label: '💰 Fees' }
                        : { border: '4px solid #ef4444', badgeBg: 'rgba(239, 68, 68, 0.1)', badgeColor: '#ef4444', label: '📢 Announcement' };

                    return (
                      <div key={notice.id} style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', borderLeft: config.border, opacity: isSeen ? 0.75 : 1, position: 'relative' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '6px', flexWrap: 'wrap', gap: '8px' }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                            <strong style={{ fontSize: '17px', color: 'var(--text)' }}>{notice.title}</strong>
                            <span style={{ fontSize: '10px', fontWeight: 800, background: config.badgeBg, color: config.badgeColor, padding: '2px 8px', borderRadius: '12px' }}>
                              {config.label}
                            </span>
                          </div>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                            <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>
                              {notice.createdAt ? (() => {
                                const d = new Date(notice.createdAt);
                                if (isNaN(d.getTime())) return '';
                                const day = String(d.getDate()).padStart(2, '0');
                                const month = String(d.getMonth() + 1).padStart(2, '0');
                                return `${day}/${month}/${d.getFullYear()}`;
                              })() : ''}
                            </span>
                            {isSeen ? (
                              <span style={{ fontSize: '10px', color: '#16a34a', fontWeight: 700 }}>
                                ✓ Read
                              </span>
                            ) : (
                              <button 
                                onClick={() => handleMarkNoticeAsSeen(notice.id)}
                                style={{
                                  background: '#ef4444',
                                  border: '1px solid #dc2626',
                                  borderRadius: 'var(--radius-sm)',
                                  padding: '2px 8px',
                                  fontSize: '10px',
                                  fontWeight: 600,
                                  cursor: 'pointer',
                                  color: '#ffffff'
                                }}
                              >
                                Read
                              </button>
                            )}
                          </div>
                        </div>
                        {nType === 'schedule' && notice.noticeDate && (
                          <div style={{
                            fontSize: '12px',
                            fontWeight: 700,
                            color: 'var(--accent)',
                            background: 'var(--accent-soft)',
                            padding: '6px 10px',
                            borderRadius: '4px',
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '4px',
                            marginBottom: '8px',
                            border: '1px solid var(--accent-ring)'
                          }}>
                            📅 Scheduled Date: {(() => {
                              const d = new Date(notice.noticeDate);
                              if (isNaN(d.getTime())) return notice.noticeDate;
                              const day = String(d.getDate()).padStart(2, '0');
                              const month = String(d.getMonth() + 1).padStart(2, '0');
                              return `${day}/${month}/${d.getFullYear()}`;
                            })()}
                          </div>
                        )}
                        <p style={{ margin: 0, fontSize: '15px', color: 'var(--text-muted)', whiteSpace: 'pre-line', lineHeight: '1.5' }}>
                          {notice.body}
                        </p>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
            
            <div className="modal-footer" style={{ padding: '12px 24px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <button
                onClick={() => setShowSeenNotices(!showSeenNotices)}
                style={{
                  background: 'none',
                  border: 'none',
                  color: 'var(--text-accent)',
                  cursor: 'pointer',
                  fontSize: '11px',
                  fontWeight: 600
                }}
              >
                {showSeenNotices ? 'Show unread only' : 'Show read announcements'}
              </button>
              <button className="btn btn-secondary" onClick={() => setIsNoticesModalOpen(false)}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Themed Custom Alert Modal */}
      {showAlert && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 30000 }}>
          <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '440px', width: '90%', display: 'flex', flexDirection: 'column', gap: '16px', boxShadow: '0 10px 25px rgba(0,0,0,0.2)' }}>
            <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 'bold', color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '8px' }}>
              ℹ️ {alertTitle || 'Notice'}
            </h3>
            <p style={{ margin: 0, fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.5' }}>
              {alertMsg}
            </p>
            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '4px' }}>
              <button 
                type="button" 
                className="btn btn-primary" 
                onClick={() => setShowAlert(false)}
              >
                OK
              </button>
            </div>
          </div>
        </div>
      )}
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
              Your child's account has an outstanding overdue balance of <strong>₹{feesData?.feeRecord?.outstandingAmount}</strong>. Please check the dues schedule and complete payment.
            </p>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <button 
                className="btn btn-primary" 
                onClick={() => {
                  router.push(`/parent/fees?studentCode=${selectedChildCode}`);
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
        
        const isAbsentNotice = type === 'exam_absent';

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
                  dangerouslySetInnerHTML={{ __html: (activeOverlayNotice.body || '').replace(/(<\/div>|<\/p>|<\/li>)\s*\r?\n/gi, '$1').replace(/\r?\n\s*(<div[^>]*>|<p[^>]*>|<ul[^>]*>|<ol[^>]*>|<li[^>]*>)/gi, '$1').replace(/\r?\n/g, '<br/>') }}
                />

                {/* Interactive Absence Reason Form for Parent */}
                {isAbsentNotice && (
                  <div style={{
                    marginTop: '16px',
                    padding: '14px',
                    background: 'rgba(239, 68, 68, 0.1)',
                    borderRadius: '8px',
                    border: '1px solid rgba(239, 68, 68, 0.3)',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '10px'
                  }}>
                    <div style={{ fontWeight: 800, fontSize: '13px', color: '#f87171' }}>
                      ⚠️ Please select reason for absence:
                    </div>
                    {[
                      '⏰ Got up Late',
                      '💬 Other Reason'
                    ].map((reasonOption) => (
                      <label key={reasonOption} style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', cursor: 'pointer', fontWeight: 600 }}>
                        <input 
                          type="radio" 
                          name="absenceReason" 
                          value={reasonOption} 
                          checked={absenceReason === reasonOption} 
                          onChange={() => setAbsenceReason(reasonOption)} 
                        />
                        {reasonOption}
                      </label>
                    ))}
                    {(absenceReason === '💬 Other Reason' || absenceReason === 'other') && (
                      <input 
                        type="text" 
                        placeholder="Please specify details..." 
                        value={absenceRemarks} 
                        onChange={(e) => setAbsenceRemarks(e.target.value)} 
                        style={{
                          width: '100%',
                          padding: '8px 10px',
                          borderRadius: '6px',
                          border: '1px solid var(--border-light)',
                          background: 'var(--surface)',
                          color: 'var(--text)',
                          fontSize: '12px',
                          marginTop: '4px'
                        }} 
                      />
                    )}
                  </div>
                )}
              </div>

              <div style={{ borderTop: '1px solid var(--border-light)', paddingTop: '16px', marginTop: '4px' }}>
                <button 
                  className="btn btn-primary" 
                  onClick={() => {
                    if (isAbsentNotice && !absenceReason) {
                      alert('Please select a reason for absence before dismissing.');
                      return;
                    }
                    handleDismissOverlayNotice(activeOverlayNotice.id, absenceReason, absenceRemarks);
                  }}
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
                  {isAbsentNotice ? 'Submit Reason & Dismiss' : 'I Understand & Dismiss'}
                </button>
              </div>
            </div>
          </div>
        );
      })()}
      {/* DAILY 5-MIN SYNC EXAM-LIKE CONTAINER MODAL */}
      {dailySyncOpen && (
        <div style={{
          position: 'fixed',
          inset: 0,
          background: 'rgba(2, 6, 23, 0.95)',
          zIndex: 11000,
          display: 'flex',
          flexDirection: 'column',
          backdropFilter: 'blur(12px)',
          overflowY: 'auto'
        }}>
          {/* Container Top Bar */}
          <div style={{
            background: 'rgba(0, 0, 0, 0.85)',
            borderBottom: '1px solid rgba(20, 184, 166, 0.3)',
            padding: '12px 20px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            flexWrap: 'wrap',
            gap: '12px'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <div style={{
                width: '36px',
                height: '36px',
                borderRadius: '50%',
                background: 'var(--accent-grad)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '18px'
              }}>
                🌙
              </div>
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 800, color: '#ffffff' }}>
                    Daily 5-Min Parent-Kid Sync
                  </h3>
                  <span style={{ fontSize: '11px', fontWeight: 700, padding: '2px 8px', borderRadius: '12px', background: 'rgba(20, 184, 166, 0.2)', color: '#5eead4', border: '1px solid rgba(20, 184, 166, 0.4)' }}>
                    9:30 PM – 10:30 PM IST Slot
                  </span>
                </div>
                <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>
                  Child: <strong>{activeChildName}</strong> · Step {dailySyncStep} of 3
                </div>
              </div>
            </div>

            {/* Right: Live WebRTC Broadcasting Badge + 5-Min Mandatory Lock Status */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px', flexWrap: 'wrap' }}>
              <div style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                background: 'rgba(239, 68, 68, 0.15)',
                border: '1px solid rgba(239, 68, 68, 0.3)',
                padding: '6px 12px',
                borderRadius: '20px',
                fontSize: '12px',
                fontWeight: 700,
                color: '#f87171'
              }}>
                <span style={{
                  width: '8px',
                  height: '8px',
                  borderRadius: '50%',
                  background: '#ef4444',
                  boxShadow: '0 0 8px #ef4444',
                  display: 'inline-block'
                }} />
                <span>Live Feed Active (Educator Monitored)</span>
              </div>

              {syncSecondsRemaining > 0 ? (
                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  background: 'linear-gradient(135deg, rgba(15, 118, 110, 0.25), rgba(20, 184, 166, 0.25))',
                  border: '1px solid rgba(20, 184, 166, 0.5)',
                  color: '#ccfbf1',
                  borderRadius: '20px',
                  padding: '6px 14px',
                  fontSize: '12px',
                  fontWeight: 800,
                  letterSpacing: '0.5px'
                }}>
                  <span>🔒 Mandatory:</span>
                  <span style={{ color: '#ffffff', fontFamily: 'monospace', fontSize: '13px' }}>{formatSyncTimer(syncSecondsRemaining)} left</span>
                </div>
              ) : (
                <button 
                  onClick={() => setDailySyncOpen(false)}
                  style={{
                    background: 'rgba(255, 255, 255, 0.1)',
                    border: '1px solid rgba(255, 255, 255, 0.2)',
                    color: '#ffffff',
                    padding: '8px 16px',
                    borderRadius: '20px',
                    fontSize: '13px',
                    fontWeight: 700,
                    cursor: 'pointer'
                  }}
                >
                  ✕ Close Sync
                </button>
              )}
            </div>
          </div>

          {/* Stepper Progress Line */}
          <div style={{ display: 'flex', background: 'rgba(255,255,255,0.05)', height: '4px' }}>
            <div style={{ flex: 1, background: dailySyncStep >= 1 ? 'var(--accent)' : 'transparent', transition: 'background 0.3s' }} />
            <div style={{ flex: 1, background: dailySyncStep >= 2 ? 'var(--accent)' : 'transparent', transition: 'background 0.3s' }} />
            <div style={{ flex: 1, background: dailySyncStep >= 3 ? 'var(--accent)' : 'transparent', transition: 'background 0.3s' }} />
          </div>

          {/* Main Sync Workspace Container */}
          <div style={{
            flex: 1,
            maxWidth: '1100px',
            width: '100%',
            margin: '0 auto',
            padding: '24px 16px',
            display: 'grid',
            gridTemplateColumns: '1fr 320px',
            gap: '24px',
            alignItems: 'start'
          }}>
            
            {/* Left: Interactive Sync Flow (Steps 1, 2, 3) */}
            <div style={{
              background: '#171a1f',
              border: '1px solid rgba(20, 184, 166, 0.3)',
              borderRadius: 'var(--radius-lg)',
              padding: '24px',
              boxShadow: '0 10px 30px rgba(0,0,0,0.3)',
              display: 'flex',
              flexDirection: 'column',
              gap: '20px'
            }}>
              
              {/* STEP 1: Current Day Activity (NOT Lifetime Totals) */}
              {dailySyncStep === 1 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '18px' }}>
                  <div style={{ borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '12px' }}>
                    <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--accent)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                      Step 1 · 60-Second Check
                    </span>
                    <h2 style={{ fontSize: '20px', fontWeight: 800, color: '#ffffff', margin: '4px 0 2px' }}>
                      Today&apos;s Study Effort ({formatDateIST(new Date().toISOString())})
                    </h2>
                    <p style={{ fontSize: '13px', color: 'var(--text-muted)', margin: 0 }}>
                      Here is what {activeChildName} achieved today. Start by appreciating their consistency!
                    </p>
                  </div>

                  {/* Today's Stats Cards Grid */}
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))', gap: '12px' }}>
                    {/* Card 1: Today's Practice Time */}
                    <div style={{ background: 'rgba(255,255,255,0.04)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: 'var(--radius)', padding: '14px', textAlign: 'center' }}>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>⏱️ Studied Today</div>
                      <div style={{ fontSize: '24px', fontWeight: 800, color: '#2dd4bf', marginTop: '4px' }}>
                        {childData?.todayStats?.todayMinutes || Math.round((childData?.snapshot?.todaySeconds || 0) / 60)}m
                      </div>
                      <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>Active Practice & Exams</div>
                    </div>

                    {/* Card 2: Sessions Completed Today */}
                    <div style={{ background: 'rgba(255,255,255,0.04)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: 'var(--radius)', padding: '14px', textAlign: 'center' }}>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>📝 Completed Today</div>
                      <div style={{ fontSize: '24px', fontWeight: 800, color: '#34d399', marginTop: '4px' }}>
                        {childData?.todayStats?.todaySessionsCount || 0}
                      </div>
                      <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>Tests / Practice Sets</div>
                    </div>

                    {/* Card 3: Questions Solved Today */}
                    <div style={{ background: 'rgba(255,255,255,0.04)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: 'var(--radius)', padding: '14px', textAlign: 'center' }}>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>🎯 Questions Today</div>
                      <div style={{ fontSize: '24px', fontWeight: 800, color: '#2dd4bf', marginTop: '4px' }}>
                        {childData?.todayStats?.todayQuestionsCount || 0}
                      </div>
                      <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>Problems Attempted</div>
                    </div>

                    {/* Card 4: Today's Average Score */}
                    <div style={{ background: 'rgba(255,255,255,0.04)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: 'var(--radius)', padding: '14px', textAlign: 'center' }}>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>📊 Today&apos;s Accuracy</div>
                      <div style={{ fontSize: '24px', fontWeight: 800, color: (childData?.todayStats?.todayAverageScore || 0) >= 70 ? '#34d399' : '#f59e0b', marginTop: '4px' }}>
                        {childData?.todayStats?.todayAverageScore !== undefined ? `${childData.todayStats.todayAverageScore}%` : '0%'}
                      </div>
                      <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>Today&apos;s Average Score</div>
                    </div>
                  </div>

                  {/* Encouragement Card */}
                  <div style={{
                    background: 'linear-gradient(135deg, rgba(15, 118, 110, 0.25), rgba(6, 22, 24, 0.4))',
                    border: '1px solid rgba(20, 184, 166, 0.3)',
                    borderRadius: 'var(--radius)',
                    padding: '14px 18px',
                    fontSize: '13px',
                    color: '#ccfbf1',
                    lineHeight: '1.5'
                  }}>
                    💬 <strong>Parent Encouragement Prompt:</strong> Tell {activeChildName}: <em>&ldquo;I saw you spent {childData?.todayStats?.todayMinutes || 25} minutes practicing today. Great job keeping your {childData?.todayStats?.streakDays || childData?.snapshot?.streakDays || 1}-day streak alive!&rdquo;</em>
                  </div>

                  <button 
                    className="btn" 
                    onClick={() => setDailySyncStep(2)}
                    style={{
                      background: 'var(--accent-grad)',
                      color: '#ffffff',
                      fontWeight: 700,
                      padding: '12px',
                      borderRadius: 'var(--radius)',
                      border: 'none',
                      cursor: 'pointer',
                      fontSize: '14px',
                      width: '100%',
                      boxShadow: '0 4px 14px rgba(15, 118, 110, 0.3)'
                    }}
                  >
                    Next: Review Diagnostic Movement & Tricky Questions →
                  </button>
                </div>
              )}

              {/* STEP 2: Diagnostic Movement & Tricky Questions */}
              {dailySyncStep === 2 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '18px' }}>
                  <div style={{ borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '12px' }}>
                    <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--accent)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                      Step 2 · 3-Minute Discussion
                    </span>
                    <h2 style={{ fontSize: '20px', fontWeight: 800, color: '#ffffff', margin: '4px 0 2px' }}>
                      Diagnostic Topic Movement & Tricky Questions
                    </h2>
                    <p style={{ fontSize: '13px', color: 'var(--text-muted)', margin: 0 }}>
                      Review which weak topics were practiced and removed from Needs Attention today.
                    </p>
                  </div>

                  {/* Diagnostic Topic Movement Breakdown */}
                  <div style={{
                    background: 'rgba(255, 255, 255, 0.03)',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    borderRadius: 'var(--radius)',
                    padding: '16px',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '14px'
                  }}>
                    <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 800, color: '#e2e8f0', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                      📊 Topic Mastery Diagnostic Movement
                    </h4>

                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '10px' }}>
                      {/* Box 1: Needs Attention Yesterday */}
                      <div style={{ background: 'rgba(239, 68, 68, 0.1)', border: '1px solid rgba(239, 68, 68, 0.25)', borderRadius: '8px', padding: '12px' }}>
                        <div style={{ fontSize: '11px', color: '#fca5a5', fontWeight: 700 }}>🔴 In Needs Attention (Yesterday)</div>
                        <div style={{ fontSize: '22px', fontWeight: 800, color: '#f87171', marginTop: '2px' }}>
                          {childData?.topicDiagnostics?.needsAttentionYesterdayCount || childData?.snapshot?.needsAttentionCount || 0} topics
                        </div>
                      </div>

                      {/* Box 2: Practiced & Removed Today */}
                      <div style={{ background: 'rgba(34, 197, 94, 0.1)', border: '1px solid rgba(34, 197, 94, 0.25)', borderRadius: '8px', padding: '12px' }}>
                        <div style={{ fontSize: '11px', color: '#86efac', fontWeight: 700 }}>🟢 Practiced & Recovered Today</div>
                        <div style={{ fontSize: '22px', fontWeight: 800, color: '#4ade80', marginTop: '2px' }}>
                          {childData?.topicDiagnostics?.recoveredTodayCount || 0} topics removed
                        </div>
                      </div>

                      {/* Box 3: Remaining in Needs Attention */}
                      <div style={{ background: 'rgba(245, 158, 11, 0.1)', border: '1px solid rgba(245, 158, 11, 0.25)', borderRadius: '8px', padding: '12px' }}>
                        <div style={{ fontSize: '11px', color: '#fde68a', fontWeight: 700 }}>🟡 Remaining Needs Attention</div>
                        <div style={{ fontSize: '22px', fontWeight: 800, color: '#f59e0b', marginTop: '2px' }}>
                          {childData?.topicDiagnostics?.needsAttentionRemainingCount || 0} topics
                        </div>
                      </div>
                    </div>

                    {/* Recovered topics tags */}
                    {(childData?.topicDiagnostics?.recoveredTodayTopics || []).length > 0 && (
                      <div style={{ marginTop: '4px' }}>
                        <div style={{ fontSize: '11px', color: '#86efac', fontWeight: 700, marginBottom: '6px' }}>
                          ✨ Topics successfully practiced and graduated today:
                        </div>
                        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                          {childData?.topicDiagnostics?.recoveredTodayTopics.map((t, idx) => (
                            <span key={idx} style={{ fontSize: '11px', padding: '3px 10px', borderRadius: '12px', background: 'rgba(34, 197, 94, 0.2)', color: '#4ade80', border: '1px solid rgba(34, 197, 94, 0.4)', fontWeight: 600 }}>
                              ✅ {t}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>

                  {/* Tricky Question Spotlight */}
                  <div style={{
                    background: 'rgba(255, 255, 255, 0.03)',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    borderRadius: 'var(--radius)',
                    padding: '16px',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '10px'
                  }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ fontSize: '10px', fontWeight: 700, background: 'rgba(239, 68, 68, 0.2)', color: '#f87171', padding: '2px 8px', borderRadius: '10px' }}>
                        Tricky Question Spotlight
                      </span>
                      <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Daily Mistake Review</span>
                    </div>

                    <div style={{ fontSize: '13px', color: '#ffffff', fontWeight: 600, lineHeight: '1.4' }}>
                      &ldquo;When solving numerical problems or multi-step derivations, double-check sign inversions and unit conversions.&rdquo;
                    </div>

                    <div style={{ fontSize: '12px', color: '#cbd5e1', background: 'rgba(0,0,0,0.3)', padding: '10px 12px', borderRadius: '6px', lineHeight: '1.4' }}>
                      💡 <strong>Discussion Question for Parent:</strong> Ask {activeChildName}: <em>&ldquo;Which question gave you the most trouble today? How did you figure out the solution?&rdquo;</em>
                    </div>
                  </div>

                  <div style={{ display: 'flex', gap: '10px' }}>
                    <button 
                      className="btn btn-secondary" 
                      onClick={() => setDailySyncStep(1)}
                      style={{ flex: 1, padding: '12px', fontSize: '13px' }}
                    >
                      ← Back
                    </button>
                    <button 
                      className="btn" 
                      onClick={() => {
                        setDailySyncStep(3);
                        captureSyncSnapshot();
                      }}
                      style={{
                        flex: 2,
                        background: 'var(--accent-grad)',
                        color: '#ffffff',
                        fontWeight: 700,
                        padding: '12px',
                        borderRadius: 'var(--radius)',
                        border: 'none',
                        cursor: 'pointer',
                        fontSize: '13px'
                      }}
                    >
                      Next: Complete Parent Signoff →
                    </button>
                  </div>
                </div>
              )}

              {/* STEP 3: Parent Signoff & Verification */}
              {dailySyncStep === 3 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '18px' }}>
                  <div style={{ borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '12px' }}>
                    <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--accent)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                      Step 3 · Final Signoff
                    </span>
                    <h2 style={{ fontSize: '20px', fontWeight: 800, color: '#ffffff', margin: '4px 0 2px' }}>
                      Parent Verification & Signoff
                    </h2>
                    <p style={{ fontSize: '13px', color: 'var(--text-muted)', margin: 0 }}>
                      Rate today&apos;s session and sign off. This logs into the educator sincerity report with zero penalty to student LQ.
                    </p>
                  </div>

                  {/* Reaction Selector */}
                  <div>
                    <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '8px' }}>
                      How did {activeChildName} perform in today&apos;s sync?
                    </div>
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px' }}>
                      {[
                        { id: 'excellent', label: '🌟 Excellent', desc: 'Deep Focus & Clarity' },
                        { id: 'good', label: '👍 Good', desc: 'Active Discussion' },
                        { id: 'needs_attention', label: '⚠️ Needs Focus', desc: 'Extra Practice Needed' }
                      ].map(r => (
                        <div 
                          key={r.id}
                          onClick={() => setDailySyncFeedback(r.id as any)}
                          style={{
                            background: dailySyncFeedback === r.id ? 'rgba(20, 184, 166, 0.25)' : 'rgba(255,255,255,0.04)',
                            border: dailySyncFeedback === r.id ? '2px solid var(--accent)' : '1px solid rgba(255,255,255,0.1)',
                            padding: '12px 10px',
                            borderRadius: 'var(--radius)',
                            cursor: 'pointer',
                            textAlign: 'center',
                            transition: 'all 0.2s'
                          }}
                        >
                          <div style={{ fontSize: '14px', fontWeight: 800, color: '#ffffff' }}>{r.label}</div>
                          <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>{r.desc}</div>
                        </div>
                      ))}
                    </div>
                  </div>

                  <div style={{ display: 'flex', gap: '10px' }}>
                    <button 
                      className="btn btn-secondary" 
                      onClick={() => setDailySyncStep(2)}
                      style={{ flex: 1, padding: '12px', fontSize: '13px' }}
                    >
                      ← Back
                    </button>
                    <button 
                      className="btn" 
                      onClick={handleCompleteDailySync}
                      disabled={dailySyncSubmitting || syncSecondsRemaining > 0}
                      style={{
                        flex: 2,
                        background: syncSecondsRemaining > 0
                          ? 'rgba(255, 255, 255, 0.08)'
                          : 'linear-gradient(135deg, #10b981, #059669)',
                        color: syncSecondsRemaining > 0 ? 'var(--text-muted)' : '#ffffff',
                        fontWeight: 800,
                        padding: '12px',
                        borderRadius: 'var(--radius)',
                        border: syncSecondsRemaining > 0 ? '1px solid rgba(255,255,255,0.15)' : 'none',
                        cursor: syncSecondsRemaining > 0 ? 'not-allowed' : 'pointer',
                        fontSize: '13px',
                        boxShadow: syncSecondsRemaining > 0 ? 'none' : '0 4px 14px rgba(16, 185, 129, 0.3)'
                      }}
                    >
                      {dailySyncSubmitting ? 'Recording Verification...' : syncSecondsRemaining > 0 ? `🔒 Complete 5-Min Sync to Sign (${formatSyncTimer(syncSecondsRemaining)} left)` : '✍️ Sign & Complete Sync'}
                    </button>
                  </div>
                </div>
              )}
            </div>

            {/* Right: Prominent 5-Minute Sync Countdown Card + Floating Live Video Proctoring Box */}
            <div style={{
              display: 'flex',
              flexDirection: 'column',
              gap: '16px',
              position: 'sticky',
              top: '20px'
            }}>
              {/* PROMINENT 5-MINUTE COUNTDOWN CARD */}
              <div style={{
                background: 'linear-gradient(135deg, #0b2426 0%, #061012 100%)',
                border: syncSecondsRemaining > 0 ? '2px solid var(--accent)' : '2px solid #10b981',
                borderRadius: 'var(--radius-lg)',
                padding: '18px',
                textAlign: 'center',
                boxShadow: syncSecondsRemaining > 0 ? '0 0 25px rgba(20, 184, 166, 0.25)' : '0 0 25px rgba(16, 185, 129, 0.35)',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: '8px'
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span style={{
                    width: '10px',
                    height: '10px',
                    borderRadius: '50%',
                    background: syncSecondsRemaining > 0 ? '#ef4444' : '#10b981',
                    boxShadow: syncSecondsRemaining > 0 ? '0 0 10px #ef4444' : '0 0 10px #10b981',
                    display: 'inline-block'
                  }} />
                  <span style={{ fontSize: '11px', fontWeight: 800, color: syncSecondsRemaining > 0 ? '#fca5a5' : '#86efac', textTransform: 'uppercase', letterSpacing: '0.8px' }}>
                    {syncSecondsRemaining > 0 ? 'Mandatory 5-Min Sync Timer' : '5-Min Goal Reached!'}
                  </span>
                </div>

                {/* Big Digital Clock Display */}
                <div style={{
                  fontSize: '44px',
                  fontWeight: 900,
                  fontFamily: 'monospace',
                  letterSpacing: '3px',
                  color: syncSecondsRemaining > 0 ? '#ffffff' : '#4ade80',
                  textShadow: syncSecondsRemaining > 0 ? '0 0 20px rgba(20, 184, 166, 0.4)' : '0 0 20px rgba(16, 185, 129, 0.6)',
                  lineHeight: '1',
                  margin: '4px 0'
                }}>
                  {formatSyncTimer(syncSecondsRemaining)}
                </div>

                {/* Visual Progress Bar */}
                <div style={{
                  width: '100%',
                  height: '8px',
                  background: 'rgba(255, 255, 255, 0.1)',
                  borderRadius: '10px',
                  overflow: 'hidden',
                  position: 'relative'
                }}>
                  <div style={{
                    width: `${((300 - syncSecondsRemaining) / 300) * 100}%`,
                    height: '100%',
                    background: syncSecondsRemaining > 0
                      ? 'linear-gradient(90deg, #0f766e, #14b8a6, #2dd4bf)'
                      : 'linear-gradient(90deg, #10b981, #34d399)',
                    transition: 'width 1s linear',
                    borderRadius: '10px'
                  }} />
                </div>

                <div style={{ fontSize: '11.5px', color: syncSecondsRemaining > 0 ? '#cbd5e1' : '#86efac', fontWeight: 600, marginTop: '2px', lineHeight: '1.4' }}>
                  {syncSecondsRemaining > 0 ? (
                    <>🔒 <strong>Active Discussion Required:</strong> Screen locked for 5 minutes. No logout or exit allowed.</>
                  ) : (
                    <>🎉 <strong>5 Minutes Completed!</strong> You may now sign off and complete the review.</>
                  )}
                </div>
              </div>

              {/* CAMERA FEED BOX */}
              <div style={{
                background: '#171a1f',
                border: '1px solid rgba(20, 184, 166, 0.3)',
                borderRadius: 'var(--radius-lg)',
                padding: '16px',
                display: 'flex',
                flexDirection: 'column',
                gap: '12px',
                boxShadow: '0 10px 30px rgba(0,0,0,0.3)'
              }}>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                  <span style={{ fontSize: '12px', fontWeight: 800, color: '#ffffff' }}>📹 Live Camera Feed</span>
                  <span style={{ fontSize: '9px', fontWeight: 700, padding: '2px 6px', borderRadius: '4px', background: '#ef4444', color: '#fff' }}>
                    LIVE
                  </span>
                </div>

                {/* Video Player */}
                <div style={{
                  width: '100%',
                  height: '180px',
                  borderRadius: '8px',
                  overflow: 'hidden',
                  background: '#000000',
                  border: '1px solid var(--accent-ring)',
                  position: 'relative'
                }}>
                  <video 
                    ref={syncVideoRef} 
                    autoPlay 
                    playsInline 
                    muted 
                    style={{
                      width: '100%',
                      height: '100%',
                      objectFit: 'cover',
                      transform: 'scaleX(-1)'
                    }} 
                  />
                  {!syncLiveStream && (
                    <div style={{
                      position: 'absolute',
                      inset: 0,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      color: 'var(--text-muted)',
                      fontSize: '11px',
                      textAlign: 'center',
                      padding: '8px'
                    }}>
                      Connecting camera & audio stream...
                    </div>
                  )}
                </div>

                <div style={{ fontSize: '11px', color: 'var(--text-muted)', background: 'rgba(255,255,255,0.03)', padding: '8px 10px', borderRadius: '6px', lineHeight: '1.4' }}>
                  📡 <strong>Educator Live Link:</strong> Your camera and audio are streaming directly to the Live Exam Monitor so educators can observe, talk, or listen during this sync.
                </div>
              </div>
            </div>

          </div>
        </div>
      )}
    </div>
  );
}
