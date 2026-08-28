'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import Script from 'next/script';
import { useMathRender } from '@/hooks/useMathRender';
import { useToggleSet } from '@/hooks/useToggleSet';
import { preprocessMathText, robustParseAIJson, parseAiSolutionsMap, parseTopicCode } from '@/lib/questionTypes';
import Image from 'next/image';
interface Question {
  id?: string;
  questionCode: string;
  qNumber?: number;
  type: string;
  text: string;
  options?: string[];
  correctAnswer?: string;
  correctAnswers?: string[];
  assertion?: string;
  reason?: string;
  solution?: string;
  difficulty: string;
  bloomLevel: string;
  board: string;
  class: string;
  subject: string;
  chapterNumber: string;
  topicNumber: string;
  timesUsed?: number;
  usedInClassroomTest?: boolean;
  requiresFigure?: boolean;
  imageUrl?: string;
  examCategory?: string;
}

export default function AdminQuestionBankPage() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Index metadata
  const [syllabusIndex, setSyllabusIndex] = useState<any>(null);
  const [boardCodes, setBoardCodes] = useState<any>({});
  const [subjectCodes, setSubjectCodes] = useState<any>({});

  // Question bank items list
  const [questions, setQuestions] = useState<Question[]>([]);
  const [totalCount, setTotalCount] = useState(0);
  const [itemsPerPage, setItemsPerPage] = useState(10);
  const [currentPage, setCurrentPage] = useState(1);
  const [lastCodesHistory, setLastCodesHistory] = useState<string[]>(['']); // Stack of last codes for prev/next paging

  // Filtering inputs
  const [filterBoard, setFilterBoard] = useState('');
  const [filterClass, setFilterClass] = useState('');
  const [filterSubject, setFilterSubject] = useState('');
  const [filterChapter, setFilterChapter] = useState('');
  const [filterTopic, setFilterTopic] = useState('');
  const [filterCategory, setFilterCategory] = useState('');
  const [filterType, setFilterType] = useState('');
  const [filterUsage, setFilterUsage] = useState('all');

  // Dropdown lists derived from index
  const [availableSubjects, setAvailableSubjects] = useState<string[]>([]);
  const [availableChapters, setAvailableChapters] = useState<any[]>([]);
  const [availableTopics, setAvailableTopics] = useState<any[]>([]);

  // Selection state
  const [selectedCodes, setSelectedCodes] = useState<Set<string>>(new Set());

  // Duplicates scanner states
  const [duplicateGroups, setDuplicateGroups] = useState<any[]>([]);
  const [scanningDuplicates, setScanningDuplicates] = useState(false);
  const [showDuplicatesModal, setShowDuplicatesModal] = useState(false);
  const [duplicateScanScope, setDuplicateScanScope] = useState<'filtered' | 'all'>('filtered');
  const [selectedDups, setSelectedDups] = useState<Set<string>>(new Set());

  // Audit Explanations states
  const [showAuditModal, setShowAuditModal] = useState(false);
  const [auditLoading, setAuditLoading] = useState(false);
  const [auditGenerating, setAuditGenerating] = useState(false);
  const [auditStats, setAuditStats] = useState<any>(null);
  const [showAiPromptBox, setShowAiPromptBox] = useState(false);
  const [pastedAiResponse, setPastedAiResponse] = useState('');
  const [importingAi, setImportingAi] = useState(false);

  // Numerical Audit states
  const [showNumericalAuditModal, setShowNumericalAuditModal] = useState(false);
  const [auditingNumerical, setAuditingNumerical] = useState(false);
  const [numericalCandidates, setNumericalCandidates] = useState<any[]>([]);

  // Question Disputes states
  const [showDisputesModal, setShowDisputesModal] = useState(false);
  const [disputesList, setDisputesList] = useState<any[]>([]);
  const [loadingDisputes, setLoadingDisputes] = useState(false);
  const [selectedDisputeScreenshot, setSelectedDisputeScreenshot] = useState<string | null>(null);

  useMathRender([questions, currentPage, lastCodesHistory, filterBoard, filterClass, filterSubject, filterChapter, filterTopic, filterType, duplicateGroups, showDuplicatesModal, showAuditModal, showNumericalAuditModal, showDisputesModal]);

  // Question Modal Editor form
  const [showEditModal, setShowEditModal] = useState(false);
  const [editorModal, setEditorModal] = useState({
    mode: 'add' as 'add' | 'edit',
    id: '',
    board: 'CBSE',
    classNum: '10',
    subjectName: '',
    chapterNumber: '1',
    topicNumber: '1.1',
    qtype: 'single_mcq',
    text: '',
    options: ['Option A', 'Option B', 'Option C', 'Option D'],
    correctAnswer: 'Option A',
    correctAnswers: [] as string[],
    assertion: '',
    reason: '',
    solution: '',
    difficulty: 'medium',
    bloomLevel: 'Remember',
    requiresFigure: false,
    imageUrl: '',
    examCategory: 'standard'
  });

  const [savingQuestion, setSavingQuestion] = useState(false);

  // Load initial configurations
  const loadInitialMetadata = async () => {
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      // Load board/class/subject trees
      const res = await fetch('/api/admin/exams/generate', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (res.ok) {
        const data = await res.json();
        setSyllabusIndex(data.syllabusSubjects);
        setBoardCodes(data.boardCodes);
        setSubjectCodes(data.subjectCodes);
      }
    } catch (err) {
      console.error('Metadata load error:', err);
    }
  };

  // Fetch paginated questions matching current filters
  const fetchQuestionsList = async (lastCode: string = '') => {
    if (!firebaseUser) return;
    if (!filterBoard || !filterClass || !filterSubject) {
      setQuestions([]);
      setTotalCount(0);
      setLoading(false);
      return;
    }
    setLoading(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const actualLimit = itemsPerPage;
      const params = new URLSearchParams({
        limit: String(actualLimit),
        lastCode,
        board: filterBoard,
        classNum: filterClass,
        subject: filterSubject,
        chapterNumber: filterChapter,
        topicNumber: filterTopic,
        category: filterCategory,
        type: filterType,
        usageStatus: filterUsage !== 'all' ? filterUsage : ''
      });

      const res = await fetch(`/api/admin/questions?${params.toString()}`, {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (!res.ok) {
        throw new Error('Failed to fetch questions list.');
      }
      const data = await res.json();
      setQuestions(data.questions || []);
      setTotalCount(data.totalCount || 0);
      setSelectedCodes(new Set());
    } catch (err: any) {
      setError(err.message || 'Error occurred pulling questions.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (firebaseUser) {
      loadInitialMetadata();

      // Read URL search parameters on mount
      if (typeof window !== 'undefined') {
        const urlParams = new URLSearchParams(window.location.search);
        let b = urlParams.get('board') || '';
        if (b === 'MSBSHSE' || b === 'MH' || b === 'State Board') b = 'Maharashtra Board';
        const c = urlParams.get('classNum') || urlParams.get('class') || '';
        const s = urlParams.get('subject') || '';
        const ch = urlParams.get('chapterNumber') || urlParams.get('chapter') || '';
        const top = urlParams.get('topicNumber') || urlParams.get('topic') || '';

        if (b) setFilterBoard(b);
        if (c) setFilterClass(c);
        if (s) setFilterSubject(s);
        if (ch) setFilterChapter(ch);
        if (top) setFilterTopic(top);
      }
    }
  }, [firebaseUser]);

  useEffect(() => {
    if (firebaseUser) {
      setCurrentPage(1);
      setLastCodesHistory(['']);
      fetchQuestionsList();
    }
  }, [firebaseUser, filterBoard, filterClass, filterSubject, filterChapter, filterTopic, filterCategory, filterType, filterUsage, itemsPerPage]);

  // Handle Page click navigation
  const handleNextPage = () => {
    if (questions.length === 0) return;
    const lastQ = questions[questions.length - 1];
    if (lastQ && lastQ.questionCode) {
      const nextStack = [...lastCodesHistory, lastQ.questionCode];
      setLastCodesHistory(nextStack);
      setCurrentPage(prev => prev + 1);
      fetchQuestionsList(lastQ.questionCode);
    }
  };

  const handlePrevPage = () => {
    if (currentPage === 1) return;
    const prevStack = [...lastCodesHistory];
    prevStack.pop(); // Remove current offset code
    const lastCode = prevStack[prevStack.length - 1] || '';
    setLastCodesHistory(prevStack);
    setCurrentPage(prev => prev - 1);
    fetchQuestionsList(lastCode);
  };

  // Cascade Filter Triggers
  const handleBoardChange = (board: string) => {
    setFilterBoard(board);
    setFilterClass('');
    setFilterSubject('');
    setFilterChapter('');
    setFilterTopic('');
    setAvailableSubjects([]);
    setAvailableChapters([]);
    setAvailableTopics([]);
  };

  const handleClassChange = (cls: string) => {
    setFilterClass(cls);
    setFilterSubject('');
    setFilterChapter('');
    setFilterTopic('');
    const list = Object.keys(syllabusIndex?.subjects?.[filterBoard]?.[cls] || {}).sort();
    setAvailableSubjects(list);
    setAvailableChapters([]);
    setAvailableTopics([]);
  };

  const handleSubjectChange = async (subj: string) => {
    setFilterSubject(subj);
    setFilterChapter('');
    setFilterTopic('');
    setAvailableChapters([]);
    setAvailableTopics([]);

    // Load chapters list for this subject
    const entry = syllabusIndex?.subjects?.[filterBoard]?.[filterClass]?.[subj];
    if (entry && entry.docId && firebaseUser) {
      try {
        const idToken = await firebaseUser.getIdToken();
        const res = await fetch(`/api/admin/exams/generate?docId=${entry.docId}`, {
          headers: { 'Authorization': `Bearer ${idToken}` }
        });
        if (res.ok) {
          const data = await res.json();
          setAvailableChapters(data.chapters || []);
        }
      } catch (err) {
        console.error(err);
      }
    }
  };

  const handleChapterChange = (chNum: string) => {
    setFilterChapter(chNum);
    setFilterTopic('');

    const chItem = availableChapters.find(c => String(c.number) === chNum);
    if (chItem) {
      const list: any[] = [];
      (chItem.topics || []).forEach((t: any) => {
        const topNum = t.number || '';
        const topName = t.name || t.topicName || '';
        if (topNum || topName) {
          list.push({ number: topNum, name: topName, isSubtopic: false });
        }
        if (Array.isArray(t.subtopics)) {
          t.subtopics.forEach((sub: any, subIdx: number) => {
            const subName = typeof sub === 'string' ? sub : (sub.name || sub.subtopic || sub.title || sub.text || '');
            const subNumber = (typeof sub === 'object' && sub && sub.number) ? String(sub.number) : (topNum ? `${topNum}.${subIdx + 1}` : `${subIdx + 1}`);
            if (subName || subNumber) {
              list.push({ number: subNumber, name: subName, isSubtopic: true });
            }
          });
        }
      });
      setAvailableTopics(list);
    } else {
      setAvailableTopics([]);
    }
  };

  const handleTopicChange = (topNum: string) => {
    setFilterTopic(topNum);
  };

  const handleCategoryChange = (cat: string) => {
    setFilterCategory(cat);
    setFilterType('');
    setCurrentPage(1);
    setLastCodesHistory(['']);
  };

  // Reset Filters
  const handleResetFilters = () => {
    setFilterBoard('');
    setFilterClass('');
    setFilterSubject('');
    setFilterChapter('');
    setFilterTopic('');
    setFilterCategory('');
    setFilterType('');
    setFilterUsage('all');
    setAvailableSubjects([]);
    setAvailableChapters([]);
    setAvailableTopics([]);
    setCurrentPage(1);
    setLastCodesHistory(['']);
  };

  // Checkbox Selection helper
  const handleToggleSelectQuestion = (qCode: string) => {
    const next = new Set(selectedCodes);
    if (next.has(qCode)) next.delete(qCode);
    else next.add(qCode);
    setSelectedCodes(next);
  };

  const handleToggleSelectAll = () => {
    if (selectedCodes.size === questions.length) {
      setSelectedCodes(new Set());
    } else {
      const next = new Set<string>();
      questions.forEach(q => {
        if (q.questionCode) next.add(q.questionCode);
      });
      setSelectedCodes(next);
    }
  };

  // Bulk deletion action
  const handleBulkDelete = async () => {
    if (selectedCodes.size === 0) return;
    if (!confirm(`Are you sure you want to delete ${selectedCodes.size} selected questions?`)) return;
    if (!firebaseUser) return;

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/questions', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ ids: Array.from(selectedCodes) })
      });

      if (!res.ok) throw new Error('Bulk delete failed.');
      alert('✅ Selected questions deleted.');
      setSelectedCodes(new Set());
      await fetchQuestionsList();
    } catch (err: any) {
      alert(err.message || 'Error executing deletion.');
    }
  };

  // Delete Individual Question
  const handleDeleteQuestion = async (qCode: string) => {
    if (!confirm(`Delete question: ${qCode}?`)) return;
    if (!firebaseUser) return;

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/questions?id=${qCode}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) throw new Error('Delete failed.');
      alert('✅ Question deleted.');
      await fetchQuestionsList();
    } catch (err: any) {
      alert(err.message || 'Error occurred.');
    }
  };

  // Find Duplicates Sweep
  const triggerDuplicatesScan = async (scope: 'filtered' | 'all' = 'filtered') => {
    setScanningDuplicates(true);
    setShowDuplicatesModal(true);
    setDuplicateScanScope(scope);
    setDuplicateGroups([]);
    setSelectedDups(new Set());

    try {
      const idToken = await firebaseUser!.getIdToken();
      let url = '/api/admin/questions?action=fetchDuplicates';
      if (scope === 'filtered') {
        const params = new URLSearchParams();
        if (filterBoard) params.set('board', filterBoard);
        if (filterClass) params.set('classNum', filterClass);
        if (filterSubject) params.set('subject', filterSubject);
        const qStr = params.toString();
        if (qStr) url += `&${qStr}`;
      }
      const res = await fetch(url, {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (res.ok) {
        const data = await res.json();
        setDuplicateGroups(data.duplicateGroups || []);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setScanningDuplicates(false);
    }
  };

  const handleToggleSelectDup = (id: string) => {
    const next = new Set(selectedDups);
    if (next.has(id)) next.delete(id);
    else next.add(id);
    setSelectedDups(next);
  };

  const handleSelectAllDuplicates = () => {
    const next = new Set<string>();
    duplicateGroups.forEach(g => {
      // Keep the first item (index 0) in each duplicate list, delete the rest
      const keep = g.questions[0];
      g.questions.forEach((q: any) => {
        if (q.questionCode !== keep.questionCode) {
          next.add(q.questionCode);
        }
      });
    });
    setSelectedDups(next);
  };

  const handleDeleteSelectedDuplicates = async () => {
    if (selectedDups.size === 0) return;
    if (!confirm(`Are you sure you want to purge ${selectedDups.size} duplicate questions?`)) return;

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/questions', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ ids: Array.from(selectedDups) })
      });

      if (!res.ok) throw new Error('Failed to delete duplicates.');
      alert('✅ Purged duplicate questions.');
      setShowDuplicatesModal(false);
      await fetchQuestionsList();
    } catch (err: any) {
      alert(err.message || 'Error occurred.');
    }
  };

  const handleOpenAuditModal = async () => {
    setShowAuditModal(true);
    setAuditLoading(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/questions/audit-explanations', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (res.ok) {
        const data = await res.json();
        setAuditStats(data);
      }
    } catch (err: any) {
      console.error('Audit load error:', err);
    } finally {
      setAuditLoading(false);
    }
  };

  const handleRunGenerateExplanations = async (forceAll = false) => {
    if (!confirm(forceAll ? 'Regenerate explanations for ALL objective questions?' : 'Auto-generate step-by-step explanations for objective questions missing solutions?')) return;
    setAuditGenerating(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/questions/audit-explanations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ forceAll })
      });
      if (!res.ok) throw new Error('Failed to generate explanations.');
      const data = await res.json();
      alert(`✅ ${data.message}`);
      await handleOpenAuditModal();
      await fetchQuestionsList();
    } catch (err: any) {
      alert(err.message || 'Error auto-generating explanations.');
    } finally {
      setAuditGenerating(false);
    }
  };

  const handleOpenNumericalAuditModal = async () => {
    setShowNumericalAuditModal(true);
    setAuditingNumerical(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/questions/audit-numerical', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (res.ok) {
        const data = await res.json();
        setNumericalCandidates(data.candidates || []);
      }
    } catch (err: any) {
      console.error('Numerical audit load error:', err);
    } finally {
      setAuditingNumerical(false);
    }
  };

  const handleMigrateNumericalQuestions = async () => {
    if (!confirm(`Are you sure you want to migrate ${numericalCandidates.length} candidate non-numerical objective questions to type 'numerical'?`)) return;
    setAuditingNumerical(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/questions/audit-numerical', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) throw new Error('Failed to execute numerical migration.');
      const data = await res.json();
      alert(`✅ ${data.message}`);
      setShowNumericalAuditModal(false);
      await fetchQuestionsList();
    } catch (err: any) {
      alert(err.message || 'Error running numerical migration.');
    } finally {
      setAuditingNumerical(false);
    }
  };

  const handleOpenDisputesModal = async () => {
    setShowDisputesModal(true);
    setLoadingDisputes(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/questions/disputes', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (res.ok) {
        const data = await res.json();
        setDisputesList(data.disputes || []);
      }
    } catch (err) {
      console.error('Failed to load disputes:', err);
    } finally {
      setLoadingDisputes(false);
    }
  };

  const handleResolveDispute = async (disputeId: string, action: 'approve' | 'reject' | 'quarantine') => {
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/questions/disputes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ disputeId, action })
      });
      if (res.ok) {
        alert(`✅ Action completed: Question ${action === 'approve' || action === 'quarantine' ? 'quarantined' : 'dismissed'}, and the dispute record & proof screenshot have been permanently deleted.`);
        handleOpenDisputesModal();
      }
    } catch (err: any) {
      alert('Error updating dispute: ' + err.message);
    }
  };

  const handleCopyAiPrompt = () => {
    if (!auditStats || !auditStats.allMissingQuestions || auditStats.allMissingQuestions.length === 0) {
      alert('No questions missing solutions!');
      return;
    }

    const missingList = auditStats.allMissingQuestions.slice(0, 40);
    const promptText = `Please act as an expert teacher. For each of the following ${missingList.length} objective questions, write a clear, concise, step-by-step pedagogical explanation/solution.

RETURN YOUR RESPONSE AS A VALID JSON OBJECT mapping each questionCode to its solution string.

Example JSON output format:
{
  "QCODE_1": "• Correct Choice: (B) Option Text\\n• Step-by-Step Explanation: Step 1...",
  "QCODE_2": "..."
}

Here are the questions:
${JSON.stringify(missingList, null, 2)}`;

    navigator.clipboard.writeText(promptText);
    alert(`📋 Copied AI Prompt for ${missingList.length} missing questions to clipboard!\n\nPaste it into ChatGPT, Gemini, or Claude, then copy the JSON response and paste it in the box below.`);
    setShowAiPromptBox(true);
  };

  const handleImportAiResponse = async () => {
    if (!pastedAiResponse.trim()) {
      alert('Please paste the AI JSON response first.');
      return;
    }

    let parsedMap: any = null;
    try {
      parsedMap = parseAiSolutionsMap(pastedAiResponse);
      if (!parsedMap || typeof parsedMap !== 'object' || Array.isArray(parsedMap)) {
        throw new Error('Response is not a valid JSON key-value object map');
      }
    } catch (e: any) {
      alert(`⚠️ Invalid JSON format: ${e.message || 'Please ensure you copied valid JSON output from the AI.'}`);
      return;
    }

    setImportingAi(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/questions/audit-explanations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'importAI',
          importedSolutions: parsedMap
        })
      });

      if (!res.ok) throw new Error('Failed to import AI solutions.');
      const resData = await res.json();
      alert(`✅ ${resData.message}`);
      setPastedAiResponse('');
      setShowAiPromptBox(false);
      await handleOpenAuditModal();
      await fetchQuestionsList();
    } catch (err: any) {
      alert(err.message || 'Error importing AI solutions.');
    } finally {
      setImportingAi(false);
    }
  };





  // Open Edit/Add Question Form
  const handleOpenAddQuestion = () => {
    setEditorModal({
      mode: 'add',
      id: '',
      board: 'CBSE',
      classNum: '10',
      subjectName: filterSubject || '',
      chapterNumber: filterChapter || '1',
      topicNumber: filterTopic || '1.1',
      qtype: 'single_mcq',
      text: '',
      options: ['Option A', 'Option B', 'Option C', 'Option D'],
      correctAnswer: 'Option A',
      correctAnswers: [],
      assertion: '',
      reason: '',
      solution: '',
      difficulty: 'medium',
      bloomLevel: 'Remember',
      requiresFigure: false,
      imageUrl: '',
      examCategory: 'standard'
    });
    setShowEditModal(true);
  };

  const handleOpenEditQuestion = (q: Question) => {
    setEditorModal({
      mode: 'edit',
      id: q.questionCode,
      board: q.board,
      classNum: q.class,
      subjectName: q.subject,
      chapterNumber: q.chapterNumber,
      topicNumber: q.topicNumber,
      qtype: q.type,
      text: q.text,
      options: q.options || [],
      correctAnswer: q.correctAnswer || '',
      correctAnswers: q.correctAnswers || [],
      assertion: q.assertion || '',
      reason: q.reason || '',
      solution: q.solution || '',
      difficulty: q.difficulty,
      bloomLevel: q.bloomLevel,
      requiresFigure: !!q.requiresFigure,
      imageUrl: q.imageUrl || '',
      examCategory: q.examCategory || 'standard'
    });
    setShowEditModal(true);
  };

  const handleSaveQuestion = async () => {
    if (!firebaseUser) return;
    setSavingQuestion(true);

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/questions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify(editorModal)
      });

      if (!res.ok) {
        throw new Error('Failed to save question.');
      }
      alert('✅ Question saved successfully!');
      setShowEditModal(false);
      await fetchQuestionsList();
    } catch (err: any) {
      alert(err.message || 'Error occurred saving question.');
    } finally {
      setSavingQuestion(false);
    }
  };

  // Option change helpers
  const handleOptionChange = (idx: number, val: string) => {
    const list = [...editorModal.options];
    list[idx] = val;
    setEditorModal(prev => ({ ...prev, options: list }));
  };

  const handleAddOption = () => {
    setEditorModal(prev => ({ ...prev, options: [...prev.options, `Option ${String.fromCharCode(65 + prev.options.length)}`] }));
  };

  const handleRemoveOption = (idx: number) => {
    setEditorModal(prev => ({ ...prev, options: prev.options.filter((_, i) => i !== idx) }));
  };

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Page Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800, cursor: 'pointer' }} onClick={() => router.push('/admin')}>YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Question Bank Manager</h1>
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Browse and manage available syllabus test items</div>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '8px' }}>
          <button className="btn btn-secondary" onClick={() => triggerDuplicatesScan('filtered')}>🔍 Find Duplicates</button>
          <button className="btn btn-secondary" onClick={handleOpenAuditModal}>⚡ Explanations Audit</button>
          <button className="btn btn-secondary" onClick={handleOpenNumericalAuditModal}>🔢 Audit Numerical</button>
          <button className="btn btn-secondary" onClick={handleOpenDisputesModal} style={{ background: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', borderColor: 'rgba(239, 68, 68, 0.3)' }}>🚩 Reported Issues</button>
          <button className="btn btn-primary" onClick={handleOpenAddQuestion}>+ Add Question</button>
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      {/* Main Content Area */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1100px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>
        
        {/* Cascade Filters card */}
        <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '20px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '15px' }}>
            <h3 style={{ fontSize: '13px', fontWeight: 700, margin: 0 }}>🔍 Search Filters</h3>
            <button className="btn btn-secondary" style={{ padding: '3px 10px', fontSize: '10px' }} onClick={handleResetFilters}>Reset All</button>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(160px, 1fr))', gap: '15px' }}>
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Board</label>
              <select 
                value={filterBoard} 
                onChange={(e) => handleBoardChange(e.target.value)}
                style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                <option value="">-- Choose Board --</option>
                {syllabusIndex && Object.keys(syllabusIndex.subjects || {}).sort().map(b => (
                  <option key={b} value={b}>{boardCodes[b] || b.toUpperCase()}</option>
                ))}
              </select>
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Class</label>
              <select 
                value={filterClass} 
                disabled={!filterBoard}
                onChange={(e) => handleClassChange(e.target.value)}
                style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                <option value="">-- Choose Class --</option>
                {filterBoard && syllabusIndex?.subjects?.[filterBoard] && Object.keys(syllabusIndex.subjects[filterBoard]).sort((a,b)=>parseInt(a)-parseInt(b)).map(c => (
                  <option key={c} value={c}>Class {c}</option>
                ))}
              </select>
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Subject</label>
              <select 
                value={filterSubject} 
                disabled={!filterClass}
                onChange={(e) => handleSubjectChange(e.target.value)}
                style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                <option value="">-- Choose Subject --</option>
                {availableSubjects.map(s => (
                  <option key={s} value={s}>{s}</option>
                ))}
              </select>
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Chapter</label>
              <select 
                value={filterChapter} 
                disabled={availableChapters.length === 0}
                onChange={(e) => handleChapterChange(e.target.value)}
                style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                <option value="">-- Choose Chapter --</option>
                {availableChapters.map((ch, idx) => (
                  <option key={idx} value={ch.number}>Ch.{ch.number}: {ch.name}</option>
                ))}
              </select>
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Topic</label>
              <select 
                value={filterTopic} 
                disabled={availableTopics.length === 0}
                onChange={(e) => handleTopicChange(e.target.value)}
                style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                <option value="">-- Choose Topic --</option>
                {availableTopics.map((top, idx) => (
                  <option key={idx} value={top.number}>
                    {top.isSubtopic ? `\u00A0\u00A0• ${top.number} ${top.name}` : `${top.number} ${top.name}`}
                  </option>
                ))}
              </select>
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Category</label>
              <select 
                value={filterCategory} 
                onChange={(e) => handleCategoryChange(e.target.value)}
                style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                <option value="">-- All Categories --</option>
                <option value="objective">Objective</option>
                <option value="subjective">Subjective</option>
              </select>
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Type</label>
              <select 
                value={filterType} 
                disabled={!filterCategory}
                onChange={(e) => setFilterType(e.target.value)}
                style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                {!filterCategory ? (
                  <option value="">-- Choose Category First --</option>
                ) : (
                  <>
                    <option value="">-- All Types --</option>
                    {filterCategory === 'objective' ? (
                      <>
                        <option value="single_mcq">Single MCQ (OSC)</option>
                        <option value="multiple_mcq">Multiple MCQ (OMC)</option>
                        <option value="true_false">True / False (OTF)</option>
                        <option value="assertion_reason">Assertion Reason (OAR)</option>
                        <option value="fill_blanks">Fill in Blanks (OFB)</option>
                        <option value="numerical">Numerical Entry (ONE)</option>
                      </>
                    ) : (
                      <>
                        <option value="subjective_short">Subjective Short (SSA - 2M)</option>
                        <option value="subjective_long">Subjective Long (SLA - 4M)</option>
                        <option value="subjective_reason">Subjective Reason (SSR - 2M)</option>
                        <option value="subjective_notes">Subjective Notes (SSR - 2M)</option>
                        <option value="subjective_define">Subjective Define (SDF - 1M)</option>
                        <option value="subjective_laws">Subjective Laws (SLP - 1M)</option>
                        <option value="numerical_short">Numerical Short (SSN - 2M)</option>
                        <option value="numerical_long">Numerical Long (SLN - 4M)</option>
                      </>
                    )}
                  </>
                )}
              </select>
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Usage</label>
              <select 
                value={filterUsage} 
                onChange={(e) => setFilterUsage(e.target.value)}
                style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                <option value="all">-- All Statuses --</option>
                <option value="used">Used in Exams</option>
                <option value="unused">Unused in Exams</option>
              </select>
            </div>
          </div>
        </div>

        {/* Questions browse table card */}
        <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
          <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '15px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <input 
                type="checkbox" 
                checked={selectedCodes.size === questions.length && questions.length > 0} 
                onChange={handleToggleSelectAll} 
              />
              <span style={{ fontSize: '12px', fontWeight: 600 }}>Select All</span>
              <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>({selectedCodes.size} selected)</span>
              {selectedCodes.size > 0 && (
                <button className="btn btn-secondary" style={{ color: 'var(--danger)', padding: '3px 10px', fontSize: '11px' }} onClick={handleBulkDelete}>
                  🗑️ Delete Selected
                </button>
              )}
            </div>
            
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Total: <strong>{totalCount}</strong> questions</span>
              <select 
                value={itemsPerPage} 
                onChange={(e) => { setItemsPerPage(parseInt(e.target.value)); setCurrentPage(1); setLastCodesHistory(['']); }}
                style={{ padding: '4px 8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', fontSize: '11px' }}
              >
                <option value="10">10 per page</option>
                <option value="20">20 per page</option>
                <option value="50">50 per page</option>
              </select>
            </div>
          </div>

          {loading ? (
            <div style={{ padding: '40px', textAlign: 'center' }}>
              <div className="spinner" style={{ margin: '0 auto 10px' }}></div>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Loading question bank records...</span>
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column' }}>
              {questions.length === 0 ? (
                <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>
                  {(!filterBoard || !filterClass || !filterSubject)
                    ? 'ℹ️ Please select Board, Class, and Subject in the filters above to load and display questions.' 
                    : 'No questions match selected filter queries.'}
                </div>
              ) : (
                questions.map((q, idx) => (
                  <div key={q.questionCode} style={{ padding: '15px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', alignItems: 'flex-start', gap: '15px' }}>
                    <input 
                      type="checkbox" 
                      checked={selectedCodes.has(q.questionCode)} 
                      onChange={() => handleToggleSelectQuestion(q.questionCode)} 
                      style={{ marginTop: '4px' }}
                    />
                    <div style={{ flex: 1 }}>
                      <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', alignItems: 'center', marginBottom: '6px' }}>
                        <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--accent)' }}>{q.questionCode}</span>
                        <span className="badge badge-info" style={{ fontSize: '10px' }}>{q.type}</span>
                        <span className="badge" style={{ fontSize: '10px', background: 'var(--bg-soft)', color: 'var(--text)' }}>{q.difficulty}</span>
                        {q.usedInClassroomTest ? (
                          <span className="badge" style={{ fontSize: '10px', background: 'rgba(107, 70, 193, 0.1)', color: 'var(--accent)', fontWeight: 700 }}>Used</span>
                        ) : (
                          <span className="badge" style={{ fontSize: '10px', background: 'rgba(16, 185, 129, 0.1)', color: 'var(--success)', fontWeight: 700 }}>Unused</span>
                        )}
                        <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Class {q.class} • Ch.{q.chapterNumber} • {q.subject}</span>
                      </div>
                      
                      <div 
                        className="math-container" 
                        style={{ fontSize: '13px', fontWeight: 600, lineHeight: 1.5, marginBottom: '8px' }}
                        dangerouslySetInnerHTML={{ __html: `${preprocessMathText(q.text)}${q.questionCode ? ` (${q.questionCode})` : ''}` }}
                      />

                      {q.imageUrl && (
                        <div style={{ margin: '8px 0' }}>
                          <Image src={q.imageUrl} alt="Question figure" width={200} height={150} style={{ objectFit: 'contain', borderRadius: '4px', border: '1px solid var(--border-light)' }} />
                        </div>
                      )}

                      {/* Render Options if MCQ */}
                      {q.options && q.options.length > 0 && (
                        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '8px' }}>
                          {q.options.map((opt, oi) => (
                            <div key={oi} style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
                              <span>{String.fromCharCode(65 + oi)}.</span> 
                              <span className="math-container" dangerouslySetInnerHTML={{ __html: preprocessMathText(opt) }} />
                            </div>
                          ))}
                        </div>
                      )}

                      {/* Correct Answers */}
                      {q.correctAnswer && (
                        <div style={{ fontSize: '10px', color: 'var(--success)', fontWeight: 600, marginBottom: '5px' }}>
                           ✓ Correct Answer: <span className="math-container" dangerouslySetInnerHTML={{ __html: preprocessMathText(q.correctAnswer) }} />
                        </div>
                      )}
                      {q.correctAnswers && q.correctAnswers.length > 0 && (
                        <div style={{ fontSize: '10px', color: 'var(--success)', fontWeight: 600, marginBottom: '5px' }}>
                          ✓ Correct Answers: {q.correctAnswers.join(', ')}
                        </div>
                      )}

                      {q.solution && (
                        <div style={{ fontSize: '10px', color: 'var(--text-muted)', background: 'var(--bg-soft)', padding: '6px', borderRadius: '4px', border: '1px solid var(--border-light)' }}>
                           <strong>Explanation:</strong> <span className="math-container" dangerouslySetInnerHTML={{ __html: preprocessMathText(q.solution) }} />
                        </div>
                      )}
                    </div>

                    <div style={{ display: 'flex', gap: '6px', flexShrink: 0 }}>
                      <button className="btn btn-secondary" style={{ padding: '3px 8px', fontSize: '11px' }} onClick={() => handleOpenEditQuestion(q)}>✏️ Edit</button>
                      <button className="btn btn-secondary" style={{ padding: '3px 8px', fontSize: '11px', color: 'var(--danger)' }} onClick={() => handleDeleteQuestion(q.questionCode)}>🗑️ Delete</button>
                    </div>
                  </div>
                ))
              )}
            </div>
          )}

          {/* Pagination */}
          <div style={{ padding: '12px 20px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <button className="btn btn-secondary" style={{ padding: '4px 12px', fontSize: '12px' }} onClick={handlePrevPage} disabled={currentPage === 1}>
              ← Previous
            </button>
            <span style={{ fontSize: '12px' }}>Page {currentPage}</span>
            <button className="btn btn-secondary" style={{ padding: '4px 12px', fontSize: '12px' }} onClick={handleNextPage} disabled={questions.length < itemsPerPage}>
              Next →
            </button>
          </div>
        </div>

      </main>

      {/* Modal: Duplicates Finder view */}
      {showDuplicatesModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.8)', zIndex: 35000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', maxWidth: '800px', width: '90%', minHeight: '300px', maxHeight: '90vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-light)', boxShadow: '0 8px 32px rgba(0,0,0,0.6)', overflow: 'hidden' }}>
            <div style={{ padding: '16px 24px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0 }}>🔍 Scan Duplicate Questions</h3>
                <div style={{ display: 'flex', background: 'var(--bg-soft)', borderRadius: '20px', padding: '2px', border: '1px solid var(--border-light)' }}>
                  <button
                    type="button"
                    onClick={() => triggerDuplicatesScan('filtered')}
                    style={{
                      padding: '3px 10px',
                      fontSize: '11px',
                      fontWeight: 600,
                      borderRadius: '16px',
                      border: 'none',
                      background: duplicateScanScope === 'filtered' ? 'var(--accent)' : 'transparent',
                      color: duplicateScanScope === 'filtered' ? '#ffffff' : 'var(--text-muted)',
                      cursor: 'pointer'
                    }}
                  >
                    🎯 {filterBoard || filterClass || filterSubject ? `${filterBoard ? filterBoard.replace('Maharashtra Board', 'MH') : ''} ${filterClass ? `Cl.${filterClass}` : ''} ${filterSubject || ''}`.trim() : 'Filtered View'}
                  </button>
                  <button
                    type="button"
                    onClick={() => triggerDuplicatesScan('all')}
                    style={{
                      padding: '3px 10px',
                      fontSize: '11px',
                      fontWeight: 600,
                      borderRadius: '16px',
                      border: 'none',
                      background: duplicateScanScope === 'all' ? 'var(--accent)' : 'transparent',
                      color: duplicateScanScope === 'all' ? '#ffffff' : 'var(--text-muted)',
                      cursor: 'pointer'
                    }}
                  >
                    🌐 All Database
                  </button>
                </div>
              </div>
              <button className="btn btn-secondary" style={{ padding: '2px 8px', fontSize: '10px' }} onClick={() => setShowDuplicatesModal(false)}>✕</button>
            </div>

            <div style={{ padding: '10px 16px', borderBottom: '1px solid var(--border-light)', display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
              <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={handleSelectAllDuplicates} disabled={duplicateGroups.length === 0}>Select Duplicates to Purge</button>
              <button className="btn btn-secondary" style={{ padding: '4px 10px', fontSize: '11px' }} onClick={() => setSelectedDups(new Set())} disabled={duplicateGroups.length === 0}>Deselect All</button>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)', marginLeft: '6px' }}>
                ({duplicateGroups.length} duplicate group{duplicateGroups.length === 1 ? '' : 's'} found • {selectedDups.size} selected for purge)
              </span>
              {selectedDups.size > 0 && (
                <button className="btn btn-primary" style={{ background: 'var(--danger)', borderColor: 'var(--danger)', padding: '4px 10px', fontSize: '11px', marginLeft: 'auto' }} onClick={handleDeleteSelectedDuplicates}>
                  🗑️ Purge {selectedDups.size} Selected
                </button>
              )}
            </div>

            <div style={{ flex: 1, overflowY: 'auto', padding: '20px' }}>
              {scanningDuplicates ? (
                <div style={{ padding: '30px', textAlign: 'center' }}>
                  <div className="spinner" style={{ margin: '0 auto 10px' }}></div>
                  <span style={{ fontSize: '12px' }}>Scanning question bank files...</span>
                </div>
              ) : duplicateGroups.length === 0 ? (
                <div style={{ textAlign: 'center', padding: '30px', color: 'var(--text-muted)', fontSize: '13px' }}>
                  🎉 No duplicate question texts found in database!
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                  {duplicateGroups.map((g, gi) => (
                    <div key={gi} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--bg-soft)', overflow: 'hidden' }}>
                      <div style={{ padding: '8px 12px', background: 'var(--surface)', borderBottom: '1px solid var(--border-light)', fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)' }}>
                        Group {gi + 1} • {g.questions.length} identical questions
                      </div>
                      <div style={{ padding: '12px' }}>
                        <div className="math-container" style={{ fontSize: '13px', fontWeight: 600, marginBottom: '8px' }}>{g.questions[0].text}{g.questions[0].questionCode ? ` (${g.questions[0].questionCode})` : ''}</div>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                          {g.questions.map((q: any, qi: number) => {
                            const isSelected = selectedDups.has(q.questionCode);
                            return (
                              <label key={q.questionCode} style={{ display: 'flex', alignItems: 'center', gap: '10px', background: qi === 0 ? 'rgba(76,175,80,0.06)' : 'var(--surface)', border: '1px solid var(--border-light)', padding: '6px 12px', borderRadius: '4px', fontSize: '11px', cursor: 'pointer' }}>
                                {qi > 0 ? (
                                  <input 
                                    type="checkbox" 
                                    checked={isSelected} 
                                    onChange={() => handleToggleSelectDup(q.questionCode)} 
                                  />
                                ) : (
                                  <span style={{ fontSize: '9px', fontWeight: 700, color: 'var(--success)' }}>KEEP</span>
                                )}
                                <span>{q.questionCode} ({q.difficulty}) • Used {q.timesUsed || 0} times</span>
                              </label>
                            );
                          })}
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Modal: Add/Edit/Fulfill Question editor */}
      {showEditModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.8)', zIndex: 1000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', maxWidth: '650px', width: '90%', maxHeight: '90vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-light)' }}>
            <div style={{ padding: '16px 24px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ fontSize: '14px', fontWeight: 800, margin: 0 }}>
                {editorModal.mode === 'add' ? 'Create Question' : `Edit Question ${editorModal.id}`}
              </h3>
              <button className="btn btn-secondary" style={{ padding: '2px 8px', fontSize: '10px' }} onClick={() => setShowEditModal(false)}>✕</button>
            </div>

            <div style={{ flex: 1, overflowY: 'auto', padding: '20px', display: 'flex', flexDirection: 'column', gap: '15px' }}>
              
              {/* Board / Class / Subject Name selections */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '8px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Board</label>
                  <input 
                    type="text" 
                    value={editorModal.board} 
                    onChange={(e) => setEditorModal(prev => ({ ...prev, board: e.target.value }))}
                    style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Class</label>
                  <input 
                    type="text" 
                    value={editorModal.classNum} 
                    onChange={(e) => setEditorModal(prev => ({ ...prev, classNum: e.target.value }))}
                    style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Subject Name</label>
                  <input 
                    type="text" 
                    value={editorModal.subjectName} 
                    onChange={(e) => setEditorModal(prev => ({ ...prev, subjectName: e.target.value }))}
                    style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                  />
                </div>
              </div>

              {/* Chapter & Topic Number details */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Chapter Number</label>
                  <input 
                    type="text" 
                    value={editorModal.chapterNumber} 
                    onChange={(e) => setEditorModal(prev => ({ ...prev, chapterNumber: e.target.value }))}
                    style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Topic Number</label>
                  <input 
                    type="text" 
                    value={editorModal.topicNumber} 
                    onChange={(e) => setEditorModal(prev => ({ ...prev, topicNumber: e.target.value }))}
                    style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                  />
                </div>
              </div>

              {/* Type, difficulty, bloom level */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '8px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Question Type</label>
                  <select 
                    value={editorModal.qtype} 
                    onChange={(e) => setEditorModal(prev => ({ ...prev, qtype: e.target.value }))}
                    style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                  >
                    <option value="single_mcq">Single MCQ (OSC)</option>
                    <option value="multiple_mcq">Multiple MCQ (OMC)</option>
                    <option value="true_false">True / False (OTF)</option>
                    <option value="assertion_reason">Assertion Reason (OAR)</option>
                    <option value="fill_blanks">Fill in Blanks (OFB)</option>
                    <option value="numerical">Numerical Entry (ONE)</option>
                    <option value="subjective_short">Subjective Short (SSA - 2M)</option>
                    <option value="subjective_long">Subjective Long (SLA - 4M)</option>
                    <option value="subjective_reason">Subjective Reason (SSR - 2M)</option>
                    <option value="subjective_notes">Subjective Notes (SSR - 2M)</option>
                    <option value="subjective_define">Subjective Define (SDF - 1M)</option>
                    <option value="subjective_laws">Subjective Laws (SLP - 1M)</option>
                    <option value="numerical_short">Numerical Short (SSN - 2M)</option>
                    <option value="numerical_long">Numerical Long (SLN - 4M)</option>
                  </select>
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Difficulty</label>
                  <select 
                    value={editorModal.difficulty} 
                    onChange={(e) => setEditorModal(prev => ({ ...prev, difficulty: e.target.value }))}
                    style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                  >
                    <option value="easy">Easy</option>
                    <option value="medium">Medium</option>
                    <option value="hard">Hard</option>
                  </select>
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Category</label>
                  <select 
                    value={(editorModal as any).examCategory || 'standard'} 
                    onChange={(e) => setEditorModal(prev => ({ ...prev, examCategory: e.target.value }))}
                    style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                  >
                    <option value="standard">Standard</option>
                    <option value="foundation">Foundation</option>
                  </select>
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Bloom Level</label>
                  <select 
                    value={editorModal.bloomLevel} 
                    onChange={(e) => setEditorModal(prev => ({ ...prev, bloomLevel: e.target.value }))}
                    style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                  >
                    <option value="Remember">Remember</option>
                    <option value="Understand">Understand</option>
                    <option value="Apply">Apply</option>
                    <option value="Analyze">Analyze</option>
                    <option value="Evaluate">Evaluate</option>
                    <option value="Create">Create</option>
                  </select>
                </div>
              </div>

              {/* Question Text */}
              <div>
                <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Question Text (support LaTeX $ ... $)</label>
                <textarea 
                  value={editorModal.text} 
                  onChange={(e) => setEditorModal(prev => ({ ...prev, text: e.target.value }))}
                  placeholder="Enter question text here..."
                  style={{ width: '100%', height: '70px', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                />
              </div>
              
              {/* Optional Figure/Diagram Image Upload */}
              <div style={{ marginTop: '10px', background: 'var(--bg-soft)', padding: '10px', borderRadius: '6px', border: '1px dashed var(--border-light)' }}>
                <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '11px', fontWeight: 'bold', color: 'var(--text)', cursor: 'pointer' }}>
                  <input 
                    type="checkbox" 
                    checked={!!editorModal.requiresFigure} 
                    onChange={(e) => setEditorModal(prev => ({ ...prev, requiresFigure: e.target.checked }))}
                  />
                  📸 Requires Figure / Diagram
                </label>
                {editorModal.requiresFigure && (
                  <div style={{ marginTop: '8px' }}>
                    <input 
                      type="file" 
                      accept="image/*" 
                      onChange={(e) => {
                        const file = e.target.files?.[0];
                        if (!file) return;
                        const reader = new FileReader();
                        reader.onload = (event) => {
                          setEditorModal(prev => ({ ...prev, imageUrl: event.target?.result as string }));
                        };
                        reader.readAsDataURL(file);
                      }}
                      style={{ fontSize: '11px' }}
                    />
                    {editorModal.imageUrl && (
                      <div style={{ marginTop: '6px' }}>
                        <Image src={editorModal.imageUrl} alt="Figure preview" width={120} height={90} style={{ objectFit: 'contain', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }} />
                      </div>
                    )}
                  </div>
                )}
              </div>

              {/* Options lists if MCQ */}
              {(editorModal.qtype === 'single_mcq' || editorModal.qtype === 'multiple_mcq') && (
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                    <label style={{ fontSize: '11px', color: 'var(--text-muted)', margin: 0 }}>Options List</label>
                    <button className="btn btn-secondary" style={{ padding: '2px 8px', fontSize: '10px' }} onClick={handleAddOption}>+ Add Option</button>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                    {editorModal.options.map((opt, oIdx) => (
                      <div key={oIdx} style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                        <span style={{ fontSize: '11px', fontWeight: 600 }}>{String.fromCharCode(65 + oIdx)}.</span>
                        <input 
                          type="text" 
                          value={opt} 
                          onChange={(e) => handleOptionChange(oIdx, e.target.value)}
                          style={{ flex: 1, padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                        />
                        {editorModal.options.length > 2 && (
                          <button className="btn btn-secondary" style={{ color: 'var(--danger)', padding: '4px' }} onClick={() => handleRemoveOption(oIdx)}>✕</button>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Assertion & Reason details */}
              {editorModal.qtype === 'assertion_reason' && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Assertion</label>
                    <textarea 
                      value={editorModal.assertion} 
                      onChange={(e) => setEditorModal(prev => ({ ...prev, assertion: e.target.value }))}
                      style={{ width: '100%', height: '50px', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                    />
                  </div>
                  <div>
                    <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Reason</label>
                    <textarea 
                      value={editorModal.reason} 
                      onChange={(e) => setEditorModal(prev => ({ ...prev, reason: e.target.value }))}
                      style={{ width: '100%', height: '50px', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                    />
                  </div>
                </div>
              )}

              {/* Correct answers */}
              {editorModal.qtype !== 'multiple_mcq' ? (
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Correct Answer (Option text value verbatim, or A/B/C/D letter)</label>
                  <input 
                    type="text" 
                    value={editorModal.correctAnswer} 
                    onChange={(e) => setEditorModal(prev => ({ ...prev, correctAnswer: e.target.value }))}
                    style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                  />
                </div>
              ) : (
                <div>
                  <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Correct Answers (comma separated verbatim values)</label>
                  <input 
                    type="text" 
                    value={editorModal.correctAnswers.join(', ')} 
                    onChange={(e) => setEditorModal(prev => ({ ...prev, correctAnswers: e.target.value.split(',').map(s=>s.trim()) }))}
                    style={{ width: '100%', padding: '6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                  />
                </div>
              )}

              {/* Solution/Explanation */}
              <div>
                <label style={{ display: 'block', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '5px' }}>Solution Explanation *</label>
                <textarea 
                  value={editorModal.solution} 
                  onChange={(e) => setEditorModal(prev => ({ ...prev, solution: e.target.value }))}
                  placeholder="Provide concise explanation of why the correct answer is correct"
                  style={{ width: '100%', height: '60px', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                />
              </div>

            </div>

            <div style={{ padding: '16px 24px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end', gap: '10px', flexShrink: 0 }}>
              <button className="btn btn-secondary" onClick={() => setShowEditModal(false)}>Cancel</button>
              <button className="btn btn-primary" onClick={handleSaveQuestion} disabled={savingQuestion}>
                {savingQuestion ? 'Saving...' : 'Save Question'}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Explanation Audit & Generator Modal */}
      {showAuditModal && (
        <div className="modal-overlay" style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.65)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 99999, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div className="modal-card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', borderRadius: 'var(--radius-lg)', maxWidth: '640px', width: '100%', maxHeight: '90vh', display: 'flex', flexDirection: 'column', overflow: 'hidden', boxShadow: 'var(--shadow-lg)' }}>
            <div style={{ padding: '20px 24px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexShrink: 0 }}>
              <div>
                <h2 style={{ fontSize: '1.25rem', fontWeight: 800, margin: 0, color: 'var(--text)' }}>⚡ Question Bank Explanations Audit</h2>
                <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', marginTop: '2px' }}>Audit and auto-generate step-by-step solutions for objective practice items</div>
              </div>
              <button onClick={() => setShowAuditModal(false)} style={{ background: 'none', border: 'none', fontSize: '20px', cursor: 'pointer', color: 'var(--text-muted)' }}>✕</button>
            </div>

            <div style={{ padding: '20px 24px', overflowY: 'auto', flex: 1, display: 'flex', flexDirection: 'column', gap: '16px' }}>
              {auditLoading ? (
                <div style={{ textAlign: 'center', padding: '30px 0', color: 'var(--text-muted)' }}>
                  <div className="spinner" style={{ margin: '0 auto 12px auto' }}></div>
                  Auditing question bank solutions...
                </div>
              ) : auditStats ? (
                <>
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '12px', textAlign: 'center' }}>
                    <div style={{ padding: '14px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                      <div style={{ fontSize: '22px', fontWeight: 800, color: 'var(--text)' }}>{auditStats.totalObjective}</div>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Total Objective Qs</div>
                    </div>
                    <div style={{ padding: '14px', background: 'rgba(16, 185, 129, 0.08)', borderRadius: 'var(--radius-md)', border: '1px solid rgba(16, 185, 129, 0.2)' }}>
                      <div style={{ fontSize: '22px', fontWeight: 800, color: 'var(--success)' }}>{auditStats.withSolution}</div>
                      <div style={{ fontSize: '11px', color: 'var(--success)' }}>With Explanations ({auditStats.coveragePercent}%)</div>
                    </div>
                    <div style={{ padding: '14px', background: 'rgba(239, 68, 68, 0.08)', borderRadius: 'var(--radius-md)', border: '1px solid rgba(239, 68, 68, 0.2)' }}>
                      <div style={{ fontSize: '22px', fontWeight: 800, color: 'var(--danger)' }}>{auditStats.missingSolution}</div>
                      <div style={{ fontSize: '11px', color: 'var(--danger)' }}>Missing Solution</div>
                    </div>
                  </div>

                  {auditStats.missingSolution > 0 ? (
                    <div style={{ background: 'var(--bg-soft)', padding: '14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                      <h4 style={{ margin: '0 0 8px 0', fontSize: '13px', fontWeight: 700, color: 'var(--text)' }}>
                        ⚠️ Sample Questions Lacking Explanations ({auditStats.sampleMissing?.length || 0} shown):
                      </h4>
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', maxHeight: '180px', overflowY: 'auto' }}>
                        {auditStats.sampleMissing?.map((s: any) => (
                          <div key={s.id} style={{ fontSize: '11.5px', padding: '6px 10px', background: 'var(--surface)', borderRadius: '4px', border: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', gap: '10px' }}>
                            <span style={{ fontWeight: 600, color: 'var(--accent)' }}>[{s.questionCode}]</span>
                            <span style={{ flex: 1, textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>{s.text}</span>
                            <span style={{ fontSize: '9px', background: 'var(--bg-soft)', padding: '1px 5px', borderRadius: '3px' }}>{s.type}</span>
                          </div>
                        ))}
                      </div>
                    </div>
                  ) : (
                    <div className="alert-box alert-box-success" style={{ display: 'block', margin: 0, textAlign: 'center' }}>
                      🎉 Excellent! 100% of objective questions in the Question Bank have explanations/solutions attached.
                    </div>
                  )}

                  <div style={{ borderTop: '1px solid var(--border-light)', paddingTop: '14px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
                    <div style={{ display: 'flex', gap: '8px' }}>
                      <button 
                        className="btn btn-primary"
                        onClick={handleCopyAiPrompt}
                        disabled={auditStats.missingSolution === 0}
                        style={{ flex: 1, padding: '10px', fontWeight: 700, fontSize: '13px' }}
                      >
                        📋 Copy External AI Prompt (ChatGPT/Gemini)
                      </button>
                      <button 
                        className="btn btn-secondary"
                        onClick={() => setShowAiPromptBox(!showAiPromptBox)}
                        style={{ padding: '10px', fontWeight: 700, fontSize: '13px' }}
                      >
                        📥 {showAiPromptBox ? 'Hide Paste Box' : 'Paste AI Response'}
                      </button>
                    </div>

                    {showAiPromptBox && (
                      <div style={{ background: 'var(--bg-soft)', padding: '12px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                        <label style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text)' }}>
                          Paste AI JSON Response (mapping questionCode to solution text):
                        </label>
                        <textarea 
                          rows={6}
                          placeholder='{\n  "QCODE_1": "• Correct Choice: (B)...\\n• Step-by-Step Explanation:...",\n  "QCODE_2": "..."\n}'
                          value={pastedAiResponse}
                          onChange={(e) => setPastedAiResponse(e.target.value)}
                          style={{ width: '100%', padding: '8px', fontSize: '11.5px', fontFamily: 'monospace', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)' }}
                        />
                        <button 
                          className="btn btn-success"
                          onClick={handleImportAiResponse}
                          disabled={importingAi || !pastedAiResponse.trim()}
                          style={{ width: '100%', padding: '8px', fontWeight: 700, fontSize: '12px' }}
                        >
                          {importingAi ? 'Importing Solutions...' : '⚡ Import & Save AI Solutions into Question Bank'}
                        </button>
                      </div>
                    )}

                    <div style={{ display: 'flex', gap: '8px', borderTop: '1px dashed var(--border-light)', paddingTop: '10px' }}>
                      <button 
                        className="btn btn-secondary btn-sm"
                        onClick={() => handleRunGenerateExplanations(false)}
                        disabled={auditGenerating || auditStats.missingSolution === 0}
                        style={{ flex: 1, fontSize: '11px' }}
                      >
                        {auditGenerating ? 'Generating...' : `⚡ Auto-Generate Internally (${auditStats.missingSolution} missing)`}
                      </button>
                      <button 
                        className="btn btn-secondary btn-sm"
                        onClick={() => handleRunGenerateExplanations(true)}
                        disabled={auditGenerating}
                        style={{ flex: 1, fontSize: '11px' }}
                      >
                        🔄 Force Regenerate All
                      </button>
                    </div>
                  </div>
                </>
              ) : null}
            </div>

            <div style={{ padding: '14px 24px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end', background: 'var(--bg-soft)' }}>
              <button className="btn btn-secondary" onClick={() => setShowAuditModal(false)}>Close Audit Window</button>
            </div>
          </div>
        </div>
      )}

      {/* Modal: Audit & Migrate Numerical Questions */}
      {showNumericalAuditModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.85)', zIndex: 30000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', maxWidth: '750px', width: '92%', maxHeight: '85vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800, color: 'var(--accent)' }}>🔢 Numerical Questions Audit & Migration</h3>
              <button className="btn btn-secondary btn-sm" onClick={() => setShowNumericalAuditModal(false)}>✕</button>
            </div>

            <div style={{ padding: '20px', overflowY: 'auto', flex: 1, display: 'flex', flexDirection: 'column', gap: '16px' }}>
              {auditingNumerical ? (
                <div style={{ textAlign: 'center', padding: '40px', color: 'var(--text-muted)' }}>
                  ⏳ Auditing non-numerical marked objective questions...
                </div>
              ) : (
                <>
                  <div style={{ background: 'var(--badge-bg)', border: '1px solid var(--badge-border)', padding: '12px 16px', borderRadius: 'var(--radius)', fontSize: '12.5px', color: 'var(--text)' }}>
                    <strong>Audit Summary:</strong> Found <strong>{numericalCandidates.length}</strong> non-numerical marked objective questions that have numeric answers or numerical problem formulations and should be re-classified under the <code>numerical</code> type.
                  </div>

                  {numericalCandidates.length > 0 ? (
                    <div style={{ overflowX: 'auto', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)' }}>
                      <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px', textAlign: 'left' }}>
                        <thead>
                          <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)' }}>
                            <th style={{ padding: '8px 12px' }}>Question Code</th>
                            <th style={{ padding: '8px 12px' }}>Current Type</th>
                            <th style={{ padding: '8px 12px' }}>Text Preview</th>
                            <th style={{ padding: '8px 12px' }}>Correct Answer</th>
                          </tr>
                        </thead>
                        <tbody>
                          {numericalCandidates.slice(0, 50).map((c, idx) => (
                            <tr key={c.id || idx} style={{ borderBottom: '1px solid var(--border-light)' }}>
                              <td style={{ padding: '8px 12px', fontFamily: 'monospace', fontWeight: 600 }}>{c.questionCode}</td>
                              <td style={{ padding: '8px 12px', color: '#d97706', fontWeight: 700 }}>{c.type}</td>
                              <td style={{ padding: '8px 12px', maxWidth: '300px', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{c.text}</td>
                              <td style={{ padding: '8px 12px', fontWeight: 700, color: '#1aa54e' }}>{c.correctAnswer}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  ) : (
                    <div style={{ textAlign: 'center', padding: '24px', color: '#1aa54e', fontWeight: 700 }}>
                      🎉 All non-numerical marked questions are clean! No unclassified numerical questions found.
                    </div>
                  )}
                </>
              )}
            </div>

            <div style={{ padding: '14px 20px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)' }}>
              <button className="btn btn-secondary" onClick={() => setShowNumericalAuditModal(false)}>Close</button>
              {numericalCandidates.length > 0 && (
                <button 
                  className="btn btn-primary"
                  disabled={auditingNumerical}
                  onClick={handleMigrateNumericalQuestions}
                >
                  {auditingNumerical ? 'Migrating...' : `⚡ Convert & Migrate ${numericalCandidates.length} Questions to 'numerical'`}
                </button>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Modal: Reported Questions / Disputes Queue */}
      {showDisputesModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.85)', zIndex: 30000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', maxWidth: '950px', width: '95%', maxHeight: '88vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 800, color: '#ef4444' }}>🚩 Student Reported Questions &amp; Proof Queue</h3>
                <span className="badge badge-danger" style={{ fontSize: '11px' }}>{disputesList.filter(d => d.status === 'pending').length} Pending</span>
              </div>
              <button className="btn btn-secondary btn-sm" onClick={() => setShowDisputesModal(false)}>✕</button>
            </div>

            <div style={{ padding: '20px', overflowY: 'auto', flex: 1, display: 'flex', flexDirection: 'column', gap: '16px' }}>
              {loadingDisputes ? (
                <div style={{ textAlign: 'center', padding: '40px', color: 'var(--text-muted)' }}>
                  ⏳ Loading dispute reports...
                </div>
              ) : disputesList.length === 0 ? (
                <div style={{ textAlign: 'center', padding: '40px', color: 'var(--text-muted)' }}>
                  🎉 No reported question issues found! Everything is in order.
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
                  {disputesList.map((disp: any) => (
                    <div 
                      key={disp.id}
                      style={{
                        background: 'var(--bg-soft)',
                        border: `1px solid ${disp.status === 'approved' ? '#10b981' : disp.status === 'rejected' ? 'var(--border-light)' : '#ef4444'}`,
                        borderRadius: 'var(--radius)',
                        padding: '16px',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '10px'
                      }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '8px' }}>
                        <div>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
                            <span style={{ fontFamily: 'monospace', fontWeight: 700, fontSize: '13px', color: 'var(--accent)' }}>
                              {disp.questionCode || disp.questionId}
                            </span>
                            <span className={`badge ${disp.status === 'pending' ? 'badge-danger' : disp.status === 'approved' ? 'badge-success' : 'badge-secondary'}`}>
                              {disp.status.toUpperCase()}
                            </span>
                            <span className="badge badge-secondary" style={{ fontSize: '10.5px' }}>
                              Source: {disp.source}
                            </span>
                          </div>
                          <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                            Reported by <strong>{disp.studentName}</strong> ({disp.class || ''}) on {disp.createdAt ? new Date(disp.createdAt).toLocaleString() : 'N/A'}
                          </div>
                        </div>

                        <div style={{ display: 'flex', gap: '8px' }}>
                          {disp.screenshotData && (
                            <button 
                              className="btn btn-secondary btn-sm"
                              onClick={() => setSelectedDisputeScreenshot(disp.screenshotData)}
                              style={{ display: 'flex', alignItems: 'center', gap: '4px' }}
                            >
                              📷 View Proof Screenshot
                            </button>
                          )}
                          {disp.status === 'pending' && (
                            <>
                              <button 
                                className="btn btn-primary btn-sm"
                                style={{ background: '#ef4444', borderColor: '#ef4444' }}
                                onClick={() => handleResolveDispute(disp.id, 'approve')}
                              >
                                🛡️ Approve &amp; Quarantine Question
                              </button>
                              <button 
                                className="btn btn-secondary btn-sm"
                                onClick={() => handleResolveDispute(disp.id, 'reject')}
                              >
                                ✕ Dismiss
                              </button>
                            </>
                          )}
                        </div>
                      </div>

                      <div style={{ background: 'var(--surface)', padding: '10px 14px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', fontSize: '12.5px' }}>
                        <div style={{ color: '#ef4444', fontWeight: 700, marginBottom: '4px' }}>
                          Reason: {disp.reason ? disp.reason.replace(/_/g, ' ').toUpperCase() : 'DEFECTIVE QUESTION'}
                        </div>
                        {disp.notes && (
                          <div style={{ color: 'var(--text)', fontStyle: 'italic', marginBottom: '6px' }}>
                            Student Note: "{disp.notes}"
                          </div>
                        )}
                        {disp.questionText && (
                          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginTop: '6px', borderTop: '1px dashed var(--border-light)', paddingTop: '6px' }}>
                            Question: {disp.questionText}
                          </div>
                        )}
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>

            <div style={{ padding: '14px 20px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end', background: 'var(--bg-soft)' }}>
              <button className="btn btn-secondary" onClick={() => setShowDisputesModal(false)}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* Screenshot Lightbox Modal */}
      {selectedDisputeScreenshot && (
        <div 
          style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.92)', zIndex: 35000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}
          onClick={() => setSelectedDisputeScreenshot(null)}
        >
          <div style={{ position: 'relative', maxWidth: '800px', width: '100%', maxHeight: '90vh', background: '#171a1f', borderRadius: '12px', overflow: 'hidden', border: '1px solid rgba(255,255,255,0.2)', display: 'flex', flexDirection: 'column' }} onClick={(e) => e.stopPropagation()}>
            <div style={{ padding: '12px 16px', background: '#222730', borderBottom: '1px solid rgba(255,255,255,0.1)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span style={{ color: '#fff', fontSize: '13px', fontWeight: 700 }}>📷 Student Question Proof Snapshot</span>
              <button className="btn btn-secondary btn-sm" onClick={() => setSelectedDisputeScreenshot(null)}>✕ Close</button>
            </div>
            <div style={{ padding: '16px', overflowY: 'auto', display: 'flex', justifyContent: 'center', background: '#0b0f19' }}>
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img 
                src={selectedDisputeScreenshot} 
                alt="Student Proof Snapshot" 
                style={{ maxWidth: '100%', maxHeight: '75vh', objectFit: 'contain', borderRadius: '8px', border: '1px solid rgba(255,255,255,0.1)' }} 
              />
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
