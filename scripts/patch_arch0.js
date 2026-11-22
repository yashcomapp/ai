const fs = require('fs');
let content = fs.readFileSync('scripts/build_clean_mth1_ch6_sub4.py', 'utf8');

const target = `            "{1} is {0} years of age. Under the traditional income tax regime, what is the basic exemption limit (income up to which income tax is Nil)?",
            "What is the basic tax-free exemption limit for {1} whose age is {0} years?",
            "Find the income tax basic exemption limit for general citizen {1} (age {0} years):",
            "If {1} is aged {0} years, up to what annual taxable income is tax liability Nil?",
            "Determine the threshold limit of tax exemption for {1} (age {0} years):",
            "What is the Nil-tax threshold for an individual {1} of age {0} years?",
            "Compute the basic income tax exemption limit for {1} having age {0} years:",
            "How much income is completely exempt from income tax for {1} aged {0} years?",
            "Calculate the basic tax exemption floor for {1} (age {0} years):",
            "Find the tax-free basic slab for individual {1} of age {0} years:"`;

const replacement = `            "{1} is {0} years old. Under the traditional regime, determine the maximum tax-free income threshold:",
            "How much annual taxable income can {1} (aged {0}) earn before any income tax liability begins?",
            "For a working professional {1} of age {0} years, state the basic exemption slab where tax rate is zero:",
            "What is the non-taxable income floor applicable to {1} at age {0} years?",
            "Under standard personal tax slabs, up to what amount is {1} (age {0}) completely exempt from income tax?",
            "Identify the Nil-tax slab boundary for {1}, who is currently {0} years of age:",
            "At age {0}, {1} pays 0% income tax up to which specific earnings limit?",
            "Determine the initial tax-free slab granted to {1} (age {0} years):",
            "What is the lower exemption boundary below which {1} (age {0}) owes zero tax?",
            "State the zero-tax limit for {1} whose age is recorded as {0} years:"`;

if (content.includes(target)) {
  content = content.replace(target, replacement);
  fs.writeFileSync('scripts/build_clean_mth1_ch6_sub4.py', content, 'utf8');
  console.log('Successfully replaced arch 0 tmpls in build_clean_mth1_ch6_sub4.py');
} else {
  console.log('Target not found, trying normalized search...');
  const normContent = content.replace(/\r\n/g, '\n');
  const normTarget = target.replace(/\r\n/g, '\n');
  if (normContent.includes(normTarget)) {
    const normReplacement = replacement.replace(/\r\n/g, '\n');
    const updated = normContent.replace(normTarget, normReplacement);
    fs.writeFileSync('scripts/build_clean_mth1_ch6_sub4.py', updated, 'utf8');
    console.log('Successfully replaced via normalized newline!');
  } else {
    console.log('Normalized target still not found');
  }
}
