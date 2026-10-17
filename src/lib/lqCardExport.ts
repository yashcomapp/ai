import { formatDateDMY } from '@/lib/dateUtils';
import { playNotificationSound } from '@/lib/audioUtils';
import { getScoreColor } from '@/lib/dashboardMetrics';

/**
 * Strips middle names and formats student name as "First Last" for clean display in reports & WhatsApp cards.
 * E.g., "Radha Sunil Bhole" -> "Radha Bhole", "Jagdish Durgasingh Lodhi" -> "Jagdish Lodhi"
 */
export function formatReportStudentName(fullName: string): string {
  if (!fullName) return '';
  const parts = fullName.trim().split(/\s+/).filter(Boolean);
  if (parts.length <= 2) return parts.join(' ');
  return `${parts[0]} ${parts[parts.length - 1]}`;
}

/**
 * Returns deep, authoritative high-contrast colors on white/light backgrounds.
 * Avoids washed out yellows, pale pinks, and neon greens that strain the eyes.
 */
export function getDeepScoreColor(score: number): string {
  if (score >= 80) return '#14532d'; // Forest green (emerald-900)
  if (score >= 60) return '#0369a1'; // Ocean blue (sky-700)
  if (score >= 40) return '#92400e'; // Warm bronze/amber (amber-800, never bright yellow!)
  return '#991b1b'; // Deep crimson (red-800)
}

/**
 * Renders an executive-grade, high-contrast score chip for white/light reports.
 * Guarantees crisp readability and effortless viewing at any zoom level.
 */
export function getScoreChip(val: number | null | undefined, isHero: boolean = false): string {
  if (val === null || val === undefined) {
    return `<span style="display:inline-block; min-width: 44px; padding: 3px 8px; border-radius: 6px; font-weight: 700; font-size: 13px; text-align: center; background: #f1f5f9; color: #64748b; border: 1px solid #cbd5e1;">-</span>`;
  }
  const num = Math.round(val);
  let bg = '#f8fafc';
  let color = '#0f172a';
  let border = '#cbd5e1';

  if (num >= 80) {
    // Forest green on soft mint (ultra high contrast > 7:1)
    bg = '#dcfce7';
    color = '#14532d';
    border = '#86efac';
  } else if (num >= 60) {
    // Deep ocean blue on soft sky
    bg = '#e0f2fe';
    color = '#0369a1';
    border = '#7dd3fc';
  } else if (num >= 40) {
    // Deep warm bronze/amber on soft cream (never washed out yellow!)
    bg = '#fef3c7';
    color = '#92400e';
    border = '#fde68a';
  } else {
    // Deep crimson on soft rose
    bg = '#fee2e2';
    color = '#991b1b';
    border = '#fca5a5';
  }

  const fontSize = isHero ? '14px' : '12.5px';
  const fontWeight = isHero ? '900' : '800';
  const minWidth = isHero ? '54px' : '46px';
  const shadow = isHero ? 'box-shadow: 0 1px 3px rgba(0,0,0,0.06);' : '';

  return `<span style="display:inline-block; min-width: ${minWidth}; padding: 3px 8px; border-radius: 6px; font-weight: ${fontWeight}; font-size: ${fontSize}; text-align: center; background: ${bg}; color: ${color}; border: 1.5px solid ${border}; ${shadow}">${num}%</span>`;
}

/**
 * Dynamically loads html2canvas from CDN if not already loaded in window
 */
export const loadHtml2Canvas = async (): Promise<any> => {
  if (typeof window === 'undefined') return null;
  const w = window as any;
  if (w.html2canvas) return w.html2canvas;
  return new Promise<any>((resolve, reject) => {
    const s = document.createElement('script');
    s.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js';
    s.onload = () => resolve((window as any).html2canvas);
    s.onerror = () => reject(new Error('Failed to load image generation library.'));
    document.head.appendChild(s);
  });
};

export interface StudentLqCardExportParams {
  student: {
    name: string;
    studentCode?: string;
    batchName?: string;
    parentMobile?: string;
  };
  quotientDetails: {
    overallQuotient: number;
    components?: any[];
    [key: string]: any;
  };
  duration?: string | number;
  commentsText?: string;
  parentMobile?: string;
  whatsAppMode?: 'app' | 'web';
  triggerWhatsApp?: boolean;
}

/**
 * Generates an Ultra HD lossless WhatsApp image card for a student's Learning Quotient (LQ) report,
 * copies it to the clipboard (for instant Ctrl+V in WhatsApp Web/Desktop), triggers a download,
 * and launches WhatsApp or native Mobile Share.
 */
export async function exportStudentLqCardImage(params: StudentLqCardExportParams): Promise<{
  blob: Blob;
  fileName: string;
  copiedToClipboard: boolean;
}> {
  if (typeof window === 'undefined') {
    throw new Error('Image export is only available in browser environments.');
  }

  const {
    student,
    quotientDetails,
    duration = 'monthly',
    commentsText = '',
    parentMobile = student.parentMobile || '',
    whatsAppMode = 'app',
    triggerWhatsApp = true
  } = params;

  const html2canvas = await loadHtml2Canvas();
  if (!html2canvas) {
    throw new Error('Could not initialize html2canvas library.');
  }

  const overallQuotient = Math.round(quotientDetails.overallQuotient || 0);
  const scoreColor = getDeepScoreColor(overallQuotient);
  const tierLabel = overallQuotient >= 85 
    ? '🌟 Excellent Tier' 
    : overallQuotient >= 60 
      ? '👍 Standard Tier' 
      : '⚠️ Needs Attention';

  const components = quotientDetails.components || [];
  const examComp = components.find((c: any) => c.parameterId === 'exam') || { score: 0, weight: 0.30, details: {} };
  const healthComp = components.find((c: any) => c.parameterId === 'topicHealth') || { score: 0, weight: 0.30, details: {} };
  const practiceComp = components.find((c: any) => c.parameterId === 'practice') || { score: 0, weight: 0.25, details: {} };
  const qualityComp = components.find((c: any) => c.parameterId === 'quality') || { score: 0, weight: 0.15, details: {} };
  const integrityComp = components.find((c: any) => c.parameterId === 'integrity') || { score: 100, weight: 0, details: {} };

  const examScore = Math.round(examComp.score || 0);
  const masteryScore = Math.round(healthComp.score || 0);
  const effortsScore = Math.round(practiceComp.score || 0);
  const qualityScore = Math.round(qualityComp.score || 0);
  const integrityScore = Math.round(integrityComp.score ?? 100);

  const examColor = getDeepScoreColor(examScore);
  const masteryColor = getDeepScoreColor(masteryScore);
  const effortsColor = getDeepScoreColor(effortsScore);
  const qualityColor = getDeepScoreColor(qualityScore);

  const attendanceRate = examComp.details?.attendanceRate ?? 100;
  const totalExams = examComp.details?.totalAssigned ?? 0;
  const completedExams = examComp.details?.completed ?? 0;

  const totalTopics = healthComp.details?.totalTopics ?? 0;
  const masteredTopics = healthComp.details?.masteredCount ?? 0;
  const averageRetention = healthComp.details?.averageRetention ?? 0;

  const totalQuestionsPracticed = practiceComp.details?.totalQuestionsAttempted ?? 0;
  const practicedTopicsCount = practiceComp.details?.topicsAttemptedCount ?? 0;

  const todayFormatted = formatDateDMY(new Date());
  // Remove middle name per user requirement
  const studentName = formatReportStudentName(student.name || 'Student');
  const batchName = student.batchName || 'Academic Batch';

  const durationLabel = typeof duration === 'number'
    ? `Past ${duration} Days`
    : duration === 'weekly'
      ? 'Past 7 Days (Weekly)'
      : 'Past 30 Days (Monthly)';

  // Create offscreen container styled with crisp typography and clean white background
  const container = document.createElement('div');
  container.style.position = 'fixed';
  container.style.left = '0';
  container.style.top = '0';
  container.style.width = '1080px';
  container.style.backgroundColor = '#ffffff';
  container.style.color = '#0f172a';
  container.style.fontFamily = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', 'Noto Sans Devanagari', 'Mangal', sans-serif";
  (container.style as any).webkitFontSmoothing = 'antialiased';
  (container.style as any).mozOsxFontSmoothing = 'grayscale';
  (container.style as any).textRendering = 'optimizeLegibility';
  container.style.padding = '32px 36px';
  container.style.boxSizing = 'border-box';
  container.style.zIndex = '-9999';
  container.style.pointerEvents = 'none';
  container.style.opacity = '1';

  container.innerHTML = `
    <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 16px; padding: 28px 32px; box-shadow: 0 8px 30px rgba(0,0,0,0.06);">
      
      <!-- Top Institute Header -->
      <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #e2e8f0; padding-bottom: 18px; margin-bottom: 20px;">
        <div>
          <div style="color: #92400e; font-size: 15px; font-weight: 900; letter-spacing: 2px; text-transform: uppercase;">
            YASHCOM FOUNDATION, SHEGAON
          </div>
          <div style="color: #0f172a; font-size: 24px; font-weight: 900; margin: 4px 0 6px; letter-spacing: -0.3px;">
            📊 Learning Quotient (LQ) Academic Dossier
          </div>
          <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
            <span style="color: #0369a1; font-size: 20px; font-weight: 900;">${studentName}</span>
            <span style="color: #94a3b8; font-size: 16px;">•</span>
            <span style="background: #f1f5f9; border: 1.5px solid #cbd5e1; color: #1e293b; font-size: 13px; font-weight: 800; padding: 4px 14px; border-radius: 6px;">
              ${batchName}
            </span>
          </div>
        </div>
        <div style="text-align: right;">
          <div style="background: #f1f5f9; border: 1.5px solid #cbd5e1; color: #1e293b; font-size: 12.5px; font-weight: 800; padding: 5px 14px; border-radius: 6px; display: inline-block;">
            📅 ${todayFormatted}
          </div>
          <div style="color: #475569; font-size: 12px; font-weight: 700; margin-top: 6px;">
            Evaluation Window: <strong style="color: #0f172a;">${durationLabel}</strong>
          </div>
        </div>
      </div>

      <!-- Hero Score & 4-Pillar KPI Overview -->
      <div style="display: grid; grid-template-columns: 280px 1fr; gap: 18px; margin-bottom: 20px;">
        
        <!-- Big Radial / Composite Score Card -->
        <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 14px; padding: 20px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
          <div style="font-size: 11.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 8px;">
            Composite Academic Score
          </div>
          <div style="font-size: 54px; font-weight: 900; color: ${scoreColor}; line-height: 1; letter-spacing: -1.5px;">
            ${overallQuotient}<span style="font-size: 22px; color: #64748b; font-weight: 700;">/100</span>
          </div>
          <div style="margin-top: 10px; display: inline-block;">
            ${getScoreChip(overallQuotient, true)}
          </div>
          <div style="font-size: 12px; color: #334155; font-weight: 800; margin-top: 10px;">
            Learning Quotient (LQ) • ${tierLabel}
          </div>
        </div>

        <!-- 4 Quick Highlight Cards -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
          
          <!-- Exam Card -->
          <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 13px; font-weight: 800; color: #1e293b;">🎯 Exam Performance</span>
              ${getScoreChip(examScore, true)}
            </div>
            <div style="font-size: 12px; color: #475569; margin-top: 8px; font-weight: 600;">
              Attendance: <strong style="color: #0f172a;">${attendanceRate}%</strong> • Exams: <strong style="color: #0f172a;">${completedExams}/${totalExams}</strong>
            </div>
          </div>

          <!-- Topic Mastery Card -->
          <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 13px; font-weight: 800; color: #1e293b;">🧠 Topic Mastery</span>
              ${getScoreChip(masteryScore, true)}
            </div>
            <div style="font-size: 12px; color: #475569; margin-top: 8px; font-weight: 600;">
              Mastered: <strong style="color: #0f172a;">${masteredTopics}/${totalTopics} Topics</strong> (${averageRetention}% Retention)
            </div>
          </div>

          <!-- Practice Efforts Card -->
          <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 13px; font-weight: 800; color: #1e293b;">⚡ Practice Efforts</span>
              ${getScoreChip(effortsScore, true)}
            </div>
            <div style="font-size: 12px; color: #475569; margin-top: 8px; font-weight: 600;">
              Attempted: <strong style="color: #0f172a;">${totalQuestionsPracticed} Qs</strong> across <strong style="color: #0f172a;">${practicedTopicsCount} Topics</strong>
            </div>
          </div>

          <!-- Practice Quality Card -->
          <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 13px; font-weight: 800; color: #1e293b;">💎 Practice Quality</span>
              ${getScoreChip(qualityScore, true)}
            </div>
            <div style="font-size: 12px; color: #475569; margin-top: 8px; font-weight: 600;">
              Independent Accuracy Rate: <strong style="color: #0f172a;">${qualityScore}%</strong>
            </div>
          </div>

        </div>
      </div>

      <!-- Core Academic Pillars Progress Breakdown -->
      <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 18px 22px; margin-bottom: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <span style="font-size: 13px; font-weight: 900; color: #0f172a; text-transform: uppercase; letter-spacing: 0.8px;">
            Academic Pillars Breakdown (Weighted Synthesis)
          </span>
          <span style="font-size: 11.5px; color: #475569; font-weight: 700;">
            Sum of weighted contributions = Official LQ
          </span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          
          <!-- Pillar 1: Exam Performance -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12.5px; font-weight: 800; margin-bottom: 5px;">
              <span style="color: #0f172a;">🎯 1. Exam Performance <span style="color: #475569; font-weight: 600;">(Weight: ${Math.round(examComp.weight * 100)}%)</span></span>
              <span style="color: ${examColor}; font-weight: 900;">${examScore}% <span style="color: #475569; font-weight: 700; font-size: 11.5px;">(+${examComp.contribution} pts)</span></span>
            </div>
            <div style="width: 100%; height: 9px; background: #e2e8f0; border-radius: 5px; overflow: hidden;">
              <div style="width: ${examScore}%; height: 100%; background: ${examColor}; border-radius: 5px;"></div>
            </div>
          </div>

          <!-- Pillar 2: Topic Mastery -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12.5px; font-weight: 800; margin-bottom: 5px;">
              <span style="color: #0f172a;">🧠 2. Topic Mastery & Retention <span style="color: #475569; font-weight: 600;">(Weight: ${Math.round(healthComp.weight * 100)}%)</span></span>
              <span style="color: ${masteryColor}; font-weight: 900;">${masteryScore}% <span style="color: #475569; font-weight: 700; font-size: 11.5px;">(+${healthComp.contribution} pts)</span></span>
            </div>
            <div style="width: 100%; height: 9px; background: #e2e8f0; border-radius: 5px; overflow: hidden;">
              <div style="width: ${masteryScore}%; height: 100%; background: ${masteryColor}; border-radius: 5px;"></div>
            </div>
          </div>

          <!-- Pillar 3: Practice Efforts -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12.5px; font-weight: 800; margin-bottom: 5px;">
              <span style="color: #0f172a;">⚡ 3. Practice Efforts & Scope <span style="color: #475569; font-weight: 600;">(Weight: ${Math.round(practiceComp.weight * 100)}%)</span></span>
              <span style="color: ${effortsColor}; font-weight: 900;">${effortsScore}% <span style="color: #475569; font-weight: 700; font-size: 11.5px;">(+${practiceComp.contribution} pts)</span></span>
            </div>
            <div style="width: 100%; height: 9px; background: #e2e8f0; border-radius: 5px; overflow: hidden;">
              <div style="width: ${effortsScore}%; height: 100%; background: ${effortsColor}; border-radius: 5px;"></div>
            </div>
          </div>

          <!-- Pillar 4: Practice Quality -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12.5px; font-weight: 800; margin-bottom: 5px;">
              <span style="color: #0f172a;">💎 4. Practice Quality & Accuracy <span style="color: #475569; font-weight: 600;">(Weight: ${Math.round(qualityComp.weight * 100)}%)</span></span>
              <span style="color: ${qualityColor}; font-weight: 900;">${qualityScore}% <span style="color: #475569; font-weight: 700; font-size: 11.5px;">(+${qualityComp.contribution} pts)</span></span>
            </div>
            <div style="width: 100%; height: 9px; background: #e2e8f0; border-radius: 5px; overflow: hidden;">
              <div style="width: ${qualityScore}%; height: 100%; background: ${qualityColor}; border-radius: 5px;"></div>
            </div>
          </div>

        </div>
      </div>

      <!-- Teacher's Diagnostic Feedback in High-Contrast Bullet List Format -->
      <div style="margin-bottom: 20px; padding: 16px 20px; background: #f8fafc; border: 1.5px solid #cbd5e1; border-left: 5px solid #0284c7; border-radius: 10px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
          <span style="font-size: 20px;">📝</span>
          <span style="font-size: 14px; font-weight: 900; color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
            शिक्षक का शैक्षणिक विश्लेषण एवं मार्गदर्शन (Educator's Diagnostic Guidance):
          </span>
        </div>
        <ul style="margin: 0; padding-left: 20px; color: #1e293b; font-size: 13px; line-height: 1.75; font-weight: 600; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
          <li style="margin-bottom: 6px;">
            <strong style="color: #0f172a;">📌 समतोल शैक्षणिक प्रगती (4-Pillar Synergy):</strong> लर्निंग कोशंट (LQ) हा सराव प्रयत्न (25%), सराव अचूकता (15%), संकल्पना प्रभुत्व (30%) आणि परीक्षा कामगिरी (30%) यांचा वैज्ञानिक निर्देशांक आहे.
          </li>
          <li style="margin-bottom: 6px;">
            <strong style="color: #0f172a;">📌 दैनिक सराव पूर्ण करा (Daily Practice):</strong> सराव प्रयत्न वाढवून सर्व निर्देशित घटक वेळेवर सोडवण्याचा सराव करा.
          </li>
          <li style="margin-bottom: 6px;">
            <strong style="color: #0f172a;">📌 अचूकतेवर भर द्या (Quality over Speed):</strong> घाईगडबडीत उत्तरे देण्यापेक्षा अचूकतेवर आणि संकल्पना समजून घेण्यावर लक्ष केंद्रित करा.
          </li>
          <li>
            <strong style="color: #0f172a;">📌 शिक्षक टीप (Educator Note):</strong> ${commentsText || 'नियमित सराव, वेळेचे व्यवस्थापन आणि त्रुटींचे विश्लेषण याद्वारे संकल्पनांची अचूक समज विकसित करा.'}
          </li>
        </ul>
      </div>

      <!-- Institutional Integrity & Exam Discipline Note -->
      <div style="margin-bottom: 18px; padding: 12px 18px; background: #f0fdf4; border: 1.5px solid #bbf7d0; border-radius: 10px; display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span style="font-size: 20px;">🛡️</span>
          <div>
            <div style="font-size: 12.5px; font-weight: 900; color: #14532d;">
              परीक्षा अनुशासन एवं सत्यनिष्ठा (Exam Integrity): ${integrityScore}%
            </div>
            <div style="font-size: 11.5px; color: #166534; font-weight: 700;">
              प्रॉक्टरिंग अनुपालन मानक • ${integrityScore >= 90 ? 'उत्कृष्ट अनुशासन एवं प्रामाणिकता 🌟' : 'स्क्रीन स्विच एवं ध्यान भटकाव से बचें ⚠️'}
            </div>
          </div>
        </div>
        <div style="background: #dcfce7; border: 1.5px solid #86efac; color: #14532d; font-size: 11.5px; font-weight: 900; padding: 4px 12px; border-radius: 6px;">
          Verified Student Record
        </div>
      </div>

      <!-- Footer -->
      <div style="display: flex; justify-content: space-between; align-items: center; font-size: 11.5px; color: #475569; border-top: 1.5px solid #e2e8f0; padding-top: 12px;">
        <span><strong style="color: #0f172a;">YASHCOM FOUNDATION, SHEGAON</strong> • Academic Excellence & Concept Mastery</span>
        <span>Official Student Performance Dossier • Confidential</span>
      </div>

    </div>
  `;

  document.body.appendChild(container);

  try {
    // Wait for fonts and browser layout to render crisp subpixels
    await new Promise(r => setTimeout(r, 300));

    // Render Ultra HD canvas (scale 3 = 3240px wide!)
    const canvas = await html2canvas(container, {
      scale: 3,
      useCORS: true,
      backgroundColor: '#ffffff',
      logging: false
    });

    // Clean up offscreen container
    document.body.removeChild(container);

    // Convert canvas to Blob
    const blob: Blob = await new Promise((resolve, reject) => {
      canvas.toBlob((b: Blob | null) => {
        if (b) resolve(b);
        else reject(new Error('Failed to generate image blob from canvas.'));
      }, 'image/png');
    });

    const cleanStudentName = studentName.replace(/[^a-zA-Z0-9_\u0900-\u097F\s-]/g, '').trim().replace(/\s+/g, '_');
    const fileName = `${cleanStudentName}_LQ_Report.png`;
    const imageUri = canvas.toDataURL('image/png');

    // 1. Copy lossless PNG to clipboard for instant Ctrl+V
    let copiedToClipboard = false;
    if (navigator.clipboard && typeof ClipboardItem !== 'undefined') {
      try {
        await navigator.clipboard.write([
          new ClipboardItem({ 'image/png': blob })
        ]);
        copiedToClipboard = true;
      } catch (clipErr) {
        console.warn('Clipboard write failed:', clipErr);
      }
    }

    // 2. Trigger lossless PNG download
    const downloadLink = document.createElement('a');
    downloadLink.download = fileName;
    downloadLink.href = imageUri;
    downloadLink.click();

    // 3. Native Mobile / Web Share API check (if supported on mobile/PWA)
    const pngFile = new File([blob], fileName, { type: 'image/png' });
    let sharedViaNative = false;
    if (navigator.canShare && navigator.canShare({ files: [pngFile] })) {
      try {
        await navigator.share({
          files: [pngFile],
          title: `Learning Quotient (LQ) Report - ${studentName}`,
          text: `Dear Parent, please find the Learning Quotient (LQ) Academic Dossier for ${studentName} from Yashcom Foundation, Shegaon.`
        });
        sharedViaNative = true;
      } catch (shareErr) {
        // User may cancel share dialog; proceed to desktop WhatsApp protocol
        console.log('Native share dialog closed or cancelled:', shareErr);
      }
    }

    // 4. If not shared via native share and WhatsApp dispatch requested
    if (!sharedViaNative && triggerWhatsApp && parentMobile) {
      const cleanPhone = parentMobile.replace(/\D/g, '');
      const phoneStr = cleanPhone.length === 10 ? '91' + cleanPhone : cleanPhone;

      const captionText = encodeURIComponent(
        `🙏 *यशकॉम फाउंडेशन, शेगाव (Yashcom Foundation, Shegaon)*\n\n` +
        `प्रिय पालक, *${studentName}* यांचा मासिक शैक्षणिक Learning Quotient (LQ) रिपोर्ट कार्ड सोबत जोडला आहे.\n\n` +
        `📊 *एकूण LQ स्कोअर:* *${overallQuotient}%*\n` +
        `🎯 *परीक्षा सरासरी:* *${examScore}%*\n` +
        `🧠 *संकल्पना प्रभुत्व (Topic Mastery):* *${masteryScore}%*\n` +
        `⚡ *सराव प्रयत्न (Practice Efforts):* *${effortsScore}%*\n\n` +
        `💡 *टीप:* अहवाल कार्ड इमेज कॉपी केली आहे. थेट Paste (Ctrl+V) करून पाठवा.`
      );

      if (whatsAppMode === 'app') {
        const link = document.createElement('a');
        link.href = `whatsapp://send?phone=${phoneStr}&text=${captionText}`;
        document.body.appendChild(link);
        link.click();
        setTimeout(() => {
          try { document.body.removeChild(link); } catch (_) {}
        }, 100);
      } else {
        const url = `https://web.whatsapp.com/send?phone=${phoneStr}&text=${captionText}`;
        window.open(url, 'whatsapp_web_broadcast_tab');
      }
    }

    playNotificationSound();

    if (copiedToClipboard) {
      alert(`✅ Ultra HD WhatsApp Card Exported!\n\n1. Lossless Ultra-HD Image downloaded: ${fileName}\n2. Copied to Clipboard! You can directly press Ctrl + V in WhatsApp.`);
    } else {
      alert(`✅ Ultra HD WhatsApp Card downloaded successfully as ${fileName}!`);
    }

    return { blob, fileName, copiedToClipboard };
  } catch (err: any) {
    if (container.parentNode) {
      document.body.removeChild(container);
    }
    throw err;
  }
}

export interface BatchStudentLqItem {
  id: string;
  name: string;
  studentCode?: string;
  overallQuotient: number | null;
  examScore: number;
  practiceScore: number;
  qualityScore: number;
  healthScore: number;
  integrityScore?: number;
  batchName?: string;
}

export interface BatchLqCardExportParams {
  batchName: string;
  duration?: string | number;
  students: BatchStudentLqItem[];
}

function getBatchStudentLqInsight(s: BatchStudentLqItem): { text: string; bg: string; color: string; border: string } {
  const lq = s.overallQuotient ?? 0;
  const exam = s.examScore ?? 0;
  const efforts = s.practiceScore ?? 0;
  const quality = s.qualityScore ?? 0;
  const mastery = s.healthScore ?? 0;

  if (lq >= 85) {
    return {
      text: '🌟 Outstanding',
      bg: '#dcfce7',
      color: '#14532d',
      border: '#86efac'
    };
  }
  if (efforts >= 70 && mastery >= 70) {
    return {
      text: '⚡ Diligent & Consistent',
      bg: '#e0f2fe',
      color: '#0369a1',
      border: '#7dd3fc'
    };
  }
  if (exam >= 75 && efforts < 20) {
    return {
      text: '⚠️ Strong Exam, Low Practice',
      bg: '#fef3c7',
      color: '#92400e',
      border: '#fcd34d'
    };
  }
  if (efforts >= 50 && quality < 50) {
    return {
      text: '🎯 Practicing, Needs Accuracy',
      bg: '#f3e8ff',
      color: '#6b21a8',
      border: '#d8b4fe'
    };
  }
  if (lq >= 60) {
    return {
      text: '🟡 Steady Progress',
      bg: '#fef9c3',
      color: '#854d0e',
      border: '#fde047'
    };
  }
  return {
    text: '🚨 Needs Daily Practice',
    bg: '#fee2e2',
    color: '#991b1b',
    border: '#fca5a5'
  };
}

/**
 * Generates an Ultra HD lossless WhatsApp summary card for an entire batch of students
 * in the Learning Quotient report with pedagogical insights, copies to clipboard, and downloads.
 */
export async function exportBatchLqCardImage(params: BatchLqCardExportParams): Promise<{
  blob: Blob;
  fileName: string;
  copiedToClipboard: boolean;
}> {
  if (typeof window === 'undefined') {
    throw new Error('Image export is only available in browser environments.');
  }

  const { batchName, duration = 'monthly', students } = params;

  if (students.length === 0) {
    alert('No students to export in this batch.');
    throw new Error('No students to export.');
  }

  const html2canvas = await loadHtml2Canvas();
  if (!html2canvas) {
    throw new Error('Could not initialize html2canvas library.');
  }

  // Sort descending by overallQuotient
  const sorted = [...students].sort((a, b) => (b.overallQuotient ?? 0) - (a.overallQuotient ?? 0));
  const totalStudents = sorted.length;
  const batchAvgLQ = Math.round(sorted.reduce((sum, s) => sum + (s.overallQuotient ?? 0), 0) / (totalStudents || 1));
  const topLQ = sorted.length > 0 ? (sorted[0].overallQuotient ?? 0) : 0;
  const avgExam = Math.round(sorted.reduce((sum, s) => sum + (s.examScore ?? 0), 0) / (totalStudents || 1));
  const avgEfforts = Math.round(sorted.reduce((sum, s) => sum + (s.practiceScore ?? 0), 0) / (totalStudents || 1));
  const avgQuality = Math.round(sorted.reduce((sum, s) => sum + (s.qualityScore ?? 0), 0) / (totalStudents || 1));

  const todayFormatted = formatDateDMY(new Date());
  const durationLabel = typeof duration === 'number'
    ? `Past ${duration} Days`
    : duration === 'weekly'
      ? 'Weekly Evaluation'
      : 'Monthly Evaluation';

  // Create offscreen container styled with crisp typography and clean white background
  const container = document.createElement('div');
  container.style.position = 'fixed';
  container.style.left = '0';
  container.style.top = '0';
  container.style.width = '1080px';
  container.style.backgroundColor = '#ffffff';
  container.style.color = '#0f172a';
  container.style.fontFamily = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', 'Noto Sans Devanagari', 'Mangal', sans-serif";
  (container.style as any).webkitFontSmoothing = 'antialiased';
  (container.style as any).mozOsxFontSmoothing = 'grayscale';
  (container.style as any).textRendering = 'optimizeLegibility';
  container.style.padding = '28px 32px';
  container.style.boxSizing = 'border-box';
  container.style.zIndex = '-9999';
  container.style.pointerEvents = 'none';
  container.style.opacity = '1';

  // Build table rows with high-contrast score chips and first+last name formatting
  const rowsHtml = sorted.map((s, idx) => {
    const rank = idx + 1;
    const rankBadge = rank === 1 ? '🥇 1' : rank === 2 ? '🥈 2' : rank === 3 ? '🥉 3' : `<span style="display:inline-block; min-width: 24px; padding: 2px 6px; border-radius: 4px; background: #e2e8f0; color: #1e293b; font-weight: 800; font-size: 12px;">${rank}</span>`;
    const displayName = formatReportStudentName(s.name);
    const rowBg = idx % 2 === 0 ? '#ffffff' : '#f8fafc';
    const insight = getBatchStudentLqInsight(s);

    return `
      <tr style="border-bottom: 1px solid #e2e8f0; height: 42px; background-color: ${rowBg};">
        <td style="padding: 8px 10px; text-align: center; font-weight: 900; font-size: 13.5px; color: #0f172a;">${rankBadge}</td>
        <td style="padding: 8px 14px; font-weight: 800; font-size: 14.5px; color: #0f172a; white-space: nowrap;">
          ${displayName}
        </td>
        <td style="padding: 8px 10px; text-align: center; white-space: nowrap;">
          ${getScoreChip(s.overallQuotient, true)}
        </td>
        <td style="padding: 8px 10px; text-align: center; white-space: nowrap;">
          ${getScoreChip(s.examScore)}
        </td>
        <td style="padding: 8px 10px; text-align: center; white-space: nowrap;">
          ${getScoreChip(s.healthScore)}
        </td>
        <td style="padding: 8px 10px; text-align: center; white-space: nowrap;">
          ${getScoreChip(s.practiceScore)}
        </td>
        <td style="padding: 8px 10px; text-align: center; white-space: nowrap;">
          ${getScoreChip(s.qualityScore)}
        </td>
        <td style="padding: 8px 12px; text-align: center; white-space: nowrap;">
          <span style="display:inline-block; padding: 4px 10px; border-radius: 6px; font-size: 11.5px; font-weight: 800; background: ${insight.bg}; color: ${insight.color}; border: 1.5px solid ${insight.border}; white-space: nowrap;">
            ${insight.text}
          </span>
        </td>
      </tr>
    `;
  }).join('');

  container.innerHTML = `
    <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 24px 28px; box-shadow: 0 8px 30px rgba(0,0,0,0.06);">
      
      <!-- Header -->
      <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #e2e8f0; padding-bottom: 16px; margin-bottom: 16px;">
        <div>
          <div style="color: #92400e; font-size: 15px; font-weight: 900; letter-spacing: 2px; text-transform: uppercase;">
            YASHCOM FOUNDATION, SHEGAON
          </div>
          <div style="color: #0f172a; font-size: 24px; font-weight: 900; margin: 3px 0 5px; letter-spacing: -0.3px;">
            🏆 Learning Quotient (LQ) Academic Report
          </div>
          <div style="color: #0369a1; font-size: 16px; font-weight: 800;">
            ${batchName}
          </div>
        </div>
        <div style="text-align: right;">
          <div style="background: #f1f5f9; border: 1.5px solid #cbd5e1; color: #1e293b; font-size: 12.5px; font-weight: 800; padding: 5px 14px; border-radius: 6px; display: inline-block;">
            📅 ${todayFormatted}
          </div>
          <div style="color: #475569; font-size: 12px; font-weight: 700; margin-top: 5px;">
            Evaluation Scope: <strong style="color:#0f172a;">${durationLabel}</strong>
          </div>
        </div>
      </div>

      <!-- KPI Summary Cards -->
      <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-bottom: 20px;">
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 26px; font-weight: 900; color: #0f172a; line-height: 1.1;">${totalStudents}</div>
          <div style="font-size: 11.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px;">Students</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 26px; font-weight: 900; color: ${getDeepScoreColor(batchAvgLQ)}; line-height: 1.1;">${batchAvgLQ}%</div>
          <div style="font-size: 11.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px;">Batch Avg LQ</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 26px; font-weight: 900; color: #047857; line-height: 1.1;">${topLQ}%</div>
          <div style="font-size: 11.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px;">Highest LQ</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 26px; font-weight: 900; color: #0369a1; line-height: 1.1;">${avgExam}%</div>
          <div style="font-size: 11.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px;">Exam Avg</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 26px; font-weight: 900; color: #047857; line-height: 1.1;">${avgEfforts}%</div>
          <div style="font-size: 11.5px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.6px; margin-top: 4px;">Practice Avg</div>
        </div>
      </div>

      <!-- Table with Executive Dark Navy Header for Maximum Legibility -->
      <table style="width: 100%; border-collapse: collapse; border: 1.5px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
        <thead>
          <tr style="background: #0f172a; color: #ffffff; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px; height: 42px;">
            <th style="padding: 10px 10px; text-align: center; width: 60px;">Rank</th>
            <th style="padding: 10px 14px; text-align: left;">Student Name</th>
            <th style="padding: 10px 10px; text-align: center; width: 100px;">LQ Score</th>
            <th style="padding: 10px 10px; text-align: center; width: 95px;">Exam Avg</th>
            <th style="padding: 10px 10px; text-align: center; width: 95px;">Mastery</th>
            <th style="padding: 10px 10px; text-align: center; width: 95px;">Efforts</th>
            <th style="padding: 10px 10px; text-align: center; width: 95px;">Quality</th>
            <th style="padding: 10px 12px; text-align: center; width: 210px;">Academic Insight</th>
          </tr>
        </thead>
        <tbody>
          ${rowsHtml}
        </tbody>
      </table>

      <!-- Educational Guidance Banner (Hindi / Marathi) - High Contrast Bullet List -->
      <div style="margin-top: 20px; padding: 16px 20px; background: #f8fafc; border: 1.5px solid #cbd5e1; border-left: 5px solid #0284c7; border-radius: 10px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
          <span style="font-size: 20px; line-height: 1;">💡</span>
          <strong style="color: #0f172a; font-size: 14.5px; font-weight: 900; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
            शैक्षणिक विश्लेषण एवं मार्गदर्शन (Academic Guidance & Key Insights):
          </strong>
        </div>
        <ul style="margin: 0; padding-left: 20px; color: #1e293b; font-size: 13px; line-height: 1.75; font-weight: 600; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
          <li style="margin-bottom: 6px;">
            <strong style="color: #0f172a;">📌 समग्र शैक्षणिक निर्देशांक (Holistic Synthesis):</strong> लर्निंग कोशंट (LQ) हा केवळ परीक्षेच्या गुणांचा नव्हे, तर नियमित सराव प्रयत्न (25%), सराव अचूकता (15%), संकल्पना प्रभुत्व (30%) आणि परीक्षा कामगिरी (30%) यांचा वैज्ञानिक ताळेबंद आहे.
          </li>
          <li style="margin-bottom: 6px;">
            <strong style="color: #0f172a;">📌 नियमित दैनिक सराव (Daily Practice Discipline):</strong> ज्या विद्यार्थ्यांचे सराव प्रयत्न कमी आहेत, त्यांनी दररोज स्वतःहून सराव पूर्ण करणे आवश्यक आहे.
          </li>
          <li style="margin-bottom: 6px;">
            <strong style="color: #0f172a;">📌 अचूकतेवर भर (Quality & Accuracy):</strong> घाईघाईत प्रश्न सोडवण्यापेक्षा प्रत्येक संकल्पना नीट समजून अचूक उत्तर देण्याचा प्रयत्न करा.
          </li>
          <li>
            <strong style="color: #0f172a;">📌 सातत्यपूर्ण प्रयत्नांतूनच प्रभुत्व (Continuous Growth):</strong> नियमित सराव आणि वेळेवर शंकांचे निरसन यामुळेच सर्वोच्च शैक्षणिक स्तर गाठता येतो.
          </li>
        </ul>
      </div>

      <!-- Footer -->
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 16px; font-size: 11.5px; color: #475569; border-top: 1.5px solid #e2e8f0; padding-top: 12px;">
        <span><strong style="color: #0f172a;">YASHCOM FOUNDATION, SHEGAON</strong> • Academic Evaluation Portal</span>
        <span>Verified Batch Academic Performance Summary • Confidential</span>
      </div>

    </div>
  `;

  document.body.appendChild(container);

  try {
    await new Promise(r => setTimeout(r, 300));

    const canvas = await html2canvas(container, {
      scale: 3,
      useCORS: true,
      backgroundColor: '#ffffff',
      logging: false
    });

    document.body.removeChild(container);

    const blob: Blob = await new Promise((resolve, reject) => {
      canvas.toBlob((b: Blob | null) => {
        if (b) resolve(b);
        else reject(new Error('Failed to generate image blob from canvas.'));
      }, 'image/png');
    });

    const cleanBatch = batchName.replace(/[^a-zA-Z0-9_-]/g, '_');
    const fileName = `LQ_Batch_Summary_${cleanBatch}.png`;
    const imageUri = canvas.toDataURL('image/png');

    let copiedToClipboard = false;
    if (navigator.clipboard && typeof ClipboardItem !== 'undefined') {
      try {
        await navigator.clipboard.write([
          new ClipboardItem({ 'image/png': blob })
        ]);
        copiedToClipboard = true;
      } catch (clipErr) {
        console.warn('Clipboard write failed:', clipErr);
      }
    }

    const downloadLink = document.createElement('a');
    downloadLink.download = fileName;
    downloadLink.href = imageUri;
    downloadLink.click();

    playNotificationSound();

    if (copiedToClipboard) {
      alert(`✅ Ultra HD WhatsApp Batch Card Exported!\n\n1. Lossless Ultra-HD Image downloaded: ${fileName}\n2. Copied to Clipboard! You can directly press Ctrl + V in WhatsApp Web.`);
    } else {
      alert(`✅ Ultra HD WhatsApp Batch Card downloaded successfully as ${fileName}!`);
    }

    return { blob, fileName, copiedToClipboard };
  } catch (err: any) {
    if (container.parentNode) {
      document.body.removeChild(container);
    }
    throw err;
  }
}

export interface BatchPracticeTracksExportParams {
  batchName: string;
  students: Array<{
    name: string;
    studentCode: string;
    [key: string]: any;
  }>;
  practiceStats: {
    [studentCode: string]: {
      totalSessions: number;
      questionsAttempted: number;
      avgScore: number;
      examAvg?: number;
      lastActive: string | null;
    };
  };
  masteryStats: {
    [studentCode: string]: {
      avgMastery: number;
      avgQuality?: number;
      efforts?: number;
      totalAssigned?: number;
      mastered: number;
      practicing: number;
      needsAttention: number;
    };
  };
  formatDateDMY?: (date: any) => string;
}

/**
 * Generates an Ultra HD lossless WhatsApp summary card for an entire batch's Practice Tracks
 * with uniform assigned topics count, efforts column, and status breakdown explanations for parents.
 */
export async function exportBatchPracticeTracksImage(params: BatchPracticeTracksExportParams): Promise<{
  blob: Blob;
  fileName: string;
  copiedToClipboard: boolean;
}> {
  if (typeof window === 'undefined') {
    throw new Error('Image export is only available in browser environments.');
  }

  const { batchName, students, practiceStats, masteryStats } = params;

  if (students.length === 0) {
    alert('No students to export in this batch.');
    throw new Error('No students to export.');
  }

  const html2canvas = await loadHtml2Canvas();
  if (!html2canvas) {
    throw new Error('Could not initialize html2canvas library.');
  }

  // Determine the uniform assigned topics count across the batch
  const batchMaxTopics = Math.max(...students.map(s => {
    const m = masteryStats[s.studentCode];
    return m ? (m.totalAssigned || (m.mastered + m.practicing + m.needsAttention)) : 0;
  }), 0);

  // Sort descending by avgMastery, then by questionsAttempted
  const sorted = [...students].sort((a, b) => {
    const ma = masteryStats[a.studentCode]?.avgMastery || 0;
    const mb = masteryStats[b.studentCode]?.avgMastery || 0;
    if (mb !== ma) return mb - ma;
    const qa = practiceStats[a.studentCode]?.questionsAttempted || 0;
    const qb = practiceStats[b.studentCode]?.questionsAttempted || 0;
    return qb - qa;
  });

  const totalStudents = sorted.length;
  const totalSessions = sorted.reduce((sum, s) => sum + (practiceStats[s.studentCode]?.totalSessions || 0), 0);
  const totalQuestions = sorted.reduce((sum, s) => sum + (practiceStats[s.studentCode]?.questionsAttempted || 0), 0);
  const batchAvgMastery = Math.round(sorted.reduce((sum, s) => sum + (masteryStats[s.studentCode]?.avgMastery || 0), 0) / (totalStudents || 1));
  const batchAvgQuality = Math.round(sorted.reduce((sum, s) => sum + (masteryStats[s.studentCode]?.avgQuality ?? 100), 0) / (totalStudents || 1));
  const batchAvgEfforts = Math.round(sorted.reduce((sum, s) => {
    const p = practiceStats[s.studentCode]?.totalSessions || 0;
    const m = masteryStats[s.studentCode];
    const t = batchMaxTopics > 0 ? batchMaxTopics : (m?.totalAssigned || 1);
    const eff = m?.efforts ?? Math.min(100, Math.round((p / t) * 100));
    return sum + eff;
  }, 0) / (totalStudents || 1));

  const todayFormatted = formatDateDMY(new Date());

  const container = document.createElement('div');
  container.style.position = 'fixed';
  container.style.left = '0';
  container.style.top = '0';
  container.style.width = '1080px';
  container.style.backgroundColor = '#ffffff';
  container.style.color = '#0f172a';
  container.style.fontFamily = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', 'Noto Sans Devanagari', 'Mangal', sans-serif";
  (container.style as any).webkitFontSmoothing = 'antialiased';
  (container.style as any).mozOsxFontSmoothing = 'grayscale';
  (container.style as any).textRendering = 'optimizeLegibility';
  container.style.padding = '28px 32px';
  container.style.boxSizing = 'border-box';
  container.style.zIndex = '-9999';
  container.style.pointerEvents = 'none';
  container.style.opacity = '1';

  const rowsHtml = sorted.map((s, idx) => {
    const rank = idx + 1;
    const rankBadge = rank === 1 ? '🥇 1' : rank === 2 ? '🥈 2' : rank === 3 ? '🥉 3' : `<span style="display:inline-block; min-width: 24px; padding: 2px 6px; border-radius: 4px; background: #e2e8f0; color: #1e293b; font-weight: 800; font-size: 12px;">${rank}</span>`;
    const displayName = formatReportStudentName(s.name);
    const rowBg = idx % 2 === 0 ? '#ffffff' : '#f8fafc';

    const pStat = practiceStats[s.studentCode] || { totalSessions: 0, questionsAttempted: 0, avgScore: 0, lastActive: null };
    const mStat = masteryStats[s.studentCode] || { avgMastery: 0, avgQuality: 100, efforts: 0, mastered: 0, practicing: 0, needsAttention: 0, totalAssigned: 0 };
    
    // Uniform batch topic harmonization
    const rawAssigned = mStat.mastered + mStat.practicing + mStat.needsAttention;
    const targetTotal = batchMaxTopics > 0 ? batchMaxTopics : (mStat.totalAssigned || rawAssigned);
    const adjustedNeedsAttention = mStat.needsAttention + Math.max(0, targetTotal - rawAssigned);
    const quality = mStat.avgQuality ?? 100;
    const efforts = mStat.efforts ?? (targetTotal > 0 ? Math.min(100, Math.round((pStat.totalSessions / targetTotal) * 100)) : 0);

    let lastActiveText = 'Never';
    if (pStat.lastActive) {
      try {
        lastActiveText = formatDateDMY(pStat.lastActive);
      } catch {
        lastActiveText = pStat.lastActive.split('T')[0] || 'Recent';
      }
    }

    return `
      <tr style="border-bottom: 1px solid #e2e8f0; height: 44px; background-color: ${rowBg};">
        <td style="padding: 8px 10px; text-align: center; font-weight: 900; font-size: 13.5px; color: #0f172a;">${rankBadge}</td>
        <td style="padding: 8px 14px; font-weight: 800; font-size: 14.5px; color: #0f172a; white-space: nowrap;">
          ${displayName}
        </td>
        <td style="padding: 8px 8px; text-align: center; font-weight: 800; font-size: 13.5px; color: #0f172a;">
          ${pStat.totalSessions}
        </td>
        <td style="padding: 8px 8px; text-align: center; font-weight: 800; font-size: 13.5px; color: #0f172a;">
          ${pStat.questionsAttempted}
        </td>
        <td style="padding: 8px 8px; text-align: center; white-space: nowrap;">
          ${pStat.totalSessions > 0 ? getScoreChip(pStat.avgScore) : `<span style="color:#94a3b8; font-weight:700;">—</span>`}
        </td>
        <td style="padding: 8px 8px; text-align: center; white-space: nowrap;">
          ${getScoreChip(mStat.avgMastery, true)}
        </td>
        <td style="padding: 8px 8px; text-align: center; white-space: nowrap;">
          ${getScoreChip(efforts)}
        </td>
        <td style="padding: 8px 8px; text-align: center; white-space: nowrap;">
          ${getScoreChip(quality)}
        </td>
        <td style="padding: 8px 12px; text-align: center; white-space: nowrap;">
          <div style="display: inline-flex; align-items: center; gap: 5px;">
            <span style="display:inline-block; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: 800; background: #dcfce7; color: #14532d; border: 1px solid #86efac;" title="Mastered (>=90%)">
              🟢 ${mStat.mastered}
            </span>
            <span style="display:inline-block; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: 800; background: #fef3c7; color: #92400e; border: 1px solid #fcd34d;" title="In Progress (50-89%)">
              🟡 ${mStat.practicing}
            </span>
            <span style="display:inline-block; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: 800; background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5;" title="Needs Attention / Unattempted">
              🔴 ${adjustedNeedsAttention}
            </span>
          </div>
          <div style="font-size: 10.5px; font-weight: 700; color: #64748b; margin-top: 2px;">
            एकूण: <strong>${targetTotal}</strong> घटक
          </div>
        </td>
        <td style="padding: 8px 10px; text-align: center; font-size: 12px; font-weight: 700; color: #475569; white-space: nowrap;">
          ${lastActiveText}
        </td>
      </tr>
    `;
  }).join('');

  container.innerHTML = `
    <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 24px 28px; box-shadow: 0 8px 30px rgba(0,0,0,0.06);">
      
      <!-- Header -->
      <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #e2e8f0; padding-bottom: 16px; margin-bottom: 16px;">
        <div>
          <div style="color: #92400e; font-size: 15px; font-weight: 900; letter-spacing: 2px; text-transform: uppercase;">
            YASHCOM FOUNDATION, SHEGAON
          </div>
          <div style="color: #0f172a; font-size: 24px; font-weight: 900; margin: 3px 0 5px; letter-spacing: -0.3px;">
            🏋️ Daily Practice & Topic Mastery Dossier
          </div>
          <div style="color: #0369a1; font-size: 16px; font-weight: 800;">
            ${batchName}
          </div>
        </div>
        <div style="text-align: right;">
          <div style="background: #f1f5f9; border: 1.5px solid #cbd5e1; color: #1e293b; font-size: 12.5px; font-weight: 800; padding: 5px 14px; border-radius: 6px; display: inline-block;">
            📅 ${todayFormatted}
          </div>
          <div style="color: #475569; font-size: 12px; font-weight: 700; margin-top: 5px;">
            Syllabus Coverage: <strong style="color:#0f172a;">${batchMaxTopics} Assigned Topics</strong>
          </div>
        </div>
      </div>

      <!-- KPI Summary Cards (6-pillar view matching LQ standards) -->
      <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin-bottom: 20px;">
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 24px; font-weight: 900; color: #0f172a; line-height: 1.1;">${totalStudents}</div>
          <div style="font-size: 11px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Students</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 24px; font-weight: 900; color: #0369a1; line-height: 1.1;">${totalSessions}</div>
          <div style="font-size: 11px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Total Sessions</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 24px; font-weight: 900; color: #047857; line-height: 1.1;">${totalQuestions}</div>
          <div style="font-size: 11px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Questions Solved</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 24px; font-weight: 900; color: ${getDeepScoreColor(batchAvgMastery)}; line-height: 1.1;">${batchAvgMastery}%</div>
          <div style="font-size: 11px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Batch Mastery</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 24px; font-weight: 900; color: ${getDeepScoreColor(batchAvgEfforts)}; line-height: 1.1;">${batchAvgEfforts}%</div>
          <div style="font-size: 11px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Batch Efforts</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 24px; font-weight: 900; color: ${getDeepScoreColor(batchAvgQuality)}; line-height: 1.1;">${batchAvgQuality}%</div>
          <div style="font-size: 11px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Avg Accuracy</div>
        </div>
      </div>

      <!-- Table with Executive Dark Navy Header for Maximum Legibility -->
      <table style="width: 100%; border-collapse: collapse; border: 1.5px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
        <thead>
          <tr style="background: #0f172a; color: #ffffff; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px; height: 42px;">
            <th style="padding: 10px 10px; text-align: center; width: 50px;">Rank</th>
            <th style="padding: 10px 14px; text-align: left;">Student Name</th>
            <th style="padding: 10px 8px; text-align: center; width: 70px;">Sessions</th>
            <th style="padding: 10px 8px; text-align: center; width: 80px;">Questions</th>
            <th style="padding: 10px 8px; text-align: center; width: 80px;">Avg Score</th>
            <th style="padding: 10px 8px; text-align: center; width: 90px;">Mastery</th>
            <th style="padding: 10px 8px; text-align: center; width: 85px;">Efforts</th>
            <th style="padding: 10px 8px; text-align: center; width: 85px;">Quality</th>
            <th style="padding: 10px 12px; text-align: center; width: 195px;">Topic Status (Assigned)</th>
            <th style="padding: 10px 10px; text-align: center; width: 95px;">Last Active</th>
          </tr>
        </thead>
        <tbody>
          ${rowsHtml}
        </tbody>
      </table>

      <!-- Pedagogical Explanation & Parent Guidance Banner (Hindi / Marathi) - High Contrast Bullet List -->
      <div style="margin-top: 20px; padding: 18px 22px; background: #f8fafc; border: 1.5px solid #cbd5e1; border-left: 5px solid #0284c7; border-radius: 10px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
          <span style="font-size: 22px; line-height: 1;">💡</span>
          <strong style="color: #0f172a; font-size: 15px; font-weight: 900; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
            पालकांसाठी अत्यंत महत्त्वाचे स्पष्टीकरण व मार्गदर्शन (Topic Status & Parent Guidance):
          </strong>
        </div>
        <ul style="margin: 0; padding-left: 20px; color: #1e293b; font-size: 13.5px; line-height: 1.8; font-weight: 600; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
          <li style="margin-bottom: 8px;">
            <strong style="color: #0f172a;">📌 एकूण नेमून दिलेले अभ्यासक्रम घटक (${batchMaxTopics} घटक):</strong> या बॅचसाठी शिकवून पूर्ण झालेले व सरावासाठी उपलब्ध असलेले एकूण घटक = 🟢 पूर्ण प्रभुत्व + 🟡 सराव सुरू + 🔴 विशेष लक्ष आवश्यक. बॅचमधील सर्व विद्यार्थ्यांना समान अभ्यासक्रम लागू आहे.
          </li>
          <li style="margin-bottom: 8px;">
            <strong style="color: #0369a1;">📌 सराव प्रयत्न (Efforts %):</strong> एकूण नेमून दिलेल्या ${batchMaxTopics} घटकांच्या तुलनेत विद्यार्थ्याने पूर्ण केलेल्या सराव सेट्सचे प्रमाण. बोर्ड परीक्षेत ९०%+ प्रभुत्व मिळवण्यासाठी १००% सराव प्रयत्न अनिवार्य आहेत.
          </li>
          <li style="margin-bottom: 8px;">
            <strong style="color: #14532d;">🟢 Mastered (संकल्पना प्रभुत्व):</strong> ज्या घटकांमध्ये विद्यार्थ्याने <strong>≥ ९०% अचूकता</strong> आणि किमान आवश्यक प्रश्नांचा सराव यशस्वीरीत्या पूर्ण केला आहे. या घटकांची तयारी उत्कृष्ट आहे.
          </li>
          <li style="margin-bottom: 8px;">
            <strong style="color: #92400e;">🟡 In Progress / Practicing (सराव सुरू):</strong> या घटकांचा सराव चालू असून अचूकता ५०% ते ८९% दरम्यान आहे. बोर्ड परीक्षेच्या दृष्टीने अजून २ ते ३ सराव सेट्स सोडवून ९०%+ अचूकता संपादन करणे आवश्यक आहे.
          </li>
          <li style="margin-bottom: 8px;">
            <strong style="color: #991b1b;">🔴 Needs Attention / Unattempted (विशेष लक्ष द्या / सराव बाकी):</strong> ज्या घटकांमध्ये अचूकता ५०% पेक्षा कमी आहे किंवा अद्याप विद्यार्थ्याने सराव सुरूच केलेला नाही. हे घटक तत्काळ सोडवून घेणे अनिवार्य आहे.
          </li>
          <li>
            <strong style="color: #0f172a;">📌 पालकांची भूमिका (Parent Action Plan):</strong> बोर्ड परीक्षेत ९०%+ गुण मिळवण्यासाठी विद्यार्थ्याने दररोज घरी न चुकता किमान २ ते ३ सराव सेट्स (१५-२० प्रश्न) सोडवणे आणि सर्व 🟡 व 🔴 घटकांना 🟢 (Mastered) मध्ये रूपांतरित करणे आवश्यक आहे.
          </li>
        </ul>
      </div>

      <!-- Footer -->
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 16px; font-size: 11.5px; color: #475569; border-top: 1.5px solid #e2e8f0; padding-top: 12px;">
        <span><strong style="color: #0f172a;">YASHCOM FOUNDATION, SHEGAON</strong> • Practice Track Evaluation Portal</span>
        <span>Verified Batch Practice & Topic Mastery Summary • Confidential</span>
      </div>

    </div>
  `;

  document.body.appendChild(container);

  try {
    await new Promise(r => setTimeout(r, 300));

    const canvas = await html2canvas(container, {
      scale: 3,
      useCORS: true,
      backgroundColor: '#ffffff',
      logging: false
    });

    document.body.removeChild(container);

    const blob: Blob = await new Promise((resolve, reject) => {
      canvas.toBlob((b: Blob | null) => {
        if (b) resolve(b);
        else reject(new Error('Failed to generate image blob from canvas.'));
      }, 'image/png');
    });

    const cleanBatch = batchName.replace(/[^a-zA-Z0-9_-]/g, '_');
    const fileName = `Practice_Tracks_${cleanBatch}.png`;
    const imageUri = canvas.toDataURL('image/png');

    let copiedToClipboard = false;
    if (navigator.clipboard && typeof ClipboardItem !== 'undefined') {
      try {
        await navigator.clipboard.write([
          new ClipboardItem({ 'image/png': blob })
        ]);
        copiedToClipboard = true;
      } catch (clipErr) {
        console.warn('Clipboard write failed:', clipErr);
      }
    }

    const downloadLink = document.createElement('a');
    downloadLink.download = fileName;
    downloadLink.href = imageUri;
    downloadLink.click();

    playNotificationSound();

    if (copiedToClipboard) {
      alert(`✅ Ultra HD WhatsApp Practice Card Exported!\n\n1. Lossless Ultra-HD Image downloaded: ${fileName}\n2. Copied to Clipboard! You can directly press Ctrl + V in WhatsApp Web.`);
    } else {
      alert(`✅ Ultra HD WhatsApp Practice Card downloaded successfully as ${fileName}!`);
    }

    return { blob, fileName, copiedToClipboard };
  } catch (err: any) {
    if (container.parentNode) {
      document.body.removeChild(container);
    }
    throw err;
  }
}

export interface StudentPracticeCardExportParams {
  student: {
    name: string;
    studentCode: string;
    batchName?: string;
  };
  practiceStats?: {
    totalSessions: number;
    questionsAttempted: number;
    avgScore: number;
    lastActive: string | null;
  };
  masteryStats?: {
    avgMastery: number;
    avgQuality?: number;
    mastered: number;
    practicing: number;
    needsAttention: number;
  };
  topicDetails?: {
    mastered: any[];
    practicing: any[];
    needsAttention: any[];
  };
  formatDateDMY?: (date: any) => string;
}

/**
 * Generates an Ultra HD lossless WhatsApp report card for an individual student's Practice & Topic Mastery
 * with detailed topic breakdowns and parent guidance.
 */
export async function exportStudentPracticeCardImage(params: StudentPracticeCardExportParams): Promise<{
  blob: Blob;
  fileName: string;
  copiedToClipboard: boolean;
}> {
  if (typeof window === 'undefined') {
    throw new Error('Image export is only available in browser environments.');
  }

  const { student, practiceStats, masteryStats, topicDetails } = params;

  const html2canvas = await loadHtml2Canvas();
  if (!html2canvas) {
    throw new Error('Could not initialize html2canvas library.');
  }

  const displayName = formatReportStudentName(student.name);
  const batchName = student.batchName || 'Academic Batch';
  const todayFormatted = formatDateDMY(new Date());

  const pStat = practiceStats || { totalSessions: 0, questionsAttempted: 0, avgScore: 0, lastActive: null };
  const mStat = masteryStats || {
    avgMastery: 0,
    avgQuality: 100,
    mastered: topicDetails?.mastered.length || 0,
    practicing: topicDetails?.practicing.length || 0,
    needsAttention: topicDetails?.needsAttention.length || 0
  };

  const masteredCount = topicDetails?.mastered.length ?? mStat.mastered;
  const practicingCount = topicDetails?.practicing.length ?? mStat.practicing;
  const needsAttentionCount = topicDetails?.needsAttention.length ?? mStat.needsAttention;
  const totalAssigned = masteredCount + practicingCount + needsAttentionCount;

  const masteredPct = totalAssigned > 0 ? Math.round((masteredCount / totalAssigned) * 100) : 0;
  const practicingPct = totalAssigned > 0 ? Math.round((practicingCount / totalAssigned) * 100) : 0;
  const needsAttentionPct = totalAssigned > 0 ? Math.round((needsAttentionCount / totalAssigned) * 100) : 0;

  // Build topic list if details exist
  let topicRowsHtml = '';
  if (topicDetails) {
    const allTopics = [
      ...topicDetails.mastered.map(t => ({ ...t, statusGroup: 'mastered' })),
      ...topicDetails.practicing.map(t => ({ ...t, statusGroup: 'practicing' })),
      ...topicDetails.needsAttention.map(t => ({ ...t, statusGroup: 'needsAttention' }))
    ];

    topicRowsHtml = allTopics.map((t, idx) => {
      const rowBg = idx % 2 === 0 ? '#ffffff' : '#f8fafc';
      let statusBadge = '';
      if (t.statusGroup === 'mastered') {
        statusBadge = `<span style="display:inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11.5px; font-weight: 800; background: #dcfce7; color: #14532d; border: 1px solid #86efac;">🟢 Mastered</span>`;
      } else if (t.statusGroup === 'practicing') {
        statusBadge = `<span style="display:inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11.5px; font-weight: 800; background: #fef3c7; color: #92400e; border: 1px solid #fcd34d;">🟡 In Progress</span>`;
      } else {
        statusBadge = `<span style="display:inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11.5px; font-weight: 800; background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5;">🔴 Needs Care</span>`;
      }

      const chapterStr = t.chapterName ? `${t.chapterName}` : (t.subjectName || '');
      const guidance = t.expText || (t.statusGroup === 'mastered' ? 'Concept thoroughly mastered' : t.statusGroup === 'practicing' ? 'Needs 1-2 more practice sets for mastery' : 'High priority revision & practice needed');

      return `
        <tr style="border-bottom: 1px solid #e2e8f0; height: 38px; background-color: ${rowBg}; font-size: 12.5px;">
          <td style="padding: 6px 10px; font-weight: 700; color: #475569;">${chapterStr}</td>
          <td style="padding: 6px 12px; font-weight: 800; color: #0f172a;">${t.topicName || t.topicCode}</td>
          <td style="padding: 6px 8px; text-align: center; white-space: nowrap;">
            ${getScoreChip(t.mastery !== undefined ? t.mastery : 0)}
          </td>
          <td style="padding: 6px 8px; text-align: center; font-weight: 800; color: #0f172a;">
            ${t.attempts || t.practiceCount || 0} Qs
          </td>
          <td style="padding: 6px 10px; text-align: center; white-space: nowrap;">
            ${statusBadge}
          </td>
          <td style="padding: 6px 12px; font-size: 11.5px; font-weight: 600; color: #334155;">
            ${guidance}
          </td>
        </tr>
      `;
    }).join('');
  }

  const container = document.createElement('div');
  container.style.position = 'fixed';
  container.style.left = '0';
  container.style.top = '0';
  container.style.width = '1080px';
  container.style.backgroundColor = '#ffffff';
  container.style.color = '#0f172a';
  container.style.fontFamily = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', 'Noto Sans Devanagari', 'Mangal', sans-serif";
  (container.style as any).webkitFontSmoothing = 'antialiased';
  (container.style as any).mozOsxFontSmoothing = 'grayscale';
  (container.style as any).textRendering = 'optimizeLegibility';
  container.style.padding = '28px 32px';
  container.style.boxSizing = 'border-box';
  container.style.zIndex = '-9999';
  container.style.pointerEvents = 'none';
  container.style.opacity = '1';

  container.innerHTML = `
    <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 24px 28px; box-shadow: 0 8px 30px rgba(0,0,0,0.06);">
      
      <!-- Header -->
      <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #e2e8f0; padding-bottom: 16px; margin-bottom: 16px;">
        <div>
          <div style="color: #92400e; font-size: 15px; font-weight: 900; letter-spacing: 2px; text-transform: uppercase;">
            YASHCOM FOUNDATION, SHEGAON
          </div>
          <div style="color: #0f172a; font-size: 24px; font-weight: 900; margin: 3px 0 5px; letter-spacing: -0.3px;">
            🏋️ Student Topic Mastery & Practice Dossier
          </div>
          <div style="color: #0369a1; font-size: 17px; font-weight: 800;">
            ${displayName} • <span style="color:#475569; font-weight:700;">${batchName}</span>
          </div>
        </div>
        <div style="text-align: right;">
          <div style="background: #f1f5f9; border: 1.5px solid #cbd5e1; color: #1e293b; font-size: 12.5px; font-weight: 800; padding: 5px 14px; border-radius: 6px; display: inline-block;">
            📅 ${todayFormatted}
          </div>
          <div style="color: #475569; font-size: 12px; font-weight: 700; margin-top: 5px;">
            Individual Curriculum Status
          </div>
        </div>
      </div>

      <!-- KPI Summary Cards -->
      <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-bottom: 20px;">
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 26px; font-weight: 900; color: #0f172a; line-height: 1.1;">${totalAssigned}</div>
          <div style="font-size: 11px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Assigned Topics</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 26px; font-weight: 900; color: #14532d; line-height: 1.1;">${masteredCount}</div>
          <div style="font-size: 11px; font-weight: 800; color: #14532d; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">🟢 Mastered (${masteredPct}%)</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 26px; font-weight: 900; color: #92400e; line-height: 1.1;">${practicingCount}</div>
          <div style="font-size: 11px; font-weight: 800; color: #92400e; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">🟡 Practicing (${practicingPct}%)</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 26px; font-weight: 900; color: #991b1b; line-height: 1.1;">${needsAttentionCount}</div>
          <div style="font-size: 11px; font-weight: 800; color: #991b1b; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">🔴 Needs Care (${needsAttentionPct}%)</div>
        </div>
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
          <div style="font-size: 26px; font-weight: 900; color: ${getDeepScoreColor(mStat.avgMastery)}; line-height: 1.1;">${mStat.avgMastery}%</div>
          <div style="font-size: 11px; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">Avg Mastery</div>
        </div>
      </div>

      ${topicRowsHtml ? `
        <!-- Topics Breakdown Table -->
        <table style="width: 100%; border-collapse: collapse; border: 1.5px solid #cbd5e1; border-radius: 10px; overflow: hidden; margin-bottom: 20px;">
          <thead>
            <tr style="background: #0f172a; color: #ffffff; font-size: 11.5px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px; height: 38px;">
              <th style="padding: 8px 10px; text-align: left; width: 140px;">Subject / Chapter</th>
              <th style="padding: 8px 12px; text-align: left;">Topic Name</th>
              <th style="padding: 8px 8px; text-align: center; width: 85px;">Mastery</th>
              <th style="padding: 8px 8px; text-align: center; width: 80px;">Attempts</th>
              <th style="padding: 8px 10px; text-align: center; width: 110px;">Status</th>
              <th style="padding: 8px 12px; text-align: left; width: 230px;">Teacher / Diagnostic Guidance</th>
            </tr>
          </thead>
          <tbody>
            ${topicRowsHtml}
          </tbody>
        </table>
      ` : ''}

      <!-- Pedagogical Explanation & Parent Guidance Banner -->
      <div style="padding: 18px 22px; background: #f8fafc; border: 1.5px solid #cbd5e1; border-left: 5px solid #0284c7; border-radius: 10px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
          <span style="font-size: 22px; line-height: 1;">💡</span>
          <strong style="color: #0f172a; font-size: 15px; font-weight: 900; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
            पालकांसाठी घटक स्थिती स्पष्टीकरण व मार्गदर्शन (Topic Status Guide):
          </strong>
        </div>
        <ul style="margin: 0; padding-left: 20px; color: #1e293b; font-size: 13.5px; line-height: 1.8; font-weight: 600; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
          <li style="margin-bottom: 8px;">
            <strong style="color: #0f172a;">📌 एकूण नेमून दिलेले अभ्यासक्रम घटक (${totalAssigned} Topics):</strong> वर्गात शिकवून पूर्ण झालेले व सरावासाठी दिलेले एकूण घटक = 🟢 पूर्ण प्रभुत्व + 🟡 सराव सुरू + 🔴 लक्ष द्यावे.
          </li>
          <li style="margin-bottom: 8px;">
            <strong style="color: #14532d;">🟢 Mastered (${masteredCount} घटक):</strong> विद्यार्थ्याने या संकल्पनांवर <strong>≥ ९०% अचूकता</strong> संपादन केली असून तयारी उत्कृष्ट आहे.
          </li>
          <li style="margin-bottom: 8px;">
            <strong style="color: #92400e;">🟡 In Progress (${practicingCount} घटक):</strong> या घटकांचा सराव चालू असून अचूकता ५०% ते ८९% दरम्यान आहे. अजून २ सराव सेट्स सोडवून ९०%+ पातळी गाठणे आवश्यक आहे.
          </li>
          <li style="margin-bottom: 8px;">
            <strong style="color: #991b1b;">🔴 Needs Attention / Unattempted (${needsAttentionCount} घटक):</strong> या घटकांत अचूकता ५०% पेक्षा कमी आहे किंवा अद्याप सराव सुरू केलेला नाही. हे घटक प्राधान्याने सोडवून घेणे अनिवार्य आहे.
          </li>
          <li>
            <strong style="color: #0369a1;">📌 पालकांसाठी कृती कार्यक्रम:</strong> दररोज घरी किमान २ ते ३ सराव सेट्स सोडवून सर्व 🟡 व 🔴 घटक 🟢 मध्ये आणल्यास बोर्ड परीक्षेत निश्चितच ९०%+ गुण मिळतील.
          </li>
        </ul>
      </div>

      <!-- Footer -->
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 16px; font-size: 11.5px; color: #475569; border-top: 1.5px solid #e2e8f0; padding-top: 12px;">
        <span><strong style="color: #0f172a;">YASHCOM FOUNDATION, SHEGAON</strong> • Student Diagnostic Dossier</span>
        <span>Verified Student Topic Mastery Summary • Confidential</span>
      </div>

    </div>
  `;

  document.body.appendChild(container);

  try {
    await new Promise(r => setTimeout(r, 300));

    const canvas = await html2canvas(container, {
      scale: 3,
      useCORS: true,
      backgroundColor: '#ffffff',
      logging: false
    });

    document.body.removeChild(container);

    const blob: Blob = await new Promise((resolve, reject) => {
      canvas.toBlob((b: Blob | null) => {
        if (b) resolve(b);
        else reject(new Error('Failed to generate image blob from canvas.'));
      }, 'image/png');
    });

    const cleanName = displayName.replace(/[^a-zA-Z0-9_-]/g, '_');
    const fileName = `Practice_Mastery_${cleanName}.png`;
    const imageUri = canvas.toDataURL('image/png');

    let copiedToClipboard = false;
    if (navigator.clipboard && typeof ClipboardItem !== 'undefined') {
      try {
        await navigator.clipboard.write([
          new ClipboardItem({ 'image/png': blob })
        ]);
        copiedToClipboard = true;
      } catch (clipErr) {
        console.warn('Clipboard write failed:', clipErr);
      }
    }

    const downloadLink = document.createElement('a');
    downloadLink.download = fileName;
    downloadLink.href = imageUri;
    downloadLink.click();

    playNotificationSound();

    if (copiedToClipboard) {
      alert(`✅ Ultra HD WhatsApp Practice Card Exported!\n\n1. Lossless Ultra-HD Image downloaded: ${fileName}\n2. Copied to Clipboard! You can directly press Ctrl + V in WhatsApp Web.`);
    } else {
      alert(`✅ Ultra HD WhatsApp Practice Card downloaded successfully as ${fileName}!`);
    }

    return { blob, fileName, copiedToClipboard };
  } catch (err: any) {
    if (container.parentNode) {
      document.body.removeChild(container);
    }
    throw err;
  }
}

