import { auth } from '@/lib/firebase/client';
import { KATEX_AUTO_RENDER_OPTIONS } from './questionTypes';
import { getScoreColor } from './dashboardMetrics';

async function getAuthHeaders(): Promise<Record<string, string>> {
  try {
    if (auth && auth.currentUser) {
      const token = await auth.currentUser.getIdToken();
      if (token) return { 'Authorization': `Bearer ${token}` };
    }
  } catch (e) {
    console.warn('PDF export getAuthHeaders error:', e);
  }
  return {};
}

export async function exportToPDF(params: {
  filename: string;
  title: string;
  sections: Array<{ id: string; name: string; checked: boolean; elementId: string }>;
}) {
  if (typeof window === 'undefined') return;
  const w = window as any;
  if (!w.html2pdf) {
    await new Promise<void>((resolve, reject) => {
      const s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
      s.onload = () => resolve();
      s.onerror = () => reject(new Error('Failed to load PDF library.'));
      document.head.appendChild(s);
    });
  }

  const printContainer = document.createElement('div');
  printContainer.id = 'pdf-print-container';
  printContainer.className = 'math-container';
  printContainer.style.cssText = 'font-family:Arial,sans-serif;background:#ffffff;color:#000000;padding:20px;';

  const styleOverride = document.createElement('style');
  styleOverride.innerHTML = `
    #pdf-print-container, #pdf-print-container *:not(.score-cell):not(.stat-val):not(.correct-option) {
      color: #000000 !important;
      text-shadow: none !important;
    }
    #pdf-print-container {
      background: #ffffff !important;
    }
    #pdf-print-container table {
      width: 100% !important;
      border-collapse: collapse !important;
      margin-bottom: 20px !important;
    }
    #pdf-print-container th {
      background: #f4f4f4 !important;
      color: #000000 !important;
      border: 1px solid #ddd !important;
      padding: 8px !important;
      font-size: 12px !important;
    }
    #pdf-print-container td {
      border: 1px solid #ddd !important;
      padding: 8px !important;
      font-size: 11px !important;
    }
  `;
  printContainer.appendChild(styleOverride);

  // Title Header block
  const titleHeader = document.createElement('div');
  titleHeader.innerHTML = `
    <div style="border-bottom: 2px solid #000000; padding-bottom: 8px; margin-bottom: 20px; text-align: center; font-family: system-ui, sans-serif;">
      <h2 style="margin: 0; color: #1aa54e; font-size: 20px; text-align: center;">${params.title}</h2>
      <div style="font-size: 11px; color: #555; margin-top: 4px; text-align: center;">
        Generated on: ${new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })}
      </div>
    </div>
  `;
  printContainer.appendChild(titleHeader);

  // Append chosen sections
  params.sections.forEach(sec => {
    if (!sec.checked) return;
    const el = document.getElementById(sec.elementId);
    if (el) {
      const clone = el.cloneNode(true) as HTMLElement;
      
      // Remove interactive elements
      clone.querySelectorAll('button, .btn, input[type="button"], input[type="submit"]').forEach(btn => {
        btn.remove();
      });
      // Replace check boxes with characters
      clone.querySelectorAll('input[type="checkbox"]').forEach(cb => {
        const inputCb = cb as HTMLInputElement;
        const span = document.createElement('span');
        span.innerHTML = inputCb.checked ? '☑ ' : '☐ ';
        inputCb.parentNode?.replaceChild(span, inputCb);
      });
      // Replace inputs with text
      clone.querySelectorAll('input[type="text"], input[type="number"], select').forEach(input => {
        const textInput = input as HTMLInputElement;
        const span = document.createElement('span');
        span.innerText = textInput.value || '';
        textInput.parentNode?.replaceChild(span, textInput);
      });

      const sectionWrapper = document.createElement('div');
      sectionWrapper.style.marginBottom = '25px';
      
      const sectionTitle = document.createElement('h3');
      sectionTitle.innerText = sec.name;
      sectionTitle.style.cssText = 'border-bottom: 1px solid #ddd; padding-bottom: 4px; margin-bottom: 12px; font-size: 14px; color: #333;';
      sectionWrapper.appendChild(sectionTitle);
      sectionWrapper.appendChild(clone);
      
      printContainer.appendChild(sectionWrapper);
    }
  });

  document.body.appendChild(printContainer);

  // Render Math Formulas with KaTeX if present
  if (w.renderMathInElement) {
    w.renderMathInElement(printContainer, KATEX_AUTO_RENDER_OPTIONS);
  }

  const opt = {
    margin:       [0.15, 0.3, 0.15, 0.3], // Minimal top & bottom margins
    filename:     params.filename,
    image:        { type: 'jpeg', quality: 0.98 },
    html2canvas:  { scale: 2, useCORS: true },
    jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
  };

  await w.html2pdf().from(printContainer).set(opt).save();
  document.body.removeChild(printContainer);
}

export async function exportSubjectiveExamDirectPdf(exam: any, questions: any[]) {
  if (typeof window === 'undefined') return;
  const w = window as any;
  if (!w.html2pdf) {
    await new Promise<void>((resolve, reject) => {
      const s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
      s.onload = () => resolve();
      s.onerror = () => reject(new Error('Failed to load PDF library.'));
      document.head.appendChild(s);
    });
  }

  const printContainer = document.createElement('div');
  printContainer.id = 'pdf-subjective-exam-container';
  printContainer.className = 'math-container';
  printContainer.style.cssText = 'font-family:Arial,sans-serif;background:#ffffff;color:#000000;padding:25px;';

  const styleOverride = document.createElement('style');
  styleOverride.innerHTML = `
    #pdf-subjective-exam-container, #pdf-subjective-exam-container * {
      color: #000000 !important;
      background: #ffffff !important;
      text-shadow: none !important;
    }
  `;
  printContainer.appendChild(styleOverride);

  // Render header
  const headerHtml = `
    <div style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 10px; margin-bottom: 20px;">
      <h1 style="margin: 0; font-size: 22px; font-weight: 800; letter-spacing: 0.5px;">Yashcom Foundation</h1>
      <h2 style="margin: 5px 0 0 0; font-size: 14px; font-weight: 600; color: #444; text-transform: uppercase;">Subjective Examination Paper</h2>
    </div>
    
    <table style="width: 100%; margin-bottom: 25px; font-size: 12px; border-collapse: collapse; border: none;">
      <tr>
        <td style="padding: 4px 0; border: none;"><strong>Exam Name:</strong> ${exam.name || 'Subjective Test'}</td>
        <td style="padding: 4px 0; border: none; text-align: right;"><strong>Class:</strong> Class ${exam.class || 'N/A'} (${exam.board || 'CBSE'})</td>
      </tr>
      <tr>
        <td style="padding: 4px 0; border: none;"><strong>Subject:</strong> ${exam.subject || 'N/A'}</td>
        <td style="padding: 4px 0; border: none; text-align: right;"><strong>Total Marks:</strong> ${exam.totalMarks || exam.maxMarks || 'N/A'} Marks</td>
      </tr>
    </table>
    
    <div style="margin-top: 20px;">
      ${questions.map((q: any, idx: number) => `
        <div style="margin-bottom: 20px; page-break-inside: avoid; border: 1px solid #ddd; border-radius: 4px; overflow: hidden;">
          <div style="background: #f5f5f5; padding: 8px 12px; font-size: 12px; font-weight: bold; border-bottom: 1px solid #ddd; display: flex; justify-content: space-between; align-items: center;">
            <span>Question ${idx + 1}</span>
            <span style="font-weight: normal; color: #666;">[${q.marks || 0} Marks]</span>
          </div>
          <div style="padding: 16px; font-size: 14px; line-height: 1.6; white-space: pre-line;">
            ${q.text}
          </div>
        </div>
      `).join('')}
    </div>
  `;
  
  const contentDiv = document.createElement('div');
  contentDiv.innerHTML = headerHtml;
  printContainer.appendChild(contentDiv);

  document.body.appendChild(printContainer);

  // Render Math Formulas with KaTeX if present
  if (w.renderMathInElement) {
    w.renderMathInElement(printContainer, KATEX_AUTO_RENDER_OPTIONS);
  }

  const opt = {
    margin:       [0.3, 0.4, 0.3, 0.4],
    filename:     `${(exam.name || 'Subjective_Exam').replace(/\s+/g, '_')}_Paper.pdf`,
    image:        { type: 'jpeg', quality: 0.98 },
    html2canvas:  { scale: 2, useCORS: true },
    jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
  };

  await w.html2pdf().from(printContainer).set(opt).save();
  document.body.removeChild(printContainer);
}

/**
 * Highlights important multi-word key phrases and domain concepts in model answer sentences.
 * Supports passing specific question keywords array.
 */
export function highlightModelAnswerKeywords(text: string, customKeywords?: string[]): string {
  if (!text) return '';

  // If the text contains HTML mark tags, convert them directly to our styled highlight spans
  if (/<mark[^>]*>.*?<\/mark>/gi.test(text)) {
    return text.replace(/<mark[^>]*>(.*?)<\/mark>/gi, (match, content) => {
      return `<span style="background-color: #fef08a; color: #713f12; font-weight: 700; border-radius: 2px; padding: 0 2px;">${content}</span>`;
    });
  }

  // Strip pre-existing <mark> or <span> HTML tags from text
  const rawText = text
    .replace(/<\/?mark[^>]*>/gi, '')
    .replace(/<span[^>]*style="[^"]*background[^"]*"[^>]*>(.*?)<\/span>/gi, '$1');

  // Clean raw database whitespace anomalies (tabs, multiple spaces) while preserving newlines
  const cleanText = rawText
    .replace(/[ \t]{2,}/g, ' ')
    .replace(/\r\n/g, '\n')
    .trim();

  const phraseSet = new Set<string>();
  const hasCustom = Array.isArray(customKeywords) && customKeywords.some(k => k && typeof k === 'string' && k.trim().length > 1);

  if (hasCustom) {
    // When custom keywords exist, ONLY highlight those exact teacher/AI defined key phrases
    customKeywords!.forEach(k => {
      if (k && typeof k === 'string' && k.trim().length > 1) {
        phraseSet.add(k.trim().toLowerCase());
      }
    });
  } else {
    // Default fallback: ONLY highlight distinct multi-word scientific key phrases (avoiding single common words like "force", "law", "sun")
    const standardKeyPhrases = [
      "directed towards the center",
      "directed toward center",
      "directed towards center",
      "directed toward the center",
      "centripetal force",
      "centrifugal force",
      "earth attracts the moon",
      "earth attracts moon",
      "motion of the moon",
      "motion of moon",
      "moving along a circle",
      "gravitational force",
      "law of gravitation",
      "inversely proportional to",
      "directly proportional to",
      "conservation of energy",
      "conservation of momentum",
      "center of mass",
      "center of gravity",
      "magnetic field",
      "electric field",
      "potential difference",
      "total internal reflection",
      "chemical equation",
      "balanced equation"
    ];
    standardKeyPhrases.forEach(p => phraseSet.add(p));
  }

  const sortedPhrases = Array.from(phraseSet).sort((a, b) => b.length - a.length);
  if (sortedPhrases.length === 0) return cleanText;

  const escaped = sortedPhrases.map(p => p.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
  const pattern = new RegExp(`\\b(${escaped.join('|')})\\b`, 'gi');

  return cleanText.replace(pattern, (match) => {
    return `<span style="background-color: #fef08a; color: #713f12; font-weight: 700; border-radius: 2px; padding: 0 2px;">${match}</span>`;
  });
}

/**
 * Universal PDF exporter for Objective, Subjective, and Practice exams including Model Answers
 */
export async function exportUniversalExamPDF(exam: any, questions: any[], options: { includeAnswers?: boolean; title?: string } = {}) {
  if (typeof window === 'undefined') return;
  const w = window as any;
  if (!w.html2pdf) {
    await new Promise<void>((resolve, reject) => {
      const s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
      s.onload = () => resolve();
      s.onerror = () => reject(new Error('Failed to load PDF library.'));
      document.head.appendChild(s);
    });
  }

  const includeAnswers = options.includeAnswers !== false; // Default true

  let resolvedQuestions: any[] = Array.isArray(questions) && questions.length > 0 
    ? questions 
    : (exam.questions || exam.questionSnapshot || exam.questionDetails || []);

  const isPlaceholderQuestion = (q: any) => {
    if (!q) return true;
    if (typeof q === 'string') return true;
    const txt = (q.text || q.question || q.questionText || '').trim();
    if (!txt) return true;
    // Only treat as placeholder if text is literally "Question X" and has no options/solution
    if (/^Question \d+$/i.test(txt) && (!q.options || q.options.length === 0) && (!q.solution || q.solution.trim().length === 0)) {
      return true;
    }
    return false;
  };

  // Only auto-hydrate if resolvedQuestions is empty or consists purely of string IDs / placeholders
  const needsHydration = resolvedQuestions.length === 0 || (
    Array.isArray(questions) && questions.length > 0 && typeof questions[0] === 'string'
  ) || resolvedQuestions.every(isPlaceholderQuestion);

  if (needsHydration) {
    let rawIds: string[] = [];

    if (Array.isArray(questions) && questions.length > 0) {
      rawIds = questions
        .map((q: any) => typeof q === 'string' ? q : (q.questionCode || q.id || q.code))
        .filter(Boolean);
    }
    
    if (rawIds.length === 0 && exam) {
      if (Array.isArray(exam.questionIds) && exam.questionIds.length > 0) {
        rawIds = exam.questionIds;
      } else if (Array.isArray(exam.questionCodes) && exam.questionCodes.length > 0) {
        rawIds = exam.questionCodes;
      } else if (Array.isArray(exam.questions) && exam.questions.length > 0) {
        rawIds = exam.questions
          .map((q: any) => typeof q === 'string' ? q : (q.questionCode || q.id || q.code))
          .filter(Boolean);
      }
    }

    const headers = await getAuthHeaders();

    if (rawIds.length > 0) {
      try {
        const res = await fetch(`/api/admin/questions?ids=${encodeURIComponent(rawIds.join(','))}`, { headers });
        if (res.ok) {
          const data = await res.json();
          if (Array.isArray(data.questions) && data.questions.length > 0) {
            const qMap = new Map(data.questions.map((q: any) => [q.id || q.code || q.questionCode, q]));
            const fetchedList = rawIds.map((id, idx) => qMap.get(id) || data.questions[idx]).filter(Boolean);
            if (fetchedList.length > 0) {
              resolvedQuestions = fetchedList;
            }
          }
        }
      } catch (e) {
        console.warn('PDF export auto-hydrate by IDs error:', e);
      }
    }

    if ((resolvedQuestions.length === 0 || resolvedQuestions.some(isPlaceholderQuestion)) && exam && (exam.id || exam.examId)) {
      const eId = exam.id || exam.examId;
      try {
        const typeLower = String(exam.type || '').toLowerCase();
        const isSubj = typeLower.includes('subjective') || 
                       typeLower.includes('classroom_test') || 
                       typeLower.includes('home_practice') || 
                       exam.examType === 'subjective' || 
                       eId.includes('Subj') || 
                       exam.name?.toLowerCase().includes('subjective');
        const endpoint = isSubj ? `/api/admin/exams/subjective?attemptId=${eId}` : `/api/admin/exams?id=${eId}`;
        const res = await fetch(endpoint, { headers });
        if (res.ok) {
          const data = await res.json();
          const qList = data.questions || data.questionSnapshot || (data.exam && data.exam.questions);
          if (Array.isArray(qList) && qList.length > 0 && !isPlaceholderQuestion(qList[0])) {
            resolvedQuestions = qList;
          }
        }
      } catch (e) {
        console.warn('PDF export auto-hydrate by examId error:', e);
      }
    }
  }

  const printContainer = document.createElement('div');
  printContainer.id = 'pdf-universal-exam-container';
  printContainer.className = 'math-container';
  printContainer.style.cssText = 'font-family: Arial, sans-serif; background: #ffffff; color: #000000; padding: 25px;';

  const styleOverride = document.createElement('style');
  styleOverride.innerHTML = `
    #pdf-universal-exam-container, #pdf-universal-exam-container * {
      color: #000000 !important;
      text-shadow: none !important;
    }
    #pdf-universal-exam-container [style*="color: #dc2626"],
    #pdf-universal-exam-container [style*="color:#dc2626"] {
      color: #dc2626 !important;
      font-weight: 700 !important;
    }
    #pdf-universal-exam-container mark {
      background-color: transparent !important;
      color: inherit !important;
      border: none !important;
      padding: 0 !important;
      margin: 0 !important;
    }
  `;
  printContainer.appendChild(styleOverride);

  const typeLower = String(exam.type || '').toLowerCase();
  const isSubj = typeLower.includes('subjective') || 
                 typeLower.includes('classroom_test') || 
                 typeLower.includes('home_practice') || 
                 exam.examType === 'subjective' || 
                 exam.name?.toLowerCase().includes('subjective');
  const examType = exam.examType || (isSubj ? 'Subjective' : (typeLower.includes('practice') ? 'Practice' : 'Objective'));
  const questionsList = resolvedQuestions;

  const headerHtml = `
    <div style="text-align: center; border-bottom: 2.5px solid #1e293b; padding-bottom: 12px; margin-bottom: 20px;">
      <h1 style="margin: 0; font-size: 24px; font-weight: 800; color: #1e293b; letter-spacing: 0.5px;">Yashcom Foundation</h1>
      <h2 style="margin: 6px 0 0 0; font-size: 15px; font-weight: 700; color: #4f46e5; text-transform: uppercase;">
        ${options.title || `${examType} Exam & Model Answer Key`}
      </h2>
    </div>
    
    <table style="width: 100%; margin-bottom: 25px; font-size: 12px; border-collapse: collapse; border: none; background: #f8fafc; padding: 12px; border-radius: 6px;">
      <tr>
        <td style="padding: 6px 10px; border: none;"><strong>Exam Title:</strong> ${exam.name || exam.title || 'Examination'}</td>
        <td style="padding: 6px 10px; border: none; text-align: right;"><strong>Class / Board:</strong> Class ${exam.class || exam.className || 'N/A'} (${exam.board || 'CBSE'})</td>
      </tr>
      <tr>
        <td style="padding: 6px 10px; border: none;"><strong>Subject:</strong> ${exam.subjectName || exam.subject || 'General'}</td>
        <td style="padding: 6px 10px; border: none; text-align: right;"><strong>Total Marks:</strong> ${exam.totalMarks || exam.maxMarks || (questionsList.length * 1)} Marks</td>
      </tr>
      <tr>
        <td style="padding: 6px 10px; border: none;"><strong>Total Questions:</strong> ${questionsList.length} Questions</td>
        <td style="padding: 6px 10px; border: none; text-align: right;"><strong>Duration:</strong> ${exam.duration || exam.totalTime || 30} Minutes</td>
      </tr>
    </table>
    
    <div style="margin-top: 20px;">
      ${questionsList.map((q: any, idx: number) => {
        const qText = q.text || q.question || q.questionText || `Question ${idx + 1}`;
        const optionsArr = q.options || q.choices || [];
        const correctAns = q.correctAnswer !== undefined ? q.correctAnswer : (q.answer || q.modelAnswer || '');
        const explanation = q.solution || q.explanation || q.modelAnswer || q.guide || '';
        const customKw = q.keywords || q.keyPhrases || [];
        const highlightedExp = highlightModelAnswerKeywords(explanation, customKw);

        return `
          <div style="margin-bottom: 22px; page-break-inside: avoid; border: 1px solid #cbd5e1; border-radius: 6px; overflow: hidden; background: #ffffff;">
            <div style="background: #e2e8f0; padding: 8px 14px; font-size: 13px; font-weight: bold; border-bottom: 1px solid #cbd5e1; display: flex; justify-content: space-between; align-items: center; color: #0f172a;">
              <span>Question ${idx + 1}</span>
              <span style="font-size: 11px; font-weight: normal; color: #475569;">[${q.marks || 1} Mark${(q.marks || 1) > 1 ? 's' : ''}]</span>
            </div>
            
            <div style="padding: 14px 16px; font-size: 13px; line-height: 1.6; color: #0f172a; white-space: pre-line;">
              ${qText}
            </div>

            ${optionsArr && optionsArr.length > 0 ? `
              <div style="padding: 0 16px 14px 16px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                ${optionsArr.map((opt: string, optIdx: number) => {
                  const cStr = String(correctAns).trim().toLowerCase();
                  const optStr = String(opt).trim().toLowerCase();
                  const letterCode = String.fromCharCode(65 + optIdx).toLowerCase();
                  const hasTextMatch = optionsArr.some((o: string) => String(o).trim().toLowerCase() === cStr);
                  
                  let isCorrect = (cStr === optStr) || 
                                  (cStr === letterCode) || 
                                  (cStr === `${letterCode}.`) || 
                                  (cStr === `(${letterCode})`);
                  
                  if (!isCorrect && Array.isArray(q.correctAnswers) && q.correctAnswers.length > 0) {
                    isCorrect = q.correctAnswers.some((ca: any) => {
                      const caStr = String(ca).trim().toLowerCase();
                      return caStr === optStr || caStr === letterCode;
                    });
                  }
                  
                  if (!isCorrect && !hasTextMatch && String(optIdx) === cStr) {
                    isCorrect = true;
                  }

                  return `
                    <div style="font-size: 12px; padding: 6px 10px; border-radius: 4px; border: 1px solid ${isCorrect ? '#16a34a' : '#e2e8f0'}; background: ${isCorrect ? '#f0fdf4' : '#f8fafc'}; color: ${isCorrect ? '#15803d' : '#334155'}; font-weight: ${isCorrect ? 'bold' : 'normal'};">
                      ${String.fromCharCode(65 + optIdx)}. ${opt} ${isCorrect ? '✓ (Correct)' : ''}
                    </div>
                  `;
                }).join('')}
              </div>
            ` : ''}

            ${includeAnswers ? `
              <div style="border-top: 1.5px dashed #cbd5e1; background: #faf5ff; padding: 12px 16px; font-size: 12px; line-height: 1.6;">
                <div style="font-weight: 800; color: #6b21a8; margin-bottom: 4px; text-transform: uppercase; font-size: 11px; letter-spacing: 0.5px;">
                  💡 Model Answer & Keyword Highlights:
                </div>
                ${correctAns !== '' && optionsArr.length === 0 ? `
                  <div style="margin-bottom: 6px; font-weight: 700; color: #15803d;">
                    Correct Answer: ${correctAns}
                  </div>
                ` : ''}
                <div style="color: #1e1b4b; line-height: 1.7; word-break: break-word;">
                  ${highlightedExp || (optionsArr.length > 0 ? `Correct option: <strong>${optionsArr[Number(correctAns)] || correctAns}</strong>` : 'Full credit awarded for complete logical steps.')}
                </div>
              </div>
            ` : ''}
          </div>
        `;
      }).join('')}
    </div>
  `;
  
  const contentDiv = document.createElement('div');
  contentDiv.innerHTML = headerHtml;
  printContainer.appendChild(contentDiv);

  document.body.appendChild(printContainer);

  if (w.renderMathInElement) {
    w.renderMathInElement(printContainer, KATEX_AUTO_RENDER_OPTIONS);
  }

  const opt = {
    margin:       [0.3, 0.35, 0.3, 0.35],
    filename:     `${(exam.name || exam.title || 'Exam_Paper').replace(/\s+/g, '_')}_Model_Answers.pdf`,
    image:        { type: 'jpeg', quality: 0.98 },
    html2canvas:  { scale: 2, useCORS: true },
    jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
  };

  await w.html2pdf().from(printContainer).set(opt).save();
  document.body.removeChild(printContainer);
}

export async function exportPasswordProtectedLearningPDF(exam: any, questions: any[]) {
  if (typeof window === 'undefined') return;
  const w = window as any;
  if (!w.html2pdf) {
    await new Promise<void>((resolve, reject) => {
      const s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
      s.onload = () => resolve();
      s.onerror = () => reject(new Error('Failed to load PDF library.'));
      document.head.appendChild(s);
    });
  }

  const wrapper = document.createElement('div');
  wrapper.style.cssText = 'position: absolute; left: -9999px; top: 0; width: 0; height: 0; overflow: hidden;';
  document.body.appendChild(wrapper);

  const printContainer = document.createElement('div');
  printContainer.id = 'pdf-learning-suite-container';
  printContainer.className = 'math-container';
  printContainer.style.cssText = 'font-family: Arial, sans-serif; background: #ffffff; color: #000000; padding: 25px;';
  wrapper.appendChild(printContainer);

  const styleOverride = document.createElement('style');
  styleOverride.innerHTML = `
    #pdf-learning-suite-container, #pdf-learning-suite-container * {
      color: #000000 !important;
      text-shadow: none !important;
    }
    #pdf-learning-suite-container mark {
      background-color: transparent !important;
      color: inherit !important;
      border: none !important;
      padding: 0 !important;
      margin: 0 !important;
    }
  `;
  printContainer.appendChild(styleOverride);

  const headerHtml = `
    <div style="text-align: center; border-bottom: 2.5px solid #1e293b; padding-bottom: 12px; margin-bottom: 20px;">
      <h1 style="margin: 0; font-size: 24px; font-weight: 800; color: #1e293b; letter-spacing: 0.5px;">Yashcom Foundation</h1>
      <h2 style="margin: 6px 0 0 0; font-size: 15px; font-weight: 700; color: #10b981; text-transform: uppercase;">
        Daily Learning & Practice Sheet (Model Answers)
      </h2>
    </div>
    
    <table style="width: 100%; margin-bottom: 25px; font-size: 12px; border-collapse: collapse; border: none; background: #f8fafc; padding: 12px; border-radius: 6px;">
      <tr>
        <td style="padding: 6px 10px; border: none;"><strong>Sheet Name:</strong> ${exam.name || 'Daily Learning Practice'}</td>
        <td style="padding: 6px 10px; border: none; text-align: right;"><strong>Class / Board:</strong> Class ${exam.class || exam.classNum || '10'} (${exam.board || 'Maharashtra Board'})</td>
      </tr>
      <tr>
        <td style="padding: 6px 10px; border: none;"><strong>Subject:</strong> ${exam.subject || 'General'}</td>
        <td style="padding: 6px 10px; border: none; text-align: right;"><strong>Total Questions:</strong> ${questions.length} Questions</td>
      </tr>
      <tr>
        <td style="padding: 6px 10px; border: none;"><strong>Chapter:</strong> Chapter ${exam.chapterNumber || 'N/A'}: ${exam.chapterName || 'N/A'}</td>
        <td style="padding: 6px 10px; border: none; text-align: right; color: #dc2626; font-weight: bold;">🔒 Password Protected</td>
      </tr>
    </table>
    
    <div style="margin-top: 20px;">
      ${questions.map((q: any, idx: number) => {
        const qText = q.text || `Question ${idx + 1}`;
        const explanation = q.solution || '';
        const customKw = q.keywords || [];
        const highlightedExp = highlightModelAnswerKeywords(explanation, customKw);

        return `
          <div style="margin-bottom: 22px; page-break-inside: avoid; border: 1px solid #cbd5e1; border-radius: 6px; overflow: hidden; background: #ffffff;">
            <div style="background: #e2e8f0; padding: 8px 14px; font-size: 13px; font-weight: bold; border-bottom: 1px solid #cbd5e1; display: flex; justify-content: space-between; align-items: center; color: #0f172a;">
              <span>Question ${idx + 1}</span>
              <span style="font-size: 11px; font-weight: normal; color: #475569;">[${q.marks || 1} Mark${(q.marks || 1) > 1 ? 's' : ''}]</span>
            </div>
            
            <div style="padding: 14px 16px; font-size: 13px; line-height: 1.6; color: #0f172a; white-space: pre-line;">
              ${qText}
            </div>

            <div style="border-top: 1.5px dashed #cbd5e1; background: #faf5ff; padding: 12px 16px; font-size: 12px; line-height: 1.6;">
              <div style="font-weight: 800; color: #6b21a8; margin-bottom: 4px; text-transform: uppercase; font-size: 11px; letter-spacing: 0.5px;">
                💡 Verbatim Model Answer & Keyword Highlights:
              </div>
              <div style="color: #1e1b4b; line-height: 1.7; word-break: break-word; white-space: pre-line;">
                ${highlightedExp || 'Full credit awarded for complete logical steps.'}
              </div>
            </div>
          </div>
        `;
      }).join('')}
    </div>
  `;

  const contentDiv = document.createElement('div');
  contentDiv.innerHTML = headerHtml;
  printContainer.appendChild(contentDiv);

  if (w.renderMathInElement) {
    w.renderMathInElement(printContainer, KATEX_AUTO_RENDER_OPTIONS);
  }

  const opt = {
    margin:       [0.3, 0.35, 0.3, 0.35],
    filename:     `${(exam.name || 'Learning_Sheet').replace(/\s+/g, '_')}_Protected.pdf`,
    image:        { type: 'jpeg', quality: 0.98 },
    html2canvas:  { scale: 2, useCORS: true, scrollY: 0, scrollX: 0 },
    jsPDF:        { 
      unit: 'in', 
      format: 'a4', 
      orientation: 'portrait',
      encryption: {
        userPassword: 'Yashcom@26',
        ownerPassword: 'Yashcom@26',
        userPermissions: ['print']
      }
    }
  };

  await w.html2pdf().from(printContainer).set(opt).save();
  document.body.removeChild(wrapper);
}

export async function exportStudentMonthlyReportPDF(params: {
  student: {
    name: string;
    studentCode: string;
    batchName: string;
    parentMobile: string;
    parentEmail: string;
    email: string;
  };
  quotientDetails: {
    overallQuotient: number;
    components: Array<{
      parameterId: string;
      parameterName: string;
      score: number;
      weight: number;
      contribution: number;
      details: any;
    }>;
  };
  comments: string;
}) {
  if (typeof window === 'undefined') return;
  const w = window as any;
  if (!w.html2pdf) {
    await new Promise<void>((resolve, reject) => {
      const s = document.createElement('script');
      s.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
      s.onload = () => resolve();
      s.onerror = () => reject(new Error('Failed to load PDF library.'));
      document.head.appendChild(s);
    });
  }

  const { student, quotientDetails, comments } = params;
  const reportMonth = new Date().toLocaleString('en-IN', { month: 'long', year: 'numeric' });
  const generationDate = new Date().toLocaleDateString('en-IN', { timeZone: 'Asia/Kolkata' });

  // Map components for easier access
  const examComp = quotientDetails.components.find(c => c.parameterId === 'exam') || { score: 0, details: {} };
  const practiceComp = quotientDetails.components.find(c => c.parameterId === 'practice') || { score: 0, details: {} };
  const healthComp = quotientDetails.components.find(c => c.parameterId === 'topicHealth') || { score: 0, details: {} };
  const integrityComp = quotientDetails.components.find(c => c.parameterId === 'integrity') || { score: 0, details: {} };
  const obsComp = quotientDetails.components.find(c => c.parameterId === 'observations') || { score: 0, details: {} };

  const getTierName = (score: number) => {
    if (score >= 85) return 'EXCELLENT TIER 🌟';
    if (score >= 60) return 'STANDARD TIER 👍';
    return 'NEEDS ATTENTION ⚠️';
  };

  const wrapper = document.createElement('div');
  wrapper.style.cssText = 'position: absolute; left: -9999px; top: 0; width: 0; height: 0; overflow: hidden;';
  document.body.appendChild(wrapper);

  // Build the print element
  const printContainer = document.createElement('div');
  printContainer.id = 'pdf-monthly-report-container';
  printContainer.style.cssText = `
    width: 210mm;
    height: 297mm;
    box-sizing: border-box;
    padding: 15mm 12mm 10mm 12mm;
    background: #ffffff;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    color: #1e293b;
    overflow: hidden;
  `;
  wrapper.appendChild(printContainer);

  // Internal Styling to override styles and force print behavior
  const styleOverride = document.createElement('style');
  styleOverride.innerHTML = `
    #pdf-monthly-report-container * {
      box-sizing: border-box;
    }
  `;
  printContainer.appendChild(styleOverride);

  // Classroom Observations breakdown list
  const obsParams = obsComp.details?.parameters || [
    { id: 'activeParticipation', name: 'Active Participation', average: 50 },
    { id: 'sincerity', name: 'Sincerity & Behavior', average: 50 },
    { id: 'timelyWork', name: 'Timely Work', average: 50 }
  ];

  const htmlContent = `
    <!-- Header -->
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2.5px solid #4f46e5; padding-bottom: 8px; margin-bottom: 14px;">
      <div>
        <h1 style="margin: 0; font-size: 22px; font-weight: 800; color: #4f46e5; letter-spacing: -0.5px;">Yashcom Foundation</h1>
        <p style="margin: 2px 0 0 0; font-size: 9px; color: #64748b; text-transform: uppercase; font-weight: 600; letter-spacing: 0.5px;">Empowering Conceptual Excellence</p>
      </div>
      <div style="text-align: right;">
        <h2 style="margin: 0; font-size: 14px; font-weight: 800; color: #1e293b; text-transform: uppercase; letter-spacing: 0.5px;">Monthly Review Report</h2>
        <p style="margin: 2px 0 0 0; font-size: 10px; color: #64748b; font-weight: 700;">Month: ${reportMonth}</p>
      </div>
    </div>

    <!-- Student Info Card -->
    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 10px 14px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 14px;">
      <div>
        <h3 style="margin: 0 0 2px 0; font-size: 8px; text-transform: uppercase; letter-spacing: 0.5px; color: #64748b; font-weight: 700;">Student Name</h3>
        <p style="margin: 0; font-size: 12px; font-weight: 700; color: #1e293b;">${student.name}</p>
      </div>
      <div>
        <h3 style="margin: 0 0 2px 0; font-size: 8px; text-transform: uppercase; letter-spacing: 0.5px; color: #64748b; font-weight: 700;">Batch Name</h3>
        <p style="margin: 0; font-size: 11px; font-weight: 700; color: #1e293b;">${student.batchName}</p>
      </div>
      <div>
        <h3 style="margin: 0 0 2px 0; font-size: 8px; text-transform: uppercase; letter-spacing: 0.5px; color: #64748b; font-weight: 700;">Parent Mobile / Email</h3>
        <p style="margin: 0; font-size: 11px; font-weight: 700; color: #1e293b;">${student.parentMobile || 'N/A'} <span style="font-weight: 500; font-size: 9.5px; color: #64748b; display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${student.parentEmail || 'N/A'}</span></p>
      </div>
    </div>

    <!-- Dashboard Columns (Two Column Split) -->
    <div style="display: grid; grid-template-columns: 80mm 100mm; gap: 6mm; margin-bottom: 14px;">
      
      <!-- Left Column: LQ Gauge & Educator Comments -->
      <div style="display: flex; flex-direction: column; gap: 14px;">
        
        <!-- LQ Circle Score Card -->
        <div style="border: 1.5px solid #e2e8f0; background: #ffffff; border-radius: 8px; padding: 10px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 130px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); position: relative;">
          <div style="font-size: 10px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px;">Learning Quotient (LQ)</div>
          
          <div style="display: flex; align-items: center; justify-content: center; position: relative; width: 75px; height: 75px;">
            <svg width="72" height="72" viewBox="0 0 120 120" style="display: block;">
              <circle cx="60" cy="60" r="50" fill="none" stroke="#f1f5f9" stroke-width="10" />
              <circle 
                cx="60" 
                cy="60" 
                r="50" 
                fill="none" 
                stroke="${getScoreColor(quotientDetails.overallQuotient)}" 
                stroke-width="10" 
                stroke-dasharray="314.16"
                stroke-dashoffset="${314.16 - (314.16 * quotientDetails.overallQuotient) / 100}"
                stroke-linecap="round"
                transform="rotate(-90 60 60)"
              />
            </svg>
            <div style="position: absolute; display: flex; flex-direction: column; align-items: center; justify-content: center; top: 0; left: 0; right: 0; bottom: 0;">
              <span style="font-size: 20px; font-weight: 900; color: #1e293b; line-height: 1;">${quotientDetails.overallQuotient}</span>
              <span style="font-size: 7.5px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 1px;">LQ</span>
            </div>
          </div>
          
          <div style="font-size: 8px; font-weight: 700; color: ${getScoreColor(quotientDetails.overallQuotient)}; text-transform: uppercase; margin-top: 6px; padding: 2px 6px; background: #ffffff; border-radius: 4px; border: 1px solid ${getScoreColor(quotientDetails.overallQuotient)}30;">
            ${getTierName(quotientDetails.overallQuotient)}
          </div>
        </div>

        <!-- Educator Comments Feedback Card -->
        <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px 14px; background: #fffdf5; flex: 1; display: flex; flex-direction: column; min-height: 216px;">
          <h4 style="margin: 0 0 8px 0; font-size: 11px; font-weight: 800; color: #b45309; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 1.5px solid #fef08a; padding-bottom: 4px; display: flex; align-items: center; gap: 4px;">
            <span>📝</span> Educator's Diagnostic Feedback
          </h4>
          <p style="margin: 0; font-size: 10px; line-height: 1.6; color: #78350f; font-weight: 500; white-space: pre-wrap; text-align: justify;">
            ${comments}
          </p>
        </div>

      </div>

      <!-- Right Column: 5 Pillars Score Breakdown -->
      <div style="display: flex; flex-direction: column; gap: 10px;">
        <h4 style="margin: 0 0 4px 0; font-size: 11px; font-weight: 800; color: #1e293b; text-transform: uppercase; letter-spacing: 0.5px; border-left: 3px solid #4f46e5; padding-left: 6px;">
          Performance Pillars Breakdown
        </h4>

        <!-- Pillar 1: Exam Performance -->
        <div style="border: 1px solid #e2e8f0; border-radius: 6px; padding: 8px 10px; background: #ffffff;">
          <div style="display: flex; justify-content: space-between; font-size: 10.5px; font-weight: 700; margin-bottom: 4px;">
            <span>🎯 1. Exam Performance</span>
            <span style="color: ${getScoreColor(examComp.score)}">${examComp.score} / 100</span>
          </div>
          <div style="width: 100%; height: 6px; background: #f1f5f9; border-radius: 3px; overflow: hidden; margin-bottom: 4px;">
            <div style="width: ${examComp.score}%; height: 100%; background: ${getScoreColor(examComp.score)}; border-radius: 3px;"></div>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 8.5px; color: #64748b; font-weight: 600;">
            <span>Attendance Rate: ${examComp.details?.attendanceRate ?? 100}%</span>
            <span>Absent: ${examComp.details?.absent ?? 0} Tests</span>
          </div>
        </div>

        <!-- Pillar 2: Practice Engagement -->
        <div style="border: 1px solid #e2e8f0; border-radius: 6px; padding: 8px 10px; background: #ffffff;">
          <div style="display: flex; justify-content: space-between; font-size: 10.5px; font-weight: 700; margin-bottom: 4px;">
            <span>🏋️ 2. Practice Engagement</span>
            <span style="color: ${getScoreColor(practiceComp.score)}">${practiceComp.score} / 100</span>
          </div>
          <div style="width: 100%; height: 6px; background: #f1f5f9; border-radius: 3px; overflow: hidden; margin-bottom: 4px;">
            <div style="width: ${practiceComp.score}%; height: 100%; background: ${getScoreColor(practiceComp.score)}; border-radius: 3px;"></div>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 8.5px; color: #64748b; font-weight: 600;">
            <span>Attempted: ${practiceComp.details?.totalQuestionsAttempted ?? 0} Qs (Topics: ${practiceComp.details?.topicsAttemptedCount ?? 0})</span>
            <span>Efficiency: ${practiceComp.score}% (Avg: ${practiceComp.details?.averageQuestionsPerTopic ?? 0} Qs/topic)</span>
          </div>
        </div>

        <!-- Pillar 3: Topic Health -->
        <div style="border: 1px solid #e2e8f0; border-radius: 6px; padding: 8px 10px; background: #ffffff;">
          <div style="display: flex; justify-content: space-between; font-size: 10.5px; font-weight: 700; margin-bottom: 4px;">
            <span>🩺 3. Topic Health</span>
            <span style="color: ${getScoreColor(healthComp.score)}">${healthComp.score} / 100</span>
          </div>
          <div style="width: 100%; height: 6px; background: #f1f5f9; border-radius: 3px; overflow: hidden; margin-bottom: 4px;">
            <div style="width: ${healthComp.score}%; height: 100%; background: ${getScoreColor(healthComp.score)}; border-radius: 3px;"></div>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 8.5px; color: #64748b; font-weight: 600;">
            <span>Mastered Ratio: ${healthComp.details?.masteryRatio ?? 0}%</span>
            <span>Attention Topics: ${healthComp.details?.attentionCount ?? 0}</span>
          </div>
        </div>

        <!-- Pillar 4: Proctoring Integrity -->
        <div style="border: 1px solid #e2e8f0; border-radius: 6px; padding: 8px 10px; background: #ffffff;">
          <div style="display: flex; justify-content: space-between; font-size: 10.5px; font-weight: 700; margin-bottom: 4px;">
            <span>🛡️ 4. Proctoring Integrity</span>
            <span style="color: ${getScoreColor(integrityComp.score)}">${integrityComp.score} / 100</span>
          </div>
          <div style="width: 100%; height: 6px; background: #f1f5f9; border-radius: 3px; overflow: hidden; margin-bottom: 4px;">
            <div style="width: ${integrityComp.score}%; height: 100%; background: ${getScoreColor(integrityComp.score)}; border-radius: 3px;"></div>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 8.5px; color: #64748b; font-weight: 600;">
            <span>Integrity Index: ${integrityComp.score}%</span>
            <span>Avg Weekly Violations: ${integrityComp.details?.averageWeeklyViolations ?? 0}</span>
          </div>
        </div>

        <!-- Pillar 5: Classroom Observations -->
        <div style="border: 1px solid #e2e8f0; border-radius: 6px; padding: 8px 10px; background: #ffffff;">
          <div style="display: flex; justify-content: space-between; font-size: 10.5px; font-weight: 700; margin-bottom: 4px;">
            <span>👥 5. Classroom Observations</span>
            <span style="color: ${getScoreColor(obsComp.score)}">${obsComp.score} / 100</span>
          </div>
          <div style="width: 100%; height: 6px; background: #f1f5f9; border-radius: 3px; overflow: hidden; margin-bottom: 4px;">
            <div style="width: ${obsComp.score}%; height: 100%; background: ${getScoreColor(obsComp.score)}; border-radius: 3px;"></div>
          </div>
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; font-size: 8px; color: #64748b; font-weight: 600; gap: 4px;">
            ${obsParams.map((p: any) => `<span>${p.name}: <strong>${p.average}%</strong></span>`).join(' | ')}
          </div>
        </div>

      </div>

    </div>

    <!-- Signatures -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; text-align: center; margin-top: 30px; border-top: 1.5px solid #e2e8f0; padding-top: 16px;">
      <div style="display: flex; flex-direction: column; align-items: center;">
        <div style="height: 35px;"></div>
        <div style="border-top: 1.5px solid #94a3b8; width: 60%; font-size: 9.5px; color: #64748b; font-weight: 700; padding-top: 4px;">Class Teacher</div>
      </div>
      <div style="display: flex; flex-direction: column; align-items: center;">
        <div style="height: 35px;"></div>
        <div style="border-top: 1.5px solid #94a3b8; width: 60%; font-size: 9.5px; color: #64748b; font-weight: 700; padding-top: 4px;">Parent Signature</div>
      </div>
    </div>

    <!-- Report Bottom Info Footer -->
    <div style="position: absolute; bottom: 8mm; left: 12mm; right: 12mm; border-top: 1px dashed #cbd5e1; padding-top: 6px; display: flex; justify-content: space-between; font-size: 8.5px; color: #94a3b8; font-weight: 600;">
      <span>Report Card generated on: ${generationDate}</span>
      <span>Yashcom Foundation &copy; 2026 - Confidential Student Dossier</span>
    </div>
  `;

  printContainer.innerHTML += htmlContent;

  const opt = {
    margin:       0,
    filename:     `${student.name.replace(/\s+/g, '_')}_Monthly_Report.pdf`,
    image:        { type: 'jpeg', quality: 0.98 },
    html2canvas:  { scale: 2.5, useCORS: true, scrollY: 0, scrollX: 0 },
    jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
  };

  try {
    const pdfObject = w.html2pdf().from(printContainer).set(opt);
    
    return {
      save: async () => {
        await pdfObject.save();
        document.body.removeChild(wrapper);
      },
      getBlob: async (): Promise<Blob> => {
        const blob = await pdfObject.output('blob');
        document.body.removeChild(wrapper);
        return blob;
      }
    };
  } catch (error) {
    try {
      document.body.removeChild(wrapper);
    } catch (_) {}
    throw error;
  }
}
