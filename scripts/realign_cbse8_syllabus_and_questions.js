const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

// Load environment variables
const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf-8');
  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx > 0) {
        let v = trimmed.slice(idx + 1).trim();
        if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = v;
      }
    }
  });
}

const sa = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({
    credential: admin.credential.cert(cred),
    projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom'
  });
}
const db = admin.firestore();

// ── DEFINITIONS OF NEW OFFICIAL CBSE CLASS 8 GANITA PRAKASH SYLLABUS ──
const MGP1_CHAPTERS = [
  {
    number: "1",
    name: "A Square and a Cube",
    topics: [
      {
        number: "1.1",
        name: "Properties of Square Numbers & Unit Digits",
        topicCode: "CBSE-8-MGP1-1-1.1",
        subtopics: [
          { number: "1.1.1", name: "Ending digits of square numbers", topicCode: "CBSE-8-MGP1-1-1.1.1" },
          { number: "1.1.2", name: "Zeros at the end of squares", topicCode: "CBSE-8-MGP1-1-1.1.2" },
          { number: "1.1.3", name: "Squares of even and odd numbers", topicCode: "CBSE-8-MGP1-1-1.1.3" }
        ]
      },
      {
        number: "1.2",
        name: "Patterns in Square Numbers & Pythagorean Triplets",
        topicCode: "CBSE-8-MGP1-1-1.2",
        subtopics: [
          { number: "1.2.1", name: "Sum of consecutive odd numbers", topicCode: "CBSE-8-MGP1-1-1.2.1" },
          { number: "1.2.2", name: "Non-square numbers between consecutive squares", topicCode: "CBSE-8-MGP1-1-1.2.2" },
          { number: "1.2.3", name: "Pythagorean triplets formula (2m, m²-1, m²+1)", topicCode: "CBSE-8-MGP1-1-1.2.3" }
        ]
      },
      {
        number: "1.3",
        name: "Finding Square Roots by Prime Factorisation",
        topicCode: "CBSE-8-MGP1-1-1.3",
        subtopics: [
          { number: "1.3.1", name: "Square root as inverse of squaring", topicCode: "CBSE-8-MGP1-1-1.3.1" },
          { number: "1.3.2", name: "Prime factor pairing", topicCode: "CBSE-8-MGP1-1-1.3.2" },
          { number: "1.3.3", name: "Smallest multiplier or divisor to get perfect square", topicCode: "CBSE-8-MGP1-1-1.3.3" }
        ]
      },
      {
        number: "1.4",
        name: "Finding Square Roots by Long Division & Decimals",
        topicCode: "CBSE-8-MGP1-1-1.4",
        subtopics: [
          { number: "1.4.1", name: "Long division algorithm", topicCode: "CBSE-8-MGP1-1-1.4.1" },
          { number: "1.4.2", name: "Square roots of decimals", topicCode: "CBSE-8-MGP1-1-1.4.2" },
          { number: "1.4.3", name: "Estimating square roots in word problems", topicCode: "CBSE-8-MGP1-1-1.4.3" }
        ]
      },
      {
        number: "1.5",
        name: "Cubes & Patterns in Cube Numbers",
        topicCode: "CBSE-8-MGP1-1-1.5",
        subtopics: [
          { number: "1.5.1", name: "Cube numbers definition", topicCode: "CBSE-8-MGP1-1-1.5.1" },
          { number: "1.5.2", name: "Adding consecutive odd numbers for cubes", topicCode: "CBSE-8-MGP1-1-1.5.2" },
          { number: "1.5.3", name: "Prime factorisation of cubes", topicCode: "CBSE-8-MGP1-1-1.5.3" }
        ]
      },
      {
        number: "1.6",
        name: "Cube Roots by Prime Factorisation & Estimation",
        topicCode: "CBSE-8-MGP1-1-1.6",
        subtopics: [
          { number: "1.6.1", name: "Cube root symbol and definition", topicCode: "CBSE-8-MGP1-1-1.6.1" },
          { number: "1.6.2", name: "Triplets of prime factors", topicCode: "CBSE-8-MGP1-1-1.6.2" },
          { number: "1.6.3", name: "Estimation method for cube roots", topicCode: "CBSE-8-MGP1-1-1.6.3" }
        ]
      }
    ]
  },
  {
    number: "2",
    name: "Power Play",
    topics: [
      {
        number: "2.1",
        name: "Powers with Negative Integral Exponents",
        topicCode: "CBSE-8-MGP1-2-2.1",
        subtopics: [
          { number: "2.1.1", name: "Multiplicative inverse using negative exponents", topicCode: "CBSE-8-MGP1-2-2.1.1" },
          { number: "2.1.2", name: "Evaluating powers with negative exponents", topicCode: "CBSE-8-MGP1-2-2.1.2" },
          { number: "2.1.3", name: "Expanded form of numbers using negative powers of 10", topicCode: "CBSE-8-MGP1-2-2.1.3" }
        ]
      },
      {
        number: "2.2",
        name: "Laws of Exponents & Simplification",
        topicCode: "CBSE-8-MGP1-2-2.2",
        subtopics: [
          { number: "2.2.1", name: "Product of powers law (a^m * a^n = a^(m+n))", topicCode: "CBSE-8-MGP1-2-2.2.1" },
          { number: "2.2.2", name: "Quotient of powers law (a^m / a^n = a^(m-n))", topicCode: "CBSE-8-MGP1-2-2.2.2" },
          { number: "2.2.3", name: "Power of a power law ((a^m)^n = a^(mn))", topicCode: "CBSE-8-MGP1-2-2.2.3" },
          { number: "2.2.4", name: "Powers with same exponent (a^m * b^m = (ab)^m)", topicCode: "CBSE-8-MGP1-2-2.2.4" },
          { number: "2.2.5", name: "Zero exponent (a^0 = 1)", topicCode: "CBSE-8-MGP1-2-2.2.5" }
        ]
      },
      {
        number: "2.3",
        name: "Standard Form (Scientific Notation) for Large & Small Numbers",
        topicCode: "CBSE-8-MGP1-2-2.3",
        subtopics: [
          { number: "2.3.1", name: "Expressing very small numbers in standard form", topicCode: "CBSE-8-MGP1-2-2.3.1" },
          { number: "2.3.2", name: "Expressing very large numbers in standard form", topicCode: "CBSE-8-MGP1-2-2.3.2" },
          { number: "2.3.3", name: "Converting standard form back to usual decimal form", topicCode: "CBSE-8-MGP1-2-2.3.3" }
        ]
      },
      {
        number: "2.4",
        name: "Comparison & Arithmetic with Exponential Quantities",
        topicCode: "CBSE-8-MGP1-2-2.4",
        subtopics: [
          { number: "2.4.1", name: "Comparing very large and very small quantities", topicCode: "CBSE-8-MGP1-2-2.4.1" },
          { number: "2.4.2", name: "Addition and subtraction of numbers in standard form", topicCode: "CBSE-8-MGP1-2-2.4.2" }
        ]
      }
    ]
  },
  {
    number: "3",
    name: "A Story of Numbers",
    topics: [
      {
        number: "3.1",
        name: "Rational Numbers & Closure, Commutative Properties",
        topicCode: "CBSE-8-MGP1-3-3.1",
        subtopics: [
          { number: "3.1.1", name: "Rational numbers definition (p/q, q != 0)", topicCode: "CBSE-8-MGP1-3-3.1.1" },
          { number: "3.1.2", name: "Closure property under addition, subtraction, multiplication", topicCode: "CBSE-8-MGP1-3-3.1.2" },
          { number: "3.1.3", name: "Commutative property for operations on rationals", topicCode: "CBSE-8-MGP1-3-3.1.3" }
        ]
      },
      {
        number: "3.2",
        name: "Associative, Distributive Properties & Identities",
        topicCode: "CBSE-8-MGP1-3-3.2",
        subtopics: [
          { number: "3.2.1", name: "Associative property for addition and multiplication", topicCode: "CBSE-8-MGP1-3-3.2.1" },
          { number: "3.2.2", name: "Additive identity (0) and additive inverse (negative)", topicCode: "CBSE-8-MGP1-3-3.2.2" },
          { number: "3.2.3", name: "Multiplicative identity (1) and reciprocal", topicCode: "CBSE-8-MGP1-3-3.2.3" },
          { number: "3.2.4", name: "Distributive property of multiplication over addition/subtraction", topicCode: "CBSE-8-MGP1-3-3.2.4" }
        ]
      },
      {
        number: "3.3",
        name: "Representation of Rational Numbers on the Number Line",
        topicCode: "CBSE-8-MGP1-3-3.3",
        subtopics: [
          { number: "3.3.1", name: "Dividing unit intervals into equal parts", topicCode: "CBSE-8-MGP1-3-3.3.1" },
          { number: "3.3.2", name: "Plotting positive and negative rationals", topicCode: "CBSE-8-MGP1-3-3.3.2" }
        ]
      },
      {
        number: "3.4",
        name: "Finding Rational Numbers Between Two Rational Numbers",
        topicCode: "CBSE-8-MGP1-3-3.4",
        subtopics: [
          { number: "3.4.1", name: "Mean / average method", topicCode: "CBSE-8-MGP1-3-3.4.1" },
          { number: "3.4.2", name: "Common denominator method", topicCode: "CBSE-8-MGP1-3-3.4.2" },
          { number: "3.4.3", name: "Density property: Infinitely many rationals exist", topicCode: "CBSE-8-MGP1-3-3.4.3" }
        ]
      }
    ]
  },
  {
    number: "4",
    name: "Quadrilaterals",
    topics: [
      {
        number: "4.1",
        name: "Polygons: Convex, Concave, Regular & Irregular",
        topicCode: "CBSE-8-MGP1-4-4.1",
        subtopics: [
          { number: "4.1.1", name: "Curves: Open, closed, simple, polygon definition", topicCode: "CBSE-8-MGP1-4-4.1.1" },
          { number: "4.1.2", name: "Convex and concave polygons", topicCode: "CBSE-8-MGP1-4-4.1.2" },
          { number: "4.1.3", name: "Regular vs irregular polygons", topicCode: "CBSE-8-MGP1-4-4.1.3" },
          { number: "4.1.4", name: "Number of diagonals in an n-gon: n(n-3)/2", topicCode: "CBSE-8-MGP1-4-4.1.4" }
        ]
      },
      {
        number: "4.2",
        name: "Angle Sum Property & Exterior Angles of Polygons",
        topicCode: "CBSE-8-MGP1-4-4.2",
        subtopics: [
          { number: "4.2.1", name: "Sum of interior angles of n-gon: (n-2) * 180°", topicCode: "CBSE-8-MGP1-4-4.2.1" },
          { number: "4.2.2", name: "Sum of exterior angles of any polygon = 360°", topicCode: "CBSE-8-MGP1-4-4.2.2" },
          { number: "4.2.3", name: "Exterior and interior angle relationship in regular polygons", topicCode: "CBSE-8-MGP1-4-4.2.3" }
        ]
      },
      {
        number: "4.3",
        name: "Properties of Trapezium, Kite & Parallelograms",
        topicCode: "CBSE-8-MGP1-4-4.3",
        subtopics: [
          { number: "4.3.1", name: "Trapezium and isosceles trapezium properties", topicCode: "CBSE-8-MGP1-4-4.3.1" },
          { number: "4.3.2", name: "Kite: Disjoint equal adjacent sides & diagonals", topicCode: "CBSE-8-MGP1-4-4.3.2" },
          { number: "4.3.3", name: "Parallelogram: Opposite sides and angles are equal", topicCode: "CBSE-8-MGP1-4-4.3.3" },
          { number: "4.3.4", name: "Parallelogram: Diagonals bisect each other", topicCode: "CBSE-8-MGP1-4-4.3.4" }
        ]
      },
      {
        number: "4.4",
        name: "Special Parallelograms: Rhombus, Rectangle, Square",
        topicCode: "CBSE-8-MGP1-4-4.4",
        subtopics: [
          { number: "4.4.1", name: "Rhombus: Diagonals perpendicular bisectors", topicCode: "CBSE-8-MGP1-4-4.4.1" },
          { number: "4.4.2", name: "Rectangle: All angles 90° & diagonals equal", topicCode: "CBSE-8-MGP1-4-4.4.2" },
          { number: "4.4.3", name: "Square: Equal sides, right angles & perpendicular equal diagonals", topicCode: "CBSE-8-MGP1-4-4.4.3" }
        ]
      }
    ]
  },
  {
    number: "5",
    name: "Number Play",
    topics: [
      {
        number: "5.1",
        name: "Patterns in Consecutive Numbers, Parity & Breaking Even",
        topicCode: "CBSE-8-MGP1-5-5.1",
        subtopics: [
          { number: "5.1.1", name: "Sum of consecutive natural numbers patterns", topicCode: "CBSE-8-MGP1-5-5.1.1" },
          { number: "5.1.2", name: "Consecutive numbers with + and - signs & parity patterns", topicCode: "CBSE-8-MGP1-5-5.1.2" },
          { number: "5.1.3", name: "Breaking even & algebraic structures for even outcomes", topicCode: "CBSE-8-MGP1-5-5.1.3" }
        ]
      },
      {
        number: "5.2",
        name: "Divisibility Rules & Mathematical Reasons (2, 3, 4, 5, 8, 9, 10, 11)",
        topicCode: "CBSE-8-MGP1-5-5.2",
        subtopics: [
          { number: "5.2.1", name: "Divisibility tests for 2, 5, and 10 using unit digits", topicCode: "CBSE-8-MGP1-5-5.2.1" },
          { number: "5.2.2", name: "Divisibility tests for 3 and 9 using digit sums", topicCode: "CBSE-8-MGP1-5-5.2.2" },
          { number: "5.2.3", name: "Divisibility test for 11 using alternating digit difference", topicCode: "CBSE-8-MGP1-5-5.2.3" },
          { number: "5.2.4", name: "Mathematical reasons using generalized form (100a + 10b + c)", topicCode: "CBSE-8-MGP1-5-5.2.4" }
        ]
      },
      {
        number: "5.3",
        name: "Digital Roots & Modular Patterns",
        topicCode: "CBSE-8-MGP1-5-5.3",
        subtopics: [
          { number: "5.3.1", name: "Digital root calculation & properties", topicCode: "CBSE-8-MGP1-5-5.3.1" },
          { number: "5.3.2", name: "Remainders when divided by 9 and digital roots", topicCode: "CBSE-8-MGP1-5-5.3.2" }
        ]
      },
      {
        number: "5.4",
        name: "Digits in Disguise (Cryptarithms & Number Puzzles)",
        topicCode: "CBSE-8-MGP1-5-5.4",
        subtopics: [
          { number: "5.4.1", name: "Letters for digits in addition problems", topicCode: "CBSE-8-MGP1-5-5.4.1" },
          { number: "5.4.2", name: "Letters for digits in multiplication problems", topicCode: "CBSE-8-MGP1-5-5.4.2" }
        ]
      }
    ]
  },
  {
    number: "6",
    name: "We Distribute, Yet Things Multiply",
    topics: [
      {
        number: "6.1",
        name: "Terms, Factors, Coefficients & Classification of Polynomials",
        topicCode: "CBSE-8-MGP1-6-6.1",
        subtopics: [
          { number: "6.1.1", name: "Terms, variables, constants & numerical coefficients", topicCode: "CBSE-8-MGP1-6-6.1.1" },
          { number: "6.1.2", name: "Like and unlike algebraic terms", topicCode: "CBSE-8-MGP1-6-6.1.2" },
          { number: "6.1.3", name: "Monomials, binomials, trinomials & polynomials", topicCode: "CBSE-8-MGP1-6-6.1.3" }
        ]
      },
      {
        number: "6.2",
        name: "Addition and Subtraction of Algebraic Expressions",
        topicCode: "CBSE-8-MGP1-6-6.2",
        subtopics: [
          { number: "6.2.1", name: "Horizontal and column addition of like terms", topicCode: "CBSE-8-MGP1-6-6.2.1" },
          { number: "6.2.2", name: "Subtraction with sign changes of subtrahend", topicCode: "CBSE-8-MGP1-6-6.2.2" }
        ]
      },
      {
        number: "6.3",
        name: "Multiplication of Monomials, Binomials & Polynomials",
        topicCode: "CBSE-8-MGP1-6-6.3",
        subtopics: [
          { number: "6.3.1", name: "Product of two or more monomials", topicCode: "CBSE-8-MGP1-6-6.3.1" },
          { number: "6.3.2", name: "Multiplying monomial by binomial/trinomial (Distributive law)", topicCode: "CBSE-8-MGP1-6-6.3.2" },
          { number: "6.3.3", name: "Multiplying binomial by binomial (FOIL method)", topicCode: "CBSE-8-MGP1-6-6.3.3" }
        ]
      },
      {
        number: "6.4",
        name: "Standard Algebraic Identities & Geometric Proofs",
        topicCode: "CBSE-8-MGP1-6-6.4",
        subtopics: [
          { number: "6.4.1", name: "Square of a sum identity: (a+b)² = a² + 2ab + b²", topicCode: "CBSE-8-MGP1-6-6.4.1" },
          { number: "6.4.2", name: "Square of a difference identity: (a-b)² = a² - 2ab + b²", topicCode: "CBSE-8-MGP1-6-6.4.2" },
          { number: "6.4.3", name: "Difference of squares identity: (a+b)(a-b) = a² - b²", topicCode: "CBSE-8-MGP1-6-6.4.3" },
          { number: "6.4.4", name: "Product with common term: (x+a)(x+b) = x² + (a+b)x + ab", topicCode: "CBSE-8-MGP1-6-6.4.4" }
        ]
      },
      {
        number: "6.5",
        name: "Applications of Distributive Law & Mental Multiplication",
        topicCode: "CBSE-8-MGP1-6-6.5",
        subtopics: [
          { number: "6.5.1", name: "Fast mental calculations using identities (103², 98², 105*95)", topicCode: "CBSE-8-MGP1-6-6.5.1" },
          { number: "6.5.2", name: "Mind mistakes, mend mistakes: Spotting and correcting algebraic errors", topicCode: "CBSE-8-MGP1-6-6.5.2" }
        ]
      }
    ]
  },
  {
    number: "7",
    name: "Proportional Reasoning 1",
    topics: [
      {
        number: "7.1",
        name: "Ratios, Equivalent Ratios & Scaling",
        topicCode: "CBSE-8-MGP1-7-7.1",
        subtopics: [
          { number: "7.1.1", name: "Observing similarity in change: Dimension scaling", topicCode: "CBSE-8-MGP1-7-7.1.1" },
          { number: "7.1.2", name: "Ratios in simplest form (reducing by HCF)", topicCode: "CBSE-8-MGP1-7-7.1.2" }
        ]
      },
      {
        number: "7.2",
        name: "Comparing Mixtures & Concentration using Ratios",
        topicCode: "CBSE-8-MGP1-7-7.2",
        subtopics: [
          { number: "7.2.1", name: "Comparing sweetness/taste/mixtures using ratios", topicCode: "CBSE-8-MGP1-7-7.2.1" },
          { number: "7.2.2", name: "Unit conversions for ratio consistency", topicCode: "CBSE-8-MGP1-7-7.2.2" }
        ]
      },
      {
        number: "7.3",
        name: "Proportional Ratios, Cross-Multiplication & Checking Proportions",
        topicCode: "CBSE-8-MGP1-7-7.3",
        subtopics: [
          { number: "7.3.1", name: "Checking proportion: Equivalence & cross-product (ad = bc)", topicCode: "CBSE-8-MGP1-7-7.3.1" },
          { number: "7.3.2", name: "Finding missing terms in proportions", topicCode: "CBSE-8-MGP1-7-7.3.2" }
        ]
      },
      {
        number: "7.4",
        name: "The Rule of Three (Trairasika) & Direct Proportion Word Problems",
        topicCode: "CBSE-8-MGP1-7-7.4",
        subtopics: [
          { number: "7.4.1", name: "Trairasika method for finding the fourth proportional", topicCode: "CBSE-8-MGP1-7-7.4.1" },
          { number: "7.4.2", name: "Direct proportion word problems", topicCode: "CBSE-8-MGP1-7-7.4.2" }
        ]
      },
      {
        number: "7.5",
        name: "Sharing Quantities in a Given Ratio",
        topicCode: "CBSE-8-MGP1-7-7.5",
        subtopics: [
          { number: "7.5.1", name: "Dividing total amounts into parts proportional to ratio", topicCode: "CBSE-8-MGP1-7-7.5.1" }
        ]
      }
    ]
  }
];

const MGP2_CHAPTERS = [
  {
    number: "1",
    name: "Fractions in Disguise",
    topics: [
      {
        number: "1.1",
        name: "Interconnecting Fractions, Decimals & Percentages (FDP Trio)",
        topicCode: "CBSE-8-MGP2-1-1.1",
        subtopics: [
          { number: "1.1.1", name: "Converting between fractions, decimals and percentages", topicCode: "CBSE-8-MGP2-1-1.1.1" },
          { number: "1.1.2", name: "Fractional and decimal percentage benchmarks", topicCode: "CBSE-8-MGP2-1-1.1.2" }
        ]
      },
      {
        number: "1.2",
        name: "Percentage Increase, Decrease & Ratio Comparisons",
        topicCode: "CBSE-8-MGP2-1-1.2",
        subtopics: [
          { number: "1.2.1", name: "Finding percentage of a given quantity", topicCode: "CBSE-8-MGP2-1-1.2.1" },
          { number: "1.2.2", name: "Percentage increase and decrease calculations", topicCode: "CBSE-8-MGP2-1-1.2.2" }
        ]
      },
      {
        number: "1.3",
        name: "Profit, Loss, Marked Price & Trade Discounts",
        topicCode: "CBSE-8-MGP2-1-1.3",
        subtopics: [
          { number: "1.3.1", name: "Cost price, selling price, profit and loss percent", topicCode: "CBSE-8-MGP2-1-1.3.1" },
          { number: "1.3.2", name: "Marked price, discount and discount percentage", topicCode: "CBSE-8-MGP2-1-1.3.2" }
        ]
      },
      {
        number: "1.4",
        name: "Sales Tax, VAT & Goods and Services Tax (GST)",
        topicCode: "CBSE-8-MGP2-1-1.4",
        subtopics: [
          { number: "1.4.1", name: "Calculating GST added to bill amount", topicCode: "CBSE-8-MGP2-1-1.4.1" },
          { number: "1.4.2", name: "Finding price before GST was added", topicCode: "CBSE-8-MGP2-1-1.4.2" }
        ]
      },
      {
        number: "1.5",
        name: "Compound Interest Concept & Annual/Half-Yearly Compounding",
        topicCode: "CBSE-8-MGP2-1-1.5",
        subtopics: [
          { number: "1.5.1", name: "Simple interest vs compound interest difference", topicCode: "CBSE-8-MGP2-1-1.5.1" },
          { number: "1.5.2", name: "Compound interest formula A = P(1 + r/100)^n", topicCode: "CBSE-8-MGP2-1-1.5.2" },
          { number: "1.5.3", name: "Compounded half-yearly calculations", topicCode: "CBSE-8-MGP2-1-1.5.3" }
        ]
      }
    ]
  },
  {
    number: "2",
    name: "The Baudhayana–Pythagoras Theorem",
    topics: [
      {
        number: "2.1",
        name: "Right-Angled Triangles & Baudhayana Sulba Sutra Statement",
        topicCode: "CBSE-8-MGP2-2-2.1",
        subtopics: [
          { number: "2.1.1", name: "Baudhayana Sulba Sutra statement & right triangle anatomy", topicCode: "CBSE-8-MGP2-2-2.1.1" },
          { number: "2.1.2", name: "Relationship between squares on hypotenuse and legs", topicCode: "CBSE-8-MGP2-2-2.1.2" }
        ]
      },
      {
        number: "2.2",
        name: "Geometric & Algebraic Proofs of Pythagoras Theorem",
        topicCode: "CBSE-8-MGP2-2-2.2",
        subtopics: [
          { number: "2.2.1", name: "Dissection and square rearrangement geometric proofs", topicCode: "CBSE-8-MGP2-2-2.2.1" },
          { number: "2.2.2", name: "Converse of Pythagoras theorem (testing right triangles)", topicCode: "CBSE-8-MGP2-2-2.2.2" }
        ]
      },
      {
        number: "2.3",
        name: "Pythagorean Triplets & Generating Formulas",
        topicCode: "CBSE-8-MGP2-2-2.3",
        subtopics: [
          { number: "2.3.1", name: "Identifying primitive Pythagorean triplets (3,4,5; 5,12,13)", topicCode: "CBSE-8-MGP2-2-2.3.1" },
          { number: "2.3.2", name: "Generating triplets using 2m, m²-1, m²+1 formula", topicCode: "CBSE-8-MGP2-2-2.3.2" }
        ]
      },
      {
        number: "2.4",
        name: "Applications in Geometry & Distance Calculations",
        topicCode: "CBSE-8-MGP2-2-2.4",
        subtopics: [
          { number: "2.4.1", name: "Finding unknown side lengths in geometric figures", topicCode: "CBSE-8-MGP2-2-2.4.1" },
          { number: "2.4.2", name: "Word problems on ladder, tree, walking distance", topicCode: "CBSE-8-MGP2-2-2.4.2" }
        ]
      }
    ]
  },
  {
    number: "3",
    name: "Proportional Reasoning 2",
    topics: [
      {
        number: "3.1",
        name: "Inverse Proportion & Constant Product Relation",
        topicCode: "CBSE-8-MGP2-3-3.1",
        subtopics: [
          { number: "3.1.1", name: "Concept of inverse variation (xy = k)", topicCode: "CBSE-8-MGP2-3-3.1.1" },
          { number: "3.1.2", name: "Distinguishing direct vs inverse proportion situations", topicCode: "CBSE-8-MGP2-3-3.1.2" }
        ]
      },
      {
        number: "3.2",
        name: "Speed, Time and Distance Problems",
        topicCode: "CBSE-8-MGP2-3-3.2",
        subtopics: [
          { number: "3.2.1", name: "Speed-time inversely proportional relationships", topicCode: "CBSE-8-MGP2-3-3.2.1" },
          { number: "3.2.2", name: "Travel schedules and constant distance problems", topicCode: "CBSE-8-MGP2-3-3.2.2" }
        ]
      },
      {
        number: "3.3",
        name: "Work and Time Problems",
        topicCode: "CBSE-8-MGP2-3-3.3",
        subtopics: [
          { number: "3.3.1", name: "Men, workers and days required (inverse proportion)", topicCode: "CBSE-8-MGP2-3-3.3.1" },
          { number: "3.3.2", name: "Pipes, cisterns and filling rates", topicCode: "CBSE-8-MGP2-3-3.3.2" }
        ]
      },
      {
        number: "3.4",
        name: "Pie Charts & Proportional Angular Distribution of Data",
        topicCode: "CBSE-8-MGP2-3-3.4",
        subtopics: [
          { number: "3.4.1", name: "Sector angles proportional to data values (θ = value/total * 360°)", topicCode: "CBSE-8-MGP2-3-3.4.1" },
          { number: "3.4.2", name: "Reading and interpreting pie charts", topicCode: "CBSE-8-MGP2-3-3.4.2" }
        ]
      }
    ]
  },
  {
    number: "4",
    name: "Exploring Some Geometric Themes",
    topics: [
      {
        number: "4.1",
        name: "2D Views of 3D Objects (Top, Front, Side Views)",
        topicCode: "CBSE-8-MGP2-4-4.1",
        subtopics: [
          { number: "4.1.1", name: "Identifying front, top and side views of simple objects", topicCode: "CBSE-8-MGP2-4-4.1.1" },
          { number: "4.1.2", name: "Orthographic views of combined block structures", topicCode: "CBSE-8-MGP2-4-4.1.2" }
        ]
      },
      {
        number: "4.2",
        name: "Mapping Space Around Us & Scale Factors",
        topicCode: "CBSE-8-MGP2-4-4.2",
        subtopics: [
          { number: "4.2.1", name: "Reading map landmarks and distances", topicCode: "CBSE-8-MGP2-4-4.2.1" },
          { number: "4.2.2", name: "Scale representation (ratio of map distance to actual distance)", topicCode: "CBSE-8-MGP2-4-4.2.2" }
        ]
      },
      {
        number: "4.3",
        name: "Faces, Edges, Vertices & Euler's Formula for Polyhedra",
        topicCode: "CBSE-8-MGP2-4-4.3",
        subtopics: [
          { number: "4.3.1", name: "Polyhedra definition: Prism vs pyramid", topicCode: "CBSE-8-MGP2-4-4.3.1" },
          { number: "4.3.2", name: "Regular polyhedra (Platonic solids)", topicCode: "CBSE-8-MGP2-4-4.3.2" },
          { number: "4.3.3", name: "Euler formula F + V - E = 2 verification", topicCode: "CBSE-8-MGP2-4-4.3.3" }
        ]
      },
      {
        number: "4.4",
        name: "3D Spatial Layouts & Geometric Nets",
        topicCode: "CBSE-8-MGP2-4-4.4",
        subtopics: [
          { number: "4.4.1", name: "Nets for building cubes, cuboids, cylinders, cones and prisms", topicCode: "CBSE-8-MGP2-4-4.4.1" }
        ]
      }
    ]
  },
  {
    number: "5",
    name: "Tales by Dots and Lines",
    topics: [
      {
        number: "5.1",
        name: "Organising Data, Frequency Distribution Tables & Tally Marks",
        topicCode: "CBSE-8-MGP2-5-5.1",
        subtopics: [
          { number: "5.1.1", name: "Raw data, frequency tables and tally marks", topicCode: "CBSE-8-MGP2-5-5.1.1" },
          { number: "5.1.2", name: "Grouped frequency distributions and class intervals", topicCode: "CBSE-8-MGP2-5-5.1.2" }
        ]
      },
      {
        number: "5.2",
        name: "Bar Graphs, Double Bar Graphs & Histograms",
        topicCode: "CBSE-8-MGP2-5-5.2",
        subtopics: [
          { number: "5.2.1", name: "Drawing and interpreting single bar graphs", topicCode: "CBSE-8-MGP2-5-5.2.1" },
          { number: "5.2.2", name: "Double bar graphs for comparative trends", topicCode: "CBSE-8-MGP2-5-5.2.2" },
          { number: "5.2.3", name: "Histograms for grouped continuous data with class intervals", topicCode: "CBSE-8-MGP2-5-5.2.3" }
        ]
      },
      {
        number: "5.3",
        name: "Line Graphs & Continuous Trends",
        topicCode: "CBSE-8-MGP2-5-5.3",
        subtopics: [
          { number: "5.3.1", name: "Reading unbroken continuous line graphs over time", topicCode: "CBSE-8-MGP2-5-5.3.1" },
          { number: "5.3.2", name: "Cartesian coordinates (x, y) & plotting points", topicCode: "CBSE-8-MGP2-5-5.3.2" }
        ]
      },
      {
        number: "5.4",
        name: "Measures of Central Tendency: Mean, Median & Mode",
        topicCode: "CBSE-8-MGP2-5-5.4",
        subtopics: [
          { number: "5.4.1", name: "Calculating arithmetic mean of ungrouped data", topicCode: "CBSE-8-MGP2-5-5.4.1" },
          { number: "5.4.2", name: "Finding median (middle value) of ordered data", topicCode: "CBSE-8-MGP2-5-5.4.2" },
          { number: "5.4.3", name: "Finding mode (most frequent value)", topicCode: "CBSE-8-MGP2-5-5.4.3" }
        ]
      }
    ]
  },
  {
    number: "6",
    name: "Algebra Play",
    topics: [
      {
        number: "6.1",
        name: "Solving Linear Equations with Variable on One Side",
        topicCode: "CBSE-8-MGP2-6-6.1",
        subtopics: [
          { number: "6.1.1", name: "Algebraic balance concept: Add, subtract, multiply, divide both sides", topicCode: "CBSE-8-MGP2-6-6.1.1" },
          { number: "6.1.2", name: "Transposition method for solving equations", topicCode: "CBSE-8-MGP2-6-6.1.2" }
        ]
      },
      {
        number: "6.2",
        name: "Solving Equations with Variables on Both Sides",
        topicCode: "CBSE-8-MGP2-6-6.2",
        subtopics: [
          { number: "6.2.1", name: "Grouping like variable terms on one side", topicCode: "CBSE-8-MGP2-6-6.2.1" },
          { number: "6.2.2", name: "Equations with parentheses and brackets", topicCode: "CBSE-8-MGP2-6-6.2.2" }
        ]
      },
      {
        number: "6.3",
        name: "Reducing Equations to Simpler Linear Form",
        topicCode: "CBSE-8-MGP2-6-6.3",
        subtopics: [
          { number: "6.3.1", name: "Cross multiplication method for fractional equations", topicCode: "CBSE-8-MGP2-6-6.3.1" },
          { number: "6.3.2", name: "Clearing denominators using LCM", topicCode: "CBSE-8-MGP2-6-6.3.2" }
        ]
      },
      {
        number: "6.4",
        name: "Algebraic Number Tricks, Calendar Puzzles & Word Problems",
        topicCode: "CBSE-8-MGP2-6-6.4",
        subtopics: [
          { number: "6.4.1", name: "Decoding 'think of a number' and calendar date tricks", topicCode: "CBSE-8-MGP2-6-6.4.1" },
          { number: "6.4.2", name: "Word problems on numbers, digits and consecutive integers", topicCode: "CBSE-8-MGP2-6-6.4.2" },
          { number: "6.4.3", name: "Word problems on age comparisons", topicCode: "CBSE-8-MGP2-6-6.4.3" },
          { number: "6.4.4", name: "Word problems on perimeter, geometry, coins and notes", topicCode: "CBSE-8-MGP2-6-6.4.4" }
        ]
      }
    ]
  },
  {
    number: "7",
    name: "Area",
    topics: [
      {
        number: "7.1",
        name: "Review of Area of Rectangles, Squares & Triangles",
        topicCode: "CBSE-8-MGP2-7-7.1",
        subtopics: [
          { number: "7.1.1", name: "Area and perimeter of rectangles and squares", topicCode: "CBSE-8-MGP2-7-7.1.1" },
          { number: "7.1.2", name: "Area of triangle: 1/2 * base * height", topicCode: "CBSE-8-MGP2-7-7.1.2" }
        ]
      },
      {
        number: "7.2",
        name: "Area of Parallelogram & Rhombus",
        topicCode: "CBSE-8-MGP2-7-7.2",
        subtopics: [
          { number: "7.2.1", name: "Area of parallelogram = base * height", topicCode: "CBSE-8-MGP2-7-7.2.1" },
          { number: "7.2.2", name: "Area of rhombus = 1/2 * d1 * d2 using perpendicular diagonals", topicCode: "CBSE-8-MGP2-7-7.2.2" }
        ]
      },
      {
        number: "7.3",
        name: "Area of Trapezium",
        topicCode: "CBSE-8-MGP2-7-7.3",
        subtopics: [
          { number: "7.3.1", name: "Area of trapezium = 1/2 * (sum of parallel sides) * height", topicCode: "CBSE-8-MGP2-7-7.3.1" },
          { number: "7.3.2", name: "Finding height or parallel side when area is given", topicCode: "CBSE-8-MGP2-7-7.3.2" }
        ]
      },
      {
        number: "7.4",
        name: "Area of General Polygons by Triangulation",
        topicCode: "CBSE-8-MGP2-7-7.4",
        subtopics: [
          { number: "7.4.1", name: "Dividing quadrilateral into two triangles along diagonal", topicCode: "CBSE-8-MGP2-7-7.4.1" },
          { number: "7.4.2", name: "Survey field book method (triangulation and trapezoids)", topicCode: "CBSE-8-MGP2-7-7.4.2" }
        ]
      },
      {
        number: "7.5",
        name: "Surface Area of Cube, Cuboid & Right Circular Cylinder",
        topicCode: "CBSE-8-MGP2-7-7.5",
        subtopics: [
          { number: "7.5.1", name: "Total and lateral surface area of cube (6a², 4a²)", topicCode: "CBSE-8-MGP2-7-7.5.1" },
          { number: "7.5.2", name: "Total and lateral surface area of cuboid (2(lb+bh+hl), 2h(l+b))", topicCode: "CBSE-8-MGP2-7-7.5.2" },
          { number: "7.5.3", name: "Curved and total surface area of cylinder (2πrh, 2πr(r+h))", topicCode: "CBSE-8-MGP2-7-7.5.3" }
        ]
      }
    ]
  }
];

// Mapping table for migrating existing questions & exams:
// 1. Former MGP1 Ch 5 (Understanding Quadrilaterals) -> MGP1 Ch 4 (Quadrilaterals)
// 2. Former MGP1 Ch 4 (Linear Equations in One Variable) -> MGP2 Ch 6 (Algebra Play)
// 3. Former MGP1 Ch 7 (Visualising Solid Shapes) -> MGP2 Ch 4 (Exploring Some Geometric Themes)
// 4. Former MGP1 Ch 6 stays MGP1 Ch 6, but chapter title updated to "We Distribute, Yet Things Multiply"

function getTargetMapping(oldTopicCode) {
  if (!oldTopicCode) return null;

  // 1. Former Ch 5 Quadrilaterals -> New Ch 4 Quadrilaterals
  if (oldTopicCode.startsWith('CBSE-8-MGP1-5-')) {
    const newTopicCode = oldTopicCode.replace('CBSE-8-MGP1-5-5.', 'CBSE-8-MGP1-4-4.');
    return {
      newTopicCode,
      newSubjectCode: 'MGP1',
      newChapterNumber: 4,
      newChapterName: 'Quadrilaterals'
    };
  }

  // 2. Former Ch 4 Linear Equations -> MGP2 Ch 6 Algebra Play
  if (oldTopicCode.startsWith('CBSE-8-MGP1-4-')) {
    const newTopicCode = oldTopicCode.replace('CBSE-8-MGP1-4-4.', 'CBSE-8-MGP2-6-6.');
    return {
      newTopicCode,
      newSubjectCode: 'MGP2',
      newChapterNumber: 6,
      newChapterName: 'Algebra Play'
    };
  }

  // 3. Former Ch 7 Visualising Solid Shapes -> MGP2 Ch 4 Exploring Some Geometric Themes
  if (oldTopicCode.startsWith('CBSE-8-MGP1-7-')) {
    const newTopicCode = oldTopicCode.replace('CBSE-8-MGP1-7-7.', 'CBSE-8-MGP2-4-4.');
    return {
      newTopicCode,
      newSubjectCode: 'MGP2',
      newChapterNumber: 4,
      newChapterName: 'Exploring Some Geometric Themes'
    };
  }

  return null;
}

async function runRealignment() {
  console.log('================================================================');
  console.log('🚀 COMMENCING CBSE CLASS 8 GANITA PRAKASH SYLLABUS REALIGNMENT');
  console.log('================================================================');

  // ── STEP 1: PRE-MUTATION SNAPSHOT (Rule 2.Q) ─────────────────────
  const now = new Date();
  const dateStr = now.toISOString().replace(/[:.]/g, '-');
  const backupDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(backupDir)) fs.mkdirSync(backupDir, { recursive: true });

  const backupFile = path.join(backupDir, `snapshot_${dateStr}_cbse8_syllabus_realignment.json`);
  console.log(`\n📸 Step 1: Creating Pre-Mutation Snapshot -> ${backupFile}...`);

  const [mgp1Doc, mgp2Doc, questionsSnap, examsSnap, reviewsSnap, practiceSnap, masterySnap] = await Promise.all([
    db.collection('syllabus').doc('cbse_8_mgp1').get(),
    db.collection('syllabus').doc('cbse_8_mgp2').get(),
    db.collection('questions').where('subjectCode', 'in', ['MGP1', 'MGP2']).get(),
    db.collection('exams').where('subjectCode', 'in', ['MGP1', 'MGP2']).get(),
    db.collection('reviews').where('examId', 'in', [
      '019-CBSE-8-Understanding-5.1-121026',
      '020-CBSE-8-Understanding-5.2-131026',
      '021-CBSE-8-Understanding-5.3-5.4-141026',
      '022-CBSE-8-Understanding-5.1-5.4-151026'
    ]).get(),
    db.collection('practiceSubmissions').where('topicCode', '>=', 'CBSE-8-MGP1').where('topicCode', '<=', 'CBSE-8-MGP1-\uf8ff').get(),
    db.collection('studentTopicMastery').where('topicCode', '>=', 'CBSE-8-MGP1').where('topicCode', '<=', 'CBSE-8-MGP1-\uf8ff').get()
  ]);

  const snapshotData = {
    timestamp: now.toISOString(),
    reason: 'Realign CBSE Class 8 Mathematics to Official NCERT Ganita Prakash Part 1 & Part 2 curriculum, migrating questions, exams and student attempts safely.',
    syllabus: {
      cbse_8_mgp1: mgp1Doc.data(),
      cbse_8_mgp2: mgp2Doc.data()
    },
    counts: {
      questions: questionsSnap.size,
      exams: examsSnap.size,
      reviews: reviewsSnap.size,
      practiceSubmissions: practiceSnap.size,
      studentTopicMastery: masterySnap.size
    },
    questions: questionsSnap.docs.map(d => ({ id: d.id, data: d.data() })),
    exams: examsSnap.docs.map(d => ({ id: d.id, data: d.data() })),
    reviews: reviewsSnap.docs.map(d => ({ id: d.id, data: d.data() })),
    practiceSubmissions: practiceSnap.docs.map(d => ({ id: d.id, data: d.data() })),
    studentTopicMastery: masterySnap.docs.map(d => ({ id: d.id, data: d.data() }))
  };

  fs.writeFileSync(backupFile, JSON.stringify(snapshotData, null, 2));
  console.log(`   ✅ Snapshot saved successfully (${(fs.statSync(backupFile).size / 1024 / 1024).toFixed(2)} MB).`);

  await db.collection('_systemBackups').doc(`backup_${dateStr}_cbse8_realignment`).set({
    timestamp: admin.firestore.Timestamp.fromDate(now),
    reason: snapshotData.reason,
    backupFile: path.basename(backupFile),
    counts: snapshotData.counts
  });
  console.log(`   ✅ Logged snapshot in _systemBackups.`);

  // ── STEP 2: REALIGN QUESTIONS COLLECTION ────────────────────────
  console.log(`\n🔄 Step 2: Realigning Questions in Firestore...`);
  let questionsUpdated = 0;
  let batch = db.batch();
  let opCount = 0;

  for (const doc of questionsSnap.docs) {
    const q = doc.data();
    const mapping = getTargetMapping(q.topicCode);
    if (!mapping) continue;

    // Update questionCode if it follows canonical format
    let newQuestionCode = q.questionCode;
    if (newQuestionCode && typeof newQuestionCode === 'string') {
      newQuestionCode = newQuestionCode
        .replace('CBSE-8-MGP1-5-5.', 'CBSE-8-MGP1-4-4.')
        .replace('CBSE-8-MGP1-4-4.', 'CBSE-8-MGP2-6-6.')
        .replace('CBSE-8-MGP1-7-7.', 'CBSE-8-MGP2-4-4.');
    }

    const updates = {
      topicCode: mapping.newTopicCode,
      subjectCode: mapping.newSubjectCode,
      chapterNumber: mapping.newChapterNumber,
      chapterName: mapping.newChapterName,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    };
    if (newQuestionCode) updates.questionCode = newQuestionCode;

    batch.update(doc.ref, updates);
    opCount++;
    questionsUpdated++;

    if (opCount >= 400) {
      await batch.commit();
      batch = db.batch();
      opCount = 0;
      console.log(`   Committed ${questionsUpdated} question updates...`);
    }
  }

  if (opCount > 0) {
    await batch.commit();
  }
  console.log(`   ✅ Total Questions Realigned: ${questionsUpdated} / ${questionsSnap.size}`);

  // ── STEP 3: REALIGN EXAMS COLLECTION ────────────────────────────
  console.log(`\n🔄 Step 3: Realigning Exams...`);
  let examsUpdated = 0;
  for (const doc of examsSnap.docs) {
    const ex = doc.data();
    let hasChanges = false;
    const updates = {};

    if (Array.isArray(ex.topicCodes)) {
      const newCodes = ex.topicCodes.map(tc => {
        const m = getTargetMapping(tc);
        if (m) {
          hasChanges = true;
          return m.newTopicCode;
        }
        return tc;
      });
      if (hasChanges) updates.topicCodes = newCodes;
    }

    if (Array.isArray(ex.topics)) {
      const newTopics = ex.topics.map(t => {
        const tc = typeof t === 'string' ? t : t?.topicCode;
        const m = getTargetMapping(tc);
        if (m) {
          hasChanges = true;
          if (typeof t === 'string') return m.newTopicCode;
          return { ...t, topicCode: m.newTopicCode };
        }
        return t;
      });
      if (hasChanges) updates.topics = newTopics;
    }

    if (hasChanges) {
      await doc.ref.update(updates);
      examsUpdated++;
      console.log(`   Updated Exam: ${doc.id}`);
    }
  }
  console.log(`   ✅ Exams Updated: ${examsUpdated}`);

  // ── STEP 4: REALIGN STUDENT REVIEWS & ATTEMPTS ──────────────────
  console.log(`\n🔄 Step 4: Realigning Student Exam Reviews...`);
  let reviewsUpdated = 0;
  let rBatch = db.batch();
  let rOpCount = 0;

  for (const doc of reviewsSnap.docs) {
    const rev = doc.data();
    let needsUpdate = false;
    const updates = {};

    // Check questions array in review
    if (Array.isArray(rev.questions)) {
      const updatedQuestions = rev.questions.map(q => {
        const m = getTargetMapping(q.topicCode);
        if (m) {
          needsUpdate = true;
          return { ...q, topicCode: m.newTopicCode };
        }
        return q;
      });
      if (needsUpdate) updates.questions = updatedQuestions;
    }

    // Check questionDetails array
    if (Array.isArray(rev.questionDetails)) {
      const updatedDetails = rev.questionDetails.map(q => {
        const m = getTargetMapping(q.topicCode);
        if (m) {
          needsUpdate = true;
          return { ...q, topicCode: m.newTopicCode };
        }
        return q;
      });
      if (needsUpdate) updates.questionDetails = updatedDetails;
    }

    if (needsUpdate) {
      rBatch.update(doc.ref, updates);
      rOpCount++;
      reviewsUpdated++;
      if (rOpCount >= 400) {
        await rBatch.commit();
        rBatch = db.batch();
        rOpCount = 0;
      }
    }
  }
  if (rOpCount > 0) await rBatch.commit();
  console.log(`   ✅ Reviews Updated: ${reviewsUpdated}`);

  // ── STEP 5: REALIGN PRACTICE SUBMISSIONS ─────────────────────────
  console.log(`\n🔄 Step 5: Realigning Practice Submissions...`);
  let pracUpdated = 0;
  let pBatch = db.batch();
  let pOpCount = 0;

  for (const doc of practiceSnap.docs) {
    const p = doc.data();
    const m = getTargetMapping(p.topicCode);
    if (m) {
      pBatch.update(doc.ref, {
        topicCode: m.newTopicCode,
        chapterNumber: m.newChapterNumber,
        subjectCode: m.newSubjectCode
      });
      pOpCount++;
      pracUpdated++;
      if (pOpCount >= 400) {
        await pBatch.commit();
        pBatch = db.batch();
        pOpCount = 0;
      }
    }
  }
  if (pOpCount > 0) await pBatch.commit();
  console.log(`   ✅ Practice Submissions Updated: ${pracUpdated}`);

  // ── STEP 6: REALIGN STUDENT TOPIC MASTERY ───────────────────────
  console.log(`\n🔄 Step 6: Realigning Student Topic Mastery...`);
  let masteryUpdated = 0;
  let mBatch = db.batch();
  let mOpCount = 0;

  for (const doc of masterySnap.docs) {
    const mas = doc.data();
    const m = getTargetMapping(mas.topicCode);
    if (m) {
      // Create new doc with target topicCode key and delete old
      const oldId = doc.id;
      const newId = oldId.replace(mas.topicCode, m.newTopicCode);

      mBatch.set(db.collection('studentTopicMastery').doc(newId), {
        ...mas,
        topicCode: m.newTopicCode,
        topicName: m.newChapterName,
        subjectCode: m.newSubjectCode,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      mBatch.delete(doc.ref);

      mOpCount += 2;
      masteryUpdated++;

      if (mOpCount >= 400) {
        await mBatch.commit();
        mBatch = db.batch();
        mOpCount = 0;
      }
    }
  }
  if (mOpCount > 0) await mBatch.commit();
  console.log(`   ✅ Student Topic Mastery Records Migrated: ${masteryUpdated}`);

  // ── STEP 7: UPDATE SYLLABUS COLLECTION IN FIRESTORE ─────────────
  console.log(`\n🔄 Step 7: Updating Official Syllabus Documents in Firestore...`);

  // Compute question counts dynamically for MGP1
  const updatedMgp1QuestionsSnap = await db.collection('questions')
    .where('subjectCode', '==', 'MGP1')
    .select('topicCode', 'type')
    .get();

  const mgp1CountsByTopic = {};
  updatedMgp1QuestionsSnap.docs.forEach(d => {
    const q = d.data();
    const tc = q.topicCode;
    mgp1CountsByTopic[tc] = (mgp1CountsByTopic[tc] || 0) + 1;
    // Also track parent topic if subtopic
    const parts = tc.split('-');
    if (parts.length >= 5) {
      const subParts = parts[4].split('.');
      if (subParts.length >= 3) {
        const parentCode = `${parts[0]}-${parts[1]}-${parts[2]}-${parts[3]}-${subParts[0]}.${subParts[1]}`;
        mgp1CountsByTopic[parentCode] = (mgp1CountsByTopic[parentCode] || 0) + 1;
      }
    }
  });

  // Calculate MGP1 chapters with counts
  let totalMgp1Obj = 0;
  const enrichedMgp1Chapters = MGP1_CHAPTERS.map(ch => {
    let chObj = 0;
    const enrichedTopics = ch.topics.map(t => {
      let tObj = 0;
      const enrichedSubtopics = (t.subtopics || []).map(st => {
        const count = mgp1CountsByTopic[st.topicCode] || 0;
        tObj += count;
        return {
          ...st,
          objectiveCount: count,
          subjectiveCount: 0
        };
      });

      // If no subtopic counts but direct topic count
      if (tObj === 0) tObj = mgp1CountsByTopic[t.topicCode] || 0;
      chObj += tObj;

      return {
        ...t,
        subtopics: enrichedSubtopics,
        objectiveCount: tObj,
        subjectiveCount: 0,
        practiceSet: `Exercise ${t.number}`,
        problemSet: `Problem Set ${ch.number}`,
        theorems: []
      };
    });

    totalMgp1Obj += chObj;
    return {
      ...ch,
      topics: enrichedTopics,
      objectiveCount: chObj,
      subjectiveCount: 0
    };
  });

  await db.collection('syllabus').doc('cbse_8_mgp1').set({
    board: 'CBSE',
    boardCode: 'CBSE',
    class: '8',
    subject: 'Ganit Prakash Part 1',
    subjectCode: 'MGP1',
    chapters: enrichedMgp1Chapters,
    objectiveCount: totalMgp1Obj,
    subjectiveCount: 0,
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  }, { merge: true });
  console.log(`   ✅ Saved cbse_8_mgp1 (${enrichedMgp1Chapters.length} chapters, ${totalMgp1Obj} questions)`);

  // Compute question counts dynamically for MGP2
  const updatedMgp2QuestionsSnap = await db.collection('questions')
    .where('subjectCode', '==', 'MGP2')
    .select('topicCode', 'type')
    .get();

  const mgp2CountsByTopic = {};
  updatedMgp2QuestionsSnap.docs.forEach(d => {
    const q = d.data();
    const tc = q.topicCode;
    mgp2CountsByTopic[tc] = (mgp2CountsByTopic[tc] || 0) + 1;
    const parts = tc.split('-');
    if (parts.length >= 5) {
      const subParts = parts[4].split('.');
      if (subParts.length >= 3) {
        const parentCode = `${parts[0]}-${parts[1]}-${parts[2]}-${parts[3]}-${subParts[0]}.${subParts[1]}`;
        mgp2CountsByTopic[parentCode] = (mgp2CountsByTopic[parentCode] || 0) + 1;
      }
    }
  });

  let totalMgp2Obj = 0;
  const enrichedMgp2Chapters = MGP2_CHAPTERS.map(ch => {
    let chObj = 0;
    const enrichedTopics = ch.topics.map(t => {
      let tObj = 0;
      const enrichedSubtopics = (t.subtopics || []).map(st => {
        const count = mgp2CountsByTopic[st.topicCode] || 0;
        tObj += count;
        return {
          ...st,
          objectiveCount: count,
          subjectiveCount: 0
        };
      });

      if (tObj === 0) tObj = mgp2CountsByTopic[t.topicCode] || 0;
      chObj += tObj;

      return {
        ...t,
        subtopics: enrichedSubtopics,
        objectiveCount: tObj,
        subjectiveCount: 0,
        practiceSet: `Exercise ${t.number}`,
        problemSet: `Problem Set ${ch.number}`,
        theorems: []
      };
    });

    totalMgp2Obj += chObj;
    return {
      ...ch,
      topics: enrichedTopics,
      objectiveCount: chObj,
      subjectiveCount: 0
    };
  });

  await db.collection('syllabus').doc('cbse_8_mgp2').set({
    board: 'CBSE',
    boardCode: 'CBSE',
    class: '8',
    subject: 'Ganit Prakash Part 2',
    subjectCode: 'MGP2',
    chapters: enrichedMgp2Chapters,
    objectiveCount: totalMgp2Obj,
    subjectiveCount: 0,
    updatedAt: admin.firestore.FieldValue.serverTimestamp()
  }, { merge: true });
  console.log(`   ✅ Saved cbse_8_mgp2 (${enrichedMgp2Chapters.length} chapters, ${totalMgp2Obj} questions)`);

  // ── STEP 8: REBUILD SYLLABUS TOPIC INDEX ────────────────────────
  console.log(`\n🔄 Step 8: Rebuilding syllabusTopicIndex for MGP1 & MGP2...`);

  // Delete old MGP1 & MGP2 index entries
  const [oldM1Index, oldM2Index] = await Promise.all([
    db.collection('syllabusTopicIndex').where('subjectCode', '==', 'MGP1').get(),
    db.collection('syllabusTopicIndex').where('subjectCode', '==', 'MGP2').get()
  ]);

  let delBatch = db.batch();
  let delCount = 0;
  for (const doc of [...oldM1Index.docs, ...oldM2Index.docs]) {
    delBatch.delete(doc.ref);
    delCount++;
    if (delCount >= 400) {
      await delBatch.commit();
      delBatch = db.batch();
      delCount = 0;
    }
  }
  if (delCount > 0) await delBatch.commit();
  console.log(`   Deleted ${oldM1Index.size + oldM2Index.size} old topic index entries.`);

  // Write fresh entries for MGP1 and MGP2
  let addBatch = db.batch();
  let addCount = 0;
  let totalIndexed = 0;

  async function indexSyllabus(docData) {
    for (const ch of (docData.chapters || [])) {
      for (const t of (ch.topics || [])) {
        // Index topic
        const tRef = db.collection('syllabusTopicIndex').doc(t.topicCode);
        addBatch.set(tRef, {
          topicCode: t.topicCode,
          topicNumber: t.number,
          topicName: t.name,
          chapterNumber: ch.number,
          chapterName: ch.name,
          subject: docData.subject,
          subjectCode: docData.subjectCode,
          class: docData.class,
          board: docData.board,
          boardCode: docData.boardCode,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        });
        addCount++;
        totalIndexed++;

        // Index subtopics
        for (const st of (t.subtopics || [])) {
          const stRef = db.collection('syllabusTopicIndex').doc(st.topicCode);
          addBatch.set(stRef, {
            topicCode: st.topicCode,
            topicNumber: st.number,
            topicName: st.name,
            parentTopicCode: t.topicCode,
            chapterNumber: ch.number,
            chapterName: ch.name,
            subject: docData.subject,
            subjectCode: docData.subjectCode,
            class: docData.class,
            board: docData.board,
            boardCode: docData.boardCode,
            updatedAt: admin.firestore.FieldValue.serverTimestamp()
          });
          addCount++;
          totalIndexed++;

          if (addCount >= 400) {
            await addBatch.commit();
            addBatch = db.batch();
            addCount = 0;
          }
        }

        if (addCount >= 400) {
          await addBatch.commit();
          addBatch = db.batch();
          addCount = 0;
        }
      }
    }
  }

  await indexSyllabus({
    chapters: enrichedMgp1Chapters,
    subject: 'Ganit Prakash Part 1',
    subjectCode: 'MGP1',
    class: '8',
    board: 'CBSE',
    boardCode: 'CBSE'
  });

  await indexSyllabus({
    chapters: enrichedMgp2Chapters,
    subject: 'Ganit Prakash Part 2',
    subjectCode: 'MGP2',
    class: '8',
    board: 'CBSE',
    boardCode: 'CBSE'
  });

  if (addCount > 0) {
    await addBatch.commit();
  }
  console.log(`   ✅ Indexed ${totalIndexed} topics and subtopics in syllabusTopicIndex.`);

  console.log('\n================================================================');
  console.log('🎉 REALIGNMENT COMPLETED SUCCESSFULLY WITH ZERO ERRORS');
  console.log('================================================================');
}

runRealignment().then(() => process.exit(0)).catch(err => {
  console.error('❌ Realignment failed:', err);
  process.exit(1);
});
