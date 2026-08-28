import { useState } from 'react';

export function useSyllabusSelector<T extends { topic: string; subject?: string; chapterNumber?: string | number }, S = any>({
  syllabusIndex,
  initialSelectedSubjects,
  emptySelectedSubjects
}: {
  syllabusIndex: any;
  initialSelectedSubjects: S;
  emptySelectedSubjects: S;
}) {
  const [selectedBoard, setSelectedBoard] = useState('');
  const [selectedClass, setSelectedClass] = useState('');
  const [availableSubjects, setAvailableSubjects] = useState<string[]>([]);
  const [selectedSubjects, setSelectedSubjects] = useState<S>(initialSelectedSubjects);
  
  const [availableChapters, setAvailableChapters] = useState<any[]>([]);
  const [selectedChapters, setSelectedChapters] = useState<Set<number>>(new Set());
  
  const [availableTopics, setAvailableTopics] = useState<T[]>([]);
  const [selectedTopics, setSelectedTopics] = useState<T[]>([]);

  const handleToggleChapter = (idx: number) => {
    const chItem = availableChapters[idx];
    if (!chItem) return;
    
    setSelectedChapters(prev => {
      const next = new Set(prev);
      const isChecking = !next.has(idx);
      if (isChecking) {
        next.add(idx);
      } else {
        next.delete(idx);
        // Remove downstream topics
        const chNum = String(chItem.chapterNumber);
        setSelectedTopics(prevTopics => prevTopics.filter(t => String(t.chapterNumber) !== chNum));
      }
      return next;
    });
  };

  const handleSelectAllChapters = () => {
    const allIdx = availableChapters.map((_, i) => i);
    setSelectedChapters(new Set(allIdx));
  };

  const handleDeselectAllChapters = () => {
    setSelectedChapters(new Set());
    setSelectedTopics([]);
  };

  const handleToggleTopic = (topicItem: T) => {
    if ((topicItem as any).hasSubtopics) return;
    setSelectedTopics(prev => {
      const exists = prev.some(t => t.topic === topicItem.topic && t.subject === topicItem.subject);
      if (exists) {
        return prev.filter(t => !(t.topic === topicItem.topic && t.subject === topicItem.subject));
      } else {
        return [...prev, topicItem];
      }
    });
  };

  const handleSelectAllTopics = (filteredTopics: T[]) => {
    setSelectedTopics(prev => {
      const copy = [...prev];
      filteredTopics.forEach(ft => {
        if ((ft as any).hasSubtopics) return;
        if (!copy.some(t => t.topic === ft.topic && t.subject === ft.subject)) {
          copy.push(ft);
        }
      });
      return copy;
    });
  };

  const handleDeselectAllTopics = (filteredTopics: T[]) => {
    setSelectedTopics(prev =>
      prev.filter(p => !filteredTopics.some(v => v.topic === p.topic && v.subject === p.subject))
    );
  };

  const handleToggleSubject = (subject: string) => {
    setSelectedSubjects(prev => {
      if (prev instanceof Set) {
        const next = new Set(prev);
        if (next.has(subject)) {
          next.delete(subject);
        } else {
          next.add(subject);
        }
        return next as unknown as S;
      } else {
        const next = { ...(prev as any) };
        if (next[subject]) {
          delete next[subject];
        } else {
          next[subject] = { selected: true, weightage: 100 };
        }
        return next as unknown as S;
      }
    });
  };

  const handleSelectAllSubjects = (subjects: string[]) => {
    setSelectedSubjects(prev => {
      if (prev instanceof Set) {
        return new Set(subjects) as unknown as S;
      } else {
        const next: any = {};
        subjects.forEach(s => {
          next[s] = { selected: true, weightage: 100 };
        });
        return next as unknown as S;
      }
    });
  };

  const handleDeselectAllSubjects = () => {
    setSelectedSubjects(prev => {
      if (prev instanceof Set) {
        return new Set() as unknown as S;
      } else {
        return {} as unknown as S;
      }
    });
  };

  const [classes, setClasses] = useState<string[]>([]);

  const handleBoardChange = (
    board: string,
    onBoardChange?: () => void
  ) => {
    setSelectedBoard(board);
    setSelectedClass('');
    setSelectedSubjects(emptySelectedSubjects);
    setAvailableChapters([]);
    setSelectedChapters(new Set());
    setAvailableTopics([]);
    setSelectedTopics([]);
    
    if (onBoardChange) onBoardChange();

    if (!board || !syllabusIndex || !syllabusIndex.subjects?.[board]) {
      setClasses([]);
      return;
    }
    const filteredClasses = Object.keys(syllabusIndex.subjects[board]).sort((a, b) => parseInt(a) - parseInt(b));
    setClasses(filteredClasses);
  };

  const handleClassChange = (
    cls: string,
    onClassChange?: () => void
  ) => {
    setSelectedClass(cls);
    setSelectedSubjects(emptySelectedSubjects);
    setAvailableChapters([]);
    setSelectedChapters(new Set());
    setAvailableTopics([]);
    setSelectedTopics([]);

    if (onClassChange) onClassChange();

    if (!selectedBoard || !cls || !syllabusIndex || !syllabusIndex.subjects?.[selectedBoard]?.[cls]) {
      setAvailableSubjects([]);
      return;
    }
    const filteredSubjects = Object.keys(syllabusIndex.subjects[selectedBoard][cls]).sort();
    setAvailableSubjects(filteredSubjects);
  };

  return {
    selectedBoard, setSelectedBoard,
    selectedClass, setSelectedClass,
    availableSubjects, setAvailableSubjects,
    selectedSubjects, setSelectedSubjects,
    availableChapters, setAvailableChapters,
    selectedChapters, setSelectedChapters,
    availableTopics, setAvailableTopics,
    selectedTopics, setSelectedTopics,
    classes, setClasses,
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
  };
}
