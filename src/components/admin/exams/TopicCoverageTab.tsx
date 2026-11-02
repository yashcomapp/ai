'use client';

import React, { useState, useEffect, useMemo, useDeferredValue } from 'react';
import { useAuth } from '@/context/AuthContext';
import { Batch } from './types';

interface TopicExam {
  examId: string;
  name: string;
  date: string;
  type: string;
}

interface StudentPerformance {
  studentCode: string;
  name: string;
  mastery: number;
  status: 'mastered' | 'practicing' | 'needsAttention' | 'unattempted';
  confidence: number;
  requiredConfidence: number;
}

interface ConductedTopic {
  topicCode: string;
  topicName: string;
  chapterName: string;
  subject: string;
  className: string;
  hasNumericals: boolean;
  examsConductedCount: number;
  exams: TopicExam[];
  batchAvgScore: number;
  totalStudents: number;
  studentsMastered: number;
  studentsPracticing: number;
  studentsNeedsAttention: number;
  students: StudentPerformance[];
}

interface TopicCoverageData {
  batchId: string;
  batchName: string;
  batchClass: string;
  totalStudents: number;
  conductedTopicsCount: number;
  topics: ConductedTopic[];
}

interface TopicCoverageTabProps {
  batches: Batch[];
}

export default function TopicCoverageTab({ batches }: TopicCoverageTabProps) {
  const { firebaseUser } = useAuth();
  
  // Batch selection
  const [selectedBatchId, setSelectedBatchId] = useState<string>('');
  
  // Data state
  const [data, setData] = useState<TopicCoverageData | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');
  
  // Search & Filter
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [subjectFilter, setSubjectFilter] = useState<string>('all');
  const [expandedTopicCode, setExpandedTopicCode] = useState<string | null>(null);
  
  // Modal for Assigning Targeted Practice
  const [assignModalTopic, setAssignModalTopic] = useState<ConductedTopic | null>(null);
  const [targetAudience, setTargetAudience] = useState<'needsAttention' | 'practicing' | 'struggling' | 'all' | 'custom'>('needsAttention');
  const [selectedStudentCodes, setSelectedStudentCodes] = useState<string[]>([]);
  const [setsCount, setSetsCount] = useState<number>(2);
  const [numericalFocus, setNumericalFocus] = useState<boolean>(false);
  const [teacherNote, setTeacherNote] = useState<string>('');
  const [isAssigning, setIsAssigning] = useState<boolean>(false);
  const [assignSuccessMsg, setAssignSuccessMsg] = useState<string>('');
  const [assignErrorMsg, setAssignErrorMsg] = useState<string>('');

  // Default to first batch if none selected
  useEffect(() => {
    if (!selectedBatchId && batches.length > 0) {
      setSelectedBatchId(batches[0].id);
    }
  }, [batches, selectedBatchId]);

  // Fetch coverage data when batch changes
  useEffect(() => {
    if (!selectedBatchId || !firebaseUser) return;
    
    let isMounted = true;
    setLoading(true);
    setError('');

    async function fetchCoverage() {
      try {
        const idToken = await firebaseUser!.getIdToken();
        const res = await fetch(`/api/admin/exams/topic-coverage?batchId=${encodeURIComponent(selectedBatchId)}`, {
          headers: {
            'Authorization': `Bearer ${idToken}`
          }
        });

        if (!res.ok) {
          const errData = await res.json().catch(() => ({}));
          throw new Error(errData.message || 'Failed to fetch topic coverage.');
        }

        const json = await res.json();
        if (isMounted) {
          setData(json);
        }
      } catch (err: any) {
        if (isMounted) {
          setError(err.message || 'Error loading conducted topics.');
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    fetchCoverage();

    return () => {
      isMounted = false;
    };
  }, [selectedBatchId, firebaseUser]);

  // Derived subjects list for filter pills
  const availableSubjects = useMemo(() => {
    if (!data?.topics) return [];
    const subjects = new Set<string>();
    data.topics.forEach(t => {
      if (t.subject) subjects.add(t.subject);
    });
    return Array.from(subjects);
  }, [data?.topics]);

  // Filtered topics
  const deferredSearch = useDeferredValue(searchQuery);
  const filteredTopics = useMemo(() => {
    if (!data?.topics) return [];
    return data.topics.filter(t => {
      const q = deferredSearch.toLowerCase().trim();
      const matchQuery = !q ||
        t.topicName.toLowerCase().includes(q) ||
        t.topicCode.toLowerCase().includes(q) ||
        t.chapterName.toLowerCase().includes(q) ||
        t.subject.toLowerCase().includes(q);

      const matchSubject = subjectFilter === 'all' || t.subject === subjectFilter;

      return matchQuery && matchSubject;
    });
  }, [data?.topics, deferredSearch, subjectFilter]);

  // Calculate high-level summary cards
  const summaryMetrics = useMemo(() => {
    if (!data?.topics || data.topics.length === 0) {
      return { totalConducted: 0, batchAvg: 0, totalMastered: 0, totalPracticing: 0, totalNeedsAttention: 0 };
    }
    const totalConducted = data.topics.length;
    let sumBatchAvg = 0;
    let mCount = 0;
    let pCount = 0;
    let nCount = 0;

    data.topics.forEach(t => {
      sumBatchAvg += t.batchAvgScore;
      mCount += t.studentsMastered;
      pCount += t.studentsPracticing;
      nCount += t.studentsNeedsAttention;
    });

    const batchAvg = Math.round(sumBatchAvg / totalConducted);
    return {
      totalConducted,
      batchAvg,
      totalMastered: mCount,
      totalPracticing: pCount,
      totalNeedsAttention: nCount
    };
  }, [data?.topics]);

  // Handler to open Assign Practice modal
  const handleOpenAssignModal = (topic: ConductedTopic) => {
    setAssignModalTopic(topic);
    setTargetAudience('needsAttention');
    // Preselect students needing attention (mastery < 50% or unattempted)
    const strugglingCodes = topic.students
      .filter(s => s.status === 'needsAttention' || s.status === 'unattempted')
      .map(s => s.studentCode);
    setSelectedStudentCodes(strugglingCodes.length > 0 ? strugglingCodes : topic.students.map(s => s.studentCode));
    setSetsCount(2);
    // Auto-enable numerical focus if topic has numericals
    setNumericalFocus(topic.hasNumericals);
    setTeacherNote('');
    setAssignSuccessMsg('');
    setAssignErrorMsg('');
  };

  // Change audience preset
  const handleAudienceChange = (audience: 'needsAttention' | 'practicing' | 'struggling' | 'all' | 'custom') => {
    setTargetAudience(audience);
    if (!assignModalTopic) return;

    if (audience === 'needsAttention') {
      const codes = assignModalTopic.students
        .filter(s => s.status === 'needsAttention' || s.status === 'unattempted')
        .map(s => s.studentCode);
      setSelectedStudentCodes(codes);
    } else if (audience === 'practicing') {
      const codes = assignModalTopic.students
        .filter(s => s.status === 'practicing')
        .map(s => s.studentCode);
      setSelectedStudentCodes(codes);
    } else if (audience === 'struggling') {
      const codes = assignModalTopic.students
        .filter(s => s.status === 'needsAttention' || s.status === 'unattempted' || s.status === 'practicing')
        .map(s => s.studentCode);
      setSelectedStudentCodes(codes);
    } else if (audience === 'all') {
      setSelectedStudentCodes(assignModalTopic.students.map(s => s.studentCode));
    }
  };

  const handleToggleStudentSelection = (sCode: string) => {
    setTargetAudience('custom');
    setSelectedStudentCodes(prev =>
      prev.includes(sCode) ? prev.filter(c => c !== sCode) : [...prev, sCode]
    );
  };

  const handleDispatchPractice = async () => {
    if (!assignModalTopic || selectedStudentCodes.length === 0 || !firebaseUser) return;

    setIsAssigning(true);
    setAssignSuccessMsg('');
    setAssignErrorMsg('');

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/exams/assign-practice', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          batchId: selectedBatchId,
          topicCode: assignModalTopic.topicCode,
          studentCodes: selectedStudentCodes,
          setsCount,
          numericalFocus: Boolean(numericalFocus && assignModalTopic.hasNumericals),
          note: teacherNote.trim()
        })
      });

      const resData = await res.json();
      if (!res.ok) {
        throw new Error(resData.message || 'Failed to dispatch practice assignment.');
      }

      setAssignSuccessMsg(resData.message || 'Practice successfully assigned!');
      setTimeout(() => {
        setAssignModalTopic(null);
      }, 1800);
    } catch (err: any) {
      setAssignErrorMsg(err.message || 'Error dispatching practice.');
    } finally {
      setIsAssigning(false);
    }
  };

  return (
    <div style={{ padding: '0 4px', color: 'var(--text)' }}>
      {/* 1. Header Toolbar & Batch Selector */}
      <div style={{
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'space-between',
        alignItems: 'center',
        gap: '12px',
        marginBottom: '20px',
        padding: '16px',
        background: 'var(--card-bg, #1a1e29)',
        borderRadius: '12px',
        border: '1px solid var(--border-light, #2d3748)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', flexWrap: 'wrap' }}>
          <span style={{ fontSize: '14px', fontWeight: 700, color: 'var(--text-muted, #94a3b8)' }}>
            Selected Batch:
          </span>
          <select
            value={selectedBatchId}
            onChange={(e) => setSelectedBatchId(e.target.value)}
            style={{
              padding: '8px 14px',
              borderRadius: '8px',
              background: '#0f172a',
              color: '#f8fafc',
              border: '1px solid #3b82f6',
              fontWeight: 600,
              fontSize: '14px',
              cursor: 'pointer'
            }}
          >
            {batches.map(b => (
              <option key={b.id} value={b.id}>
                {b.name || b.id} {b.class ? `(${b.class})` : ''}
              </option>
            ))}
          </select>

          <span style={{ fontSize: '13px', color: '#64748b' }}>
            {data ? `• ${data.totalStudents} Active Students` : ''}
          </span>
        </div>

        {/* Search Input */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <input
            type="text"
            placeholder="Search conducted topics or chapters..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{
              padding: '8px 12px',
              borderRadius: '8px',
              background: '#0f172a',
              color: '#f8fafc',
              border: '1px solid var(--border-light, #334155)',
              fontSize: '13px',
              width: '260px'
            }}
          />
        </div>
      </div>

      {/* 2. High-Level Summary Metrics Cards */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(210px, 1fr))',
        gap: '14px',
        marginBottom: '24px'
      }}>
        <div style={{
          background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.7), rgba(15, 23, 42, 0.9))',
          padding: '16px',
          borderRadius: '12px',
          border: '1px solid #334155'
        }}>
          <div style={{ fontSize: '12px', color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.5px', fontWeight: 700 }}>
            Conducted Topics
          </div>
          <div style={{ fontSize: '28px', fontWeight: 800, color: '#38bdf8', marginTop: '4px' }}>
            {summaryMetrics.totalConducted}
          </div>
          <div style={{ fontSize: '11px', color: '#64748b', marginTop: '2px' }}>
            Strictly tested in assigned exams
          </div>
        </div>

        <div style={{
          background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.7), rgba(15, 23, 42, 0.9))',
          padding: '16px',
          borderRadius: '12px',
          border: '1px solid #334155'
        }}>
          <div style={{ fontSize: '12px', color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.5px', fontWeight: 700 }}>
            Batch Mastery Average
          </div>
          <div style={{ fontSize: '28px', fontWeight: 800, color: summaryMetrics.batchAvg >= 75 ? '#22c55e' : (summaryMetrics.batchAvg >= 50 ? '#eab308' : '#ef4444'), marginTop: '4px' }}>
            {summaryMetrics.batchAvg}%
          </div>
          <div style={{ fontSize: '11px', color: '#64748b', marginTop: '2px' }}>
            Across all conducted topics
          </div>
        </div>

        <div style={{
          background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.7), rgba(15, 23, 42, 0.9))',
          padding: '16px',
          borderRadius: '12px',
          border: '1px solid #334155'
        }}>
          <div style={{ fontSize: '12px', color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.5px', fontWeight: 700 }}>
            Performance Distribution
          </div>
          <div style={{ display: 'flex', gap: '8px', marginTop: '8px', alignItems: 'center' }}>
            <span style={{ fontSize: '12px', background: 'rgba(34, 197, 94, 0.15)', color: '#4ade80', padding: '4px 8px', borderRadius: '6px', fontWeight: 700 }}>
              🟢 {summaryMetrics.totalMastered} Mastered
            </span>
            <span style={{ fontSize: '12px', background: 'rgba(234, 179, 8, 0.15)', color: '#facc15', padding: '4px 8px', borderRadius: '6px', fontWeight: 700 }}>
              🟡 {summaryMetrics.totalPracticing} Practicing
            </span>
            <span style={{ fontSize: '12px', background: 'rgba(239, 68, 68, 0.15)', color: '#f87171', padding: '4px 8px', borderRadius: '6px', fontWeight: 700 }}>
              🔴 {summaryMetrics.totalNeedsAttention} Needs Attention
            </span>
          </div>
        </div>
      </div>

      {/* 3. Subject Filter Pills */}
      {availableSubjects.length > 0 && (
        <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '16px' }}>
          <button
            onClick={() => setSubjectFilter('all')}
            style={{
              padding: '6px 14px',
              borderRadius: '20px',
              fontSize: '12px',
              fontWeight: 700,
              cursor: 'pointer',
              border: 'none',
              background: subjectFilter === 'all' ? '#3b82f6' : '#1e293b',
              color: subjectFilter === 'all' ? '#ffffff' : '#94a3b8'
            }}
          >
            All Subjects ({data?.topics.length || 0})
          </button>
          {availableSubjects.map(sub => {
            const count = data?.topics.filter(t => t.subject === sub).length || 0;
            return (
              <button
                key={sub}
                onClick={() => setSubjectFilter(sub)}
                style={{
                  padding: '6px 14px',
                  borderRadius: '20px',
                  fontSize: '12px',
                  fontWeight: 700,
                  cursor: 'pointer',
                  border: 'none',
                  background: subjectFilter === sub ? '#3b82f6' : '#1e293b',
                  color: subjectFilter === sub ? '#ffffff' : '#94a3b8'
                }}
              >
                {sub} ({count})
              </button>
            );
          })}
        </div>
      )}

      {/* 4. Loading & Error States */}
      {loading && (
        <div style={{ textAlign: 'center', padding: '40px 20px', color: '#94a3b8' }}>
          <div style={{ fontSize: '16px', fontWeight: 600 }}>⏳ Loading conducted topics for this batch...</div>
          <div style={{ fontSize: '12px', color: '#64748b', marginTop: '6px' }}>Aggregating exam assignments and student mastery scores.</div>
        </div>
      )}

      {error && !loading && (
        <div style={{
          padding: '16px',
          background: 'rgba(239, 68, 68, 0.1)',
          border: '1px solid #ef4444',
          borderRadius: '8px',
          color: '#f87171',
          marginBottom: '20px'
        }}>
          ⚠️ {error}
        </div>
      )}

      {/* 5. Conducted Topics Table */}
      {!loading && !error && filteredTopics.length === 0 && (
        <div style={{
          textAlign: 'center',
          padding: '60px 20px',
          background: 'var(--card-bg, #1a1e29)',
          borderRadius: '12px',
          border: '1px dashed #334155',
          color: '#94a3b8'
        }}>
          <div style={{ fontSize: '18px', fontWeight: 700, color: '#f1f5f9' }}>No Conducted Topics Found</div>
          <div style={{ fontSize: '13px', marginTop: '6px' }}>
            No exams have been assigned or conducted on topics for this batch yet.
          </div>
        </div>
      )}

      {!loading && filteredTopics.length > 0 && (
        <div style={{
          background: 'var(--card-bg, #1a1e29)',
          borderRadius: '12px',
          border: '1px solid var(--border-light, #2d3748)',
          overflow: 'hidden'
        }}>
          <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
            <thead>
              <tr style={{ background: '#0f172a', borderBottom: '1px solid #334155', color: '#94a3b8' }}>
                <th style={{ padding: '12px 16px', fontWeight: 700 }}>Topic & Chapter</th>
                <th style={{ padding: '12px 16px', fontWeight: 700 }}>Subject</th>
                <th style={{ padding: '12px 16px', fontWeight: 700 }}>Exams Tested</th>
                <th style={{ padding: '12px 16px', fontWeight: 700 }}>Batch Avg</th>
                <th style={{ padding: '12px 16px', fontWeight: 700 }}>Student Mastery Breakdown</th>
                <th style={{ padding: '12px 16px', fontWeight: 700, textAlign: 'right' }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {filteredTopics.map((topic) => {
                const isExpanded = expandedTopicCode === topic.topicCode;

                return (
                  <React.Fragment key={topic.topicCode}>
                    <tr
                      style={{
                        borderBottom: '1px solid #1e293b',
                        background: isExpanded ? 'rgba(59, 130, 246, 0.05)' : 'transparent',
                        transition: 'background 0.2s'
                      }}
                    >
                      {/* Topic & Chapter */}
                      <td style={{ padding: '14px 16px' }}>
                        <div style={{ fontWeight: 700, color: '#f8fafc', fontSize: '14px' }}>
                          {topic.topicName}
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginTop: '4px', flexWrap: 'wrap' }}>
                          <span style={{ fontSize: '11px', color: '#94a3b8', background: '#0f172a', padding: '2px 6px', borderRadius: '4px', fontFamily: 'monospace' }}>
                            {topic.topicCode}
                          </span>
                          <span style={{ fontSize: '12px', color: '#cbd5e1' }}>
                            {topic.chapterName}
                          </span>
                          {topic.hasNumericals ? (
                            <span style={{ fontSize: '10px', background: 'rgba(56, 189, 248, 0.15)', color: '#38bdf8', padding: '2px 6px', borderRadius: '4px', fontWeight: 700 }}>
                              🔢 Numericals (ONE)
                            </span>
                          ) : (
                            <span style={{ fontSize: '10px', background: 'rgba(148, 163, 184, 0.15)', color: '#94a3b8', padding: '2px 6px', borderRadius: '4px' }}>
                              📖 Conceptual
                            </span>
                          )}
                        </div>
                      </td>

                      {/* Subject */}
                      <td style={{ padding: '14px 16px', color: '#cbd5e1', fontWeight: 600 }}>
                        {topic.subject}
                      </td>

                      {/* Exams Tested */}
                      <td style={{ padding: '14px 16px' }}>
                        <span style={{
                          background: '#0f172a',
                          color: '#e2e8f0',
                          padding: '4px 8px',
                          borderRadius: '6px',
                          fontWeight: 700,
                          fontSize: '12px',
                          border: '1px solid #334155'
                        }}>
                          {topic.examsConductedCount} Exam{topic.examsConductedCount === 1 ? '' : 's'}
                        </span>
                      </td>

                      {/* Batch Avg */}
                      <td style={{ padding: '14px 16px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <div style={{
                            width: '44px',
                            fontWeight: 800,
                            fontSize: '14px',
                            color: topic.batchAvgScore >= 75 ? '#22c55e' : (topic.batchAvgScore >= 50 ? '#eab308' : '#ef4444')
                          }}>
                            {topic.batchAvgScore}%
                          </div>
                          <div style={{ width: '80px', height: '6px', background: '#334155', borderRadius: '3px', overflow: 'hidden' }}>
                            <div style={{
                              width: `${topic.batchAvgScore}%`,
                              height: '100%',
                              background: topic.batchAvgScore >= 75 ? '#22c55e' : (topic.batchAvgScore >= 50 ? '#eab308' : '#ef4444'),
                              borderRadius: '3px'
                            }} />
                          </div>
                        </div>
                      </td>

                      {/* Student Mastery Breakdown */}
                      <td style={{ padding: '14px 16px' }}>
                        <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                          <button
                            onClick={() => setExpandedTopicCode(isExpanded ? null : topic.topicCode)}
                            title="Click to view student roster"
                            style={{
                              background: 'rgba(34, 197, 94, 0.15)',
                              color: '#4ade80',
                              border: '1px solid rgba(34, 197, 94, 0.3)',
                              padding: '3px 8px',
                              borderRadius: '4px',
                              fontSize: '11px',
                              fontWeight: 700,
                              cursor: 'pointer'
                            }}
                          >
                            🟢 {topic.studentsMastered}
                          </button>
                          <button
                            onClick={() => setExpandedTopicCode(isExpanded ? null : topic.topicCode)}
                            title="Click to view student roster"
                            style={{
                              background: 'rgba(234, 179, 8, 0.15)',
                              color: '#facc15',
                              border: '1px solid rgba(234, 179, 8, 0.3)',
                              padding: '3px 8px',
                              borderRadius: '4px',
                              fontSize: '11px',
                              fontWeight: 700,
                              cursor: 'pointer'
                            }}
                          >
                            🟡 {topic.studentsPracticing}
                          </button>
                          <button
                            onClick={() => setExpandedTopicCode(isExpanded ? null : topic.topicCode)}
                            title="Click to view student roster"
                            style={{
                              background: 'rgba(239, 68, 68, 0.15)',
                              color: '#f87171',
                              border: '1px solid rgba(239, 68, 68, 0.3)',
                              padding: '3px 8px',
                              borderRadius: '4px',
                              fontSize: '11px',
                              fontWeight: 700,
                              cursor: 'pointer'
                            }}
                          >
                            🔴 {topic.studentsNeedsAttention}
                          </button>
                          <button
                            onClick={() => setExpandedTopicCode(isExpanded ? null : topic.topicCode)}
                            style={{
                              background: 'none',
                              border: 'none',
                              color: '#60a5fa',
                              fontSize: '11px',
                              cursor: 'pointer',
                              padding: '0 4px',
                              textDecoration: 'underline'
                            }}
                          >
                            {isExpanded ? 'Hide' : 'Details'}
                          </button>
                        </div>
                      </td>

                      {/* Actions */}
                      <td style={{ padding: '14px 16px', textAlign: 'right' }}>
                        <button
                          onClick={() => handleOpenAssignModal(topic)}
                          style={{
                            background: 'linear-gradient(135deg, #2563eb, #1d4ed8)',
                            color: '#ffffff',
                            border: 'none',
                            padding: '6px 14px',
                            borderRadius: '6px',
                            fontWeight: 700,
                            fontSize: '12px',
                            cursor: 'pointer',
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '6px',
                            boxShadow: '0 2px 4px rgba(0,0,0,0.2)'
                          }}
                        >
                          <span>🎯</span> Assign Practice
                        </button>
                      </td>
                    </tr>

                    {/* Collapsible Student Roster */}
                    {isExpanded && (
                      <tr style={{ background: '#0b1120', borderBottom: '1px solid #1e293b' }}>
                        <td colSpan={6} style={{ padding: '16px 20px' }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                            <div style={{ fontSize: '13px', fontWeight: 700, color: '#f8fafc' }}>
                              Student Mastery Breakdown for <span style={{ color: '#38bdf8' }}>{topic.topicName}</span>
                            </div>
                            <button
                              onClick={() => handleOpenAssignModal(topic)}
                              style={{
                                background: '#3b82f6',
                                color: '#ffffff',
                                border: 'none',
                                padding: '4px 10px',
                                borderRadius: '4px',
                                fontSize: '11px',
                                fontWeight: 700,
                                cursor: 'pointer'
                              }}
                            >
                              Assign Practice on This Topic
                            </button>
                          </div>

                          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', gap: '8px' }}>
                            {topic.students.map((st) => (
                              <div
                                key={st.studentCode}
                                style={{
                                  background: '#1e293b',
                                  padding: '8px 12px',
                                  borderRadius: '6px',
                                  border: '1px solid #334155',
                                  display: 'flex',
                                  justifyContent: 'space-between',
                                  alignItems: 'center'
                                }}
                              >
                                <div>
                                  <div style={{ fontWeight: 600, fontSize: '13px', color: '#f8fafc' }}>
                                    {st.name}
                                  </div>
                                  <div style={{ fontSize: '10px', color: '#94a3b8' }}>
                                    {st.status === 'unattempted' ? 'Unattempted' : `Confidence: ${st.confidence}/${st.requiredConfidence}`}
                                  </div>
                                </div>
                                <div style={{ textAlign: 'right' }}>
                                  <span style={{
                                    fontSize: '11px',
                                    fontWeight: 700,
                                    padding: '2px 6px',
                                    borderRadius: '4px',
                                    background: st.status === 'mastered' ? 'rgba(34, 197, 94, 0.2)' : (st.status === 'practicing' ? 'rgba(234, 179, 8, 0.2)' : 'rgba(239, 68, 68, 0.2)'),
                                    color: st.status === 'mastered' ? '#4ade80' : (st.status === 'practicing' ? '#facc15' : '#f87171')
                                  }}>
                                    {st.status === 'unattempted' ? '🔴 0%' : `${st.status === 'mastered' ? '🟢' : (st.status === 'practicing' ? '🟡' : '🔴')} ${st.mastery}%`}
                                  </span>
                                </div>
                              </div>
                            ))}
                          </div>
                        </td>
                      </tr>
                    )}
                  </React.Fragment>
                );
              })}
            </tbody>
          </table>
        </div>
      )}

      {/* 6. Assign Targeted Practice Modal */}
      {assignModalTopic && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          background: 'rgba(0, 0, 0, 0.75)',
          backdropFilter: 'blur(4px)',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 1000,
          padding: '16px'
        }}>
          <div style={{
            background: '#1e293b',
            borderRadius: '16px',
            border: '1px solid #3b82f6',
            width: '100%',
            maxWidth: '620px',
            maxHeight: '90vh',
            display: 'flex',
            flexDirection: 'column',
            boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.5)',
            overflow: 'hidden'
          }}>
            {/* Modal Header */}
            <div style={{ padding: '16px 20px', borderBottom: '1px solid #334155', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <h3 style={{ margin: 0, fontSize: '17px', fontWeight: 800, color: '#f8fafc' }}>
                  🎯 Assign Practice: {assignModalTopic.topicName}
                </h3>
                <div style={{ fontSize: '12px', color: '#94a3b8', marginTop: '2px' }}>
                  {assignModalTopic.subject} • {assignModalTopic.chapterName}
                </div>
              </div>
              <button
                onClick={() => setAssignModalTopic(null)}
                style={{
                  background: 'none',
                  border: 'none',
                  color: '#94a3b8',
                  fontSize: '20px',
                  cursor: 'pointer',
                  padding: '4px'
                }}
              >
                ✕
              </button>
            </div>

            {/* Modal Body */}
            <div style={{ padding: '20px', overflowY: 'auto', flex: 1 }}>
              {/* Preset Audience Selection */}
              <div style={{ marginBottom: '18px' }}>
                <label style={{ fontSize: '13px', fontWeight: 700, color: '#cbd5e1', display: 'block', marginBottom: '8px' }}>
                  Target Audience Preset:
                </label>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '8px' }}>
                  <button
                    type="button"
                    onClick={() => handleAudienceChange('needsAttention')}
                    style={{
                      padding: '8px 12px',
                      borderRadius: '8px',
                      fontSize: '12px',
                      fontWeight: 700,
                      cursor: 'pointer',
                      textAlign: 'left',
                      background: targetAudience === 'needsAttention' ? 'rgba(239, 68, 68, 0.2)' : '#0f172a',
                      border: targetAudience === 'needsAttention' ? '1.5px solid #ef4444' : '1px solid #334155',
                      color: targetAudience === 'needsAttention' ? '#f87171' : '#cbd5e1'
                    }}
                  >
                    🔴 Struggling Only (&lt; 50% / Unattempted)
                    <div style={{ fontSize: '10px', color: '#94a3b8', marginTop: '2px' }}>
                      {assignModalTopic.students.filter(s => s.status === 'needsAttention' || s.status === 'unattempted').length} students
                    </div>
                  </button>

                  <button
                    type="button"
                    onClick={() => handleAudienceChange('practicing')}
                    style={{
                      padding: '8px 12px',
                      borderRadius: '8px',
                      fontSize: '12px',
                      fontWeight: 700,
                      cursor: 'pointer',
                      textAlign: 'left',
                      background: targetAudience === 'practicing' ? 'rgba(234, 179, 8, 0.2)' : '#0f172a',
                      border: targetAudience === 'practicing' ? '1.5px solid #eab308' : '1px solid #334155',
                      color: targetAudience === 'practicing' ? '#facc15' : '#cbd5e1'
                    }}
                  >
                    🟡 In-Progress (50% - 89%)
                    <div style={{ fontSize: '10px', color: '#94a3b8', marginTop: '2px' }}>
                      {assignModalTopic.students.filter(s => s.status === 'practicing').length} students
                    </div>
                  </button>

                  <button
                    type="button"
                    onClick={() => handleAudienceChange('struggling')}
                    style={{
                      padding: '8px 12px',
                      borderRadius: '8px',
                      fontSize: '12px',
                      fontWeight: 700,
                      cursor: 'pointer',
                      textAlign: 'left',
                      background: targetAudience === 'struggling' ? 'rgba(59, 130, 246, 0.2)' : '#0f172a',
                      border: targetAudience === 'struggling' ? '1.5px solid #3b82f6' : '1px solid #334155',
                      color: targetAudience === 'struggling' ? '#60a5fa' : '#cbd5e1'
                    }}
                  >
                    🔴+🟡 All Non-Mastered
                    <div style={{ fontSize: '10px', color: '#94a3b8', marginTop: '2px' }}>
                      {assignModalTopic.students.filter(s => s.status !== 'mastered').length} students
                    </div>
                  </button>

                  <button
                    type="button"
                    onClick={() => handleAudienceChange('all')}
                    style={{
                      padding: '8px 12px',
                      borderRadius: '8px',
                      fontSize: '12px',
                      fontWeight: 700,
                      cursor: 'pointer',
                      textAlign: 'left',
                      background: targetAudience === 'all' ? 'rgba(147, 51, 234, 0.2)' : '#0f172a',
                      border: targetAudience === 'all' ? '1.5px solid #9333ea' : '1px solid #334155',
                      color: targetAudience === 'all' ? '#c084fc' : '#cbd5e1'
                    }}
                  >
                    👥 Entire Batch
                    <div style={{ fontSize: '10px', color: '#94a3b8', marginTop: '2px' }}>
                      {assignModalTopic.students.length} students
                    </div>
                  </button>
                </div>
              </div>

              {/* Individual Student Checklist */}
              <div style={{ marginBottom: '18px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                  <span style={{ fontSize: '12px', fontWeight: 700, color: '#94a3b8' }}>
                    Selected Students ({selectedStudentCodes.length} of {assignModalTopic.students.length}):
                  </span>
                  <div style={{ display: 'flex', gap: '8px' }}>
                    <button
                      type="button"
                      onClick={() => setSelectedStudentCodes(assignModalTopic.students.map(s => s.studentCode))}
                      style={{ background: 'none', border: 'none', color: '#38bdf8', fontSize: '11px', cursor: 'pointer' }}
                    >
                      Select All
                    </button>
                    <button
                      type="button"
                      onClick={() => setSelectedStudentCodes([])}
                      style={{ background: 'none', border: 'none', color: '#94a3b8', fontSize: '11px', cursor: 'pointer' }}
                    >
                      Clear
                    </button>
                  </div>
                </div>

                <div style={{
                  maxHeight: '140px',
                  overflowY: 'auto',
                  background: '#0f172a',
                  borderRadius: '8px',
                  border: '1px solid #334155',
                  padding: '8px'
                }}>
                  {assignModalTopic.students.map(st => {
                    const isChecked = selectedStudentCodes.includes(st.studentCode);
                    return (
                      <label
                        key={st.studentCode}
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'space-between',
                          padding: '4px 8px',
                          borderRadius: '4px',
                          background: isChecked ? 'rgba(59, 130, 246, 0.1)' : 'transparent',
                          cursor: 'pointer',
                          fontSize: '12px'
                        }}
                      >
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <input
                            type="checkbox"
                            checked={isChecked}
                            onChange={() => handleToggleStudentSelection(st.studentCode)}
                          />
                          <span style={{ color: isChecked ? '#f8fafc' : '#94a3b8', fontWeight: isChecked ? 600 : 400 }}>
                            {st.name}
                          </span>
                        </div>
                        <span style={{
                          fontSize: '10px',
                          fontWeight: 700,
                          color: st.status === 'mastered' ? '#4ade80' : (st.status === 'practicing' ? '#facc15' : '#f87171')
                        }}>
                          {st.status === 'unattempted' ? '🔴 Unattempted' : `${st.status === 'mastered' ? '🟢' : (st.status === 'practicing' ? '🟡' : '🔴')} ${st.mastery}%`}
                        </span>
                      </label>
                    );
                  })}
                </div>
              </div>

              {/* Practice Sets Count */}
              <div style={{ marginBottom: '18px' }}>
                <label style={{ fontSize: '13px', fontWeight: 700, color: '#cbd5e1', display: 'block', marginBottom: '8px' }}>
                  Number of Practice Sets to Assign:
                </label>
                <div style={{ display: 'flex', gap: '8px' }}>
                  {[1, 2, 3, 4].map(n => (
                    <button
                      key={n}
                      type="button"
                      onClick={() => setSetsCount(n)}
                      style={{
                        flex: 1,
                        padding: '8px',
                        borderRadius: '8px',
                        fontSize: '12px',
                        fontWeight: 700,
                        cursor: 'pointer',
                        background: setsCount === n ? '#3b82f6' : '#0f172a',
                        color: setsCount === n ? '#ffffff' : '#94a3b8',
                        border: setsCount === n ? '1px solid #3b82f6' : '1px solid #334155'
                      }}
                    >
                      {n} Set{n > 1 ? 's' : ''} ({n * 6} Qs)
                      {n === 2 ? ' ⭐' : ''}
                    </button>
                  ))}
                </div>
                <div style={{ fontSize: '11px', color: '#64748b', marginTop: '4px' }}>
                  Teacher-directed assignments bypass the default 2-session self-serve lock.
                </div>
              </div>

              {/* Numerical Focus Option */}
              <div style={{
                marginBottom: '18px',
                padding: '12px 14px',
                background: assignModalTopic.hasNumericals ? 'rgba(56, 189, 248, 0.08)' : 'rgba(15, 23, 42, 0.5)',
                borderRadius: '8px',
                border: assignModalTopic.hasNumericals ? '1px solid rgba(56, 189, 248, 0.3)' : '1px solid #334155'
              }}>
                <label style={{ display: 'flex', alignItems: 'center', gap: '10px', cursor: assignModalTopic.hasNumericals ? 'pointer' : 'not-allowed' }}>
                  <input
                    type="checkbox"
                    checked={numericalFocus}
                    disabled={!assignModalTopic.hasNumericals}
                    onChange={(e) => setNumericalFocus(e.target.checked)}
                    style={{ width: '16px', height: '16px' }}
                  />
                  <div>
                    <div style={{ fontWeight: 700, fontSize: '13px', color: assignModalTopic.hasNumericals ? '#38bdf8' : '#64748b' }}>
                      🔢 Focus on Numerical Calculations (ONE type)
                    </div>
                    <div style={{ fontSize: '11px', color: '#94a3b8', marginTop: '2px' }}>
                      {assignModalTopic.hasNumericals
                        ? 'Serves authentic textbook calculation problems (Given ➔ Formula ➔ Substitution ➔ Answer).'
                        : 'Not available: This chapter/topic is qualitative and conceptual without numerical formulas.'}
                    </div>
                  </div>
                </label>
              </div>

              {/* Optional Teacher Note */}
              <div style={{ marginBottom: '14px' }}>
                <label style={{ fontSize: '12px', fontWeight: 700, color: '#94a3b8', display: 'block', marginBottom: '4px' }}>
                  Instructions / Note for Students (Optional):
                </label>
                <input
                  type="text"
                  placeholder="e.g. Please solve these numericals before the unit test."
                  value={teacherNote}
                  onChange={(e) => setTeacherNote(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '8px 12px',
                    borderRadius: '8px',
                    background: '#0f172a',
                    color: '#f8fafc',
                    border: '1px solid #334155',
                    fontSize: '13px'
                  }}
                />
              </div>

              {/* Success / Error Messages */}
              {assignSuccessMsg && (
                <div style={{ padding: '10px', background: 'rgba(34, 197, 94, 0.2)', border: '1px solid #22c55e', borderRadius: '6px', color: '#4ade80', fontSize: '12px', marginBottom: '12px' }}>
                  ✅ {assignSuccessMsg}
                </div>
              )}
              {assignErrorMsg && (
                <div style={{ padding: '10px', background: 'rgba(239, 68, 68, 0.2)', border: '1px solid #ef4444', borderRadius: '6px', color: '#f87171', fontSize: '12px', marginBottom: '12px' }}>
                  ⚠️ {assignErrorMsg}
                </div>
              )}
            </div>

            {/* Modal Footer */}
            <div style={{ padding: '14px 20px', borderTop: '1px solid #334155', display: 'flex', justifyContent: 'flex-end', gap: '10px', background: '#0f172a' }}>
              <button
                type="button"
                onClick={() => setAssignModalTopic(null)}
                style={{
                  background: 'none',
                  border: '1px solid #475569',
                  color: '#cbd5e1',
                  padding: '8px 16px',
                  borderRadius: '6px',
                  fontWeight: 600,
                  fontSize: '13px',
                  cursor: 'pointer'
                }}
              >
                Cancel
              </button>
              <button
                type="button"
                disabled={isAssigning || selectedStudentCodes.length === 0}
                onClick={handleDispatchPractice}
                style={{
                  background: selectedStudentCodes.length === 0 ? '#475569' : 'linear-gradient(135deg, #2563eb, #1d4ed8)',
                  color: '#ffffff',
                  border: 'none',
                  padding: '8px 20px',
                  borderRadius: '6px',
                  fontWeight: 700,
                  fontSize: '13px',
                  cursor: selectedStudentCodes.length === 0 ? 'not-allowed' : 'pointer',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '6px'
                }}
              >
                {isAssigning ? '⏳ Dispatching...' : `🚀 Assign Practice (${selectedStudentCodes.length} Students)`}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
