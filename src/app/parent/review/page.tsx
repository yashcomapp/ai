'use client';

import React, { useEffect, useState, Suspense } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { t } from '@/lib/i18n';
import { useRouter } from 'next/navigation';
import dynamic from 'next/dynamic';
const ScorecardModal = dynamic(() => import('@/components/ScorecardModal'), { ssr: false });
import { useMathRender } from '@/hooks/useMathRender';
import { useScorecard } from '@/hooks/useScorecard';
import { preprocessMathText, formatRichText, parseAnswerList, isOptionSelectedByUser, isBlank, getReasonForQuestion, getRawOptionKey, getRawOptionText, formatUserAnswerSummary } from '@/lib/questionTypes';
import { highlightModelAnswerKeywords } from '@/lib/pdfExport';
import { formatDateIST, getDateKeyIST, formatDateTimeIST } from '@/lib/dateUtils';

interface ReviewItem {
  id: string;
  type: string;
  name: string;
  subject: string;
  chapter: string;
  date: string | null;
  score?: number;
  totalMarks?: number;
  percentage?: number;
  scorePercent?: number;
  correctCount?: number;
  totalQuestions?: number;
  tabViolations?: number;
  proctoringViolations?: any;
  noFaceCount?: number;
  multipleFacesCount?: number;
  awayTimeTotal?: number;
  timeSpentSeconds?: number;
  mode?: string;
  status: string;
  masteryBefore?: number;
  masteryAfter?: number;
  wrongAnswers?: any[];
  unattemptedQuestions?: any[];
  wrongAnswerReasons?: any;
  proctoringViolationTriggered?: boolean;
}

export default function ParentReviewPanel() {
  const { firebaseUser, user, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [children, setChildren] = useState<{ code: string; name: string }[]>([]);
  const [selectedChild, setSelectedChild] = useState<string>('');

  // Review states
  const [reviewsLoading, setReviewsLoading] = useState(true);
  const [objectiveReviews, setObjectiveReviews] = useState<ReviewItem[]>([]);
  const [practiceReviews, setPracticeReviews] = useState<ReviewItem[]>([]);
  const [subjectiveReviews, setSubjectiveReviews] = useState<ReviewItem[]>([]);
  const [entranceReviews, setEntranceReviews] = useState<ReviewItem[]>([]);
  const [activeTab, setActiveTab] = useState<'objective' | 'subjective' | 'practice' | 'mock'>('objective');
  const [isAutonomousChild, setIsAutonomousChild] = useState(false);

  // Detail modal state
  const [selectedReview, setSelectedReview] = useState<ReviewItem | null>(null);
  const [selectedDayGroup, setSelectedDayGroup] = useState<any | null>(null);
  const [approving, setApproving] = useState(false);
  const { scorecard, loading: scorecardLoading, loadScorecard: fetchScorecard, setScorecard } = useScorecard();

  // Actor selection & verification photo modal
  const [actorModal, setActorModal] = useState<{
    show: boolean;
    title: string;
    onSelectActor: (actor: 'parent' | 'student') => Promise<void>;
  }>({
    show: false,
    title: '',
    onSelectActor: async () => {}
  });
  const [capturingSnapshot, setCapturingSnapshot] = useState(false);

  const captureVerificationSnapshot = async (): Promise<string | null> => {
    try {
      if (typeof navigator === 'undefined' || !navigator.mediaDevices?.getUserMedia) {
        throw new Error('Camera and microphone hardware is not supported or accessible on this device.');
      }
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { width: { ideal: 480 }, height: { ideal: 360 }, facingMode: 'user' },
        audio: true
      });
      const video = document.createElement('video');
      video.playsInline = true;
      video.muted = true;
      video.srcObject = stream;
      await video.play();

      await new Promise(res => setTimeout(res, 500));

      const canvas = document.createElement('canvas');
      canvas.width = 480;
      canvas.height = 360;
      const ctx = canvas.getContext('2d');
      if (ctx) {
        ctx.drawImage(video, 0, 0, 480, 360);
      }
      const dataUrl = canvas.toDataURL('image/jpeg', 0.7);
      stream.getTracks().forEach(t => t.stop());
      return dataUrl;
    } catch (e: any) {
      console.error('Camera/Mic verification failed:', e);
      throw new Error(e.message || 'Camera and microphone access is required.');
    }
  };

  const requestActorConfirmation = (title: string, onConfirm: (actor: 'parent' | 'student', photoThumbnail: string | null) => Promise<void>) => {
    setActorModal({
      show: true,
      title,
      onSelectActor: async (actor) => {
        let photo: string | null = null;
        if (actor === 'parent') {
          setCapturingSnapshot(true);
          try {
            photo = await captureVerificationSnapshot();
            if (!photo) {
              throw new Error('Verification snapshot could not be generated.');
            }
          } catch (camErr: any) {
            setCapturingSnapshot(false);
            alert('⚠️ Camera & Microphone access is MANDATORY for Parent Exam Review Verification.\n\nPlease allow camera and microphone permissions in your browser settings to verify this review.');
            return;
          }
          setCapturingSnapshot(false);
        }
        setActorModal(prev => ({ ...prev, show: false }));
        await onConfirm(actor, photo);
      }
    });
  };

  useEffect(() => {
    if (!selectedReview) {
      setScorecard(null);
      return;
    }
    if (selectedReview.type === 'subjective') return;

    const loadScorecardDetails = async () => {
      try {
        await fetchScorecard(selectedReview.id, selectedChild);
      } catch (err: any) {
        console.error(err);
      }
    };
    loadScorecardDetails();
  }, [selectedReview, selectedChild]);

  // Subjective evaluation states
  const [questions, setQuestions] = useState<any[]>([]);
  const [subjectiveAttempt, setSubjectiveAttempt] = useState<any>(null);
  const [loadingQuestions, setLoadingQuestions] = useState(false);
  const [reviewAnswers, setReviewAnswers] = useState<{ [key: string]: number | string }>({});
  const [reviewFeedback, setReviewFeedback] = useState<{ [key: string]: string }>({});

  // Fetch children list from parent profile
  useEffect(() => {
    async function loadParentProfile() {
      if (!firebaseUser) return;
      try {
        const idToken = await firebaseUser.getIdToken();
        const res = await fetch('/api/parent/dashboard', {
          headers: {
            'Authorization': `Bearer ${idToken}`
          }
        });
        if (!res.ok) {
          throw new Error('Failed to fetch parent profile details');
        }
        const pData = await res.json();
        
        // Children profiles
        const mappedChildren = (pData.children || []).map((c: any) => ({
          code: c.studentCode,
          name: c.name || c.studentCode
        }));
        setChildren(mappedChildren);
        if (mappedChildren.length > 0) {
          const params = new URLSearchParams(window.location.search);
          const childParam = params.get('child') || params.get('studentCode');
          if (childParam && mappedChildren.some((c: any) => c.code === childParam)) {
            setSelectedChild(childParam);
          } else {
            setSelectedChild(mappedChildren[0].code);
          }
        } else {
          setReviewsLoading(false);
        }
      } catch (err: any) {
        console.error(err);
        setError(err.message || 'Error loading parent data');
        setReviewsLoading(false);
      } finally {
        setLoading(false);
      }
    }
    loadParentProfile();
  }, [firebaseUser]);

  // Load reviews when child changes
  const loadReviewsForChild = async (childCode: string) => {
    if (!firebaseUser || !childCode) return;
    setReviewsLoading(true);
    setObjectiveReviews([]);
    setPracticeReviews([]);
    setSubjectiveReviews([]);
    setEntranceReviews([]);
    setSelectedReview(null);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/parent/review?studentCode=${childCode}`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        throw new Error('Failed to fetch reviews list');
      }
      const data = await res.json();
      const obj = data.objectiveReviews || [];
      const prac = data.practiceReviews || [];
      const subj = data.subjectiveReviews || [];
      const entr = data.entranceReviews || [];

      setObjectiveReviews(obj);
      setPracticeReviews(prac);
      setSubjectiveReviews(subj);
      setEntranceReviews(entr);
      setIsAutonomousChild(data.isAutonomousChild || false);
      if (data.isAutonomousChild) {
        setActiveTab('objective');
      }

      // Auto-open review if query param "select" matches
      if (typeof window !== 'undefined') {
        const params = new URLSearchParams(window.location.search);
        const selectId = params.get('select');
        if (selectId) {
          const allReviews = [...obj, ...prac, ...subj, ...entr];
          const found = allReviews.find(r => r.id === selectId);
          if (found) {
            setSelectedReview(found);
          }
        }
      }
    } catch (err: any) {
      console.error(err);
      alert(err.message || 'Error loading reviews list');
    } finally {
      setReviewsLoading(false);
    }
  };

  useEffect(() => {
    if (selectedChild) {
      loadReviewsForChild(selectedChild);
    }
  }, [selectedChild]);

  // Read tab param on initial load
  useEffect(() => {
    if (typeof window !== 'undefined') {
      const params = new URLSearchParams(window.location.search);
      const tabParam = params.get('tab');
      if (tabParam === 'objective' || tabParam === 'subjective' || tabParam === 'practice' || tabParam === 'mock') {
        setActiveTab(tabParam);
      }
    }
  }, []);

  // Hook for rendering LaTeX in question lists dynamically
  useMathRender([selectedReview, questions]);

  useEffect(() => {
    const fetchQuestions = async () => {
      if (!selectedReview || selectedReview.type !== 'subjective' || !firebaseUser) {
        setQuestions([]);
        return;
      }
      setLoadingQuestions(true);
      try {
        const idToken = await firebaseUser.getIdToken();
        const res = await fetch(`/api/parent/review?attemptId=${selectedReview.id}`, {
          headers: {
            'Authorization': `Bearer ${idToken}`
          }
        });
        if (!res.ok) throw new Error('Failed to load attempt details.');
        const data = await res.json();
        const rawQuestions = data.questions || [];
        const examData = data.exam || {};
        const attemptData = data.attempt || {};
        setSubjectiveAttempt(attemptData);

        const resolvedQuestions = rawQuestions.map((q: any) => {
          let m = q.marks || q.maxMarks;
          if (m === undefined || m === null) {
            const total = examData.totalMarks || attemptData.totalMarks || 0;
            const count = rawQuestions.length || examData.questionCount || 1;
            m = total > 0 ? (total / count) : 4;
          }
          return { ...q, marks: m };
        });

        setQuestions(resolvedQuestions);
        
        // Populate default marks
        const initialAnswers: { [key: string]: number | string } = {};
        const initialFeedback: { [key: string]: string } = {};

        if (data.existingReview && data.existingReview.questionReviews) {
          data.existingReview.questionReviews.forEach((qr: any, idx: number) => {
            if (qr.stepMarks && qr.stepMarks.length > 0) {
              qr.stepMarks.forEach((step: any, si: number) => {
                initialAnswers[`ps_${idx}_${si}`] = step.awarded;
              });
            } else {
              initialAnswers[`ps_${idx}_0`] = qr.marksAwarded;
            }
            initialFeedback[`pf_${idx}`] = qr.feedback || '';
          });
        }
        
        setReviewAnswers(initialAnswers);
        setReviewFeedback(initialFeedback);
      } catch (err) {
        console.error(err);
      } finally {
        setLoadingQuestions(false);
      }
    };
    fetchQuestions();
  }, [selectedReview, firebaseUser]);

  const handleApprove = async () => {
    if (!firebaseUser || !selectedReview || approving) return;
    
    let bodyPayload: any = {
      reviewId: selectedReview.id,
      type: selectedReview.type,
      childStudentCode: selectedChild
    };

    if (selectedReview.type === 'subjective') {
      // Validate all evaluation fields are explicitly answered
      for (let i = 0; i < questions.length; i++) {
        const q = questions[i];
        if (q.steps && q.steps.length > 0) {
          for (let s = 0; s < q.steps.length; s++) {
            const rawVal = reviewAnswers[`ps_${i}_${s}`];
            if (rawVal === undefined || rawVal === null || rawVal === "") {
              alert(`Please award marks for Question ${i + 1}, Step ${s + 1}.`);
              return;
            }
          }
        } else {
          const rawVal = reviewAnswers[`ps_${i}_0`];
          if (rawVal === undefined || rawVal === null || rawVal === "") {
            alert(`Please award marks for Question ${i + 1}.`);
            return;
          }
        }
      }

      const questionReviews = [];
      let totalScore = 0;

      for (let i = 0; i < questions.length; i++) {
        const q = questions[i];
        let questionTotal = 0;
        const stepMarks: Array<{ stepNo: number; awarded: number }> = [];

        if (q.steps && q.steps.length > 0) {
          for (let s = 0; s < q.steps.length; s++) {
            const val = Number(reviewAnswers[`ps_${i}_${s}`]);
            stepMarks.push({ stepNo: s + 1, awarded: val });
            questionTotal += val;
          }
        } else {
          const val = Number(reviewAnswers[`ps_${i}_0`]);
          stepMarks.push({ stepNo: 1, awarded: val });
          questionTotal = val;
        }

        const feedback = reviewFeedback[`pf_${i}`] || '';
        questionReviews.push({
          questionId: q.id,
          maxMarks: q.marks,
          marksAwarded: questionTotal,
          stepMarks,
          feedback
        });
        totalScore += questionTotal;
      }

      bodyPayload = {
        ...bodyPayload,
        questionReviews,
        totalScore
      };
    }

    requestActorConfirmation(
      `Approve Review: ${selectedReview.name || 'Submission'}`,
      async (actor, photoThumbnail) => {
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
              ...bodyPayload,
              reviewedByActor: actor,
              photoThumbnail
            })
          });

          if (!res.ok) {
            throw new Error('Failed to submit approval review');
          }

          alert(`✅ Review successfully submitted (${actor === 'parent' ? '👨‍👩‍👧 Parent Verified' : '👨‍🎓 Student Solo'})!`);
          setSelectedReview(null);
          await loadReviewsForChild(selectedChild);
        } catch (err: any) {
          alert(err.message || 'Error submitting review');
        } finally {
          setApproving(false);
        }
      }
    );
  };

  const formatDate = (dateStr: string | null) => {
    if (!dateStr) return '-';
    const d = new Date(dateStr);
    if (isNaN(d.getTime())) return '-';
    return d.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' });
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

  const renderChildSelectorSkeleton = () => (
    <div className="child-selector-container skeleton-blink">
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <div style={{ width: '32px', height: '32px', borderRadius: '50%', background: 'var(--bg-soft)' }}></div>
        <div style={{ width: '120px', height: '14px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
      </div>
      <div className="child-selector-select" style={{ background: 'var(--bg-soft)' }}></div>
    </div>
  );

  const renderTabsSkeleton = () => (
    <div className="review-tabs skeleton-blink">
      <div style={{ flex: 1, background: 'var(--surface)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}></div>
      <div style={{ flex: 1, background: 'var(--surface)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}></div>
      {!isAutonomousChild && (
        <>
          <div style={{ flex: 1, background: 'var(--surface)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}></div>
          <div style={{ flex: 1, background: 'var(--surface)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}></div>
        </>
      )}
    </div>
  );

  const renderReviewsSkeleton = () => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
      {/* 1. Pending Reviews skeleton */}
      <div style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
        <div style={{ background: 'var(--bg-soft)', height: '45px', borderBottom: '1px solid var(--border-light)', display: 'flex', alignItems: 'center', padding: '0 20px' }}>
          <div style={{ width: '180px', height: '16px', background: 'var(--border-light)', borderRadius: '4px' }} className="skeleton-blink"></div>
        </div>
        <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {[1, 2].map(i => (
            <div key={i} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '12px', borderBottom: '1px solid var(--border-light)' }} className="skeleton-blink">
              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <div style={{ width: '200px', height: '14px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
                <div style={{ width: '250px', height: '10px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
              </div>
              <div style={{ width: '60px', height: '24px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
            </div>
          ))}
        </div>
      </div>

      {/* 2. Approved Reviews skeleton */}
      <div style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
        <div style={{ background: 'var(--bg-soft)', height: '45px', borderBottom: '1px solid var(--border-light)', display: 'flex', alignItems: 'center', padding: '0 20px' }}>
          <div style={{ width: '150px', height: '16px', background: 'var(--border-light)', borderRadius: '4px' }} className="skeleton-blink"></div>
        </div>
        <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {[1, 2].map(i => (
            <div key={i} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '12px', borderBottom: '1px solid var(--border-light)' }} className="skeleton-blink">
              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <div style={{ width: '220px', height: '14px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
                <div style={{ width: '180px', height: '10px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
              </div>
              <div style={{ width: '60px', height: '24px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );

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

  const getGreeting = () => {
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

  // Practice Day-wise Consolidation Helper
  const getDayWisePracticeGroups = () => {
    const groupsMap = new Map<string, {
      dateFormatted: string;
      dateKey: string;
      rawDate: Date | null;
      items: ReviewItem[];
      setsDone: number;
      totalQuestions: number;
      correctCount: number;
      accuracy: number;
      totalTimeSeconds: number;
      isApproved: boolean;
      allReviewIds: string[];
    }>();

    practiceReviews.forEach(item => {
      let dObj = item.date ? new Date(item.date) : null;
      if (!dObj || isNaN(dObj.getTime())) {
        dObj = (item as any).rawTimestamp ? new Date((item as any).rawTimestamp) : new Date();
      }
      
      const dateFormatted = formatDateIST(dObj);
      const dateKey = getDateKeyIST(dObj);

      if (!groupsMap.has(dateKey)) {
        groupsMap.set(dateKey, {
          dateFormatted,
          dateKey,
          rawDate: dObj,
          items: [],
          setsDone: 0,
          totalQuestions: 0,
          correctCount: 0,
          accuracy: 0,
          totalTimeSeconds: 0,
          isApproved: true,
          allReviewIds: []
        });
      }

      const g = groupsMap.get(dateKey)!;
      g.items.push(item);
      g.setsDone += 1;
      const qCount = item.totalQuestions || 1;
      g.totalQuestions += qCount;
      g.correctCount += (item.correctCount !== undefined ? item.correctCount : Math.round((item.scorePercent || 0) * qCount / 100));
      g.totalTimeSeconds += (qCount * 90); // Estimated 90s per question
      if (item.status !== 'approved') {
        g.isApproved = false;
      }
      g.allReviewIds.push(item.id);
    });

    const result = Array.from(groupsMap.values()).map(g => {
      g.accuracy = Math.round((g.correctCount / (g.totalQuestions || 1)) * 100);
      return g;
    });

    return result.sort((a, b) => (b.rawDate?.getTime() || 0) - (a.rawDate?.getTime() || 0));
  };

  const isPracticeDigestAvailable = (dateKey: string) => {
    const now = new Date();
    const todayKey = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
    
    if (dateKey < todayKey) return true; // Past dates are available
    if (dateKey > todayKey) return false;

    // Today: Available at or after 10:30 PM (22:30)
    const hour = now.getHours();
    const min = now.getMinutes();
    return hour > 22 || (hour === 22 && min >= 30);
  };

  const handleApproveDayGroup = async (group: any) => {
    if (!firebaseUser || approving || !selectedChild) return;

    requestActorConfirmation(
      `Approve Practice Digest: ${group.dateFormatted}`,
      async (actor, photoThumbnail) => {
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
              type: 'bulk_practice',
              reviewIds: group.allReviewIds,
              childStudentCode: selectedChild,
              reviewedByActor: actor,
              photoThumbnail
            })
          });

          if (!res.ok) {
            throw new Error('Failed to approve practice digest');
          }

          alert(`✅ Practice digest for ${group.dateFormatted} approved (${actor === 'parent' ? '👨‍👩‍👧 Parent Verified' : '👨‍🎓 Student Solo'})!`);
          await loadReviewsForChild(selectedChild);
        } catch (err: any) {
          alert(err.message || 'Error approving practice digest');
        } finally {
          setApproving(false);
        }
      }
    );
  };

  // Segment reviews
  const currentReviews = activeTab === 'objective'
    ? objectiveReviews
    : (activeTab === 'subjective'
      ? subjectiveReviews
      : (activeTab === 'mock'
        ? entranceReviews
        : practiceReviews));
  const pendingReviews = currentReviews.filter(r => r.status === 'pending');
  const approvedReviews = currentReviews.filter(r => r.status === 'approved');

  return (
    <div className="page-wrapper" style={{ display: 'flex', flexDirection: 'column' }}>
      <style dangerouslySetInnerHTML={{__html: `
        @keyframes skeleton-blink {
          0% { opacity: 0.6; }
          50% { opacity: 1; }
          100% { opacity: 0.6; }
        }
        .skeleton-blink {
          animation: skeleton-blink 1.5s infinite ease-in-out;
        }
        .child-selector-container {
          display: flex;
          align-items: center;
          justify-content: space-between;
          padding: 10px 16px;
          border-radius: var(--radius-lg);
          background: var(--surface);
          border: 1px solid var(--border-light);
          margin-bottom: 16px;
          height: 60px;
          box-sizing: border-box;
        }
        .child-selector-select {
          width: 180px;
          height: 34px;
          background: var(--bg-soft);
          border-radius: 6px;
        }
        .review-tabs {
          display: flex;
          margin-bottom: 16px;
          align-items: stretch;
          box-sizing: border-box;
          background: var(--surface);
          border-radius: var(--radius-md);
          border: 1px solid var(--border-light);
          overflow: hidden;
        }
        .review-tabs .tab-btn {
          flex: 1;
          padding: 10px 12px;
          font-size: 13px;
          font-weight: 600;
          text-align: center;
          white-space: nowrap;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 6px;
          border-bottom: 2px solid transparent;
          border-right: 1px solid var(--border-light);
          border-top: none;
          border-left: none;
          color: var(--text-muted);
          background: none;
          cursor: pointer;
          font-family: inherit;
          transition: all 0.2s ease;
          box-sizing: border-box;
        }
        .review-tabs .tab-btn:last-child {
          border-right: none;
        }
        .review-tabs .tab-btn.active {
          color: var(--accent);
          background: var(--bg-soft);
          border-bottom-color: var(--accent);
          font-weight: 700;
        }
        @media (max-width: 640px) {
          .review-tabs .tab-btn {
            font-size: 11.5px;
            padding: 8px 4px;
          }
        }
      `}} />
      {/* Page Header */}
      <div className="page-header glass" style={{ padding: '8px 16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderRadius: '0', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <button 
            onClick={() => router.push('/parent')}
            style={{
              background: 'transparent',
              border: 'none',
              color: 'var(--text)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              padding: '6px',
              borderRadius: '50%',
              transition: 'background 0.2s'
            }}
            title="Back to Dashboard"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>
          </button>
          <span className="brand" style={{ fontWeight: 800, fontSize: '1.1rem', color: 'var(--accent)', cursor: 'pointer' }} onClick={() => router.push('/parent')}>YASHCOM</span>
        </div>
        <div className="page-header-right" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          
          <button className="btn btn-secondary logout-btn" onClick={logout} style={{ fontSize: '1rem', padding: '6px 10px', display: 'flex', alignItems: 'center', justifyContent: 'center' }} title="Logout">🚪</button>
        </div>
      </div>

      <div className="dashboard-container" style={{ maxWidth: '1000px', width: '100%', margin: '0 auto', padding: '16px 12px' }}>
        {/* Inherited Child Name Header */}
        {!loading && children.length > 0 && (
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '14px' }}>
            <span style={{ fontSize: '1.1rem' }}>👦</span>
            <strong style={{ fontSize: '15px', fontWeight: 800, color: 'var(--text)' }}>
              {children.find(c => c.code === selectedChild)?.name || 'Student'}
            </strong>
          </div>
        )}

        {loading || reviewsLoading ? (
          renderTabsSkeleton()
        ) : (
          <div className="review-tabs">
            <button className={`tab-btn ${activeTab === 'objective' ? 'active' : ''}`} onClick={() => setActiveTab('objective')}>
              Obj <span className="tab-count">{objectiveReviews.filter(r => r.status === 'pending').length}</span>
            </button>
            {!isAutonomousChild && (
              <button className={`tab-btn ${activeTab === 'subjective' ? 'active' : ''}`} onClick={() => setActiveTab('subjective')}>
                Subj <span className="tab-count">{subjectiveReviews.filter(r => r.status === 'pending').length}</span>
              </button>
            )}
            <button className={`tab-btn ${activeTab === 'mock' ? 'active' : ''}`} onClick={() => setActiveTab('mock')}>
              Mock <span className="tab-count">{entranceReviews.filter(r => r.status === 'pending').length}</span>
            </button>
            {!isAutonomousChild && (
              <button className={`tab-btn ${activeTab === 'practice' ? 'active' : ''}`} onClick={() => setActiveTab('practice')}>
                Prac <span className="tab-count">{practiceReviews.filter(r => r.status === 'pending').length}</span>
              </button>
            )}
          </div>
        )}

        {loading || reviewsLoading ? (
          renderReviewsSkeleton()
        ) : activeTab === 'practice' ? (
          /* Day-Wise Practice Register Table */
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <div style={{ background: 'var(--bg-soft)', padding: '14px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <h3 style={{ fontSize: '13.5px', fontWeight: 800, color: 'var(--text)', margin: 0 }}>📚 Day-Wise Practice Register</h3>
                <p style={{ margin: '3px 0 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>
                  Practice sets are consolidated daily. Today's practice digest opens for parent review after 10:30 PM.
                </p>
              </div>
            </div>

            <div style={{ overflowX: 'auto' }}>
              {getDayWisePracticeGroups().length === 0 ? (
                <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-faint)' }}>📭 No practice sessions recorded.</div>
              ) : (
                <table style={{ width: '100%', fontSize: '12.5px', borderCollapse: 'collapse', textAlign: 'left' }}>
                  <thead>
                    <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)' }}>
                      <th style={{ padding: '12px 16px' }}>Date</th>
                      <th style={{ padding: '12px 16px', textAlign: 'center' }}>Sets Done</th>
                      <th style={{ padding: '12px 16px', textAlign: 'center' }}>Questions Practiced</th>
                      <th style={{ padding: '12px 16px', textAlign: 'center' }}>Time Spent</th>
                      <th style={{ padding: '12px 16px', textAlign: 'center' }}>Accuracy</th>
                      <th style={{ padding: '12px 16px', textAlign: 'right' }}>Status / Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    {getDayWisePracticeGroups().map((group, idx) => {
                      const isAvailable = isPracticeDigestAvailable(group.dateKey);
                      return (
                        <tr key={group.dateKey} style={{ borderBottom: '1px solid var(--border-light)', background: idx % 2 === 0 ? 'rgba(255,255,255,0.02)' : 'transparent' }}>
                          <td style={{ padding: '12px 16px', fontWeight: 700 }}>
                            <button 
                              onClick={() => setSelectedDayGroup(group)}
                              style={{ background: 'none', border: 'none', color: 'var(--accent)', textDecoration: 'underline', cursor: 'pointer', fontWeight: 800, fontSize: '13px' }}
                              title="Click to view full day digest"
                            >
                              📅 {group.dateFormatted}
                            </button>
                          </td>
                          <td style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700 }}>{group.setsDone} sets</td>
                          <td style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700 }}>{group.totalQuestions} Qs</td>
                          <td style={{ padding: '12px 16px', textAlign: 'center', color: 'var(--text-muted)' }}>{Math.floor(group.totalTimeSeconds / 60)}m {group.totalTimeSeconds % 60}s</td>
                          <td style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 800, color: group.accuracy >= 75 ? '#34d399' : group.accuracy >= 50 ? '#fbbf24' : '#f87171' }}>
                            {group.accuracy}%
                          </td>
                          <td style={{ padding: '12px 16px', textAlign: 'right' }}>
                            {group.isApproved ? (
                              <span className="badge badge-success" style={{ fontSize: '10.5px' }}>✓ Approved</span>
                            ) : isAvailable ? (
                              <button
                                className="btn btn-primary"
                                onClick={() => handleApproveDayGroup(group)}
                                disabled={approving}
                                style={{ padding: '4px 12px', fontSize: '11px', fontWeight: 700, borderRadius: '16px' }}
                              >
                                Approve Day
                              </button>
                            ) : (
                              <span style={{ fontSize: '10.5px', color: '#fbbf24', fontWeight: 600 }}>
                                ⏳ Available at 10:30 PM
                              </span>
                            )}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              )}
            </div>
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
            {/* 1. Pending Reviews Accordion */}
            <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
              <div style={{ background: 'var(--bg-soft)', padding: '12px 20px', borderBottom: '1px solid var(--border-light)' }}>
                <h3 style={{ fontSize: '13px', fontWeight: 'bold', color: 'var(--text)' }}>⏳ Pending Review Submissions</h3>
              </div>
              <div className="results-list">
                {pendingReviews.length === 0 ? (
                  <div style={{ textAlign: 'center', padding: '30px 0', color: 'var(--text-faint)' }}>📭 No pending submissions for review.</div>
                ) : (
                  pendingReviews.map(item => (
                    <div 
                      key={item.id} 
                      onClick={() => setSelectedReview(item)}
                      style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 20px', borderBottom: '1px solid var(--border-light)', cursor: 'pointer' }}
                    >
                      <div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                          <span style={{ fontWeight: 'bold', fontSize: '13px' }}>{item.name}</span>
                          {item.proctoringViolationTriggered && (
                            <span className="badge" style={{ background: 'var(--danger)', color: '#ffffff', fontSize: '10px', fontWeight: 800, padding: '3px 8px', borderRadius: '4px' }}>
                              🚨 Doubtful
                            </span>
                          )}
                        </div>
                        <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '4px' }}>
                          {formatDate(item.date)} • Subject: {item.subject} • Chapter: {item.chapter}
                        </div>
                      </div>
                      <div style={{ textTransform: 'uppercase' }}>
                        <div style={{ textAlign: 'right' }}>
                          <div style={{ fontWeight: 'bold', fontSize: '13px' }}>{item.percentage}%</div>
                          <div style={{ fontSize: '10px', color: 'var(--text-muted)' }}>{item.score}/{item.totalMarks}</div>
                        </div>
                      </div>
                    </div>
                  ))
                )}
              </div>
            </div>

            {/* 2. Approved Reviews Accordion */}
            <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
              <div style={{ background: 'var(--bg-soft)', padding: '12px 20px', borderBottom: '1px solid var(--border-light)' }}>
                <h3 style={{ fontSize: '13px', fontWeight: 'bold', color: 'var(--text)' }}>✅ Approved Submissions</h3>
              </div>
              <div className="results-list">
                {approvedReviews.length === 0 ? (
                  <div style={{ textAlign: 'center', padding: '30px 0', color: 'var(--text-faint)' }}>📭 No approved reviews yet.</div>
                ) : (
                  approvedReviews.map(item => (
                    <div 
                      key={item.id} 
                      onClick={() => setSelectedReview(item)}
                      style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 20px', borderBottom: '1px solid var(--border-light)', cursor: 'pointer' }}
                    >
                      <div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                          <span style={{ fontWeight: 'bold', fontSize: '13px' }}>{item.name}</span>
                          {item.proctoringViolationTriggered && (
                            <span className="badge" style={{ background: 'var(--danger)', color: '#ffffff', fontSize: '10px', fontWeight: 800, padding: '3px 8px', borderRadius: '4px' }}>
                              🚨 Doubtful
                            </span>
                          )}
                        </div>
                        <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '4px' }}>
                          {formatDate(item.date)} • Subject: {item.subject}
                        </div>
                      </div>
                      <span className="badge badge-success" style={{ fontSize: '10px' }}>Approved</span>
                    </div>
                  ))
                )}
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Day Digest Modal */}
      {selectedDayGroup && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '560px', width: '100%', padding: 0, overflow: 'hidden', boxShadow: 'var(--shadow-lg)' }}>
            <div className="modal-header" style={{ padding: '16px 24px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold', color: 'var(--text)' }}>
                📅 Day Practice Digest — {selectedDayGroup.dateFormatted}
              </h4>
              <button className="close-modal" onClick={() => setSelectedDayGroup(null)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>

            <div className="modal-body" style={{ padding: '20px', fontSize: '13px' }}>
              {/* 4 Digest Stat Boxes */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '10px', marginBottom: '18px' }}>
                <div style={{ padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                  <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>PRACTICE SETS</span>
                  <strong style={{ fontSize: '18px', color: 'var(--text)' }}>{selectedDayGroup.setsDone} Sets</strong>
                </div>
                <div style={{ padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                  <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>QUESTIONS PRACTICED</span>
                  <strong style={{ fontSize: '18px', color: 'var(--accent)' }}>{selectedDayGroup.totalQuestions} Qs</strong>
                </div>
                <div style={{ padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                  <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>TIME SPENT</span>
                  <strong style={{ fontSize: '18px', color: 'var(--text)' }}>{Math.floor(selectedDayGroup.totalTimeSeconds / 60)} mins</strong>
                </div>
                <div style={{ padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                  <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>ACCURACY</span>
                  <strong style={{ fontSize: '18px', color: selectedDayGroup.accuracy >= 75 ? '#34d399' : '#fbbf24' }}>{selectedDayGroup.accuracy}%</strong>
                </div>
              </div>

              {/* Practice Sets List */}
              <h5 style={{ fontSize: '13px', fontWeight: 800, margin: '0 0 10px 0', color: 'var(--text)' }}>📝 Attempted Practice Sets:</h5>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '220px', overflowY: 'auto' }}>
                {selectedDayGroup.items.map((item: any) => (
                  <div key={item.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                    <div>
                      <strong style={{ fontSize: '12.5px', color: 'var(--text)', display: 'block' }}>{item.name}</strong>
                      <span style={{ fontSize: '10.5px', color: 'var(--text-muted)' }}>Subject: {item.subject} • Chapter: {item.chapter}</span>
                    </div>
                    <div style={{ textAlign: 'right' }}>
                      <strong style={{ fontSize: '13px', color: 'var(--accent)' }}>{item.scorePercent}%</strong>
                      <div style={{ fontSize: '10px', color: 'var(--text-muted)' }}>{item.correctCount}/{item.totalQuestions} Qs</div>
                    </div>
                  </div>
                ))}
              </div>

              {/* Action Button */}
              <div style={{ marginTop: '20px' }}>
                {selectedDayGroup.isApproved ? (
                  <div style={{ textAlign: 'center', padding: '10px', background: 'rgba(34, 197, 94, 0.1)', color: '#34d399', fontWeight: 700, borderRadius: 'var(--radius-sm)' }}>
                    ✓ Entire Day Practice Approved
                  </div>
                ) : isPracticeDigestAvailable(selectedDayGroup.dateKey) ? (
                  <button
                    className="btn btn-primary"
                    onClick={() => {
                      handleApproveDayGroup(selectedDayGroup);
                      setSelectedDayGroup(null);
                    }}
                    disabled={approving}
                    style={{ width: '100%', padding: '12px', fontSize: '13px', fontWeight: 800 }}
                  >
                    ✅ Approve All Practices for {selectedDayGroup.dateFormatted}
                  </button>
                ) : (
                  <div style={{ textAlign: 'center', padding: '10px', background: 'rgba(245, 158, 11, 0.1)', color: '#fbbf24', fontSize: '12px', fontWeight: 600, borderRadius: 'var(--radius-sm)' }}>
                    ⏳ Today's practice is in progress. Full day digest will open for approval at 10:30 PM.
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Review Dialog Modal (Subjective only) */}
      {selectedReview && selectedReview.type === 'subjective' && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '800px', width: '100%', height: 'fit-content', maxHeight: '90vh', display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
            <div className="modal-header" style={{ padding: '16px 24px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold' }}>
                📝 Subjective Exam Evaluation
              </h4>
              <button className="close-modal" onClick={() => setSelectedReview(null)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem' }}>✕</button>
            </div>
            <div className="modal-body" style={{ padding: '24px', overflowY: 'auto', flex: 1 }}>
              <div style={{ background: 'var(--bg-soft)', padding: '16px', borderRadius: 'var(--radius)', fontSize: '13px', marginBottom: '20px', color: 'var(--text)' }}>
                <p style={{ margin: '4px 0' }}><strong>Student:</strong> {children.find(c => c.code === selectedChild)?.name || 'Student'}</p>
                <p style={{ margin: '4px 0' }}><strong>Exam:</strong> {selectedReview.name}</p>
                <p style={{ margin: '4px 0' }}><strong>Subject:</strong> {selectedReview.subject}</p>
                <p style={{ margin: '4px 0' }}><strong>Date:</strong> {formatDate(selectedReview.date)}</p>
                <p style={{ margin: '4px 0' }}><strong>Submission Type:</strong> Subjective Home Test</p>
                <p style={{ margin: '4px 0' }}><strong>Tab Switches:</strong> {selectedReview.tabViolations || 0} times</p>
              </div>

              {/* Detailed Subjective Grading Form */}
              {selectedReview.type === 'subjective' && (
                <div style={{ marginTop: '10px' }}>
                  {loadingQuestions ? (
                    <div style={{ display: 'flex', justifyContent: 'center', padding: '30px 0' }}>
                      <div className="spinner"></div>
                    </div>
                  ) : questions.length === 0 ? (
                    <div style={{ textAlign: 'center', padding: '20px', color: 'var(--text-muted)' }}>
                      No questions found for this exam.
                    </div>
                  ) : (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                      <div className="info-box blue" style={{ fontSize: '11px', background: '#eef8ff', borderLeft: '4px solid var(--accent)', padding: '10px 14px', borderRadius: '4px', color: '#1d4ed8', marginBottom: '10px' }}>
                        💡 <strong>Parent Evaluation Mode:</strong> Please check your child's physical paper/notebook against the Model Answer Key (with highlighted keywords) shown below and award marks for each question.
                      </div>

                      {questions.map((q, idx) => {
                        let rawAnswerText = '';
                        if (q.answerLines && q.answerLines.length > 0) {
                          rawAnswerText = q.answerLines.map((l: any) => `${l.lineNo}. ${l.text}`).join('\n');
                        } else if (q.solution) {
                          rawAnswerText = q.solution;
                        } else {
                          rawAnswerText = 'No model answer config.';
                        }
                        const highlightedSolution = highlightModelAnswerKeywords(rawAnswerText, q.keywords);

                        return (
                          <div key={q.id} className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-md)', border: '1.5px solid var(--border)', overflow: 'hidden', boxShadow: 'var(--shadow-sm)', marginBottom: '16px' }}>
                            <div style={{ padding: '10px 14px', background: 'var(--surface-2)', borderBottom: '1.5px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                              <span style={{ fontWeight: 800, color: 'var(--accent)', fontSize: '13px' }}>Question {idx + 1}</span>
                              <span style={{ fontSize: '11.5px', fontWeight: 700, color: 'var(--text-muted)', background: 'var(--surface)', padding: '2px 8px', borderRadius: '12px', border: '1px solid var(--border)' }}>{q.marks} Marks</span>
                            </div>

                            <div style={{ padding: '16px' }}>
                              <p className="math-container" style={{ fontSize: '13.5px', color: 'var(--text)', lineHeight: 1.5, margin: 0, whiteSpace: 'pre-line', fontWeight: 600 }}>
                                {preprocessMathText(q.text)}{q.questionCode ? ` (${q.questionCode})` : ''}
                              </p>
                            </div>

                            <div style={{ borderTop: '1px dashed var(--border)', background: 'var(--surface-2)', padding: '14px' }}>
                              <div style={{ background: 'var(--success-bg)', border: '1.5px solid var(--success)', padding: '12px', borderRadius: '8px', marginBottom: '14px' }}>
                                <strong style={{ fontSize: '12px', color: 'var(--success)', display: 'flex', alignItems: 'center', gap: '6px' }}>📖 Model Answer Key (Keyword Highlighted):</strong>
                                <div className="math-container" dangerouslySetInnerHTML={{ __html: highlightedSolution }} style={{ fontSize: '12.5px', marginTop: '8px', color: 'var(--text)', whiteSpace: 'pre-line', lineHeight: 1.6 }} />
                              </div>

                              <strong style={{ fontSize: '12px', fontWeight: 800, display: 'block', marginBottom: '10px', color: 'var(--text)' }}>✏️ Award Marks:</strong>
                              
                              {q.steps && q.steps.length > 0 ? (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                                  {q.steps.map((step: any, si: number) => (
                                    <div key={si} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', background: 'var(--surface)', border: '1.5px solid var(--border)', borderRadius: 'var(--radius-md)' }}>
                                      <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text)' }}>{step.description}</span>
                                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                        <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)' }}>Max: {step.marks}</span>
                                        <input 
                                          type="number" 
                                          min="0" 
                                          max={step.marks} 
                                          step="0.5" 
                                          disabled={selectedReview.status !== 'pending'}
                                          value={reviewAnswers[`ps_${idx}_${si}`] ?? ""}
                                          onChange={(e) => {
                                            const raw = e.target.value;
                                            if (raw === "") {
                                              setReviewAnswers(prev => {
                                                const copy = { ...prev };
                                                delete copy[`ps_${idx}_${si}`];
                                                return copy;
                                              });
                                            } else {
                                              const val = Math.min(step.marks, Math.max(0, parseFloat(raw) || 0));
                                              setReviewAnswers(prev => ({ ...prev, [`ps_${idx}_${si}`]: val }));
                                            }
                                          }}
                                          style={{ width: '70px', padding: '6px', border: '2px solid var(--accent)', borderRadius: '6px', textAlign: 'center', background: 'var(--surface-2)', color: 'var(--text)', fontWeight: 800, fontSize: '14px', outline: 'none' }}
                                        />
                                      </div>
                                    </div>
                                  ))}
                                </div>
                              ) : (
                                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', background: 'var(--surface)', border: '1.5px solid var(--border)', borderRadius: 'var(--radius-md)' }}>
                                  <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text)' }}>Overall Question Score</span>
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)' }}>Max: {q.marks}</span>
                                    <input 
                                      type="number" 
                                      min="0" 
                                      max={q.marks} 
                                      step="0.5" 
                                      disabled={selectedReview.status !== 'pending'}
                                      value={reviewAnswers[`ps_${idx}_0`] ?? ""}
                                      onChange={(e) => {
                                        const raw = e.target.value;
                                        if (raw === "") {
                                          setReviewAnswers(prev => {
                                            const copy = { ...prev };
                                            delete copy[`ps_${idx}_0`];
                                            return copy;
                                          });
                                        } else {
                                          const val = Math.min(q.marks, Math.max(0, parseFloat(raw) || 0));
                                          setReviewAnswers(prev => ({ ...prev, [`ps_${idx}_0`]: val }));
                                        }
                                      }}
                                      style={{ width: '70px', padding: '6px', border: '2px solid var(--accent)', borderRadius: '6px', textAlign: 'center', background: 'var(--surface-2)', color: 'var(--text)', fontWeight: 800, fontSize: '14px', outline: 'none' }}
                                    />
                                  </div>
                                </div>
                              )}

                              <textarea 
                                placeholder="Add comments / feedback (optional)"
                                rows={2}
                                disabled={selectedReview.status !== 'pending'}
                                value={reviewFeedback[`pf_${idx}`] || ''}
                                onChange={(e) => setReviewFeedback(prev => ({ ...prev, [`pf_${idx}`]: e.target.value }))}
                                style={{ width: '100%', marginTop: '10px', padding: '8px 12px', border: '1.5px solid var(--border)', borderRadius: '6px', fontSize: '12.5px', background: 'var(--surface-2)', color: 'var(--text)', fontFamily: 'inherit', outline: 'none' }}
                              />
                            </div>
                          </div>
                        );
                      })}

                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '16px', background: 'var(--bg-soft)', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', fontWeight: 'bold', fontSize: '14px', marginTop: '10px' }}>
                        <span>Dynamically Summed Score:</span>
                        <span style={{ color: 'var(--accent)' }}>
                          {(() => {
                            let total = 0;
                            questions.forEach((q, idx) => {
                              if (q.steps && q.steps.length > 0) {
                                q.steps.forEach((step: any, si: number) => {
                                  total += Number(reviewAnswers[`ps_${idx}_${si}`]) || 0;
                                });
                              } else {
                                total += Number(reviewAnswers[`ps_${idx}_0`]) || 0;
                              }
                            });
                            const maxTotal = questions.reduce((sum, q) => sum + (q.marks || 0), 0);
                            return `${total} / ${maxTotal}`;
                          })()} Marks
                        </span>
                      </div>
                    </div>
                  )}
                </div>
              )}

            </div>
            <div className="modal-footer" style={{ padding: '12px 24px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
              <button className="btn btn-secondary" onClick={() => setSelectedReview(null)}>Close</button>
              {selectedReview.status === 'pending' && questions.length > 0 && (
                <button className="btn className-primary" style={{ background: 'var(--accent)', color: 'white', border: 'none', padding: '8px 16px', borderRadius: 'var(--radius)', cursor: 'pointer', fontSize: '13px', fontWeight: 600 }} onClick={handleApprove} disabled={approving || loadingQuestions}>
                  {approving ? 'Submitting evaluations...' : '✅ Submit Subjective Review'}
                </button>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Review Dialog Modal (Objective/Practice scorecards) */}
      {selectedReview && selectedReview.type !== 'subjective' && (
        <ScorecardModal 
          scorecard={scorecard as any}
          loading={scorecardLoading}
          onClose={() => {
            setSelectedReview(null);
            setScorecard(null);
          }}
          actionButton={
            selectedReview.status === 'pending' ? (
              <button 
                className="btn btn-primary" 
                onClick={handleApprove} 
                disabled={approving}
                style={{ padding: '8px 16px' }}
              >
                {approving ? 'Processing Approval...' : '✅ Approve Submission'}
              </button>
            ) : (
              <div style={{ color: 'var(--success)', fontWeight: 'bold', display: 'flex', alignItems: 'center' }}>
                ✓ Approved Review
              </div>
            )
          }
        />
      )}

      {/* Actor Selection & Camera Verification Modal */}
      {actorModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.8)', zIndex: 11000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '16px' }}>
          <div style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', maxWidth: '440px', width: '100%', padding: '24px', border: '1px solid var(--border-light)', boxShadow: '0 20px 40px rgba(0,0,0,0.3)', textAlign: 'center' }}>
            <div style={{ fontSize: '32px', marginBottom: '8px' }}>📝</div>
            <h3 style={{ fontSize: '16px', fontWeight: 800, margin: '0 0 6px 0' }}>Who is completing this review?</h3>
            <p style={{ fontSize: '12px', color: 'var(--text-muted)', margin: '0 0 20px 0' }}>
              Select who went through the mistakes and solutions to record parent sincerity verification.
            </p>

            {capturingSnapshot ? (
              <div style={{ padding: '30px 20px', background: 'var(--bg-soft)', borderRadius: 'var(--radius)', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '10px' }}>
                <div className="spinner"></div>
                <div style={{ fontSize: '13px', fontWeight: 600, color: 'var(--accent)' }}>
                  Processing verification...
                </div>
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                {/* 1. Parent + Student Button */}
                <button 
                  className="btn"
                  onClick={() => actorModal.onSelectActor('parent')}
                  style={{
                    background: 'var(--accent)',
                    color: '#ffffff',
                    padding: '14px 16px',
                    borderRadius: 'var(--radius)',
                    border: 'none',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    cursor: 'pointer',
                    textAlign: 'left'
                  }}
                >
                  <div>
                    <div style={{ fontWeight: 700, fontSize: '13px' }}>👨‍👩‍👧 Parent & Student Together</div>
                    <div style={{ fontSize: '11px', opacity: 0.85 }}>Parent sat & reviewed mistakes together</div>
                  </div>
                  <span style={{ fontSize: '18px' }}>➔</span>
                </button>

                {/* 2. Student Solo Button */}
                <button 
                  className="btn"
                  onClick={() => actorModal.onSelectActor('student')}
                  style={{
                    background: 'var(--bg-soft)',
                    color: 'var(--text)',
                    padding: '12px 16px',
                    borderRadius: 'var(--radius)',
                    border: '1px solid var(--border-light)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    cursor: 'pointer',
                    textAlign: 'left'
                  }}
                >
                  <div>
                    <div style={{ fontWeight: 600, fontSize: '13px' }}>👨‍🎓 Student Solo</div>
                    <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Student completed review independently</div>
                  </div>
                  <span style={{ fontSize: '16px', color: 'var(--text-muted)' }}>➔</span>
                </button>

                {/* Cancel */}
                <button 
                  className="btn btn-secondary"
                  onClick={() => setActorModal(prev => ({ ...prev, show: false }))}
                  style={{ marginTop: '8px', padding: '8px 16px', fontSize: '12px' }}
                >
                  Cancel
                </button>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
