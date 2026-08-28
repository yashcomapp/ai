'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import dynamic from 'next/dynamic';
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });

interface Subject {
  id: string;
  board: string;
  class: string;
  subject: string;
  subjectCode: string;
  chapters?: any[];
}

interface Chapter {
  number: string;
  name: string;
  chapterCode?: string;
  topics?: Topic[];
  objectiveCount?: number;
  subjectiveCount?: number;
  testsCount?: number;
  tests?: any[];
  chapterExercises?: any[];
}

interface Topic {
  number: string;
  name: string;
  topicCode?: string;
  subtopics?: Subtopic[];
  objectiveCount?: number;
  subjectiveCount?: number;
  testsCount?: number;
  tests?: any[];
  textbookSets?: any[];
  targetQuestions?: number;
}

interface Subtopic {
  number: string;
  name: string;
  subtopicCode?: string;
  objectiveCount?: number;
  subjectiveCount?: number;
  testsCount?: number;
  tests?: any[];
  targetQuestions?: number;
}

const getObjectiveTestsCount = (tests: any[] | undefined) => {
  if (!Array.isArray(tests)) return 0;
  const seen = new Set();
  const objTests = tests.filter(t => {
    if (t.type === 'objective' && !seen.has(t.id)) {
      seen.add(t.id);
      return true;
    }
    return false;
  });
  return objTests.length;
};

const getSubjectiveTestsCount = (tests: any[] | undefined) => {
  if (!Array.isArray(tests)) return 0;
  const seen = new Set();
  const subjTests = tests.filter(t => {
    if (t.type === 'subjective' && !seen.has(t.id)) {
      seen.add(t.id);
      return true;
    }
    return false;
  });
  return subjTests.length;
};

export default function AdminSyllabusPage() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const renderTabsSkeleton = () => (
    <div className="tabs-container skeleton-blink" style={{ display: 'flex', gap: '8px', marginBottom: '20px', borderBottom: '1.5px solid var(--border-light)', paddingBottom: '8px', height: '45px' }}>
      {[1, 2, 3].map(i => (
        <div key={i} style={{ width: '100px', height: '30px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
      ))}
    </div>
  );

  const renderTableSkeleton = () => (
    <div className="card skeleton-blink" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
      <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', height: '56px', display: 'flex', alignItems: 'center' }}>
        <div style={{ width: '220px', height: '16px', background: 'var(--bg-soft)', borderRadius: '4px' }}></div>
      </div>
      <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {[1, 2, 3, 4, 5].map(i => (
          <div key={i} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', height: '36px', borderBottom: '1px solid var(--border-light)' }}>
            <div style={{ width: '150px', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
            <div style={{ width: '80px', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
            <div style={{ width: '60px', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
          </div>
        ))}
      </div>
    </div>
  );
  const [activeTab, setActiveTab] = useState<'subjects' | 'tree' | 'ai'>('subjects');

  // Master subjects list
  const [subjects, setSubjects] = useState<Subject[]>([]);

  // Sorting and PDF export states
  const [sortField, setSortField] = useState<'subject' | 'board' | 'class'>('subject');
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('asc');
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);

  // Selected subject for tree view
  const [selectedSubjectId, setSelectedSubjectId] = useState('');
  const [activeSubjectDoc, setActiveSubjectDoc] = useState<Subject | null>(null);

  // Drag and drop states for topic rearrangement
  const [draggedTopic, setDraggedTopic] = useState<{ chIdx: number; topIdx: number } | null>(null);
  const [dragOverTopic, setDragOverTopic] = useState<{ chIdx: number; topIdx: number } | null>(null);

  // Drag and drop states for subtopic rearrangement
  const [draggedSubtopic, setDraggedSubtopic] = useState<{ chIdx: number; topIdx: number; subIdx: number } | null>(null);
  const [dragOverSubtopic, setDragOverSubtopic] = useState<{ chIdx: number; topIdx: number; subIdx: number } | null>(null);

  // Collapse / expand states for chapters list
  const [expandedChapters, setExpandedChapters] = useState<Record<number, boolean>>({});

  // Subject Modal states
  const [subjectModal, setSubjectModal] = useState({
    show: false,
    mode: 'add' as 'add' | 'edit',
    docId: '',
    board: '',
    classNum: '',
    subjectName: '',
    subjectCode: ''
  });

  // Chapter Modal states
  const [chapterModal, setChapterModal] = useState({
    show: false,
    mode: 'add' as 'add' | 'edit',
    editIdx: null as number | null,
    number: '',
    name: '',
    code: '',
    chapterExercisesStr: ''
  });

  // Topic Modal states
  const [topicModal, setTopicModal] = useState({
    show: false,
    mode: 'add' as 'add' | 'edit',
    chIdx: 0,
    editIdx: null as number | null,
    number: '',
    name: '',
    code: '',
    textbookSetsStr: '',
    targetQuestions: 30 as number | string,
    hasSubtopics: false,
    subtopicsSum: 0
  });

  // Subtopic Modal states
  const [subtopicModal, setSubtopicModal] = useState({
    show: false,
    mode: 'add' as 'add' | 'edit',
    chIdx: 0,
    topIdx: 0,
    editIdx: null as number | null,
    number: '',
    name: '',
    code: '',
    targetQuestions: 30 as number | string
  });

  // AI syllabus generator state
  const [aiBoard, setAiBoard] = useState('CBSE');
  const [aiClass, setAiClass] = useState('10');
  const [aiSubject, setAiSubject] = useState('');
  const [aiSubjectCode, setAiSubjectCode] = useState('');
  const [aiPrompt, setAiPrompt] = useState('');
  const [aiResponse, setAiResponse] = useState('');
  const [aiPreviewData, setAiPreviewData] = useState<any>(null);

  // Tests Modal states
  const [testsModal, setTestsModal] = useState({
    show: false,
    title: '',
    tests: [] as any[]
  });

  const handleOpenTestsModal = (title: string, testsList: any[]) => {
    setTestsModal({
      show: true,
      title,
      tests: testsList
    });
  };

  // Rebuilder utilities loading overlays
  const [utilityLoading, setUtilityLoading] = useState(false);
  const [utilityMessage, setUtilityMessage] = useState('');
  const [saving, setSaving] = useState(false);

  const fetchSubjects = async () => {
    if (!firebaseUser) return;
    setLoading(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/syllabus', {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        throw new Error('Failed to fetch subjects list.');
      }
      const data = await res.json();
      
      // Sort subjects by Board, then Class (numeric), and then Subject name
      const sortedData = data.sort((a: any, b: any) => {
        const boardA = String(a.board || '').toLowerCase();
        const boardB = String(b.board || '').toLowerCase();
        if (boardA !== boardB) {
          return boardA.localeCompare(boardB);
        }

        const classA = parseInt(a.class, 10) || 0;
        const classB = parseInt(b.class, 10) || 0;
        if (classA !== classB) {
          return classA - classB;
        }

        const subjA = String(a.subject || '').toLowerCase();
        const subjB = String(b.subject || '').toLowerCase();
        return subjA.localeCompare(subjB);
      });

      setSubjects(sortedData);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error occurred fetching subjects.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (firebaseUser) {
      fetchSubjects();
    }
  }, [firebaseUser]);

  const handleSort = (field: 'subject' | 'board' | 'class') => {
    if (sortField === field) {
      setSortDir(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortField(field);
      setSortDir('asc');
    }
  };

  const sortedSubjects = [...subjects].sort((a, b) => {
    let comparison = 0;
    if (sortField === 'subject') {
      comparison = (a.subject || '').localeCompare(b.subject || '');
    } else if (sortField === 'board') {
      comparison = (a.board || '').localeCompare(b.board || '');
    } else {
      comparison = (parseInt(a.class) || 0) - (parseInt(b.class) || 0);
    }
    return sortDir === 'asc' ? comparison : -comparison;
  });

  // Load selected subject doc detail
  const handleSubjectTreeSelect = async (id: string) => {
    setSelectedSubjectId(id);
    if (!id) {
      setActiveSubjectDoc(null);
      return;
    }
    if (!firebaseUser) return;

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/syllabus?subjectId=${id}`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (res.ok) {
        const data = await res.json();
        setActiveSubjectDoc(data);
      }
    } catch (err) {
      console.error(err);
    }
  };

  // Re-fetch tree detail
  const refreshTreeDoc = async () => {
    if (selectedSubjectId) {
      await handleSubjectTreeSelect(selectedSubjectId);
    }
  };

  useEffect(() => {
    setExpandedChapters({});
  }, [activeSubjectDoc?.id]);

  const toggleChapterExpand = (chIdx: number) => {
    setExpandedChapters(prev => ({
      ...prev,
      [chIdx]: !prev[chIdx]
    }));
  };

  const handleDragStart = (chIdx: number, topIdx: number) => {
    setDraggedTopic({ chIdx, topIdx });
  };

  const handleDragEnd = () => {
    setDraggedTopic(null);
    setDragOverTopic(null);
  };

  const handleDragOver = (e: React.DragEvent, chIdx: number, topIdx: number) => {
    e.preventDefault();
    if (!draggedTopic) return;
    if (draggedTopic.chIdx === chIdx && draggedTopic.topIdx !== topIdx) {
      setDragOverTopic({ chIdx, topIdx });
    }
  };

  const handleDrop = async (e: React.DragEvent, targetChIdx: number, targetTopIdx: number) => {
    e.preventDefault();
    if (!draggedTopic || !activeSubjectDoc) return;
    const { chIdx: sourceChIdx, topIdx: sourceTopIdx } = draggedTopic;

    setDraggedTopic(null);
    setDragOverTopic(null);

    if (sourceChIdx !== targetChIdx || sourceTopIdx === targetTopIdx) return;

    const chapter = activeSubjectDoc.chapters?.[sourceChIdx];
    if (!chapter) return;

    const topicA = chapter.topics[sourceTopIdx];
    const topicB = chapter.topics[targetTopIdx];

    if (!confirm(`Are you sure you want to swap Topic ${topicA.number} ("${topicA.name}") with Topic ${topicB.number} ("${topicB.name}")?\n\nThis will also automatically swap all of their questions in the database!`)) {
      return;
    }

    setSaving(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/syllabus/swap-topics', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          subjectId: activeSubjectDoc.id,
          chapterNumber: chapter.number,
          sourceTopicIdx: sourceTopIdx,
          targetTopicIdx: targetTopIdx
        })
      });

      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.message || 'Failed to swap topics.');
      }

      const resData = await res.json();
      alert(`✅ Topics successfully swapped! ${resData.migratedCount} questions migrated.`);
      await refreshTreeDoc();
    } catch (err: any) {
      console.error(err);
      alert(err.message || 'Error swapping topics.');
    } finally {
      setSaving(false);
    }
  };

  // Subtopic Drag & Drop and Move Handlers
  const handleMoveSubtopic = async (chIdx: number, topIdx: number, subIdx: number, direction: 'up' | 'down') => {
    if (!activeSubjectDoc) return;
    const chapters = [...activeSubjectDoc.chapters!];
    const topic = chapters[chIdx]?.topics?.[topIdx];
    if (!topic || !Array.isArray(topic.subtopics)) return;

    const targetIdx = direction === 'up' ? subIdx - 1 : subIdx + 1;
    if (targetIdx < 0 || targetIdx >= topic.subtopics.length) return;

    const subtopics = [...topic.subtopics];
    const temp = subtopics[subIdx];
    subtopics[subIdx] = subtopics[targetIdx];
    subtopics[targetIdx] = temp;

    topic.subtopics = subtopics;
    await saveChaptersArray(chapters);
  };

  const handleSubtopicDragStart = (chIdx: number, topIdx: number, subIdx: number) => {
    setDraggedSubtopic({ chIdx, topIdx, subIdx });
  };

  const handleSubtopicDragEnd = () => {
    setDraggedSubtopic(null);
    setDragOverSubtopic(null);
  };

  const handleSubtopicDragOver = (e: React.DragEvent, chIdx: number, topIdx: number, subIdx: number) => {
    e.preventDefault();
    e.stopPropagation();
    if (!draggedSubtopic) return;
    if (draggedSubtopic.chIdx === chIdx && draggedSubtopic.topIdx === topIdx && draggedSubtopic.subIdx !== subIdx) {
      setDragOverSubtopic({ chIdx, topIdx, subIdx });
    }
  };

  const handleSubtopicDrop = async (e: React.DragEvent, targetChIdx: number, targetTopIdx: number, targetSubIdx: number) => {
    e.preventDefault();
    e.stopPropagation();
    if (!draggedSubtopic || !activeSubjectDoc) return;
    const { chIdx: sourceChIdx, topIdx: sourceTopIdx, subIdx: sourceSubIdx } = draggedSubtopic;

    setDraggedSubtopic(null);
    setDragOverSubtopic(null);

    if (sourceChIdx !== targetChIdx || sourceTopIdx !== targetTopIdx || sourceSubIdx === targetSubIdx) return;

    const chapters = [...activeSubjectDoc.chapters!];
    const topic = chapters[targetChIdx]?.topics?.[targetTopIdx];
    if (!topic || !Array.isArray(topic.subtopics)) return;

    const subtopics = [...topic.subtopics];
    const [movedItem] = subtopics.splice(sourceSubIdx, 1);
    subtopics.splice(targetSubIdx, 0, movedItem);

    topic.subtopics = subtopics;
    await saveChaptersArray(chapters);
  };

  // Auto subject preview codes derivation
  const getSubjectCodePreview = (board: string, subject: string) => {
    if (!board || !subject) return '';
    const bPart = board.trim().substring(0, 4).toUpperCase();
    const sPart = subject.trim().substring(0, 4).toUpperCase();
    return `${bPart}_${sPart}`;
  };

  // Add/Edit Subject Modal saves
  const handleOpenAddSubject = () => {
    setSubjectModal({
      show: true,
      mode: 'add',
      docId: '',
      board: 'CBSE',
      classNum: '10',
      subjectName: '',
      subjectCode: ''
    });
  };

  const handleOpenEditSubject = (sub: Subject) => {
    setSubjectModal({
      show: true,
      mode: 'edit',
      docId: sub.id,
      board: sub.board,
      classNum: sub.class,
      subjectName: sub.subject,
      subjectCode: sub.subjectCode
    });
  };

  const handleSaveSubject = async () => {
    if (saving) return;
    if (!subjectModal.board || !subjectModal.classNum || !subjectModal.subjectName || !subjectModal.subjectCode) {
      alert('Please fill out all fields.');
      return;
    }

    setSaving(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/syllabus', {
        method: subjectModal.mode === 'add' ? 'POST' : 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          docId: subjectModal.docId,
          board: subjectModal.board,
          classNum: subjectModal.classNum,
          subjectName: subjectModal.subjectName,
          subjectCode: subjectModal.subjectCode
        })
      });

      if (!res.ok) {
        throw new Error('Failed to save subject.');
      }

      alert('✅ Subject saved successfully!');
      setSubjectModal(prev => ({ ...prev, show: false }));
      await fetchSubjects();
      // Rebuild index in backend automatically
      await fetch('/api/admin/syllabus/rebuild', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ action: 'rebuild' })
      });
    } catch (err: any) {
      alert(err.message || 'Error occurred saving subject.');
    } finally {
      setSaving(false);
    }
  };

  // Delete Subject Action
  const handleDeleteSubject = async (id: string, name: string) => {
    if (!confirm(`Are you sure you want to delete subject: "${name}"?\n\nThis will permanently remove the subject and all unused questions under it.`)) {
      return;
    }
    if (!firebaseUser) return;

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/syllabus?subjectId=${id}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });

      if (!res.ok) {
        throw new Error('Failed to delete subject.');
      }
      const data = await res.json();
      alert(`✅ Subject deleted! Removed ${data.questionsDeleted} unused questions. (${data.questionsSkippedUsed} used questions were skipped for safety).`);
      await fetchSubjects();
      if (selectedSubjectId === id) {
        setSelectedSubjectId('');
        setActiveSubjectDoc(null);
      }
    } catch (err: any) {
      alert(err.message || 'Error deleting subject.');
    }
  };

  // Subject Tree array mutation saves
  const saveChaptersArray = async (chapters: any[]) => {
    if (!activeSubjectDoc) return;
    if (saving) return;
    setSaving(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/syllabus', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          id: activeSubjectDoc.id,
          chapters
        })
      });
      if (!res.ok) {
        throw new Error('Failed to save syllabus hierarchy.');
      }
      
      const updated = { ...activeSubjectDoc, chapters };
      setActiveSubjectDoc(updated);
      setSubjects(prev => prev.map(s => s.id === updated.id ? updated : s));

      // Rebuild index
      await fetch('/api/admin/syllabus/rebuild', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ action: 'rebuild' })
      });
    } catch (err: any) {
      alert(err.message || 'Error occurred saving tree changes.');
    } finally {
      setSaving(false);
    }
  };

  // Chapter CRUD
  const handleOpenAddChapter = () => {
    if (!activeSubjectDoc) return;
    setChapterModal({
      show: true,
      mode: 'add',
      editIdx: null,
      number: '',
      name: '',
      code: '',
      chapterExercisesStr: ''
    });
  };

  const handleOpenEditChapter = (idx: number, ch: any) => {
    const exercisesList = ch.chapterExercises || [];
    const exercisesStr = Array.isArray(exercisesList)
      ? exercisesList.map((e: any) => `${e.name}: ${e.questionCount || 8}`).join(', ')
      : '';
    setChapterModal({
      show: true,
      mode: 'edit',
      editIdx: idx,
      number: ch.number,
      name: ch.name,
      code: ch.chapterCode || '',
      chapterExercisesStr: exercisesStr
    });
  };

  const handleSaveChapter = async () => {
    if (!activeSubjectDoc) return;
    const { mode, editIdx, number, name, chapterExercisesStr } = chapterModal;

    if (!number || !name) {
      alert('Please fill out all chapter fields.');
      return;
    }

    const bPart = activeSubjectDoc.board.substring(0, 4).toUpperCase();
    const sPart = activeSubjectDoc.subjectCode || 'GEN';
    const code = `${bPart}-${activeSubjectDoc.class}-${sPart}-${number}`;

    const parsedExercises = (chapterExercisesStr || '').split(',').map(s => {
      const parts = s.split(':');
      if (parts.length >= 2) {
        const nameVal = parts[0].trim();
        const count = parseInt(parts[1].trim(), 10) || 8;
        return { name: nameVal, type: 'problem_set', questionCount: count };
      }
      return null;
    }).filter(Boolean);

    const chapters = Array.isArray(activeSubjectDoc.chapters) ? [...activeSubjectDoc.chapters] : [];
    if (mode === 'add') {
      chapters.push({
        number,
        name,
        chapterCode: code,
        topics: [],
        chapterExercises: parsedExercises
      });
    } else if (editIdx !== null) {
      chapters[editIdx] = {
        ...chapters[editIdx],
        number,
        name,
        chapterCode: code,
        chapterExercises: parsedExercises
      };
    }

    setChapterModal(prev => ({ ...prev, show: false }));
    await saveChaptersArray(chapters);
  };

  const handleDeleteChapter = async (idx: number) => {
    if (!activeSubjectDoc) return;
    if (!confirm('Are you sure you want to delete this chapter and all its topics?')) return;
    const chapters = activeSubjectDoc.chapters!.filter((_, i) => i !== idx);
    await saveChaptersArray(chapters);
  };

  // Topic CRUD
  const handleOpenAddTopic = (chIdx: number) => {
    setTopicModal({
      show: true,
      mode: 'add',
      chIdx,
      editIdx: null,
      number: '',
      name: '',
      code: '',
      textbookSetsStr: '',
      targetQuestions: 30,
      hasSubtopics: false,
      subtopicsSum: 0
    });
  };

  const handleOpenEditTopic = (chIdx: number, topIdx: number, topic: any) => {
    const setsList = topic.textbookSets || [];
    const setsStr = Array.isArray(setsList)
      ? setsList.map((s: any) => `${s.name}: ${s.questionCount || 8}`).join(', ')
      : '';
    const subs = Array.isArray(topic.subtopics) ? topic.subtopics : [];
    const hasSubtopics = subs.length > 0;
    const subtopicsSum = subs.reduce((sum: number, s: any) => sum + (Number(typeof s === 'object' ? s.targetQuestions : 0) || 30), 0);
    setTopicModal({
      show: true,
      mode: 'edit',
      chIdx,
      editIdx: topIdx,
      number: topic.number,
      name: topic.name,
      code: topic.topicCode || '',
      textbookSetsStr: setsStr,
      targetQuestions: hasSubtopics ? subtopicsSum : (topic.targetQuestions !== undefined ? Number(topic.targetQuestions) : 30),
      hasSubtopics,
      subtopicsSum
    });
  };

  const handleSaveTopic = async () => {
    if (!activeSubjectDoc) return;
    const { mode, chIdx, editIdx, number, name, textbookSetsStr, targetQuestions, hasSubtopics, subtopicsSum } = topicModal;

    if (!number || !name) {
      alert('Please fill out all topic fields.');
      return;
    }

    const chapters = [...activeSubjectDoc.chapters!];
    const chapter = chapters[chIdx];
    if (!chapter) return;

    const bPart = activeSubjectDoc.board.substring(0, 4).toUpperCase();
    const sPart = activeSubjectDoc.subjectCode || 'GEN';
    const code = `${bPart}-${activeSubjectDoc.class}-${sPart}-${chapter.number}-${number}`;

    const parsedSets = (textbookSetsStr || '').split(',').map(s => {
      const parts = s.split(':');
      if (parts.length >= 2) {
        const nameVal = parts[0].trim();
        const count = parseInt(parts[1].trim(), 10) || 8;
        const type = nameVal.toLowerCase().includes('solved') ? 'solved_examples' : 'practice_set';
        return { name: nameVal, type, questionCount: count };
      }
      return null;
    }).filter(Boolean);

    const topics = Array.isArray(chapter.topics) ? [...chapter.topics] : [];
    const finalTarget = hasSubtopics ? subtopicsSum : (Number(targetQuestions) || 30);

    if (mode === 'add') {
      topics.push({
        number,
        name,
        topicCode: code,
        subtopics: [],
        textbookSets: parsedSets,
        targetQuestions: finalTarget
      });
    } else if (editIdx !== null) {
      topics[editIdx] = {
        ...topics[editIdx],
        number,
        name,
        topicCode: code,
        textbookSets: parsedSets,
        targetQuestions: finalTarget
      };
    }

    chapter.topics = topics;
    setTopicModal(prev => ({ ...prev, show: false }));
    await saveChaptersArray(chapters);
  };

  const handleDeleteTopic = async (chIdx: number, topIdx: number) => {
    if (!activeSubjectDoc) return;
    if (!confirm('Are you sure you want to delete this topic?')) return;
    const chapters = [...activeSubjectDoc.chapters!];
    chapters[chIdx].topics = chapters[chIdx].topics.filter((_: any, i: number) => i !== topIdx);
    await saveChaptersArray(chapters);
  };

  // Subtopic CRUD
  const handleOpenAddSubtopic = (chIdx: number, topIdx: number) => {
    const parentTopic = activeSubjectDoc?.chapters?.[chIdx]?.topics?.[topIdx];
    const nextSubNum = parentTopic ? `${parentTopic.number}.${(parentTopic.subtopics?.length || 0) + 1}` : '';
    setSubtopicModal({
      show: true,
      mode: 'add',
      chIdx,
      topIdx,
      editIdx: null,
      number: nextSubNum,
      name: '',
      code: '',
      targetQuestions: 30
    });
  };

  const handleOpenEditSubtopic = (chIdx: number, topIdx: number, subIdx: number, sub: any) => {
    const parentTopic = activeSubjectDoc?.chapters?.[chIdx]?.topics?.[topIdx];
    const subName = typeof sub === 'string' 
      ? sub 
      : (sub?.name || sub?.subtopic || sub?.title || sub?.text || '');
    const subNumber = (typeof sub === 'object' && sub && sub.number) 
      ? String(sub.number) 
      : (parentTopic ? `${parentTopic.number}.${subIdx + 1}` : `${subIdx + 1}`);
    const targetQ = (typeof sub === 'object' && sub && sub.targetQuestions !== undefined) 
      ? Number(sub.targetQuestions) 
      : 30;

    setSubtopicModal({
      show: true,
      mode: 'edit',
      chIdx,
      topIdx,
      editIdx: subIdx,
      number: subNumber,
      name: subName,
      code: (typeof sub === 'object' && (sub.subtopicCode || sub.code)) || '',
      targetQuestions: targetQ
    });
  };

  const handleSaveSubtopic = async () => {
    if (!activeSubjectDoc) return;
    const { mode, chIdx, topIdx, editIdx, number, name, targetQuestions } = subtopicModal;

    if (!number || !name) {
      alert('Please fill out all subtopic fields.');
      return;
    }

    const chapters = [...activeSubjectDoc.chapters!];
    const chapter = chapters[chIdx];
    const topic = chapter?.topics?.[topIdx];
    if (!topic) return;

    const bPart = activeSubjectDoc.board.substring(0, 4).toUpperCase();
    const sPart = activeSubjectDoc.subjectCode || 'GEN';
    const code = `${bPart}-${activeSubjectDoc.class}-${sPart}-${chapter.number}-${number}`;
    const quotaVal = Number(targetQuestions) || 30;

    const subtopics = Array.isArray(topic.subtopics) ? [...topic.subtopics] : [];
    if (mode === 'add') {
      subtopics.push({
        number,
        name,
        subtopicCode: code,
        targetQuestions: quotaVal
      });
    } else if (editIdx !== null) {
      const existingSub = typeof subtopics[editIdx] === 'object' ? subtopics[editIdx] : {};
      subtopics[editIdx] = {
        ...existingSub,
        number,
        name,
        subtopicCode: code,
        targetQuestions: quotaVal
      };
    }

    topic.subtopics = subtopics;
    // Auto-update parent topic target questions to equal the sum of its subtopics
    topic.targetQuestions = subtopics.reduce((acc: number, s: any) => acc + (Number(s.targetQuestions) || 30), 0);

    setSubtopicModal(prev => ({ ...prev, show: false }));
    await saveChaptersArray(chapters);
  };

  const handleDeleteSubtopic = async (chIdx: number, topIdx: number, subIdx: number) => {
    if (!activeSubjectDoc) return;
    if (!confirm('Are you sure you want to delete this subtopic?')) return;
    const chapters = [...activeSubjectDoc.chapters!];
    chapters[chIdx].topics[topIdx].subtopics = chapters[chIdx].topics[topIdx].subtopics.filter((_: any, i: number) => i !== subIdx);
    await saveChaptersArray(chapters);
  };

  // Rebuild Index manually
  const triggerManualReindex = async () => {
    if (!confirm('Rebuild the entire fast topic lookup index? This might take a few moments.')) return;
    setUtilityLoading(true);
    setUtilityMessage('Scanning subjects and reindexing...');

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/syllabus/rebuild', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ action: 'rebuild' })
      });

      if (!res.ok) throw new Error('Rebuild failed.');
      const data = await res.json();
      alert(`✅ Reindex complete! Indexed ${data.summary.topicsIndexed} topics across ${data.summary.subjectsProcessed} subjects. Removed ${data.summary.staleRemoved} stale entries.`);
    } catch (err: any) {
      alert(err.message || 'Error occurred.');
    } finally {
      setUtilityLoading(false);
    }
  };

  // Deduplicate entries manually
  const triggerDeduplicationSweep = async () => {
    if (!confirm('🧹 Remove duplicate chapters/topics across all subjects? This sweeps and cleans the database.')) return;
    setUtilityLoading(true);
    setUtilityMessage('Sweeping duplicates and updating syllabus index...');

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/syllabus/rebuild', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ action: 'dedupe' })
      });

      if (!res.ok) throw new Error('Deduplication failed.');
      const data = await res.json();
      alert(`✅ Sweep Complete!\n\nChapters Removed: ${data.chaptersRemoved}\nTopics Removed: ${data.topicsRemoved}\nSubtopics Removed: ${data.subtopicsRemoved}\nSubjects Modified: ${data.subjectsChanged}`);
      await fetchSubjects();
      await refreshTreeDoc();
    } catch (err: any) {
      alert(err.message || 'Error occurred.');
    } finally {
      setUtilityLoading(false);
    }
  };

  const handleResetTopicTests = async (topicCode?: string) => {
    if (!firebaseUser) return;
    const isGlobal = !topicCode;
    const confirmMsg = isGlobal 
      ? `⚠️ WARNING!\n\nAre you sure you want to perform a Global Academic Reset for the entire subject?\n\nThis will permanently delete all student attempts, scores, and reviews for ALL exams linked to this subject. This action is irreversible and should only be done for the new academic year!`
      : `⚠️ WARNING!\n\nAre you sure you want to reset all test attempts/submissions for topic code "${topicCode}"?\n\nThis will permanently delete all student submissions, test scores, and reviews for any tests linked to this topic. This action is irreversible!`;

    if (!confirm(confirmMsg)) {
      return;
    }

    setUtilityLoading(true);
    setUtilityMessage(isGlobal ? 'Performing global academic reset...' : 'Resetting test attempts for this topic...');
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/reports/test-coverage/reset', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          subjectId: selectedSubjectId,
          topicCode: topicCode || null
        })
      });

      if (!res.ok) {
        throw new Error('Failed to reset attempts.');
      }
      
      alert(isGlobal ? '✅ Global Academic Reset completed successfully!' : '✅ Test attempts successfully reset for this topic!');
      await refreshTreeDoc();
    } catch (err: any) {
      alert(err.message || 'Error occurred during reset.');
    } finally {
      setUtilityLoading(false);
    }
  };

  // AI Prompt generator
  const handleGenerateAIPrompt = () => {
    if (!aiBoard || !aiClass || !aiSubject) {
      alert('Please enter Board, Class, and Subject name.');
      return;
    }

    const p = `Act as an expert curriculum designer and senior board paper setter. 
Your task is to generate a highly detailed, 100% correct syllabus structure for Board: ${aiBoard}, Class: ${aiClass}, Subject: ${aiSubject} (using Subject Code: ${aiSubjectCode || 'GEN'}).

IMPORTANT RESEARCH REQUIREMENT:
You MUST search/research the official prescribed textbook (e.g., NCERT or State Board books) for this class and subject to fetch the actual, real chapter names, topic-level subtopics, practice sets/exercises, problem sets, and solved examples, along with their exact question counts.

CRITICAL THEOREM INCLUSION REQUIREMENT:
If the subject is Mathematics, Geometry, or contains proofs, you MUST include EACH and EVERY theorem mentioned in the textbook as a separate, distinct topic or subtopic. Do not skip or group them under a single general header. Every theorem (e.g., Basic Proportionality Theorem, Angle Bisector Theorem, Property of Three Parallel Lines, Geometric Mean Theorem, Pythagoras Theorem, Converse of Pythagoras Theorem, Apollonius Theorem, Tangent Theorem, Tangent Segment Theorem, Theorem of Touching Circles, Inscribed Angle Theorem, Cyclic Quadrilateral Theorem, Tangent Secant Segment Theorem, etc.) MUST be listed individually with its exact name, proof, and application mapping.

Return ONLY a valid JSON object matching the schema below:
{
  "board": "${aiBoard}",
  "class": "${aiClass}",
  "subject": "${aiSubject}",
  "subjectCode": "${aiSubjectCode || 'GEN'}",
  "chapters": [
    {
      "number": "1",
      "name": "Chapter Name",
      "chapterCode": "${aiBoard}-${aiClass}-${aiSubjectCode || 'GEN'}-1",
      "chapterExercises": [
        {
          "name": "Problem Set 1",
          "type": "problem_set",
          "questionCount": 9
        }
      ],
      "topics": [
        {
          "number": "1.1",
          "name": "Topic Name",
          "topicCode": "${aiBoard}-${aiClass}-${aiSubjectCode || 'GEN'}-1-1.1",
          "textbookSets": [
            {
              "name": "Practice Set 1.1",
              "type": "practice_set",
              "questionCount": 5
            },
            {
              "name": "Chapter 1 Solved Examples (Topic 1.1)",
              "type": "solved_examples",
              "questionCount": 3
            }
          ],
          "subtopics": [
            {
              "number": "1.1.1",
              "name": "Subtopic Name",
              "subtopicCode": "${aiBoard}-${aiClass}-${aiSubjectCode || 'GEN'}-1-1.1.1"
            }
          ]
        }
      ]
    }
  ]
}`;
    setAiPrompt(p);
  };

  const handleCopyPrompt = () => {
    navigator.clipboard.writeText(aiPrompt);
    alert('📋 Prompt copied to clipboard!');
  };

  const handleParseAndPreview = () => {
    try {
      const parsed = JSON.parse(aiResponse);
      if (!parsed.board || !parsed.class || !parsed.subject) {
        throw new Error('JSON is missing mandatory board, class, or subject fields.');
      }
      setAiPreviewData(parsed);
      alert('✅ Parsing complete! Preview generated below.');
    } catch (err: any) {
      alert('❌ Parsing Error: ' + err.message);
    }
  };

  const handleSaveAISyllabus = async () => {
    if (!aiPreviewData || !firebaseUser) return;
    if (saving) return;

    setSaving(true);
    try {
      const docId = `${aiPreviewData.board.toLowerCase()}_${aiPreviewData.class}_${aiPreviewData.subject.toLowerCase().replace(/\s+/g, '_')}`;
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/syllabus', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          docId,
          board: aiPreviewData.board,
          classNum: aiPreviewData.class,
          subjectName: aiPreviewData.subject,
          chapters: aiPreviewData.chapters
        })
      });

      if (!res.ok) {
        throw new Error('Failed to save AI-generated syllabus.');
      }

      alert('✅ AI Syllabus saved to database successfully!');
      setAiPreviewData(null);
      setAiResponse('');
      setAiPrompt('');
      await fetchSubjects();
      // Rebuild index
      await fetch('/api/admin/syllabus/rebuild', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ action: 'rebuild' })
      });
    } catch (err: any) {
      alert(err.message || 'Error occurred saving syllabus.');
    } finally {
      setSaving(false);
    }
  };

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <style>{`
        @keyframes skeleton-blink {
          0% { opacity: 0.6; }
          50% { opacity: 1; }
          100% { opacity: 0.6; }
        }
        .skeleton-blink {
          animation: skeleton-blink 1.5s infinite ease-in-out;
        }
      `}</style>
      {/* Page Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800, cursor: 'pointer' }} onClick={() => router.push('/admin')}>YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Syllabus Manager</h1>
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Configure chapters, topics, and subtopics</div>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '8px' }}>
          
          <button className="btn btn-primary" style={{ padding: '6px 12px', fontSize: '12px' }} onClick={() => setPdfSelectorOpen(true)}>📄 Export PDF</button>
          <button className="btn btn-secondary" onClick={triggerDeduplicationSweep}>🧹 Deduplicate</button>
          <button className="btn btn-secondary" onClick={triggerManualReindex}>🔄 Rebuild Index</button>
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      {/* Tabs list */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1000px', width: '100%', margin: '0 auto' }}>
        {loading ? (
          <>
            {renderTabsSkeleton()}
            {renderTableSkeleton()}
          </>
        ) : (
          <>
            <div className="tabs-container" style={{ display: 'flex', gap: '8px', marginBottom: '20px', borderBottom: '1.5px solid var(--border-light)', paddingBottom: '8px' }}>
          <button 
            className={`tab-btn ${activeTab === 'subjects' ? 'active' : ''}`}
            onClick={() => setActiveTab('subjects')}
            style={{ padding: '8px 16px', border: 'none', cursor: 'pointer', background: 'none', fontWeight: 600, borderBottom: activeTab === 'subjects' ? '2.5px solid var(--accent)' : 'none', color: activeTab === 'subjects' ? 'var(--accent)' : 'var(--text-muted)' }}
          >
            📚 Subjects
          </button>
          <button 
            className={`tab-btn ${activeTab === 'tree' ? 'active' : ''}`}
            onClick={() => setActiveTab('tree')}
            style={{ padding: '8px 16px', border: 'none', cursor: 'pointer', background: 'none', fontWeight: 600, borderBottom: activeTab === 'tree' ? '2.5px solid var(--accent)' : 'none', color: activeTab === 'tree' ? 'var(--accent)' : 'var(--text-muted)' }}
          >
            📖 Chapters & Tree Topics
          </button>
          <button 
            className={`tab-btn ${activeTab === 'ai' ? 'active' : ''}`}
            onClick={() => setActiveTab('ai')}
            style={{ padding: '8px 16px', border: 'none', cursor: 'pointer', background: 'none', fontWeight: 600, borderBottom: activeTab === 'ai' ? '2.5px solid var(--accent)' : 'none', color: activeTab === 'ai' ? 'var(--accent)' : 'var(--text-muted)' }}
          >
            🤖 AI Syllabus Generator
          </button>
        </div>

        {/* Tab 1: Subjects List */}
        {activeTab === 'subjects' && (
          <div id="syllabus-subjects-section" className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span style={{ fontWeight: 700 }}>📋 Registered Syllabus Subjects</span>
              <button className="btn btn-primary" onClick={handleOpenAddSubject}>+ New Subject</button>
            </div>
            <div style={{ overflowX: 'auto' }}>
              <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
                <thead>
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                    <th onClick={() => handleSort('subject')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                      Subject Name {sortField === 'subject' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th onClick={() => handleSort('board')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                      Board {sortField === 'board' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th onClick={() => handleSort('class')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                      Class {sortField === 'class' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th style={{ padding: '12px 16px' }}>Subject Code</th>
                    <th style={{ padding: '12px 16px' }}>Chapters</th>
                    <th style={{ padding: '12px 16px', textAlign: 'right' }}>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {sortedSubjects.length === 0 ? (
                    <tr>
                      <td colSpan={6} style={{ padding: '30px', textAlign: 'center', color: 'var(--text-muted)' }}>No syllabus subjects registered yet.</td>
                    </tr>
                  ) : (
                    sortedSubjects.map(s => (
                      <tr key={s.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                        <td style={{ padding: '12px 16px', fontWeight: 600 }}>{s.subject}</td>
                        <td style={{ padding: '12px 16px' }}>{s.board}</td>
                        <td style={{ padding: '12px 16px' }}>Class {s.class}</td>
                        <td style={{ padding: '12px 16px' }}>{s.subjectCode}</td>
                        <td style={{ padding: '12px 16px' }}>{s.chapters?.length || 0} chapters</td>
                        <td style={{ padding: '12px 16px', textAlign: 'right' }}>
                          <div style={{ display: 'flex', gap: '8px', justifyContent: 'flex-end' }}>
                            <button className="btn btn-secondary" style={{ padding: '3px 10px', fontSize: '11px' }} onClick={() => handleOpenEditSubject(s)}>
                              ✏️ Edit
                            </button>
                            <button className="btn btn-secondary" style={{ padding: '3px 10px', fontSize: '11px', color: 'var(--danger)' }} onClick={() => handleDeleteSubject(s.id, s.subject)}>
                              🗑️ Delete
                            </button>
                          </div>
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* Tab 2: Tree View list */}
        {activeTab === 'tree' && (
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '15px', flexWrap: 'wrap' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <span style={{ fontWeight: 700, fontSize: '13px' }}>Syllabus:</span>
                <select 
                  value={selectedSubjectId} 
                  onChange={(e) => handleSubjectTreeSelect(e.target.value)}
                  style={{ padding: '6px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                >
                  <option value="">-- Choose Subject --</option>
                  {subjects.map(s => (
                    <option key={s.id} value={s.id}>{s.board} | Class {s.class} | {s.subject}</option>
                  ))}
                </select>
              </div>

              {activeSubjectDoc && (
                <div style={{ display: 'flex', gap: '8px' }}>
                  <button className="btn btn-secondary" style={{ fontSize: '11px', color: 'var(--danger)', borderColor: 'var(--danger)' }} onClick={() => handleResetTopicTests()}>
                    🎓 Academic Reset
                  </button>
                  <button className="btn btn-primary" style={{ fontSize: '11px' }} onClick={handleOpenAddChapter}>
                    + Add Chapter
                  </button>
                </div>
              )}
            </div>

            <div style={{ padding: '20px' }}>
              {!activeSubjectDoc ? (
                <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>
                  Please select a syllabus subject above to display and edit its chapter node tree.
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  {(!activeSubjectDoc.chapters || activeSubjectDoc.chapters.length === 0) ? (
                    <div style={{ textAlign: 'center', color: 'var(--text-muted)', padding: '20px', fontSize: '12px' }}>
                      No chapters added yet. Click "+ Add Chapter" to start building your hierarchy.
                    </div>
                  ) : (
                    activeSubjectDoc.chapters.map((ch, chIdx) => {
                      const isExpanded = !!expandedChapters[chIdx];
                      return (
                        <div key={`ch_${chIdx}`} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--bg-soft)', overflow: 'hidden', marginBottom: '8px' }}>
                          
                          {/* Chapter Node header */}
                          <div style={{ padding: '10px 15px', background: 'var(--surface)', borderBottom: isExpanded ? '1px solid var(--border-light)' : 'none', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                            <div 
                              style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer', flex: 1 }}
                              onClick={() => toggleChapterExpand(chIdx)}
                            >
                              <span style={{ fontSize: '12px', color: 'var(--accent)', marginRight: '4px', userSelect: 'none' }}>
                                {isExpanded ? '▼' : '▶'}
                              </span>
                              <div>
                                <span style={{ fontWeight: 800, fontSize: '13px', color: 'var(--accent)' }}>📗 Chapter {ch.number}:</span>{' '}
                                <span style={{ fontWeight: 600, fontSize: '13px' }}>{ch.name}</span>
                                <span style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginLeft: '10px' }}>
                                  [
                                  <span
                                    onClick={(e) => {
                                      e.stopPropagation();
                                      if (activeSubjectDoc) {
                                        router.push(`/admin/question-bank?board=${encodeURIComponent(activeSubjectDoc.board)}&class=${encodeURIComponent(activeSubjectDoc.class)}&subject=${encodeURIComponent(activeSubjectDoc.subject)}&chapter=${encodeURIComponent(ch.number)}`);
                                      }
                                    }}
                                    title="Click to view questions in Question Bank"
                                    style={{ cursor: 'pointer', textDecoration: 'underline', color: '#2980b9' }}
                                  >
                                    O - {ch.objectiveCount || 0}
                                  </span>
                                  {' | '}
                                  S - {ch.subjectiveCount || 0} |{' '}
                                  <span 
                                    onClick={(e) => { 
                                      e.stopPropagation(); 
                                      if (ch.tests && ch.tests.length > 0) {
                                        handleOpenTestsModal(ch.name || 'Chapter', ch.tests);
                                      }
                                    }}
                                    style={{ 
                                      cursor: (ch.tests && ch.tests.length > 0) ? 'pointer' : 'default',
                                      textDecoration: (ch.tests && ch.tests.length > 0) ? 'underline' : 'none',
                                      color: '#2980b9'
                                    }}
                                  >
                                    O.Tests - {getObjectiveTestsCount(ch.tests)}
                                  </span>
                                  {' | '}
                                  <span 
                                    onClick={(e) => { 
                                      e.stopPropagation(); 
                                      if (ch.tests && ch.tests.length > 0) {
                                        handleOpenTestsModal(ch.name || 'Chapter', ch.tests);
                                      }
                                    }}
                                    style={{ 
                                      cursor: (ch.tests && ch.tests.length > 0) ? 'pointer' : 'default',
                                      textDecoration: (ch.tests && ch.tests.length > 0) ? 'underline' : 'none',
                                      color: '#8e44ad'
                                    }}
                                  >
                                    S.Tests - {getSubjectiveTestsCount(ch.tests)}
                                  </span>
                                  ]
                                </span>
                                <small style={{ display: 'block', fontSize: '9px', color: 'var(--text-muted)' }}>{ch.chapterCode}</small>
                                {Array.isArray(ch.chapterExercises) && ch.chapterExercises.map((ex: any, exIdx: number) => (
                                  <span key={exIdx} style={{ display: 'inline-block', fontSize: '9px', fontWeight: 650, background: 'rgba(230, 126, 34, 0.1)', color: '#d35400', padding: '1px 6px', borderRadius: '4px', marginTop: '4px', marginRight: '6px', border: '1px solid rgba(230, 126, 34, 0.2)' }}>
                                    📖 {ex.name} ({ex.questionCount || 8} Qs)
                                  </span>
                                ))}
                              </div>
                            </div>
                            <div style={{ display: 'flex', gap: '5px' }}>
                              <button className="btn btn-secondary" style={{ padding: '2px 6px', fontSize: '10px' }} onClick={() => handleOpenEditChapter(chIdx, ch)}>✏️</button>
                              <button className="btn btn-secondary" style={{ padding: '2px 6px', fontSize: '10px', color: 'var(--danger)' }} onClick={() => handleDeleteChapter(chIdx)}>🗑️</button>
                              <button className="btn btn-primary" style={{ padding: '2px 8px', fontSize: '10px' }} onClick={() => handleOpenAddTopic(chIdx)}>+ Topic</button>
                            </div>
                          </div>

                          {/* Topics Node (collapsible) */}
                          {isExpanded && (
                            <div style={{ padding: '10px 15px 10px 30px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
                              {(!ch.topics || ch.topics.length === 0) ? (
                                <div style={{ fontSize: '11px', color: 'var(--text-muted)', fontStyle: 'italic' }}>No topics added.</div>
                              ) : (
                                ch.topics.map((topic: Topic, topIdx: number) => (
                                  <div
                                    key={`t_${topIdx}`}
                                    draggable={true}
                                    onDragStart={() => handleDragStart(chIdx, topIdx)}
                                    onDragEnd={handleDragEnd}
                                    onDragOver={(e) => handleDragOver(e, chIdx, topIdx)}
                                    onDrop={(e) => handleDrop(e, chIdx, topIdx)}
                                    style={{
                                      background: 'var(--surface)',
                                      border: (dragOverTopic?.chIdx === chIdx && dragOverTopic?.topIdx === topIdx)
                                        ? '2px dashed var(--accent)'
                                        : '1px solid var(--border-light)',
                                      borderRadius: 'var(--radius-sm)',
                                      overflow: 'hidden',
                                      opacity: (draggedTopic?.chIdx === chIdx && draggedTopic?.topIdx === topIdx) ? 0.4 : 1,
                                      cursor: 'grab',
                                      transition: 'all 0.15s ease-in-out'
                                    }}
                                  >
                                    
                                    <div style={{ padding: '8px 12px', borderBottom: '1.2px dashed var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                      <div>
                                        <span style={{ fontWeight: 700, fontSize: '12px' }}>📍 Topic {topic.number}:</span>{' '}
                                        <span style={{ fontSize: '12px' }}>{topic.name}</span>
                                        <div style={{ display: 'inline-flex', gap: '6px', marginLeft: '12px', alignItems: 'center', flexWrap: 'wrap' }}>
                                          <span 
                                            onClick={(e) => {
                                              e.stopPropagation();
                                              if (activeSubjectDoc) {
                                                router.push(`/admin/question-bank?board=${encodeURIComponent(activeSubjectDoc.board)}&class=${encodeURIComponent(activeSubjectDoc.class)}&subject=${encodeURIComponent(activeSubjectDoc.subject)}&chapter=${encodeURIComponent(ch.number)}&topic=${encodeURIComponent(topic.number)}`);
                                              }
                                            }}
                                            title="Click to view questions in Question Bank"
                                            style={{ fontSize: '10px', fontWeight: 650, background: 'rgba(52, 152, 219, 0.1)', color: '#2980b9', padding: '1px 6px', borderRadius: '4px', cursor: 'pointer', textDecoration: 'underline' }}
                                          >
                                            O - {topic.objectiveCount || 0}
                                          </span>
                                          <span style={{ fontSize: '10px', fontWeight: 650, background: 'rgba(155, 89, 182, 0.1)', color: '#8e44ad', padding: '1px 6px', borderRadius: '4px' }}>
                                            S - {topic.subjectiveCount || 0}
                                          </span>
                                          {(() => {
                                            const subs = Array.isArray(topic.subtopics) ? topic.subtopics : [];
                                            const hasSubs = subs.length > 0;
                                            const targetCount = hasSubs
                                              ? subs.reduce((acc: number, s: any) => acc + (Number(typeof s === 'object' ? s.targetQuestions : 0) || 30), 0)
                                              : (topic.targetQuestions || 30);
                                            return (
                                              <span style={{ fontSize: '10px', fontWeight: 700, background: 'rgba(243, 156, 18, 0.12)', color: '#d35400', padding: '1px 6px', borderRadius: '4px' }}>
                                                🎯 Target: {targetCount} Qs {hasSubs ? `(Sum of ${subs.length} Subtopics)` : ''}
                                              </span>
                                            );
                                          })()}
                                          <span style={{ 
                                            fontSize: '10px', 
                                            fontWeight: 650, 
                                            background: 'rgba(52, 152, 219, 0.1)', 
                                            color: '#2980b9', 
                                            padding: '1px 6px', 
                                            borderRadius: '4px',
                                            display: 'inline-flex',
                                            alignItems: 'center',
                                            gap: '4px'
                                          }}>
                                            <span
                                              onClick={(e) => {
                                                e.stopPropagation();
                                                if (topic.tests && topic.tests.length > 0) {
                                                  handleOpenTestsModal(topic.name || 'Topic', topic.tests);
                                                }
                                              }}
                                              style={{
                                                cursor: (topic.tests && topic.tests.length > 0) ? 'pointer' : 'default',
                                                textDecoration: (topic.tests && topic.tests.length > 0) ? 'underline' : 'none'
                                              }}
                                            >
                                              O.Tests - {getObjectiveTestsCount(topic.tests)}
                                            </span>
                                          </span>
                                          <span style={{ 
                                            fontSize: '10px', 
                                            fontWeight: 650, 
                                            background: 'rgba(155, 89, 182, 0.1)', 
                                            color: '#8e44ad', 
                                            padding: '1px 6px', 
                                            borderRadius: '4px',
                                            display: 'inline-flex',
                                            alignItems: 'center',
                                            gap: '4px'
                                          }}>
                                            <span
                                              onClick={(e) => {
                                                e.stopPropagation();
                                                if (topic.tests && topic.tests.length > 0) {
                                                  handleOpenTestsModal(topic.name || 'Topic', topic.tests);
                                                }
                                              }}
                                              style={{
                                                cursor: (topic.tests && topic.tests.length > 0) ? 'pointer' : 'default',
                                                textDecoration: (topic.tests && topic.tests.length > 0) ? 'underline' : 'none'
                                              }}
                                            >
                                              S.Tests - {getSubjectiveTestsCount(topic.tests)}
                                            </span>
                                          </span>
                                          {Number(topic.testsCount || 0) > 0 && (
                                            <button 
                                              onClick={(e) => { e.stopPropagation(); handleResetTopicTests(topic.topicCode || ''); }} 
                                              title="Reset test attempts/submissions for this topic" 
                                              style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '10px', padding: '0 2px', display: 'flex', alignItems: 'center' }}
                                            >
                                              🔄
                                            </button>
                                          )}
                                          {Array.isArray(topic.textbookSets) && topic.textbookSets.map((set: any, sIdx: number) => {
                                            const isTh = /theorem|proof/i.test(set.name || '') || /theorem|proof/i.test(set.type || '');
                                            return (
                                              <span key={sIdx} style={{ fontSize: '10px', fontWeight: 650, background: isTh ? 'rgba(241, 196, 15, 0.1)' : 'rgba(46, 204, 113, 0.1)', color: isTh ? '#d35400' : '#27ae60', padding: '1px 6px', borderRadius: '4px', border: isTh ? '1px solid rgba(241, 196, 15, 0.2)' : '1px solid rgba(46, 204, 113, 0.2)', display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                                                📖 {set.name} ({set.questionCount || 8} Qs) {isTh && '📐 Theorem'}
                                              </span>
                                            );
                                          })}
                                        </div>
                                        <small style={{ display: 'block', fontSize: '8px', color: 'var(--text-muted)', marginTop: '2px' }}>{topic.topicCode}</small>
                                      </div>
                                      <div style={{ display: 'flex', gap: '5px' }}>
                                        <button className="btn btn-secondary" style={{ padding: '2px 5px', fontSize: '9px' }} onClick={() => handleOpenEditTopic(chIdx, topIdx, topic)}>✏️</button>
                                        <button className="btn btn-secondary" style={{ padding: '2px 5px', fontSize: '9px', color: 'var(--danger)' }} onClick={() => handleDeleteTopic(chIdx, topIdx)}>🗑️</button>
                                        <button className="btn btn-primary" style={{ padding: '2px 7px', fontSize: '9px' }} onClick={() => handleOpenAddSubtopic(chIdx, topIdx)}>+ Subtopic</button>
                                      </div>
                                    </div>

                                    {/* Subtopics List */}
                                    <div style={{ padding: '8px 12px 8px 30px', display: 'flex', flexDirection: 'column', gap: '6px' }}>
                                      {(!topic.subtopics || topic.subtopics.length === 0) ? (
                                        <span style={{ fontSize: '10px', color: 'var(--text-muted)', fontStyle: 'italic' }}>No subtopics.</span>
                                      ) : (
                                        topic.subtopics.map((sub: any, subIdx: number) => {
                                          const subName = typeof sub === 'string' 
                                            ? sub 
                                            : (sub?.name || sub?.subtopic || sub?.title || sub?.text || '');
                                          const subNumber = (typeof sub === 'object' && sub && sub.number) 
                                            ? sub.number 
                                            : `${topic.number}.${subIdx + 1}`;
                                          const objCount = typeof sub === 'object' ? (sub.objectiveCount || 0) : 0;
                                          const subjCount = typeof sub === 'object' ? (sub.subjectiveCount || 0) : 0;
                                          const testsList = (typeof sub === 'object' && Array.isArray(sub.tests)) ? sub.tests : [];
                                          return (
                                            <div 
                                              key={`s_${subIdx}`} 
                                              draggable={true}
                                              onDragStart={(e) => { e.stopPropagation(); handleSubtopicDragStart(chIdx, topIdx, subIdx); }}
                                              onDragEnd={(e) => { e.stopPropagation(); handleSubtopicDragEnd(); }}
                                              onDragOver={(e) => handleSubtopicDragOver(e, chIdx, topIdx, subIdx)}
                                              onDrop={(e) => handleSubtopicDrop(e, chIdx, topIdx, subIdx)}
                                              style={{ 
                                                display: 'flex', 
                                                justifyContent: 'space-between', 
                                                alignItems: 'center', 
                                                background: 'var(--bg-soft)', 
                                                padding: '5px 10px', 
                                                borderRadius: '4px', 
                                                border: (dragOverSubtopic?.chIdx === chIdx && dragOverSubtopic?.topIdx === topIdx && dragOverSubtopic?.subIdx === subIdx)
                                                  ? '2px dashed var(--accent)'
                                                  : '1.2px solid var(--border-light)',
                                                opacity: (draggedSubtopic?.chIdx === chIdx && draggedSubtopic?.topIdx === topIdx && draggedSubtopic?.subIdx === subIdx) ? 0.4 : 1,
                                                cursor: 'grab',
                                                transition: 'all 0.15s ease-in-out'
                                              }}
                                            >
                                              <div>
                                                <span style={{ fontWeight: 600, fontSize: '11px', color: 'var(--text-muted)' }}>📌 Subtopic {subNumber}:</span>{' '}
                                                <span style={{ fontSize: '11px' }}>{subName}</span>
                                                <div style={{ display: 'inline-flex', gap: '6px', marginLeft: '12px', alignItems: 'center' }}>
                                                  <span style={{ fontSize: '9px', fontWeight: 650, background: 'rgba(52, 152, 219, 0.08)', color: '#2980b9', padding: '1px 4px', borderRadius: '3px' }}>
                                                    O - {objCount}
                                                  </span>
                                                  <span style={{ fontSize: '9px', fontWeight: 650, background: 'rgba(155, 89, 182, 0.08)', color: '#8e44ad', padding: '1px 4px', borderRadius: '3px' }}>
                                                    S - {subjCount}
                                                  </span>
                                                  <span style={{ fontSize: '9px', fontWeight: 700, background: 'rgba(243, 156, 18, 0.12)', color: '#d35400', padding: '1px 4px', borderRadius: '3px' }}>
                                                    🎯 Target: {typeof sub === 'object' ? (sub.targetQuestions || 30) : 30} Qs
                                                  </span>
                                                  <span style={{ 
                                                     fontSize: '9px', 
                                                     fontWeight: 650, 
                                                     background: 'rgba(52, 152, 219, 0.08)', 
                                                     color: '#2980b9', 
                                                     padding: '1px 4px', 
                                                     borderRadius: '3px', 
                                                     display: 'inline-flex', 
                                                     alignItems: 'center', 
                                                     gap: '3px' 
                                                   }}>
                                                     <span 
                                                       onClick={(e) => { 
                                                         e.stopPropagation(); 
                                                         if (testsList.length > 0) {
                                                           handleOpenTestsModal(subName || 'Subtopic', testsList);
                                                         }
                                                       }}
                                                       style={{ 
                                                         cursor: (testsList.length > 0) ? 'pointer' : 'default',
                                                         textDecoration: (testsList.length > 0) ? 'underline' : 'none'
                                                       }}
                                                     >
                                                       O.Tests - {getObjectiveTestsCount(testsList)}
                                                     </span>
                                                   </span>
                                                   <span style={{ 
                                                     fontSize: '9px', 
                                                     fontWeight: 650, 
                                                     background: 'rgba(155, 89, 182, 0.08)', 
                                                     color: '#8e44ad', 
                                                     padding: '1px 4px', 
                                                     borderRadius: '3px', 
                                                     display: 'inline-flex', 
                                                     alignItems: 'center', 
                                                     gap: '3px' 
                                                   }}>
                                                     <span 
                                                       onClick={(e) => { 
                                                         e.stopPropagation(); 
                                                         if (testsList.length > 0) {
                                                           handleOpenTestsModal(subName || 'Subtopic', testsList);
                                                         }
                                                       }}
                                                       style={{ 
                                                         cursor: (testsList.length > 0) ? 'pointer' : 'default',
                                                         textDecoration: (testsList.length > 0) ? 'underline' : 'none'
                                                       }}
                                                     >
                                                       S.Tests - {getSubjectiveTestsCount(testsList)}
                                                     </span>
                                                   </span>
                                                   {Number(sub?.testsCount || 0) > 0 && (
                                                     <button 
                                                       onClick={(e) => { e.stopPropagation(); handleResetTopicTests(sub?.subtopicCode || ''); }} 
                                                       title="Reset test attempts/submissions for this subtopic" 
                                                       style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '9px', padding: '0 1px', display: 'flex', alignItems: 'center' }}
                                                     >
                                                       🔄
                                                     </button>
                                                   )}
                                                </div>
                                              </div>
                                              <div style={{ display: 'flex', gap: '3px', alignItems: 'center' }}>
                                                <button 
                                                  className="btn btn-secondary" 
                                                  style={{ padding: '2px 4px', fontSize: '8px', opacity: subIdx === 0 ? 0.35 : 1, cursor: subIdx === 0 ? 'not-allowed' : 'pointer' }} 
                                                  disabled={subIdx === 0} 
                                                  onClick={(e) => { e.stopPropagation(); handleMoveSubtopic(chIdx, topIdx, subIdx, 'up'); }} 
                                                  title="Move Subtopic Up"
                                                >
                                                  🔼
                                                </button>
                                                <button 
                                                  className="btn btn-secondary" 
                                                  style={{ padding: '2px 4px', fontSize: '8px', opacity: subIdx === (topic.subtopics?.length || 0) - 1 ? 0.35 : 1, cursor: subIdx === (topic.subtopics?.length || 0) - 1 ? 'not-allowed' : 'pointer' }} 
                                                  disabled={subIdx === (topic.subtopics?.length || 0) - 1} 
                                                  onClick={(e) => { e.stopPropagation(); handleMoveSubtopic(chIdx, topIdx, subIdx, 'down'); }} 
                                                  title="Move Subtopic Down"
                                                >
                                                  🔽
                                                </button>
                                                <button className="btn btn-secondary" style={{ padding: '2px 4px', fontSize: '8px' }} onClick={() => handleOpenEditSubtopic(chIdx, topIdx, subIdx, sub)} title="Edit Subtopic">✏️</button>
                                                <button className="btn btn-secondary" style={{ padding: '2px 4px', fontSize: '8px', color: 'var(--danger)' }} onClick={() => handleDeleteSubtopic(chIdx, topIdx, subIdx)} title="Delete Subtopic">🗑️</button>
                                              </div>
                                            </div>
                                          );
                                        })
                                      )}
                                    </div>

                                  </div>
                                ))
                              )}
                            </div>
                          )}

                        </div>
                      );
                    })
                  )}
                </div>
              )}
            </div>
          </div>
        )}

        {/* Tab 3: AI Syllabus Generator */}
        {activeTab === 'ai' && (
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '20px' }}>
            <h3 style={{ fontSize: '14px', fontWeight: 700, marginBottom: '15px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px' }}>
              🤖 AI Syllabus Generator
            </h3>
            
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '15px', marginBottom: '20px' }}>
              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Board</label>
                <input 
                  type="text" 
                  value={aiBoard} 
                  onChange={(e) => setAiBoard(e.target.value)}
                  style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                />
              </div>
              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Class</label>
                <input 
                  type="text" 
                  value={aiClass} 
                  onChange={(e) => setAiClass(e.target.value)}
                  style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                />
              </div>
              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Subject Name</label>
                <input 
                  type="text" 
                  value={aiSubject} 
                  placeholder="e.g. Mathematics"
                  onChange={(e) => setAiSubject(e.target.value)}
                  style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                />
              </div>
              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Subject Code</label>
                <input 
                  type="text" 
                  value={aiSubjectCode} 
                  placeholder="e.g. MTH1"
                  onChange={(e) => setAiSubjectCode(e.target.value)}
                  style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                />
              </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '20px' }}>
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                  <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>📋 AI Prompt (Copy to Gemini)</label>
                  <button className="btn btn-secondary" style={{ padding: '2px 8px', fontSize: '10px' }} onClick={handleCopyPrompt}>Copy Prompt</button>
                </div>
                <textarea 
                  value={aiPrompt}
                  readOnly
                  placeholder="Click 'Generate Prompt' below to compose"
                  style={{ width: '100%', height: '140px', padding: '10px', background: 'var(--bg-soft)', color: 'var(--text-muted)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '11px', fontFamily: 'monospace' }}
                />
              </div>
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                  <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>📥 Paste AI Response</label>
                  <button className="btn btn-primary" style={{ padding: '2px 8px', fontSize: '10px' }} onClick={handleParseAndPreview}>Parse & Preview</button>
                </div>
                <textarea 
                  value={aiResponse}
                  onChange={(e) => setAiResponse(e.target.value)}
                  placeholder="Paste JSON response from Gemini here..."
                  style={{ width: '100%', height: '140px', padding: '10px', background: 'var(--surface)', color: 'var(--text)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '11px', fontFamily: 'monospace' }}
                />
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'center', gap: '10px', marginTop: '15px', borderBottom: aiPreviewData ? '1px solid var(--border-light)' : 'none', paddingBottom: '15px' }}>
              <button className="btn btn-primary" onClick={handleGenerateAIPrompt}>🔧 Generate Prompt</button>
            </div>

            {/* AI Preview Tree */}
            {aiPreviewData && (
              <div style={{ marginTop: '20px' }}>
                <h4 style={{ fontSize: '13px', fontWeight: 700, marginBottom: '12px' }}>📖 Generated Syllabus Preview</h4>
                <div style={{ background: 'var(--bg-soft)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '15px', maxHeight: '250px', overflowY: 'auto' }}>
                  <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--accent)', marginBottom: '10px' }}>
                    Syllabus: {aiPreviewData.board} | Class {aiPreviewData.class} | {aiPreviewData.subject} ({aiPreviewData.subjectCode})
                  </div>
                   {aiPreviewData.chapters?.map((ch: any, ci: number) => (
                    <div key={ci} style={{ fontSize: '12px', marginLeft: '10px', marginBottom: '5px' }}>
                      🟢 <strong>Ch.{ch.number}: {ch.name}</strong>
                      {ch.chapterExercises && Array.isArray(ch.chapterExercises) && ch.chapterExercises.map((ex: any, exIdx: number) => (
                        <span key={exIdx} style={{ fontSize: '9px', fontWeight: 650, background: 'rgba(230, 126, 34, 0.1)', color: '#d35400', padding: '1px 5px', borderRadius: '4px', marginLeft: '5px' }}>
                          📖 {ex.name} ({ex.questionCount || 8} Qs)
                        </span>
                      ))}
                      {ch.topics?.map((t: any, ti: number) => (
                        <div key={ti} style={{ fontSize: '11px', marginLeft: '20px', color: 'var(--text)', marginBottom: '3px' }}>
                          • Topic {t.number}: {t.name}
                          {t.textbookSets && Array.isArray(t.textbookSets) && t.textbookSets.map((set: any, sIdx: number) => (
                            <span key={sIdx} style={{ fontSize: '9px', fontWeight: 650, background: 'rgba(46, 204, 113, 0.1)', color: '#27ae60', padding: '1px 5px', borderRadius: '4px', marginLeft: '5px' }}>
                              📖 {set.name} ({set.questionCount || 8} Qs)
                            </span>
                          ))}
                          {t.subtopics?.map((sub: any, subIdx: number) => (
                            <div key={subIdx} style={{ fontSize: '10px', marginLeft: '20px', color: 'var(--text-muted)' }}>
                              ▫️ Subtopic {sub.number}: {sub.name}
                            </div>
                          ))}
                        </div>
                      ))}
                    </div>
                  ))}
                </div>
                <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '15px' }}>
                  <button className="btn btn-primary" style={{ background: 'var(--success)', borderColor: 'var(--success)' }} onClick={handleSaveAISyllabus} disabled={saving}>
                    💾 Save to Database
                  </button>
                </div>
              </div>
            )}
          </div>
        )}
      </>
    )}
  </main>

      {/* Modal: Subject Add/Edit */}
      {subjectModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '450px', width: '90%', padding: '24px', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0 }}>
              {subjectModal.mode === 'add' ? 'Add New Subject' : 'Edit Subject details'}
            </h3>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Document ID (immutable once saved)</label>
              <input 
                type="text" 
                value={subjectModal.docId}
                disabled={subjectModal.mode === 'edit'}
                placeholder="e.g. cbse_10_mathematics"
                onChange={(e) => setSubjectModal(prev => ({ ...prev, docId: e.target.value }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: subjectModal.mode === 'edit' ? 'var(--bg-soft)' : 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
              <small style={{ fontSize: '9px', color: 'var(--text-muted)', marginTop: '3px', display: 'block' }}>Format: board_class_subject</small>
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Board</label>
              <input 
                type="text" 
                value={subjectModal.board}
                placeholder="e.g. CBSE"
                onChange={(e) => setSubjectModal(prev => ({ ...prev, board: e.target.value }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Class</label>
              <input 
                type="text" 
                value={subjectModal.classNum}
                placeholder="e.g. 10"
                onChange={(e) => setSubjectModal(prev => ({ ...prev, classNum: e.target.value }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Subject Name</label>
              <input 
                type="text" 
                value={subjectModal.subjectName}
                placeholder="e.g. Mathematics"
                onChange={(e) => setSubjectModal(prev => ({ ...prev, subjectName: e.target.value }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
            </div>

            <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
              Resolved Subject Code preview: <strong>{getSubjectCodePreview(subjectModal.board, subjectModal.subjectName) || '—'}</strong>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px' }}>
              <button className="btn btn-secondary" onClick={() => setSubjectModal(prev => ({ ...prev, show: false }))}>Cancel</button>
              <button className="btn btn-primary" onClick={handleSaveSubject} disabled={saving}>Save Subject</button>
            </div>
          </div>
        </div>
      )}

      {/* Modal: Chapter Add/Edit */}
      {chapterModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '400px', width: '90%', padding: '24px', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0 }}>
              {chapterModal.mode === 'add' ? 'Add Chapter' : 'Edit Chapter'}
            </h3>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Chapter Number</label>
              <input 
                type="text" 
                value={chapterModal.number}
                placeholder="e.g. 1"
                onChange={(e) => setChapterModal(prev => ({ ...prev, number: e.target.value }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Chapter Name</label>
              <input 
                type="text" 
                value={chapterModal.name}
                placeholder="e.g. Real Numbers"
                onChange={(e) => setChapterModal(prev => ({ ...prev, name: e.target.value }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Problem Sets / Exercises (Format: Name: QsCount, Name: QsCount)</label>
              <input 
                type="text" 
                value={chapterModal.chapterExercisesStr}
                placeholder="e.g. Problem Set 1: 9"
                onChange={(e) => setChapterModal(prev => ({ ...prev, chapterExercisesStr: e.target.value }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
              <span style={{ fontSize: '9px', color: 'var(--text-muted)', marginTop: '2px', display: 'block' }}>Comma-separated textbook sets. E.g., <code>Problem Set 1: 9</code></span>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px' }}>
              <button className="btn btn-secondary" onClick={() => setChapterModal(prev => ({ ...prev, show: false }))}>Cancel</button>
              <button className="btn btn-primary" onClick={handleSaveChapter} disabled={saving}>Save Chapter</button>
            </div>
          </div>
        </div>
      )}

      {/* Modal: Topic Add/Edit */}
      {topicModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '400px', width: '90%', padding: '24px', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0 }}>
              {topicModal.mode === 'add' ? 'Add Topic' : 'Edit Topic'}
            </h3>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Topic Number</label>
              <input 
                type="text" 
                value={topicModal.number}
                placeholder="e.g. 1.1"
                onChange={(e) => setTopicModal(prev => ({ ...prev, number: e.target.value }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Topic Name</label>
              <input 
                type="text" 
                value={topicModal.name}
                placeholder="e.g. Fundamental Theorem of Arithmetic"
                onChange={(e) => setTopicModal(prev => ({ ...prev, name: e.target.value }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
            </div>

            {topicModal.hasSubtopics ? (
              <div style={{ background: 'var(--bg-soft)', padding: '10px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '3px' }}>Target Question Quota</label>
                <div style={{ fontSize: '12px', fontWeight: 700, color: '#d35400', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span>🎯 {topicModal.subtopicsSum} Qs</span>
                  <span style={{ fontSize: '10.5px', fontWeight: 'normal', color: 'var(--text-muted)' }}>(Sum of {activeSubjectDoc?.chapters?.[topicModal.chIdx]?.topics?.[topicModal.editIdx || 0]?.subtopics?.length || 0} subtopics)</span>
                </div>
                <small style={{ fontSize: '9.5px', color: 'var(--text-muted)', display: 'block', marginTop: '4px' }}>
                  💡 Topics with subtopics derive their quota automatically from the sum of subtopic quotas.
                </small>
              </div>
            ) : (
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '5px' }}>
                  <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Target Question Quota</label>
                  <div style={{ display: 'flex', gap: '4px' }}>
                    <button type="button" className="btn btn-secondary btn-sm" style={{ fontSize: '10px', padding: '1px 6px', borderRadius: '10px' }} onClick={() => setTopicModal(p => ({ ...p, targetQuestions: 50 }))}>🔥 Deep (50)</button>
                    <button type="button" className="btn btn-secondary btn-sm" style={{ fontSize: '10px', padding: '1px 6px', borderRadius: '10px' }} onClick={() => setTopicModal(p => ({ ...p, targetQuestions: 30 }))}>⚡ Std (30)</button>
                    <button type="button" className="btn btn-secondary btn-sm" style={{ fontSize: '10px', padding: '1px 6px', borderRadius: '10px' }} onClick={() => setTopicModal(p => ({ ...p, targetQuestions: 15 }))}>🎯 Light (15)</button>
                  </div>
                </div>
                <input 
                  type="number" 
                  value={topicModal.targetQuestions}
                  min={5}
                  max={150}
                  placeholder="e.g. 30"
                  onChange={(e) => setTopicModal(prev => ({ ...prev, targetQuestions: e.target.value === '' ? '' : (parseInt(e.target.value, 10) || '') }))}
                  style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                />
              </div>
            )}

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Textbook Sets (Format: Name: QsCount, Name: QsCount)</label>
              <input 
                type="text" 
                value={topicModal.textbookSetsStr}
                placeholder="e.g. Practice Set 1.1: 5, Chapter 1 Solved Examples (Topic 1.1): 3"
                onChange={(e) => setTopicModal(prev => ({ ...prev, textbookSetsStr: e.target.value }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
              <span style={{ fontSize: '9px', color: 'var(--text-muted)', marginTop: '2px', display: 'block' }}>E.g., <code>Practice Set 1.1: 5</code>. Solved examples should include the word <strong>"Solved"</strong> in their name.</span>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px' }}>
              <button className="btn btn-secondary" onClick={() => setTopicModal(prev => ({ ...prev, show: false }))}>Cancel</button>
              <button className="btn btn-primary" onClick={handleSaveTopic} disabled={saving}>Save Topic</button>
            </div>
          </div>
        </div>
      )}

      {/* Modal: Subtopic Add/Edit */}
      {subtopicModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '400px', width: '90%', padding: '24px', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0 }}>
              {subtopicModal.mode === 'add' ? 'Add Subtopic' : 'Edit Subtopic'}
            </h3>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Subtopic Number</label>
              <input 
                type="text" 
                value={subtopicModal.number}
                placeholder="e.g. 1.1.1"
                onChange={(e) => setSubtopicModal(prev => ({ ...prev, number: e.target.value }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Subtopic Name</label>
              <input 
                type="text" 
                value={subtopicModal.name}
                placeholder="e.g. Proof of Irrationality of √2"
                onChange={(e) => setSubtopicModal(prev => ({ ...prev, name: e.target.value }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
            </div>

            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '5px' }}>
                <label style={{ fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)' }}>Target Question Quota</label>
                <div style={{ display: 'flex', gap: '4px' }}>
                  <button type="button" className="btn btn-secondary btn-sm" style={{ fontSize: '10px', padding: '1px 6px', borderRadius: '10px' }} onClick={() => setSubtopicModal(p => ({ ...p, targetQuestions: 50 }))}>🔥 Deep (50)</button>
                  <button type="button" className="btn btn-secondary btn-sm" style={{ fontSize: '10px', padding: '1px 6px', borderRadius: '10px' }} onClick={() => setSubtopicModal(p => ({ ...p, targetQuestions: 30 }))}>⚡ Std (30)</button>
                  <button type="button" className="btn btn-secondary btn-sm" style={{ fontSize: '10px', padding: '1px 6px', borderRadius: '10px' }} onClick={() => setSubtopicModal(p => ({ ...p, targetQuestions: 15 }))}>🎯 Light (15)</button>
                </div>
              </div>
              <input 
                type="number" 
                value={subtopicModal.targetQuestions}
                min={5}
                max={150}
                placeholder="e.g. 30"
                onChange={(e) => setSubtopicModal(prev => ({ ...prev, targetQuestions: e.target.value === '' ? '' : (parseInt(e.target.value, 10) || '') }))}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              />
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px' }}>
              <button className="btn btn-secondary" onClick={() => setSubtopicModal(prev => ({ ...prev, show: false }))}>Cancel</button>
              <button className="btn btn-primary" onClick={handleSaveSubtopic} disabled={saving}>Save Subtopic</button>
            </div>
          </div>
        </div>
      )}

      {/* Modal: Covered Tests List */}
      {testsModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 9999, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', padding: '24px', maxWidth: '500px', width: '90%', maxHeight: '80vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-popover)', boxShadow: 'var(--shadow-lg)' }}>
            
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px', borderBottom: '1px solid var(--border-light)', paddingBottom: '12px' }}>
              <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0 }}>📝 Tests covering: "{testsModal.title}"</h3>
              <button 
                onClick={() => setTestsModal(prev => ({ ...prev, show: false }))} 
                style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '16px', color: 'var(--text-muted)' }}
              >
                ✕
              </button>
            </div>

            <div style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '10px', paddingRight: '4px' }}>
              {testsModal.tests.map((test, index) => (
                <div 
                  key={index} 
                  style={{ 
                    padding: '12px', 
                    borderRadius: 'var(--radius-sm)', 
                    background: 'var(--bg-soft)', 
                    border: '1.2px solid var(--border-light)', 
                    display: 'flex', 
                    justifyContent: 'space-between', 
                    alignItems: 'center', 
                    gap: '10px' 
                  }}
                >
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '3px' }}>
                    <span style={{ fontSize: '12.5px', fontWeight: 650, color: 'var(--text)' }}>
                      {test.name}
                    </span>
                    <span style={{ fontSize: '10px', color: 'var(--text-muted)', fontFamily: 'monospace' }}>
                      ID: {test.id}
                    </span>
                  </div>
                  <span 
                    style={{ 
                      fontSize: '9.5px', 
                      fontWeight: 700, 
                      padding: '2px 8px', 
                      borderRadius: '10px', 
                      background: test.type === 'subjective' ? 'rgba(46, 204, 113, 0.15)' : 'rgba(52, 152, 219, 0.15)', 
                      color: test.type === 'subjective' ? '#2ecc71' : '#3498db',
                      textTransform: 'uppercase' 
                    }}
                  >
                    {test.type}
                  </span>
                </div>
              ))}
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '16px', borderTop: '1px solid var(--border-light)', paddingTop: '12px' }}>
              <button className="btn btn-secondary" onClick={() => setTestsModal(prev => ({ ...prev, show: false }))}>Close</button>
            </div>

          </div>
        </div>
      )}

      {/* Rebuilder Overlay Loader */}
      {utilityLoading && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', padding: '30px', maxWidth: '380px', width: '90%', textAlign: 'center', border: '1px solid var(--border-popover)', boxShadow: 'var(--shadow-lg)' }}>
            <div className="spinner" style={{ margin: '0 auto 15px' }}></div>
            <h3 style={{ fontSize: '15px', fontWeight: 800, margin: '0 0 5px' }}>⚙️ Running Curricular Rebuild...</h3>
            <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>{utilityMessage}</div>
          </div>
        </div>
      )}
      <ExportPdfModal
        isOpen={pdfSelectorOpen}
        onClose={() => setPdfSelectorOpen(false)}
        title="Classroom Syllabus Curriculum Matrix"
        filename="Syllabus_Curriculum.pdf"
        sections={[
          { id: 'subjects', name: 'Syllabus Subjects Table', elementId: 'syllabus-subjects-section' }
        ]}
      />
    </div>
  );
}
