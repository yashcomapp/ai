'use client';

import React, { useEffect, useState, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import { useReports } from '@/hooks/useReports';
import { exportStudentMonthlyReportPDF } from '@/lib/pdfExport';
import { getScoreColor } from '@/lib/dashboardMetrics';

interface StudentLQ {
  id: string;
  name: string;
  studentCode?: string;
  email?: string;
  parentEmail?: string;
  batchName?: string;
  batchIds?: string[];
  overallQuotient: number | null;
  examScore: number;
  practiceScore: number;
  qualityScore: number;
  healthScore: number;
  integrityScore: number;
  obsScore: number;
  parentName?: string;
  parentMobile?: string;
}

export default function LearningQuotientReportPage() {
  const { firebaseUser, logout, user } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();
  const { 
    getQuotientReport, 
    saveQuotientParameter, 
    deleteQuotientParameter, 
    batchAwardObservations, 
    logSingleObservation 
  } = useReports();

  const [loading, setLoading] = useState(true);
  const [students, setStudents] = useState<StudentLQ[]>([]);
  const [batches, setBatches] = useState<{ id: string; name: string }[]>([]);
  const [parameters, setParameters] = useState<{ id: string; name: string }[]>([]);
  const [selectedBatchId, setSelectedBatchId] = useState<string>('all');

  // Sorting state
  const [sortField, setSortField] = useState<string>('overallQuotient');
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('desc');

  const handleSort = (field: string) => {
    if (sortField === field) {
      setSortDirection(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortField(field);
      setSortDirection('desc');
    }
  };

  const filteredStudents = useMemo(() => {
    return selectedBatchId === 'all'
      ? students
      : students.filter(s => s.batchIds?.includes(selectedBatchId));
  }, [students, selectedBatchId]);

  const sortedStudents = useMemo(() => {
    return [...filteredStudents].sort((a, b) => {
      let aVal: any = a[sortField as keyof StudentLQ];
      let bVal: any = b[sortField as keyof StudentLQ];

      if (aVal === null || aVal === undefined) return 1;
      if (bVal === null || bVal === undefined) return -1;

      if (typeof aVal === 'string' && typeof bVal === 'string') {
        aVal = aVal.toLowerCase();
        bVal = bVal.toLowerCase();
      }

      if (aVal < bVal) return sortDirection === 'asc' ? -1 : 1;
      if (aVal > bVal) return sortDirection === 'asc' ? 1 : -1;
      return 0;
    });
  }, [filteredStudents, sortField, sortDirection]);

  // Modal toggles
  const [showManageModal, setShowManageModal] = useState(false);
  const [showSingleModal, setShowSingleModal] = useState(false);
  
  // Selection and details state
  const [selectedCode, setSelectedCode] = useState('');
  const [quotientDetails, setQuotientDetails] = useState<any>(null);
  const [loadingDetails, setLoadingDetails] = useState(false);

  // Search & details modal state
  const [showSearchModal, setShowSearchModal] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [showDetailsModal, setShowDetailsModal] = useState(false);
  const [selectedStudentInfo, setSelectedStudentInfo] = useState<{ name: string; email?: string } | null>(null);
  
  // Parent & report state
  const [parentMobile, setParentMobile] = useState('');
  const [parentName, setParentName] = useState('');
  const [studentMobile, setStudentMobile] = useState('');
  const [commentsText, setCommentsText] = useState('');
  const [isCommentsEdited, setIsCommentsEdited] = useState(false);
  
  // Single Student rating modal state
  const [singleStudentCode, setSingleStudentCode] = useState('');
  const [singleStudentName, setSingleStudentName] = useState('');
  const [singleStudentScores, setSingleStudentScores] = useState<Record<string, number>>({});
  const [singleObsMsg, setSingleObsMsg] = useState('');
  const [singleLoading, setSingleLoading] = useState(false);

  // Bulk Observations Tab state
  const [manageTab, setManageTab] = useState<'bulk' | 'params'>('bulk');
  const [bulkBatchId, setBulkBatchId] = useState('all');
  const [bulkParamId, setBulkParamId] = useState('');
  const [bulkScore, setBulkScore] = useState(80);
  const [selectedStudentCodes, setSelectedStudentCodes] = useState<string[]>([]);
  const [bulkMsg, setBulkMsg] = useState('');
  const [bulkLoading, setBulkLoading] = useState(false);
  const [bulkAssignments, setBulkAssignments] = useState<Record<string, 'A' | 'B' | 'C' | 'D' | 'E'>>({});
  const [selectedStudents, setSelectedStudents] = useState<string[]>([]);

  // Manage Parameters Tab state
  const [newParamName, setNewParamName] = useState('');
  const [paramMsg, setParamMsg] = useState('');
  const [paramLoading, setParamLoading] = useState(false);

  // WhatsApp Broadcast Queue Wizard state
  const [showBroadcastModal, setShowBroadcastModal] = useState(false);
  const [broadcastQueue, setBroadcastQueue] = useState<any[]>([]);
  const [broadcastIndex, setBroadcastIndex] = useState(0);
  const [broadcastActiveDetails, setBroadcastActiveDetails] = useState<any>(null);
  const [loadingBroadcastDetails, setLoadingBroadcastDetails] = useState(false);
  const [duration, setDuration] = useState<string>('monthly');

  // Load initial student roster based on duration
  const loadRoster = async (selectedDuration: string = duration) => {
    setLoading(true);
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const resData = await getQuotientReport(idToken, undefined, selectedDuration);
      if (resData && resData.success) {
        setStudents(resData.students || []);
        setBatches(resData.batches || []);
        setParameters(resData.parameters || []);
      }
    } catch (e) {
      console.error('Error loading quotient roster:', e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadRoster(duration);
  }, [firebaseUser, duration]);

  const generateStudentComments = (studentInfo: any, details: any): string => {
    if (!details || !details.components) return '';

    const name = studentInfo?.name || 'The student';
    const examComp = details.components.find((c: any) => c.parameterId === 'exam') || { score: 0, details: {} };
    const practiceComp = details.components.find((c: any) => c.parameterId === 'practice') || { score: 0, details: {} };
    const healthComp = details.components.find((c: any) => c.parameterId === 'topicHealth') || { score: 0, details: {} };
    const integrityComp = details.components.find((c: any) => c.parameterId === 'integrity') || { score: 0, details: {} };
    const obsComp = details.components.find((c: any) => c.parameterId === 'observations') || { score: 0, details: {} };

    const sentences: string[] = [];

    // 1. Exam Performance comment
    if (examComp.score >= 85) {
      sentences.push(`${name} is demonstrating outstanding academic performance in exams, showing a deep conceptual understanding of the topics.`);
    } else if (examComp.score >= 60) {
      sentences.push(`${name} is performing steadily in assessments, but can achieve higher scores by focusing on minor conceptual gaps and thorough revision.`);
    } else {
      sentences.push(`${name}'s exam scores indicate that they need additional academic support and structured review to strengthen their fundamentals.`);
    }

    if (examComp.details?.absent > 0) {
      sentences.push(`Note that ${examComp.details.absent} missed test(s) have impacted their overall score mapping.`);
    }

    // 2. Practice Engagement comment
    const avgQuestions = practiceComp.details?.averageQuestionsPerTopic ?? 0;
    if (practiceComp.score >= 80) {
      if (avgQuestions > 0 && avgQuestions <= 15) {
        sentences.push(`Their self-practice habits are exemplary, mastering concepts quickly (avg ${avgQuestions} Qs/topic) with high efficiency.`);
      } else {
        sentences.push(`Their self-practice habits are exemplary, completing ${practiceComp.details?.totalQuestionsAttempted || 0} questions with high mastery efficiency.`);
      }
    } else if (practiceComp.score >= 60) {
      if (avgQuestions > 15) {
        sentences.push(`They are actively practicing, but solving too many questions (avg ${avgQuestions} Qs/topic) to achieve mastery. We recommend reading the textbook and reviewing concepts before taking tests.`);
      } else {
        sentences.push(`They are actively practicing (${practiceComp.details?.totalQuestionsAttempted || 0} questions), but need to focus on completing topics in fewer attempts.`);
      }
    } else {
      if (avgQuestions > 15) {
        sentences.push(`Practice engagement is high in volume, but has low efficiency (avg ${avgQuestions} Qs/topic) without achieving mastery. Reading the textbook and thorough concept revision is strongly recommended.`);
      } else {
        sentences.push(`Practice engagement is below expectations with only ${practiceComp.details?.totalQuestionsAttempted || 0} questions attempted; regular practice is highly recommended.`);
      }
    }

    // 3. Topic Health comment
    if (healthComp.score >= 80) {
      sentences.push(`Their subject topic health is excellent, showing consistent mastery across assigned coursework.`);
    } else if (healthComp.details?.attentionCount > 0) {
      sentences.push(`Currently, there are ${healthComp.details.attentionCount} focus topic(s) requiring immediate attention and review to achieve complete mastery.`);
    } else {
      sentences.push(`Concept mastery is stable, but they should proactively review newly assigned chapters.`);
    }

    // 4. Proctoring Integrity comment
    if (integrityComp.score >= 90) {
      sentences.push(`They maintain high focus and integrity during online testing environments.`);
    } else if (integrityComp.score < 80) {
      sentences.push(`Some focus deviations (tab-switching) were observed during online tests; parental supervision is recommended.`);
    }

    // 5. Classroom Observations
    const obsParams = obsComp.details?.parameters || [];
    const sincerity = obsParams.find((p: any) => p.id === 'sincerity')?.average ?? 50;
    const participation = obsParams.find((p: any) => p.id === 'activeParticipation')?.average ?? 50;
    const timelyWork = obsParams.find((p: any) => p.id === 'timelyWork')?.average ?? 50;

    const classroomSentences: string[] = [];
    if (sincerity >= 80) classroomSentences.push('shows exemplary behavior');
    else if (sincerity < 50) classroomSentences.push('needs to improve classroom sincerity');

    if (participation >= 80) classroomSentences.push('is highly active in participation');
    else if (participation < 50) classroomSentences.push('needs encouragement to participate');

    if (timelyWork >= 80) classroomSentences.push('consistently submits work on time');
    else if (timelyWork < 50) classroomSentences.push('needs to submit assignments promptly');

    if (classroomSentences.length > 0) {
      sentences.push(`In the classroom, ${name} ` + classroomSentences.join(', ') + '.');
    }

    // Overall Tier advice
    const lq = details.overallQuotient ?? 0;
    if (lq >= 85) {
      sentences.push(`Overall, with a Learning Quotient (LQ) of ${lq}, ${name} exhibits excellent academic consistency and behavior.`);
    } else if (lq >= 60) {
      sentences.push(`Overall, with an LQ of ${lq}, ${name} shows solid potential and can reach the excellent tier with consistent effort.`);
    } else {
      sentences.push(`Overall, with an LQ of ${lq}, immediate parent-teacher alignment is advised to help ${name} focus on practice and revision.`);
    }

    return sentences.join(' ');
  };

  // Open student quotient details modal
  const handleOpenDetailsModal = async (student: StudentLQ) => {
    setSelectedCode(student.studentCode || '');
    setSelectedStudentInfo({ name: student.name, email: student.email });
    setLoadingDetails(true);
    setShowDetailsModal(true);
    setQuotientDetails(null);
    setParentMobile('');
    setParentName('');
    setStudentMobile('');
    setCommentsText('');
    setIsCommentsEdited(false);

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await getQuotientReport(idToken, student.studentCode);
      if (res && res.success) {
        setQuotientDetails(res.quotientData);
        setParentMobile(res.parentMobile || '');
        setParentName(res.parentName || '');
        setStudentMobile(res.studentMobile || '');
        
        const autoComments = generateStudentComments(
          { name: student.name, studentCode: student.studentCode, email: student.email },
          res.quotientData
        );
        setCommentsText(autoComments);
      }
    } catch (err) {
      console.error('Error fetching student LQ details:', err);
    } finally {
      setLoadingDetails(false);
    }
  };

  const [sharingLoading, setSharingLoading] = useState(false);

  const handleDownloadReportPdf = async () => {
    if (!quotientDetails) return;
    setSharingLoading(true);
    try {
      const exporter = await exportStudentMonthlyReportPDF({
        student: {
          name: selectedStudentInfo?.name || '',
          studentCode: selectedCode,
          batchName: students.find(s => s.studentCode === selectedCode)?.batchName || '',
          parentMobile,
          parentEmail: students.find(s => s.studentCode === selectedCode)?.parentEmail || '',
          email: selectedStudentInfo?.email || ''
        },
        quotientDetails,
        comments: commentsText
      });
      if (exporter) {
        await exporter.save();
      }
    } catch (e: any) {
      console.error('Error generating PDF:', e);
      alert(`Error exporting PDF: ${e.message}`);
    } finally {
      setSharingLoading(false);
    }
  };

  const handlePwaShare = async () => {
    if (!quotientDetails) return;
    setSharingLoading(true);
    try {
      const exporter = await exportStudentMonthlyReportPDF({
        student: {
          name: selectedStudentInfo?.name || '',
          studentCode: selectedCode,
          batchName: students.find(s => s.studentCode === selectedCode)?.batchName || '',
          parentMobile,
          parentEmail: students.find(s => s.studentCode === selectedCode)?.parentEmail || '',
          email: selectedStudentInfo?.email || ''
        },
        quotientDetails,
        comments: commentsText
      });
      if (!exporter) return;

      const blob = await exporter.getBlob();
      const file = new File([blob], `${(selectedStudentInfo?.name || 'Student').replace(/\s+/g, '_')}_Monthly_Report.pdf`, {
        type: 'application/pdf'
      });

      // Copy student's name to clipboard to easily paste in the WhatsApp search bar
      try {
        if (selectedStudentInfo?.name) {
          await navigator.clipboard.writeText(selectedStudentInfo.name).catch(() => {});
        }
      } catch (_) {}

      if (navigator.canShare && navigator.canShare({ files: [file] })) {
        await navigator.share({
          files: [file],
          title: `Monthly Review Report - ${selectedStudentInfo?.name}`,
          text: `Dear Parent, please find the attached Monthly Review Report for ${selectedStudentInfo?.name}.`
        });
      } else {
        alert('File sharing is not supported on this browser/environment. Downloading report instead.');
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${(selectedStudentInfo?.name || 'Student').replace(/\s+/g, '_')}_Monthly_Report.pdf`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
      }
    } catch (e: any) {
      console.error('Error sharing report:', e);
      alert(`Failed to share PDF: ${e.message}`);
    } finally {
      setSharingLoading(false);
    }
  };

  const handleWhatsAppDirectText = () => {
    if (!quotientDetails) return;
    const cleanPhone = parentMobile.replace(/\D/g, '');
    const phoneStr = cleanPhone.length === 10 ? '91' + cleanPhone : cleanPhone;
    
    const isWeekly = duration === 'weekly';
    const durationLabel = isWeekly ? 'Weekly' : 'Monthly';
    const reportPeriod = isWeekly 
      ? `this week, ending ${new Date().toLocaleDateString('en-IN', { day: 'numeric', month: 'long', year: 'numeric' })}`
      : new Date().toLocaleString('en-IN', { month: 'long', year: 'numeric' });
    
    const examComp = quotientDetails.components.find((c: any) => c.parameterId === 'exam') || { score: 0, details: {} };
    const practiceComp = quotientDetails.components.find((c: any) => c.parameterId === 'practice') || { score: 0, details: {} };
    const healthComp = quotientDetails.components.find((c: any) => c.parameterId === 'topicHealth') || { score: 0, details: {} };
    const integrityComp = quotientDetails.components.find((c: any) => c.parameterId === 'integrity') || { score: 0, details: {} };
    const obsComp = quotientDetails.components.find((c: any) => c.parameterId === 'observations') || { score: 0, details: {} };

    const activePart = obsComp.details?.parameters?.find((p: any) => p.id === 'activeParticipation')?.average ?? 50;
    const sincerity = obsComp.details?.parameters?.find((p: any) => p.id === 'sincerity')?.average ?? 50;
    const timelyWork = obsComp.details?.parameters?.find((p: any) => p.id === 'timelyWork')?.average ?? 50;

    const lq = quotientDetails.overallQuotient;
    const tierName = lq >= 85 ? 'Excellent Tier 🌟' : lq >= 60 ? 'Standard Tier 👍' : 'Needs Attention ⚠️';

    const message = `*📚 YASHCOM FOUNDATION 📚*
*🌟 ${durationLabel} Performance Review 🌟*
=========================
Dear Parent,

Here is the ${durationLabel} Performance & Learning Quotient (LQ) summary for *${selectedStudentInfo?.name || 'your child'}* for *${reportPeriod}*.

📈 *OVERALL ${durationLabel.toUpperCase()} LEARNING QUOTIENT (LQ)*
👉 *${lq} / 100* (${tierName})

📊 *PERFORMANCE PILLARS BREAKDOWN*
🎯 *1. Exam Performance:* *${examComp.score !== null ? examComp.score + '/100' : 'N/A'}*
   ${examComp.score !== null 
     ? `└ _Attendance: ${examComp.details?.attendanceRate ?? 100}%, Absent: ${examComp.details?.absent ?? 0} Tests_`
     : `└ _No exams completed in this period_`}
🏋️ *2. Practice Engagement (Efficiency):* *${practiceComp.score}/100*
   └ _Attempted: ${practiceComp.details?.totalQuestionsAttempted ?? 0} Qs, Topics: ${practiceComp.details?.topicsAttemptedCount ?? 0}, Avg Qs/Topic: ${practiceComp.details?.averageQuestionsPerTopic ?? 0}_
🩺 *3. Topic Health:* *${healthComp.score}/100*
   └ _Mastery Ratio: ${healthComp.details?.masteryRatio ?? 0}%, Attention Topics: ${healthComp.details?.attentionCount ?? 0}_
🛡️ *4. Proctoring Integrity:* *${integrityComp.score}/100*
   └ _Integrity Index: ${integrityComp.score}%, Avg Infractions: ${integrityComp.details?.averageWeeklyViolations ?? 0}/wk_
👥 *5. Classroom Observations:* *${obsComp.score !== null ? obsComp.score + '/100' : 'N/A'}*
   ${obsComp.score !== null
     ? `└ _Participation: ${activePart}%, Sincerity: ${sincerity}%, Work Submission: ${timelyWork}%_`
     : `└ _No observations logged in this period_`}

📝 *${isWeekly ? 'WEEKLY STUDY TIP' : "EDUCATOR'S DIAGNOSTIC FEEDBACK"}*
"${commentsText || 'Keep up the good effort!'}"

=========================
Thank you for your partnership in your child's learning journey!

_Yashcom Foundation_
_Empowering Conceptual Excellence_`;

    const encodedMessage = encodeURIComponent(message);
    const url = `https://api.whatsapp.com/send?phone=${phoneStr}&text=${encodedMessage}`;
    window.open(url, '_blank');
  };

  // Open single observation rating sliders
  const handleOpenSingleModal = async (student: StudentLQ) => {
    setSingleStudentCode(student.studentCode || '');
    setSingleStudentName(student.name);
    setSingleObsMsg('');
    setSingleLoading(true);
    setShowSingleModal(true);

    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await getQuotientReport(idToken, student.studentCode);
      if (res && res.success && res.quotientData) {
        const obsComponent = res.quotientData.components.find((c: any) => c.parameterId === 'observations');
        const initialScores: Record<string, number> = {};
        
        parameters.forEach(p => {
          const detail = obsComponent?.details?.parameters?.find((param: any) => param.id === p.id);
          initialScores[p.id] = detail ? detail.average : 50;
        });
        setSingleStudentScores(initialScores);
      } else {
        const initialScores: Record<string, number> = {};
        parameters.forEach(p => {
          initialScores[p.id] = 50;
        });
        setSingleStudentScores(initialScores);
      }
    } catch (err) {
      console.error(err);
      const initialScores: Record<string, number> = {};
      parameters.forEach(p => {
        initialScores[p.id] = 50;
      });
      setSingleStudentScores(initialScores);
    } finally {
      setSingleLoading(false);
    }
  };

  // Submit single student observation update
  const handleSubmitSingleObservation = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!firebaseUser || !singleStudentCode) return;

    setSingleLoading(true);
    setSingleObsMsg('');
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await logSingleObservation(idToken, singleStudentCode, singleStudentScores);
      if (res && res.success) {
        setSingleObsMsg('✅ Observations logged successfully!');
        loadRoster();
        setTimeout(() => setShowSingleModal(false), 800);
      } else {
        setSingleObsMsg('❌ Failed to log observations.');
      }
    } catch (err: any) {
      setSingleObsMsg(`❌ Error: ${err.message || 'Saving failed'}`);
    } finally {
      setSingleLoading(false);
    }
  };

  // Submit bulk parameters observations checklist log
  const handleSubmitBulkAward = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!firebaseUser || !bulkParamId) {
      setBulkMsg('⚠️ Please select a parameter.');
      return;
    }

    const batchStudents = bulkBatchId === 'all'
      ? students
      : students.filter(s => s.batchIds?.includes(bulkBatchId));
    
    const allAssigned = batchStudents.length > 0 && batchStudents.every(s => s.studentCode && bulkAssignments[s.studentCode]);
    if (!allAssigned) {
      setBulkMsg('⚠️ Please place all students into columns before saving.');
      return;
    }

    setBulkLoading(true);
    setBulkMsg('');
    try {
      const idToken = await firebaseUser.getIdToken();
      
      // Group students by category
      const colA: string[] = [];
      const colB: string[] = [];
      const colC: string[] = [];
      const colD: string[] = [];
      const colE: string[] = [];

      batchStudents.forEach(s => {
        const code = s.studentCode;
        if (!code) return;
        const cat = bulkAssignments[code];
        if (cat === 'A') colA.push(code);
        else if (cat === 'B') colB.push(code);
        else if (cat === 'C') colC.push(code);
        else if (cat === 'D') colD.push(code);
        else if (cat === 'E') colE.push(code);
      });

      const promises = [];
      if (colA.length > 0) promises.push(batchAwardObservations(idToken, { studentCodes: colA, parameterId: bulkParamId, score: 80 }));
      if (colB.length > 0) promises.push(batchAwardObservations(idToken, { studentCodes: colB, parameterId: bulkParamId, score: 60 }));
      if (colC.length > 0) promises.push(batchAwardObservations(idToken, { studentCodes: colC, parameterId: bulkParamId, score: 40 }));
      if (colD.length > 0) promises.push(batchAwardObservations(idToken, { studentCodes: colD, parameterId: bulkParamId, score: 20 }));
      if (colE.length > 0) promises.push(batchAwardObservations(idToken, { studentCodes: colE, parameterId: bulkParamId, score: 0 }));

      const results = await Promise.all(promises);
      const failed = results.some(r => !r || !r.success);

      if (!failed) {
        setBulkMsg('✅ Observations bulk logged successfully!');
        setBulkAssignments({});
        setSelectedStudents([]);
        loadRoster();
      } else {
        setBulkMsg('❌ Failed to save some bulk observations.');
      }
    } catch (err: any) {
      setBulkMsg(`❌ Error: ${err.message || 'Operation failed'}`);
    } finally {
      setBulkLoading(false);
    }
  };

  // Add Dynamic parameter CRUD action
  const handleAddParameter = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!firebaseUser || !newParamName.trim()) return;

    setParamLoading(true);
    setParamMsg('');
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await saveQuotientParameter(idToken, newParamName);
      if (res && res.success) {
        setParamMsg('✅ Parameter added successfully!');
        setNewParamName('');
        const refreshData = await getQuotientReport(idToken);
        if (refreshData && refreshData.success) {
          setParameters(refreshData.parameters || []);
        }
      } else {
        setParamMsg('❌ Failed to add parameter.');
      }
    } catch (err: any) {
      setParamMsg(`❌ Error: ${err.message || 'Save failed'}`);
    } finally {
      setParamLoading(false);
    }
  };

  // Delete Dynamic parameter CRUD action
  const handleDeleteParameter = async (parameterId: string) => {
    if (!firebaseUser) return;
    if (!confirm('Are you sure you want to delete this observation parameter? Historical logs for this parameter will default to baseline.')) return;

    setParamLoading(true);
    setParamMsg('');
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await deleteQuotientParameter(idToken, parameterId);
      if (res && res.success) {
        setParamMsg('✅ Parameter deleted successfully!');
        const refreshData = await getQuotientReport(idToken);
        if (refreshData && refreshData.success) {
          setParameters(refreshData.parameters || []);
        }
      } else {
        setParamMsg('❌ Failed to delete parameter.');
      }
    } catch (err: any) {
      setParamMsg(`❌ Error: ${err.message || 'Delete failed'}`);
    } finally {
      setParamLoading(false);
    }
  };

  const loadQueueStudentDetails = async (index: number, queue: any[]) => {
    if (!firebaseUser || index >= queue.length) return;
    setLoadingBroadcastDetails(true);
    setBroadcastActiveDetails(null);
    try {
      const student = queue[index];
      const idToken = await firebaseUser.getIdToken();
      const res = await getQuotientReport(idToken, student.studentCode, duration);
      if (res && res.success) {
        setBroadcastActiveDetails(res.quotientData);
      }
    } catch (e) {
      console.error('Error loading queue student details:', e);
    } finally {
      setLoadingBroadcastDetails(false);
    }
  };

  const handleStartBroadcast = () => {
    const queue = filteredStudents
      .filter(s => s.parentMobile && s.parentMobile.trim().length > 0)
      .map(s => ({
        studentCode: s.studentCode || '',
        studentName: s.name,
        parentName: s.parentName || 'Parent',
        parentMobile: s.parentMobile || '',
        email: s.email || '',
        status: 'pending' as 'pending' | 'sent' | 'skipped'
      }));

    if (queue.length === 0) {
      alert('⚠️ No parents with valid mobile numbers found in this batch.');
      return;
    }

    setBroadcastQueue(queue);
    setBroadcastIndex(0);
    setShowBroadcastModal(true);
    loadQueueStudentDetails(0, queue);
  };

  const handleSendNextParent = () => {
    if (broadcastIndex >= broadcastQueue.length || !broadcastActiveDetails) return;

    const student = broadcastQueue[broadcastIndex];
    const cleanPhone = student.parentMobile.replace(/\D/g, '');
    const phoneStr = cleanPhone.length === 10 ? '91' + cleanPhone : cleanPhone;

    const isWeekly = duration === 'weekly';
    const durationLabel = isWeekly ? 'Weekly' : 'Monthly';
    const reportPeriod = isWeekly 
      ? `this week, ending ${new Date().toLocaleDateString('en-IN', { day: 'numeric', month: 'long', year: 'numeric' })}`
      : new Date().toLocaleString('en-IN', { month: 'long', year: 'numeric' });

    const examComp = broadcastActiveDetails.components.find((c: any) => c.parameterId === 'exam') || { score: 0, details: {} };
    const practiceComp = broadcastActiveDetails.components.find((c: any) => c.parameterId === 'practice') || { score: 0, details: {} };
    const healthComp = broadcastActiveDetails.components.find((c: any) => c.parameterId === 'topicHealth') || { score: 0, details: {} };
    const integrityComp = broadcastActiveDetails.components.find((c: any) => c.parameterId === 'integrity') || { score: 0, details: {} };
    const obsComp = broadcastActiveDetails.components.find((c: any) => c.parameterId === 'observations') || { score: 0, details: {} };

    const activePart = obsComp.details?.parameters?.find((p: any) => p.id === 'activeParticipation')?.average ?? 50;
    const sincerity = obsComp.details?.parameters?.find((p: any) => p.id === 'sincerity')?.average ?? 50;
    const timelyWork = obsComp.details?.parameters?.find((p: any) => p.id === 'timelyWork')?.average ?? 50;

    const lq = broadcastActiveDetails.overallQuotient;
    const tierName = lq >= 85 ? 'Excellent Tier 🌟' : lq >= 60 ? 'Standard Tier 👍' : 'Needs Attention ⚠️';

    const comments = generateStudentComments(
      { name: student.studentName, studentCode: student.studentCode, email: student.email },
      broadcastActiveDetails
    );

    const message = `*📚 YASHCOM FOUNDATION 📚*
*🌟 ${durationLabel} Performance Review 🌟*
=========================
Dear Parent,

Here is the ${durationLabel} Performance & Learning Quotient (LQ) summary for *${student.studentName}* for *${reportPeriod}*.

📈 *OVERALL ${durationLabel.toUpperCase()} LEARNING QUOTIENT (LQ)*
👉 *${lq} / 100* (${tierName})

📊 *PERFORMANCE PILLARS BREAKDOWN*
🎯 *1. Exam Performance:* *${examComp.score !== null ? examComp.score + '/100' : 'N/A'}*
   ${examComp.score !== null 
     ? `└ _Attendance: ${examComp.details?.attendanceRate ?? 100}%, Absent: ${examComp.details?.absent ?? 0} Tests_`
     : `└ _No exams completed in this period_`}
🏋️ *2. Practice Engagement (Efficiency):* *${practiceComp.score}/100*
   └ _Attempted: ${practiceComp.details?.totalQuestionsAttempted ?? 0} Qs, Topics: ${practiceComp.details?.topicsAttemptedCount ?? 0}, Avg Qs/Topic: ${practiceComp.details?.averageQuestionsPerTopic ?? 0}_
🩺 *3. Topic Health:* *${healthComp.score}/100*
   └ _Mastery Ratio: ${healthComp.details?.masteryRatio ?? 0}%, Attention Topics: ${healthComp.details?.attentionCount ?? 0}_
🛡️ *4. Proctoring Integrity:* *${integrityComp.score}/100*
   └ _Integrity Index: ${integrityComp.score}%, Avg Infractions: ${integrityComp.details?.averageWeeklyViolations ?? 0}/wk_
👥 *5. Classroom Observations:* *${obsComp.score !== null ? obsComp.score + '/100' : 'N/A'}*
   ${obsComp.score !== null
     ? `└ _Participation: ${activePart}%, Sincerity: ${sincerity}%, Work Submission: ${timelyWork}%_`
     : `└ _No observations logged in this period_`}

📝 *${isWeekly ? 'WEEKLY STUDY TIP' : "EDUCATOR'S DIAGNOSTIC FEEDBACK"}*
"${comments || 'Keep up the good effort!'}"

=========================
Thank you for your partnership in your child's learning journey!

_Yashcom Foundation_
_Empowering Conceptual Excellence_`;

    const encodedMessage = encodeURIComponent(message);
    const url = `https://api.whatsapp.com/send?phone=${phoneStr}&text=${encodedMessage}`;
    
    window.open(url, '_blank');

    const updatedQueue = [...broadcastQueue];
    updatedQueue[broadcastIndex].status = 'sent';
    setBroadcastQueue(updatedQueue);

    const nextIndex = broadcastIndex + 1;
    setBroadcastIndex(nextIndex);

    if (nextIndex < updatedQueue.length) {
      loadQueueStudentDetails(nextIndex, updatedQueue);
    }
  };

  const handleSkipCurrentParent = () => {
    if (broadcastIndex >= broadcastQueue.length) return;

    const updatedQueue = [...broadcastQueue];
    updatedQueue[broadcastIndex].status = 'skipped';
    setBroadcastQueue(updatedQueue);

    const nextIndex = broadcastIndex + 1;
    setBroadcastIndex(nextIndex);

    if (nextIndex < updatedQueue.length) {
      loadQueueStudentDetails(nextIndex, updatedQueue);
    }
  };

  const renderSortHeader = (label: string, field: string, align: 'left' | 'center' = 'center') => {
    const isSorted = sortField === field;
    return (
      <th 
        onClick={() => handleSort(field)} 
        style={{ 
          padding: '12px 8px', 
          cursor: 'pointer', 
          userSelect: 'none',
          textAlign: align,
          transition: 'color 0.2s ease',
          whiteSpace: 'nowrap'
        }}
      >
        <div style={{ display: 'inline-flex', alignItems: 'center', justifyContent: align === 'center' ? 'center' : 'flex-start', gap: '4px' }}>
          <span>{label}</span>
          <span style={{ fontSize: '10px', color: isSorted ? 'var(--accent)' : 'var(--text-muted)', opacity: isSorted ? 1 : 0.4 }}>
            {isSorted ? (sortDirection === 'asc' ? '▲' : '▼') : '⇅'}
          </span>
        </div>
      </th>
    );
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading Learning Quotient scorecard...
        </div>
      </div>
    );
  }



  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      
      {/* Page Header */}
      <div className="page-header glass" style={{ padding: '8px 12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderRadius: '0', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left" style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
          <span className="brand" style={{ fontWeight: 800, fontSize: '1.2rem', color: 'var(--accent)', cursor: 'pointer' }} onClick={() => router.push('/admin')}>YASHCOM</span>
          <nav style={{ display: 'flex', gap: '15px' }}>
            <span style={{ fontSize: '13px', fontWeight: 700, color: 'var(--accent)', borderBottom: '2px solid var(--accent)', paddingBottom: '4px' }}>Learning Quotient (LQ) 📊</span>
            <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-muted)', cursor: 'pointer' }} onClick={() => router.push('/admin/reports/parent-pending')}>Parent Sincerity 👨‍👩‍👧</span>
          </nav>
        </div>
        <div className="page-header-right" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span className="badge badge-info" id="usernameDisplay">{user?.name || 'Admin'}</span>
          
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </div>

      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1400px', width: '100%', margin: '0 auto' }}>
        
        {/* Top Controls Toolbar */}
        <div className="card glass" style={{ padding: '12px 16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '12px', marginBottom: '20px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'nowrap', maxWidth: '100%', overflowX: 'auto', paddingBottom: '2px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'nowrap', flexShrink: 0 }}>
              <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)' }}>Batch:</span>
              <select
                value={selectedBatchId}
                onChange={(e) => setSelectedBatchId(e.target.value)}
                style={{
                  padding: '6px 10px',
                  borderRadius: 'var(--radius-sm)',
                  border: '1px solid var(--border-light)',
                  background: 'var(--bg-soft)',
                  color: 'var(--text)',
                  fontSize: '11px',
                  fontWeight: 700,
                  cursor: 'pointer'
                }}
              >
                <option value="all">🌐 All Batches</option>
                {batches.map(b => (
                  <option key={b.id} value={b.id}>📦 {b.name}</option>
                ))}
              </select>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'nowrap', flexShrink: 0 }}>
              <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)' }}>Duration:</span>
              <select
                value={duration}
                onChange={(e) => setDuration(e.target.value)}
                style={{
                  padding: '6px 10px',
                  borderRadius: 'var(--radius-sm)',
                  border: '1px solid var(--border-light)',
                  background: 'var(--bg-soft)',
                  color: 'var(--text)',
                  fontSize: '11px',
                  fontWeight: 700,
                  cursor: 'pointer'
                }}
              >
                <option value="all">♾️ All Time</option>
                <option value="7d">📅 Last 7 Days</option>
                <option value="30d">📅 Last 30 Days</option>
                <option value="weekly">📅 Weekly LQ</option>
                <option value="monthly">📅 Monthly LQ</option>
                <option value="3m">📅 Last 3 Months</option>
                <option value="6m">📅 Last 6 Months</option>
              </select>
            </div>

            <button
              className="btn btn-secondary"
              onClick={() => {
                setShowSearchModal(true);
                setSearchQuery('');
              }}
              style={{ display: 'flex', alignItems: 'center', gap: '4px', fontSize: '11px', fontWeight: 700, padding: '6px 10px', height: '28px', flexShrink: 0 }}
            >
              🔍 Search
            </button>
            
            <div style={{ fontSize: '10.5px', color: 'var(--text-muted)', whiteSpace: 'nowrap', flexShrink: 0 }}>
              ({filteredStudents.length} students)
            </div>
          </div>

          <div style={{ display: 'flex', gap: '8px' }}>
            <button
              className="btn btn-secondary"
              onClick={handleStartBroadcast}
              style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px', fontWeight: 700, padding: '8px 16px', background: 'rgba(37, 211, 102, 0.1)', color: '#25D366', border: '1px solid rgba(37, 211, 102, 0.3)' }}
            >
              📱 WhatsApp Broadcast to Parents
            </button>
            <button 
              className="btn btn-primary"
              onClick={() => {
                setShowManageModal(true);
                setManageTab('bulk');
                setBulkMsg('');
                setSelectedStudentCodes([]);
                if (parameters.length > 0) {
                  setBulkParamId(parameters[0].id);
                }
              }}
              style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px', fontWeight: 700, padding: '8px 16px' }}
            >
              ⚙️ Bulk Award & Parameters
            </button>
          </div>
        </div>

        {/* Master Tabular Scores Spread Sheet */}
        <div className="card" style={{ background: 'var(--surface)', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflowX: 'auto' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
            <thead>
              <tr style={{ borderBottom: '2px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px', fontWeight: 700 }}>
                {renderSortHeader('Student', 'name', 'left')}
                {renderSortHeader('Exam (25%)', 'examScore')}
                {renderSortHeader('Practice (20%)', 'practiceScore')}
                {renderSortHeader('Quality (10%)', 'qualityScore')}
                {renderSortHeader('Topic Health (20%)', 'healthScore')}
                {renderSortHeader('Integrity (10%)', 'integrityScore')}
                {renderSortHeader('Obs (15%)', 'obsScore')}
                {renderSortHeader('LQ', 'overallQuotient')}
                <th style={{ padding: '12px 8px', textAlign: 'center', whiteSpace: 'nowrap' }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {sortedStudents.length === 0 ? (
                <tr>
                  <td colSpan={9} style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)', fontSize: '12px' }}>
                    No students mapped to this batch.
                  </td>
                </tr>
              ) : (
                sortedStudents.map(s => {
                  const hasScore = s.overallQuotient !== null;
                  return (
                    <tr key={s.id} style={{ borderBottom: '1px solid var(--border-light)', fontSize: '12px', transition: 'background 0.2s ease' }} className="table-row-hover">
                      <td style={{ padding: '12px 8px' }}>
                        <div 
                          style={{ fontWeight: 700, color: 'var(--text)', cursor: 'pointer', textDecoration: 'underline decoration-dotted' }}
                          onClick={() => handleOpenDetailsModal(s)}
                          title="Click to view LQ breakdown details"
                        >
                          {s.name}
                        </div>
                      </td>
                      <td style={{ padding: '12px 8px', textAlign: 'center' }}>
                        <span style={{ fontWeight: 700, color: getScoreColor(s.examScore) }}>{s.examScore}</span>
                      </td>
                      <td style={{ padding: '12px 8px', textAlign: 'center' }}>
                        <span style={{ fontWeight: 700, color: getScoreColor(s.practiceScore) }}>{s.practiceScore}</span>
                      </td>
                      <td style={{ padding: '12px 8px', textAlign: 'center' }}>
                        <span style={{ fontWeight: 700, color: getScoreColor(s.qualityScore) }}>{s.qualityScore}</span>
                      </td>
                      <td style={{ padding: '12px 8px', textAlign: 'center' }}>
                        <span style={{ fontWeight: 700, color: getScoreColor(s.healthScore) }}>{s.healthScore}</span>
                      </td>
                      <td style={{ padding: '12px 8px', textAlign: 'center' }}>
                        <span style={{ fontWeight: 700, color: getScoreColor(s.integrityScore) }}>{s.integrityScore}</span>
                      </td>
                      <td style={{ padding: '12px 8px', textAlign: 'center' }}>
                        <span style={{ fontWeight: 700, color: getScoreColor(s.obsScore) }}>{s.obsScore}</span>
                      </td>
                      <td style={{ padding: '12px 8px', textAlign: 'center' }}>
                        {hasScore ? (
                          <span 
                            style={{
                              fontSize: '13px',
                              fontWeight: 800,
                              padding: '4px 10px',
                              borderRadius: '12px',
                              background: `${getScoreColor(s.overallQuotient!)}15`,
                              color: getScoreColor(s.overallQuotient!),
                              border: `1px solid ${getScoreColor(s.overallQuotient!)}25`
                            }}
                          >
                            {s.overallQuotient}
                          </span>
                        ) : (
                          <span style={{ color: 'var(--text-muted)' }}>--</span>
                        )}
                      </td>
                      <td style={{ padding: '12px 8px', textAlign: 'center' }}>
                        <button
                          className="btn btn-secondary"
                          onClick={() => handleOpenSingleModal(s)}
                          style={{ padding: '4px 8px', fontSize: '11px', fontWeight: 700 }}
                        >
                          📝 Log Obs
                        </button>
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>
      </main>

      {/* Single Student Rating Modal */}
      {showSingleModal && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.5)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000, padding: '16px' }}>
          <div className="card glass" style={{ background: 'var(--surface)', maxWidth: '500px', width: '100%', padding: '24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '15px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800 }}>✍️ Log Classroom Observations</h3>
              <button onClick={() => setShowSingleModal(false)} style={{ background: 'transparent', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', fontSize: '1.2rem' }}>✕</button>
            </div>
            
            <div>
              <strong style={{ fontSize: '13px', color: 'var(--text)' }}>{singleStudentName}</strong>
              <div style={{ fontSize: '10px', color: 'var(--text-muted)' }}>Code: <code>{singleStudentCode}</code></div>
            </div>

            {singleLoading && Object.keys(singleStudentScores).length === 0 ? (
              <div style={{ textAlign: 'center', padding: '30px 0' }}>
                <div className="spinner" style={{ margin: '0 auto 10px auto' }}></div>
                <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Retrieving parameters...</span>
              </div>
            ) : (
              <form onSubmit={handleSubmitSingleObservation} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                <div style={{ maxHeight: '300px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '12px', paddingRight: '5px' }}>
                  {parameters.length === 0 ? (
                    <div style={{ fontSize: '11px', color: 'var(--text-muted)', textAlign: 'center', padding: '20px 0' }}>
                      No active observation parameters. Add parameters in settings first.
                    </div>
                  ) : (
                    parameters.map(p => (
                      <div key={p.id}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', fontWeight: 700, marginBottom: '4px' }}>
                          <span>{p.name}</span>
                          <span style={{ color: 'var(--accent)' }}>{singleStudentScores[p.id] ?? 50} / 100</span>
                        </div>
                        <input 
                          type="range" 
                          min="0" 
                          max="100" 
                          value={singleStudentScores[p.id] ?? 50}
                          onChange={(e) => {
                            setSingleStudentScores(prev => ({
                              ...prev,
                              [p.id]: Number(e.target.value)
                            }));
                          }}
                          style={{ width: '100%', accentColor: 'var(--accent)' }}
                        />
                      </div>
                    ))
                  )}
                </div>

                {singleObsMsg && (
                  <div style={{ fontSize: '11px', fontWeight: 700, color: singleObsMsg.includes('✅') ? 'var(--success)' : '#f43f5e' }}>
                    {singleObsMsg}
                  </div>
                )}

                <div style={{ display: 'flex', gap: '10px', marginTop: '10px' }}>
                  <button type="button" className="btn btn-secondary" onClick={() => setShowSingleModal(false)} style={{ flex: 1 }}>
                    Cancel
                  </button>
                  <button type="submit" className="btn btn-primary" disabled={singleLoading || parameters.length === 0} style={{ flex: 1 }}>
                    {singleLoading ? 'Saving...' : '💾 Save Observations'}
                  </button>
                </div>
              </form>
            )}
          </div>
        </div>
      )}

      {/* Manage Parameters & Bulk Award Modal */}
      {showManageModal && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.5)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000, padding: '16px' }}>
          <div className="card glass" style={{ background: 'var(--surface)', maxWidth: manageTab === 'bulk' ? '900px' : '650px', width: '100%', padding: '24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '15px', maxHeight: '90vh', transition: 'max-width 0.2s' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800 }}>⚙️ Bulk Award & Parameters Manager</h3>
              <button onClick={() => setShowManageModal(false)} style={{ background: 'transparent', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', fontSize: '1.2rem' }}>✕</button>
            </div>

            {/* Tab navigation */}
            <div style={{ display: 'flex', borderBottom: '1px solid var(--border-light)', gap: '15px' }}>
              <span 
                onClick={() => setManageTab('bulk')}
                style={{ fontSize: '13px', fontWeight: 700, paddingBottom: '8px', cursor: 'pointer', color: manageTab === 'bulk' ? 'var(--accent)' : 'var(--text-muted)', borderBottom: manageTab === 'bulk' ? '2px solid var(--accent)' : 'none' }}
              >
                👥 Bulk Observation Award
              </span>
              <span 
                onClick={() => setManageTab('params')}
                style={{ fontSize: '13px', fontWeight: 700, paddingBottom: '8px', cursor: 'pointer', color: manageTab === 'params' ? 'var(--accent)' : 'var(--text-muted)', borderBottom: manageTab === 'params' ? '2px solid var(--accent)' : 'none' }}
              >
                🛠️ Manage Parameters (CRUD)
              </span>
            </div>

            {/* Tab 1 Content: Bulk Award */}
            {manageTab === 'bulk' && (() => {
              const batchStudents = bulkBatchId === 'all'
                ? students
                : students.filter(s => s.batchIds?.includes(bulkBatchId));
              
              const unassignedStudents = batchStudents.filter(s => s.studentCode && !bulkAssignments[s.studentCode]);
              const allAssigned = batchStudents.length > 0 && batchStudents.every(s => s.studentCode && bulkAssignments[s.studentCode]);

              const handleDragStart = (e: React.DragEvent, studentCode: string) => {
                e.dataTransfer.setData('text/plain', studentCode);
              };

              return (
                <form onSubmit={handleSubmitBulkAward} style={{ display: 'flex', flexDirection: 'column', gap: '12px', overflow: 'hidden', flex: 1 }}>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '15px' }}>
                    <div>
                      <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, marginBottom: '4px', color: 'var(--text-muted)' }}>1. Select Batch:</label>
                      <select
                        value={bulkBatchId}
                        onChange={(e) => {
                          setBulkBatchId(e.target.value);
                          setBulkAssignments({});
                          setSelectedStudents([]);
                        }}
                        style={{ width: '100%', padding: '6px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '12px' }}
                      >
                        <option value="all">🌐 All Batches</option>
                        {batches.map(b => (
                          <option key={b.id} value={b.id}>{b.name}</option>
                        ))}
                      </select>
                    </div>
                    <div>
                      <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, marginBottom: '4px', color: 'var(--text-muted)' }}>2. Select Parameter:</label>
                      <select
                        value={bulkParamId}
                        onChange={(e) => setBulkParamId(e.target.value)}
                        style={{ width: '100%', padding: '6px 10px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '12px' }}
                      >
                        <option value="">-- Choose Parameter --</option>
                        {parameters.map(p => (
                          <option key={p.id} value={p.id}>{p.name}</option>
                        ))}
                      </select>
                    </div>
                  </div>

                  {/* Unassigned Students Pills */}
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                    <label style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', display: 'flex', justifyContent: 'space-between' }}>
                      <span>3. Unassigned Students:</span>
                      <span style={{ color: 'var(--accent)' }}>{unassignedStudents.length} remaining</span>
                    </label>
                    <div 
                      onDragOver={(e) => e.preventDefault()}
                      onDrop={(e) => {
                        e.preventDefault();
                        const studentCode = e.dataTransfer.getData('text/plain');
                        if (studentCode) {
                          const codesToMove = selectedStudents.includes(studentCode)
                            ? selectedStudents
                            : [studentCode];
                          setBulkAssignments(prev => {
                            const next = { ...prev };
                            codesToMove.forEach(code => {
                              delete next[code];
                            });
                            return next;
                          });
                          setSelectedStudents([]);
                        }
                      }}
                      style={{
                        border: '1px dashed var(--border-light)',
                        borderRadius: '4px',
                        padding: '10px',
                        background: 'var(--bg-soft)',
                        minHeight: '60px',
                        display: 'flex',
                        flexWrap: 'wrap',
                        gap: '6px',
                        alignItems: 'center',
                        maxHeight: '100px',
                        overflowY: 'auto'
                      }}
                    >
                      {unassignedStudents.length === 0 ? (
                        <span style={{ fontSize: '11px', color: 'var(--text-muted)', width: '100%', textAlign: 'center' }}>
                          🎉 All students placed! Drag to move or submit below.
                        </span>
                      ) : (
                        unassignedStudents.map(s => {
                          const isSelected = selectedStudents.includes(s.studentCode || '');
                          return (
                            <div
                              key={s.studentCode}
                              draggable
                              onDragStart={(e) => handleDragStart(e, s.studentCode!)}
                              onClick={(e) => {
                                e.stopPropagation();
                                const code = s.studentCode;
                                if (!code) return;
                                if (e.ctrlKey || e.metaKey) {
                                  setSelectedStudents(prev => {
                                    if (prev.includes(code)) return prev.filter(c => c !== code);
                                    return [...prev, code];
                                  });
                                } else {
                                  setSelectedStudents(prev => {
                                    if (prev.length === 1 && prev[0] === code) return [];
                                    return [code];
                                  });
                                }
                              }}
                              style={{
                                fontSize: '11px',
                                padding: '5px 10px',
                                background: isSelected ? 'var(--accent)' : 'var(--surface)',
                                color: isSelected ? '#ffffff' : 'var(--text)',
                                borderRadius: '12px',
                                border: isSelected ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                                cursor: 'grab',
                                userSelect: 'none',
                                transition: 'all 0.2s',
                                boxShadow: isSelected ? '0 0 8px var(--accent)' : 'none'
                              }}
                            >
                              {s.name}
                            </div>
                          );
                        })
                      )}
                    </div>
                    <span style={{ fontSize: '9px', color: 'var(--text-muted)', fontStyle: 'italic' }}>
                      💡 Drag & drop students into columns, or click student names (hold Ctrl/Cmd for multi-select) and click a column below.
                    </span>
                  </div>

                  {/* Category Placement Columns */}
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: '10px', marginTop: '10px', flex: 1, minHeight: '220px', overflowY: 'auto' }}>
                    {[
                      { key: 'A', name: 'A (Excellent)', score: 80, color: 'var(--success)' },
                      { key: 'B', name: 'B', score: 60, color: '#06b6d4' },
                      { key: 'C', name: 'C', score: 40, color: '#f59e0b' },
                      { key: 'D', name: 'D', score: 20, color: '#ea580c' },
                      { key: 'E', name: 'E', score: 0, color: 'var(--danger)' }
                    ].map(col => {
                      const colStudents = batchStudents.filter(s => s.studentCode && bulkAssignments[s.studentCode] === col.key);
                      return (
                        <div
                          key={col.key}
                          onDragOver={(e) => e.preventDefault()}
                          onDrop={(e) => {
                            e.preventDefault();
                            const studentCode = e.dataTransfer.getData('text/plain');
                            if (studentCode) {
                              const codesToMove = selectedStudents.includes(studentCode)
                                ? selectedStudents
                                : [studentCode];
                              setBulkAssignments(prev => {
                                const next = { ...prev };
                                codesToMove.forEach(code => {
                                  next[code] = col.key as any;
                                });
                                return next;
                              });
                              setSelectedStudents([]);
                            }
                          }}
                          onClick={() => {
                            if (selectedStudents.length > 0) {
                              setBulkAssignments(prev => {
                                const next = { ...prev };
                                selectedStudents.forEach(code => {
                                  next[code] = col.key as any;
                                });
                                return next;
                              });
                              setSelectedStudents([]);
                            }
                          }}
                          style={{
                            background: 'var(--bg-soft)',
                            borderRadius: 'var(--radius-md)',
                            border: selectedStudents.length > 0 ? '1px dashed var(--accent)' : `1px solid var(--border-light)`,
                            padding: '10px 6px',
                            minHeight: '200px',
                            display: 'flex',
                            flexDirection: 'column',
                            gap: '8px',
                            cursor: selectedStudents.length > 0 ? 'pointer' : 'default',
                            transition: 'border 0.2s, background 0.2s',
                            position: 'relative'
                          }}
                        >
                          <div style={{
                            fontSize: '10px',
                            fontWeight: 800,
                            textAlign: 'center',
                            paddingBottom: '6px',
                            borderBottom: `2px solid ${col.color}`,
                            color: col.color,
                            lineHeight: '1.2'
                          }}>
                            <div>{col.name}</div>
                            <div style={{ fontSize: '11px', marginTop: '2px' }}>{col.score}%</div>
                          </div>
                          
                          <div style={{
                            display: 'flex',
                            flexDirection: 'column',
                            gap: '4px',
                            flex: 1,
                            overflowY: 'auto',
                            padding: '4px 2px'
                          }}>
                            {colStudents.map(s => {
                              const isSelected = selectedStudents.includes(s.studentCode || '');
                              return (
                                <div
                                  key={s.studentCode}
                                  draggable
                                  onDragStart={(e) => handleDragStart(e, s.studentCode!)}
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    const code = s.studentCode;
                                    if (!code) return;
                                    if (e.ctrlKey || e.metaKey) {
                                      setSelectedStudents(prev => {
                                        if (prev.includes(code)) return prev.filter(c => c !== code);
                                        return [...prev, code];
                                      });
                                    } else {
                                      setSelectedStudents(prev => {
                                        if (prev.length === 1 && prev[0] === code) return [];
                                        return [code];
                                      });
                                    }
                                  }}
                                  style={{
                                    fontSize: '10px',
                                    padding: '4px 6px',
                                    background: isSelected ? 'var(--accent)' : 'var(--surface)',
                                    color: isSelected ? '#ffffff' : 'var(--text)',
                                    borderRadius: '6px',
                                    border: isSelected ? '1px solid var(--accent)' : '1px solid var(--border-light)',
                                    cursor: 'grab',
                                    textAlign: 'center',
                                    userSelect: 'none',
                                    wordBreak: 'break-word',
                                    boxShadow: 'var(--shadow-sm)'
                                  }}
                                >
                                  {s.name}
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      );
                    })}
                  </div>

                  {bulkMsg && (
                    <div style={{ fontSize: '11px', fontWeight: 700, color: bulkMsg.includes('✅') ? 'var(--success)' : '#f43f5e' }}>
                      {bulkMsg}
                    </div>
                  )}

                  <div style={{ display: 'flex', gap: '10px', marginTop: '5px', alignItems: 'center' }}>
                    <button type="button" className="btn btn-secondary" onClick={() => setShowManageModal(false)} style={{ flex: 1 }}>
                      Cancel
                    </button>
                    <button 
                      type="submit" 
                      className="btn btn-primary" 
                      disabled={bulkLoading || !allAssigned || !bulkParamId} 
                      style={{ flex: 2, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px' }}
                    >
                      {bulkLoading ? 'Saving...' : `💾 Save Observations (${Object.keys(bulkAssignments).length}/${batchStudents.length} Placed)`}
                    </button>
                  </div>
                </form>
              );
            })()}

            {/* Tab 2 Content: Manage Parameters (CRUD) */}
            {manageTab === 'params' && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '15px', overflow: 'hidden', flex: 1 }}>
                
                <form onSubmit={handleAddParameter} style={{ display: 'flex', gap: '10px', alignItems: 'end' }}>
                  <div style={{ flex: 1 }}>
                    <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, marginBottom: '4px', color: 'var(--text-muted)' }}>
                      ➕ Add Custom Parameter:
                    </label>
                    <input
                      type="text"
                      placeholder="e.g. Team Collaboration, Politeness"
                      value={newParamName}
                      onChange={(e) => setNewParamName(e.target.value)}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '12px' }}
                    />
                  </div>
                  <button type="submit" className="btn btn-primary" disabled={paramLoading || !newParamName.trim()} style={{ height: '38px', fontSize: '12px', fontWeight: 700 }}>
                    Add
                  </button>
                </form>

                <div style={{ flex: 1, display: 'flex', flexDirection: 'column', minHeight: '150px', overflow: 'hidden' }}>
                  <label style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '6px' }}>
                    📋 Active Observation Parameters:
                  </label>

                  <div style={{ flex: 1, overflowY: 'auto', border: '1px solid var(--border-light)', borderRadius: '4px', padding: '10px', background: 'var(--bg-soft)', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                    {parameters.map(p => {
                      const isDefault = ['activeParticipation', 'sincerity', 'timelyWork'].includes(p.id);
                      return (
                        <div key={p.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'var(--surface)', padding: '8px 12px', borderRadius: '4px', border: '1px solid var(--border-light)' }}>
                          <div>
                            <strong style={{ fontSize: '12px', color: 'var(--text)' }}>{p.name}</strong>
                            <div style={{ fontSize: '9px', color: 'var(--text-muted)' }}>slug: <code>{p.id}</code> {isDefault && <span style={{ color: 'var(--accent)', fontWeight: 700 }}> [System Default]</span>}</div>
                          </div>
                          {!isDefault && (
                            <button
                              type="button"
                              className="btn btn-secondary"
                              onClick={() => handleDeleteParameter(p.id)}
                              disabled={paramLoading}
                              style={{ padding: '4px 8px', fontSize: '10px', color: '#f43f5e', border: '1px solid #f43f5e25', background: '#f43f5e10' }}
                            >
                              🗑️ Delete
                            </button>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>

                {paramMsg && (
                  <div style={{ fontSize: '11px', fontWeight: 700, color: paramMsg.includes('✅') ? 'var(--success)' : '#f43f5e' }}>
                    {paramMsg}
                  </div>
                )}

                <div style={{ display: 'flex', justifyContent: 'end' }}>
                  <button type="button" className="btn btn-secondary" onClick={() => setShowManageModal(false)} style={{ width: '120px' }}>
                    Close
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      )}
      {/* Search Student Modal */}
      {showSearchModal && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.5)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000, padding: '16px' }}>
          <div className="card glass" style={{ background: 'var(--surface)', maxWidth: '500px', width: '100%', padding: '24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '15px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800 }}>🔍 Search Student</h3>
              <button onClick={() => setShowSearchModal(false)} style={{ background: 'transparent', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', fontSize: '1.2rem' }}>✕</button>
            </div>

            <div>
              <input
                type="text"
                placeholder="Type student name to search..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                autoFocus
                style={{
                  width: '100%',
                  padding: '10px 14px',
                  borderRadius: 'var(--radius-sm)',
                  border: '1px solid var(--border-light)',
                  background: 'var(--bg-soft)',
                  color: 'var(--text)',
                  fontSize: '13px',
                  marginBottom: '10px'
                }}
              />
            </div>

            <div style={{ maxHeight: '300px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '6px' }}>
              {students
                .filter(s => s.name.toLowerCase().includes(searchQuery.toLowerCase()))
                .slice(0, 15)
                .map(s => (
                  <div
                    key={s.id}
                    onClick={() => {
                      handleOpenDetailsModal(s);
                      setShowSearchModal(false);
                    }}
                    style={{
                      padding: '10px 12px',
                      borderRadius: '4px',
                      background: 'var(--bg-soft)',
                      cursor: 'pointer',
                      fontSize: '12px',
                      fontWeight: 600,
                      color: 'var(--text)',
                      transition: 'background 0.2s',
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center'
                    }}
                  >
                    <span>{s.name}</span>
                    <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>{s.batchName || 'No Batch'}</span>
                  </div>
                ))}
              {students.filter(s => s.name.toLowerCase().includes(searchQuery.toLowerCase())).length === 0 && (
                <div style={{ textAlign: 'center', padding: '20px 0', color: 'var(--text-muted)', fontSize: '11px' }}>
                  No students found matching "{searchQuery}"
                </div>
              )}
            </div>

            <div style={{ display: 'flex', justifyContent: 'end', marginTop: '5px' }}>
              <button type="button" className="btn btn-secondary" onClick={() => setShowSearchModal(false)} style={{ width: '100px' }}>
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Quotient Details Modal */}
      {showDetailsModal && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.5)', backdropFilter: 'blur(4px)', zIndex: 1000, padding: '16px' }}>
          <div className="card glass" style={{ background: 'var(--surface)', maxWidth: '700px', width: '100%', padding: '24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '15px', maxHeight: '90vh', overflowY: 'auto' }}>
            
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800 }}>📊 Student Monthly Performance Dossier</h3>
              <button onClick={() => setShowDetailsModal(false)} style={{ background: 'transparent', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', fontSize: '1.2rem' }}>✕</button>
            </div>
 
            {loadingDetails ? (
              <div style={{ textAlign: 'center', padding: '40px 0' }}>
                <div className="spinner" style={{ margin: '0 auto 15px auto' }}></div>
                <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Retrieving LQ breakdown details...</span>
              </div>
            ) : quotientDetails ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                
                {/* Header Summary */}
                <div style={{ display: 'flex', gap: '20px', alignItems: 'center', flexWrap: 'wrap', background: 'var(--bg-soft)', padding: '12px', borderRadius: 'var(--radius)' }}>
                  
                  {/* Radial indicator */}
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', position: 'relative', width: '80px', height: '80px', flexShrink: 0 }}>
                    <svg width="75" height="75" viewBox="0 0 120 120">
                      <circle cx="60" cy="60" r="50" fill="none" stroke="var(--border-light)" strokeWidth="10" />
                      <circle 
                        cx="60" 
                        cy="60" 
                        r="50" 
                        fill="none" 
                        stroke={getScoreColor(quotientDetails.overallQuotient)} 
                        strokeWidth="10" 
                        strokeDasharray="314.16"
                        strokeDashoffset={314.16 - (314.16 * quotientDetails.overallQuotient) / 100}
                        strokeLinecap="round"
                        transform="rotate(-90 60 60)"
                        style={{ transition: 'stroke-dashoffset 0.8s ease' }}
                      />
                    </svg>
                    <div style={{ position: 'absolute', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                      <span style={{ fontSize: '18px', fontWeight: 800, color: 'var(--text)' }}>{quotientDetails.overallQuotient}</span>
                      <span style={{ fontSize: '8px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>LQ</span>
                    </div>
                  </div>
 
                  <div>
                    <h4 style={{ fontSize: '15px', fontWeight: 800, margin: '0 0 6px 0', color: 'var(--text)' }}>{selectedStudentInfo?.name}</h4>
                    <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                      <span 
                        style={{
                          fontSize: '9px',
                          fontWeight: 700,
                          padding: '3px 6px',
                          borderRadius: '4px',
                          background: `${getScoreColor(quotientDetails.overallQuotient)}20`,
                          color: getScoreColor(quotientDetails.overallQuotient)
                        }}
                      >
                        {quotientDetails.overallQuotient >= 85 ? 'Excellent Tier 🌟' : quotientDetails.overallQuotient >= 60 ? 'Standard Tier 👍' : 'Needs Attention ⚠️'}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Parent Share Actions Settings Panel */}
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1.2fr', gap: '15px', background: 'var(--bg-soft)', padding: '14px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)' }}>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                    <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)' }}>👪 PARENT MOBILE (WHATSAPP):</label>
                    <input 
                      type="text" 
                      placeholder="e.g. 9876543210" 
                      value={parentMobile} 
                      onChange={(e) => setParentMobile(e.target.value)} 
                      style={{
                        padding: '8px 10px',
                        borderRadius: 'var(--radius-sm)',
                        border: '1px solid var(--border-light)',
                        background: 'var(--bg)',
                        color: 'var(--text)',
                        fontSize: '12px',
                        fontWeight: 600
                      }}
                    />
                    {parentName ? (
                      <span style={{ fontSize: '9.5px', color: 'var(--text-muted)' }}>
                        Parent: <strong>{parentName}</strong>
                      </span>
                    ) : (
                      <span style={{ fontSize: '9.5px', color: 'var(--text-muted)' }}>
                        Type contact number to prefill WhatsApp links
                      </span>
                    )}
                  </div>
                  
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                    <label style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)' }}>📝 EDIT DRAFT DIAGNOSTIC COMMENTARY:</label>
                    <textarea 
                      rows={3} 
                      value={commentsText} 
                      onChange={(e) => {
                        setCommentsText(e.target.value);
                        setIsCommentsEdited(true);
                      }} 
                      placeholder="Auto-generated commentary card content..." 
                      style={{
                        padding: '8px 10px',
                        borderRadius: 'var(--radius-sm)',
                        border: '1px solid var(--border-light)',
                        background: 'var(--bg)',
                        color: 'var(--text)',
                        fontSize: '10px',
                        lineHeight: '1.4',
                        resize: 'vertical',
                        fontFamily: 'inherit'
                      }}
                    />
                  </div>
                </div>
 
                {/* Metrics Progress bars */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                  <h4 style={{ fontSize: '11px', fontWeight: 700, margin: '0', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                    Metrics Contribution Breakdown
                  </h4>
 
                  {quotientDetails.components.map((comp: any) => (
                    <div key={comp.parameterId} style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px' }}>
                        <span style={{ fontWeight: 700, color: 'var(--text)', flex: 1 }}>{comp.parameterName}</span>
                        <span style={{ color: 'var(--text-muted)' }}>
                          Score: <strong style={{ color: getScoreColor(comp.score) }}>{comp.score}</strong> (Weight: {Math.round(comp.weight * 100)}%)
                        </span>
                      </div>
                      
                      <div style={{ width: '100%', height: '6px', background: 'var(--border-light)', borderRadius: '3px', overflow: 'hidden' }}>
                        <div 
                          style={{ 
                            width: `${comp.score}%`, 
                            height: '100%', 
                            background: getScoreColor(comp.score),
                            borderRadius: '3px',
                            transition: 'width 0.6s ease'
                          }} 
                        />
                      </div>
                      
                      <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '9.5px', color: 'var(--text-muted)' }}>
                        <span>
                          {comp.parameterId === 'exam' && `Attendance: ${comp.details.attendanceRate}%, Absent: ${comp.details.absent}`}
                          {comp.parameterId === 'practice' && `Attempted: ${comp.details.totalQuestionsAttempted} Qs, Topics: ${comp.details.topicsAttemptedCount}, Engagement: ${comp.details.engagementScore}%, Quality: ${comp.details.qualityScore}%`}
                          {comp.parameterId === 'topicHealth' && `Mastered: ${comp.details.masteryRatio}%, Attention: ${comp.details.attentionRatio}%`}
                          {comp.parameterId === 'integrity' && `Avg Infractions: ${comp.details.averageWeeklyViolations} / week`}
                          {comp.parameterId === 'observations' && `Logs: ${comp.details.observationCount} observations`}
                        </span>
                        <span style={{ fontWeight: 700, color: 'var(--text)' }}>
                          +{comp.contribution} LQ Points
                        </span>
                      </div>
                    </div>
                  ))}
                </div>
 
                {/* Action Buttons Footer */}
                <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', justifyContent: 'end', marginTop: '5px', borderTop: '1px solid var(--border-light)', paddingTop: '12px' }}>
                  <button
                    type="button"
                    className="btn btn-secondary"
                    onClick={() => {
                      setShowDetailsModal(false);
                      const sObj = students.find(s => s.studentCode === selectedCode);
                      if (sObj) handleOpenSingleModal(sObj);
                    }}
                    style={{ fontSize: '11px', fontWeight: 700, padding: '6px 10px' }}
                  >
                    📝 Log Obs
                  </button>
                  
                  <button
                    type="button"
                    className="btn btn-primary"
                    disabled={sharingLoading}
                    onClick={handleDownloadReportPdf}
                    style={{ fontSize: '11px', fontWeight: 700, padding: '6px 12px', background: 'var(--accent)' }}
                  >
                    📥 {sharingLoading ? 'Generating...' : 'Download PDF'}
                  </button>
                  
                  <button
                    type="button"
                    className="btn btn-primary"
                    disabled={sharingLoading}
                    onClick={handlePwaShare}
                    style={{ fontSize: '11px', fontWeight: 700, padding: '6px 12px', background: 'var(--success)' }}
                  >
                    🟢 {sharingLoading ? 'Sharing...' : 'PWA Share (PDF)'}
                  </button>
                  
                  <button
                    type="button"
                    className="btn btn-primary"
                    disabled={!parentMobile}
                    onClick={handleWhatsAppDirectText}
                    style={{ fontSize: '11px', fontWeight: 700, padding: '6px 12px', background: '#25D366', color: '#fff', borderColor: '#25D366' }}
                  >
                    💬 WhatsApp Msg
                  </button>
                  
                  <button type="button" className="btn btn-secondary" onClick={() => setShowDetailsModal(false)} style={{ width: '90px', fontSize: '11px', padding: '6px 10px' }}>
                    Close
                  </button>
                </div>

                {/* Helpful Tip about Mobile OS file sharing */}
                <div style={{ marginTop: '10px', padding: '10px 12px', background: 'rgba(52, 152, 219, 0.08)', borderRadius: '6px', border: '1px solid rgba(52, 152, 219, 0.2)', fontSize: '10.5px', color: 'var(--text-muted)', lineHeight: '1.4' }}>
                  💡 <strong>Tip on PWA Share (PDF):</strong> Due to mobile OS privacy sandboxing (Android/iOS), pre-selecting a contact is only supported for text links (like <strong>WhatsApp Msg</strong>), not binary file sharing. Clicking <strong>PWA Share</strong> automatically copies the student's name (<strong>{selectedStudentInfo?.name}</strong>) to your clipboard so you can instantly paste it into the WhatsApp search bar to find the parent.
                </div>
 
              </div>
            ) : (
              <div style={{ textAlign: 'center', padding: '20px 0', color: 'var(--text-muted)', fontSize: '12px' }}>
                Failed to resolve details.
              </div>
            )}
          </div>
        </div>
      )}

      {/* WhatsApp Broadcast Queue Wizard Modal */}
      {showBroadcastModal && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.5)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000, padding: '16px' }}>
          <div className="card glass" style={{ background: 'var(--surface)', maxWidth: '650px', width: '100%', padding: '24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '15px', maxHeight: '90vh' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800 }}>📱 WhatsApp Parent Broadcast Wizard</h3>
              <button onClick={() => setShowBroadcastModal(false)} style={{ background: 'transparent', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', fontSize: '1.2rem' }}>✕</button>
            </div>

            {/* Progress indicator */}
            <div style={{ background: 'var(--bg-soft)', padding: '12px 16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '12px', fontWeight: 700, marginBottom: '6px' }}>
                <span>Overall Progress</span>
                <span>{broadcastQueue.filter(q => q.status === 'sent').length} / {broadcastQueue.length} Sent</span>
              </div>
              <div style={{ width: '100%', height: '8px', background: 'var(--border-light)', borderRadius: '4px', overflow: 'hidden' }}>
                <div style={{ width: `${(broadcastQueue.filter(q => q.status === 'sent').length / broadcastQueue.length) * 100}%`, height: '100%', background: '#25D366', transition: 'width 0.3s ease' }}></div>
              </div>
            </div>

            {/* Current Target Student Box */}
            {broadcastIndex < broadcastQueue.length ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', flex: 1, overflowY: 'auto' }}>
                <div style={{ padding: '16px', borderRadius: 'var(--radius-md)', border: '1px solid rgba(37, 211, 102, 0.3)', background: 'rgba(37, 211, 102, 0.03)' }}>
                  <div style={{ fontSize: '11px', fontWeight: 700, color: '#25D366', textTransform: 'uppercase', marginBottom: '4px' }}>Now Preparing Message For:</div>
                  <div style={{ fontSize: '18px', fontWeight: 800, color: 'var(--text)' }}>{broadcastQueue[broadcastIndex].studentName}</div>
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '4px' }}>
                    Parent Contact: <strong>{broadcastQueue[broadcastIndex].parentMobile}</strong> ({broadcastQueue[broadcastIndex].parentName})
                  </div>
                </div>

                {loadingBroadcastDetails ? (
                  <div style={{ padding: '20px', textAlign: 'center', color: 'var(--text-muted)' }}>
                    <div className="spinner" style={{ margin: '0 auto 10px auto' }}></div>
                    Loading performance scores and generating comments...
                  </div>
                ) : broadcastActiveDetails ? (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                    <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)' }}>Message Preview Summary:</div>
                    <div style={{ fontSize: '11px', background: 'var(--bg-soft)', padding: '10px 14px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', maxHeight: '180px', overflowY: 'auto', whiteSpace: 'pre-wrap', fontFamily: 'monospace' }}>
                      Overall LQ: {broadcastActiveDetails.overallQuotient}/100
                      {"\n"}Exam: {broadcastActiveDetails.components.find((c: any) => c.parameterId === 'exam')?.score ?? 0}/100
                      {"\n"}Practice: {broadcastActiveDetails.components.find((c: any) => c.parameterId === 'practice')?.score ?? 0}/100
                      {"\n"}Comments: "{generateStudentComments(
                        { name: broadcastQueue[broadcastIndex].studentName, studentCode: broadcastQueue[broadcastIndex].studentCode, email: broadcastQueue[broadcastIndex].email },
                        broadcastActiveDetails
                      )}"
                    </div>
                  </div>
                ) : (
                  <div style={{ color: '#f43f5e', fontSize: '12px', textAlign: 'center', padding: '10px' }}>
                    ⚠️ Failed to load scores. You can still skip or attempt to send.
                  </div>
                )}

                <div style={{ display: 'flex', gap: '10px', marginTop: '10px' }}>
                  <button className="btn btn-secondary" style={{ flex: 1, height: '40px', fontWeight: 700 }} onClick={handleSkipCurrentParent}>
                    ⏭️ Skip
                  </button>
                  <button 
                    className="btn btn-primary" 
                    style={{ flex: 2, height: '40px', fontWeight: 700, background: '#25D366', borderColor: '#22c35e' }} 
                    onClick={handleSendNextParent}
                    disabled={loadingBroadcastDetails || !broadcastActiveDetails}
                  >
                    📱 Open WhatsApp & Next
                  </button>
                </div>
              </div>
            ) : (
              <div style={{ textAlign: 'center', padding: '30px 20px', display: 'flex', flexDirection: 'column', gap: '15px', alignItems: 'center' }}>
                <span style={{ fontSize: '3rem' }}>🎉</span>
                <h4 style={{ margin: 0, fontWeight: 800 }}>Broadcast Queue Completed!</h4>
                <p style={{ margin: 0, fontSize: '13px', color: 'var(--text-muted)' }}>All parent WhatsApp messages in the queue have been processed.</p>
                <button className="btn btn-primary" style={{ width: '120px', marginTop: '10px' }} onClick={() => setShowBroadcastModal(false)}>
                  Close
                </button>
              </div>
            )}

            {/* Queue List checklist */}
            <div style={{ borderTop: '1px solid var(--border-light)', paddingTop: '10px', display: 'flex', flexDirection: 'column', gap: '6px' }}>
              <div style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)' }}>Queue Sequence Details:</div>
              <div style={{ maxHeight: '120px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '4px', paddingRight: '4px' }}>
                {broadcastQueue.map((item, idx) => {
                  const isCurrent = idx === broadcastIndex;
                  return (
                    <div key={item.studentCode} style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', padding: '4px 8px', borderRadius: 'var(--radius-sm)', background: isCurrent ? 'rgba(37, 211, 102, 0.1)' : 'transparent', border: isCurrent ? '1px solid rgba(37, 211, 102, 0.2)' : 'none' }}>
                      <span style={{ fontWeight: isCurrent ? 700 : 500, color: isCurrent ? 'var(--text)' : 'var(--text-muted)' }}>
                        {idx + 1}. {item.studentName}
                      </span>
                      <span>
                        {item.status === 'sent' && <span style={{ color: '#25D366', fontWeight: 700 }}>✓ Sent</span>}
                        {item.status === 'skipped' && <span style={{ color: 'var(--text-muted)' }}>⏭️ Skipped</span>}
                        {item.status === 'pending' && idx > broadcastIndex && <span style={{ color: 'var(--text-muted)' }}>⏳ Waiting</span>}
                        {isCurrent && <span style={{ color: '#25D366', fontWeight: 700 }}>👉 Current</span>}
                      </span>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
