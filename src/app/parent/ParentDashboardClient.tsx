'use client';

import React, { useEffect, useState, useRef } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter, usePathname } from 'next/navigation';
import useSWR from 'swr';
import { fetchWithToken, createTokenFetcher } from '@/lib/swrFetcher';
import { usePushNotifications } from '@/hooks/usePushNotifications';
import { useUnreadChatCount } from '@/hooks/useUnreadChatCount';
import {
  ParentDashboardData,
  ReviewItem,
  ParentNotice,
  ParentHeader,
  ParentChildBar,
  ParentGlanceCard,
  ParentSrsCard,
  ParentActionLedger,
  ParentQuickActions,
  ParentSnapshotModals,
  ParentNoticeModals
} from '@/components/parent';
import { useNotices } from '@/hooks/useNotices';
import { getGreeting } from '@/lib/dateUtils';

export default function ParentDashboardClient({ initialData: serverInitialData }: { initialData?: ParentDashboardData }) {
  const { user, firebaseUser, loading: authLoading, logout } = useAuth();
  const router = useRouter();
  const pathname = usePathname();
  const unreadChatCount = useUnreadChatCount('parent', pathname);
  const { initFCM } = usePushNotifications();

  const defaultChildCode = serverInitialData?.childInfo?.studentCode || serverInitialData?.children?.[0]?.studentCode || '';
  const [selectedChildCode, setSelectedChildCode] = useState<string>(() => {
    if (typeof window !== 'undefined') {
      try {
        const key = user?.email ? `yc_parent_selected_child_${user.email}` : 'yc_parent_selected_child';
        return localStorage.getItem(key) || defaultChildCode;
      } catch (e) {
        return defaultChildCode;
      }
    }
    return defaultChildCode;
  });

  useEffect(() => {
    if (selectedChildCode && typeof window !== 'undefined') {
      try {
        const key = user?.email ? `yc_parent_selected_child_${user.email}` : 'yc_parent_selected_child';
        localStorage.setItem(key, selectedChildCode);
      } catch (e) {}
    }
  }, [selectedChildCode, user?.email]);

  const [activeModal, setActiveModal] = useState<string | null>(null);
  const [selectedActivity, setSelectedActivity] = useState<any | null>(null);
  const [dismissedOverdue, setDismissedOverdue] = useState(false);

  // Themed Custom Dialogs
  const [showAlert, setShowAlert] = useState(false);
  const [alertTitle, setAlertTitle] = useState('');
  const [alertMsg, setAlertMsg] = useState('');
  
  const triggerAlert = (title: string, msg: string) => {
    setAlertTitle(title);
    setAlertMsg(msg);
    setShowAlert(true);
  };

  const [mounted, setMounted] = useState(false);
  useEffect(() => {
    setMounted(true);
    // Warm up parent subroutes during background idle time
    const routes = ['/parent/review', '/parent/attendance', '/parent/fees', '/parent/chat'];
    const timer = setTimeout(() => {
      routes.forEach(r => router.prefetch(r));
    }, 1200);
    return () => clearTimeout(timer);
  }, [router]);

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

  // Modals & Notices extra state
  const [isNoticesModalOpen, setIsNoticesModalOpen] = useState(false);
  const [absenceReason, setAbsenceReason] = useState('');
  const [absenceRemarks, setAbsenceRemarks] = useState('');

  const {
    notices: rawNotices,
    seenNoticeIds,
    visibleNotices: rawVisibleNotices,
    showSeenNotices,
    setShowSeenNotices,
    activeOverlayNotice: rawActiveOverlayNotice,
    handleDismissOverlayNotice: dismissOverlayHook,
    handleMarkNoticeAsSeen
  } = useNotices({ role: 'parent', firebaseUser });

  const notices = rawNotices as ParentNotice[];
  const visibleNotices = rawVisibleNotices as ParentNotice[];
  const activeOverlayNotice = rawActiveOverlayNotice as ParentNotice | null;

  const handleDismissOverlayNotice = async (noticeId: string, reason?: string, remarks?: string) => {
    await dismissOverlayHook(noticeId, reason || absenceReason, remarks || absenceRemarks);
    setAbsenceReason('');
    setAbsenceRemarks('');
  };

  const fetcher = createTokenFetcher(firebaseUser);

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

  // 1. Single unified SWR hook for parent dashboard (fetches active child + children list)
  const dashboardSwrKey = firebaseUser 
    ? (selectedChildCode ? `/api/parent/dashboard?studentCode=${encodeURIComponent(selectedChildCode)}` : '/api/parent/dashboard')
    : null;

  const { data: dashboardData, error: dashboardError, isLoading: dashboardLoading } = useSWR<ParentDashboardData>(
    dashboardSwrKey,
    async (url: string) => {
      const resData = await fetcher(url);
      if (resData && selectedChildCode) {
        try {
          localStorage.setItem(`yc_parent_dashboard_cache_${selectedChildCode}`, JSON.stringify(resData));
        } catch (e) {
          console.warn('Failed to save parent dashboard cache:', e);
        }
      }
      return resData;
    },
    { 
      fallbackData: selectedChildCode === defaultChildCode ? serverInitialData : (localCache || undefined),
      revalidateOnFocus: false,
      revalidateOnMount: !serverInitialData,
      revalidateIfStale: true,
      keepPreviousData: true,
      dedupingInterval: 10000 
    }
  );

  // Auto-select valid child on load
  useEffect(() => {
    if (dashboardData?.children && dashboardData.children.length > 0) {
      const validCodes = dashboardData.children.map((c: any) => c.studentCode);
      if (!selectedChildCode || !validCodes.includes(selectedChildCode)) {
        setSelectedChildCode(dashboardData.children[0].studentCode);
      }
    }
  }, [dashboardData, selectedChildCode]);

  const reviewsFetcher = async (url: string) => {
    if (!firebaseUser) return null;
    const idToken = await firebaseUser.getIdToken();
    const res = await fetch(url, {
      cache: 'no-store',
      headers: {
        'Authorization': `Bearer ${idToken}`
      }
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.message || 'Failed to fetch reviews');
    }
    const resData = await res.json();
    if (resData && selectedChildCode) {
      try {
        localStorage.setItem(`yc_parent_reviews_cache_${selectedChildCode}`, JSON.stringify(resData));
      } catch (e) {
        console.warn('Failed to save parent reviews cache:', e);
      }
    }
    return resData;
  };

  // 2. Fetch reviews for selected child
  const { data: reviewsData } = useSWR<{
    objectiveReviews: ReviewItem[];
    practiceReviews: ReviewItem[];
    subjectiveReviews: ReviewItem[];
    entranceReviews: ReviewItem[];
  }>(
    firebaseUser && selectedChildCode ? `/api/parent/review?studentCode=${selectedChildCode}` : null,
    reviewsFetcher,
    {
      fallbackData: localReviewsCache || undefined,
      revalidateOnFocus: false,
      revalidateOnMount: true,
      revalidateIfStale: true,
      dedupingInterval: 10000
    }
  );

  const children = dashboardData?.children || serverInitialData?.children || [];
  const data = dashboardData || serverInitialData || localCache;

  const objectiveReviews = reviewsData?.objectiveReviews || (selectedChildCode === defaultChildCode ? localReviewsCache?.objectiveReviews : []) || [];
  const practiceReviews = reviewsData?.practiceReviews || (selectedChildCode === defaultChildCode ? localReviewsCache?.practiceReviews : []) || [];
  const subjectiveReviews = reviewsData?.subjectiveReviews || (selectedChildCode === defaultChildCode ? localReviewsCache?.subjectiveReviews : []) || [];

  const isGlobalLoading = authLoading || (dashboardLoading && !data && !localCache) || (!dashboardData && !dashboardError && !serverInitialData && !localCache);
  const isChildDataLoading = isGlobalLoading || (dashboardLoading && !data && !localCache);

  const fatalError = (dashboardError?.message && (dashboardError.message.toLowerCase().includes('autonomous') || dashboardError.message.toLowerCase().includes('disabled') || dashboardError.message.toLowerCase().includes('unauthorized') || dashboardError.message.toLowerCase().includes('access denied'))) 
    ? dashboardError.message 
    : (!dashboardData && !localCache && dashboardError?.message ? dashboardError.message : '');

  if (fatalError) {
    const isAutonomousError = fatalError.toLowerCase().includes('autonomous') || fatalError.toLowerCase().includes('disabled');
    return (
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '20px' }}>
        <div style={{ maxWidth: '480px', width: '100%', textAlign: 'center', padding: '32px 24px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: `1px solid ${isAutonomousError ? 'var(--danger)' : 'var(--border-light)'}`, boxShadow: 'var(--shadow-glass)' }}>
          <div style={{ fontSize: '3rem', marginBottom: '12px' }}>🔒</div>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--danger)', marginBottom: '8px' }}>
            {isAutonomousError ? 'Login Denied / Access Restricted • प्रवेश प्रतिबंधित' : 'Notice • सूचना'}
          </h3>
          <p style={{ fontSize: '13.5px', color: 'var(--text)', lineHeight: '1.5', marginBottom: '20px' }}>
            {fatalError}
          </p>
          <button 
            className="btn btn-primary" 
            onClick={logout} 
            style={{ background: 'var(--danger)', color: 'var(--text-white)', border: 'none', padding: '10px 20px', borderRadius: 'var(--radius-md)', fontWeight: 'bold', cursor: 'pointer' }}
          >
            Back to Login • वापस लॉगिन पर जाएं
          </button>
        </div>
      </div>
    );
  }

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

  return (
    <div className="page-wrapper" style={{
      background: 'var(--bg)',
      minHeight: '100vh'
    }}>
      {/* Page Header Header Bar */}
      <ParentHeader 
        pendingReviewsCount={pendingReviews.length}
        onOpenNotifications={fetchNotificationHistory}
        onLogout={logout}
        count={unreadChatCount}
      />

      {/* Main Dashboard Container */}
      <div className="dashboard-container" style={{ maxWidth: '1000px', width: '100%', margin: '0 auto', padding: '4px 8px 30px 8px' }}>

        {/* ROW 1: Parent Greeting & Child Selector in ONE unified top glass bar */}
        <ParentChildBar
          isLoading={isGlobalLoading}
          userName={user?.name}
          userDisplayName={user?.displayName}
          greeting={getGreeting(mounted)}
          childrenList={children}
          selectedChildCode={selectedChildCode}
          onSelectChild={setSelectedChildCode}
        />

        {/* CARD 1: Child at a Glance */}
        <ParentGlanceCard
          isLoading={isChildDataLoading}
          selectedChildCode={selectedChildCode}
          data={data}
        />

        {/* SRS Memory Refresher Alert Card */}
        <ParentSrsCard data={data} />

        {/* CARD 2: Pending Reviews / Action Ledger */}
        <ParentActionLedger
          selectedChildCode={selectedChildCode}
          pendingReviews={pendingReviews}
        />

        {/* CARD 3: Compact 1-Line Quick Actions Bento Card */}
        <ParentQuickActions
          selectedChildCode={selectedChildCode}
          data={data}
          childData={data}
        />
      </div>

      {/* Snapshot Details & Custom Dialog Modals */}
      <ParentSnapshotModals
        activeModal={activeModal}
        onCloseModal={() => { setActiveModal(null); setSelectedActivity(null); }}
        snapshot={data?.snapshot}
        childInfo={data?.childInfo}
        selectedActivity={selectedActivity}
        showAlert={showAlert}
        alertTitle={alertTitle}
        alertMsg={alertMsg}
        onCloseAlert={() => setShowAlert(false)}
        hasOverdueInstallment={(data as any)?.feeRecord?.hasOverdueInstallment}
        outstandingAmount={(data as any)?.feeRecord?.outstandingAmount}
        dismissedOverdue={dismissedOverdue}
        onDismissOverdue={() => setDismissedOverdue(true)}
        selectedChildCode={selectedChildCode}
      />

      {/* Notifications & Announcements Modals */}
      <ParentNoticeModals
        isNotificationHistoryOpen={activeModal === 'notificationHistory'}
        onCloseNotificationHistory={() => setActiveModal(null)}
        notificationHistory={notificationHistory}
        loadingHistory={loadingHistory}
        isNoticesModalOpen={isNoticesModalOpen}
        onCloseNoticesModal={() => setIsNoticesModalOpen(false)}
        notices={notices}
        visibleNotices={visibleNotices}
        seenNoticeIds={seenNoticeIds}
        showSeenNotices={showSeenNotices}
        onToggleShowSeenNotices={() => setShowSeenNotices(!showSeenNotices)}
        onMarkNoticeAsSeen={handleMarkNoticeAsSeen}
        activeOverlayNotice={activeOverlayNotice}
        onDismissOverlayNotice={handleDismissOverlayNotice}
        absenceReason={absenceReason}
        setAbsenceReason={setAbsenceReason}
        absenceRemarks={absenceRemarks}
        setAbsenceRemarks={setAbsenceRemarks}
      />
    </div>
  );
}
