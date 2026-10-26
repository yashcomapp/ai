'use client';

import DateInputDMY from '@/components/DateInputDMY';

import React, { useEffect, useState, useMemo, useDeferredValue } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import { formatDateDMY } from '@/lib/dateUtils';
import { loadHtml2Canvas, formatReportStudentName, getScoreChip } from '@/lib/lqCardExport';
import { playNotificationSound } from '@/lib/audioUtils';

interface StudentSummary {
  studentCode: string;
  name: string;
  batchIds: string[];
  className: string;
  isAutonomous: boolean;
  activeLocks: string[];
  sessionsCount: number;
  avgAccuracy: number;
  avgHonesty: number; // Stored in backend as avgHonesty
  avgMastery: number;
  totalQuestions: number;
  totalTimeSpent: number;
}

export default function DailyPracticeSummaryPage() {
  const { firebaseUser, user } = useAuth();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [students, setStudents] = useState<StudentSummary[]>([]);
  const [batches, setBatches] = useState<{ id: string; name: string }[]>([]);
  const [selectedBatchId, setSelectedBatchId] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState<string>('');
  
  // Format current date in IST timezone as YYYY-MM-DD
  const getTodayISTStr = () => {
    return new Date().toLocaleDateString('en-CA', { timeZone: 'Asia/Kolkata' });
  };
  const [selectedDate, setSelectedDate] = useState<string>(getTodayISTStr());

  // Sorting state
  const [sortField, setSortField] = useState<keyof StudentSummary>('name');
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc');

  // Client-side authentication check
  useEffect(() => {
    if (user && (user as any).role !== 'admin') {
      router.replace('/student');
    }
  }, [user, router]);

  const loadData = async (dateVal: string) => {
    setLoading(true);
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/reports/daily-practice?date=${dateVal}&refresh=true`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (res.ok) {
        const data = await res.json();
        setStudents(data.students || []);
        setBatches(data.batches || []);
      }
    } catch (e) {
      console.error('Error loading daily practice summary:', e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (firebaseUser) {
      loadData(selectedDate);
    }
  }, [firebaseUser, selectedDate]);

  const handleSort = (field: keyof StudentSummary) => {
    if (sortField === field) {
      setSortDirection(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortField(field);
      setSortDirection(field === 'name' ? 'asc' : 'desc');
    }
  };

  const [exportingImage, setExportingImage] = useState(false);

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

  const handleExportWhatsAppImage = async () => {
    if (typeof window === 'undefined') return;
    if (filteredStudents.length === 0) {
      alert('No student data to export for this date and batch.');
      return;
    }

    setExportingImage(true);

    try {
      const html2canvas = await loadHtml2Canvas();
      if (!html2canvas) throw new Error('Could not initialize image export library.');

      const dateLabel = formatDisplayDate(selectedDate);
      const totalEnrolled = filteredStudents.length;
      const totalActive = activeList.length;
      const totalSessions = activeList.reduce((sum, s) => sum + s.sessionsCount, 0);
      const activeRate = totalEnrolled > 0 ? Math.round((totalActive / totalEnrolled) * 100) : 0;

      // Create offscreen container styled with ultra-crisp typography on clean white background
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

      // Build active table rows
      const activeRowsHtml = sortedActiveStudents.map((s, idx) => {
        const rank = idx + 1;
        const rankBadge = rank === 1 ? '🥇 1' : rank === 2 ? '🥈 2' : rank === 3 ? '🥉 3' : `<span style="display:inline-block; min-width: 24px; padding: 2px 6px; border-radius: 4px; background: #e2e8f0; color: #1e293b; font-weight: 800; font-size: 12px;">${rank}</span>`;
        const displayName = formatReportStudentName(s.name);
        const rowBg = idx % 2 === 0 ? '#ffffff' : '#f8fafc';

        let remarkHtml = '';
        if (s.avgAccuracy >= 90) {
          remarkHtml = `<span style="display:inline-block; padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 800; background: #dcfce7; color: #14532d; border: 1.5px solid #86efac; white-space: nowrap;">🌟 Outstanding</span>`;
        } else if (s.avgAccuracy >= 75) {
          remarkHtml = `<span style="display:inline-block; padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 800; background: #e0f2fe; color: #0369a1; border: 1.5px solid #7dd3fc; white-space: nowrap;">✅ Strong</span>`;
        } else if (s.avgAccuracy >= 50) {
          remarkHtml = `<span style="display:inline-block; padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 800; background: #fef9c3; color: #854d0e; border: 1.5px solid #fde047; white-space: nowrap;">🟡 Moderate</span>`;
        } else {
          remarkHtml = `<span style="display:inline-block; padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 800; background: #fee2e2; color: #991b1b; border: 1.5px solid #fca5a5; white-space: nowrap;">⚠️ Needs Practice</span>`;
        }

        return `
          <tr style="background-color: ${rowBg}; border-bottom: 1px solid #e2e8f0;">
            <td style="padding: 10px 12px; font-weight: 800; text-align: center;">${rankBadge}</td>
            <td style="padding: 10px 12px; font-weight: 800; font-size: 13.5px; color: #0f172a;">${displayName}</td>
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

      // Build inactive section if any students didn't practice
      const inactiveNamesHtml = inactiveList.length > 0 ? `
        <div style="margin-top: 18px; margin-bottom: 18px; padding: 14px 18px; border-radius: 10px; background: #fef2f2; border: 1.5px solid #fca5a5;">
          <div style="font-weight: 900; font-size: 13px; color: #991b1b; margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between;">
            <span>🔴 Did Not Practice Today (${inactiveList.length} Students)</span>
            <span style="font-size: 11px; font-weight: 700; color: #b91c1c;">Follow-up required</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px 12px; font-size: 12px; font-weight: 700; color: #7f1d1d;">
            ${[...inactiveList].sort((a, b) => a.name.localeCompare(b.name)).map(s => `<div>• ${formatReportStudentName(s.name)}</div>`).join('')}
          </div>
        </div>
      ` : '';

      container.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 16px; border-bottom: 2px solid #e2e8f0; margin-bottom: 16px;">
          <div>
            <div style="font-size: 20px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a; display: flex; align-items: center; gap: 8px;">
              <span>🏆 YASHCOM Learning OS</span>
              <span style="font-size: 12px; font-weight: 800; padding: 2px 8px; border-radius: 6px; background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe;">Daily Practice Summary</span>
            </div>
            <div style="font-size: 13px; font-weight: 600; color: #64748b; margin-top: 4px;">
              <strong>Batch:</strong> ${selectedBatchName} &nbsp;•&nbsp; <strong>Date:</strong> ${dateLabel}
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
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px;">
          <div style="padding: 12px 14px; border-radius: 8px; background: #f8fafc; border: 1.5px solid #e2e8f0; text-align: center;">
            <div style="font-size: 11px; font-weight: 800; color: #64748b; text-transform: uppercase;">Students Active</div>
            <div style="font-size: 22px; font-weight: 900; color: #0f172a; margin-top: 2px;">${totalActive} <span style="font-size: 12px; font-weight: 700; color: #94a3b8;">/ ${totalEnrolled}</span></div>
          </div>
          <div style="padding: 12px 14px; border-radius: 8px; background: #f8fafc; border: 1.5px solid #e2e8f0; text-align: center;">
            <div style="font-size: 11px; font-weight: 800; color: #64748b; text-transform: uppercase;">Sessions Done</div>
            <div style="font-size: 22px; font-weight: 900; color: #3b82f6; margin-top: 2px;">${totalSessions}</div>
          </div>
          <div style="padding: 12px 14px; border-radius: 8px; background: #f8fafc; border: 1.5px solid #e2e8f0; text-align: center;">
            <div style="font-size: 11px; font-weight: 800; color: #64748b; text-transform: uppercase;">Avg Accuracy</div>
            <div style="font-size: 22px; font-weight: 900; color: #10b981; margin-top: 2px;">${avgBatchAccuracy}%</div>
          </div>
          <div style="padding: 12px 14px; border-radius: 8px; background: #f8fafc; border: 1.5px solid #e2e8f0; text-align: center;">
            <div style="font-size: 11px; font-weight: 800; color: #64748b; text-transform: uppercase;">Avg Integrity</div>
            <div style="font-size: 22px; font-weight: 900; color: #8b5cf6; margin-top: 2px;">${avgBatchIntegrity}%</div>
          </div>
        </div>

        ${inactiveNamesHtml}

        <!-- Active Students Table -->
        ${sortedActiveStudents.length > 0 ? `
          <div style="border-radius: 8px; border: 1.5px solid #e2e8f0; overflow: hidden; margin-bottom: 14px;">
            <table style="width: 100%; border-collapse: collapse; font-size: 12px;">
              <thead>
                <tr style="background: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
                  <th style="padding: 8px 12px; font-weight: 800; text-align: center; color: #475569; width: 48px;">Rank</th>
                  <th style="padding: 8px 12px; font-weight: 800; text-align: left; color: #475569;">Student</th>
                  <th style="padding: 8px 12px; font-weight: 800; text-align: center; color: #475569;">Sessions</th>
                  <th style="padding: 8px 12px; font-weight: 800; text-align: center; color: #475569;">Questions</th>
                  <th style="padding: 8px 12px; font-weight: 800; text-align: center; color: #475569;">Accuracy</th>
                  <th style="padding: 8px 12px; font-weight: 800; text-align: center; color: #475569;">Integrity</th>
                  <th style="padding: 8px 12px; font-weight: 800; text-align: center; color: #475569;">Mastery</th>
                  <th style="padding: 8px 12px; font-weight: 800; text-align: center; color: #475569;">Time</th>
                  <th style="padding: 8px 12px; font-weight: 800; text-align: center; color: #475569;">Remark</th>
                </tr>
              </thead>
              <tbody>
                ${activeRowsHtml}
              </tbody>
            </table>
          </div>
        ` : `
          <div style="padding: 24px; text-align: center; background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 8px; font-weight: 700; color: #64748b;">
            No active practice sessions recorded on this date.
          </div>
        `}

        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 10px; border-top: 1px solid #e2e8f0; font-size: 11px; font-weight: 700; color: #94a3b8;">
          <span>YASHCOM LOS • Daily Practice Diagnostic Report</span>
          <span>Confidential • Designed for Parents & Teachers</span>
        </div>
      `;

      document.body.appendChild(container);

      const canvas = await html2canvas(container, {
        scale: 2,
        useCORS: true,
        logging: false,
        backgroundColor: '#ffffff'
      });

      document.body.removeChild(container);

      // Convert to blob
      const blob: Blob = await new Promise((resolve, reject) => {
        canvas.toBlob((b: Blob | null) => {
          if (b) resolve(b);
          else reject(new Error('Canvas to Blob conversion failed.'));
        }, 'image/png');
      });

      // 1. Copy to clipboard
      let copied = false;
      try {
        if (navigator.clipboard && (window as any).ClipboardItem) {
          await navigator.clipboard.write([
            new (window as any).ClipboardItem({ 'image/png': blob })
          ]);
          copied = true;
        }
      } catch (clipErr) {
        console.warn('Clipboard write warning:', clipErr);
      }

      // 2. Download file
      const cleanBatch = selectedBatchName.replace(/[^a-zA-Z0-9_-]/g, '_');
      const fileName = `Daily_Practice_${cleanBatch}_${selectedDate}.png`;
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = fileName;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);

      playNotificationSound();

      if (copied) {
        alert('📸 WhatsApp image report copied to clipboard & downloaded!\n\nYou can now paste it directly into WhatsApp (Ctrl + V).');
      } else {
        alert('📸 WhatsApp image report downloaded successfully!');
      }

    } catch (err: any) {
      console.error('Error generating WhatsApp image card:', err);
      alert(`❌ Failed to export WhatsApp image card: ${err.message || err}`);
    } finally {
      setExportingImage(false);
    }
  };

  const deferredSearch = useDeferredValue(searchQuery);

  // Filter students by selected batch and search query
  const filteredStudents = useMemo(() => {
    const qLower = deferredSearch.toLowerCase().trim();
    return students.filter(student => {
      const matchesBatch = selectedBatchId === 'all' || student.batchIds?.includes(selectedBatchId);
      if (!matchesBatch) return false;
      if (!qLower) return true;
      return student.name.toLowerCase().includes(qLower) || 
             student.studentCode.toLowerCase().includes(qLower);
    });
  }, [students, selectedBatchId, deferredSearch]);

  // Separate active (completed >= 1 session) vs. inactive (0 sessions, did not practice) students
  const activeList = useMemo(() => filteredStudents.filter(s => s.sessionsCount > 0), [filteredStudents]);
  const inactiveList = useMemo(() => filteredStudents.filter(s => s.sessionsCount === 0), [filteredStudents]);

  // Sort only the active list for display
  const sortedActiveStudents = useMemo(() => {
    return [...activeList].sort((a, b) => {
      let aVal = a[sortField];
      let bVal = b[sortField];

      if (typeof aVal === 'string' && typeof bVal === 'string') {
        return sortDirection === 'asc' 
          ? aVal.localeCompare(bVal) 
          : bVal.localeCompare(aVal);
      }

      // Number sorting
      const numA = Number(aVal || 0);
      const numB = Number(bVal || 0);
      return sortDirection === 'asc' ? numA - numB : numB - numA;
    });
  }, [activeList, sortField, sortDirection]);

  // Aggregate stats of current filtered selection
  const totalPracticedCount = activeList.length;
  const totalSessionsCount = activeList.reduce((sum, s) => sum + s.sessionsCount, 0);
  
  const sumAccuracy = activeList.reduce((sum, s) => sum + s.avgAccuracy, 0);
  const avgBatchAccuracy = totalPracticedCount > 0 ? parseFloat((sumAccuracy / totalPracticedCount).toFixed(1)) : 0;

  const sumHonesty = activeList.reduce((sum, s) => sum + s.avgHonesty, 0);
  const avgBatchIntegrity = totalPracticedCount > 0 ? parseFloat((sumHonesty / totalPracticedCount).toFixed(1)) : 100;

  const selectedBatchName = selectedBatchId === 'all' 
    ? 'All Batches' 
    : batches.find(b => b.id === selectedBatchId)?.name || 'Selected Batch';

  // Format date nicely for display
  const formatDisplayDate = (dateStr: string) => {
    return formatDateDMY(dateStr);
  };

  const getLockTag = (student: StudentSummary) => {
    if (student.isAutonomous) {
      return <span style={{ color: 'var(--warning)', fontSize: '11px', fontWeight: 800 }}>🤖 Autonomous</span>;
    }
    if (student.activeLocks.length > 0) {
      // Find clean code of first lock
      const lock = student.activeLocks[0];
      const code = lock.split(':')[0] || 'Topic';
      const type = lock.includes('Daily') ? 'Daily' : 'Cooldown';
      return (
        <span style={{ color: 'var(--error)', fontSize: '11px', fontWeight: 800 }} title={student.activeLocks.join(', ')}>
          🔒 {type} ({code})
        </span>
      );
    }
    return null;
  };

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
      <div className="no-print" style={{ maxWidth: '1400px', width: '100%', margin: '0 auto', padding: '12px 12px 0 12px' }}>
        <nav style={{ display: 'flex', gap: '15px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', overflowX: 'auto' }}>
          <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/learning-quotient')}>Learning Quotient (LQ)</span>
          <span style={{ fontSize: '13px', fontWeight: 700, color: 'var(--accent)', borderBottom: '2px solid var(--accent)', paddingBottom: '4px', whiteSpace: 'nowrap' }}>Daily Practice Summary</span>
          <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/parent-pending')}>Parent Pending</span>
          <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/usage')}>System Usage</span>
          <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/login-register')}>Login Register</span>
        </nav>
      </div>

      {/* Header Info Block (Only visible on Print) */}
      <div className="print-header-info">
        <h2 style={{ margin: '0 0 5px 0', color: 'var(--text)' }}>Yashcom Foundation - Daily Practice Summary</h2>
        <div style={{ fontSize: '12px', color: 'var(--text-muted)', borderBottom: '2px solid var(--text)', paddingBottom: '10px' }}>
          <strong>Batch:</strong> {selectedBatchName} | <strong>Date:</strong> {formatDisplayDate(selectedDate)} | <strong>Exported:</strong> {new Date().toLocaleTimeString('en-IN')}
        </div>
        <div style={{ display: 'flex', gap: '20px', marginTop: '10px', fontSize: '11px' }}>
          <span><strong>Total Students Practiced:</strong> {totalPracticedCount}</span>
          <span><strong>Total Practice Sessions:</strong> {totalSessionsCount}</span>
          <span><strong>Avg Accuracy:</strong> {avgBatchAccuracy}%</span>
          <span><strong>Avg Integrity:</strong> {avgBatchIntegrity}%</span>
        </div>
      </div>

      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1400px', width: '100%', margin: '0 auto' }}>
        
        {/* Toolbar Controls (Hidden on Print) */}
        <div className="card glass no-print" style={{ padding: '16px 20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '15px', marginBottom: '20px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '15px', flexWrap: 'wrap' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text-muted)' }}>Batch:</span>
              <select
                value={selectedBatchId}
                onChange={(e) => setSelectedBatchId(e.target.value)}
                style={{
                  padding: '8px 14px',
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
              <span style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text-muted)' }}>Date:</span>
              <DateInputDMY value={selectedDate} onChange={(val) => setSelectedDate(val)} style={{ width: '140px' }} inputStyle={{ padding: '7px 28px 7px 10px', background: 'var(--bg-soft)', fontWeight: 700 }} />
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text-muted)' }}>Search:</span>
              <input
                type="text"
                placeholder="Search student..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                style={{
                  padding: '7px 12px',
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

          <div>
            <button 
              className="btn"
              onClick={handleExportWhatsAppImage}
              disabled={exportingImage || loading}
              style={{ 
                display: 'inline-flex', 
                alignItems: 'center', 
                gap: '6px', 
                fontSize: '13px', 
                fontWeight: 700, 
                padding: '8px 18px',
                background: 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
                color: '#ffffff',
                border: 'none',
                borderRadius: 'var(--radius-sm, 6px)',
                cursor: (exportingImage || loading) ? 'wait' : 'pointer',
                boxShadow: '0 2px 8px rgba(16, 185, 129, 0.3)'
              }}
              title="Export lossless card optimized for WhatsApp sharing"
            >
              {exportingImage ? '⏳ Generating Card...' : '📸 WhatsApp Report Card'}
            </button>
          </div>
        </div>

        {/* Stats Cards Row (Hidden on Print) */}
        <div className="no-print" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '16px', marginBottom: '20px' }}>
          <div className="card glass" style={{ padding: '16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Students Active</div>
            <div style={{ fontSize: '1.8rem', fontWeight: 800, color: 'var(--accent)', marginTop: '4px' }}>{totalPracticedCount}</div>
          </div>
          <div className="card glass" style={{ padding: '16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Sessions Done</div>
            <div style={{ fontSize: '1.8rem', fontWeight: 800, color: 'var(--accent)', marginTop: '4px' }}>{totalSessionsCount}</div>
          </div>
          <div className="card glass" style={{ padding: '16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Avg Accuracy</div>
            <div style={{ fontSize: '1.8rem', fontWeight: 800, color: 'var(--success)', marginTop: '4px' }}>{avgBatchAccuracy}%</div>
          </div>
          <div className="card glass" style={{ padding: '16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Avg Integrity</div>
            <div style={{ fontSize: '1.8rem', fontWeight: 800, color: avgBatchIntegrity < 85 ? 'var(--warning)' : 'var(--accent)', marginTop: '4px' }}>{avgBatchIntegrity}%</div>
          </div>
        </div>

        {/* Data Table */}
        <div className="card glass print-table-card" style={{ borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
          {loading ? (
            <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '60px 0' }}>
              <div className="spinner"></div>
              <span style={{ marginLeft: '10px', fontWeight: 600, color: 'var(--text-muted)' }}>Loading summary data...</span>
            </div>
          ) : filteredStudents.length === 0 ? (
            <div style={{ textAlign: 'center', padding: '60px 20px', color: 'var(--text-muted)' }}>
              📭 No student practice data found for {selectedBatchName} on {formatDisplayDate(selectedDate)}.
            </div>
          ) : (
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                    <th 
                      onClick={() => handleSort('name')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'left', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Student Name {sortField === 'name' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('sessionsCount')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      No. of Sessions {sortField === 'sessionsCount' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('totalQuestions')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Questions Solved {sortField === 'totalQuestions' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('avgAccuracy')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Accuracy {sortField === 'avgAccuracy' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('avgHonesty')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Integrity {sortField === 'avgHonesty' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('avgMastery')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Mastery {sortField === 'avgMastery' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                    <th 
                      onClick={() => handleSort('totalTimeSpent')}
                      className="sortable-th"
                      style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--text-muted)' }}
                    >
                      Time Spent {sortField === 'totalTimeSpent' ? (sortDirection === 'asc' ? '▲' : '▼') : ''}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {/* Absent / Did Not Practice Section (Pinned to top, matching objective exam layout) */}
                  {inactiveList.length > 0 && (
                    <tr style={{ borderBottom: '1px solid var(--border-light)', background: 'var(--danger-bg)' }}>
                      <td colSpan={7} style={{ padding: '14px 16px', color: 'var(--danger)' }}>
                        <div style={{ textAlign: 'center', fontWeight: 800, fontSize: '14px', marginBottom: '10px', color: 'var(--danger)' }}>
                          🔴 Did Not Practice Today ({inactiveList.length})
                        </div>
                        <div style={{ 
                          display: 'grid', 
                          gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', 
                          gap: '8px 16px',
                          fontSize: '13px',
                          fontWeight: 700,
                          color: 'var(--danger)'
                        }}>
                          {[...inactiveList]
                            .sort((a, b) => a.name.localeCompare(b.name))
                            .map(a => (
                              <div key={a.studentCode} style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', color: 'var(--danger)', fontWeight: 700, fontSize: '13px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                                <span>• {a.name}</span>
                                {getLockTag(a)}
                              </div>
                            ))
                          }
                        </div>
                      </td>
                    </tr>
                  )}

                  {/* Active Practice Attempts List */}
                  {sortedActiveStudents.length === 0 ? (
                    <tr>
                      <td colSpan={7} style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
                        📭 No active practice sessions completed today.
                      </td>
                    </tr>
                  ) : (
                    sortedActiveStudents.map((row, idx) => (
                      <tr 
                        key={row.studentCode} 
                        style={{ 
                          borderBottom: idx === sortedActiveStudents.length - 1 ? 'none' : '1px solid var(--border-light)',
                          background: idx % 2 === 1 ? 'var(--bg-soft-even)' : 'transparent'
                        }}
                      >
                        <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <span>{row.name}</span>
                            {getLockTag(row)}
                          </div>
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700 }}>
                          {row.sessionsCount}
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'center', fontWeight: 700, color: 'var(--accent)' }}>
                          {row.totalQuestions}
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'center' }}>
                          <span style={{ color: 'var(--success)', fontWeight: 700 }}>{row.avgAccuracy}%</span>
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'center' }}>
                          <span style={{ 
                            color: row.avgHonesty < 70 ? 'var(--error)' : (row.avgHonesty < 90 ? 'var(--warning)' : 'var(--success)'),
                            fontWeight: 700
                          }}>
                            {row.avgHonesty}%
                          </span>
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'center' }}>
                          <span style={{ color: 'var(--accent)', fontWeight: 700 }}>{row.avgMastery}%</span>
                        </td>
                        <td style={{ padding: '12px 16px', textAlign: 'center' }}>
                          {formatTimeSpent(row.totalTimeSpent)}
                        </td>
                      </tr>
                    ))
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
