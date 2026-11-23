/**
 * scripts/fix_remaining_b2_ac.js
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

const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

const REPLACEMENTS = {
  'CBSE-8-MGP1-7-7.3-OTF-054': {
    text: "True or False: In any proportion \\(a : b :: c : d\\), the product of the extremes is equal to the product of the means, that is, \\(a \\times d = b \\times c\\).",
    options: ["True", "False"],
    correctAnswer: "True",
    solution: "**Step 1: Cross-multiplication property**\nIn Ganita Prakash Chapter 7, two ratios \\(a : b\\) and \\(c : d\\) are proportional if and only if \\(a \\times d = b \\times c\\) (or \\(ad = bc\\)).\n\n**Step 2: Conclusion**\nThe product of extremes equals the product of means. The statement is True."
  },
  'CBSE-8-MGP1-7-7.1-OSC-031': {
    text: "What is the simplest form of the ratio of \\(60\\text{ mm}\\) to \\(40\\text{ mm}\\)?",
    options: [
      "\\(3 : 2\\)",
      "\\(2 : 3\\)",
      "\\(6 : 4\\)",
      "\\(3 : 1\\)"
    ],
    correctAnswer: "\\(3 : 2\\)",
    solution: "**Step 1: Find the HCF of 60 and 40**\n\\(\\text{HCF}(60, 40) = 20\\).\n\n**Step 2: Divide terms by HCF**\n\\(\\frac{60}{20} : \\frac{40}{20} = 3 : 2\\).\n\n**Step 3: Conclusion**\nThe simplest form is \\(3 : 2\\) (Option A)."
  },
  'CBSE-8-MGP1-7-7.3-OSC-082': {
    text: "If \\(14 : 21\\) is proportional to \\(2 : x\\), what is the value of \\(x\\)?",
    options: [
      "\\(3\\)",
      "\\(4\\)",
      "\\(6\\)",
      "\\(7\\)"
    ],
    correctAnswer: "\\(3\\)",
    solution: "**Step 1: Set up the proportion**\n\\(14 : 21 :: 2 : x\\).\n\n**Step 2: Apply cross-multiplication**\n\\(14 \\times x = 21 \\times 2 = 42\\).\n\n**Step 3: Solve for x**\n\\(x = \\frac{42}{14} = 3\\). Option A is correct."
  }
};

async function main() {
  console.log('Replacing remaining 3 questions...');
  const batch = adminDb.batch();
  for (const [docId, rep] of Object.entries(REPLACEMENTS)) {
    const docRef = adminDb.collection('questions').doc(docId);
    batch.update(docRef, {
      text: rep.text,
      options: rep.options,
      correctAnswer: rep.correctAnswer,
      solution: rep.solution,
      updatedAt: new Date().toISOString()
    });
  }
  await batch.commit();
  console.log('✓ Successfully replaced remaining 3 questions in Firestore!');
}

main().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
