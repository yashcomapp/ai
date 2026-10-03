'use client';

import React, { useEffect, useState, useRef } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import useSWR from 'swr';
import { fetchWithToken } from '@/lib/swrFetcher';
import { usePushNotifications } from '@/hooks/usePushNotifications';
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

export default function ParentDashboardClient({ initialData: serverInitialData }: { initialData?: ParentDashboardData }) {
  const { user, firebaseUser, loading: authLoading, logout } = useAuth();
  const router = useRouter();
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
  }, []);

  const getGreeting = () => {
    if (!mounted) return 'Good Morning';
    const hour = new Date().getHours();
    if (hour < 12) return 'Good Morning';
    if (hour < 17) return 'Good Afternoon';
    return 'Good Evening';
  };

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
  const [notices, setNotices] = useState<ParentNotice[]>([]);
  const [seenNoticeIds, setSeenNoticeIds] = useState<string[]>([]);
  const [showSeenNotices, setShowSeenNotices] = useState(false);
  const [isNoticesModalOpen, setIsNoticesModalOpen] = useState(false);
  const [activeOverlayNotice, setActiveOverlayNotice] = useState<ParentNotice | null>(null);
  const [absenceReason, setAbsenceReason] = useState('');
  const [absenceRemarks, setAbsenceRemarks] = useState('');

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
    const alreadySeen = seenNoticeIds.includes(noticeId);
    if (!alreadySeen) {
      const updated = [...seenNoticeIds, noticeId];
      setSeenNoticeIds(updated);
      localStorage.setItem('yc_seenNotices', JSON.stringify(updated));
      window.dispatchEvent(new Event('yc_seen_notices_changed'));
    }
    
    // Call the seen API only if not already seen OR an absence reason/remarks was provided
    if ((!alreadySeen || reason || remarks) && firebaseUser) {
      try {
        const token = await firebaseUser.getIdToken();
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
    if (seenNoticeIds.includes(id)) return;
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
      revalidateOnMount: !(serverInitialData || localCache),
      revalidateIfStale: !(serverInitialData || localCache),
      keepPreviousData: true,
      dedupingInterval: 60000 
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
    firebaseUser && selectedChildCode ? `/api/parent/reviews?studentCode=${selectedChildCode}` : null,
    reviewsFetcher,
    {
      fallbackData: localReviewsCache || undefined,
      revalidateOnFocus: false,
      revalidateOnMount: !localReviewsCache,
      revalidateIfStale: !localReviewsCache,
      dedupingInterval: 60000
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
            {isAutonomousError ? 'Login Denied / Access Restricted' : 'Notice'}
          </h3>
          <p style={{ fontSize: '13.5px', color: 'var(--text)', lineHeight: '1.5', marginBottom: '20px' }}>
            {fatalError}
          </p>
          <button 
            className="btn btn-primary" 
            onClick={logout} 
            style={{ background: 'var(--danger)', color: 'var(--text-white)', border: 'none', padding: '10px 20px', borderRadius: 'var(--radius-md)', fontWeight: 'bold', cursor: 'pointer' }}
          >
            Back to Login
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
      />

      {/* Main Dashboard Container */}
      <div className="dashboard-container" style={{ maxWidth: '1000px', width: '100%', margin: '0 auto', padding: '4px 8px 30px 8px' }}>

        {/* ROW 1: Parent Greeting & Child Selector in ONE unified top glass bar */}
        <ParentChildBar
          isLoading={isGlobalLoading}
          userName={user?.name}
          userDisplayName={user?.displayName}
          greeting={getGreeting()}
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
