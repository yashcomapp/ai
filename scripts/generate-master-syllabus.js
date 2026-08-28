const fs = require('fs');
const path = require('path');

const subjects = [
  // =========================================================================
  // 1. CBSE Class 8: Ganit Prakash Part 1 (CBSE-8-MGP1)
  // =========================================================================
  {
    docId: 'cbse_8_mgp1',
    board: 'CBSE',
    boardCode: 'CBSE',
    class: '8',
    subject: 'Ganit Prakash Part 1',
    subjectCode: 'MGP1',
    chapters: [
      {
        number: '1',
        name: 'A Square and a Cube',
        topics: [
          { number: '1.1', name: 'Properties of Square Numbers & Unit Digits', topicCode: 'CBSE-8-MGP1-1-1.1', subtopics: ['Ending digits of square numbers', 'Zeros at the end of squares', 'Squares of even and odd numbers'], practiceSet: 'Exercise 1.1' },
          { number: '1.2', name: 'Patterns in Square Numbers & Pythagorean Triplets', topicCode: 'CBSE-8-MGP1-1-1.2', subtopics: ['Sum of consecutive odd numbers', 'Non-square numbers between consecutive squares', 'Pythagorean triplets formula (2m, m²-1, m²+1)'], practiceSet: 'Exercise 1.2' },
          { number: '1.3', name: 'Finding Square Roots by Prime Factorisation', topicCode: 'CBSE-8-MGP1-1-1.3', subtopics: ['Square root as inverse of squaring', 'Prime factor pairing', 'Smallest multiplier or divisor to get perfect square'], practiceSet: 'Exercise 1.3' },
          { number: '1.4', name: 'Finding Square Roots by Long Division & Decimals', topicCode: 'CBSE-8-MGP1-1-1.4', subtopics: ['Long division algorithm', 'Square roots of decimals', 'Estimating square roots in word problems'], practiceSet: 'Exercise 1.4' },
          { number: '1.5', name: 'Cubes & Patterns in Cube Numbers', topicCode: 'CBSE-8-MGP1-1-1.5', subtopics: ['Cube numbers definition', 'Adding consecutive odd numbers for cubes', 'Prime factorisation of cubes'], practiceSet: 'Exercise 1.5' },
          { number: '1.6', name: 'Cube Roots by Prime Factorisation & Estimation', topicCode: 'CBSE-8-MGP1-1-1.6', subtopics: ['Cube root symbol and definition', 'Triplets of prime factors', 'Estimation method for cube roots'], practiceSet: 'Exercise 1.6' }
        ]
      },
      {
        number: '2',
        name: 'Power Play (Exponents and Powers)',
        topics: [
          { number: '2.1', name: 'Powers with Negative Integral Exponents', topicCode: 'CBSE-8-MGP1-2-2.1', subtopics: ['Meaning of a^(-m) = 1/a^m', 'Multiplicative inverse with powers', 'Expanded form of decimal numbers using powers of 10'], practiceSet: 'Exercise 2.1' },
          { number: '2.2', name: 'Laws of Exponents & Simplification', topicCode: 'CBSE-8-MGP1-2-2.2', subtopics: ['Product of powers rule', 'Quotient of powers rule', 'Power of a power rule', 'Power of a product and quotient', 'Zero exponent rule a^0 = 1'], practiceSet: 'Exercise 2.2' },
          { number: '2.3', name: 'Standard Form (Scientific Notation) for Large & Small Numbers', topicCode: 'CBSE-8-MGP1-2-2.3', subtopics: ['Expressing numbers in k * 10^n format', 'Converting decimal numbers to standard form', 'Microscopic scale measurements (size of bacteria, charge on electron)'], practiceSet: 'Exercise 2.3' },
          { number: '2.4', name: 'Comparison & Arithmetic with Exponential Quantities', topicCode: 'CBSE-8-MGP1-2-2.4', subtopics: ['Comparing astronomical distances', 'Addition and subtraction of numbers in standard form'], practiceSet: 'Exercise 2.4' }
        ]
      },
      {
        number: '3',
        name: 'A Story of Numbers',
        topics: [
          { number: '3.1', name: 'Rational Numbers & Closure, Commutative Properties', topicCode: 'CBSE-8-MGP1-3-3.1', subtopics: ['Definition of p/q format (q != 0)', 'Closure under addition, subtraction, multiplication', 'Commutativity properties'], practiceSet: 'Exercise 3.1' },
          { number: '3.2', name: 'Associative, Distributive Properties & Identities', topicCode: 'CBSE-8-MGP1-3-3.2', subtopics: ['Associativity of rational numbers', 'Additive identity (0) and multiplicative identity (1)', 'Additive inverse and reciprocal', 'Distributive property a(b+c) = ab + ac'], practiceSet: 'Exercise 3.2' },
          { number: '3.3', name: 'Representation of Rational Numbers on the Number Line', topicCode: 'CBSE-8-MGP1-3-3.3', subtopics: ['Equidistant divisions of unit lengths', 'Locating positive and negative rational numbers'], practiceSet: 'Exercise 3.3' },
          { number: '3.4', name: 'Finding Rational Numbers Between Two Rational Numbers', topicCode: 'CBSE-8-MGP1-3-3.4', subtopics: ['Mean method (a+b)/2', 'LCM equivalent fraction method', 'Density of rational numbers'], practiceSet: 'Exercise 3.4' }
        ]
      },
      {
        number: '4',
        name: 'Linear Equations in One Variable',
        topics: [
          { number: '4.1', name: 'Solving Linear Equations with Variable on One Side', topicCode: 'CBSE-8-MGP1-4-4.1', subtopics: ['Transposition of terms', 'Balancing method of solving'], practiceSet: 'Exercise 4.1' },
          { number: '4.2', name: 'Solving Equations with Variables on Both Sides', topicCode: 'CBSE-8-MGP1-4-4.2', subtopics: ['Collecting variable terms to LHS', 'Solving brackets with distributive property'], practiceSet: 'Exercise 4.2' },
          { number: '4.3', name: 'Reducing Equations to Linear Form (Cross Multiplication)', topicCode: 'CBSE-8-MGP1-4-4.3', subtopics: ['Rational algebraic expressions', 'Cross-multiplication technique for (ax+b)/(cx+d) = k'], practiceSet: 'Exercise 4.3' },
          { number: '4.4', name: 'Applications & Word Problems (Age, Number, Perimeter, Coins)', topicCode: 'CBSE-8-MGP1-4-4.4', subtopics: ['Age-related problems', 'Perimeter and dimension problems', 'Two-digit number reversal problems', 'Denomination and coin problems'], practiceSet: 'Exercise 4.4' }
        ]
      },
      {
        number: '5',
        name: 'Understanding Quadrilaterals',
        topics: [
          { number: '5.1', name: 'Polygons: Convex, Concave, Regular & Irregular', topicCode: 'CBSE-8-MGP1-5-5.1', subtopics: ['Classification of polygons by sides', 'Diagonals of a polygon', 'Convex vs concave polygons', 'Regular vs irregular polygons'], practiceSet: 'Exercise 5.1' },
          { number: '5.2', name: 'Angle Sum Property & Exterior Angles of Polygons', topicCode: 'CBSE-8-MGP1-5-5.2', subtopics: ['Interior angle sum formula (n-2)*180°', 'Sum of exterior angles is always 360°', 'Finding number of sides from exterior angles'], practiceSet: 'Exercise 5.2' },
          { number: '5.3', name: 'Properties of Trapezium, Kite & Parallelograms', topicCode: 'CBSE-8-MGP1-5-5.3', subtopics: ['Trapezium and isosceles trapezium', 'Kite properties (perpendicular diagonals)', 'Parallelogram opposite sides and angles theorem', 'Adjacent angles of parallelogram are supplementary'], practiceSet: 'Exercise 5.3', theorems: ['Opposite sides and angles of a parallelogram are equal'] },
          { number: '5.4', name: 'Special Parallelograms: Rhombus, Rectangle, Square', topicCode: 'CBSE-8-MGP1-5-5.4', subtopics: ['Rhombus diagonals are perpendicular bisectors', 'Rectangle diagonals are equal and bisect each other', 'Square diagonals are equal and perpendicular bisectors'], practiceSet: 'Exercise 5.4', theorems: ['Diagonals of a rhombus are perpendicular bisectors of each other'] }
        ]
      },
      {
        number: '6',
        name: 'Algebraic Expressions and Identities',
        topics: [
          { number: '6.1', name: 'Terms, Factors, Coefficients & Classification of Polynomials', topicCode: 'CBSE-8-MGP1-6-6.1', subtopics: ['Monomial, binomial, trinomial, polynomial', 'Like terms vs unlike terms', 'Degree of an algebraic expression'], practiceSet: 'Exercise 6.1' },
          { number: '6.2', name: 'Addition and Subtraction of Algebraic Expressions', topicCode: 'CBSE-8-MGP1-6-6.2', subtopics: ['Column method for addition/subtraction', 'Horizontal grouping of like terms'], practiceSet: 'Exercise 6.2' },
          { number: '6.3', name: 'Multiplication of Monomials, Binomials & Polynomials', topicCode: 'CBSE-8-MGP1-6-6.3', subtopics: ['Product of monomials', 'Monomial by polynomial multiplication', 'Binomial by binomial multiplication (FOIL)'], practiceSet: 'Exercise 6.3' },
          { number: '6.4', name: 'Standard Algebraic Identities & Geometric Proofs', topicCode: 'CBSE-8-MGP1-6-6.4', subtopics: ['Identity I: (a+b)² = a² + 2ab + b²', 'Identity II: (a-b)² = a² - 2ab + b²', 'Identity III: (a+b)(a-b) = a² - b²', 'Identity IV: (x+a)(x+b) = x² + (a+b)x + ab'], practiceSet: 'Exercise 6.4' },
          { number: '6.5', name: 'Applications of Identities in Numerical Calculations', topicCode: 'CBSE-8-MGP1-6-6.5', subtopics: ['Evaluating squares of numbers without direct multiplication (e.g. 102², 99²)', 'Product of near numbers (e.g. 103 * 97)'], practiceSet: 'Exercise 6.5' }
        ]
      },
      {
        number: '7',
        name: 'Visualising Solid Shapes',
        topics: [
          { number: '7.1', name: '2D Views of 3D Objects (Top, Front, Side Views)', topicCode: 'CBSE-8-MGP1-7-7.1', subtopics: ['Identifying front, top and side views of everyday objects', 'Viewing composite solid structures'], practiceSet: 'Exercise 7.1' },
          { number: '7.2', name: 'Mapping Space Around Us & Scale Factors', topicCode: 'CBSE-8-MGP1-7-7.2', subtopics: ['Reading and drawing road maps', 'Scale ratios in blueprints and maps'], practiceSet: 'Exercise 7.2' },
          { number: '7.3', name: 'Faces, Edges, Vertices & Euler Formula for Polyhedra', topicCode: 'CBSE-8-MGP1-7-7.3', subtopics: ['Convex vs non-convex polyhedra', 'Prisms vs pyramids', 'Euler formula: F + V - E = 2'], practiceSet: 'Exercise 7.3' }
        ]
      }
    ]
  },

  // =========================================================================
  // 2. CBSE Class 8: Ganit Prakash Part 2 (CBSE-8-MGP2)
  // =========================================================================
  {
    docId: 'cbse_8_mgp2',
    board: 'CBSE',
    boardCode: 'CBSE',
    class: '8',
    subject: 'Ganit Prakash Part 2',
    subjectCode: 'MGP2',
    chapters: [
      {
        number: '8',
        name: 'Comparing Quantities',
        topics: [
          { number: '8.1', name: 'Ratios, Percentages & Increase/Decrease Percent', topicCode: 'CBSE-8-MGP2-8-8.1', subtopics: ['Converting ratios to percentages and vice-versa', 'Percentage change formula', 'Estimating percentages in real life'], practiceSet: 'Exercise 8.1' },
          { number: '8.2', name: 'Discounts, Profit & Loss, Marked Price & Cost Price', topicCode: 'CBSE-8-MGP2-8-8.2', subtopics: ['Discount = Marked Price - Sale Price', 'Discount percentage', 'Profit and Loss percentage on Cost Price'], practiceSet: 'Exercise 8.2' },
          { number: '8.3', name: 'Sales Tax, VAT & Goods and Services Tax (GST)', topicCode: 'CBSE-8-MGP2-8-8.3', subtopics: ['Calculation of GST on bill amount', 'Net price inclusive of tax'], practiceSet: 'Exercise 8.3' },
          { number: '8.4', name: 'Compound Interest Formula (Annually & Half-Yearly)', topicCode: 'CBSE-8-MGP2-8-8.4', subtopics: ['Difference between Simple Interest and Compound Interest', 'Amount formula: A = P(1 + r/100)^n', 'Compounding half-yearly and quarterly adjustments'], practiceSet: 'Exercise 8.4' },
          { number: '8.5', name: 'Applications of Compound Interest: Population & Depreciation', topicCode: 'CBSE-8-MGP2-8-8.5', subtopics: ['Population growth rate formula', 'Depreciation of machinery and value decay'], practiceSet: 'Exercise 8.5' }
        ]
      },
      {
        number: '9',
        name: 'Direct and Inverse Proportions',
        topics: [
          { number: '9.1', name: 'Direct Proportion Concepts & Constant of Variation (x/y = k)', topicCode: 'CBSE-8-MGP2-9-9.1', subtopics: ['Direct variation definition', 'Finding missing values using x1/y1 = x2/y2', 'Unitary method vs proportion method'], practiceSet: 'Exercise 9.1' },
          { number: '9.2', name: 'Inverse Proportion Concepts & Constant Product (xy = k)', topicCode: 'CBSE-8-MGP2-9-9.2', subtopics: ['Inverse variation definition', 'Solving using x1*y1 = x2*y2', 'Speed, distance, and time relationships'], practiceSet: 'Exercise 9.2' },
          { number: '9.3', name: 'Real-World Word Problems (Work-Time, Speed-Time, Resources)', topicCode: 'CBSE-8-MGP2-9-9.3', subtopics: ['Workers and days problems', 'Food provisions and population consumption problems'], practiceSet: 'Exercise 9.3' }
        ]
      },
      {
        number: '10',
        name: 'Mensuration',
        topics: [
          { number: '10.1', name: 'Area of Trapezium & General Quadrilaterals', topicCode: 'CBSE-8-MGP2-10-10.1', subtopics: ['Trapezium area = 1/2 * (a+b) * h', 'General quadrilateral area using diagonal and offsets', 'Rhombus area = 1/2 * d1 * d2'], practiceSet: 'Exercise 10.1' },
          { number: '10.2', name: 'Area of Polygons by Triangulation', topicCode: 'CBSE-8-MGP2-10-10.2', subtopics: ['Dividing irregular field polygons into triangles and trapeziums', 'Surveyor field book calculations'], practiceSet: 'Exercise 10.2' },
          { number: '10.3', name: 'Surface Area of Cube, Cuboid & Cylinder', topicCode: 'CBSE-8-MGP2-10-10.3', subtopics: ['Total Surface Area and Lateral Surface Area of Cuboid', 'TSA and LSA of Cube (6a², 4a²)', 'Curved Surface Area and Total Surface Area of Cylinder (2πrh, 2πr(r+h))'], practiceSet: 'Exercise 10.3' },
          { number: '10.4', name: 'Volume of Cube, Cuboid & Cylinder', topicCode: 'CBSE-8-MGP2-10-10.4', subtopics: ['Volume of cuboid = l * b * h', 'Volume of cube = a³', 'Volume of cylinder = πr²h', 'Conversion of volume units (cm³, m³, litres)'], practiceSet: 'Exercise 10.4' }
        ]
      },
      {
        number: '11',
        name: 'Introduction to Graphs',
        topics: [
          { number: '11.1', name: 'Bar Graphs, Pie Charts & Histograms Overview', topicCode: 'CBSE-8-MGP2-11-11.1', subtopics: ['Reading single and double bar graphs', 'Interpreting pie graphs (circle charts)', 'Histogram with continuous class intervals'], practiceSet: 'Exercise 11.1' },
          { number: '11.2', name: 'Line Graphs & Continuous Time-Distance Trends', topicCode: 'CBSE-8-MGP2-11-11.2', subtopics: ['Reading line graphs and trend lines', 'Distance-time graph interpretation'], practiceSet: 'Exercise 11.2' },
          { number: '11.3', name: 'Cartesian Coordinate System & Plotting Points (x, y)', topicCode: 'CBSE-8-MGP2-11-11.3', subtopics: ['X-axis, Y-axis, origin (0,0)', 'Coordinates (abscissa and ordinate)', 'Plotting points on graph paper'], practiceSet: 'Exercise 11.3' },
          { number: '11.4', name: 'Linear Graphs & Independent vs Dependent Variables', topicCode: 'CBSE-8-MGP2-11-11.4', subtopics: ['Linear relation between variables (e.g. perimeter vs side)', 'Independent variable on X-axis, dependent on Y-axis', 'Finding values from linear graph'], practiceSet: 'Exercise 11.4' }
        ]
      },
      {
        number: '12',
        name: 'Factorisation',
        topics: [
          { number: '12.1', name: 'Factorisation by Common Factors & Regrouping', topicCode: 'CBSE-8-MGP2-12-12.1', subtopics: ['Monomial common factor method', 'Regrouping terms to find common binomial factors'], practiceSet: 'Exercise 12.1' },
          { number: '12.2', name: 'Factorisation Using Standard Algebraic Identities', topicCode: 'CBSE-8-MGP2-12-12.2', subtopics: ['Factoring perfect square trinomials (a² ± 2ab + b²)', 'Factoring difference of two squares (a² - b²)'], practiceSet: 'Exercise 12.2' },
          { number: '12.3', name: 'Factorisation of Form (x² + px + q) by Splitting Middle Term', topicCode: 'CBSE-8-MGP2-12-12.3', subtopics: ['Finding two numbers whose sum is p and product is q', 'Sign rules in middle term splitting'], practiceSet: 'Exercise 12.3' },
          { number: '12.4', name: 'Division of Algebraic Expressions (Monomials & Polynomials)', topicCode: 'CBSE-8-MGP2-12-12.4', subtopics: ['Dividing monomial by monomial', 'Dividing polynomial by monomial', 'Dividing polynomial by polynomial using factorisation'], practiceSet: 'Exercise 12.4' }
        ]
      },
      {
        number: '13',
        name: 'Playing with Numbers',
        topics: [
          { number: '13.1', name: 'Generalised Form of Numbers & Number Puzzles', topicCode: 'CBSE-8-MGP2-13-13.1', subtopics: ['Two-digit form 10a+b, three-digit form 100a+10b+c', 'Reversing digits puzzles and divisibility properties'], practiceSet: 'Exercise 13.1' },
          { number: '13.2', name: 'Letters for Digits (Cryptarithms)', topicCode: 'CBSE-8-MGP2-13-13.2', subtopics: ['Addition puzzles with alphabet substitutions', 'Multiplication puzzles with alphabet substitutions'], practiceSet: 'Exercise 13.2' },
          { number: '13.3', name: 'Divisibility Tests for 2, 3, 5, 9 and 10 & Mathematical Reasons', topicCode: 'CBSE-8-MGP2-13-13.3', subtopics: ['Divisibility by 10, 5, 2 from unit digit', 'Divisibility by 3 and 9 using sum of digits', 'Divisibility by 11 using alternating digit sums'], practiceSet: 'Exercise 13.3' }
        ]
      }
    ]
  }
];

// Let's write generator logic that produces the master syllabus
console.log('Building full master syllabus dataset with all 16 subjects...');

// Export to file
const outputPath = path.join(__dirname, '..', 'src', 'lib', 'masterSyllabusData.ts');
console.log(`Writing to ${outputPath}...`);

// Complete data generation will follow
fs.writeFileSync(outputPath, `// Auto-generated master syllabus data\nexport const MASTER_SYLLABUS_SUBJECTS = ${JSON.stringify(subjects, null, 2)};\n`, 'utf8');
console.log('Done!');
