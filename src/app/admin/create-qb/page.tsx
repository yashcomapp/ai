'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter, useSearchParams } from 'next/navigation';
import Script from 'next/script';
import { useMathRender } from '@/hooks/useMathRender';
import { preprocessMathText, robustParseAIJson, validateQuestion, normalizeOptionText, cleanOptionPrefix, cleanStringForMatch, isOptionMatch, shuffleArray, normalizeBloomLevel, BLOOM_TAXONOMY_MAP } from '@/lib/questionTypes';
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


  // Topic Distribution and Custom Counts State
  const [weightageMode, setWeightageMode] = useState<'equal' | 'custom'>('equal');
  const [topicWeightageMode, setTopicWeightageMode] = useState<'custom_counts' | 'equal' | 'percentage'>('custom_counts');
  const [topicWeightageMap, setTopicWeightageMap] = useState<Record<string, number | string>>({});
  const [topicCustomCounts, setTopicCustomCounts] = useState<Record<string, number | string>>({});
  const [defaultPerTopicCount, setDefaultPerTopicCount] = useState<number | string>(80);
  const [totalBatchQuestions, setTotalBatchQuestions] = useState<number | string>(80);







  // Image Upload State
  const [uploadedImageBase64, setUploadedImageBase64] = useState<string | null>(null);

  // Question Type and Generation settings
  const [questionType, setQuestionType] = useState<'objective' | 'subjective'>('objective');
  const [examCategory, setExamCategory] = useState<'standard' | 'foundation'>('standard');
  const [vault, setVault] = useState<'practice' | 'exam' | 'mock'>('practice');
  const [includeNumericals, setIncludeNumericals] = useState<boolean>(false);
  const [numericalsManuallyToggled, setNumericalsManuallyToggled] = useState<boolean>(false);

  useEffect(() => {
    const qtype = searchParams.get('questionType');
    if (qtype === 'subjective' || qtype === 'objective') {
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

  // Auto-detect whether selected subject/topics are mathematical or calculative physics to suggest numericals default
  useEffect(() => {
    if (numericalsManuallyToggled) return;
    const subjs = Object.keys(selectedSubjects);
    if (subjs.length === 0) return;
    const primary = subjs[0] || '';
    const isMath = /math|algebra|geometry|ganit/i.test(primary);
    const isPhysics = /physic|motion|force|gravitat|light|electric|circuit|sound|work|energy|power|heat|kinematics|optics/i.test(primary);
    setIncludeNumericals(isMath || isPhysics);
  }, [selectedSubjects, numericalsManuallyToggled]);



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

  const handleSwitchType = (type: 'objective' | 'subjective') => {
    setQuestionType(type);
    if (type === 'subjective') {
      const currentVal = Number(defaultPerTopicCount) || 80;
      if (currentVal > 20) {
        setDefaultPerTopicCount(10);
        if (selectedTopics[0]) {
          setTopicCustomCounts({ [topicKey(selectedTopics[0])]: 10 });
        }
      }
    } else {
      const currentVal = Number(defaultPerTopicCount) || 10;
      if (currentVal < 30) {
        setDefaultPerTopicCount(80);
        if (selectedTopics[0]) {
          setTopicCustomCounts({ [topicKey(selectedTopics[0])]: 80 });
        }
      }
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

  const getTotalTargetQuestions = (): number => {
    return typeof defaultPerTopicCount === 'number' ? defaultPerTopicCount : (parseInt(String(defaultPerTopicCount), 10) || 80);
  };

  const getEffectiveTopicCounts = (): Record<string, number> => {
    const map: Record<string, number> = {};
    const count = getTotalTargetQuestions();
    const promptTopics = getPromptTargetTopics();
    promptTopics.forEach(t => {
      map[topicKey(t)] = count;
    });
    return map;
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
  const compilePrompt = (type: 'objective' | 'subjective') => {
    if (!selectedBoard || !selectedClass || getSelectedSubjectsCount() === 0 || selectedTopics.length === 0) {
      return '';
    }

    const subj = getSelectedSubjectsList()[0] || '';
    const isMath = /math|algebra|geometry|ganit/i.test(subj);
    const isFoundation = examCategory === 'foundation';
    const totalQs = getTotalTargetQuestions() || 10;
    const topicCounts = getEffectiveTopicCounts();
    const ctx = buildTopicsContextBlock(topicCounts);
    const promptTopics = getPromptTargetTopics();

    let requirementsSection = '';
    if (paramRequirements) {
      requirementsSection = `\n========================================\nCONSOLIDATED STUDENT REQUESTED REQUIREMENTS:\n========================================\nPlease generate questions specifically matching these student requested targets:\n${paramRequirements.split(', ').map(r => `- ${r}`).join('\n')}\n`;
    }

    const isCalculativeTopic = isMath || promptTopics.some(t => {
      const text = `${t.subject || ''} ${t.chapterName || ''} ${t.topic || ''}`.toLowerCase();
      return /physic|motion|force|gravitat|light|reflection|refraction|electric|current|circuit|sound|work|energy|power|heat|thermodynamic|optics|lens|mirror|wave|mole concept|stoichiometr|density|pressure|floatation|kinematics|fluid|magnetic/i.test(text);
    });

    const allowNumericals = isMath || includeNumericals;

    const buildBatchInstruction = (total: number) => {
      return `========================================
OUTPUT FORMAT (DIRECT SINGLE-SHOT COMPLETE SUITE):
========================================
TOTAL QUESTIONS TO GENERATE: EXACTLY ${total} questions across ${promptTopics.length} topic(s).
Output ALL ${total} questions directly in a SINGLE, COMPLETE, VALID JSON array [...] adhering strictly to the schema below.
⚠️ CRITICAL: DO NOT split across multiple turns or prompt the user to "Type NEXT". Generate all ${total} questions completely in this single response.`;
    };

    const buildNegativeConstraints = () => {
      return `========================================
CRITICAL NEGATIVE CONSTRAINTS (ZERO-TOLERANCE RULES):
========================================
1. ZERO PHANTOM FIGURES / DIAGRAMS: Strictly DO NOT generate questions referencing diagrams, figures, graphs, or tables (e.g. "as shown in the figure", "refer to diagram", "in the figure above", "from the table below", "fig 1.1"). Every question must be 100% self-contained in text unless an image is explicitly provided.
2. ZERO DUMMY OR LAZY OPTIONS: Every distractor option must be a plausible, realistic scientific/mathematical choice. NEVER output "None of these", "All of the above", "Both A and B", "Option A", or placeholder text.
3. STRICT MATH ESCAPING: Wrap all math expressions in \\( ... \\) with double-escaped backslashes. Wrap chemical formulas in \\ce{...}.
4. RANDOMIZE CORRECT ANSWER KEYS: Distribute correct answers evenly across index 0, 1, 2, 3 (A, B, C, D). Do NOT always place the correct answer as Option A.
5. ZERO OUT-OF-GRADE / ZERO INVENTED STOICHIOMETRY: Strictly DO NOT invent complex organic molar mass conversions, college-level stoichiometry, or artificial calculations for Class ${selectedClass}. Keep all questions strictly within the prescribed ${selectedBoard} Class ${selectedClass} curriculum.`;
    };

    if (type === 'objective') {
      const easyC = Math.round((isFoundation ? 0.10 : 0.30) * totalQs);
      const medC = Math.round((isFoundation ? 0.40 : 0.50) * totalQs);
      const hardC = Math.max(0, totalQs - easyC - medC);

      // Canonical Question Types across all levels:
      const canonicalTypeGuide = allowNumericals ? `
========================================
5 CANONICAL OBJECTIVE QUESTION FORMATS (Used Across All Levels):
========================================
1. Single Choice MCQ ("single_mcq" / OSC): 4 options, exactly 1 correct answer.
   Example: { "contextId":"CTX-001", "type":"single_mcq", "vault":"practice", "text":"Question text...", "options":["Option A","Option B","Option C","Option D"], "correctAnswer":"Option B", "solution":"Step-by-step reasoning...", "difficulty":"easy", "bloomLevel":"Remember", "conceptTag":"..." }

2. Multiple Choice MCQ ("multiple_mcq" / OMC): 4 options, 2 or more correct answers.
   Example: { "contextId":"CTX-001", "type":"multiple_mcq", "vault":"exam", "text":"Which of the following are properties of...?", "options":["Option A","Option B","Option C","Option D"], "correctAnswers":["Option A","Option C"], "solution":"Detailed explanation...", "difficulty":"hard", "bloomLevel":"Analyze", "conceptTag":"..." }

3. True / False ("true_false" / OTF): Evaluates conceptual facts or rules.
   Example: { "contextId":"CTX-001", "type":"true_false", "vault":"practice", "text":"Statement to evaluate...", "options":["True","False"], "correctAnswer":"True", "solution":"Why it is true/false...", "difficulty":"easy", "bloomLevel":"Remember", "conceptTag":"..." }

4. Assertion & Reason ("assertion_reason" / OAR): Evaluates logical cause-and-effect.
   Example: { "contextId":"CTX-001", "type":"assertion_reason", "vault":"practice", "text":"Assertion (A): ...\\nReason (R): ...", "correctAnswer":"A", "solution":"Explain why both are true and R explains A...", "difficulty":"medium", "bloomLevel":"Analyze", "conceptTag":"..." }
   * Canonical Answer Rules for OAR: "A" = Both true & R explains A | "B" = Both true & R does NOT explain A | "C" = A true & R false | "D" = A false & R true. Do NOT include options array for assertion_reason.

5. Numerical Objective ("numerical" / ONE): Single Choice Numerical MCQ with 4 distinct numerical options and exactly 1 correct answer.
   Example: { "contextId":"CTX-001", "type":"numerical", "vault":"practice", "text":"Calculate the value of... in standard units:", "options":["12.5","24.5","36.5","48.5"], "correctAnswer":"24.5", "solution":"Step 1: Formula ... Step 2: Calculation = 24.5", "difficulty":"medium", "bloomLevel":"Apply", "conceptTag":"..." }
   * Note: Numerical Objective (ONE) questions must ALWAYS have exactly 4 numerical options and 1 correct answer so students select a single choice option without typing.
` : `
========================================
4 CANONICAL OBJECTIVE QUESTION FORMATS (THEORY & CONCEPTUAL ONLY):
========================================
1. Single Choice MCQ ("single_mcq" / OSC): 4 options, exactly 1 correct answer.
   Example: { "contextId":"CTX-001", "type":"single_mcq", "vault":"practice", "text":"Question text...", "options":["Option A","Option B","Option C","Option D"], "correctAnswer":"Option B", "solution":"Step-by-step reasoning...", "difficulty":"easy", "bloomLevel":"Remember", "conceptTag":"..." }

2. Multiple Choice MCQ ("multiple_mcq" / OMC): 4 options, 2 or more correct answers.
   Example: { "contextId":"CTX-001", "type":"multiple_mcq", "vault":"exam", "text":"Which of the following are properties of...?", "options":["Option A","Option B","Option C","Option D"], "correctAnswers":["Option A","Option C"], "solution":"Detailed explanation...", "difficulty":"hard", "bloomLevel":"Analyze", "conceptTag":"..." }

3. True / False ("true_false" / OTF): Evaluates conceptual facts or rules.
   Example: { "contextId":"CTX-001", "type":"true_false", "vault":"practice", "text":"Statement to evaluate...", "options":["True","False"], "correctAnswer":"True", "solution":"Why it is true/false...", "difficulty":"easy", "bloomLevel":"Remember", "conceptTag":"..." }

4. Assertion & Reason ("assertion_reason" / OAR): Evaluates logical cause-and-effect.
   Example: { "contextId":"CTX-001", "type":"assertion_reason", "vault":"practice", "text":"Assertion (A): ...\\nReason (R): ...", "correctAnswer":"A", "solution":"Explain why both are true and R explains A...", "difficulty":"medium", "bloomLevel":"Analyze", "conceptTag":"..." }
   * Canonical Answer Rules for OAR: "A" = Both true & R explains A | "B" = Both true & R does NOT explain A | "C" = A true & R false | "D" = A false & R true. Do NOT include options array for assertion_reason.
`;

      const getVaultBreakdown = (count: number) => {
        if (count === 50) {
          return { practice: 30, exam: 20 };
        } else if (count === 80) {
          return { practice: 50, exam: 30 };
        } else if (count === 90) {
          return { practice: 55, exam: 35 };
        } else {
          const practice = Math.round(count * 0.6);
          const exam = Math.max(0, count - practice);
          return { practice, exam };
        }
      };

      const { practice: totalPracticeQs, exam: totalExamQs } = getVaultBreakdown(totalQs);

      const vaultPartitionGuide = allowNumericals ? `
========================================
UNIVERSAL 2-VAULT PARTITION REQUIREMENT:
========================================
For each topic (${totalQs} Questions Total), generate and tag questions strictly into the 2 Storage Vaults:
1. 🟢 PRACTICE VAULT ("vault": "practice") — EXACTLY ${totalPracticeQs} QUESTIONS:
   - Dedicated for student self-paced practice, diagnostic recovery, and spaced repetition (SRS).
   - Distribution: Foundation & Recall (~30%) + Conceptual Reasoning (~40%) + Numerical & Application (~30%).
   - Mix: OSC, OMC, OTF, OAR, ONE.

2. 🔵 EXAM VAULT ("vault": "exam") — EXACTLY ${totalExamQs} QUESTIONS:
   - Reserved exclusively for teacher classroom tests, chapter tests, and scheduled term exams (must be fresh and unseen by students).
   - Distribution: Core Recall (~25%) + Conceptual Reasoning (~40%) + Numerical & Higher Application (~35%).
   - Mix: OSC, OMC, OTF, OAR, ONE.
` : `
========================================
UNIVERSAL 2-VAULT PARTITION REQUIREMENT (THEORY ONLY - ZERO NUMERICALS):
========================================
For each topic (${totalQs} Questions Total), generate and tag questions strictly into the 2 Storage Vaults:
1. 🟢 PRACTICE VAULT ("vault": "practice") — EXACTLY ${totalPracticeQs} QUESTIONS:
   - Dedicated for student self-paced practice, diagnostic recovery, and spaced repetition (SRS).
   - Distribution: Foundation & Recall (~35%) + Conceptual Reasoning (~40%) + Application & Mechanisms (~25%).
   - Mix: OSC, OMC, OTF, OAR. (NO ONE / NO NUMERICALS).

2. 🔵 EXAM VAULT ("vault": "exam") — EXACTLY ${totalExamQs} QUESTIONS:
   - Reserved exclusively for teacher classroom tests, chapter tests, and scheduled term exams (must be fresh and unseen by students).
   - Distribution: Core Recall (~30%) + Conceptual Reasoning (~40%) + Applied Scenarios (~30%).
   - Mix: OSC, OMC, OTF, OAR. (NO ONE / NO NUMERICALS).
`;

      (window as any).lastPromptMeta = { mode: 'objective', totalQs };

      let topicDistributionSummary = '\n\n========================================\nPER-TOPIC QUESTION ALLOCATION QUOTAS:\n========================================';
      promptTopics.forEach(tp => {
        const k = topicKey(tp);
        const cnt = topicCounts[k] || 80;
        const { practice, exam } = getVaultBreakdown(cnt);
        topicDistributionSummary += `\n- ${tp.subject ? '[' + tp.subject + '] ' : ''}${tp.topic}: EXACTLY ${cnt} questions (${practice} Practice/SRS + ${exam} Exam)`;
      });

      const roleBlock = `========================================
ROLE AND PEDAGOGICAL OBJECTIVE
========================================
Act as an expert Master Educator and Curriculum Specialist under the ${selectedBoard} Class ${selectedClass} curriculum.

Generate a complete, scientifically balanced Question Suite of EXACTLY ${totalQs} OBJECTIVE questions matching the per-topic quotas specified below.
${requirementsSection}`;

      return `${roleBlock}
========================================
QUESTION BANK DETAILS:
========================================
- Board: ${selectedBoard}
- Class: ${selectedClass}
- Track: ${isFoundation ? 'Foundation / Olympiad (HOTS)' : 'Standard Curriculum'}
- Subject Mode: ${allowNumericals ? 'Numericals & Calculations Enabled' : 'Theory & Conceptual Only (Zero Numericals)'}
- Total Questions: EXACTLY ${totalQs} (in ONE single complete JSON array)

${buildBatchInstruction(totalQs)}

${vaultPartitionGuide}

${canonicalTypeGuide}
${topicDistributionSummary}

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
CRITICAL RULES & LEVEL/SOURCE FIDELITY:
========================================
1. STRICT BOARD & CLASS LEVEL ALIGNMENT: Align difficulty, vocabulary, and concepts with official ${selectedBoard} Class ${selectedClass} textbooks (NCERT / State Board).
2. ZERO PLACEHOLDER & ZERO SYNTHETIC LOOPS POLICY:
   - NEVER generate dummy/placeholder options like "Option A", "None of these", or "All of the above". Every option MUST be an authentic, plausible scientific/mathematical choice.
   - NEVER generate repetitive template clones differing only by 1-2 filler words. Every question must test a distinct sub-concept, scenario, or variation.
3. RANDOMIZE CORRECT ANSWER KEY POSITIONS (ANTI-OPTION-A BIAS):
   - Distribute the correct answer position randomly and evenly across options A, B, C, and D (roughly 25% for each position). NEVER place the correct answer as Option A in majority of questions.
4. "correctAnswer" for single_mcq and true_false MUST be an exact verbatim string matching one of the items in "options".
5. For multiple_mcq: "correctAnswers" MUST be an array of exact matching strings copied from "options".
6. "correctAnswer" for assertion_reason MUST be exactly one of "A", "B", "C", or "D".
7. For numerical: "correctAnswer" MUST be a clean numeric string (e.g. "24.5", "10", "3:1"). Specify required unit in question text.
8. ${allowNumericals ? `STRICT GRADE-LEVEL & SYLLABUS REALISM (Class ${selectedClass}):
   - All numerical questions (ONE) MUST strictly match the formulas, concepts, and mathematical scope taught in prescribed ${selectedBoard} Class ${selectedClass} textbooks (NCERT / State Board).
   - ZERO HIGHER-GRADE OR UNIVERSITY HALLUCINATIONS: Strictly forbid introducing complex organic stoichiometry (e.g. lactose molar mass 342 g/mol, fermentation conversion to lactic acid, advanced molarity conversions), multi-step chemical kinetics, or university-level formulas not taught in the Class ${selectedClass} textbook.
   - NEVER invent artificial numerical calculations or fake arithmetic problems on purely qualitative concepts (e.g. cell biology, taxonomy, tissue functions, bacterial fermentation). Only generate numericals where authentic, textbook-standard numerical problems exist for this specific topic and grade.` : `NUMERICAL QUESTIONS STRICTLY FORBIDDEN / ZERO FAKE ARITHMETIC:
   - Numericals (ONE) are DISABLED for this topic. Strictly DO NOT generate any "numerical" (ONE) or arithmetic calculation questions.
   - Strictly DO NOT invent or fabricate artificial stoichiometry, chemical molar mass calculations (e.g. lactose molar mass 342 g/mol, lactic acid moles, organic reaction stoichiometry), fake speeds, or synthetic physics equations for qualitative/biological concepts (fermentation, lactobacilli, cell structure, tissues, classification, ecological relations).
   - All questions MUST be purely conceptual, mechanistic, experimental, or factual questions using OSC, OMC, OTF, and OAR only.`}
9. MANDATORY ATTRIBUTES: Each question object MUST include:
   - "vault": "practice" | "exam" | "mock"
   - "bloomLevel": "Remember" | "Understand" | "Apply" | "Analyze" | "Evaluate" | "Create"
   - "difficulty": "easy" | "medium" | "hard"
   - "examCategory": "${isFoundation ? 'foundation' : 'standard'}"
   - "conceptTag": "concise subtopic or concept name"
10. Strict KaTeX Math Formatting: Use \\( ... \\) for inline math and \\[ ... \\] for display math. Double-escape all backslashes (\\\\frac, \\\\pi, \\\\theta). Wrap chemical formulas in \\ce{...}.

CRITICAL JSON ESCAPING RULES:
1. Return ONLY the raw valid JSON array [...]. No explanations, markdown preamble, or extra text.
2. Ensure valid JSON escaping for all quotes (\\\") and double backslashes.

${buildNegativeConstraints()}`;
    } else {
      let topicDistributionSummary = '\n\n========================================\nPER-TOPIC QUESTION ALLOCATION QUOTAS:\n========================================';
      promptTopics.forEach(tp => {
        const k = topicKey(tp);
        const cnt = topicCounts[k] || 10;
        topicDistributionSummary += `\n- ${tp.subject ? '[' + tp.subject + '] ' : ''}${tp.topic}: EXACTLY ${cnt} questions`;
      });

      const isCBSE = /^cbse/i.test(selectedBoard);
      const isMH = /^(mh|maharashtra)/i.test(selectedBoard);

      const boardFullName = isCBSE 
        ? 'Central Board of Secondary Education (CBSE / NCERT)' 
        : (isMH ? 'Maharashtra State Board of Secondary and Higher Secondary Education (MSBSHSE / Balbharti)' : `${selectedBoard} Board`);

      const officialTextbook = isCBSE
        ? `Prescribed NCERT Textbook & NCERT Exemplar for CBSE Class ${selectedClass}`
        : (isMH ? `Official Balbharti State Board Textbook & State Question Bank for Class ${selectedClass}` : `Official ${selectedBoard} Class ${selectedClass} Textbook`);

      const pyqGuideline = isCBSE
        ? `Strictly past CBSE Board Exams (e.g., "CBSE Board 2023", "CBSE All India 2020", "CBSE Compartment 2019", "CBSE Sample Paper 2024"). DO NOT include State Board or Maharashtra Board questions.`
        : (isMH ? `Strictly past Maharashtra State Board Exams (e.g., "MSBSHSE March 2022", "MSBSHSE July 2020", "MSBSHSE March 2019", "State Board Question Bank"). DO NOT include CBSE or NCERT questions.` : `Past Board Examination Questions for ${selectedBoard}.`);

      const exclusionRule = isCBSE
        ? `STRICT EXCLUSION: Do NOT generate questions from Maharashtra State Board (Balbharti), ICSE, or other state boards.`
        : (isMH ? `STRICT EXCLUSION: Do NOT generate questions from CBSE (NCERT), ICSE, or other national boards.` : '');

      const samplePyq = isCBSE ? 'CBSE Board 2022' : (isMH ? 'MSBSHSE March 2020' : `${selectedBoard} Board 2021`);
      const sampleSource = isCBSE ? 'NCERT Exercise Q3' : (isMH ? 'Balbharti Exercise Q2(a)' : 'Textbook Exercise Q1');

      const defCount = Math.max(1, Math.round(totalQs * 0.25));
      const shortCount = Math.max(2, Math.round(totalQs * 0.50));
      const longCount = Math.max(1, totalQs - defCount - shortCount);

      const questionBreakdownInstruction = isMath ? `
========================================
MATHEMATICS SUBJECTIVE REQUIREMENTS (${totalQs} Questions Total):
========================================
Generate EXACTLY ${totalQs} authentic subjective mathematics questions strictly sourced from ${boardFullName}:
- 1-Mark short questions/formulas (type: "subjective_define", marks: 1, ${defCount} questions: direct formulas, statements of theorems, or definitions).
- 2-Mark short specific / reasoned problems (type: "numerical_short" or "subjective_short", marks: 2, ${shortCount} questions: 2-4 step calculations or proofs).
- 4-Mark long analytical / derivation problems (type: "numerical_long" or "subjective_long", marks: 4, ${longCount} questions: multi-step comprehensive problems, geometric proofs, or word problems).
- 100% AUTHENTIC TEXTBOOK PROBLEMS: Every question MUST be drawn directly from official ${officialTextbook} (${isMH ? 'Practice Sets, Problem Sets, and Solved Examples' : 'Exercises, In-text problems, and Solved Examples'}).
- Reference tagging: Specify the exact source in "sourceSection" (e.g., "${isMH ? 'Practice Set 2.1: Q3' : 'Exercise 3.2: Q4'}").
` : `
========================================
SCIENCE & GENERAL SUBJECTIVE REQUIREMENTS (${totalQs} Questions Total):
========================================
Generate EXACTLY ${totalQs} authentic subjective questions strictly sourced from ${boardFullName}:
- 1-Mark Definition / Laws / Principles (type: "subjective_define" or "subjective_laws", marks: 1, ${defCount} questions).
- 2-Mark Short Answers / Scientific Reasons / Distinguish Between / Short Notes (type: "subjective_short" or "subjective_reason" or "subjective_notes", marks: 2, ${shortCount} questions).
- 4-Mark Long Answers / Detailed Mechanisms / Experimental Setups / Derivations (type: "subjective_long", marks: 4, ${longCount} questions).
${allowNumericals ? `- For calculative physics/chemistry topics, include authentic textbook numericals ("numerical_short" 2M / "numerical_long" 4M) strictly matching ${officialTextbook}.` : '- ZERO INVENTED NUMERICALS: For qualitative/theoretical topics, strictly DO NOT generate any numerical problems. Focus exclusively on authentic conceptual questions.'}
`;

      (window as any).lastPromptMeta = { mode: 'subjective', totalQs };

      return `========================================
ROLE AND TARGET BOARD SPECIFICATION:
========================================
You are an official Senior Paper Setter and Curriculum Author for the ${boardFullName}.

Your mission is to generate EXACTLY ${totalQs} authentic, textbook-verbatim subjective questions exclusively for:
- Target Board: ${selectedBoard} (${boardFullName})
- Target Class: ${selectedClass}
- Subject: ${subj}
- Target Scope: 5 to 10 focused high-yield questions (${totalQs} Qs specified)
- Source Authority: ${officialTextbook}
${exclusionRule ? `- ${exclusionRule}` : ''}
${topicDistributionSummary}
${requirementsSection}
${questionBreakdownInstruction}

========================================
QUESTION GENERATION CONTEXT & TOPIC QUOTAS:
========================================
${ctx}

========================================
CRITICAL BOARD FIDELITY & ZERO-INVENTION RULES:
========================================
1. 100% BOARD-SPECIFIC EXCLUSIVITY:
   - All questions, terminology, notations, and expected model answers MUST strictly belong to ${selectedBoard}.
   - ${pyqGuideline}
   - NEVER mix or blend questions from other boards.

2. ABSOLUTELY ZERO INVENTED / SYNTHETIC QUESTIONS:
   - Every single question generated MUST be an authentic, real question sourced directly from official ${officialTextbook} (Chapter-End Exercises, In-Text questions ${isMH ? 'like "Can you tell?", "Use your brain power", "Think about it"' : ''}) or actual past ${selectedBoard} Board Exam papers.
   - Strictly DO NOT make up fictional hypothetical scenarios, imaginary stories, or artificial questions to fill counts.

3. ANSWERS VERBATIM & KEYWORD HIGHLIGHTING:
   - Answers MUST be 100% verbatim from standard prescribed ${officialTextbook}. Absolutely NO paraphrasing.
   - Embed key technical phrases inside HTML <mark>keyword</mark> tags directly within the model answer text string (e.g. "The <mark>acceleration due to gravity</mark> is...").
   - Separate each logical answer point on a new numbered line (1., 2., 3...) inside the "solution" string.

4. ACCURATE METADATA TAGGING:
   - Add "pyqInfo" with authentic board year (e.g., "${samplePyq}").
   - Add "sourceSection" indicating exact location (e.g., "${sampleSource}").

5. FORMULAS & KaTeX FORMATTING:
   - Use \\( ... \\) for inline math expressions with double-escaped backslashes (\\\\frac, \\\\times).
   - Wrap chemical formulas in \\ce{...} or standard notation.

${buildImageInstruction()}

========================================
CRITICAL JSON ESCAPING RULES:
========================================
1. Return ONLY the raw valid JSON array [...]. No explanations, markdown preamble, or extra text.
2. Double-escape backslashes in LaTeX (\\\\frac, \\\\pi, \\\\theta).
3. Do NOT use raw control characters inside string values.

========================================
OUTPUT FORMAT: Return ONLY a valid JSON array of objects with schema:
========================================
[
  {
    "contextId": "CTX-001",
    "topicName": "Topic name from the context list",
    "type": "${allowNumericals ? 'subjective_define / subjective_laws / subjective_short / subjective_reason / subjective_notes / subjective_long / numerical_short / numerical_long' : 'subjective_define / subjective_laws / subjective_short / subjective_reason / subjective_notes / subjective_long'}",
    "marks": 1,
    "vault": "${vault}",
    "conceptTag": "Specific concept or subtopic name",
    "sourceSection": "${sampleSource}",
    "text": "Exact authentic question text...",
    "solution": "1. Verbatim point one with <mark>key term</mark>\\n2. Verbatim point two...",
    "keywords": ["key term 1", "key term 2"],
    "pyqInfo": "${samplePyq}"
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
        const matched = cleanOptions.find(opt => isOptionMatch(opt, cleanedAns) || isOptionMatch(opt, rawAns));
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
        const matched = cleanOptions.find(opt => isOptionMatch(opt, cleaned) || isOptionMatch(opt, str));
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
      vault: q.vault || vault,
      conceptTag: q.conceptTag || finalTopicName,
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
      vault: q.vault || vault,
      conceptTag: q.conceptTag || finalTopicName,
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
      const formattedQuestions = questionsList.map(q => {
        const bCode = boardCodes?.[selectedBoard] || (selectedBoard?.toUpperCase().includes('CBSE') ? 'CBSE' : 'MH');
        const sName = q.subject || getSelectedSubjectsList()[0] || '';
        const sCode = subjectCodes?.[sName] || 'MTH';
        const chNum = String(q.chapterNumber || '1');
        const tNum = String(q.topicNumber || '1.1');
        const canonicalTopicCode = `${bCode}-${selectedClass}-${sCode}-${chNum}-${tNum}`;

        return {
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
          boardCode: bCode,
          classNum: selectedClass,
          subjectName: sName,
          subjectCode: sCode,
          chapterNumber: chNum,
          topicNumber: tNum,
          topicCode: q.topicCode || canonicalTopicCode,
          topic: q.topic || q.topicName || '',
          topicName: q.topicName || q.topic || '',
          keywords: q.keywords || [],
          textbookPracticeSet: q.textbookPracticeSet || '',
          marks: Number(q.marks) || 0,
          vault: q.vault || vault,
          conceptTag: q.conceptTag || q.topicName || q.topic || ''
        };
      });

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
  const handleParseJSON = (isAppend = false) => {
    const text = aiPasteText.trim();
    if (!text) {
      triggerAlert('Input Required', 'Please paste the AI JSON response array first.');
      return;
    }

    try {
      const parsed = robustParseAIJson(text);
      let transformed: any[] = [];
      const offset = isAppend ? generatedQuestions.length : 0;

      if (questionType === 'objective') {
        const arr = Array.isArray(parsed) ? parsed : (parsed.questions || []);
        if (!arr.length) throw new Error('No questions list found in JSON.');
        transformed = arr.map((q: any, i: number) => transformObjectiveQuestion(q, offset + i));
      } else {
        const arr = parsed.questions || (Array.isArray(parsed) ? parsed : [parsed]);
        if (!arr.length) throw new Error('No questions list found in JSON.');
        transformed = arr.map((q: any) => transformSubjectiveQuestion(q));
      }

      if (isAppend) {
        const combined = [...generatedQuestions, ...transformed];
        setGeneratedQuestions(combined);
        setAiPasteText('');
        const validation = validateQuestionsForSave(combined);
        if (!validation.valid) {
          triggerAlert('Questions Appended with Warnings', `✅ Appended ${transformed.length} questions (Total: ${combined.length}), but ${validation.errors.length} issue(s) need attention.`);
        } else {
          triggerAlert('Questions Appended', `✅ Successfully appended ${transformed.length} questions! Total preview pool: ${combined.length} questions.`);
        }
      } else {
        setGeneratedQuestions(transformed);
        const validation = validateQuestionsForSave(transformed);
        if (!validation.valid) {
          triggerAlert('Success with Warnings', `✅ Successfully parsed ${transformed.length} questions, but ${validation.errors.length} issue(s) need attention. Review or fix/delete them below before saving.`);
        }
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
      triggerConfirm(
        'Validation Issues Detected',
        `⚠️ ${validation.errors.length} issue(s) were found in the parsed questions:\n\n${validation.errors.slice(0, 5).join('\n')}\n\nDo you want to proceed and save them anyway?`,
        () => executeBulkSave(generatedQuestions)
      );
      return;
    }

    // No issues found: save immediately without unnecessary confirmation prompt
    executeBulkSave(generatedQuestions);
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

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* CDN Script Injections for KaTeX */}




      {/* Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800, cursor: 'pointer' }} onClick={() => router.push('/admin')}>YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Create Question Bank</h1>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          
          <button className="btn btn-secondary" onClick={() => router.push('/admin/question-bank')}>Manage QB</button>
        </div>
      </header>

      {/* Main Workspace */}
      <main style={{ flex: 1, padding: '12px 10px', maxWidth: '1080px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '10px' }}>
        
        {/* Card 1: Syllabus Mapping Cascading Selects */}
        <div className="card" style={{ background: 'var(--surface)', padding: '12px 14px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
          <h3 style={{ fontSize: '13px', fontWeight: 800, margin: '0 0 8px', textTransform: 'uppercase', color: 'var(--text)' }}>Syllabus Mapping</h3>
          
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '8px', marginBottom: '10px' }}>
            {/* Board */}
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '3px' }}>Board</label>
              <select 
                className="form-input" 
                value={selectedBoard} 
                onChange={(e) => handleBoardChange(e.target.value, () => { setTopicWeightageMap({}); clearImage(); })}
                style={{ width: '100%', padding: '6px 8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                <option value="">— Select Board —</option>
                {boards.map(b => (
                  <option key={b} value={b}>{boardCodes[b] || b.toUpperCase()}</option>
                ))}
              </select>
            </div>

            {/* Class */}
            <div>
              <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '3px' }}>Class</label>
              <select 
                className="form-input" 
                value={selectedClass} 
                onChange={(e) => handleClassChange(e.target.value, () => { setTopicWeightageMap({}); clearImage(); })} 
                disabled={!selectedBoard}
                style={{ width: '100%', padding: '6px 8px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
              >
                <option value="">— Select Class —</option>
                {classes.map(c => (
                  <option key={c} value={c}>Class {c}</option>
                ))}
              </select>
            </div>

          </div>
          
          {/* Subjects checkboxes & Single Topic Selector */}
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
            onToggleTopic={(topic) => {
              setSelectedTopics([topic]);
              const count = topic.targetQuestions || (defaultPerTopicCount ? Number(defaultPerTopicCount) : 80);
              setDefaultPerTopicCount(count);
              setTopicCustomCounts({ [topicKey(topic)]: count });
            }}
            onSelectAllTopics={() => {}}
            onDeselectAllTopics={() => setSelectedTopics([])}
            singleTopicSelect={true}
          />

          {/* Single Topic Target Question Quota */}
          {selectedTopics.length > 0 && (
            <div style={{ marginTop: '12px', borderTop: '1px solid var(--border-light)', paddingTop: '10px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px', flexWrap: 'wrap', gap: '6px' }}>
                <h3 style={{ fontSize: '12.5px', fontWeight: 800, margin: 0, color: 'var(--text)' }}>Target Question Quota</h3>
                <span style={{ fontSize: '11.5px', fontWeight: 700, background: 'var(--info-bg)', color: 'var(--info)', padding: '2px 8px', borderRadius: '12px' }}>
                  Target: <strong>{getTotalTargetQuestions()} Questions</strong>
                </span>
              </div>

              {/* Topic Scope Presets */}
              <div style={{ background: 'var(--bg-soft)', padding: '8px 12px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', marginBottom: '10px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '8px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span style={{ fontSize: '10.5px', fontWeight: 800, textTransform: 'uppercase', color: 'var(--text-muted)' }}>
                    {questionType === 'subjective' ? 'Subjective Presets:' : 'Objective Presets:'}
                  </span>
                </div>
                <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                  {questionType === 'subjective' ? (
                    <>
                      <button
                        type="button"
                        className={`btn btn-sm ${Number(defaultPerTopicCount) === 5 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => {
                          setDefaultPerTopicCount(5);
                          if (selectedTopics[0]) {
                            setTopicCustomCounts({ [topicKey(selectedTopics[0])]: 5 });
                          }
                        }}
                        style={{ fontSize: '11px', padding: '4px 10px', borderRadius: '12px' }}
                        title="Core in-text & basic definitions: 5 Questions"
                      >
                        🎯 Core (5 Qs)
                      </button>
                      <button
                        type="button"
                        className={`btn btn-sm ${Number(defaultPerTopicCount) === 8 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => {
                          setDefaultPerTopicCount(8);
                          if (selectedTopics[0]) {
                            setTopicCustomCounts({ [topicKey(selectedTopics[0])]: 8 });
                          }
                        }}
                        style={{ fontSize: '11px', padding: '4px 10px', borderRadius: '12px' }}
                        title="Standard Subjective Suite: 8 Questions"
                      >
                        ⚡ Standard (8 Qs)
                      </button>
                      <button
                        type="button"
                        className={`btn btn-sm ${Number(defaultPerTopicCount) === 10 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => {
                          setDefaultPerTopicCount(10);
                          if (selectedTopics[0]) {
                            setTopicCustomCounts({ [topicKey(selectedTopics[0])]: 10 });
                          }
                        }}
                        style={{ fontSize: '11px', padding: '4px 10px', borderRadius: '12px' }}
                        title="Comprehensive Chapter Exercise & PYQs: 10 Questions"
                      >
                        📚 Comprehensive (10 Qs)
                      </button>
                      <button
                        type="button"
                        className={`btn btn-sm ${Number(defaultPerTopicCount) === 15 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => {
                          setDefaultPerTopicCount(15);
                          if (selectedTopics[0]) {
                            setTopicCustomCounts({ [topicKey(selectedTopics[0])]: 15 });
                          }
                        }}
                        style={{ fontSize: '11px', padding: '4px 10px', borderRadius: '12px' }}
                        title="Full Topic Suite with Numericals & PYQs: 15 Questions"
                      >
                        🏆 Full Suite (15 Qs)
                      </button>
                    </>
                  ) : (
                    <>
                      <button
                        type="button"
                        className={`btn btn-sm ${Number(defaultPerTopicCount) === 50 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => {
                          setDefaultPerTopicCount(50);
                          if (selectedTopics[0]) {
                            setTopicCustomCounts({ [topicKey(selectedTopics[0])]: 50 });
                          }
                        }}
                        style={{ fontSize: '11px', padding: '4px 12px', borderRadius: '12px' }}
                        title="Minor topic: 50 Questions (30 Practice/SRS + 20 Exam)"
                      >
                        Minor Topic (50 Qs)
                      </button>
                      <button
                        type="button"
                        className={`btn btn-sm ${Number(defaultPerTopicCount) === 80 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => {
                          setDefaultPerTopicCount(80);
                          if (selectedTopics[0]) {
                            setTopicCustomCounts({ [topicKey(selectedTopics[0])]: 80 });
                          }
                        }}
                        style={{ fontSize: '11px', padding: '4px 12px', borderRadius: '12px' }}
                        title="Medium topic: 80 Questions (50 Practice/SRS + 30 Exam)"
                      >
                        Medium Topic (80 Qs)
                      </button>
                      <button
                        type="button"
                        className={`btn btn-sm ${Number(defaultPerTopicCount) === 90 ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => {
                          setDefaultPerTopicCount(90);
                          if (selectedTopics[0]) {
                            setTopicCustomCounts({ [topicKey(selectedTopics[0])]: 90 });
                          }
                        }}
                        style={{ fontSize: '11px', padding: '4px 12px', borderRadius: '12px' }}
                        title="Major topic: 90 Questions (55 Practice/SRS + 35 Exam)"
                      >
                        Major Topic (90 Qs)
                      </button>
                    </>
                  )}
                </div>
              </div>

              {/* Selected Topic Details & Count Input */}
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: 'var(--bg-soft)', padding: '12px 16px', borderRadius: 'var(--radius-sm)', flexWrap: 'wrap', gap: '10px' }}>
                <div>
                  <div style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text)' }}>
                    {selectedTopics[0]?.topic}
                  </div>
                  <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                    {selectedTopics[0]?.chapterName} • {selectedTopics[0]?.subject}
                  </div>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <label style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)' }}>Questions to Generate:</label>
                  <input
                    type="number"
                    min={5}
                    max={100}
                    value={defaultPerTopicCount}
                    onChange={(e) => {
                      const raw = e.target.value;
                      if (raw === '') {
                        setDefaultPerTopicCount('');
                      } else {
                        const val = parseInt(raw, 10);
                        const v = isNaN(val) ? '' : Math.max(1, val);
                        setDefaultPerTopicCount(v);
                        if (selectedTopics[0]) {
                          setTopicCustomCounts({ [topicKey(selectedTopics[0])]: v });
                        }
                      }
                    }}
                    onBlur={() => {
                      if (defaultPerTopicCount === '' || Number(defaultPerTopicCount) < 1) {
                        setDefaultPerTopicCount(80);
                        if (selectedTopics[0]) {
                          setTopicCustomCounts({ [topicKey(selectedTopics[0])]: 80 });
                        }
                      }
                    }}
                    style={{ width: '70px', padding: '6px 8px', textAlign: 'center', border: '1px solid var(--border-light)', borderRadius: '4px', background: 'var(--surface)', color: 'var(--text)', fontWeight: 700, fontSize: '13px' }}
                  />
                  <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)' }}>Qs</span>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Card 2: Workspace Settings & Actions */}
        {selectedTopics.length > 0 && (
          <div className="card" style={{ background: 'var(--surface)', padding: '18px 24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
            <h3 style={{ fontSize: '13px', fontWeight: 800, margin: '0 0 12px', textTransform: 'uppercase', color: 'var(--text)' }}>Workspace Settings &amp; Generator Actions</h3>

            {/* Optional Textbook/Diagram Image Upload */}
            <div style={{ marginTop: '10px', borderTop: '1px dashed var(--border-light)', paddingTop: '12px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '10px' }}>
              <label style={{ fontSize: '12px', fontWeight: 'bold', margin: 0 }}>🖼️ Upload Textbook/Diagram Image (optional)</label>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px', alignItems: 'center' }}>
                <input type="file" id="questionImageInput" accept="image/*" onChange={handleImageSelected} style={{ fontSize: '12px' }} />
                {uploadedImageBase64 && (
                  <button className="btn btn-secondary btn-sm" onClick={clearImage}>✕ Clear</button>
                )}
              </div>
            </div>
            {uploadedImageBase64 && (
              <div style={{ marginTop: '10px' }}>
                <img src={uploadedImageBase64} alt="Selected source preview" style={{ maxWidth: '240px', maxHeight: '180px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }} />
              </div>
            )}

            {/* Generator Mode Selector (SSOT) */}
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '10px', marginTop: '16px', borderTop: '1px solid var(--border-light)', paddingTop: '14px' }}>
              <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
                <span style={{ fontSize: '12px', fontWeight: 'bold' }}>Generator Mode:</span>
                <button 
                  type="button"
                  className={`btn btn-sm ${questionType === 'objective' ? 'btn-primary' : 'btn-secondary'}`}
                  onClick={() => handleSwitchType('objective')}
                  style={{ borderRadius: '20px', fontWeight: questionType === 'objective' ? 700 : 500 }}
                >
                  🎯 Objective
                </button>
                <button 
                  type="button"
                  className={`btn btn-sm ${questionType === 'subjective' ? 'btn-primary' : 'btn-secondary'}`}
                  onClick={() => handleSwitchType('subjective')}
                  style={{ borderRadius: '20px', fontWeight: questionType === 'subjective' ? 700 : 500 }}
                >
                  📝 Subjective
                </button>
              </div>
            </div>

            {/* Numericals / Calculation Questions Toggle */}
            <div style={{ marginTop: '12px', padding: '10px 14px', background: includeNumericals ? 'var(--info-bg)' : 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: `1px solid ${includeNumericals ? 'var(--info)' : 'var(--border-light)'}`, display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '10px' }}>
              <label style={{ display: 'flex', alignItems: 'center', gap: '10px', cursor: 'pointer', margin: 0, flex: 1 }}>
                <input
                  type="checkbox"
                  checked={includeNumericals}
                  onChange={(e) => {
                    setIncludeNumericals(e.target.checked);
                    setNumericalsManuallyToggled(true);
                  }}
                  style={{ width: '16px', height: '16px', cursor: 'pointer' }}
                />
                <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text)' }}>
                  Include Numericals &amp; Calculation Problems (ONE / Numerical Types)
                </div>
              </label>
              <span style={{ fontSize: '11px', fontWeight: 700, padding: '3px 10px', borderRadius: '12px', background: includeNumericals ? 'var(--info-bg)' : 'var(--border-light)', color: includeNumericals ? 'var(--info)' : 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                {includeNumericals ? 'Numericals ON' : 'Theory / Qualitative Only'}
              </span>
            </div>

            {/* Subjective verbatim requirements warning */}
            {questionType === 'subjective' && (
              <div style={{ marginTop: '16px', padding: '12px', background: 'var(--warning-bg)', color: 'var(--warning)', borderRadius: 'var(--radius-sm)', borderLeft: '4px solid var(--warning)' }}>
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
                <h3 style={{ fontSize: '13px', fontWeight: 800, margin: 0, textTransform: 'uppercase', color: 'var(--text)' }}>📋 Generated AI Prompt</h3>
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
                <h3 style={{ fontSize: '13px', fontWeight: 800, margin: 0, textTransform: 'uppercase', color: 'var(--text)' }}>📥 Paste AI Response</h3>
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

          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
            {generatedQuestions.length > 0 ? (
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ background: 'var(--info-bg)', color: 'var(--info)', padding: '5px 12px', borderRadius: '14px', fontSize: '11px', fontWeight: 700 }}>
                  📦 {generatedQuestions.length} Questions Loaded in Preview
                </span>
                <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                  (Or paste additional questions and click &quot;Append More Questions&quot;)
                </span>
              </div>
            ) : (
              <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                💡 Tip: Paste the complete JSON array generated by AI and click &quot;Parse &amp; Preview Questions&quot;.
              </div>
            )}

            <div style={{ display: 'flex', gap: '8px', marginLeft: 'auto' }}>
              {generatedQuestions.length > 0 && (
                <button
                  type="button"
                  className="btn btn-success"
                  onClick={() => handleParseJSON(true)}
                  style={{ padding: '9px 18px', fontWeight: 700, fontSize: '12px' }}
                >
                  ➕ Append More Questions
                </button>
              )}
              <button 
                type="button"
                className="btn btn-primary" 
                onClick={() => handleParseJSON(false)} 
                style={{ padding: '9px 22px', fontWeight: 800, fontSize: '12.5px' }}
              >
                ⚙️ Parse &amp; Preview Questions
              </button>
            </div>
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
                        color: previewFilter === 'all' ? 'var(--text-white)' : 'var(--text-muted)',
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
                        background: previewFilter === 'issues' ? 'var(--danger)' : 'transparent',
                        color: previewFilter === 'issues' ? 'var(--text-white)' : (validation.invalidIndices.size > 0 ? 'var(--danger)' : 'var(--text-muted)'),
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
                    <span style={{ fontWeight: 700, color: 'var(--text)' }}>📊 Suite Composition:</span>
                    {objList.length > 0 && (
                      <span style={{ background: 'var(--info-bg)', color: 'var(--info)', padding: '3px 8px', borderRadius: '12px', fontWeight: 600 }}>
                        🎯 <strong>{objList.length} Objective</strong> ({easyC} Easy, {medC} Med, {hardC} Hard)
                      </span>
                    )}
                    {subList.length > 0 && (
                      <span style={{ background: 'var(--success-bg)', color: 'var(--success)', padding: '3px 8px', borderRadius: '12px', fontWeight: 600 }}>
                        📝 <strong>{subList.length} Subjective</strong> ({m1C} × 1M, {m2C} × 2M, {m4C} × 4M)
                      </span>
                    )}
                  </div>
                );
              })()}

              {/* TOP VALIDATION ISSUES ACTION BANNER */}
              {!validation.valid && (
                <div style={{ padding: '12px 16px', borderRadius: 'var(--radius-sm)', background: 'rgba(239, 68, 68, 0.12)', border: '1.5px solid var(--danger)', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <div style={{ fontSize: '12px', fontWeight: 'bold', color: 'var(--danger)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <span>⚠️ {validation.errors.length} validation issue{validation.errors.length > 1 ? 's' : ''} require attention before saving:</span>
                    </div>
                    {previewFilter !== 'issues' && (
                      <button
                        type="button"
                        onClick={() => setPreviewFilter('issues')}
                        style={{ background: 'var(--danger)', color: 'var(--text-white)', border: 'none', borderRadius: '4px', padding: '3px 8px', fontSize: '11px', fontWeight: 600, cursor: 'pointer' }}
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
                              el.style.boxShadow = '0 0 15px rgba(239, 68, 68, 0.6)';
                              setTimeout(() => { el.style.boxShadow = ''; }, 2000);
                            }
                          }, 50);
                        }}
                        style={{
                          background: 'var(--surface)',
                          border: '1px solid var(--danger)',
                          color: 'var(--danger)',
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
                        background: hasErrors ? 'rgba(239, 68, 68, 0.04)' : 'var(--bg-soft)', 
                        padding: '12px', 
                        borderRadius: 'var(--radius-sm)', 
                        borderLeft: hasErrors ? '5px solid var(--danger)' : '4px solid var(--accent)',
                        border: hasErrors ? '1.5px solid rgba(239, 68, 68, 0.4)' : '1px solid var(--border-light)',
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
                          <div style={{ padding: '6px 10px', background: 'rgba(239, 68, 68, 0.15)', border: '1px solid var(--danger)', borderRadius: '4px', color: 'var(--danger)', fontSize: '11px', fontWeight: 600, marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                            <span>⚠️ Issue:</span>
                            <span>{qErrors.join(' | ')}</span>
                          </div>
                        )}

                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '6px' }}>
                          <span>Type: <strong>{q.type}</strong> | Difficulty: <strong>{q.difficulty}</strong> | Bloom: <strong>{q.bloomLevel || 'Remember'}</strong></span>
                          <span>Ch {q.chapterNumber || '1'} • Topic {q.topicNumber || '1.1'}</span>
                        </div>
                        
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', marginBottom: '8px' }}>
                          <label style={{ fontSize: '10px', fontWeight: 700, color: hasErrors ? 'var(--danger)' : 'var(--text-muted)', textTransform: 'uppercase' }}>
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
                              border: hasErrors ? '1.5px solid var(--danger)' : '1px solid var(--border-light)',
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
                              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginTop: '8px' }}>
                                <div style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                  <span>Options &amp; Correct Answer:</span>
                                  <span style={{ fontWeight: 'normal', textTransform: 'none', fontSize: '10.5px' }}>Click indicator to set correct answer, or edit text directly</span>
                                </div>
                                {q.options.map((opt: string, oi: number) => {
                                  const isCorrect = isOptionMatch(opt, q.correctAnswer) || 
                                    (q.correctAnswers && q.correctAnswers.some((ans: string) => isOptionMatch(opt, ans)));
                                  const optLetter = String.fromCharCode(65 + oi);

                                  return (
                                    <div 
                                      key={oi} 
                                      style={{ 
                                        display: 'flex', 
                                        flexDirection: 'column', 
                                        gap: '4px',
                                        background: isCorrect ? 'rgba(16, 185, 129, 0.08)' : 'var(--surface)',
                                        border: isCorrect ? '1.5px solid var(--success)' : '1px solid var(--border-light)',
                                        borderRadius: '6px',
                                        padding: '6px 10px',
                                        transition: 'all 0.2s'
                                      }}
                                    >
                                      <div style={{ display: 'flex', alignItems: 'center', gap: '10px', width: '100%' }}>
                                        {/* Select Indicator Button */}
                                        <button 
                                          type="button"
                                          onClick={() => {
                                            setGeneratedQuestions(prev => {
                                              const next = [...prev];
                                              const currentQ = { ...next[idx] };
                                              if (currentQ.type === 'multiple_mcq') {
                                                const cAnswers = Array.isArray(currentQ.correctAnswers) ? [...currentQ.correctAnswers] : [];
                                                const exists = cAnswers.some((ans: string) => isOptionMatch(ans, opt));
                                                if (exists) {
                                                  currentQ.correctAnswers = cAnswers.filter((ans: string) => !isOptionMatch(ans, opt));
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
                                            width: '22px',
                                            height: '22px',
                                            borderRadius: q.type === 'multiple_mcq' ? '4px' : '50%',
                                            border: isCorrect ? '2px solid var(--success)' : '2px solid var(--text-muted)',
                                            background: isCorrect ? 'var(--success)' : 'transparent',
                                            display: 'flex',
                                            alignItems: 'center',
                                            justifyContent: 'center',
                                            cursor: 'pointer',
                                            color: 'var(--text-white)',
                                            fontSize: '11px',
                                            fontWeight: 'bold',
                                            flexShrink: 0,
                                            padding: 0
                                          }}
                                          title={q.type === 'multiple_mcq' ? 'Toggle correct option' : 'Set as correct option'}
                                        >
                                          {isCorrect && '✓'}
                                        </button>

                                        {/* Option Letter Label */}
                                        <span style={{ 
                                          fontSize: '11px', 
                                          fontWeight: 800, 
                                          color: isCorrect ? 'var(--success)' : 'var(--text-muted)',
                                          minWidth: '18px',
                                          flexShrink: 0
                                        }}>
                                          {optLetter}.
                                        </span>

                                        {/* Explicitly Editable Option Input */}
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
                                              if (isOptionMatch(currentQ.correctAnswer, oldVal) || currentQ.correctAnswer === oldVal) {
                                                currentQ.correctAnswer = val;
                                              }
                                              if (Array.isArray(currentQ.correctAnswers)) {
                                                currentQ.correctAnswers = currentQ.correctAnswers.map((a: string) => (isOptionMatch(a, oldVal) || a === oldVal) ? val : a);
                                              }
                                              next[idx] = currentQ;
                                              return next;
                                            });
                                          }}
                                          style={{
                                            flex: 1,
                                            border: '1px solid var(--border-light)',
                                            background: 'var(--bg-soft)',
                                            fontSize: '12px',
                                            fontWeight: 600,
                                            color: 'var(--text)',
                                            padding: '6px 10px',
                                            borderRadius: '4px',
                                            outline: 'none'
                                          }}
                                          placeholder={`Option ${optLetter} text...`}
                                        />

                                        {/* Delete Option Button (allowed if > 2 options) */}
                                        {q.options.length > 2 && (
                                          <button
                                            type="button"
                                            onClick={() => {
                                              setGeneratedQuestions(prev => {
                                                const next = [...prev];
                                                const currentQ = { ...next[idx] };
                                                const oldVal = currentQ.options[oi];
                                                const nextOpts = currentQ.options.filter((_: any, i: number) => i !== oi);
                                                currentQ.options = nextOpts;
                                                if (isOptionMatch(currentQ.correctAnswer, oldVal)) {
                                                  currentQ.correctAnswer = nextOpts[0] || '';
                                                }
                                                if (Array.isArray(currentQ.correctAnswers)) {
                                                  currentQ.correctAnswers = currentQ.correctAnswers.filter((a: string) => !isOptionMatch(a, oldVal));
                                                  if (currentQ.correctAnswers.length === 0 && nextOpts.length > 0) {
                                                    currentQ.correctAnswers = [nextOpts[0]];
                                                    currentQ.correctAnswer = nextOpts[0];
                                                  }
                                                }
                                                next[idx] = currentQ;
                                                return next;
                                              });
                                            }}
                                            style={{
                                              background: 'transparent',
                                              border: 'none',
                                              color: 'var(--text-muted)',
                                              cursor: 'pointer',
                                              fontSize: '14px',
                                              padding: '4px 6px',
                                              borderRadius: '4px',
                                              lineHeight: 1
                                            }}
                                            title="Remove this option"
                                            onMouseEnter={(e) => (e.currentTarget.style.color = 'var(--danger)')}
                                            onMouseLeave={(e) => (e.currentTarget.style.color = 'var(--text-muted)')}
                                          >
                                            ✕
                                          </button>
                                        )}
                                      </div>

                                      {/* Live Math Render Preview (Only shown when opt contains math formatting to avoid duplicates) */}
                                      {/\\\(|\\\)|\\\[|\\\]|\$\$|\$|\\ce/g.test(opt) && (
                                        <div className="math-container" style={{ fontSize: '11px', color: 'var(--text-muted)', paddingLeft: '50px', borderTop: '1px dashed var(--border-light)', paddingTop: '3px', marginTop: '2px' }}>
                                          {preprocessMathText(opt)}
                                        </div>
                                      )}
                                    </div>
                                  );
                                })}

                                {/* Add Option Button */}
                                {q.options.length < 6 && (
                                  <button
                                    type="button"
                                    onClick={() => {
                                      setGeneratedQuestions(prev => {
                                        const next = [...prev];
                                        const currentQ = { ...next[idx] };
                                        const opts = [...(currentQ.options || [])];
                                        opts.push(`Option ${String.fromCharCode(65 + opts.length)}`);
                                        currentQ.options = opts;
                                        next[idx] = currentQ;
                                        return next;
                                      });
                                    }}
                                    style={{
                                      alignSelf: 'flex-start',
                                      background: 'var(--surface)',
                                      border: '1px dashed var(--border-light)',
                                      color: 'var(--primary)',
                                      padding: '4px 10px',
                                      borderRadius: '4px',
                                      fontSize: '11px',
                                      fontWeight: 700,
                                      cursor: 'pointer',
                                      display: 'flex',
                                      alignItems: 'center',
                                      gap: '4px'
                                    }}
                                  >
                                    ➕ Add Option {String.fromCharCode(65 + q.options.length)}
                                  </button>
                                )}
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
