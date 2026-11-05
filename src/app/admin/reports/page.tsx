'use client';

import React, { useState, useEffect, useMemo, useCallback } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/context/AuthContext';
import { useReports } from '@/hooks/useReports';
import type { InterventionItem, InterventionSummary } from '@/services/intervention.service';

export default function AdminReportsHubPage() {
  const router = useRouter();
  const { firebaseUser } = useAuth();
  const { getInterventionQueue } = useReports();

  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<InterventionSummary | null>(null);

  // Filters
  const [selectedBatch, setSelectedBatch] = useState<string>('all');
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [copiedId, setCopiedId] = useState<string | null>(null);

  const fetchQueue = useCallback(async (forceRefresh = false) => {
    if (!firebaseUser) return;
    if (forceRefresh) setRefreshing(true);
    else setLoading(true);
    setError(null);

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await getInterventionQueue(idToken, forceRefresh);
      if (res && res.items) {
        setData(res);
      } else {
        setError('Failed to load intervention queue data.');
      }
    } catch (err: any) {
      console.error('Error fetching intervention queue:', err);
      setError(err.message || 'An unexpected error occurred while loading interventions.');
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  }, [firebaseUser, getInterventionQueue]);

  useEffect(() => {
    if (!firebaseUser) return;
    fetchQueue(false);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [firebaseUser]);

  // Unique batches from items
  const batches = useMemo(() => {
    if (!data?.items) return [];
    const set = new Set<string>();
    data.items.forEach(item => {
      if (item.className) set.add(item.className);
    });
    return Array.from(set).sort();
  }, [data]);

  // Filtered items
  const filteredItems = useMemo(() => {
    if (!data?.items) return [];
    return data.items.filter(item => {
      // Batch filter
      if (selectedBatch !== 'all' && item.className !== selectedBatch) {
        return false;
      }
      // Category filter
      if (selectedCategory !== 'all' && item.category !== selectedCategory) {
        return false;
      }
      // Search query filter (search by student name or topic/exam title)
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase();
        const matchesName = item.studentName.toLowerCase().includes(q);
        const matchesTitle = item.title.toLowerCase().includes(q);
        const matchesTopic = (item.topicName || '').toLowerCase().includes(q);
        if (!matchesName && !matchesTitle && !matchesTopic) {
          return false;
        }
      }
      return true;
    });
  }, [data, selectedBatch, selectedCategory, searchQuery]);

  // Copy WhatsApp message
  const handleCopyMessage = (id: string, text: string) => {
    if (navigator?.clipboard) {
      navigator.clipboard.writeText(text);
      setCopiedId(id);
      setTimeout(() => setCopiedId(null), 2500);
    }
  };

  // Open WhatsApp Web
  const handleOpenWhatsApp = (phone?: string, text?: string) => {
    if (!text) return;
    const cleanPhone = (phone || '').replace(/\D/g, '');
    let targetPhone = '';
    if (cleanPhone.length === 10) targetPhone = `91${cleanPhone}`;
    else if (cleanPhone.length === 12 && cleanPhone.startsWith('91')) targetPhone = cleanPhone;

    const url = targetPhone
      ? `https://wa.me/${targetPhone}?text=${encodeURIComponent(text)}`
      : `https://wa.me/?text=${encodeURIComponent(text)}`;
    window.open(url, '_blank');
  };

  return (
    <div style={{ background: 'var(--bg)', flex: 1, display: 'flex', flexDirection: 'column' }}>

      {/* Reports Hub Sub-Navigation Bar */}
      <div style={{ maxWidth: '1280px', width: '100%', margin: '0 auto', padding: '8px 16px 0 16px' }}>
        <nav style={{ display: 'flex', gap: '14px', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px', overflowX: 'auto' }}>
          <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--accent)', borderBottom: '2px solid var(--accent)', paddingBottom: '4px', whiteSpace: 'nowrap' }}>
            ⚡ Daily Intervention Queue
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

      {/* Main Workspace */}
      <main style={{ flex: 1, padding: '10px 14px', maxWidth: '1280px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '10px' }}>
        
        {/* Page Title & Refresh */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <h2 style={{ fontSize: '17px', fontWeight: 800, color: 'var(--text)', margin: 0 }}>
                ⚡ Daily Intervention Queue
              </h2>
              <span style={{
                fontSize: '10px',
                fontWeight: 700,
                padding: '1px 6px',
                borderRadius: '6px',
                background: 'rgba(239, 68, 68, 0.12)',
                color: 'var(--danger, #ef4444)'
              }}>
                Exam-to-Practice Remediation Hub
              </span>
            </div>
            <p style={{ fontSize: '11.5px', color: 'var(--text-muted)', margin: '2px 0 0 0' }}>
              Tracks students failing to recover from exam baselines through daily practice. Actionable triggers for teachers & admins.
            </p>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            {data?.lastUpdated && (
              <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                Updated {new Date(data.lastUpdated).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
              </span>
            )}
            <button
              onClick={() => fetchQueue(true)}
              disabled={loading || refreshing}
              style={{
                background: 'var(--surface)',
                border: '1px solid var(--border)',
                borderRadius: '6px',
                padding: '5px 10px',
                fontSize: '11.5px',
                fontWeight: 600,
                color: 'var(--text)',
                cursor: loading || refreshing ? 'not-allowed' : 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '5px'
              }}
            >
              <span>{refreshing ? '🔄' : '⚡'}</span>
              <span>{refreshing ? 'Refreshing...' : 'Refresh Queue'}</span>
            </button>
          </div>
        </div>

        {/* 4-Stage Metric Cards Aligned with Lifecycle */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
          gap: '10px'
        }}>
          {/* Card 1: Missed Baseline Exams (Step 1) */}
          <div
            onClick={() => setSelectedCategory('missed_exam')}
            style={{
              background: 'var(--surface)',
              border: selectedCategory === 'missed_exam' ? '2px solid var(--danger, #ef4444)' : '1px solid var(--border-light)',
              borderRadius: '8px',
              padding: '10px 12px',
              cursor: 'pointer',
              transition: 'all 0.15s ease'
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2px' }}>
              <span style={{ fontSize: '11px', fontWeight: 600, color: 'var(--danger, #ef4444)' }}>
                🔴 1. Missed Exams
              </span>
              <span style={{ fontSize: '9.5px', fontWeight: 700, padding: '1px 5px', borderRadius: '4px', background: 'rgba(239, 68, 68, 0.15)', color: 'var(--danger, #ef4444)' }}>
                Baseline Missing
              </span>
            </div>
            <div style={{ fontSize: '20px', fontWeight: 800, color: 'var(--danger, #ef4444)' }}>
              {data?.criticalCount ?? (loading ? '...' : 0)}
            </div>
            <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
              Assigned exams unattempted
            </div>
          </div>

          {/* Card 2: Practice Locked (Step 3 Lockdown) */}
          <div
            onClick={() => setSelectedCategory('reflection_gate')}
            style={{
              background: 'var(--surface)',
              border: selectedCategory === 'reflection_gate' ? '2px solid #f97316' : '1px solid var(--border-light)',
              borderRadius: '8px',
              padding: '10px 12px',
              cursor: 'pointer',
              transition: 'all 0.15s ease'
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2px' }}>
              <span style={{ fontSize: '11px', fontWeight: 600, color: '#f97316' }}>
                🟠 2. Practice Locked
              </span>
              <span style={{ fontSize: '9.5px', fontWeight: 700, padding: '1px 5px', borderRadius: '4px', background: 'rgba(249, 115, 22, 0.15)', color: '#f97316' }}>
                Reflection Pending
              </span>
            </div>
            <div style={{ fontSize: '20px', fontWeight: 800, color: '#f97316' }}>
              {data?.gateBlockedCount ?? (loading ? '...' : 0)}
            </div>
            <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
              Locked out due to mistake review
            </div>
          </div>

          {/* Card 3: Conceptual Block (Practiced but still stuck in 🔴) */}
          <div
            onClick={() => setSelectedCategory('conceptual_block')}
            style={{
              background: 'var(--surface)',
              border: selectedCategory === 'conceptual_block' ? '2px solid #ef4444' : '1px solid var(--border-light)',
              borderRadius: '8px',
              padding: '10px 12px',
              cursor: 'pointer',
              transition: 'all 0.15s ease'
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2px' }}>
              <span style={{ fontSize: '11px', fontWeight: 600, color: '#ef4444' }}>
                🔴 3. Needs Re-Teach
              </span>
              <span style={{ fontSize: '9.5px', fontWeight: 700, padding: '1px 5px', borderRadius: '4px', background: 'rgba(239, 68, 68, 0.15)', color: '#ef4444' }}>
                Stuck &lt;50%
              </span>
            </div>
            <div style={{ fontSize: '20px', fontWeight: 800, color: '#ef4444' }}>
              {data?.conceptualBlockCount ?? (loading ? '...' : 0)}
            </div>
            <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
              Practiced questions, but still &lt;50%
            </div>
          </div>

          {/* Card 4: Remediation Neglected (0 practice done on 🔴 topic) */}
          <div
            onClick={() => setSelectedCategory('neglected_topic')}
            style={{
              background: 'var(--surface)',
              border: selectedCategory === 'neglected_topic' ? '2px solid #eab308' : '1px solid var(--border-light)',
              borderRadius: '8px',
              padding: '10px 12px',
              cursor: 'pointer',
              transition: 'all 0.15s ease'
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2px' }}>
              <span style={{ fontSize: '11px', fontWeight: 600, color: '#eab308' }}>
                🟡 4. Practice Neglected
              </span>
              <span style={{ fontSize: '9.5px', fontWeight: 700, padding: '1px 5px', borderRadius: '4px', background: 'rgba(234, 179, 8, 0.15)', color: '#eab308' }}>
                0 Sets Done
              </span>
            </div>
            <div style={{ fontSize: '20px', fontWeight: 800, color: '#eab308' }}>
              {data?.neglectedTopicCount ?? (loading ? '...' : 0)}
            </div>
            <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
              Weak topic with 0 practice started
            </div>
          </div>
        </div>

        {/* Filter Controls Toolbar */}
        <div style={{
          background: 'var(--surface)',
          border: '1px solid var(--border-light)',
          borderRadius: '8px',
          padding: '8px 12px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '8px'
        }}>
          {/* Category Tabs */}
          <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
            {[
              { id: 'all', label: `All (${data?.totalItems ?? 0})` },
              { id: 'missed_exam', label: `🔴 Missed (${data?.criticalCount ?? 0})` },
              { id: 'reflection_gate', label: `🟠 Locked (${data?.gateBlockedCount ?? 0})` },
              { id: 'conceptual_block', label: `🔴 Re-Teach (${data?.conceptualBlockCount ?? 0})` },
              { id: 'neglected_topic', label: `🟡 0 Practice (${data?.neglectedTopicCount ?? 0})` }
            ].map(tab => (
              <button
                key={tab.id}
                onClick={() => setSelectedCategory(tab.id)}
                style={{
                  background: selectedCategory === tab.id ? 'var(--accent)' : 'var(--bg-soft, rgba(255, 255, 255, 0.04))',
                  color: selectedCategory === tab.id ? '#ffffff' : 'var(--text)',
                  border: '1px solid ' + (selectedCategory === tab.id ? 'var(--accent)' : 'var(--border)'),
                  borderRadius: '6px',
                  padding: '4px 10px',
                  fontSize: '11px',
                  fontWeight: 600,
                  cursor: 'pointer',
                  transition: 'all 0.15s ease'
                }}
              >
                {tab.label}
              </button>
            ))}
          </div>

          {/* Right Filters: Batch & Search */}
          <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
            <select
              value={selectedBatch}
              onChange={(e) => setSelectedBatch(e.target.value)}
              style={{
                background: 'var(--surface)',
                border: '1px solid var(--border)',
                borderRadius: '6px',
                padding: '4px 8px',
                fontSize: '11.5px',
                color: 'var(--text)',
                outline: 'none',
                cursor: 'pointer'
              }}
            >
              <option value="all">All Batches</option>
              {batches.map(b => (
                <option key={b} value={b}>{b}</option>
              ))}
            </select>

            <input
              type="text"
              placeholder="Search student or topic..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              style={{
                background: 'var(--surface)',
                border: '1px solid var(--border)',
                borderRadius: '6px',
                padding: '4px 8px',
                fontSize: '11.5px',
                color: 'var(--text)',
                outline: 'none',
                minWidth: '160px'
              }}
            />
          </div>
        </div>

        {/* Loading & Error States */}
        {loading && !data && (
          <div style={{ textAlign: 'center', padding: '30px 0', color: 'var(--text-muted)' }}>
            <div style={{ fontSize: '22px', marginBottom: '6px' }}>⏳</div>
            <div style={{ fontSize: '12.5px', fontWeight: 600 }}>Analyzing exam baseline performance & practice recovery status...</div>
          </div>
        )}

        {error && !loading && (
          <div style={{
            background: 'rgba(239, 68, 68, 0.1)',
            border: '1px solid rgba(239, 68, 68, 0.3)',
            color: 'var(--danger, #ef4444)',
            padding: '10px 14px',
            borderRadius: '6px',
            fontSize: '12px',
            fontWeight: 600
          }}>
            ⚠️ {error}
          </div>
        )}

        {/* Empty State */}
        {!loading && !error && filteredItems.length === 0 && (
          <div style={{
            background: 'var(--surface)',
            border: '1px solid var(--border-light)',
            borderRadius: '8px',
            padding: '30px 16px',
            textAlign: 'center',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: '8px'
          }}>
            <div style={{ fontSize: '32px' }}>🎉</div>
            <h3 style={{ fontSize: '15px', fontWeight: 800, color: 'var(--text)', margin: 0 }}>
              All Clear! No Remediation Blockers
            </h3>
            <p style={{ fontSize: '12px', color: 'var(--text-muted)', margin: 0, maxWidth: '480px' }}>
              {selectedBatch !== 'all' || selectedCategory !== 'all' || searchQuery
                ? 'No students match your selected filters. Try switching batches or categories.'
                : 'All scheduled exams are baselined, practice sets are unlocked, and students are successfully recovering from weak topics!'}
            </p>
          </div>
        )}

        {/* Intervention Cards Feed */}
        {!error && filteredItems.length > 0 && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <div style={{ fontSize: '11.5px', fontWeight: 600, color: 'var(--text-muted)' }}>
              Showing {filteredItems.length} student intervention{filteredItems.length === 1 ? '' : 's'}
            </div>

            {filteredItems.map(item => {
              const isMissed = item.category === 'missed_exam';
              const isBlock = item.category === 'conceptual_block';
              const isGate = item.category === 'reflection_gate';

              const badgeColor = (isMissed || isBlock) ? 'var(--danger, #ef4444)' : (isGate ? '#f97316' : '#eab308');
              const badgeBg = (isMissed || isBlock) ? 'rgba(239, 68, 68, 0.12)' : (isGate ? 'rgba(249, 115, 22, 0.12)' : 'rgba(234, 179, 8, 0.12)');

              const categoryBadgeText = isMissed 
                ? '🔴 1. Baseline Missed' 
                : (isGate 
                    ? '🟠 2. Locked (Reflection)' 
                    : (isBlock 
                        ? '🔴 3. Re-Teach (Stuck 🔴)' 
                        : '🟡 4. 0 Practice'));

              return (
                <div
                  key={item.id}
                  style={{
                    background: 'var(--surface)',
                    border: '1px solid ' + ((isMissed || isBlock) ? 'rgba(239, 68, 68, 0.4)' : 'var(--border-light)'),
                    borderLeft: `3px solid ${badgeColor}`,
                    borderRadius: '8px',
                    padding: '10px 14px',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    flexWrap: 'wrap',
                    gap: '10px',
                    boxShadow: 'var(--shadow-sm)'
                  }}
                >
                  {/* Left Column: Student & Issue */}
                  <div style={{ flex: 1, minWidth: '260px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', marginBottom: '4px' }}>
                      <span style={{ fontSize: '13.5px', fontWeight: 800, color: 'var(--text)' }}>
                        {item.studentName}
                      </span>
                      <span style={{
                        fontSize: '10.5px',
                        fontWeight: 600,
                        padding: '1px 6px',
                        borderRadius: '4px',
                        background: 'var(--bg-soft, rgba(255, 255, 255, 0.05))',
                        color: 'var(--text-muted)',
                        border: '1px solid var(--border)'
                      }}>
                        {item.className}
                      </span>
                      <span style={{
                        fontSize: '10.5px',
                        fontWeight: 700,
                        padding: '1px 6px',
                        borderRadius: '4px',
                        background: badgeBg,
                        color: badgeColor
                      }}>
                        {categoryBadgeText}
                      </span>
                    </div>

                    <div style={{ fontSize: '12.5px', fontWeight: 700, color: 'var(--text)', marginBottom: '2px' }}>
                      {item.title}
                    </div>

                    <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginBottom: '4px' }}>
                      {item.subtitle}
                    </div>

                    <div style={{ fontSize: '11.5px', color: 'var(--text)', opacity: 0.85, lineHeight: 1.35 }}>
                      💡 {item.description}
                    </div>
                  </div>

                  {/* Right Column: 1-Click Action Buttons */}
                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
                    
                    {/* 1. WhatsApp 1-Click Action */}
                    <button
                      onClick={() => handleOpenWhatsApp(item.phone || item.parentPhone, item.whatsappMessage)}
                      style={{
                        background: '#25D366',
                        color: '#ffffff',
                        border: 'none',
                        borderRadius: '6px',
                        padding: '5px 10px',
                        fontSize: '11.5px',
                        fontWeight: 700,
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '5px',
                        boxShadow: '0 2px 4px rgba(37, 211, 102, 0.25)'
                      }}
                      title="Open WhatsApp with pre-filled message"
                    >
                      <span>💬</span>
                      <span>{item.actionLabel}</span>
                    </button>

                    {/* 2. Copy Message */}
                    <button
                      onClick={() => handleCopyMessage(item.id, item.whatsappMessage)}
                      style={{
                        background: 'var(--surface)',
                        color: 'var(--text-muted)',
                        border: '1px solid var(--border)',
                        borderRadius: '6px',
                        padding: '5px 8px',
                        fontSize: '11px',
                        fontWeight: 600,
                        cursor: 'pointer'
                      }}
                      title="Copy pre-composed message"
                    >
                      {copiedId === item.id ? '✓ Copied' : '📋 Copy'}
                    </button>

                    {/* 3. View Student Dossier Drill-down */}
                    <button
                      onClick={() => router.push(`/admin/reports/learning-quotient?studentCode=${encodeURIComponent(item.studentCode)}`)}
                      style={{
                        background: 'var(--accent-soft, rgba(217, 123, 56, 0.12))',
                        color: 'var(--accent)',
                        border: '1px solid var(--accent)',
                        borderRadius: '6px',
                        padding: '5px 10px',
                        fontSize: '11.5px',
                        fontWeight: 700,
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '4px'
                      }}
                      title="View Student 4-Pillar Learning Profile"
                    >
                      <span>📊</span>
                      <span>Dossier</span>
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        )}

      </main>
    </div>
  );
}
