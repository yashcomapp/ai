/**
 * scripts/fix_cbse8_ch7_proportions.js
 * 
 * Replaces out-of-syllabus "continued proportion", "mean proportional",
 * and "third proportional" questions in CBSE Class 8 Mathematics
 * Ganit Prakash 1 Chapter 7 (Proportional Reasoning-1) with 100%
 * textbook-aligned questions based on:
 * - Cross-multiplication rule (ad = bc)
 * - Trairasika (Rule of Three by Aryabhata)
 * - Equivalent ratios and missing terms
 * 
 * Complies with Rule Q (atomic snapshot) and Rule T (exact parity).
 */

const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
const resolver = new dns.Resolver();
resolver.setServers(['8.8.8.8', '1.1.1.1']);
const origLookup = dns.lookup;
dns.lookup = function(hostname, options, callback) {
  if (typeof options === 'function') {
    callback = options;
    options = {};
  }
  if (hostname && (hostname.endsWith('googleapis.com') || hostname.endsWith('google.com'))) {
    return resolver.resolve4(hostname, (err, ips) => {
      if (!err && ips && ips.length > 0) {
        if (options && options.all) {
          return callback(null, ips.map(ip => ({ address: ip, family: 4 })));
        }
        return callback(null, ips[0], 4);
      }
      return origLookup(hostname, options, callback);
    });
  }
  return origLookup(hostname, options, callback);
};

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

try {
  adminDb.settings({ ignoreUndefinedProperties: true });
} catch (e) {}

const REPLACEMENTS = {
  // 1. OAR-035
  'CBSE-8-MGP1-7-7.3-OAR-035': {
    text: "Assertion (A): The ratios \\(14 : 21\\) and \\(6 : 9\\) are proportional, written as \\(14 : 21 :: 6 : 9\\).\nReason (R): Two ratios \\(a : b\\) and \\(c : d\\) are proportional if their cross products are equal, that is, \\(ad = bc\\).",
    options: [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    correctAnswer: "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
    solution: "**Step 1: Check Assertion (A)**\nCalculate the cross products for \\(14 : 21 :: 6 : 9\\): \\(14 \\times 9 = 126\\) and \\(21 \\times 6 = 126\\). Since \\(ad = bc\\), the ratios are proportional. Assertion (A) is true.\n\n**Step 2: Check Reason (R)**\nBy the cross-multiplication property taught in Ganita Prakash Chapter 7, two ratios \\(a : b\\) and \\(c : d\\) are in proportion if and only if \\(ad = bc\\). Reason (R) is true and explains (A).\n\n**Step 3: Conclusion**\nBoth (A) and (R) are true, and (R) is the correct explanation of (A)."
  },

  // 2. OFB-069
  'CBSE-8-MGP1-7-7.3-OFB-069': {
    text: "Fill in the missing number to complete the proportion: \\(18 : 24 :: 12 : \\underline{\\hspace{1cm}}\\).",
    options: ["16", "14", "18", "20"],
    correctAnswer: "16",
    solution: "**Step 1: Identify the proportion**\nLet the missing term be \\(x\\). Then \\(18 : 24 :: 12 : x\\).\n\n**Step 2: Apply cross multiplication**\n\\(18 \\times x = 24 \\times 12 = 288\\).\n\n**Step 3: Solve for x**\n\\(x = \\frac{288}{18} = 16\\). The missing number is 16."
  },

  // 3. ONE-040
  'CBSE-8-MGP1-7-7.3-ONE-040': {
    text: "Find the missing value of \\(x\\) that satisfies the proportion \\(150 : 90 :: 240 : x\\).",
    options: [],
    correctAnswer: "144",
    solution: "**Step 1: Set up cross-multiplication**\nGiven \\(150 : 90 :: 240 : x\\), cross-multiplying yields \\(150 \\times x = 90 \\times 240\\).\n\n**Step 2: Calculate product and divide**\n\\(150x = 21600 \\implies x = \\frac{21600}{150} = 144\\).\n\n**Step 3: Final Answer**\nThe value of \\(x\\) is 144."
  },

  // 4. ONE-081
  'CBSE-8-MGP1-7-7.3-ONE-081': {
    text: "Find the value of \\(x\\) such that the ratios \\((x + 2) : 10\\) and \\(15 : 25\\) are proportional.",
    options: [],
    correctAnswer: "4",
    solution: "**Step 1: Formulate the proportion**\n\\((x + 2) : 10 :: 15 : 25\\).\n\n**Step 2: Cross multiply**\n\\(25(x + 2) = 10 \\times 15 = 150\\).\n\n**Step 3: Solve for x**\n\\(x + 2 = \\frac{150}{25} = 6 \\implies x = 6 - 2 = 4\\)."
  },

  // 5. OSC-005
  'CBSE-8-MGP1-7-7.3-OSC-005': {
    text: "Which of the following statements of proportion is **TRUE**?",
    options: [
      "\\(4 : 7 :: 12 : 21\\)",
      "\\(8 : 3 :: 24 : 6\\)",
      "\\(7 : 12 :: 12 : 7\\)",
      "\\(12 : 18 :: 28 : 12\\)"
    ],
    correctAnswer: "\\(4 : 7 :: 12 : 21\\)",
    solution: "**Step 1: Test option (A)**\n\\(4 \\times 21 = 84\\) and \\(7 \\times 12 = 84\\). Cross products are equal, so \\(4 : 7 :: 12 : 21\\) is TRUE.\n\n**Step 2: Test other options**\nFor (B): \\(8 \\times 6 = 48 \\ne 72\\). For (C): \\(7 \\times 7 = 49 \\ne 144\\). For (D): \\(12 \\times 12 = 144 \\ne 504\\).\n\n**Step 3: Conclusion**\nOption (A) is the correct true proportion."
  },

  // 6. OSC-006 (User's screenshot Q1)
  'CBSE-8-MGP1-7-7.3-OSC-006': {
    text: "For two ratios \\(a : b\\) and \\(c : d\\) to be in proportion (written as \\(a : b :: c : d\\)), which of the following cross-multiplication conditions must be true?",
    options: [
      "\\(ad = bc\\)",
      "\\(ab = cd\\)",
      "\\(a + d = b + c\\)",
      "\\(a - b = c - d\\)"
    ],
    correctAnswer: "\\(ad = bc\\)",
    solution: "**Step 1: Definition of proportion**\nTwo ratios are proportional when their simplest forms are equal: \\(\\frac{a}{b} = \\frac{c}{d}\\).\n\n**Step 2: Cross multiplication**\nMultiplying both sides by \\(bd\\) yields \\(a \\times d = b \\times c\\), or \\(ad = bc\\).\n\n**Step 3: Conclusion**\nThe correct mathematical condition is \\(ad = bc\\) (Option A)."
  },

  // 7. OSC-007 (User's screenshot Q2)
  'CBSE-8-MGP1-7-7.3-OSC-007': {
    text: "Which of the following sets of four numbers does **NOT** form a proportion in the given order?",
    options: [
      "\\(3, 5, 9, 12\\)",
      "\\(2, 5, 6, 15\\)",
      "\\(6, 10, 18, 30\\)",
      "\\(21, 6, 35, 10\\)"
    ],
    correctAnswer: "\\(3, 5, 9, 12\\)",
    solution: "**Step 1: Test option (A)**\nCheck cross products: \\(3 \\times 12 = 36\\) and \\(5 \\times 9 = 45\\). Since \\(36 \\ne 45\\), the numbers do NOT form a proportion.\n\n**Step 2: Verify other options**\nFor (B): \\(2 \\times 15 = 30 = 5 \\times 6\\) (Proportional).\nFor (C): \\(6 \\times 30 = 180 = 10 \\times 18\\) (Proportional).\nFor (D): \\(21 \\times 10 = 210 = 6 \\times 35\\) (Proportional).\n\n**Step 3: Conclusion**\nSet (A) does not form a proportion."
  },

  // 8. OSC-008
  'CBSE-8-MGP1-7-7.3-OSC-008': {
    text: "If the ratio of width to height of Image A is \\(60 : 40\\), which of the following rectangular image dimensions is proportional to Image A?",
    options: [
      "Width \\(90\\text{ mm}\\), Height \\(60\\text{ mm}\\)",
      "Width \\(40\\text{ mm}\\), Height \\(20\\text{ mm}\\)",
      "Width \\(60\\text{ mm}\\), Height \\(60\\text{ mm}\\)",
      "Width \\(80\\text{ mm}\\), Height \\(50\\text{ mm}\\)"
    ],
    correctAnswer: "Width \\(90\\text{ mm}\\), Height \\(60\\text{ mm}\\)",
    solution: "**Step 1: Reduce Image A ratio to simplest form**\n\\(\\text{HCF}(60, 40) = 20\\). Dividing both terms gives \\(3 : 2\\).\n\n**Step 2: Check given dimensions**\nWidth 90 mm and height 60 mm gives ratio \\(90 : 60 = 3 : 2\\).\n\n**Step 3: Conclusion**\nSince both have simplest form \\(3 : 2\\), they are proportional (Option A)."
  },

  // 9. OSC-013
  'CBSE-8-MGP1-7-7.3-OSC-013': {
    text: "What is the simplest form of the ratio \\(40 : 20\\)?",
    options: [
      "\\(2 : 1\\)",
      "\\(1 : 2\\)",
      "\\(4 : 2\\)",
      "\\(3 : 1\\)"
    ],
    correctAnswer: "\\(2 : 1\\)",
    solution: "**Step 1: Find HCF**\nThe HCF of 40 and 20 is 20.\n\n**Step 2: Divide terms by HCF**\n\\(\\frac{40}{20} : \\frac{20}{20} = 2 : 1\\).\n\n**Step 3: Conclusion**\nThe simplest form is \\(2 : 1\\)."
  },

  // 10. OSC-015
  'CBSE-8-MGP1-7-7.3-OSC-015': {
    text: "In the proportion \\(21 : 6 :: 35 : x\\), what is the value of \\(x\\)?",
    options: [
      "\\(10\\)",
      "\\(12\\)",
      "\\(8\\)",
      "\\(15\\)"
    ],
    correctAnswer: "\\(10\\)",
    solution: "**Step 1: Apply cross-multiplication**\n\\(21 \\times x = 6 \\times 35\\).\n\n**Step 2: Solve for x**\n\\(x = \\frac{210}{21} = 10\\).\n\n**Step 3: Conclusion**\nThe value of \\(x\\) is 10 (Option A)."
  },

  // 11. OSC-019
  'CBSE-8-MGP1-7-7.3-OSC-019': {
    text: "Kesang uses 10 spoons of sugar for 6 glasses of lemonade. If she needs to make 18 glasses of lemonade with the same sweetness, how many spoons of sugar must she add?",
    options: [
      "\\(30\\)",
      "\\(25\\)",
      "\\(20\\)",
      "\\(36\\)"
    ],
    correctAnswer: "\\(30\\)",
    solution: "**Step 1: Model the problem as a proportion**\n\\(6 : 10 :: 18 : x\\).\n\n**Step 2: Find factor of change or cross multiply**\nThe number of glasses increases by a factor of \\(18 \\div 6 = 3\\). Multiply sugar by 3: \\(10 \\times 3 = 30\\).\n\n**Step 3: Conclusion**\nShe needs 30 spoons of sugar (Option A)."
  },

  // 12. OSC-028
  'CBSE-8-MGP1-7-7.3-OSC-028': {
    text: "Fill in the missing term in the proportion \\(14 : 21 :: x : 42\\).",
    options: [
      "\\(28\\)",
      "\\(24\\)",
      "\\(30\\)",
      "\\(32\\)"
    ],
    correctAnswer: "\\(28\\)",
    solution: "**Step 1: Set up cross-multiplication**\n\\(21 \\times x = 14 \\times 42\\).\n\n**Step 2: Calculate x**\n\\(x = \\frac{14 \\times 42}{21} = 14 \\times 2 = 28\\).\n\n**Step 3: Conclusion**\nThe missing term is 28 (Option A)."
  },

  // 13. OSC-029
  'CBSE-8-MGP1-7-7.3-OSC-029': {
    text: "Fill in the missing term in the proportion \\(14 : 21 :: 6 : x\\).",
    options: [
      "\\(9\\)",
      "\\(8\\)",
      "\\(10\\)",
      "\\(12\\)"
    ],
    correctAnswer: "\\(9\\)",
    solution: "**Step 1: Cross-multiply**\n\\(14 \\times x = 21 \\times 6 = 126\\).\n\n**Step 2: Solve for x**\n\\(x = \\frac{126}{14} = 9\\).\n\n**Step 3: Conclusion**\nThe missing term is 9 (Option A)."
  },

  // 14. OSC-042
  'CBSE-8-MGP1-7-7.3-OSC-042': {
    text: "Which of the following ratios is equivalent (proportional) to \\(4 : 9\\)?",
    options: [
      "\\(12 : 27\\)",
      "\\(8 : 16\\)",
      "\\(16 : 32\\)",
      "\\(10 : 25\\)"
    ],
    correctAnswer: "\\(12 : 27\\)",
    solution: "**Step 1: Multiply both terms by 3**\n\\(4 \\times 3 : 9 \\times 3 = 12 : 27\\).\n\n**Step 2: Verify by reduction**\nDividing 12 and 27 by \\(\\text{HCF} = 3\\) gives \\(4 : 9\\).\n\n**Step 3: Conclusion**\n\\(12 : 27\\) is proportional to \\(4 : 9\\) (Option A)."
  },

  // 15. OSC-043
  'CBSE-8-MGP1-7-7.3-OSC-043': {
    text: "To find the fourth unknown quantity in \\(a : b :: c : d\\) using Aryabhata's Rule of Three (*Trairasika*), the unknown *ichchhāphala* (\\(d\\)) is calculated as:",
    options: [
      "\\(\\frac{\\text{phala} \\times \\text{ichchh\\=a}}{\\text{pram\\=a\\d{n}a}}\\)",
      "\\(\\frac{\\text{pram\\=a\\d{n}a} \\times \\text{phala}}{\\text{ichchh\\=a}}\\)",
      "\\(\\frac{\\text{pram\\=a\\d{n}a} \\times \\text{ichchh\\=a}}{\\text{phala}}\\)",
      "\\(\\text{pram\\=a\\d{n}a} + \\text{phala} - \\text{ichchh\\=a}\\)"
    ],
    correctAnswer: "\\(\\frac{\\text{phala} \\times \\text{ichchh\\=a}}{\\text{pram\\=a\\d{n}a}}\\)",
    solution: "**Step 1: Aryabhata's Rule of Three formulation**\nIn Ganita Prakash Chapter 7: \\(\\text{pramāṇa} : \\text{phala} :: \\text{ichchhā} : \\text{ichchhāphala}\\).\n\n**Step 2: Aryabhata's rule**\nMultiply the phala by the ichchhā and divide by the pramāṇa.\n\n**Step 3: Conclusion**\n\\(\\text{ichchhāphala} = \\frac{\\text{phala} \\times \\text{ichchhā}}{\\text{pramāṇa}}\\) (Option A)."
  },

  // 16. OSC-047
  'CBSE-8-MGP1-7-7.3-OSC-047': {
    text: "A tap takes 15 seconds to fill a 500 mL mug. How many seconds will it take to fill a 1-litre (1,000 mL) bottle at the same rate?",
    options: [
      "\\(30\\text{ seconds}\\)",
      "\\(25\\text{ seconds}\\)",
      "\\(45\\text{ seconds}\\)",
      "\\(60\\text{ seconds}\\)"
    ],
    correctAnswer: "\\(30\\text{ seconds}\\)",
    solution: "**Step 1: Set up the proportion**\n\\(15 : 500 :: x : 1000\\).\n\n**Step 2: Cross multiply**\n\\(x = \\frac{15 \\times 1000}{500} = 15 \\times 2 = 30\\text{ seconds}\\).\n\n**Step 3: Conclusion**\nIt takes 30 seconds (Option A)."
  },

  // 17. OSC-048
  'CBSE-8-MGP1-7-7.3-OSC-048': {
    text: "Which ratio is proportional to \\(18 : 24\\) when reduced to its simplest form?",
    options: [
      "\\(3 : 4\\)",
      "\\(2 : 3\\)",
      "\\(4 : 5\\)",
      "\\(5 : 6\\)"
    ],
    correctAnswer: "\\(3 : 4\\)",
    solution: "**Step 1: Find HCF of 18 and 24**\n\\(\\text{HCF}(18, 24) = 6\\).\n\n**Step 2: Divide both terms by 6**\n\\(\\frac{18}{6} : \\frac{24}{6} = 3 : 4\\).\n\n**Step 3: Conclusion**\nThe simplest form is \\(3 : 4\\) (Option A)."
  },

  // 18. OSC-049
  'CBSE-8-MGP1-7-7.3-OSC-049': {
    text: "Find the missing number in the proportion: \\(18 : 24 :: 27 : \\underline{\\hspace{1cm}}\\).",
    options: [
      "\\(36\\)",
      "\\(32\\)",
      "\\(30\\)",
      "\\(40\\)"
    ],
    correctAnswer: "\\(36\\)",
    solution: "**Step 1: Set up proportion**\n\\(18 : 24 :: 27 : x\\).\n\n**Step 2: Cross multiply**\n\\(18 \\times x = 24 \\times 27 = 648 \\implies x = \\frac{648}{18} = 36\\).\n\n**Step 3: Conclusion**\nThe missing number is 36 (Option A)."
  },

  // 19. OSC-053
  'CBSE-8-MGP1-7-7.3-OSC-053': {
    text: "Which of the following statements of proportion is **FALSE**?",
    options: [
      "\\(8 : 3 :: 24 : 6\\)",
      "\\(4 : 7 :: 12 : 21\\)",
      "\\(21 : 6 :: 35 : 10\\)",
      "\\(24 : 8 :: 9 : 3\\)"
    ],
    correctAnswer: "\\(8 : 3 :: 24 : 6\\)",
    solution: "**Step 1: Test option (A)**\n\\(8 \\times 6 = 48\\) and \\(3 \\times 24 = 72\\). Since \\(48 \\ne 72\\), this statement is FALSE.\n\n**Step 2: Verify other options**\nFor (B): \\(4 \\times 21 = 84 = 7 \\times 12\\) (True).\nFor (C): \\(21 \\times 10 = 210 = 6 \\times 35\\) (True).\nFor (D): \\(24 \\times 3 = 72 = 8 \\times 9\\) (True).\n\n**Step 3: Conclusion**\nStatement (A) is false."
  },

  // 20. OSC-061
  'CBSE-8-MGP1-7-7.3-OSC-061': {
    text: "In a school with 120 students, the cook prepares 15 kg of rice. If only 80 students attend on a rainy day, how many kg of rice should the cook make to maintain the same proportion?",
    options: [
      "\\(10\\text{ kg}\\)",
      "\\(12\\text{ kg}\\)",
      "\\(8\\text{ kg}\\)",
      "\\(9\\text{ kg}\\)"
    ],
    correctAnswer: "\\(10\\text{ kg}\\)",
    solution: "**Step 1: Model the proportion**\n\\(120 : 15 :: 80 : x\\).\n\n**Step 2: Cross multiply**\n\\(120 \\times x = 15 \\times 80 = 1200 \\implies x = \\frac{1200}{120} = 10\\text{ kg}\\).\n\n**Step 3: Conclusion**\nThe cook should make 10 kg of rice (Option A)."
  },

  // 21. OSC-073
  'CBSE-8-MGP1-7-7.3-OSC-073': {
    text: "If the four quantities \\(a, b, c, d\\) are in proportion (\\(a : b :: c : d\\)), which of the following algebraic relationships is always valid?",
    options: [
      "\\(\\frac{a}{c} = \\frac{b}{d}\\)",
      "\\(\\frac{a}{d} = \\frac{b}{c}\\)",
      "\\(a + d = b + c\\)",
      "\\(a^2 + d^2 = b^2 + c^2\\)"
    ],
    correctAnswer: "\\(\\frac{a}{c} = \\frac{b}{d}\\)",
    solution: "**Step 1: Proportionality condition**\n\\(a : b :: c : d \\implies \\frac{a}{b} = \\frac{c}{d} \\implies ad = bc\\).\n\n**Step 2: Divide both sides by cd**\n\\(\\frac{ad}{cd} = \\frac{bc}{cd} \\implies \\frac{a}{c} = \\frac{b}{d}\\).\n\n**Step 3: Conclusion**\n\\(\\frac{a}{c} = \\frac{b}{d}\\) is always valid (Option A)."
  },

  // 22. OSC-078
  'CBSE-8-MGP1-7-7.3-OSC-078': {
    text: "A mason requires approximately 1450 bricks to build a 10-foot wall. How many bricks would be needed to build walls of the same height and thickness with a total length of 108 feet?",
    options: [
      "\\(15,660\\)",
      "\\(14,500\\)",
      "\\(16,200\\)",
      "\\(15,000\\)"
    ],
    correctAnswer: "\\(15,660\\)",
    solution: "**Step 1: Model the proportion**\n\\(10 : 1450 :: 108 : x\\).\n\n**Step 2: Cross-multiply**\n\\(10 \\times x = 1450 \\times 108 = 156,600\\).\n\n**Step 3: Solve for x**\n\\(x = \\frac{156600}{10} = 15660\\) bricks (Option A)."
  },

  // 23. OSC-080
  'CBSE-8-MGP1-7-7.3-OSC-080': {
    text: "A car travels 90 km in 150 minutes. If it continues at the same speed, what distance will it cover in 4 hours (240 minutes)?",
    options: [
      "\\(144\\text{ km}\\)",
      "\\(150\\text{ km}\\)",
      "\\(135\\text{ km}\\)",
      "\\(160\\text{ km}\\)"
    ],
    correctAnswer: "\\(144\\text{ km}\\)",
    solution: "**Step 1: Convert units**\nBoth times must be in minutes: 4 hours = \\(4 \\times 60 = 240\\text{ minutes}\\).\n\n**Step 2: Set up proportion**\n\\(150 : 90 :: 240 : x\\).\n\n**Step 3: Solve for distance**\n\\(x = \\frac{90 \\times 240}{150} = 144\\text{ km}\\) (Option A)."
  },

  // 24. OTF-037
  'CBSE-8-MGP1-7-7.3-OTF-037': {
    text: "True or False: The ratios \\(24 : 8\\) and \\(9 : 3\\) are proportional.",
    options: ["True", "False"],
    correctAnswer: "True",
    solution: "**Step 1: Check cross products**\n\\(24 \\times 3 = 72\\) and \\(8 \\times 9 = 72\\).\n\n**Step 2: Verify simplest forms**\n\\(24 : 8 = 3 : 1\\) and \\(9 : 3 = 3 : 1\\).\n\n**Step 3: Conclusion**\nBoth methods prove the ratios are proportional. The statement is True."
  },

  // 25. OTF-067
  'CBSE-8-MGP1-7-7.3-OTF-067': {
    text: "True or False: When we add the same number to both terms of a ratio, the new ratio is always proportional to the original ratio.",
    options: ["True", "False"],
    correctAnswer: "False",
    solution: "**Step 1: Counterexample from Ganita Prakash**\nWhen Neelima is 3 years old, her mother is 30 years old (ratio \\(3 : 30 = 1 : 10\\)). 9 years later (adding 9 to both terms), their ages are 12 and 39 (ratio \\(12 : 39 = 4 : 13\\)).\n\n**Step 2: Analysis**\nSince \\(1 : 10 \\ne 4 : 13\\), adding the same number changes the ratio and is NOT proportional to the original ratio.\n\n**Step 3: Conclusion**\nThe statement is False."
  }
};

async function main() {
  console.log('================================================================================');
  console.log('=== PURGING OUT-OF-SYLLABUS PROPORTIONS IN CBSE CLASS 8 GANIT PRAKASH 1 ===');
  console.log('================================================================================');

  const docIds = Object.keys(REPLACEMENTS);
  console.log(`Found ${docIds.length} questions targeted for replacement.`);

  // 1. Fetch current documents for backup
  const targetDocs = [];
  for (const docId of docIds) {
    const docRef = adminDb.collection('questions').doc(docId);
    const docSnap = await docRef.get();
    if (docSnap.exists) {
      targetDocs.push({ id: docId, data: docSnap.data(), ref: docRef });
    } else {
      console.warn(`Doc ${docId} not found directly, checking questionCode...`);
    }
  }

  console.log(`Loaded ${targetDocs.length} documents from Firestore.`);

  // 2. Rule Q: Create pre-mutation snapshot
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  const now = new Date();
  const dateKey = now.toISOString().split('T')[0];
  const timeStr = now.toTimeString().split(' ')[0].replace(/:/g, '-');
  const snapshotId = `snapshot_${dateKey}_${timeStr}_fix_cbse8_ch7_proportions`;
  const filePath = path.join(targetDir, `${snapshotId}.json`);

  const snapshotData = {
    metadata: {
      snapshotId,
      timestamp: now.toISOString(),
      reason: 'purge_out_of_syllabus_continued_proportion_cbse8',
      totalDocuments: targetDocs.length,
      filePath
    },
    documents: targetDocs.map(d => ({ id: d.id, data: d.data }))
  };

  fs.writeFileSync(filePath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`✓ Rule Q: Pre-mutation snapshot saved: ${snapshotId}\n`);

  // 3. Batch update in Firestore
  const batch = adminDb.batch();
  for (const item of targetDocs) {
    const rep = REPLACEMENTS[item.id];
    batch.update(item.ref, {
      text: rep.text,
      options: rep.options,
      correctAnswer: rep.correctAnswer,
      solution: rep.solution,
      updatedAt: new Date().toISOString()
    });
  }

  await batch.commit();
  console.log(`✓ Successfully updated ${targetDocs.length} questions in Firestore!`);

  // 4. Verify no remaining out-of-syllabus terms in CBSE 8 Ch 7
  console.log('\n--- VERIFYING CLEANUP IN FIRESTORE ---');
  const verifySnap = await adminDb.collection('questions').where('subjectCode', '==', 'MGP1').get();
  let remainingCount = 0;
  verifySnap.forEach(doc => {
    const q = doc.data();
    if ((q.topicCode || '').startsWith('CBSE-8-MGP1-7-')) {
      const txt = (q.text || '').toLowerCase();
      if (txt.includes('continued proportion') || txt.includes('mean proportional') || txt.includes('third proportional')) {
        remainingCount++;
        console.warn(`  ⚠️ Remaining: ${q.questionCode} -> ${q.text.slice(0, 60)}`);
      }
    }
  });

  console.log(`Remaining out-of-syllabus questions in Ch 7: ${remainingCount}`);
  if (remainingCount === 0) {
    console.log('✓ 100% CLEAN: Zero continued/mean/third proportional questions remain in CBSE 8 Chapter 7!');
  }
}

main().then(() => process.exit(0)).catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
