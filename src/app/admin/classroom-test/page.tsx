'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import { useMathRender } from '@/hooks/useMathRender';
import { preprocessMathText, robustParseAIJson, validateQuestion } from '@/lib/questionTypes';
import { highlightModelAnswerKeywords } from '@/lib/pdfExport';
import { toISTDateTimeLocalInput, getDateKeyIST } from '@/lib/dateUtils';

interface Batch {
  id: string;
  name: string;
}

interface DayConfig {
  dayName: string;
  date: string; // YYYY-MM-DD
  active: boolean;
  topics: string[];
  isSaturday?: boolean;
}

export default function AdminClassroomTestPage() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [batches, setBatches] = useState<Batch[]>([]);

  // Syllabus configuration indexes loaded from firestore
  const [syllabusSubjects, setSyllabusSubjects] = useState<{ [key: string]: any }>({});
  const [boards, setBoards] = useState<string[]>([]);
  const [classes, setClasses] = useState<string[]>([]);
  const [subjects, setSubjects] = useState<string[]>([]);
  const [chapters, setChapters] = useState<{ subject?: string; number: number; name: string; topics?: any[] }[]>([]);
  const [currentChapterTopics, setCurrentChapterTopics] = useState<string[]>([]);

  // Selections
  const [testType, setTestType] = useState<'weekly_suite' | 'weekly' | 'chapter' | 'multi-chapter'>('weekly_suite');
  const [selectedBoard, setSelectedBoard] = useState('');
  const [selectedClass, setSelectedClass] = useState('');
  const [mathType, setMathType] = useState<'algebra' | 'geometry' | ''>('');
  const [selectedSubjects, setSelectedSubjects] = useState<string[]>([]);
  const [selectedChapters, setSelectedChapters] = useState<string[]>([]);
  const [multiChapters, setMultiChapters] = useState('');
  const [selectedBatch, setSelectedBatch] = useState('');
  const [assignBatchId, setAssignBatchId] = useState('');
  const [assignedStatusMsg, setAssignedStatusMsg] = useState('');
  const [totalQuestions, setTotalQuestions] = useState<number | string>(6);
  const [weekNumber, setWeekNumber] = useState(2);

  // Weekly Suite Scheduler State
  const [weekStartDate, setWeekStartDate] = useState<string>(() => {
    const today = new Date();
    const day = today.getDay();
    let diff = today.getDate() - day;
    if (day === 0) {
      diff = today.getDate() + 1;
    } else if (day === 6) {
      diff = today.getDate() + 2;
    } else {
      diff = today.getDate() - day + 1;
    }
    const mon = new Date(today.getFullYear(), today.getMonth(), diff);
    const yr = mon.getFullYear();
    const mo = String(mon.getMonth() + 1).padStart(2, '0');
    const dy = String(mon.getDate()).padStart(2, '0');
    return `${yr}-${mo}-${dy}`;
  });

  const [daysConfig, setDaysConfig] = useState<DayConfig[]>([]);
  const [suiteMode, setSuiteMode] = useState<'revision'>('revision');

  // In-Place QB AI Generator & Preview State
  const [qbPrompt, setQbPrompt] = useState('');
  const [qbPasteJson, setQbPasteJson] = useState('');
  const [qbStatus, setQbStatus] = useState('');
  const [qbSaving, setQbSaving] = useState(false);
  const [saveStats, setSaveStats] = useState({ current: 0, total: 0 });
  const [previewQuestions, setPreviewQuestions] = useState<any[]>([]);

  // Scheduled Suites Manager Modal State
  const [showManagerModal, setShowManagerModal] = useState(false);
  const [scheduledExamsList, setScheduledExamsList] = useState<any[]>([]);
  const [loadingScheduled, setLoadingScheduled] = useState(false);
  const [isCompletedSectionExpanded, setIsCompletedSectionExpanded] = useState(false);
  const [assignments, setAssignments] = useState<any[]>([]);
  const [saturdayAssignModal, setSaturdayAssignModal] = useState<{
    show: boolean;
    examId: string;
    examName: string;
    batchId: string;
    startAtStr: string;
    endAtStr: string;
    examDuration: number | string;
    assignmentId?: string;
  }>({
    show: false,
    examId: '',
    examName: '',
    batchId: '',
    startAtStr: '',
    endAtStr: '',
    examDuration: 60
  });

  // Result state
  const [generating, setGenerating] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [errorMsg, setErrorMsg] = useState('');

  const getTopicNamesForDisplay = (topics: string[], questions: any[]) => {
    return (topics || []).map((t: string) => {
      if (!/^[A-Z]{2,}-\d+-/i.test(t)) {
        return t;
      }
      const qSource = questions || [];
      const foundQ = qSource.find((q: any) => {
        const qTopicCode = (() => {
          const code = q.questionCode || q.id || '';
          if (!code) return '';
          const parts = code.split('-');
          return parts.length > 2 ? parts.slice(0, parts.length - 2).join('-').toLowerCase() : code.toLowerCase();
        })();
        return qTopicCode === t.toLowerCase();
      });
      if (foundQ) {
        return foundQ.topicName || foundQ.topic || t;
      }
      for (const ch of chapters) {
        const findInTopics = (topicsList: any[]): any => {
          for (const x of topicsList) {
            const xCode = String(x.topicCode || x.code || x.id || '').toLowerCase();
            const xName = String(x.name || x.topicName || '').toLowerCase();
            if (xCode === t.toLowerCase() || xName === t.toLowerCase()) {
              return x;
            }
            if (x.subtopics && Array.isArray(x.subtopics)) {
              const subFound = findInTopics(x.subtopics);
              if (subFound) return subFound;
            }
          }
          return null;
        };
        const found = findInTopics(ch.topics || []);
        if (found) {
          return found.name || found.topicName || found.topic || t;
        }
      }
      return t;
    });
  };

  // Standard KaTeX Auto-Render Hook (Same as create-qb and rest of app)
  useMathRender([previewQuestions, daysConfig, result]);

  // Fetch initial config and batches via backend API
  useEffect(() => {
    const init = async () => {
      if (!firebaseUser) return;
      try {
        const idToken = await firebaseUser.getIdToken();
        const res = await fetch('/api/admin/classroom-test', {
          headers: { 'Authorization': `Bearer ${idToken}` }
        });
        if (!res.ok) throw new Error('Failed to load init configs.');
        const data = await res.json();
        
        setBatches(data.batches || []);
        const sSubjects = data.syllabusSubjects || {};
        setSyllabusSubjects(sSubjects);
        setBoards(Object.keys(sSubjects));
        await loadAssignments();
      } catch (err) {
        console.error('Initialization error:', err);
      } finally {
        setLoading(false);
      }
    };
    init();
  }, [firebaseUser]);



  // Cascading selects
  useEffect(() => {
    if (!selectedBoard || !syllabusSubjects[selectedBoard]) {
      setClasses([]);
      setSelectedClass('');
      return;
    }
    const clsKeys = Object.keys(syllabusSubjects[selectedBoard]);
    setClasses(clsKeys);
    setSelectedClass('');
  }, [selectedBoard, syllabusSubjects]);

  useEffect(() => {
    if (!selectedBoard || !selectedClass || !syllabusSubjects[selectedBoard]?.[selectedClass]) {
      setSubjects([]);
      setSelectedSubjects([]);
      return;
    }
    const subKeys = Object.keys(syllabusSubjects[selectedBoard][selectedClass]);
    setSubjects(subKeys);
    setSelectedSubjects([]);
  }, [selectedClass, selectedBoard, syllabusSubjects]);

  useEffect(() => {
    const loadChaptersList = async () => {
      if (!firebaseUser || !selectedBoard || !selectedClass || selectedSubjects.length === 0) {
        setChapters([]);
        setSelectedChapters([]);
        setCurrentChapterTopics([]);
        return;
      }
      try {
        const idToken = await firebaseUser.getIdToken();
        const allChapters: any[] = [];
        
        await Promise.all(selectedSubjects.map(async (subj) => {
          const docId = syllabusSubjects[selectedBoard]?.[selectedClass]?.[subj]?.docId;
          if (!docId) return;
          
          const res = await fetch(`/api/admin/syllabus?subjectId=${docId}`, {
            headers: { 'Authorization': `Bearer ${idToken}` }
          });
          if (res.ok) {
            const data = await res.json();
            const list = data.chapters || [];
            list.forEach((ch: any) => {
              allChapters.push({
                subject: subj,
                number: ch.number || ch.chapterNumber,
                name: ch.name || ch.chapterName,
                topics: ch.topics || []
              });
            });
          }
        }));
        
        allChapters.sort((a, b) => {
          if (a.subject !== b.subject) return a.subject.localeCompare(b.subject);
          return Number(a.number) - Number(b.number);
        });
        
        setChapters(allChapters);
      } catch (err) {
        console.error(err);
      }
      setSelectedChapters([]);
      setCurrentChapterTopics([]);
    };
    loadChaptersList();
  }, [selectedSubjects, selectedClass, selectedBoard, syllabusSubjects]);

  const fetchTextbookSets = async () => {
    if (selectedChapters.length === 0 || !firebaseUser) return [];
    try {
      const idToken = await firebaseUser.getIdToken();
      const sets: string[] = [];
      
      let qBoard = selectedBoard;
      if (qBoard === 'State Board' || qBoard === 'MSBSHSE' || qBoard === 'MH') {
        qBoard = 'Maharashtra Board';
      }

      const chapterFetches = selectedChapters.map(async (chKey) => {
        const [subj, chNum] = chKey.split('||');
        try {
          const res = await fetch(`/api/admin/questions?board=${qBoard}&classNum=${selectedClass}&subject=${subj}&chapterNumber=${chNum}&limit=150`, {
            headers: { 'Authorization': `Bearer ${idToken}` }
          });
          if (res.ok) {
            const data = await res.json();
            return data.questions || [];
          }
        } catch (e) {
          console.warn(`Failed to fetch questions for ${chKey}:`, e);
        }
        return [];
      });

      const chapterResults = await Promise.all(chapterFetches);
      chapterResults.flat().forEach((q: any) => {
        const rawSet = q.textbookPracticeSet || q.textbookProblemSet || '';
        if (rawSet) {
          const match = rawSet.match(/(Practice Set|Problem Set|Exercise|Figure it out|Try these|Question Tag|Question Box)\s*\d+(\.\d+)?/i);
          if (match) {
            let cleanSet = match[0].trim().replace(/\s+/g, ' ');
            cleanSet = cleanSet.split(' ').map((w: string) => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join(' ');
            cleanSet = cleanSet.replace(/Figure It Out/i, 'Figure it out')
                               .replace(/Try These/i, 'Try these');
            if (!sets.includes(cleanSet)) {
              sets.push(cleanSet);
            }
          }
        }
      });

      sets.sort((a, b) => {
        return a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' });
      });
      return sets;
    } catch (e) {
      console.error("Failed to fetch textbook sets", e);
      return [];
    }
  };

  // When selectedChapters changes, update topics list and initialize schedule
  useEffect(() => {
    if (selectedChapters.length === 0) {
      setCurrentChapterTopics([]);
      setDaysConfig([]);
      return;
    }

    const tList: string[] = [];
    selectedChapters.forEach(chKey => {
      const [subj, chNum] = chKey.split('||');
      const chObj = chapters.find(c => c.subject === subj && String(c.number) === String(chNum));
      if (chObj) {
        const rawTopics = chObj.topics || [];
        const flatten = (items: any[]) => {
          items.forEach((item: any) => {
            const name = typeof item === 'string' ? item : (item.name || item.topicName || '');
            if (name && !tList.includes(name)) {
              tList.push(name);
            }
            if (item && Array.isArray(item.subtopics)) {
              flatten(item.subtopics);
            }
          });
        };
        flatten(rawTopics);
      }
    });

    const isMath = selectedSubjects.some(subj => /math|algebra|geometry|ganit/i.test(subj));
    if (isMath) {
      const mathTopicsList: string[] = [];
      const seenSetNames = new Set<string>();

      // 1. Load from Syllabus first (both topic textbookSets and chapterExercises)
      selectedChapters.forEach(chKey => {
        const [subj, chNum] = chKey.split('||');
        const chObj = chapters.find(c => c.subject === subj && String(c.number) === String(chNum));
        if (chObj) {
          const chData = chObj as any;
          // Topic-level sets (Practice Sets & Solved Examples)
          if (Array.isArray(chData.topics)) {
            chData.topics.forEach((t: any) => {
              if (Array.isArray(t.textbookSets)) {
                t.textbookSets.forEach((set: any) => {
                  const label = `${set.name} (${set.questionCount || 8} Qs)`;
                  if (!seenSetNames.has(set.name.toLowerCase().trim())) {
                    mathTopicsList.push(label);
                    seenSetNames.add(set.name.toLowerCase().trim());
                  }
                });
              }
            });
          }
          // Chapter-level problem sets
          if (Array.isArray(chData.chapterExercises)) {
            chData.chapterExercises.forEach((set: any) => {
              const label = `${set.name} (${set.questionCount || 8} Qs)`;
              if (!seenSetNames.has(set.name.toLowerCase().trim())) {
                mathTopicsList.push(label);
                seenSetNames.add(set.name.toLowerCase().trim());
              }
            });
          }
        }
      });

      // 2. Load from Question Bank to merge/fallback if needed
      fetchTextbookSets().then(dbSets => {
        dbSets.forEach(s => {
          if (!seenSetNames.has(s.toLowerCase().trim())) {
            let qCount = 8;
            selectedChapters.forEach(chKey => {
              const [subj, chNum] = chKey.split('||');
              const chObj = chapters.find(c => c.subject === subj && String(c.number) === String(chNum));
              if (chObj && Array.isArray((chObj as any).chapterExercises)) {
                (chObj as any).chapterExercises.forEach((ex: any) => {
                  if (ex.name && ex.name.trim().toLowerCase() === s.trim().toLowerCase()) {
                    qCount = ex.questionCount || 8;
                  }
                });
              }
            });
            mathTopicsList.push(`${s} (${qCount} Qs)`);
            seenSetNames.add(s.toLowerCase().trim());
          }
        });

        // 3. Populate state and rebuild schedule config
        if (mathTopicsList.length > 0) {
          mathTopicsList.sort((a, b) => a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' }));
          setCurrentChapterTopics(mathTopicsList);
          rebuildDaysConfig(weekStartDate, mathTopicsList);
        } else {
          alert("⚠️ No textbook sets are configured in the syllabus, and no questions exist in the Question Bank for this chapter.\n\nPlease either:\n1. Define the textbook sets in the Syllabus Manager (/admin/syllabus),\n2. Or generate questions via 'Create QB (AI)' first.");
          setCurrentChapterTopics(tList);
          rebuildDaysConfig(weekStartDate, tList);
        }
      });
    } else {
      setCurrentChapterTopics(tList);
      rebuildDaysConfig(weekStartDate, tList);
    }
  }, [selectedChapters, weekStartDate, chapters, selectedSubjects, firebaseUser]);

  // Dynamic days config generation based on selected start date and topics list
  const rebuildDaysConfig = (selectedDateStr: string, topics: string[]) => {
    if (!selectedDateStr) return;
    const parts = selectedDateStr.split('-');
    if (parts.length !== 3) return;
    const yr = parseInt(parts[0], 10);
    const mo = parseInt(parts[1], 10) - 1;
    const dy = parseInt(parts[2], 10);
    const startDate = new Date(yr, mo, dy);

    const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    const newConfig: DayConfig[] = [];
    let current = new Date(startDate);
    
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    const maxTopicsPerDay = 3;
    let topicIndex = 0;

    // Loop until all topics are assigned and we finish the current week up to Saturday
    while (topicIndex < topics.length || (newConfig.length > 0 && current.getDay() !== 0)) {
      if (topicIndex >= topics.length && current.getDay() === 0) {
        break; // Stop at Sunday if all topics are covered
      }

      const dayNum = current.getDay();
      const dName = dayNames[dayNum];
      const curYr = current.getFullYear();
      const curMo = String(current.getMonth() + 1).padStart(2, '0');
      const curDy = String(current.getDate()).padStart(2, '0');
      const dateStr = `${curYr}-${curMo}-${curDy}`;

      const dateObj = new Date(curYr, current.getMonth(), current.getDate());
      const isPast = dateObj < today;

      if (dayNum === 0) {
        // Sunday Holiday
        newConfig.push({
          dayName: dName,
          date: dateStr,
          active: false,
          topics: ['Sunday Holiday']
        });
      } else if (dayNum === 6) {
        // Saturday classroom test day (inactive if in the past)
        newConfig.push({
          dayName: dName,
          date: dateStr,
          active: !isPast,
          isSaturday: true,
          topics: ['Saturday Classroom Exam (Auto-Sampled)']
        });
      } else {
        // Weekday (Mon-Fri)
        let dayTopics: string[] = [];
        let isDayActive = false;

        // Only assign topics to days that are not in the past
        if (!isPast && topicIndex < topics.length) {
          dayTopics = topics.slice(topicIndex, topicIndex + maxTopicsPerDay);
          topicIndex += maxTopicsPerDay;
          isDayActive = true;
        } else {
          isDayActive = false;
        }

        newConfig.push({
          dayName: dName,
          date: dateStr,
          active: isDayActive,
          topics: dayTopics
        });
      }

      current.setDate(current.getDate() + 1);
    }

    setDaysConfig(newConfig);
  };

  // Helper to assign topics in chunks of max 3 to active weekdays
  const distributeTopicsEvenly = (config: DayConfig[], topics: string[]) => {
    const activeDays = config.filter(d => !d.isSaturday && d.active);
    if (activeDays.length === 0) return;

    // Reset assigned topics for active days
    config.forEach(d => {
      if (!d.isSaturday) d.topics = [];
    });

    if (topics.length === 0) return;

    const maxTopicsPerDay = 3;
    let topicIndex = 0;

    for (const d of activeDays) {
      if (topicIndex >= topics.length) break;
      d.topics = topics.slice(topicIndex, topicIndex + maxTopicsPerDay);
      topicIndex += maxTopicsPerDay;
    }

    setDaysConfig([...config]);
  };

  const handleAutoDistribute = () => {
    distributeTopicsEvenly(daysConfig, currentChapterTopics);
  };

  const handleSelectAllTopics = () => {
    const updated = [...daysConfig];
    updated.forEach(d => {
      if (!d.isSaturday && d.active) {
        d.topics = [...currentChapterTopics];
      }
    });
    setDaysConfig(updated);
  };

  const handleClearAllTopics = () => {
    const updated = [...daysConfig];
    updated.forEach(d => {
      if (!d.isSaturday) {
        d.topics = [];
      }
    });
    setDaysConfig(updated);
  };

  const handleToggleDayActive = (index: number) => {
    const updated = [...daysConfig];
    const targetDay = updated[index];

    // Prevent activating back dates (past dates)
    if (!targetDay.active) {
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      const parts = targetDay.date.split('-');
      const targetDate = new Date(parseInt(parts[0], 10), parseInt(parts[1], 10) - 1, parseInt(parts[2], 10));
      if (targetDate < today) {
        alert('❌ Error: Cannot schedule exams on back dates (dates in the past).');
        return;
      }
    }

    updated[index].active = !updated[index].active;

    // Re-distribute topics among active days
    const activeDays = updated.filter(d => !d.isSaturday && d.active);
    updated.forEach(d => {
      if (!d.isSaturday) d.topics = [];
    });

    if (currentChapterTopics.length > 0 && activeDays.length > 0) {
      currentChapterTopics.forEach((t, i) => {
        const targetDayIndex = i % activeDays.length;
        activeDays[targetDayIndex].topics.push(t);
      });
    }

    setDaysConfig(updated);
  };

  const handleDayTopicToggle = (dayIndex: number, topicName: string) => {
    const updated = [...daysConfig];
    const currentTopics = updated[dayIndex].topics || [];
    if (currentTopics.includes(topicName)) {
      updated[dayIndex].topics = currentTopics.filter(t => t !== topicName);
    } else {
      updated[dayIndex].topics = [...currentTopics, topicName];
    }
    setDaysConfig(updated);
  };

  // Generate PYQ AI Prompt for Selected Chapter Topics
  const handleGeneratePYQPrompt = () => {
    if (!selectedBoard || !selectedClass || selectedSubjects.length === 0 || selectedChapters.length === 0) {
      alert('Please select Board, Class, Subjects, and Chapters first.');
      return;
    }
    const [subj, chNum] = selectedChapters[0].split('||');
    const chName = chapters.find(c => c.subject === subj && String(c.number) === String(chNum))?.name || `Chapter ${chNum}`;
    const activeTopics = daysConfig
      .filter(d => !d.isSaturday && d.active)
      .flatMap(d => d.topics);
    
    const uniqueTopics = currentChapterTopics;
    const isMath = /math|algebra|geometry|ganit/i.test(subj);

    const promptText = `
Role & Goal: You are an expert CBSE & State Board Paper Setter. 
Generate authentic, high-yield Previous Year Questions (PYQs) and PYQ-style subjective questions for:
- Board: ${selectedBoard}
- Class: ${selectedClass}
- Subject: ${subj}
- Chapter ${chNum}: ${chName}

Topics to cover (${uniqueTopics.length}):
${uniqueTopics.map((t, idx) => `${idx + 1}. ${t}`).join('\n')}

COMPREHENSIVE QUESTION GENERATION REQUIREMENTS:
For each topic listed above, you must generate a comprehensive set of questions to ensure complete coverage:
- For Science / other subjects: You MUST extract and generate EVERY SINGLE question matching each topic from the official Digest (Navneet, Target, etc.) and textbook. Do NOT skip or omit any questions.
- You MUST pull and include ALL past Board Exam Questions (PYQs) for each topic from the last 10 years, tagging their exact exam year (e.g., "MSBSHSE 2019", "CBSE 2020") in the "pyqInfo" field.
- Generate a thorough variety of question types for each topic:
  * 1-Mark short/definitions/fill-in/state laws (type: "subjective_define", marks: 1)
  * 2-Mark short specific / scientific reasons / distinguish between / short notes (type: "subjective_short", marks: 2)
  * 4-Mark long specific / detailed explanations / diagram-based / experimental setups (type: "subjective_long", marks: 4)
- Aim to generate at least 8 to 15 questions per topic to ensure maximum textbook and digest coverage.
${isMath ? `
- For Mathematics, 80% of the generated questions/problems MUST be taken directly and verbatim from the official textbook exercises, practice sets, problem sets, solved examples, or figure-it-out sections (absolutely no modified numbers, coefficients, or variables). The remaining 20% of the questions/problems MUST be designed on a similar pattern (using the exact same structural concept, method, and difficulty as textbook problems but with altered values).
- You MUST specify the corresponding textbook reference or pattern source for each question in the "textbookPracticeSet" key:
  * For CBSE Class 8 Mathematics (using Ganit Prakash): Use "Figure it out X.Y: Qz" (e.g., "Figure it out 1.1: Q2") or "Question Tag X.Y: Qz" based on the book's terminology.
  * For other CBSE classes: Use "Exercise X.Y: Qz" (e.g., "Exercise 2.3: Q4").
  * For Maharashtra State Board: Use "Practice Set X.Y: Qz" (e.g., "Practice Set 1.2: Q3") or "Problem Set X: Qz".
` : ''}

STRICT VERBATIM, PYQ TAGGING & INLINE HIGHLIGHT RULES:
1. Answers MUST be verbatim from standard prescribed NCERT / State Board textbook. Absolutely NO paraphrasing.
2. Embed key phrases inside HTML <mark>keyword</mark> tags directly within the model answer text string (e.g. "The <mark>latent heat of fusion</mark> is...").
3. Separate each logical answer sentence on a new numbered line (1., 2., 3...).
4. VERY IMPORTANT: You must add a "pyqInfo" property indicating which year and exam this question or a similar question appeared in (e.g., "CBSE Board 2020", "MSBSHSE 2022", "CBSE 2019 Compartment", "Board Exam 2023"). If it is a predicted/style question, write "PYQ Style Practice".

CRITICAL JSON ESCAPING & MATH FORMATTING RULES:
1. Return ONLY the raw valid JSON array/object. DO NOT wrap it in any explanations, introduction, or extra text.
2. Any backslashes (\) in LaTeX math expressions (like \frac, \propto, \pi, \theta, \times, etc.) MUST be double-escaped as \\ (e.g. \\frac, \\propto, \\pi, \\theta). Never use a single backslash inside a JSON string.
3. If using standard math delimiters, represent inline math as \\( ... \\) and block display math as \\\\[ ... \\\\] (always with double-escaped backslashes).
4. Do NOT use raw control characters, actual tab characters, or actual unescaped newlines inside the JSON string values. Use literal "\n" sequence for newlines inside string values.
5. All double quotes inside string values must be properly escaped as \".
6. Ensure there are no trailing commas at the end of lists, arrays, or objects.

OUTPUT FORMAT: Return ONLY a valid JSON array of objects with schema:
[
  {
    "topicName": "One of the topic names listed in 'Topics to cover' above that this question belongs to",
    "type": "${isMath ? 'numerical_short' : 'subjective_define'}",
    "marks": ${isMath ? 2 : 1},
    "text": "Question text here...",
    "solution": "Verbatim model answer with <mark>key terms</mark> highlighted...",
    "keywords": ["key term 1", "key term 2"],
    "pyqInfo": "CBSE Board 2020"${isMath ? `,\n    "textbookPracticeSet": "Exercise 1.1: Complete set",\n    "isTheorem": false` : ''}
  }
]
    `.trim();

    setQbPrompt(promptText);
    navigator.clipboard.writeText(promptText);
    setQbStatus('📋 PYQ Prompt generated and copied to clipboard! Paste into Gemini or ChatGPT, then paste response on the right to parse.');
  };

  // Generate AI Prompt for Selected Chapter Topics
  const handleGeneratePromptForChapter = () => {
    if (!selectedBoard || !selectedClass || selectedSubjects.length === 0 || selectedChapters.length === 0) {
      alert('Please select Board, Class, Subjects, and Chapters first.');
      return;
    }
    const [subj, chNum] = selectedChapters[0].split('||');
    const chName = chapters.find(c => c.subject === subj && String(c.number) === String(chNum))?.name || `Chapter ${chNum}`;
    const activeTopics = daysConfig
      .filter(d => !d.isSaturday && d.active)
      .flatMap(d => d.topics);
    
    const uniqueTopics = Array.from(new Set(activeTopics.length > 0 ? activeTopics : currentChapterTopics));
    const isMath = /math|algebra|geometry|ganit/i.test(subj);

    const promptText = `
Role & Goal: You are a Subjective Question Generator for an Indian Secondary School Question Bank.
Generate textbook-verbatim subjective questions for:
- Board: ${selectedBoard}
- Class: ${selectedClass}
- Subject: ${subj}
- Chapter ${chNum}: ${chName}

Topics to cover (${uniqueTopics.length}):
${uniqueTopics.map((t, idx) => `${idx + 1}. ${t}`).join('\n')}

COMPREHENSIVE QUESTION GENERATION REQUIREMENTS:
For each topic listed above, you must generate a comprehensive set of questions to ensure complete coverage:
- For Science / other subjects: You MUST extract and generate EVERY SINGLE question matching each topic from the official Digest (Navneet, Target, etc.) and textbook. Do NOT skip or omit any questions.
- You MUST pull and include ALL past Board Exam Questions (PYQs) for each topic from the last 10 years, tagging their exact exam year (e.g., "MSBSHSE 2019", "CBSE 2020") in the "pyqInfo" field.
- Generate a thorough variety of question types for each topic:
  * 1-Mark short/definitions/fill-in/state laws (type: "subjective_define", marks: 1)
  * 2-Mark short specific / scientific reasons / distinguish between / short notes (type: "subjective_short", marks: 2)
  * 4-Mark long specific / detailed explanations / diagram-based / experimental setups (type: "subjective_long", marks: 4)
- Aim to generate at least 8 to 15 questions per topic to ensure maximum textbook and digest coverage.
${isMath ? `
- For Mathematics, 80% of the generated questions/problems MUST be taken directly and verbatim from the official textbook exercises, practice sets, problem sets, solved examples, or figure-it-out sections (absolutely no modified numbers, coefficients, or variables). The remaining 20% of the questions/problems MUST be designed on a similar pattern (using the exact same structural concept, method, and difficulty as textbook problems but with altered values).
- You MUST specify the corresponding textbook reference or pattern source for each question in the "textbookPracticeSet" key:
  * For CBSE Class 8 Mathematics (using Ganit Prakash): Use "Figure it out X.Y: Qz" (e.g., "Figure it out 1.1: Q2") or "Question Tag X.Y: Qz" based on the book's terminology.
  * For other CBSE classes: Use "Exercise X.Y: Qz" (e.g., "Exercise 2.3: Q4").
  * For Maharashtra State Board: Use "Practice Set X.Y: Qz" (e.g., "Practice Set 1.2: Q3") or "Problem Set X: Qz".
` : ''}

STRICT VERBATIM & INLINE HIGHLIGHT RULES:
1. Answers MUST be verbatim from standard prescribed NCERT / State Board textbook. Absolutely NO paraphrasing.
2. Embed key phrases inside HTML <mark>keyword</mark> tags directly within the model answer text string (e.g. "The <mark>latent heat of fusion</mark> is the amount of heat...").
3. Separate each logical answer sentence on a new numbered line (1., 2., 3...).

CRITICAL JSON ESCAPING & MATH FORMATTING RULES:
1. Return ONLY the raw valid JSON array/object. DO NOT wrap it in any explanations, introduction, or extra text.
2. Any backslashes (\) in LaTeX math expressions (like \frac, \propto, \pi, \theta, \times, etc.) MUST be double-escaped as \\ (e.g. \\frac, \\propto, \\pi, \\theta). Never use a single backslash inside a JSON string.
3. If using standard math delimiters, represent inline math as \\( ... \\) and block display math as \\\\[ ... \\\\] (always with double-escaped backslashes).
4. Do NOT use raw control characters, actual tab characters, or actual unescaped newlines inside the JSON string values. Use literal "\n" sequence for newlines inside string values.
5. All double quotes inside string values must be properly escaped as \".
6. Ensure there are no trailing commas at the end of lists, arrays, or objects.

OUTPUT FORMAT: Return ONLY a valid JSON array of objects with schema:
[
  {
    "topicName": "${uniqueTopics[0] || 'General'}",
    "type": "${isMath ? 'numerical_short' : 'subjective_define'}",
    "marks": ${isMath ? 2 : 1},
    "text": "Question text here...",
    "solution": "Verbatim model answer with <mark>key terms</mark> highlighted...",
    "keywords": ["key term 1", "key term 2"]${isMath ? `,\n    "textbookPracticeSet": "Exercise 1.1: Complete set",\n    "isTheorem": false` : ''}
  }
]
    `.trim();

    setQbPrompt(promptText);
    try {
      navigator.clipboard.writeText(promptText)
        .then(() => {
          setQbStatus('📋 Prompt generated and copied to clipboard! Paste into Gemini or ChatGPT, then paste response on the right to parse.');
        })
        .catch(() => {
          const ta = document.createElement('textarea');
          ta.value = promptText;
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.focus();
          ta.select();
          document.execCommand('copy');
          document.body.removeChild(ta);
          setQbStatus('📋 Prompt generated and copied to clipboard! Paste into Gemini or ChatGPT, then paste response on the right to parse.');
        });
    } catch {
      const ta = document.createElement('textarea');
      ta.value = promptText;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.focus();
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
      setQbStatus('📋 Prompt generated and copied to clipboard! Paste into Gemini or ChatGPT, then paste response on the right to parse.');
    }
  };



  const fixRacInText = (text: string) => preprocessMathText(text);

  const resolveTopicNumber = (topicNameFromAI: string, chNumInput?: string, subjectNameInput?: string): string => {
    const chNum = chNumInput || (selectedChapters[0]?.split('||')[1] || '1');
    const subj = subjectNameInput || (selectedChapters[0]?.split('||')[0] || '');
    const chObj = chapters.find(c => c.subject === subj && String(c.number) === String(chNum)) as any;
    if (!chObj || !chObj.topics) return `${chNum}.1`;
    
    const aiNameClean = String(topicNameFromAI || '').trim().toLowerCase();
    
    const cleanStringForMatching = (s: string): string => {
      return s
        .toLowerCase()
        .replace(/^[0-9.]+\s*/, '') // strip topic number prefixes (e.g. 6.1)
        .replace(/[^a-z0-9]/g, '') // remove special characters
        .trim();
    };

    const targetClean = cleanStringForMatching(aiNameClean);

    // Recursive search helper
    const findRecursively = (topicsList: any[]): { name: string; number: string } | null => {
      for (let i = 0; i < topicsList.length; i++) {
        const t = topicsList[i];
        const name = String(typeof t === 'string' ? t : (t.name || t || ''));
        const num = String(t.number || `${chNum}.${i + 1}`);
        
        if (cleanStringForMatching(name) === targetClean) {
          return { name, number: num };
        }
        
        if (t && Array.isArray(t.subtopics)) {
          const found = findRecursively(t.subtopics);
          if (found) return found;
        }
      }
      return null;
    };

    const matchedNode = findRecursively(chObj.topics);
    if (matchedNode) {
      return matchedNode.number;
    }

    // Fallback substring matching helper
    const findSubRecursively = (topicsList: any[]): { name: string; number: string } | null => {
      for (let i = 0; i < topicsList.length; i++) {
        const t = topicsList[i];
        const name = String(typeof t === 'string' ? t : (t.name || t || ''));
        const num = String(t.number || `${chNum}.${i + 1}`);
        const sClean = cleanStringForMatching(name);
        
        if (sClean.includes(targetClean) || targetClean.includes(sClean)) {
          return { name, number: num };
        }
        
        if (t && Array.isArray(t.subtopics)) {
          const found = findSubRecursively(t.subtopics);
          if (found) return found;
        }
      }
      return null;
    };

    const matchedSubNode = findSubRecursively(chObj.topics);
    if (matchedSubNode) {
      return matchedSubNode.number;
    }

    return `${chNum}.1`;
  };

  // Parse JSON response into editable Preview Cards for Teacher Review
  const handleParseQuestions = () => {
    if (!qbPasteJson.trim()) {
      alert('Please paste the AI JSON response array first.');
      return;
    }

    try {
      setQbStatus('⏳ Parsing JSON response...');

      const parsed = robustParseAIJson(qbPasteJson);

      if (!Array.isArray(parsed) || parsed.length === 0) {
        throw new Error('Parsed questions array is empty.');
      }

      if (selectedChapters.length === 0) {
        throw new Error('Please select at least one Chapter first.');
      }

      const [subj, chNum] = selectedChapters[0].split('||');
      const chName = chapters.find(c => c.subject === subj && String(c.number) === String(chNum))?.name || `Chapter ${chNum}`;

      const transformed = parsed.map(q => {
        const marks = Number(q.marks) || (['subjective_define', 'subjective_laws'].includes(q.type) ? 1 : (q.type === 'subjective_long' || q.type === 'numerical_long' ? 4 : 2));
        const defaultType = marks === 1 ? 'subjective_define' : (marks === 4 ? 'subjective_long' : 'subjective_short');
        const rawText = fixRacInText(q.text || q.question || '');
        const solText = fixRacInText(q.solution || q.answer || rawText);
        const kwList = Array.isArray(q.keywords) 
          ? q.keywords.map((k: any) => fixRacInText(String(k))) 
          : (q.keywords ? String(q.keywords).split(',').map(s => fixRacInText(s.trim())) : []);

        const resolvedTopicName = q.topicName || q.topic || '';
        const isTheorem = !!q.isTheorem || 
          /theorem|proof|BPT|Pythagoras|Appollonius|angle\s+bisector|parallel\s+lines|cyclic\s+quadrilateral|inscribed\s+angle/i.test(rawText) || 
          /theorem|proof|BPT|Pythagoras|Appollonius|angle\s+bisector|parallel\s+lines|cyclic\s+quadrilateral|inscribed\s+angle/i.test(resolvedTopicName);

        return {
          type: q.type || defaultType,
          qtype: q.type || defaultType, // PASS qtype REQUIRED BY /api/admin/questions!
          text: rawText,
          marks,
          solution: solText,
          keywords: kwList,
          keywordsText: kwList.join(', '), // PRESERVE RAW KEYWORDS TEXT FOR SMOOTH INPUT TYPING!
          textbookPracticeSet: (() => {
            const raw = q.textbookPracticeSet || q.practiceSet || '';
            return /problem\s*set/i.test(raw) ? '' : raw;
          })(),
          textbookProblemSet: (() => {
            const raw = q.textbookPracticeSet || q.practiceSet || '';
            return /problem\s*set/i.test(raw) ? raw : '';
          })(),
          pyqInfo: q.pyqInfo || q.yearInfo || '',
          board: selectedBoard,
          classNum: selectedClass,
          subjectName: subj,
          chapterNumber: String(chNum),
          chapterName: chName,
          topicNumber: q.topicNumber || resolveTopicNumber(resolvedTopicName, chNum, subj),
          topicName: resolvedTopicName,
          isTheorem
        };
      });

      setPreviewQuestions(transformed);
      setQbStatus(`✅ Successfully parsed ${transformed.length} question(s)! Review and edit them below before saving.`);
    } catch (err: any) {
      setQbStatus(`❌ Parsing Failed: ${err.message}`);
    }
  };

  // Save Reviewed & Validated Questions to Firestore with Bulk Progress Overlay
  const handleSaveValidatedQuestions = async () => {
    if (previewQuestions.length === 0) {
      alert('No questions to save.');
      return;
    }

    // 1. Strict Client-Side Pre-Save Validation Check using SSOT function
    const validationErrors: string[] = [];
    previewQuestions.forEach((q, idx) => {
      const qErrors = validateQuestion(q, 'subjective');
      qErrors.forEach(err => validationErrors.push(`Question #${idx + 1}: ${err}`));
    });

    if (validationErrors.length > 0) {
      const msg = `❌ Pre-Save Validation Failed:\n${validationErrors.join('\n')}`;
      setQbStatus(msg);
      alert(`Validation Failed:\n\n${validationErrors.join('\n')}\n\nPlease fix these issues before saving.`);
      return;
    }

    try {
      setQbSaving(true);
      setSaveStats({ current: 0, total: previewQuestions.length });
      setQbStatus('⏳ Writing validated questions to Question Bank...');

      const idToken = await firebaseUser!.getIdToken();
      const formattedQuestions = previewQuestions.map((q) => ({
        ...q,
        qtype: q.type || q.qtype || 'subjective_define',
        pyqInfo: q.pyqInfo || '',
        keywords: Array.isArray(q.keywords) 
          ? q.keywords 
          : (q.keywordsText ? q.keywordsText.split(',').map((s: string) => s.trim()).filter(Boolean) : [])
      }));

      // Ingest all questions in a single atomic bulk batch request
      const res = await fetch('/api/admin/questions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ action: 'bulkSave', questions: formattedQuestions })
      });

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.message || errData.error || `API rejected batch question saving (Status ${res.status}).`);
      }

      const resData = await res.json().catch(() => ({}));
      const savedCount = resData.savedCount || formattedQuestions.length;
      setSaveStats({ current: savedCount, total: previewQuestions.length });

      setQbStatus(`✅ Successfully saved ${savedCount} question(s) to Question Bank! You can now click "⚡ Generate 1-Click Weekly Suite" below.`);
      setPreviewQuestions([]);
      setQbPasteJson('');

      // Auto-scroll up to the status banner
      const bannerEl = document.getElementById('qb-status-banner');
      if (bannerEl) {
        bannerEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    } catch (err: any) {
      const errMsg = `❌ Save Failed: ${err.message}`;
      setQbStatus(errMsg);

      // Auto-scroll to status banner on error
      const bannerEl = document.getElementById('qb-status-banner');
      if (bannerEl) {
        bannerEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    } finally {
      setQbSaving(false);
    }
  };

  const checkAndGenerateRevisionSuite = async () => {
    if (!selectedBoard || !selectedClass || selectedSubjects.length === 0 || selectedChapters.length === 0) {
      alert('Please select Board, Class, Subjects, and Chapters first.');
      return;
    }
    if (!selectedBatch) {
      alert('Revision Mode requires a Target Batch. Please select a Target Batch to automatically assign the suite.');
      return;
    }

    const todayStr = new Date().toLocaleDateString('en-CA');
    const hasPastActiveDay = daysConfig.some(d => d.active && d.date < todayStr);
    if (hasPastActiveDay) {
      alert('Cannot schedule tests on past dates. Please ensure all active days are today or in the future.');
      return;
    }

    setGenerating(true);
    setResult(null);
    setErrorMsg('');
    setAssignedStatusMsg('');
    setQbStatus('');

    try {
      const idToken = await firebaseUser!.getIdToken();
      setQbStatus('⏳ Checking Question Bank for existing questions for selected chapters...');

      const targetChapters = selectedChapters.map(chKey => {
        const [subj, chNum] = chKey.split('||');
        const chName = chapters.find(c => c.subject === subj && String(c.number) === String(chNum))?.name || `Chapter ${chNum}`;
        return { subject: subj, chapterNumber: chNum, chapterName: chName };
      });

      // Loop through each selected chapter to generate questions if needed
      const activeDays = daysConfig
        .filter(d => !d.isSaturday && d.active);
      const activeTopics = activeDays.flatMap(d => d.topics);
      const uniqueTopics = Array.from(new Set(activeTopics.length > 0 ? activeTopics : currentChapterTopics));

      const isMath = selectedSubjects.some(subj => /math|algebra|geometry|ganit/i.test(subj));
      if (!isMath) {
        await Promise.all(targetChapters.map(async (tc) => {
          const qRes = await fetch(`/api/admin/questions?board=${selectedBoard}&classNum=${selectedClass}&subject=${tc.subject}&chapterNumber=${tc.chapterNumber}&limit=20`, {
            headers: { 'Authorization': `Bearer ${idToken}` }
          });
          const qData = await qRes.json().catch(() => ({}));
          const existingQs = qData.questions || [];

          if (existingQs.length < 8) {
            throw new Error(`The Question Bank only contains ${existingQs.length} question(s) for ${tc.subject} - Chapter ${tc.chapterNumber}. You must have at least 8 questions in the Question Bank for this chapter. Please manually add questions to the Question Bank first.`);
          }
        }));
      }
      setQbStatus('✅ Found/Generated questions in Question Bank.');

      // Now compile and assign
      setQbStatus('⏳ Compiling and assigning Weekly Suite...');
      if (activeDays.length === 0) {
        throw new Error('Please keep at least one weekday active.');
      }

      const firstChapterKey = selectedChapters[0];
      const [firstSubj, firstChNum] = firstChapterKey.split('||');
      const firstChName = chapters.find(c => c.subject === firstSubj && String(c.number) === String(firstChNum))?.name || `Chapter ${firstChNum}`;

      const payload = {
        board: selectedBoard,
        class: selectedClass,
        subject: firstSubj,
        subjects: selectedSubjects,
        chapterNumber: firstChNum,
        selectedChaptersList: targetChapters,
        chapterName: targetChapters.map(c => c.chapterName).join(', '),
        weekStartDate,
        batchId: selectedBatch, // Assigned automatically!
        daysConfig,
        mathType,
        createdBy: firebaseUser!.email
      };

      const res = await fetch('/api/admin/classroom-test/weekly-suite', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify(payload)
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to compile Weekly Suite.');

      setResult({ isWeeklySuite: true, ...data });
      setAssignedStatusMsg(`🟢 Assigned to Batch: ${batches.find(b => b.id === selectedBatch)?.name}`);
      setQbStatus('🎉 Revision suite generated and assigned successfully!');
    } catch (err: any) {
      setErrorMsg(err.message || 'Revision Mode execution failed.');
      setQbStatus(`❌ Failed: ${err.message}`);
    } finally {
      setGenerating(false);
    }
  };

  const handleGenerate = async () => {
    if (!selectedBoard || !selectedClass || selectedSubjects.length === 0) {
      alert('Please fill out Board, Class, and Subjects.');
      return;
    }

    if (testType === 'weekly_suite') {
      if (suiteMode === 'revision') {
        await checkAndGenerateRevisionSuite();
        return;
      }

      if (selectedChapters.length === 0) {
        alert('Please select at least one Chapter for the Weekly Suite.');
        return;
      }

      const activeDays = daysConfig.filter(d => !d.isSaturday && d.active);
      if (activeDays.length === 0) {
        alert('Please keep at least one weekday active (not on break).');
        return;
      }

      const todayStr = new Date().toLocaleDateString('en-CA');
      const hasPastActiveDay = daysConfig.some(d => d.active && d.date < todayStr);
      if (hasPastActiveDay) {
        alert('Cannot schedule tests on past dates. Please ensure all active days are today or in the future.');
        return;
      }

      setGenerating(true);
      setResult(null);
      setErrorMsg('');
      setAssignedStatusMsg('');

      try {
        const idToken = await firebaseUser!.getIdToken();
        const targetChapters = selectedChapters.map(chKey => {
          const [subj, chNum] = chKey.split('||');
          const chName = chapters.find(c => c.subject === subj && String(c.number) === String(chNum))?.name || `Chapter ${chNum}`;
          return { subject: subj, chapterNumber: chNum, chapterName: chName };
        });

        const firstChapterKey = selectedChapters[0];
        const [firstSubj, firstChNum] = firstChapterKey.split('||');

        const payload = {
          board: selectedBoard,
          class: selectedClass,
          subject: firstSubj,
          subjects: selectedSubjects,
          chapterNumber: firstChNum,
          selectedChaptersList: targetChapters,
          chapterName: targetChapters.map(c => c.chapterName).join(', '),
          weekStartDate,
          batchId: selectedBatch || null, // Optional - unassigned by default
          daysConfig,
          mathType,
          createdBy: firebaseUser!.email
        };

        const res = await fetch('/api/admin/classroom-test/weekly-suite', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
          },
          body: JSON.stringify(payload)
        });

        const data = await res.json();
        if (!res.ok) throw new Error(data.error || 'Failed to generate Weekly Suite.');

        setResult({ isWeeklySuite: true, ...data });
      } catch (err: any) {
        setErrorMsg(err.message || 'Weekly Suite Generation failed.');
      } finally {
        setGenerating(false);
      }
      return;
    }

    // Standard test types
    if (testType !== 'multi-chapter' && selectedChapters.length === 0) {
      alert('Please select at least one Chapter.');
      return;
    }

    setGenerating(true);
    setResult(null);
    setErrorMsg('');

    try {
      const idToken = await firebaseUser!.getIdToken();
      const targetChapters = selectedChapters.map(chKey => {
        const [subj, chNum] = chKey.split('||');
        const chName = chapters.find(c => c.subject === subj && String(c.number) === String(chNum))?.name || `Chapter ${chNum}`;
        return { subject: subj, chapterNumber: chNum, chapterName: chName };
      });

      const firstChapterKey = selectedChapters.length > 0 ? selectedChapters[0] : '';
      const firstSubj = firstChapterKey ? firstChapterKey.split('||')[0] : (selectedSubjects[0] || '');
      const firstChNum = firstChapterKey ? firstChapterKey.split('||')[1] : '';
      const firstChName = firstChapterKey ? (chapters.find(c => c.subject === firstSubj && String(c.number) === String(firstChNum))?.name || `Chapter ${firstChNum}`) : '';

      const params = {
        testType,
        board: selectedBoard,
        class: selectedClass,
        subject: firstSubj,
        subjects: selectedSubjects,
        chapterNumber: testType === 'multi-chapter' ? multiChapters : firstChNum,
        selectedChaptersList: targetChapters,
        chapterName: testType === 'multi-chapter' ? 'Multi-Chapter' : firstChName,
        weekNumber,
        totalQuestions,
        batchId: selectedBatch || null,
        createdBy: firebaseUser!.email
      };

      const res = await fetch('/api/admin/classroom-test', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify(params)
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to compile test.');
      
      setResult(data);
    } catch (err: any) {
      setErrorMsg(err.message || 'Generation failed.');
    } finally {
      setGenerating(false);
    }
  };

  // Manual Batch Assignment Handler
  const handleAssignSuiteToBatch = async () => {
    if (!assignBatchId) {
      alert('Please select a Target Batch to assign this suite.');
      return;
    }
    if (!result || !result.isWeeklySuite) return;

    try {
      const idToken = await firebaseUser!.getIdToken();
      const examIds = [
        ...(result.dailyTests || []).map((t: any) => t.examId),
        result.saturdayTest?.examId
      ].filter(Boolean);

      const res = await fetch('/api/admin/classroom-test/weekly-suite', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'assign',
          examIds,
          targetBatchId: assignBatchId
        })
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Assignment failed.');

      const batchName = batches.find(b => b.id === assignBatchId)?.name || assignBatchId;
      setAssignedStatusMsg(`🟢 Assigned to Batch: ${batchName}`);
    } catch (err: any) {
      alert('Assign error: ' + err.message);
    }
  };

  const loadAssignments = async () => {
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/classroom-test/weekly-suite', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      const data = await res.json();
      setAssignments(data.assignments || []);
    } catch (err) {
      console.error('Failed to load assignments:', err);
    }
  };

  const toISTString = toISTDateTimeLocalInput;

  const openSaturdayAssign = (exam: any) => {
    const existing = assignments.find((a: any) => a.examId === exam.id || a.examId === exam.examId);
    const examDate = exam.scheduledDate || exam.date || getDateKeyIST();
    const defaultStart = `${examDate}T09:00`;
    const defaultEnd = `${examDate}T21:00`;

    setSaturdayAssignModal({
      show: true,
      examId: exam.id || exam.examId,
      examName: exam.name || `Saturday Classroom Test — ${result?.chapterName || ''}`,
      batchId: existing?.targetBatches?.[0] || exam.batchId || '',
      startAtStr: existing ? toISTString(existing.startAt) : defaultStart,
      endAtStr: existing ? toISTString(existing.endAt) : defaultEnd,
      examDuration: existing?.examDuration || existing?.classroomDuration || 60,
      assignmentId: existing?.id
    });
  };

  const handleSaveSaturdayAssignment = async () => {
    if (!firebaseUser) return;
    const { examId, batchId, startAtStr, endAtStr, examDuration, assignmentId } = saturdayAssignModal;

    if (!batchId) {
      alert('Please select a target batch to assign.');
      return;
    }

    if (!startAtStr || !endAtStr) {
      alert('Please select start and end datetimes.');
      return;
    }

    const startDateTime = new Date(startAtStr);
    const endDateTime = new Date(endAtStr);
    if (endDateTime <= startDateTime) {
      alert('❌ Error: End datetime must be after start datetime.');
      return;
    }

    try {
      const idToken = await firebaseUser.getIdToken();
      
      if (assignmentId) {
        const res = await fetch('/api/admin/exams', {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
          },
          body: JSON.stringify({
            id: assignmentId,
            collection: 'subjectiveAssignments',
            openMode: 'scheduled',
            startAtStr,
            endAtStr,
            attemptLimit: 1,
            examDuration
          })
        });

        if (!res.ok) throw new Error('Failed to update Saturday test assignment.');
        alert('✅ Saturday Classroom Test assignment updated successfully!');
      } else {
        const res = await fetch('/api/admin/exams', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
          },
          body: JSON.stringify({
            examId,
            type: 'subjective',
            targetType: 'batch',
            targetBatches: [batchId],
            targetStudents: [],
            openMode: 'scheduled',
            startAtStr,
            endAtStr,
            attemptLimit: 1,
            examDuration,
            examMode: 'classroom',
            classroomDuration: examDuration,
            classroomTimePerQ: 5
          })
        });

        if (!res.ok) throw new Error('Failed to assign Saturday test.');
        alert('✅ Saturday Classroom Test activated successfully!');
      }

      setSaturdayAssignModal(prev => ({ ...prev, show: false }));
      loadAssignments();
    } catch (err: any) {
      alert('Error: ' + err.message);
    }
  };

  // Scheduled Suites Manager: Fetch & Delete
  const handleOpenManager = async () => {
    setShowManagerModal(true);
    setLoadingScheduled(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/classroom-test/weekly-suite', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      const data = await res.json();
      setScheduledExamsList(data.exams || []);
      setAssignments(data.assignments || []);
    } catch (err) {
      console.error(err);
    } finally {
      setLoadingScheduled(false);
    }
  };

  const handleDeleteSuiteGroup = async (examIds: string[]) => {
    if (!confirm(`Are you sure you want to delete these ${examIds.length} scheduled test documents?`)) return;

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/classroom-test/weekly-suite', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ examIds })
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Delete failed.');

      alert(data.message || 'Deleted successfully.');
      handleOpenManager(); // Refresh list
    } catch (err: any) {
      alert('Delete error: ' + err.message);
    }
  };

  // Export Master Weekly PDF Bundle helper
  const handleExportMasterPDF = async () => {
    if (!result || !result.isWeeklySuite) return;

    try {
      const printWin = window.open('', '_blank');
      if (!printWin) return;

      const dailyTests = result.dailyTests || [];
      const saturdayTest = result.saturdayTest || {};

      let htmlContent = `
        <!DOCTYPE html>
        <html>
        <head>
          <title>${result.chapterName} — Master Weekly Subjective Suite</title>
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css">
          <style>
            body { font-family: system-ui, -apple-system, sans-serif; color: #171a1f; padding: 20px; line-height: 1.45; }
            h1, h2, h3 { margin: 0 0 8px; }
            .header-banner { text-align: center; border-bottom: 2px solid #2563eb; padding-bottom: 12px; margin-bottom: 20px; }
            .day-card { border: 1px solid #cbd5e1; border-radius: 8px; margin-bottom: 24px; page-break-inside: avoid; overflow: hidden; }
            .day-title { background: #0f172a; color: #fff; padding: 8px 14px; font-size: 13px; font-weight: bold; display: flex; justify-content: space-between; }
            .topic-badge { background: #3b82f6; color: #fff; font-size: 10.5px; padding: 2px 8px; border-radius: 12px; margin-right: 6px; }
            .q-box { border-bottom: 1px solid #f1f5f9; padding: 10px 14px; page-break-inside: avoid; }
            .q-box:last-child { border-bottom: none; }
            .q-text { font-size: 12.5px; font-weight: 700; margin-bottom: 5px; color: #171a1f; line-height: 1.4; }
            .ans-box { background: #f8fafc; border-left: 4px solid #10b981; padding: 6px 10px; margin-top: 6px; font-size: 11.5px; border-radius: 4px; line-height: 1.4; }
            .ans-text { margin-top: 3px; white-space: pre-wrap; word-break: break-word; color: #222730; }
            mark { background-color: #fef08a !important; color: #854d0e !important; padding: 1px 3px; border-radius: 3px; font-weight: 700; }
            @media print {
              body { padding: 10px; }
              .day-card { page-break-after: always; }
              mark { background-color: #fef08a !important; color: #854d0e !important; -webkit-print-color-adjust: exact; }
            }
          </style>
          <script src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js"></script>
          <script src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js"></script>
        </head>
        <body>
          <div class="header-banner math-container">
            <h1 style="font-size: 18px; color: #0f172a;">YASHCOM Performance Learning OS — Master Weekly Suite</h1>
            <div style="font-size: 12.5px; font-weight: bold; color: #475569;">
              ${selectedBoard} Class ${selectedClass} | ${selectedSubjects.join(', ')} | Chapter(s) ${selectedChapters.map(c => c.split('||')[1]).join(', ')}: ${result.chapterName}
            </div>
            <div style="font-size: 11px; color: #64748b; margin-top: 3px;">Week Starting: ${weekStartDate}</div>
          </div>
      `;

      // Helper to clean up model answer text without excessive blank lines
      const sanitizeAnswer = (solution?: string, text?: string, keywords?: string[]) => {
        let ans = (solution && typeof solution === 'string' ? solution : '').trim();
        if (!ans || ans === (text || '').trim()) {
          ans = 'Refer to prescribed textbook for the complete step-by-step model solution.';
        }
        ans = ans.replace(/\n{3,}/g, '\n\n');
        ans = ans.split('\n').map(l => l.trimEnd()).join('\n').trim();
        return highlightModelAnswerKeywords(preprocessMathText(ans), keywords);
      };

      // Render Daily Home Practice sheets (Mon-Fri)
      dailyTests.forEach((dTest: any) => {
        const qSource = dTest.learningQuestions || dTest.questions || [];
        const practiceSets = qSource
          .map((q: any) => q.textbookPracticeSet || q.textbookProblemSet)
          .filter(Boolean);
        const uniquePracticeSets = Array.from(new Set(practiceSets));
        const totalMarksForLearning = qSource.reduce((sum: number, q: any) => sum + (Number(q.marks) || 1), 0);

        htmlContent += `
          <div class="day-card math-container">
            <div class="day-title">
              <span>📅 ${dTest.dayName.toUpperCase()} HOME PRACTICE — ${dTest.date}</span>
              <span>Total: ${totalMarksForLearning} Marks</span>
            </div>
            <div style="padding: 8px 14px; background: #eff6ff; font-size: 11px; color: #1e40af; border-bottom: 1px solid #dbeafe; display: flex; flex-direction: column; gap: 3px;">
              <div><strong>Topics Covered:</strong> ${getTopicNamesForDisplay(dTest.topics, dTest.learningQuestions || dTest.questions).join(', ') || 'Chapter Review'}</div>
              ${uniquePracticeSets.length > 0 ? `
                <div style="color: #b91c1c; font-weight: 700; margin-top: 2px;">
                  📖 Required Textbook Practice Set: ${uniquePracticeSets.join(' | ')}
                </div>
              ` : ''}
            </div>
            ${qSource.map((q: any, idx: number) => `
              <div class="q-box">
                <div class="q-text">
                  Q${idx + 1}. ${preprocessMathText(q.text)} <span style="font-weight: normal; color: #64748b; font-size: 11px;">[${q.marks} Mark${q.marks > 1 ? 's' : ''}]</span>
                </div>
                <div class="ans-box">
                  <strong style="color: #065f46;">💡 Model Answer:</strong>
                  <div class="ans-text">${sanitizeAnswer(q.solution, q.text, q.keywords)}</div>
                </div>
              </div>
            `).join('')}
          </div>
        `;
      });

      htmlContent += `
          <script>
            document.addEventListener("DOMContentLoaded", function() {
              renderMathInElement(document.body, {
                delimiters: [
                  {left: '$$', right: '$$', display: true},
                  {left: '$', right: '$', display: false},
                  {left: '\\\\(', right: '\\\\)', display: false},
                  {left: '\\\\[', right: '\\\\]', display: true}
                ],
                throwOnError : false
              });
            });
          </script>
        </body>
        </html>
      `;

      printWin.document.write(htmlContent);
      printWin.document.close();
      setTimeout(() => {
        printWin.focus();
        printWin.print();
      }, 500);
    } catch (err: any) {
      alert('Print PDF error: ' + err.message);
    }
  };

  // Helper to print date-wise topic planner sheet
  const printPlannerForSuite = (chapterName: string, dailyTests: any[], saturdayTest: any) => {
    try {
      const printWin = window.open('', '_blank');
      if (!printWin) return;

      // Sort dailyTests by date
      const sortedDaily = [...dailyTests].sort((a, b) => {
        if (!a.date || !b.date) return 0;
        return a.date.localeCompare(b.date);
      });

      // Find the first date or week starting date
      const firstDate = sortedDaily[0]?.date || 'Scheduled Week';

      // Resolve board, class, subjects from the first test's attributes
      const boardVal = sortedDaily[0]?.board || selectedBoard || 'MH State Board';
      const classVal = sortedDaily[0]?.class || selectedClass || '10';
      const subjectVal = sortedDaily[0]?.subject || (selectedSubjects.join(', ')) || 'Science';

      let htmlContent = `
        <!DOCTYPE html>
        <html>
        <head>
          <title>${chapterName} — Weekly Study Planner</title>
          <style>
            body { font-family: system-ui, -apple-system, sans-serif; color: #222730; padding: 30px; line-height: 1.5; background: #fff; }
            .header-banner { text-align: center; border-bottom: 3px solid #2563eb; padding-bottom: 16px; margin-bottom: 24px; }
            .header-title { font-size: 24px; font-weight: 800; color: #0f172a; margin: 0; text-transform: uppercase; letter-spacing: 0.5px; }
            .meta-info { font-size: 13px; font-weight: bold; color: #475569; margin-top: 6px; }
            .week-info { font-size: 12px; color: #64748b; margin-top: 4px; }
            
            table { width: 100%; border-collapse: collapse; margin-top: 20px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05); }
            th { background: #0f172a; color: #fff; padding: 12px 16px; font-size: 13px; font-weight: 800; text-align: left; text-transform: uppercase; }
            td { padding: 12px 16px; border-bottom: 1px solid #e2e8f0; font-size: 12.5px; vertical-align: top; }
            tr:nth-child(even) { background: #f8fafc; }
            
            .day-cell { font-weight: bold; color: #171a1f; }
            .type-badge { display: inline-block; padding: 3px 8px; border-radius: 4px; font-size: 10.5px; font-weight: 700; text-transform: uppercase; }
            .badge-practice { background: #eff6ff; color: #1e40af; border: 1px solid #bfdbfe; }
            .badge-exam { background: #ecfdf5; color: #065f46; border: 1px solid #a7f3d0; }
            
            .topic-list { margin: 0; padding-left: 18px; }
            .topic-list li { margin-bottom: 4px; }
            .practice-set { margin-top: 6px; font-size: 11px; font-weight: bold; color: #b91c1c; }
            
            .footer-note { text-align: center; margin-top: 40px; font-size: 11px; color: #64748b; border-top: 1px solid #e2e8f0; padding-top: 15px; }
            @media print {
              body { padding: 10px; }
              table { box-shadow: none; page-break-inside: avoid; }
              th { background-color: #0f172a !important; color: #fff !important; -webkit-print-color-adjust: exact; }
              .badge-practice { background-color: #eff6ff !important; color: #1e40af !important; -webkit-print-color-adjust: exact; }
              .badge-exam { background-color: #ecfdf5 !important; color: #065f46 !important; -webkit-print-color-adjust: exact; }
            }
          </style>
        </head>
        <body>
          <div class="header-banner">
            <h1 class="header-title">YASHCOM Performance Learning OS</h1>
            <div style="font-size: 15px; font-weight: 700; color: #2563eb; margin-top: 4px;">📅 Weekly Study Planner & Schedule</div>
            <div class="meta-info">
              ${boardVal} Class ${classVal} | ${subjectVal} | Chapter: ${chapterName}
            </div>
            <div class="week-info">Week Starting Date: <strong>${firstDate}</strong></div>
          </div>

          <table>
            <thead>
              <tr>
                <th style="width: 25%;">Day / Date</th>
                <th style="width: 20%;">Activity Type</th>
                <th style="width: 55%;">Topics & Assignments</th>
              </tr>
            </thead>
            <tbody>
      `;

      sortedDaily.forEach((dTest: any) => {
        const qSource = dTest.learningQuestions || dTest.questions || [];
        const practiceSets = qSource
          .map((q: any) => q.textbookPracticeSet || q.textbookProblemSet)
          .filter(Boolean);
        const uniquePracticeSets = Array.from(new Set(practiceSets));

        htmlContent += `
          <tr>
            <td class="day-cell">
              <div>${dTest.dayName}</div>
              <div style="font-size: 11px; font-weight: normal; color: #64748b; margin-top: 2px;">${dTest.date || ''}</div>
            </td>
            <td>
              <span class="type-badge badge-practice">✍️ Daily Practice</span>
            </td>
            <td>
              <ul class="topic-list">
                ${getTopicNamesForDisplay(dTest.topics || [], dTest.learningQuestions || dTest.questions).map((name: string) => `<li>${name}</li>`).join('') || '<li>General Practice Exercises</li>'}
              </ul>
              ${uniquePracticeSets.length > 0 ? `
                <div class="practice-set">📖 Required Textbook Exercises: ${uniquePracticeSets.join(' | ')}</div>
              ` : ''}
            </td>
          </tr>
        `;
      });

      if (saturdayTest) {
        htmlContent += `
          <tr>
            <td class="day-cell" style="border-bottom: 2px solid #0f172a;">
              <div>Saturday</div>
              <div style="font-size: 11px; font-weight: normal; color: #64748b; margin-top: 2px;">Exam Day</div>
            </td>
            <td style="border-bottom: 2px solid #0f172a;">
              <span class="type-badge badge-exam">🏫 Classroom Test</span>
            </td>
            <td style="border-bottom: 2px solid #0f172a;">
              <div style="font-weight: bold; color: #171a1f;">Weekly Revision & Evaluation</div>
              <div style="font-size: 11px; color: #475569; margin-top: 3px;">
                Cumulative exam covering all topics listed from Monday to Friday.
              </div>
              <div style="margin-top: 6px; font-size: 11.5px; font-weight: 600; color: #059669;">
                📝 Format: Subjective Assessment (${saturdayTest.totalMarks || 40} Marks)
              </div>
            </td>
          </tr>
        `;
      }

      htmlContent += `
            </tbody>
          </table>

          <div class="footer-note">
            <p><strong>Note for Students:</strong> Please ensure your daily homework practice is completed and uploaded on time. The Saturday Classroom Test is mandatory.</p>
            <p style="font-size: 9.5px; color: #94a3b8; margin-top: 4px;">Generated dynamically by YASHCOM Syllabus Manager</p>
          </div>
        </body>
        </html>
      `;

      printWin.document.write(htmlContent);
      printWin.document.close();
      setTimeout(() => {
        printWin.focus();
        printWin.print();
      }, 500);
    } catch (err: any) {
      alert('Print Planner error: ' + err.message);
    }
  };

  const handlePrintPlanner = () => {
    if (!result || !result.isWeeklySuite) return;
    printPlannerForSuite(result.chapterName, result.dailyTests || [], result.saturdayTest);
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading syllabus parameters...
        </div>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800 }}>🏫 YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Classroom Test & Weekly Suite Generator</h1>
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Automate daily home practice & Saturday classroom exams</div>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          <button 
            className="btn btn-secondary btn-sm"
            onClick={handleOpenManager}
            style={{ fontSize: '11px', fontWeight: 700, padding: '4px 10px', background: '#fef2f2', color: '#b91c1c', border: '1px solid #fca5a5' }}
          >
            🗑️ Manage & Delete Scheduled Suites
          </button>
          
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      {/* Main Workspace */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '900px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>
        
        {/* Form Container */}
        <div className="card" style={{ background: 'var(--surface)', padding: '20px 24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '16px' }}>
          
          {/* Tabs */}
          <div className="test-type-tabs" style={{ display: 'flex', gap: '4px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', overflowX: 'auto' }}>
            <button className={`btn btn-sm ${testType === 'weekly_suite' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setTestType('weekly_suite')}>⚡ 1-Click Weekly Suite</button>
            <button className={`btn btn-sm ${testType === 'weekly' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setTestType('weekly')}>📅 PYQ Subjective</button>
            <button className={`btn btn-sm ${testType === 'chapter' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setTestType('chapter')}>📗 Chapter Test</button>
            <button className={`btn btn-sm ${testType === 'multi-chapter' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setTestType('multi-chapter')}>📚 Multi-Chapter</button>
          </div>

          {/* Core Cascades */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '8px' }}>
            <div className="form-group">
              <label style={{ fontSize: '11px', fontWeight: 600 }}>🏛️ Board</label>
              <select className="form-input" value={selectedBoard} onChange={(e) => setSelectedBoard(e.target.value)}>
                <option value="">Select Board</option>
                {boards.map(b => {
                  const codes: Record<string, string> = { 'Maharashtra Board': 'MH', 'maharashtra board': 'MH', 'CBSE': 'CBSE', 'cbse': 'CBSE', 'ICSE': 'ICSE', 'icse': 'ICSE' };
                  return <option key={b} value={b}>{codes[b] || b}</option>;
                })}
              </select>
            </div>
            
            <div className="form-group">
              <label style={{ fontSize: '11px', fontWeight: 600 }}>🎓 Class</label>
              <select className="form-input" value={selectedClass} onChange={(e) => setSelectedClass(e.target.value)} disabled={classes.length === 0}>
                <option value="">Select Class</option>
                {classes.map(c => <option key={c} value={c}>Class {c}</option>)}
              </select>
            </div>

            <div className="form-group" style={{ gridColumn: 'span 2' }}>
              <label style={{ fontSize: '11px', fontWeight: 600, display: 'block', marginBottom: '6px' }}>📖 Select Subjects</label>
              {subjects.length === 0 ? (
                <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Select board and class first.</div>
              ) : (
                <div style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fill, minmax(180px, 1fr))',
                  gap: '8px',
                  maxHeight: '120px',
                  overflowY: 'auto',
                  background: 'var(--bg)',
                  padding: '8px',
                  borderRadius: 'var(--radius-md)',
                  border: '1px solid var(--border-light)'
                }}>
                  {subjects.map(s => (
                    <label key={s} style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '12px', cursor: 'pointer', color: 'var(--text)' }}>
                      <input 
                        type="checkbox" 
                        checked={selectedSubjects.includes(s)} 
                        onChange={() => {
                          setSelectedSubjects(prev => 
                            prev.includes(s) ? prev.filter(item => item !== s) : [...prev, s]
                          );
                        }} 
                      />
                      {s}
                    </label>
                  ))}
                </div>
              )}
            </div>

            <div className="form-group" style={{ gridColumn: 'span 2' }}>
              <label style={{ fontSize: '11px', fontWeight: 600, display: 'block', marginBottom: '6px' }}>📗 Select Chapters</label>
              {chapters.length === 0 ? (
                <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Select subjects first.</div>
              ) : (
                <div style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))',
                  gap: '8px',
                  maxHeight: '150px',
                  overflowY: 'auto',
                  background: 'var(--bg)',
                  padding: '8px',
                  borderRadius: 'var(--radius-md)',
                  border: '1px solid var(--border-light)'
                }}>
                  {chapters.map(ch => {
                    const key = `${ch.subject}||${ch.number}`;
                    const labelText = `${ch.subject} - Ch ${ch.number}: ${ch.name}`;
                    return (
                      <label key={key} style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '12px', cursor: 'pointer', color: 'var(--text)' }}>
                        <input 
                          type="checkbox" 
                          checked={selectedChapters.includes(key)} 
                          onChange={() => {
                            setSelectedChapters(prev => 
                              prev.includes(key) ? prev.filter(item => item !== key) : [...prev, key]
                            );
                          }} 
                        />
                        {labelText}
                      </label>
                    );
                  })}
                </div>
              )}
            </div>
          </div>

          {/* Week & Batch */}
          {testType !== 'weekly' && (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '8px' }}>
              <div className="form-group">
                <label style={{ fontSize: '11px', fontWeight: 600 }}>📦 Target Batch (Optional)</label>
                <select className="form-input" value={selectedBatch} onChange={(e) => setSelectedBatch(e.target.value)}>
                  <option value="">Unassigned (Assign Later)</option>
                  {batches.map(b => <option key={b.id} value={b.id}>{b.name}</option>)}
                </select>
              </div>

              {selectedSubjects.some(subj => /math|algebra|geometry|ganit/i.test(subj)) && (
                <div className="form-group">
                  <label style={{ fontSize: '11px', fontWeight: 600 }}>📐 Math Subject Type (Override)</label>
                  <select className="form-input" value={mathType} onChange={(e) => setMathType(e.target.value as any)}>
                    <option value="">Auto-Detect</option>
                    <option value="algebra">Algebra / Mathematics Part 1</option>
                    <option value="geometry">Geometry / Mathematics Part 2</option>
                  </select>
                </div>
              )}

              {testType === 'weekly_suite' ? (
                <div className="form-group">
                  <label style={{ fontSize: '11px', fontWeight: 600 }}>📅 Week Calendar Date (Pick Any Date)</label>
                  <input 
                    type="date" 
                    className="form-input" 
                    value={weekStartDate} 
                    onChange={(e) => setWeekStartDate(e.target.value)} 
                  />
                </div>
              ) : (
                <div className="form-group">
                  <label style={{ fontSize: '11px', fontWeight: 600 }}>🔢 Total Questions</label>
                  <input 
                    type="number" 
                    className="form-input" 
                    min={2} 
                    max={20} 
                    value={totalQuestions} 
                    onChange={(e) => {
                      const raw = e.target.value;
                      if (raw === '') {
                        setTotalQuestions('');
                      } else {
                        const val = parseInt(raw, 10);
                        setTotalQuestions(isNaN(val) ? '' : Math.max(2, Math.min(20, val)));
                      }
                    }} 
                    onBlur={() => {
                      if (totalQuestions === '' || Number(totalQuestions) < 2) {
                        setTotalQuestions(6);
                      }
                    }}
                  />
                </div>
              )}
            </div>
          )}

          {testType === 'weekly_suite' && (
            <div style={{ background: 'var(--surface-3)', padding: '10px 14px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', margin: '4px 0 8px' }}>
              <div style={{ fontSize: '12px', fontWeight: 800, color: 'var(--accent)', marginBottom: '3px' }}>
                🚀 Revision Mode Enabled (Autonomous)
              </div>
              <div style={{ fontSize: '10px', color: 'var(--text-muted)' }}>
                Auto-checks Question Bank for topics in this chapter. If missing/insufficient (less than 8 questions), it invokes Gemini AI to generate, parse, save, and automatically assign the schedule to the selected batch in 1 click.
              </div>
            </div>
          )}

          {/* ⚡ WEEKLY SCHEDULE ORGANIZER BOARD */}
          {testType === 'weekly_suite' && daysConfig.length > 0 && (
            <div style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius)', padding: '16px', background: 'var(--bg-soft)', display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 800, color: 'var(--accent)' }}>
                  🗓️ Interactive Weekly Schedule Board (Mon–Sat)
                </h4>

                {/* Topic Distribution & Selection Controls */}
                <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                  <button 
                    className="btn btn-secondary btn-sm" 
                    onClick={handleAutoDistribute}
                    style={{ fontSize: '11px', padding: '4px 10px' }}
                    title="Auto-distribute topics evenly across active days"
                  >
                    🔄 Auto-Distribute
                  </button>
                  <button 
                    className="btn btn-secondary btn-sm" 
                    onClick={handleSelectAllTopics}
                    style={{ fontSize: '11px', padding: '4px 10px' }}
                    title="Select all topics for all active days"
                  >
                    ✅ Select All
                  </button>
                  <button 
                    className="btn btn-secondary btn-sm" 
                    onClick={handleClearAllTopics}
                    style={{ fontSize: '11px', padding: '4px 10px', color: '#dc2626', borderColor: '#fca5a5' }}
                    title="Deselect all topics to select manually"
                  >
                    🧹 Clear / Deselect All
                  </button>
                </div>
              </div>

              <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                Configure active practice days, breaks, and topic combinations. Each active day generates a 10-Mark Test (8:30 PM – 10:30 PM availability window).
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '12px', marginTop: '6px' }}>
                {daysConfig.map((day, idx) => (
                  <div 
                    key={day.dayName} 
                    style={{ 
                      border: `1px solid ${day.isSaturday ? 'var(--success)' : (day.active ? 'var(--border-light)' : '#fca5a5')}`,
                      background: day.isSaturday ? 'rgba(16, 185, 129, 0.05)' : (day.active ? 'var(--surface)' : '#fef2f2'),
                      borderRadius: 'var(--radius)',
                      padding: '12px',
                      display: 'flex',
                      flexDirection: 'column',
                      gap: '8px'
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px' }}>
                      <div style={{ fontWeight: 800, fontSize: '13px' }}>
                        {day.isSaturday ? '🏫' : '📅'} {day.dayName}
                        <span style={{ fontSize: '10px', color: 'var(--text-muted)', marginLeft: '6px', fontWeight: 500 }}>{day.date}</span>
                      </div>
                      <label style={{ 
                        fontSize: '10px', 
                        cursor: day.date < new Date().toLocaleDateString('en-CA') ? 'not-allowed' : 'pointer', 
                        display: 'flex', 
                        alignItems: 'center', 
                        gap: '4px', 
                        fontWeight: 700, 
                        color: day.active ? 'var(--success)' : '#dc2626',
                        opacity: day.date < new Date().toLocaleDateString('en-CA') ? 0.6 : 1
                      }}>
                        <input 
                          type="checkbox" 
                          checked={day.active} 
                          onChange={() => handleToggleDayActive(idx)} 
                          disabled={day.date < new Date().toLocaleDateString('en-CA')}
                        />
                        {day.active ? 'Active' : 'Break ☕'}
                      </label>
                    </div>

                    {!day.isSaturday ? (
                      day.active ? (
                        <div>
                          <div style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '4px' }}>Topics Covered:</div>
                          {currentChapterTopics.length === 0 ? (
                            <div style={{ fontSize: '11px', color: '#94a3b8', fontStyle: 'italic' }}>No topics loaded for chapter</div>
                          ) : (
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '3px', maxHeight: '120px', overflowY: 'auto' }}>
                              {currentChapterTopics.map(topName => (
                                <label key={topName} style={{ fontSize: '11px', display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer' }}>
                                  <input 
                                    type="checkbox"
                                    checked={day.topics.includes(topName)}
                                    onChange={() => handleDayTopicToggle(idx, topName)}
                                  />
                                  <span>{topName}</span>
                                </label>
                              ))}
                            </div>
                          )}
                        </div>
                      ) : (
                        <div style={{ fontSize: '11px', color: '#dc2626', fontWeight: 600, textAlign: 'center', padding: '10px 0' }}>
                          ☕ Holiday / Break Day (No Test Scheduled)
                        </div>
                      )
                    ) : (
                      <div style={{ fontSize: '11px', color: 'var(--success)', fontWeight: 600 }}>
                        🎯 Auto-sampled strictly from Mon–Fri assigned practice pools.
                      </div>
                    )}
                  </div>
                ))}
              </div>

              {/* 🤖 IN-PLACE AI QUESTION GENERATOR & REVIEW WORKSPACE */}
              <div style={{ border: '2px solid var(--accent)', borderRadius: 'var(--radius)', padding: '16px', background: 'var(--surface)', display: 'flex', flexDirection: 'column', gap: '12px', marginTop: '10px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                  <div>
                    <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 800, color: 'var(--accent)' }}>
                      🤖 Generate & Parse Questions for Selected Chapter Topics (If missing in QB)
                    </h4>
                    <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>
                      Generate AI prompt, paste response below, parse & review questions before saving to Question Bank.
                    </div>
                  </div>
                  <button 
                    className="btn btn-secondary btn-sm"
                    onClick={handleGeneratePromptForChapter}
                    style={{ fontSize: '11px', fontWeight: 700, padding: '6px 14px', background: '#7c3aed', color: '#fff', border: 'none' }}
                  >
                    🔧 Generate & Copy AI Prompt
                  </button>
                </div>

                {/* Status Banner with Anchor ID */}
                {qbStatus && (
                  <div 
                    id="qb-status-banner"
                    style={{ padding: '8px 12px', background: qbStatus.startsWith('❌') ? '#fef2f2' : '#f0fdf4', border: `1px solid ${qbStatus.startsWith('❌') ? '#fca5a5' : '#bbf7d0'}`, borderRadius: '4px', fontSize: '11px', color: qbStatus.startsWith('❌') ? '#b91c1c' : '#166534', fontWeight: 600, whiteSpace: 'pre-line' }}
                  >
                    {qbStatus}
                  </div>
                )}

                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '12px' }}>
                  <div className="form-group">
                    <label style={{ fontSize: '11px', fontWeight: 700 }}>📋 Generated AI Prompt</label>
                    <textarea 
                      className="form-input" 
                      rows={5} 
                      value={qbPrompt} 
                      onChange={(e) => setQbPrompt(e.target.value)}
                      placeholder="Click 'Generate & Copy AI Prompt' above to populate prompt..."
                      style={{ fontSize: '11px', fontFamily: 'monospace' }}
                    />
                  </div>

                  <div className="form-group">
                    <label style={{ fontSize: '11px', fontWeight: 700 }}>📥 Paste AI Response (JSON)</label>
                    <textarea 
                      className="form-input" 
                      rows={5} 
                      value={qbPasteJson} 
                      onChange={(e) => setQbPasteJson(e.target.value)}
                      placeholder="Paste JSON array response from Gemini or ChatGPT here..."
                      style={{ fontSize: '11px', fontFamily: 'monospace' }}
                    />
                  </div>
                </div>

                <button 
                  className="btn btn-secondary btn-sm"
                  onClick={handleParseQuestions}
                  disabled={!qbPasteJson.trim()}
                  style={{ alignSelf: 'flex-end', padding: '8px 18px', fontSize: '12px', fontWeight: 700, background: '#3b82f6', color: '#fff', border: 'none' }}
                >
                  ⚡ Parse & Preview Questions for Review
                </button>

                {/* Interactive Question Preview & Review Cards with Standard KaTeX Rendering */}
                {previewQuestions.length > 0 && (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginTop: '10px', borderTop: '1px dashed var(--border-light)', paddingTop: '14px' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 800, color: 'var(--accent)' }}>
                        🔍 Review & Edit Parsed Questions ({previewQuestions.length} Qs)
                      </h4>
                      <button 
                        className="btn btn-secondary btn-sm"
                        onClick={() => setPreviewQuestions([])}
                        style={{ fontSize: '10px', padding: '2px 8px' }}
                      >
                        ✕ Clear Preview
                      </button>
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', maxHeight: '450px', overflowY: 'auto' }}>
                      {previewQuestions.map((q, idx) => (
                        <div key={idx} className="math-container" style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '12px', background: 'var(--bg-soft)', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '11px' }}>
                            <span style={{ fontWeight: 800, color: 'var(--accent)' }}>
                              Q{idx + 1} • Topic: {q.topicName || 'General'}
                            </span>
                            <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                              <span className="badge" style={{ background: 'var(--surface-3)', color: 'var(--text)', padding: '2px 8px', borderRadius: '4px', fontSize: '10px' }}>
                                {q.marks} Mark{q.marks > 1 ? 's' : ''} ({q.type})
                              </span>
                              <button 
                                className="btn btn-secondary btn-sm" 
                                onClick={() => setPreviewQuestions(prev => prev.filter((_, i) => i !== idx))}
                                style={{ background: '#fef2f2', color: '#b91c1c', border: '1px solid #fca5a5', fontSize: '10px', padding: '2px 6px' }}
                              >
                                🗑️ Delete
                              </button>
                            </div>
                          </div>

                          {/* Editable Question Text */}
                          <div className="form-group">
                            <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)' }}>Question Text:</label>
                            <textarea 
                              className="form-input" 
                              rows={2} 
                              value={q.text} 
                              onChange={(e) => {
                                const val = e.target.value;
                                setPreviewQuestions(prev => {
                                  const next = [...prev];
                                  next[idx] = { ...next[idx], text: val };
                                  return next;
                                });
                              }}
                              style={{ fontSize: '11px' }}
                            />
                          </div>

                          {/* Editable Model Answer */}
                          <div className="form-group">
                            <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)' }}>Model Answer:</label>
                            <textarea 
                              className="form-input" 
                              rows={3} 
                              value={q.solution} 
                              onChange={(e) => {
                                const val = e.target.value;
                                setPreviewQuestions(prev => {
                                  const next = [...prev];
                                  next[idx] = { ...next[idx], solution: val };
                                  return next;
                                });
                              }}
                              style={{ fontSize: '11px' }}
                            />
                          </div>

                          {/* Editable Keywords with Smooth Unbound Text State */}
                          <div className="form-group">
                            <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--accent)' }}>🏷️ Key Words / Phrases (Comma Separated):</label>
                            <input 
                              type="text" 
                              className="form-input" 
                              value={q.keywordsText ?? (Array.isArray(q.keywords) ? q.keywords.join(', ') : '')} 
                              onChange={(e) => {
                                const val = e.target.value;
                                const kwArr = val.split(',').map(s => s.trim()).filter(Boolean);
                                setPreviewQuestions(prev => {
                                  const next = [...prev];
                                  next[idx] = { ...next[idx], keywordsText: val, keywords: kwArr };
                                  return next;
                                });
                              }}
                              style={{ fontSize: '11px' }}
                            />
                          </div>

                          {/* Textbook Practice Set Reference (For Math) */}
                          {selectedSubjects.some(subj => /math|algebra|geometry|ganit/i.test(subj)) && (
                            <div className="form-group">
                              <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--accent)' }}>📖 Textbook Practice Set Reference (Optional):</label>
                              <input 
                                type="text" 
                                className="form-input" 
                                value={q.textbookPracticeSet || ''} 
                                onChange={(e) => {
                                  const val = e.target.value;
                                  setPreviewQuestions(prev => {
                                    const next = [...prev];
                                    next[idx] = { ...next[idx], textbookPracticeSet: val };
                                    return next;
                                  });
                                }}
                                placeholder="e.g. Practice Set 1.2: Q1 to Q5"
                                style={{ fontSize: '11px' }}
                              />
                            </div>
                          )}

                          {/* Live Standard KaTeX Highlight Preview */}
                          <div className="math-container" style={{ background: 'var(--surface)', padding: '8px 12px', borderRadius: '4px', border: '1px solid var(--border-light)', fontSize: '11px', lineHeight: 1.5, whiteSpace: 'pre-line' }}>
                            <strong style={{ color: '#065f46', fontSize: '10px', display: 'block', marginBottom: '2px' }}>💡 Live KaTeX Model Answer Highlight Preview:</strong>
                            <div 
                              dangerouslySetInnerHTML={{ 
                                __html: preprocessMathText(highlightModelAnswerKeywords(q.solution, q.keywords)) 
                              }} 
                            />
                          </div>
                        </div>
                      ))}
                    </div>

                    <button 
                      className="btn btn-primary"
                      onClick={handleSaveValidatedQuestions}
                      disabled={qbSaving}
                      style={{ padding: '10px', fontSize: '12px', fontWeight: 800, marginTop: '8px' }}
                    >
                      {qbSaving ? '⏳ Saving Validated Questions...' : `💾 Save ${previewQuestions.length} Validated Questions to Question Bank`}
                    </button>
                  </div>
                )}
              </div>

            </div>
          )}

          {testType === 'weekly' && (
            <div style={{ border: '2px solid var(--accent)', borderRadius: 'var(--radius)', padding: '16px', background: 'var(--surface)', display: 'flex', flexDirection: 'column', gap: '12px', marginTop: '10px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                <div>
                  <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 800, color: 'var(--accent)' }}>
                    🎓 PYQ Subjective Question Generator & Review Workspace
                  </h4>
                  <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>
                    Generate Previous Year Questions (PYQs) prompt, paste response below, parse & review questions before saving to Question Bank.
                  </div>
                </div>
                <button 
                  className="btn btn-secondary btn-sm"
                  onClick={handleGeneratePYQPrompt}
                  style={{ fontSize: '11px', fontWeight: 700, padding: '6px 14px', background: '#7c3aed', color: '#fff', border: 'none' }}
                >
                  🔧 Generate & Copy PYQ Prompt
                </button>
              </div>

              {/* Status Banner with Anchor ID */}
              {qbStatus && (
                <div 
                  id="qb-status-banner"
                  style={{ padding: '8px 12px', background: qbStatus.startsWith('❌') ? '#fef2f2' : '#f0fdf4', border: `1px solid ${qbStatus.startsWith('❌') ? '#fca5a5' : '#bbf7d0'}`, borderRadius: '4px', fontSize: '11px', color: qbStatus.startsWith('❌') ? '#b91c1c' : '#166534', fontWeight: 600, whiteSpace: 'pre-line' }}
                >
                  {qbStatus}
                </div>
              )}

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '12px' }}>
                <div className="form-group">
                  <label style={{ fontSize: '11px', fontWeight: 700 }}>📋 Generated PYQ Prompt</label>
                  <textarea 
                    className="form-input" 
                    rows={5} 
                    value={qbPrompt} 
                    onChange={(e) => setQbPrompt(e.target.value)}
                    placeholder="Click 'Generate & Copy PYQ Prompt' above to populate prompt..."
                    style={{ fontSize: '11px', fontFamily: 'monospace' }}
                  />
                </div>

                <div className="form-group">
                  <label style={{ fontSize: '11px', fontWeight: 700 }}>📥 Paste AI Response (JSON)</label>
                  <textarea 
                    className="form-input" 
                    rows={5} 
                    value={qbPasteJson} 
                    onChange={(e) => setQbPasteJson(e.target.value)}
                    placeholder="Paste JSON array response from Gemini or ChatGPT here..."
                    style={{ fontSize: '11px', fontFamily: 'monospace' }}
                  />
                </div>
              </div>

              <button 
                className="btn btn-secondary btn-sm"
                onClick={handleParseQuestions}
                style={{ fontSize: '11px', fontWeight: 700, padding: '8px', background: 'var(--accent-grad)', color: '#fff', border: 'none' }}
              >
                📥 Parse JSON Questions
              </button>

              {/* Interactive Question Preview & Review Cards with Standard KaTeX Rendering */}
              {previewQuestions.length > 0 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginTop: '10px', borderTop: '1px dashed var(--border-light)', paddingTop: '14px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 800, color: 'var(--accent)' }}>
                      🔍 Review & Edit Parsed Questions ({previewQuestions.length} Qs)
                    </h4>
                    <button 
                      className="btn btn-secondary btn-sm"
                      onClick={() => setPreviewQuestions([])}
                      style={{ fontSize: '10px', padding: '2px 8px' }}
                    >
                      ✕ Clear Preview
                    </button>
                  </div>

                  <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', maxHeight: '450px', overflowY: 'auto' }}>
                    {previewQuestions.map((q, idx) => (
                      <div key={idx} className="math-container" style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', padding: '12px', background: 'var(--bg-soft)', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '11px' }}>
                          <span style={{ fontWeight: 800, color: 'var(--accent)' }}>
                            Q{idx + 1} • Topic: {q.topicName || 'General'}
                          </span>
                          <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                            <span className="badge" style={{ background: 'var(--surface-3)', color: 'var(--text)', padding: '2px 8px', borderRadius: '4px', fontSize: '10px' }}>
                              {q.marks} Mark{q.marks > 1 ? 's' : ''} ({q.type})
                            </span>
                            <button 
                              className="btn btn-secondary btn-sm" 
                              onClick={() => setPreviewQuestions(prev => prev.filter((_, i) => i !== idx))}
                              style={{ background: '#fef2f2', color: '#b91c1c', border: '1px solid #fca5a5', fontSize: '10px', padding: '2px 6px' }}
                            >
                              🗑️ Delete
                            </button>
                          </div>
                        </div>

                        {/* Editable Question Text */}
                        <div className="form-group">
                          <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)' }}>Question Text:</label>
                          <textarea 
                            className="form-input" 
                            rows={2} 
                            value={q.text} 
                            onChange={(e) => {
                              const val = e.target.value;
                              setPreviewQuestions(prev => {
                                const next = [...prev];
                                next[idx] = { ...next[idx], text: val };
                                return next;
                              });
                            }}
                            style={{ fontSize: '11px' }}
                          />
                        </div>

                        {/* Editable Model Answer */}
                        <div className="form-group">
                          <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)' }}>Model Answer:</label>
                          <textarea 
                            className="form-input" 
                            rows={3} 
                            value={q.solution} 
                            onChange={(e) => {
                              const val = e.target.value;
                              setPreviewQuestions(prev => {
                                const next = [...prev];
                                next[idx] = { ...next[idx], solution: val };
                                return next;
                              });
                            }}
                            style={{ fontSize: '11px' }}
                          />
                        </div>

                        {/* Editable Keywords with Smooth Unbound Text State */}
                        <div className="form-group">
                          <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--accent)' }}>🏷️ Key Words / Phrases (Comma Separated):</label>
                          <input 
                            type="text" 
                            className="form-input" 
                            value={q.keywordsText ?? (Array.isArray(q.keywords) ? q.keywords.join(', ') : '')} 
                            onChange={(e) => {
                              const val = e.target.value;
                              const kwArr = val.split(',').map(s => s.trim()).filter(Boolean);
                              setPreviewQuestions(prev => {
                                const next = [...prev];
                                next[idx] = { ...next[idx], keywordsText: val, keywords: kwArr };
                                return next;
                              });
                            }}
                            style={{ fontSize: '11px' }}
                          />
                        </div>

                        {/* PYQ Info Reference */}
                        <div className="form-group">
                          <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--accent)' }}>🎓 PYQ Info / Board Year Reference (Optional):</label>
                          <input 
                            type="text" 
                            className="form-input" 
                            value={q.pyqInfo || ''} 
                            onChange={(e) => {
                              const val = e.target.value;
                              setPreviewQuestions(prev => {
                                const next = [...prev];
                                next[idx] = { ...next[idx], pyqInfo: val };
                                return next;
                              });
                            }}
                            placeholder="e.g. CBSE Board 2020 or PYQ Style Practice"
                            style={{ fontSize: '11px' }}
                          />
                        </div>

                        {/* Textbook Practice Set Reference (For Math) */}
                        {selectedSubjects.some(subj => /math|algebra|geometry|ganit/i.test(subj)) && (
                          <div className="form-group">
                            <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--accent)' }}>📖 Textbook Practice Set Reference (Optional):</label>
                            <input 
                              type="text" 
                              className="form-input" 
                              value={q.textbookPracticeSet || ''} 
                              onChange={(e) => {
                                const val = e.target.value;
                                setPreviewQuestions(prev => {
                                  const next = [...prev];
                                  next[idx] = { ...next[idx], textbookPracticeSet: val };
                                  return next;
                                });
                              }}
                              placeholder="e.g. Practice Set 1.2: Q1 to Q5"
                              style={{ fontSize: '11px' }}
                            />
                          </div>
                        )}

                        {/* Live Standard KaTeX Highlight Preview */}
                        <div className="math-container" style={{ background: 'var(--surface)', padding: '8px 12px', borderRadius: '4px', border: '1px solid var(--border-light)', fontSize: '11px', lineHeight: 1.5, whiteSpace: 'pre-line' }}>
                          <strong style={{ color: '#065f46', fontSize: '10px', display: 'block', marginBottom: '2px' }}>💡 Live KaTeX Model Answer Highlight Preview:</strong>
                          <div 
                            dangerouslySetInnerHTML={{ 
                              __html: preprocessMathText(highlightModelAnswerKeywords(q.solution, q.keywords)) 
                            }} 
                          />
                        </div>
                      </div>
                    ))}
                  </div>

                  <button 
                    className="btn btn-primary"
                    onClick={handleSaveValidatedQuestions}
                    disabled={qbSaving}
                    style={{ padding: '10px', fontSize: '12px', fontWeight: 800, marginTop: '8px' }}
                  >
                    {qbSaving ? '⏳ Saving Validated Questions...' : `💾 Save ${previewQuestions.length} Validated Questions to Question Bank`}
                  </button>
                </div>
              )}
            </div>
          )}

          {testType !== 'weekly' && (
            <button 
              className="btn btn-primary" 
              onClick={handleGenerate} 
              disabled={generating}
              style={{ width: '100%', padding: '12px', fontSize: '13px', fontWeight: 700 }}
            >
              {generating ? '🔧 Compiling Subjective Suite...' : (testType === 'weekly_suite' ? '⚡ Generate 1-Click Weekly Suite' : '🔧 Generate Classroom Test')}
            </button>
          )}
        </div>

        {/* Error Container */}
        {errorMsg && (
          <div className="card" style={{ background: '#fef2f2', border: '1px solid #fca5a5', padding: '16px 20px', borderRadius: 'var(--radius)', color: '#b91c1c' }}>
            <h3 style={{ fontSize: '13px', fontWeight: 800, margin: 0 }}>❌ Generation Failed</h3>
            <p style={{ fontSize: '12px', margin: '4px 0 0' }}>{errorMsg}</p>
          </div>
        )}

        {/* Results Container */}
        {result && (
          <div className="card" style={{ background: 'var(--surface)', padding: '24px', borderRadius: 'var(--radius-lg)', border: '2px solid var(--success)', display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px' }}>
              <h3 style={{ fontSize: '14px', fontWeight: 800, color: 'var(--success)', margin: 0 }}>
                🎉 {result.isWeeklySuite ? 'Weekly Subjective Suite Compiled Successfully!' : 'Classroom Exam Created Successfully!'}
              </h3>
            </div>

            {result.isWeeklySuite ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                <div style={{ fontSize: '13px', display: 'flex', flexWrap: 'wrap', gap: '15px', alignItems: 'center' }}>
                  <div><strong>📖 Chapter:</strong> {result.chapterName}</div>
                  <div><strong>📅 Daily Release Window:</strong> 08:30 PM – 10:30 PM</div>
                  <div><strong>📄 Daily Tests:</strong> {result.dailyTests?.length || 0} Days</div>
                </div>

                {/* Explicit Batch Assignment Controls */}
                <div style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius)', padding: '12px 16px', background: 'var(--bg-soft)', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text)' }}>
                    📦 Manual Batch Assignment Control:
                  </div>
                  {assignedStatusMsg ? (
                    <div style={{ fontSize: '12px', fontWeight: 800, color: 'var(--success)' }}>{assignedStatusMsg}</div>
                  ) : (
                    <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                      Status: 🟡 Draft / Unassigned (Not visible on student dashboards until assigned below)
                    </div>
                  )}

                  <div style={{ display: 'flex', gap: '10px', alignItems: 'center', flexWrap: 'wrap', marginTop: '4px' }}>
                    <select 
                      className="form-input" 
                      style={{ maxWidth: '240px', fontSize: '12px' }}
                      value={assignBatchId}
                      onChange={(e) => setAssignBatchId(e.target.value)}
                    >
                      <option value="">Select Batch to Assign</option>
                      {batches.map(b => <option key={b.id} value={b.id}>{b.name}</option>)}
                    </select>

                    <button 
                      className="btn btn-primary btn-sm"
                      onClick={handleAssignSuiteToBatch}
                      disabled={!assignBatchId}
                      style={{ padding: '6px 14px', fontSize: '11px', fontWeight: 700 }}
                    >
                      📤 Assign Suite to Selected Batch
                    </button>
                  </div>
                </div>

                {/* Master PDF Download Button */}
                <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
                  <button className="btn btn-primary" onClick={handleExportMasterPDF} style={{ padding: '10px 16px', fontWeight: 700 }}>
                    📄 Download Master Printable PDF Suite (Mon–Sat Bundle)
                  </button>
                  <button className="btn btn-success" onClick={handlePrintPlanner} style={{ padding: '10px 16px', fontWeight: 700 }}>
                    🖨️ Print Weekly Topic Planner
                  </button>
                  <button className="btn btn-secondary" onClick={() => router.push('/admin/exams')}>
                    📋 View All Exams
                  </button>
                </div>

                {/* Grid preview of days */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '10px', marginTop: '10px' }}>
                  {result.dailyTests?.map((d: any) => (
                    <div key={d.dayName} className="math-container" style={{ border: '1px solid var(--border-light)', padding: '10px', borderRadius: '6px', background: 'var(--bg-soft)', fontSize: '11px' }}>
                      <div style={{ fontWeight: 800, color: 'var(--accent)' }}>📅 {d.dayName} ({d.date})</div>
                      <div><strong>Marks:</strong> {d.totalMarks} Marks ({d.totalQuestions} Qs)</div>
                      <div style={{ color: 'var(--text-muted)', fontSize: '10px', marginTop: '2px' }}>
                        {getTopicNamesForDisplay(d.topics || [], d.learningQuestions || d.questions).join(', ') || 'General Practice'}
                      </div>
                    </div>
                  ))}
                  {result.saturdayTest && (
                    <div className="math-container" style={{ border: '1px solid var(--success)', padding: '10px', borderRadius: '6px', background: 'rgba(16, 185, 129, 0.05)', fontSize: '11px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                      <div>
                        <div style={{ fontWeight: 800, color: 'var(--success)' }}>🏫 Saturday Classroom Test</div>
                        <div><strong>Marks:</strong> {result.saturdayTest.totalMarks} Marks ({result.saturdayTest.totalQuestions} Qs)</div>
                        <div style={{ color: 'var(--text-muted)', fontSize: '10px', marginTop: '2px' }}>Auto-sampled pool</div>
                      </div>
                      
                      {(() => {
                        const satAssign = assignments.find((a: any) => a.examId === result.saturdayTest.examId || a.examId === result.saturdayTest.id);
                        return (
                          <div style={{ marginTop: '8px' }}>
                            {satAssign ? (
                              <div style={{ background: 'var(--success-tint)', color: 'var(--success)', padding: '4px 8px', borderRadius: '4px', fontSize: '10px', fontWeight: 700, marginBottom: '6px' }}>
                                Active: {toISTString(satAssign.startAt).replace('T', ' ')} to {toISTString(satAssign.endAt).split('T')[1]}
                              </div>
                            ) : (
                              <div style={{ background: 'var(--warning-tint)', color: 'var(--warning)', padding: '4px 8px', borderRadius: '4px', fontSize: '10px', fontWeight: 700, marginBottom: '6px' }}>
                                Not Activated Yet (Pending Timing)
                              </div>
                            )}
                            <button 
                              className="btn btn-primary btn-sm"
                              style={{ width: '100%', fontSize: '10px', padding: '4px 0' }}
                              onClick={() => openSaturdayAssign(result.saturdayTest)}
                            >
                              ⚙️ {satAssign ? 'Modify Timing' : 'Set Saturday Timing & Activate'}
                            </button>
                          </div>
                        );
                      })()}
                    </div>
                  )}
                </div>
              </div>
            ) : (
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '20px' }}>
                <div style={{ flex: 1, minWidth: '240px', display: 'flex', flexDirection: 'column', gap: '10px', fontSize: '13px' }}>
                  <div><strong>📋 Exam Name:</strong> {result.examName}</div>
                  <div><strong>🆔 Exam ID:</strong> <code style={{ background: 'var(--bg-soft)', padding: '2px 6px', borderRadius: '3px' }}>{result.examId}</code></div>
                  <div><strong>📅 Type:</strong> {String(result.testType || '').toUpperCase()}</div>

                  <div style={{ display: 'flex', gap: '8px', marginTop: '15px' }}>
                    <button className="btn btn-secondary btn-sm" onClick={() => router.push('/admin/exams')}>📋 View All Exams</button>
                    <button className="btn btn-secondary btn-sm" onClick={() => router.push(`/admin/exams?assignSubj=${result.examId}`)}>📤 Assign</button>
                  </div>
                </div>
              </div>
            )}

          </div>
        )}
      </main>

      {/* SCHEDULED EXAMS MANAGER & DELETE MODAL */}
      {showManagerModal && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.6)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
          <div style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', width: '100%', maxWidth: '950px', maxHeight: '90vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-light)', overflow: 'hidden', boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.3)' }}>
            
            <div style={{ padding: '14px 20px', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--bg-soft)' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800, color: 'var(--text)' }}>
                📅 Scheduled Home Practices & Classroom Tests
              </h3>
              <button className="btn btn-secondary btn-sm" onClick={() => setShowManagerModal(false)}>✕ Close</button>
            </div>

            <div style={{ padding: '20px', overflowY: 'auto', flex: 1 }}>
              {loadingScheduled ? (
                <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
                  Loading scheduled exams...
                </div>
              ) : scheduledExamsList.length === 0 ? (
                <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>No scheduled exams found.</div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
                  {(() => {
                    // Helper to get week start/end date range
                    const getWeekRange = (dateStr: string) => {
                      if (!dateStr) return 'Unknown Week';
                      const parts = dateStr.split('-');
                      if (parts.length !== 3) return 'Unknown Week';
                      
                      const year = Number(parts[0]);
                      const month = Number(parts[1]) - 1;
                      const dayVal = Number(parts[2]);
                      
                      const tempDate = new Date(year, month, dayVal);
                      const dayOfWeek = tempDate.getDay();
                      
                      const mondayOffset = dayOfWeek === 0 ? -6 : 1 - dayOfWeek;
                      const monday = new Date(year, month, dayVal + mondayOffset);
                      const saturday = new Date(monday.getFullYear(), monday.getMonth(), monday.getDate() + 5);
                      
                      const fmt = (d: Date) => {
                        const m = d.toLocaleString('en-US', { month: 'short' });
                        return `${m} ${d.getDate()}, ${d.getFullYear()}`;
                      };
                      return `Week of ${fmt(monday)} – ${fmt(saturday)}`;
                    };

                    // Sort list by date ascending
                    const sortedExams = [...scheduledExamsList].sort((a: any, b: any) => {
                      return (a.scheduledDate || '').localeCompare(b.scheduledDate || '');
                    });

                    // Group by week
                    const groups: Record<string, any[]> = {};
                    sortedExams.forEach((exam: any) => {
                      const weekKey = getWeekRange(exam.scheduledDate);
                      if (!groups[weekKey]) groups[weekKey] = [];
                      groups[weekKey].push(exam);
                    });

                    const todayStr = getDateKeyIST();

                    const ongoingGroups: [string, any[]][] = [];
                    const completedGroups: [string, any[]][] = [];

                    Object.entries(groups).forEach(([weekRange, groupItems]) => {
                      const dates = groupItems.map((item: any) => item.scheduledDate || '');
                      const maxDate = dates.reduce((a: string, b: string) => a > b ? a : b, '');
                      if (maxDate >= todayStr) {
                        ongoingGroups.push([weekRange, groupItems]);
                      } else {
                        completedGroups.push([weekRange, groupItems]);
                      }
                    });

                    const renderGroup = ([weekRange, groupItems]: [string, any[]]) => {
                      const allGroupIds = groupItems.map((item: any) => item.id);
                      const dailyTests = groupItems.filter((item: any) => item.type === 'home_practice');
                      const saturdayTest = groupItems.find((item: any) => item.type === 'classroom_test');
                      const chapName = groupItems[0]?.chapterName || 'General';

                      return (
                        <div key={weekRange} style={{ border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', background: 'var(--bg-soft)', overflow: 'hidden', marginBottom: '16px' }}>
                          {/* Week Header */}
                          <div style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                              <span style={{ fontSize: '15px' }}>📅</span>
                              <strong style={{ fontSize: '13px', color: 'var(--text)' }}>{weekRange}</strong>
                              <span style={{ fontSize: '11px', color: 'var(--text-muted)', background: 'var(--bg-main)', padding: '2px 8px', borderRadius: '12px', fontWeight: 600 }}>
                                {groupItems.length} Tests
                              </span>
                            </div>
                            
                            <div style={{ display: 'flex', gap: '8px' }}>
                              <button 
                                className="btn btn-secondary btn-sm"
                                onClick={() => printPlannerForSuite(chapName, dailyTests, saturdayTest)}
                                style={{ fontSize: '11px', padding: '4px 10px', display: 'flex', alignItems: 'center', gap: '4px' }}
                              >
                                🖨️ Print Planner
                              </button>
                              <button 
                                className="btn btn-secondary btn-sm"
                                onClick={() => handleDeleteSuiteGroup(allGroupIds)}
                                style={{ background: '#fef2f2', color: '#b91c1c', border: '1px solid #fca5a5', fontSize: '11px', padding: '4px 10px' }}
                              >
                                🗑️ Delete Entire Week
                              </button>
                            </div>
                          </div>

                          {/* Tests Table */}
                          <div style={{ overflowX: 'auto', background: 'var(--surface)' }}>
                            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '12px' }}>
                              <thead>
                                <tr style={{ borderBottom: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text-muted)', fontWeight: 600 }}>
                                  <th style={{ padding: '10px 14px' }}>Date & Day</th>
                                  <th style={{ padding: '10px 14px' }}>Type</th>
                                  <th style={{ padding: '10px 14px' }}>Subject & Topics Covered</th>
                                  <th style={{ padding: '10px 14px' }}>Questions / Marks</th>
                                  <th style={{ padding: '10px 14px' }}>Saturday Status & Setup</th>
                                  <th style={{ padding: '10px 14px', textAlign: 'center' }}>Actions</th>
                                </tr>
                              </thead>
                              <tbody>
                                {groupItems.map((item: any) => {
                                  const dateParts = (item.scheduledDate || '').split('-');
                                  const dateLabel = dateParts.length === 3 ? `${dateParts[1]}/${dateParts[2]}` : item.scheduledDate || '';
                                  const dayLabel = item.dayName ? `(${item.dayName.substring(0, 3)})` : '';
                                  
                                  // Extract proper topics names
                                  const topicNames = Array.from(new Set(item.questions?.map((q: any) => q.topicName || q.topic).filter(Boolean)));
                                  const chapterNumLabel = item.chapterNumber ? `Ch ${item.chapterNumber}: ` : '';
                                  const topicsDisplay = topicNames.length > 0 ? topicNames.join(', ') : (item.chapterName || 'General Practice');

                                  const isSat = item.type === 'classroom_test';
                                  const satAssign = isSat ? assignments.find((a: any) => a.examId === item.id) : null;

                                  return (
                                    <tr key={item.id} style={{ borderBottom: '1px solid var(--border-light)' }}>
                                      {/* Date */}
                                      <td style={{ padding: '12px 14px', whiteSpace: 'nowrap', fontWeight: 600, color: 'var(--text)' }}>
                                        {dateLabel} {dayLabel}
                                      </td>
                                      
                                      {/* Type */}
                                      <td style={{ padding: '12px 14px' }}>
                                        {isSat ? (
                                          <span style={{ background: '#f5f3ff', color: '#7c3aed', padding: '2px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700, border: '1px solid #ddd6fe' }}>
                                            🏫 Classroom Test
                                          </span>
                                        ) : (
                                          <span style={{ background: '#eff6ff', color: '#2563eb', padding: '2px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700, border: '1px solid #bfdbfe' }}>
                                            🏠 Home Practice
                                          </span>
                                        )}
                                      </td>

                                      {/* Subject & Topics */}
                                      <td style={{ padding: '12px 14px', maxWidth: '300px' }}>
                                        <div style={{ fontWeight: 600, color: 'var(--text-muted)', fontSize: '11px', textTransform: 'uppercase' }}>
                                          {item.subject}
                                        </div>
                                        <div style={{ marginTop: '2px', fontSize: '11px', color: 'var(--text)', lineHeight: '1.4' }}>
                                          <strong>{chapterNumLabel}</strong>{topicsDisplay}
                                        </div>
                                      </td>

                                      {/* Qs / Marks */}
                                      <td style={{ padding: '12px 14px', whiteSpace: 'nowrap', color: 'var(--text-muted)' }}>
                                        <strong>{item.totalQuestions || 0}</strong> Qs / <strong>{item.totalMarks || 0}</strong> Marks
                                      </td>

                                      {/* Sat Timing status */}
                                      <td style={{ padding: '12px 14px' }}>
                                        {isSat ? (
                                          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', alignItems: 'flex-start' }}>
                                            {satAssign ? (
                                              <span style={{ background: 'var(--success-tint)', color: 'var(--success)', fontSize: '10px', padding: '2px 6px', borderRadius: '4px', fontWeight: 800 }}>
                                                Active: {toISTString(satAssign.startAt).replace('T', ' ')} to {toISTString(satAssign.endAt).split('T')[1]}
                                              </span>
                                            ) : (
                                              <span style={{ background: 'var(--warning-tint)', color: 'var(--warning)', fontSize: '10px', padding: '2px 6px', borderRadius: '4px', fontWeight: 800 }}>
                                                Pending Activation
                                              </span>
                                            )}
                                            <button 
                                              className="btn btn-primary btn-sm"
                                              style={{ padding: '2px 6px', fontSize: '10px', height: 'auto', lineHeight: 1 }}
                                              onClick={() => openSaturdayAssign(item)}
                                            >
                                              ⚙️ {satAssign ? 'Modify' : 'Activate'}
                                            </button>
                                          </div>
                                        ) : (
                                          <span style={{ color: 'var(--text-muted)', fontSize: '11px' }}>—</span>
                                        )}
                                      </td>

                                      {/* Actions */}
                                      <td style={{ padding: '12px 14px', textAlign: 'center' }}>
                                        <button
                                          onClick={() => handleDeleteSuiteGroup([item.id])}
                                          style={{ background: 'none', border: 'none', color: '#ef4444', cursor: 'pointer', fontSize: '14px', padding: '4px' }}
                                          title="Delete this test"
                                        >
                                          🗑️
                                        </button>
                                      </td>
                                    </tr>
                                  );
                                })}
                              </tbody>
                            </table>
                          </div>
                        </div>
                      );
                    };

                    return (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                        {/* Ongoing Weekly Suites */}
                        <div>
                          <h4 style={{ margin: '0 0 12px 0', fontSize: '13px', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.5px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <span>🚀 Ongoing Weekly Suites</span>
                            <span style={{ background: 'rgba(59, 130, 246, 0.12)', color: '#2563eb', padding: '2px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700 }}>
                              {ongoingGroups.length}
                            </span>
                          </h4>
                          {ongoingGroups.length === 0 ? (
                            <div style={{ padding: '20px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-lg)', border: '1px dashed var(--border-light)', color: 'var(--text-faint)', fontSize: '12px', textAlign: 'center' }}>
                              No ongoing weekly suites.
                            </div>
                          ) : (
                            ongoingGroups.map(renderGroup)
                          )}
                        </div>

                        {/* Completed Weekly Suites (Collapsible at bottom) */}
                        <div style={{ borderTop: '1px solid var(--border-light)', paddingTop: '20px', marginTop: '10px' }}>
                          <button
                            onClick={() => setIsCompletedSectionExpanded(!isCompletedSectionExpanded)}
                            style={{
                              width: '100%',
                              background: 'var(--bg-soft)',
                              border: '1px solid var(--border-light)',
                              borderRadius: 'var(--radius-md)',
                              padding: '10px 16px',
                              display: 'flex',
                              justifyContent: 'space-between',
                              alignItems: 'center',
                              cursor: 'pointer',
                              color: 'var(--text)',
                              fontSize: '12.5px',
                              fontWeight: 700,
                              outline: 'none',
                              textAlign: 'left'
                            }}
                          >
                            <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                              <span>✅ Completed Weekly Suites</span>
                              <span style={{ background: 'var(--border-light)', color: 'var(--text-muted)', padding: '2px 8px', borderRadius: '12px', fontSize: '10px', fontWeight: 700 }}>
                                {completedGroups.length}
                              </span>
                            </span>
                            <span style={{ color: 'var(--text-muted)', fontSize: '11px', fontWeight: 600 }}>
                              {isCompletedSectionExpanded ? 'Hide completed suites ▲' : 'Show completed suites ▼'}
                            </span>
                          </button>

                          {isCompletedSectionExpanded && (
                            <div style={{ marginTop: '16px' }}>
                              {completedGroups.length === 0 ? (
                                <div style={{ padding: '20px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-lg)', border: '1px dashed var(--border-light)', color: 'var(--text-faint)', fontSize: '12px', textAlign: 'center' }}>
                                  No completed weekly suites.
                                </div>
                              ) : (
                                completedGroups.map(renderGroup)
                              )}
                            </div>
                          )}
                        </div>
                      </div>
                    );
                  })()}
                </div>
              )}
            </div>


          </div>
        </div>
      )}

      {/* Bulk Save Progress Modal */}
      {qbSaving && saveStats.total > 0 && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.8)', zIndex: 20000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '16px' }}>
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', padding: '30px', maxWidth: '440px', width: '90%', textAlign: 'center', border: '1px solid var(--border-light)', margin: 'auto' }}>
            <h3 style={{ margin: '0 0 6px', color: 'var(--text)', fontSize: '16px', fontWeight: 800 }}>💾 Saving Questions to Question Bank...</h3>
            <p style={{ fontSize: '12px', color: 'var(--text-muted)', marginBottom: '18px' }}>
              Writing database records sequentially. Please do not close or refresh this tab.
            </p>
            <div style={{ width: '100%', height: '14px', borderRadius: '8px', background: 'var(--bg-soft)', overflow: 'hidden', border: '1px solid var(--border-light)' }}>
              <div style={{ height: '100%', width: `${Math.round((saveStats.current / saveStats.total) * 100)}%`, background: 'var(--accent)', borderRadius: '8px', transition: 'width 0.2s ease' }} />
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '10px', fontSize: '11px', color: 'var(--text-muted)', fontWeight: 700 }}>
              <span>Progress: {Math.round((saveStats.current / saveStats.total) * 100)}%</span>
              <span>{saveStats.current} / {saveStats.total} Saved</span>
            </div>
          </div>
        </div>
      )}
      {/* Saturday classroom test timing modal */}
      {saturdayAssignModal.show && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.6)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 10000, padding: '16px' }}>
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', width: '100%', maxWidth: '480px', border: '1px solid var(--border-light)', overflow: 'hidden', padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
            
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800, color: 'var(--accent)' }}>
                🏫 {saturdayAssignModal.assignmentId ? 'Modify Saturday Test Timing' : 'Set Saturday Test Timing & Activate'}
              </h3>
              <button style={{ background: 'none', border: 'none', cursor: 'pointer', fontSize: '16px', color: 'var(--text-muted)' }} onClick={() => setSaturdayAssignModal(prev => ({ ...prev, show: false }))}>✕</button>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <div>
                <strong style={{ fontSize: '11px', color: 'var(--text-muted)', textTransform: 'uppercase' }}>Exam Name:</strong>
                <div style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text)', marginTop: '2px' }}>{saturdayAssignModal.examName}</div>
              </div>

              <div className="form-group">
                <label style={{ fontSize: '11px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>Target Batch</label>
                <select 
                  className="form-input" 
                  value={saturdayAssignModal.batchId} 
                  onChange={(e) => setSaturdayAssignModal(prev => ({ ...prev, batchId: e.target.value }))}
                  disabled={!!saturdayAssignModal.assignmentId}
                >
                  <option value="">-- Select Batch --</option>
                  {batches.map(b => <option key={b.id} value={b.id}>{b.name}</option>)}
                </select>
              </div>

              <div className="form-group">
                <label style={{ fontSize: '11px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>Start Datetime (local)</label>
                <input 
                  type="datetime-local" 
                  className="form-input"
                  value={saturdayAssignModal.startAtStr}
                  onChange={(e) => setSaturdayAssignModal(prev => ({ ...prev, startAtStr: e.target.value }))}
                />
              </div>

              <div className="form-group">
                <label style={{ fontSize: '11px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>End Datetime (local)</label>
                <input 
                  type="datetime-local" 
                  className="form-input"
                  value={saturdayAssignModal.endAtStr}
                  onChange={(e) => setSaturdayAssignModal(prev => ({ ...prev, endAtStr: e.target.value }))}
                />
              </div>

              <div className="form-group">
                <label style={{ fontSize: '11px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>Exam Duration (minutes)</label>
                <input 
                  type="number" 
                  className="form-input"
                  min={5}
                  max={300}
                  value={saturdayAssignModal.examDuration}
                  onChange={(e) => {
                    const raw = e.target.value;
                    if (raw === '') {
                      setSaturdayAssignModal(prev => ({ ...prev, examDuration: '' as any }));
                    } else {
                      const val = parseInt(raw, 10);
                      setSaturdayAssignModal(prev => ({ ...prev, examDuration: isNaN(val) ? '' as any : Math.max(5, Math.min(300, val)) }));
                    }
                  }}
                  onBlur={() => {
                    if (!saturdayAssignModal.examDuration || Number(saturdayAssignModal.examDuration) < 5) {
                      setSaturdayAssignModal(prev => ({ ...prev, examDuration: 60 }));
                    }
                  }}
                />
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', borderTop: '1px solid var(--border-light)', paddingTop: '14px', marginTop: '4px' }}>
              <button className="btn btn-secondary btn-sm" onClick={() => setSaturdayAssignModal(prev => ({ ...prev, show: false }))}>Cancel</button>
              <button className="btn btn-primary btn-sm" onClick={handleSaveSaturdayAssignment}>
                {saturdayAssignModal.assignmentId ? 'Save Changes' : 'Activate Exam'}
              </button>
            </div>

          </div>
        </div>
      )}

    </div>
  );
}
