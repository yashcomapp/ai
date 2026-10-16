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

  // Create offscreen container styled with crisp typography and dark slate background
  const container = document.createElement('div');
  container.style.position = 'fixed';
  container.style.left = '0';
  container.style.top = '0';
  container.style.width = '1080px';
  container.style.backgroundColor = '#0b1120';
  container.style.color = '#f8fafc';
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
    <div style="background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%); border: 1.5px solid #334155; border-radius: 16px; padding: 28px 32px; box-shadow: 0 16px 40px rgba(0,0,0,0.6);">
      
      <!-- Top Institute Header -->
      <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #334155; padding-bottom: 18px; margin-bottom: 20px;">
        <div>
          <div style="color: #fbbf24; font-size: 16px; font-weight: 800; letter-spacing: 2.5px; text-transform: uppercase;">
            YASHCOM FOUNDATION, SHEGAON
          </div>
          <div style="color: #ffffff; font-size: 24px; font-weight: 900; margin: 4px 0 6px; letter-spacing: -0.3px;">
            📊 Learning Quotient (LQ) Academic Dossier
          </div>
          <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
            <span style="color: #38bdf8; font-size: 19px; font-weight: 800;">${studentName}</span>
            <span style="color: #64748b; font-size: 16px;">•</span>
            <span style="background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.35); color: #7dd3fc; font-size: 13px; font-weight: 700; padding: 3px 12px; border-radius: 6px;">
              ${batchName}
            </span>
          </div>
        </div>
        <div style="text-align: right;">
          <div style="background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; font-size: 12.5px; font-weight: 800; padding: 5px 14px; border-radius: 6px; display: inline-block;">
            📅 ${todayFormatted}
          </div>
          <div style="color: #94a3b8; font-size: 12px; font-weight: 600; margin-top: 6px;">
            Evaluation Window: <strong style="color: #ffffff;">${durationLabel}</strong>
          </div>
        </div>
      </div>

      <!-- Hero Score & 4-Pillar KPI Overview -->
      <div style="display: grid; grid-template-columns: 280px 1fr; gap: 18px; margin-bottom: 20px;">
        
        <!-- Big Radial / Composite Score Card -->
        <div style="background: #0f172a; border: 1.5px solid #334155; border-radius: 14px; padding: 20px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: inset 0 2px 12px rgba(0,0,0,0.4);">
          <div style="font-size: 11px; font-weight: 800; color: #94a3b8; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 8px;">
            Composite Academic Score
          </div>
          <div style="font-size: 52px; font-weight: 900; color: ${scoreColor}; line-height: 1; letter-spacing: -1.5px;">
            ${overallQuotient}<span style="font-size: 22px; color: #94a3b8; font-weight: 700;">/100</span>
          </div>
          <div style="margin-top: 10px; display: inline-block; padding: 4px 14px; border-radius: 20px; font-size: 12px; font-weight: 800; background: ${scoreColor}22; color: ${scoreColor}; border: 1px solid ${scoreColor}45;">
            ${tierLabel}
          </div>
          <div style="font-size: 11px; color: #94a3b8; font-weight: 600; margin-top: 10px;">
            Learning Quotient (LQ)
          </div>
        </div>

        <!-- 4 Quick Highlight Cards -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
          
          <!-- Exam Card -->
          <div style="background: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 12.5px; font-weight: 700; color: #94a3b8;">🎯 Exam Performance</span>
              <span style="font-size: 20px; font-weight: 900; color: ${examColor};">${examScore}%</span>
            </div>
            <div style="font-size: 11.5px; color: #cbd5e1; margin-top: 6px;">
              Attendance: <strong style="color: #ffffff;">${attendanceRate}%</strong> • Exams: <strong style="color: #ffffff;">${completedExams}/${totalExams}</strong>
            </div>
          </div>

          <!-- Topic Mastery Card -->
          <div style="background: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 12.5px; font-weight: 700; color: #94a3b8;">🧠 Topic Mastery</span>
              <span style="font-size: 20px; font-weight: 900; color: ${masteryColor};">${masteryScore}%</span>
            </div>
            <div style="font-size: 11.5px; color: #cbd5e1; margin-top: 6px;">
              Mastered: <strong style="color: #ffffff;">${masteredTopics}/${totalTopics} Topics</strong> (${averageRetention}% Retention)
            </div>
          </div>

          <!-- Practice Efforts Card -->
          <div style="background: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 12.5px; font-weight: 700; color: #94a3b8;">⚡ Practice Efforts</span>
              <span style="font-size: 20px; font-weight: 900; color: ${effortsColor};">${effortsScore}%</span>
            </div>
            <div style="font-size: 11.5px; color: #cbd5e1; margin-top: 6px;">
              Attempted: <strong style="color: #ffffff;">${totalQuestionsPracticed} Qs</strong> across <strong style="color: #ffffff;">${practicedTopicsCount} Topics</strong>
            </div>
          </div>

          <!-- Practice Quality Card -->
          <div style="background: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 12.5px; font-weight: 700; color: #94a3b8;">💎 Practice Quality</span>
              <span style="font-size: 20px; font-weight: 900; color: ${qualityColor};">${qualityScore}%</span>
            </div>
            <div style="font-size: 11.5px; color: #cbd5e1; margin-top: 6px;">
              Independent Practice Accuracy Rate: <strong style="color: #ffffff;">${qualityScore}%</strong>
            </div>
          </div>

        </div>
      </div>

      <!-- Core Academic Pillars Progress Breakdown -->
      <div style="background: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 16px 20px; margin-bottom: 18px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <span style="font-size: 12px; font-weight: 800; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.8px;">
            Academic Pillars Breakdown (Weighted Synthesis)
          </span>
          <span style="font-size: 11px; color: #94a3b8;">
            Sum of weighted contributions = Official LQ
          </span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 12px;">
          
          <!-- Pillar 1: Exam Performance -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; margin-bottom: 4px;">
              <span style="color: #ffffff;">🎯 1. Exam Performance <span style="color: #94a3b8; font-weight: 500;">(Weight: ${Math.round(examComp.weight * 100)}%)</span></span>
              <span style="color: ${examColor}; font-weight: 800;">${examScore}% <span style="color: #94a3b8; font-weight: 600; font-size: 11px;">(+${examComp.contribution} pts)</span></span>
            </div>
            <div style="width: 100%; height: 8px; background: #1e293b; border-radius: 4px; overflow: hidden;">
              <div style="width: ${examScore}%; height: 100%; background: ${examColor}; border-radius: 4px;"></div>
            </div>
          </div>

          <!-- Pillar 2: Topic Mastery -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; margin-bottom: 4px;">
              <span style="color: #ffffff;">🧠 2. Topic Mastery & Retention <span style="color: #94a3b8; font-weight: 500;">(Weight: ${Math.round(healthComp.weight * 100)}%)</span></span>
              <span style="color: ${masteryColor}; font-weight: 800;">${masteryScore}% <span style="color: #94a3b8; font-weight: 600; font-size: 11px;">(+${healthComp.contribution} pts)</span></span>
            </div>
            <div style="width: 100%; height: 8px; background: #1e293b; border-radius: 4px; overflow: hidden;">
              <div style="width: ${masteryScore}%; height: 100%; background: ${masteryColor}; border-radius: 4px;"></div>
            </div>
          </div>

          <!-- Pillar 3: Practice Efforts -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; margin-bottom: 4px;">
              <span style="color: #ffffff;">⚡ 3. Practice Efforts & Scope <span style="color: #94a3b8; font-weight: 500;">(Weight: ${Math.round(practiceComp.weight * 100)}%)</span></span>
              <span style="color: ${effortsColor}; font-weight: 800;">${effortsScore}% <span style="color: #94a3b8; font-weight: 600; font-size: 11px;">(+${practiceComp.contribution} pts)</span></span>
            </div>
            <div style="width: 100%; height: 8px; background: #1e293b; border-radius: 4px; overflow: hidden;">
              <div style="width: ${effortsScore}%; height: 100%; background: ${effortsColor}; border-radius: 4px;"></div>
            </div>
          </div>

          <!-- Pillar 4: Practice Quality -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; margin-bottom: 4px;">
              <span style="color: #ffffff;">💎 4. Practice Quality & Accuracy <span style="color: #94a3b8; font-weight: 500;">(Weight: ${Math.round(qualityComp.weight * 100)}%)</span></span>
              <span style="color: ${qualityColor}; font-weight: 800;">${qualityScore}% <span style="color: #94a3b8; font-weight: 600; font-size: 11px;">(+${qualityComp.contribution} pts)</span></span>
            </div>
            <div style="width: 100%; height: 8px; background: #1e293b; border-radius: 4px; overflow: hidden;">
              <div style="width: ${qualityScore}%; height: 100%; background: ${qualityColor}; border-radius: 4px;"></div>
            </div>
          </div>

        </div>
      </div>

      <!-- Teacher's Diagnostic Feedback in Hindi -->
      <div style="margin-bottom: 18px; padding: 16px 20px; background: rgba(251, 191, 36, 0.08); border: 1px solid rgba(251, 191, 36, 0.35); border-radius: 12px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
          <span style="font-size: 18px;">📝</span>
          <span style="font-size: 13px; font-weight: 800; color: #fbbf24; text-transform: uppercase; letter-spacing: 0.5px;">
            शिक्षक का शैक्षणिक विश्लेषण एवं मार्गदर्शन (Educator's Diagnostic Guidance)
          </span>
        </div>
        <div style="font-size: 13.5px; color: #fde68a; line-height: 1.6; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans Devanagari', 'Mangal', sans-serif; white-space: pre-wrap;">
${commentsText || 'नियमित अभ्यास, समय प्रबंधन एवं परीक्षा विश्लेषण के माध्यम से संकल्पनाओं की गहरी समझ विकसित करना जारी रखें।'}
        </div>
      </div>

      <!-- Institutional Integrity & Exam Discipline Note -->
      <div style="margin-bottom: 18px; padding: 12px 18px; background: rgba(56, 189, 248, 0.06); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 10px; display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span style="font-size: 20px;">🛡️</span>
          <div>
            <div style="font-size: 12px; font-weight: 800; color: #38bdf8;">
              परीक्षा अनुशासन एवं सत्यनिष्ठा (Exam Integrity): ${integrityScore}%
            </div>
            <div style="font-size: 11px; color: #94a3b8;">
              प्रॉक्टरिंग अनुपालन मानक • ${integrityScore >= 90 ? 'उत्कृष्ट अनुशासन एवं प्रामाणिकता 🌟' : 'स्क्रीन स्विच एवं ध्यान भटकाव से बचें ⚠️'}
            </div>
          </div>
        </div>
        <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.35); color: #34d399; font-size: 11px; font-weight: 800; padding: 4px 10px; border-radius: 6px;">
          Verified Student Record
        </div>
      </div>

      <!-- Footer -->
      <div style="display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: #94a3b8; border-top: 1px solid #334155; padding-top: 12px;">
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
      backgroundColor: '#0b1120',
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
