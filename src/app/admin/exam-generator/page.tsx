'use client';

import React, { useEffect, useState, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import Script from 'next/script';
import { useMathRender } from '@/hooks/useMathRender';
import { preprocessMathText, smartJsonParse, robustParseAIJson, cleanStringForMatch, toCanonicalQuestionType } from '@/lib/questionTypes';
import { highlightModelAnswerKeywords } from '@/lib/pdfExport';
import { SyllabusSelector } from '@/components/SyllabusSelector';
import { useSyllabusSelector } from '@/hooks/useSyllabusSelector';
import { distributeCountsByWeight as distributeCountsByWeightLib, buildObjectiveSchema, isSameTopic } from '@/lib/syllabusUtils';
import { areQuestionsTooSimilar } from '@/lib/questionSimilarity';

interface Template {
  id: string;
  name: string;
  totalQuestions: number;
  duration: number;
  positiveMarks: number;
  negativeMarks: number;
  difficulty?: { easy: number; medium: number; hard: number };
  typeCounts?: { [key: string]: number };
  objectiveDistribution?: { [key: string]: number };
  subjectiveDistribution?: { [key: string]: number };
  examCategory?: 'standard' | 'foundation' | 'mock';
}

const CANONICAL_EXAM_PRESETS: Template[] = [
  {
    id: 'daily_topic_30',
    name: 'Daily Topic Objective Test (30 Questions • 45 Mins • 120 Marks)',
    totalQuestions: 30,
    duration: 45,
    positiveMarks: 4,
    negativeMarks: 1,
    difficulty: { easy: 30, medium: 50, hard: 20 },
    objectiveDistribution: { single_choice: 18, assertion_reason: 4, multiple_choice: 4, numerical: 4 },
    examCategory: 'standard'
  },
  {
    id: 'chapter_mastery_30',
    name: 'Chapter Mastery Test (30 Questions • 45 Mins • 120 Marks)',
    totalQuestions: 30,
    duration: 45,
    positiveMarks: 4,
    negativeMarks: 1,
    difficulty: { easy: 20, medium: 50, hard: 30 },
    objectiveDistribution: { single_choice: 18, assertion_reason: 4, multiple_choice: 4, numerical: 4 },
    examCategory: 'standard'
  },
  {
    id: 'full_chapter_mock_30',
    name: 'Full Chapter Mock Test (30 Questions • 45 Mins • 120 Marks)',
    totalQuestions: 30,
    duration: 45,
    positiveMarks: 4,
    negativeMarks: 1,
    difficulty: { easy: 25, medium: 50, hard: 25 },
    objectiveDistribution: { single_choice: 20, assertion_reason: 5, multiple_choice: 3, numerical: 2 },
    examCategory: 'mock'
  },
  {
    id: 'combined_portions_mock_60',
    name: 'Combined Syllabus / Term Mock (60 Questions • 90 Mins • 240 Marks)',
    totalQuestions: 60,
    duration: 90,
    positiveMarks: 4,
    negativeMarks: 1,
    difficulty: { easy: 20, medium: 50, hard: 30 },
    objectiveDistribution: { single_choice: 40, assertion_reason: 10, multiple_choice: 5, numerical: 5 },
    examCategory: 'mock'
  },
  {
    id: 'foundation_olympiad_50',
    name: 'Foundation / Olympiad Mock (50 Questions • 60 Mins • 200 Marks)',
    totalQuestions: 50,
    duration: 60,
    positiveMarks: 4,
    negativeMarks: 1,
    difficulty: { easy: 10, medium: 40, hard: 50 },
    objectiveDistribution: { single_choice: 30, assertion_reason: 10, multiple_choice: 5, numerical: 5 },
    examCategory: 'foundation'
  },
  {
    id: 'homi_bhabha_9_100',
    name: 'Dr. Homi Bhabha Science Mock (100 Questions • 90 Mins • 100 Marks)',
    totalQuestions: 100,
    duration: 90,
    positiveMarks: 1,
    negativeMarks: 0,
    difficulty: { easy: 20, medium: 50, hard: 30 },
    objectiveDistribution: { single_choice: 94, numerical: 6 },
    examCategory: 'foundation'
  },
  {
    id: 'quick_revision_15',
    name: 'Quick Practice Quiz (15 Questions • 20 Mins • 60 Marks)',
    totalQuestions: 15,
    duration: 20,
    positiveMarks: 4,
    negativeMarks: 1,
    difficulty: { easy: 40, medium: 40, hard: 20 },
    objectiveDistribution: { single_choice: 10, assertion_reason: 3, numerical: 2 },
    examCategory: 'standard'
  },
  {
    id: 'custom_blueprint',
    name: 'Custom Blueprint (Configure Qs & Time)',
    totalQuestions: 30,
    duration: 45,
    positiveMarks: 4,
    negativeMarks: 1
  }
];

const CANONICAL_SUBJECTIVE_PRESETS: Template[] = [
  {
    id: 'daily_subjective_3',
    name: 'Daily Subjective Practice (3 Questions • 10 Mins • 8 Marks)',
    totalQuestions: 3,
    duration: 10,
    positiveMarks: 2,
    negativeMarks: 0,
    subjectiveDistribution: { subjective_short: 2, subjective_long: 1 }
  },
  {
    id: 'saturday_classroom_6',
    name: 'Saturday Classroom Test (6 Questions • 60 Mins • 20 Marks)',
    totalQuestions: 6,
    duration: 60,
    positiveMarks: 4,
    negativeMarks: 0,
    subjectiveDistribution: { subjective_short: 4, subjective_long: 2 }
  },
  {
    id: 'custom_subjective',
    name: 'Custom Subjective Blueprint',
    totalQuestions: 6,
    duration: 45,
    positiveMarks: 2,
    negativeMarks: 0
  }
];

interface SelectedTopic {
  subject: string;
  chapterName: string;
  chapterNumber: string;
  topic: string;
  topicNumber: string;
}

interface Question {
  id?: string;
  questionCode?: string;
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
  topicOrigin?: string;
  marks?: number;
  keywords?: string[];
  topicNumber?: string;
  topicCode?: string;
  topic?: string;
  topicName?: string;
  subtopic?: string;
  subtopicName?: string;
  conceptTag?: string;
  chapterNumber?: string;
  board?: string;
  boardCode?: string;
  class?: string | number;
  subject?: string;
  subjectCode?: string;
}

export default function AdminExamGeneratorPage() {
  const { firebaseUser, logout } = useAuth();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Index metadata
  const [templates, setTemplates] = useState<Template[]>([]);
  const [syllabusIndex, setSyllabusIndex] = useState<any>(null);
  const [boardCodes, setBoardCodes] = useState<any>({});
  const [subjectCodes, setSubjectCodes] = useState<any>({});

  // Input states
  const {
    selectedBoard, setSelectedBoard,
    selectedClass, setSelectedClass,
    availableSubjects, setAvailableSubjects,
    selectedSubjects, setSelectedSubjects,
    availableChapters, setAvailableChapters,
    selectedChapters, setSelectedChapters,
    availableTopics, setAvailableTopics,
    selectedTopics, setSelectedTopics,
    classes,
    handleBoardChange,
    handleClassChange,
    handleToggleSubject,
    handleSelectAllSubjects,
    handleDeselectAllSubjects,
    handleToggleChapter,
    handleSelectAllChapters,
    handleDeselectAllChapters,
    handleToggleTopic,
    handleSelectAllTopics,
    handleDeselectAllTopics
  } = useSyllabusSelector<any, Set<string>>({
    syllabusIndex,
    initialSelectedSubjects: new Set<string>(),
    emptySelectedSubjects: new Set<string>()
  });

  const [selectedTemplateId, setSelectedTemplateId] = useState('daily_topic_30');
  const [currentTemplate, setCurrentTemplate] = useState<Template | null>(CANONICAL_EXAM_PRESETS[0]);
  const [questionType, setQuestionType] = useState<'objective' | 'subjective'>('objective');

  // Custom Blueprint Configuration States
  const [customTotalQs, setCustomTotalQs] = useState<number>(30);
  const [customDuration, setCustomDuration] = useState<number>(45);
  const [customPositiveMarks, setCustomPositiveMarks] = useState<number>(4);
  const [customNegativeMarks, setCustomNegativeMarks] = useState<number>(1);
  const [customPoolMode, setCustomPoolMode] = useState<'flexible' | 'custom_types'>('flexible');
  const [customTypeCounts, setCustomTypeCounts] = useState<{ [key: string]: number }>({
    single_mcq: 18,
    assertion_reason: 4,
    multiple_mcq: 4,
    numerical: 4
  });
  const [customDifficulty, setCustomDifficulty] = useState<{ easy: number; medium: number; hard: number }>({
    easy: 30,
    medium: 50,
    hard: 20
  });

  // Custom Subjective Configuration States
  const [customSubjTotalQs, setCustomSubjTotalQs] = useState<number>(6);
  const [customSubjDuration, setCustomSubjDuration] = useState<number>(45);
  const [customSubjPositiveMarks, setCustomSubjPositiveMarks] = useState<number>(2);
  const [customSubjPoolMode, setCustomSubjPoolMode] = useState<'flexible' | 'custom_types'>('flexible');
  const [customSubjTypeCounts, setCustomSubjTypeCounts] = useState<{ [key: string]: number }>({
    subjective_short: 4,
    subjective_long: 2
  });

  const handleSwitchType = (type: 'objective' | 'subjective') => {
    setQuestionType(type);
    if (type === 'objective') {
      setSelectedTemplateId('daily_topic_30');
      setCurrentTemplate(CANONICAL_EXAM_PRESETS[0]);
    } else {
      setSelectedTemplateId('daily_subjective_3');
      setCurrentTemplate(CANONICAL_SUBJECTIVE_PRESETS[0]);
    }
    setAvailablePool([]);
    setGeneratedQuestions([]);
    setShortfalls([]);
  };

  const isSubjectiveTemplate = (template: Template) => {
    const subjectiveKeys = [
      'numerical_short', 'numerical_long', 'subjective_short', 
      'subjective_long', 'subjective_reason', 'subjective_notes', 'subjective_define',
      'subjective_laws'
    ];
    if (template.typeCounts) {
      return Object.entries(template.typeCounts).some(([key, val]) => 
        subjectiveKeys.includes(key) && Number(val || 0) > 0
      );
    }
    if (template.subjectiveDistribution) {
      return Object.values(template.subjectiveDistribution).some(val => Number(val || 0) > 0);
    }
    return false;
  };

  // Subject selection states
  const [weightageMode, setWeightageMode] = useState<'equal' | 'custom'>('equal');
  const [subjectWeights, setSubjectWeights] = useState<{ [key: string]: number }>({});
  const [topicWeights, setTopicWeights] = useState<{ [key: string]: number | string }>({});
  const [topicWeightMode, setTopicWeightMode] = useState<'equal' | 'custom'>('equal');

  // Question selection pools
  const [availablePool, setAvailablePool] = useState<Question[]>([]);
  const [generatedQuestions, setGeneratedQuestions] = useState<Question[]>([]);
  const [shortfalls, setShortfalls] = useState<any[]>([]);
  const [fetchingPool, setFetchingPool] = useState(false);

  // In-Place Shortfall AI Generation Modal State
  const [showShortfallModal, setShowShortfallModal] = useState(false);
  const [shortfallAiPrompt, setShortfallAiPrompt] = useState('');
  const [shortfallAiPasteText, setShortfallAiPasteText] = useState('');
  const [shortfallSaving, setShortfallSaving] = useState(false);
  const [shortfallError, setShortfallError] = useState('');

  // AI Generation overlay
  const [aiGenerating, setAiGenerating] = useState(false);
  const [aiStatusSub, setAiStatusSub] = useState('');
  const [aiStatusCount, setAiStatusCount] = useState('');
  useMathRender([generatedQuestions, selectedBoard, selectedClass, selectedTemplateId]);
  const [savingExam, setSavingExam] = useState(false);

  // Load initial settings metadata
  const loadInitialMetadata = async () => {
    if (!firebaseUser) return;
    setLoading(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/exams/generate', {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        throw new Error('Failed to load initial configuration metadata.');
      }
      const data = await res.json();
      const examTemplates = (data.templates || []).filter((t: any) => 
        t.type === 'exam' || t.templateType === 'exam' || t.type === 'both' || t.templateType === 'both'
      );
      setTemplates(examTemplates);
      setSyllabusIndex(data.syllabusSubjects);
      setBoardCodes(data.boardCodes);
      setSubjectCodes(data.subjectCodes);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error occurred loading metadata.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (firebaseUser) {
      loadInitialMetadata();
    }
  }, [firebaseUser]);



  useEffect(() => {
    triggerLoadChapters(selectedSubjects);
  }, [selectedSubjects]);



  const resetChaptersTopics = () => {
    setAvailableChapters([]);
    setSelectedChapters(new Set());
    setAvailableTopics([]);
    setSelectedTopics([]);
    setGeneratedQuestions([]);
    setShortfalls([]);
    setAvailablePool([]);
  };

  const triggerLoadChapters = async (subs: Set<string>) => {
    resetChaptersTopics();
    if (subs.size === 0) return;

    // 1. INSTANT: Synchronously populate chapters and topics from loaded syllabusIndex (0ms delay)
    const instantChaptersList: any[] = [];
    Array.from(subs).forEach((subject) => {
      const entry = syllabusIndex?.subjects?.[selectedBoard]?.[selectedClass]?.[subject];
      if (entry && Array.isArray(entry.chapters)) {
        entry.chapters.forEach((ch: any, idx: number) => {
          instantChaptersList.push({
            subject,
            chapter: ch,
            chapterName: ch.name || `Chapter ${ch.number || idx + 1}`,
            chapterNumber: String(ch.number || idx + 1),
            objectiveCount: ch.objectiveCount || 0,
            subjectiveCount: ch.subjectiveCount || 0
          });
        });
      }
    });

    if (instantChaptersList.length > 0) {
      const instantTopicsList: any[] = [];
      instantChaptersList.forEach((chItem) => {
        const rawTopics = chItem.chapter.topics || [];
        const walk = (tList: any[], parentNum?: string, parentCode?: string) => {
          tList.forEach((t, sIdx) => {
            const isObj = t && typeof t === 'object';
            const subNum = !isObj && parentNum ? `${parentNum}.${sIdx + 1}` : '';
            const rawNum = isObj ? (t.number || t.topicNumber || '') : subNum;
            const name = isObj ? (t.name || t.title || '') : String(t);
            const label = rawNum ? `${rawNum} ${name}` : name;
            const num = rawNum || label;
            const topCode = isObj ? (t.topicCode || t.subtopicCode || '') : (parentCode ? `${parentCode}.${sIdx + 1}` : '');
            instantTopicsList.push({
              subject: chItem.subject,
              chapterName: chItem.chapterName,
              chapterNumber: chItem.chapterNumber,
              topic: label,
              topicName: name || label,
              topicNumber: num,
              topicCode: topCode,
              objectiveCount: isObj ? (t.objectiveCount || 0) : 0,
              subjectiveCount: isObj ? (t.subjectiveCount || 0) : 0,
              hasSubtopics: isObj && Array.isArray(t.subtopics) && t.subtopics.length > 0
            });
            if (isObj && t.subtopics && t.subtopics.length > 0) walk(t.subtopics, num, topCode);
          });
        };
        walk(rawTopics);
      });

      setAvailableChapters(instantChaptersList);
      setAvailableTopics(instantTopicsList);
    }

    if (!firebaseUser) return;
    
    setFetchingPool(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const allChaptersList: any[] = [];
      
      await Promise.all(
        Array.from(subs).map(async (subject) => {
          const entry = syllabusIndex?.subjects?.[selectedBoard]?.[selectedClass]?.[subject];
          if (entry && entry.docId) {
            const res = await fetch(`/api/admin/exams/generate?docId=${entry.docId}`, {
              headers: { 'Authorization': `Bearer ${idToken}` }
            });
            if (res.ok) {
              const syllabusDoc = await res.json();
              const list = syllabusDoc.chapters || [];
              list.forEach((ch: any, idx: number) => {
                allChaptersList.push({
                  subject,
                  chapter: ch,
                  chapterName: ch.name || `Chapter ${ch.number || idx + 1}`,
                  chapterNumber: String(ch.number || idx + 1),
                  objectiveCount: ch.objectiveCount || 0,
                  subjectiveCount: ch.subjectiveCount || 0
                });
              });
            }
          }
        })
      );

      if (allChaptersList.length > 0) {
        // Compile flat list of all topics with enriched live counts
        const allTopicsList: any[] = [];
        allChaptersList.forEach((chItem) => {
          const rawTopics = chItem.chapter.topics || [];
          const walk = (tList: any[], parentNum?: string, parentCode?: string) => {
            tList.forEach((t, sIdx) => {
              const isObj = t && typeof t === 'object';
              const subNum = !isObj && parentNum ? `${parentNum}.${sIdx + 1}` : '';
              const rawNum = isObj ? (t.number || t.topicNumber || '') : subNum;
              const name = isObj ? (t.name || t.title || '') : String(t);
              const label = rawNum ? `${rawNum} ${name}` : name;
              const num = rawNum || label;
              const topCode = isObj ? (t.topicCode || t.subtopicCode || '') : (parentCode ? `${parentCode}.${sIdx + 1}` : '');
              allTopicsList.push({
                subject: chItem.subject,
                chapterName: chItem.chapterName,
                chapterNumber: chItem.chapterNumber,
                topic: label,
                topicName: name || label,
                topicNumber: num,
                topicCode: topCode,
                objectiveCount: isObj ? (t.objectiveCount || 0) : 0,
                subjectiveCount: isObj ? (t.subjectiveCount || 0) : 0,
                hasSubtopics: isObj && Array.isArray(t.subtopics) && t.subtopics.length > 0
              });
              if (isObj && t.subtopics && t.subtopics.length > 0) walk(t.subtopics, num, topCode);
            });
          };
          walk(rawTopics);
        });

        setAvailableChapters(allChaptersList);
        setAvailableTopics(allTopicsList);

        // Reconcile and deduplicate selectedTopics against live allTopicsList
        setSelectedTopics(prev => {
          const reconciled: any[] = [];
          prev.forEach(p => {
            const match = allTopicsList.find(t => isSameTopic(t, p));
            const itemToKeep = match || p;
            if (!reconciled.some(r => isSameTopic(r, itemToKeep))) {
              reconciled.push(itemToKeep);
            }
          });
          return reconciled;
        });
      }
    } catch (err) {
      console.error(err);
    } finally {
      setFetchingPool(false);
    }
  };

  // Helper: check if a question matches a selected topic or subtopic
  const isQuestionMatchingTopic = (q: Question, t: any): boolean => {
    if (!q || !t) return false;
    const qTopNum = String(q.topicNumber || '').trim();
    const qTopCode = String(q.topicCode || '').trim();
    const qTopicName = String(q.topic || q.topicName || '').trim().toLowerCase();
    const qSubtopicName = String(q.subtopic || q.subtopicName || '').trim().toLowerCase();
    const qConceptTag = String(q.conceptTag || '').trim().toLowerCase();
    const qCode = String(q.questionCode || q.id || '').trim();

    const tTopNum = String(t.topicNumber || '').trim();
    const tTopCode = String(t.topicCode || '').trim();
    const tTopicName = String(t.topicName || t.topic || '').trim().toLowerCase();
    const tTopicTitle = String(t.name || t.title || '').trim().toLowerCase();

    if (tTopNum && (qTopNum === tTopNum || qTopNum.endsWith(`.${tTopNum}`) || tTopNum.endsWith(`.${qTopNum}`))) return true;
    if (tTopCode && (qTopCode === tTopCode || qTopCode.endsWith(`-${tTopCode}`) || qCode.includes(`-${tTopCode}-`))) return true;

    const targetNames = [tTopicName, tTopicTitle].filter(Boolean);
    const questionNames = [qTopicName, qSubtopicName, qConceptTag].filter(Boolean);

    for (const tName of targetNames) {
      const tClean = cleanStringForMatch(tName);
      for (const qName of questionNames) {
        if (qName === tName || qName.includes(tName) || tName.includes(qName)) return true;
        if (tClean && cleanStringForMatch(qName) === tClean) return true;
      }
    }

    if (tTopNum) {
      if (qCode.includes(`-${tTopNum}-`) || qCode.includes(`-${tTopNum}.`)) return true;
      if (tTopNum.includes('.')) {
        const parts = tTopNum.split('.');
        if (parts.length >= 2 && qCode.includes(`-${parts[parts.length - 1]}-`)) return true;
      }
    }

    return false;
  };

  // Handle template selection change
  const handleTemplateChange = (id: string) => {
    setSelectedTemplateId(id);
    const pool = questionType === 'subjective' ? CANONICAL_SUBJECTIVE_PRESETS : CANONICAL_EXAM_PRESETS;
    const tmpl = pool.find(t => t.id === id) || null;
    if (id === 'custom_blueprint') {
      setCurrentTemplate({
        id: 'custom_blueprint',
        name: 'Custom Blueprint (Configure Qs & Time)',
        totalQuestions: customTotalQs,
        duration: customDuration,
        positiveMarks: customPositiveMarks,
        negativeMarks: customNegativeMarks,
        difficulty: customDifficulty,
        typeCounts: customPoolMode === 'custom_types' ? customTypeCounts : undefined
      });
    } else if (id === 'custom_subjective') {
      setCurrentTemplate({
        id: 'custom_subjective',
        name: 'Custom Subjective Blueprint',
        totalQuestions: customSubjTotalQs,
        duration: customSubjDuration,
        positiveMarks: customSubjPositiveMarks,
        negativeMarks: 0,
        typeCounts: customSubjPoolMode === 'custom_types' ? customSubjTypeCounts : undefined
      });
    } else {
      setCurrentTemplate(tmpl);
    }
  };

  const getNormalizedTypeCounts = (tmpl: Template | null, qType: 'objective' | 'subjective') => {
    if (!tmpl) return null;
    if (tmpl.id === 'custom_blueprint') {
      if (customPoolMode === 'flexible') return null;
      return customTypeCounts;
    }
    if (tmpl.id === 'custom_subjective') {
      if (customSubjPoolMode === 'flexible') return null;
      return customSubjTypeCounts;
    }
    if (tmpl.typeCounts && Object.keys(tmpl.typeCounts).length > 0) {
      return tmpl.typeCounts;
    }
    if (qType === 'subjective') {
      if (tmpl.subjectiveDistribution && Object.keys(tmpl.subjectiveDistribution).length > 0) {
        return tmpl.subjectiveDistribution;
      }
      return { subjective_short: Math.max(1, Math.floor((tmpl.totalQuestions || 3) * 0.7)), subjective_long: Math.max(1, Math.ceil((tmpl.totalQuestions || 3) * 0.3)) };
    }
    if (tmpl.objectiveDistribution && Object.keys(tmpl.objectiveDistribution).length > 0) {
      const counts: Record<string, number> = {};
      Object.entries(tmpl.objectiveDistribution).forEach(([k, v]) => {
        const num = Number(v) || 0;
        if (num <= 0) return;
        if (k === 'single_choice' || k === 'single_mcq') counts['single_mcq'] = num;
        else if (k === 'multiple_choice' || k === 'multiple_mcq') counts['multiple_mcq'] = num;
        else if (k === 'assertion_reason') counts['assertion_reason'] = num;
        else if (k === 'numerical' || k === 'numerical_obj') counts['numerical'] = num;
        else if (k === 'true_false') counts['true_false'] = num;
        else counts[k] = num;
      });
      if (Object.keys(counts).length > 0) return counts;
    }
    return { single_mcq: tmpl.totalQuestions || 30 };
  };

  // Boards and Classes derivation
  const getBoards = () => {
    if (!syllabusIndex || !syllabusIndex.subjects) return [];
    return Object.keys(syllabusIndex.subjects).sort();
  };

  const filteredTopics = useMemo(() => {
    const selectedChs = Array.from(selectedChapters).map(idx => availableChapters[idx]).filter(Boolean);
    return availableTopics.filter(top => 
      selectedChs.some(ch => ch.chapterNumber === top.chapterNumber && ch.subject === top.subject)
    );
  }, [selectedChapters, availableChapters, availableTopics]);

  const getTopicKey = (t: any) => t?.topicCode || t?.topicNumber || t?.topic || '';

  // Distribute counts based on equal/custom weightages
  const distributeCountsByWeight = (count: number) => {
    const cleanWeights: Record<string, number> = {};
    selectedTopics.forEach(t => {
      const key = getTopicKey(t);
      const raw = topicWeights[key];
      cleanWeights[key] = typeof raw === 'number' ? raw : (parseInt(String(raw), 10) || 0);
    });
    return distributeCountsByWeightLib(
      count,
      selectedTopics,
      cleanWeights,
      topicWeightMode,
      getTopicKey
    );
  };

  // Fetch Pool Candidate Questions
  const handleFetchPool = async () => {
    if (!currentTemplate) {
      alert('Select a template first.');
      return;
    }
    if (!selectedBoard || !selectedClass) {
      alert('Select board and class configurations.');
      return;
    }
    if (selectedTopics.length === 0) {
      alert('Please select at least one topic checkbox.');
      return;
    }
    if (topicWeightMode === 'custom') {
      const sum = selectedTopics.reduce((acc, t) => {
        const raw = topicWeights[getTopicKey(t)];
        const val = typeof raw === 'number' ? raw : (parseInt(String(raw), 10) || 0);
        return acc + (raw !== undefined && raw !== '' ? val : Math.floor(100 / selectedTopics.length));
      }, 0);
      if (sum !== 100) {
        alert('⚠️ Total custom topic weightage must sum up to exactly 100% before fetching questions.');
        return;
      }
    }
    if (!firebaseUser) return;

    setFetchingPool(true);
    try {
      const allSubjects = Array.from(selectedSubjects).join(',');
      const topicNumbers = Array.from(new Set(
        selectedTopics.flatMap(t => [t.topicNumber, t.topicName, t.topicCode, t.topic].filter(Boolean))
      )).join(',');
      const examCategory = currentTemplate?.examCategory || 'standard';

      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/exams/generate?action=fetchPool&board=${selectedBoard}&classNum=${selectedClass}&subject=${encodeURIComponent(allSubjects)}&topicNumbers=${encodeURIComponent(topicNumbers)}&questionType=${questionType}&examCategory=${examCategory}`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });

      if (!res.ok) {
        throw new Error('Failed to load candidate questions from bank.');
      }
      const data = await res.json();
      const pool: Question[] = data.questions || data.pool || [];
      setAvailablePool(pool);

      const isCustom = selectedTemplateId === 'custom_blueprint' || selectedTemplateId === 'custom_subjective';
      const effectiveTotalQs = isCustom 
        ? (questionType === 'subjective' ? customSubjTotalQs : customTotalQs)
        : (currentTemplate.totalQuestions || 10);
      const effectiveDifficulty = isCustom && questionType === 'objective'
        ? customDifficulty
        : (currentTemplate.difficulty || { easy: 30, medium: 50, hard: 20 });

      const normalizedTypeCounts = getNormalizedTypeCounts(currentTemplate, questionType);

      const selected: Question[] = [];
      const usedCodes = new Set<string>();
      const shortfallReqs: any[] = [];

      // Calculate total topic question targets based on topic weightages
      const topicQuestionTargets = distributeCountsByWeight(effectiveTotalQs);

      if (!normalizedTypeCounts) {
        // Flexible Pool Mode: Fill up each topic's target quota from available questions in that topic
        selectedTopics.forEach(t => {
          const targetForTopic = topicQuestionTargets[getTopicKey(t)] || 0;
          if (targetForTopic <= 0) return;

          const easyTarget = Math.round((effectiveDifficulty.easy / 100) * targetForTopic);
          const medTarget = Math.round((effectiveDifficulty.medium / 100) * targetForTopic);
          const hardTarget = targetForTopic - easyTarget - medTarget;

          const diffReqs = [
            { diff: 'easy', count: easyTarget },
            { diff: 'medium', count: medTarget },
            { diff: 'hard', count: hardTarget }
          ].filter(r => r.count > 0);

          let pickedForTopic = 0;

          // 1. Pick preferred difficulty distributions
          diffReqs.forEach(req => {
            const candidates = pool.filter(q =>
              q.difficulty === req.diff &&
              isQuestionMatchingTopic(q, t) &&
              !usedCodes.has(q.questionCode || q.id || '') &&
              !selected.some(sel => areQuestionsTooSimilar(q, sel))
            );
            const picked = candidates.slice(0, req.count);
            picked.forEach(q => {
              usedCodes.add(q.questionCode || q.id || '');
              selected.push(q);
              pickedForTopic++;
            });
          });

          // 2. If topic target not fully reached, pick any remaining valid questions for this topic
          if (pickedForTopic < targetForTopic) {
            const remaining = pool.filter(q =>
              isQuestionMatchingTopic(q, t) &&
              !usedCodes.has(q.questionCode || q.id || '') &&
              !selected.some(sel => areQuestionsTooSimilar(q, sel))
            ).slice(0, targetForTopic - pickedForTopic);

            remaining.forEach(q => {
              usedCodes.add(q.questionCode || q.id || '');
              selected.push(q);
              pickedForTopic++;
            });
          }

          // 3. If still short of topic target, record shortfall
          if (pickedForTopic < targetForTopic) {
            const shortfallCount = targetForTopic - pickedForTopic;
            const matchIdx = selectedTopics.findIndex(tp => tp.topicNumber === t.topicNumber);
            shortfallReqs.push({
              type: questionType === 'subjective' ? 'SSA' : 'OSC',
              difficulty: 'medium',
              count: shortfallCount,
              contextId: 'CTX-' + String(matchIdx + 1).padStart(3, '0'),
              topicName: t.topic
            });
          }
        });
      } else {
        // Structured Blueprint / Preset Mode
        const needed: any[] = [];
        Object.entries(normalizedTypeCounts).forEach(([type, count]) => {
          if (!count) return;
          const easyC = Math.round((effectiveDifficulty.easy / 100) * count);
          const medC = Math.round((effectiveDifficulty.medium / 100) * count);
          const hardC = count - easyC - medC;
          if (easyC > 0) needed.push({ type, difficulty: 'easy', count: easyC });
          if (medC > 0) needed.push({ type, difficulty: 'medium', count: medC });
          if (hardC > 0) needed.push({ type, difficulty: 'hard', count: hardC });
        });

        // Track how many questions each topic has received
        const topicPickedCounts: Record<string, number> = {};
        selectedTopics.forEach(t => { topicPickedCounts[getTopicKey(t)] = 0; });

        needed.forEach(req => {
          const topicCounts = distributeCountsByWeight(req.count);

          selectedTopics.forEach(t => {
            const targetForTopicAndType = topicCounts[t.topicNumber] || 0;
            if (targetForTopicAndType <= 0) return;

            // 1. Exact match (type + difficulty + topic)
            const candidates = pool.filter(q =>
              toCanonicalQuestionType(q.type) === toCanonicalQuestionType(req.type) &&
              q.difficulty === req.difficulty &&
              isQuestionMatchingTopic(q, t) &&
              !usedCodes.has(q.questionCode || q.id || '') &&
              !selected.some(sel => areQuestionsTooSimilar(q, sel))
            );

            const picked = candidates.slice(0, targetForTopicAndType);
            picked.forEach(q => {
              usedCodes.add(q.questionCode || q.id || '');
              selected.push(q);
              topicPickedCounts[t.topicNumber] = (topicPickedCounts[t.topicNumber] || 0) + 1;
            });

            let stillNeeded = targetForTopicAndType - picked.length;
            
            // 2. Relax difficulty for same type in topic
            if (stillNeeded > 0) {
              const relaxed = pool.filter(q =>
                toCanonicalQuestionType(q.type) === toCanonicalQuestionType(req.type) &&
                isQuestionMatchingTopic(q, t) &&
                !usedCodes.has(q.questionCode || q.id || '') &&
                !selected.some(sel => areQuestionsTooSimilar(q, sel))
              ).slice(0, stillNeeded);

              relaxed.forEach(q => {
                usedCodes.add(q.questionCode || q.id || '');
                selected.push(q);
                topicPickedCounts[t.topicNumber] = (topicPickedCounts[t.topicNumber] || 0) + 1;
              });
              stillNeeded -= relaxed.length;
            }

            // 3. Graceful Backfill: If the bank doesn't have enough questions of this exact type in this topic, backfill from other valid question types in this topic so the exam is filled
            if (stillNeeded > 0) {
              const otherTypes = pool.filter(q =>
                isQuestionMatchingTopic(q, t) &&
                !usedCodes.has(q.questionCode || q.id || '') &&
                !selected.some(sel => areQuestionsTooSimilar(q, sel))
              ).slice(0, stillNeeded);

              otherTypes.forEach(q => {
                usedCodes.add(q.questionCode || q.id || '');
                selected.push(q);
                topicPickedCounts[t.topicNumber] = (topicPickedCounts[t.topicNumber] || 0) + 1;
              });
              stillNeeded -= otherTypes.length;
            }

            // 4. True shortfall if the topic itself has run out of candidate questions
            if (stillNeeded > 0) {
              const matchIdx = selectedTopics.findIndex(tp => tp.topicNumber === t.topicNumber);
              shortfallReqs.push({
                type: req.type,
                difficulty: req.difficulty,
                count: stillNeeded,
                contextId: 'CTX-' + String(matchIdx + 1).padStart(3, '0'),
                topicName: t.topic
              });
            }
          });
        });
      }

      setGeneratedQuestions(selected);
      setShortfalls(shortfallReqs);

      if (pool.length === 0) {
        alert('⚠️ No candidate questions found in the Question Bank matching the selected topics. You can generate them with AI below.');
      }

    } catch (err: any) {
      alert(err.message || 'Error pulling matching questions.');
    } finally {
      setFetchingPool(false);
    }
  };

  // In-Place Shortfall AI Generation
  const handleOpenShortfallModal = () => {
    if (shortfalls.length === 0 || selectedTopics.length === 0) return;

    const primaryTopic = selectedTopics[0];
    const subjectCode = primaryTopic.subject;
    const isMath = /math|algebra|geometry|ganit/i.test(subjectCode);
    const examCategory = currentTemplate?.examCategory === 'foundation' ? 'foundation' : 'standard';

    let totalMissing = 0;
    shortfalls.forEach(s => { totalMissing += Number(s.count) || 0; });

    let shortfallDetailsBlock = '';
    shortfalls.forEach((s, idx) => {
      shortfallDetailsBlock += `\n${idx + 1}. [${s.contextId || 'CTX-001'}] ${s.topicName}: EXACTLY ${s.count} questions of type "${s.type}" with difficulty "${s.difficulty}"`;
    });

    const ctxBlock = selectedTopics.map((t, idx) => {
      const cid = 'CTX-' + String(idx + 1).padStart(3, '0');
      return `contextId: ${cid}\nSubject: ${t.subject || ''}\nChapter: ${t.chapterName || ''}\nChapter Number: ${t.chapterNumber || ''}\nTopic: ${t.topic || ''}\nTopic Number: ${t.topicNumber || ''}`;
    }).join('\n\n');

    const promptText = `========================================
ROLE & EXACT SHORTFALL FULFILLMENT GOAL
========================================
Act as an expert curriculum architect and senior exam paper setter for ${selectedBoard} Class ${selectedClass}.

An assessment blueprint requires EXACTLY ${totalMissing} missing questions that are currently not in the Question Bank.
Generate EXACTLY the required question counts matching each topic context and specification listed below:
${shortfallDetailsBlock}

========================================
TOPIC CONTEXT LIST:
========================================
${ctxBlock}

========================================
CRITICAL PEDAGOGICAL & CONTENT RULES:
========================================
1. STRICT BOARD & CLASS LEVEL: Strictly align difficulty, calculations, and vocabulary with ${selectedBoard} Class ${selectedClass} curriculum.
2. ZERO PLACEHOLDERS / SYNTHETIC LOOPS: Every question and option must be authentic, context-rich, and non-repetitive.
3. MATH / CHEMICAL EXPRESSIONS: Format with LaTeX double-escaped backslashes \\\\( ... \\\\) and \\\\ce{...}.
4. Tag each question object with "examCategory": "${examCategory}".
5. Ensure "contextId" matches the topic context (e.g. "CTX-001", "CTX-002").
${isMath ? '6. MATHEMATICS: 80% textbook verbatim exercises / practice sets, 20% pattern variants. Specify "textbookPracticeSet" key.' : '6. ZERO INVENTED NUMERICALS / ZERO FAKE STOICHIOMETRY: For non-mathematical or qualitative topics (biology, general science concepts), strictly DO NOT generate fake arithmetic or advanced stoichiometry (e.g. molar mass calculations of organic sugars like lactose/lactic acid, college mole conversions). Focus on authentic textbook-level concepts, mechanisms, and reasoning.'}
7. ZERO OUT-OF-GRADE HALLUCINATIONS: Absolutely forbid college or higher secondary (Class 11/12/NEET/JEE) level stoichiometry or formulas for Class ${selectedClass}. Keep all questions strictly within the prescribed ${selectedBoard} Class ${selectedClass} textbook standard.

========================================
OUTPUT SCHEMA SPECIFICATION:
========================================
Return ONLY a valid raw JSON array containing exactly ${totalMissing} question objects:

[
  {
    "contextId": "CTX-001",
    "type": "OSC", // Canonical 3-letter codes: OSC (Single MCQ), OMC (Multiple MCQ), OTF (True/False), OAR (Assertion/Reason), ONE (Numerical MCQ), SDF (Define), SSA (Short Answer), SLA (Long Answer), etc.
    "text": "Question statement...",
    "options": ["Option A", "Option B", "Option C", "Option D"], // (omit for numerical, assertion_reason, and subjective)
    "correctAnswer": "Option B", // (exact string from options; for assertion_reason exactly "A", "B", "C", or "D"; for numerical clean number)
    "solution": "Step-by-step reasoning...",
    "difficulty": "easy/medium/hard",
    "bloomLevel": "Understand/Apply/Analyze",
    "examCategory": "${examCategory}"
  }
]

Return ONLY valid JSON. No markdown wrappers or extra commentary.`;

    setShortfallAiPrompt(promptText);
    setShortfallAiPasteText('');
    setShortfallError('');
    setShowShortfallModal(true);
  };

  const handleParseAndSaveShortfall = async () => {
    const text = shortfallAiPasteText.trim();
    if (!text) {
      setShortfallError('Please paste the AI JSON response first.');
      return;
    }

    try {
      const parsed = robustParseAIJson(text);
      const arr = Array.isArray(parsed) ? parsed : (parsed.questions || [parsed]);
      if (!arr.length) throw new Error('No question array found in pasted JSON.');

      setShortfallSaving(true);
      setShortfallError('');

      const idToken = await firebaseUser!.getIdToken();

      const formattedQuestions = arr.map((q: any) => {
        const topicMatch = selectedTopics.find((t, idx) => {
          const cid = 'CTX-' + String(idx + 1).padStart(3, '0');
          return q.contextId === cid || String(q.topicNumber) === String(t.topicNumber) || q.topic === t.topic;
        }) || selectedTopics[0];

        return {
          qtype: toCanonicalQuestionType(q.type || q.qtype || 'OSC'),
          text: q.text || '',
          options: q.options || [],
          correctAnswer: q.correctAnswer || '',
          correctAnswers: q.correctAnswers || [],
          assertion: q.assertion || '',
          reason: q.reason || '',
          solution: q.solution || '',
          answerLines: q.answerLines || [],
          pyqInfo: q.pyqInfo || '',
          difficulty: q.difficulty || 'medium',
          bloomLevel: q.bloomLevel || 'Understand',
          board: selectedBoard,
          classNum: selectedClass,
          subjectName: topicMatch?.subject || Array.from(selectedSubjects)[0] || '',
          chapterNumber: topicMatch?.chapterNumber || '1',
          topicNumber: topicMatch?.topicNumber || '1.1',
          topic: topicMatch?.topic || '',
          topicName: topicMatch?.topic || '',
          keywords: q.keywords || [],
          textbookPracticeSet: q.textbookPracticeSet || '',
          marks: Number(q.marks) || (q.type?.startsWith('subjective_') ? 2 : 4)
        };
      });

      const res = await fetch('/api/admin/questions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'bulkSave',
          questions: formattedQuestions
        })
      });

      if (!res.ok) {
        throw new Error('Failed to save shortfall questions to database.');
      }

      setShowShortfallModal(false);
      alert(`✅ Successfully saved ${formattedQuestions.length} missing questions to Question Bank! Replenishing exam pool...`);
      
      // Auto-replenish pool
      await handleFetchPool();
    } catch (err: any) {
      setShortfallError(err.message || 'Parsing / saving failed.');
    } finally {
      setShortfallSaving(false);
    }
  };

  const handleRemoveQuestion = (idx: number) => {
    setGeneratedQuestions(prev => prev.filter((_, i) => i !== idx));
  };

  // Compile and save the complete exam
  const handleSaveExam = async () => {
    if (generatedQuestions.length === 0 || !firebaseUser || !currentTemplate) return;
    setSavingExam(true);

    try {
      const primarySubject = Array.from(selectedSubjects)[0] || 'General';
      const topicCodes = selectedTopics.map(t => t.topicNumber);
      const isMixed = topicCodes.length > 1;

      const chapterNames = Array.from(new Set(selectedTopics.map(t => t.chapterName))).join(', ');
      const chapterNumbers = Array.from(new Set(selectedTopics.map(t => t.chapterNumber))).join(', ');
      const questionCodes = generatedQuestions.map(q => q.questionCode || q.id || '');

      const idToken = await firebaseUser.getIdToken();
      const isCustom = selectedTemplateId === 'custom_blueprint' || selectedTemplateId === 'custom_subjective';
      const effectiveDuration = isCustom
        ? (questionType === 'subjective' ? customSubjDuration : customDuration)
        : (currentTemplate.duration || 30);
      const effectivePositiveMarks = isCustom
        ? (questionType === 'subjective' ? customSubjPositiveMarks : customPositiveMarks)
        : (currentTemplate.positiveMarks || 4);
      const effectiveNegativeMarks = isCustom
        ? (questionType === 'subjective' ? 0 : customNegativeMarks)
        : (currentTemplate.negativeMarks ?? 1);

      const templateDetailsPayload = {
        ...currentTemplate,
        totalQuestions: generatedQuestions.length,
        duration: effectiveDuration,
        positiveMarks: effectivePositiveMarks,
        negativeMarks: effectiveNegativeMarks
      };

      const res = await fetch('/api/admin/exams/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'saveExam',
          name: '', // Auto-generate name in backend
          board: selectedBoard,
          classNum: selectedClass,
          subjectName: primarySubject,
          subjects: Array.from(selectedSubjects),
          subjectWeightage: {},
          weightageMode,
          chapter: chapterNames,
          chapterNumber: chapterNumbers,
          topicCodes,
          isMixed,
          totalMarks: generatedQuestions.reduce((s, q) => s + (q.marks || effectivePositiveMarks), 0),
          questionCodes,
          templateId: selectedTemplateId,
          templateDetails: templateDetailsPayload,
          duration: effectiveDuration,
          positiveMarks: effectivePositiveMarks,
          negativeMarks: effectiveNegativeMarks,
          examCategory: currentTemplate.examCategory || 'standard',
          isMasteryExempt: currentTemplate.examCategory === 'mock' || currentTemplate.examCategory === 'foundation',
          examType: currentTemplate.examCategory === 'foundation' ? 'entrance' : (questionType === 'subjective' ? 'subjective' : 'obj')
        })
      });

      if (!res.ok) {
        throw new Error('Failed to save exam.');
      }
      const data = await res.json();
      alert('✅ Exam generated successfully!');
      setTimeout(() => {
        router.push(`/admin/exams?assign=${data.examId}`);
      }, 1500);
    } catch (err: any) {
      alert(err.message || 'Error occurred compiling exam.');
    } finally {
      setSavingExam(false);
    }
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Initializing exam compiler...
        </div>
      </div>
    );
  }

  const templateRequiredTypes = currentTemplate?.typeCounts ? Object.keys(currentTemplate.typeCounts) : [];
  const matchingPoolCount = templateRequiredTypes.length > 0
    ? availablePool.filter(q => templateRequiredTypes.some(reqType => toCanonicalQuestionType(reqType) === toCanonicalQuestionType(q.type))).length
    : availablePool.length;

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Page Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800, cursor: 'pointer' }} onClick={() => router.push('/admin')}>YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Exam Generator</h1>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          
          <button className="btn btn-secondary" onClick={() => router.push('/admin/exams')}>← Back</button>
        </div>
      </header>

      {/* Main Form container */}
      <main style={{ flex: 1, padding: '12px', maxWidth: '1240px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {error && (
          <div className="alert-box alert-box-danger" style={{ display: 'block', margin: 0, padding: '8px 12px', fontSize: '12px' }}>
            {error}
          </div>
        )}
        <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '12px 16px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px', margin: 0 }}>
            <h3 style={{ fontSize: '13px', fontWeight: 800, margin: 0, textTransform: 'uppercase', letterSpacing: '0.4px', color: 'var(--text)' }}>
              Exam Configuration
            </h3>
            {currentTemplate && (
              <span style={{ fontSize: '11px', color: 'var(--text-muted)', fontWeight: 600 }}>
                {currentTemplate.totalQuestions} Qs • {currentTemplate.duration} mins • +{currentTemplate.positiveMarks}/-{currentTemplate.negativeMarks} Marks
              </span>
            )}
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '10px 14px', alignItems: 'end' }}>
            <div>
              <label style={{ display: 'block', fontSize: '10px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '3px' }}>Question Type</label>
              <div style={{ display: 'flex', gap: '6px', alignItems: 'center', height: '32px' }}>
                <button 
                  type="button"
                  className={`btn btn-sm ${questionType === 'objective' ? 'btn-primary' : 'btn-secondary'}`}
                  onClick={() => handleSwitchType('objective')}
                  style={{ borderRadius: '16px', flex: 1, padding: '4px 8px', fontSize: '11px', fontWeight: 700 }}
                >
                  Objective
                </button>
                <button 
                  type="button"
                  className={`btn btn-sm ${questionType === 'subjective' ? 'btn-success' : 'btn-secondary'}`}
                  onClick={() => handleSwitchType('subjective')}
                  style={{ borderRadius: '16px', flex: 1, padding: '4px 8px', fontSize: '11px', fontWeight: 700 }}
                >
                  Subjective
                </button>
              </div>
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '10px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '3px' }}>Exam Blueprint / Preset</label>
              <select 
                value={selectedTemplateId} 
                onChange={(e) => handleTemplateChange(e.target.value)}
                style={{ width: '100%', padding: '5px 8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', height: '32px', fontWeight: 600 }}
              >
                {(questionType === 'subjective' ? CANONICAL_SUBJECTIVE_PRESETS : CANONICAL_EXAM_PRESETS).map(t => (
                  <option key={t.id} value={t.id}>{t.name}</option>
                ))}
              </select>
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '10px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '3px' }}>Select Board</label>
              <select 
                value={selectedBoard} 
                onChange={(e) => handleBoardChange(e.target.value, () => { setGeneratedQuestions([]); setShortfalls([]); })}
                style={{ width: '100%', padding: '5px 8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', height: '32px' }}
              >
                <option value="">-- Choose Board --</option>
                {getBoards().map(b => (
                  <option key={b} value={b}>{boardCodes[b] || b.toUpperCase()}</option>
                ))}
              </select>
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '10px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '3px' }}>Select Class</label>
              <select 
                value={selectedClass} 
                disabled={!selectedBoard}
                onChange={(e) => handleClassChange(e.target.value, () => { setGeneratedQuestions([]); setShortfalls([]); })}
                style={{ width: '100%', padding: '5px 8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', height: '32px' }}
              >
                <option value="">-- Choose Class --</option>
                {classes.map(c => (
                  <option key={c} value={c}>Class {c}</option>
                ))}
              </select>
            </div>
          </div>
          
          {/* Subjects, Chapters, and Topics selectors */}
          <SyllabusSelector
            availableSubjects={availableSubjects}
            selectedSubjects={selectedSubjects}
            onToggleSubject={handleToggleSubject}
            availableChapters={availableChapters}
            selectedChapters={selectedChapters}
            onToggleChapter={handleToggleChapter}
            onSelectAllChapters={handleSelectAllChapters}
            onDeselectAllChapters={handleDeselectAllChapters}
            availableTopics={filteredTopics}
            selectedTopics={selectedTopics}
            onToggleTopic={handleToggleTopic}
            onSelectAllTopics={() => handleSelectAllTopics(filteredTopics)}
            onDeselectAllTopics={() => handleDeselectAllTopics(filteredTopics)}
          />

          {currentTemplate && (
            <div style={{ background: 'var(--bg-soft)', padding: '6px 12px', borderRadius: 'var(--radius-sm)', fontSize: '11px', borderLeft: '3px solid var(--accent)', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '8px' }}>
              <span>📋 <strong>Template parameters:</strong> {selectedTemplateId === 'custom_blueprint' ? customTotalQs : selectedTemplateId === 'custom_subjective' ? customSubjTotalQs : currentTemplate.totalQuestions} Questions • {selectedTemplateId === 'custom_blueprint' ? customDuration : selectedTemplateId === 'custom_subjective' ? customSubjDuration : currentTemplate.duration} mins • +{selectedTemplateId === 'custom_blueprint' ? customPositiveMarks : selectedTemplateId === 'custom_subjective' ? customSubjPositiveMarks : currentTemplate.positiveMarks} / -{selectedTemplateId === 'custom_blueprint' ? customNegativeMarks : selectedTemplateId === 'custom_subjective' ? 0 : currentTemplate.negativeMarks} Marks</span>
              {selectedTemplateId === 'custom_blueprint' && (
                <span className="badge" style={{ background: 'rgba(59, 130, 246, 0.15)', color: '#60a5fa', border: '1px solid rgba(59, 130, 246, 0.3)', padding: '2px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700 }}>
                  ⚙️ Custom Mode: {customPoolMode === 'flexible' ? 'Flexible (All Available Types)' : 'Exact Type Counts'}
                </span>
              )}
            </div>
          )}

          {/* Custom Blueprint Configuration Panel (Objective) */}
          {selectedTemplateId === 'custom_blueprint' && (
            <div style={{ background: 'var(--surface-light)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', padding: '12px 14px', marginTop: '6px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px' }}>
                <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--text)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>⚙️ Custom Blueprint Configuration</span>
                <div style={{ display: 'flex', gap: '6px' }}>
                  <button
                    type="button"
                    className={`btn btn-sm ${customPoolMode === 'flexible' ? 'btn-primary' : 'btn-secondary'}`}
                    onClick={() => setCustomPoolMode('flexible')}
                    style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '12px' }}
                  >
                    🎯 Flexible Pool (Auto-Fill)
                  </button>
                  <button
                    type="button"
                    className={`btn btn-sm ${customPoolMode === 'custom_types' ? 'btn-primary' : 'btn-secondary'}`}
                    onClick={() => setCustomPoolMode('custom_types')}
                    style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '12px' }}
                  >
                    📑 Exact Type Breakdown
                  </button>
                </div>
              </div>

              {/* Row 1: Total Qs, Duration, Marks */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))', gap: '10px', alignItems: 'end' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>Total Questions</label>
                  <div style={{ display: 'flex', gap: '4px', alignItems: 'center' }}>
                    <input
                      type="number"
                      min={1}
                      max={200}
                      value={customTotalQs}
                      onChange={(e) => setCustomTotalQs(Math.max(1, parseInt(e.target.value, 10) || 1))}
                      style={{ width: '100%', padding: '4px 6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', height: '28px', fontWeight: 700 }}
                    />
                  </div>
                  <div style={{ display: 'flex', gap: '3px', marginTop: '3px', flexWrap: 'wrap' }}>
                    {[10, 15, 20, 30, 45, 60].map(cnt => (
                      <button
                        key={cnt}
                        type="button"
                        onClick={() => setCustomTotalQs(cnt)}
                        style={{ fontSize: '9px', padding: '1px 5px', borderRadius: '4px', border: '1px solid var(--border-light)', background: customTotalQs === cnt ? 'var(--accent)' : 'var(--surface)', color: customTotalQs === cnt ? '#fff' : 'var(--text-muted)', cursor: 'pointer' }}
                      >
                        {cnt}
                      </button>
                    ))}
                  </div>
                </div>

                <div>
                  <label style={{ display: 'block', fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>Duration (Mins)</label>
                  <input
                    type="number"
                    min={5}
                    max={300}
                    value={customDuration}
                    onChange={(e) => setCustomDuration(Math.max(5, parseInt(e.target.value, 10) || 5))}
                    style={{ width: '100%', padding: '4px 6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', height: '28px', fontWeight: 700 }}
                  />
                  <div style={{ display: 'flex', gap: '3px', marginTop: '3px', flexWrap: 'wrap' }}>
                    {[15, 30, 45, 60, 90].map(dur => (
                      <button
                        key={dur}
                        type="button"
                        onClick={() => setCustomDuration(dur)}
                        style={{ fontSize: '9px', padding: '1px 5px', borderRadius: '4px', border: '1px solid var(--border-light)', background: customDuration === dur ? 'var(--accent)' : 'var(--surface)', color: customDuration === dur ? '#fff' : 'var(--text-muted)', cursor: 'pointer' }}
                      >
                        {dur}m
                      </button>
                    ))}
                  </div>
                </div>

                <div>
                  <label style={{ display: 'block', fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>Positive Marks (+)</label>
                  <select
                    value={customPositiveMarks}
                    onChange={(e) => setCustomPositiveMarks(Number(e.target.value))}
                    style={{ width: '100%', padding: '4px 6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', height: '28px' }}
                  >
                    <option value={1}>+1 Mark</option>
                    <option value={2}>+2 Marks</option>
                    <option value={4}>+4 Marks (Standard)</option>
                  </select>
                </div>

                <div>
                  <label style={{ display: 'block', fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>Negative Marks (-)</label>
                  <select
                    value={customNegativeMarks}
                    onChange={(e) => setCustomNegativeMarks(Number(e.target.value))}
                    style={{ width: '100%', padding: '4px 6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', height: '28px' }}
                  >
                    <option value={0}>0 (No Penalty)</option>
                    <option value={0.25}>-0.25 Marks</option>
                    <option value={0.5}>-0.5 Marks</option>
                    <option value={1}>-1 Mark (Standard)</option>
                  </select>
                </div>
              </div>

              {/* Exact Type Breakdown Controls (when active) */}
              {customPoolMode === 'custom_types' && (
                <div style={{ background: 'var(--surface)', padding: '8px 10px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                  <div style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '6px', textTransform: 'uppercase' }}>Specify Target Counts Per Format:</div>
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(90px, 1fr))', gap: '6px' }}>
                    {[
                      { key: 'single_mcq', label: 'Single MCQ (OSC)' },
                      { key: 'multiple_mcq', label: 'Multi MCQ (OMC)' },
                      { key: 'true_false', label: 'True / False (OTF)' },
                      { key: 'assertion_reason', label: 'Assert-Reason (OAR)' },
                      { key: 'numerical', label: 'Numerical (ONE)' }
                    ].map(t => (
                      <div key={t.key}>
                        <span style={{ display: 'block', fontSize: '9px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '2px' }}>{t.label}</span>
                        <input
                          type="number"
                          min={0}
                          value={customTypeCounts[t.key] || 0}
                          onChange={(e) => {
                            const val = Math.max(0, parseInt(e.target.value, 10) || 0);
                            setCustomTypeCounts(prev => ({ ...prev, [t.key]: val }));
                          }}
                          style={{ width: '100%', padding: '3px 5px', border: '1px solid var(--border-light)', borderRadius: '4px', background: 'var(--surface-light)', color: 'var(--text)', fontSize: '11px', height: '26px' }}
                        />
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Difficulty breakdown */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px', fontSize: '10px', color: 'var(--text-muted)', flexWrap: 'wrap' }}>
                <span style={{ fontWeight: 700 }}>Difficulty Distribution:</span>
                <span>🟢 Easy: <strong>{customDifficulty.easy}%</strong></span>
                <span>🟡 Medium: <strong>{customDifficulty.medium}%</strong></span>
                <span>🔴 Hard: <strong>{customDifficulty.hard}%</strong></span>
                <div style={{ display: 'flex', gap: '4px', marginLeft: 'auto' }}>
                  <button
                    type="button"
                    onClick={() => setCustomDifficulty({ easy: 30, medium: 50, hard: 20 })}
                    style={{ fontSize: '9px', padding: '1px 6px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', cursor: 'pointer' }}
                  >
                    Balanced (30/50/20)
                  </button>
                  <button
                    type="button"
                    onClick={() => setCustomDifficulty({ easy: 50, medium: 40, hard: 10 })}
                    style={{ fontSize: '9px', padding: '1px 6px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', cursor: 'pointer' }}
                  >
                    Foundation (50/40/10)
                  </button>
                  <button
                    type="button"
                    onClick={() => setCustomDifficulty({ easy: 10, medium: 40, hard: 50 })}
                    style={{ fontSize: '9px', padding: '1px 6px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', cursor: 'pointer' }}
                  >
                    Challenger (10/40/50)
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* Custom Subjective Configuration Panel */}
          {selectedTemplateId === 'custom_subjective' && (
            <div style={{ background: 'var(--surface-light)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', padding: '12px 14px', marginTop: '6px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px' }}>
                <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--text)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>⚙️ Custom Subjective Configuration</span>
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))', gap: '10px', alignItems: 'end' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>Total Questions</label>
                  <input
                    type="number"
                    min={1}
                    max={50}
                    value={customSubjTotalQs}
                    onChange={(e) => setCustomSubjTotalQs(Math.max(1, parseInt(e.target.value, 10) || 1))}
                    style={{ width: '100%', padding: '4px 6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', height: '28px', fontWeight: 700 }}
                  />
                  <div style={{ display: 'flex', gap: '3px', marginTop: '3px' }}>
                    {[3, 5, 6, 8, 10].map(cnt => (
                      <button
                        key={cnt}
                        type="button"
                        onClick={() => setCustomSubjTotalQs(cnt)}
                        style={{ fontSize: '9px', padding: '1px 5px', borderRadius: '4px', border: '1px solid var(--border-light)', background: customSubjTotalQs === cnt ? 'var(--accent)' : 'var(--surface)', color: customSubjTotalQs === cnt ? '#fff' : 'var(--text-muted)', cursor: 'pointer' }}
                      >
                        {cnt}
                      </button>
                    ))}
                  </div>
                </div>

                <div>
                  <label style={{ display: 'block', fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>Duration (Mins)</label>
                  <input
                    type="number"
                    min={5}
                    max={240}
                    value={customSubjDuration}
                    onChange={(e) => setCustomSubjDuration(Math.max(5, parseInt(e.target.value, 10) || 5))}
                    style={{ width: '100%', padding: '4px 6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', height: '28px', fontWeight: 700 }}
                  />
                </div>

                <div>
                  <label style={{ display: 'block', fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>Marks Per Question (Avg)</label>
                  <select
                    value={customSubjPositiveMarks}
                    onChange={(e) => setCustomSubjPositiveMarks(Number(e.target.value))}
                    style={{ width: '100%', padding: '4px 6px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px', height: '28px' }}
                  >
                    <option value={1}>1 Mark (Define / Laws)</option>
                    <option value={2}>2 Marks (Short / Reasoning)</option>
                    <option value={4}>4 Marks (Long / Complex)</option>
                  </select>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Topic Weightage Section */}
        {selectedTopics.length > 0 && (
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '20px' }}>
            <h3 style={{ fontSize: '13px', fontWeight: 800, margin: '0 0 12px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', color: 'var(--accent)' }}>📊 Topic Weightage Distribution</h3>
            
            <div style={{ display: 'flex', gap: '15px', alignItems: 'center', marginBottom: '15px' }}>
              <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)' }}>Weightage Mode:</span>
              <button 
                type="button"
                className={`btn btn-sm ${topicWeightMode === 'equal' ? 'btn-primary' : 'btn-secondary'}`}
                onClick={() => setTopicWeightMode('equal')}
                style={{ borderRadius: '20px', padding: '4px 12px', fontSize: '11px' }}
              >
                ⚖️ Equal Weightage
              </button>
              <button 
                type="button"
                className={`btn btn-sm ${topicWeightMode === 'custom' ? 'btn-primary' : 'btn-secondary'}`}
                onClick={() => setTopicWeightMode('custom')}
                style={{ borderRadius: '20px', padding: '4px 12px', fontSize: '11px' }}
              >
                ⚙️ Custom Weightage
              </button>
            </div>

            {topicWeightMode === 'custom' ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 100px', gap: '10px', fontWeight: 'bold', fontSize: '11px', borderBottom: '1px dashed var(--border-light)', paddingBottom: '6px' }}>
                  <span>Topic Name</span>
                  <span style={{ textAlign: 'right' }}>Weight (%)</span>
                </div>
                {selectedTopics.map((top, idx) => {
                  const key = getTopicKey(top);
                  const currentWeight = topicWeights[key] !== undefined ? topicWeights[key] : Math.floor(100 / selectedTopics.length);
                  return (
                    <div key={idx} style={{ display: 'grid', gridTemplateColumns: '1fr 100px', gap: '10px', alignItems: 'center', fontSize: '12px' }}>
                      <span>{top.topic}</span>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <input 
                          type="number"
                          min={0}
                          max={100}
                          value={currentWeight === undefined || currentWeight === null ? '' : currentWeight}
                          onChange={(e) => {
                            const raw = e.target.value;
                            if (raw === '') {
                              setTopicWeights(prev => ({ ...prev, [key]: '' }));
                            } else {
                              const val = parseInt(raw, 10);
                              setTopicWeights(prev => ({ ...prev, [key]: isNaN(val) ? '' : Math.max(0, Math.min(100, val)) }));
                            }
                          }}
                          onBlur={() => {
                            if (currentWeight === '' || currentWeight === undefined) {
                              setTopicWeights(prev => ({ ...prev, [key]: 0 }));
                            }
                          }}
                          style={{ width: '60px', padding: '4px', textAlign: 'right', border: '1px solid var(--border-light)', borderRadius: '4px', background: 'var(--bg-soft)', color: 'var(--text)' }}
                        />
                        <span>%</span>
                      </div>
                    </div>
                  );
                })}
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 100px', gap: '10px', fontWeight: 'bold', fontSize: '12px', borderTop: '1px dashed var(--border-light)', paddingTop: '8px', marginTop: '5px' }}>
                  <span>Total Weightage</span>
                  <span style={{ textAlign: 'right', color: selectedTopics.reduce((acc, t) => {
                    const raw = topicWeights[getTopicKey(t)];
                    const val = typeof raw === 'number' ? raw : (parseInt(String(raw), 10) || 0);
                    return acc + (raw !== undefined && raw !== '' ? val : Math.floor(100 / selectedTopics.length));
                  }, 0) === 100 ? 'var(--success)' : 'var(--danger)' }}>
                    {selectedTopics.reduce((acc, t) => {
                      const raw = topicWeights[getTopicKey(t)];
                      const val = typeof raw === 'number' ? raw : (parseInt(String(raw), 10) || 0);
                      return acc + (raw !== undefined && raw !== '' ? val : Math.floor(100 / selectedTopics.length));
                    }, 0)}%
                  </span>
                </div>
                {selectedTopics.reduce((acc, t) => {
                  const raw = topicWeights[getTopicKey(t)];
                  const val = typeof raw === 'number' ? raw : (parseInt(String(raw), 10) || 0);
                  return acc + (raw !== undefined && raw !== '' ? val : Math.floor(100 / selectedTopics.length));
                }, 0) !== 100 && (
                  <p style={{ margin: '5px 0 0', fontSize: '11px', color: 'var(--danger)' }}>
                    ⚠️ Total custom weightage must sum up to exactly 100%.
                  </p>
                )}
              </div>
            ) : (
              <div style={{ fontSize: '12px', color: 'var(--text-muted)', background: 'var(--bg-soft)', padding: '10px', borderRadius: '4px' }}>
                ℹ️ Question counts will be distributed equally among the {selectedTopics.length} selected topics.
              </div>
            )}
          </div>
        )}

        {/* Scan / Generate Pool trigger */}
        {selectedTopics.length > 0 && currentTemplate && (
          <div style={{ display: 'flex', justifyContent: 'center' }}>
            <button className="btn btn-primary" onClick={handleFetchPool} disabled={fetchingPool} style={{ padding: '12px 30px' }}>
              {fetchingPool ? '🔍 Scanning Question Bank Pool...' : '🔎 Fetch Available Questions'}
            </button>
          </div>
        )}

        {/* Candidate Questions summary checklist */}
        {(availablePool.length > 0 || shortfalls.length > 0) && (
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '20px' }}>
            <h3 style={{ fontSize: '14px', fontWeight: 700, marginBottom: '15px' }}>📬 Candidate Check & shortfalls</h3>
            
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', background: 'var(--bg-soft)', padding: '15px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', marginBottom: '15px' }}>
              <div style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', borderBottom: '1px solid var(--border-light)', paddingBottom: '5px' }}>Pool Scan results:</div>
              <div style={{ fontSize: '12px' }}>Total Unused Candidate Questions Found: <strong>{matchingPoolCount}</strong></div>
              <div style={{ fontSize: '12px' }}>Questions Chosen for Exam: <strong>{generatedQuestions.length}</strong></div>
            </div>

            {shortfalls.length > 0 ? (
              <div style={{ background: 'rgba(255,152,0,0.06)', borderLeft: '3px solid var(--warning)', padding: '12px', borderRadius: 'var(--radius-sm)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '15px', flexWrap: 'wrap' }}>
                <div style={{ fontSize: '12px' }}>
                  ⚠️ Missing <strong>{shortfalls.reduce((s, r) => s + r.count, 0)}</strong> questions of specific format/difficulty combinations from bank.
                </div>
                <button className="btn btn-primary" onClick={handleOpenShortfallModal} style={{ background: 'var(--success)', borderColor: 'var(--success)', fontSize: '11px', padding: '6px 12px' }}>
                  ✨ Auto-Generate Missing with AI
                </button>
              </div>
            ) : (
              <div style={{ background: 'rgba(76,175,80,0.06)', borderLeft: '3px solid var(--success)', padding: '10px', borderRadius: 'var(--radius-sm)', fontSize: '12px', color: 'var(--success)', fontWeight: 600 }}>
                ✅ Found all {generatedQuestions.length} questions needed for this template in the bank!
              </div>
            )}
          </div>
        )}

        {/* Selected Questions List */}
        {generatedQuestions.length > 0 && (
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '16px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px' }}>
              <h3 style={{ fontSize: '13px', fontWeight: 700, margin: 0 }}>📝 Selected Exam Questions</h3>
              <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>({generatedQuestions.length} selected)</span>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              {generatedQuestions.map((q, idx) => (
                <div key={idx} style={{ background: 'var(--review-card-bg)', border: '1.5px solid var(--review-card-border)', padding: '10px 12px', borderRadius: 'var(--radius-sm)', display: 'flex', flexDirection: 'column', gap: '6px', width: '100%' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '4px', flexWrap: 'wrap', gap: '6px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
                      <span style={{ fontWeight: 800, fontSize: '12px', color: 'var(--accent)' }}>Q{idx + 1}</span>
                      <span style={{ fontSize: '10.5px', fontWeight: 700, padding: '1px 6px', borderRadius: '4px', background: 'var(--surface)', border: '1px solid var(--border-light)', color: 'var(--text)' }}>
                        {q.questionCode || 'AI_GENERATED'}
                      </span>
                      <span style={{ fontSize: '9.5px', textTransform: 'uppercase', padding: '1px 6px', borderRadius: '4px', background: 'var(--info-bg)', color: 'var(--info)', fontWeight: 700, border: '1px solid rgba(56, 189, 248, 0.3)' }}>
                        {q.type}
                      </span>
                      <span style={{ fontSize: '9.5px', textTransform: 'capitalize', padding: '1px 6px', borderRadius: '4px', background: 'var(--success-bg)', color: 'var(--success)', fontWeight: 700, border: '1px solid rgba(52, 211, 153, 0.3)' }}>
                        {q.difficulty}
                      </span>
                      <span style={{ fontSize: '10.5px', fontWeight: 700, color: 'var(--text-muted)' }}>
                        {q.marks || 4} Marks
                      </span>
                    </div>
                    <button className="btn btn-secondary btn-sm" style={{ color: 'var(--danger)', borderColor: 'rgba(239, 68, 68, 0.3)', padding: '2px 8px', fontSize: '10.5px' }} onClick={() => handleRemoveQuestion(idx)}>
                      🗑️ Remove
                    </button>
                  </div>

                  {/* Question Text */}
                  <div 
                    className="math-container" 
                    style={{ fontSize: '12.5px', fontWeight: 'bold', lineHeight: '1.35', color: 'var(--text)', width: '100%', wordBreak: 'break-word', margin: '2px 0 4px 0' }} 
                  >
                    {preprocessMathText(q.text)}
                  </div>
                  
                  {/* Render Options if MCQ */}
                  {q.options && q.options.length > 0 && (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', fontSize: '11.5px', color: 'var(--text)', width: '100%', marginBottom: '4px' }}>
                       {q.options.map((opt, oi) => {
                         const label = String.fromCharCode(65 + oi);
                         const isCorrect = q.correctAnswers 
                           ? (q.correctAnswers.includes(label) || q.correctAnswers.includes(opt)) 
                           : (q.correctAnswer === label || q.correctAnswer === opt);
                         return (
                           <div key={oi} style={{ display: 'flex', alignItems: 'center', gap: '6px', padding: '4px 8px', background: isCorrect ? 'var(--success-bg)' : 'var(--review-option-bg)', borderRadius: 'var(--radius-sm)', border: isCorrect ? '1.5px solid var(--success)' : '1px solid var(--review-option-border)', color: isCorrect ? 'var(--success)' : 'var(--text)', fontWeight: isCorrect ? 600 : 400 }}>
                             <span style={{ fontWeight: 700, flexShrink: 0 }}>{isCorrect ? '✅ ' : ''}{label}.</span> 
                             <span className="math-container" style={{ flex: 1, wordBreak: 'break-word' }}>{preprocessMathText(opt)}</span>
                           </div>
                         );
                       })}
                    </div>
                  )}

                  {/* Correct Answers Banner */}
                  {(q.correctAnswer || (q.correctAnswers && q.correctAnswers.length > 0)) && (
                    <div style={{ fontSize: '11.5px', color: 'var(--success)', fontWeight: 700, padding: '4px 8px', background: 'rgba(16, 185, 129, 0.08)', borderRadius: 'var(--radius-sm)', border: '1px solid rgba(16, 185, 129, 0.2)', width: '100%' }}>
                      ✓ Correct Answer: <span className="math-container" style={{ fontWeight: 600 }}>{preprocessMathText(q.correctAnswers && q.correctAnswers.length > 0 ? q.correctAnswers.join(', ') : q.correctAnswer)}</span>
                    </div>
                  )}

                  {/* Proctoring Settings */}
                  <div style={{ marginTop: '2px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '10.5px', cursor: 'pointer', userSelect: 'none', color: 'var(--text-muted)' }}>
                      <input 
                        type="checkbox"
                        checked={!!(q as any).relaxProctoring}
                        onChange={(e) => {
                          const checked = e.target.checked;
                          setGeneratedQuestions(prev => {
                            const next = [...prev];
                            next[idx] = { ...next[idx], relaxProctoring: checked } as any;
                            return next;
                          });
                        }}
                        style={{ cursor: 'pointer', width: '12px', height: '12px' }}
                      />
                      <span>Relax Camera Proctoring (Calculations required)</span>
                    </label>
                  </div>

                  {/* Editable Keywords & Solution Preview */}
                  {(q.type === 'subjective' || q.type === 'subjective_short' || q.type === 'subjective_long' || q.solution) && (
                    <div style={{ marginTop: '6px', padding: '12px 14px', background: 'var(--surface)', borderRadius: '6px', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '8px', fontSize: '12px', width: '100%' }}>
                      <div>
                        <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--accent)', marginBottom: '4px' }}>
                          🏷️ Essential Keywords / Key Phrases for Subject (Comma-Separated):
                        </label>
                        <input 
                          type="text"
                          className="form-input"
                          placeholder="e.g. centripetal force, directed towards center, gravitational force"
                          value={Array.isArray(q.keywords) ? q.keywords.join(', ') : (q.keywords || '')}
                          onChange={(e) => {
                            const kwList = e.target.value.split(',').map(s => s.trim()).filter(Boolean);
                            setGeneratedQuestions(prev => {
                              const next = [...prev];
                              next[idx] = { ...next[idx], keywords: kwList };
                              return next;
                            });
                          }}
                          style={{ width: '100%', padding: '6px 10px', fontSize: '12px', borderRadius: '4px', background: 'var(--bg-soft)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                        />
                      </div>

                      {q.solution && (
                        <div style={{ marginTop: '4px', fontSize: '12px', lineHeight: 1.6, padding: '10px 12px', background: 'var(--bg-soft)', borderRadius: '6px', border: '1px solid var(--border-light)', width: '100%' }}>
                          <strong style={{ display: 'block', fontSize: '11px', textTransform: 'uppercase', color: 'var(--accent)', marginBottom: '4px', letterSpacing: '0.4px' }}>
                            💡 Model Answer & Solution Explanation:
                          </strong>
                          <div 
                            className="math-container"
                            dangerouslySetInnerHTML={{ 
                              __html: highlightModelAnswerKeywords(q.solution, q.keywords) 
                            }} 
                            style={{ wordBreak: 'break-word' }}
                          />
                        </div>
                      )}
                    </div>
                  )}
                </div>
              ))}
            </div>

            {/* Exam compilation trigger */}
            <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px', borderTop: '1px solid var(--border-light)', paddingTop: '15px' }}>
              <button className="btn btn-primary" onClick={handleSaveExam} disabled={savingExam} style={{ padding: '12px 40px' }}>
                {savingExam ? '💾 Saving Exam...' : '💾 Create & Save Exam'}
              </button>
            </div>
          </div>
        )}
      </main>

      {/* In-Place Shortfall AI Generation Modal */}
      {showShortfallModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.55)', backdropFilter: 'blur(6px)', WebkitBackdropFilter: 'blur(6px)', zIndex: 30000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '16px' }}>
          <div style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-popover)', maxWidth: '800px', width: '100%', maxHeight: '90vh', display: 'flex', flexDirection: 'column', overflow: 'hidden', boxShadow: 'var(--shadow-xl)' }}>
            
            <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <h3 style={{ fontSize: '15px', fontWeight: 800, margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span>⚡ In-Place AI Question Generator</span>
                  <span style={{ fontSize: '11px', background: 'var(--warning-bg)', color: 'var(--warning)', padding: '2px 8px', borderRadius: '12px' }}>
                    {shortfalls.reduce((s, r) => s + r.count, 0)} Questions Missing
                  </span>
                </h3>
                <p style={{ margin: '3px 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>
                  Generate and save missing questions directly without losing your exam configuration.
                </p>
              </div>
              <button 
                onClick={() => setShowShortfallModal(false)}
                style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}
              >
                ✕
              </button>
            </div>

            <div style={{ padding: '16px 20px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '16px', flex: 1 }}>
              {/* Prompt box */}
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                  <label style={{ fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', color: 'var(--accent)' }}>
                    1. Copy Tailored AI Prompt (for Gemini / ChatGPT)
                  </label>
                  <button 
                    className="btn btn-secondary btn-sm"
                    onClick={() => {
                      navigator.clipboard.writeText(shortfallAiPrompt);
                      alert('📋 AI Prompt copied to clipboard!');
                    }}
                    style={{ fontSize: '11px', padding: '3px 10px' }}
                  >
                    📋 Copy Prompt
                  </button>
                </div>
                <textarea 
                  value={shortfallAiPrompt}
                  readOnly
                  style={{ width: '100%', height: '150px', background: 'var(--bg-soft)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '10px', fontSize: '11px', fontFamily: 'monospace', color: 'var(--text-muted)' }}
                />
              </div>

              {/* Paste response box */}
              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, textTransform: 'uppercase', color: 'var(--success)', marginBottom: '6px' }}>
                  2. Paste AI JSON Response Array
                </label>
                <textarea 
                  value={shortfallAiPasteText}
                  onChange={(e) => setShortfallAiPasteText(e.target.value)}
                  placeholder="Paste JSON output array from Gemini here..."
                  style={{ width: '100%', height: '140px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '10px', fontSize: '11px', fontFamily: 'monospace', color: 'var(--text)' }}
                />
              </div>

              {shortfallError && (
                <div style={{ padding: '8px 12px', borderRadius: '4px', background: 'rgba(231, 76, 60, 0.1)', color: 'var(--danger)', fontSize: '11px', border: '1px solid var(--danger)' }}>
                  ⚠️ {shortfallError}
                </div>
              )}
            </div>

            <div style={{ padding: '12px 20px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end', gap: '10px', background: 'var(--bg-soft)' }}>
              <button 
                className="btn btn-secondary" 
                onClick={() => setShowShortfallModal(false)}
                disabled={shortfallSaving}
              >
                Cancel
              </button>
              <button 
                className="btn btn-primary"
                onClick={handleParseAndSaveShortfall}
                disabled={shortfallSaving || !shortfallAiPasteText.trim()}
                style={{ padding: '8px 20px' }}
              >
                {shortfallSaving ? '⏳ Saving & Replenishing...' : '⚙️ Parse & Save to Question Bank'}
              </button>
            </div>

          </div>
        </div>
      )}

    </div>
  );
}
