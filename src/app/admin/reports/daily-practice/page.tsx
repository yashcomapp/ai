'use client';

import DateInputDMY from '@/components/DateInputDMY';
import React, { useEffect, useState, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import { formatDateDMY, getDateKeyIST } from '@/lib/dateUtils';
import { loadHtml2Canvas, formatReportStudentName, getScoreChip } from '@/lib/lqCardExport';
import { playNotificationSound } from '@/lib/audioUtils';
import { getStudentMode } from '@/types/user.types';

interface StudentSummary {
  studentCode: string;
  name: string;
  batchIds: string[];
  className: string;
  isAutonomous: boolean;
  studentMode?: string;
  activeLocks: string[];
  sessionsCount: number;
  avgAccuracy: number;
  avgHonesty: number;
  avgMastery: number;
  totalQuestions: number;
  totalTimeSpent: number;
  totalAssignedTopics?: number;
  topicsAttemptedCount?: number;
  unattemptedTopicsCount?: number;
  masteredTopicsCount?: number;
  coveragePercent?: number;
  hasPracticedAllAssigned?: boolean;
  allTopicsMastered?: boolean;
}

type DurationPreset = 'today' | 'yesterday' | '7d' | '14d' | '30d' | 'thisMonth' | 'custom';

interface StudentRemarkEvaluation {
  text: string;
  badgeType: 'all_done' | 'outstanding' | 'strong' | 'sincere' | 'irregular' | 'careless' | 'needs_practice';
  bg: string;
  color: string;
  border?: string;
}

function evaluateStudentPracticeRemark(
  s: StudentSummary,
  durationDays: number
): StudentRemarkEvaluation {
  const totalTopics = s.totalAssignedTopics || 0;
  const attemptedTopics = s.topicsAttemptedCount || 0;
  const pendingTopics = Math.max(0, totalTopics - attemptedTopics);
  const isFullyCovered = totalTopics > 0 && attemptedTopics >= totalTopics;

  // Case 1: Student has 100% completed practice on all assigned curriculum topics
  if (isFullyCovered) {
    if (durationDays > 1 && s.sessionsCount >= durationDays && s.avgAccuracy >= 85) {
      return {
        text: '✨ 100% Covered (Active)',
        badgeType: 'all_done',
        bg: '#dcfce7',
        color: '#14532d',
        border: '1.5px solid #86efac'
      };
    }
    return {
      text: '✨ 100% Topics Covered',
      badgeType: 'all_done',
      bg: '#dcfce7',
      color: '#14532d',
      border: '1.5px solid #86efac'
    };
  }

  // Case 2: Multi-day duration (e.g. 7d, 10d, 14d, 30d, thisMonth) AND full topics are NOT covered
  if (durationDays >= 2) {
    // Severe low volume: Student barely practiced while having unpracticed topics (<= 40% of days, e.g. <= 4 in 10d, <= 2 in 7d)
    const severeLowThreshold = Math.max(1, Math.floor(durationDays * 0.4));
    if (s.sessionsCount <= severeLowThreshold) {
      return {
        text: `⚠️ Careless (${s.sessionsCount} sess / ${durationDays}d)`,
        badgeType: 'careless',
        bg: '#fee2e2',
        color: '#991b1b',
        border: '1.5px solid #fca5a5'
      };
    }

    // Irregular pace: Student did fewer sessions than days (e.g. 5 to 9 sessions in 10 days)
    if (s.sessionsCount < durationDays) {
      return {
        text: `⚠️ Irregular (${s.sessionsCount} sess / ${durationDays}d)`,
        badgeType: 'irregular',
        bg: '#ffedd5',
        color: '#c2410c',
        border: '1.5px solid #fdba74'
      };
    }

    // High volume: Student did >= durationDays sessions (e.g. >= 10 sessions in 10 days)
    if (s.avgAccuracy >= 90 && s.avgHonesty >= 85) {
      return {
        text: '🌟 Outstanding & Sincere',
        badgeType: 'outstanding',
        bg: '#dcfce7',
        color: '#14532d',
        border: '1.5px solid #86efac'
      };
    }
    if (s.avgAccuracy >= 75) {
      return {
        text: '✅ Strong & Sincere',
        badgeType: 'strong',
        bg: '#e0f2fe',
        color: '#0369a1',
        border: '1.5px solid #7dd3fc'
      };
    }
    if (s.avgAccuracy >= 50) {
      return {
        text: '🟡 Moderate Accuracy',
        badgeType: 'sincere',
        bg: '#fef9c3',
        color: '#854d0e',
        border: '1.5px solid #fde047'
      };
    }
    return {
      text: '⚠️ Low Accuracy',
      badgeType: 'needs_practice',
      bg: '#fee2e2',
      color: '#991b1b',
      border: '1.5px solid #fca5a5'
    };
  }

  // Case 3: Single Day duration (durationDays <= 1)
  if (s.sessionsCount >= 3 && s.avgAccuracy >= 85) {
    return {
      text: '🌟 Highly Active Today',
      badgeType: 'outstanding',
      bg: '#dcfce7',
      color: '#14532d',
      border: '1.5px solid #86efac'
    };
  }
  if (s.avgAccuracy >= 80) {
    return {
      text: '✅ Sincere Today',
      badgeType: 'strong',
      bg: '#e0f2fe',
      color: '#0369a1',
      border: '1.5px solid #7dd3fc'
    };
  }
  if (s.avgAccuracy >= 50) {
    return {
      text: '🟡 Moderate Today',
      badgeType: 'sincere',
      bg: '#fef9c3',
      color: '#854d0e',
      border: '1.5px solid #fde047'
    };
  }
  return {
    text: '⚠️ Needs Practice',
    badgeType: 'needs_practice',
    bg: '#fee2e2',
    color: '#991b1b',
    border: '1.5px solid #fca5a5'
  };
}

export default function DailyPracticeSummaryPage() {
  const { firebaseUser, user } = useAuth();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [students, setStudents] = useState<StudentSummary[]>([]);
  const [batches, setBatches] = useState<{ id: string; name: string }[]>([]);
  const [selectedBatchId, setSelectedBatchId] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState<string>('');

  // Date range and duration presets
  const getTodayISTStr = () => getDateKeyIST(new Date());

  const [durationPreset, setDurationPreset] = useState<DurationPreset>('today');
  const [startDate, setStartDate] = useState<string>(getTodayISTStr());
  const [endDate, setEndDate] = useState<string>(getTodayISTStr());

  // Sorting state
  const [sortField, setSortField] = useState<keyof StudentSummary>('name');
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc');
  const [exportingImage, setExportingImage] = useState(false);
  const [copiedRecently, setCopiedRecently] = useState(false);

  // Client-side authentication check
  useEffect(() => {
    if (user && (user as any).role !== 'admin') {
      router.replace('/student');
    }
  }, [user, router]);

  const loadData = async (startVal: string, endVal: string, forceRefresh: boolean = false) => {
    if (!firebaseUser) return;
    setLoading(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const refreshParam = forceRefresh ? '&refresh=true' : '';
      const res = await fetch(
        `/api/admin/reports/daily-practice?startDate=${encodeURIComponent(startVal)}&endDate=${encodeURIComponent(endVal)}${refreshParam}`,
        {
          headers: {
            'Authorization': `Bearer ${idToken}`
          }
        }
      );
      if (res.ok) {
        const data = await res.json();
        setStudents(data.students || []);
        setBatches(data.batches || []);
      }
    } catch (e) {
      console.error('Error loading practice summary:', e);
    } finally {
      setLoading(false);
    }
  };

  // Preset switcher helper
  const handlePresetChange = (preset: DurationPreset) => {
    setDurationPreset(preset);
    const today = new Date();
    const todayStr = getDateKeyIST(today);

    if (preset === 'today') {
      setStartDate(todayStr);
      setEndDate(todayStr);
      loadData(todayStr, todayStr);
    } else if (preset === 'yesterday') {
      const y = new Date(today);
      y.setDate(y.getDate() - 1);
      const yStr = getDateKeyIST(y);
      setStartDate(yStr);
      setEndDate(yStr);
      loadData(yStr, yStr);
    } else if (preset === '7d') {
      const d = new Date(today);
      d.setDate(d.getDate() - 6);
      const sStr = getDateKeyIST(d);
      setStartDate(sStr);
      setEndDate(todayStr);
      loadData(sStr, todayStr);
    } else if (preset === '14d') {
      const d = new Date(today);
      d.setDate(d.getDate() - 13);
      const sStr = getDateKeyIST(d);
      setStartDate(sStr);
      setEndDate(todayStr);
      loadData(sStr, todayStr);
    } else if (preset === '30d') {
      const d = new Date(today);
      d.setDate(d.getDate() - 29);
      const sStr = getDateKeyIST(d);
      setStartDate(sStr);
      setEndDate(todayStr);
      loadData(sStr, todayStr);
    } else if (preset === 'thisMonth') {
      const first = new Date(today.getFullYear(), today.getMonth(), 1);
      const sStr = getDateKeyIST(first);
      setStartDate(sStr);
      setEndDate(todayStr);
      loadData(sStr, todayStr);
    }
    // 'custom' does not auto-fetch until user applies or picks date
  };

  const handleApplyCustomRange = () => {
    if (!startDate || !endDate) {
      alert('Please select both from and to dates.');
      return;
    }
    if (startDate > endDate) {
      alert('Start date must be before or equal to end date.');
      return;
    }
    loadData(startDate, endDate);
  };

  useEffect(() => {
    if (firebaseUser) {
      loadData(startDate, endDate);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [firebaseUser]);

  const handleSort = (field: keyof StudentSummary) => {
    if (sortField === field) {
      setSortDirection(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortField(field);
      setSortDirection(field === 'name' ? 'asc' : 'desc');
    }
  };

  const formatTimeSpent = (totalSeconds: number) => {
    if (!totalSeconds || totalSeconds <= 0) return '0s';
    if (totalSeconds < 60) return `${totalSeconds}s`;
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    if (mins < 60) {
      return `${mins}m ${secs}s`;
    }
    const hrs = Math.floor(mins / 60);
    const remMins = mins % 60;
    return `${hrs}h ${remMins}m`;
  };

  // Format date range nicely for display
  const formatDurationLabel = () => {
    if (startDate === endDate) {
      return formatDateDMY(startDate);
    }
    return `${formatDateDMY(startDate)} – ${formatDateDMY(endDate)}`;
  };

  // Calculate duration in days
  const durationDays = useMemo(() => {
    try {
      const d1 = new Date(startDate);
      const d2 = new Date(endDate);
      const diffTime = Math.abs(d2.getTime() - d1.getTime());
      const diffDays = Math.round(diffTime / (1000 * 60 * 60 * 24)) + 1;
      return Math.max(1, diffDays);
    } catch (_) {
      return 1;
    }
  }, [startDate, endDate]);

  const selectedBatchName = selectedBatchId === 'all' 
    ? 'All Batches' 
    : batches.find(b => b.id === selectedBatchId)?.name || 'Selected Batch';

  // Filtered students by batch and search (strictly excluding Limited Mode students)
  const filteredStudents = useMemo(() => {
    return students.filter(student => {
      if (getStudentMode(student) === 'limited') return false;
      if (selectedBatchId !== 'all') {
        const isInBatch = student.batchIds && student.batchIds.includes(selectedBatchId);
        if (!isInBatch) return false;
      }
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase();
        const matchesName = student.name.toLowerCase().includes(q);
        const matchesCode = (student.studentCode || '').toLowerCase().includes(q);
        if (!matchesName && !matchesCode) return false;
      }
      return true;
    });
  }, [students, selectedBatchId, searchQuery]);

  // Active in this selected duration (sessions > 0)
  const activeList = useMemo(() => {
    return filteredStudents.filter(s => s.sessionsCount > 0);
  }, [filteredStudents]);

  // Inactive in this selected duration (sessions === 0)
  const inactiveList = useMemo(() => {
    return filteredStudents.filter(s => s.sessionsCount === 0);
  }, [filteredStudents]);

  // Students who did not practice in this duration BUT HAVE ALREADY PRACTICED ON ALL ASSIGNED TOPICS!
  // "check if students have practiced on every topic assigned .. then they should be marked differently as they do not have anything to practice in that duration"
  const fullyCoveredInactiveList = useMemo(() => {
    return inactiveList.filter(s => {
      const total = s.totalAssignedTopics || 0;
      const attempted = s.topicsAttemptedCount || 0;
      return total > 0 && attempted >= total;
    });
  }, [inactiveList]);

  // Students who did not practice in this duration AND STILL HAVE UNATTEMPTED/PENDING TOPICS TO PRACTICE!
  const pendingPracticeInactiveList = useMemo(() => {
    const fullyCoveredSet = new Set(fullyCoveredInactiveList.map(s => s.studentCode));
    return inactiveList.filter(s => !fullyCoveredSet.has(s.studentCode));
  }, [inactiveList, fullyCoveredInactiveList]);

  // Sorted active students
  const sortedActiveStudents = useMemo(() => {
    return [...activeList].sort((a, b) => {
      let aVal = a[sortField];
      let bVal = b[sortField];

      if (typeof aVal === 'string' && typeof bVal === 'string') {
        return sortDirection === 'asc' 
          ? aVal.localeCompare(bVal) 
          : bVal.localeCompare(aVal);
      }

      const numA = Number(aVal || 0);
      const numB = Number(bVal || 0);
      return sortDirection === 'asc' ? numA - numB : numB - numA;
    });
  }, [activeList, sortField, sortDirection]);

  // Aggregate stats of current filtered selection
  const totalEnrolledCount = filteredStudents.length;
  const totalPracticedCount = activeList.length;
  const totalSessionsCount = activeList.reduce((sum, s) => sum + s.sessionsCount, 0);
  const totalQuestionsCount = activeList.reduce((sum, s) => sum + s.totalQuestions, 0);

  const sumAccuracy = activeList.reduce((sum, s) => sum + s.avgAccuracy, 0);
  const avgBatchAccuracy = totalPracticedCount > 0 ? parseFloat((sumAccuracy / totalPracticedCount).toFixed(1)) : 0;

  const sumHonesty = activeList.reduce((sum, s) => sum + s.avgHonesty, 0);
  const avgBatchIntegrity = totalPracticedCount > 0 ? parseFloat((sumHonesty / totalPracticedCount).toFixed(1)) : 100;

  const getLockTag = (student: StudentSummary) => {
    const hasLocks = student.activeLocks && student.activeLocks.length > 0;
    const lockCount = student.activeLocks ? student.activeLocks.length : 0;
    if (hasLocks) {
      const firstLock = student.activeLocks[0];
      const parts = firstLock.split(':');
      const code = parts[0] || 'Topic';
      const type = firstLock.includes('Quota') ? 'Quota' : (firstLock.includes('Daily') ? 'Daily' : 'Cooldown');
      const label = lockCount > 1 ? `🔒 ${lockCount} Locked` : `🔒 ${type} (${code})`;
      return (
        <span style={{ color: '#ef4444', fontSize: '11px', fontWeight: 800, display: 'inline-flex', alignItems: 'center', gap: '4px' }} title={student.activeLocks.join(', ')}>
          {label}
          {student.isAutonomous && <span style={{ color: 'var(--warning)', fontSize: '10px' }}>(Auto)</span>}
        </span>
      );
    }
    if (student.isAutonomous) {
      return <span style={{ color: 'var(--warning)', fontSize: '11px', fontWeight: 800 }}>🤖 Autonomous</span>;
    }
    return null;
  };

  // WhatsApp Image Export with clean separation of All Topics Covered vs Follow-up Required
  const handleExportWhatsAppImage = async () => {
    if (typeof window === 'undefined') return;
    if (filteredStudents.length === 0) {
      alert('No student data to export for this selection.');
      return;
    }

    setExportingImage(true);

    try {
      const html2canvas = await loadHtml2Canvas();
      if (!html2canvas) throw new Error('Could not initialize image export library.');

      const dateLabel = formatDurationLabel();
      const totalEnrolled = filteredStudents.length;
      const totalActive = activeList.length;
      const totalSessions = totalSessionsCount;
      const activeRate = totalEnrolled > 0 ? Math.round((totalActive / totalEnrolled) * 100) : 0;

      const container = document.createElement('div');
      container.style.position = 'fixed';
      container.style.left = '0';
      container.style.top = '0';
      container.style.width = '1080px';
      container.style.backgroundColor = '#ffffff';
      container.style.color = '#0f172a';
      container.style.fontFamily = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', sans-serif";
      (container.style as any).webkitFontSmoothing = 'antialiased';
      (container.style as any).mozOsxFontSmoothing = 'grayscale';
      (container.style as any).textRendering = 'optimizeLegibility';
      container.style.padding = '28px 32px';
      container.style.boxSizing = 'border-box';
      container.style.zIndex = '-9999';
      container.style.pointerEvents = 'none';
      container.style.opacity = '1';

      const activeRowsHtml = sortedActiveStudents.map((s, idx) => {
        const rank = idx + 1;
        const rankBadge = rank === 1 ? '🥇 1' : rank === 2 ? '🥈 2' : rank === 3 ? '🥉 3' : `<span style="display:inline-block; min-width: 24px; padding: 2px 6px; border-radius: 4px; background: #e2e8f0; color: #1e293b; font-weight: 800; font-size: 12px;">${rank}</span>`;
        const displayName = formatReportStudentName(s.name);
        const rowBg = idx % 2 === 0 ? '#ffffff' : '#f8fafc';

        const evalResult = evaluateStudentPracticeRemark(s, durationDays);
        const remarkHtml = `<span style="display:inline-block; padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 800; background: ${evalResult.bg}; color: ${evalResult.color}; border: ${evalResult.border || 'none'}; white-space: nowrap;">${evalResult.text}</span>`;

        const pendingTopics = s.totalAssignedTopics ? Math.max(0, s.totalAssignedTopics - (s.topicsAttemptedCount || 0)) : 0;
        const topicCoverageChip = s.totalAssignedTopics 
          ? `<span style="font-size: 11px; font-weight: 700; color: #475569;">${s.topicsAttemptedCount || 0}/${s.totalAssignedTopics}${pendingTopics > 0 ? ` <span style="font-size: 9.5px; color: #dc2626; font-weight: 800;">(${pendingTopics} pend)</span>` : ''}</span>`
          : '—';

        return `
          <tr style="background-color: ${rowBg}; border-bottom: 1px solid #e2e8f0;">
            <td style="padding: 10px 12px; font-weight: 800; text-align: center;">${rankBadge}</td>
            <td style="padding: 10px 12px; font-weight: 800; font-size: 13.5px; color: #0f172a;">${displayName}</td>
            <td style="padding: 10px 12px; text-align: center;">${topicCoverageChip}</td>
            <td style="padding: 10px 12px; font-weight: 800; text-align: center; color: #3b82f6;">${s.sessionsCount}</td>
            <td style="padding: 10px 12px; font-weight: 800; text-align: center; color: #6366f1;">${s.totalQuestions}</td>
            <td style="padding: 10px 12px; text-align: center;">${getScoreChip(s.avgAccuracy)}</td>
            <td style="padding: 10px 12px; text-align: center;">${getScoreChip(s.avgHonesty)}</td>
            <td style="padding: 10px 12px; text-align: center;">${getScoreChip(s.avgMastery)}</td>
            <td style="padding: 10px 12px; font-weight: 700; text-align: center; color: #475569; font-size: 12px;">${formatTimeSpent(s.totalTimeSpent)}</td>
            <td style="padding: 10px 12px; text-align: center;">${remarkHtml}</td>
          </tr>
        `;
      }).join('');

      // Section A: All Assigned Topics Practiced (No pending practice)
      const fullyCoveredSectionHtml = fullyCoveredInactiveList.length > 0 ? `
        <div style="margin-top: 16px; margin-bottom: 14px; padding: 14px 18px; border-radius: 10px; background: #ecfdf5; border: 1.5px solid #6ee7b7;">
          <div style="font-weight: 900; font-size: 13px; color: #065f46; margin-bottom: 6px; display: flex; align-items: center; justify-content: space-between;">
            <span>🎉 All Assigned Topics Practiced (${fullyCoveredInactiveList.length} Students)</span>
            <span style="font-size: 11px; font-weight: 800; color: #047857; background: #d1fae5; padding: 2px 8px; border-radius: 6px;">0 Pending Topics • Fully Caught Up</span>
          </div>
          <div style="font-size: 11.5px; color: #047857; margin-bottom: 8px;">These students have practiced on every topic currently assigned in this curriculum. They had no pending topics to practice in this duration.</div>
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px 12px; font-size: 12px; font-weight: 700; color: #065f46;">
            ${[...fullyCoveredInactiveList].sort((a, b) => a.name.localeCompare(b.name)).map(s => `<div>🟢 ${formatReportStudentName(s.name)}</div>`).join('')}
          </div>
        </div>
      ` : '';

      // Section B: Pending Practice Follow-Up Required
      const pendingSectionHtml = pendingPracticeInactiveList.length > 0 ? `
        <div style="margin-top: 14px; margin-bottom: 18px; padding: 14px 18px; border-radius: 10px; background: #fef2f2; border: 1.5px solid #fca5a5;">
          <div style="font-weight: 900; font-size: 13px; color: #991b1b; margin-bottom: 6px; display: flex; align-items: center; justify-content: space-between;">
            <span>🔴 Did Not Practice / Pending Practice (${pendingPracticeInactiveList.length} Students)</span>
            <span style="font-size: 11px; font-weight: 700; color: #b91c1c;">Follow-up required</span>
          </div>
          <div style="font-size: 11.5px; color: #991b1b; margin-bottom: 8px;">These students have unattempted assigned topics remaining and require encouragement to complete daily practice workouts.</div>
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px 12px; font-size: 12px; font-weight: 700; color: #7f1d1d;">
            ${[...pendingPracticeInactiveList].sort((a, b) => a.name.localeCompare(b.name)).map(s => `<div>• ${formatReportStudentName(s.name)}${s.unattemptedTopicsCount ? ` <span style="font-size: 10px; font-weight: 600; color: #b91c1c;">(${s.unattemptedTopicsCount} pending)</span>` : ''}</div>`).join('')}
          </div>
        </div>
      ` : '';

      container.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 16px; border-bottom: 2px solid #e2e8f0; margin-bottom: 16px;">
          <div>
            <div style="font-size: 20px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a; display: flex; align-items: center; gap: 8px;">
              <span>🏆 YASHCOM Learning OS</span>
              <span style="font-size: 12px; font-weight: 800; padding: 2px 8px; border-radius: 6px; background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe;">Practice Track Summary</span>
            </div>
            <div style="font-size: 13px; font-weight: 600; color: #64748b; margin-top: 4px;">
              <strong>Batch:</strong> ${selectedBatchName} &nbsp;•&nbsp; <strong>Duration:</strong> ${dateLabel}
            </div>
          </div>
          <div style="text-align: right;">
            <div style="font-size: 16px; font-weight: 900; color: #10b981;">
              ${activeRate}% Active
            </div>
            <div style="font-size: 11px; font-weight: 600; color: #94a3b8; margin-top: 2px;">
              Generated on ${new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' })}
            </div>
          </div>
        </div>

        <!-- KPI Strip -->
        <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-bottom: 16px;">
          <div style="padding: 10px 12px; border-radius: 8px; background: #f8fafc; border: 1.5px solid #e2e8f0; text-align: center;">
            <div style="font-size: 10.5px; font-weight: 800; color: #64748b; text-transform: uppercase;">Students Active</div>
            <div style="font-size: 20px; font-weight: 900; color: #0f172a; margin-top: 2px;">${totalActive} <span style="font-size: 11px; font-weight: 700; color: #94a3b8;">/ ${totalEnrolled}</span></div>
          </div>
          <div style="padding: 10px 12px; border-radius: 8px; background: #f8fafc; border: 1.5px solid #e2e8f0; text-align: center;">
            <div style="font-size: 10.5px; font-weight: 800; color: #64748b; text-transform: uppercase;">All Topics Done</div>
            <div style="font-size: 20px; font-weight: 900; color: #10b981; margin-top: 2px;">${fullyCoveredInactiveList.length}</div>
          </div>
          <div style="padding: 10px 12px; border-radius: 8px; background: #f8fafc; border: 1.5px solid #e2e8f0; text-align: center;">
            <div style="font-size: 10.5px; font-weight: 800; color: #64748b; text-transform: uppercase;">Sessions Done</div>
            <div style="font-size: 20px; font-weight: 900; color: #3b82f6; margin-top: 2px;">${totalSessions}</div>
          </div>
          <div style="padding: 10px 12px; border-radius: 8px; background: #f8fafc; border: 1.5px solid #e2e8f0; text-align: center;">
            <div style="font-size: 10.5px; font-weight: 800; color: #64748b; text-transform: uppercase;">Avg Accuracy</div>
            <div style="font-size: 20px; font-weight: 900; color: #10b981; margin-top: 2px;">${avgBatchAccuracy}%</div>
          </div>
          <div style="padding: 10px 12px; border-radius: 8px; background: #f8fafc; border: 1.5px solid #e2e8f0; text-align: center;">
            <div style="font-size: 10.5px; font-weight: 800; color: #64748b; text-transform: uppercase;">Avg Integrity</div>
            <div style="font-size: 20px; font-weight: 900; color: #8b5cf6; margin-top: 2px;">${avgBatchIntegrity}%</div>
          </div>
        </div>

        ${fullyCoveredSectionHtml}
        ${pendingSectionHtml}

        <!-- Active Students Table -->
        ${sortedActiveStudents.length > 0 ? `
          <div style="border-radius: 8px; border: 1.5px solid #e2e8f0; overflow: hidden; margin-bottom: 14px;">
            <table style="width: 100%; border-collapse: collapse; font-size: 12px;">
              <thead>
                <tr style="background: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
                  <th style="padding: 8px 10px; font-weight: 800; text-align: center; color: #475569; width: 44px;">Rank</th>
                  <th style="padding: 8px 10px; font-weight: 800; text-align: left; color: #475569;">Student</th>
                  <th style="padding: 8px 10px; font-weight: 800; text-align: center; color: #475569;">Coverage</th>
                  <th style="padding: 8px 10px; font-weight: 800; text-align: center; color: #475569;">Sessions</th>
                  <th style="padding: 8px 10px; font-weight: 800; text-align: center; color: #475569;">Questions</th>
                  <th style="padding: 8px 10px; font-weight: 800; text-align: center; color: #475569;">Accuracy</th>
                  <th style="padding: 8px 10px; font-weight: 800; text-align: center; color: #475569;">Integrity</th>
                  <th style="padding: 8px 10px; font-weight: 800; text-align: center; color: #475569;">Mastery</th>
                  <th style="padding: 8px 10px; font-weight: 800; text-align: center; color: #475569;">Time</th>
                  <th style="padding: 8px 10px; font-weight: 800; text-align: center; color: #475569;">Remark</th>
                </tr>
              </thead>
              <tbody>
                ${activeRowsHtml}
              </tbody>
            </table>
          </div>
        ` : `
          <div style="padding: 24px; text-align: center; background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 8px; font-weight: 700; color: #64748b;">
            No active practice sessions recorded during this duration.
          </div>
        `}

        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 10px; border-top: 1px solid #e2e8f0; font-size: 11px; font-weight: 700; color: #94a3b8;">
          <span>Official Yashcom Learning OS Report</span>
          <span>Single Source of Truth (SSOT) Practice Metrics</span>
        </div>
      `;

      document.body.appendChild(container);

      const canvas = await html2canvas(container, {
        scale: 2,
        useCORS: true,
        backgroundColor: '#ffffff'
      });

      document.body.removeChild(container);

      const blob: Blob = await new Promise((resolve, reject) => {
        canvas.toBlob((b: Blob | null) => {
          if (b) resolve(b);
          else reject(new Error('Failed to generate image blob from canvas.'));
        }, 'image/png');
      });

      const cleanBatch = selectedBatchName.replace(/[^a-zA-Z0-9_-]/g, '_');
      const fileName = `Practice_Track_${cleanBatch}_${startDate}_to_${endDate}.png`;
      const imageUri = canvas.toDataURL('image/png');

      // 1. Copy lossless PNG to clipboard for instant Ctrl+V
      let copiedToClipboard = false;
      if (typeof navigator !== 'undefined' && navigator.clipboard && typeof ClipboardItem !== 'undefined') {
        try {
          await navigator.clipboard.write([
            new ClipboardItem({ 'image/png': blob })
          ]);
          copiedToClipboard = true;
        } catch (clipErr) {
          console.warn('Clipboard write attempt 1 failed, trying fallback:', clipErr);
          try {
            await navigator.clipboard.write([
              new ClipboardItem({ 'image/png': Promise.resolve(blob) })
            ]);
            copiedToClipboard = true;
          } catch (clipErr2) {
            console.warn('Clipboard write fallback failed:', clipErr2);
          }
        }
      }

      // 2. Trigger lossless PNG download
      const downloadLink = document.createElement('a');
      downloadLink.download = fileName;
      downloadLink.href = imageUri;
      document.body.appendChild(downloadLink);
      downloadLink.click();
      setTimeout(() => {
        try { document.body.removeChild(downloadLink); } catch (_) {}
      }, 100);

      playNotificationSound();

      if (copiedToClipboard) {
        setCopiedRecently(true);
        setTimeout(() => setCopiedRecently(false), 4000);
        alert(`✅ WhatsApp Report Card Copied & Downloaded!\n\n1. Copied to Clipboard! You can directly press Ctrl + V in WhatsApp.\n2. Also downloaded as ${fileName}`);
      } else {
        alert(`✅ WhatsApp Report Card downloaded as ${fileName}!\n(Image downloaded to your computer for WhatsApp sharing).`);
      }
    } catch (err: any) {
      console.error('Error generating WhatsApp export:', err);
      alert('Failed to generate export card: ' + (err.message || 'Unknown error'));
    } finally {
      setExportingImage(false);
    }
  };

  const getPresetBtnStyle = (isActive: boolean) => ({
    padding: '5px 11px',
    fontSize: '11.5px',
    fontWeight: 700,
    borderRadius: '6px',
    border: '1px solid ' + (isActive ? 'var(--primary)' : 'var(--border-light)'),
    cursor: 'pointer',
    background: isActive ? 'var(--primary)' : 'var(--bg-soft)',
    color: isActive ? '#ffffff' : 'var(--text-muted)',
    transition: 'all 0.15s ease',
    whiteSpace: 'nowrap' as const
  });

  return (
    <div style={{ background: 'var(--bg)', flex: 1, display: 'flex', flexDirection: 'column' }}>
      
      {/* Printable CSS Override Block */}
      <style jsx global>{`
        @media print {
          body {
            background: white !important;
            color: black !important;
            font-size: 11px !important;
          }
          .no-print, nav, header, select, button, .page-header, .sidebar, .card:not(.print-table-card) {
            display: none !important;
          }
          .print-header-info {
            display: block !important;
            margin-bottom: 20px !important;
          }
          .print-table-card {
            border: none !important;
            box-shadow: none !important;
            background: transparent !important;
            padding: 0 !important;
            margin: 0 !important;
          }
          table {
            width: 100% !important;
            border-collapse: collapse !important;
            margin-top: 15px !important;
          }
          th, td {
            border: 1px solid var(--border) !important;
            padding: 6px 8px !important;
            text-align: left !important;
          }
          th {
            background-color: var(--surface-2) !important;
            color: var(--text) !important;
            font-weight: 700 !important;
          }
        }
        .print-header-info {
          display: none;
        }
        .sortable-th {
          cursor: pointer;
          user-select: none;
          transition: background-color 0.2s ease;
        }
        .sortable-th:hover {
          background-color: var(--bg-hover) !important;
        }
      `}</style>

      {/* Reports Sub-Navigation Bar (Hidden on Print) */}
      <div className="no-print" style={{ maxWidth: '1400px', width: '100%', margin: '0 auto', padding: '10px 16px 0 16px' }}>
        <nav style={{ display: 'flex', gap: '14px', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px', overflowX: 'auto' }}>
          <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports')}>
            ⚡ Daily Intervention Queue
          </span>
          <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--accent)', borderBottom: '2px solid var(--accent)', paddingBottom: '4px', whiteSpace: 'nowrap' }}>
            📝 Practice Track Report
          </span>
          <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/remediation')}>
            🎯 Topic Remediation Tracker
          </span>
          <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/learning-quotient')}>
            📊 Student Learning Profiles (LQ)
          </span>
          <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/usage')}>
            🛡️ System Health & Audit
          </span>
        </nav>
      </div>

      {/* Header Info Block (Only visible on Print) */}
      <div className="print-header-info">
        <h2 style={{ margin: '0 0 5px 0', color: 'var(--text)' }}>Yashcom Foundation - Practice Track Summary</h2>
        <div style={{ fontSize: '12px', color: 'var(--text-muted)', borderBottom: '2px solid var(--text)', paddingBottom: '10px' }}>
          <strong>Batch:</strong> {selectedBatchName} | <strong>Duration:</strong> {formatDurationLabel()} | <strong>Exported:</strong> {new Date().toLocaleTimeString('en-IN')}
        </div>
        <div style={{ display: 'flex', gap: '20px', marginTop: '10px', fontSize: '11px' }}>
          <span><strong>Total Students Practiced:</strong> {totalPracticedCount}</span>
          <span><strong>Total Practice Sessions:</strong> {totalSessionsCount}</span>
          <span><strong>Avg Accuracy:</strong> {avgBatchAccuracy}%</span>
          <span><strong>Avg Integrity:</strong> {avgBatchIntegrity}%</span>
        </div>
      </div>

      <main style={{ flex: 1, padding: '16px', maxWidth: '1400px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '14px' }}>
        
        {/* Page Title & Subtitle */}
        <div className="no-print" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <h2 style={{ fontSize: '19px', fontWeight: 800, color: 'var(--text)', margin: 0 }}>
                📝 Practice Track & Daily Report
              </h2>
              <span style={{
                fontSize: '11px',
                fontWeight: 700,
                padding: '2px 8px',
                borderRadius: '8px',
                background: 'rgba(16, 185, 129, 0.12)',
                color: 'var(--success, #10b981)'
              }}>
                Multi-Day Duration & Topic Breadth
              </span>
            </div>
            <p style={{ fontSize: '12.5px', color: 'var(--text-muted)', margin: '4px 0 0 0' }}>
              Track student self-practice sessions, problem accuracy, and topic completion across any duration or single date.
            </p>
          </div>

          <div>
            <button 
              className="btn"
              onClick={handleExportWhatsAppImage}
              disabled={exportingImage || loading}
              style={{ 
                display: 'inline-flex', 
                alignItems: 'center', 
                gap: '6px', 
                fontSize: '12.5px', 
                fontWeight: 700, 
                padding: '7px 16px',
                background: copiedRecently 
                  ? 'linear-gradient(135deg, #059669 0%, #047857 100%)' 
                  : 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
                color: '#ffffff',
                border: 'none',
                borderRadius: 'var(--radius-sm, 6px)',
                cursor: (exportingImage || loading) ? 'wait' : 'pointer',
                boxShadow: copiedRecently 
                  ? '0 2px 10px rgba(5, 150, 105, 0.5)' 
                  : '0 2px 8px rgba(16, 185, 129, 0.3)',
                transition: 'all 0.2s ease'
              }}
              title="Copy lossless card to clipboard and download for WhatsApp sharing"
            >
              {exportingImage ? '⏳ Generating Card...' : copiedRecently ? '📋 Copied to Clipboard!' : '📸 WhatsApp Report Card'}
            </button>
          </div>
        </div>

        {/* Toolbar Controls (Hidden on Print) */}
        <div className="card glass no-print" style={{ padding: '14px 16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '12px' }}>
          
          {/* Row 1: Duration Presets & Range */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '10px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
              <span style={{ fontSize: '11.5px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', marginRight: '4px' }}>
                Duration:
              </span>
              <button type="button" onClick={() => handlePresetChange('today')} style={getPresetBtnStyle(durationPreset === 'today')}>
                Today
              </button>
              <button type="button" onClick={() => handlePresetChange('yesterday')} style={getPresetBtnStyle(durationPreset === 'yesterday')}>
                Yesterday
              </button>
              <button type="button" onClick={() => handlePresetChange('7d')} style={getPresetBtnStyle(durationPreset === '7d')}>
                Last 7 Days
              </button>
              <button type="button" onClick={() => handlePresetChange('14d')} style={getPresetBtnStyle(durationPreset === '14d')}>
                Last 14 Days
              </button>
              <button type="button" onClick={() => handlePresetChange('30d')} style={getPresetBtnStyle(durationPreset === '30d')}>
                Last 30 Days
              </button>
              <button type="button" onClick={() => handlePresetChange('thisMonth')} style={getPresetBtnStyle(durationPreset === 'thisMonth')}>
                This Month
              </button>
              <button type="button" onClick={() => setDurationPreset('custom')} style={getPresetBtnStyle(durationPreset === 'custom')}>
                Custom Range
              </button>
            </div>

            {/* Active Duration Display Badge & Live Refresh */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{
                fontSize: '11.5px',
                fontWeight: 700,
                padding: '4px 10px',
                borderRadius: '6px',
                background: 'rgba(59, 130, 246, 0.12)',
                color: 'var(--primary, #3b82f6)',
                border: '1px solid rgba(59, 130, 246, 0.25)'
              }}>
                📅 {formatDurationLabel()}
              </span>
              <button
                type="button"
                onClick={() => loadData(startDate, endDate, true)}
                disabled={loading}
                title="Force refresh live database records"
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px',
                  padding: '4px 10px',
                  fontSize: '11.5px',
                  fontWeight: 700,
                  borderRadius: '6px',
                  background: 'var(--surface, #fff)',
                  border: '1px solid var(--border, #e2e8f0)',
                  cursor: loading ? 'not-allowed' : 'pointer',
                  color: 'var(--text)'
                }}
              >
                {loading ? '⏳' : '🔄 Refresh'}
              </button>
            </div>
          </div>

          {/* Row 2: Custom Date Inputs (when 'custom' preset is selected) */}
          {durationPreset === 'custom' && (
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap', padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: '6px', border: '1px solid var(--border-light)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)' }}>From:</span>
                <DateInputDMY value={startDate} onChange={(val) => setStartDate(val)} style={{ width: '135px' }} inputStyle={{ padding: '6px 24px 6px 8px', background: 'var(--surface)', fontWeight: 700, fontSize: '12px' }} />
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)' }}>To:</span>
                <DateInputDMY value={endDate} onChange={(val) => setEndDate(val)} style={{ width: '135px' }} inputStyle={{ padding: '6px 24px 6px 8px', background: 'var(--surface)', fontWeight: 700, fontSize: '12px' }} />
              </div>
              <button 
                type="button" 
                onClick={handleApplyCustomRange}
                disabled={loading}
                style={{
                  padding: '6px 14px',
                  fontSize: '12px',
                  fontWeight: 700,
                  borderRadius: '6px',
                  background: 'var(--primary)',
                  color: '#ffffff',
                  border: 'none',
                  cursor: loading ? 'wait' : 'pointer'
                }}
              >
                Apply Range ➔
              </button>
            </div>
          )}

          {/* Row 3: Batch Selector and Search */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '12px', borderTop: '1px solid var(--border-light)', paddingTop: '10px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '14px', flexWrap: 'wrap' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)' }}>Batch:</span>
                <select
                  value={selectedBatchId}
                  onChange={(e) => setSelectedBatchId(e.target.value)}
                  style={{
                    padding: '6px 12px',
                    borderRadius: 'var(--radius-sm)',
                    border: '1px solid var(--border-light)',
                    background: 'var(--bg-soft)',
                    color: 'var(--text)',
                    fontSize: '12px',
                    fontWeight: 700,
                    cursor: 'pointer'
                  }}
                >
                  <option value="all">🌐 All Batches</option>
                  {batches.map(b => (
                    <option key={b.id} value={b.id}>📦 {b.name}</option>
                  ))}
                </select>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)' }}>Search:</span>
                <input
                  type="text"
                  placeholder="Student name..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  style={{
                    padding: '6px 10px',
                    borderRadius: 'var(--radius-sm)',
                    border: '1px solid var(--border-light)',
                    background: 'var(--bg-soft)',
                    color: 'var(--text)',
                    fontSize: '12px',
                    width: '180px'
                  }}
                />
              </div>
            </div>

            <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)' }}>
              Showing {filteredStudents.length} Students ({totalPracticedCount} Practiced)
            </div>
          </div>
        </div>

        {/* Stats Cards Row (Hidden on Print) */}
        <div className="no-print" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '12px' }}>
          <div className="card glass" style={{ padding: '12px 14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '10.5px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Active Students</div>
            <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--accent)', marginTop: '2px' }}>
              {totalPracticedCount} <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)' }}>/ {totalEnrolledCount}</span>
            </div>
          </div>
          <div className="card glass" style={{ padding: '12px 14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '10.5px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>All Topics Done</div>
            <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--success, #10b981)', marginTop: '2px' }}>
              {fullyCoveredInactiveList.length} <span style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>caught up</span>
            </div>
          </div>
          <div className="card glass" style={{ padding: '12px 14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '10.5px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Sessions Done</div>
            <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--primary, #3b82f6)', marginTop: '2px' }}>{totalSessionsCount}</div>
          </div>
          <div className="card glass" style={{ padding: '12px 14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '10.5px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Questions Solved</div>
            <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#6366f1', marginTop: '2px' }}>{totalQuestionsCount}</div>
          </div>
          <div className="card glass" style={{ padding: '12px 14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '10.5px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Avg Accuracy</div>
            <div style={{ fontSize: '1.6rem', fontWeight: 800, color: 'var(--success)', marginTop: '2px' }}>{avgBatchAccuracy}%</div>
          </div>
          <div className="card glass" style={{ padding: '12px 14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '10.5px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Avg Integrity</div>
            <div style={{ fontSize: '1.6rem', fontWeight: 800, color: avgBatchIntegrity < 85 ? 'var(--warning)' : 'var(--accent)', marginTop: '2px' }}>{avgBatchIntegrity}%</div>
          </div>
        </div>

        {/* Data Table */}
        <div className="card glass print-table-card" style={{ borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
          {loading ? (
            <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '60px 0' }}>
              <div className="spinner"></div>
              <span style={{ marginLeft: '10px', fontWeight: 600, color: 'var(--text-muted)' }}>Loading practice track data...</span>
            </div>
          ) : filteredStudents.length === 0 ? (
            <div style={{ textAlign: 'center', padding: '60px 20px', color: 'var(--text-muted)' }}>
              📭 No student practice data found for {selectedBatchName} during {formatDurationLabel()}.
            </div>
          ) : (
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                    <th 
                      onClick={() => handleSort('name')}
                      className="sortable-th"
                      style={{ padding: '10px 14px', textAlign: 'left', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Student Name {sortField === 'name' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Topic Coverage
                    </th>
                    <th 
                      onClick={() => handleSort('sessionsCount')}
                      className="sortable-th"
                      style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Sessions {sortField === 'sessionsCount' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('totalQuestions')}
                      className="sortable-th"
                      style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Questions {sortField === 'totalQuestions' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('avgAccuracy')}
                      className="sortable-th"
                      style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Accuracy {sortField === 'avgAccuracy' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('avgHonesty')}
                      className="sortable-th"
                      style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Integrity {sortField === 'avgHonesty' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('avgMastery')}
                      className="sortable-th"
                      style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Mastery {sortField === 'avgMastery' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('totalTimeSpent')}
                      className="sortable-th"
                      style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Time Spent {sortField === 'totalTimeSpent' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Status / Remark
                    </th>
                  </tr>
                </thead>
                <tbody>

                  {/* ─────────────────────────────────────────────────────────────
                      SECTION 1: STUDENTS WHO PRACTICED ALL ASSIGNED TOPICS
                      (Did not practice in this duration ONLY because they have 0 pending topics!)
                     ───────────────────────────────────────────────────────────── */}
                  {fullyCoveredInactiveList.length > 0 && (
                    <tr style={{ borderBottom: '1px solid var(--border-light)', background: 'rgba(16, 185, 129, 0.08)' }}>
                      <td colSpan={9} style={{ padding: '12px 16px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '6px', flexWrap: 'wrap', gap: '6px' }}>
                          <span style={{ fontWeight: 800, fontSize: '13px', color: '#047857' }}>
                            🎉 All Assigned Topics Practiced ({fullyCoveredInactiveList.length} Students)
                          </span>
                          <span style={{ fontSize: '11px', fontWeight: 700, color: '#065f46', background: '#d1fae5', padding: '2px 8px', borderRadius: '4px' }}>
                            0 Pending Topics • Fully Caught Up
                          </span>
                        </div>
                        <div style={{ fontSize: '12px', color: '#047857', marginBottom: '8px' }}>
                          These students have practiced on every topic currently assigned in their syllabus. They had no pending topics to practice in this selected duration.
                        </div>
                        <div style={{ 
                          display: 'grid', 
                          gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', 
                          gap: '6px 12px',
                          fontSize: '12.5px',
                          fontWeight: 700,
                          color: '#065f46'
                        }}>
                          {[...fullyCoveredInactiveList]
                            .sort((a, b) => a.name.localeCompare(b.name))
                            .map(s => (
                              <div key={s.studentCode} style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                                <span>🟢 {s.name}</span>
                                <span style={{ fontSize: '10.5px', fontWeight: 700, color: '#047857', background: '#d1fae5', padding: '1px 6px', borderRadius: '4px' }}>
                                  100% Topics Covered
                                </span>
                              </div>
                            ))
                          }
                        </div>
                      </td>
                    </tr>
                  )}

                  {/* ─────────────────────────────────────────────────────────────
                      SECTION 2: STUDENTS WHO DID NOT PRACTICE & HAVE PENDING TOPICS
                      (Follow-up required!)
                     ───────────────────────────────────────────────────────────── */}
                  {pendingPracticeInactiveList.length > 0 && (
                    <tr style={{ borderBottom: '1px solid var(--border-light)', background: 'var(--danger-bg)' }}>
                      <td colSpan={9} style={{ padding: '12px 16px', color: 'var(--danger)' }}>
                        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '6px', flexWrap: 'wrap', gap: '6px' }}>
                          <span style={{ fontWeight: 800, fontSize: '13px', color: 'var(--danger)' }}>
                            🔴 Did Not Practice / Pending Practice ({pendingPracticeInactiveList.length} Students)
                          </span>
                          <span style={{ fontSize: '11px', fontWeight: 700, color: '#991b1b', background: '#fee2e2', padding: '2px 8px', borderRadius: '4px' }}>
                            Follow-up required
                          </span>
                        </div>
                        <div style={{ fontSize: '12px', color: 'var(--danger)', marginBottom: '8px' }}>
                          These students did not practice in this duration and still have unattempted assigned topics waiting to be practiced.
                        </div>
                        <div style={{ 
                          display: 'grid', 
                          gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', 
                          gap: '6px 12px',
                          fontSize: '12.5px',
                          fontWeight: 700,
                          color: 'var(--danger)'
                        }}>
                          {[...pendingPracticeInactiveList]
                            .sort((a, b) => a.name.localeCompare(b.name))
                            .map(a => (
                              <div key={a.studentCode} style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', display: 'flex', alignItems: 'center', gap: '6px' }}>
                                <span>• {a.name}</span>
                                {a.unattemptedTopicsCount ? (
                                  <span style={{ fontSize: '10.5px', fontWeight: 700, color: '#991b1b', background: '#fee2e2', padding: '1px 6px', borderRadius: '4px' }}>
                                    {a.unattemptedTopicsCount} topic(s) pending
                                  </span>
                                ) : null}
                                {getLockTag(a)}
                              </div>
                            ))
                          }
                        </div>
                      </td>
                    </tr>
                  )}

                  {/* ─────────────────────────────────────────────────────────────
                      SECTION 3: ACTIVE STUDENTS WHO PRACTICED IN THIS DURATION
                     ───────────────────────────────────────────────────────────── */}
                  {sortedActiveStudents.length === 0 ? (
                    <tr>
                      <td colSpan={9} style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
                        📭 No active practice sessions completed in this duration.
                      </td>
                    </tr>
                  ) : (
                    sortedActiveStudents.map((row, idx) => {
                      const evalResult = evaluateStudentPracticeRemark(row, durationDays);
                      const pendingTopics = row.totalAssignedTopics ? Math.max(0, row.totalAssignedTopics - (row.topicsAttemptedCount || 0)) : 0;

                      return (
                        <tr 
                          key={row.studentCode} 
                          style={{ 
                            borderBottom: idx === sortedActiveStudents.length - 1 ? 'none' : '1px solid var(--border-light)',
                            background: idx % 2 === 1 ? 'var(--bg-soft-even)' : 'transparent'
                          }}
                        >
                          <td style={{ padding: '10px 14px', fontWeight: 600 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                              <span>{row.name}</span>
                              {getLockTag(row)}
                            </div>
                          </td>
                          <td style={{ padding: '10px 14px', textAlign: 'center' }}>
                            {row.totalAssignedTopics ? (
                              <div style={{ display: 'inline-flex', flexDirection: 'column', alignItems: 'center', gap: '2px' }}>
                                <span style={{ 
                                  fontSize: '11.5px', 
                                  fontWeight: 800, 
                                  padding: '2px 8px',
                                  borderRadius: '4px',
                                  background: (row.topicsAttemptedCount || 0) >= row.totalAssignedTopics ? '#dcfce7' : 'var(--bg-soft)',
                                  color: (row.topicsAttemptedCount || 0) >= row.totalAssignedTopics ? '#14532d' : 'var(--text)',
                                  border: '1px solid ' + ((row.topicsAttemptedCount || 0) >= row.totalAssignedTopics ? '#86efac' : 'var(--border-light)')
                                }}>
                                  {row.topicsAttemptedCount || 0} / {row.totalAssignedTopics}
                                </span>
                                {pendingTopics > 0 ? (
                                  <span style={{ fontSize: '10px', fontWeight: 800, color: 'var(--danger, #ef4444)' }}>
                                    {pendingTopics} pending
                                  </span>
                                ) : (
                                  <span style={{ fontSize: '10px', fontWeight: 800, color: '#16a34a' }}>
                                    100% Covered
                                  </span>
                                )}
                              </div>
                            ) : (
                              <span style={{ color: 'var(--text-muted)' }}>—</span>
                            )}
                          </td>
                          <td style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 700 }}>
                            {row.sessionsCount}
                          </td>
                          <td style={{ padding: '10px 14px', textAlign: 'center', fontWeight: 700, color: 'var(--accent)' }}>
                            {row.totalQuestions}
                          </td>
                          <td style={{ padding: '10px 14px', textAlign: 'center' }}>
                            <span style={{ color: 'var(--success)', fontWeight: 700 }}>{row.avgAccuracy}%</span>
                          </td>
                          <td style={{ padding: '10px 14px', textAlign: 'center' }}>
                            <span style={{ 
                              color: row.avgHonesty < 70 ? 'var(--error)' : (row.avgHonesty < 90 ? 'var(--warning)' : 'var(--success)'),
                              fontWeight: 700
                            }}>
                              {row.avgHonesty}%
                            </span>
                          </td>
                          <td style={{ padding: '10px 14px', textAlign: 'center' }}>
                            <span style={{ color: 'var(--accent)', fontWeight: 700 }}>{row.avgMastery}%</span>
                          </td>
                          <td style={{ padding: '10px 14px', textAlign: 'center' }}>
                            {formatTimeSpent(row.totalTimeSpent)}
                          </td>
                          <td style={{ padding: '10px 14px', textAlign: 'center' }}>
                            <span style={{ 
                              display: 'inline-block', 
                              padding: '3px 8px', 
                              borderRadius: '6px', 
                              fontSize: '11px', 
                              fontWeight: 800, 
                              background: evalResult.bg, 
                              color: evalResult.color, 
                              border: evalResult.border || 'none',
                              whiteSpace: 'nowrap'
                            }}>
                              {evalResult.text}
                            </span>
                          </td>
                        </tr>
                      );
                    })
                  )}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
