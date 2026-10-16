import { formatDateDMY } from '@/lib/dateUtils';
import { playNotificationSound } from '@/lib/audioUtils';
import { getScoreColor } from '@/lib/dashboardMetrics';

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
  const scoreColor = getScoreColor(overallQuotient);
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

  const examColor = getScoreColor(examScore);
  const masteryColor = getScoreColor(masteryScore);
  const effortsColor = getScoreColor(effortsScore);
  const qualityColor = getScoreColor(qualityScore);

  const attendanceRate = examComp.details?.attendanceRate ?? 100;
  const totalExams = examComp.details?.totalAssigned ?? 0;
  const completedExams = examComp.details?.completed ?? 0;

  const totalTopics = healthComp.details?.totalTopics ?? 0;
  const masteredTopics = healthComp.details?.masteredCount ?? 0;
  const averageRetention = healthComp.details?.averageRetention ?? 0;

  const totalQuestionsPracticed = practiceComp.details?.totalQuestionsAttempted ?? 0;
  const practicedTopicsCount = practiceComp.details?.topicsAttemptedCount ?? 0;

  const todayFormatted = formatDateDMY(new Date());
  const studentName = student.name || 'Student';
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
  container.style.fontFamily = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', 'Helvetica Neue', Arial, sans-serif";
  (container.style as any).webkitFontSmoothing = 'antialiased';
  (container.style as any).mozOsxFontSmoothing = 'grayscale';
  (container.style as any).textRendering = 'optimizeLegibility';
  container.style.padding = '32px 36px';
  container.style.boxSizing = 'border-box';
  container.style.zIndex = '-9999';
  container.style.pointerEvents = 'none';
  container.style.opacity = '1';

  container.innerHTML = `
    <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 16px; padding: 28px 32px; box-shadow: 0 8px 30px rgba(0,0,0,0.06);">
      
      <!-- Top Institute Header -->
      <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #e2e8f0; padding-bottom: 18px; margin-bottom: 20px;">
        <div>
          <div style="color: #b45309; font-size: 16px; font-weight: 800; letter-spacing: 2.5px; text-transform: uppercase;">
            YASHCOM FOUNDATION, SHEGAON
          </div>
          <div style="color: #0f172a; font-size: 24px; font-weight: 900; margin: 4px 0 6px; letter-spacing: -0.3px;">
            📊 Learning Quotient (LQ) Academic Dossier
          </div>
          <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
            <span style="color: #0284c7; font-size: 19px; font-weight: 800;">${studentName}</span>
            <span style="color: #cbd5e1; font-size: 16px;">•</span>
            <span style="background: #f0f9ff; border: 1px solid #bae6fd; color: #0369a1; font-size: 13px; font-weight: 700; padding: 3px 12px; border-radius: 6px;">
              ${batchName}
            </span>
          </div>
        </div>
        <div style="text-align: right;">
          <div style="background: #f0f9ff; border: 1px solid #bae6fd; color: #0369a1; font-size: 12.5px; font-weight: 800; padding: 5px 14px; border-radius: 6px; display: inline-block;">
            📅 ${todayFormatted}
          </div>
          <div style="color: #64748b; font-size: 12px; font-weight: 600; margin-top: 6px;">
            Evaluation Window: <strong style="color: #0f172a;">${durationLabel}</strong>
          </div>
        </div>
      </div>

      <!-- Hero Score & 4-Pillar KPI Overview -->
      <div style="display: grid; grid-template-columns: 280px 1fr; gap: 18px; margin-bottom: 20px;">
        
        <!-- Big Radial / Composite Score Card -->
        <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 20px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
          <div style="font-size: 11px; font-weight: 800; color: #64748b; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 8px;">
            Composite Academic Score
          </div>
          <div style="font-size: 52px; font-weight: 900; color: ${scoreColor}; line-height: 1; letter-spacing: -1.5px;">
            ${overallQuotient}<span style="font-size: 22px; color: #64748b; font-weight: 700;">/100</span>
          </div>
          <div style="margin-top: 10px; display: inline-block; padding: 4px 14px; border-radius: 20px; font-size: 12px; font-weight: 800; background: ${scoreColor}18; color: ${scoreColor}; border: 1.5px solid ${scoreColor}40;">
            ${tierLabel}
          </div>
          <div style="font-size: 11.5px; color: #64748b; font-weight: 700; margin-top: 10px;">
            Learning Quotient (LQ)
          </div>
        </div>

        <!-- 4 Quick Highlight Cards -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
          
          <!-- Exam Card -->
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 12.5px; font-weight: 700; color: #475569;">🎯 Exam Performance</span>
              <span style="font-size: 20px; font-weight: 900; color: ${examColor};">${examScore}%</span>
            </div>
            <div style="font-size: 11.5px; color: #64748b; margin-top: 6px;">
              Attendance: <strong style="color: #0f172a;">${attendanceRate}%</strong> • Exams: <strong style="color: #0f172a;">${completedExams}/${totalExams}</strong>
            </div>
          </div>

          <!-- Topic Mastery Card -->
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 12.5px; font-weight: 700; color: #475569;">🧠 Topic Mastery</span>
              <span style="font-size: 20px; font-weight: 900; color: ${masteryColor};">${masteryScore}%</span>
            </div>
            <div style="font-size: 11.5px; color: #64748b; margin-top: 6px;">
              Mastered: <strong style="color: #0f172a;">${masteredTopics}/${totalTopics} Topics</strong> (${averageRetention}% Retention)
            </div>
          </div>

          <!-- Practice Efforts Card -->
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 12.5px; font-weight: 700; color: #475569;">⚡ Practice Efforts</span>
              <span style="font-size: 20px; font-weight: 900; color: ${effortsColor};">${effortsScore}%</span>
            </div>
            <div style="font-size: 11.5px; color: #64748b; margin-top: 6px;">
              Attempted: <strong style="color: #0f172a;">${totalQuestionsPracticed} Qs</strong> across <strong style="color: #0f172a;">${practicedTopicsCount} Topics</strong>
            </div>
          </div>

          <!-- Practice Quality Card -->
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 12.5px; font-weight: 700; color: #475569;">💎 Practice Quality</span>
              <span style="font-size: 20px; font-weight: 900; color: ${qualityColor};">${qualityScore}%</span>
            </div>
            <div style="font-size: 11.5px; color: #64748b; margin-top: 6px;">
              Independent Accuracy Rate: <strong style="color: #0f172a;">${qualityScore}%</strong>
            </div>
          </div>

        </div>
      </div>

      <!-- Core Academic Pillars Progress Breakdown -->
      <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 16px 20px; margin-bottom: 18px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <span style="font-size: 12px; font-weight: 800; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">
            Academic Pillars Breakdown (Weighted Synthesis)
          </span>
          <span style="font-size: 11px; color: #64748b;">
            Sum of weighted contributions = Official LQ
          </span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 12px;">
          
          <!-- Pillar 1: Exam Performance -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; margin-bottom: 4px;">
              <span style="color: #0f172a;">🎯 1. Exam Performance <span style="color: #64748b; font-weight: 500;">(Weight: ${Math.round(examComp.weight * 100)}%)</span></span>
              <span style="color: ${examColor}; font-weight: 800;">${examScore}% <span style="color: #64748b; font-weight: 600; font-size: 11px;">(+${examComp.contribution} pts)</span></span>
            </div>
            <div style="width: 100%; height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden;">
              <div style="width: ${examScore}%; height: 100%; background: ${examColor}; border-radius: 4px;"></div>
            </div>
          </div>

          <!-- Pillar 2: Topic Mastery -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; margin-bottom: 4px;">
              <span style="color: #0f172a;">🧠 2. Topic Mastery & Retention <span style="color: #64748b; font-weight: 500;">(Weight: ${Math.round(healthComp.weight * 100)}%)</span></span>
              <span style="color: ${masteryColor}; font-weight: 800;">${masteryScore}% <span style="color: #64748b; font-weight: 600; font-size: 11px;">(+${healthComp.contribution} pts)</span></span>
            </div>
            <div style="width: 100%; height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden;">
              <div style="width: ${masteryScore}%; height: 100%; background: ${masteryColor}; border-radius: 4px;"></div>
            </div>
          </div>

          <!-- Pillar 3: Practice Efforts -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; margin-bottom: 4px;">
              <span style="color: #0f172a;">⚡ 3. Practice Efforts & Scope <span style="color: #64748b; font-weight: 500;">(Weight: ${Math.round(practiceComp.weight * 100)}%)</span></span>
              <span style="color: ${effortsColor}; font-weight: 800;">${effortsScore}% <span style="color: #64748b; font-weight: 600; font-size: 11px;">(+${practiceComp.contribution} pts)</span></span>
            </div>
            <div style="width: 100%; height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden;">
              <div style="width: ${effortsScore}%; height: 100%; background: ${effortsColor}; border-radius: 4px;"></div>
            </div>
          </div>

          <!-- Pillar 4: Practice Quality -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; margin-bottom: 4px;">
              <span style="color: #0f172a;">💎 4. Practice Quality & Accuracy <span style="color: #64748b; font-weight: 500;">(Weight: ${Math.round(qualityComp.weight * 100)}%)</span></span>
              <span style="color: ${qualityColor}; font-weight: 800;">${qualityScore}% <span style="color: #64748b; font-weight: 600; font-size: 11px;">(+${qualityComp.contribution} pts)</span></span>
            </div>
            <div style="width: 100%; height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden;">
              <div style="width: ${qualityScore}%; height: 100%; background: ${qualityColor}; border-radius: 4px;"></div>
            </div>
          </div>

        </div>
      </div>

      <!-- Teacher's Diagnostic Feedback in Bullet List Format -->
      <div style="margin-bottom: 18px; padding: 14px 18px; background: #fffbeb; border: 1.5px solid #fde68a; border-radius: 10px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
          <span style="font-size: 18px;">📝</span>
          <span style="font-size: 13.5px; font-weight: 800; color: #b45309; text-transform: uppercase; letter-spacing: 0.5px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
            शिक्षक का शैक्षणिक विश्लेषण एवं मार्गदर्शन (Educator's Diagnostic Guidance):
          </span>
        </div>
        <ul style="margin: 0; padding-left: 20px; color: #78350f; font-size: 12px; line-height: 1.65; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
          <li style="margin-bottom: 4px;">
            <strong>📌 समतोल शैक्षणिक प्रगती (4-Pillar Synergy):</strong> लर्निंग कोशंट (LQ) हा सराव प्रयत्न (25%), सराव अचूकता (15%), संकल्पना प्रभुत्व (30%) आणि परीक्षा कामगिरी (30%) यांचा वैज्ञानिक निर्देशांक आहे.
          </li>
          <li style="margin-bottom: 4px;">
            <strong>📌 दैनिक सराव पूर्ण करा (Daily Practice):</strong> सराव प्रयत्न वाढवून सर्व निर्देशित घटक वेळेवर सोडवण्याचा सराव करा.
          </li>
          <li style="margin-bottom: 4px;">
            <strong>📌 अचूकतेवर भर द्या (Quality over Speed):</strong> घाईगडबडीत उत्तरे देण्यापेक्षा अचूकतेवर आणि संकल्पना समजून घेण्यावर लक्ष केंद्रित करा.
          </li>
          <li>
            <strong>📌 शिक्षक टीप (Educator Note):</strong> ${commentsText || 'नियमित सराव, वेळेचे व्यवस्थापन आणि त्रुटींचे विश्लेषण याद्वारे संकल्पनांची अचूक समज विकसित करा.'}
          </li>
        </ul>
      </div>

      <!-- Institutional Integrity & Exam Discipline Note -->
      <div style="margin-bottom: 18px; padding: 12px 18px; background: #f0fdf4; border: 1.5px solid #bbf7d0; border-radius: 10px; display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span style="font-size: 20px;">🛡️</span>
          <div>
            <div style="font-size: 12px; font-weight: 800; color: #166534;">
              परीक्षा अनुशासन एवं सत्यनिष्ठा (Exam Integrity): ${integrityScore}%
            </div>
            <div style="font-size: 11px; color: #15803d; font-weight: 600;">
              प्रॉक्टरिंग अनुपालन मानक • ${integrityScore >= 90 ? 'उत्कृष्ट अनुशासन एवं प्रामाणिकता 🌟' : 'स्क्रीन स्विच एवं ध्यान भटकाव से बचें ⚠️'}
            </div>
          </div>
        </div>
        <div style="background: #dcfce7; border: 1px solid #86efac; color: #166534; font-size: 11px; font-weight: 800; padding: 4px 10px; border-radius: 6px;">
          Verified Student Record
        </div>
      </div>

      <!-- Footer -->
      <div style="display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: #64748b; border-top: 1px solid #e2e8f0; padding-top: 12px;">
        <span><strong>YASHCOM FOUNDATION, SHEGAON</strong> • Academic Excellence & Concept Mastery</span>
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
      bg: '#ecfdf5',
      color: '#059669',
      border: '#a7f3d0'
    };
  }
  if (efforts >= 70 && mastery >= 70) {
    return {
      text: '⚡ Diligent & Consistent',
      bg: '#f0f9ff',
      color: '#0284c7',
      border: '#bae6fd'
    };
  }
  if (exam >= 75 && efforts < 20) {
    return {
      text: '⚠️ Strong Exam, Low Practice',
      bg: '#fefce8',
      color: '#d97706',
      border: '#fde047'
    };
  }
  if (efforts >= 50 && quality < 50) {
    return {
      text: '🎯 Practicing, Needs Accuracy',
      bg: '#f5f3ff',
      color: '#7c3aed',
      border: '#ddd6fe'
    };
  }
  if (lq >= 60) {
    return {
      text: '🟡 Steady Progress',
      bg: '#fefce8',
      color: '#d97706',
      border: '#fde047'
    };
  }
  return {
    text: '🚨 Needs Daily Practice',
    bg: '#fee2e2',
    color: '#dc2626',
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
  container.style.fontFamily = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', 'Helvetica Neue', Arial, sans-serif";
  (container.style as any).webkitFontSmoothing = 'antialiased';
  (container.style as any).mozOsxFontSmoothing = 'grayscale';
  (container.style as any).textRendering = 'optimizeLegibility';
  container.style.padding = '28px 32px';
  container.style.boxSizing = 'border-box';
  container.style.zIndex = '-9999';
  container.style.pointerEvents = 'none';
  container.style.opacity = '1';

  // Build table rows
  const rowsHtml = sorted.map((s, idx) => {
    const rank = idx + 1;
    const rankBadge = rank === 1 ? '🥇 1' : rank === 2 ? '🥈 2' : rank === 3 ? '🥉 3' : `${rank}`;
    const lq = s.overallQuotient ?? 0;
    const lqColor = getScoreColor(lq);
    const rowBg = idx % 2 === 0 ? '#ffffff' : '#f8fafc';
    const insight = getBatchStudentLqInsight(s);

    return `
      <tr style="border-bottom: 1px solid #e2e8f0; height: 38px; background-color: ${rowBg};">
        <td style="padding: 8px 10px; text-align: center; font-weight: 700; font-size: 13px; color: #64748b;">${rankBadge}</td>
        <td style="padding: 8px 12px; font-weight: 700; font-size: 14px; color: #0f172a; white-space: nowrap;">
          ${s.name}
        </td>
        <td style="padding: 8px 12px; text-align: center; font-weight: 900; font-size: 15px; color: ${lqColor}; white-space: nowrap;">
          ${lq}%
        </td>
        <td style="padding: 8px 10px; text-align: center; font-size: 13px; font-weight: 700; color: ${getScoreColor(s.examScore)}; white-space: nowrap;">
          ${s.examScore}%
        </td>
        <td style="padding: 8px 10px; text-align: center; font-size: 13px; font-weight: 700; color: ${getScoreColor(s.healthScore)}; white-space: nowrap;">
          ${s.healthScore}%
        </td>
        <td style="padding: 8px 10px; text-align: center; font-size: 13px; font-weight: 700; color: ${getScoreColor(s.practiceScore)}; white-space: nowrap;">
          ${s.practiceScore}%
        </td>
        <td style="padding: 8px 10px; text-align: center; font-size: 13px; font-weight: 700; color: ${getScoreColor(s.qualityScore)}; white-space: nowrap;">
          ${s.qualityScore}%
        </td>
        <td style="padding: 8px 12px; text-align: center; white-space: nowrap;">
          <span style="display:inline-block; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; background: ${insight.bg}; color: ${insight.color}; border: 1px solid ${insight.border}; white-space: nowrap;">
            ${insight.text}
          </span>
        </td>
      </tr>
    `;
  }).join('');

  container.innerHTML = `
    <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 24px 28px; box-shadow: 0 8px 30px rgba(0,0,0,0.06);">
      
      <!-- Header -->
      <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #e2e8f0; padding-bottom: 16px; margin-bottom: 16px;">
        <div>
          <div style="color: #b45309; font-size: 15px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase;">
            YASHCOM FOUNDATION, SHEGAON
          </div>
          <div style="color: #0f172a; font-size: 22px; font-weight: 900; margin: 3px 0 5px; letter-spacing: -0.3px;">
            🏆 Learning Quotient (LQ) Academic Report
          </div>
          <div style="color: #0284c7; font-size: 15px; font-weight: 700;">
            ${batchName}
          </div>
        </div>
        <div style="text-align: right;">
          <div style="background: #f0f9ff; border: 1px solid #bae6fd; color: #0369a1; font-size: 12px; font-weight: 800; padding: 4px 12px; border-radius: 6px; display: inline-block;">
            📅 ${todayFormatted}
          </div>
          <div style="color: #64748b; font-size: 11.5px; font-weight: 600; margin-top: 5px;">
            Evaluation Scope: <strong style="color:#0f172a;">${durationLabel}</strong>
          </div>
        </div>
      </div>

      <!-- KPI Summary Cards -->
      <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-bottom: 18px;">
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 12px; text-align: center;">
          <div style="font-size: 22px; font-weight: 800; color: #0f172a;">${totalStudents}</div>
          <div style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px;">Students</div>
        </div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 12px; text-align: center;">
          <div style="font-size: 22px; font-weight: 800; color: ${getScoreColor(batchAvgLQ)};">${batchAvgLQ}%</div>
          <div style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px;">Batch Avg LQ</div>
        </div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 12px; text-align: center;">
          <div style="font-size: 22px; font-weight: 800; color: #d97706;">${topLQ}%</div>
          <div style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px;">Highest LQ</div>
        </div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 12px; text-align: center;">
          <div style="font-size: 22px; font-weight: 800; color: #0284c7;">${avgExam}%</div>
          <div style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px;">Exam Avg</div>
        </div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 12px; text-align: center;">
          <div style="font-size: 22px; font-weight: 800; color: #059669;">${avgEfforts}%</div>
          <div style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px;">Practice Avg</div>
        </div>
      </div>

      <!-- Table -->
      <table style="width: 100%; border-collapse: collapse; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden;">
        <thead>
          <tr style="background: #f8fafc; color: #475569; font-size: 11.5px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px; border-bottom: 2px solid #cbd5e1; height: 36px;">
            <th style="padding: 8px 10px; text-align: center; width: 50px;">Rank</th>
            <th style="padding: 8px 12px; text-align: left;">Student Name</th>
            <th style="padding: 8px 12px; text-align: center; width: 95px;">LQ Score</th>
            <th style="padding: 8px 10px; text-align: center; width: 90px;">Exam Avg</th>
            <th style="padding: 8px 10px; text-align: center; width: 90px;">Mastery</th>
            <th style="padding: 8px 10px; text-align: center; width: 90px;">Efforts</th>
            <th style="padding: 8px 10px; text-align: center; width: 90px;">Quality</th>
            <th style="padding: 8px 12px; text-align: center; width: 190px;">Insight</th>
          </tr>
        </thead>
        <tbody>
          ${rowsHtml}
        </tbody>
      </table>

      <!-- Educational Guidance Banner (Hindi / Marathi) - Bullet List -->
      <div style="margin-top: 16px; padding: 14px 18px; background: #fffbeb; border: 1.5px solid #fde68a; border-radius: 10px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
          <span style="font-size: 20px; line-height: 1;">💡</span>
          <strong style="color: #b45309; font-size: 13.5px; font-weight: 800; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
            शैक्षणिक विश्लेषण एवं मार्गदर्शन (Academic Guidance & Key Insights):
          </strong>
        </div>
        <ul style="margin: 0; padding-left: 20px; color: #78350f; font-size: 12px; line-height: 1.65; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif;">
          <li style="margin-bottom: 4px;">
            <strong>📌 समग्र शैक्षणिक निर्देशांक (Holistic Synthesis):</strong> लर्निंग कोशंट (LQ) हा केवळ परीक्षेच्या गुणांचा नव्हे, तर नियमित सराव प्रयत्न (25%), सराव अचूकता (15%), संकल्पना प्रभुत्व (30%) आणि परीक्षा कामगिरी (30%) यांचा वैज्ञानिक ताळेबंद आहे.
          </li>
          <li style="margin-bottom: 4px;">
            <strong>📌 नियमित दैनिक सराव (Daily Practice Discipline):</strong> ज्या विद्यार्थ्यांचे सराव प्रयत्न कमी आहेत, त्यांनी दररोज स्वतःहून सराव पूर्ण करणे आवश्यक आहे.
          </li>
          <li style="margin-bottom: 4px;">
            <strong>📌 अचूकतेवर भर (Quality & Accuracy):</strong> घाईघाईत प्रश्न सोडवण्यापेक्षा प्रत्येक संकल्पना नीट समजून अचूक उत्तर देण्याचा प्रयत्न करा.
          </li>
          <li>
            <strong>📌 सातत्यपूर्ण प्रयत्नांतूनच प्रभुत्व (Continuous Growth):</strong> नियमित सराव आणि वेळेवर शंकांचे निरसन यामुळेच सर्वोच्च शैक्षणिक स्तर गाठता येतो.
          </li>
        </ul>
      </div>

      <!-- Footer -->
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 16px; font-size: 11px; color: #64748b; border-top: 1px solid #e2e8f0; padding-top: 12px;">
        <span><strong>YASHCOM FOUNDATION, SHEGAON</strong> • Academic Evaluation Portal</span>
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

