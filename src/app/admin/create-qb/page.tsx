'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter, useSearchParams } from 'next/navigation';
import Script from 'next/script';
import { useMathRender } from '@/hooks/useMathRender';
import { preprocessMathText, robustParseAIJson, validateQuestion, normalizeOptionText, cleanOptionPrefix, cleanStringForMatch, shuffleArray, normalizeBloomLevel, BLOOM_TAXONOMY_MAP } from '@/lib/questionTypes';
import { highlightModelAnswerKeywords } from '@/lib/pdfExport';
import { SyllabusSelector } from '@/components/SyllabusSelector';
import { useSyllabusSelector } from '@/hooks/useSyllabusSelector';
import { distributeCountsByWeight as distributeCountsByWeightLib, buildObjectiveSchema } from '@/lib/syllabusUtils';
import Image from 'next/image';
interface SyllabusEntry {
  docId: string;
  board: string;
  class: string;
  subject: string;
}

interface Template {
  id: string;
  name: string;
  type: string; // 'exam' | 'qb'
  totalQuestions: number;
  difficulty: { easy: number; medium: number; hard: number };
  bloom: { r: number; u: number; ap: number; an: number; e: number; c: number };
  typeCounts?: { [key: string]: number };
}

interface ExamBlueprint {
  id: string;
  name: string;
  icon: string;
  type: 'objective' | 'subjective';
  typeRatios: Record<string, number>;
  difficulty: { easy: number; medium: number; hard: number };
  examCategory?: 'standard' | 'foundation';
  description: string;
}

const CANONICAL_QB_OBJECTIVE_BLUEPRINTS: ExamBlueprint[] = [
  {
    id: 'daily_topic',
    name: 'Daily Topic Test',
    icon: '⚡',
    type: 'objective',
    typeRatios: { single_mcq: 60, assertion_reason: 15, multiple_mcq: 15, numerical: 10 },
    difficulty: { easy: 30, medium: 50, hard: 20 },
    examCategory: 'standard',
    description: '60% Single Choice • 15% Assertion-Reason • 15% Multi Choice • 10% Numerical (or conceptual MCQ for non-numerical topics)'
  },
  {
    id: 'chapter_mastery',
    name: 'Chapter Mastery',
    icon: '📖',
    type: 'objective',
    typeRatios: { single_mcq: 60, assertion_reason: 15, multiple_mcq: 15, numerical: 10 },
    difficulty: { easy: 20, medium: 50, hard: 30 },
    examCategory: 'standard',
    description: '60% Single Choice • 15% Assertion-Reason • 15% Multi Choice • 10% Numerical (20% Easy • 50% Med • 30% Hard)'
  },
  {
    id: 'foundation_olympiad',
    name: 'Foundation / Olympiad Mock',
    icon: '🏆',
    type: 'objective',
    typeRatios: { single_mcq: 60, assertion_reason: 20, multiple_mcq: 10, numerical: 10 },
    difficulty: { easy: 10, medium: 40, hard: 50 },
    examCategory: 'foundation',
    description: 'HOTS Application • 60% Single Choice • 20% Assertion-Reason • 10% Multi • 10% Numerical (50% Hard)'
  },
  {
    id: 'quick_revision',
    name: 'Quick Practice Quiz',
    icon: '🎯',
    type: 'objective',
    typeRatios: { single_mcq: 65, assertion_reason: 20, numerical: 15 },
    difficulty: { easy: 40, medium: 40, hard: 20 },
    examCategory: 'standard',
    description: '65% Single Choice • 20% Assertion-Reason • 15% Numerical (40% Easy • 40% Med • 20% Hard)'
  },
  {
    id: 'custom_blueprint',
    name: 'Custom Blueprint',
    icon: '🛠️',
    type: 'objective',
    typeRatios: { single_mcq: 100 },
    difficulty: { easy: 33, medium: 34, hard: 33 },
    description: 'Standard MCQ mix with custom difficulty'
  }
];

const CANONICAL_QB_SUBJECTIVE_BLUEPRINTS: ExamBlueprint[] = [
  {
    id: 'daily_subjective',
    name: 'Daily Subjective Practice',
    icon: '✍️',
    type: 'subjective',
    typeRatios: { subjective_short: 65, subjective_long: 35 },
    difficulty: { easy: 30, medium: 50, hard: 20 },
    description: '65% Short Answers (2 Marks) • 35% Long Answers (4 Marks)'
  },
  {
    id: 'saturday_classroom',
    name: 'Saturday Classroom Test',
    icon: '🏫',
    type: 'subjective',
    typeRatios: { subjective_define: 20, subjective_short: 50, subjective_long: 30 },
    difficulty: { easy: 20, medium: 50, hard: 30 },
    description: '20% Definitions/Laws (1M) • 50% Short Answers (2M) • 30% Long/Numerical (4M)'
  },
  {
    id: 'comprehensive_subjective',
    name: 'Comprehensive Paper',
    icon: '📚',
    type: 'subjective',
    typeRatios: { subjective_define: 15, subjective_laws: 15, subjective_short: 35, subjective_long: 25, numerical_long: 10 },
    difficulty: { easy: 20, medium: 50, hard: 30 },
    description: 'Definitions, Laws, Short Answers, Long Answers & Multi-step Numericals'
  },
  {
    id: 'custom_subjective',
    name: 'Custom Subjective',
    icon: '🛠️',
    type: 'subjective',
    typeRatios: { subjective_short: 60, subjective_long: 40 },
    difficulty: { easy: 33, medium: 34, hard: 33 },
    description: 'Custom distribution of subjective question types'
  }
];

interface SelectedSubjectData {
  selected: boolean;
  weightage: number;
}

interface ChapterItem {
  subject: string;
  chapter: any;
  chapterName: string;
  chapterNumber: string;
  objectiveCount?: number;
  subjectiveCount?: number;
}

interface TopicItem {
  chapterIdx: number;
  subject: string;
  chapterName: string;
  chapterNumber: string;
  topic: string;
  topicNumber: string;
  objectiveCount?: number;
  subjectiveCount?: number;
  targetQuestions?: number;
  hasSubtopics?: boolean;
}

function CreateQBContent() {
  const { firebaseUser } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();
  const searchParams = useSearchParams();
  const paramBoard = searchParams.get('board') || '';
  const paramClass = searchParams.get('classNum') || '';
  const paramSubject = searchParams.get('subject') || '';
  const paramChapter = searchParams.get('chapter') || '';
  const paramTopic = searchParams.get('topic') || '';
  const paramRequirements = searchParams.get('requirements') || '';

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Syllabus and configuration metadata
  const [syllabusIndex, setSyllabusIndex] = useState<any>(null);
  const [boardCodes, setBoardCodes] = useState<Record<string, string>>({});
  const [subjectCodes, setSubjectCodes] = useState<Record<string, string>>({});
  const [boards, setBoards] = useState<string[]>([]);

  const {
    selectedBoard, setSelectedBoard,
    selectedClass, setSelectedClass,
    availableSubjects, setAvailableSubjects,
    selectedSubjects, setSelectedSubjects,
    availableChapters: currentChapters, setAvailableChapters: setCurrentChapters,
    selectedChapters, setSelectedChapters,
    availableTopics: currentAllTopics, setAvailableTopics: setCurrentAllTopics,
    selectedTopics, setSelectedTopics,
    classes, setClasses,
    handleBoardChange,
    handleClassChange,
    handleToggleSubject,
    handleToggleChapter,
    handleSelectAllChapters,
    handleDeselectAllChapters,
    handleToggleTopic,
    handleSelectAllTopics,
    handleDeselectAllTopics
  } = useSyllabusSelector<TopicItem, Record<string, SelectedSubjectData>>({
    syllabusIndex,
    initialSelectedSubjects: {},
    emptySelectedSubjects: {}
  });

  // Canonical Blueprint selection state
  const [selectedBlueprintId, setSelectedBlueprintId] = useState<string>('chapter_mastery');

  // Topic Distribution and Custom Counts State
  const [weightageMode, setWeightageMode] = useState<'equal' | 'custom'>('equal');
  const [topicWeightageMode, setTopicWeightageMode] = useState<'custom_counts' | 'equal' | 'percentage'>('custom_counts');
  const [topicWeightageMap, setTopicWeightageMap] = useState<Record<string, number | string>>({});
  const [topicCustomCounts, setTopicCustomCounts] = useState<Record<string, number | string>>({});
  const [defaultPerTopicCount, setDefaultPerTopicCount] = useState<number | string>(10);
  const [totalBatchQuestions, setTotalBatchQuestions] = useState<number | string>(30);







  // Image Upload State
  const [uploadedImageBase64, setUploadedImageBase64] = useState<string | null>(null);

  // Question Type and Generation settings
  const [questionType, setQuestionType] = useState<'all_in_one' | 'dual_track' | 'objective' | 'subjective'>('all_in_one');
  const [examCategory, setExamCategory] = useState<'standard' | 'foundation'>('standard');
  const [masterObjectiveRatio, setMasterObjectiveRatio] = useState<number>(70);
  const [dualTrackStandardRatio, setDualTrackStandardRatio] = useState<number>(70);

  useEffect(() => {
    const qtype = searchParams.get('questionType');
    if (qtype === 'subjective' || qtype === 'objective' || qtype === 'all_in_one' || qtype === 'dual_track') {
      setQuestionType(qtype as any);
    }
  }, [searchParams]);

  // Manual Paste Workspace
  const [aiPrompt, setAiPrompt] = useState('');
  const [aiPasteText, setAiPasteText] = useState('');
  const [generatedQuestions, setGeneratedQuestions] = useState<any[]>([]);
  const [previewFilter, setPreviewFilter] = useState<'all' | 'issues'>('all');
  useMathRender([generatedQuestions]);



  // Bulk save stats
  const [savingProgress, setSavingProgress] = useState(false);
  const [savePercentage, setSavePercentage] = useState(0);
  const [saveStats, setSaveStats] = useState({ current: 0, total: 0 });

  // Themed Custom Dialogs
  const [showConfirmModal, setShowConfirmModal] = useState(false);
  const [confirmTitle, setConfirmTitle] = useState('');
  const [confirmMessage, setConfirmMessage] = useState('');
  const [onConfirmCallback, setOnConfirmCallback] = useState<(() => void) | null>(null);
  const [onCancelCallback, setOnCancelCallback] = useState<(() => void) | null>(null);

  const [showAlertModal, setShowAlertModal] = useState(false);
  const [alertTitle, setAlertTitle] = useState('');
  const [alertMessage, setAlertMessage] = useState('');
  const [onAlertCloseCallback, setOnAlertCloseCallback] = useState<(() => void) | null>(null);
  const [alertHasOkButton, setAlertHasOkButton] = useState(true);

  const triggerConfirm = (title: string, msg: string, onConfirm: () => void, onCancel?: () => void) => {
    setConfirmTitle(title);
    setConfirmMessage(msg);
    setOnConfirmCallback(() => onConfirm);
    setOnCancelCallback(() => onCancel || null);
    setShowConfirmModal(true);
  };

  const triggerAlert = (
    title: string, 
    msg: string, 
    onClose?: () => void, 
    showOk = true, 
    autoCloseMs?: number
  ) => {
    setAlertTitle(title);
    setAlertMessage(msg);
    setOnAlertCloseCallback(() => onClose || null);
    setAlertHasOkButton(showOk);
    setShowAlertModal(true);

    if (autoCloseMs) {
      setTimeout(() => {
        setShowAlertModal(prev => {
          if (prev) {
            if (onClose) onClose();
          }
          return false;
        });
      }, autoCloseMs);
    }
  };

  // Load syllabus and templates index on init
  const loadInitialConfig = async () => {
    if (!firebaseUser) return;
    setLoading(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/exams/generate', {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) throw new Error('Failed to load initial configurations.');
      const data = await res.json();
      setSyllabusIndex(data.syllabusSubjects || { subjects: {} });
      setBoardCodes(data.boardCodes || {});
      setSubjectCodes(data.subjectCodes || {});
      
      const uniqueBoards = data.syllabusSubjects?.subjects ? Object.keys(data.syllabusSubjects.subjects).sort() : [];
      setBoards(uniqueBoards);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error loading configurations.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (firebaseUser) {
      loadInitialConfig();
    }
  }, [firebaseUser]);



  // Pre-fill cascade based on query parameters
  useEffect(() => {
    if (!syllabusIndex) return;

    // Resolve Board from code (e.g. "MH" -> "Maharashtra Board")
    let resolvedBoard = paramBoard;
    if (paramBoard) {
      if (syllabusIndex.subjects?.[paramBoard]) {
        resolvedBoard = paramBoard;
      } else if (boardCodes) {
        const match = Object.entries(boardCodes).find(([k, v]) => v.toLowerCase() === paramBoard.toLowerCase() || k.toLowerCase() === paramBoard.toLowerCase());
        if (match && syllabusIndex.subjects?.[match[0]]) {
          resolvedBoard = match[0];
        }
      }
    }

    // Resolve Subject from code (e.g. "SCIT1" -> "Science and Technology Part 1")
    let resolvedSubject = paramSubject;
    if (paramSubject && subjectCodes) {
      const match = Object.entries(subjectCodes).find(([k, v]) => v.toLowerCase() === paramSubject.toLowerCase() || k.toLowerCase() === paramSubject.toLowerCase());
      if (match) {
        resolvedSubject = match[0];
      }
    }

    if (resolvedBoard && syllabusIndex.subjects?.[resolvedBoard]) {
      setSelectedBoard(resolvedBoard);
      const filteredClasses = Object.keys(syllabusIndex.subjects[resolvedBoard]).sort((a, b) => parseInt(a) - parseInt(b));
      setClasses(filteredClasses);

      if (paramClass && syllabusIndex.subjects[resolvedBoard][paramClass]) {
        setSelectedClass(paramClass);
        const filteredSubjects = Object.keys(syllabusIndex.subjects[resolvedBoard][paramClass]).sort();
        setAvailableSubjects(filteredSubjects);

        // Robust matching for subject
        let matchedSubject = '';
        if (resolvedSubject) {
          // 1. Exact match
          if (filteredSubjects.includes(resolvedSubject)) {
            matchedSubject = resolvedSubject;
          }
          // 2. Case-insensitive match
          else if (filteredSubjects.find(s => s.toLowerCase() === resolvedSubject.toLowerCase())) {
            matchedSubject = filteredSubjects.find(s => s.toLowerCase() === resolvedSubject.toLowerCase())!;
          }
          // 3. subjectCodes match
          else if (subjectCodes) {
            const byCode = filteredSubjects.find(s => subjectCodes[s]?.toLowerCase() === paramSubject.toLowerCase());
            if (byCode) matchedSubject = byCode;
          }
          // 4. Prefix / Fuzzy match (e.g. GANI -> Ganit Prakash 1, SCIT1 -> Science and Technology Part 1)
          if (!matchedSubject && paramSubject) {
            const pUpper = paramSubject.toUpperCase();
            const fuzzy = filteredSubjects.find(s => {
              const sUpper = s.toUpperCase();
              return sUpper.includes(pUpper) ||
                pUpper.includes(sUpper.substring(0, 3)) ||
                (pUpper.startsWith('GAN') && sUpper.startsWith('GANIT')) ||
                (pUpper.startsWith('MATH') && sUpper.startsWith('MATH')) ||
                (pUpper.startsWith('MGP') && sUpper.startsWith('GANIT')) ||
                (pUpper.startsWith('SCI') && sUpper.startsWith('SCI'));
            });
            if (fuzzy) matchedSubject = fuzzy;
          }
        }

        // If only 1 subject available in class
        if (!matchedSubject && filteredSubjects.length === 1) {
          matchedSubject = filteredSubjects[0];
        }

        if (matchedSubject) {
          setSelectedSubjects({
            [matchedSubject]: { selected: true, weightage: 100 }
          });
        }
      }
    }
  }, [syllabusIndex, boardCodes, subjectCodes, paramBoard, paramClass, paramSubject]);

  useEffect(() => {
    if (currentChapters.length === 0 || !paramChapter) return;

    const chaptersList = String(paramChapter).split(',');
    const newSelectedChapters = new Set<number>();
    currentChapters.forEach((ch, idx) => {
      if (chaptersList.includes(String(ch.chapterNumber))) {
        newSelectedChapters.add(idx);
      }
    });
    if (newSelectedChapters.size > 0) {
      setSelectedChapters(newSelectedChapters);
    }
  }, [currentChapters, paramChapter]);

  useEffect(() => {
    if (currentAllTopics.length === 0 || !paramTopic) return;

    const topicsList = String(paramTopic).split(',');
    const matchedTopics = currentAllTopics.filter(t => topicsList.includes(String(t.topicNumber)));
    if (matchedTopics.length > 0) {
      setSelectedTopics(matchedTopics);
    }
  }, [currentAllTopics, paramTopic]);



  useEffect(() => {
    if (paramRequirements && selectedTopics.length > 0 && !aiPrompt) {
      const text = compilePrompt(questionType);
      if (text) {
        setAiPrompt(text);
        
        const scrollTarget = () => {
          setTimeout(() => {
            document.getElementById('paste-response-card')?.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }, 300);
        };

        // Auto-copy to clipboard
        try {
          navigator.clipboard.writeText(text)
            .then(() => {
              triggerAlert('Success', '⚡ Prompt generated from student request and copied to clipboard successfully!', undefined, false, 1500);
              scrollTarget();
            })
            .catch(() => {
              const ta = document.createElement('textarea');
              ta.value = text;
              ta.style.position = 'fixed';
              ta.style.opacity = '0';
              document.body.appendChild(ta);
              ta.focus();
              ta.select();
              document.execCommand('copy');
              document.body.removeChild(ta);
              triggerAlert('Success', '⚡ Prompt generated from student request and copied to clipboard successfully!', undefined, false, 1500);
              scrollTarget();
            });
        } catch {
          const ta = document.createElement('textarea');
          ta.value = text;
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.focus();
          ta.select();
          document.execCommand('copy');
          document.body.removeChild(ta);
          triggerAlert('Success', '⚡ Prompt generated from student request and copied to clipboard successfully!', undefined, false, 1500);
          scrollTarget();
        }
      }
    }
  }, [paramRequirements, selectedTopics, aiPrompt, questionType]);






  // Synchronize chapter loading when selectedSubjects changes
  useEffect(() => {
    triggerLoadChapters(selectedSubjects);
  }, [selectedSubjects]);

  // Triggers background loading of chapters map
  const triggerLoadChapters = async (subMap: Record<string, SelectedSubjectData>) => {
    const subjects = Object.keys(subMap);
    if (!subjects.length) {
      setCurrentChapters([]);
      setSelectedChapters(new Set());
      setCurrentAllTopics([]);
      setSelectedTopics([]);
      return;
    }

    const allChapters: ChapterItem[] = [];
    try {
      const idToken = await firebaseUser!.getIdToken();
      await Promise.all(
        subjects.map(async (subject) => {
          const entry = syllabusIndex.subjects?.[selectedBoard]?.[selectedClass]?.[subject];
          if (entry && entry.docId) {
            const res = await fetch(`/api/admin/exams/generate?docId=${entry.docId}`, {
              headers: { 'Authorization': `Bearer ${idToken}` }
            });
            if (res.ok) {
              const data = await res.json();
              if (data.chapters) {
                data.chapters.forEach((ch: any) => {
                  allChapters.push({
                    subject,
                    chapter: ch,
                    chapterName: ch.name || `Chapter ${ch.number}`,
                    chapterNumber: String(ch.number || ''),
                    objectiveCount: ch.objectiveCount || 0,
                    subjectiveCount: ch.subjectiveCount || 0
                  });
                });
              }
            }
          }
        })
      );
      setCurrentChapters(allChapters);
      setSelectedChapters(new Set());
      setCurrentAllTopics([]);
      setSelectedTopics([]);
    } catch (err) {
      console.error('Error loading chapters:', err);
    }
  };

  // Render topics list for checked chapters
  useEffect(() => {
    if (selectedChapters.size === 0) {
      setCurrentAllTopics([]);
      setSelectedTopics([]);
      return;
    }

    const allTopics: TopicItem[] = [];
    selectedChapters.forEach((chIdx) => {
      const item = currentChapters[chIdx];
      if (!item) return;

      const extractTopicsRecursively = (topicsList: any[], prefix = '') => {
        (topicsList || []).forEach(t => {
          const hasSubs = Array.isArray(t.subtopics) && t.subtopics.length > 0;
          const n = (t.number ? t.number + ' ' : '') + (t.name || (typeof t === 'string' ? t : ''));
          const fullName = prefix + n.trim();
          if (n.trim()) {
            if (!allTopics.some(at => at.topic === fullName && at.subject === item.subject)) {
              const subsTargetSum = hasSubs
                ? t.subtopics.reduce((acc: number, s: any) => acc + (Number(typeof s === 'object' ? s.targetQuestions : 0) || 30), 0)
                : 0;

              allTopics.push({
                chapterIdx: chIdx,
                subject: item.subject,
                chapterName: item.chapter.name || '',
                chapterNumber: String(item.chapter.number || ''),
                topic: fullName,
                topicNumber: (fullName.match(/^\s*([0-9]+(?:\.[0-9]+)+)/) || [, ''])[1] || String(t.number || ''),
                objectiveCount: t.objectiveCount || 0,
                subjectiveCount: t.subjectiveCount || 0,
                targetQuestions: hasSubs ? subsTargetSum : (t.targetQuestions || 30),
                hasSubtopics: hasSubs
              });
            }
          }
          if (hasSubs) {
            extractTopicsRecursively(t.subtopics, prefix + '  ');
          }
        });
      };

      extractTopicsRecursively(item.chapter.topics || []);
    });

    setCurrentAllTopics(allTopics);
    // Keep only topics that are still valid in currentAllTopics
    setSelectedTopics(prev => prev.filter(p => allTopics.some(a => a.topic === p.topic)));
  }, [selectedChapters, currentChapters]);

  // Topic key compiler
  const topicKey = (t: TopicItem) => `${t.subject}_ch${t.chapterNumber}_${t.topic}`;

  // Topic weightage & custom counts handlers
  const handleTopicWeightChange = (topic: TopicItem, val: number | string) => {
    const key = topicKey(topic);
    setTopicWeightageMap(prev => ({ ...prev, [key]: val }));
  };

  const handleTopicCustomCountChange = (topic: TopicItem, val: number | string) => {
    const key = topicKey(topic);
    setTopicCustomCounts(prev => ({ ...prev, [key]: val }));
  };

  const getSelectedBlueprint = (): ExamBlueprint => {
    const list = questionType === 'subjective' ? CANONICAL_QB_SUBJECTIVE_BLUEPRINTS : CANONICAL_QB_OBJECTIVE_BLUEPRINTS;
    return list.find(b => b.id === selectedBlueprintId) || list[0];
  };

  const handleSwitchType = (type: 'all_in_one' | 'dual_track' | 'objective' | 'subjective') => {
    setQuestionType(type);
    if (type === 'subjective') {
      setSelectedBlueprintId('saturday_classroom');
    } else if (type === 'dual_track') {
      setSelectedBlueprintId('chapter_mastery');
      setDefaultPerTopicCount(90);
      const newCounts: Record<string, number> = {};
      selectedTopics.forEach(t => { newCounts[topicKey(t)] = 90; });
      setTopicCustomCounts(newCounts);
    } else {
      setSelectedBlueprintId('chapter_mastery');
    }
  };

  const getPromptTargetTopics = (): TopicItem[] => {
    const leafTopics: TopicItem[] = [];
    selectedTopics.forEach(st => {
      if (!st.hasSubtopics) {
        leafTopics.push(st);
      } else {
        // Expand parent topic to its child subtopics so the parent sum is NEVER passed as a generation target
        const childSubs = currentAllTopics.filter(
          at => !at.hasSubtopics && at.subject === st.subject && at.chapterNumber === st.chapterNumber && at.topicNumber.startsWith(st.topicNumber + '.')
        );
        if (childSubs.length > 0) {
          childSubs.forEach(cs => {
            if (!leafTopics.some(lt => lt.topic === cs.topic && lt.subject === cs.subject)) {
              leafTopics.push(cs);
            }
          });
        } else {
          leafTopics.push(st);
        }
      }
    });
    return leafTopics.length > 0 ? leafTopics : selectedTopics;
  };

  const getEffectiveTopicCounts = (): Record<string, number> => {
    const map: Record<string, number> = {};
    const fallbackCount = typeof defaultPerTopicCount === 'number' ? defaultPerTopicCount : (parseInt(String(defaultPerTopicCount), 10) || 30);
    const promptTopics = getPromptTargetTopics();

    if (topicWeightageMode === 'custom_counts') {
      promptTopics.forEach(t => {
        const k = topicKey(t);
        const raw = topicCustomCounts[k];
        const val = typeof raw === 'number' ? raw : (raw !== undefined && raw !== '' ? (parseInt(String(raw), 10) || fallbackCount) : (t.targetQuestions || fallbackCount));
        map[k] = val;
      });
    } else if (topicWeightageMode === 'equal') {
      promptTopics.forEach(t => {
        const k = topicKey(t);
        map[k] = fallbackCount;
      });
    } else {
      // Percentage mode
      const total = typeof totalBatchQuestions === 'number' ? totalBatchQuestions : (parseInt(String(totalBatchQuestions), 10) || 30);
      const cleanWeightMap: Record<string, number> = {};
      promptTopics.forEach(t => {
        const k = topicKey(t);
        const raw = topicWeightageMap[k];
        cleanWeightMap[k] = typeof raw === 'number' ? raw : (parseInt(String(raw), 10) || 0);
      });
      return distributeCountsByWeightLib(
        total,
        promptTopics,
        cleanWeightMap,
        'custom',
        topicKey
      );
    }
    return map;
  };

  const getTotalTargetQuestions = (): number => {
    const fallbackCount = typeof defaultPerTopicCount === 'number' ? defaultPerTopicCount : (parseInt(String(defaultPerTopicCount), 10) || 30);
    const promptTopics = getPromptTargetTopics();

    if (topicWeightageMode === 'custom_counts') {
      return promptTopics.reduce((sum, top) => {
        const k = topicKey(top);
        const raw = topicCustomCounts[k];
        const val = typeof raw === 'number' ? raw : (raw !== undefined && raw !== '' ? (parseInt(String(raw), 10) || fallbackCount) : (top.targetQuestions || fallbackCount));
        return sum + val;
      }, 0);
    }
    if (topicWeightageMode === 'equal') {
      return promptTopics.length * fallbackCount;
    }
    const total = typeof totalBatchQuestions === 'number' ? totalBatchQuestions : (parseInt(String(totalBatchQuestions), 10) || 30);
    return total;
  };

  // Image Upload helper conversion
  const handleImageSelected = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (event) => {
      setUploadedImageBase64(event.target?.result as string);
    };
    reader.readAsDataURL(file);
  };

  const clearImage = () => {
    setUploadedImageBase64(null);
    const fileInp = document.getElementById('questionImageInput') as HTMLInputElement;
    if (fileInp) fileInp.value = '';
  };

  const clearAllSelections = () => {
    setSelectedSubjects({});
    setSelectedChapters(new Set());
    setSelectedTopics([]);
    setTopicWeightageMap({});
    setTopicCustomCounts({});
    setTopicWeightageMode('custom_counts');
    clearImage();
  };

  // Subject counts
  const getSelectedSubjectsList = () => Object.keys(selectedSubjects);
  const getSelectedSubjectsCount = () => getSelectedSubjectsList().length;

  const getWeightageMap = () => {
    const weightMap: Record<string, number> = {};
    let total = 0;
    const list = getSelectedSubjectsList();
    if (weightageMode === 'equal') {
      const eq = Math.floor(100 / (list.length || 1));
      list.forEach(s => {
        weightMap[s] = eq;
        total += eq;
      });
    } else {
      list.forEach(s => {
        const w = selectedSubjects[s]?.weightage || 0;
        weightMap[s] = w;
        total += w;
      });
    }
    return { weightMap, total };
  };

  const getTopicWeightageTotal = () => {
    return selectedTopics.reduce((sum, top) => {
      const raw = topicWeightageMap[topicKey(top)];
      const w = typeof raw === 'number' ? raw : (parseInt(String(raw), 10) || 0);
      return sum + (raw !== undefined && raw !== '' ? w : Math.floor(100 / (selectedTopics.length || 1)));
    }, 0);
  };

  // Distribute questions count by weight
  const distributeCountsByWeight = (totalQs: number) => {
    const cleanWeightMap: Record<string, number> = {};
    const promptTopics = getPromptTargetTopics();
    promptTopics.forEach(t => {
      const k = topicKey(t);
      const raw = topicWeightageMap[k];
      cleanWeightMap[k] = typeof raw === 'number' ? raw : (parseInt(String(raw), 10) || 0);
    });
    return distributeCountsByWeightLib(
      totalQs,
      promptTopics,
      cleanWeightMap,
      topicWeightageMode === 'percentage' ? 'custom' : 'equal',
      topicKey
    );
  };

  const buildTopicsContextBlock = (countsMap: Record<string, number> | null) => {
    (window as any).questionContextLookup = {};
    const promptTopics = getPromptTargetTopics();
    return promptTopics.map((t, idx) => {
      const cid = 'CTX-' + String(idx + 1).padStart(3, '0');
      (window as any).questionContextLookup[cid] = {
        subject: t.subject || '',
        chapterName: t.chapterName || '',
        chapterNumber: t.chapterNumber || '',
        topic: t.topic || '',
        topicNumber: t.topicNumber || ''
      };
      const count = countsMap ? countsMap[topicKey(t)] : (t.targetQuestions || defaultPerTopicCount || 30);
      const countLine = (count !== null && count !== undefined) ? `\nMandatory questions to generate for this topic: ${count}` : '';
      return `contextId: ${cid}\nSubject: ${t.subject || ''}\nChapter: ${t.chapterName || ''}\nChapter Number: ${t.chapterNumber || ''}\nTopic: ${t.topic || ''}\nTopic Number: ${t.topicNumber || ''}${countLine}`;
    }).join('\n\n');
  };

  const buildImageInstruction = () => {
    if (!uploadedImageBase64) return '';
    return `
========================================
IMAGE-BASED QUESTION EXTRACTION
========================================
An image has been provided (textbook page / diagram / question paper).
In addition to the topic-based questions:
- Extract and adapt any questions visible in the image.
- For diagram-based questions, describe the diagram in the "text" field.
- Tag image-extracted questions with "source": "image_extracted".
`;
  };

  // Compile prompt string
  const compilePrompt = (type: 'all_in_one' | 'dual_track' | 'objective' | 'subjective') => {
    if (!selectedBoard || !selectedClass || getSelectedSubjectsCount() === 0 || selectedTopics.length === 0) {
      return '';
    }

    const subj = getSelectedSubjectsList()[0] || '';
    const isMath = /math|algebra|geometry|ganit/i.test(subj);
    const blueprint = getSelectedBlueprint();
    const isFoundation = examCategory === 'foundation' || blueprint.examCategory === 'foundation';
    const totalQs = getTotalTargetQuestions() || 10;
    const topicCounts = getEffectiveTopicCounts();
    const ctx = buildTopicsContextBlock(topicCounts);
    const promptTopics = getPromptTargetTopics();

    let requirementsSection = '';
    if (paramRequirements) {
      requirementsSection = `\n========================================\nCONSOLIDATED STUDENT REQUESTED REQUIREMENTS:\n========================================\nPlease generate questions specifically matching these student requested targets:\n${paramRequirements.split(', ').map(r => `- ${r}`).join('\n')}\n`;
    }

    const isCalculativeTopic = isMath || promptTopics.some(t => {
      const text = `${t.subject || ''} ${t.chapter || ''} ${t.topic || ''}`.toLowerCase();
      return /physic|motion|force|gravitat|light|reflection|refraction|electric|current|circuit|sound|work|energy|power|heat|thermodynamic|optics|lens|mirror|wave|mole concept|stoichiometr|density|pressure|floatation|kinematics|fluid|magnetic/i.test(text);
    });

    if (type === 'all_in_one') {
      let topicBreakdownBlock = '';
      promptTopics.forEach((tp, idx) => {
        const k = topicKey(tp);
        const rawCnt = topicCounts[k] !== undefined ? topicCounts[k] : (tp.targetQuestions || defaultPerTopicCount);
        const cnt = typeof rawCnt === 'number' ? rawCnt : (parseInt(String(rawCnt), 10) || 30);
        
        let objC = 0;
        let subC = 0;
        if (masterObjectiveRatio >= 100) {
          objC = cnt;
          subC = 0;
        } else if (masterObjectiveRatio <= 0) {
          objC = 0;
          subC = cnt;
        } else {
          objC = Math.max(1, Math.round(cnt * (masterObjectiveRatio / 100)));
          subC = Math.max(1, cnt - objC);
        }
        
        const easyC = objC > 0 ? Math.max(1, Math.round(objC * 0.30)) : 0;
        const medC = objC > 0 ? Math.max(1, Math.round(objC * 0.50)) : 0;
        const hardC = objC > 0 ? Math.max(0, objC - easyC - medC) : 0;

        const m1C = subC > 0 ? Math.max(1, Math.round(subC * 0.35)) : 0;
        const m2C = subC > 0 ? Math.max(1, Math.round(subC * 0.40)) : 0;
        const m4C = subC > 0 ? Math.max(0, subC - m1C - m2C) : 0;

        let objBlock = '';
        if (objC > 0) {
          objBlock = `\n  A) OBJECTIVE SUITE (${objC} Questions for Adaptive Practice & Exams):\n     • Easy (Foundation / Warmup): ${easyC} questions\n     • Medium (Standard Board Level): ${medC} questions\n     • Hard (HOTS / Traps): ${hardC} questions`;
        }

        let subBlock = '';
        if (subC > 0) {
          const letter = objC > 0 ? 'B' : 'A';
          subBlock = `\n  ${letter}) SUBJECTIVE SUITE (${subC} Questions with Model Answer Solutions & Keywords):\n     • 1-Mark (Definitions / Laws / Formulas): ${m1C} questions (type: "subjective_define" or "subjective_laws")\n     • 2-Mark (Short Answer / Scientific Reasons): ${m2C} questions (type: "subjective_short" or "subjective_reason"${isCalculativeTopic ? ' or "numerical_short"' : ''})\n     • 4-Mark (Long Problems / Proofs / Derivations): ${m4C} questions (type: "subjective_long"${isCalculativeTopic ? ' or "numerical_long"' : ''})`;
        }

        const cid = 'CTX-' + String(idx + 1).padStart(3, '0');
        topicBreakdownBlock += `
------------------------------------------------------------
📍 TOPIC ${idx + 1}: ${tp.topic} (Code: ${tp.topicNumber || ''}) [contextId: "${cid}"]
- Target Questions for this topic: EXACTLY ${cnt} Questions${objBlock}${subBlock}`;
      });

      (window as any).lastPromptMeta = { mode: 'all_in_one', totalQs };

      return `========================================
ROLE AND MASTER TOPIC SUITE GOAL
========================================
Act as an expert curriculum architect, textbook author, and senior exam paper setter for ${selectedBoard} Class ${selectedClass}.

Your mission is to generate the COMPLETE, EXHAUSTIVE Question Bank Suite for the selected topic(s) in a single unified JSON output array.
This question suite will serve BOTH:
1. Official Exam Blueprints (Daily Topic Tests, Chapter Tests, Saturday Classroom Peer-Reviewed Tests).
2. Adaptive Student Practice Engine (Easy/Medium/Hard progressive mastery from Foundation to HOTS).

TOTAL QUESTIONS TO GENERATE: EXACTLY ${totalQs} questions across ${promptTopics.length} topic(s).
${requirementsSection}
========================================
PER-TOPIC COMPREHENSIVE BREAKDOWN & QUOTAS:
========================================
${topicBreakdownBlock}

========================================
QUESTION GENERATION CONTEXT:
========================================
${ctx}

========================================
SUBJECT-ADAPTIVE QUESTION TYPE DISTRIBUTION:
========================================
${isMath ? `
MATHEMATICS SPECIAL RULES:
- Objective Types: ~70% Single Choice Calculation MCQs ("single_mcq"), ~20% Direct Numerical ("numerical" with clean numeric answer, no options), ~10% Assertion-Reason ("assertion_reason").
- Subjective Types: 1-Mark Formulas/Definitions ("subjective_define"), 2-Mark Short Calculations ("numerical_short" or "subjective_short"), 4-Mark Multi-step Problems/Proofs ("numerical_long" or "subjective_long").
- 80% of questions MUST be selected verbatim from official textbook exercises/practice sets. 20% must be similar pattern variants.
- Specify "textbookPracticeSet" key on each question (e.g. "Practice Set 1.2: Q3", "Figure it out 2.1: Q4").
` : `
SCIENCE & GENERAL SPECIAL RULES:
- For Quantitative/Physics/Chemistry Topics: Include clean numerical problems ("numerical", "numerical_short", "numerical_long") with realistic physical values, proper units, and step-by-step solutions.
- For Qualitative/Biology/Descriptive Topics (e.g. Cell, Diversity, Tissues, Plant Movements/Phototropism, Metal Properties, Environment):
  * ZERO FAKE MATH RULE: Strictly DO NOT generate synthetic arithmetic or fake calculations.
  * Instead, focus on deep Conceptual Single MCQs ("single_mcq"), Assertion & Reason ("assertion_reason"), Multiple Correct ("multiple_mcq"), Definitions ("subjective_define"), and Scientific Reasons ("subjective_reason") with marked keywords.
`}

========================================
UNIFIED JSON OUTPUT SCHEMA SPECIFICATION:
========================================
Return a single JSON array where each item conforms to one of the following schemas:

1. Single Choice MCQ (Objective):
{
  "contextId": "CTX-001",
  "type": "single_mcq",
  "text": "Clear question text formatted with KaTeX \\\\( ... \\\\)...",
  "options": ["Option A", "Option B", "Option C", "Option D"],
  "correctAnswer": "Option B",
  "solution": "Step-by-step reasoning explaining why Option B is correct...",
  "difficulty": "easy/medium/hard",
  "bloomLevel": "Remember/Understand/Apply/Analyze",
  "topicOrigin": "${selectedTopics[0]?.topic || ''}",
  "examCategory": "${isFoundation ? 'foundation' : 'standard'}"
}

2. Assertion & Reason (Objective):
{
  "contextId": "CTX-001",
  "type": "assertion_reason",
  "text": "Assertion (A): Statement...\\nReason (R): Statement...",
  "correctAnswer": "A",
  "solution": "Detailed reasoning explaining connection between A and R...",
  "difficulty": "medium/hard",
  "bloomLevel": "Analyze",
  "topicOrigin": "${selectedTopics[0]?.topic || ''}",
  "examCategory": "${isFoundation ? 'foundation' : 'standard'}"
}
(Note: correctAnswer MUST be exactly "A", "B", "C", or "D". Do NOT include options array).

3. Multiple Choice MCQ (Objective with 2+ correct answers):
{
  "contextId": "CTX-001",
  "type": "multiple_mcq",
  "text": "Select all statements that apply...",
  "options": ["Option A", "Option B", "Option C", "Option D"],
  "correctAnswers": ["Option A", "Option C"],
  "solution": "Explanation of correct options...",
  "difficulty": "medium/hard",
  "bloomLevel": "Apply",
  "topicOrigin": "${selectedTopics[0]?.topic || ''}",
  "examCategory": "${isFoundation ? 'foundation' : 'standard'}"
}

4. Direct Numerical Objective (Physics / Chemistry / Math):
{
  "contextId": "CTX-001",
  "type": "numerical",
  "text": "Calculate the magnitude of force when mass is 2 kg and acceleration is 5 m/s²...",
  "correctAnswer": "10",
  "solution": "F = m * a = 2 * 5 = 10 N",
  "difficulty": "medium",
  "bloomLevel": "Apply",
  "topicOrigin": "${selectedTopics[0]?.topic || ''}",
  "examCategory": "${isFoundation ? 'foundation' : 'standard'}"
}
(Note: correctAnswer MUST be a clean numeric string like "10" or "3.14". Do NOT include options array).

5. Subjective Question (1-Mark, 2-Mark, or 4-Mark):
{
  "contextId": "CTX-001",
  "type": "subjective_define",
  "text": "Question statement...",
  "marks": 1,
  "answerLines": [
    { "lineNo": 1, "text": "First key step or point of the model answer" },
    { "lineNo": 2, "text": "Second key step or point of the model answer" }
  ],
  "keywords": ["<mark>essential keyword 1</mark>", "<mark>essential keyword 2</mark>"],
  "solution": "Full complete model answer solution with step-by-step points...",
  "difficulty": "easy/medium/hard",
  "bloomLevel": "Remember/Understand/Apply/Analyze/Evaluate",
  "pyqInfo": "Board PYQ 2023 / High-Yield Textbook Problem",
  "topicOrigin": "${selectedTopics[0]?.topic || ''}",
  "examCategory": "${isFoundation ? 'foundation' : 'standard'}"
}

${buildImageInstruction()}

========================================
CRITICAL RULES & FORMATTING:
========================================
1. Return ONLY a single raw valid JSON array. DO NOT wrap with markdown commentary or intro/outro.
2. Every item MUST include "contextId" matching the topic context (e.g. "CTX-001", "CTX-002", etc.).
3. Math expressions must be in LaTeX format using \\\\( ... \\\\) with double-escaped backslashes. Chemical formulas wrapped in \\\\ce{...}.
4. NO placeholder options, NO synthetic dummy variables, NO repeated sentence loops.
5. RANDOMIZE CORRECT OPTION POSITIONS: Distribute the correct answer position randomly and evenly across option index 0, 1, 2, and 3 (A, B, C, D). Do NOT always place the correct answer as the first item in "options".`;
    }

    if (type === 'dual_track') {
      let topicBreakdownBlock = '';
      promptTopics.forEach((tp, idx) => {
        const k = topicKey(tp);
        const rawCnt = topicCounts[k] !== undefined ? topicCounts[k] : (tp.targetQuestions || defaultPerTopicCount);
        const cnt = typeof rawCnt === 'number' ? rawCnt : (parseInt(String(rawCnt), 10) || 90);
        
        let stdC = 0;
        let fndC = 0;
        if (dualTrackStandardRatio >= 100) {
          stdC = cnt;
          fndC = 0;
        } else if (dualTrackStandardRatio <= 0) {
          stdC = 0;
          fndC = cnt;
        } else {
          stdC = Math.max(1, Math.round(cnt * (dualTrackStandardRatio / 100)));
          fndC = Math.max(1, cnt - stdC);
        }
        
        const stdEasy = stdC > 0 ? Math.max(1, Math.round(stdC * 0.30)) : 0;
        const stdMed = stdC > 0 ? Math.max(1, Math.round(stdC * 0.50)) : 0;
        const stdHard = stdC > 0 ? Math.max(0, stdC - stdEasy - stdMed) : 0;

        const fndEasy = fndC > 0 ? Math.max(1, Math.round(fndC * 0.10)) : 0;
        const fndMed = fndC > 0 ? Math.max(1, Math.round(fndC * 0.40)) : 0;
        const fndHard = fndC > 0 ? Math.max(0, fndC - fndEasy - fndMed) : 0;

        const cid = 'CTX-' + String(idx + 1).padStart(3, '0');
        topicBreakdownBlock += `
------------------------------------------------------------
📍 TOPIC ${idx + 1}: ${tp.topic} (Code: ${tp.topicNumber || ''}) [contextId: "${cid}"]
- Total Target: EXACTLY ${cnt} Questions
  A) 📘 TRACK 1: STANDARD SUITE (${stdC} Questions, "examCategory": "standard"):
     • Purpose: 30-Question Daily Topic Tests & Adaptive Practice Mastery
     • Composition: ~60% Single Choice MCQ, ~15% Assertion-Reason, ~15% Multiple Correct MCQ, ~10% Numerical/Application
     • Difficulty: ${stdEasy} Easy (LOTS/Recall) • ${stdMed} Medium (Standard Board Level) • ${stdHard} Hard (Tricky/Nuance)

  B) 🏆 TRACK 2: FOUNDATION & OLYMPIAD MOCK SUITE (${fndC} Questions, "examCategory": "foundation"):
     • Purpose: Reserved Foundation Mock Tests & HOTS Olympiad Benchmarking (Untouched by daily tests)
     • Composition: ~60% Single Choice HOTS MCQ, ~20% Assertion-Reason HOTS, ~10% Multi-Concept MCQ, ~10% Deep Numerical
     • Difficulty: ${fndEasy} Easy (Concept Check) • ${fndMed} Medium (Cross-topic Synthesis) • ${fndHard} Hard (Olympiad/HOTS Analysis)`;
      });

      (window as any).lastPromptMeta = { mode: 'dual_track', totalQs };

      return `========================================
ROLE AND DUAL-TRACK TOPIC SUITE GOAL
========================================
Act as an expert curriculum architect, textbook author, and senior exam paper setter for ${selectedBoard} Class ${selectedClass}.

Your mission is to generate the COMPLETE DUAL-TRACK OBJECTIVE QUESTION SUITE for the selected topic(s) in a single unified JSON output array.
This question suite fulfills TWO DISTINCT PURPOSES:
1. 📘 TRACK 1: STANDARD SUITE ("examCategory": "standard") — For Daily 30-Q Topic Tests, Adaptive Practice, and Progressive Topic Mastery.
2. 🏆 TRACK 2: FOUNDATION / OLYMPIAD SUITE ("examCategory": "foundation") — Reserved for Olympiad mocks and high-rigor HOTS testing (kept separate from daily tests).

TOTAL QUESTIONS TO GENERATE: EXACTLY ${totalQs} questions across ${promptTopics.length} topic(s).
${requirementsSection}
========================================
PER-TOPIC DUAL-TRACK BREAKDOWN & ALLOCATIONS:
========================================
${topicBreakdownBlock}

========================================
QUESTION GENERATION CONTEXT:
========================================
${ctx}

========================================
SUBJECT-ADAPTIVE RULES & SCIENTIFIC RIGOR:
========================================
${isMath ? `
MATHEMATICS SPECIAL RULES:
- Standard Track: ~70% Single Choice Calculation MCQs ("single_mcq"), ~20% Direct Numerical ("numerical" with clean numeric answer, no options), ~10% Assertion-Reason ("assertion_reason").
- Foundation Track: Deep multi-step algebraic/geometric problem solving, application theorems, and non-routine Olympiad variants.
- Specify "textbookPracticeSet" key where applicable (e.g. "Practice Set 1.2: Q3").
` : `
SCIENCE & GENERAL SPECIAL RULES:
- For Quantitative/Physics/Chemistry Topics: Include clean numerical problems ("numerical") with realistic physical values, proper standard units, and step-by-step mathematical reasoning.
- For Qualitative/Biology/Descriptive Topics (e.g. Cell, Diversity, Tissues, Plant Movements, Metal Properties, Heredity):
  * ZERO FAKE MATH RULE: Strictly DO NOT generate synthetic arithmetic or fake calculations.
  * Instead, generate deep Conceptual Single MCQs ("single_mcq"), Assertion & Reason ("assertion_reason"), and Multiple Correct ("multiple_mcq") testing deep scientific understanding.
`}

========================================
MATHEMATICAL & LATEX FORMATTING RULES:
========================================
1. All math formulas, equations, variables, and units MUST be formatted with KaTeX:
   - Inline Math: \\\\( F = G \\\\frac{m_1 m_2}{r^2} \\\\)
   - Display Math: \\\\[ g = \\\\frac{GM}{R^2} \\\\]
2. "correctAnswer" MUST verbatim match the exact string in "options".

========================================
UNIFIED JSON OUTPUT SCHEMA:
========================================
Return a single JSON array containing all ${totalQs} questions:

[
  {
    "contextId": "CTX-001",
    "type": "single_mcq",
    "examCategory": "standard",
    "text": "When the distance between two bodies is tripled, the gravitational force between them becomes:",
    "options": ["\\\\( 3 \\\\) times", "\\\\( \\\\frac{1}{3} \\\\) times", "\\\\( 9 \\\\) times", "\\\\( \\\\frac{1}{9} \\\\) times"],
    "correctAnswer": "\\\\( \\\\frac{1}{9} \\\\) times",
    "solution": "According to Newton's Law of Gravitation, \\\\( F \\\\propto \\\\frac{1}{r^2} \\\\). When \\\\( r' = 3r \\\\), \\\\( F' = \\\\frac{F}{3^2} = \\\\frac{F}{9} \\\\).",
    "difficulty": "easy",
    "bloomLevel": "Understand",
    "topicOrigin": "${selectedTopics[0]?.topic || ''}"
  },
  {
    "contextId": "CTX-001",
    "type": "assertion_reason",
    "examCategory": "standard",
    "text": "Read the statements and select the correct option.",
    "assertion": "The value of acceleration due to gravity \\\\( g \\\\) is zero at the center of the Earth.",
    "reason": "At the center of the Earth, the mass of Earth attracting a body from all sides cancels out symmetrically.",
    "options": [
      "Both Assertion and Reason are true, and Reason is the correct explanation of Assertion.",
      "Both Assertion and Reason are true, but Reason is NOT the correct explanation of Assertion.",
      "Assertion is true, but Reason is false.",
      "Assertion is false, but Reason is true."
    ],
    "correctAnswer": "Both Assertion and Reason are true, and Reason is the correct explanation of Assertion.",
    "solution": "At the center of the Earth, \\\\( r = 0 \\\\), hence effective gravitational field and \\\\( g \\\\) become zero.",
    "difficulty": "medium",
    "bloomLevel": "Analyze",
    "topicOrigin": "${selectedTopics[0]?.topic || ''}"
  },
  {
    "contextId": "CTX-001",
    "type": "single_mcq",
    "examCategory": "foundation",
    "text": "A hypothetical planet has twice the average density of Earth and radius \\\\( R = 1.5 R_e \\\\). If the escape velocity on Earth is \\\\( v_e \\\\), the escape velocity on this planet will be:",
    "options": ["\\\\( \\\\sqrt{3} v_e \\\\)", "\\\\( 3 v_e \\\\)", "\\\\( \\\\frac{\\\\sqrt{3}}{2} v_e \\\\)", "\\\\( 2.25 v_e \\\\)"],
    "correctAnswer": "\\\\( \\\\sqrt{3} v_e \\\\)",
    "solution": "Escape velocity \\\\( v_e = \\\\sqrt{\\\\frac{2GM}{R}} = \\\\sqrt{\\\\frac{8}{3} \\\\pi G \\\\rho R^2} \\\\propto R\\\\sqrt{\\\\rho} \\\\). Therefore \\\\( \\\\frac{v'}{v} = 1.5 \\\\times \\\\sqrt{2} = \\\\sqrt{2.25 \\\\times 2} = \\\\sqrt{4.5} \\\\approx 2.12 = \\\\sqrt{3} \\\\times 1.22 \\\\).",
    "difficulty": "hard",
    "bloomLevel": "Analyze",
    "topicOrigin": "${selectedTopics[0]?.topic || ''}"
  }
]

${buildImageInstruction()}

========================================
CRITICAL RULES & FORMATTING:
========================================
1. Return ONLY a single raw valid JSON array. DO NOT wrap with markdown commentary or intro/outro.
2. Every item MUST include "contextId" matching the topic context (e.g. "CTX-001", "CTX-002", etc.).
3. Math expressions must be in LaTeX format using \\\\( ... \\\\) with double-escaped backslashes.
4. Set "examCategory" strictly to "standard" for Track 1 and "foundation" for Track 2.
5. RANDOMIZE CORRECT OPTION POSITIONS: Distribute correct answers across options evenly.`;
    }

    if (type === 'objective') {
      const diff = blueprint.difficulty || { easy: 30, medium: 50, hard: 20 };
      const easyC = Math.round((diff.easy / 100) * totalQs);
      const medC = Math.round((diff.medium / 100) * totalQs);
      const hardC = Math.max(0, totalQs - easyC - medC);

      // Compute type counts based on blueprint type ratios (dynamically sanitize for qualitative topics)
      let typeBD = '', typeInst = '', reqTypes: any[] = [];
      const rawRatios = blueprint.typeRatios || { single_mcq: 100 };
      const ratios: Record<string, number> = {};
      let shiftedPct = 0;
      Object.entries(rawRatios).forEach(([tid, pct]) => {
        if (tid === 'numerical' && !isCalculativeTopic) {
          shiftedPct += pct;
        } else {
          ratios[tid] = pct;
        }
      });
      if (shiftedPct > 0) {
        ratios['single_mcq'] = (ratios['single_mcq'] || 0) + shiftedPct;
      }

      let allocatedCount = 0;
      const ratioEntries = Object.entries(ratios);

      ratioEntries.forEach(([tid, pct], idx) => {
        let count = 0;
        if (idx === ratioEntries.length - 1) {
          count = Math.max(0, totalQs - allocatedCount);
        } else {
          count = Math.max(1, Math.round((pct / 100) * totalQs));
          allocatedCount += count;
        }
        if (count > 0) {
          reqTypes.push({ id: tid, count });
          typeBD += `\n- ${tid}: ${count} questions`;
        }
      });

      if (!reqTypes.length) {
        reqTypes = [{ id: 'single_mcq', count: totalQs }];
        typeBD = `\n- single_mcq: ${totalQs} questions (Single Correct MCQ)`;
      }

      (window as any).lastPromptMeta = { mode: 'objective', totalQs, reqTypes: reqTypes.map(rt => ({ ...rt })) };

      let topicDistributionSummary = '\n\n========================================\nPER-TOPIC QUESTION ALLOCATION QUOTAS:\n========================================';
      promptTopics.forEach(tp => {
        const k = topicKey(tp);
        const cnt = topicCounts[k] || 0;
        topicDistributionSummary += `\n- ${tp.subject ? '[' + tp.subject + '] ' : ''}${tp.topic}: EXACTLY ${cnt} questions`;
      });

      reqTypes.forEach(rt => {
        typeInst += `\n\n--- Type: "${rt.id}" (${rt.count} questions across the exam) ---`;
        if (rt.id === 'single_mcq') typeInst += `\nExample: { "contextId":"CTX-001","type":"${rt.id}","text":"Question text...","options":["Option A","Option B","Option C","Option D"],"correctAnswer":"Option B","solution":"Step-by-step reasoning...","difficulty":"easy/medium/hard","bloomLevel":"Understand","topicOrigin":"..." }`;
        else if (rt.id === 'multiple_mcq') typeInst += `\nExample: { "contextId":"CTX-001","type":"${rt.id}","text":"Question with multiple correct options...","options":["Option A","Option B","Option C","Option D"],"correctAnswers":["Option A","Option C"],"solution":"Step-by-step explanation...","difficulty":"medium/hard","bloomLevel":"Apply","topicOrigin":"..." }`;
        else if (rt.id === 'true_false') typeInst += `\nExample: { "contextId":"CTX-001","type":"${rt.id}","text":"Statement to evaluate","correctAnswer":"True","solution":"Reasoning...","difficulty":"easy/medium","bloomLevel":"Remember","topicOrigin":"..." }`;
        else if (rt.id === 'assertion_reason') typeInst += `\nExample: { "contextId":"CTX-001","type":"${rt.id}","text":"Assertion (A): ...\\nReason (R): ...","correctAnswer":"A","solution":"Explain why both are true and R explains A...","difficulty":"medium/hard","bloomLevel":"Analyze","topicOrigin":"..." }\nNote: correctAnswer must be exactly one letter: "A" = both true & R explains A, "B" = both true & R does NOT explain A, "C" = A true & R false, "D" = A false & R true. Do NOT include options array for assertion_reason.`;
        else if (rt.id === 'fill_blanks') typeInst += `\nExample: { "contextId":"CTX-001","type":"${rt.id}","text":"The chemical formula of rust is _______ .","correctAnswer":"Fe2O3.xH2O","difficulty":"medium","bloomLevel":"Remember","topicOrigin":"..." }`;
        else if (rt.id === 'numerical') typeInst += `\nExample: { "contextId":"CTX-001","type":"${rt.id}","text":"Calculate the work done when a force of 10 N moves an object through 5 m in the direction of force.","correctAnswer":"50","solution":"Work = Force * Displacement = 10 * 5 = 50 J","difficulty":"medium","bloomLevel":"Apply","topicOrigin":"..." }\nNote: For numerical questions, correctAnswer MUST be a clean numeric string (integer or decimal, e.g. "50", "3.14"). Do NOT include options array for numerical type questions.`;
      });

      const roleBlock = isFoundation ? `========================================
ROLE AND PEDAGOGICAL OBJECTIVE (FOUNDATION / OLYMPIAD)
========================================
Act as an expert competitive exam coach and paper setter preparing students for prestigious examinations such as Homi Bhabha Balvaidnyanik Competition (focusing on observation, experiment, and practical application), Science/Math Olympiads (SOF NSO, IMO, etc.), and JEE/NEET Foundation Courses.

Generate EXACTLY ${totalQs} OBJECTIVE questions matching the per-topic quotas specified below.

Generate questions that:
- Remain conceptually mapped to the selected syllabus, chapter, and topic boundaries but are at a significantly higher analytical level.
- Test deep conceptual application, multi-step problem solving, and logical deduction.
${requirementsSection}
========================================
FOUNDATION LEVEL & QUESTION DESIGN RULES:
========================================
- Focus on higher-order thinking skills (HOTS) and conceptual puzzles rather than simple recall or direct textbook-verbatim matching.
- For Science: Include observation-based scenarios, experimental design, or practical life applications.
- For Math: Frame challenging word problems or non-trivial numeric relationships.
- Distractors: Design highly plausible incorrect options that represent common conceptual misunderstandings or mathematical errors.
- Explanation: Provide a comprehensive step-by-step logic description in the "solution" key explaining how to derive the correct option.` : `========================================
ROLE AND PEDAGOGICAL OBJECTIVE (STANDARD SCHOOL / BOARD)
========================================
Act as an experienced Educator teaching students of Class ${selectedClass} under the ${selectedBoard} curriculum.

Generate EXACTLY ${totalQs} OBJECTIVE questions matching the per-topic quotas specified below.

Generate questions that:
- Strictly remain within the selected syllabus, chapter, and topic boundaries.
- Match the learning level expected for Class ${selectedClass}.
${requirementsSection}
${isMath ? `
========================================
MATHEMATICS SOURCE & PATTERN RULES:
========================================
- 80% of the questions generated MUST be selected directly and verbatim from the official textbook exercises, practice sets, problem sets, solved examples, or figure-it-out sections. Absolutely NO modified values, changed coefficients, or fake variables.
- 20% of the questions generated MUST be designed on a similar pattern (using the same structural concept, method, and difficulty as textbook problems but with different numerical values/coefficients).
- Specify the corresponding textbook reference or pattern source for each question in the "textbookPracticeSet" key:
  * For CBSE Class 8 Mathematics (using Ganit Prakash): Use "Figure it out X.Y: Qz" (e.g., "Figure it out 1.1: Q2") or "Question Tag X.Y: Qz" based on the book's terminology.
  * For other CBSE classes: Use "Exercise X.Y: Qz" (e.g., "Exercise 2.3: Q4").
  * For Maharashtra State Board: Use "Practice Set X.Y: Qz" (e.g., "Practice Set 1.2: Q3") or "Problem Set X: Qz".
` : ''}`;

      return `${roleBlock}
========================================
EXAM DETAILS & BLUEPRINT:
========================================
- Board: ${selectedBoard}
- Class: ${selectedClass}
- Blueprint Style: ${blueprint.name} (${blueprint.description})

========================================
DIFFICULTY DISTRIBUTION:
========================================
- easy: ${easyC} questions (${diff.easy}%)
- medium: ${medC} questions (${diff.medium}%)
- hard: ${hardC} questions (${diff.hard}%)

========================================
REQUIRED QUESTION TYPES (BLUEPRINT COMPOSITION):
=======================================${typeBD}${topicDistributionSummary}

========================================
QUESTION GENERATION CONTEXT & TOPIC QUOTAS:
========================================
${ctx}

========================================
MANDATORY CONTEXT ID RULE
========================================
Use contextId CTX-001, CTX-002, etc. matching the context block. Do NOT repeat contextId.
${buildImageInstruction()}
========================================
FORMAT INSTRUCTIONS:
=======================================${typeInst}

========================================
CRITICAL RULES & LEVEL/SOURCE FIDELITY:
========================================
1. STRICT BOARD & CLASS LEVEL ALIGNMENT: You MUST strictly align the question difficulty, vocabulary, and concepts with the official ${selectedBoard} Class ${selectedClass} curriculum. Do NOT generate questions using concepts, equations, or details from higher grade levels.
2. ZERO PLACEHOLDER & ZERO SYNTHETIC LOOPS POLICY:
   - NEVER generate dummy/placeholder options like "Option A (Advanced...)", "Option B (Analytical...)", "Option A (Correct)", or "Option A". Every option MUST be a realistic, context-rich scientific or mathematical answer.
   - NEVER generate generic synthetic variable loop questions like "Calculate resultant value when variable A is ... and variable B is ...". Every problem MUST describe an authentic real-world or textbook scenario.
   - NEVER use programmatic question loops where the only difference between questions is incrementing numbers in a fixed sentence template.
3. SOURCE TEXTBOOK & DIGEST FIDELITY: If any reference text, digest notes, textbook pages, or context is provided in the prompt (or via uploaded image), you MUST strictly extract and adapt questions directly from that material.
4. "correctAnswer" for single_mcq and true_false MUST be an exact, verbatim copy of one of the strings in "options". NEVER "A"/"B"/"C"/"D".
4a. RANDOMIZE CORRECT OPTION POSITIONS: Distribute the correct answer position randomly and evenly across option index 0, 1, 2, and 3 (A, B, C, D). Do NOT always place the correct answer as the first item in "options".
4b. "correctAnswer" for assertion_reason MUST be exactly one of the letters "A", "B", "C", or "D".
5. For multiple_mcq: "correctAnswers" MUST be an array of exact strings copied from "options".
6. DO NOT generate: board, class, subject, chapter, chapterNumber, topic, topicNumber, questionCode.
6b. You MUST include "examCategory": "${isFoundation ? 'foundation' : 'standard'}" key inside each question object.
7. Use \\( ... \\) for math expressions (KaTeX). Wrap chemical formulas inside \\ce{...}.
8. Return ONLY a valid JSON array.
${isMath ? '9. For Mathematics, you MUST include a "textbookPracticeSet" key inside each question object containing the textbook reference (e.g., "Practice Set 1.2: Q3") or pattern source.' : ''}
10. STRICT ZERO FAKE NUMERICALS ON BIOLOGY & QUALITATIVE CONCEPTS:
   - For Biology, life processes, human anatomy, nervous coordination (e.g., nerve impulses, reflex arcs, brain functions), ecology, cellular structure, plant science, or qualitative chemistry:
     * NEVER invent synthetic physics formulas, speeds, arithmetic equations, or time-taken calculations (e.g., calculating nerve impulse velocity, time for reflex action in milliseconds, rate of enzyme reaction arithmetic).
     * All questions for biological and qualitative topics MUST be pure conceptual MCQs, Assertion-Reason, Diagrams, or Scientific Reasons based on real textbook facts and mechanisms.

CRITICAL JSON ESCAPING & MATH FORMATTING RULES:
1. Return ONLY the raw valid JSON array. DO NOT wrap it in any explanations, introduction, or extra text.
2. Any backslashes (\\) in LaTeX math expressions (like \\frac, \\propto, \\pi, \\theta, \\times, etc.) MUST be double-escaped as \\\\ (e.g. \\\\frac, \\\\propto, \\\\pi, \\\\theta). Never use a single backslash inside a JSON string.
3. If using standard math delimiters, represent inline math as \\\\( ... \\\\) and block display math as \\\\[ ... \\\\] (always with double-escaped backslashes).
4. Do NOT use raw control characters inside string values.
5. All double quotes inside string values must be properly escaped as \\\".`;
    } else {
      let topicDistributionSummary = '\n\n========================================\nPER-TOPIC QUESTION ALLOCATION QUOTAS:\n========================================';
      promptTopics.forEach(tp => {
        const k = topicKey(tp);
        const cnt = topicCounts[k] || 0;
        topicDistributionSummary += `\n- ${tp.subject ? '[' + tp.subject + '] ' : ''}${tp.topic}: EXACTLY ${cnt} questions`;
      });

      const questionBreakdownInstruction = isMath ? `
========================================
QUESTION BREAKDOWN REQUIREMENTS (MATHEMATICS):
========================================
Generate EXACTLY ${totalQs} subjective mathematics questions distributed according to the per-topic quotas:
- Generate 1-Mark short questions/formulas (type: "subjective_define", marks: 1, simple definitions, formulas, or units).
- Generate 2-Mark short specific / reasoned problems (type: "numerical_short" or "subjective_short", marks: 2, 2-4 step solution).
- Generate 4-Mark long analytical / derivation problems (type: "numerical_long" or "subjective_long", marks: 4, multi-step calculation or proof).
- 80% of the generated questions MUST be taken directly and verbatim from official textbook exercises, practice sets, problem sets, or figure-it-out sections. The remaining 20% MUST be designed on a similar pattern.
- You MUST specify the corresponding textbook reference or pattern source for each question in the "textbookPracticeSet" key:
  * For CBSE Class 8 Mathematics: "Figure it out X.Y: Qz" or "Question Tag X.Y: Qz".
  * For other CBSE classes: "Exercise X.Y: Qz".
  * For Maharashtra State Board: "Practice Set X.Y: Qz" or "Problem Set X: Qz".
` : `
========================================
QUESTION BREAKDOWN REQUIREMENTS (SCIENCE / GENERAL):
========================================
Generate EXACTLY ${totalQs} subjective questions matching the per-topic quotas:
- 1-Mark short questions (type: "subjective_define" or "subjective_laws", marks: 1, Definitions, Laws, Principles, Statements).
- 2-Mark short specific / reasoned questions (type: "subjective_short" or "subjective_reason" or "subjective_notes", marks: 2).
- 4-Mark long specific / analytical / derivation questions (type: "subjective_long", marks: 4).
- Extract and prioritize Previous Year Questions (PYQs) and high-yield textbook concepts.
`;

      (window as any).lastPromptMeta = { mode: 'subjective', totalQs };

      return `========================================
Role & Goal:
========================================
You are an expert CBSE & State Board Paper Setter.
Generate authentic, high-yield subjective questions matching the Blueprint "${blueprint.name}":
- Board: ${selectedBoard}
- Class: ${selectedClass}
- Subject: ${subj}
- Total Desired Questions: EXACTLY ${totalQs}
${topicDistributionSummary}
${requirementsSection}
${questionBreakdownInstruction}

========================================
QUESTION GENERATION CONTEXT & TOPIC QUOTAS:
========================================
${ctx}

========================================
STRICT SYLLABUS, LEVEL & SOURCE FIDELITY RULES:
========================================
1. STRICT BOARD & CLASS LEVEL ALIGNMENT: Align difficulty and expected answer depth with official ${selectedBoard} Class ${selectedClass} curriculum.
2. ANSWERS VERBATIM: Answers MUST be verbatim from standard prescribed NCERT / State Board textbooks. Absolutely NO paraphrasing.
3. KEYWORD HIGHLIGHTING: Embed key phrases inside HTML <mark>keyword</mark> tags directly within the model answer text string.
4. STEP-BY-STEP SOLUTION: Separate each logical answer sentence on a new numbered line (1., 2., 3...) inside the "solution" string.
5. PYQ INFO: Add "pyqInfo" indicating year/exam (e.g. "CBSE Board 2020", "MSBSHSE 2022", "PYQ Style Practice").
6. FORMULAS: Use \\( ... \\) for math expressions (KaTeX) and \\ce{...} for chemical formulas.
${buildImageInstruction()}

========================================
CRITICAL JSON ESCAPING & MATH FORMATTING RULES:
========================================
1. Return ONLY the raw valid JSON array. DO NOT wrap in extra explanations.
2. Double-escape backslashes in LaTeX (\\\\frac, \\\\pi, \\\\theta).
3. Do NOT use raw control characters inside string values.

========================================
OUTPUT FORMAT: Return ONLY a valid JSON array of objects with schema:
========================================
[
  {
    "contextId": "CTX-001",
    "topicName": "Topic name from the context list",
    "type": "subjective_define / subjective_laws / subjective_short / subjective_reason / subjective_notes / subjective_long / numerical_short / numerical_long",
    "marks": 1,
    "text": "Question text here...",
    "solution": "Verbatim model answer with <mark>key terms</mark> highlighted...",
    "keywords": ["key term 1", "key term 2"],
    "pyqInfo": "CBSE Board 2020"
  }
]

Return ONLY valid JSON. No extra text.`;
    }
  };

  // Compile instructions templates for Gemini AI
  const handleGeneratePrompt = () => {
    if (!selectedBoard || !selectedClass || getSelectedSubjectsCount() === 0 || selectedTopics.length === 0) {
      triggerAlert('Configuration Required', 'Please configure Board, Class, Subjects, and Topics first.');
      return;
    }
    if (topicWeightageMode === 'percentage' && selectedTopics.length > 1) {
      if (getTopicWeightageTotal() !== 100) {
        triggerAlert('Configuration Error', '⚠️ Total custom topic weightage must sum up to exactly 100% before generating questions.');
        return;
      }
    }
    const text = compilePrompt(questionType);
    setAiPrompt(text);

    if (text) {
      try {
        navigator.clipboard.writeText(text)
          .then(() => {
            triggerAlert('Success', '⚡ Prompt generated and copied to clipboard successfully!', undefined, false, 1000);
          })
          .catch(() => {
            const ta = document.createElement('textarea');
            ta.value = text;
            ta.style.position = 'fixed';
            ta.style.opacity = '0';
            document.body.appendChild(ta);
            ta.focus();
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            triggerAlert('Success', '⚡ Prompt generated and copied to clipboard successfully!', undefined, false, 1000);
          });
      } catch {
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.focus();
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        triggerAlert('Success', '⚡ Prompt generated and copied to clipboard successfully!', undefined, false, 1000);
      }
    }

    // Auto scroll to paste response card
    setTimeout(() => {
      document.getElementById('paste-response-card')?.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }, 100);
  };



  const resolveTopicNumber = (topicNameFromAI: string, fallbackNum: string = '1.1'): string => {
    if (!topicNameFromAI) return fallbackNum;
    const aiNameClean = String(topicNameFromAI).trim().toLowerCase();
    
    // 1. Try to extract prefix pattern like "6.1" or "6.2" or "6.1.2"
    const prefixMatch = aiNameClean.match(/^\s*(\d+(?:\.\d+)+)/);
    if (prefixMatch) {
      const extractedNum = prefixMatch[1];
      const matchedByNum = currentAllTopics.find(t => String(t.topicNumber) === extractedNum);
      if (matchedByNum) return matchedByNum.topicNumber;
    }

    // 2. Perform fuzzy string comparisons
    const matched = currentAllTopics.find(t => {
      const name1 = String(t.topic || '').trim().toLowerCase();
      if (name1 === aiNameClean) return true;
      
      const name2 = name1.replace(/^\s*\d+(?:\.\d+)*\s*/, '').trim();
      if (name2 === aiNameClean) return true;
      
      const aiNameNoNum = aiNameClean.replace(/^\s*\d+(?:\.\d+)*\s*/, '').trim();
      if (name2 === aiNameNoNum) return true;
      
      return false;
    });
    
    if (matched) return matched.topicNumber;

    // 3. Fallback: Check if any topic name is a substring of the AI topic name or vice versa
    const substringMatch = currentAllTopics.find(t => {
      const nameClean = String(t.topic || '').trim().toLowerCase().replace(/^\s*\d+(?:\.\d+)*\s*/, '').trim();
      const aiNameNoNum = aiNameClean.replace(/^\s*\d+(?:\.\d+)*\s*/, '').trim();
      if (nameClean.length > 3 && aiNameNoNum.length > 3) {
        if (nameClean.includes(aiNameNoNum) || aiNameNoNum.includes(nameClean)) return true;
      }
      return false;
    });

    return substringMatch ? substringMatch.topicNumber : fallbackNum;
  };

  const transformObjectiveQuestion = (q: any, i: number) => {
    const fallback = selectedTopics[0] || {};
    const cid = q.contextId || 'CTX-001';
    const ctx = (window as any).questionContextLookup?.[cid] || {};
    const resolvedTopicName = q.topic || q.topicName || q.topicOrigin || ctx.topic || fallback.topic || '';
    const resolvedTopicNumber = q.topicNumber || ctx.topicNumber || resolveTopicNumber(resolvedTopicName, fallback.topicNumber || '1.1');
    const matchedTopic = currentAllTopics.find(t => String(t.topicNumber) === String(resolvedTopicNumber));
    const finalTopicName = matchedTopic ? matchedTopic.topic : resolvedTopicName;

    let rawType = q.type || 'single_mcq';
    if (rawType === 'numerical5') rawType = 'numerical';
    const isMultiple = rawType === 'multiple_mcq' || (rawType === 'single_mcq' && Array.isArray(q.correctAnswers) && q.correctAnswers.length > 1);
    const finalType = isMultiple ? 'multiple_mcq' : rawType;

    // 1. Clean options array: strip "A. ", "Option A: ", "(A) ", etc.
    let cleanOptions: string[] = [];
    if (Array.isArray(q.options) && q.options.length > 0) {
      cleanOptions = q.options.map((opt: any) => cleanOptionPrefix(String(opt || '')).trim()).filter(Boolean);
    }

    // 2. Resolve correct answer(s)
    let finalCorrectAnswer = '';
    let finalCorrectAnswers: string[] = [];

    if (finalType === 'single_mcq' || finalType === 'true_false') {
      let rawAns = String(q.correctAnswer || (Array.isArray(q.correctAnswers) ? q.correctAnswers[0] : '') || '').trim();
      const letterMatch = rawAns.match(/^[A-D]$/i);
      const digitMatch = rawAns.match(/^[1-4]$/);

      if (letterMatch && cleanOptions.length >= 2) {
        const lIdx = letterMatch[0].toUpperCase().charCodeAt(0) - 65;
        if (cleanOptions[lIdx]) finalCorrectAnswer = cleanOptions[lIdx];
      } else if (digitMatch && cleanOptions.length >= 2) {
        const dIdx = parseInt(digitMatch[0], 10) - 1;
        if (cleanOptions[dIdx]) finalCorrectAnswer = cleanOptions[dIdx];
      } else {
        const cleanedAns = cleanOptionPrefix(rawAns);
        const matched = cleanOptions.find(opt => 
          normalizeOptionText(opt) === normalizeOptionText(cleanedAns) ||
          cleanStringForMatch(opt) === cleanStringForMatch(cleanedAns)
        );
        finalCorrectAnswer = matched || cleanedAns || rawAns;
      }
      finalCorrectAnswers = finalCorrectAnswer ? [finalCorrectAnswer] : [];

      // 3. Shuffle options so Option A is not always correct:
      if (cleanOptions.length >= 2) {
        cleanOptions = shuffleArray(cleanOptions);
      }
    } else if (finalType === 'multiple_mcq') {
      const rawAnsList = Array.isArray(q.correctAnswers) ? q.correctAnswers : (q.correctAnswer ? [q.correctAnswer] : []);
      finalCorrectAnswers = rawAnsList.map((rawAns: any) => {
        const str = String(rawAns || '').trim();
        const letterMatch = str.match(/^[A-D]$/i);
        const digitMatch = str.match(/^[1-4]$/);
        if (letterMatch && cleanOptions.length >= 2) {
          const lIdx = letterMatch[0].toUpperCase().charCodeAt(0) - 65;
          return cleanOptions[lIdx] || str;
        } else if (digitMatch && cleanOptions.length >= 2) {
          const dIdx = parseInt(digitMatch[0], 10) - 1;
          return cleanOptions[dIdx] || str;
        }
        const cleaned = cleanOptionPrefix(str);
        const matched = cleanOptions.find(opt => 
          normalizeOptionText(opt) === normalizeOptionText(cleaned) ||
          cleanStringForMatch(opt) === cleanStringForMatch(cleaned)
        );
        return matched || cleaned || str;
      }).filter(Boolean);

      finalCorrectAnswer = finalCorrectAnswers[0] || '';

      if (cleanOptions.length >= 2) {
        cleanOptions = shuffleArray(cleanOptions);
      }
    } else if (finalType === 'assertion_reason') {
      const normLetter = String(q.correctAnswer || '').trim().toUpperCase();
      finalCorrectAnswer = ['A', 'B', 'C', 'D'].includes(normLetter) ? normLetter : (normLetter.match(/[A-D]/i)?.[0]?.toUpperCase() || 'A');
      cleanOptions = [];
    } else {
      finalCorrectAnswer = String(q.correctAnswer || '').trim();
    }

    return {
      board: selectedBoard,
      class: selectedClass,
      subject: ctx.subject || getSelectedSubjectsList()[0] || '',
      chapter: ctx.chapterName || fallback.chapterName || '',
      chapterNumber: String(ctx.chapterNumber || fallback.chapterNumber || '1'),
      topic: finalTopicName,
      topicNumber: String(resolvedTopicNumber),
      type: finalType,
      text: q.text || '',
      options: cleanOptions,
      correctAnswer: finalCorrectAnswer,
      correctAnswers: finalCorrectAnswers,
      assertion: q.assertion || '',
      reason: q.reason || '',
      solution: q.solution || '',
      difficulty: q.difficulty || 'medium',
      bloomLevel: normalizeBloomLevel(q.bloomLevel, q.difficulty, finalType),
      requiresFigure: !!q.requiresFigure || (q.text || '').toLowerCase().includes('figure') || (q.text || '').toLowerCase().includes('diagram') || (q.text || '').toLowerCase().includes('fig.'),
      imageUrl: q.imageUrl || '',
      examCategory: q.examCategory || examCategory,
      source: 'ai_generated',
      createdAt: new Date().toISOString(),
      createdBy: firebaseUser?.email || 'admin'
    };
  };

  const transformSubjectiveQuestion = (q: any) => {
    const fallback = selectedTopics[0] || {};
    const marks = Number(q.marks) || (['subjective_define', 'subjective_laws'].includes(q.type) ? 1 : (q.type === 'subjective_long' || q.type === 'numerical_long' ? 4 : 2));
    const defaultType = marks === 1 ? 'subjective_define' : (marks === 4 ? 'subjective_long' : 'subjective_short');
    const solText = q.solution || (Array.isArray(q.answerLines) ? q.answerLines.map((l: any) => l.text || l).join('\n') : '');
    
    let answerLines = q.answerLines || [];
    if (!answerLines.length && solText) {
      const lines = solText.split('\n').map((l: any) => String(l || '').trim()).filter(Boolean);
      answerLines = lines.map((l: string, idx: number) => {
        const cleanText = l.replace(/^\d+[\.\)]\s*/, '').trim();
        return { lineNo: idx + 1, text: cleanText };
      });
    }

    const resolvedTopicName = q.topicName || q.topic || q.topicOrigin || fallback.topic || '';
    const resolvedTopicNumber = q.topicNumber || resolveTopicNumber(resolvedTopicName, fallback.topicNumber || '1.1');
    const matchedTopic = currentAllTopics.find(t => String(t.topicNumber) === String(resolvedTopicNumber));
    const finalTopicName = matchedTopic ? matchedTopic.topic : resolvedTopicName;

    return {
      board: selectedBoard,
      class: selectedClass,
      subject: q.subject || getSelectedSubjectsList()[0] || '',
      chapter: q.chapterName || fallback.chapterName || '',
      chapterNumber: String(q.chapterNumber || fallback.chapterNumber || '1'),
      topic: finalTopicName,
      topicNumber: String(resolvedTopicNumber),
      type: q.type || defaultType,
      text: q.text || '',
      marks: marks,
      difficulty: q.difficulty || 'medium',
      bloomLevel: normalizeBloomLevel(q.bloomLevel, q.difficulty, q.type || defaultType),
      answerLines: answerLines,
      keywords: q.keywords || [],
      solution: solText,
      pyqInfo: q.pyqInfo || 'PYQ Style Practice',
      requiresFigure: !!q.requiresFigure || (q.text || '').toLowerCase().includes('figure') || (q.text || '').toLowerCase().includes('diagram') || (q.text || '').toLowerCase().includes('fig.'),
      imageUrl: q.imageUrl || '',
      examCategory: q.examCategory || examCategory,
      source: 'ai_generated',
      createdAt: new Date().toISOString(),
      createdBy: firebaseUser?.email || 'admin'
    };
  };

  // Execute sequential bulk save
  const executeBulkSave = async (questionsList: any[]) => {
    setSavingProgress(true);
    setSavePercentage(0);
    setSaveStats({ current: 0, total: questionsList.length });

    try {
      const idToken = await firebaseUser!.getIdToken();
      let successfulCount = 0;

      // Build payload array for single atomic bulkSave request
      const formattedQuestions = questionsList.map(q => ({
        qtype: q.type || 'single_mcq',
        text: q.text,
        options: q.options || [],
        correctAnswer: q.correctAnswer || '',
        correctAnswers: q.correctAnswers || [],
        assertion: q.assertion || '',
        reason: q.reason || '',
        solution: q.solution || '',
        answerLines: q.answerLines || [],
        pyqInfo: q.pyqInfo || '',
        difficulty: q.difficulty || 'medium',
        bloomLevel: q.bloomLevel || 'Remember',
        board: selectedBoard,
        classNum: selectedClass,
        subjectName: q.subject || getSelectedSubjectsList()[0] || '',
        chapterNumber: q.chapterNumber || '1',
        topicNumber: q.topicNumber || '1.1',
        topic: q.topic || q.topicName || '',
        topicName: q.topicName || q.topic || '',
        keywords: q.keywords || [],
        textbookPracticeSet: q.textbookPracticeSet || '',
        marks: Number(q.marks) || 0
      }));

      // Try instant atomic bulkSave API first
      let bulkSuccess = false;
      let lastErrorMessage = '';

      try {
        setSavePercentage(50);
        setSaveStats({ current: Math.floor(questionsList.length / 2), total: questionsList.length });
        
        const bulkRes = await fetch('/api/admin/questions', {
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

        if (bulkRes.ok) {
          const bulkData = await bulkRes.json();
          successfulCount = bulkData.count || questionsList.length;
          bulkSuccess = true;
          setSavePercentage(100);
          setSaveStats({ current: questionsList.length, total: questionsList.length });
        } else {
          const errData = await bulkRes.json().catch(() => ({}));
          lastErrorMessage = errData.message || 'Server rejected questions payload.';
          console.warn('bulkSave API returned error:', lastErrorMessage);
        }
      } catch (err: any) {
        lastErrorMessage = err.message || 'Network error on bulkSave';
        console.warn('bulkSave API fallback to chunked parallel save:', err);
      }

      // Fallback: Parallel chunked saving if bulkSave fails
      if (!bulkSuccess) {
        const BATCH_SIZE = 6;
        let completedCount = 0;

        for (let i = 0; i < questionsList.length; i += BATCH_SIZE) {
          const chunk = formattedQuestions.slice(i, i + BATCH_SIZE);
          const results = await Promise.all(
            chunk.map(async (payload) => {
              try {
                const res = await fetch('/api/admin/questions', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${idToken}`
                  },
                  body: JSON.stringify(payload)
                });
                if (!res.ok) {
                  const errJson = await res.json().catch(() => ({}));
                  if (errJson.message) lastErrorMessage = errJson.message;
                }
                return res.ok;
              } catch (e) {
                return false;
              }
            })
          );

          results.forEach(ok => {
            if (ok) successfulCount++;
            completedCount++;
          });

          const progress = Math.round((completedCount / questionsList.length) * 100);
          setSavePercentage(progress);
          setSaveStats({ current: completedCount, total: questionsList.length });
        }
      }

      if (successfulCount === 0) {
        throw new Error(lastErrorMessage || 'Failed to save questions to database. Please check question requirements.');
      }

      // Stay here, clear workspace, keep selections
      setGeneratedQuestions([]);
      setAiPasteText('');
      setAiPrompt('');
      if (typeof (window as any).clearImage === 'function') {
        (window as any).clearImage();
      } else {
        clearImage();
      }
      
      triggerConfirm(
        'Questions Saved',
        `✅ ${successfulCount} questions successfully saved! Do you want to generate more questions?`,
        () => {
          // Yes: stay on the page with selections intact
        },
        () => {
          // No: redirect to Question Bank
          router.push('/admin/question-bank');
        }
      );
    } catch (err: any) {
      triggerAlert('Error Saving Questions', err.message || 'Error occurred saving questions.');
    } finally {
      setSavingProgress(false);
    }
  };

  // Parse pasted JSON response from text input
  const handleParseJSON = () => {
    const text = aiPasteText.trim();
    if (!text) {
      triggerAlert('Input Required', 'Please paste the AI JSON response array first.');
      return;
    }

    try {
      const parsed = robustParseAIJson(text);
      let transformed: any[] = [];

      if (questionType === 'objective' || questionType === 'dual_track') {
        const arr = Array.isArray(parsed) ? parsed : (parsed.questions || []);
        if (!arr.length) throw new Error('No questions list found.');
        transformed = arr.map((q: any, i: number) => transformObjectiveQuestion(q, i));
      } else if (questionType === 'subjective') {
        const arr = parsed.questions || (Array.isArray(parsed) ? parsed : [parsed]);
        if (!arr.length) throw new Error('No questions list found.');
        transformed = arr.map((q: any) => transformSubjectiveQuestion(q));
      } else {
        // all_in_one mode: smart hybrid detection
        const arr = Array.isArray(parsed) ? parsed : (parsed.questions || [parsed]);
        if (!arr.length) throw new Error('No questions list found.');
        transformed = arr.map((q: any, i: number) => {
          const type = q.type || q.qtype || '';
          const isSub = type.startsWith('subjective_') || 
            type.startsWith('numerical_') || 
            (q.marks && !q.options?.length && type !== 'numerical') ||
            (q.answerLines?.length > 0 && !q.options?.length);
          return isSub ? transformSubjectiveQuestion(q) : transformObjectiveQuestion(q, i);
        });
      }

      setGeneratedQuestions(transformed);
      
      const validation = validateQuestionsForSave(transformed);
      if (!validation.valid) {
        triggerAlert('Success with Warnings', `✅ Successfully parsed ${transformed.length} questions, but ${validation.errors.length} issue(s) need attention. Review or fix/delete them below before saving.`);
      }
      
      setTimeout(() => {
        document.getElementById('previewQuestionsSection')?.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    } catch (err: any) {
      triggerAlert('Parsing Failed', `❌ Parsing failed: ${err.message}`);
    }
  };

  // Validate questions schema before write using SSOT validation function
  const validateQuestionsForSave = (list: any[]) => {
    const errorItems: { index: number; qNum: number; error: string; question: any }[] = [];
    const questionErrorsMap: Record<number, string[]> = {};

    list.forEach((q, idx) => {
      const qNum = idx + 1;
      const qErrors = validateQuestion(q, questionType);
      if (qErrors.length > 0) {
        questionErrorsMap[idx] = qErrors;
        qErrors.forEach(err => {
          errorItems.push({ index: idx, qNum, error: `Q${qNum}: ${err}`, question: q });
        });
      }
    });

    return {
      valid: errorItems.length === 0,
      errors: errorItems.map(e => e.error),
      errorItems,
      questionErrorsMap,
      invalidIndices: new Set(errorItems.map(e => e.index))
    };
  };

  // Execute sequential bulk save
  const handleBulkSave = async () => {
    if (savingProgress) return;
    if (generatedQuestions.length === 0) return;
    const validation = validateQuestionsForSave(generatedQuestions);
    if (!validation.valid) {
      triggerAlert('Validation Issues', `❌ Cannot save — ${validation.errors.length} issues found. Fix or delete them first:\n\n${validation.errors.slice(0, 5).join('\n')}`);
      return;
    }

    triggerConfirm(
      'Save to Question Bank',
      `Save all ${generatedQuestions.length} parsed questions to the Question Bank?`,
      () => executeBulkSave(generatedQuestions)
    );
  };

  const handleDeletePreviewQuestion = (idx: number) => {
    setGeneratedQuestions(prev => prev.filter((_, i) => i !== idx));
  };

  // Run render math helper


  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div style={{ textAlign: 'center' }}>
          <div className="spinner" style={{ margin: '0 auto 12px' }}></div>
          <div style={{ color: 'var(--text-muted)' }}>Loading syllabus metadata...</div>
        </div>
      </div>
    );
  }

  const { total: totalSubjectWeight } = getWeightageMap();
  const totalTopicWeight = getTopicWeightageTotal();

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* CDN Script Injections for KaTeX */}




      {/* Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800 }}>🤖 YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Create Question Bank</h1>
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>AI-assisted bulk question generation and syllabus compiler</div>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          
          <button className="btn btn-secondary" onClick={() => router.push('/admin/question-bank')}>Manage QB</button>
        </div>
      </header>

      {/* Main Workspace */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1000px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        
        {/* Card 1: Syllabus Mapping Cascading Selects */}
        <div className="card" style={{ background: 'var(--surface)', padding: '18px 24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
          <h3 style={{ fontSize: '13px', fontWeight: 800, margin: '0 0 12px', textTransform: 'uppercase', color: 'var(--accent)' }}>Syllabus Mapping</h3>
          
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '12px', marginBottom: '16px' }}>
            {/* Board */}
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Board</label>
              <select 
                className="form-input" 
                value={selectedBoard} 
                onChange={(e) => handleBoardChange(e.target.value, () => { setTopicWeightageMap({}); clearImage(); })}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                <option value="">— Select Board —</option>
                {boards.map(b => (
                  <option key={b} value={b}>{boardCodes[b] || b.toUpperCase()}</option>
                ))}
              </select>
            </div>

            {/* Class */}
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '5px' }}>Class</label>
              <select 
                className="form-input" 
                value={selectedClass} 
                onChange={(e) => handleClassChange(e.target.value, () => { setTopicWeightageMap({}); clearImage(); })} 
                disabled={!selectedBoard}
                style={{ width: '100%', padding: '8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                <option value="">— Select Class —</option>
                {classes.map(c => (
                  <option key={c} value={c}>Class {c}</option>
                ))}
              </select>
            </div>

          </div>
          
          {/* Subjects checkboxes */}
          <SyllabusSelector
            availableSubjects={availableSubjects}
            selectedSubjects={selectedSubjects}
            onToggleSubject={handleToggleSubject}
            availableChapters={currentChapters}
            selectedChapters={selectedChapters}
            onToggleChapter={handleToggleChapter}
            onSelectAllChapters={handleSelectAllChapters}
            onDeselectAllChapters={handleDeselectAllChapters}
            availableTopics={currentAllTopics}
            selectedTopics={selectedTopics}
            onToggleTopic={handleToggleTopic}
            onSelectAllTopics={() => handleSelectAllTopics(currentAllTopics)}
            onDeselectAllTopics={() => handleDeselectAllTopics(currentAllTopics)}
          />

          {/* Topic Weightage Section */}
          {selectedTopics.length > 0 && (
            <div style={{ marginTop: '20px', borderTop: '1px solid var(--border-light)', paddingTop: '15px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', flexWrap: 'wrap', gap: '8px' }}>
                <h3 style={{ fontSize: '13px', fontWeight: 800, margin: 0, color: 'var(--accent)' }}>📊 Topic Question Count &amp; Weightage Distribution</h3>
                <span style={{ fontSize: '12px', fontWeight: 700, background: 'rgba(52, 152, 219, 0.15)', color: '#2980b9', padding: '3px 10px', borderRadius: '12px' }}>
                  🎯 Total Target: <strong>{getTotalTargetQuestions()} Questions</strong> across {selectedTopics.length} selected topics
                </span>
              </div>
              
              <div style={{ display: 'flex', gap: '10px', alignItems: 'center', marginBottom: '15px', flexWrap: 'wrap' }}>
                <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)' }}>Distribution Mode:</span>
                <button 
                  type="button"
                  className={`btn btn-sm ${topicWeightageMode === 'custom_counts' ? 'btn-primary' : 'btn-secondary'}`}
                  onClick={() => setTopicWeightageMode('custom_counts')}
                  style={{ borderRadius: '20px', padding: '4px 12px', fontSize: '11px' }}
                >
                  🔢 Custom Count Per Topic
                </button>
                <button 
                  type="button"
                  className={`btn btn-sm ${topicWeightageMode === 'equal' ? 'btn-primary' : 'btn-secondary'}`}
                  onClick={() => setTopicWeightageMode('equal')}
                  style={{ borderRadius: '20px', padding: '4px 12px', fontSize: '11px' }}
                >
                  ⚖️ Equal Count ({defaultPerTopicCount} Qs/Topic)
                </button>
                <button 
                  type="button"
                  className={`btn btn-sm ${topicWeightageMode === 'percentage' ? 'btn-primary' : 'btn-secondary'}`}
                  onClick={() => setTopicWeightageMode('percentage')}
                  style={{ borderRadius: '20px', padding: '4px 12px', fontSize: '11px' }}
                >
                  📊 Percentage Weightage
                </button>
              </div>

              {/* Mode 1: Custom Count Per Topic */}
              {topicWeightageMode === 'custom_counts' && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', background: 'var(--bg-soft)', padding: '12px', borderRadius: 'var(--radius-sm)' }}>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 140px', gap: '10px', fontWeight: 'bold', fontSize: '11px', borderBottom: '1px dashed var(--border-light)', paddingBottom: '6px' }}>
                    <span>Topic Name</span>
                    <span style={{ textAlign: 'right' }}>Target Questions</span>
                  </div>
                  {selectedTopics.map((top, idx) => {
                    const key = topicKey(top);
                    const currentCount = topicCustomCounts[key] !== undefined ? topicCustomCounts[key] : defaultPerTopicCount;
                    return (
                      <div key={idx} style={{ display: 'grid', gridTemplateColumns: '1fr 140px', gap: '10px', alignItems: 'center', fontSize: '12px' }}>
                        <span>📍 {top.topic}</span>
                        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-end', gap: '6px' }}>
                          <input 
                            type="number"
                            min={1}
                            max={200}
                            value={currentCount === undefined || currentCount === null ? '' : currentCount}
                            onChange={(e) => {
                              const raw = e.target.value;
                              if (raw === '') {
                                handleTopicCustomCountChange(top, '');
                              } else {
                                const val = parseInt(raw, 10);
                                handleTopicCustomCountChange(top, isNaN(val) ? '' : Math.max(1, val));
                              }
                            }}
                            onBlur={() => {
                              if (currentCount === '' || currentCount === undefined || Number(currentCount) < 1) {
                                handleTopicCustomCountChange(top, typeof defaultPerTopicCount === 'number' ? defaultPerTopicCount : 10);
                              }
                            }}
                            style={{ width: '65px', padding: '4px 6px', textAlign: 'center', border: '1px solid var(--border-light)', borderRadius: '4px', background: 'var(--surface)', color: 'var(--text)', fontWeight: 600 }}
                          />
                          <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Qs</span>
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}

              {/* Mode 2: Equal Count */}
              {topicWeightageMode === 'equal' && (
                <div style={{ display: 'flex', alignItems: 'center', gap: '15px', background: 'var(--bg-soft)', padding: '12px', borderRadius: 'var(--radius-sm)', fontSize: '12px' }}>
                  <span>Set questions per topic:</span>
                  <input 
                    type="number"
                    min={1}
                    max={200}
                    value={defaultPerTopicCount}
                    onChange={(e) => {
                      const raw = e.target.value;
                      if (raw === '') {
                        setDefaultPerTopicCount('');
                      } else {
                        const val = parseInt(raw, 10);
                        setDefaultPerTopicCount(isNaN(val) ? '' : Math.max(1, val));
                      }
                    }}
                    onBlur={() => {
                      if (defaultPerTopicCount === '' || Number(defaultPerTopicCount) < 1) {
                        setDefaultPerTopicCount(10);
                      }
                    }}
                    style={{ width: '70px', padding: '4px 8px', textAlign: 'center', border: '1px solid var(--border-light)', borderRadius: '4px', background: 'var(--surface)', color: 'var(--text)', fontWeight: 700 }}
                  />
                  <span style={{ color: 'var(--text-muted)' }}>
                    ({selectedTopics.length} topics × {defaultPerTopicCount || 0} = <strong>{selectedTopics.length * (Number(defaultPerTopicCount) || 0)} Total Questions</strong>)
                  </span>
                </div>
              )}

              {/* Mode 3: Percentage Weightage */}
              {topicWeightageMode === 'percentage' && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', background: 'var(--bg-soft)', padding: '12px', borderRadius: 'var(--radius-sm)' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px' }}>
                    <span style={{ fontSize: '12px', fontWeight: 600 }}>Total Batch Questions:</span>
                    <input 
                      type="number"
                      min={5}
                      max={500}
                      value={totalBatchQuestions}
                      onChange={(e) => {
                        const raw = e.target.value;
                        if (raw === '') {
                          setTotalBatchQuestions('');
                        } else {
                          const val = parseInt(raw, 10);
                          setTotalBatchQuestions(isNaN(val) ? '' : Math.max(1, val));
                        }
                      }}
                      onBlur={() => {
                        if (totalBatchQuestions === '' || Number(totalBatchQuestions) < 5) {
                          setTotalBatchQuestions(30);
                        }
                      }}
                      style={{ width: '70px', padding: '4px 8px', textAlign: 'center', border: '1px solid var(--border-light)', borderRadius: '4px', background: 'var(--surface)', color: 'var(--text)', fontWeight: 700 }}
                    />
                  </div>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 100px', gap: '10px', fontWeight: 'bold', fontSize: '11px', borderBottom: '1px dashed var(--border-light)', paddingBottom: '6px' }}>
                    <span>Topic Name</span>
                    <span style={{ textAlign: 'right' }}>Weight (%)</span>
                  </div>
                  {selectedTopics.map((top, idx) => {
                    const key = topicKey(top);
                    const currentWeight = topicWeightageMap[key] !== undefined ? topicWeightageMap[key] : Math.floor(100 / selectedTopics.length);
                    return (
                      <div key={idx} style={{ display: 'grid', gridTemplateColumns: '1fr 100px', gap: '10px', alignItems: 'center', fontSize: '12px' }}>
                        <span>📍 {top.topic}</span>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '4px', justifyContent: 'flex-end' }}>
                          <input 
                            type="number"
                            min={0}
                            max={100}
                            value={currentWeight === undefined || currentWeight === null ? '' : currentWeight}
                            onChange={(e) => {
                              const raw = e.target.value;
                              if (raw === '') {
                                handleTopicWeightChange(top, '');
                              } else {
                                const val = parseInt(raw, 10);
                                handleTopicWeightChange(top, isNaN(val) ? '' : Math.max(0, Math.min(100, val)));
                              }
                            }}
                            onBlur={() => {
                              if (currentWeight === '' || currentWeight === undefined) {
                                handleTopicWeightChange(top, 0);
                              }
                            }}
                            style={{ width: '60px', padding: '4px', textAlign: 'right', border: '1px solid var(--border-light)', borderRadius: '4px', background: 'var(--surface)', color: 'var(--text)' }}
                          />
                          <span>%</span>
                        </div>
                      </div>
                    );
                  })}
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 100px', gap: '10px', fontWeight: 'bold', fontSize: '12px', borderTop: '1px dashed var(--border-light)', paddingTop: '8px', marginTop: '5px' }}>
                    <span>Total Weightage</span>
                    <span style={{ textAlign: 'right', color: getTopicWeightageTotal() === 100 ? 'var(--success)' : 'var(--danger)' }}>
                      {getTopicWeightageTotal()}%
                    </span>
                  </div>
                  {getTopicWeightageTotal() !== 100 && (
                    <p style={{ margin: '5px 0 0', fontSize: '11px', color: 'var(--danger)' }}>
                      ⚠️ Total custom weightage must sum up to exactly 100%.
                    </p>
                  )}
                </div>
              )}
            </div>
          )}
        </div>

        {/* Card 2: Workspace Settings & Actions */}
        {selectedTopics.length > 0 && (
          <div className="card" style={{ background: 'var(--surface)', padding: '18px 24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
            <h3 style={{ fontSize: '13px', fontWeight: 800, margin: '0 0 12px', textTransform: 'uppercase', color: 'var(--accent)' }}>Workspace Settings &amp; Generator Actions</h3>

            {/* Optional Textbook/Diagram Image Upload */}
            <div style={{ marginTop: '10px', borderTop: '1px dashed var(--border-light)', paddingTop: '12px' }}>
              <label style={{ fontSize: '12px', fontWeight: 'bold', display: 'block', marginBottom: '6px' }}>🖼️ Upload Textbook/Diagram Image (optional)</label>
              <p style={{ fontSize: '11px', color: 'var(--text-muted)', margin: '0 0 10px' }}>
                If you have textbook content, question lists, or diagrams, upload them here to instruct the AI model to parse and extract them.
              </p>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px', alignItems: 'center' }}>
                <input type="file" id="questionImageInput" accept="image/*" onChange={handleImageSelected} style={{ fontSize: '12px' }} />
                {uploadedImageBase64 && (
                <button className="btn btn-secondary btn-sm" onClick={clearImage}>✕ Clear</button>
                )}
              </div>
              {uploadedImageBase64 && (
                <div style={{ marginTop: '10px' }}>
                  <img src={uploadedImageBase64} alt="Selected source preview" style={{ maxWidth: '240px', maxHeight: '180px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }} />
                </div>
              )}
            </div>

            {/* Question Type & Category Choice Toggles */}
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '15px', alignItems: 'center', marginTop: '16px', borderTop: '1px solid var(--border-light)', paddingTop: '12px' }}>
              <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
                <span style={{ fontSize: '12px', fontWeight: 'bold' }}>Generator Mode:</span>
                <button 
                  type="button"
                  className={`btn btn-sm ${questionType === 'all_in_one' ? 'btn-primary' : 'btn-secondary'}`}
                  onClick={() => handleSwitchType('all_in_one')}
                  style={{ borderRadius: '20px', fontWeight: questionType === 'all_in_one' ? 700 : 500 }}
                >
                  🌟 1. Master Suite (Obj + Sub)
                </button>
                <button 
                  type="button"
                  className={`btn btn-sm ${questionType === 'dual_track' ? 'btn-primary' : 'btn-secondary'}`}
                  onClick={() => handleSwitchType('dual_track')}
                  style={{ borderRadius: '20px', fontWeight: questionType === 'dual_track' ? 700 : 500 }}
                >
                  ⚡ 2. Dual-Track (Standard + Foundation)
                </button>
                <button 
                  type="button"
                  className={`btn btn-sm ${questionType === 'objective' ? 'btn-primary' : 'btn-secondary'}`}
                  onClick={() => handleSwitchType('objective')}
                  style={{ borderRadius: '20px' }}
                >
                  🎯 3. Objective Only
                </button>
                <button 
                  type="button"
                  className={`btn btn-sm ${questionType === 'subjective' ? 'btn-success' : 'btn-secondary'}`}
                  onClick={() => handleSwitchType('subjective')}
                  style={{ borderRadius: '20px' }}
                >
                  📝 4. Subjective Only
                </button>
              </div>

              <div style={{ display: 'flex', gap: '8px', alignItems: 'center', marginLeft: 'auto' }}>
                <span style={{ fontSize: '12px', fontWeight: 'bold' }}>Category:</span>
                <button 
                  type="button"
                  className={`btn btn-sm ${examCategory === 'standard' ? 'btn-primary' : 'btn-secondary'}`}
                  onClick={() => setExamCategory('standard')}
                  style={{ borderRadius: '20px' }}
                >
                  📘 Standard
                </button>
                <button 
                  type="button"
                  className={`btn btn-sm ${examCategory === 'foundation' ? 'btn-success' : 'btn-secondary'}`}
                  onClick={() => setExamCategory('foundation')}
                  style={{ borderRadius: '20px' }}
                >
                  🏆 Foundation
                </button>
              </div>
            </div>

            {/* Quick Topic Presets & Ratio Customization for Master Suite */}
            {questionType === 'all_in_one' && (
              <div style={{ marginTop: '14px', background: 'var(--bg-soft)', padding: '14px 16px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '12px' }}>
                {/* Row 1: Volume Presets */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                  <span style={{ fontSize: '11px', fontWeight: 800, textTransform: 'uppercase', color: 'var(--accent)' }}>
                    ⚡ Volume Presets (Questions per Topic):
                  </span>
                  <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                    <button
                      type="button"
                      className="btn btn-secondary btn-sm"
                      onClick={() => {
                        setDefaultPerTopicCount(50);
                        const newCounts: Record<string, number> = {};
                        selectedTopics.forEach(t => { newCounts[topicKey(t)] = 50; });
                        setTopicCustomCounts(newCounts);
                      }}
                      style={{ fontSize: '11px', padding: '3px 8px', borderRadius: '12px' }}
                    >
                      🔥 Deep Mastery (50 Qs)
                    </button>
                    <button
                      type="button"
                      className="btn btn-secondary btn-sm"
                      onClick={() => {
                        setDefaultPerTopicCount(30);
                        const newCounts: Record<string, number> = {};
                        selectedTopics.forEach(t => { newCounts[topicKey(t)] = 30; });
                        setTopicCustomCounts(newCounts);
                      }}
                      style={{ fontSize: '11px', padding: '3px 8px', borderRadius: '12px' }}
                    >
                      ⚡ Standard (30 Qs)
                    </button>
                    <button
                      type="button"
                      className="btn btn-secondary btn-sm"
                      onClick={() => {
                        setDefaultPerTopicCount(20);
                        const newCounts: Record<string, number> = {};
                        selectedTopics.forEach(t => { newCounts[topicKey(t)] = 20; });
                        setTopicCustomCounts(newCounts);
                      }}
                      style={{ fontSize: '11px', padding: '3px 8px', borderRadius: '12px' }}
                    >
                      🎯 Compact Drill (20 Qs)
                    </button>
                  </div>
                </div>

                {/* Row 2: Objective vs Subjective Ratio Presets & Slider */}
                <div style={{ borderTop: '1px dashed var(--border-light)', paddingTop: '10px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                    <span style={{ fontSize: '11px', fontWeight: 800, textTransform: 'uppercase', color: 'var(--accent)' }}>
                      ⚖️ Question Type Division Ratio:
                    </span>
                    <div style={{ display: 'flex', gap: '5px', flexWrap: 'wrap' }}>
                      <button
                        type="button"
                        className={`btn btn-sm ${masterObjectiveRatio === 85 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setMasterObjectiveRatio(85)}
                        style={{ fontSize: '11px', padding: '2px 7px', borderRadius: '10px' }}
                      >
                        🎯 85% Obj / 15% Sub
                      </button>
                      <button
                        type="button"
                        className={`btn btn-sm ${masterObjectiveRatio === 70 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setMasterObjectiveRatio(70)}
                        style={{ fontSize: '11px', padding: '2px 7px', borderRadius: '10px' }}
                      >
                        ⚖️ 70% Obj / 30% Sub
                      </button>
                      <button
                        type="button"
                        className={`btn btn-sm ${masterObjectiveRatio === 40 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setMasterObjectiveRatio(40)}
                        style={{ fontSize: '11px', padding: '2px 7px', borderRadius: '10px' }}
                      >
                        📝 40% Obj / 60% Sub
                      </button>
                      <button
                        type="button"
                        className={`btn btn-sm ${masterObjectiveRatio === 100 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setMasterObjectiveRatio(100)}
                        style={{ fontSize: '11px', padding: '2px 7px', borderRadius: '10px' }}
                      >
                        🔘 100% Obj
                      </button>
                      <button
                        type="button"
                        className={`btn btn-sm ${masterObjectiveRatio === 0 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setMasterObjectiveRatio(0)}
                        style={{ fontSize: '11px', padding: '2px 7px', borderRadius: '10px' }}
                      >
                        📄 100% Sub
                      </button>
                    </div>
                  </div>

                  {/* Interactive Slider */}
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px', background: 'var(--surface)', padding: '6px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                    <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--text)', whiteSpace: 'nowrap', minWidth: '150px' }}>
                      🎯 {masterObjectiveRatio}% Obj • 📝 {100 - masterObjectiveRatio}% Sub
                    </span>
                    <input 
                      type="range"
                      min={0}
                      max={100}
                      step={5}
                      value={masterObjectiveRatio}
                      onChange={(e) => setMasterObjectiveRatio(Number(e.target.value))}
                      style={{ flex: 1, accentColor: 'var(--accent)', cursor: 'pointer', height: '6px' }}
                    />
                  </div>
                </div>
                
                {/* Dynamic Breakdown Display */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', marginTop: '2px' }}>
                  {selectedTopics.map((top, idx) => {
                    const key = topicKey(top);
                    const count = topicCustomCounts[key] !== undefined ? Number(topicCustomCounts[key]) || defaultPerTopicCount : defaultPerTopicCount;
                    const c = typeof count === 'number' ? count : (parseInt(String(count), 10) || 30);
                    
                    let objC = 0;
                    let subC = 0;
                    if (masterObjectiveRatio >= 100) {
                      objC = c;
                      subC = 0;
                    } else if (masterObjectiveRatio <= 0) {
                      objC = 0;
                      subC = c;
                    } else {
                      objC = Math.max(1, Math.round(c * (masterObjectiveRatio / 100)));
                      subC = Math.max(1, c - objC);
                    }

                    const easyC = objC > 0 ? Math.max(1, Math.round(objC * 0.30)) : 0;
                    const medC = objC > 0 ? Math.max(1, Math.round(objC * 0.50)) : 0;
                    const hardC = objC > 0 ? Math.max(0, objC - easyC - medC) : 0;

                    const m1C = subC > 0 ? Math.max(1, Math.round(subC * 0.35)) : 0;
                    const m2C = subC > 0 ? Math.max(1, Math.round(subC * 0.40)) : 0;
                    const m4C = subC > 0 ? Math.max(0, subC - m1C - m2C) : 0;

                    return (
                      <div key={idx} style={{ fontSize: '11px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--surface)', padding: '6px 10px', borderRadius: '4px', border: '1px solid var(--border-light)' }}>
                        <span>📍 <strong>Topic {idx + 1}:</strong> {top.topic} (<strong>{c} Qs</strong>)</span>
                        <span style={{ color: 'var(--text-muted)' }}>
                          {objC > 0 && <span>🎯 <strong>{objC} Obj</strong> ({easyC}E / {medC}M / {hardC}H)</span>}
                          {objC > 0 && subC > 0 && <span> + </span>}
                          {subC > 0 && <span>📝 <strong>{subC} Sub</strong> ({m1C}x1M, {m2C}x2M, {m4C}x4M)</span>}
                        </span>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* Quick Topic Presets & Ratio Customization for Dual-Track Mode */}
            {questionType === 'dual_track' && (
              <div style={{ marginTop: '14px', background: 'var(--bg-soft)', padding: '14px 16px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '12px' }}>
                {/* Row 1: Volume Presets */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                  <span style={{ fontSize: '11px', fontWeight: 800, textTransform: 'uppercase', color: 'var(--accent)' }}>
                    ⚡ Dual-Track Volume Presets (Questions per Topic):
                  </span>
                  <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                    <button
                      type="button"
                      className="btn btn-secondary btn-sm"
                      onClick={() => {
                        setDefaultPerTopicCount(120);
                        const newCounts: Record<string, number> = {};
                        selectedTopics.forEach(t => { newCounts[topicKey(t)] = 120; });
                        setTopicCustomCounts(newCounts);
                      }}
                      style={{ fontSize: '11px', padding: '3px 8px', borderRadius: '12px' }}
                    >
                      🏆 Exhaustive (120 Qs)
                    </button>
                    <button
                      type="button"
                      className="btn btn-secondary btn-sm"
                      onClick={() => {
                        setDefaultPerTopicCount(90);
                        const newCounts: Record<string, number> = {};
                        selectedTopics.forEach(t => { newCounts[topicKey(t)] = 90; });
                        setTopicCustomCounts(newCounts);
                      }}
                      style={{ fontSize: '11px', padding: '3px 8px', borderRadius: '12px' }}
                    >
                      🔥 Recommended (90 Qs: 60 Std + 30 Fnd)
                    </button>
                    <button
                      type="button"
                      className="btn btn-secondary btn-sm"
                      onClick={() => {
                        setDefaultPerTopicCount(60);
                        const newCounts: Record<string, number> = {};
                        selectedTopics.forEach(t => { newCounts[topicKey(t)] = 60; });
                        setTopicCustomCounts(newCounts);
                      }}
                      style={{ fontSize: '11px', padding: '3px 8px', borderRadius: '12px' }}
                    >
                      ⚡ Compact (60 Qs)
                    </button>
                  </div>
                </div>

                {/* Row 2: Standard vs Foundation Ratio Presets & Slider */}
                <div style={{ borderTop: '1px dashed var(--border-light)', paddingTop: '10px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                    <span style={{ fontSize: '11px', fontWeight: 800, textTransform: 'uppercase', color: 'var(--accent)' }}>
                      ⚖️ Track Division Ratio:
                    </span>
                    <div style={{ display: 'flex', gap: '5px', flexWrap: 'wrap' }}>
                      <button
                        type="button"
                        className={`btn btn-sm ${dualTrackStandardRatio === 70 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setDualTrackStandardRatio(70)}
                        style={{ fontSize: '11px', padding: '2px 7px', borderRadius: '10px' }}
                      >
                        ⚖️ 70% Std / 30% Fnd
                      </button>
                      <button
                        type="button"
                        className={`btn btn-sm ${dualTrackStandardRatio === 60 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setDualTrackStandardRatio(60)}
                        style={{ fontSize: '11px', padding: '2px 7px', borderRadius: '10px' }}
                      >
                        🎯 60% Std / 40% Fnd
                      </button>
                      <button
                        type="button"
                        className={`btn btn-sm ${dualTrackStandardRatio === 80 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setDualTrackStandardRatio(80)}
                        style={{ fontSize: '11px', padding: '2px 7px', borderRadius: '10px' }}
                      >
                        📘 80% Std / 20% Fnd
                      </button>
                      <button
                        type="button"
                        className={`btn btn-sm ${dualTrackStandardRatio === 50 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setDualTrackStandardRatio(50)}
                        style={{ fontSize: '11px', padding: '2px 7px', borderRadius: '10px' }}
                      >
                        🔘 50% Std / 50% Fnd
                      </button>
                    </div>
                  </div>

                  {/* Interactive Slider */}
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px', background: 'var(--surface)', padding: '6px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                    <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--text)', whiteSpace: 'nowrap', minWidth: '180px' }}>
                      📘 {dualTrackStandardRatio}% Standard • 🏆 {100 - dualTrackStandardRatio}% Foundation
                    </span>
                    <input 
                      type="range"
                      min={0}
                      max={100}
                      step={5}
                      value={dualTrackStandardRatio}
                      onChange={(e) => setDualTrackStandardRatio(Number(e.target.value))}
                      style={{ flex: 1, accentColor: 'var(--accent)', cursor: 'pointer', height: '6px' }}
                    />
                  </div>
                </div>
                
                {/* Dynamic Breakdown Display */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', marginTop: '2px' }}>
                  {selectedTopics.map((top, idx) => {
                    const key = topicKey(top);
                    const count = topicCustomCounts[key] !== undefined ? Number(topicCustomCounts[key]) || defaultPerTopicCount : defaultPerTopicCount;
                    const c = typeof count === 'number' ? count : (parseInt(String(count), 10) || 90);
                    
                    let stdC = 0;
                    let fndC = 0;
                    if (dualTrackStandardRatio >= 100) {
                      stdC = c;
                      fndC = 0;
                    } else if (dualTrackStandardRatio <= 0) {
                      stdC = 0;
                      fndC = c;
                    } else {
                      stdC = Math.max(1, Math.round(c * (dualTrackStandardRatio / 100)));
                      fndC = Math.max(1, c - stdC);
                    }

                    const stdEasy = stdC > 0 ? Math.max(1, Math.round(stdC * 0.30)) : 0;
                    const stdMed = stdC > 0 ? Math.max(1, Math.round(stdC * 0.50)) : 0;
                    const stdHard = stdC > 0 ? Math.max(0, stdC - stdEasy - stdMed) : 0;

                    const fndEasy = fndC > 0 ? Math.max(1, Math.round(fndC * 0.10)) : 0;
                    const fndMed = fndC > 0 ? Math.max(1, Math.round(fndC * 0.40)) : 0;
                    const fndHard = fndC > 0 ? Math.max(0, fndC - fndEasy - fndMed) : 0;

                    return (
                      <div key={idx} style={{ fontSize: '11px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--surface)', padding: '6px 10px', borderRadius: '4px', border: '1px solid var(--border-light)' }}>
                        <span>📍 <strong>Topic {idx + 1}:</strong> {top.topic} (<strong>{c} Qs</strong>)</span>
                        <span style={{ color: 'var(--text-muted)' }}>
                          {stdC > 0 && <span>📘 <strong>{stdC} Standard</strong> ({stdEasy}E / {stdMed}M / {stdHard}H)</span>}
                          {stdC > 0 && fndC > 0 && <span> + </span>}
                          {fndC > 0 && <span>🏆 <strong>{fndC} Foundation</strong> ({fndEasy}E / {fndMed}M / {fndHard}H HOTS)</span>}
                        </span>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* Exam Blueprint Matcher (shown for individual objective/subjective modes) */}
            {(questionType === 'objective' || questionType === 'subjective') && (
              <div style={{ marginTop: '16px', borderTop: '1px dashed var(--border-light)', paddingTop: '12px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                  <label style={{ fontSize: '12px', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <span>🎯 Exam Blueprint Matcher:</span>
                    <span style={{ fontSize: '11px', fontWeight: 'normal', color: 'var(--text-muted)' }}>
                      (Applies exam pedagogical composition &amp; difficulty to your {getTotalTargetQuestions()} questions)
                    </span>
                  </label>
                </div>

                <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
                  {(questionType === 'objective' ? CANONICAL_QB_OBJECTIVE_BLUEPRINTS : CANONICAL_QB_SUBJECTIVE_BLUEPRINTS).map(bp => {
                    const isSelected = selectedBlueprintId === bp.id;
                    return (
                      <button
                        key={bp.id}
                        type="button"
                        onClick={() => {
                          setSelectedBlueprintId(bp.id);
                          if (bp.examCategory) setExamCategory(bp.examCategory);
                        }}
                        style={{
                          padding: '6px 12px',
                          borderRadius: 'var(--radius-sm)',
                          border: isSelected ? '1.5px solid var(--accent)' : '1px solid var(--border-light)',
                          background: isSelected ? 'rgba(52, 152, 219, 0.15)' : 'var(--bg-soft)',
                          color: isSelected ? 'var(--accent)' : 'var(--text)',
                          fontWeight: isSelected ? 700 : 500,
                          fontSize: '12px',
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '6px',
                          transition: 'all 0.15s ease'
                        }}
                        title={bp.description}
                      >
                        <span>{bp.icon}</span>
                        <span>{bp.name}</span>
                      </button>
                    );
                  })}
                </div>

                {/* Active Blueprint Summary */}
                <div style={{ marginTop: '8px', fontSize: '11px', color: 'var(--text-muted)', background: 'var(--bg-soft)', padding: '6px 10px', borderRadius: '4px', borderLeft: '3px solid var(--accent)' }}>
                  <strong>Active Blueprint:</strong> {getSelectedBlueprint().name} — {getSelectedBlueprint().description}
                </div>
              </div>
            )}

            {/* Subjective verbatim requirements warning */}
            {questionType === 'subjective' && (
              <div style={{ marginTop: '16px', padding: '12px', background: 'rgba(243, 156, 18, 0.15)', color: '#f39c12', borderRadius: 'var(--radius-sm)', borderLeft: '4px solid #f39c12' }}>
                <p style={{ margin: '0 0 6px', fontWeight: 'bold', fontSize: '12px' }}>⚠️ Verbatim Textbook Requirements for Subjective Questions:</p>
                <ul style={{ margin: 0, paddingLeft: '20px', fontSize: '11px' }}>
                  <li>Answers must exactly match prescribed textbook vocabulary.</li>
                  <li>Separate each answer sentence on a new numbered line (1., 2., 3...).</li>
                  <li>Keywords must be clearly defined for underlining student feedback.</li>
                  <li>No paraphrasing allowed - absolute verbatim alignment is required.</li>
                </ul>
              </div>
            )}

            <div style={{ display: 'flex', gap: '10px', justifyContent: 'flex-end', marginTop: '16px' }}>
              <button className="btn btn-secondary" onClick={clearAllSelections}>Clear All</button>
              
              <button className="btn btn-primary" onClick={handleGeneratePrompt}>
                🔧 Generate &amp; Copy AI Prompt
              </button>
            </div>
          </div>
        )}

        {/* Card 3: AI Workspace Prompt and response */}
        <div id="aiWorkspaceSection" style={{ display: 'grid', gridTemplateColumns: '1fr', gap: '16px' }}>
          
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '16px' }}>
            {/* Prompt generated view */}
            <div className="card" style={{ background: 'var(--surface)', padding: '18px 24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <h3 style={{ fontSize: '13px', fontWeight: 800, margin: 0, textTransform: 'uppercase', color: 'var(--accent)' }}>📋 Generated AI Prompt</h3>
                {aiPrompt && (
                  <button 
                    className="btn btn-secondary btn-sm" 
                    onClick={() => {
                      navigator.clipboard.writeText(aiPrompt);
                      triggerAlert('Success', '📋 Prompt copied to clipboard!', undefined, false, 1000);
                    }}
                    style={{ padding: '2px 8px', fontSize: '10px' }}
                  >
                    Copy
                  </button>
                )}
              </div>
              <textarea 
                placeholder="Configure mapping configurations and click generate AI prompt above..."
                value={aiPrompt}
                onChange={(e) => setAiPrompt(e.target.value)}
                style={{ width: '100%', height: '140px', background: 'var(--bg-soft)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '8px', fontSize: '11px', fontFamily: 'monospace', color: 'var(--text)' }}
              />
            </div>

            {/* Paste Response block */}
            <div id="paste-response-card" className="card" style={{ background: 'var(--surface)', padding: '18px 24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <h3 style={{ fontSize: '13px', fontWeight: 800, margin: 0, textTransform: 'uppercase', color: 'var(--accent)' }}>📥 Paste AI Response</h3>
                <button 
                  className="btn btn-secondary btn-sm" 
                  onClick={async () => {
                    try {
                      const text = await navigator.clipboard.readText();
                      setAiPasteText(text);
                    } catch (e) {
                      triggerAlert('Clipboard Access Denied', 'Clipboard access denied. Use Ctrl+V to paste.');
                    }
                  }}
                  style={{ padding: '2px 8px', fontSize: '10px' }}
                >
                  Paste
                </button>
              </div>
              <textarea 
                placeholder="Paste JSON output array from Gemini here..."
                value={aiPasteText}
                onChange={(e) => setAiPasteText(e.target.value)}
                style={{ width: '100%', height: '140px', background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '8px', fontSize: '11px', fontFamily: 'monospace', color: 'var(--text)' }}
              />
            </div>
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
            <button className="btn btn-primary" onClick={handleParseJSON} style={{ padding: '10px 24px' }}>
              ⚙️ Parse &amp; Preview Questions
            </button>
          </div>
        </div>

        {/* Card 4: Preview Questions & Repair */}
        {generatedQuestions.length > 0 && (() => {
          const validation = validateQuestionsForSave(generatedQuestions);
          const visibleQuestions = generatedQuestions.map((q, idx) => ({ q, idx })).filter(({ idx }) => {
            if (previewFilter === 'issues') {
              return validation.invalidIndices.has(idx);
            }
            return true;
          });

          return (
            <div id="previewQuestionsSection" className="card" style={{ background: 'var(--surface)', padding: '18px 24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '16px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px', flexWrap: 'wrap', gap: '10px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                  <h3 style={{ fontSize: '13px', fontWeight: 800, margin: 0, textTransform: 'uppercase', color: 'var(--success)' }}>
                    Parsed Questions Preview ({generatedQuestions.length} items)
                  </h3>

                  {/* Filter View Switcher */}
                  <div style={{ display: 'flex', background: 'var(--bg-soft)', borderRadius: '20px', padding: '2px', border: '1px solid var(--border-light)' }}>
                    <button
                      type="button"
                      onClick={() => setPreviewFilter('all')}
                      style={{
                        padding: '3px 10px',
                        fontSize: '11px',
                        fontWeight: 600,
                        borderRadius: '16px',
                        border: 'none',
                        background: previewFilter === 'all' ? 'var(--accent)' : 'transparent',
                        color: previewFilter === 'all' ? '#ffffff' : 'var(--text-muted)',
                        cursor: 'pointer',
                        transition: 'all 0.2s'
                      }}
                    >
                      All ({generatedQuestions.length})
                    </button>
                    <button
                      type="button"
                      onClick={() => setPreviewFilter('issues')}
                      style={{
                        padding: '3px 10px',
                        fontSize: '11px',
                        fontWeight: 600,
                        borderRadius: '16px',
                        border: 'none',
                        background: previewFilter === 'issues' ? '#e74c3c' : 'transparent',
                        color: previewFilter === 'issues' ? '#ffffff' : (validation.invalidIndices.size > 0 ? '#e74c3c' : 'var(--text-muted)'),
                        cursor: 'pointer',
                        transition: 'all 0.2s',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '4px'
                      }}
                    >
                      ⚠️ Issues Only ({validation.invalidIndices.size})
                    </button>
                  </div>
                </div>
                
                <div style={{ display: 'flex', gap: '8px' }}>
                  <button className="btn btn-secondary" onClick={() => setGeneratedQuestions([])}>
                    Cancel
                  </button>
                   <button className="btn btn-primary" onClick={handleBulkSave} disabled={savingProgress}>
                    💾 Save all to Question Bank
                  </button>
                </div>
              </div>

              {/* Parsed Suite Breakdown Summary */}
              {(() => {
                const objList = generatedQuestions.filter(q => !q.type?.startsWith('subjective_') && !q.type?.startsWith('numerical_') && (!q.marks || q.marks === 4 || q.options?.length > 0));
                const subList = generatedQuestions.filter(q => q.type?.startsWith('subjective_') || q.type?.startsWith('numerical_') || (q.marks && !q.options?.length && q.type !== 'numerical'));
                const easyC = objList.filter(q => q.difficulty === 'easy').length;
                const medC = objList.filter(q => q.difficulty === 'medium').length;
                const hardC = objList.filter(q => q.difficulty === 'hard').length;
                const m1C = subList.filter(q => q.marks === 1 || q.type === 'subjective_define' || q.type === 'subjective_laws').length;
                const m2C = subList.filter(q => q.marks === 2 || q.type === 'subjective_short' || q.type === 'subjective_reason' || q.type === 'numerical_short').length;
                const m4C = subList.filter(q => q.marks === 4 || q.type === 'subjective_long' || q.type === 'numerical_long').length;

                return (
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', background: 'var(--bg-soft)', padding: '10px 14px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', fontSize: '11px', alignItems: 'center' }}>
                    <span style={{ fontWeight: 700, color: 'var(--accent)' }}>📊 Suite Composition:</span>
                    {objList.length > 0 && (
                      <span style={{ background: 'rgba(52, 152, 219, 0.15)', color: '#2980b9', padding: '3px 8px', borderRadius: '12px', fontWeight: 600 }}>
                        🎯 <strong>{objList.length} Objective</strong> ({easyC} Easy, {medC} Med, {hardC} Hard)
                      </span>
                    )}
                    {subList.length > 0 && (
                      <span style={{ background: 'rgba(46, 204, 113, 0.15)', color: '#27ae60', padding: '3px 8px', borderRadius: '12px', fontWeight: 600 }}>
                        📝 <strong>{subList.length} Subjective</strong> ({m1C} × 1M, {m2C} × 2M, {m4C} × 4M)
                      </span>
                    )}
                  </div>
                );
              })()}

              {/* TOP VALIDATION ISSUES ACTION BANNER */}
              {!validation.valid && (
                <div style={{ padding: '12px 16px', borderRadius: 'var(--radius-sm)', background: 'rgba(231, 76, 60, 0.12)', border: '1.5px solid #e74c3c', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <div style={{ fontSize: '12px', fontWeight: 'bold', color: '#e74c3c', display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <span>⚠️ {validation.errors.length} validation issue{validation.errors.length > 1 ? 's' : ''} require attention before saving:</span>
                    </div>
                    {previewFilter !== 'issues' && (
                      <button
                        type="button"
                        onClick={() => setPreviewFilter('issues')}
                        style={{ background: '#e74c3c', color: '#ffffff', border: 'none', borderRadius: '4px', padding: '3px 8px', fontSize: '11px', fontWeight: 600, cursor: 'pointer' }}
                      >
                        🔍 Show only problematic questions
                      </button>
                    )}
                  </div>
                  
                  {/* Clickable Quick Jump Pills */}
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', maxHeight: '120px', overflowY: 'auto', paddingTop: '4px' }}>
                    {validation.errorItems.map((item, errIdx) => (
                      <button
                        key={errIdx}
                        type="button"
                        onClick={() => {
                          setPreviewFilter('all');
                          setTimeout(() => {
                            const el = document.getElementById(`preview-q-${item.index}`);
                            if (el) {
                              el.scrollIntoView({ behavior: 'smooth', block: 'center' });
                              el.style.boxShadow = '0 0 15px rgba(231, 76, 60, 0.6)';
                              setTimeout(() => { el.style.boxShadow = ''; }, 2000);
                            }
                          }, 50);
                        }}
                        style={{
                          background: 'var(--surface)',
                          border: '1px solid #e74c3c',
                          color: '#e74c3c',
                          padding: '4px 8px',
                          borderRadius: '4px',
                          fontSize: '11px',
                          fontWeight: 600,
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '4px',
                          textAlign: 'left'
                        }}
                        title="Click to jump directly to this question and fix"
                      >
                        <span>🎯 Fix <strong>Q{item.qNum}</strong>:</span>
                        <span style={{ fontWeight: 'normal', color: 'var(--text)' }}>{item.error.replace(/^Q\d+:\s*/, '')}</span>
                      </button>
                    ))}
                  </div>
                </div>
              )}

              {/* Questions preview grid container */}
              <div id="questionsListPreviewContainer" style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '480px', overflowY: 'auto', paddingRight: '8px' }}>
                {visibleQuestions.map(({ q, idx }) => {
                  const hasErrors = !!validation.questionErrorsMap[idx];
                  const qErrors = validation.questionErrorsMap[idx] || [];

                  return (
                    <div 
                      key={idx} 
                      id={`preview-q-${idx}`}
                      style={{ 
                        background: hasErrors ? 'rgba(231, 76, 60, 0.04)' : 'var(--bg-soft)', 
                        padding: '12px', 
                        borderRadius: 'var(--radius-sm)', 
                        borderLeft: hasErrors ? '5px solid #e74c3c' : '4px solid var(--accent)',
                        border: hasErrors ? '1.5px solid rgba(231, 76, 60, 0.4)' : '1px solid var(--border-light)',
                        display: 'flex', 
                        justifyContent: 'space-between', 
                        alignItems: 'start', 
                        gap: '15px',
                        transition: 'box-shadow 0.3s'
                      }}
                    >
                      <div style={{ flex: 1 }}>
                        {/* Inline Error Callout on Question Card */}
                        {hasErrors && (
                          <div style={{ padding: '6px 10px', background: 'rgba(231, 76, 60, 0.15)', border: '1px solid #e74c3c', borderRadius: '4px', color: '#e74c3c', fontSize: '11px', fontWeight: 600, marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                            <span>⚠️ Issue:</span>
                            <span>{qErrors.join(' | ')}</span>
                          </div>
                        )}

                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '6px' }}>
                          <span>Type: <strong>{q.type}</strong> | Difficulty: <strong>{q.difficulty}</strong> | Bloom: <strong>{q.bloomLevel || 'Remember'}</strong></span>
                          <span>Ch {q.chapterNumber || '1'} • Topic {q.topicNumber || '1.1'}</span>
                        </div>
                        
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', marginBottom: '8px' }}>
                          <label style={{ fontSize: '10px', fontWeight: 700, color: hasErrors ? '#e74c3c' : 'var(--text-muted)', textTransform: 'uppercase' }}>
                            Question {idx + 1}:
                          </label>
                          <textarea
                            value={q.text}
                            onChange={(e) => {
                              const val = e.target.value;
                              setGeneratedQuestions(prev => {
                                const next = [...prev];
                                next[idx] = { ...next[idx], text: val };
                                return next;
                              });
                            }}
                            style={{
                              width: '100%',
                              minHeight: '44px',
                              background: 'var(--surface)',
                              border: hasErrors ? '1.5px solid #e74c3c' : '1px solid var(--border-light)',
                              borderRadius: '4px',
                              padding: '6px 8px',
                              fontSize: '12px',
                              fontWeight: 600,
                              color: 'var(--text)',
                              resize: 'vertical',
                              outline: 'none'
                            }}
                          />
                          {/* Live Math Render Preview */}
                          <div className="math-container" style={{ fontSize: '11.5px', color: 'var(--text-muted)', marginTop: '4px', padding: '4px 8px', background: 'rgba(255, 255, 255, 0.03)', border: '1px dashed var(--border-light)', borderRadius: '4px', minHeight: '18px', whiteSpace: 'pre-line' }}>
                            {preprocessMathText(q.text)}
                          </div>
                        </div>

                        {/* Proctoring Settings */}
                        <div style={{ marginTop: '4px', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '11px', cursor: 'pointer', userSelect: 'none', color: 'var(--text)' }}>
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
                              style={{ cursor: 'pointer', width: '13px', height: '13px' }}
                            />
                            <span>Relax Camera Proctoring (Numerical / Mathematical question requiring calculations)</span>
                          </label>
                        </div>

                        {/* Subjective preview formatting */}
                        {(questionType === 'subjective' || q.type?.startsWith('subjective_') || (q.marks && !q.options?.length && q.type !== 'numerical')) ? (
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', background: 'var(--surface)', padding: '10px', borderRadius: '6px', fontSize: '11px', border: '1px solid var(--border-light)' }}>
                            <span style={{ fontWeight: 'bold', color: 'var(--text)' }}>Verbatim textbook lines:</span>
                            {q.answerLines?.map((line: any, li: number) => (
                              <div key={li}>{line.lineNo}. {line.text}</div>
                            ))}

                            {/* Editable Keywords Field */}
                            <div style={{ marginTop: '6px', paddingTop: '8px', borderTop: '1px dashed var(--border-light)' }}>
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
                                style={{ width: '100%', padding: '6px 10px', fontSize: '11px', borderRadius: '4px', background: 'var(--bg-soft)', color: 'var(--text)', border: '1px solid var(--border-light)' }}
                              />
                            </div>

                            {/* Live Keyword Highlight Preview */}
                            {q.solution && (
                              <div style={{ marginTop: '4px', fontSize: '11px', lineHeight: 1.6, padding: '8px 10px', background: 'var(--bg-soft)', borderRadius: '4px', border: '1px solid var(--border-light)' }}>
                                <strong style={{ display: 'block', fontSize: '10px', textTransform: 'uppercase', color: 'var(--text-muted)', marginBottom: '4px' }}>
                                  💡 Live Model Answer Highlight Preview:
                                </strong>
                                <div 
                                  dangerouslySetInnerHTML={{ 
                                    __html: highlightModelAnswerKeywords(q.solution, q.keywords) 
                                  }} 
                                />
                              </div>
                            )}
                          </div>
                        ) : (
                          /* Objective preview formatting */
                          <>
                            {q.options && q.options.length > 0 && (
                              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', marginTop: '6px' }}>
                                {q.options.map((opt: string, oi: number) => {
                                  const isCorrect = normalizeOptionText(opt) === normalizeOptionText(q.correctAnswer) || 
                                    (q.correctAnswers && q.correctAnswers.some((ans: string) => normalizeOptionText(ans) === normalizeOptionText(opt)));
                                  return (
                                    <div 
                                      key={oi} 
                                      style={{ 
                                        display: 'flex', 
                                        flexDirection: 'column', 
                                        gap: '4px',
                                        background: isCorrect ? 'rgba(46, 204, 113, 0.08)' : 'var(--surface)',
                                        border: isCorrect ? '1.5px solid #2ecc71' : '1px solid var(--border-light)',
                                        borderRadius: '6px',
                                        padding: '6px 8px',
                                        transition: 'all 0.2s'
                                      }}
                                    >
                                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', width: '100%' }}>
                                        {/* Select Indicator */}
                                        <div 
                                          onClick={() => {
                                            setGeneratedQuestions(prev => {
                                              const next = [...prev];
                                              const currentQ = { ...next[idx] };
                                              if (currentQ.type === 'multiple_mcq') {
                                                const cAnswers = Array.isArray(currentQ.correctAnswers) ? [...currentQ.correctAnswers] : [];
                                                const exists = cAnswers.some((ans: string) => normalizeOptionText(ans) === normalizeOptionText(opt));
                                                if (exists) {
                                                  currentQ.correctAnswers = cAnswers.filter((ans: string) => normalizeOptionText(ans) !== normalizeOptionText(opt));
                                                } else {
                                                  currentQ.correctAnswers = [...cAnswers, opt];
                                                }
                                                currentQ.correctAnswer = currentQ.correctAnswers[0] || '';
                                              } else {
                                                currentQ.correctAnswer = opt;
                                                currentQ.correctAnswers = [opt];
                                              }
                                              next[idx] = currentQ;
                                              return next;
                                            });
                                          }}
                                          style={{
                                            width: '18px',
                                            height: '18px',
                                            borderRadius: q.type === 'multiple_mcq' ? '4px' : '50%',
                                            border: isCorrect ? '2px solid #2ecc71' : '2px solid var(--text-muted)',
                                            background: isCorrect ? '#2ecc71' : 'transparent',
                                            display: 'flex',
                                            alignItems: 'center',
                                            justifyContent: 'center',
                                            cursor: 'pointer',
                                            color: '#ffffff',
                                            fontSize: '10px',
                                            fontWeight: 'bold',
                                            userSelect: 'none'
                                          }}
                                          title={q.type === 'multiple_mcq' ? 'Toggle correct option' : 'Set as correct option'}
                                        >
                                          {isCorrect && '✓'}
                                        </div>

                                        {/* Option Text Input */}
                                        <input 
                                          type="text"
                                          value={opt}
                                          onChange={(e) => {
                                            const val = e.target.value;
                                            setGeneratedQuestions(prev => {
                                              const next = [...prev];
                                              const currentQ = { ...next[idx] };
                                              const opts = [...(currentQ.options || [])];
                                              const oldVal = opts[oi];
                                              opts[oi] = val;
                                              currentQ.options = opts;
                                              
                                              // Sync correctness mapping
                                              if (currentQ.correctAnswer === oldVal) {
                                                currentQ.correctAnswer = val;
                                              }
                                              if (Array.isArray(currentQ.correctAnswers)) {
                                                currentQ.correctAnswers = currentQ.correctAnswers.map((a: string) => a === oldVal ? val : a);
                                              }
                                              next[idx] = currentQ;
                                              return next;
                                            });
                                          }}
                                          style={{
                                            flex: 1,
                                            border: 'none',
                                            background: 'transparent',
                                            fontSize: '11.5px',
                                            color: 'var(--text)',
                                            padding: '4px 6px',
                                            outline: 'none'
                                          }}
                                          placeholder={`Option ${String.fromCharCode(65 + oi)}`}
                                        />
                                      </div>

                                      {/* Live Math Render Preview (Only shown when opt contains math formatting to avoid duplicates) */}
                                      {/\\\(|\\\)|\\\[|\\\]|\$\$|\$|\\ce/g.test(opt) && (
                                        <div className="math-container" style={{ fontSize: '11px', color: 'var(--text-muted)', paddingLeft: '26px', borderTop: '1px dashed rgba(255,255,255,0.02)', paddingTop: '2px' }}>
                                          {preprocessMathText(opt)}
                                        </div>
                                      )}
                                    </div>
                                  );
                                })}
                              </div>
                            )}
                            {q.correctAnswer && !q.options && (
                              <div style={{ fontSize: '11px', marginTop: '6px', color: 'var(--success)' }}>
                                <strong>Correct:</strong> <span className="math-container">{preprocessMathText(q.correctAnswer)}</span>
                              </div>
                            )}
                            <div style={{ marginTop: '8px' }}>
                              <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>
                                Solution / Explanation:
                              </label>
                              <textarea
                                value={q.solution || ''}
                                onChange={(e) => {
                                  const val = e.target.value;
                                  setGeneratedQuestions(prev => {
                                    const next = [...prev];
                                    next[idx] = { ...next[idx], solution: val };
                                    return next;
                                  });
                                }}
                                style={{
                                  width: '100%',
                                  minHeight: '35px',
                                  background: 'var(--surface)',
                                  border: '1px solid var(--border-light)',
                                  borderRadius: '4px',
                                  padding: '4px 6px',
                                  fontSize: '11px',
                                  color: 'var(--text)',
                                  resize: 'vertical',
                                  outline: 'none',
                                  fontStyle: 'italic'
                                }}
                              />
                              {/* Live Math Render Preview */}
                              <div className="math-container" style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '4px', padding: '4px 8px', background: 'rgba(255, 255, 255, 0.03)', border: '1px dashed var(--border-light)', borderRadius: '4px', minHeight: '18px', whiteSpace: 'pre-line' }}>
                                {preprocessMathText(q.solution || '')}
                              </div>
                            </div>
                          </>
                        )}
                        <div style={{ marginTop: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                          <label style={{ fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer', fontWeight: 600, color: 'var(--text)' }}>
                            <input 
                              type="checkbox" 
                              checked={!!q.requiresFigure} 
                              onChange={(e) => {
                                setGeneratedQuestions(prev => {
                                  const next = [...prev];
                                  next[idx] = { ...next[idx], requiresFigure: e.target.checked };
                                  return next;
                                });
                              }}
                            />
                            📸 Requires Figure / Diagram
                          </label>
                        </div>

                        {q.requiresFigure && (
                          <div style={{ marginTop: '8px', padding: '8px 12px', background: 'rgba(230, 126, 34, 0.1)', border: '1px dashed var(--warning)', borderRadius: '6px' }}>
                            <label style={{ display: 'block', fontSize: '11px', fontWeight: 'bold', color: 'var(--warning)', marginBottom: '4px' }}>
                              ⚠️ Figure/Diagram Required: Please upload:
                            </label>
                            <input 
                              type="file" 
                              accept="image/*" 
                              onChange={(e) => {
                                const file = e.target.files?.[0];
                                if (!file) return;
                                const reader = new FileReader();
                                reader.onload = (event) => {
                                  setGeneratedQuestions(prev => {
                                    const next = [...prev];
                                    next[idx] = { ...next[idx], imageUrl: event.target?.result as string };
                                    return next;
                                  });
                                };
                                reader.readAsDataURL(file);
                              }}
                              style={{ fontSize: '10px' }}
                            />
                            {q.imageUrl && (
                              <div style={{ marginTop: '6px' }}>
                                 <Image src={q.imageUrl} alt="Uploaded figure" width={120} height={90} style={{ objectFit: 'contain', borderRadius: '4px', border: '1px solid var(--border-light)' }} />
                              </div>
                            )}
                          </div>
                        )}
                      </div>

                      <button className="btn btn-danger btn-sm" onClick={() => handleDeletePreviewQuestion(idx)} style={{ padding: '4px 8px', fontSize: '10px' }}>
                        🗑️ Delete
                      </button>
                    </div>
                  );
                })}
              </div>
            </div>
          );
        })()}

      </main>



      {/* Bulk Save Progress Modal */}
      {savingProgress && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.8)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', padding: '30px', maxWidth: '420px', width: '90%', textAlign: 'center', border: '1px solid var(--border-light)', margin: 'auto' }}>
            <h3 style={{ margin: '0 0 6px', color: 'var(--text)', fontSize: '16px' }}>💾 Saving Questions...</h3>
            <p style={{ fontSize: '12px', color: 'var(--text-muted)', marginBottom: '18px' }}>
              Writing database records sequentially. Do not close this browser tab.
            </p>
            <div style={{ width: '100%', height: '14px', borderRadius: '8px', background: 'var(--bg-soft)', overflow: 'hidden', border: '1px solid var(--border-light)' }}>
              <div style={{ height: '100%', width: `${savePercentage}%`, background: 'var(--accent)', borderRadius: '8px', transition: 'width 0.2s ease' }} />
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '10px', fontSize: '11px', color: 'var(--text-muted)' }}>
              <span>Progress: {savePercentage}%</span>
              <span>{saveStats.current} / {saveStats.total} Saved</span>
            </div>
          </div>
        </div>
      )}



      {/* Themed Confirmation Modal */}
      {showConfirmModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 30000 }}>
          <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '440px', width: '90%', display: 'flex', flexDirection: 'column', gap: '16px', boxShadow: '0 10px 25px rgba(0,0,0,0.2)' }}>
            <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 'bold', color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '8px' }}>
              ❓ {confirmTitle || 'Confirm Action'}
            </h3>
            <p style={{ margin: 0, fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.5' }}>
              {confirmMessage}
            </p>
            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '4px' }}>
              <button 
                type="button" 
                className="btn btn-secondary" 
                onClick={() => {
                  setShowConfirmModal(false);
                  if (onCancelCallback) onCancelCallback();
                  setOnConfirmCallback(null);
                  setOnCancelCallback(null);
                }}
              >
                Cancel
              </button>
              <button 
                type="button" 
                className="btn btn-primary" 
                onClick={() => {
                  setShowConfirmModal(false);
                  if (onConfirmCallback) onConfirmCallback();
                  setOnConfirmCallback(null);
                  setOnCancelCallback(null);
                }}
              >
                Confirm
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Themed Alert Modal */}
      {showAlertModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 30000 }}>
          <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '440px', width: '90%', display: 'flex', flexDirection: 'column', gap: '16px', boxShadow: '0 10px 25px rgba(0,0,0,0.2)' }}>
            <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 'bold', color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '8px' }}>
              {alertTitle?.toLowerCase().includes('success') ? '✅' : '⚠️'} {alertTitle || 'Notice'}
            </h3>
            <p style={{ margin: 0, fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.5' }}>
              {alertMessage}
            </p>
            {alertHasOkButton && (
              <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '4px' }}>
                <button 
                  type="button" 
                  className="btn btn-primary" 
                  onClick={() => {
                    setShowAlertModal(false);
                    if (onAlertCloseCallback) onAlertCloseCallback();
                    setOnAlertCloseCallback(null);
                  }}
                >
                  OK
                </button>
              </div>
            )}
          </div>
        </div>
      )}

    </div>
  );
}

export default function CreateQBPage() {
  return (
    <React.Suspense fallback={<div style={{ padding: '40px', color: 'var(--text-muted)' }}>Loading Question Bank generator...</div>}>
      <CreateQBContent />
    </React.Suspense>
  );
}
