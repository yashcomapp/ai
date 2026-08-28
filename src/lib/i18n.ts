const DICT: Record<string, string> = {
  // Nav — top-level chips
  'Dashboard': 'डैशबोर्ड',
  'Exams': 'परीक्षाएं',
  'Exam': 'परीक्षा',
  'Manage': 'प्रबंधन',
  'Reports': 'रिपोर्ट',
  'Settings': 'सेटिंग्स',
  'Theme': 'थीम',
  'Logout': 'लॉगआउट',
  'Learning': 'लर्निंग',
  'Truth': 'ट्रुथ टेस्ट',
  'Results': 'परिणाम',
  'Review': 'समीक्षा',
  'Menu': 'मेनू',
  // Nav — submenu items
  'Templates': 'टेम्पलेट्स',
  'Create Exam': 'परीक्षा बनाएं',
  'Classroom Test': 'क्लासरूम टेस्ट',
  'All Exams': 'सभी परीक्षाएं',
  'Live Monitor': 'लाइव मॉनिटर',
  'Create QB': 'प्रश्न बैंक बनाएं',
  'QB': 'प्रश्न बैंक',
  'Students': 'छात्र',
  'Batches': 'बैच',
  'Registrations': 'रजिस्ट्रेशन',
  'Syllabus Manager': 'पाठ्यक्रम प्रबंधक',
  'Integrity Scores': 'ईमानदारी स्कोर',
  'Usage Report': 'उपयोग रिपोर्ट',
  'Student 360° Report': 'छात्र 360° रिपोर्ट',
  'Export to PDF': 'PDF में निर्यात करें',
  'Backup & Restore': 'बैकअप और रीस्टोर',
  'Cleanup Orphaned': 'अनाथ डेटा हटाएं',
  'System Reset': 'सिस्टम रीसेट',
  'Reset Used Flags': 'उपयोग किए गए फ्लैग रीसेट करें',
  // Common statuses / toasts
  'Please fill all required fields': 'कृपया सभी ज़रूरी जानकारी भरें',
  'Please select at least one batch or student': 'कृपया कम से कम एक बैच या छात्र चुनें',
  'Select at least one subject': 'कृपया कम से कम एक विषय चुनें',
  'Select at least one topic': 'कृपया कम से कम एक टॉपिक चुनें',
  'Select a template first': 'पहले एक टेम्पलेट चुनें',
  'Select class first': 'पहले क्लास चुनें',
  'Select board first': 'पहले बोर्ड चुनें',
  'Please select start and end dates': 'कृपया शुरू और अंत की तारीख चुनें',
  'End date must be after start date': 'अंत की तारीख शुरू की तारीख के बाद होनी चाहिए',
  'No questions selected': 'कोई प्रश्न नहीं चुना गया',
  'No questions to save': 'सहेजने के लिए कोई प्रश्न नहीं है',
  'Failed to load syllabus': 'पाठ्यक्रम लोड नहीं हो सका',
  'Camera active': 'कैमरा चालू है',
  'Camera access denied': 'कैमरे की अनुमति नहीं मिली',
  'Camera not ready.': 'कैमरा अभी तैयार नहीं है।',
  'Cleared': 'साफ़ किया गया',
  'Reset cancelled': 'रीसेट रद्द किया गया',
  // Live monitor
  'Unmute Audio': 'ऑडियो चालू करें',
  'Mute Audio': 'ऑडियो बंद करें',
  'Audio muted for privacy': 'गोपनीयता के लिए ऑडियो बंद है',
  'Audio muted': 'ऑडियो बंद है',
  'Audio live': 'ऑडियो लाइव है',
  'Still waiting — student may have closed the tab.': 'अभी भी इंतज़ार हो रहा है — हो सकता है छात्र ने टैब बंद कर दिया हो।',
  // Exam-taking (high stakes — student sees these mid-exam)
  'Time up! Submitting...': 'समय समाप्त! जमा किया जा रहा है...',
  'Maximum tab violations (3) reached! Exam will be submitted.': 'अधिकतम टैब उल्लंघन (3) हो गया है! परीक्षा जमा कर दी जाएगी।',
  'Could not save your exam results. Please check your connection and try again.': 'आपकी परीक्षा के परिणाम सहेजे नहीं जा सके। कृपया अपना इंटरनेट कनेक्शन जांचें और दोबारा कोशिश करें।',
  'Could not save your submission. Please check your connection and try again.': 'आपकी जमा की गई एंट्री सहेजी नहीं जा सकी। कृपया अपना इंटरनेट कनेक्शन जांचें और दोबारा कोशिश करें।',
  'Could not submit review. Check your connection and try again.': 'समीक्षा जमा नहीं हो सकी। कृपया अपना इंटरनेट कनेक्शन जांचें और दोबारा कोशिश करें।',
  'Time is up for this attempt. Submitting your exam now.': 'इस प्रयास का समय समाप्त हो गया है। आपकी परीक्षा अभी जमा की जा रही है।',
  'No re-attempt is allowed.': 'दोबारा प्रयास की अनुमति नहीं है।',
  // Auth
  'Please enter both email and password': 'कृपया ईमेल और पासवर्ड दोनों दर्ज करें',
  'Login cancelled. Your other session is still active.': 'लॉगिन रद्द किया गया। आपका दूसरा सेशन अभी भी चालू है।',
  'User profile not found. Please contact admin.': 'यूज़र प्रोफ़ाइल नहीं मिली। कृपया एडमिन से संपर्क करें।'
};

function bi(en: string, hi?: string): string {
  if (!hi) return en;
  const joiner = (en + ' ' + hi).length > 46 ? '\n' : ' / ';
  return en + joiner + hi;
}

// Translate helper: resolves from DICT and appends Hindi only if it is an error/warning message
export function t(en: string): string {
  if (!en) return en;
  const lower = en.toLowerCase();
  const isErrorOrWarning = 
    lower.includes('fail') || 
    lower.includes('wrong') || 
    lower.includes('invalid') || 
    lower.includes('not found') || 
    lower.includes('error') || 
    lower.includes('denied') || 
    lower.includes('limit') || 
    lower.includes('connection') || 
    lower.includes('blocked') || 
    lower.includes('must be') || 
    lower.includes('please fill') || 
    lower.includes('select at least') || 
    lower.includes('time up');

  if (isErrorOrWarning && DICT[en]) {
    return bi(en, DICT[en]);
  }
  return en;
}
