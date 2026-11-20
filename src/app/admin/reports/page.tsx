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
  const [copiedAgenda, setCopiedAgenda] = useState(false);

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
        setError('Failed to load classroom remediation data.');
      }
    } catch (err: any) {
      console.error('Error fetching intervention queue:', err);
      setError(err.message || 'An unexpected error occurred while loading remediation data.');
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
      // Search query filter (search by topic name, student name, or topic code)
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase();
        const matchesName = (item.studentName || '').toLowerCase().includes(q);
        const matchesTitle = item.title.toLowerCase().includes(q);
        const matchesTopic = (item.topicName || '').toLowerCase().includes(q);
        const matchesCode = (item.topicCode || '').toLowerCase().includes(q);
        const matchesStudents = item.students?.some(s => s.studentName.toLowerCase().includes(q));
        if (!matchesName && !matchesTitle && !matchesTopic && !matchesCode && !matchesStudents) {
          return false;
        }
      }
      return true;
    });
  }, [data, selectedBatch, selectedCategory, searchQuery]);

  // Copy Full Classroom Teaching Agenda for Whiteboard
  const handleCopyClassroomAgenda = () => {
    if (!data?.reTeachTopics) return;
    const targetTopics = data.reTeachTopics.filter(t => selectedBatch === 'all' || t.className === selectedBatch);
    if (targetTopics.length === 0) return;

    let agendaText = `📋 YASHCOM CLASSROOM RE-TEACH AGENDA\n`;
    agendaText += `Batch: ${selectedBatch === 'all' ? 'All Batches' : selectedBatch}\n`;
    agendaText += `Date: ${new Date().toLocaleDateString('en-IN')}\n`;
    agendaText += `==============================================\n\n`;

    targetTopics.forEach((t, idx) => {
      agendaText += `${idx + 1}. [${t.className}] ${t.topicName} (${t.topicCode})\n`;
      agendaText += `   Struggling Students (${t.studentCount}, Avg Mastery: ${t.avgMastery}%):\n`;
      t.students.forEach(s => {
        agendaText += `   • ${s.studentName} — ${s.mastery}% mastery (${s.questionsAttempted} Qs attempted)\n`;
      });
      agendaText += `\n`;
    });

    if (navigator?.clipboard) {
      navigator.clipboard.writeText(agendaText);
      setCopiedAgenda(true);
      setTimeout(() => setCopiedAgenda(false), 2500);
    }
  };

  // Copy Individual Topic Item Summary
  const handleCopyItemNote = (item: InterventionItem) => {
    let text = `📌 [${item.className}] ${item.title}\n${item.subtitle}\n`;
    if (item.students && item.students.length > 0) {
      text += `Students Needing Re-Teach:\n`;
      item.students.forEach(s => {
        text += `• ${s.studentName} (${s.mastery}%)\n`;
      });
    } else if (item.topics && item.topics.length > 0) {
      text += `Unattempted Weak Topics:\n`;
      item.topics.forEach(t => {
        text += `• ${t.topicName} (Exam: ${t.examScore}%)\n`;
      });
    }
    if (navigator?.clipboard) {
      navigator.clipboard.writeText(text);
      setCopiedId(item.id);
      setTimeout(() => setCopiedId(null), 2500);
    }
  };

  return (
    <div style={{ background: 'var(--bg)', flex: 1, display: 'flex', flexDirection: 'column' }}>

      {/* Reports Hub Sub-Navigation Bar */}
      <div style={{ maxWidth: '1280px', width: '100%', margin: '0 auto', padding: '8px 16px 0 16px' }}>
        <nav style={{ display: 'flex', gap: '14px', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px', overflowX: 'auto' }}>
          <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--accent)', borderBottom: '2px solid var(--accent)', paddingBottom: '4px', whiteSpace: 'nowrap' }}>
            ⚡ Classroom Remediation Hub
          </span>
          <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer', whiteSpace: 'nowrap' }} onClick={() => router.push('/admin/reports/daily-practice')}>
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

      {/* Main Workspace */}
      <main style={{ flex: 1, padding: '10px 14px', maxWidth: '1280px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '10px' }}>
        
        {/* Page Title & Refresh */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <h2 style={{ fontSize: '17px', fontWeight: 800, color: 'var(--text)', margin: 0 }}>
                ⚡ Classroom Remediation Hub
              </h2>
              <span style={{
                fontSize: '10px',
                fontWeight: 700,
                padding: '1px 6px',
                borderRadius: '6px',
                background: 'rgba(239, 68, 68, 0.12)',
                color: 'var(--danger, #ef4444)'
              }}>
                Teaching & Concept Doubts
              </span>
            </div>
            <p style={{ fontSize: '11.5px', color: 'var(--text-muted)', margin: '2px 0 0 0' }}>
              Identifies concepts where students completed their 2 practice sets but failed to master the topic. Use this to guide 10-minute classroom whiteboard reviews.
            </p>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            {data?.reTeachTopics && data.reTeachTopics.length > 0 && (
              <button
                onClick={handleCopyClassroomAgenda}
                style={{
                  background: copiedAgenda ? 'rgba(16, 185, 129, 0.15)' : 'var(--accent)',
                  color: copiedAgenda ? 'var(--success, #10b981)' : '#ffffff',
                  border: copiedAgenda ? '1px solid var(--success)' : 'none',
                  borderRadius: '6px',
                  padding: '5px 12px',
                  fontSize: '11.5px',
                  fontWeight: 700,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  boxShadow: 'var(--shadow-sm)'
                }}
                title="Copy formatted whiteboard teaching agenda to clipboard"
              >
                <span>{copiedAgenda ? '✓' : '📋'}</span>
                <span>{copiedAgenda ? 'Agenda Copied!' : 'Copy Classroom Agenda'}</span>
              </button>
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
              <span>{refreshing ? 'Refreshing...' : 'Refresh'}</span>
            </button>
          </div>
        </div>

        {/* 3 Executive Metric Cards */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
          gap: '10px'
        }}>
          {/* Card 1: Re-Teach Agenda Topics (Primary Teacher Value) */}
          <div
            onClick={() => setSelectedCategory('conceptual_block')}
            style={{
              background: 'var(--surface)',
              border: selectedCategory === 'conceptual_block' ? '2px solid var(--danger, #ef4444)' : '1px solid var(--border-light)',
              borderRadius: '8px',
              padding: '10px 12px',
              cursor: 'pointer',
              transition: 'all 0.15s ease'
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2px' }}>
              <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--danger, #ef4444)' }}>
                🔴 1. Needs Re-Teach (Topics)
              </span>
              <span style={{ fontSize: '9.5px', fontWeight: 700, padding: '1px 5px', borderRadius: '4px', background: 'rgba(239, 68, 68, 0.15)', color: 'var(--danger, #ef4444)' }}>
                Classroom Action
              </span>
            </div>
            <div style={{ fontSize: '20px', fontWeight: 800, color: 'var(--danger, #ef4444)' }}>
              {data?.conceptualBlockCount ?? (loading ? '...' : 0)}
              <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', marginLeft: '6px' }}>
                ({data?.reTeachStudentCount ?? 0} students)
              </span>
            </div>
            <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
              Practice done, concept still stuck &lt; 50%
            </div>
          </div>

          {/* Card 2: Neglected Practice (0 Sets Done) */}
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
              <span style={{ fontSize: '11px', fontWeight: 700, color: '#eab308' }}>
                🟡 2. Practice Neglected
              </span>
              <span style={{ fontSize: '9.5px', fontWeight: 700, padding: '1px 5px', borderRadius: '4px', background: 'rgba(234, 179, 8, 0.15)', color: '#eab308' }}>
                0 Sets Done
              </span>
            </div>
            <div style={{ fontSize: '20px', fontWeight: 800, color: '#eab308' }}>
              {data?.neglectedTopicCount ?? (loading ? '...' : 0)}
              <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', marginLeft: '6px' }}>
                students
              </span>
            </div>
            <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
              Exam weakness with 0 practice workouts
            </div>
          </div>

          {/* Card 3: Missed Baseline Exams */}
          <div
            onClick={() => setSelectedCategory('missed_exam')}
            style={{
              background: 'var(--surface)',
              border: selectedCategory === 'missed_exam' ? '2px solid #64748b' : '1px solid var(--border-light)',
              borderRadius: '8px',
              padding: '10px 12px',
              cursor: 'pointer',
              transition: 'all 0.15s ease'
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2px' }}>
              <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)' }}>
                ⚪ 3. Missed Exams
              </span>
              <span style={{ fontSize: '9.5px', fontWeight: 700, padding: '1px 5px', borderRadius: '4px', background: 'rgba(100, 116, 139, 0.15)', color: 'var(--text-muted)' }}>
                Baseline
              </span>
            </div>
            <div style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text)' }}>
              {data?.criticalCount ?? (loading ? '...' : 0)}
              <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', marginLeft: '6px' }}>
                exams
              </span>
            </div>
            <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
              Scheduled exams unattempted
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
              { id: 'conceptual_block', label: `🔴 Re-Teach Topics (${data?.conceptualBlockCount ?? 0})` },
              { id: 'neglected_topic', label: `🟡 0 Practice Students (${data?.neglectedTopicCount ?? 0})` },
              { id: 'missed_exam', label: `⚪ Missed Exams (${data?.criticalCount ?? 0})` }
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
              placeholder="Search topic or student..."
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

        {/* Loading State */}
        {loading && !data && (
          <div style={{ textAlign: 'center', padding: '30px 0', color: 'var(--text-muted)' }}>
            <div style={{ fontSize: '22px', marginBottom: '6px' }}>⏳</div>
            <div style={{ fontSize: '12.5px', fontWeight: 600 }}>Analyzing exam baseline performance & classroom re-teach topics...</div>
          </div>
        )}

        {/* Error State */}
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
              All Clear! No Classroom Concept Blockers
            </h3>
            <p style={{ fontSize: '12px', color: 'var(--text-muted)', margin: 0, maxWidth: '480px' }}>
              {selectedBatch !== 'all' || selectedCategory !== 'all' || searchQuery
                ? 'No items match your selected filters. Try switching batches or tabs.'
                : 'All scheduled exams are baselined and students are progressing smoothly through their curriculum!'}
            </p>
          </div>
        )}

        {/* Actionable Digest Feed */}
        {!error && filteredItems.length > 0 && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <div style={{ fontSize: '11.5px', fontWeight: 600, color: 'var(--text-muted)' }}>
              Showing {filteredItems.length} classroom remediation item{filteredItems.length === 1 ? '' : 's'}
            </div>

            {filteredItems.map(item => {
              const isBlock = item.category === 'conceptual_block';
              const isNeglect = item.category === 'neglected_topic';
              const isMissed = item.category === 'missed_exam';

              const badgeColor = isBlock ? 'var(--danger, #ef4444)' : (isNeglect ? '#eab308' : '#64748b');
              const badgeBg = isBlock ? 'rgba(239, 68, 68, 0.12)' : (isNeglect ? 'rgba(234, 179, 8, 0.12)' : 'rgba(100, 116, 139, 0.12)');
              const categoryLabel = isBlock ? '🔴 Needs Re-Teach' : (isNeglect ? '🟡 0 Practice' : '⚪ Missed Exam');

              return (
                <div
                  key={item.id}
                  style={{
                    background: 'var(--surface)',
                    border: '1px solid ' + (isBlock ? 'rgba(239, 68, 68, 0.35)' : 'var(--border-light)'),
                    borderLeft: `4px solid ${badgeColor}`,
                    borderRadius: '8px',
                    padding: '12px 14px',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '8px',
                    boxShadow: 'var(--shadow-sm)'
                  }}
                >
                  {/* Card Header */}
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '8px' }}>
                    <div style={{ flex: 1, minWidth: '260px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', marginBottom: '3px' }}>
                        <span style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text)' }}>
                          {item.title}
                        </span>
                        <span style={{
                          fontSize: '10px',
                          fontWeight: 700,
                          padding: '1px 6px',
                          borderRadius: '4px',
                          background: 'var(--bg-soft, rgba(255, 255, 255, 0.05))',
                          color: 'var(--text-muted)',
                          border: '1px solid var(--border)'
                        }}>
                          {item.className}
                        </span>
                        <span style={{
                          fontSize: '10px',
                          fontWeight: 700,
                          padding: '1px 6px',
                          borderRadius: '4px',
                          background: badgeBg,
                          color: badgeColor
                        }}>
                          {categoryLabel}
                        </span>
                        {item.topicCode && (
                          <span style={{
                            fontSize: '9.5px',
                            fontWeight: 700,
                            padding: '1px 5px',
                            borderRadius: '4px',
                            background: 'rgba(59, 130, 246, 0.1)',
                            color: '#3b82f6',
                            border: '1px solid rgba(59, 130, 246, 0.25)'
                          }}>
                            {item.topicCode}
                          </span>
                        )}
                      </div>

                      <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', fontWeight: 600 }}>
                        {item.subtitle}
                      </div>
                    </div>

                    {/* Right Header: 1-Click Action Buttons */}
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
                      <button
                        onClick={() => handleCopyItemNote(item)}
                        style={{
                          background: 'var(--surface)',
                          color: 'var(--text)',
                          border: '1px solid var(--border)',
                          borderRadius: '6px',
                          padding: '4px 9px',
                          fontSize: '11px',
                          fontWeight: 600,
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '4px'
                        }}
                        title="Copy details to clipboard for notes or whiteboard"
                      >
                        <span>{copiedId === item.id ? '✓' : '📋'}</span>
                        <span>{copiedId === item.id ? 'Copied' : 'Copy Note'}</span>
                      </button>

                      {/* Dossier button (for student items or first student in topic group) */}
                      {(item.studentCode || (item.students && item.students[0]?.studentCode)) && (
                        <button
                          onClick={() => {
                            const sCode = item.studentCode || item.students![0].studentCode;
                            router.push(`/admin/reports/learning-quotient?studentCode=${encodeURIComponent(sCode)}`);
                          }}
                          style={{
                            background: 'var(--accent-soft, rgba(217, 123, 56, 0.12))',
                            color: 'var(--accent)',
                            border: '1px solid var(--accent)',
                            borderRadius: '6px',
                            padding: '4px 10px',
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
                      )}
                    </div>
                  </div>

                  {/* Card Content: Re-Teach Struggling Students Grid */}
                  {isBlock && item.students && item.students.length > 0 && (
                    <div style={{
                      marginTop: '4px',
                      padding: '8px 10px',
                      background: 'var(--bg-soft, rgba(0, 0, 0, 0.08))',
                      borderRadius: '6px',
                      border: '1px solid var(--border-light)'
                    }}>
                      <div style={{ fontSize: '10.5px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.5px', marginBottom: '6px' }}>
                        Students Requiring Classroom Whiteboard Review ({item.students.length}):
                      </div>
                      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                        {item.students.map(s => (
                          <div
                            key={s.studentCode}
                            onClick={() => router.push(`/admin/reports/learning-quotient?studentCode=${encodeURIComponent(s.studentCode)}`)}
                            style={{
                              display: 'inline-flex',
                              alignItems: 'center',
                              gap: '5px',
                              padding: '3px 8px',
                              borderRadius: '4px',
                              background: 'var(--surface)',
                              border: '1px solid var(--border)',
                              fontSize: '11px',
                              cursor: 'pointer',
                              color: 'var(--text)'
                            }}
                            title={`Click to view ${s.studentName}'s learning dossier`}
                          >
                            <span style={{ fontWeight: 700 }}>{s.studentName}</span>
                            <span style={{
                              fontWeight: 800,
                              color: s.mastery < 30 ? '#ef4444' : '#f59e0b',
                              fontSize: '10.5px'
                            }}>
                              {s.mastery}%
                            </span>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {/* Card Content: Neglected Topics Breakdown */}
                  {isNeglect && item.topics && item.topics.length > 0 && (
                    <div style={{
                      marginTop: '4px',
                      padding: '8px 10px',
                      background: 'var(--bg-soft, rgba(0, 0, 0, 0.08))',
                      borderRadius: '6px',
                      border: '1px solid var(--border-light)'
                    }}>
                      <div style={{ fontSize: '10.5px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.5px', marginBottom: '6px' }}>
                        Weak Topics From Exams With 0 Practice Sets Started ({item.topics.length}):
                      </div>
                      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                        {item.topics.map(t => (
                          <div
                            key={t.topicCode}
                            style={{
                              display: 'inline-flex',
                              alignItems: 'center',
                              gap: '6px',
                              padding: '3px 8px',
                              borderRadius: '4px',
                              background: 'var(--surface)',
                              border: '1px solid var(--border)',
                              fontSize: '11px',
                              color: 'var(--text)'
                            }}
                          >
                            <span style={{ fontWeight: 600 }}>{t.topicName}</span>
                            <span style={{ fontWeight: 800, color: '#eab308', fontSize: '10.5px' }}>
                              Exam: {t.examScore}%
                            </span>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                </div>
              );
            })}
          </div>
        )}

      </main>
    </div>
  );
}
