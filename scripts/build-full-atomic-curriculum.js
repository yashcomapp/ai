const fs = require('fs');
const path = require('path');

// Helper to create atomic topic
function createTopic(boardCode, classNum, subjectCode, chNum, topNum, name, subtopics = [], practiceSet = '', theorems = [], problemSet = '') {
  const numStr = `${chNum}.${topNum}`;
  const topicCode = `${boardCode}-${classNum}-${subjectCode}-${chNum}-${numStr}`;
  return {
    number: numStr,
    name,
    topicCode,
    subtopics,
    practiceSet: practiceSet || `Exercise ${numStr}`,
    theorems,
    problemSet: problemSet || `Problem Set ${chNum}`
  };
}

const subjects = [];

// =========================================================================
// 1. CBSE Class 8: Ganit Prakash Part 1 (CBSE-8-MGP1)
// =========================================================================
subjects.push({
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
        createTopic('CBSE', '8', 'MGP1', '1', '1', 'Properties of Square Numbers & Unit Digits', ['Ending digits of square numbers', 'Zeros at the end of squares', 'Squares of even and odd numbers']),
        createTopic('CBSE', '8', 'MGP1', '1', '2', 'Patterns in Square Numbers & Pythagorean Triplets', ['Sum of consecutive odd numbers', 'Non-square numbers between consecutive squares', 'Pythagorean triplets formula (2m, m²-1, m²+1)']),
        createTopic('CBSE', '8', 'MGP1', '1', '3', 'Finding Square Roots by Prime Factorisation', ['Square root as inverse of squaring', 'Prime factor pairing', 'Smallest multiplier or divisor to get perfect square']),
        createTopic('CBSE', '8', 'MGP1', '1', '4', 'Finding Square Roots by Long Division & Decimals', ['Long division algorithm', 'Square roots of decimals', 'Estimating square roots in word problems']),
        createTopic('CBSE', '8', 'MGP1', '1', '5', 'Cubes & Patterns in Cube Numbers', ['Cube numbers definition', 'Adding consecutive odd numbers for cubes', 'Prime factorisation of cubes']),
        createTopic('CBSE', '8', 'MGP1', '1', '6', 'Cube Roots by Prime Factorisation & Estimation', ['Cube root symbol and definition', 'Triplets of prime factors', 'Estimation method for cube roots'])
      ]
    },
    {
      number: '2',
      name: 'Power Play (Exponents and Powers)',
      topics: [
        createTopic('CBSE', '8', 'MGP1', '2', '1', 'Powers with Negative Integral Exponents', ['Meaning of a^(-m) = 1/a^m', 'Multiplicative inverse with powers', 'Expanded form of decimal numbers using powers of 10']),
        createTopic('CBSE', '8', 'MGP1', '2', '2', 'Laws of Exponents & Simplification', ['Product of powers rule', 'Quotient of powers rule', 'Power of a power rule', 'Power of a product and quotient', 'Zero exponent rule a^0 = 1']),
        createTopic('CBSE', '8', 'MGP1', '2', '3', 'Standard Form (Scientific Notation) for Large & Small Numbers', ['Expressing numbers in k * 10^n format', 'Converting decimal numbers to standard form', 'Microscopic scale measurements (size of bacteria, charge on electron)']),
        createTopic('CBSE', '8', 'MGP1', '2', '4', 'Comparison & Arithmetic with Exponential Quantities', ['Comparing astronomical distances', 'Addition and subtraction of numbers in standard form'])
      ]
    },
    {
      number: '3',
      name: 'A Story of Numbers',
      topics: [
        createTopic('CBSE', '8', 'MGP1', '3', '1', 'Rational Numbers & Closure, Commutative Properties', ['Definition of p/q format (q != 0)', 'Closure under addition, subtraction, multiplication', 'Commutativity properties']),
        createTopic('CBSE', '8', 'MGP1', '3', '2', 'Associative, Distributive Properties & Identities', ['Associativity of rational numbers', 'Additive identity (0) and multiplicative identity (1)', 'Additive inverse and reciprocal', 'Distributive property a(b+c) = ab + ac']),
        createTopic('CBSE', '8', 'MGP1', '3', '3', 'Representation of Rational Numbers on the Number Line', ['Equidistant divisions of unit lengths', 'Locating positive and negative rational numbers']),
        createTopic('CBSE', '8', 'MGP1', '3', '4', 'Finding Rational Numbers Between Two Rational Numbers', ['Mean method (a+b)/2', 'LCM equivalent fraction method', 'Density of rational numbers'])
      ]
    },
    {
      number: '4',
      name: 'Linear Equations in One Variable',
      topics: [
        createTopic('CBSE', '8', 'MGP1', '4', '1', 'Solving Linear Equations with Variable on One Side', ['Transposition of terms', 'Balancing method of solving']),
        createTopic('CBSE', '8', 'MGP1', '4', '2', 'Solving Equations with Variables on Both Sides', ['Collecting variable terms to LHS', 'Solving brackets with distributive property']),
        createTopic('CBSE', '8', 'MGP1', '4', '3', 'Reducing Equations to Linear Form (Cross Multiplication)', ['Rational algebraic expressions', 'Cross-multiplication technique for (ax+b)/(cx+d) = k']),
        createTopic('CBSE', '8', 'MGP1', '4', '4', 'Applications & Word Problems (Age, Number, Perimeter, Coins)', ['Age-related problems', 'Perimeter and dimension problems', 'Two-digit number reversal problems', 'Denomination and coin problems'])
      ]
    },
    {
      number: '5',
      name: 'Understanding Quadrilaterals',
      topics: [
        createTopic('CBSE', '8', 'MGP1', '5', '1', 'Polygons: Convex, Concave, Regular & Irregular', ['Classification of polygons by sides', 'Diagonals of a polygon', 'Convex vs concave polygons', 'Regular vs irregular polygons']),
        createTopic('CBSE', '8', 'MGP1', '5', '2', 'Angle Sum Property & Exterior Angles of Polygons', ['Interior angle sum formula (n-2)*180°', 'Sum of exterior angles is always 360°', 'Finding number of sides from exterior angles']),
        createTopic('CBSE', '8', 'MGP1', '5', '3', 'Properties of Trapezium, Kite & Parallelograms', ['Trapezium and isosceles trapezium', 'Kite properties (perpendicular diagonals)', 'Parallelogram opposite sides and angles theorem', 'Adjacent angles of parallelogram are supplementary'], '', ['Opposite sides and angles of a parallelogram are equal']),
        createTopic('CBSE', '8', 'MGP1', '5', '4', 'Special Parallelograms: Rhombus, Rectangle, Square', ['Rhombus diagonals are perpendicular bisectors', 'Rectangle diagonals are equal and bisect each other', 'Square diagonals are equal and perpendicular bisectors'], '', ['Diagonals of a rhombus are perpendicular bisectors of each other'])
      ]
    },
    {
      number: '6',
      name: 'Algebraic Expressions and Identities',
      topics: [
        createTopic('CBSE', '8', 'MGP1', '6', '1', 'Terms, Factors, Coefficients & Classification of Polynomials', ['Monomial, binomial, trinomial, polynomial', 'Like terms vs unlike terms', 'Degree of an algebraic expression']),
        createTopic('CBSE', '8', 'MGP1', '6', '2', 'Addition and Subtraction of Algebraic Expressions', ['Column method for addition/subtraction', 'Horizontal grouping of like terms']),
        createTopic('CBSE', '8', 'MGP1', '6', '3', 'Multiplication of Monomials, Binomials & Polynomials', ['Product of monomials', 'Monomial by polynomial multiplication', 'Binomial by binomial multiplication (FOIL)']),
        createTopic('CBSE', '8', 'MGP1', '6', '4', 'Standard Algebraic Identities & Geometric Proofs', ['Identity I: (a+b)² = a² + 2ab + b²', 'Identity II: (a-b)² = a² - 2ab + b²', 'Identity III: (a+b)(a-b) = a² - b²', 'Identity IV: (x+a)(x+b) = x² + (a+b)x + ab']),
        createTopic('CBSE', '8', 'MGP1', '6', '5', 'Applications of Identities in Numerical Calculations', ['Evaluating squares of numbers without direct multiplication (e.g. 102², 99²)', 'Product of near numbers (e.g. 103 * 97)'])
      ]
    },
    {
      number: '7',
      name: 'Visualising Solid Shapes',
      topics: [
        createTopic('CBSE', '8', 'MGP1', '7', '1', '2D Views of 3D Objects (Top, Front, Side Views)', ['Identifying front, top and side views of everyday objects', 'Viewing composite solid structures']),
        createTopic('CBSE', '8', 'MGP1', '7', '2', 'Mapping Space Around Us & Scale Factors', ['Reading and drawing road maps', 'Scale ratios in blueprints and maps']),
        createTopic('CBSE', '8', 'MGP1', '7', '3', 'Faces, Edges, Vertices & Euler Formula for Polyhedra', ['Convex vs non-convex polyhedra', 'Prisms vs pyramids', 'Euler formula: F + V - E = 2'])
      ]
    }
  ]
});

// =========================================================================
// 2. CBSE Class 8: Ganit Prakash Part 2 (CBSE-8-MGP2)
// =========================================================================
subjects.push({
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
        createTopic('CBSE', '8', 'MGP2', '8', '1', 'Ratios, Percentages & Increase/Decrease Percent', ['Converting ratios to percentages and vice-versa', 'Percentage change formula', 'Estimating percentages in real life']),
        createTopic('CBSE', '8', 'MGP2', '8', '2', 'Discounts, Profit & Loss, Marked Price & Cost Price', ['Discount = Marked Price - Sale Price', 'Discount percentage', 'Profit and Loss percentage on Cost Price']),
        createTopic('CBSE', '8', 'MGP2', '8', '3', 'Sales Tax, VAT & Goods and Services Tax (GST)', ['Calculation of GST on bill amount', 'Net price inclusive of tax']),
        createTopic('CBSE', '8', 'MGP2', '8', '4', 'Compound Interest Formula (Annually & Half-Yearly)', ['Difference between Simple Interest and Compound Interest', 'Amount formula: A = P(1 + r/100)^n', 'Compounding half-yearly and quarterly adjustments']),
        createTopic('CBSE', '8', 'MGP2', '8', '5', 'Applications of Compound Interest: Population & Depreciation', ['Population growth rate formula', 'Depreciation of machinery and value decay'])
      ]
    },
    {
      number: '9',
      name: 'Direct and Inverse Proportions',
      topics: [
        createTopic('CBSE', '8', 'MGP2', '9', '1', 'Direct Proportion Concepts & Constant of Variation (x/y = k)', ['Direct variation definition', 'Finding missing values using x1/y1 = x2/y2', 'Unitary method vs proportion method']),
        createTopic('CBSE', '8', 'MGP2', '9', '2', 'Inverse Proportion Concepts & Constant Product (xy = k)', ['Inverse variation definition', 'Solving using x1*y1 = x2*y2', 'Speed, distance, and time relationships']),
        createTopic('CBSE', '8', 'MGP2', '9', '3', 'Real-World Word Problems (Work-Time, Speed-Time, Resources)', ['Workers and days problems', 'Food provisions and population consumption problems'])
      ]
    },
    {
      number: '10',
      name: 'Mensuration',
      topics: [
        createTopic('CBSE', '8', 'MGP2', '10', '1', 'Area of Trapezium & General Quadrilaterals', ['Trapezium area = 1/2 * (a+b) * h', 'General quadrilateral area using diagonal and offsets', 'Rhombus area = 1/2 * d1 * d2']),
        createTopic('CBSE', '8', 'MGP2', '10', '2', 'Area of Polygons by Triangulation', ['Dividing irregular field polygons into triangles and trapeziums', 'Surveyor field book calculations']),
        createTopic('CBSE', '8', 'MGP2', '10', '3', 'Surface Area of Cube, Cuboid & Cylinder', ['Total Surface Area and Lateral Surface Area of Cuboid', 'TSA and LSA of Cube (6a², 4a²)', 'Curved Surface Area and Total Surface Area of Cylinder (2πrh, 2πr(r+h))']),
        createTopic('CBSE', '8', 'MGP2', '10', '4', 'Volume of Cube, Cuboid & Cylinder', ['Volume of cuboid = l * b * h', 'Volume of cube = a³', 'Volume of cylinder = πr²h', 'Conversion of volume units (cm³, m³, litres)'])
      ]
    },
    {
      number: '11',
      name: 'Introduction to Graphs',
      topics: [
        createTopic('CBSE', '8', 'MGP2', '11', '1', 'Bar Graphs, Pie Charts & Histograms Overview', ['Reading single and double bar graphs', 'Interpreting pie graphs (circle charts)', 'Histogram with continuous class intervals']),
        createTopic('CBSE', '8', 'MGP2', '11', '2', 'Line Graphs & Continuous Time-Distance Trends', ['Reading line graphs and trend lines', 'Distance-time graph interpretation']),
        createTopic('CBSE', '8', 'MGP2', '11', '3', 'Cartesian Coordinate System & Plotting Points (x, y)', ['X-axis, Y-axis, origin (0,0)', 'Coordinates (abscissa and ordinate)', 'Plotting points on graph paper']),
        createTopic('CBSE', '8', 'MGP2', '11', '4', 'Linear Graphs & Independent vs Dependent Variables', ['Linear relation between variables (e.g. perimeter vs side)', 'Independent variable on X-axis, dependent on Y-axis', 'Finding values from linear graph'])
      ]
    },
    {
      number: '12',
      name: 'Factorisation',
      topics: [
        createTopic('CBSE', '8', 'MGP2', '12', '1', 'Factorisation by Common Factors & Regrouping', ['Monomial common factor method', 'Regrouping terms to find common binomial factors']),
        createTopic('CBSE', '8', 'MGP2', '12', '2', 'Factorisation Using Standard Algebraic Identities', ['Factoring perfect square trinomials (a² ± 2ab + b²)', 'Factoring difference of two squares (a² - b²)']),
        createTopic('CBSE', '8', 'MGP2', '12', '3', 'Factorisation of Form (x² + px + q) by Splitting Middle Term', ['Finding two numbers whose sum is p and product is q', 'Sign rules in middle term splitting']),
        createTopic('CBSE', '8', 'MGP2', '12', '4', 'Division of Algebraic Expressions (Monomials & Polynomials)', ['Dividing monomial by monomial', 'Dividing polynomial by monomial', 'Dividing polynomial by polynomial using factorisation'])
      ]
    },
    {
      number: '13',
      name: 'Playing with Numbers',
      topics: [
        createTopic('CBSE', '8', 'MGP2', '13', '1', 'Generalised Form of Numbers & Number Puzzles', ['Two-digit form 10a+b, three-digit form 100a+10b+c', 'Reversing digits puzzles and divisibility properties']),
        createTopic('CBSE', '8', 'MGP2', '13', '2', 'Letters for Digits (Cryptarithms)', ['Addition puzzles with alphabet substitutions', 'Multiplication puzzles with alphabet substitutions']),
        createTopic('CBSE', '8', 'MGP2', '13', '3', 'Divisibility Tests for 2, 3, 5, 9 and 10 & Mathematical Reasons', ['Divisibility by 10, 5, 2 from unit digit', 'Divisibility by 3 and 9 using sum of digits', 'Divisibility by 11 using alternating digit sums'])
      ]
    }
  ]
});

console.log(`Loaded ${subjects.length} subjects so far...`);
