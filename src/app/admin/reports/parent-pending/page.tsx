'use client';

import React, { useEffect, useState, useMemo, useDeferredValue } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import { useReports } from '@/hooks/useReports';
import { formatDateTimeIST } from '@/lib/dateUtils';
import dynamic from 'next/dynamic';
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });

interface SincerityRecord {
  id: string;
  studentCode: string;
  studentName: string;
  className: string;
  batchIds: string[];
  examName: string;
  type: string;
  reviewedByActor: 'parent' | 'student';
  reviewedByEmail?: string;
  photoThumbnail?: string | null;
  photoPurged?: boolean;
  expiresAt?: number | null;
  timestamp: string;
}

interface Batch {
  id: string;
  name: string;
}

interface SummaryStats {
  totalReviews: number;
  parentVerifiedCount: number;
  studentSoloCount: number;
  parentSincerityRate: number;
  verifiedTodayCount: number;
}

export default function ParentPendingReportPage() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();
  const { getParentPendingReport } = useReports();

  const [loading, setLoading] = useState(true);
  const [records, setRecords] = useState<SincerityRecord[]>([]);
  const [batches, setBatches] = useState<Batch[]>([]);
  const [summary, setSummary] = useState<SummaryStats>({
    totalReviews: 0,
    parentVerifiedCount: 0,
    studentSoloCount: 0,
    parentSincerityRate: 100,
    verifiedTodayCount: 0
  });

  // Filters & sorting
  const [searchQuery, setSearchQuery] = useState('');
  const deferredSearch = useDeferredValue(searchQuery);
  const [selectedBatchFilter, setSelectedBatchFilter] = useState<string>('all');
  const [actorFilter, setActorFilter] = useState<'all' | 'parent' | 'student' | 'photo'>('all');
  const [sessionTypeFilter, setSessionTypeFilter] = useState<string>('all');
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);

  // Photo viewer modal
  const [previewPhoto, setPreviewPhoto] = useState<{
    show: boolean;
    photoUrl: string;
    studentName: string;
    examName: string;
    timestamp: string;
    expiresAt?: number | null;
  } | null>(null);

  useEffect(() => {
    const loadReportData = async () => {
      if (!firebaseUser) return;
      try {
        const idToken = await firebaseUser.getIdToken();
        const data = await getParentPendingReport(idToken);
        if (data && data.success) {
          setRecords(data.records || []);
          setBatches(data.batches || []);
          if (data.summary) {
            setSummary(data.summary);
          }
        }
      } catch (err) {
        console.error('Failed to load parent sincerity report:', err);
      } finally {
        setLoading(false);
      }
    };
    loadReportData();
  }, [firebaseUser]);

  // Filtered list using deferred value & memoization
  const filteredRecords = useMemo(() => {
    return records.filter(r => {
      // 1. Batch filter
      if (selectedBatchFilter !== 'all') {
        if (!r.batchIds?.includes(selectedBatchFilter)) return false;
      }

      // 2. Actor filter
      if (actorFilter === 'parent' && r.reviewedByActor !== 'parent') return false;
      if (actorFilter === 'student' && r.reviewedByActor !== 'student') return false;
      if (actorFilter === 'photo' && !r.photoThumbnail) return false;

      // 3. Session Type filter
      if (sessionTypeFilter !== 'all') {
        const t = (r.type || '').toLowerCase();
        const name = (r.examName || '').toLowerCase();
        if (sessionTypeFilter === 'daily_5min_sync') {
          if (t !== 'daily_5min_sync' && !name.includes('daily') && !name.includes('sync')) return false;
        } else if (sessionTypeFilter === 'objective') {
          if (t !== 'objective' && t !== 'obj' && !name.includes('objective')) return false;
        } else if (sessionTypeFilter === 'practice') {
          if (t !== 'practice' && !name.includes('practice')) return false;
        } else if (sessionTypeFilter === 'subjective') {
          if (t !== 'subjective' && t !== 'subj' && !name.includes('subjective')) return false;
        } else if (sessionTypeFilter === 'entrance') {
          if (t !== 'entrance' && !name.includes('entrance') && !name.includes('mock')) return false;
        } else {
          if (t !== sessionTypeFilter) return false;
        }
      }

      // 4. Search query
      if (deferredSearch.trim()) {
        const q = deferredSearch.toLowerCase();
        const matchesName = r.studentName?.toLowerCase().includes(q);
        const matchesExam = r.examName?.toLowerCase().includes(q);
        const matchesClass = r.className?.toLowerCase().includes(q);
        if (!matchesName && !matchesExam && !matchesClass) return false;
      }

      return true;
    });
  }, [records, selectedBatchFilter, actorFilter, sessionTypeFilter, deferredSearch]);

  const formatDateIST = (dateStr: string) => dateStr ? formatDateTimeIST(dateStr) : '—';

  const getHoursUntilExpiry = (expiresAt?: number | null) => {
    if (!expiresAt) return null;
    const diffMs = expiresAt - Date.now();
    if (diffMs <= 0) return 'Expired';
    const hrs = Math.ceil(diffMs / (1000 * 60 * 60));
    return `${hrs}h left`;
  };

  const exportSections = [
    { id: 'summary', name: 'Parent Sincerity Summary Stats', elementId: 'sincerity-summary-cards' },
    { id: 'records', name: 'Parent Verification Logs Table', elementId: 'sincerity-table-section' }
  ];

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading Parent Sincerity Audit Report...
        </div>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800, cursor: 'pointer' }} onClick={() => router.push('/admin')}>YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Parent Reviews & Sincerity Audit</h1>
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
              Verification logs for parent-supervised daily sync and exam reviews vs. student solo reviews
            </div>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          
          <button className="btn btn-primary" style={{ padding: '6px 12px', fontSize: '12px' }} onClick={() => setPdfSelectorOpen(true)}>
            📄 Export PDF
          </button>
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      {/* Main Content */}
      <main style={{ flex: 1, padding: '16px 14px', maxWidth: '1100px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '14px' }}>
        
        {/* KPI Summary Bento Grid - One Compact Line on Desktop, 2x2 on Mobile */}
        <div id="sincerity-summary-cards" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '10px' }}>
          
          {/* Card 1: Sincerity Rate */}
          <div className="card" style={{ background: 'var(--surface)', padding: '12px 16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '2px' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.4px' }}>Parent Sincerity Rate</div>
            <div style={{ fontSize: '24px', fontWeight: 900, color: summary.parentSincerityRate >= 70 ? 'var(--success)' : 'var(--accent)', lineHeight: 1.1, marginTop: '2px' }}>
              {summary.parentSincerityRate}%
            </div>
          </div>

          {/* Card 2: Verified Today */}
          <div className="card" style={{ background: 'var(--surface)', padding: '12px 16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '2px' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.4px' }}>Verified Today (24h)</div>
            <div style={{ fontSize: '24px', fontWeight: 900, color: 'var(--accent)', lineHeight: 1.1, marginTop: '2px' }}>
              {summary.verifiedTodayCount}
            </div>
          </div>

          {/* Card 3: Student Solo */}
          <div className="card" style={{ background: 'var(--surface)', padding: '12px 16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '2px' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.4px' }}>Student Solo Reviews</div>
            <div style={{ fontSize: '24px', fontWeight: 900, color: 'var(--text)', lineHeight: 1.1, marginTop: '2px' }}>
              {summary.studentSoloCount}
            </div>
          </div>

          {/* Card 4: 24h Auto-Purge Policy */}
          <div className="card" style={{ background: 'var(--surface)', padding: '12px 16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '2px' }}>
            <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.4px' }}>Privacy & Auto-Purge</div>
            <div style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text)', lineHeight: 1.1, marginTop: '4px', display: 'flex', alignItems: 'center', gap: '4px' }}>
              <span>🛡️ 24h TTL</span>
            </div>
          </div>

        </div>

        {/* Filter Controls Toolbar - Single Line */}
        <div className="card" style={{ background: 'var(--surface)', padding: '10px 14px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
          
          {/* Search Box */}
          <div style={{ flex: '1 1 200px', minWidth: '150px' }}>
            <input 
              type="text" 
              className="form-control" 
              placeholder="🔍 Search student name, exam, class..." 
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              style={{ width: '100%', fontSize: '12px', padding: '6px 12px', borderRadius: 'var(--radius)', background: 'var(--bg-soft)' }}
            />
          </div>

          {/* Batch Filter */}
          <div style={{ flex: '0 0 auto' }}>
            <select
              className="form-control"
              value={selectedBatchFilter}
              onChange={(e) => setSelectedBatchFilter(e.target.value)}
              style={{ fontSize: '12px', padding: '6px 10px', borderRadius: 'var(--radius)', background: 'var(--bg-soft)', width: 'auto' }}
            >
              <option value="all">All Batches ({batches.length})</option>
              {batches.map(b => (
                <option key={b.id} value={b.id}>{b.name}</option>
              ))}
            </select>
          </div>

          {/* Actor Filter */}
          <div style={{ flex: '0 0 auto' }}>
            <select
              className="form-control"
              value={actorFilter}
              onChange={(e: any) => setActorFilter(e.target.value)}
              style={{ fontSize: '12px', padding: '6px 10px', borderRadius: 'var(--radius)', background: 'var(--bg-soft)', width: 'auto' }}
            >
              <option value="all">All Reviewers</option>
              <option value="parent">👨‍👩‍👧 Parent Verified</option>
              <option value="student">👨‍🎓 Student Solo</option>
              <option value="photo">📸 Photo Proof Only</option>
            </select>
          </div>

          {/* Session Type Filter */}
          <div style={{ flex: '0 0 auto' }}>
            <select
              className="form-control"
              value={sessionTypeFilter}
              onChange={(e) => setSessionTypeFilter(e.target.value)}
              style={{ fontSize: '12px', padding: '6px 10px', borderRadius: 'var(--radius)', background: 'var(--bg-soft)', width: 'auto' }}
            >
              <option value="all">All Session Types</option>
              <option value="daily_5min_sync">🌙 Daily Sync</option>
              <option value="objective">📝 Objective Exam</option>
              <option value="practice">📚 Practice Review</option>
              <option value="subjective">✍️ Subjective Exam</option>
              <option value="entrance">🎯 Entrance Mock</option>
            </select>
          </div>

        </div>

        {/* Audit Table */}
        <div id="sincerity-table-section" className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
          <div style={{ padding: '12px 18px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h3 style={{ fontSize: '13.5px', fontWeight: 800, margin: 0 }}>
              Verification Log History ({filteredRecords.length})
            </h3>
            <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Latest sessions first</span>
          </div>

          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px' }}>
              <thead>
                <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', textAlign: 'left' }}>
                  <th style={{ padding: '10px 16px', fontWeight: 600 }}>Student &amp; Class</th>
                  <th style={{ padding: '10px 16px', fontWeight: 600 }}>Session / Exam</th>
                  <th style={{ padding: '10px 16px', fontWeight: 600 }}>Review Actor</th>
                  <th style={{ padding: '10px 16px', fontWeight: 600, textAlign: 'center' }}>Verification Proof</th>
                  <th style={{ padding: '10px 16px', fontWeight: 600, textAlign: 'right' }}>Timestamp (IST)</th>
                </tr>
              </thead>
              <tbody>
                {filteredRecords.length === 0 ? (
                  <tr>
                    <td colSpan={5} style={{ padding: '40px 20px', textAlign: 'center', color: 'var(--text-muted)' }}>
                      No sincerity records matching your criteria.
                    </td>
                  </tr>
                ) : (
                  filteredRecords.map(r => {
                    const isParent = r.reviewedByActor === 'parent';
                    const hasPhoto = Boolean(r.photoThumbnail);
                    const expiryLabel = getHoursUntilExpiry(r.expiresAt);

                    return (
                      <tr key={r.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        {/* Student Name & Class (Never studentCode) */}
                        <td style={{ padding: '12px 16px' }}>
                          <div style={{ fontWeight: 700, color: 'var(--text)' }}>{r.studentName}</div>
                          <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>{r.className || 'General'}</div>
                        </td>

                        {/* Exam Title & Type */}
                        <td style={{ padding: '12px 16px' }}>
                          <div style={{ fontWeight: 600, color: 'var(--text)' }}>{r.examName}</div>
                          <span style={{ 
                            fontSize: '10px', 
                            fontWeight: 700,
                            padding: '2px 8px', 
                            borderRadius: '12px', 
                            background: r.type === 'Sync Session' ? 'rgba(168, 85, 247, 0.15)' : 'var(--bg-soft)', 
                            color: r.type === 'Sync Session' ? '#a855f7' : 'var(--text-muted)',
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '3px',
                            marginTop: '2px'
                          }}>
                            {r.type === 'Sync Session' ? '✨ Sync Session' : r.type}
                          </span>
                        </td>

                        {/* Actor Badge */}
                        <td style={{ padding: '12px 16px' }}>
                          {isParent ? (
                            <span style={{ background: '#dcfce7', color: '#15803d', padding: '4px 10px', borderRadius: '12px', fontSize: '11px', fontWeight: 700, display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
                              👨‍👩‍👧 Parent Verified
                            </span>
                          ) : (
                            <span style={{ background: 'var(--bg-soft)', color: 'var(--text-muted)', padding: '4px 10px', borderRadius: '12px', fontSize: '11px', fontWeight: 600, display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
                              👨‍🎓 Student Solo
                            </span>
                          )}
                        </td>

                        {/* Photo Verification Thumbnail */}
                        <td style={{ padding: '12px 16px', textAlign: 'center' }}>
                          {hasPhoto ? (
                            <div style={{ display: 'inline-flex', flexDirection: 'column', alignItems: 'center', gap: '4px' }}>
                              <img 
                                src={r.photoThumbnail!} 
                                alt="Verification Proof"
                                onClick={() => setPreviewPhoto({
                                  show: true,
                                  photoUrl: r.photoThumbnail!,
                                  studentName: r.studentName,
                                  examName: r.examName,
                                  timestamp: r.timestamp,
                                  expiresAt: r.expiresAt
                                })}
                                style={{
                                  width: '48px',
                                  height: '36px',
                                  objectFit: 'cover',
                                  borderRadius: '4px',
                                  border: '1px solid var(--accent)',
                                  cursor: 'pointer',
                                  boxShadow: '0 2px 4px rgba(0,0,0,0.15)'
                                }}
                                title="Click to enlarge verification photo"
                              />
                              {expiryLabel && (
                                <span style={{ fontSize: '9px', color: '#b45309', fontWeight: 600 }}>
                                  ⏳ {expiryLabel}
                                </span>
                              )}
                            </div>
                          ) : r.photoPurged ? (
                            <span style={{ fontSize: '11px', color: 'var(--text-muted)', display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                              🔒 Auto-purged (24h)
                            </span>
                          ) : isParent ? (
                            <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                              Camera bypassed
                            </span>
                          ) : (
                            <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>—</span>
                          )}
                        </td>

                        {/* Timestamp */}
                        <td style={{ padding: '12px 16px', textAlign: 'right', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                          {formatDateIST(r.timestamp)}
                        </td>
                      </tr>
                    );
                  })
                )}
              </tbody>
            </table>
          </div>
        </div>

      </main>

      {/* Photo Enlarge Modal */}
      {previewPhoto?.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.85)', zIndex: 12000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '16px' }}>
          <div style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', maxWidth: '420px', width: '100%', padding: '20px', border: '1px solid var(--border-light)', textAlign: 'center' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
              <div style={{ textAlign: 'left' }}>
                <h4 style={{ margin: 0, fontSize: '14px', fontWeight: 700 }}>📷 Parent Verification Proof</h4>
                <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>{previewPhoto.studentName} · {previewPhoto.examName}</div>
              </div>
              <button className="btn btn-secondary" style={{ padding: '2px 8px', fontSize: '11px' }} onClick={() => setPreviewPhoto(null)}>✕</button>
            </div>

            <div style={{ borderRadius: 'var(--radius)', overflow: 'hidden', border: '1px solid var(--border-light)', marginBottom: '12px', background: '#000' }}>
              <img 
                src={previewPhoto.photoUrl} 
                alt="Enlarged Proof" 
                style={{ width: '100%', height: 'auto', display: 'block' }}
              />
            </div>

            <div style={{ fontSize: '11px', color: 'var(--text-muted)', background: 'var(--bg-soft)', padding: '8px 12px', borderRadius: 'var(--radius)', marginBottom: '14px', textAlign: 'left' }}>
              <div>📅 <strong>Timestamp:</strong> {formatDateIST(previewPhoto.timestamp)}</div>
              <div>🛡️ <strong>Auto-Purge Policy:</strong> This snapshot is temporarily held for verification and automatically purged after 24 hours.</div>
            </div>

            <button className="btn btn-primary" style={{ width: '100%', padding: '8px' }} onClick={() => setPreviewPhoto(null)}>
              Close Preview
            </button>
          </div>
        </div>
      )}

      {/* PDF Export Modal */}
      <ExportPdfModal 
        isOpen={pdfSelectorOpen}
        onClose={() => setPdfSelectorOpen(false)}
        title="Parent Sincerity Audit Report"
        filename="Parent_Sincerity_Audit_Report.pdf"
        sections={exportSections}
      />

    </div>
  );
}
