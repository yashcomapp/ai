/**
 * Master Syllabus Data SSOT (Official NCERT & Balbharti Curricula)
 * Contains the complete 16 baseline subjects with canonical deep atomic topic codes,
 * subtopics micro-concepts, practice sets, problem sets, and named theorems.
 */

export interface MasterTopic {
  number: string;
  name: string;
  topicCode: string;
  subtopics?: string[];
  practiceSet?: string;
  theorems?: string[];
  problemSet?: string;
}

export interface MasterChapter {
  number: string;
  name: string;
  topics: MasterTopic[];
}

export interface MasterSyllabusSubject {
  docId: string;
  board: 'CBSE' | 'Maharashtra Board';
  boardCode: 'CBSE' | 'MH';
  class: string;
  subject: string;
  subjectCode: string;
  chapters: MasterChapter[];
}

export const MASTER_SYLLABUS_SUBJECTS: MasterSyllabusSubject[] = [
  {
    "docId": "cbse_8_mgp1",
    "board": "CBSE",
    "boardCode": "CBSE",
    "class": "8",
    "subject": "Ganit Prakash Part 1",
    "subjectCode": "MGP1",
    "chapters": [
      {
        "number": "1",
        "name": "A Square and a Cube",
        "topics": [
          {
            "number": "1.1",
            "name": "Properties of Square Numbers & Unit Digits",
            "topicCode": "CBSE-8-MGP1-1-1.1",
            "subtopics": [
              "Ending digits of square numbers",
              "Zeros at the end of squares",
              "Squares of even and odd numbers"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Patterns in Square Numbers & Pythagorean Triplets",
            "topicCode": "CBSE-8-MGP1-1-1.2",
            "subtopics": [
              "Sum of consecutive odd numbers",
              "Non-square numbers between consecutive squares",
              "Pythagorean triplets formula (2m, m²-1, m²+1)"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Finding Square Roots by Prime Factorisation",
            "topicCode": "CBSE-8-MGP1-1-1.3",
            "subtopics": [
              "Square root as inverse of squaring",
              "Prime factor pairing",
              "Smallest multiplier or divisor to get perfect square"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Finding Square Roots by Long Division & Decimals",
            "topicCode": "CBSE-8-MGP1-1-1.4",
            "subtopics": [
              "Long division algorithm",
              "Square roots of decimals",
              "Estimating square roots in word problems"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.5",
            "name": "Cubes & Patterns in Cube Numbers",
            "topicCode": "CBSE-8-MGP1-1-1.5",
            "subtopics": [
              "Cube numbers definition",
              "Adding consecutive odd numbers for cubes",
              "Prime factorisation of cubes"
            ],
            "practiceSet": "Exercise 1.5",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.6",
            "name": "Cube Roots by Prime Factorisation & Estimation",
            "topicCode": "CBSE-8-MGP1-1-1.6",
            "subtopics": [
              "Cube root symbol and definition",
              "Triplets of prime factors",
              "Estimation method for cube roots"
            ],
            "practiceSet": "Exercise 1.6",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Power Play (Exponents and Powers)",
        "topics": [
          {
            "number": "2.1",
            "name": "Powers with Negative Integral Exponents",
            "topicCode": "CBSE-8-MGP1-2-2.1",
            "subtopics": [
              "Meaning of a^(-m) = 1/a^m",
              "Multiplicative inverse with powers",
              "Expanded form of decimal numbers using powers of 10"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Laws of Exponents & Simplification",
            "topicCode": "CBSE-8-MGP1-2-2.2",
            "subtopics": [
              "Product of powers rule",
              "Quotient of powers rule",
              "Power of a power rule",
              "Power of a product and quotient",
              "Zero exponent rule a^0 = 1"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Standard Form (Scientific Notation) for Large & Small Numbers",
            "topicCode": "CBSE-8-MGP1-2-2.3",
            "subtopics": [
              "Expressing numbers in k * 10^n format",
              "Converting decimal numbers to standard form",
              "Microscopic scale measurements (size of bacteria, charge on electron)"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Comparison & Arithmetic with Exponential Quantities",
            "topicCode": "CBSE-8-MGP1-2-2.4",
            "subtopics": [
              "Comparing astronomical distances",
              "Addition and subtraction of numbers in standard form"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "A Story of Numbers",
        "topics": [
          {
            "number": "3.1",
            "name": "Rational Numbers & Closure, Commutative Properties",
            "topicCode": "CBSE-8-MGP1-3-3.1",
            "subtopics": [
              "Definition of p/q format (q != 0)",
              "Closure under addition, subtraction, multiplication",
              "Commutativity properties"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Associative, Distributive Properties & Identities",
            "topicCode": "CBSE-8-MGP1-3-3.2",
            "subtopics": [
              "Associativity of rational numbers",
              "Additive identity (0) and multiplicative identity (1)",
              "Additive inverse and reciprocal",
              "Distributive property a(b+c) = ab + ac"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Representation of Rational Numbers on the Number Line",
            "topicCode": "CBSE-8-MGP1-3-3.3",
            "subtopics": [
              "Equidistant divisions of unit lengths",
              "Locating positive and negative rational numbers"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Finding Rational Numbers Between Two Rational Numbers",
            "topicCode": "CBSE-8-MGP1-3-3.4",
            "subtopics": [
              "Mean method (a+b)/2",
              "LCM equivalent fraction method",
              "Density of rational numbers"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Linear Equations in One Variable",
        "topics": [
          {
            "number": "4.1",
            "name": "Solving Linear Equations with Variable on One Side",
            "topicCode": "CBSE-8-MGP1-4-4.1",
            "subtopics": [
              "Transposition of terms",
              "Balancing method of solving"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Solving Equations with Variables on Both Sides",
            "topicCode": "CBSE-8-MGP1-4-4.2",
            "subtopics": [
              "Collecting variable terms to LHS",
              "Solving brackets with distributive property"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Reducing Equations to Linear Form (Cross Multiplication)",
            "topicCode": "CBSE-8-MGP1-4-4.3",
            "subtopics": [
              "Rational algebraic expressions",
              "Cross-multiplication technique for (ax+b)/(cx+d) = k"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.4",
            "name": "Applications & Word Problems (Age, Number, Perimeter, Coins)",
            "topicCode": "CBSE-8-MGP1-4-4.4",
            "subtopics": [
              "Age-related problems",
              "Perimeter and dimension problems",
              "Two-digit number reversal problems",
              "Denomination and coin problems"
            ],
            "practiceSet": "Exercise 4.4",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Understanding Quadrilaterals",
        "topics": [
          {
            "number": "5.1",
            "name": "Polygons: Convex, Concave, Regular & Irregular",
            "topicCode": "CBSE-8-MGP1-5-5.1",
            "subtopics": [
              "Classification of polygons by sides",
              "Diagonals of a polygon",
              "Convex vs concave polygons",
              "Regular vs irregular polygons"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Angle Sum Property & Exterior Angles of Polygons",
            "topicCode": "CBSE-8-MGP1-5-5.2",
            "subtopics": [
              "Interior angle sum formula (n-2)*180°",
              "Sum of exterior angles is always 360°",
              "Finding number of sides from exterior angles"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Properties of Trapezium, Kite & Parallelograms",
            "topicCode": "CBSE-8-MGP1-5-5.3",
            "subtopics": [
              "Trapezium and isosceles trapezium",
              "Kite properties (perpendicular diagonals)",
              "Parallelogram opposite sides and angles theorem",
              "Adjacent angles of parallelogram are supplementary"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [
              "Opposite sides and angles of a parallelogram are equal"
            ],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.4",
            "name": "Special Parallelograms: Rhombus, Rectangle, Square",
            "topicCode": "CBSE-8-MGP1-5-5.4",
            "subtopics": [
              "Rhombus diagonals are perpendicular bisectors",
              "Rectangle diagonals are equal and bisect each other",
              "Square diagonals are equal and perpendicular bisectors"
            ],
            "practiceSet": "Exercise 5.4",
            "theorems": [
              "Diagonals of a rhombus are perpendicular bisectors of each other"
            ],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Algebraic Expressions and Identities",
        "topics": [
          {
            "number": "6.1",
            "name": "Terms, Factors, Coefficients & Classification of Polynomials",
            "topicCode": "CBSE-8-MGP1-6-6.1",
            "subtopics": [
              "Monomial, binomial, trinomial, polynomial",
              "Like terms vs unlike terms",
              "Degree of an algebraic expression"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Addition and Subtraction of Algebraic Expressions",
            "topicCode": "CBSE-8-MGP1-6-6.2",
            "subtopics": [
              "Column method for addition/subtraction",
              "Horizontal grouping of like terms"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Multiplication of Monomials, Binomials & Polynomials",
            "topicCode": "CBSE-8-MGP1-6-6.3",
            "subtopics": [
              "Product of monomials",
              "Monomial by polynomial multiplication",
              "Binomial by binomial multiplication (FOIL)"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.4",
            "name": "Standard Algebraic Identities & Geometric Proofs",
            "topicCode": "CBSE-8-MGP1-6-6.4",
            "subtopics": [
              "Identity I: (a+b)² = a² + 2ab + b²",
              "Identity II: (a-b)² = a² - 2ab + b²",
              "Identity III: (a+b)(a-b) = a² - b²",
              "Identity IV: (x+a)(x+b) = x² + (a+b)x + ab"
            ],
            "practiceSet": "Exercise 6.4",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.5",
            "name": "Applications of Identities in Numerical Calculations",
            "topicCode": "CBSE-8-MGP1-6-6.5",
            "subtopics": [
              "Evaluating squares of numbers without direct multiplication (e.g. 102², 99²)",
              "Product of near numbers (e.g. 103 * 97)"
            ],
            "practiceSet": "Exercise 6.5",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Visualising Solid Shapes",
        "topics": [
          {
            "number": "7.1",
            "name": "2D Views of 3D Objects (Top, Front, Side Views)",
            "topicCode": "CBSE-8-MGP1-7-7.1",
            "subtopics": [
              "Identifying front, top and side views of everyday objects",
              "Viewing composite solid structures"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Mapping Space Around Us & Scale Factors",
            "topicCode": "CBSE-8-MGP1-7-7.2",
            "subtopics": [
              "Reading and drawing road maps",
              "Scale ratios in blueprints and maps"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Faces, Edges, Vertices & Euler Formula for Polyhedra",
            "topicCode": "CBSE-8-MGP1-7-7.3",
            "subtopics": [
              "Convex vs non-convex polyhedra",
              "Prisms vs pyramids",
              "Euler formula: F + V - E = 2"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      }
    ]
  },
  {
    "docId": "cbse_8_mgp2",
    "board": "CBSE",
    "boardCode": "CBSE",
    "class": "8",
    "subject": "Ganit Prakash Part 2",
    "subjectCode": "MGP2",
    "chapters": [
      {
        "number": "8",
        "name": "Comparing Quantities",
        "topics": [
          {
            "number": "8.1",
            "name": "Ratios, Percentages & Increase/Decrease Percent",
            "topicCode": "CBSE-8-MGP2-8-8.1",
            "subtopics": [
              "Converting ratios to percentages and vice-versa",
              "Percentage change formula",
              "Estimating percentages in real life"
            ],
            "practiceSet": "Exercise 8.1",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.2",
            "name": "Discounts, Profit & Loss, Marked Price & Cost Price",
            "topicCode": "CBSE-8-MGP2-8-8.2",
            "subtopics": [
              "Discount = Marked Price - Sale Price",
              "Discount percentage",
              "Profit and Loss percentage on Cost Price"
            ],
            "practiceSet": "Exercise 8.2",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.3",
            "name": "Sales Tax, VAT & Goods and Services Tax (GST)",
            "topicCode": "CBSE-8-MGP2-8-8.3",
            "subtopics": [
              "Calculation of GST on bill amount",
              "Net price inclusive of tax"
            ],
            "practiceSet": "Exercise 8.3",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.4",
            "name": "Compound Interest Formula (Annually & Half-Yearly)",
            "topicCode": "CBSE-8-MGP2-8-8.4",
            "subtopics": [
              "Difference between Simple Interest and Compound Interest",
              "Amount formula: A = P(1 + r/100)^n",
              "Compounding half-yearly and quarterly adjustments"
            ],
            "practiceSet": "Exercise 8.4",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.5",
            "name": "Applications of Compound Interest: Population & Depreciation",
            "topicCode": "CBSE-8-MGP2-8-8.5",
            "subtopics": [
              "Population growth rate formula",
              "Depreciation of machinery and value decay"
            ],
            "practiceSet": "Exercise 8.5",
            "theorems": [],
            "problemSet": "Problem Set 8"
          }
        ]
      },
      {
        "number": "9",
        "name": "Direct and Inverse Proportions",
        "topics": [
          {
            "number": "9.1",
            "name": "Direct Proportion Concepts & Constant of Variation (x/y = k)",
            "topicCode": "CBSE-8-MGP2-9-9.1",
            "subtopics": [
              "Direct variation definition",
              "Finding missing values using x1/y1 = x2/y2",
              "Unitary method vs proportion method"
            ],
            "practiceSet": "Exercise 9.1",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.2",
            "name": "Inverse Proportion Concepts & Constant Product (xy = k)",
            "topicCode": "CBSE-8-MGP2-9-9.2",
            "subtopics": [
              "Inverse variation definition",
              "Solving using x1*y1 = x2*y2",
              "Speed, distance, and time relationships"
            ],
            "practiceSet": "Exercise 9.2",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.3",
            "name": "Real-World Word Problems (Work-Time, Speed-Time, Resources)",
            "topicCode": "CBSE-8-MGP2-9-9.3",
            "subtopics": [
              "Workers and days problems",
              "Food provisions and population consumption problems"
            ],
            "practiceSet": "Exercise 9.3",
            "theorems": [],
            "problemSet": "Problem Set 9"
          }
        ]
      },
      {
        "number": "10",
        "name": "Mensuration",
        "topics": [
          {
            "number": "10.1",
            "name": "Area of Trapezium & General Quadrilaterals",
            "topicCode": "CBSE-8-MGP2-10-10.1",
            "subtopics": [
              "Trapezium area = 1/2 * (a+b) * h",
              "General quadrilateral area using diagonal and offsets",
              "Rhombus area = 1/2 * d1 * d2"
            ],
            "practiceSet": "Exercise 10.1",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.2",
            "name": "Area of Polygons by Triangulation",
            "topicCode": "CBSE-8-MGP2-10-10.2",
            "subtopics": [
              "Dividing irregular field polygons into triangles and trapeziums",
              "Surveyor field book calculations"
            ],
            "practiceSet": "Exercise 10.2",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.3",
            "name": "Surface Area of Cube, Cuboid & Cylinder",
            "topicCode": "CBSE-8-MGP2-10-10.3",
            "subtopics": [
              "Total Surface Area and Lateral Surface Area of Cuboid",
              "TSA and LSA of Cube (6a², 4a²)",
              "Curved Surface Area and Total Surface Area of Cylinder (2πrh, 2πr(r+h))"
            ],
            "practiceSet": "Exercise 10.3",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.4",
            "name": "Volume of Cube, Cuboid & Cylinder",
            "topicCode": "CBSE-8-MGP2-10-10.4",
            "subtopics": [
              "Volume of cuboid = l * b * h",
              "Volume of cube = a³",
              "Volume of cylinder = πr²h",
              "Conversion of volume units (cm³, m³, litres)"
            ],
            "practiceSet": "Exercise 10.4",
            "theorems": [],
            "problemSet": "Problem Set 10"
          }
        ]
      },
      {
        "number": "11",
        "name": "Introduction to Graphs",
        "topics": [
          {
            "number": "11.1",
            "name": "Bar Graphs, Pie Charts & Histograms Overview",
            "topicCode": "CBSE-8-MGP2-11-11.1",
            "subtopics": [
              "Reading single and double bar graphs",
              "Interpreting pie graphs (circle charts)",
              "Histogram with continuous class intervals"
            ],
            "practiceSet": "Exercise 11.1",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.2",
            "name": "Line Graphs & Continuous Time-Distance Trends",
            "topicCode": "CBSE-8-MGP2-11-11.2",
            "subtopics": [
              "Reading line graphs and trend lines",
              "Distance-time graph interpretation"
            ],
            "practiceSet": "Exercise 11.2",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.3",
            "name": "Cartesian Coordinate System & Plotting Points (x, y)",
            "topicCode": "CBSE-8-MGP2-11-11.3",
            "subtopics": [
              "X-axis, Y-axis, origin (0,0)",
              "Coordinates (abscissa and ordinate)",
              "Plotting points on graph paper"
            ],
            "practiceSet": "Exercise 11.3",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.4",
            "name": "Linear Graphs & Independent vs Dependent Variables",
            "topicCode": "CBSE-8-MGP2-11-11.4",
            "subtopics": [
              "Linear relation between variables (e.g. perimeter vs side)",
              "Independent variable on X-axis, dependent on Y-axis",
              "Finding values from linear graph"
            ],
            "practiceSet": "Exercise 11.4",
            "theorems": [],
            "problemSet": "Problem Set 11"
          }
        ]
      },
      {
        "number": "12",
        "name": "Factorisation",
        "topics": [
          {
            "number": "12.1",
            "name": "Factorisation by Common Factors & Regrouping",
            "topicCode": "CBSE-8-MGP2-12-12.1",
            "subtopics": [
              "Monomial common factor method",
              "Regrouping terms to find common binomial factors"
            ],
            "practiceSet": "Exercise 12.1",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.2",
            "name": "Factorisation Using Standard Algebraic Identities",
            "topicCode": "CBSE-8-MGP2-12-12.2",
            "subtopics": [
              "Factoring perfect square trinomials (a² ± 2ab + b²)",
              "Factoring difference of two squares (a² - b²)"
            ],
            "practiceSet": "Exercise 12.2",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.3",
            "name": "Factorisation of Form (x² + px + q) by Splitting Middle Term",
            "topicCode": "CBSE-8-MGP2-12-12.3",
            "subtopics": [
              "Finding two numbers whose sum is p and product is q",
              "Sign rules in middle term splitting"
            ],
            "practiceSet": "Exercise 12.3",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.4",
            "name": "Division of Algebraic Expressions (Monomials & Polynomials)",
            "topicCode": "CBSE-8-MGP2-12-12.4",
            "subtopics": [
              "Dividing monomial by monomial",
              "Dividing polynomial by monomial",
              "Dividing polynomial by polynomial using factorisation"
            ],
            "practiceSet": "Exercise 12.4",
            "theorems": [],
            "problemSet": "Problem Set 12"
          }
        ]
      },
      {
        "number": "13",
        "name": "Playing with Numbers",
        "topics": [
          {
            "number": "13.1",
            "name": "Generalised Form of Numbers & Number Puzzles",
            "topicCode": "CBSE-8-MGP2-13-13.1",
            "subtopics": [
              "Two-digit form 10a+b, three-digit form 100a+10b+c",
              "Reversing digits puzzles and divisibility properties"
            ],
            "practiceSet": "Exercise 13.1",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.2",
            "name": "Letters for Digits (Cryptarithms)",
            "topicCode": "CBSE-8-MGP2-13-13.2",
            "subtopics": [
              "Addition puzzles with alphabet substitutions",
              "Multiplication puzzles with alphabet substitutions"
            ],
            "practiceSet": "Exercise 13.2",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.3",
            "name": "Divisibility Tests for 2, 3, 5, 9 and 10 & Mathematical Reasons",
            "topicCode": "CBSE-8-MGP2-13-13.3",
            "subtopics": [
              "Divisibility by 10, 5, 2 from unit digit",
              "Divisibility by 3 and 9 using sum of digits",
              "Divisibility by 11 using alternating digit sums"
            ],
            "practiceSet": "Exercise 13.3",
            "theorems": [],
            "problemSet": "Problem Set 13"
          }
        ]
      }
    ]
  },
  {
    "docId": "cbse_8_curi",
    "board": "CBSE",
    "boardCode": "CBSE",
    "class": "8",
    "subject": "Curiosity Science",
    "subjectCode": "CURI",
    "chapters": [
      {
        "number": "1",
        "name": "Crop Production and Management",
        "topics": [
          {
            "number": "1.1",
            "name": "Agricultural Practices: Kharif vs Rabi Crops",
            "topicCode": "CBSE-8-CURI-1-1.1",
            "subtopics": [
              "Definition of crop",
              "Kharif crops (sown in rainy season e.g. paddy, maize)",
              "Rabi crops (sown in winter season e.g. wheat, gram, pea)"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Soil Preparation, Ploughing & Sowing Methods",
            "topicCode": "CBSE-8-CURI-1-1.2",
            "subtopics": [
              "Tilling and ploughing tools (plough, hoe, cultivator)",
              "Selection of healthy seeds",
              "Traditional tools vs modern seed drills"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Adding Manure and Fertilisers & Crop Rotation",
            "topicCode": "CBSE-8-CURI-1-1.3",
            "subtopics": [
              "Organic manure vs chemical fertilisers (NPK, Urea)",
              "Advantages of manure on soil texture and water retention",
              "Crop rotation and leguminous plants with Rhizobium"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Irrigation Systems: Traditional vs Modern (Drip & Sprinkler)",
            "topicCode": "CBSE-8-CURI-1-1.4",
            "subtopics": [
              "Traditional methods (moat, chain pump, dheli, rahat)",
              "Sprinkler system for uneven land",
              "Drip system for water conservation in arid regions"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.5",
            "name": "Protection from Weeds, Harvesting, Threshing & Storage",
            "topicCode": "CBSE-8-CURI-1-1.5",
            "subtopics": [
              "Weeds and weedicides (e.g. 2,4-D)",
              "Harvesting tools (sickle, combine harvester)",
              "Threshing and winnowing",
              "Grain silos, granaries, and buffer stock storage"
            ],
            "practiceSet": "Exercise 1.5",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Microorganisms: Friend and Foe",
        "topics": [
          {
            "number": "2.1",
            "name": "Classification of Microorganisms & Habitats",
            "topicCode": "CBSE-8-CURI-2-2.1",
            "subtopics": [
              "Bacteria, Fungi, Protozoa, Algae",
              "Viruses: obligate intracellular nature",
              "Habitats: ice cold to hot springs, desert to marshy land"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Friendly Microbes: Food Production, Fermentation & Antibiotics",
            "topicCode": "CBSE-8-CURI-2-2.2",
            "subtopics": [
              "Lactobacillus in curd and cheese",
              "Yeast in bread and alcohol fermentation",
              "Commercial antibiotics (Penicillin, Streptomycin, Tetracycline)",
              "Vaccine production and antibodies"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Harmful Microorganisms: Human, Plant & Animal Diseases",
            "topicCode": "CBSE-8-CURI-2-2.3",
            "subtopics": [
              "Communicable diseases and pathogen modes of transmission",
              "Carriers: Female Anopheles (Malaria), Aedes (Dengue)",
              "Plant diseases: Citrus canker, Rust of wheat, Yellow vein mosaic",
              "Anthrax disease in animals"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Food Preservation Methods & Pasteurisation",
            "topicCode": "CBSE-8-CURI-2-2.4",
            "subtopics": [
              "Chemical preservatives (sodium benzoate, metabisulphite)",
              "Common salt, sugar, oil, and vinegar preservation",
              "Heat and cold treatments",
              "Pasteurisation method (Louis Pasteur)"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.5",
            "name": "Nitrogen Fixation & the Nitrogen Cycle",
            "topicCode": "CBSE-8-CURI-2-2.5",
            "subtopics": [
              "Atmospheric nitrogen fixation by Rhizobium & blue-green algae",
              "Lightning nitrogen fixation",
              "Nitrification, assimilation, and denitrification steps in nitrogen cycle"
            ],
            "practiceSet": "Exercise 2.5",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Coal and Petroleum",
        "topics": [
          {
            "number": "3.1",
            "name": "Exhaustible vs Inexhaustible Natural Resources",
            "topicCode": "CBSE-8-CURI-3-3.1",
            "subtopics": [
              "Inexhaustible resources (sunlight, air)",
              "Exhaustible resources (coal, petroleum, minerals)"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Coal: Carbonisation, Coke, Coal Tar and Coal Gas",
            "topicCode": "CBSE-8-CURI-3-3.2",
            "subtopics": [
              "Formation of coal from dead vegetation (Carbonisation)",
              "Coke properties and uses in steel extraction",
              "Coal tar and chemical products",
              "Coal gas as industrial fuel"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Petroleum: Refining & Fractional Distillation Products",
            "topicCode": "CBSE-8-CURI-3-3.3",
            "subtopics": [
              "Formation and drilling of petroleum oil",
              "Fractional distillation column",
              "Fractions: Petrol, Diesel, Kerosene, LPG, Lubricating oil, Paraffin wax, Bitumen"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Natural Gas (CNG) & Conservation of Fossil Fuels",
            "topicCode": "CBSE-8-CURI-3-3.4",
            "subtopics": [
              "Compressed Natural Gas advantages and pipeline network",
              "PCRA tips for saving petrol and diesel"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Combustion and Flame",
        "topics": [
          {
            "number": "4.1",
            "name": "Combustion Definition & Essential Conditions for Burning",
            "topicCode": "CBSE-8-CURI-4-4.1",
            "subtopics": [
              "Combustible vs non-combustible substances",
              "Presence of oxygen/air necessity",
              "Ignition temperature definition"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Types of Combustion: Rapid, Spontaneous & Explosion",
            "topicCode": "CBSE-8-CURI-4-4.2",
            "subtopics": [
              "Rapid combustion (LPG burner)",
              "Spontaneous combustion (white phosphorus, coal dust)",
              "Explosion (fireworks, sudden gas expansion)"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Structure of a Candle Flame (Three Zones)",
            "topicCode": "CBSE-8-CURI-4-4.3",
            "subtopics": [
              "Innermost dark zone (unburnt wax vapors)",
              "Middle luminous yellow zone (incomplete combustion)",
              "Outermost non-luminous blue zone (complete combustion & hottest)"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.4",
            "name": "Fuel Efficiency, Calorific Value & Harmful Effects of Burning",
            "topicCode": "CBSE-8-CURI-4-4.4",
            "subtopics": [
              "Calorific value (kJ/kg)",
              "Ideal fuel characteristics",
              "Harmful combustion products: carbon monoxide poisoning, acid rain (SO2, NO2), global warming (CO2)"
            ],
            "practiceSet": "Exercise 4.4",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Conservation of Plants and Animals",
        "topics": [
          {
            "number": "5.1",
            "name": "Deforestation: Causes and Consequences",
            "topicCode": "CBSE-8-CURI-5-5.1",
            "subtopics": [
              "Agricultural expansion, logging, urbanisation",
              "Desertification, soil erosion, and disrupted water cycle"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Biosphere Reserves, National Parks & Wildlife Sanctuaries",
            "topicCode": "CBSE-8-CURI-5-5.2",
            "subtopics": [
              "Panchmarhi Biosphere Reserve",
              "Core, buffer, and transition zones",
              "In-situ vs ex-situ conservation"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Flora, Fauna & Endemic Species",
            "topicCode": "CBSE-8-CURI-5-5.3",
            "subtopics": [
              "Flora and fauna definitions",
              "Endemic species of Panchmarhi (sal, wild mango, Indian giant squirrel)"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.4",
            "name": "Endangered Species, Red Data Book, Migration & Reforestation",
            "topicCode": "CBSE-8-CURI-5-5.4",
            "subtopics": [
              "Threatened vs endangered vs extinct species",
              "IUCN Red Data Book records",
              "Bird migration reasons",
              "Reforestation practices and Forest Conservation Act"
            ],
            "practiceSet": "Exercise 5.4",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Reproduction in Animals",
        "topics": [
          {
            "number": "6.1",
            "name": "Modes of Reproduction: Sexual vs Asexual",
            "topicCode": "CBSE-8-CURI-6-6.1",
            "subtopics": [
              "Basic difference between sexual and asexual modes",
              "Importance of reproduction in species continuity"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Male and Female Reproductive Systems in Humans",
            "topicCode": "CBSE-8-CURI-6-6.2",
            "subtopics": [
              "Male organs: Testes, sperm ducts, penis, sperm structure",
              "Female organs: Ovaries, oviducts (fallopian tubes), uterus, ovum"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Fertilisation: Internal vs External Fertilisation",
            "topicCode": "CBSE-8-CURI-6-6.3",
            "subtopics": [
              "Zygote formation",
              "Internal fertilisation in humans, cows, hens",
              "External fertilisation in frogs and fish"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.4",
            "name": "Embryo Development, Viviparous vs Oviparous Animals",
            "topicCode": "CBSE-8-CURI-6-6.4",
            "subtopics": [
              "Cleavage, blastocyst, implantation in uterine wall, foetus formation",
              "Viviparous (give birth) vs Oviparous (lay eggs)"
            ],
            "practiceSet": "Exercise 6.4",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.5",
            "name": "Metamorphosis in Frog & Asexual Reproduction (Budding, Binary Fission)",
            "topicCode": "CBSE-8-CURI-6-6.5",
            "subtopics": [
              "Tadpole to adult metamorphosis under thyroxine control",
              "Budding in Hydra",
              "Binary fission in Amoeba",
              "Cloning of Dolly the sheep"
            ],
            "practiceSet": "Exercise 6.5",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Reaching the Age of Adolescence",
        "topics": [
          {
            "number": "7.1",
            "name": "Adolescence, Puberty & Physical Body Changes",
            "topicCode": "CBSE-8-CURI-7-7.1",
            "subtopics": [
              "Growth spurt, increase in height",
              "Change in body shape and voice (Adam apple)",
              "Sweat and sebaceous gland activation"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Secondary Sexual Characteristics & Hormonal Control",
            "topicCode": "CBSE-8-CURI-7-7.2",
            "subtopics": [
              "Testosterone and estrogen roles",
              "Endocrine system and pituitary master gland hormones"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Reproductive Phase of Life & Menstrual Cycle",
            "topicCode": "CBSE-8-CURI-7-7.3",
            "subtopics": [
              "Menarche and Menopause",
              "Uterine thickening, ovulation, and menstruation cycle"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.4",
            "name": "Sex Determination in Humans & Other Endocrine Hormones",
            "topicCode": "CBSE-8-CURI-7-7.4",
            "subtopics": [
              "XY sex chromosomes in males, XX in females",
              "Thyroid (Thyroxine), Pancreas (Insulin), Adrenal (Adrenaline) glands",
              "Metamorphosis hormones in insects (juvenile hormone, ecdysone)"
            ],
            "practiceSet": "Exercise 7.4",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.5",
            "name": "Nutritional Needs of Adolescents & Reproductive Hygiene",
            "topicCode": "CBSE-8-CURI-7-7.5",
            "subtopics": [
              "Balanced diet and iron-rich foods",
              "Personal hygiene, drug abuse prevention, HIV/AIDS awareness"
            ],
            "practiceSet": "Exercise 7.5",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      },
      {
        "number": "8",
        "name": "Force and Pressure",
        "topics": [
          {
            "number": "8.1",
            "name": "Force: A Push or a Pull & Resultant Forces",
            "topicCode": "CBSE-8-CURI-8-8.1",
            "subtopics": [
              "Forces due to interaction",
              "Adding forces in same direction, subtracting opposing forces",
              "Net resultant force and equilibrium"
            ],
            "practiceSet": "Exercise 8.1",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.2",
            "name": "Effects of Force on State of Motion & Shape",
            "topicCode": "CBSE-8-CURI-8-8.2",
            "subtopics": [
              "Changing speed of object",
              "Changing direction of motion",
              "Changing physical shape of flexible objects"
            ],
            "practiceSet": "Exercise 8.2",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.3",
            "name": "Contact Forces: Muscular Force & Friction Force",
            "topicCode": "CBSE-8-CURI-8-8.3",
            "subtopics": [
              "Muscular force action in living organisms",
              "Frictional force opposing relative motion"
            ],
            "practiceSet": "Exercise 8.3",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.4",
            "name": "Non-Contact Forces: Magnetic, Electrostatic & Gravitational",
            "topicCode": "CBSE-8-CURI-8-8.4",
            "subtopics": [
              "Magnetic attraction and repulsion",
              "Electrostatic force using charged comb/straw",
              "Universal gravitational pull of Earth"
            ],
            "practiceSet": "Exercise 8.4",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.5",
            "name": "Pressure: Formula (P = F/A) & Liquid/Atmospheric Pressure",
            "topicCode": "CBSE-8-CURI-8-8.5",
            "subtopics": [
              "Pressure definition and SI unit Pascal (N/m²)",
              "Dependence of pressure on surface contact area (sharp knife vs blunt)",
              "Liquid pressure increases with depth & exerts equal sideways pressure",
              "Atmospheric pressure measurement and Magdeburg hemispheres experiment"
            ],
            "practiceSet": "Exercise 8.5",
            "theorems": [],
            "problemSet": "Problem Set 8"
          }
        ]
      },
      {
        "number": "9",
        "name": "Friction",
        "topics": [
          {
            "number": "9.1",
            "name": "Force of Friction & Microscopic Irregularities",
            "topicCode": "CBSE-8-CURI-9-9.1",
            "subtopics": [
              "Friction opposes relative motion between surfaces in contact",
              "Interlocking of microscopic irregularities on surfaces",
              "Rough vs smooth surfaces"
            ],
            "practiceSet": "Exercise 9.1",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.2",
            "name": "Factors Affecting Friction: Normal Force & Surface Texture",
            "topicCode": "CBSE-8-CURI-9-9.2",
            "subtopics": [
              "Effect of pressing forces (normal reaction)",
              "Spring balance measurement of friction"
            ],
            "practiceSet": "Exercise 9.2",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.3",
            "name": "Static, Sliding & Rolling Friction (Hierarchy Comparison)",
            "topicCode": "CBSE-8-CURI-9-9.3",
            "subtopics": [
              "Static friction (maximum limiting friction)",
              "Sliding friction is less than static friction",
              "Rolling friction is much smaller than sliding friction"
            ],
            "practiceSet": "Exercise 9.3",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.4",
            "name": "Friction: A Necessary Evil (Advantages & Disadvantages)",
            "topicCode": "CBSE-8-CURI-9-9.4",
            "subtopics": [
              "Advantages: Walking, writing, braking automobiles",
              "Disadvantages: Wear and tear of shoes/tires, energy loss as heat"
            ],
            "practiceSet": "Exercise 9.4",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.5",
            "name": "Methods of Increasing & Decreasing Friction & Fluid Drag",
            "topicCode": "CBSE-8-CURI-9-9.5",
            "subtopics": [
              "Increasing: Treaded tires, grooved soles, spikes for athletes",
              "Decreasing: Lubricants (oil, grease, graphite), ball bearings",
              "Fluid friction (Drag) and streamlined shapes in airplanes, fish, birds"
            ],
            "practiceSet": "Exercise 9.5",
            "theorems": [],
            "problemSet": "Problem Set 9"
          }
        ]
      },
      {
        "number": "10",
        "name": "Sound",
        "topics": [
          {
            "number": "10.1",
            "name": "Sound Produced by Vibrating Bodies & Musical Instruments",
            "topicCode": "CBSE-8-CURI-10-10.1",
            "subtopics": [
              "Vibrating tuning fork, rubber band, string",
              "Vocal cords (larynx) in humans",
              "Wind, percussion, string musical instruments"
            ],
            "practiceSet": "Exercise 10.1",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.2",
            "name": "Sound Needs a Medium for Propagation (Vacuum Bell Jar Experiment)",
            "topicCode": "CBSE-8-CURI-10-10.2",
            "subtopics": [
              "Propagation through solids, liquids, gases",
              "Speed of sound comparison in different media",
              "Cannot travel through vacuum"
            ],
            "practiceSet": "Exercise 10.2",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.3",
            "name": "Human Ear Anatomy & Hearing Mechanism",
            "topicCode": "CBSE-8-CURI-10-10.3",
            "subtopics": [
              "Outer ear (pinna, ear canal)",
              "Middle ear (tympanic membrane/eardrum, three tiny bones)",
              "Inner ear (cochlea) and auditory nerve to brain"
            ],
            "practiceSet": "Exercise 10.3",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.4",
            "name": "Amplitude, Time Period, Frequency, Loudness & Pitch",
            "topicCode": "CBSE-8-CURI-10-10.4",
            "subtopics": [
              "Oscillation and frequency (Hertz, Hz)",
              "Loudness is proportional to square of amplitude (Decibels, dB)",
              "Pitch/shrillness is determined by frequency"
            ],
            "practiceSet": "Exercise 10.4",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.5",
            "name": "Audible vs Inaudible Sounds & Noise Pollution Control",
            "topicCode": "CBSE-8-CURI-10-10.5",
            "subtopics": [
              "Audible range: 20 Hz to 20,000 Hz",
              "Infrasonic (<20 Hz) and Ultrasonic (>20 kHz) sounds",
              "Noise vs music, health hazards of noise pollution, tree belt mitigation"
            ],
            "practiceSet": "Exercise 10.5",
            "theorems": [],
            "problemSet": "Problem Set 10"
          }
        ]
      },
      {
        "number": "11",
        "name": "Chemical Effects of Electric Current",
        "topics": [
          {
            "number": "11.1",
            "name": "Electrical Conductivity of Liquids & Electrolytes",
            "topicCode": "CBSE-8-CURI-11-11.1",
            "subtopics": [
              "Good conductors vs poor conductors",
              "Testing distilled water vs salt/acid/base solutions",
              "LED and magnetic compass tester sensitivity"
            ],
            "practiceSet": "Exercise 11.1",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.2",
            "name": "Chemical Effects of Current (Electrolysis of Water)",
            "topicCode": "CBSE-8-CURI-11-11.2",
            "subtopics": [
              "William Nicholson electrolysis experiment (1800)",
              "Oxygen gas at positive anode, Hydrogen gas at negative cathode",
              "Color changes in potato conduction test"
            ],
            "practiceSet": "Exercise 11.2",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.3",
            "name": "Electroplating Principles, Setup & Industrial Applications",
            "topicCode": "CBSE-8-CURI-11-11.3",
            "subtopics": [
              "Electroplating definition using copper sulphate electrolyte",
              "Cathode (object to be plated), Anode (pure metal plate)",
              "Chromium plating on car rims/taps, Gold/silver plating on jewellery, Tin cans, Zinc galvanisation"
            ],
            "practiceSet": "Exercise 11.3",
            "theorems": [],
            "problemSet": "Problem Set 11"
          }
        ]
      },
      {
        "number": "12",
        "name": "Some Natural Phenomena",
        "topics": [
          {
            "number": "12.1",
            "name": "Static Electricity & Charging by Friction",
            "topicCode": "CBSE-8-CURI-12-12.1",
            "subtopics": [
              "Rubbing glass rod with silk, plastic comb with hair",
              "Positive and negative charge conventions",
              "Like charges repel, unlike charges attract"
            ],
            "practiceSet": "Exercise 12.1",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.2",
            "name": "Electroscope & Transfer of Electric Charge",
            "topicCode": "CBSE-8-CURI-12-12.2",
            "subtopics": [
              "Gold-leaf electroscope construction and working",
              "Earthing / grounding definition"
            ],
            "practiceSet": "Exercise 12.2",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.3",
            "name": "Lightning: Story of Lightning, Safety & Lightning Conductors",
            "topicCode": "CBSE-8-CURI-12-12.3",
            "subtopics": [
              "Benjamin Franklin kite experiment",
              "Cloud charge accumulation and electric discharge",
              "Lightning safety outdoors and indoors",
              "Lightning conductor installation on buildings"
            ],
            "practiceSet": "Exercise 12.3",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.4",
            "name": "Earthquakes: Tectonic Plates, Seismic Waves & Richter Scale",
            "topicCode": "CBSE-8-CURI-12-12.4",
            "subtopics": [
              "Fault zones and tectonic plate boundaries",
              "Epicentre, focus, and seismic waves recorded by seismograph",
              "Richter scale logarithmic measurement",
              "Earthquake safe structural design and safety protocols"
            ],
            "practiceSet": "Exercise 12.4",
            "theorems": [],
            "problemSet": "Problem Set 12"
          }
        ]
      },
      {
        "number": "13",
        "name": "Light",
        "topics": [
          {
            "number": "13.1",
            "name": "Laws of Reflection & Normal Angle Geometry",
            "topicCode": "CBSE-8-CURI-13-13.1",
            "subtopics": [
              "Angle of incidence = Angle of reflection (∠i = ∠r)",
              "Incident ray, normal, and reflected ray lie in same plane",
              "Regular vs diffused/irregular reflection"
            ],
            "practiceSet": "Exercise 13.1",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.2",
            "name": "Image Formation by Plane Mirror & Lateral Inversion",
            "topicCode": "CBSE-8-CURI-13-13.2",
            "subtopics": [
              "Virtual, erect, same-size image at same distance behind mirror",
              "Lateral inversion (left appears right and right appears left)"
            ],
            "practiceSet": "Exercise 13.2",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.3",
            "name": "Multiple Images, Kaleidoscope & Periscope",
            "topicCode": "CBSE-8-CURI-13-13.3",
            "subtopics": [
              "Formula for number of images: n = (360/θ) - 1",
              "Kaleidoscope construction and symmetrical patterns",
              "Periscope working using two plane mirrors at 45°"
            ],
            "practiceSet": "Exercise 13.3",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.4",
            "name": "Refraction & Dispersion of Light by Glass Prism",
            "topicCode": "CBSE-8-CURI-13-13.4",
            "subtopics": [
              "Splitting of white light into 7 colors (VIBGYOR)",
              "Rainbow formation as natural dispersion"
            ],
            "practiceSet": "Exercise 13.4",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.5",
            "name": "Human Eye Anatomy, Defects (Myopia/Hypermetropia) & Care",
            "topicCode": "CBSE-8-CURI-13-13.5",
            "subtopics": [
              "Cornea, iris, pupil, eye lens, retina, rods & cones, blind spot",
              "Persistence of vision (1/16th second)",
              "Near point (25 cm) and eye hygiene",
              "Braille system for visually impaired (Louis Braille)"
            ],
            "practiceSet": "Exercise 13.5",
            "theorems": [],
            "problemSet": "Problem Set 13"
          }
        ]
      }
    ]
  },
  {
    "docId": "mh_8_mth",
    "board": "Maharashtra Board",
    "boardCode": "MH",
    "class": "8",
    "subject": "Mathematics",
    "subjectCode": "MTH",
    "chapters": [
      {
        "number": "1",
        "name": "Rational and Irrational Numbers",
        "topics": [
          {
            "number": "1.1",
            "name": "Rational Numbers & Number Line Representation",
            "topicCode": "MH-8-MTH-1-1.1",
            "subtopics": [
              "Definition of rational numbers m/n",
              "Plotting fractions and negative rational numbers on number line",
              "Equivalent fractions"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Comparison of Rational Numbers",
            "topicCode": "MH-8-MTH-1-1.2",
            "subtopics": [
              "Cross multiplication rule (a/b vs c/d)",
              "Comparing positive and negative rational numbers"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Decimal Representation of Rational Numbers",
            "topicCode": "MH-8-MTH-1-1.3",
            "subtopics": [
              "Terminating decimal form",
              "Non-terminating recurring decimal form (dot/bar notation)"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Irrational Numbers & Representation of √2 on Number Line",
            "topicCode": "MH-8-MTH-1-1.4",
            "subtopics": [
              "Definition of irrational numbers (non-terminating non-recurring)",
              "Geometric construction of √2 and √3 on number line using Pythagoras"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Parallel Lines and Transversal",
        "topics": [
          {
            "number": "2.1",
            "name": "Transversal & Angles Made by Transversal",
            "topicCode": "MH-8-MTH-2-2.1",
            "subtopics": [
              "Definition of transversal",
              "Pairs of corresponding angles",
              "Pairs of alternate interior & alternate exterior angles",
              "Pairs of interior angles"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Properties of Angles Formed by Parallel Lines & Transversal",
            "topicCode": "MH-8-MTH-2-2.2",
            "subtopics": [
              "Corresponding angles property (equal)",
              "Alternate angles property (equal)",
              "Interior angles property (supplementary = 180°)"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [
              "Interior Angles Theorem",
              "Alternate Angles Theorem"
            ],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Construction of Parallel Lines",
            "topicCode": "MH-8-MTH-2-2.3",
            "subtopics": [
              "Drawing parallel line through given point outside line using set squares",
              "Drawing parallel line at given distance using compass"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Indices and Cube Root",
        "topics": [
          {
            "number": "3.1",
            "name": "Indices Laws with Integer Exponents",
            "topicCode": "MH-8-MTH-3-3.1",
            "subtopics": [
              "Product rule a^m * a^n",
              "Quotient rule a^m / a^n",
              "Power of power (a^m)^n",
              "Zero exponent a^0 = 1",
              "Negative exponent a^(-m) = 1/a^m"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Meaning of Numbers Having Index in Rational Form (1/n)",
            "topicCode": "MH-8-MTH-3-3.2",
            "subtopics": [
              "Meaning of a^(1/n) as nth root of a",
              "Reading and writing index forms (e.g. 5th root of 32)"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Meaning of Numbers Having Index in Rational Form (m/n)",
            "topicCode": "MH-8-MTH-3-3.3",
            "subtopics": [
              "Meaning of a^(m/n) as mth power of nth root or nth root of mth power",
              "Evaluation of fractional indices"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Cube and Cube Root Calculations",
            "topicCode": "MH-8-MTH-3-3.4",
            "subtopics": [
              "Finding cube of positive and negative numbers and decimals",
              "Finding cube root by prime factorisation method"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Altitudes and Medians of a Triangle",
        "topics": [
          {
            "number": "4.1",
            "name": "Altitude of a Triangle & Orthocentre (O)",
            "topicCode": "MH-8-MTH-4-4.1",
            "subtopics": [
              "Definition of altitude",
              "Drawing altitudes in acute, right, and obtuse angled triangles",
              "Point of concurrence: Orthocentre (O) location"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Median of a Triangle & Centroid (G)",
            "topicCode": "MH-8-MTH-4-4.2",
            "subtopics": [
              "Definition of median and midpoint of side",
              "Drawing medians of a triangle",
              "Point of concurrence: Centroid (G)"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Centroid 2:1 Ratio Property & Numerical Applications",
            "topicCode": "MH-8-MTH-4-4.3",
            "subtopics": [
              "Centroid divides each median in the ratio 2:1",
              "Calculating segment lengths from centroid property"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Expansion Formulae",
        "topics": [
          {
            "number": "5.1",
            "name": "Expansion of (x + a)(x + b)",
            "topicCode": "MH-8-MTH-5-5.1",
            "subtopics": [
              "Formula: (x+a)(x+b) = x² + (a+b)x + ab",
              "Application to algebraic and numerical expansions"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Expansion of (a + b)³",
            "topicCode": "MH-8-MTH-5-5.2",
            "subtopics": [
              "Formula: (a+b)³ = a³ + 3a²b + 3ab² + b³ = a³ + b³ + 3ab(a+b)",
              "Evaluating numerical cubes (e.g. 52³)"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Expansion of (a - b)³",
            "topicCode": "MH-8-MTH-5-5.3",
            "subtopics": [
              "Formula: (a-b)³ = a³ - 3a²b + 3ab² - b³ = a³ - b³ - 3ab(a-b)",
              "Evaluating numerical cubes (e.g. 48³)"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.4",
            "name": "Expansion of (a + b + c)²",
            "topicCode": "MH-8-MTH-5-5.4",
            "subtopics": [
              "Formula: (a+b+c)² = a² + b² + c² + 2ab + 2bc + 2ca",
              "Simplification of polynomial expressions"
            ],
            "practiceSet": "Exercise 5.4",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Factorisation of Algebraic Expressions",
        "topics": [
          {
            "number": "6.1",
            "name": "Factorisation of Quadratic Trinomial (ax² + bx + c)",
            "topicCode": "MH-8-MTH-6-6.1",
            "subtopics": [
              "Finding factors by splitting middle term",
              "Sign rules in quadratic factorisation"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Factorisation of (a³ + b³)",
            "topicCode": "MH-8-MTH-6-6.2",
            "subtopics": [
              "Formula: a³ + b³ = (a + b)(a² - ab + b²)",
              "Factoring algebraic binomials"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Factorisation of (a³ - b³)",
            "topicCode": "MH-8-MTH-6-6.3",
            "subtopics": [
              "Formula: a³ - b³ = (a - b)(a² + ab + b²)",
              "Factoring algebraic expressions with differences of cubes"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.4",
            "name": "Rational Algebraic Expressions Simplification",
            "topicCode": "MH-8-MTH-6-6.4",
            "subtopics": [
              "Factorising numerator and denominator",
              "Cancelling common polynomial factors"
            ],
            "practiceSet": "Exercise 6.4",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Variation",
        "topics": [
          {
            "number": "7.1",
            "name": "Direct Variation & Constant of Variation (k)",
            "topicCode": "MH-8-MTH-7-7.1",
            "subtopics": [
              "Concept of direct proportion (x ∝ y)",
              "Equation of variation x = ky",
              "Finding constant of variation k"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Inverse Variation & Constant Product",
            "topicCode": "MH-8-MTH-7-7.2",
            "subtopics": [
              "Concept of inverse variation (x ∝ 1/y)",
              "Equation xy = k",
              "Solving missing values in tables"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Time, Work and Speed Word Problems",
            "topicCode": "MH-8-MTH-7-7.3",
            "subtopics": [
              "Man-days calculations",
              "Speed and time variations in transportation"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      },
      {
        "number": "8",
        "name": "Quadrilateral: Constructions and Types",
        "topics": [
          {
            "number": "8.1",
            "name": "Constructing Quadrilateral with Sides & Angles/Diagonals",
            "topicCode": "MH-8-MTH-8-8.1",
            "subtopics": [
              "Construction with 4 sides and 1 diagonal",
              "Construction with 3 sides and 2 diagonals",
              "Construction with adjacent sides and included angles"
            ],
            "practiceSet": "Exercise 8.1",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.2",
            "name": "Rectangle & Square Properties and Constructions",
            "topicCode": "MH-8-MTH-8-8.2",
            "subtopics": [
              "Opposite sides equal, 90° angles, equal diagonals",
              "Square construction with given side length"
            ],
            "practiceSet": "Exercise 8.2",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.3",
            "name": "Rhombus & Parallelogram Properties and Constructions",
            "topicCode": "MH-8-MTH-8-8.3",
            "subtopics": [
              "Rhombus perpendicular bisecting diagonals",
              "Parallelogram construction with adjacent sides and included angle"
            ],
            "practiceSet": "Exercise 8.3",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.4",
            "name": "Trapezium & Kite Properties",
            "topicCode": "MH-8-MTH-8-8.4",
            "subtopics": [
              "Trapezium definition and parallel sides",
              "Kite adjacent side equality and diagonal properties"
            ],
            "practiceSet": "Exercise 8.4",
            "theorems": [],
            "problemSet": "Problem Set 8"
          }
        ]
      },
      {
        "number": "9",
        "name": "Discount and Commission",
        "topics": [
          {
            "number": "9.1",
            "name": "Discount Calculation on Marked Price",
            "topicCode": "MH-8-MTH-9-9.1",
            "subtopics": [
              "Discount = Marked Price - Selling Price",
              "Discount % = (Discount / Marked Price) * 100"
            ],
            "practiceSet": "Exercise 9.1",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.2",
            "name": "Commission & Commission Agent Services",
            "topicCode": "MH-8-MTH-9-9.2",
            "subtopics": [
              "Commission definition and rate percent",
              "Income calculation of commission agents"
            ],
            "practiceSet": "Exercise 9.2",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.3",
            "name": "Rebate on Handloom and Khadi Goods",
            "topicCode": "MH-8-MTH-9-9.3",
            "subtopics": [
              "Government subsidy and rebate discounts",
              "Net amount paid by consumer"
            ],
            "practiceSet": "Exercise 9.3",
            "theorems": [],
            "problemSet": "Problem Set 9"
          }
        ]
      },
      {
        "number": "10",
        "name": "Division of Polynomials",
        "topics": [
          {
            "number": "10.1",
            "name": "Introduction to Polynomials & Degree of Polynomial",
            "topicCode": "MH-8-MTH-10-10.1",
            "subtopics": [
              "Definition of polynomial in one variable",
              "Degree of monomial and polynomial"
            ],
            "practiceSet": "Exercise 10.1",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.2",
            "name": "Dividing a Monomial by a Monomial",
            "topicCode": "MH-8-MTH-10-10.2",
            "subtopics": [
              "Exponent subtraction in variable division",
              "Coefficient division"
            ],
            "practiceSet": "Exercise 10.2",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.3",
            "name": "Dividing a Polynomial by a Monomial & Binomial",
            "topicCode": "MH-8-MTH-10-10.3",
            "subtopics": [
              "Long division algorithm for polynomials",
              "Dividend = Divisor * Quotient + Remainder"
            ],
            "practiceSet": "Exercise 10.3",
            "theorems": [],
            "problemSet": "Problem Set 10"
          }
        ]
      },
      {
        "number": "11",
        "name": "Statistics",
        "topics": [
          {
            "number": "11.1",
            "name": "Average / Arithmetic Mean of Ungrouped Data",
            "topicCode": "MH-8-MTH-11-11.1",
            "subtopics": [
              "Mean formula: X̄ = Σx / N",
              "Weighted mean calculations using frequency tables Σ(f * x) / N"
            ],
            "practiceSet": "Exercise 11.1",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.2",
            "name": "Subdivided Bar Diagram Construction",
            "topicCode": "MH-8-MTH-11-11.2",
            "subtopics": [
              "Subdividing bar heights for multiple component data",
              "Scale and labeling on graph"
            ],
            "practiceSet": "Exercise 11.2",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.3",
            "name": "Percentage Bar Diagram Construction",
            "topicCode": "MH-8-MTH-11-11.3",
            "subtopics": [
              "Converting component frequencies to percentages (100%)",
              "Constructing percentage bars and comparative analysis"
            ],
            "practiceSet": "Exercise 11.3",
            "theorems": [],
            "problemSet": "Problem Set 11"
          }
        ]
      },
      {
        "number": "12",
        "name": "Equations in One Variable",
        "topics": [
          {
            "number": "12.1",
            "name": "Solving Equations in One Variable by Transposition",
            "topicCode": "MH-8-MTH-12-12.1",
            "subtopics": [
              "Adding, subtracting, multiplying, dividing non-zero terms on both sides",
              "Solving brackets"
            ],
            "practiceSet": "Exercise 12.1",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.2",
            "name": "Word Problems on Numbers, Ages, and Currency",
            "topicCode": "MH-8-MTH-12-12.2",
            "subtopics": [
              "Formulating linear equations from given conditions",
              "Step-by-step verification of solutions"
            ],
            "practiceSet": "Exercise 12.2",
            "theorems": [],
            "problemSet": "Problem Set 12"
          }
        ]
      },
      {
        "number": "13",
        "name": "Congruence of Triangles",
        "topics": [
          {
            "number": "13.1",
            "name": "One-to-One Correspondence & Congruence Concept",
            "topicCode": "MH-8-MTH-13-13.1",
            "subtopics": [
              "Vertices correspondence (ABC ↔ PQR)",
              "Congruence of corresponding sides and angles"
            ],
            "practiceSet": "Exercise 13.1",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.2",
            "name": "Tests of Congruence: SAS, SSS, ASA, AAS & Hypotenuse-Side",
            "topicCode": "MH-8-MTH-13-13.2",
            "subtopics": [
              "Side-Angle-Side test",
              "Side-Side-Side test",
              "Angle-Side-Angle & Angle-Angle-Side tests",
              "Hypotenuse-Side test for right-angled triangles"
            ],
            "practiceSet": "Exercise 13.2",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.3",
            "name": "Writing Congruence Proofs & Remaining Congruent Parts",
            "topicCode": "MH-8-MTH-13-13.3",
            "subtopics": [
              "Proving triangles congruent by specific test",
              "Stating remaining congruent angles and sides"
            ],
            "practiceSet": "Exercise 13.3",
            "theorems": [],
            "problemSet": "Problem Set 13"
          }
        ]
      },
      {
        "number": "14",
        "name": "Compound Interest",
        "topics": [
          {
            "number": "14.1",
            "name": "Compound Interest Formula: A = P(1 + r/100)^N",
            "topicCode": "MH-8-MTH-14-14.1",
            "subtopics": [
              "Principal, Rate, Period in years",
              "Calculation of total amount A and Interest I = A - P"
            ],
            "practiceSet": "Exercise 14.1",
            "theorems": [],
            "problemSet": "Problem Set 14"
          },
          {
            "number": "14.2",
            "name": "Applications of Formula: Population Growth and Depreciation",
            "topicCode": "MH-8-MTH-14-14.2",
            "subtopics": [
              "Formula for appreciation: A = P(1 + r/100)^N",
              "Formula for depreciation / decay: A = P(1 - r/100)^N"
            ],
            "practiceSet": "Exercise 14.2",
            "theorems": [],
            "problemSet": "Problem Set 14"
          }
        ]
      },
      {
        "number": "15",
        "name": "Area",
        "topics": [
          {
            "number": "15.1",
            "name": "Area of Parallelogram: Base * Height",
            "topicCode": "MH-8-MTH-15-15.1",
            "subtopics": [
              "Formula and derivation",
              "Finding height or base when area is given"
            ],
            "practiceSet": "Exercise 15.1",
            "theorems": [],
            "problemSet": "Problem Set 15"
          },
          {
            "number": "15.2",
            "name": "Area of Rhombus: 1/2 * Product of Diagonals",
            "topicCode": "MH-8-MTH-15-15.2",
            "subtopics": [
              "Formula: 1/2 * d1 * d2",
              "Pythagoras theorem relation with rhombus sides and half diagonals"
            ],
            "practiceSet": "Exercise 15.2",
            "theorems": [],
            "problemSet": "Problem Set 15"
          },
          {
            "number": "15.3",
            "name": "Area of Trapezium: 1/2 * (Sum of Parallel Sides) * Height",
            "topicCode": "MH-8-MTH-15-15.3",
            "subtopics": [
              "Formula: 1/2 * (a + b) * h",
              "Word problems on cross-sectional canal and road areas"
            ],
            "practiceSet": "Exercise 15.3",
            "theorems": [],
            "problemSet": "Problem Set 15"
          },
          {
            "number": "15.4",
            "name": "Area of Triangle with Heron Formula",
            "topicCode": "MH-8-MTH-15-15.4",
            "subtopics": [
              "Semi-perimeter s = (a+b+c)/2",
              "Formula: A = √[s(s-a)(s-b)(s-c)]"
            ],
            "practiceSet": "Exercise 15.4",
            "theorems": [],
            "problemSet": "Problem Set 15"
          },
          {
            "number": "15.5",
            "name": "Area of Irregular Polygons and Field Plots",
            "topicCode": "MH-8-MTH-15-15.5",
            "subtopics": [
              "Dividing plots into triangles and trapeziums",
              "Summing individual region areas"
            ],
            "practiceSet": "Exercise 15.5",
            "theorems": [],
            "problemSet": "Problem Set 15"
          }
        ]
      },
      {
        "number": "16",
        "name": "Surface Area and Volume",
        "topics": [
          {
            "number": "16.1",
            "name": "Surface Area & Volume of Cuboid and Cube",
            "topicCode": "MH-8-MTH-16-16.1",
            "subtopics": [
              "Total surface area = 2(lb + bh + lh)",
              "Volume of cuboid = l * b * h",
              "TSA of cube = 6l², Volume = l³"
            ],
            "practiceSet": "Exercise 16.1",
            "theorems": [],
            "problemSet": "Problem Set 16"
          },
          {
            "number": "16.2",
            "name": "Curved Surface Area & Total Surface Area of Cylinder",
            "topicCode": "MH-8-MTH-16-16.2",
            "subtopics": [
              "Curved surface area = 2πrh",
              "Total surface area = 2πr(r + h)"
            ],
            "practiceSet": "Exercise 16.2",
            "theorems": [],
            "problemSet": "Problem Set 16"
          },
          {
            "number": "16.3",
            "name": "Volume of Cylinder & Capacity in Litres",
            "topicCode": "MH-8-MTH-16-16.3",
            "subtopics": [
              "Volume = πr²h",
              "Conversion: 1 litre = 1000 cm³, 1 m³ = 1000 litres"
            ],
            "practiceSet": "Exercise 16.3",
            "theorems": [],
            "problemSet": "Problem Set 16"
          }
        ]
      },
      {
        "number": "17",
        "name": "Circle: Chord and Arc",
        "topics": [
          {
            "number": "17.1",
            "name": "Properties of Chord of a Circle",
            "topicCode": "MH-8-MTH-17-17.1",
            "subtopics": [
              "Perpendicular drawn from centre to chord bisects chord",
              "Segment joining centre and midpoint of chord is perpendicular to chord"
            ],
            "practiceSet": "Exercise 17.1",
            "theorems": [
              "Perpendicular from centre to chord theorem"
            ],
            "problemSet": "Problem Set 17"
          },
          {
            "number": "17.2",
            "name": "Arcs of a Circle & Measure of Arc",
            "topicCode": "MH-8-MTH-17-17.2",
            "subtopics": [
              "Minor arc, Major arc, and Semicircular arc",
              "Central angle and measure of minor arc",
              "Measure of major arc = 360° - measure of minor arc"
            ],
            "practiceSet": "Exercise 17.2",
            "theorems": [],
            "problemSet": "Problem Set 17"
          },
          {
            "number": "17.3",
            "name": "Congruence of Arcs & Corresponding Chords",
            "topicCode": "MH-8-MTH-17-17.3",
            "subtopics": [
              "Arcs having equal measures and same radius are congruent",
              "Chords corresponding to congruent arcs are congruent"
            ],
            "practiceSet": "Exercise 17.3",
            "theorems": [],
            "problemSet": "Problem Set 17"
          }
        ]
      }
    ]
  },
  {
    "docId": "mh_8_sci",
    "board": "Maharashtra Board",
    "boardCode": "MH",
    "class": "8",
    "subject": "General Science",
    "subjectCode": "SCI",
    "chapters": [
      {
        "number": "1",
        "name": "Living World and Classification of Microbes",
        "topics": [
          {
            "number": "1.1",
            "name": "Five Kingdom Classification System (Robert Whittaker)",
            "topicCode": "MH-8-SCI-1-1.1",
            "subtopics": [
              "Criteria for classification: complexity of cell, body organization, mode of nutrition, life style, phylogenetic relationship",
              "Kingdom Monera, Protista, Fungi, Plantae, Animalia"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Characteristics of Kingdom Monera, Protista & Fungi",
            "topicCode": "MH-8-SCI-1-1.2",
            "subtopics": [
              "Monera: unicellular prokaryotes (Streptococcus, Clostridium)",
              "Protista: unicellular eukaryotes with pseudopodia/cilia (Amoeba, Euglena)",
              "Fungi: saprophytic eukaryotes with chitin cell wall (Aspergillus, Penicillium, Yeast)"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Classification of Microorganisms: Bacteria, Protozoa, Fungi, Algae",
            "topicCode": "MH-8-SCI-1-1.3",
            "subtopics": [
              "Size hierarchy in micrometres and nanometres",
              "Bacteria shapes (coccus, bacillus, spirillum)",
              "Protozoa free living and parasitic (Plasmodium, Entamoeba)",
              "Algae autotrophs with chloroplast (Chlorella)"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Viruses: Structure, Types & Pathogenicity",
            "topicCode": "MH-8-SCI-1-1.4",
            "subtopics": [
              "Submicroscopic size (10 to 100 nm)",
              "DNA or RNA genome surrounded by protein coat",
              "Bacteriophage and plant/animal viruses"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Health and Diseases",
        "topics": [
          {
            "number": "2.1",
            "name": "Health Definition & Types of Diseases",
            "topicCode": "MH-8-SCI-2-2.1",
            "subtopics": [
              "WHO definition of health (physical, mental, and social well-being)",
              "Chronic vs acute diseases",
              "Hereditary (Down syndrome) vs acquired diseases"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Infectious Diseases & Modes of Transmission",
            "topicCode": "MH-8-SCI-2-2.2",
            "subtopics": [
              "Tuberculosis (Mycobacterium tuberculosis, BCG vaccine)",
              "Hepatitis/Jaundice (Hepatitis virus)",
              "Dysentery, Cholera (Vibrio cholerae), Typhoid (Salmonella typhi)",
              "Transmission through air, contaminated water, food, vectors"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Present Day Diseases: Dengue, Swine Flu, Bird Flu, AIDS",
            "topicCode": "MH-8-SCI-2-2.3",
            "subtopics": [
              "Dengue (Flavivirus / Aedes aegypti vector, thrombocytopenia)",
              "Swine flu (Influenza virus H1N1)",
              "AIDS (HIV virus, ELISA test for diagnosis)"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Non-Infectious Diseases: Cancer, Diabetes & Heart Diseases",
            "topicCode": "MH-8-SCI-2-2.4",
            "subtopics": [
              "Cancer: uncontrolled cell division, biopsy, chemotherapy, radiation",
              "Diabetes: insulin deficiency from pancreas, blood sugar monitoring",
              "Heart attack: atherosclerosis, hypertension, angioplasty, bypass surgery"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.5",
            "name": "Generic Medicines & Lifestyle Diseases Prevention",
            "topicCode": "MH-8-SCI-2-2.5",
            "subtopics": [
              "Pradhan Mantri Jan Aushadhi Yojana",
              "Generic vs branded medicines",
              "First aid for heart disease (CPR - Cardio-Pulmonary Resuscitation)"
            ],
            "practiceSet": "Exercise 2.5",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Force and Pressure",
        "topics": [
          {
            "number": "3.1",
            "name": "Contact and Non-Contact Forces",
            "topicCode": "MH-8-SCI-3-3.1",
            "subtopics": [
              "Contact forces: Muscular force, mechanical force, frictional force",
              "Non-contact forces: Magnetic, electrostatic, gravitational forces"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Balanced and Unbalanced Forces & Inertia",
            "topicCode": "MH-8-SCI-3-3.2",
            "subtopics": [
              "Newton first law of motion and inertia",
              "Inertia of rest, inertia of motion, inertia of direction"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Pressure Formula (P = F/A) & Pressure on Solids",
            "topicCode": "MH-8-SCI-3-3.3",
            "subtopics": [
              "Definition of pressure and SI unit N/m² (Pascal)",
              "Effect of contact area on pressure (pins, heavy vehicle tires)"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Pressure of Liquids and Gases",
            "topicCode": "MH-8-SCI-3-3.4",
            "subtopics": [
              "Liquid pressure formula (P = hρg) and depth dependence",
              "Atmospheric pressure (1 bar = 10^5 Pa) and decrease with altitude"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.5",
            "name": "Buoyant Force & Archimedes Principle",
            "topicCode": "MH-8-SCI-3-3.5",
            "subtopics": [
              "Factors affecting buoyant force: volume of submerged object and density of liquid",
              "Archimedes principle statement and applications",
              "Law of flotation and relative density (hydrometer, lactometer)"
            ],
            "practiceSet": "Exercise 3.5",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Current Electricity and Magnetism",
        "topics": [
          {
            "number": "4.1",
            "name": "Current Electricity & Electrostatic Potential",
            "topicCode": "MH-8-SCI-4-4.1",
            "subtopics": [
              "Flow of electrons in conductors",
              "Electric potential definition and potential difference (V)",
              "Unit of potential difference (Volt) and electric current (Ampere)"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Dry Cell, Lead-Acid Cell & Ni-Cd Cells",
            "topicCode": "MH-8-SCI-4-4.2",
            "subtopics": [
              "Dry cell construction: zinc container cathode, carbon rod anode, ammonium chloride & manganese dioxide paste",
              "Lead-acid cell: Pb and PbO2 electrodes in dilute H2SO4 (rechargeable)",
              "Ni-Cd cells and lithium-ion cells"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Electric Circuit Components & Symbols",
            "topicCode": "MH-8-SCI-4-4.3",
            "subtopics": [
              "Connecting wires, battery, plug key, bulb, ammeter, voltmeter"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.4",
            "name": "Magnetic Effect of Electric Current (Hans Christian Oersted)",
            "topicCode": "MH-8-SCI-4-4.4",
            "subtopics": [
              "Deflection of magnetic needle around current carrying conductor",
              "Right hand thumb rule basics"
            ],
            "practiceSet": "Exercise 4.4",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.5",
            "name": "Electromagnet Construction & Electric Bell Working",
            "topicCode": "MH-8-SCI-4-4.5",
            "subtopics": [
              "Winding insulated copper wire around iron nail",
              "Electric bell circuit, striker, gong, and contact screw mechanism"
            ],
            "practiceSet": "Exercise 4.5",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Inside the Atom",
        "topics": [
          {
            "number": "5.1",
            "name": "Dalton Atomic Theory & Thomson Plum Pudding Model",
            "topicCode": "MH-8-SCI-5-5.1",
            "subtopics": [
              "Dalton: hard indivisible spheres",
              "Thomson: positively charged sphere with embedded negatively charged electrons (cathode ray discovery)"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Rutherford Gold Foil Experiment & Nuclear Model of Atom",
            "topicCode": "MH-8-SCI-5-5.2",
            "subtopics": [
              "Alpha particle scattering experiment",
              "Positively charged dense central nucleus, empty space around nucleus, planetary electrons",
              "Drawbacks of Rutherford model (stability of orbital electrons)"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Bohr Stable Orbit Atomic Model",
            "topicCode": "MH-8-SCI-5-5.3",
            "subtopics": [
              "Electrons revolve in discrete stable circular orbits (K, L, M, N shells)",
              "Energy emission and absorption during quantum electron jumps"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.4",
            "name": "Subatomic Particles: Protons (p), Neutrons (n), Electrons (e)",
            "topicCode": "MH-8-SCI-5-5.4",
            "subtopics": [
              "Proton: positive charge in nucleus (1.6 * 10^-19 C)",
              "Neutron: electrically neutral particle (James Chadwick, 1932)",
              "Electron: negatively charged particle with negligible mass (1/1837 of H atom)"
            ],
            "practiceSet": "Exercise 5.4",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.5",
            "name": "Atomic Number (Z), Mass Number (A) & Electronic Configuration",
            "topicCode": "MH-8-SCI-5-5.5",
            "subtopics": [
              "Atomic number Z = number of protons = number of electrons",
              "Mass number A = protons + neutrons",
              "Shell capacity formula 2n² (K=2, L=8, M=18, N=32)",
              "Valence electrons and valency determination"
            ],
            "practiceSet": "Exercise 5.5",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.6",
            "name": "Isotopes & Uses of Radioactive Isotopes",
            "topicCode": "MH-8-SCI-5-5.6",
            "subtopics": [
              "Definition: same atomic number Z, different mass number A (e.g. C-12, C-14; H-1, H-2, H-3)",
              "Uses: Uranium-235 in nuclear reactors, Cobalt-60 in cancer therapy, Iodine-131 in goitre, Carbon-14 dating"
            ],
            "practiceSet": "Exercise 5.6",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Composition of Matter",
        "topics": [
          {
            "number": "6.1",
            "name": "States of Matter: Solid, Liquid, Gas (Intermolecular Forces)",
            "topicCode": "MH-8-SCI-6-6.1",
            "subtopics": [
              "Intermolecular forces of attraction and particle spacing",
              "Definite shape, volume, rigidity, fluidity, compressibility comparison"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Elements, Compounds and Mixtures",
            "topicCode": "MH-8-SCI-6-6.2",
            "subtopics": [
              "Element: purest substance consisting of single type of atom",
              "Compound: chemical combination of elements in fixed proportion by weight",
              "Mixture: physical combination of substances in any proportion"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Types of Mixtures: Homogeneous vs Heterogeneous",
            "topicCode": "MH-8-SCI-6-6.3",
            "subtopics": [
              "Homogeneous mixture: uniform composition throughout (solutions)",
              "Heterogeneous mixture: non-uniform composition (suspensions, colloids)"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.4",
            "name": "Solutions, Suspensions and Colloids (Tyndall Effect)",
            "topicCode": "MH-8-SCI-6-6.4",
            "subtopics": [
              "Solution: solute and solvent, true solution particle size < 1 nm",
              "Suspension: heterogeneous mixture particle size > 1000 nm, settles on standing",
              "Colloid: particle size 1 to 1000 nm, Tyndall scattering of light (milk, ink, smoke)"
            ],
            "practiceSet": "Exercise 6.4",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.5",
            "name": "Molecular Formula & Valency (Cross-Over Method)",
            "topicCode": "MH-8-SCI-6-6.5",
            "subtopics": [
              "Writing chemical formulae using constituent elements and valency cross-over technique"
            ],
            "practiceSet": "Exercise 6.5",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Metals and Non-metals",
        "topics": [
          {
            "number": "7.1",
            "name": "Physical Properties of Metals",
            "topicCode": "MH-8-SCI-7-7.1",
            "subtopics": [
              "Lustre, hardness, malleability, ductility, conduction of heat and electricity, sonority, high density and melting points",
              "Exceptions: Mercury and Gallium (liquids), Sodium and Potassium (soft, low density)"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Physical Properties of Non-metals",
            "topicCode": "MH-8-SCI-7-7.2",
            "subtopics": [
              "Non-lustrous, brittle, poor conductors of heat and electricity",
              "Exceptions: Diamond (hardest substance, good heat conductor), Graphite (good electric conductor), Iodine (lustrous)"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Chemical Properties of Metals (Oxides, Water, Acids)",
            "topicCode": "MH-8-SCI-7-7.3",
            "subtopics": [
              "Reaction with oxygen: basic metal oxides",
              "Reaction with water: metal hydroxides and hydrogen gas",
              "Reaction with dilute acids: salt and hydrogen gas evolution"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.4",
            "name": "Chemical Properties of Non-metals (Oxides, Water, Acids)",
            "topicCode": "MH-8-SCI-7-7.4",
            "subtopics": [
              "Reaction with oxygen: acidic or neutral non-metal oxides (CO2, SO2)",
              "Non-metals generally do not react with dilute acids"
            ],
            "practiceSet": "Exercise 7.4",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.5",
            "name": "Uses of Metals/Non-metals, Noble Metals, Corrosion & Alloys",
            "topicCode": "MH-8-SCI-7-7.5",
            "subtopics": [
              "Noble metals: Gold, Silver, Platinum, Palladium and purity in Carats (24K, 22K)",
              "Corrosion: Rusting of iron, green patina on copper, tarnishing of silver",
              "Alloys: Brass (Cu+Zn), Bronze (Cu+Sn), Stainless Steel (Fe+C+Cr+Ni)"
            ],
            "practiceSet": "Exercise 7.5",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      },
      {
        "number": "8",
        "name": "Pollution",
        "topics": [
          {
            "number": "8.1",
            "name": "Pollution & Pollutants (Natural vs Man-made)",
            "topicCode": "MH-8-SCI-8-8.1",
            "subtopics": [
              "Definition of pollution and degradable vs non-degradable pollutants"
            ],
            "practiceSet": "Exercise 8.1",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.2",
            "name": "Air Pollution: Causes, Pollutants & Effects",
            "topicCode": "MH-8-SCI-8-8.2",
            "subtopics": [
              "Pollutants: SO2, CO, NO, particulate matter (PM), lead compounds",
              "Acid rain (formation of H2SO4 and HNO3) and corrosion of historical monuments (Taj Mahal)",
              "Greenhouse effect and global warming"
            ],
            "practiceSet": "Exercise 8.2",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.3",
            "name": "Water Pollution: Biological, Inorganic & Organic Pollutants",
            "topicCode": "MH-8-SCI-8-8.3",
            "subtopics": [
              "Domestic sewage, industrial effluents, agricultural pesticides and fertilisers",
              "Eutrophication and depletion of dissolved oxygen (BOD)",
              "Water-borne diseases (Typhoid, Jaundice, Amoebiasis)"
            ],
            "practiceSet": "Exercise 8.3",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.4",
            "name": "Soil Pollution: Causes & Preventive Measures",
            "topicCode": "MH-8-SCI-8-8.4",
            "subtopics": [
              "Chemical fertilisers, plastic waste, radioactive fallout, saline soil",
              "Solid waste management and organic farming methods"
            ],
            "practiceSet": "Exercise 8.4",
            "theorems": [],
            "problemSet": "Problem Set 8"
          }
        ]
      },
      {
        "number": "9",
        "name": "Disaster Management",
        "topics": [
          {
            "number": "9.1",
            "name": "Earthquakes: Causes, Effects & Seismometer",
            "topicCode": "MH-8-SCI-9-9.1",
            "subtopics": [
              "Underground tectonic plate stress release",
              "Seismometer and Richter scale measurement",
              "Precautionary measures during earthquake"
            ],
            "practiceSet": "Exercise 9.1",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.2",
            "name": "Fire: Types of Fire (Class A, B, C, D, E) & Fire Extinguishers",
            "topicCode": "MH-8-SCI-9-9.2",
            "subtopics": [
              "Class A (solid fires - wood, paper)",
              "Class B (liquid fires - petrol, kerosene)",
              "Class C (gas fires - LPG, methane)",
              "Class D (combustible metal fires - Na, Mg)",
              "Class E (electrical fires)",
              "Fire extinguishers: CO2, dry powder, foam"
            ],
            "practiceSet": "Exercise 9.2",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.3",
            "name": "Landslides / Rifts: Causes, Effects & Disaster Management Authority",
            "topicCode": "MH-8-SCI-9-9.3",
            "subtopics": [
              "Heavy rainfall, deforestation, excavation on mountain slopes",
              "Malin landslide case study in Maharashtra",
              "Disaster rescue techniques and first aid mock drills"
            ],
            "practiceSet": "Exercise 9.3",
            "theorems": [],
            "problemSet": "Problem Set 9"
          }
        ]
      },
      {
        "number": "10",
        "name": "Cell and Cell Organelles",
        "topics": [
          {
            "number": "10.1",
            "name": "Cell Structure & Plant vs Animal Cell Comparison",
            "topicCode": "MH-8-SCI-10-10.1",
            "subtopics": [
              "Cell wall (cellulose in plant cells)",
              "Plasma membrane: selectively permeable fluid-mosaic structure",
              "Cytoplasm and cytosol"
            ],
            "practiceSet": "Exercise 10.1",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.2",
            "name": "Nucleus & Endoplasmic Reticulum (Rough & Smooth)",
            "topicCode": "MH-8-SCI-10-10.2",
            "subtopics": [
              "Nucleus: nuclear membrane, nucleolus, chromatin network, genetic control",
              "Endoplasmic Reticulum: RER with ribosomes (protein synthesis) and SER (lipid synthesis)"
            ],
            "practiceSet": "Exercise 10.2",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.3",
            "name": "Golgi Complex & Lysosomes (Suicide Bags)",
            "topicCode": "MH-8-SCI-10-10.3",
            "subtopics": [
              "Golgi complex: cisternae, packaging and secretory organelle (Camillo Golgi)",
              "Lysosomes: digestive hydrolytic enzymes, autolysis (suicide bags)"
            ],
            "practiceSet": "Exercise 10.3",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.4",
            "name": "Mitochondria (Powerhouse of the Cell) & Plastids",
            "topicCode": "MH-8-SCI-10-10.4",
            "subtopics": [
              "Mitochondria: double membrane, cristae, matrix, ATP synthesis",
              "Plastids: Chloroplasts (photosynthesis), Chromoplasts (colored pigments), Leucoplasts (storage)"
            ],
            "practiceSet": "Exercise 10.4",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.5",
            "name": "Vacuoles & Cell Osmoregulation",
            "topicCode": "MH-8-SCI-10-10.5",
            "subtopics": [
              "Single membrane tonoplast in plant cell",
              "Storage of water, sap, excretory substances"
            ],
            "practiceSet": "Exercise 10.5",
            "theorems": [],
            "problemSet": "Problem Set 10"
          }
        ]
      },
      {
        "number": "11",
        "name": "Human Body and Organ System",
        "topics": [
          {
            "number": "11.1",
            "name": "Human Respiratory System Anatomy & Mechanism",
            "topicCode": "MH-8-SCI-11-11.1",
            "subtopics": [
              "Nose, pharynx, larynx (sound box), trachea (windpipe), bronchi, bronchioles, alveoli",
              "Mechanism of breathing: Diaphragm and intercostal muscle movement"
            ],
            "practiceSet": "Exercise 11.1",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.2",
            "name": "Gas Exchange in Alveoli & Cellular Respiration",
            "topicCode": "MH-8-SCI-11-11.2",
            "subtopics": [
              "Diffusion of oxygen and carbon dioxide across alveolar-capillary membrane",
              "Aerobic breakdown of glucose to generate ATP"
            ],
            "practiceSet": "Exercise 11.2",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.3",
            "name": "Human Circulatory System: Heart Anatomy & Pumping Cycle",
            "topicCode": "MH-8-SCI-11-11.3",
            "subtopics": [
              "Four chambers: Right and left atria, right and left ventricles",
              "Pericardium membrane, valves (tricuspid, bicuspid/mitral, semilunar)",
              "Systole and diastole pumping cycle"
            ],
            "practiceSet": "Exercise 11.3",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.4",
            "name": "Blood Vessels: Arteries, Veins and Capillaries",
            "topicCode": "MH-8-SCI-11-11.4",
            "subtopics": [
              "Arteries: thick muscular walls, high pressure, no valves, carry oxygenated blood (except pulmonary artery)",
              "Veins: thin walls, valves present, carry deoxygenated blood (except pulmonary vein)",
              "Capillaries: single-cell thick endothelial layer for nutrient and gas exchange"
            ],
            "practiceSet": "Exercise 11.4",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.5",
            "name": "Blood Composition, Blood Groups (ABO & Rh) & Blood Pressure",
            "topicCode": "MH-8-SCI-11-11.5",
            "subtopics": [
              "Plasma (55%) and formed elements (RBCs with hemoglobin, WBCs, platelets)",
              "ABO blood groups (Karl Landsteiner) and Universal donor (O-) / recipient (AB+)",
              "Sphygmomanometer blood pressure measurement (Normal 120/80 mmHg)"
            ],
            "practiceSet": "Exercise 11.5",
            "theorems": [],
            "problemSet": "Problem Set 11"
          }
        ]
      },
      {
        "number": "12",
        "name": "Introduction to Acid and Base",
        "topics": [
          {
            "number": "12.1",
            "name": "Acids: Definition, Natural vs Mineral Acids & Properties",
            "topicCode": "MH-8-SCI-12-12.1",
            "subtopics": [
              "Sour taste, produces H+ ions in aqueous solution, turns blue litmus red",
              "Natural organic acids (citric acid in lemon, tartaric acid in tamarind, lactic acid in curd, acetic acid in vinegar)",
              "Mineral acids (HCl, H2SO4, HNO3)"
            ],
            "practiceSet": "Exercise 12.1",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.2",
            "name": "Bases / Alkalis: Properties & Uses",
            "topicCode": "MH-8-SCI-12-12.2",
            "subtopics": [
              "Bitter taste, soapy touch, produces OH- ions in water, turns red litmus blue",
              "Common bases: NaOH, KOH, Ca(OH)2 (slaked lime), Mg(OH)2 (antacid)"
            ],
            "practiceSet": "Exercise 12.2",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.3",
            "name": "Indicators: Natural & Synthetic (Litmus, Phenolphthalein, Methyl Orange)",
            "topicCode": "MH-8-SCI-12-12.3",
            "subtopics": [
              "Natural indicators: Litmus (lichen extract), turmeric paper, red cabbage juice",
              "Synthetic indicators: Phenolphthalein (colorless in acid, pink in base), Methyl orange (pink in acid, yellow in base)"
            ],
            "practiceSet": "Exercise 12.3",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.4",
            "name": "Neutralisation Reaction & Industrial Applications",
            "topicCode": "MH-8-SCI-12-12.4",
            "subtopics": [
              "Acid + Base → Salt + Water (HCl + NaOH → NaCl + H2O)",
              "Antacids for hyperacidity, lime application to acidic agricultural soil, treating alkaline industrial waste"
            ],
            "practiceSet": "Exercise 12.4",
            "theorems": [],
            "problemSet": "Problem Set 12"
          }
        ]
      },
      {
        "number": "13",
        "name": "Chemical Change and Chemical Bond",
        "topics": [
          {
            "number": "13.1",
            "name": "Physical vs Chemical Changes & Indicators of Chemical Reaction",
            "topicCode": "MH-8-SCI-13-13.1",
            "subtopics": [
              "Reversible vs irreversible transformations",
              "Change in color, evolution of gas, temperature change, precipitate formation"
            ],
            "practiceSet": "Exercise 13.1",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.2",
            "name": "Natural Chemical Changes (Respiration, Photosynthesis, Rusting)",
            "topicCode": "MH-8-SCI-13-13.2",
            "subtopics": [
              "Photosynthesis: 6CO2 + 6H2O → C6H12O6 + 6O2",
              "Respiration: C6H12O6 + 6O2 → 6CO2 + 6H2O + Energy",
              "Rusting of iron in moist air"
            ],
            "practiceSet": "Exercise 13.2",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.3",
            "name": "Man-Made Chemical Changes (Combustion, Effervescence, Bleaching)",
            "topicCode": "MH-8-SCI-13-13.3",
            "subtopics": [
              "Combustion of fuels",
              "Cleaning tiles with hydrochloric acid",
              "Softening hard water"
            ],
            "practiceSet": "Exercise 13.3",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.4",
            "name": "Chemical Bonds: Ionic (Electrovalent) Bond Formation",
            "topicCode": "MH-8-SCI-13-13.4",
            "subtopics": [
              "Transfer of electrons from metal to non-metal to achieve stable octet",
              "Formation of NaCl (Na+ and Cl-), MgCl2, CaO"
            ],
            "practiceSet": "Exercise 13.4",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.5",
            "name": "Covalent Bond Formation (Single, Double & Triple Bonds)",
            "topicCode": "MH-8-SCI-13-13.5",
            "subtopics": [
              "Sharing of electron pairs between non-metallic atoms",
              "Formation of H2, Cl2 (single bond), O2 (double bond), N2 (triple bond), H2O, CH4"
            ],
            "practiceSet": "Exercise 13.5",
            "theorems": [],
            "problemSet": "Problem Set 13"
          }
        ]
      },
      {
        "number": "14",
        "name": "Measurement and Effects of Heat",
        "topics": [
          {
            "number": "14.1",
            "name": "Heat vs Temperature & Kinetic Theory of Heat",
            "topicCode": "MH-8-SCI-14-14.1",
            "subtopics": [
              "Heat as form of total kinetic energy (Joules / Calories)",
              "Temperature as average kinetic energy of molecules (Degree Celsius, Kelvin, Fahrenheit)"
            ],
            "practiceSet": "Exercise 14.1",
            "theorems": [],
            "problemSet": "Problem Set 14"
          },
          {
            "number": "14.2",
            "name": "Thermometer Types (Clinical, Laboratory, Maximum-Minimum)",
            "topicCode": "MH-8-SCI-14-14.2",
            "subtopics": [
              "Mercury and alcohol thermometers",
              "Clinical thermometer range (35°C to 42°C) with constriction kink",
              "Digital and infrared thermometers"
            ],
            "practiceSet": "Exercise 14.2",
            "theorems": [],
            "problemSet": "Problem Set 14"
          },
          {
            "number": "14.3",
            "name": "Specific Heat Capacity & Calorimeter",
            "topicCode": "MH-8-SCI-14-14.3",
            "subtopics": [
              "Specific heat definition (c)",
              "Heat absorbed or lost formula: Q = m * c * ΔT",
              "Principle of heat exchange in copper calorimeter"
            ],
            "practiceSet": "Exercise 14.3",
            "theorems": [],
            "problemSet": "Problem Set 14"
          },
          {
            "number": "14.4",
            "name": "Thermal Expansion of Solids (Linear, Areal, Volumetric)",
            "topicCode": "MH-8-SCI-14-14.4",
            "subtopics": [
              "Linear expansion coefficient (λ): Δl = l1 * λ * ΔT",
              "Superficial / areal expansion (β) and cubical / volumetric expansion (γ)",
              "Gaps in railway tracks and bi-metallic strips"
            ],
            "practiceSet": "Exercise 14.4",
            "theorems": [],
            "problemSet": "Problem Set 14"
          },
          {
            "number": "14.5",
            "name": "Thermal Expansion of Liquids and Gases",
            "topicCode": "MH-8-SCI-14-14.5",
            "subtopics": [
              "Apparent vs real expansion of liquids",
              "Expansion of gases under constant pressure"
            ],
            "practiceSet": "Exercise 14.5",
            "theorems": [],
            "problemSet": "Problem Set 14"
          }
        ]
      },
      {
        "number": "15",
        "name": "Sound",
        "topics": [
          {
            "number": "15.1",
            "name": "Production & Propagation of Sound (Compressions & Rarefactions)",
            "topicCode": "MH-8-SCI-15-15.1",
            "subtopics": [
              "Vibration of tuning fork prongs",
              "Longitudinal sound waves: high pressure compressions and low pressure rarefactions"
            ],
            "practiceSet": "Exercise 15.1",
            "theorems": [],
            "problemSet": "Problem Set 15"
          },
          {
            "number": "15.2",
            "name": "Frequency, Wavelength & Velocity of Sound (v = ν * λ)",
            "topicCode": "MH-8-SCI-15-15.2",
            "subtopics": [
              "Frequency (Hz), Wavelength (λ in metres), Amplitude, Time period (T)",
              "Wave equation: Velocity = Frequency * Wavelength"
            ],
            "practiceSet": "Exercise 15.2",
            "theorems": [],
            "problemSet": "Problem Set 15"
          },
          {
            "number": "15.3",
            "name": "Human Vocal Cords & Sound Generation",
            "topicCode": "MH-8-SCI-15-15.3",
            "subtopics": [
              "Larynx structure, vocal cord tension adjustment during speech and singing"
            ],
            "practiceSet": "Exercise 15.3",
            "theorems": [],
            "problemSet": "Problem Set 15"
          },
          {
            "number": "15.4",
            "name": "Human Ear Structure & Auditory Pathway",
            "topicCode": "MH-8-SCI-15-15.4",
            "subtopics": [
              "Pinna, auditory canal, tympanic membrane, malleus, incus, stapes bones, cochlea, auditory nerve"
            ],
            "practiceSet": "Exercise 15.4",
            "theorems": [],
            "problemSet": "Problem Set 15"
          },
          {
            "number": "15.5",
            "name": "Noise Pollution, Decibel Scale & Protective Measures",
            "topicCode": "MH-8-SCI-15-15.5",
            "subtopics": [
              "Threshold of hearing (0 dB), Normal conversation (60 dB), Noise threshold (>80 dB)",
              "Acoustic insulation, tree plantation, silencers in machinery"
            ],
            "practiceSet": "Exercise 15.5",
            "theorems": [],
            "problemSet": "Problem Set 15"
          }
        ]
      },
      {
        "number": "16",
        "name": "Reflection of Light",
        "topics": [
          {
            "number": "16.1",
            "name": "Laws of Reflection of Light",
            "topicCode": "MH-8-SCI-16-16.1",
            "subtopics": [
              "Incident ray, reflected ray, normal to reflecting surface",
              "Angle of incidence (i) = Angle of reflection (r)",
              "Coplanar property of rays"
            ],
            "practiceSet": "Exercise 16.1",
            "theorems": [],
            "problemSet": "Problem Set 16"
          },
          {
            "number": "16.2",
            "name": "Regular vs Irregular (Diffused) Reflection",
            "topicCode": "MH-8-SCI-16-16.2",
            "subtopics": [
              "Parallel incident rays on smooth vs rough surfaces",
              "Visibility of non-luminous objects"
            ],
            "practiceSet": "Exercise 16.2",
            "theorems": [],
            "problemSet": "Problem Set 16"
          },
          {
            "number": "16.3",
            "name": "Reflection of Reflected Light & Periscope",
            "topicCode": "MH-8-SCI-16-16.3",
            "subtopics": [
              "Successive reflections from two parallel or inclined mirrors",
              "Periscope construction and applications in submarines"
            ],
            "practiceSet": "Exercise 16.3",
            "theorems": [],
            "problemSet": "Problem Set 16"
          },
          {
            "number": "16.4",
            "name": "Multiple Images & Kaleidoscope",
            "topicCode": "MH-8-SCI-16-16.4",
            "subtopics": [
              "Formula for number of images: n = (360° / A) - 1",
              "Kaleidoscope three rectangular mirror strips at 60°"
            ],
            "practiceSet": "Exercise 16.4",
            "theorems": [],
            "problemSet": "Problem Set 16"
          },
          {
            "number": "16.5",
            "name": "Sunlight: White Light Dispersion & Rainbow Formation",
            "topicCode": "MH-8-SCI-16-16.5",
            "subtopics": [
              "Newton disc experiment",
              "Seven spectrum colors (VIBGYOR)"
            ],
            "practiceSet": "Exercise 16.5",
            "theorems": [],
            "problemSet": "Problem Set 16"
          }
        ]
      },
      {
        "number": "17",
        "name": "Man Made Materials",
        "topics": [
          {
            "number": "17.1",
            "name": "Plastic: Types (Thermoplastics vs Thermosetting Plastics)",
            "topicCode": "MH-8-SCI-17-17.1",
            "subtopics": [
              "Thermoplastics: reshaped on heating (Polythene, PVC, Polystyrene)",
              "Thermosetting plastics: permanently hardened on heating (Bakelite, Melamine, Formica)"
            ],
            "practiceSet": "Exercise 17.1",
            "theorems": [],
            "problemSet": "Problem Set 17"
          },
          {
            "number": "17.2",
            "name": "Plastic and Environment: 4R Principle",
            "topicCode": "MH-8-SCI-17-17.2",
            "subtopics": [
              "Non-biodegradable pollution hazard",
              "4R Principle: Reduce, Reuse, Recycle, Recover"
            ],
            "practiceSet": "Exercise 17.2",
            "theorems": [],
            "problemSet": "Problem Set 17"
          },
          {
            "number": "17.3",
            "name": "Thermocol (Polystyrene) Properties and Hazards",
            "topicCode": "MH-8-SCI-17-17.3",
            "subtopics": [
              "Thermal insulation and shock absorption packaging uses",
              "Carcinogenic styrene vapors on burning, disposal issues"
            ],
            "practiceSet": "Exercise 17.3",
            "theorems": [],
            "problemSet": "Problem Set 17"
          },
          {
            "number": "17.4",
            "name": "Glass: Composition, Types and Manufacturing",
            "topicCode": "MH-8-SCI-17-17.4",
            "subtopics": [
              "Raw materials: Silica (SiO2), soda, limestone",
              "Types: Soda-lime glass, Borosilicate (Pyrex) glass, Silica glass, Optical glass, Colored glass, Toughened / safety glass"
            ],
            "practiceSet": "Exercise 17.4",
            "theorems": [],
            "problemSet": "Problem Set 17"
          }
        ]
      },
      {
        "number": "18",
        "name": "Ecosystems",
        "topics": [
          {
            "number": "18.1",
            "name": "Structure of Ecosystem: Biotic and Abiotic Factors",
            "topicCode": "MH-8-SCI-18-18.1",
            "subtopics": [
              "Abiotic factors: Air, water, soil, sunlight, temperature, minerals",
              "Biotic factors: Producers (autotrophs), Consumers (herbivores, carnivores, omnivores), Decomposers (bacteria, fungi)"
            ],
            "practiceSet": "Exercise 18.1",
            "theorems": [],
            "problemSet": "Problem Set 18"
          },
          {
            "number": "18.2",
            "name": "Types of Ecosystems: Terrestrial & Aquatic",
            "topicCode": "MH-8-SCI-18-18.2",
            "subtopics": [
              "Terrestrial ecosystems: Forest, grassland, evergreen, desert ecosystems",
              "Aquatic ecosystems: Freshwater (river, pond, lake) and Marine (ocean, estuary) ecosystems"
            ],
            "practiceSet": "Exercise 18.2",
            "theorems": [],
            "problemSet": "Problem Set 18"
          },
          {
            "number": "18.3",
            "name": "Biomes & Ecosystem Degradation Due to Human Activities",
            "topicCode": "MH-8-SCI-18-18.3",
            "subtopics": [
              "Global biomes distribution",
              "Dam construction, deforestation, urbanization, industrialization impact",
              "Ecosystem conservation initiatives"
            ],
            "practiceSet": "Exercise 18.3",
            "theorems": [],
            "problemSet": "Problem Set 18"
          }
        ]
      },
      {
        "number": "19",
        "name": "Life Cycle of Stars",
        "topics": [
          {
            "number": "19.1",
            "name": "Properties of the Sun and Stars",
            "topicCode": "MH-8-SCI-19-19.1",
            "subtopics": [
              "Composition (Hydrogen, Helium), Mass, Radius, Surface temperature",
              "Units: Light year, Astronomical Unit (AU)"
            ],
            "practiceSet": "Exercise 19.1",
            "theorems": [],
            "problemSet": "Problem Set 19"
          },
          {
            "number": "19.2",
            "name": "Birth of Stars: Interstellar Clouds & Protostars",
            "topicCode": "MH-8-SCI-19-19.2",
            "subtopics": [
              "Gravitational contraction of hydrogen and dust clouds",
              "Nuclear fusion trigger (4 Hydrogen → 1 Helium + Energy)"
            ],
            "practiceSet": "Exercise 19.2",
            "theorems": [],
            "problemSet": "Problem Set 19"
          },
          {
            "number": "19.3",
            "name": "Evolution of Stars (Low Mass vs High Mass Stars)",
            "topicCode": "MH-8-SCI-19-19.3",
            "subtopics": [
              "Main sequence equilibrium (Gas pressure vs Gravity)",
              "Red giant stage expansion"
            ],
            "practiceSet": "Exercise 19.3",
            "theorems": [],
            "problemSet": "Problem Set 19"
          },
          {
            "number": "19.4",
            "name": "End Stages of Stars: White Dwarf, Neutron Star & Black Hole",
            "topicCode": "MH-8-SCI-19-19.4",
            "subtopics": [
              "Chandrasekhar Limit (1.4 Solar Masses)",
              "Low mass stars end as White Dwarf and Planetary Nebula",
              "Massive stars undergo Supernova explosion ending as Neutron Star or Black Hole"
            ],
            "practiceSet": "Exercise 19.4",
            "theorems": [],
            "problemSet": "Problem Set 19"
          }
        ]
      }
    ]
  },
  {
    "docId": "cbse_9_mgm",
    "board": "CBSE",
    "boardCode": "CBSE",
    "class": "9",
    "subject": "Mathematics (Ganita Manjari)",
    "subjectCode": "MGM",
    "chapters": [
      {
        "number": "1",
        "name": "Number Systems",
        "topics": [
          {
            "number": "1.1",
            "name": "Real Numbers: Rational Numbers & Decimal Expansions",
            "topicCode": "CBSE-9-MGM-1-1.1",
            "subtopics": [
              "Definition of rational numbers p/q (q != 0)",
              "Terminating vs non-terminating recurring decimals",
              "Converting 0.p̄ and 0.pq̄ to p/q fraction form"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Irrational Numbers & Geometric Construction on Number Line",
            "topicCode": "CBSE-9-MGM-1-1.2",
            "subtopics": [
              "Definition of irrational numbers (non-terminating non-repeating)",
              "Constructing √2, √3, √5 on number line using Pythagoras spiral method",
              "Locating √x geometrically for any positive real number x"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Operations on Real Numbers & Rationalisation of Surds",
            "topicCode": "CBSE-9-MGM-1-1.3",
            "subtopics": [
              "Properties of addition, subtraction, multiplication, division of irrationals",
              "Rationalising monomial and binomial denominators using conjugate surds (1/(a + √b))"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Laws of Exponents for Real Numbers",
            "topicCode": "CBSE-9-MGM-1-1.4",
            "subtopics": [
              "Fractional exponents a^(p/q)",
              "Laws: a^p * a^q = a^(p+q), (a^p)^q = a^(pq), a^p / a^q = a^(p-q), a^p * b^p = (ab)^p"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Polynomials",
        "topics": [
          {
            "number": "2.1",
            "name": "Polynomials in One Variable, Degree & Classification",
            "topicCode": "CBSE-9-MGM-2-2.1",
            "subtopics": [
              "Terms, coefficients, degree of polynomial",
              "Monomials, binomials, trinomials",
              "Linear, quadratic, cubic, zero polynomials"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Zeroes of a Polynomial & Geometric Meaning",
            "topicCode": "CBSE-9-MGM-2-2.2",
            "subtopics": [
              "Evaluating p(k) for given value k",
              "Finding zeroes of linear and quadratic polynomials algebraically"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Remainder Theorem & Long Division Algorithm",
            "topicCode": "CBSE-9-MGM-2-2.3",
            "subtopics": [
              "Statement: If p(x) is divided by (x - a), remainder is p(a)",
              "Verifying polynomial division by long division method"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [
              "Remainder Theorem"
            ],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Factor Theorem & Splitting Middle Term for Quadratics",
            "topicCode": "CBSE-9-MGM-2-2.4",
            "subtopics": [
              "Statement: (x - a) is a factor of p(x) if and only if p(a) = 0",
              "Factoring quadratic trinomials ax² + bx + c",
              "Factoring cubic polynomials using trial and factor theorem"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [
              "Factor Theorem"
            ],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.5",
            "name": "Algebraic Identities (Squares, Cubes & Three Variables)",
            "topicCode": "CBSE-9-MGM-2-2.5",
            "subtopics": [
              "(x + y + z)² = x² + y² + z² + 2xy + 2yz + 2zx",
              "(x ± y)³ = x³ ± y³ ± 3xy(x ± y)",
              "x³ + y³ + z³ - 3xyz = (x + y + z)(x² + y² + z² - xy - yz - zx)",
              "Conditional identity: If x + y + z = 0, then x³ + y³ + z³ = 3xyz"
            ],
            "practiceSet": "Exercise 2.5",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Coordinate Geometry",
        "topics": [
          {
            "number": "3.1",
            "name": "Cartesian Coordinate Plane, Axes & Quadrants",
            "topicCode": "CBSE-9-MGM-3-3.1",
            "subtopics": [
              "X-axis (abscissa) and Y-axis (ordinate)",
              "Origin (0,0)",
              "Four quadrants (I: +,+, II: -,+, III: -,-, IV: +,-)"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Plotting Points & Reading Coordinates on Graph",
            "topicCode": "CBSE-9-MGM-3-3.2",
            "subtopics": [
              "Plotting points (x, y) with positive and negative coordinates",
              "Points lying on axes (x, 0) and (0, y)"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Linear Equations in Two Variables",
        "topics": [
          {
            "number": "4.1",
            "name": "Linear Equation Standard Form: ax + by + c = 0",
            "topicCode": "CBSE-9-MGM-4-4.1",
            "subtopics": [
              "Identifying coefficients a, b, c",
              "Expressing word statements as linear equations in two variables"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Solutions of a Linear Equation in Two Variables",
            "topicCode": "CBSE-9-MGM-4-4.2",
            "subtopics": [
              "Infinitely many solutions property",
              "Finding four distinct solutions (x, y) for a given equation"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Graph of a Linear Equation in Two Variables",
            "topicCode": "CBSE-9-MGM-4-4.3",
            "subtopics": [
              "Plotting solutions and drawing straight line graph",
              "Equations of lines parallel to X-axis (y = k) and Y-axis (x = k)"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Introduction to Euclid Geometry",
        "topics": [
          {
            "number": "5.1",
            "name": "Euclid Definitions, Axioms & Historical Context",
            "topicCode": "CBSE-9-MGM-5-5.1",
            "subtopics": [
              "Point, line, surface definitions",
              "7 Euclidean Axioms (Things equal to same thing are equal, etc.)"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Euclid Five Postulates & Parallel Postulate",
            "topicCode": "CBSE-9-MGM-5-5.2",
            "subtopics": [
              "Postulate 1 to 4: Straight line, terminated line, circle, right angles",
              "Postulate 5: Playfair axiom and equivalent versions of parallel postulate"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Lines and Angles",
        "topics": [
          {
            "number": "6.1",
            "name": "Basic Terms: Ray, Line Segment, Collinear & Types of Angles",
            "topicCode": "CBSE-9-MGM-6-6.1",
            "subtopics": [
              "Acute, right, obtuse, straight, reflex angles",
              "Complementary and supplementary angles",
              "Adjacent angles and linear pair axiom"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Vertically Opposite Angles Theorem & Intersecting Lines",
            "topicCode": "CBSE-9-MGM-6-6.2",
            "subtopics": [
              "Proving vertically opposite angles are equal when two lines intersect"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [
              "Vertically Opposite Angles Theorem"
            ],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Parallel Lines & Transversal Angle Theorems",
            "topicCode": "CBSE-9-MGM-6-6.3",
            "subtopics": [
              "Corresponding angles axiom",
              "Alternate interior angles theorem and converse",
              "Consecutive interior angles supplementary theorem and converse"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [
              "Alternate Interior Angles Theorem",
              "Consecutive Interior Angles Theorem"
            ],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.4",
            "name": "Angle Sum Property of a Triangle & Exterior Angle Theorem",
            "topicCode": "CBSE-9-MGM-6-6.4",
            "subtopics": [
              "Sum of angles in a triangle is 180° theorem",
              "Exterior angle = sum of two interior opposite angles theorem"
            ],
            "practiceSet": "Exercise 6.4",
            "theorems": [
              "Angle Sum Theorem of Triangle",
              "Exterior Angle Theorem"
            ],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Triangles",
        "topics": [
          {
            "number": "7.1",
            "name": "Congruence Criteria: SAS and ASA Axioms/Theorems",
            "topicCode": "CBSE-9-MGM-7-7.1",
            "subtopics": [
              "Side-Angle-Side (SAS) congruence axiom",
              "Angle-Side-Angle (ASA) congruence theorem and AAS corollary"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [
              "ASA Congruence Theorem"
            ],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Isosceles Triangle Theorems & Angle-Side Relationships",
            "topicCode": "CBSE-9-MGM-7-7.2",
            "subtopics": [
              "Angles opposite to equal sides of an isosceles triangle are equal theorem",
              "Sides opposite to equal angles of a triangle are equal theorem"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [
              "Isosceles Triangle Theorem",
              "Converse of Isosceles Triangle Theorem"
            ],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "SSS and RHS Congruence Criteria",
            "topicCode": "CBSE-9-MGM-7-7.3",
            "subtopics": [
              "Side-Side-Side (SSS) congruence rule",
              "Right angle-Hypotenuse-Side (RHS) congruence rule"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [
              "SSS Congruence Rule",
              "RHS Congruence Rule"
            ],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.4",
            "name": "Inequalities in a Triangle",
            "topicCode": "CBSE-9-MGM-7-7.4",
            "subtopics": [
              "Angle opposite to longer side is greater theorem",
              "Side opposite to greater angle is longer theorem",
              "Sum of any two sides of a triangle is greater than third side theorem"
            ],
            "practiceSet": "Exercise 7.4",
            "theorems": [
              "Triangle Inequality Theorem"
            ],
            "problemSet": "Problem Set 7"
          }
        ]
      },
      {
        "number": "8",
        "name": "Quadrilaterals",
        "topics": [
          {
            "number": "8.1",
            "name": "Angle Sum Property of a Quadrilateral (360°)",
            "topicCode": "CBSE-9-MGM-8-8.1",
            "subtopics": [
              "Proof that sum of four interior angles of a quadrilateral is 360°"
            ],
            "practiceSet": "Exercise 8.1",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.2",
            "name": "Properties of Parallelograms & Theorems",
            "topicCode": "CBSE-9-MGM-8-8.2",
            "subtopics": [
              "Diagonal divides parallelogram into two congruent triangles",
              "Opposite sides and angles are equal theorems",
              "Diagonals bisect each other theorem and converses"
            ],
            "practiceSet": "Exercise 8.2",
            "theorems": [
              "Parallelogram Diagonal Congruence Theorem",
              "Parallelogram Diagonals Bisection Theorem"
            ],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.3",
            "name": "The Midpoint Theorem & Its Converse",
            "topicCode": "CBSE-9-MGM-8-8.3",
            "subtopics": [
              "Segment joining midpoints of two sides of a triangle is parallel to third side and half of it",
              "Converse: Line drawn through midpoint of one side parallel to another side bisects third side"
            ],
            "practiceSet": "Exercise 8.3",
            "theorems": [
              "Midpoint Theorem",
              "Converse of Midpoint Theorem"
            ],
            "problemSet": "Problem Set 8"
          }
        ]
      },
      {
        "number": "9",
        "name": "Circles",
        "topics": [
          {
            "number": "9.1",
            "name": "Circle Anatomy: Chord, Arc, Sector, Segment",
            "topicCode": "CBSE-9-MGM-9-9.1",
            "subtopics": [
              "Radius, diameter, chord, secant, tangent basics",
              "Minor/major arcs, minor/major sectors, segments"
            ],
            "practiceSet": "Exercise 9.1",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.2",
            "name": "Perpendicular from Centre to Chord & Distance Theorems",
            "topicCode": "CBSE-9-MGM-9-9.2",
            "subtopics": [
              "Perpendicular from centre to chord bisects the chord theorem and converse",
              "Equal chords of a circle are equidistant from centre theorem and converse"
            ],
            "practiceSet": "Exercise 9.2",
            "theorems": [
              "Perpendicular to Chord Bisection Theorem",
              "Equal Chords Equidistance Theorem"
            ],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.3",
            "name": "Angle Subtended by Arc at Centre & Circumference",
            "topicCode": "CBSE-9-MGM-9-9.3",
            "subtopics": [
              "Angle subtended by arc at centre is double the angle subtended at remaining circumference",
              "Angles in same segment of a circle are equal theorem",
              "Angle in a semicircle is a right angle (90°)"
            ],
            "practiceSet": "Exercise 9.3",
            "theorems": [
              "Inscribed Angle Theorem",
              "Angle in Semicircle Theorem"
            ],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.4",
            "name": "Cyclic Quadrilaterals: Opposite Angle Sum Theorem",
            "topicCode": "CBSE-9-MGM-9-9.4",
            "subtopics": [
              "Opposite angles of cyclic quadrilateral are supplementary (sum = 180°)",
              "Converse: If opposite angles sum to 180°, quadrilateral is concyclic"
            ],
            "practiceSet": "Exercise 9.4",
            "theorems": [
              "Cyclic Quadrilateral Theorem",
              "Converse of Cyclic Quadrilateral Theorem"
            ],
            "problemSet": "Problem Set 9"
          }
        ]
      },
      {
        "number": "10",
        "name": "Heron Formula",
        "topics": [
          {
            "number": "10.1",
            "name": "Heron Formula Derivation & Semi-Perimeter",
            "topicCode": "CBSE-9-MGM-10-10.1",
            "subtopics": [
              "Semi-perimeter s = (a + b + c) / 2",
              "Area formula: A = √[s(s - a)(s - b)(s - c)]",
              "Area of equilateral and isosceles triangles using Heron formula"
            ],
            "practiceSet": "Exercise 10.1",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.2",
            "name": "Applications in Finding Areas of Quadrilaterals & Land Plots",
            "topicCode": "CBSE-9-MGM-10-10.2",
            "subtopics": [
              "Splitting quadrilaterals along diagonal into two triangles",
              "Real-world field and banner triangular design calculations"
            ],
            "practiceSet": "Exercise 10.2",
            "theorems": [],
            "problemSet": "Problem Set 10"
          }
        ]
      },
      {
        "number": "11",
        "name": "Surface Areas and Volumes",
        "topics": [
          {
            "number": "11.1",
            "name": "Surface Area & Volume of Right Circular Cone",
            "topicCode": "CBSE-9-MGM-11-11.1",
            "subtopics": [
              "Slant height formula: l = √(r² + h²)",
              "Curved Surface Area = πrl",
              "Total Surface Area = πr(r + l)",
              "Volume = 1/3 * πr²h"
            ],
            "practiceSet": "Exercise 11.1",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.2",
            "name": "Surface Area & Volume of Sphere and Hemisphere",
            "topicCode": "CBSE-9-MGM-11-11.2",
            "subtopics": [
              "Surface Area of Sphere = 4πr²",
              "Curved Surface Area of Hemisphere = 2πr²",
              "Total Surface Area of Hemisphere = 3πr²",
              "Volume of Sphere = 4/3 * πr³",
              "Volume of Hemisphere = 2/3 * πr³"
            ],
            "practiceSet": "Exercise 11.2",
            "theorems": [],
            "problemSet": "Problem Set 11"
          }
        ]
      },
      {
        "number": "12",
        "name": "Statistics",
        "topics": [
          {
            "number": "12.1",
            "name": "Bar Graphs & Histograms with Varying Base Widths",
            "topicCode": "CBSE-9-MGM-12-12.1",
            "subtopics": [
              "Constructing bar graphs",
              "Histograms with uniform class width",
              "Histograms with varying class intervals: Adjusted Frequency formula"
            ],
            "practiceSet": "Exercise 12.1",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.2",
            "name": "Frequency Polygons Construction",
            "topicCode": "CBSE-9-MGM-12-12.2",
            "subtopics": [
              "Using mid-points / class marks (Upper limit + Lower limit)/2",
              "Constructing frequency polygon with and without histogram"
            ],
            "practiceSet": "Exercise 12.2",
            "theorems": [],
            "problemSet": "Problem Set 12"
          }
        ]
      }
    ]
  },
  {
    "docId": "cbse_9_scie",
    "board": "CBSE",
    "boardCode": "CBSE",
    "class": "9",
    "subject": "Science (Exploration)",
    "subjectCode": "SCIE",
    "chapters": [
      {
        "number": "1",
        "name": "Matter in Our Surroundings",
        "topics": [
          {
            "number": "1.1",
            "name": "Particulate Nature of Matter & Characteristics of Particles",
            "topicCode": "CBSE-9-SCIE-1-1.1",
            "subtopics": [
              "Matter made of tiny particles",
              "Particles have space between them, attract each other, and continuously move (Brownian motion)"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "States of Matter: Solid, Liquid, Gas (Density, Compressibility)",
            "topicCode": "CBSE-9-SCIE-1-1.2",
            "subtopics": [
              "Solid, liquid, gas comparison on shape, volume, rigidity, compressibility, diffusion"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Change of State: Melting, Boiling & Latent Heat",
            "topicCode": "CBSE-9-SCIE-1-1.3",
            "subtopics": [
              "Melting point and Latent Heat of Fusion",
              "Boiling point and Latent Heat of Vaporisation",
              "Effect of temperature change (Kelvin scale = °C + 273.15)"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Effect of Pressure, Sublimation & Deposition",
            "topicCode": "CBSE-9-SCIE-1-1.4",
            "subtopics": [
              "Liquefaction of gases by increasing pressure and decreasing temperature",
              "Sublimation of camphor/ammonium chloride, dry ice (solid CO2)"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.5",
            "name": "Evaporation & Factors Affecting Evaporation",
            "topicCode": "CBSE-9-SCIE-1-1.5",
            "subtopics": [
              "Surface phenomenon vs bulk phenomenon",
              "Factors: surface area, temperature, humidity, wind speed",
              "Evaporative cooling mechanism (earthen pots, sweating, cotton clothes)"
            ],
            "practiceSet": "Exercise 1.5",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Is Matter Around Us Pure?",
        "topics": [
          {
            "number": "2.1",
            "name": "Pure Substances vs Mixtures (Elements, Compounds & Mixtures)",
            "topicCode": "CBSE-9-SCIE-2-2.1",
            "subtopics": [
              "Element definition (metals, non-metals, metalloids)",
              "Compounds: fixed composition by mass, distinct chemical properties",
              "Mixtures: homogeneous vs heterogeneous"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Solutions: Concentration, Saturated Solutions & Solubility",
            "topicCode": "CBSE-9-SCIE-2-2.2",
            "subtopics": [
              "Solute and solvent",
              "Mass by mass percentage & mass by volume percentage concentration formulas",
              "Saturated vs unsaturated solutions, effect of temperature on solubility"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Suspensions, Colloids & Tyndall Effect",
            "topicCode": "CBSE-9-SCIE-2-2.3",
            "subtopics": [
              "Properties of suspension: heterogeneous, visible particles, filtration separation",
              "Properties of colloid: Tyndall light scattering effect, Brownian motion, dispersed phase & dispersion medium types (sol, gel, emulsion, aerosol)"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Separation Techniques of Mixtures",
            "topicCode": "CBSE-9-SCIE-2-2.4",
            "subtopics": [
              "Evaporation, centrifugation, separating funnel for immiscible liquids",
              "Sublimation, paper chromatography for dye separation",
              "Simple distillation vs fractional distillation (fractionating column) for miscible liquids, air component separation"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Atoms and Molecules",
        "topics": [
          {
            "number": "3.1",
            "name": "Laws of Chemical Combination (Conservation of Mass & Constant Proportions)",
            "topicCode": "CBSE-9-SCIE-3-3.1",
            "subtopics": [
              "Law of Conservation of Mass (Lavoisier)",
              "Law of Definite / Constant Proportions (Proust) with water and ammonia examples"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [
              "Law of Conservation of Mass",
              "Law of Constant Proportions"
            ],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Dalton Atomic Theory & Modern Atomic Symbols (IUPAC)",
            "topicCode": "CBSE-9-SCIE-3-3.2",
            "subtopics": [
              "Postulates of Dalton theory explaining chemical laws",
              "IUPAC symbols of elements and Latin names (Fe, Na, K, Cu, Au, Ag)"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Atomic Mass, Unified Mass Unit (u) & Relative Atomic Mass",
            "topicCode": "CBSE-9-SCIE-3-3.3",
            "subtopics": [
              "Standard reference: Carbon-12 isotope (1/12th mass)",
              "Atomic mass scale definitions"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Molecules of Elements, Compounds, Ions & Radicals",
            "topicCode": "CBSE-9-SCIE-3-3.4",
            "subtopics": [
              "Molecules of elements (monoatomic, diatomic, polyatomic e.g. He, O2, P4, S8)",
              "Cations (+) vs Anions (-), polyatomic ions (NH4+, SO4^2-, CO3^2-, NO3-)"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.5",
            "name": "Writing Chemical Formulae & Valency Cross-Over",
            "topicCode": "CBSE-9-SCIE-3-3.5",
            "subtopics": [
              "Valency rules and criss-cross method for binary compounds and polyatomic salts"
            ],
            "practiceSet": "Exercise 3.5",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.6",
            "name": "Molecular Mass & Formula Unit Mass Calculations",
            "topicCode": "CBSE-9-SCIE-3-3.6",
            "subtopics": [
              "Calculating molecular mass by summing atomic masses of constituent atoms",
              "Formula unit mass of ionic compounds (e.g. NaCl, CaCl2)"
            ],
            "practiceSet": "Exercise 3.6",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Structure of the Atom",
        "topics": [
          {
            "number": "4.1",
            "name": "Charged Particles: Electron (J.J. Thomson) & Proton (E. Goldstein Canal Rays)",
            "topicCode": "CBSE-9-SCIE-4-4.1",
            "subtopics": [
              "Discovery of cathode rays and electrons (e/m ratio)",
              "Canal rays / anode rays and proton discovery"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Thomson Plum Pudding Model & Rutherford Alpha Scattering Experiment",
            "topicCode": "CBSE-9-SCIE-4-4.2",
            "subtopics": [
              "Thomson model limitations",
              "Rutherford alpha particle scattering with gold foil",
              "Discovery of atomic nucleus and nuclear planetary model",
              "Drawbacks of Rutherford model (electrodynamic orbital collapse)"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Bohr Model of Atom & Energy Shells (K, L, M, N)",
            "topicCode": "CBSE-9-SCIE-4-4.3",
            "subtopics": [
              "Discrete non-radiating circular orbits",
              "Quantum energy transitions"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.4",
            "name": "Discovery of Neutrons (James Chadwick, 1932)",
            "topicCode": "CBSE-9-SCIE-4-4.4",
            "subtopics": [
              "Charge neutral particle in nucleus with mass equal to proton"
            ],
            "practiceSet": "Exercise 4.4",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.5",
            "name": "Bohr-Bury Rules of Electron Distribution & Valency",
            "topicCode": "CBSE-9-SCIE-4-4.5",
            "subtopics": [
              "Max electrons in shell = 2n² (K=2, L=8, M=18, N=32)",
              "Octet rule for outermost valence shell",
              "Valency definition and determination for first 20 elements"
            ],
            "practiceSet": "Exercise 4.5",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.6",
            "name": "Atomic Number (Z), Mass Number (A), Isotopes & Isobars",
            "topicCode": "CBSE-9-SCIE-4-4.6",
            "subtopics": [
              "Z = protons, A = protons + neutrons",
              "Isotopes: same Z, different A (fractional atomic mass of Chlorine = 35.5 u)",
              "Isobars: same A, different Z (e.g. 40_Ar_18 and 40_Ca_20)",
              "Applications of isotopes in nuclear energy, medicine, archaeology"
            ],
            "practiceSet": "Exercise 4.6",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "The Fundamental Unit of Life",
        "topics": [
          {
            "number": "5.1",
            "name": "Discovery of Cell & Cell Theory (Hooke, Leeuwenhoek, Schleiden, Schwann, Virchow)",
            "topicCode": "CBSE-9-SCIE-5-5.1",
            "subtopics": [
              "Robert Hooke cork cells (1665)",
              "Anton van Leeuwenhoek free living cells (1674)",
              "Cell Theory postulates (All organisms made of cells, Omnis cellula-e-cellula)"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Plasma Membrane: Structure, Diffusion & Osmosis (Hypotonic, Isotonic, Hypertonic)",
            "topicCode": "CBSE-9-SCIE-5-5.2",
            "subtopics": [
              "Phospholipid bilayer with proteins",
              "Diffusion of gases (CO2, O2)",
              "Osmosis across semi-permeable membrane: endosmosis, exosmosis, plasmolysis"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Cell Wall, Plasmolysis & Turgidity in Plant Cells",
            "topicCode": "CBSE-9-SCIE-5-5.3",
            "subtopics": [
              "Cellulose composition, protection against osmotic burst"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.4",
            "name": "Nucleus, Chromosomes, DNA & Prokaryotic vs Eukaryotic Cells",
            "topicCode": "CBSE-9-SCIE-5-5.4",
            "subtopics": [
              "Nuclear envelope, nucleoplasm, nucleolus, chromatin threads",
              "Chromosomes containing DNA and genes",
              "Prokaryotes (nucleoid, 70S ribosomes, no membrane organelles) vs Eukaryotes (true nucleus, 80S ribosomes)"
            ],
            "practiceSet": "Exercise 5.4",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.5",
            "name": "Cytoplasm & Cell Organelles (ER, Golgi, Lysosomes, Mitochondria, Plastids, Vacuoles)",
            "topicCode": "CBSE-9-SCIE-5-5.5",
            "subtopics": [
              "Endoplasmic Reticulum (RER & SER membrane biogenesis)",
              "Golgi apparatus (packaging and secretor)",
              "Lysosomes (digestive enzymes, suicide bags)",
              "Mitochondria (cristae, ATP synthesis, own DNA & ribosomes)",
              "Plastids (Chloroplasts, Chromoplasts, Leucoplasts)",
              "Vacuoles and central sap vacuole in plants"
            ],
            "practiceSet": "Exercise 5.5",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Tissues",
        "topics": [
          {
            "number": "6.1",
            "name": "Plant Tissues: Meristematic Tissues (Apical, Intercalary, Lateral)",
            "topicCode": "CBSE-9-SCIE-6-6.1",
            "subtopics": [
              "Characteristics of meristematic cells (dense cytoplasm, prominent nuclei, thin walls)",
              "Apical meristem (root and shoot tips length)",
              "Intercalary meristem (internode growth)",
              "Lateral meristem / cambium (secondary girth growth)"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Simple Permanent Plant Tissues (Parenchyma, Collenchyma, Sclerenchyma)",
            "topicCode": "CBSE-9-SCIE-6-6.2",
            "subtopics": [
              "Parenchyma (storage, aerenchyma, chlorenchyma)",
              "Collenchyma (flexibility and mechanical support, pectin thickening)",
              "Sclerenchyma (dead cells with lignin walls, husk of coconut)"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Complex Permanent Plant Tissues: Xylem and Phloem",
            "topicCode": "CBSE-9-SCIE-6-6.3",
            "subtopics": [
              "Xylem elements: Tracheids, vessels, xylem parenchyma, xylem fibres (unidirectional water transport)",
              "Phloem elements: Sieve tubes, companion cells, phloem parenchyma, phloem fibres (bidirectional food translocation)"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.4",
            "name": "Animal Tissues: Epithelial Tissues (Squamous, Cuboidal, Columnar, Ciliated, Stratified)",
            "topicCode": "CBSE-9-SCIE-6-6.4",
            "subtopics": [
              "Simple squamous (alveoli, blood vessels)",
              "Stratified squamous (skin wear and tear)",
              "Cuboidal (kidney tubules)",
              "Columnar and ciliated columnar (intestine, respiratory tract)"
            ],
            "practiceSet": "Exercise 6.4",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.5",
            "name": "Animal Tissues: Connective Tissues (Blood, Bone, Cartilage, Ligament, Tendon, Areolar, Adipose)",
            "topicCode": "CBSE-9-SCIE-6-6.5",
            "subtopics": [
              "Fluid connective tissue: Blood plasma, RBCs, WBCs, platelets",
              "Skeletal connective tissues: Bone (calcium-phosphate matrix), Cartilage (chondrocytes, ear/nose tips)",
              "Dense connective: Ligaments (bone to bone), Tendons (muscle to bone)",
              "Packaging: Areolar and Adipose (fat storage subcutaneous insulator)"
            ],
            "practiceSet": "Exercise 6.5",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.6",
            "name": "Animal Tissues: Muscular Tissue (Striated, Smooth, Cardiac) & Nervous Tissue (Neuron)",
            "topicCode": "CBSE-9-SCIE-6-6.6",
            "subtopics": [
              "Striated / skeletal muscle (voluntary, multinucleate, striations)",
              "Smooth / involuntary muscle (spindle shaped, unstriated, internal organs)",
              "Cardiac muscle (involuntary, branched, uninucleate, intercalated discs)",
              "Nervous tissue: Neuron anatomy (cyton/cell body, dendrites, axon, myelin sheath, synapse)"
            ],
            "practiceSet": "Exercise 6.6",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Motion",
        "topics": [
          {
            "number": "7.1",
            "name": "Distance vs Displacement & Uniform vs Non-Uniform Motion",
            "topicCode": "CBSE-9-SCIE-7-7.1",
            "subtopics": [
              "Scalar quantity distance vs vector quantity displacement",
              "Zero displacement with non-zero distance",
              "Equal distances in equal time intervals"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Speed, Velocity & Average Speed/Velocity Formulas",
            "topicCode": "CBSE-9-SCIE-7-7.2",
            "subtopics": [
              "Speed = Distance / Time (m/s)",
              "Velocity = Displacement / Time",
              "Average Speed = Total Distance / Total Time",
              "Average Velocity = (u + v) / 2 for uniform acceleration"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Acceleration (Uniform & Non-Uniform) & Retardation",
            "topicCode": "CBSE-9-SCIE-7-7.3",
            "subtopics": [
              "Acceleration formula: a = (v - u) / t",
              "SI unit m/s²",
              "Deceleration / negative acceleration (retardation)"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.4",
            "name": "Graphical Representation: Distance-Time & Velocity-Time Graphs",
            "topicCode": "CBSE-9-SCIE-7-7.4",
            "subtopics": [
              "Slope of distance-time graph = Speed",
              "Slope of velocity-time graph = Acceleration",
              "Area under velocity-time graph = Displacement"
            ],
            "practiceSet": "Exercise 7.4",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.5",
            "name": "Derivation of Three Equations of Motion by Graphical Method",
            "topicCode": "CBSE-9-SCIE-7-7.5",
            "subtopics": [
              "First equation: v = u + at",
              "Second equation: s = ut + 1/2 * at²",
              "Third equation: v² - u² = 2as"
            ],
            "practiceSet": "Exercise 7.5",
            "theorems": [
              "Equations of Motion"
            ],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.6",
            "name": "Uniform Circular Motion & Centripetal Acceleration",
            "topicCode": "CBSE-9-SCIE-7-7.6",
            "subtopics": [
              "Speed constant but direction continuously changing",
              "Formula for circular speed: v = 2πr / T",
              "Centripetal acceleration toward center"
            ],
            "practiceSet": "Exercise 7.6",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      },
      {
        "number": "8",
        "name": "Force and Laws of Motion",
        "topics": [
          {
            "number": "8.1",
            "name": "Balanced & Unbalanced Forces and Galileo Inclined Plane Experiment",
            "topicCode": "CBSE-9-SCIE-8-8.1",
            "subtopics": [
              "Net zero force in balanced system",
              "Galileo deduction of inertia of moving bodies"
            ],
            "practiceSet": "Exercise 8.1",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.2",
            "name": "Newton First Law of Motion, Inertia & Mass",
            "topicCode": "CBSE-9-SCIE-8-8.2",
            "subtopics": [
              "Statement of first law of motion",
              "Mass as quantitative measure of inertia (heavier object = more inertia)"
            ],
            "practiceSet": "Exercise 8.2",
            "theorems": [
              "Newton First Law of Motion"
            ],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.3",
            "name": "Momentum (p = mv) & Newton Second Law of Motion (F = ma)",
            "topicCode": "CBSE-9-SCIE-8-8.3",
            "subtopics": [
              "Definition of linear momentum and SI unit kg·m/s",
              "Mathematical derivation: F = k * d(mv)/dt = ma",
              "SI unit Newton (N) = 1 kg·m/s²",
              "Applications: cricketer pulling hands back, high jump cushion"
            ],
            "practiceSet": "Exercise 8.3",
            "theorems": [
              "Newton Second Law of Motion"
            ],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.4",
            "name": "Newton Third Law of Motion: Action & Reaction Pairs",
            "topicCode": "CBSE-9-SCIE-8-8.4",
            "subtopics": [
              "Statement: To every action, there is an equal and opposite reaction",
              "Action and reaction act on two different bodies simultaneously",
              "Walking, swimming, rocket propulsion, gun recoil"
            ],
            "practiceSet": "Exercise 8.4",
            "theorems": [
              "Newton Third Law of Motion"
            ],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.5",
            "name": "Law of Conservation of Linear Momentum & Recoil of Gun",
            "topicCode": "CBSE-9-SCIE-8-8.5",
            "subtopics": [
              "Total momentum before collision = Total momentum after collision (m1u1 + m2u2 = m1v1 + m2v2)",
              "Recoil velocity of gun formula: V = -(m/M) * v"
            ],
            "practiceSet": "Exercise 8.5",
            "theorems": [
              "Law of Conservation of Momentum"
            ],
            "problemSet": "Problem Set 8"
          }
        ]
      },
      {
        "number": "9",
        "name": "Gravitation",
        "topics": [
          {
            "number": "9.1",
            "name": "Universal Law of Gravitation & Gravitational Constant (G)",
            "topicCode": "CBSE-9-SCIE-9-9.1",
            "subtopics": [
              "Formula: F = G * (m1 * m2) / r²",
              "Value and SI unit of G = 6.673 * 10^-11 N·m²/kg² (Cavendish)",
              "Importance of universal gravitation (planetary orbits, ocean tides)"
            ],
            "practiceSet": "Exercise 9.1",
            "theorems": [
              "Universal Law of Gravitation"
            ],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.2",
            "name": "Free Fall & Acceleration Due to Gravity (g = GM/R²)",
            "topicCode": "CBSE-9-SCIE-9-9.2",
            "subtopics": [
              "Free fall definition and independence of falling body mass",
              "Calculation of g on Earth surface = 9.8 m/s²",
              "Variation of g with altitude, depth, and equator vs poles (g_pole > g_equator)"
            ],
            "practiceSet": "Exercise 9.2",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.3",
            "name": "Motion of Objects Under Gravity (Equations with g)",
            "topicCode": "CBSE-9-SCIE-9-9.3",
            "subtopics": [
              "Modifying equations of motion: v = u + gt, h = ut + 1/2*gt², v² - u² = 2gh",
              "Sign conventions for upward and downward projectile motion"
            ],
            "practiceSet": "Exercise 9.3",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.4",
            "name": "Mass vs Weight & Weight on the Moon (W_moon = 1/6 * W_earth)",
            "topicCode": "CBSE-9-SCIE-9-9.4",
            "subtopics": [
              "Mass is constant scalar quantity (kg)",
              "Weight is gravitational force vector W = mg (Newton)",
              "Derivation of moon weight being 1/6th of earth weight"
            ],
            "practiceSet": "Exercise 9.4",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.5",
            "name": "Thrust, Pressure, Buoyancy & Archimedes Principle",
            "topicCode": "CBSE-9-SCIE-9-9.5",
            "subtopics": [
              "Thrust definition (perpendicular force) and Pressure = Thrust / Area",
              "Buoyant upthrust force exerted by liquids",
              "Archimedes Principle statement and applications (ships, submarines, hydrometers)",
              "Relative density = Density of substance / Density of water"
            ],
            "practiceSet": "Exercise 9.5",
            "theorems": [
              "Archimedes Principle"
            ],
            "problemSet": "Problem Set 9"
          }
        ]
      },
      {
        "number": "10",
        "name": "Work and Energy",
        "topics": [
          {
            "number": "10.1",
            "name": "Work Done by Constant Force (W = F * s * cosθ)",
            "topicCode": "CBSE-9-SCIE-10-10.1",
            "subtopics": [
              "Scientific conception of work",
              "Positive work (force along displacement), Negative work (friction opposing motion), Zero work (force perpendicular to displacement)",
              "SI unit of work: Joule (1 J = 1 N·m)"
            ],
            "practiceSet": "Exercise 10.1",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.2",
            "name": "Kinetic Energy Formula (KE = 1/2 * m * v²)",
            "topicCode": "CBSE-9-SCIE-10-10.2",
            "subtopics": [
              "Definition of kinetic energy",
              "Mathematical derivation of KE = 1/2 * m * v²",
              "Work-Energy theorem (Work done = Change in KE)"
            ],
            "practiceSet": "Exercise 10.2",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.3",
            "name": "Gravitational Potential Energy Formula (PE = mgh)",
            "topicCode": "CBSE-9-SCIE-10-10.3",
            "subtopics": [
              "Energy stored due to change in position or configuration",
              "Derivation of PE = mgh above ground reference level"
            ],
            "practiceSet": "Exercise 10.3",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.4",
            "name": "Law of Conservation of Energy & Freely Falling Body Proof",
            "topicCode": "CBSE-9-SCIE-10-10.4",
            "subtopics": [
              "Statement: Energy cannot be created nor destroyed, only transformed",
              "Mathematical proof that Total Mechanical Energy (KE + PE) is constant at all points of free fall"
            ],
            "practiceSet": "Exercise 10.4",
            "theorems": [
              "Law of Conservation of Energy"
            ],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.5",
            "name": "Power: Rate of Doing Work & Commercial Unit (kWh)",
            "topicCode": "CBSE-9-SCIE-10-10.5",
            "subtopics": [
              "Power formula P = W / t (Watt, 1 W = 1 J/s)",
              "Kilowatt (kW) and Horsepower (1 hp = 746 W)",
              "Commercial unit of electrical energy: 1 kWh (Unit) = 3.6 * 10^6 Joules"
            ],
            "practiceSet": "Exercise 10.5",
            "theorems": [],
            "problemSet": "Problem Set 10"
          }
        ]
      },
      {
        "number": "11",
        "name": "Sound",
        "topics": [
          {
            "number": "11.1",
            "name": "Production and Propagation of Longitudinal Sound Waves",
            "topicCode": "CBSE-9-SCIE-11-11.1",
            "subtopics": [
              "Vibrating tuning fork and propagation through air",
              "Compressions (regions of high pressure/density) and Rarefactions (low pressure/density)"
            ],
            "practiceSet": "Exercise 11.1",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.2",
            "name": "Wave Characteristics: Frequency, Wavelength, Amplitude, Speed",
            "topicCode": "CBSE-9-SCIE-11-11.2",
            "subtopics": [
              "Wavelength (λ), Frequency (ν = 1/T), Amplitude (A)",
              "Wave speed relationship: v = ν * λ",
              "Pitch depends on frequency, Loudness depends on amplitude, Quality/Timbre depends on waveform"
            ],
            "practiceSet": "Exercise 11.2",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.3",
            "name": "Speed of Sound in Different Media & Sonic Boom",
            "topicCode": "CBSE-9-SCIE-11-11.3",
            "subtopics": [
              "Speed of sound in solids > liquids > gases",
              "Temperature dependence of speed of sound (344 m/s at 22°C in air)",
              "Supersonic speed and shock wave sonic boom"
            ],
            "practiceSet": "Exercise 11.3",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.4",
            "name": "Reflection of Sound, Echo & Reverberation",
            "topicCode": "CBSE-9-SCIE-11-11.4",
            "subtopics": [
              "Laws of reflection of sound",
              "Echo condition: Minimum obstacle distance = 17.2 m (persistence of hearing 0.1 s)",
              "Reverberation in auditoriums and sound absorbing materials (curtains, compressed fiberboard)"
            ],
            "practiceSet": "Exercise 11.4",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.5",
            "name": "Applications of Ultrasound & SONAR (Sound Navigation and Ranging)",
            "topicCode": "CBSE-9-SCIE-11-11.5",
            "subtopics": [
              "Medical echocardiography, ultrasonography, kidney stone breaking",
              "Industrial metal flaw detection",
              "SONAR depth calculation formula: 2d = v * t"
            ],
            "practiceSet": "Exercise 11.5",
            "theorems": [],
            "problemSet": "Problem Set 11"
          }
        ]
      },
      {
        "number": "12",
        "name": "Improvement in Food Resources",
        "topics": [
          {
            "number": "12.1",
            "name": "Crop Variety Improvement & Plant Hybridisation",
            "topicCode": "CBSE-9-SCIE-12-12.1",
            "subtopics": [
              "Breeding for higher yield, improved quality, biotic and abiotic resistance, wider adaptability",
              "Hybridisation (intervarietal, interspecific, intergeneric) and GM crops"
            ],
            "practiceSet": "Exercise 12.1",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.2",
            "name": "Crop Production Management: Nutrients, Manures & Fertilisers",
            "topicCode": "CBSE-9-SCIE-12-12.2",
            "subtopics": [
              "16 essential plant nutrients (Macro vs Micro nutrients)",
              "Organic manures (compost, vermicompost, green manure)",
              "Chemical fertilisers (NPK hazards on soil microflora)"
            ],
            "practiceSet": "Exercise 12.2",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.3",
            "name": "Irrigation Systems & Cropping Patterns (Mixed, Intercropping, Rotation)",
            "topicCode": "CBSE-9-SCIE-12-12.3",
            "subtopics": [
              "Wells, canal systems, river lift systems, tanks",
              "Mixed cropping (wheat + gram), Intercropping (soybean + maize), Crop rotation"
            ],
            "practiceSet": "Exercise 12.3",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.4",
            "name": "Crop Protection Management: Weeds, Insect Pests & Diseases",
            "topicCode": "CBSE-9-SCIE-12-12.4",
            "subtopics": [
              "Weeds (Xanthium, Parthenium, Cyperinus)",
              "Insect pests (chewing, sucking, boring insects)",
              "Biopesticides and preventive grain storage measures"
            ],
            "practiceSet": "Exercise 12.4",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.5",
            "name": "Animal Husbandry: Cattle Farming, Poultry, Fish Production & Apiculture",
            "topicCode": "CBSE-9-SCIE-12-12.5",
            "subtopics": [
              "Cattle farming: Milk producers (milch) vs Draught animals (Bos indicus, Bos bubalis)",
              "Poultry farming: Broilers (meat) vs Layers (eggs)",
              "Fish production: Capture fishing, Aquaculture, Composite fish culture (Catla, Rohu, Mrigal, Grass carp)",
              "Apiculture: Honey bee varieties (Apis cerana indica, Apis mellifera) and pasturage"
            ],
            "practiceSet": "Exercise 12.5",
            "theorems": [],
            "problemSet": "Problem Set 12"
          }
        ]
      }
    ]
  },
  {
    "docId": "mh_9_mth1",
    "board": "Maharashtra Board",
    "boardCode": "MH",
    "class": "9",
    "subject": "Mathematics Part - 1 (Algebra)",
    "subjectCode": "MTH1",
    "chapters": [
      {
        "number": "1",
        "name": "Sets",
        "topics": [
          {
            "number": "1.1",
            "name": "Sets: Definition, Elements & Methods of Writing (Listing & Rule Form)",
            "topicCode": "MH-9-MTH1-1-1.1",
            "subtopics": [
              "Well-defined collection of objects",
              "Roster / Listing method",
              "Set-builder / Rule method"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Types of Sets: Singleton, Empty, Finite & Infinite Sets",
            "topicCode": "MH-9-MTH1-1-1.2",
            "subtopics": [
              "Singleton set (one element)",
              "Null / Empty set (∅ or {})",
              "Finite set (countable elements)",
              "Infinite set (N, W, I, Q, R)"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Equal Sets, Subsets & Universal Set",
            "topicCode": "MH-9-MTH1-1-1.3",
            "subtopics": [
              "Equal sets condition (same elements)",
              "Subset definition (A ⊆ B)",
              "Universal set (U) and Complement of a set (A')"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Venn Diagrams & Operations on Sets (Union & Intersection)",
            "topicCode": "MH-9-MTH1-1-1.4",
            "subtopics": [
              "John Venn diagram representations",
              "Intersection of sets (A ∩ B)",
              "Disjoint sets",
              "Union of sets (A ∪ B)"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.5",
            "name": "Number of Elements in Set Formula: n(A ∪ B) = n(A) + n(B) - n(A ∩ B)",
            "topicCode": "MH-9-MTH1-1-1.5",
            "subtopics": [
              "Cardinality of sets",
              "Word problems on languages spoken, newspaper readers, sports participants"
            ],
            "practiceSet": "Exercise 1.5",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Real Numbers",
        "topics": [
          {
            "number": "2.1",
            "name": "Properties of Rational Numbers & Decimal Representation",
            "topicCode": "MH-9-MTH1-2-2.1",
            "subtopics": [
              "p/q form where q != 0",
              "Terminating vs non-terminating recurring forms",
              "Order relation properties (Trichotomy law)"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Irrational Numbers: Geometric Proof of Irrationality of √2",
            "topicCode": "MH-9-MTH1-2-2.2",
            "subtopics": [
              "Proof by contradiction",
              "Representation of √5, √10 on number line"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Surds: Definition, Order, Like/Unlike Surds & Simplest Form",
            "topicCode": "MH-9-MTH1-2-2.3",
            "subtopics": [
              "Definition of surd ⁿ√a",
              "Order of surd (n)",
              "Like / similar surds",
              "Simplest radical form"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Operations on Surds & Comparison of Surds",
            "topicCode": "MH-9-MTH1-2-2.4",
            "subtopics": [
              "Addition, subtraction, multiplication, division of surds",
              "Comparing pure and mixed surds"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.5",
            "name": "Rationalisation of Surds & Conjugate Pairs",
            "topicCode": "MH-9-MTH1-2-2.5",
            "subtopics": [
              "Rationalising factor definition",
              "Conjugate pair of binomial surd (√a + √b)(√a - √b)"
            ],
            "practiceSet": "Exercise 2.5",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.6",
            "name": "Absolute Value / Modulus of Real Numbers",
            "topicCode": "MH-9-MTH1-2-2.6",
            "subtopics": [
              "Definition |x|",
              "Solving modulus equations |x - a| = b"
            ],
            "practiceSet": "Exercise 2.6",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Polynomials",
        "topics": [
          {
            "number": "3.1",
            "name": "Introduction: Degree of Polynomials & Forms",
            "topicCode": "MH-9-MTH1-3-3.1",
            "subtopics": [
              "Degree in one and more variables",
              "Standard form, Index form, and Coefficient form"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Operations on Polynomials: Addition, Subtraction, Multiplication",
            "topicCode": "MH-9-MTH1-3-3.2",
            "subtopics": [
              "Degree of sum, difference and product polynomials"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Division of Polynomials: Synthetic Division & Linear Method",
            "topicCode": "MH-9-MTH1-3-3.3",
            "subtopics": [
              "Synthetic division algorithm using opposite coefficients",
              "Linear division method"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Value of Polynomial, Remainder Theorem & Factor Theorem",
            "topicCode": "MH-9-MTH1-3-3.4",
            "subtopics": [
              "Evaluating p(x) for x = a",
              "Remainder theorem statement & verification",
              "Factor theorem for checking factorability"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [
              "Remainder Theorem",
              "Factor Theorem"
            ],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.5",
            "name": "Factorisation of Polynomials (Middle Term Splitting & Substitution)",
            "topicCode": "MH-9-MTH1-3-3.5",
            "subtopics": [
              "Factoring quadratic expressions (x² - x)² - 8(x² - x) + 12",
              "Factoring cubic polynomials"
            ],
            "practiceSet": "Exercise 3.5",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Ratio and Proportion",
        "topics": [
          {
            "number": "4.1",
            "name": "Ratio Concepts & Properties of Ratio (a:b)",
            "topicCode": "MH-9-MTH1-4-4.1",
            "subtopics": [
              "Units consistency",
              "Order of terms",
              "Multiplying/dividing terms by non-zero scalar"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Direct & Inverse Proportion Word Problems",
            "topicCode": "MH-9-MTH1-4-4.2",
            "subtopics": [
              "Applications in work, rate, and geometry"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Properties of Equal Ratios (Invertendo, Alternendo, Componendo, Dividendo)",
            "topicCode": "MH-9-MTH1-4-4.3",
            "subtopics": [
              "Invertendo: a/b = c/d => b/a = d/c",
              "Alternendo: a/b = c/d => a/c = b/d",
              "Componendo: (a+b)/b = (c+d)/d",
              "Dividendo: (a-b)/b = (c-d)/d",
              "Componendo-Dividendo: (a+b)/(a-b) = (c+d)/(c-d)"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.4",
            "name": "Theorem on Equal Ratios & Continued Proportion",
            "topicCode": "MH-9-MTH1-4-4.4",
            "subtopics": [
              "Theorem: a/b = c/d = (a+c)/(b+d)",
              "Continued proportion a/b = b/c = c/d",
              "Geometric mean formula b² = ac",
              "k-method of proof"
            ],
            "practiceSet": "Exercise 4.4",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Linear Equations in Two Variables",
        "topics": [
          {
            "number": "5.1",
            "name": "Simultaneous Linear Equations & Elimination Method",
            "topicCode": "MH-9-MTH1-5-5.1",
            "subtopics": [
              "Standard form ax + by = c",
              "Eliminating variable by equating coefficients"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Substitution Method for Simultaneous Equations",
            "topicCode": "MH-9-MTH1-5-5.2",
            "subtopics": [
              "Expressing one variable in terms of other and substituting"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Word Problems on Ages, Numbers, Speed-Distance & Fractions",
            "topicCode": "MH-9-MTH1-5-5.3",
            "subtopics": [
              "Two-digit reversal problems",
              "Numerator and denominator modifications",
              "Speed and time variations"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Financial Planning",
        "topics": [
          {
            "number": "6.1",
            "name": "Savings & Investments: Bank, Shares, Mutual Funds, Insurance",
            "topicCode": "MH-9-MTH1-6-6.1",
            "subtopics": [
              "Importance of savings",
              "Fixed deposit, recurring deposit, PPF, mutual funds (SIP), Life and Health insurance"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Income Tax Basics: PAN Card, Financial Year & Assessment Year",
            "topicCode": "MH-9-MTH1-6-6.2",
            "subtopics": [
              "Direct tax vs Indirect tax",
              "Permanent Account Number (PAN)",
              "Financial Year (FY: 1 Apr - 31 Mar) vs Assessment Year (AY)"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Income Tax Computation, Tax Slabs & Deductions (80C, 80D)",
            "topicCode": "MH-9-MTH1-6-6.3",
            "subtopics": [
              "Taxable income calculation",
              "Deductions under section 80C up to 1.5 Lakh",
              "Tax slabs for general citizens, senior citizens, and super senior citizens"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Statistics",
        "topics": [
          {
            "number": "7.1",
            "name": "Primary vs Secondary Data & Grouped/Ungrouped Frequency Tables",
            "topicCode": "MH-9-MTH1-7-7.1",
            "subtopics": [
              "Data collection methods",
              "Class intervals: Inclusive (discrete) vs Exclusive (continuous) method",
              "Class mark = (Lower limit + Upper limit)/2"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Cumulative Frequency Distribution (Less Than & More Than Types)",
            "topicCode": "MH-9-MTH1-7-7.2",
            "subtopics": [
              "Running cumulative sum",
              "Frequency interpretation"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Measures of Central Tendency: Mean, Median and Mode of Ungrouped Data",
            "topicCode": "MH-9-MTH1-7-7.3",
            "subtopics": [
              "Mean: X̄ = Σx / N and Σ(f*x) / N",
              "Median: Middle value of sorted array (N odd/even)",
              "Mode: Most frequently occurring value"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      }
    ]
  },
  {
    "docId": "mh_9_mth2",
    "board": "Maharashtra Board",
    "boardCode": "MH",
    "class": "9",
    "subject": "Mathematics Part - 2 (Geometry)",
    "subjectCode": "MTH2",
    "chapters": [
      {
        "number": "1",
        "name": "Basic Concepts in Geometry",
        "topics": [
          {
            "number": "1.1",
            "name": "Coordinates of Points & Distance on Number Line (d(A, B))",
            "topicCode": "MH-9-MTH2-1-1.1",
            "subtopics": [
              "Coordinates on number line",
              "Distance formula: d(A, B) = Greater coordinate - Smaller coordinate"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Betweenness of Points (A-B-C) & Collinear Points",
            "topicCode": "MH-9-MTH2-1-1.2",
            "subtopics": [
              "Condition: d(A, B) + d(B, C) = d(A, C)",
              "Collinear vs non-collinear test"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Line Segment, Ray, Congruence of Segments & Midpoint",
            "topicCode": "MH-9-MTH2-1-1.3",
            "subtopics": [
              "Segment definition and length",
              "Opposite rays",
              "Midpoint: AM = MB = 1/2 AB"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Conditional Statements, Converse, Postulates & Proofs",
            "topicCode": "MH-9-MTH2-1-1.4",
            "subtopics": [
              "Antecedent (If part) vs Consequent (Then part)",
              "Converse formulation",
              "Direct and indirect proof methods"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Parallel Lines",
        "topics": [
          {
            "number": "2.1",
            "name": "Properties of Parallel Lines & Interior Angles Theorem",
            "topicCode": "MH-9-MTH2-2-2.1",
            "subtopics": [
              "Sum of interior angles on same side of transversal is 180° theorem",
              "Indirect proof method"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [
              "Interior Angles Theorem"
            ],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Corresponding Angles & Alternate Angles Theorems",
            "topicCode": "MH-9-MTH2-2-2.2",
            "subtopics": [
              "Alternate angles theorem proof",
              "Corresponding angles theorem proof"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [
              "Alternate Angles Theorem",
              "Corresponding Angles Theorem"
            ],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Tests for Parallel Lines (Interior, Alternate, Corresponding Angle Tests)",
            "topicCode": "MH-9-MTH2-2-2.3",
            "subtopics": [
              "Proving two lines parallel using angle criteria"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [
              "Parallel Lines Tests"
            ],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Use of Properties of Parallel Lines (Triangle Angle Sum = 180°)",
            "topicCode": "MH-9-MTH2-2-2.4",
            "subtopics": [
              "Theorem: Sum of all three angles of a triangle is 180°",
              "Exterior angle theorem applications"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [
              "Angle Sum Property Theorem"
            ],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Triangles",
        "topics": [
          {
            "number": "3.1",
            "name": "Theorem of Remote Interior Angles of a Triangle",
            "topicCode": "MH-9-MTH2-3-3.1",
            "subtopics": [
              "Measure of exterior angle = sum of its remote interior angles"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [
              "Remote Interior Angles Theorem"
            ],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Congruence of Triangles Tests (SAS, ASA, SSS, Hypotenuse-Side)",
            "topicCode": "MH-9-MTH2-3-3.2",
            "subtopics": [
              "Rigorous two-column geometric proofs",
              "Corresponding angles/sides of congruent triangles (c.a.c.t. & c.s.c.t.)"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Isosceles Triangle Theorem & 30°-60°-90° / 45°-45°-90° Theorems",
            "topicCode": "MH-9-MTH2-3-3.3",
            "subtopics": [
              "Isosceles triangle theorem and converse",
              "30°-60°-90° theorem: Side opposite 30° is 1/2 hyp, opposite 60° is √3/2 hyp",
              "45°-45°-90° theorem: Perpendicular sides are 1/√2 hyp"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [
              "Isosceles Triangle Theorem",
              "30-60-90 Triangle Theorem",
              "45-45-90 Triangle Theorem"
            ],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Median of Right Angled Triangle & Perpendicular Bisector Theorem",
            "topicCode": "MH-9-MTH2-3-3.4",
            "subtopics": [
              "Length of median to hypotenuse = 1/2 hypotenuse",
              "Perpendicular bisector theorem: Every point on perpendicular bisector is equidistant from endpoints"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [
              "Median to Hypotenuse Theorem",
              "Perpendicular Bisector Theorem"
            ],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.5",
            "name": "Angle Bisector Theorem & Similar Triangles",
            "topicCode": "MH-9-MTH2-3-3.5",
            "subtopics": [
              "Every point on angle bisector is equidistant from arms of angle",
              "Similar triangles: ratio of corresponding sides equal"
            ],
            "practiceSet": "Exercise 3.5",
            "theorems": [
              "Angle Bisector Theorem"
            ],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Constructions of Triangles",
        "topics": [
          {
            "number": "4.1",
            "name": "Constructing Triangle Given Base, Base Angle & Sum of Other Two Sides (AB + AC)",
            "topicCode": "MH-9-MTH2-4-4.1",
            "subtopics": [
              "Compass and ruler step-by-step construction"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Constructing Triangle Given Base, Base Angle & Difference of Other Two Sides (AB - AC)",
            "topicCode": "MH-9-MTH2-4-4.2",
            "subtopics": [
              "Case 1: AB > AC",
              "Case 2: AC > AB"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Constructing Triangle Given Perimeter (AB + BC + CA) & Two Base Angles",
            "topicCode": "MH-9-MTH2-4-4.3",
            "subtopics": [
              "Dividing baseline and drawing perpendicular bisectors"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Quadrilaterals",
        "topics": [
          {
            "number": "5.1",
            "name": "Parallelogram Theorems & Tests for Parallelograms",
            "topicCode": "MH-9-MTH2-5-5.1",
            "subtopics": [
              "Opposite sides and opposite angles theorem",
              "Diagonals bisect each other theorem",
              "Tests to prove a quadrilateral is a parallelogram"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [
              "Parallelogram Theorems",
              "Parallelogram Tests"
            ],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Special Parallelograms: Rectangle, Rhombus and Square Theorems",
            "topicCode": "MH-9-MTH2-5-5.2",
            "subtopics": [
              "Diagonals of rectangle are congruent",
              "Diagonals of rhombus are perpendicular bisectors",
              "Diagonals of square are congruent and perpendicular bisectors"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [
              "Rectangle Diagonals Theorem",
              "Rhombus Diagonals Theorem"
            ],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Trapezium & Midpoint Theorem of Triangle",
            "topicCode": "MH-9-MTH2-5-5.3",
            "subtopics": [
              "Midpoint theorem: Segment joining midpoints of two sides is parallel to third side and half of it",
              "Converse of midpoint theorem"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [
              "Midpoint Theorem of Triangle",
              "Converse of Midpoint Theorem"
            ],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Circle",
        "topics": [
          {
            "number": "6.1",
            "name": "Chord Properties & Distance from Centre Theorems",
            "topicCode": "MH-9-MTH2-6-6.1",
            "subtopics": [
              "Perpendicular from centre to chord bisects chord theorem and converse",
              "Congruent chords are equidistant from centre theorem and converse"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [
              "Perpendicular to Chord Theorem",
              "Congruent Chords Distance Theorem"
            ],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Incircle of a Triangle Construction",
            "topicCode": "MH-9-MTH2-6-6.2",
            "subtopics": [
              "Constructing angle bisectors of triangle",
              "Incentre (I) and inradius"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Circumcircle of a Triangle Construction",
            "topicCode": "MH-9-MTH2-6-6.3",
            "subtopics": [
              "Constructing perpendicular bisectors of sides of triangle",
              "Circumcentre (C) location in acute, right, and obtuse triangles"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Coordinate Geometry",
        "topics": [
          {
            "number": "7.1",
            "name": "Axes, Origin & Plotting Coordinates on Cartesian Plane",
            "topicCode": "MH-9-MTH2-7-7.1",
            "subtopics": [
              "X-axis, Y-axis, Origin (0,0)",
              "Plotting points in all four quadrants"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Equations of Lines Parallel to Axes (x = a, y = b)",
            "topicCode": "MH-9-MTH2-7-7.2",
            "subtopics": [
              "Line parallel to Y-axis: x = c",
              "Line parallel to X-axis: y = c",
              "Equation of X-axis (y=0) and Y-axis (x=0)"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Graph of Linear Equations in Two Variables: ax + by + c = 0",
            "topicCode": "MH-9-MTH2-7-7.3",
            "subtopics": [
              "Finding solutions table and plotting straight lines on graph paper"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      },
      {
        "number": "8",
        "name": "Trigonometry",
        "topics": [
          {
            "number": "8.1",
            "name": "Trigonometric Ratios: sin θ, cos θ, tan θ Definitions",
            "topicCode": "MH-9-MTH2-8-8.1",
            "subtopics": [
              "In right angled triangle: sin θ = Opposite / Hypotenuse",
              "cos θ = Adjacent / Hypotenuse",
              "tan θ = Opposite / Adjacent = sin θ / cos θ"
            ],
            "practiceSet": "Exercise 8.1",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.2",
            "name": "Relations Among Trigonometric Ratios & Identity sin²θ + cos²θ = 1",
            "topicCode": "MH-9-MTH2-8-8.2",
            "subtopics": [
              "tan θ * tan (90-θ) = 1",
              "sin θ = cos (90-θ) and cos θ = sin (90-θ)",
              "Fundamental identity: sin²θ + cos²θ = 1"
            ],
            "practiceSet": "Exercise 8.2",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.3",
            "name": "Trigonometric Values of Standard Angles (0°, 30°, 45°, 60°, 90°)",
            "topicCode": "MH-9-MTH2-8-8.3",
            "subtopics": [
              "Derivation of values using geometric triangles",
              "Evaluating trigonometric algebraic expressions"
            ],
            "practiceSet": "Exercise 8.3",
            "theorems": [],
            "problemSet": "Problem Set 8"
          }
        ]
      },
      {
        "number": "9",
        "name": "Surface Area and Volume",
        "topics": [
          {
            "number": "9.1",
            "name": "Surface Area and Volume of Cone",
            "topicCode": "MH-9-MTH2-9-9.1",
            "subtopics": [
              "Slant height l = √(r² + h²)",
              "Curved Surface Area = πrl",
              "Total Surface Area = πr(r + l)",
              "Volume = 1/3 * πr²h"
            ],
            "practiceSet": "Exercise 9.1",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.2",
            "name": "Surface Area and Volume of Sphere and Hemisphere",
            "topicCode": "MH-9-MTH2-9-9.2",
            "subtopics": [
              "Surface Area of Sphere = 4πr²",
              "Volume of Sphere = 4/3 * πr³",
              "Curved Surface Area of Hemisphere = 2πr²",
              "Total Surface Area of Hemisphere = 3πr²",
              "Volume of Hemisphere = 2/3 * πr³"
            ],
            "practiceSet": "Exercise 9.2",
            "theorems": [],
            "problemSet": "Problem Set 9"
          }
        ]
      }
    ]
  },
  {
    "docId": "mh_9_scit",
    "board": "Maharashtra Board",
    "boardCode": "MH",
    "class": "9",
    "subject": "Science and Technology",
    "subjectCode": "SCIT",
    "chapters": [
      {
        "number": "1",
        "name": "Laws of Motion",
        "topics": [
          {
            "number": "1.1",
            "name": "Distance, Displacement, Speed and Velocity",
            "topicCode": "MH-9-SCIT-1-1.1",
            "subtopics": [
              "Scalar distance vs vector displacement",
              "Speed = distance / time, Velocity = displacement / time",
              "Uniform vs non-uniform motion along straight line"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Acceleration (Positive, Negative/Deceleration, Zero)",
            "topicCode": "MH-9-SCIT-1-1.2",
            "subtopics": [
              "Acceleration formula a = (v - u) / t",
              "SI unit m/s²"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Distance-Time and Velocity-Time Graphs",
            "topicCode": "MH-9-SCIT-1-1.3",
            "subtopics": [
              "Interpreting slopes for velocity and acceleration",
              "Area under velocity-time graph gives displacement"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Equations of Motion by Graphical Method (v=u+at, s=ut+1/2at², v²=u²+2as)",
            "topicCode": "MH-9-SCIT-1-1.4",
            "subtopics": [
              "Derivation of first, second, and third kinematic equations"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [
              "Kinematic Equations of Motion"
            ],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.5",
            "name": "Uniform Circular Motion & Centripetal Force",
            "topicCode": "MH-9-SCIT-1-1.5",
            "subtopics": [
              "v = 2πr / t",
              "Centripetal force towards center formula F = mv²/r"
            ],
            "practiceSet": "Exercise 1.5",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.6",
            "name": "Newton Three Laws of Motion & Law of Conservation of Momentum",
            "topicCode": "MH-9-SCIT-1-1.6",
            "subtopics": [
              "First law (Inertia)",
              "Second law (F = ma)",
              "Third law (Action and Reaction)",
              "Conservation of momentum (m1u1 + m2u2 = m1v1 + m2v2)",
              "Recoil of gun"
            ],
            "practiceSet": "Exercise 1.6",
            "theorems": [
              "Newton Laws of Motion",
              "Law of Conservation of Momentum"
            ],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Work and Energy",
        "topics": [
          {
            "number": "2.1",
            "name": "Work: Positive, Negative and Zero Work (W = F * s * cosθ)",
            "topicCode": "MH-9-SCIT-2-2.1",
            "subtopics": [
              "Definition of work, Joule and Erg (1 J = 10^7 erg)",
              "Direction of force and displacement"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Energy & Kinetic Energy Derivation (KE = 1/2 * m * v²)",
            "topicCode": "MH-9-SCIT-2-2.2",
            "subtopics": [
              "Definition of energy",
              "Derivation using Newton second law and work formula"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Potential Energy Formula (PE = mgh)",
            "topicCode": "MH-9-SCIT-2-2.3",
            "subtopics": [
              "Stored energy due to state or position"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Law of Conservation of Energy & Free Fall Proof",
            "topicCode": "MH-9-SCIT-2-2.4",
            "subtopics": [
              "Transformation of energy forms",
              "Proof that Total Energy = KE + PE is constant during free fall"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [
              "Law of Conservation of Energy"
            ],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.5",
            "name": "Power: Rate of Doing Work & Commercial Electrical Energy",
            "topicCode": "MH-9-SCIT-2-2.5",
            "subtopics": [
              "Power P = W / t (Watt, kW, Horsepower: 1 hp = 746 W)",
              "1 kWh = 3.6 * 10^6 J"
            ],
            "practiceSet": "Exercise 2.5",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Current Electricity",
        "topics": [
          {
            "number": "3.1",
            "name": "Electric Current & Potential Difference",
            "topicCode": "MH-9-SCIT-3-3.1",
            "subtopics": [
              "Current I = Q / t (Ampere)",
              "Potential difference V = W / Q (Volt)"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Ohm Law & Resistance of a Conductor",
            "topicCode": "MH-9-SCIT-3-3.2",
            "subtopics": [
              "Statement: V = I * R (George Simon Ohm)",
              "SI unit Ohm (Ω)",
              "I-V characteristic graph of ohmic conductors"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [
              "Ohm Law"
            ],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Resistivity of Material (R = ρ * L / A)",
            "topicCode": "MH-9-SCIT-3-3.3",
            "subtopics": [
              "Factors affecting resistance: length, cross-sectional area, material resistivity (ρ in Ω·m), temperature"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Resistors in Series (Rs = R1 + R2 + R3)",
            "topicCode": "MH-9-SCIT-3-3.4",
            "subtopics": [
              "Same current through all resistors, V = V1 + V2 + V3",
              "Equivalent resistance is greater than individual resistors"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.5",
            "name": "Resistors in Parallel (1/Rp = 1/R1 + 1/R2 + 1/R3)",
            "topicCode": "MH-9-SCIT-3-3.5",
            "subtopics": [
              "Same potential difference across all resistors, I = I1 + I2 + I3",
              "Equivalent resistance is less than smallest resistor"
            ],
            "practiceSet": "Exercise 3.5",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.6",
            "name": "Domestic Electrical Wiring & Safety (Fuse, MCB, Earthing)",
            "topicCode": "MH-9-SCIT-3-3.6",
            "subtopics": [
              "Live wire (brown/red), Neutral wire (blue/black), Earth wire (green/yellow)",
              "Cartridge fuse and Miniature Circuit Breakers (MCB)"
            ],
            "practiceSet": "Exercise 3.6",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Measurement of Matter",
        "topics": [
          {
            "number": "4.1",
            "name": "Laws of Chemical Combination (Conservation of Mass & Constant Proportion)",
            "topicCode": "MH-9-SCIT-4-4.1",
            "subtopics": [
              "Antoine Lavoisier and Joseph Proust laws"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [
              "Law of Conservation of Mass",
              "Law of Constant Proportion"
            ],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Atom Size, Mass and Valency",
            "topicCode": "MH-9-SCIT-4-4.2",
            "subtopics": [
              "Atomic radius in nanometres (1 nm = 10^-9 m)",
              "Atomic mass unit (Dalton / u based on C-12)"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Mole Concept & Avogadro Number (N_A = 6.022 * 10²³)",
            "topicCode": "MH-9-SCIT-4-4.3",
            "subtopics": [
              "Number of moles = Mass in grams / Molar mass",
              "Avogadro number of particles in 1 mole"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.4",
            "name": "Valency, Radicals (Basic vs Acidic) & Writing Chemical Formulae",
            "topicCode": "MH-9-SCIT-4-4.4",
            "subtopics": [
              "Simple vs composite radicals",
              "Cations (basic radicals) and Anions (acidic radicals)",
              "Criss-cross valency method"
            ],
            "practiceSet": "Exercise 4.4",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Acids, Bases and Salts",
        "topics": [
          {
            "number": "5.1",
            "name": "Arrhenius Theory of Acids and Bases",
            "topicCode": "MH-9-SCIT-5-5.1",
            "subtopics": [
              "Acid produces H+ (H3O+) in water",
              "Base produces OH- in water",
              "Strong vs weak acids and bases (degree of dissociation)"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "pH Scale & Universal Indicator",
            "topicCode": "MH-9-SCIT-5-5.2",
            "subtopics": [
              "pH range 0 to 14 (pH < 7 acidic, pH = 7 neutral, pH > 7 basic)",
              "Measurement of pH using pH paper and digital pH meter"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Chemical Properties of Acids & Bases (Metals, Oxides, Carbonates)",
            "topicCode": "MH-9-SCIT-5-5.3",
            "subtopics": [
              "Reaction with active metals -> Salt + H2 gas",
              "Reaction with metal oxides -> Salt + H2O",
              "Reaction with carbonates and bicarbonates -> Salt + H2O + CO2 gas"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.4",
            "name": "Salts: Types, pH of Salt Solutions & Water of Crystallization",
            "topicCode": "MH-9-SCIT-5-5.4",
            "subtopics": [
              "Neutral, acidic, basic salts",
              "Water of crystallization in hydrated crystals (CuSO4·5H2O, FeSO4·7H2O, Na2CO3·10H2O, CaSO4·2H2O Plaster of Paris)"
            ],
            "practiceSet": "Exercise 5.4",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.5",
            "name": "Electrolysis of Water & Copper Sulphate Solution",
            "topicCode": "MH-9-SCIT-5-5.5",
            "subtopics": [
              "Cathode (-ve) and Anode (+ve) reactions in electrolytic cell"
            ],
            "practiceSet": "Exercise 5.5",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Classification of Plants",
        "topics": [
          {
            "number": "6.1",
            "name": "Kingdom Plantae: Cryptogams (Non-flowering)",
            "topicCode": "MH-9-SCIT-6-6.1",
            "subtopics": [
              "Division Thallophyta (Algae: Spirogyra, Ulva, Chara)",
              "Division Bryophyta (Amphibians of plant kingdom: Moss/Funaria, Riccia, Marchantia)",
              "Division Pteridophyta (Ferns: Nephrolepis, Marsilea, conducting tissues present)"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Phanerogams: Gymnosperms vs Angiosperms",
            "topicCode": "MH-9-SCIT-6-6.2",
            "subtopics": [
              "Gymnosperms (Naked seeds, non-flowering evergreen woody e.g. Cycas, Pinus)",
              "Angiosperms (Enclosed seeds within fruit, flowering)"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Angiosperms: Dicotyledonous vs Monocotyledonous Plants",
            "topicCode": "MH-9-SCIT-6-6.3",
            "subtopics": [
              "Dicot (Two cotyledons, tap root system, reticulate venation, tetramerous/pentamerous flowers, open vascular bundles)",
              "Monocot (Single cotyledon, fibrous root system, parallel venation, trimerous flowers, closed vascular bundles)"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Energy Flow in an Ecosystem",
        "topics": [
          {
            "number": "7.1",
            "name": "Food Chain, Food Web & Trophic Levels",
            "topicCode": "MH-9-SCIT-7-7.1",
            "subtopics": [
              "Producers, Primary consumers (herbivores), Secondary consumers (carnivores), Apex consumers, Decomposers"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "The Energy Pyramid & Lindeman 10% Energy Rule",
            "topicCode": "MH-9-SCIT-7-7.2",
            "subtopics": [
              "Energy decrease at successive trophic levels (Lindeman 10% law)",
              "Unidirectional flow of energy in ecosystem"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Biogeochemical Cycles: Carbon Cycle, Oxygen Cycle, Nitrogen Cycle",
            "topicCode": "MH-9-SCIT-7-7.3",
            "subtopics": [
              "Carbon cycle: Photosynthesis and respiration balance",
              "Oxygen cycle: Photolysis and respiration",
              "Nitrogen cycle: Nitrogen fixation, ammonification, nitrification, denitrification"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      },
      {
        "number": "8",
        "name": "Useful and Harmful Microbes",
        "topics": [
          {
            "number": "8.1",
            "name": "Useful Microbes: Lactobacilli, Rhizobium & Yeast",
            "topicCode": "MH-9-SCIT-8-8.1",
            "subtopics": [
              "Lactobacilli in dairy fermentation and yogurt/probiotics",
              "Rhizobium symbiosis in root nodules of leguminous plants for nitrogen fixation",
              "Yeast (Saccharomyces cerevisiae) in bread baking and bio-ethanol fuel"
            ],
            "practiceSet": "Exercise 8.1",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.2",
            "name": "Antibiotics: Penicillin (Alexander Fleming) & Broad vs Narrow Spectrum",
            "topicCode": "MH-9-SCIT-8-8.2",
            "subtopics": [
              "Discovery of penicillin (Penicillium notatum)",
              "Broad spectrum (Amoxicillin, Tetracycline) vs Narrow spectrum antibiotics"
            ],
            "practiceSet": "Exercise 8.2",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.3",
            "name": "Harmful Microbes: Clostridium & Other Pathogens",
            "topicCode": "MH-9-SCIT-8-8.3",
            "subtopics": [
              "Clostridium botulinum (food poisoning / botulism, anaerobic)",
              "Pathogens of Dengue, Malaria, Bird Flu, Swine Flu, Hepatitis, Typhoid"
            ],
            "practiceSet": "Exercise 8.3",
            "theorems": [],
            "problemSet": "Problem Set 8"
          }
        ]
      },
      {
        "number": "9",
        "name": "Environmental Management",
        "topics": [
          {
            "number": "9.1",
            "name": "Weather, Climate & Meteorology",
            "topicCode": "MH-9-SCIT-9-9.1",
            "subtopics": [
              "Meteorological elements, India Meteorological Department (IMD) forecasts, monsoon prediction models"
            ],
            "practiceSet": "Exercise 9.1",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.2",
            "name": "Solid Waste Management: Biodegradable vs Non-biodegradable",
            "topicCode": "MH-9-SCIT-9-9.2",
            "subtopics": [
              "Domestic, industrial, hazardous, biomedical, e-waste",
              "Principles of 7R (Rethink, Refuse, Reduce, Reuse, Recycle, Rethink, Recover)"
            ],
            "practiceSet": "Exercise 9.2",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.3",
            "name": "Scientific Waste Disposal: Composting, Vermicomposting, Incineration, Landfills",
            "topicCode": "MH-9-SCIT-9-9.3",
            "subtopics": [
              "Segregation of dry and wet waste",
              "Pyrolysis and sanitary landfilling"
            ],
            "practiceSet": "Exercise 9.3",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.4",
            "name": "Disaster Management: First Aid Principles (RICE - Rest, Ice, Compression, Elevation)",
            "topicCode": "MH-9-SCIT-9-9.4",
            "subtopics": [
              "ABC of first aid (Airway, Breathing, Circulation)",
              "Transportation methods for injured patients (cradle method, human crutch, stretcher)"
            ],
            "practiceSet": "Exercise 9.4",
            "theorems": [],
            "problemSet": "Problem Set 9"
          }
        ]
      },
      {
        "number": "10",
        "name": "Information Communication Technology (ICT)",
        "topics": [
          {
            "number": "10.1",
            "name": "Computer Hardware, Software & Generations of Computers",
            "topicCode": "MH-9-SCIT-10-10.1",
            "subtopics": [
              "Input devices, CPU (ALU, Control Unit, Memory), Output devices",
              "Operating system vs Application software"
            ],
            "practiceSet": "Exercise 10.1",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.2",
            "name": "Productivity Software: MS Word, MS Excel & MS PowerPoint",
            "topicCode": "MH-9-SCIT-10-10.2",
            "subtopics": [
              "Formula creation in spreadsheets (SUM, AVERAGE)",
              "Slide animations and presentations"
            ],
            "practiceSet": "Exercise 10.2",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.3",
            "name": "ICT in Science Education & Indian Supercomputers (PARAM)",
            "topicCode": "MH-9-SCIT-10-10.3",
            "subtopics": [
              "Simulations, modeling, data analysis",
              "C-DAC supercomputers (PARAM series by Dr. Vijay Bhatkar)"
            ],
            "practiceSet": "Exercise 10.3",
            "theorems": [],
            "problemSet": "Problem Set 10"
          }
        ]
      },
      {
        "number": "11",
        "name": "Reflection of Light",
        "topics": [
          {
            "number": "11.1",
            "name": "Mirrors: Plane Mirrors & Image Formation",
            "topicCode": "MH-9-SCIT-11-11.1",
            "subtopics": [
              "Laws of reflection",
              "Plane mirror image characteristics: virtual, erect, laterally inverted, same size, equal object-image distance"
            ],
            "practiceSet": "Exercise 11.1",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.2",
            "name": "Spherical Mirrors: Concave vs Convex Mirror Terminology",
            "topicCode": "MH-9-SCIT-11-11.2",
            "subtopics": [
              "Pole (P), Centre of Curvature (C), Radius of Curvature (R), Principal Focus (F), Focal Length (f = R/2), Principal Axis"
            ],
            "practiceSet": "Exercise 11.2",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.3",
            "name": "Ray Diagrams for Concave Mirror at Different Object Positions",
            "topicCode": "MH-9-SCIT-11-11.3",
            "subtopics": [
              "Object at infinity, beyond C, at C, between C and F, at F, between F and P",
              "Real/inverted vs virtual/erect image nature"
            ],
            "practiceSet": "Exercise 11.3",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.4",
            "name": "Ray Diagrams for Convex Mirror & Uses",
            "topicCode": "MH-9-SCIT-11-11.4",
            "subtopics": [
              "Diminished virtual erect image",
              "Rear-view mirrors in vehicles, security surveillance"
            ],
            "practiceSet": "Exercise 11.4",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.5",
            "name": "Mirror Formula (1/f = 1/v + 1/u) & Magnification (m = -v/u)",
            "topicCode": "MH-9-SCIT-11-11.5",
            "subtopics": [
              "Cartesian sign convention rules",
              "Solving numerical ray optics problems"
            ],
            "practiceSet": "Exercise 11.5",
            "theorems": [],
            "problemSet": "Problem Set 11"
          }
        ]
      },
      {
        "number": "12",
        "name": "Study of Sound",
        "topics": [
          {
            "number": "12.1",
            "name": "Sound Waves: Velocity of Sound Formula (v = ν * λ)",
            "topicCode": "MH-9-SCIT-12-12.1",
            "subtopics": [
              "Longitudinal wave nature: compressions and rarefactions",
              "Factors affecting velocity of sound in gases: Density (v ∝ 1/√ρ), Temperature (v ∝ √T), Molecular weight (v ∝ 1/√M)"
            ],
            "practiceSet": "Exercise 12.1",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.2",
            "name": "Audible, Infrasonic and Ultrasonic Sound",
            "topicCode": "MH-9-SCIT-12-12.2",
            "subtopics": [
              "Audible range 20 Hz to 20 kHz",
              "Infrasound (<20 Hz - whales, elephants, earthquake waves)",
              "Ultrasound (>20 kHz - bats, dolphins, medical SONAR)"
            ],
            "practiceSet": "Exercise 12.2",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.3",
            "name": "Reflection of Sound, Echo & Reverberation",
            "topicCode": "MH-9-SCIT-12-12.3",
            "subtopics": [
              "Echo condition: minimum 17.2 m obstacle distance at 22°C",
              "Acoustics of buildings and reverberation control"
            ],
            "practiceSet": "Exercise 12.3",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.4",
            "name": "SONAR Technique & Medical Ultrasonography",
            "topicCode": "MH-9-SCIT-12-12.4",
            "subtopics": [
              "Transmitter and detector underwater echo sounding (2d = v * t)",
              "Ultrasound scanning in obstetric and cardiac medicine"
            ],
            "practiceSet": "Exercise 12.4",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.5",
            "name": "Structure of Human Ear",
            "topicCode": "MH-9-SCIT-12-12.5",
            "subtopics": [
              "Pinna, auditory meatus, tympanic membrane, ossicles (hammer, anvil, stirrup), cochlea with sensory hair cells"
            ],
            "practiceSet": "Exercise 12.5",
            "theorems": [],
            "problemSet": "Problem Set 12"
          }
        ]
      },
      {
        "number": "13",
        "name": "Carbon: An Important Element",
        "topics": [
          {
            "number": "13.1",
            "name": "Occurrence, Properties & Tetravalency of Carbon",
            "topicCode": "MH-9-SCIT-13-13.1",
            "subtopics": [
              "Atomic number 6, electronic configuration (2,4), covalent bonding"
            ],
            "practiceSet": "Exercise 13.1",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.2",
            "name": "Allotropes of Carbon: Crystalline (Diamond, Graphite, Fullerenes)",
            "topicCode": "MH-9-SCIT-13-13.2",
            "subtopics": [
              "Diamond: 3D tetrahedral network, hardest substance, non-conductor",
              "Graphite: hexagonal layered structure, soft, lubricant, good electrical conductor (delocalized electrons)",
              "Fullerenes: Buckyball C60 geodesic cage structure (Buckminster Fuller)"
            ],
            "practiceSet": "Exercise 13.2",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.3",
            "name": "Non-Crystalline / Amorphous Allotropes of Carbon",
            "topicCode": "MH-9-SCIT-13-13.3",
            "subtopics": [
              "Coal (Anthracite, Bituminous, Lignite, Peat)",
              "Coke, Charcoal, Lamp black / carbon black"
            ],
            "practiceSet": "Exercise 13.3",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.4",
            "name": "Hydrocarbons: Saturated (Alkanes) vs Unsaturated (Alkenes & Alkynes)",
            "topicCode": "MH-9-SCIT-13-13.4",
            "subtopics": [
              "Methane (CH4), Ethane (C2H6)",
              "Ethene (C2H4), Ethyne (C2H2)"
            ],
            "practiceSet": "Exercise 13.4",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.5",
            "name": "Carbon Dioxide (CO2) & Methane (CH4) Properties & Fire Extinguishers",
            "topicCode": "MH-9-SCIT-13-13.5",
            "subtopics": [
              "CO2 preparation and lime water test (Ca(OH)2 + CO2 -> CaCO3 + H2O)",
              "Dry ice and fire extinguisher mechanism",
              "Methane marsh gas biogas production"
            ],
            "practiceSet": "Exercise 13.5",
            "theorems": [],
            "problemSet": "Problem Set 13"
          }
        ]
      },
      {
        "number": "14",
        "name": "Substances in Common Use",
        "topics": [
          {
            "number": "14.1",
            "name": "Important Salts: Common Salt (NaCl), Baking Soda (NaHCO3), Washing Soda (Na2CO3·10H2O)",
            "topicCode": "MH-9-SCIT-14-14.1",
            "subtopics": [
              "Preparation, properties, and household/industrial uses"
            ],
            "practiceSet": "Exercise 14.1",
            "theorems": [],
            "problemSet": "Problem Set 14"
          },
          {
            "number": "14.2",
            "name": "Bleaching Powder (CaOCl2) & Plaster of Paris (CaSO4·1/2H2O)",
            "topicCode": "MH-9-SCIT-14-14.2",
            "subtopics": [
              "Disinfection of drinking water with bleaching powder",
              "POP casting of broken bones and statue sculpting"
            ],
            "practiceSet": "Exercise 14.2",
            "theorems": [],
            "problemSet": "Problem Set 14"
          },
          {
            "number": "14.3",
            "name": "Radioactive Substances & Alpha, Beta, Gamma Rays",
            "topicCode": "MH-9-SCIT-14-14.3",
            "subtopics": [
              "Natural radioactivity (Henry Becquerel, Marie Curie)",
              "Properties of α (He²⁺), β (high speed e⁻), γ (electromagnetic radiation)",
              "Industrial, agricultural, medical applications (Cobalt-60, Iodine-131, Phosphorus-32) and radiation hazards"
            ],
            "practiceSet": "Exercise 14.3",
            "theorems": [],
            "problemSet": "Problem Set 14"
          },
          {
            "number": "14.4",
            "name": "Chemical Substances in Day-to-Day Life (Food Colors, Dyes, Artificial Sweeteners, Deodorants, Teflon, Ceramics)",
            "topicCode": "MH-9-SCIT-14-14.4",
            "subtopics": [
              "Food adulteration dyes",
              "Teflon non-stick cookware coating",
              "Ceramics and porcelain bone china"
            ],
            "practiceSet": "Exercise 14.4",
            "theorems": [],
            "problemSet": "Problem Set 14"
          }
        ]
      },
      {
        "number": "15",
        "name": "Life Processes in Living Organisms",
        "topics": [
          {
            "number": "15.1",
            "name": "Transportation in Plants: Xylem (Water) & Phloem (Food Translocation)",
            "topicCode": "MH-9-SCIT-15-15.1",
            "subtopics": [
              "Root pressure theory",
              "Transpiration pull mechanism through stomata",
              "Phloem transport using ATP energy"
            ],
            "practiceSet": "Exercise 15.1",
            "theorems": [],
            "problemSet": "Problem Set 15"
          },
          {
            "number": "15.2",
            "name": "Excretion: Excretion in Plants & Excretion in Humans",
            "topicCode": "MH-9-SCIT-15-15.2",
            "subtopics": [
              "Plant excretion: shed leaves, resins, gums, calcium oxalate raphides",
              "Human excretory system: Kidney nephron anatomy (Bowman capsule, glomerulus, renal tubule), urine formation, Dialysis artificial kidney"
            ],
            "practiceSet": "Exercise 15.2",
            "theorems": [],
            "problemSet": "Problem Set 15"
          },
          {
            "number": "15.3",
            "name": "Coordination in Plants (Tropic Movements & Phytohormones)",
            "topicCode": "MH-9-SCIT-15-15.3",
            "subtopics": [
              "Phototropism, Geotropism, Hydrotropism, Thigmotropism",
              "Plant hormones: Auxin, Gibberellin, Cytokinin, Abscisic acid (growth inhibitor)"
            ],
            "practiceSet": "Exercise 15.3",
            "theorems": [],
            "problemSet": "Problem Set 15"
          },
          {
            "number": "15.4",
            "name": "Coordination in Humans: Nervous System (CNS, PNS, ANS)",
            "topicCode": "MH-9-SCIT-15-15.4",
            "subtopics": [
              "Brain anatomy: Cerebrum, Cerebellum, Medulla oblongata, Pons",
              "Spinal cord and Reflex arc pathway"
            ],
            "practiceSet": "Exercise 15.4",
            "theorems": [],
            "problemSet": "Problem Set 15"
          },
          {
            "number": "15.5",
            "name": "Endocrine System in Humans & Hormones",
            "topicCode": "MH-9-SCIT-15-15.5",
            "subtopics": [
              "Pituitary, Thyroid (Thyroxine), Parathyroid, Pancreas (Insulin/Glucagon), Adrenal (Adrenaline), Testes, Ovaries"
            ],
            "practiceSet": "Exercise 15.5",
            "theorems": [],
            "problemSet": "Problem Set 15"
          }
        ]
      },
      {
        "number": "16",
        "name": "Heredity and Variation",
        "topics": [
          {
            "number": "16.1",
            "name": "Inheritance, Chromosomes Types (Metacentric, Submetacentric, Acrocentric, Telocentric)",
            "topicCode": "MH-9-SCIT-16-16.1",
            "subtopics": [
              "Centromere position and arms ratio",
              "Homologous vs heterologous chromosomes, Autosomes vs Sex chromosomes"
            ],
            "practiceSet": "Exercise 16.1",
            "theorems": [],
            "problemSet": "Problem Set 16"
          },
          {
            "number": "16.2",
            "name": "DNA (Deoxyribonucleic Acid) - Watson & Crick Double Helix Model",
            "topicCode": "MH-9-SCIT-16-16.2",
            "subtopics": [
              "Nucleotides: Deoxyribose sugar, Phosphate group, Nitrogen bases (Adenine-Thymine, Guanine-Cytosine)",
              "Gene definition as functional segment of DNA",
              "RNA types: mRNA, tRNA, rRNA"
            ],
            "practiceSet": "Exercise 16.2",
            "theorems": [],
            "problemSet": "Problem Set 16"
          },
          {
            "number": "16.3",
            "name": "Mendel Laws of Inheritance: Monohybrid Cross (3:1 Phenotype, 1:2:1 Genotype)",
            "topicCode": "MH-9-SCIT-16-16.3",
            "subtopics": [
              "Gregor Johann Mendel experiments on Pisum sativum garden pea",
              "Law of Segregation"
            ],
            "practiceSet": "Exercise 16.3",
            "theorems": [
              "Law of Segregation"
            ],
            "problemSet": "Problem Set 16"
          },
          {
            "number": "16.4",
            "name": "Mendel Dihybrid Cross (9:3:3:1 Ratio) & Law of Independent Assortment",
            "topicCode": "MH-9-SCIT-16-16.4",
            "subtopics": [
              "Punnett square cross of round-yellow and wrinkled-green seeds"
            ],
            "practiceSet": "Exercise 16.4",
            "theorems": [
              "Law of Independent Assortment"
            ],
            "problemSet": "Problem Set 16"
          },
          {
            "number": "16.5",
            "name": "Genetic Disorders: Chromosomal (Down, Turner, Klinefelter) & Monogenic (Sickle Cell Anemia, Hemophilia)",
            "topicCode": "MH-9-SCIT-16-16.5",
            "subtopics": [
              "Down syndrome (Trisomy 21 - 47 chromosomes)",
              "Turner syndrome (44+XO)",
              "Klinefelter syndrome (44+XXY)",
              "Sickle cell anemia (HbA vs HbS genotype, red blood cell sickle deformity)"
            ],
            "practiceSet": "Exercise 16.5",
            "theorems": [],
            "problemSet": "Problem Set 16"
          }
        ]
      },
      {
        "number": "17",
        "name": "Introduction to Biotechnology",
        "topics": [
          {
            "number": "17.1",
            "name": "Tissue Culture: Technique, Nutrient Medium & Explants",
            "topicCode": "MH-9-SCIT-17-17.1",
            "subtopics": [
              "Totipotency concept",
              "Aseptic micropropagation, callogenesis, organogenesis, hardening"
            ],
            "practiceSet": "Exercise 17.1",
            "theorems": [],
            "problemSet": "Problem Set 17"
          },
          {
            "number": "17.2",
            "name": "Agricultural Biotechnology: GM Crops (Bt Cotton, Golden Rice) & Biofertilisers",
            "topicCode": "MH-9-SCIT-17-17.2",
            "subtopics": [
              "Genetically Modified crops resistance against bollworm pest",
              "Golden Rice with Vitamin A precursor beta-carotene",
              "Biofertilisers (Azotobacter, Nostoc, Anabaena)"
            ],
            "practiceSet": "Exercise 17.2",
            "theorems": [],
            "problemSet": "Problem Set 17"
          },
          {
            "number": "17.3",
            "name": "Agri-tourism, Animal Husbandry & Sericulture",
            "topicCode": "MH-9-SCIT-17-17.3",
            "subtopics": [
              "Preserving biodiversity and rural tourism",
              "Cattle breeding and artificial insemination",
              "Silk production from silkworm (Bombyx mori) and mulberry cultivation"
            ],
            "practiceSet": "Exercise 17.3",
            "theorems": [],
            "problemSet": "Problem Set 17"
          }
        ]
      },
      {
        "number": "18",
        "name": "Observing Space: Telescopes",
        "topics": [
          {
            "number": "18.1",
            "name": "Forms of Light & Electromagnetic Spectrum",
            "topicCode": "MH-9-SCIT-18-18.1",
            "subtopics": [
              "Visible light (400-800 nm), Radio waves, Micro waves, Infrared, UV, X-rays, Gamma rays"
            ],
            "practiceSet": "Exercise 18.1",
            "theorems": [],
            "problemSet": "Problem Set 18"
          },
          {
            "number": "18.2",
            "name": "Optical Telescopes: Refracting (Galilean, Keplerian) & Reflecting (Newtonian, Cassegrain)",
            "topicCode": "MH-9-SCIT-18-18.2",
            "subtopics": [
              "Refracting telescope using lenses and chromatic aberration defect",
              "Reflecting telescope using parabolic concave mirrors (Newtonian and Cassegrain designs)"
            ],
            "practiceSet": "Exercise 18.2",
            "theorems": [],
            "problemSet": "Problem Set 18"
          },
          {
            "number": "18.3",
            "name": "Radio Telescopes: GMRT (Giant Metrewave Radio Telescope at Pune)",
            "topicCode": "MH-9-SCIT-18-18.3",
            "subtopics": [
              "GMRT array of 30 parabolic dishes at Narayangaon near Pune (Prof. Govind Swarup)"
            ],
            "practiceSet": "Exercise 18.3",
            "theorems": [],
            "problemSet": "Problem Set 18"
          },
          {
            "number": "18.4",
            "name": "Space Telescopes: Hubble Space Telescope & Chandra X-ray Observatory",
            "topicCode": "MH-9-SCIT-18-18.4",
            "subtopics": [
              "Atmospheric absorption and distortion avoidance",
              "Hubble visual telescope and Chandra X-ray space observatory (Subrahmanyan Chandrasekhar)"
            ],
            "practiceSet": "Exercise 18.4",
            "theorems": [],
            "problemSet": "Problem Set 18"
          }
        ]
      }
    ]
  },
  {
    "docId": "cbse_10_math",
    "board": "CBSE",
    "boardCode": "CBSE",
    "class": "10",
    "subject": "Mathematics",
    "subjectCode": "MATH",
    "chapters": [
      {
        "number": "1",
        "name": "Real Numbers",
        "topics": [
          {
            "number": "1.1",
            "name": "Fundamental Theorem of Arithmetic & Prime Factorisation",
            "topicCode": "CBSE-10-MATH-1-1.1",
            "subtopics": [
              "Statement: Every composite number uniquely expressed as product of primes",
              "Finding HCF and LCM using prime factors",
              "Formula: HCF(a, b) * LCM(a, b) = a * b"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [
              "Fundamental Theorem of Arithmetic"
            ],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Revisiting Irrational Numbers & Proof of Irrationality",
            "topicCode": "CBSE-10-MATH-1-1.2",
            "subtopics": [
              "Theorem: If p divides a², then p divides a",
              "Rigorous proofs of irrationality for √2, √3, √5, 3+2√5 by contradiction"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [
              "Irrationality Theorem"
            ],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Decimal Representation of Rational Numbers (2ⁿ5ᵐ denominator rule)",
            "topicCode": "CBSE-10-MATH-1-1.3",
            "subtopics": [
              "Terminating decimal condition: denominator in 2ⁿ5ᵐ form",
              "Non-terminating recurring decimal criteria"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Polynomials",
        "topics": [
          {
            "number": "2.1",
            "name": "Geometric Meaning of Zeroes of a Polynomial",
            "topicCode": "CBSE-10-MATH-2-2.1",
            "subtopics": [
              "Parabolic graphs of quadratic polynomials (upward/downward opening)",
              "Number of zeroes = number of X-axis intersections"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Relationship Between Zeroes & Coefficients of Quadratic Polynomial",
            "topicCode": "CBSE-10-MATH-2-2.2",
            "subtopics": [
              "Sum of zeroes: α + β = -b/a",
              "Product of zeroes: α * β = c/a",
              "Forming quadratic polynomial: k[x² - (α+β)x + αβ]"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Zeroes & Coefficients of Cubic Polynomials",
            "topicCode": "CBSE-10-MATH-2-2.3",
            "subtopics": [
              "Sum of zeroes: α + β + γ = -b/a",
              "Sum of products in pairs: αβ + βγ + γα = c/a",
              "Product of zeroes: αβγ = -d/a"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Division Algorithm for Polynomials & Finding Remaining Zeroes",
            "topicCode": "CBSE-10-MATH-2-2.4",
            "subtopics": [
              "p(x) = g(x) * q(x) + r(x)",
              "Finding remaining zeroes when two irrational or complex zeroes are given (e.g. ±√5/3)"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Pair of Linear Equations in Two Variables",
        "topics": [
          {
            "number": "3.1",
            "name": "Graphical Method & Consistency Conditions (a1/a2 vs b1/b2 vs c1/c2)",
            "topicCode": "CBSE-10-MATH-3-3.1",
            "subtopics": [
              "Intersecting lines (unique solution, consistent: a1/a2 != b1/b2)",
              "Parallel lines (no solution, inconsistent: a1/a2 = b1/b2 != c1/c2)",
              "Coincident lines (infinitely many solutions, dependent consistent: a1/a2 = b1/b2 = c1/c2)"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Algebraic Method: Substitution Method",
            "topicCode": "CBSE-10-MATH-3-3.2",
            "subtopics": [
              "Expressing one variable in terms of the other and substituting"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Algebraic Method: Elimination Method by Equating Coefficients",
            "topicCode": "CBSE-10-MATH-3-3.3",
            "subtopics": [
              "Multiplying equations by suitable constants and adding/subtracting"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Equations Reducible to Linear Form (1/x, 1/y Substitutions)",
            "topicCode": "CBSE-10-MATH-3-3.4",
            "subtopics": [
              "Variable denominators substitution method u = 1/x, v = 1/y"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.5",
            "name": "Applied Word Problems (Upstream/Downstream, Time-Work, Digits, Ages, Geometry)",
            "topicCode": "CBSE-10-MATH-3-3.5",
            "subtopics": [
              "Upstream speed (x - y) and downstream speed (x + y)",
              "Fixed charge and per km charge taxi problems",
              "Two-digit number reversal problems"
            ],
            "practiceSet": "Exercise 3.5",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Quadratic Equations",
        "topics": [
          {
            "number": "4.1",
            "name": "Standard Form & Identifying Quadratic Equations",
            "topicCode": "CBSE-10-MATH-4-4.1",
            "subtopics": [
              "Standard form: ax² + bx + c = 0 (a != 0)",
              "Formulating quadratic equations from verbal descriptions"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Solving Quadratic Equations by Factorisation (Splitting Middle Term)",
            "topicCode": "CBSE-10-MATH-4-4.2",
            "subtopics": [
              "Finding roots by factoring quadratic trinomials"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Solving by Quadratic Formula (Shreedharacharya Formula)",
            "topicCode": "CBSE-10-MATH-4-4.3",
            "subtopics": [
              "Quadratic formula derivation: x = [-b ± √(b² - 4ac)] / (2a)"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.4",
            "name": "Nature of Roots & Discriminant (D = b² - 4ac)",
            "topicCode": "CBSE-10-MATH-4-4.4",
            "subtopics": [
              "D > 0: Two distinct real roots",
              "D = 0: Two equal real roots",
              "D < 0: No real roots / imaginary roots",
              "Finding unknown parameter k for equal roots"
            ],
            "practiceSet": "Exercise 4.4",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.5",
            "name": "Applied Word Problems (Speed-Distance, Pipes-Cisterns, Areas)",
            "topicCode": "CBSE-10-MATH-4-4.5",
            "subtopics": [
              "Train speed decrease/increase problems",
              "Two water taps filling a pool together problems"
            ],
            "practiceSet": "Exercise 4.5",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Arithmetic Progressions",
        "topics": [
          {
            "number": "5.1",
            "name": "AP Definition, First Term (a) & Common Difference (d)",
            "topicCode": "CBSE-10-MATH-5-5.1",
            "subtopics": [
              "Arithmetic progression sequence: a, a+d, a+2d, ...",
              "Determining whether a given sequence forms an AP"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "nth Term of an AP Formula (a_n = a + (n - 1)d)",
            "topicCode": "CBSE-10-MATH-5-5.2",
            "subtopics": [
              "Finding specific terms, number of terms n, and first negative term of AP",
              "nth term from the end formula: l - (n - 1)d"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Sum of First n Terms of an AP (S_n = n/2[2a + (n - 1)d])",
            "topicCode": "CBSE-10-MATH-5-5.3",
            "subtopics": [
              "Sum formula with last term: S_n = n/2(a + l)",
              "Relation between sum and nth term: a_n = S_n - S_(n-1)"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.4",
            "name": "Applied Real-Life Word Problems on AP Sums",
            "topicCode": "CBSE-10-MATH-5-5.4",
            "subtopics": [
              "Savings ladders, logs stacking, potato race distances, loan repayments"
            ],
            "practiceSet": "Exercise 5.4",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Triangles",
        "topics": [
          {
            "number": "6.1",
            "name": "Similar Figures & Criteria of Similarity (AAA, SSS, SAS)",
            "topicCode": "CBSE-10-MATH-6-6.1",
            "subtopics": [
              "Definition of similarity (equiangular and proportional sides)",
              "Equiangular triangles (AAA / AA similarity)",
              "Proportional sides (SSS similarity)",
              "Ratio of two sides and included angle (SAS similarity)"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Basic Proportionality Theorem (Thales Theorem) & Its Converse",
            "topicCode": "CBSE-10-MATH-6-6.2",
            "subtopics": [
              "Statement and geometric proof: Line drawn parallel to one side dividing other two sides in same ratio",
              "Converse of BPT theorem and proofs"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [
              "Basic Proportionality Theorem",
              "Converse of Basic Proportionality Theorem"
            ],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Areas of Similar Triangles Theorem",
            "topicCode": "CBSE-10-MATH-6-6.3",
            "subtopics": [
              "Ratio of areas of two similar triangles = square of ratio of corresponding sides = square of altitudes = square of medians"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [
              "Areas of Similar Triangles Theorem"
            ],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.4",
            "name": "Pythagoras Theorem & Its Converse",
            "topicCode": "CBSE-10-MATH-6-6.4",
            "subtopics": [
              "Theorem and geometric proof using similarity in right triangle",
              "Converse of Pythagoras theorem",
              "Applications in geometric calculations and ladder problems"
            ],
            "practiceSet": "Exercise 6.4",
            "theorems": [
              "Pythagoras Theorem",
              "Converse of Pythagoras Theorem"
            ],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Coordinate Geometry",
        "topics": [
          {
            "number": "7.1",
            "name": "Distance Formula: d = √[(x2 - x1)² + (y2 - y1)²]",
            "topicCode": "CBSE-10-MATH-7-7.1",
            "subtopics": [
              "Derivation of distance formula from Pythagoras theorem",
              "Collinear points test and classifying triangles/quadrilaterals (equilateral, isosceles, square, rhombus, parallelogram)"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Section Formula for Internal Division: (mx2+nx1)/(m+n)",
            "topicCode": "CBSE-10-MATH-7-7.2",
            "subtopics": [
              "Coordinates of point dividing line segment in ratio m1:m2",
              "Finding ratio when dividing point coordinates are given",
              "Midpoint formula: ((x1+x2)/2, (y1+y2)/2)",
              "Points of trisection"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Centroid of a Triangle Formula: ((x1+x2+x3)/3, (y1+y2+y3)/3)",
            "topicCode": "CBSE-10-MATH-7-7.3",
            "subtopics": [
              "Coordinates of point of concurrence of medians"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.4",
            "name": "Area of Triangle by Coordinates Formula",
            "topicCode": "CBSE-10-MATH-7-7.4",
            "subtopics": [
              "Area = 1/2 |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|",
              "Condition for collinearity of three points: Area = 0"
            ],
            "practiceSet": "Exercise 7.4",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      },
      {
        "number": "8",
        "name": "Introduction to Trigonometry",
        "topics": [
          {
            "number": "8.1",
            "name": "Trigonometric Ratios of Acute Angle (sin, cos, tan, cot, sec, cosec)",
            "topicCode": "CBSE-10-MATH-8-8.1",
            "subtopics": [
              "Definitions in right triangle (Opposite, Adjacent, Hypotenuse)",
              "Reciprocal relations: cosec = 1/sin, sec = 1/cos, cot = 1/tan = cos/sin"
            ],
            "practiceSet": "Exercise 8.1",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.2",
            "name": "Trigonometric Ratios of Specific Angles (0°, 30°, 45°, 60°, 90°)",
            "topicCode": "CBSE-10-MATH-8-8.2",
            "subtopics": [
              "Values table derivation",
              "Evaluating algebraic trigonometric expressions"
            ],
            "practiceSet": "Exercise 8.2",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.3",
            "name": "Trigonometric Ratios of Complementary Angles",
            "topicCode": "CBSE-10-MATH-8-8.3",
            "subtopics": [
              "sin(90-θ) = cos θ, cos(90-θ) = sin θ",
              "tan(90-θ) = cot θ, cot(90-θ) = tan θ",
              "sec(90-θ) = cosec θ, cosec(90-θ) = sec θ"
            ],
            "practiceSet": "Exercise 8.3",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.4",
            "name": "Trigonometric Identities & Rigorous Algebraic Proofs",
            "topicCode": "CBSE-10-MATH-8-8.4",
            "subtopics": [
              "sin²θ + cos²θ = 1",
              "1 + tan²θ = sec²θ",
              "1 + cot²θ = cosec²θ",
              "Proving complex trigonometric identities"
            ],
            "practiceSet": "Exercise 8.4",
            "theorems": [],
            "problemSet": "Problem Set 8"
          }
        ]
      },
      {
        "number": "9",
        "name": "Some Applications of Trigonometry (Heights and Distances)",
        "topics": [
          {
            "number": "9.1",
            "name": "Line of Sight, Angle of Elevation & Angle of Depression",
            "topicCode": "CBSE-10-MATH-9-9.1",
            "subtopics": [
              "Definitions and horizontal reference lines",
              "Alternate interior angles relation for angle of depression"
            ],
            "practiceSet": "Exercise 9.1",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.2",
            "name": "Single Triangle Height and Distance Problems",
            "topicCode": "CBSE-10-MATH-9-9.2",
            "subtopics": [
              "Direct height of tower, tree broken by storm, kite string length"
            ],
            "practiceSet": "Exercise 9.2",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.3",
            "name": "Multi-Triangle & Dual Observer Word Problems",
            "topicCode": "CBSE-10-MATH-9-9.3",
            "subtopics": [
              "Two ships approaching lighthouse from opposite sides",
              "Pedestal and statue heights, cloud reflection in lake problems"
            ],
            "practiceSet": "Exercise 9.3",
            "theorems": [],
            "problemSet": "Problem Set 9"
          }
        ]
      },
      {
        "number": "10",
        "name": "Circles",
        "topics": [
          {
            "number": "10.1",
            "name": "Tangent to a Circle & Point of Contact",
            "topicCode": "CBSE-10-MATH-10-10.1",
            "subtopics": [
              "Secant vs tangent",
              "Number of tangents from point inside, on, and outside circle"
            ],
            "practiceSet": "Exercise 10.1",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.2",
            "name": "Tangent Perpendicular to Radius Theorem",
            "topicCode": "CBSE-10-MATH-10-10.2",
            "subtopics": [
              "Theorem and proof: Tangent at any point is perpendicular to radius through point of contact"
            ],
            "practiceSet": "Exercise 10.2",
            "theorems": [
              "Tangent-Radius Perpendicularity Theorem"
            ],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.3",
            "name": "Lengths of Tangents from External Point Theorem",
            "topicCode": "CBSE-10-MATH-10-10.3",
            "subtopics": [
              "Theorem and proof: Tangents drawn from external point to a circle are equal in length",
              "Inscribed circles in quadrilaterals (AB + CD = AD + BC)"
            ],
            "practiceSet": "Exercise 10.3",
            "theorems": [
              "Tangent Segments Equality Theorem"
            ],
            "problemSet": "Problem Set 10"
          }
        ]
      },
      {
        "number": "11",
        "name": "Areas Related to Circles",
        "topics": [
          {
            "number": "11.1",
            "name": "Perimeter (Circumference = 2πr) & Area of Circle (πr²)",
            "topicCode": "CBSE-10-MATH-11-11.1",
            "subtopics": [
              "Pi (π) as ratio of circumference to diameter",
              "Distance covered in wheel revolutions"
            ],
            "practiceSet": "Exercise 11.1",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.2",
            "name": "Area of Sector of a Circle (Major & Minor Sector)",
            "topicCode": "CBSE-10-MATH-11-11.2",
            "subtopics": [
              "Length of arc: l = (θ / 360) * 2πr",
              "Area of sector: A = (θ / 360) * πr² = 1/2 * l * r"
            ],
            "practiceSet": "Exercise 11.2",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.3",
            "name": "Area of Segment of a Circle (Major & Minor Segment)",
            "topicCode": "CBSE-10-MATH-11-11.3",
            "subtopics": [
              "Area of segment = Area of sector - Area of corresponding triangle",
              "Triangle area with angle θ (1/2 r² sin θ)"
            ],
            "practiceSet": "Exercise 11.3",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.4",
            "name": "Areas of Combinations of Plane Figures",
            "topicCode": "CBSE-10-MATH-11-11.4",
            "subtopics": [
              "Designs in circles, squares with semicircular ends, shaded region problem solving"
            ],
            "practiceSet": "Exercise 11.4",
            "theorems": [],
            "problemSet": "Problem Set 11"
          }
        ]
      },
      {
        "number": "12",
        "name": "Surface Areas and Volumes",
        "topics": [
          {
            "number": "12.1",
            "name": "Surface Area of Combination of Solids",
            "topicCode": "CBSE-10-MATH-12-12.1",
            "subtopics": [
              "Toy (cone mounted on hemisphere), circus tent (cylinder with conical roof), capsule (cylinder with two hemispherical ends)"
            ],
            "practiceSet": "Exercise 12.1",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.2",
            "name": "Volume of Combination of Solids",
            "topicCode": "CBSE-10-MATH-12-12.2",
            "subtopics": [
              "Gulab jamun sugar syrup volume, decorative solid shapes"
            ],
            "practiceSet": "Exercise 12.2",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.3",
            "name": "Conversion of Solid from One Shape to Another",
            "topicCode": "CBSE-10-MATH-12-12.3",
            "subtopics": [
              "Melting spheres into cylinder, digging well and spreading embankment",
              "Volume invariance principle"
            ],
            "practiceSet": "Exercise 12.3",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.4",
            "name": "Frustum of a Right Circular Cone",
            "topicCode": "CBSE-10-MATH-12-12.4",
            "subtopics": [
              "Slant height of frustum: l = √[h² + (r1 - r2)²]",
              "CSA = πl(r1 + r2), TSA = πl(r1 + r2) + πr1² + πr2²",
              "Volume = 1/3 * πh(r1² + r2² + r1*r2)",
              "Drinking glass and bucket problems"
            ],
            "practiceSet": "Exercise 12.4",
            "theorems": [],
            "problemSet": "Problem Set 12"
          }
        ]
      },
      {
        "number": "13",
        "name": "Statistics",
        "topics": [
          {
            "number": "13.1",
            "name": "Mean of Grouped Data: Direct Method (Σ(f*x) / Σf)",
            "topicCode": "CBSE-10-MATH-13-13.1",
            "subtopics": [
              "Class marks and direct tabulation method"
            ],
            "practiceSet": "Exercise 13.1",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.2",
            "name": "Mean of Grouped Data: Assumed Mean Method & Step-Deviation Method",
            "topicCode": "CBSE-10-MATH-13-13.2",
            "subtopics": [
              "Assumed mean (a) and deviations d_i = x_i - a: X̄ = a + (Σf*d / Σf)",
              "Step deviation u_i = (x_i - a)/h: X̄ = a + h * (Σf*u / Σf)"
            ],
            "practiceSet": "Exercise 13.2",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.3",
            "name": "Mode of Grouped Data Formula: l + [(f1 - f0)/(2f1 - f0 - f2)] * h",
            "topicCode": "CBSE-10-MATH-13-13.3",
            "subtopics": [
              "Modal class identification",
              "Calculation of modal value"
            ],
            "practiceSet": "Exercise 13.3",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.4",
            "name": "Median of Grouped Data Formula: l + [((N/2 - cf)/f)] * h",
            "topicCode": "CBSE-10-MATH-13-13.4",
            "subtopics": [
              "Cumulative frequency table and median class",
              "Finding missing frequencies x and y when median is known"
            ],
            "practiceSet": "Exercise 13.4",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.5",
            "name": "Empirical Relationship Between Measures of Central Tendency & Ogives",
            "topicCode": "CBSE-10-MATH-13-13.5",
            "subtopics": [
              "Empirical formula: 3 Median = Mode + 2 Mean",
              "Less-than and more-than ogives intersection gives median"
            ],
            "practiceSet": "Exercise 13.5",
            "theorems": [],
            "problemSet": "Problem Set 13"
          }
        ]
      },
      {
        "number": "14",
        "name": "Probability",
        "topics": [
          {
            "number": "14.1",
            "name": "Theoretical (Classical) Probability Definition: P(E) = n(E) / n(S)",
            "topicCode": "CBSE-10-MATH-14-14.1",
            "subtopics": [
              "Equally likely outcomes",
              "Range of probability: 0 <= P(E) <= 1",
              "Sure event (P=1) and Impossible event (P=0)"
            ],
            "practiceSet": "Exercise 14.1",
            "theorems": [],
            "problemSet": "Problem Set 14"
          },
          {
            "number": "14.2",
            "name": "Complementary Events: P(E) + P(not E) = 1",
            "topicCode": "CBSE-10-MATH-14-14.2",
            "subtopics": [
              "Elementary events and sum of probabilities of all elementary events equals 1"
            ],
            "practiceSet": "Exercise 14.2",
            "theorems": [],
            "problemSet": "Problem Set 14"
          },
          {
            "number": "14.3",
            "name": "Standard Probability Experiments (Coins, Dice, Cards & Marbles)",
            "topicCode": "CBSE-10-MATH-14-14.3",
            "subtopics": [
              "Tossing 2 and 3 coins sample space",
              "Throwing a pair of dice (36 outcomes)",
              "52-card deck distribution (Spades, Hearts, Diamonds, Clubs, Face cards)"
            ],
            "practiceSet": "Exercise 14.3",
            "theorems": [],
            "problemSet": "Problem Set 14"
          }
        ]
      }
    ]
  },
  {
    "docId": "cbse_10_sci",
    "board": "CBSE",
    "boardCode": "CBSE",
    "class": "10",
    "subject": "Science",
    "subjectCode": "SCI",
    "chapters": [
      {
        "number": "1",
        "name": "Chemical Reactions and Equations",
        "topics": [
          {
            "number": "1.1",
            "name": "Chemical Equations & Balancing Chemical Reactions",
            "topicCode": "CBSE-10-SCI-1-1.1",
            "subtopics": [
              "Word equations vs chemical equations",
              "Law of conservation of mass in balancing",
              "Physical state notation: (s), (l), (g), (aq) and catalysts/heat"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Combination Reactions & Exothermic Reactions",
            "topicCode": "CBSE-10-SCI-1-1.2",
            "subtopics": [
              "Formation of single product from two or more reactants (CaO + H2O -> Ca(OH)2 quicklime to slaked lime)",
              "Exothermic reactions: Burning of natural gas, respiration"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Decomposition Reactions (Thermal, Electrolytic & Photolytic)",
            "topicCode": "CBSE-10-SCI-1-1.3",
            "subtopics": [
              "Thermal decomposition (FeSO4 heating, CaCO3 -> CaO + CO2, Pb(NO3)2 brown fumes of NO2)",
              "Electrolytic decomposition of water (2:1 H2 to O2 volume ratio)",
              "Photolytic decomposition of AgCl and AgBr in black and white photography",
              "Endothermic reactions"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Displacement & Double Displacement Reactions (Precipitation)",
            "topicCode": "CBSE-10-SCI-1-1.4",
            "subtopics": [
              "Displacement: Fe + CuSO4 -> FeSO4 + Cu (Reactivity series)",
              "Double displacement: Na2SO4 + BaCl2 -> BaSO4 (white precipitate) + 2NaCl"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.5",
            "name": "Oxidation, Reduction, Redox Reactions & Corrosion/Rancidity",
            "topicCode": "CBSE-10-SCI-1-1.5",
            "subtopics": [
              "Oxidation: gain of oxygen / loss of hydrogen; Reduction: gain of hydrogen / loss of oxygen",
              "Redox reaction examples (CuO + H2 -> Cu + H2O, ZnO + C -> Zn + CO, MnO2 + 4HCl -> MnCl2 + 2H2O + Cl2)",
              "Corrosion of metals (rusting of iron, black silver sulphide, green basic copper carbonate)",
              "Rancidity of fats and oils and prevention using antioxidants and nitrogen flushing"
            ],
            "practiceSet": "Exercise 1.5",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Acids, Bases and Salts",
        "topics": [
          {
            "number": "2.1",
            "name": "Chemical Properties of Acids and Bases (Indicators, Metals, Carbonates)",
            "topicCode": "CBSE-10-SCI-2-2.1",
            "subtopics": [
              "Olfactory indicators (onion, vanilla, clove oil)",
              "Reaction with metals -> Salt + H2 gas (Pop sound test)",
              "Reaction of acids with metal carbonates & hydrogen carbonates -> Salt + CO2 + H2O (Lime water milkiness test)",
              "Reaction of metal oxides (basic) with acids, non-metal oxides (acidic) with bases"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "What do all Acids and Bases have in Common? (H+ & OH- Ions)",
            "topicCode": "CBSE-10-SCI-2-2.2",
            "subtopics": [
              "Conduction of electricity in aqueous solutions due to free ions",
              "Dry HCl gas vs aqueous HCl litmus test",
              "Dilution of acid: exothermic process (Always add acid slowly to water with constant stirring)"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "pH Scale & Importance of pH in Everyday Life",
            "topicCode": "CBSE-10-SCI-2-2.3",
            "subtopics": [
              "pH = -log[H+], range 0 to 14",
              "Human body pH range 7.0 - 7.8",
              "Acid rain (pH < 5.6)",
              "pH in digestive system (HCl acidity & antacid Mg(OH)2)",
              "Tooth decay starts below pH 5.5 (calcium hydroxyapatite corrosion)",
              "Self defense by animals and plants (methanoic acid in bee sting and nettle leaf sting, dock plant relief)"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Chemicals from Common Salt: Sodium Hydroxide (Chlor-Alkali Process)",
            "topicCode": "CBSE-10-SCI-2-2.4",
            "subtopics": [
              "Electrolysis of brine: 2NaCl + 2H2O -> 2NaOH + Cl2 + H2",
              "Anode: Cl2 gas; Cathode: H2 gas; Near cathode: NaOH solution; Uses of all three products"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.5",
            "name": "Bleaching Powder, Baking Soda, Washing Soda & Plaster of Paris",
            "topicCode": "CBSE-10-SCI-2-2.5",
            "subtopics": [
              "Bleaching powder: Ca(OH)2 + Cl2 -> CaOCl2 + H2O",
              "Baking soda: NaCl + H2O + CO2 + NH3 -> NH4Cl + NaHCO3 (Baking powder = NaHCO3 + tartaric acid, CO2 puffiness)",
              "Washing soda: Na2CO3 + 10H2O -> Na2CO3·10H2O",
              "Plaster of Paris: CaSO4·2H2O (Gypsum heated at 373 K) -> CaSO4·1/2H2O + 1.5H2O"
            ],
            "practiceSet": "Exercise 2.5",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Metals and Non-metals",
        "topics": [
          {
            "number": "3.1",
            "name": "Physical Properties of Metals and Non-metals & Exceptions",
            "topicCode": "CBSE-10-SCI-3-3.1",
            "subtopics": [
              "Malleability, ductility, thermal & electrical conductivity, sonority, metallic lustre",
              "Exceptions: Mercury (liquid metal), Bromine (liquid non-metal), Iodine (lustrous non-metal), Diamond & Graphite, Alkali metals Na/K (soft, cut with knife, low melting point), Gallium/Caesium (melt on palm)"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Chemical Properties of Metals (Reactivity with Oxygen, Water & Acids)",
            "topicCode": "CBSE-10-SCI-3-3.2",
            "subtopics": [
              "Amphoteric oxides (Al2O3 and ZnO react with both acids and bases e.g. Sodium aluminate / zincate)",
              "Reaction of Na/K with cold water (violent), Mg with hot water, Al/Fe/Zn with steam, Cu/Ag/Au no reaction",
              "Reaction of metals with dilute HNO3 (produces N2O/NO2 except Mg and Mn produce H2)",
              "Aqua regia (3 HCl : 1 HNO3)"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Reactivity Series of Metals & Displacement Reactions",
            "topicCode": "CBSE-10-SCI-3-3.3",
            "subtopics": [
              "Order: K > Na > Ca > Mg > Al > Zn > Fe > Pb > [H] > Cu > Hg > Ag > Au"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Formation and Properties of Ionic Compounds",
            "topicCode": "CBSE-10-SCI-3-3.4",
            "subtopics": [
              "Electron dot structures (NaCl, MgCl2, CaO)",
              "Properties: Physical nature (hard crystalline solids), high melting and boiling points, solubility in polar solvents, electrical conduction in molten/solution states"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.5",
            "name": "Metallurgy: Concentration of Ores, Roasting, Calcination & Reduction",
            "topicCode": "CBSE-10-SCI-3-3.5",
            "subtopics": [
              "Minerals, ores, gangue",
              "Roasting (heating sulphide ores in excess air)",
              "Calcination (heating carbonate ores in limited air)",
              "Reduction of oxides using Carbon / Smelting or Thermite reaction (Fe2O3 + 2Al -> 2Fe + Al2O3 + Heat for welding railway tracks)",
              "Electrolytic reduction of highly reactive metals (Na, Al)"
            ],
            "practiceSet": "Exercise 3.5",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.6",
            "name": "Refining of Metals (Electrolytic Refining of Copper) & Corrosion Prevention",
            "topicCode": "CBSE-10-SCI-3-3.6",
            "subtopics": [
              "Electrolytic refining: impure anode, pure thin cathode, acidified CuSO4 electrolyte, anode mud",
              "Prevention of corrosion: Painting, oiling, galvanisation (zinc coating), tin plating, anodising, alloying (Steel, Stainless steel, Brass, Bronze, Solder, Amalgam)"
            ],
            "practiceSet": "Exercise 3.6",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Carbon and its Compounds",
        "topics": [
          {
            "number": "4.1",
            "name": "Covalent Bonding & Versatile Nature of Carbon (Catenation & Tetravalency)",
            "topicCode": "CBSE-10-SCI-4-4.1",
            "subtopics": [
              "Sharing of electron pairs (H2, O2, N2, CH4, CO2)",
              "Catenation: self-linking property forming long chains, branched chains, rings",
              "Tetravalency forming strong covalent bonds due to small atomic size"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Saturated and Unsaturated Carbon Compounds & Homologous Series",
            "topicCode": "CBSE-10-SCI-4-4.2",
            "subtopics": [
              "Alkanes (C_n H_2n+2), Alkenes (C_n H_2n), Alkynes (C_n H_2n-2)",
              "Homologous series: differing by -CH2- unit (14 u molar mass), gradation in physical properties"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Nomenclature of Carbon Compounds (IUPAC Rules & Functional Groups)",
            "topicCode": "CBSE-10-SCI-4-4.3",
            "subtopics": [
              "Functional groups: Halogens (-Cl, -Br), Alcohol (-OH), Aldehyde (-CHO), Ketone (-CO-), Carboxylic acid (-COOH)",
              "Prefixes and suffixes (meth-, eth-, prop-, but-, pent-, hex-)"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.4",
            "name": "Chemical Properties: Combustion, Oxidation, Addition & Substitution Reactions",
            "topicCode": "CBSE-10-SCI-4-4.4",
            "subtopics": [
              "Combustion: Blue clean flame vs yellow sooty flame",
              "Oxidation using Alkaline KMnO4 or Acidified K2Cr2O7 (Ethanol -> Ethanoic acid)",
              "Addition reaction of unsaturated hydrocarbons (Hydrogenation using Nickel catalyst for vegetable ghee)",
              "Substitution reaction of methane with chlorine in sunlight"
            ],
            "practiceSet": "Exercise 4.4",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.5",
            "name": "Ethanol & Ethanoic Acid: Properties, Reactions (Esterification & Saponification)",
            "topicCode": "CBSE-10-SCI-4-4.5",
            "subtopics": [
              "Ethanol (C2H5OH): reaction with Sodium (H2 gas evolution), dehydration with conc. H2SO4 to ethene",
              "Ethanoic acid (CH3COOH): Vinegar (5-8% solution), Esterification reaction with alcohol -> Sweet smelling ester, Saponification (alkaline hydrolysis of esters to soap), Reaction with NaHCO3/Na2CO3 (effervescence of CO2)"
            ],
            "practiceSet": "Exercise 4.5",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.6",
            "name": "Soaps, Detergents & Micelle Formation Cleansing Mechanism",
            "topicCode": "CBSE-10-SCI-4-4.6",
            "subtopics": [
              "Soap: Sodium/potassium salts of long chain fatty acids",
              "Structure: Hydrophobic hydrocarbon tail (oil soluble) and Hydrophilic ionic head (water soluble)",
              "Micelle formation and emulsification of grease",
              "Hard water scum formation with Ca²⁺/Mg²⁺ and synthetic detergents advantage"
            ],
            "practiceSet": "Exercise 4.6",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Life Processes",
        "topics": [
          {
            "number": "5.1",
            "name": "Autotrophic Nutrition & Photosynthesis Mechanism",
            "topicCode": "CBSE-10-SCI-5-5.1",
            "subtopics": [
              "Equation: 6CO2 + 12H2O -> C6H12O6 + 6O2 + 6H2O",
              "Three events: Absorption of light energy by chlorophyll, conversion of light to chemical energy & water photolysis, reduction of CO2 to carbohydrates",
              "Stomata opening and closing controlled by guard cells turgor"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Heterotrophic Nutrition & Human Alimentary Canal Anatomy",
            "topicCode": "CBSE-10-SCI-5-5.2",
            "subtopics": [
              "Holozoic nutrition in Amoeba (pseudopodia, food vacuole)",
              "Human digestive system: Mouth (salivary amylase), Stomach (HCl, pepsin, mucus), Small intestine (Bile juice for fat emulsification, pancreatic amylase/trypsin/lipase, intestinal juice), Villi absorption, Large intestine"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Respiration: Breakdown of Glucose Pathways & Human Respiratory System",
            "topicCode": "CBSE-10-SCI-5-5.3",
            "subtopics": [
              "Glycolysis in cytoplasm -> Pyruvate (3-carbon)",
              "Pathway 1 (Aerobic in mitochondria): CO2 + H2O + 38 ATP",
              "Pathway 2 (Anaerobic yeast fermentation): Ethanol + CO2 + 2 ATP",
              "Pathway 3 (Lack of oxygen in muscle cells): Lactic acid + 2 ATP (muscle cramps)",
              "Human respiration: Nostrils, pharynx, larynx, trachea with cartilage rings, bronchi, alveoli for gas exchange with hemoglobin"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.4",
            "name": "Transportation in Humans: Heart Anatomy, Double Circulation & Blood Vessels",
            "topicCode": "CBSE-10-SCI-5-5.4",
            "subtopics": [
              "Four chambers of heart (right/left atria and ventricles)",
              "Double circulation: Pulmonary circulation and Systemic circulation",
              "Blood pressure (120/80 mmHg), Lymph / tissue fluid transport"
            ],
            "practiceSet": "Exercise 5.4",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.5",
            "name": "Transportation in Plants: Xylem (Water & Minerals) & Phloem (Translocation)",
            "topicCode": "CBSE-10-SCI-5-5.5",
            "subtopics": [
              "Root pressure and transpiration pull in xylem vessels and tracheids",
              "Translocation of sucrose in phloem sieve tubes and companion cells using ATP energy"
            ],
            "practiceSet": "Exercise 5.5",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.6",
            "name": "Excretion in Humans (Nephron Anatomy & Urine Formation) & Excretion in Plants",
            "topicCode": "CBSE-10-SCI-5-5.6",
            "subtopics": [
              "Human excretory system: Pair of kidneys, ureters, urinary bladder, urethra",
              "Nephron structure: Glomerular ultrafiltration, tubular selective reabsorption (glucose, amino acids, salts, water), tubular secretion, collecting duct",
              "Hemodialysis / artificial kidney",
              "Plant excretion: Stomatal transpiration, storage in leaves and bark, resins, gums"
            ],
            "practiceSet": "Exercise 5.6",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Control and Coordination",
        "topics": [
          {
            "number": "6.1",
            "name": "Nervous System: Neuron Anatomy & Synapse Transmission",
            "topicCode": "CBSE-10-SCI-6-6.1",
            "subtopics": [
              "Receptors (gustatory, olfactory, photoreceptors, phonoreceptors)",
              "Neuron structure: Dendrite, cell body, axon, nerve ending",
              "Synapse chemical neurotransmitter transmission"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Reflex Action and Reflex Arc",
            "topicCode": "CBSE-10-SCI-6-6.2",
            "subtopics": [
              "Involuntary sudden response pathway: Receptor -> Sensory neuron -> Spinal cord (Relay neuron) -> Motor neuron -> Effector muscle"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Human Brain Anatomy & Functions (Forebrain, Midbrain, Hindbrain)",
            "topicCode": "CBSE-10-SCI-6-6.3",
            "subtopics": [
              "Forebrain: Cerebrum (thinking, sensory interpretation, voluntary motor control, memory, hunger center)",
              "Midbrain: Visual and auditory reflex centers",
              "Hindbrain: Cerebellum (posture and balance precision), Pons (respiratory regulation), Medulla oblongata (involuntary blood pressure, salivation, vomiting)"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.4",
            "name": "Coordination in Plants: Nastic Movements vs Tropic Movements",
            "topicCode": "CBSE-10-SCI-6-6.4",
            "subtopics": [
              "Nastic / non-directional immediate movement (Mimosa pudica touch-me-not turgor change)",
              "Tropic movements: Phototropism, Geotropism, Chemotropism (pollen tube growth towards ovule), Hydrotropism"
            ],
            "practiceSet": "Exercise 6.4",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.5",
            "name": "Plant Hormones (Auxin, Gibberellin, Cytokinin, Abscisic Acid, Ethylene)",
            "topicCode": "CBSE-10-SCI-6-6.5",
            "subtopics": [
              "Auxin (shoot tip elongation towards light)",
              "Gibberellin (stem growth)",
              "Cytokinin (rapid cell division in fruits/seeds)",
              "Abscisic acid (stress hormone, stomatal closure, wilting of leaves)"
            ],
            "practiceSet": "Exercise 6.5",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.6",
            "name": "Hormones in Animals: Endocrine Glands and Feedback Mechanism",
            "topicCode": "CBSE-10-SCI-6-6.6",
            "subtopics": [
              "Pituitary (Growth hormone - dwarfism/gigantism)",
              "Thyroid (Thyroxine - Iodine requirement and goitre prevention)",
              "Pancreas (Insulin - diabetes and blood glucose feedback regulation)",
              "Adrenal (Adrenaline - Fight or flight emergency responses)",
              "Testes (Testosterone) & Ovaries (Estrogen)"
            ],
            "practiceSet": "Exercise 6.6",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "How do Organisms Reproduce?",
        "topics": [
          {
            "number": "7.1",
            "name": "DNA Copying & Importance of Variation",
            "topicCode": "CBSE-10-SCI-7-7.1",
            "subtopics": [
              "DNA replication in cell division and biochemical inaccuracy creating variations",
              "Survival advantage of variations in changing ecological niches"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Asexual Reproduction Modes (Fission, Fragmentation, Regeneration, Budding, Vegetative Propagation, Spores)",
            "topicCode": "CBSE-10-SCI-7-7.2",
            "subtopics": [
              "Binary fission (Amoeba, Leishmania with whip-like flagellum)",
              "Multiple fission (Plasmodium)",
              "Fragmentation (Spirogyra)",
              "Regeneration (Planaria, Hydra specialized cells)",
              "Budding (Hydra, Yeast)",
              "Vegetative propagation (Bryophyllum leaf notches, layering, grafting)",
              "Spore formation (Rhizopus bread mould sporangia)"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Sexual Reproduction in Flowering Plants (Pollination & Double Fertilisation)",
            "topicCode": "CBSE-10-SCI-7-7.3",
            "subtopics": [
              "Flower structure: Stamen (anther and filament) and Carpel/Pistil (stigma, style, ovary)",
              "Self pollination vs Cross pollination (agents: wind, water, insects)",
              "Pollen tube growth and pollen germination on stigma",
              "Syngamy (male gamete + egg -> zygote) and Triple fusion (male gamete + 2 polar nuclei -> PEN endosperm)",
              "Seed and fruit formation"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.4",
            "name": "Sexual Reproduction in Humans: Male & Female Reproductive Systems",
            "topicCode": "CBSE-10-SCI-7-7.4",
            "subtopics": [
              "Male system: Testes in scrotum (lower temperature for spermatogenesis), vas deferens, seminal vesicles & prostate gland (nourishing fluids), urethra, penis",
              "Female system: Ovaries (egg release), oviduct / fallopian tube (site of fertilisation), uterus (implantation), cervix, vagina"
            ],
            "practiceSet": "Exercise 7.4",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.5",
            "name": "Menstrual Cycle, Fertilisation, Implantation & Placenta",
            "topicCode": "CBSE-10-SCI-7-7.5",
            "subtopics": [
              "Monthly cycle (28 days) and shedding of uterine endometrium lining",
              "Fertilisation in ampulla of fallopian tube",
              "Placenta: specialized disc tissue with villi for glucose/oxygen exchange and embryonic waste removal",
              "Gestation period (9 months) and parturition"
            ],
            "practiceSet": "Exercise 7.5",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.6",
            "name": "Reproductive Health, Contraceptive Methods & STDs",
            "topicCode": "CBSE-10-SCI-7-7.6",
            "subtopics": [
              "Contraceptive barrier methods (condoms, diaphragms)",
              "Chemical methods (oral contraceptive pills preventing ovulation)",
              "Intrauterine devices (IUCDs - Copper-T)",
              "Surgical methods (Vasectomy in males, Tubectomy in females)",
              "Sexually Transmitted Diseases: Bacterial (Gonorrhoea, Syphilis) vs Viral (Warts, HIV/AIDS)"
            ],
            "practiceSet": "Exercise 7.6",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      },
      {
        "number": "8",
        "name": "Heredity and Evolution",
        "topics": [
          {
            "number": "8.1",
            "name": "Accumulation of Variation During Reproduction",
            "topicCode": "CBSE-10-SCI-8-8.1",
            "subtopics": [
              "Inheritance of traits from parental generations"
            ],
            "practiceSet": "Exercise 8.1",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.2",
            "name": "Mendel Laws of Inheritance: Monohybrid Cross (Dominant vs Recessive)",
            "topicCode": "CBSE-10-SCI-8-8.2",
            "subtopics": [
              "Cross of Pure Tall (TT) and Pure Dwarf (tt)",
              "F1 generation (all Tall - Tt) and F2 generation (Phenotypic ratio 3:1, Genotypic ratio 1:2:1)",
              "Law of Segregation"
            ],
            "practiceSet": "Exercise 8.2",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.3",
            "name": "Mendel Dihybrid Cross & Law of Independent Assortment",
            "topicCode": "CBSE-10-SCI-8-8.3",
            "subtopics": [
              "Cross of Round-Yellow (RRYY) and Wrinkled-Green (rryy)",
              "F2 generation phenotypic ratio 9:3:3:1",
              "Independent assortment of genes"
            ],
            "practiceSet": "Exercise 8.3",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.4",
            "name": "Sex Determination in Humans & Environmental Sex Determination",
            "topicCode": "CBSE-10-SCI-8-8.4",
            "subtopics": [
              "Human sex chromosomes: XX (female) and XY (male)",
              "50% probability of male/female child determined strictly by father sperm (X or Y)",
              "Environmental sex determination in reptiles (temperature dependent in turtles/lizards), snails changing sex"
            ],
            "practiceSet": "Exercise 8.4",
            "theorems": [],
            "problemSet": "Problem Set 8"
          }
        ]
      },
      {
        "number": "9",
        "name": "Light - Reflection and Refraction",
        "topics": [
          {
            "number": "9.1",
            "name": "Spherical Mirrors: Terminology, Ray Rules & Concave Mirror Ray Diagrams",
            "topicCode": "CBSE-10-SCI-9-9.1",
            "subtopics": [
              "Pole (P), Focus (F), Centre of curvature (C), Principal axis, Focal length (f = R/2)",
              "Four rules of ray tracing for spherical mirrors",
              "Ray diagrams for all 6 object positions for concave mirror"
            ],
            "practiceSet": "Exercise 9.1",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.2",
            "name": "Convex Mirror Ray Diagrams & Practical Applications",
            "topicCode": "CBSE-10-SCI-9-9.2",
            "subtopics": [
              "Ray diagrams for convex mirror (always virtual, erect, diminished)",
              "Uses: Rear-view mirrors (wide field of view), street lights, concave mirror shaving and solar furnaces"
            ],
            "practiceSet": "Exercise 9.2",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.3",
            "name": "Mirror Formula (1/f = 1/v + 1/u) & Magnification (m = -v/u = h'/h)",
            "topicCode": "CBSE-10-SCI-9-9.3",
            "subtopics": [
              "New Cartesian Sign Convention rules",
              "Solving numerical mirror problems"
            ],
            "practiceSet": "Exercise 9.3",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.4",
            "name": "Refraction of Light & Snell Law of Refraction",
            "topicCode": "CBSE-10-SCI-9-9.4",
            "subtopics": [
              "Cause of refraction (change in speed of light in different media)",
              "Snell Law: (sin i / sin r) = constant = n21",
              "Refraction through a rectangular glass slab and lateral displacement"
            ],
            "practiceSet": "Exercise 9.4",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.5",
            "name": "Absolute & Relative Refractive Index (n = c / v)",
            "topicCode": "CBSE-10-SCI-9-9.5",
            "subtopics": [
              "Speed of light in vacuum c = 3 * 10^8 m/s",
              "Optical density: denser medium (slower light, bends towards normal) vs rarer medium (faster light, bends away from normal)",
              "Relative refractive index n21 = v1 / v2"
            ],
            "practiceSet": "Exercise 9.5",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.6",
            "name": "Spherical Lenses: Convex & Concave Lens Ray Diagrams",
            "topicCode": "CBSE-10-SCI-9-9.6",
            "subtopics": [
              "Optical centre (O), Principal focus (F1, F2), Focal length",
              "Ray diagrams for convex lens (6 positions) and concave lens (2 positions)"
            ],
            "practiceSet": "Exercise 9.6",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.7",
            "name": "Lens Formula (1/f = 1/v - 1/u) & Magnification (m = v/u = h'/h)",
            "topicCode": "CBSE-10-SCI-9-9.7",
            "subtopics": [
              "Sign conventions for convex (+f) and concave (-f) lenses",
              "Solving numerical lens problems"
            ],
            "practiceSet": "Exercise 9.7",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.8",
            "name": "Power of a Lens Formula: P = 1 / f (in metres)",
            "topicCode": "CBSE-10-SCI-9-9.8",
            "subtopics": [
              "SI unit Dioptre (1 D = 1 m⁻¹)",
              "Power of convex lens (+ve) and concave lens (-ve)",
              "Combination of thin lenses: P = P1 + P2 + P3"
            ],
            "practiceSet": "Exercise 9.8",
            "theorems": [],
            "problemSet": "Problem Set 9"
          }
        ]
      },
      {
        "number": "10",
        "name": "The Human Eye and the Colourful World",
        "topics": [
          {
            "number": "10.1",
            "name": "Human Eye Anatomy & Power of Accommodation",
            "topicCode": "CBSE-10-SCI-10-10.1",
            "subtopics": [
              "Cornea, iris (regulates pupil size), pupil, crystalline lens, ciliary muscles, retina (photoreceptor rods and cones), optic nerve",
              "Power of accommodation: focal length adjustment for near point (25 cm) and far point (infinity)"
            ],
            "practiceSet": "Exercise 10.1",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.2",
            "name": "Defects of Vision: Myopia (Near-sightedness) & Correction",
            "topicCode": "CBSE-10-SCI-10-10.2",
            "subtopics": [
              "Causes: Excessive curvature of eye lens or elongation of eyeball",
              "Image formed in front of retina",
              "Correction using concave lens of suitable focal length"
            ],
            "practiceSet": "Exercise 10.2",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.3",
            "name": "Defects of Vision: Hypermetropia & Presbyopia",
            "topicCode": "CBSE-10-SCI-10-10.3",
            "subtopics": [
              "Hypermetropia causes: Focal length too long or eyeball too short; image behind retina; correction by convex lens",
              "Presbyopia: Aging weakening of ciliary muscles and flexibility loss; correction by bifocal lenses (upper concave, lower convex)",
              "Cataract surgery"
            ],
            "practiceSet": "Exercise 10.3",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.4",
            "name": "Refraction Through a Triangular Glass Prism & Angle of Deviation (D)",
            "topicCode": "CBSE-10-SCI-10-10.4",
            "subtopics": [
              "Angle of prism (A), angle of incidence (i), angle of emergence (e)",
              "Relation: i + e = A + D"
            ],
            "practiceSet": "Exercise 10.4",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.5",
            "name": "Dispersion of White Light, Newton Glass Prism Experiment & Rainbow",
            "topicCode": "CBSE-10-SCI-10-10.5",
            "subtopics": [
              "Splitting into VIBGYOR (Red bends least, Violet bends most)",
              "Recombination of spectrum using inverted second prism (Newton experiment)",
              "Rainbow formation: Refraction -> Dispersion -> Internal Reflection -> Refraction in raindrops"
            ],
            "practiceSet": "Exercise 10.5",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.6",
            "name": "Atmospheric Refraction (Twinkling of Stars, Advanced Sunrise & Delayed Sunset)",
            "topicCode": "CBSE-10-SCI-10-10.6",
            "subtopics": [
              "Continuous gradation of atmospheric refractive index",
              "Apparent higher position of stars and twinkling effect (point source vs extended planet source)",
              "Early sunrise (2 min before) and delayed sunset (2 min after) making day 4 min longer"
            ],
            "practiceSet": "Exercise 10.6",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.7",
            "name": "Scattering of Light: Tyndall Effect & Color of Sky / Sunrise-Sunset",
            "topicCode": "CBSE-10-SCI-10-10.7",
            "subtopics": [
              "Tyndall effect in colloidal smoke/fog and dense forest canopy",
              "Rayleigh scattering: Intensity ∝ 1/λ⁴",
              "Blue color of sky (short wavelength blue scattered more)",
              "Reddish appearance of sun at sunrise and sunset (longer red wavelength travels longer distance through atmosphere)"
            ],
            "practiceSet": "Exercise 10.7",
            "theorems": [],
            "problemSet": "Problem Set 10"
          }
        ]
      },
      {
        "number": "11",
        "name": "Electricity",
        "topics": [
          {
            "number": "11.1",
            "name": "Electric Current (I = Q/t) & Potential Difference (V = W/Q)",
            "topicCode": "CBSE-10-SCI-11-11.1",
            "subtopics": [
              "Definition of electric charge (Coulomb), Ampere, Volt",
              "Direction of conventional current vs electron flow",
              "Ammeter (in series, low resistance) and Voltmeter (in parallel, high resistance)"
            ],
            "practiceSet": "Exercise 11.1",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.2",
            "name": "Ohm Law & Circuit Diagram Verification",
            "topicCode": "CBSE-10-SCI-11-11.2",
            "subtopics": [
              "Statement: V ∝ I at constant temperature (V = IR)",
              "Ohmic vs non-ohmic conductors and V-I slope = Resistance"
            ],
            "practiceSet": "Exercise 11.2",
            "theorems": [
              "Ohm Law"
            ],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.3",
            "name": "Factors Affecting Resistance & Resistivity Formula (R = ρ * L / A)",
            "topicCode": "CBSE-10-SCI-11-11.3",
            "subtopics": [
              "Resistance depends on length (L), cross-sectional area (A), material, temperature",
              "Resistivity (ρ in Ω·m) of conductors, alloys (Nichrome), insulators",
              "Why heating elements of toasters/irons are made of alloys rather than pure metals"
            ],
            "practiceSet": "Exercise 11.3",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.4",
            "name": "Resistors in Series Combination (Rs = R1 + R2 + R3)",
            "topicCode": "CBSE-10-SCI-11-11.4",
            "subtopics": [
              "Derivation of equivalent resistance",
              "Current is same throughout, total voltage divides: V = V1 + V2 + V3",
              "Disadvantages of series connection in domestic appliances"
            ],
            "practiceSet": "Exercise 11.4",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.5",
            "name": "Resistors in Parallel Combination (1/Rp = 1/R1 + 1/R2 + 1/R3)",
            "topicCode": "CBSE-10-SCI-11-11.5",
            "subtopics": [
              "Derivation of equivalent resistance",
              "Voltage is same across each resistor, total current divides: I = I1 + I2 + I3",
              "Advantages of parallel connection in domestic circuits"
            ],
            "practiceSet": "Exercise 11.5",
            "theorems": [],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.6",
            "name": "Heating Effect of Electric Current & Joule Law of Heating (H = I²Rt)",
            "topicCode": "CBSE-10-SCI-11-11.6",
            "subtopics": [
              "Derivation: H = VIt = I²Rt = (V²/R)t (Joules)",
              "Applications: Electric iron, heater, electric toaster, electric bulb (tungsten filament, inert argon/nitrogen filling), electric fuse safety mechanism"
            ],
            "practiceSet": "Exercise 11.6",
            "theorems": [
              "Joule Law of Heating"
            ],
            "problemSet": "Problem Set 11"
          },
          {
            "number": "11.7",
            "name": "Electric Power Formulas (P = VI = I²R = V²/R) & Commercial Units (kWh)",
            "topicCode": "CBSE-10-SCI-11-11.7",
            "subtopics": [
              "Power SI unit Watt (1 W = 1 V * 1 A)",
              "Commercial unit of electrical energy: 1 kWh (1 Board of Trade Unit) = 3.6 * 10^6 Joules",
              "Calculating electricity bills for household appliances"
            ],
            "practiceSet": "Exercise 11.7",
            "theorems": [],
            "problemSet": "Problem Set 11"
          }
        ]
      },
      {
        "number": "12",
        "name": "Magnetic Effects of Electric Current",
        "topics": [
          {
            "number": "12.1",
            "name": "Magnetic Field & Properties of Magnetic Field Lines",
            "topicCode": "CBSE-10-SCI-12-12.1",
            "subtopics": [
              "Oersted experiment",
              "Field lines emerge from North pole and enter South pole (closed continuous curves)",
              "Closeness of lines indicates field strength",
              "No two magnetic field lines intersect (two directions of compass needle impossible)"
            ],
            "practiceSet": "Exercise 12.1",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.2",
            "name": "Magnetic Field Due to Current Carrying Straight Conductor & Right Hand Thumb Rule",
            "topicCode": "CBSE-10-SCI-12-12.2",
            "subtopics": [
              "Concentric circular magnetic field lines around straight wire",
              "Maxwell Right Hand Thumb Rule (Thumb in current direction, curled fingers in field direction)"
            ],
            "practiceSet": "Exercise 12.2",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.3",
            "name": "Magnetic Field Due to Circular Loop & Solenoid",
            "topicCode": "CBSE-10-SCI-12-12.3",
            "subtopics": [
              "Field at center of circular loop is uniform and perpendicular",
              "Solenoid behaves like a bar magnet with North and South poles",
              "Electromagnet formation inside soft iron core"
            ],
            "practiceSet": "Exercise 12.3",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.4",
            "name": "Force on Current Carrying Conductor in Magnetic Field & Fleming Left Hand Rule",
            "topicCode": "CBSE-10-SCI-12-12.4",
            "subtopics": [
              "Lorentz magnetic force principle",
              "Maximum force when conductor is perpendicular to magnetic field",
              "Fleming Left Hand Rule (Forefinger = Field, Middle finger = Current, Thumb = Motion/Force)",
              "Principle of electric motor"
            ],
            "practiceSet": "Exercise 12.4",
            "theorems": [],
            "problemSet": "Problem Set 12"
          },
          {
            "number": "12.5",
            "name": "Domestic Electric Circuits: Live, Neutral, Earth Wires & Safety",
            "topicCode": "CBSE-10-SCI-12-12.5",
            "subtopics": [
              "Live wire (220 V, red insulation), Neutral wire (0 V, black insulation), Earth wire (green insulation)",
              "Earthing of metallic appliances safety (prevents electric shocks)",
              "Short circuiting vs overloading",
              "Fuse rating and circuit breakers"
            ],
            "practiceSet": "Exercise 12.5",
            "theorems": [],
            "problemSet": "Problem Set 12"
          }
        ]
      },
      {
        "number": "13",
        "name": "Our Environment",
        "topics": [
          {
            "number": "13.1",
            "name": "Ecosystem Components: Biotic & Abiotic Factors",
            "topicCode": "CBSE-10-SCI-13-13.1",
            "subtopics": [
              "Producers (chlorophyll containing autotrophs)",
              "Consumers (herbivores, carnivores, omnivores, parasites)",
              "Decomposers (bacteria and fungi recycling inorganic nutrients)"
            ],
            "practiceSet": "Exercise 13.1",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.2",
            "name": "Food Chains, Food Webs & 10% Energy Transfer Law",
            "topicCode": "CBSE-10-SCI-13-13.2",
            "subtopics": [
              "Trophic levels (T1, T2, T3, T4)",
              "Lindeman 10% Law: Only 10% energy transferred to next trophic level; 90% lost as heat and metabolic maintenance",
              "Unidirectional energy flow"
            ],
            "practiceSet": "Exercise 13.2",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.3",
            "name": "Biological Magnification of Non-Biodegradable Pesticides",
            "topicCode": "CBSE-10-SCI-13-13.3",
            "subtopics": [
              "Accumulation of persistent chemicals (e.g. DDT) increasing at successive trophic levels, maximum concentration in apex humans"
            ],
            "practiceSet": "Exercise 13.3",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.4",
            "name": "Ozone Layer Depletion & Montreal Protocol (CFCs)",
            "topicCode": "CBSE-10-SCI-13-13.4",
            "subtopics": [
              "Formation of Ozone (O2 + UV -> O + O; O + O2 -> O3)",
              "Ozone shields earth from harmful UV radiation (skin cancer, cataracts)",
              "Depletion by Chlorofluorocarbons (CFCs in refrigerants/fire extinguishers)",
              "UNEP Montreal Protocol (1987) banning CFC production"
            ],
            "practiceSet": "Exercise 13.4",
            "theorems": [],
            "problemSet": "Problem Set 13"
          },
          {
            "number": "13.5",
            "name": "Solid Waste Management: Biodegradable vs Non-Biodegradable Waste",
            "topicCode": "CBSE-10-SCI-13-13.5",
            "subtopics": [
              "Biodegradable waste (broken down by biological enzymes)",
              "Non-biodegradable waste (plastics, persistent chemicals)",
              "Eco-friendly disposal: Composting, recycling, sewage treatment, banning disposable plastics"
            ],
            "practiceSet": "Exercise 13.5",
            "theorems": [],
            "problemSet": "Problem Set 13"
          }
        ]
      }
    ]
  },
  {
    "docId": "mh_10_mth1",
    "board": "Maharashtra Board",
    "boardCode": "MH",
    "class": "10",
    "subject": "Mathematics Part - 1 (Algebra)",
    "subjectCode": "MTH1",
    "chapters": [
      {
        "number": "1",
        "name": "Linear Equations in Two Variables",
        "topics": [
          {
            "number": "1.1",
            "name": "Simultaneous Linear Equations & Elimination/Substitution Methods",
            "topicCode": "MH-10-MTH1-1-1.1",
            "subtopics": [
              "Standard form ax + by = c",
              "Equating coefficients method",
              "Substitution method for simultaneous equations"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Graphical Method of Solving Linear Equations",
            "topicCode": "MH-10-MTH1-1-1.2",
            "subtopics": [
              "Table of values construction",
              "Plotting straight lines and finding intersection point (x, y)"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Determinant & Cramer Rule (Determinant Method)",
            "topicCode": "MH-10-MTH1-1-1.3",
            "subtopics": [
              "Value of 2x2 determinant |a b; c d| = ad - bc",
              "Cramer Rule formulas: D, Dx, Dy and x = Dx/D, y = Dy/D"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Equations Reducible to a Pair of Linear Equations in Two Variables",
            "topicCode": "MH-10-MTH1-1-1.4",
            "subtopics": [
              "Substitutions for variable denominators (e.g. 1/(x-y) = m, 1/(x+y) = n)"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.5",
            "name": "Applied Word Problems (Numbers, Age, Speed-Distance, Boat & Stream)",
            "topicCode": "MH-10-MTH1-1-1.5",
            "subtopics": [
              "Two-digit number reverse equations",
              "Upstream and downstream river speed problems",
              "Fixed charge and variable cost problems"
            ],
            "practiceSet": "Exercise 1.5",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Quadratic Equations",
        "topics": [
          {
            "number": "2.1",
            "name": "Quadratic Equation Definition, Standard Form & Roots",
            "topicCode": "MH-10-MTH1-2-2.1",
            "subtopics": [
              "Standard form: ax² + bx + c = 0 (a != 0)",
              "Deciding whether given values are roots/solutions of equation"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Solving Quadratic Equations by Factorisation Method",
            "topicCode": "MH-10-MTH1-2-2.2",
            "subtopics": [
              "Splitting middle term and finding linear factors"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Solving Quadratic Equations by Completing the Square Method",
            "topicCode": "MH-10-MTH1-2-2.3",
            "subtopics": [
              "Third term formula: [1/2 * (coefficient of x)]²",
              "Transforming to perfect square trinomial (x + k)² = d"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Solving Quadratic Equations by Formula Method (Shreedharacharya)",
            "topicCode": "MH-10-MTH1-2-2.4",
            "subtopics": [
              "Formula: x = [-b ± √(b² - 4ac)] / (2a)"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.5",
            "name": "Nature of Roots & Discriminant (Δ = b² - 4ac)",
            "topicCode": "MH-10-MTH1-2-2.5",
            "subtopics": [
              "Δ > 0: Real and unequal roots",
              "Δ = 0: Real and equal roots",
              "Δ < 0: Not real roots",
              "Finding unknown k for equal roots"
            ],
            "practiceSet": "Exercise 2.5",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.6",
            "name": "Relation Between Roots and Coefficients (α + β, α * β)",
            "topicCode": "MH-10-MTH1-2-2.6",
            "subtopics": [
              "α + β = -b/a and α * β = c/a",
              "Obtaining quadratic equation from given roots: x² - (α+β)x + αβ = 0",
              "Evaluating symmetric functions: α² + β², α³ + β³"
            ],
            "practiceSet": "Exercise 2.6",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.7",
            "name": "Applied Word Problems on Quadratic Equations",
            "topicCode": "MH-10-MTH1-2-2.7",
            "subtopics": [
              "Speed-time-distance problems",
              "Area and perimeter geometric dimensions",
              "Consecutive natural/even/odd integer problems"
            ],
            "practiceSet": "Exercise 2.7",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Arithmetic Progression",
        "topics": [
          {
            "number": "3.1",
            "name": "Sequence & Arithmetic Progression (AP) Concept",
            "topicCode": "MH-10-MTH1-3-3.1",
            "subtopics": [
              "Common difference d = t_(n) - t_(n-1)",
              "Identifying whether given sequence is an AP"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "nth Term of an AP Formula: t_n = a + (n - 1)d",
            "topicCode": "MH-10-MTH1-3-3.2",
            "subtopics": [
              "Finding specific term values, total number of terms n",
              "Three consecutive terms (a-d, a, a+d) and four terms (a-3d, a-d, a+d, a+3d)"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Sum of First n Terms of an AP: S_n = n/2 [2a + (n - 1)d]",
            "topicCode": "MH-10-MTH1-3-3.3",
            "subtopics": [
              "Sum formula with last term: S_n = n/2 [t1 + tn]",
              "Finding sum of even/odd natural numbers"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Applied Word Problems on AP",
            "topicCode": "MH-10-MTH1-3-3.4",
            "subtopics": [
              "Savings schemes, loan repayments with decreasing monthly interest, auditorium seating rows"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Financial Planning",
        "topics": [
          {
            "number": "4.1",
            "name": "Goods and Services Tax (GST), CGST and SGST Structure",
            "topicCode": "MH-10-MTH1-4-4.1",
            "subtopics": [
              "GSTIN identification number (15 digits)",
              "CGST (Central GST) and SGST (State GST) equality: CGST = SGST = 1/2 * GST Rate",
              "Tax invoice layout: HSN code, SAC code, taxable value"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Input Tax Credit (ITC) & GST Payable in Business Chain",
            "topicCode": "MH-10-MTH1-4-4.2",
            "subtopics": [
              "GST Payable = Output Tax - Input Tax Credit (ITC)",
              "Manufacturer -> Wholesaler -> Retailer -> Consumer tax flow"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Shares: Face Value (FV), Market Value (MV), Dividend & Brokerage",
            "topicCode": "MH-10-MTH1-4-4.3",
            "subtopics": [
              "At par (MV = FV), At premium (MV > FV), At discount (MV < FV)",
              "Dividend calculated strictly on Face Value",
              "Brokerage and GST on brokerage calculations"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.4",
            "name": "Mutual Funds, Systematic Investment Plan (SIP) & NAV",
            "topicCode": "MH-10-MTH1-4-4.4",
            "subtopics": [
              "Net Asset Value (NAV)",
              "Return on Investment (ROI) calculation"
            ],
            "practiceSet": "Exercise 4.4",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Probability",
        "topics": [
          {
            "number": "5.1",
            "name": "Random Experiment, Outcome & Sample Space (S)",
            "topicCode": "MH-10-MTH1-5-5.1",
            "subtopics": [
              "Sample space S and number of sample points n(S)",
              "Sample spaces for tossing 1, 2, 3 coins",
              "Sample spaces for throwing 1 and 2 dice (n(S) = 36)"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Types of Events: Certain, Impossible, Complementary Events",
            "topicCode": "MH-10-MTH1-5-5.2",
            "subtopics": [
              "Subset event sets A, B, C and counting sample points n(A)"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Probability of an Event Formula: P(A) = n(A) / n(S)",
            "topicCode": "MH-10-MTH1-5-5.3",
            "subtopics": [
              "Probability range: 0 <= P(A) <= 1 or 0% to 100%",
              "Card deck problems (52 playing cards - 26 Red, 26 Black, 12 Face cards, 4 Aces)",
              "Digit cards and committee formation problems"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Statistics",
        "topics": [
          {
            "number": "6.1",
            "name": "Mean of Grouped Frequency Distribution: Direct Method",
            "topicCode": "MH-10-MTH1-6-6.1",
            "subtopics": [
              "Class marks x_i and formula: X̄ = Σ(f_i * x_i) / N"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Mean by Assumed Mean Method & Step Deviation Method",
            "topicCode": "MH-10-MTH1-6-6.2",
            "subtopics": [
              "Assumed mean (A), deviations d_i = x_i - A, formula: X̄ = A + d̄",
              "Step deviation u_i = (x_i - A) / g, formula: X̄ = A + ū * g"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Median of Grouped Frequency Distribution Formula",
            "topicCode": "MH-10-MTH1-6-6.3",
            "subtopics": [
              "Median = L + [(N/2 - cf) / f] * h",
              "Continuous class intervals requirement"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.4",
            "name": "Mode of Grouped Frequency Distribution Formula",
            "topicCode": "MH-10-MTH1-6-6.4",
            "subtopics": [
              "Mode = L + [(f1 - f0) / (2f1 - f0 - f2)] * h",
              "Modal class identification"
            ],
            "practiceSet": "Exercise 6.4",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.5",
            "name": "Histogram and Frequency Polygon Construction",
            "topicCode": "MH-10-MTH1-6-6.5",
            "subtopics": [
              "Continuous classes on X-axis, frequency on Y-axis",
              "Polygon joining midpoints of histogram tops"
            ],
            "practiceSet": "Exercise 6.5",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.6",
            "name": "Pie Diagram: Drawing & Interpreting Central Angles (θ)",
            "topicCode": "MH-10-MTH1-6-6.6",
            "subtopics": [
              "Central angle formula: θ = (Value of component / Total value) * 360°",
              "Protractor circle subdivision and sector interpretation"
            ],
            "practiceSet": "Exercise 6.6",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      }
    ]
  },
  {
    "docId": "mh_10_mth2",
    "board": "Maharashtra Board",
    "boardCode": "MH",
    "class": "10",
    "subject": "Mathematics Part - 2 (Geometry)",
    "subjectCode": "MTH2",
    "chapters": [
      {
        "number": "1",
        "name": "Similarity",
        "topics": [
          {
            "number": "1.1",
            "name": "Ratio of Areas of Two Triangles (Base & Height Properties)",
            "topicCode": "MH-10-MTH2-1-1.1",
            "subtopics": [
              "Ratio of areas = (b1 * h1) / (b2 * h2)",
              "Triangles with equal heights: A1/A2 = b1/b2",
              "Triangles with equal bases: A1/A2 = h1/h2",
              "Triangles with equal bases and equal heights: A1 = A2"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Basic Proportionality Theorem (BPT) & Its Converse",
            "topicCode": "MH-10-MTH2-1-1.2",
            "subtopics": [
              "Statement and geometric proof: Line parallel to side dividing remaining two sides in equal ratio",
              "Converse of Basic Proportionality Theorem"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [
              "Basic Proportionality Theorem",
              "Converse of BPT"
            ],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Property of Angle Bisector of a Triangle & Property of Three Parallel Lines",
            "topicCode": "MH-10-MTH2-1-1.3",
            "subtopics": [
              "Angle bisector theorem: BD/DC = AB/AC and converse",
              "Intercept theorem for three parallel lines: AB/BC = XY/YZ"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [
              "Angle Bisector Theorem",
              "Three Parallel Lines Intercept Theorem"
            ],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Tests of Similarity of Triangles (AAA, AA, SAS, SSS)",
            "topicCode": "MH-10-MTH2-1-1.4",
            "subtopics": [
              "Tests to prove triangles similar",
              "Corresponding sides in proportion and corresponding angles congruent"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.5",
            "name": "Theorem of Areas of Similar Triangles",
            "topicCode": "MH-10-MTH2-1-1.5",
            "subtopics": [
              "Statement and proof: Ratio of areas of two similar triangles = square of ratio of corresponding sides (A1/A2 = s1²/s2² = h1²/h2² = m1²/m2²)"
            ],
            "practiceSet": "Exercise 1.5",
            "theorems": [
              "Theorem of Areas of Similar Triangles"
            ],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Pythagoras Theorem",
        "topics": [
          {
            "number": "2.1",
            "name": "Similarity of Right Angled Triangles & Theorem of Geometric Mean",
            "topicCode": "MH-10-MTH2-2-2.1",
            "subtopics": [
              "Altitude to hypotenuse divides triangle into two triangles similar to original and to each other",
              "Theorem of Geometric Mean: CD² = AD * DB"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [
              "Similarity and Right Angled Triangle Theorem",
              "Theorem of Geometric Mean"
            ],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Pythagoras Theorem & Its Converse",
            "topicCode": "MH-10-MTH2-2-2.2",
            "subtopics": [
              "Statement and geometric proof: In right triangle, Hypotenuse² = Base² + Height²",
              "Converse of Pythagoras theorem",
              "Pythagorean triplets identification (e.g. 3,4,5; 5,12,13; 8,15,17)"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [
              "Pythagoras Theorem",
              "Converse of Pythagoras Theorem"
            ],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Application of Pythagoras Theorem in Acute & Obtuse Triangles",
            "topicCode": "MH-10-MTH2-2-2.3",
            "subtopics": [
              "Obtuse angled triangle: AC² = AB² + BC² + 2 * BC * BD",
              "Acute angled triangle: AC² = AB² + BC² - 2 * BC * BD"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Apollonius Theorem on Medians of Triangle",
            "topicCode": "MH-10-MTH2-2-2.4",
            "subtopics": [
              "Statement and proof: In triangle ABC with median AM on BC, AB² + AC² = 2(AM² + BM²)",
              "Calculating lengths of medians in triangles and diagonals of parallelograms"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [
              "Apollonius Theorem"
            ],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Circle",
        "topics": [
          {
            "number": "3.1",
            "name": "Circles Passing Through 1, 2, and 3 Non-Collinear Points",
            "topicCode": "MH-10-MTH2-3-3.1",
            "subtopics": [
              "Infinite circles through 1 and 2 points",
              "Unique circle passing through 3 non-collinear points; No circle through 3 collinear points"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Tangent Theorem & Converse (Tangent Perpendicular to Radius)",
            "topicCode": "MH-10-MTH2-3-3.2",
            "subtopics": [
              "Tangent theorem statement and proof: Tangent at point on circle is perpendicular to radius",
              "Converse of tangent theorem"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [
              "Tangent Theorem",
              "Converse of Tangent Theorem"
            ],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Tangent Segment Theorem (Tangents from External Point are Congruent)",
            "topicCode": "MH-10-MTH2-3-3.3",
            "subtopics": [
              "Statement and proof: Tangent segments from external point are congruent (AP = BP)"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [
              "Tangent Segment Theorem"
            ],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Touching Circles Theorem (Externally & Internally Touching)",
            "topicCode": "MH-10-MTH2-3-3.4",
            "subtopics": [
              "Theorem: Point of contact of touching circles lies on line joining their centres",
              "Distance between centres: d = r1 + r2 (externally) and d = |r1 - r2| (internally)"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [
              "Theorem of Touching Circles"
            ],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.5",
            "name": "Arc of a Circle, Central Angle & Measure of Arc",
            "topicCode": "MH-10-MTH2-3-3.5",
            "subtopics": [
              "Minor arc, major arc, semicircular arc",
              "Measure of minor arc = measure of central angle",
              "Measure of circle = 360°"
            ],
            "practiceSet": "Exercise 3.5",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.6",
            "name": "Inscribed Angle Theorem & Corollary (Angles in Same Segment)",
            "topicCode": "MH-10-MTH2-3-3.6",
            "subtopics": [
              "Statement and proof: Inscribed angle = 1/2 * intercepted arc",
              "Angles in same segment are congruent",
              "Angle in a semicircle is a right angle"
            ],
            "practiceSet": "Exercise 3.6",
            "theorems": [
              "Inscribed Angle Theorem",
              "Angle in Semicircle Theorem"
            ],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.7",
            "name": "Cyclic Quadrilateral Theorem & Its Converse",
            "topicCode": "MH-10-MTH2-3-3.7",
            "subtopics": [
              "Statement and proof: Opposite angles of cyclic quadrilateral are supplementary (sum = 180°)",
              "Corollary: Exterior angle of cyclic quadrilateral = interior opposite angle",
              "Converse of cyclic quadrilateral theorem"
            ],
            "practiceSet": "Exercise 3.7",
            "theorems": [
              "Cyclic Quadrilateral Theorem",
              "Converse of Cyclic Quadrilateral Theorem"
            ],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.8",
            "name": "Theorem of Angle Between Tangent and Secant & Tangent Secant Segment Theorem",
            "topicCode": "MH-10-MTH2-3-3.8",
            "subtopics": [
              "Tangent-Secant angle theorem: Angle = 1/2 * intercepted arc",
              "Tangent Secant Segment Theorem: PT² = PA * PB",
              "Theorem of internal and external division of chords: PA * PB = PC * PD"
            ],
            "practiceSet": "Exercise 3.8",
            "theorems": [
              "Tangent Secant Theorem",
              "Internal Division of Chords Theorem"
            ],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Geometric Constructions",
        "topics": [
          {
            "number": "4.1",
            "name": "Construction of Similar Triangle (Having Common Vertex)",
            "topicCode": "MH-10-MTH2-4-4.1",
            "subtopics": [
              "Step-by-step compass division and drawing parallel lines"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Construction of Similar Triangle (Having No Common Vertex)",
            "topicCode": "MH-10-MTH2-4-4.2",
            "subtopics": [
              "Calculating dimensions using similarity ratio and constructing triangle"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Construction of Tangent to Circle at Point on Circle (Using & Without Centre)",
            "topicCode": "MH-10-MTH2-4-4.3",
            "subtopics": [
              "Method 1: Extending radius and drawing perpendicular bisector",
              "Method 2: Using inscribed angle and alternate segment chord"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.4",
            "name": "Construction of Tangents to Circle from External Point",
            "topicCode": "MH-10-MTH2-4-4.4",
            "subtopics": [
              "Drawing perpendicular bisector of OP and intersecting arcs"
            ],
            "practiceSet": "Exercise 4.4",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Coordinate Geometry",
        "topics": [
          {
            "number": "5.1",
            "name": "Distance Formula Derivation: d = √[(x2 - x1)² + (y2 - y1)²]",
            "topicCode": "MH-10-MTH2-5-5.1",
            "subtopics": [
              "Distance of point (x, y) from origin: √(x² + y²)",
              "Proving collinearity and types of quadrilaterals (Rhombus, Rectangle, Square)"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Section Formula for Internal Division: ((mx2+nx1)/(m+n), (my2+ny1)/(m+n))",
            "topicCode": "MH-10-MTH2-5-5.2",
            "subtopics": [
              "Coordinates of point dividing line segment in ratio m:n",
              "Midpoint formula: ((x1+x2)/2, (y1+y2)/2)",
              "Centroid formula: G = ((x1+x2+x3)/3, (y1+y2+y3)/3)"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Slope of a Line: Formula m = tan θ and m = (y2 - y1) / (x2 - x1)",
            "topicCode": "MH-10-MTH2-5-5.3",
            "subtopics": [
              "Slope definition with positive direction of X-axis",
              "Slope of X-axis = 0, Slope of Y-axis is undefined",
              "Parallel lines have equal slopes (m1 = m2)",
              "Collinear points slope condition"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Trigonometry",
        "topics": [
          {
            "number": "6.1",
            "name": "Trigonometric Ratios & Fundamental Identities",
            "topicCode": "MH-10-MTH2-6-6.1",
            "subtopics": [
              "sin θ, cos θ, tan θ, cot θ, sec θ, cosec θ definitions",
              "Identities: sin²θ + cos²θ = 1; 1 + tan²θ = sec²θ; 1 + cot²θ = cosec²θ",
              "Proving trigonometric identities"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Evaluating Trigonometric Values for Standard Angles (0°, 30°, 45°, 60°, 90°)",
            "topicCode": "MH-10-MTH2-6-6.2",
            "subtopics": [
              "Derivation table and simplification"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Application of Trigonometry: Line of Sight, Angle of Elevation & Depression",
            "topicCode": "MH-10-MTH2-6-6.3",
            "subtopics": [
              "Height and distance problems: Lighthouse, ships, towers, broken trees, airplanes"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Mensuration",
        "topics": [
          {
            "number": "7.1",
            "name": "Surface Area and Volume of Cuboid, Cube, Cylinder, Cone",
            "topicCode": "MH-10-MTH2-7-7.1",
            "subtopics": [
              "Total Surface Area and Volume formulas review",
              "Slant height of cone: l = √(r² + h²)",
              "Cone CSA = πrl, TSA = πr(r+l), Volume = 1/3 πr²h"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Surface Area and Volume of Sphere and Hemisphere",
            "topicCode": "MH-10-MTH2-7-7.2",
            "subtopics": [
              "Sphere: Surface area = 4πr², Volume = 4/3 πr³",
              "Hemisphere: CSA = 2πr², TSA = 3πr², Volume = 2/3 πr³"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Frustum of a Cone: Surface Area & Volume",
            "topicCode": "MH-10-MTH2-7-7.3",
            "subtopics": [
              "Slant height: l = √[h² + (r1 - r2)²]",
              "CSA = πl(r1 + r2), TSA = πl(r1 + r2) + πr1² + πr2²",
              "Volume = 1/3 * πh(r1² + r2² + r1*r2)"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.4",
            "name": "Area of Sector & Length of Arc of a Circle",
            "topicCode": "MH-10-MTH2-7-7.4",
            "subtopics": [
              "Length of arc: l = (θ / 360) * 2πr",
              "Area of sector: A = (θ / 360) * πr² = 1/2 * l * r"
            ],
            "practiceSet": "Exercise 7.4",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.5",
            "name": "Area of Segment of a Circle (Minor & Major Segment)",
            "topicCode": "MH-10-MTH2-7-7.5",
            "subtopics": [
              "Area of segment = Area of sector - Area of triangle",
              "Area of triangle = 1/2 * r² * sin θ"
            ],
            "practiceSet": "Exercise 7.5",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      }
    ]
  },
  {
    "docId": "mh_10_scit1",
    "board": "Maharashtra Board",
    "boardCode": "MH",
    "class": "10",
    "subject": "Science and Technology Part - 1",
    "subjectCode": "SCIT1",
    "chapters": [
      {
        "number": "1",
        "name": "Gravitation",
        "topics": [
          {
            "number": "1.1",
            "name": "Gravitation & Kepler Three Laws of Planetary Motion",
            "topicCode": "MH-10-SCIT1-1-1.1",
            "subtopics": [
              "Centripetal force definition",
              "Kepler 1st Law (Law of Orbits - Elliptical orbit with Sun at one focus)",
              "Kepler 2nd Law (Law of Areas - Equal areas in equal intervals of time)",
              "Kepler 3rd Law (Law of Periods - T² ∝ r³)"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [
              "Kepler Laws of Planetary Motion"
            ],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Newton Universal Law of Gravitation & Inverse Square Law Deduction",
            "topicCode": "MH-10-SCIT1-1-1.2",
            "subtopics": [
              "F = G * (m1 * m2) / r²",
              "Value of G = 6.67 * 10^-11 N·m²/kg²",
              "Derivation of inverse square law from Kepler 3rd law"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [
              "Newton Universal Law of Gravitation"
            ],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Acceleration Due to Gravity (g = GM/R²) & Variations in g",
            "topicCode": "MH-10-SCIT1-1-1.3",
            "subtopics": [
              "Value of g on Earth surface = 9.8 m/s²",
              "Variation with altitude / height (decreases)",
              "Variation with depth (decreases to 0 at centre)",
              "Variation along surface: g_pole (9.83 m/s²) > g_equator (9.78 m/s²)"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Mass vs Weight & Gravitational Potential Energy",
            "topicCode": "MH-10-SCIT1-1-1.4",
            "subtopics": [
              "Mass (kg) vs Weight W = mg (N)",
              "Gravitational Potential Energy at height h: -GMm/(R+h)"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.5",
            "name": "Free Fall, Equations of Motion Under Gravity & Escape Velocity (v_esc)",
            "topicCode": "MH-10-SCIT1-1-1.5",
            "subtopics": [
              "Free fall acceleration +g and -g equations",
              "Escape velocity derivation: v_esc = √(2GM/R) = √(2gR) = 11.2 km/s on Earth",
              "Weightlessness in space satellite"
            ],
            "practiceSet": "Exercise 1.5",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Periodic Classification of Elements",
        "topics": [
          {
            "number": "2.1",
            "name": "Dobereiner Triads & Newlands Law of Octaves",
            "topicCode": "MH-10-SCIT1-2-2.1",
            "subtopics": [
              "Dobereiner: Arithmetic mean atomic mass of middle element (e.g. Li, Na, K; Ca, Sr, Ba)",
              "Newlands Law of Octaves: Musical notes similarity (Sa, Re, Ga, Ma, Pa, Dha, Ni) up to Calcium"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Mendeleev Periodic Table: Principles, Merits & Limitations",
            "topicCode": "MH-10-SCIT1-2-2.2",
            "subtopics": [
              "Periodic Law: Properties of elements are periodic functions of atomic masses",
              "Merits: Predicted undiscovered elements (Eka-Boron/Scandium, Eka-Aluminium/Gallium, Eka-Silicon/Germanium), Noble gas inclusion",
              "Limitations: Position of Hydrogen, Isotopes anomaly, Inversion of atomic masses (Co and Ni)"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Modern Periodic Table (Henry Moseley, 1913): Structure (Periods & Groups)",
            "topicCode": "MH-10-SCIT1-2-2.3",
            "subtopics": [
              "Modern Periodic Law: Properties of elements are periodic functions of atomic numbers (Z)",
              "7 Horizontal Periods and 18 Vertical Groups",
              "s-block, p-block, d-block (transition elements), f-block (lanthanides and actinides)"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Periodic Trends: Valency & Atomic Size (Atomic Radius)",
            "topicCode": "MH-10-SCIT1-2-2.4",
            "subtopics": [
              "Valency: determined by valence electrons (increases 1 to 4 then decreases to 0 across period, constant in group)",
              "Atomic radius: Decreases across period (effective nuclear charge increases) and Increases down group (new shells added)"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.5",
            "name": "Periodic Trends: Metallic vs Non-Metallic Character & Electronegativity",
            "topicCode": "MH-10-SCIT1-2-2.5",
            "subtopics": [
              "Metallic character (electropositivity): Decreases across period, Increases down group",
              "Non-metallic character & Electronegativity: Increases across period, Decreases down group",
              "Gradation in Halogen group (F2 gas, Cl2 gas, Br2 liquid, I2 solid)"
            ],
            "practiceSet": "Exercise 2.5",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Chemical Reactions and Equations",
        "topics": [
          {
            "number": "3.1",
            "name": "Chemical Reactions: Rules for Writing & Balancing Equations",
            "topicCode": "MH-10-SCIT1-3-3.1",
            "subtopics": [
              "Reactants and Products, State symbols (s, l, g, aq)",
              "Step-by-step balancing method matching atom counts on LHS and RHS"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Types of Reactions: Combination & Decomposition Reactions",
            "topicCode": "MH-10-SCIT1-3-3.2",
            "subtopics": [
              "Combination: 2Mg + O2 -> 2MgO",
              "Decomposition: Thermal (CaCO3 -> CaO + CO2), Electrolytic (2H2O -> 2H2 + O2)"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Displacement & Double Displacement (Precipitation) Reactions",
            "topicCode": "MH-10-SCIT1-3-3.3",
            "subtopics": [
              "Displacement: CuSO4 + Fe -> FeSO4 + Cu",
              "Double displacement: AgNO3 + NaCl -> AgCl (white ppt) + NaNO3"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Endothermic vs Exothermic Reactions & Factors Affecting Reaction Rate",
            "topicCode": "MH-10-SCIT1-3-3.4",
            "subtopics": [
              "Endothermic (absorbs heat) vs Exothermic (releases heat)",
              "Factors: Nature of reactants, Particle size (smaller = faster), Concentration (higher = faster), Temperature, Catalyst (MnO2 in H2O2 decomposition)"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.5",
            "name": "Oxidation, Reduction, Redox Reactions, Corrosion & Rancidity",
            "topicCode": "MH-10-SCIT1-3-3.5",
            "subtopics": [
              "Oxidation: gain of oxygen / loss of hydrogen / loss of electrons",
              "Reduction: gain of hydrogen / loss of oxygen / gain of electrons",
              "Redox reaction examples and reducing/oxidizing agents",
              "Corrosion: Rusting formula Fe2O3·xH2O, Galvanic cell action on iron surface",
              "Rancidity of edible oils and antioxidant prevention"
            ],
            "practiceSet": "Exercise 3.5",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Effects of Electric Current",
        "topics": [
          {
            "number": "4.1",
            "name": "Energy Transfer in an Electric Circuit & Joule Law of Heating",
            "topicCode": "MH-10-SCIT1-4-4.1",
            "subtopics": [
              "Power P = V * I = I²R = V²/R",
              "Heat energy H = I²Rt (Joules)"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [
              "Joule Law of Heating"
            ],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Heating Appliances & Short Circuit / Overloading Safety",
            "topicCode": "MH-10-SCIT1-4-4.2",
            "subtopics": [
              "Heating coil of high resistivity Nichrome alloy",
              "Tungsten bulb filament (melting point 3422°C)",
              "Electric fuse wire (lead-tin alloy with low melting point), MCB"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Magnetic Effect of Electric Current & Right Hand Thumb Rule",
            "topicCode": "MH-10-SCIT1-4-4.3",
            "subtopics": [
              "Hans Christian Oersted discovery",
              "Right hand thumb rule / Maxwell corkscrew rule for magnetic field direction"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.4",
            "name": "Magnetic Field of Solenoid & Fleming Left Hand Rule",
            "topicCode": "MH-10-SCIT1-4-4.4",
            "subtopics": [
              "Solenoid magnetic field like bar magnet",
              "Fleming Left Hand Rule (Thumb = Force, Forefinger = Magnetic Field, Middle finger = Current)"
            ],
            "practiceSet": "Exercise 4.4",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.5",
            "name": "Electric Motor: Principle, Construction & Working",
            "topicCode": "MH-10-SCIT1-4-4.5",
            "subtopics": [
              "Armature coil in strong magnetic field",
              "Split ring commutator reversing current every half turn, Carbon brushes"
            ],
            "practiceSet": "Exercise 4.5",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.6",
            "name": "Electromagnetic Induction (Michael Faraday) & Fleming Right Hand Rule",
            "topicCode": "MH-10-SCIT1-4-4.6",
            "subtopics": [
              "Galvanometer deflection when magnet moves in coil",
              "Faraday Law of Induction: Induced current is produced whenever magnetic flux changes",
              "Fleming Right Hand Rule for induced current direction"
            ],
            "practiceSet": "Exercise 4.6",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.7",
            "name": "Electric Generator (AC & DC Generator) & Domestic AC Current",
            "topicCode": "MH-10-SCIT1-4-4.7",
            "subtopics": [
              "AC generator with two slip rings (50 Hz alternating current in India, reverses every 1/100 s)",
              "DC generator with split ring commutator (unidirectional current)"
            ],
            "practiceSet": "Exercise 4.7",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Heat",
        "topics": [
          {
            "number": "5.1",
            "name": "Latent Heat: Latent Heat of Fusion & Latent Heat of Vaporization",
            "topicCode": "MH-10-SCIT1-5-5.1",
            "subtopics": [
              "Temperature stays constant during phase change",
              "Specific Latent Heat of Fusion of ice (80 cal/g or 3.33 * 10^5 J/kg)",
              "Specific Latent Heat of Vaporization of steam (540 cal/g or 2.26 * 10^6 J/kg)"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Regelation of Ice & Ice Skate Working",
            "topicCode": "MH-10-SCIT1-5-5.2",
            "subtopics": [
              "Phenomenon: Ice melts under pressure and refreezes when pressure is released"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Anomalous Behavior of Water & Hope Apparatus",
            "topicCode": "MH-10-SCIT1-5-5.3",
            "subtopics": [
              "Water contracts on heating from 0°C to 4°C (Maximum density at 4°C = 1 g/cm³)",
              "Hope apparatus experiment verifying 4°C water at bottom",
              "Survival of aquatic plants and animals in frozen lakes"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.4",
            "name": "Dew Point, Humidity & Relative Humidity",
            "topicCode": "MH-10-SCIT1-5-5.4",
            "subtopics": [
              "Absolute humidity (mass of water vapor in 1 m³ air)",
              "Relative Humidity % = [(Actual mass of vapor) / (Mass required for saturation)] * 100",
              "Dew point temperature (100% relative humidity)"
            ],
            "practiceSet": "Exercise 5.4",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.5",
            "name": "Unit of Heat & Specific Heat Capacity (c)",
            "topicCode": "MH-10-SCIT1-5-5.5",
            "subtopics": [
              "1 Calorie = 4.184 Joules (Heat to raise 1 g water by 1°C from 14.5°C to 15.5°C)",
              "Specific heat capacity: Q = m * c * ΔT",
              "Iron, copper, lead spheres in paraffin wax experiment (c_iron > c_copper > c_lead)"
            ],
            "practiceSet": "Exercise 5.5",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.6",
            "name": "Principle of Heat Exchange & Calorimeter",
            "topicCode": "MH-10-SCIT1-5-5.6",
            "subtopics": [
              "Heat lost by hot object = Heat gained by cold object (in isolated system)"
            ],
            "practiceSet": "Exercise 5.6",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Refraction of Light",
        "topics": [
          {
            "number": "6.1",
            "name": "Refraction of Light & Laws of Refraction",
            "topicCode": "MH-10-SCIT1-6-6.1",
            "subtopics": [
              "Bending of light at boundary of two transparent media",
              "Incident ray, refracted ray, normal lie in same plane",
              "Snell Law: sin i / sin r = constant (n)"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Refractive Index (Absolute & Relative Refractive Index)",
            "topicCode": "MH-10-SCIT1-6-6.2",
            "subtopics": [
              "Absolute refractive index n = c / v (Vacuum speed / Medium speed)",
              "Relative refractive index 2n1 = v1 / v2 = n2 / n1",
              "Optical rarer to denser medium (bends towards normal) and vice versa"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Apparent Depth & Twinkling of Stars / Atmospheric Refraction",
            "topicCode": "MH-10-SCIT1-6-6.3",
            "subtopics": [
              "Apparent depth = Real depth / Refractive index",
              "Twinkling of stars due to changing atmospheric density and refractive index",
              "Planets do not twinkle (extended source)",
              "Advanced sunrise and delayed sunset"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.4",
            "name": "Dispersion of Light & Rainbow Formation",
            "topicCode": "MH-10-SCIT1-6-6.4",
            "subtopics": [
              "Separation of white light into spectrum colors (VIBGYOR) through prism",
              "Wavelength order: Red (700 nm) to Violet (400 nm)",
              "Rainbow formation (Combined refraction, dispersion, and total internal reflection)"
            ],
            "practiceSet": "Exercise 6.4",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.5",
            "name": "Total Internal Reflection & Critical Angle (i_c)",
            "topicCode": "MH-10-SCIT1-6-6.5",
            "subtopics": [
              "When light travels from denser to rarer medium: Critical angle is angle of incidence where angle of refraction is 90°",
              "When i > i_c: Total Internal Reflection occurs",
              "Optical fibers and mirage phenomenon"
            ],
            "practiceSet": "Exercise 6.5",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Lenses",
        "topics": [
          {
            "number": "7.1",
            "name": "Convex and Concave Lenses: Centers of Curvature & Focus",
            "topicCode": "MH-10-SCIT1-7-7.1",
            "subtopics": [
              "Biconvex (converging) vs Biconcave (diverging) lenses",
              "Centers of Curvature (C1, C2), Radii (R1, R2), Optical Centre (O), Principal Focus (F1, F2), Focal Length (f)"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Rules for Drawing Ray Diagrams for Lenses",
            "topicCode": "MH-10-SCIT1-7-7.2",
            "subtopics": [
              "Ray parallel to principal axis passes through focus",
              "Ray passing through focus emerges parallel",
              "Ray passing through optical centre passes without deviation"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Ray Diagrams for Images Formed by Convex & Concave Lenses",
            "topicCode": "MH-10-SCIT1-7-7.3",
            "subtopics": [
              "Convex lens 6 positions (Real/inverted images, and Virtual/erect magnified image when object between F1 and O)",
              "Concave lens (Always virtual, erect, diminished image)"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.4",
            "name": "Lens Formula (1/v - 1/u = 1/f) & Magnification (M = v/u = h2/h1)",
            "topicCode": "MH-10-SCIT1-7-7.4",
            "subtopics": [
              "Cartesian sign conventions for lenses",
              "Numerical problem solving for object/image distances and heights"
            ],
            "practiceSet": "Exercise 7.4",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.5",
            "name": "Power of Lens (P = 1/f in metres) & Combination of Lenses",
            "topicCode": "MH-10-SCIT1-7-7.5",
            "subtopics": [
              "Unit Dioptre (D)",
              "Convex lens power is positive, Concave lens power is negative",
              "Combined power P = P1 + P2"
            ],
            "practiceSet": "Exercise 7.5",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.6",
            "name": "Human Eye Anatomy & Defects of Vision (Myopia, Hypermetropia, Presbyopia)",
            "topicCode": "MH-10-SCIT1-7-7.6",
            "subtopics": [
              "Ciliary muscles accommodation",
              "Myopia (Near sightedness - concave lens correction)",
              "Hypermetropia (Far sightedness - convex lens correction)",
              "Presbyopia (Bifocal lens correction)"
            ],
            "practiceSet": "Exercise 7.6",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.7",
            "name": "Optical Instruments: Simple Microscope, Compound Microscope & Astronomical Telescope",
            "topicCode": "MH-10-SCIT1-7-7.7",
            "subtopics": [
              "Simple microscope (Magnifying glass: M = 1 + D/f)",
              "Compound microscope (Objective lens of small aperture and Eyepiece of large aperture)",
              "Astronomical refracting telescope (Objective of large focal length/aperture and Eyepiece of small focal length)"
            ],
            "practiceSet": "Exercise 7.7",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      },
      {
        "number": "8",
        "name": "Metallurgy",
        "topics": [
          {
            "number": "8.1",
            "name": "Physical & Chemical Properties of Metals and Non-Metals",
            "topicCode": "MH-10-SCIT1-8-8.1",
            "subtopics": [
              "Reactivity of metals with oxygen, water, dilute acids, and other metal salt solutions",
              "Reactivity series of metals"
            ],
            "practiceSet": "Exercise 8.1",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.2",
            "name": "Ionic Compounds: Formation, Crystal Lattice & Properties",
            "topicCode": "MH-10-SCIT1-8-8.2",
            "subtopics": [
              "Electron transfer, strong electrostatic attraction force",
              "High melting points, electrical conduction in liquid/molten state"
            ],
            "practiceSet": "Exercise 8.2",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.3",
            "name": "Basic Principles of Metallurgy & Concentration of Ores",
            "topicCode": "MH-10-SCIT1-8-8.3",
            "subtopics": [
              "Minerals, ores, gangue matrix",
              "Gravity separation: Wilfley table method & Hydraulic separation",
              "Magnetic separation method (e.g. tin stone and magnetic wolframite)",
              "Froth floatation method (for sulphide ores using pine oil and collectors)",
              "Leaching method (Extraction of Aluminium from Bauxite using NaOH / Baeyer process)"
            ],
            "practiceSet": "Exercise 8.3",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.4",
            "name": "Extraction of Reactive Metals: Electrolytic Reduction of Alumina (Hall-Heroult Process)",
            "topicCode": "MH-10-SCIT1-8-8.4",
            "subtopics": [
              "Purification of bauxite (Hall and Baeyer processes)",
              "Electrolysis of molten alumina with Cryolite (Na3AlF6) and Fluorspar (CaF2)",
              "Cathode: carbon lining (molten Al), Anode: graphite rods (O2 gas)"
            ],
            "practiceSet": "Exercise 8.4",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.5",
            "name": "Extraction of Moderately & Less Reactive Metals (Roasting & Calcination)",
            "topicCode": "MH-10-SCIT1-8-8.5",
            "subtopics": [
              "Roasting of zinc blende (2ZnS + 3O2 -> 2ZnO + 2SO2)",
              "Calcination of calamine (ZnCO3 -> ZnO + CO2)",
              "Reduction of ZnO using carbon coke (ZnO + C -> Zn + CO)"
            ],
            "practiceSet": "Exercise 8.5",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.6",
            "name": "Corrosion of Metals & Prevention Methods",
            "topicCode": "MH-10-SCIT1-8-8.6",
            "subtopics": [],
            "practiceSet": "Exercise 8.6",
            "theorems": [],
            "problemSet": "Problem Set 8"
          }
        ]
      },
      {
        "number": "9",
        "name": "Carbon Compounds",
        "topics": [
          {
            "number": "9.1",
            "name": "Bonds in Carbon Compounds & Tetravalency / Catenation Ability",
            "topicCode": "MH-10-SCIT1-9-9.1",
            "subtopics": [
              "Covalent single, double, and triple bonds",
              "Catenation power: open chains, branched chains, closed ring structures",
              "Isomerism: Structural isomers of butane (n-butane and isobutane)"
            ],
            "practiceSet": "Exercise 9.1",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.2",
            "name": "Hydrocarbons: Saturated (Alkanes) vs Unsaturated (Alkenes & Alkynes)",
            "topicCode": "MH-10-SCIT1-9-9.2",
            "subtopics": [
              "Alkanes (C_n H_2n+2), Alkenes (C_n H_2n), Alkynes (C_n H_2n-2)",
              "Straight chain, branched chain and cyclic hydrocarbons (Cyclohexane, Benzene C6H6)"
            ],
            "practiceSet": "Exercise 9.2",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.3",
            "name": "Functional Groups & Homologous Series",
            "topicCode": "MH-10-SCIT1-9-9.3",
            "subtopics": [
              "Halide (-X), Alcohol (-OH), Aldehyde (-CHO), Ketone (-CO-), Carboxylic Acid (-COOH), Ether (-O-), Ester (-COO-), Amine (-NH2)",
              "Homologous series characteristics (same general formula, gradation in melting/boiling points)"
            ],
            "practiceSet": "Exercise 9.3",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.4",
            "name": "IUPAC Nomenclature of Carbon Compounds",
            "topicCode": "MH-10-SCIT1-9-9.4",
            "subtopics": [
              "Parent alkane identification, numbering carbon chain from functional group side, prefix and suffix rules"
            ],
            "practiceSet": "Exercise 9.4",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.5",
            "name": "Chemical Properties: Combustion, Oxidation, Addition & Substitution",
            "topicCode": "MH-10-SCIT1-9-9.5",
            "subtopics": [
              "Combustion equation: CH4 + 2O2 -> CO2 + 2H2O + Heat",
              "Oxidation of ethanol with alkaline KMnO4 to ethanoic acid",
              "Addition reaction of ethene with H2 (catalytic hydrogenation)",
              "Substitution of methane with chlorine in presence of sunlight"
            ],
            "practiceSet": "Exercise 9.5",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.6",
            "name": "Important Carbon Compounds: Ethanol & Ethanoic Acid",
            "topicCode": "MH-10-SCIT1-9-9.6",
            "subtopics": [
              "Ethanol properties, reaction with sodium (H2 gas), dehydration with conc. H2SO4 at 170°C to ethene",
              "Ethanoic acid (Glacial acetic acid melting point 17°C), esterification reaction with ethanol, saponification reaction"
            ],
            "practiceSet": "Exercise 9.6",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.7",
            "name": "Macromolecules and Polymers (Natural & Synthetic Polymers)",
            "topicCode": "MH-10-SCIT1-9-9.7",
            "subtopics": [
              "Polymers formed by repeated monomer units (Polyethylene from ethylene)",
              "Natural polymers: Polysaccharides (starch, cellulose), Proteins (amino acids), DNA/RNA, Natural rubber (isoprene)",
              "Synthetic polymers: Teflon, Nylon, Polystyrene, PVC, Terylene"
            ],
            "practiceSet": "Exercise 9.7",
            "theorems": [],
            "problemSet": "Problem Set 9"
          }
        ]
      },
      {
        "number": "10",
        "name": "Space Missions",
        "topics": [
          {
            "number": "10.1",
            "name": "Need & Importance of Space Missions",
            "topicCode": "MH-10-SCIT1-10-10.1",
            "subtopics": [
              "Telecommunication, weather broadcasting, disaster management, military surveillance, astronomy"
            ],
            "practiceSet": "Exercise 10.1",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.2",
            "name": "Artificial Satellites: Types & Functions",
            "topicCode": "MH-10-SCIT1-10-10.2",
            "subtopics": [
              "Weather satellites (INSAT, GSAT)",
              "Communication satellites",
              "Broadcast satellites",
              "Navigational satellites (IRNSS / NavIC)",
              "Earth observation satellites (IRS)",
              "Military / surveillance satellites"
            ],
            "practiceSet": "Exercise 10.2",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.3",
            "name": "Orbits of Artificial Satellites (GEO, MEO, LEO)",
            "topicCode": "MH-10-SCIT1-10-10.3",
            "subtopics": [
              "High Earth Orbits (HEO / GEO): Height > 35,786 km, Period 24 hours (geostationary)",
              "Medium Earth Orbits (MEO): Height 2,000 to 35,786 km, Period 2 to 24 hours (GPS)",
              "Low Earth Orbits (LEO): Height 180 to 2,000 km, Period 90 minutes (ISS, Hubble)"
            ],
            "practiceSet": "Exercise 10.3",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.4",
            "name": "Satellite Launch Vehicles (PSLV by ISRO) & Multi-Stage Rockets",
            "topicCode": "MH-10-SCIT1-10-10.4",
            "subtopics": [
              "Newton 3rd law and conservation of momentum principle",
              "Multi-stage rocket fuel stages detachment for mass reduction"
            ],
            "practiceSet": "Exercise 10.4",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.5",
            "name": "Space Missions Beyond Earth (Moon, Mars) & Space Debris Management",
            "topicCode": "MH-10-SCIT1-10-10.5",
            "subtopics": [
              "Chandrayaan-1 (discovery of water molecules on Moon), Chandrayaan-2 and 3",
              "Mangalyaan (Mars Orbiter Mission - MOM, 2013)",
              "Space debris hazards to operational satellites and space debris mitigation methods"
            ],
            "practiceSet": "Exercise 10.5",
            "theorems": [],
            "problemSet": "Problem Set 10"
          }
        ]
      }
    ]
  },
  {
    "docId": "mh_10_scit2",
    "board": "Maharashtra Board",
    "boardCode": "MH",
    "class": "10",
    "subject": "Science and Technology Part - 2",
    "subjectCode": "SCIT2",
    "chapters": [
      {
        "number": "1",
        "name": "Heredity and Evolution",
        "topics": [
          {
            "number": "1.1",
            "name": "Heredity & Molecular Protein Synthesis (Transcription, Translation, Translocation)",
            "topicCode": "MH-10-SCIT2-1-1.1",
            "subtopics": [
              "Central Dogma of molecular biology: DNA -> RNA -> Protein",
              "Transcription: Synthesis of mRNA from DNA template strand using RNA polymerase (Codons & Triplet codon discoveries by Dr. Har Gobind Khorana)",
              "Translation: tRNA with anticodon complementary to mRNA brings amino acids to ribosome",
              "Translocation: Ribosome moves along mRNA by one triplet codon"
            ],
            "practiceSet": "Exercise 1.1",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.2",
            "name": "Mutation: Gene Sequences Alterations & Genetic Disorders",
            "topicCode": "MH-10-SCIT2-1-1.2",
            "subtopics": [
              "Sudden changes in nucleotide sequence",
              "Sickle cell anemia monogenic mutation"
            ],
            "practiceSet": "Exercise 1.2",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.3",
            "name": "Evolution & Evidences of Evolution (Morphological, Anatomical, Vestigial Organs, Paleontological, Connecting Links, Embryological)",
            "topicCode": "MH-10-SCIT2-1-1.3",
            "subtopics": [
              "Morphological: Similarity in bone and muscle structure of mouth/nose/ears",
              "Anatomical: Similar bone structure in human hand, cat foreleg, whale flipper, bat wing",
              "Vestigial organs: Appendix, tailbone (coccyx), wisdom teeth, ear pinna muscles",
              "Paleontological: Fossils and Carbon Dating (C-14 half-life Willard Libby)",
              "Connecting links: Peripatus (annelida & arthropoda), Duck-billed platypus (reptiles & mammals), Lungfish (fishes & amphibians)",
              "Embryological: Extreme similarity in initial embryonic stages of vertebrates"
            ],
            "practiceSet": "Exercise 1.3",
            "theorems": [],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.4",
            "name": "Darwin Theory of Natural Selection & Lamarckism",
            "topicCode": "MH-10-SCIT2-1-1.4",
            "subtopics": [
              "Darwin \"Origin of Species\" (Survival of the fittest, Overproduction, Struggle for existence)",
              "Lamarckism: Theory of inheritance of acquired characters (Use and disuse of organs - giraffe neck) and its disproof"
            ],
            "practiceSet": "Exercise 1.4",
            "theorems": [
              "Darwin Theory of Natural Selection"
            ],
            "problemSet": "Problem Set 1"
          },
          {
            "number": "1.5",
            "name": "Speciation & Journey of Human Evolution",
            "topicCode": "MH-10-SCIT2-1-1.5",
            "subtopics": [
              "Speciation: Formation of new species due to genetic variation and geographic/reproductive isolation",
              "Human evolution chronology: Dryopithecus -> Ramapithecus -> Australopithecus -> Homo habilis (handy man) -> Homo erectus (upright man, discovered fire) -> Neanderthal man (first wise man, 100,000 yrs ago) -> Cro-Magnon man (Homo sapiens, 50,000 yrs ago) -> Agriculture (10,000 yrs ago)"
            ],
            "practiceSet": "Exercise 1.5",
            "theorems": [],
            "problemSet": "Problem Set 1"
          }
        ]
      },
      {
        "number": "2",
        "name": "Life Processes in Living Organisms Part - 1",
        "topics": [
          {
            "number": "2.1",
            "name": "Living Organisms & Respiration (External vs Cellular Respiration)",
            "topicCode": "MH-10-SCIT2-2-2.1",
            "subtopics": [
              "Respiration at body level (inhalation/exhalation)",
              "Respiration at cellular level (complete oxidation of glucose)"
            ],
            "practiceSet": "Exercise 2.1",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.2",
            "name": "Aerobic Cellular Respiration: Glycolysis, TCA Cycle (Krebs Cycle) & Electron Transfer Chain (ETC)",
            "topicCode": "MH-10-SCIT2-2-2.2",
            "subtopics": [
              "Glycolysis (EMP pathway in cytoplasm): Glucose -> 2 Pyruvic acid + 2 ATP + 2 NADH2 + 2 H2O",
              "TCA / Krebs Cycle (in mitochondrial matrix): Acetyl-CoA -> CO2 + H2O + NADH2 + FADH2 + ATP",
              "Electron Transfer Chain (on mitochondrial cristae): NADH2 yields 3 ATP, FADH2 yields 2 ATP",
              "Total yield = 38 ATP per glucose molecule"
            ],
            "practiceSet": "Exercise 2.2",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.3",
            "name": "Anaerobic Respiration: Fermentation in Yeast and Muscle Cells",
            "topicCode": "MH-10-SCIT2-2-2.3",
            "subtopics": [
              "Fermentation of pyruvic acid to alcohol/lactic acid with 2 ATP yield",
              "Lactic acid accumulation causing fatigue in athletes"
            ],
            "practiceSet": "Exercise 2.3",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.4",
            "name": "Energy Production from Different Food Components (Proteins, Fats, Vitamins)",
            "topicCode": "MH-10-SCIT2-2-2.4",
            "subtopics": [
              "Carbohydrates yield 4 kcal/g energy",
              "Proteins (amino acids) yield 4 kcal/g energy",
              "Lipids / Fats (fatty acids and glycerol) yield 9 kcal/g energy",
              "Water-soluble (B, C) and Fat-soluble (A, D, E, K) vitamins"
            ],
            "practiceSet": "Exercise 2.4",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.5",
            "name": "Cell Division: Mitosis (Karyokinesis & Cytokinesis) & Somatic Growth",
            "topicCode": "MH-10-SCIT2-2-2.5",
            "subtopics": [
              "Karyokinesis stages: Prophase (chromosomes condense, nuclear membrane vanishes), Metaphase (chromosomes align on equatorial plate), Anaphase (centromeres split, sister chromatids pulled to opposite poles), Telophase (chromosomes decondense, nuclear membrane reforms)",
              "Cytokinesis: Cell plate in plants, cleavage furrow in animals",
              "Significance: Body growth, wound healing, blood cell restoration"
            ],
            "practiceSet": "Exercise 2.5",
            "theorems": [],
            "problemSet": "Problem Set 2"
          },
          {
            "number": "2.6",
            "name": "Cell Division: Meiosis (Meiosis I, Meiosis II & Crossing Over)",
            "topicCode": "MH-10-SCIT2-2-2.6",
            "subtopics": [
              "Meiosis I: Prophase I stages (Leptotene, Zygotene, Pachytene crossing over/recombination, Diplotene, Diakinesis)",
              "Reduction division (2n -> n) producing 4 haploid gametes",
              "Significance of genetic variation in sexual reproduction"
            ],
            "practiceSet": "Exercise 2.6",
            "theorems": [],
            "problemSet": "Problem Set 2"
          }
        ]
      },
      {
        "number": "3",
        "name": "Life Processes in Living Organisms Part - 2",
        "topics": [
          {
            "number": "3.1",
            "name": "Asexual Reproduction in Unicellular Organisms (Binary Fission, Multiple Fission, Budding)",
            "topicCode": "MH-10-SCIT2-3-3.1",
            "subtopics": [
              "Binary fission: Simple (Amoeba), Transverse (Paramecium), Longitudinal (Euglena)",
              "Multiple fission in Amoeba during adverse conditions (cyst formation)",
              "Budding in Yeast"
            ],
            "practiceSet": "Exercise 3.1",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.2",
            "name": "Asexual Reproduction in Multicellular Organisms",
            "topicCode": "MH-10-SCIT2-3-3.2",
            "subtopics": [
              "Fragmentation (Spirogyra)",
              "Regeneration (Planaria)",
              "Budding (Hydra)",
              "Vegetative propagation (Potato eyes, Bryophyllum foliar buds, Sugarcane root buds)",
              "Spore formation (Mucor/Rhizopus sporangiospores)"
            ],
            "practiceSet": "Exercise 3.2",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.3",
            "name": "Sexual Reproduction in Plants: Flower Structure, Pollination & Double Fertilisation",
            "topicCode": "MH-10-SCIT2-3-3.3",
            "subtopics": [
              "Floral whorls: Calyx, Corolla, Androecium (stamen), Gynoecium (carpel/pistil)",
              "Unisexual vs Bisexual flowers",
              "Self vs Cross pollination",
              "Double fertilisation: Syngamy (Zygote) and Triple Fusion (Endosperm)"
            ],
            "practiceSet": "Exercise 3.3",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.4",
            "name": "Human Male Reproductive System Anatomy & Spermatogenesis",
            "topicCode": "MH-10-SCIT2-3-3.4",
            "subtopics": [
              "Testes in scrotum, Seminiferous tubules, Epididymis, Vas deferens, Ejaculatory duct, Urethra",
              "Accessory glands: Seminal vesicles, Prostate gland, Cowper glands",
              "Sperm anatomy (Head with acrosome/nucleus, Middle piece with mitochondria, Tail)"
            ],
            "practiceSet": "Exercise 3.4",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.5",
            "name": "Human Female Reproductive System Anatomy & Oogenesis",
            "topicCode": "MH-10-SCIT2-3-3.5",
            "subtopics": [
              "Pair of Ovaries, Oviducts (Fallopian tubes), Uterus, Vagina",
              "Monthly ovulation of one mature ovum"
            ],
            "practiceSet": "Exercise 3.5",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.6",
            "name": "Menstrual Cycle: Phases & Hormonal Control (FSH, LH, Estrogen, Progesterone)",
            "topicCode": "MH-10-SCIT2-3-3.6",
            "subtopics": [
              "Follicular phase (FSH stimulates follicle growth & estrogen secretion)",
              "Ovulatory phase (LH surge causes follicle rupture and ovulation around day 14)",
              "Luteal phase (Corpus luteum secretes progesterone to thicken endometrium)",
              "Menstrual bleeding phase (Corpus albicans regression when fertilisation does not occur)"
            ],
            "practiceSet": "Exercise 3.6",
            "theorems": [],
            "problemSet": "Problem Set 3"
          },
          {
            "number": "3.7",
            "name": "Reproduction & Modern Assistive Technologies (IVF, Surrogacy, Sperm Bank) & Twins",
            "topicCode": "MH-10-SCIT2-3-3.7",
            "subtopics": [
              "In Vitro Fertilisation (IVF - test tube baby)",
              "Surrogacy (womb mother)",
              "Sperm banks and Cryopreservation",
              "Twins: Monozygotic (identical, same sex) vs Dizygotic (fraternal) twins and Siamese conjoined twins",
              "Reproductive health and population explosion"
            ],
            "practiceSet": "Exercise 3.7",
            "theorems": [],
            "problemSet": "Problem Set 3"
          }
        ]
      },
      {
        "number": "4",
        "name": "Environmental Management",
        "topics": [
          {
            "number": "4.1",
            "name": "Ecosystem Review & Balance of Food Chains/Webs",
            "topicCode": "MH-10-SCIT2-4-4.1",
            "subtopics": [
              "Biotic and Abiotic components interaction",
              "Biogeochemical cycles equilibrium"
            ],
            "practiceSet": "Exercise 4.1",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.2",
            "name": "Environmental Conservation & Factors Affecting Environment (Pollution & Laws)",
            "topicCode": "MH-10-SCIT2-4-4.2",
            "subtopics": [
              "Air, water, soil pollution sources",
              "Environment Protection Act 1986, Forest Conservation Act 1980",
              "National Green Tribunal (NGT)"
            ],
            "practiceSet": "Exercise 4.2",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.3",
            "name": "Sacred Groves (Devrai) of Maharashtra & Conservation Heritage",
            "topicCode": "MH-10-SCIT2-4-4.3",
            "subtopics": [
              "Forests conserved in the name of God by local communities in Western Ghats"
            ],
            "practiceSet": "Exercise 4.3",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.4",
            "name": "Biodiversity: Three Levels (Genetic, Species, Ecosystem Diversity)",
            "topicCode": "MH-10-SCIT2-4-4.4",
            "subtopics": [
              "Genetic diversity within same species",
              "Species diversity in a region",
              "Ecosystem diversity across geographic biomes"
            ],
            "practiceSet": "Exercise 4.4",
            "theorems": [],
            "problemSet": "Problem Set 4"
          },
          {
            "number": "4.5",
            "name": "Biodiversity Hotspots & Classification of Threatened Species",
            "topicCode": "MH-10-SCIT2-4-4.5",
            "subtopics": [
              "34 Global Hotspots (Western Ghats, Indo-Burma, Himalayas in India)",
              "IUCN Red Data Book categories: Endangered species (Lion-tailed macaque, Red panda), Rare species (Musk deer), Vulnerable species (Tiger, Lion), Indeterminate species (Giant squirrel / Shekru - State animal of Maharashtra)"
            ],
            "practiceSet": "Exercise 4.5",
            "theorems": [],
            "problemSet": "Problem Set 4"
          }
        ]
      },
      {
        "number": "5",
        "name": "Towards Green Energy",
        "topics": [
          {
            "number": "5.1",
            "name": "Generation of Electrical Energy & Principle of Electromagnetic Induction",
            "topicCode": "MH-10-SCIT2-5-5.1",
            "subtopics": [
              "Turbine rotation driving generator armature",
              "Thermal vs mechanical energy conversions"
            ],
            "practiceSet": "Exercise 5.1",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.2",
            "name": "Thermal Power Plants & Air Pollution Problems",
            "topicCode": "MH-10-SCIT2-5-5.2",
            "subtopics": [
              "Burning of coal to produce high pressure steam",
              "Energy conversion schematic: Chemical energy in coal -> Thermal energy -> Kinetic energy in steam -> Kinetic energy in turbine -> Electrical energy",
              "Environmental problems: Greenhouse gas emissions (CO2), SOx/NOx toxic gases, fly ash disposal"
            ],
            "practiceSet": "Exercise 5.2",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.3",
            "name": "Nuclear Power Plants: Nuclear Fission of Uranium-235",
            "topicCode": "MH-10-SCIT2-5-5.3",
            "subtopics": [
              "Chain reaction: U-235 + Neutron -> Barium-141 + Krypton-92 + 3 Neutrons + 200 MeV energy",
              "Control rods (Boron/Cadmium) and Moderator (Heavy water/Graphite)",
              "Nuclear waste disposal hazards and radiation accident risks (Chernobyl, Fukushima)"
            ],
            "practiceSet": "Exercise 5.3",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.4",
            "name": "Natural Gas Power Plants",
            "topicCode": "MH-10-SCIT2-5-5.4",
            "subtopics": [
              "Combustion of natural gas driving gas turbine (Higher efficiency, lower pollution than coal)"
            ],
            "practiceSet": "Exercise 5.4",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.5",
            "name": "Hydroelectric Power Plants: Clean Renewable Energy",
            "topicCode": "MH-10-SCIT2-5-5.5",
            "subtopics": [
              "Potential energy of dam water -> Kinetic energy of flowing water -> Kinetic energy in turbine -> Electrical energy",
              "Advantages (no fuel combustion) and Disadvantages (displacement of villages, submergence of forests, river siltation)"
            ],
            "practiceSet": "Exercise 5.5",
            "theorems": [],
            "problemSet": "Problem Set 5"
          },
          {
            "number": "5.6",
            "name": "Wind Energy & Solar Energy (Photovoltaic Cells & Solar Thermal Plants)",
            "topicCode": "MH-10-SCIT2-5-5.6",
            "subtopics": [
              "Windmill kinetic energy conversion",
              "Solar Photovoltaic (PV) cells: Silicon semiconductor converting sunlight directly into DC electricity",
              "Solar PV modules, strings, and arrays with inverters",
              "Solar thermal collectors focusing sunlight to boil water for steam turbines"
            ],
            "practiceSet": "Exercise 5.6",
            "theorems": [],
            "problemSet": "Problem Set 5"
          }
        ]
      },
      {
        "number": "6",
        "name": "Animal Classification",
        "topics": [
          {
            "number": "6.1",
            "name": "History of Animal Classification (Aristotle to Robert Whittaker & Carl Woese)",
            "topicCode": "MH-10-SCIT2-6-6.1",
            "subtopics": [
              "Artificial classification (Aristotle, Pliny)",
              "Traditional two subkingdoms: Non-Chordates vs Chordates"
            ],
            "practiceSet": "Exercise 6.1",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.2",
            "name": "Criteria for Modern Animal Classification",
            "topicCode": "MH-10-SCIT2-6-6.2",
            "subtopics": [
              "Levels of organization (Cellular, Tissue, Organ, Organ-system level)",
              "Body symmetry (Asymmetrical e.g. Sponges, Radial e.g. Starfish/Hydra, Bilateral e.g. Human/Fish)",
              "Germ layers (Diploblastic - Ectoderm & Endoderm; Triploblastic - Ectoderm, Mesoderm, Endoderm)",
              "Body cavity / Coelom (Acoelomate e.g. Platyhelminthes, Pseudocoelomate e.g. Aschelminthes, Eucoelomate true coelom e.g. Annelida to Chordata)",
              "Body segmentation (Metameric segmentation in Annelids)"
            ],
            "practiceSet": "Exercise 6.2",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.3",
            "name": "Phylum Porifera (Sponges) & Phylum Coelenterata / Cnidaria",
            "topicCode": "MH-10-SCIT2-6-6.3",
            "subtopics": [
              "Porifera: Cellular level, ostia (pores) and osculum, collar cells (choanocytes), spicules (Sycon, Euspongia bath sponge)",
              "Coelenterata: Radial symmetry, diploblastic, tentacles with cnidoblasts (stinging cells for defense/prey capture), Polyp vs Medusa body forms (Hydra, Jellyfish/Aurelia, Physalia, Sea anemone)"
            ],
            "practiceSet": "Exercise 6.3",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.4",
            "name": "Phylum Platyhelminthes, Aschelminthes & Phylum Annelida",
            "topicCode": "MH-10-SCIT2-6-6.4",
            "subtopics": [
              "Platyhelminthes (Flatworms): Bilateral, triploblastic, acoelomate, hermaphrodite, hooks and suckers (Planaria, Tapeworm/Taenia, Liverfluke)",
              "Aschelminthes (Roundworms): Pseudocoelomate, cylindrical body, sexual dimorphism (Ascaris intestinal worm, Filarial worm / Wuchereria bancrofti)",
              "Annelida (Segmented worms): Eucoelomate, metameric rings, setae/parapodia for locomotion, closed circulation (Earthworm, Leech, Nereis)"
            ],
            "practiceSet": "Exercise 6.4",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.5",
            "name": "Phylum Arthropoda & Phylum Mollusca",
            "topicCode": "MH-10-SCIT2-6-6.5",
            "subtopics": [
              "Arthropoda (Largest phylum): Jointed appendages, chitinous exoskeleton, open circulation, compound eyes (Crab, Prawn, Butterfly, Mosquito, Scorpion, Centipede)",
              "Mollusca (Second largest phylum): Soft unsegmented body, calcareous shell, muscular foot, mantle cavity (Snail, Bivalve/Pearl oyster, Octopus)"
            ],
            "practiceSet": "Exercise 6.5",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.6",
            "name": "Phylum Echinodermata & Phylum Hemichordata",
            "topicCode": "MH-10-SCIT2-6-6.6",
            "subtopics": [
              "Echinodermata: Calcareous spines, adult radial symmetry & larva bilateral symmetry, water vascular system with tube feet (Starfish, Sea urchin, Sea cucumber, Brittle star)",
              "Hemichordata: Acorn worms, Proboscis, collar, trunk body, stomochord (Balanoglossus, Saccoglossus - Connecting link between non-chordates and chordates)"
            ],
            "practiceSet": "Exercise 6.6",
            "theorems": [],
            "problemSet": "Problem Set 6"
          },
          {
            "number": "6.7",
            "name": "Phylum Chordata: Urochordata, Cephalochordata & Vertebrata Classes",
            "topicCode": "MH-10-SCIT2-6-6.7",
            "subtopics": [
              "Chordata features: Notochord, dorsal hollow nerve cord, pharyngeal gill slits",
              "Subphylum Urochordata (Herdmania, Doliolum - Notochord only in larval tail)",
              "Subphylum Cephalochordata (Amphioxus - Notochord extends whole length)",
              "Class Cyclostomata (Jawless circular mouth e.g. Petromyzon)",
              "Class Pisces (Fishes: cold-blooded, gills, fins, 2-chambered heart e.g. Shark, Rohu, Pomfret)",
              "Class Amphibia (Dual habitat, moist skin, 3-chambered heart, external fertilisation e.g. Frog, Toad, Salamander)",
              "Class Reptilia (Poikilotherms, creeping locomotion, scaly dry skin e.g. Wall lizard, Snake, Crocodile)",
              "Class Aves (Birds: homeotherms, pneumatic bones, feathers, beak, 4-chambered heart e.g. Peacock, Pigeon, Ostrich)",
              "Class Mammalia (Mammary glands, body hair, pinna, homeotherms, viviparous e.g. Bat, Whale, Human, Kangaroo)"
            ],
            "practiceSet": "Exercise 6.7",
            "theorems": [],
            "problemSet": "Problem Set 6"
          }
        ]
      },
      {
        "number": "7",
        "name": "Introduction to Microbiology",
        "topics": [
          {
            "number": "7.1",
            "name": "Applied & Industrial Microbiology: Dairy Products & Cheese Production",
            "topicCode": "MH-10-SCIT2-7-7.1",
            "subtopics": [
              "Lactic acid fermentation of milk (Lactobacillus bulgaricus, Streptococcus thermophilus)",
              "Cheese production: Coagulation by rennet microbial enzymes (Protease / Chymosin), ripening by fungi (Roquefort cheese)"
            ],
            "practiceSet": "Exercise 7.1",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.2",
            "name": "Probiotics & Yoghurt Health Benefits",
            "topicCode": "MH-10-SCIT2-7-7.2",
            "subtopics": [
              "Probiotic organisms: Lactobacillus acidophilus, Bifidobacterium bifidum",
              "Restoring gut microflora balance, suppressing pathogenic Clostridium"
            ],
            "practiceSet": "Exercise 7.2",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.3",
            "name": "Bread, Vinegar Production & Microbial Enzymes",
            "topicCode": "MH-10-SCIT2-7-7.3",
            "subtopics": [
              "Yeast (Saccharomyces cerevisiae) baker yeast for bread sponge rise",
              "Vinegar production (Ethanol oxidized to Acetic acid by Acetobacter and Gluconobacter)",
              "Microbial enzymes: Proteases, lipases, cellulases used in detergents and fruit juice clarification"
            ],
            "practiceSet": "Exercise 7.3",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.4",
            "name": "Industrial Organic Acids, Amino Acids & Antibiotics",
            "topicCode": "MH-10-SCIT2-7-7.4",
            "subtopics": [
              "Citric acid (Aspergillus niger), Gluconic acid, L-Glutamic acid (Monosodium glutamate / Ajinomoto)",
              "Antibiotics: Penicillin, Cephalosporins, Streptomycin, Tetracycline, Rifamycin"
            ],
            "practiceSet": "Exercise 7.4",
            "theorems": [],
            "problemSet": "Problem Set 7"
          },
          {
            "number": "7.5",
            "name": "Microbial Pollution Control (Bioremediation of Oil Spills & Sewage)",
            "topicCode": "MH-10-SCIT2-7-7.5",
            "subtopics": [
              "Hydrocarbonoclastic Bacteria (HCB): Pseudomonas and Alcanivorax borkumensis decomposing oceanic oil slicks",
              "Sewage treatment plant (STP) using anaerobic microbial digesters",
              "Bio-fuels: Bio-ethanol and bio-diesel from algae and sugarcane molasses"
            ],
            "practiceSet": "Exercise 7.5",
            "theorems": [],
            "problemSet": "Problem Set 7"
          }
        ]
      },
      {
        "number": "8",
        "name": "Cell Biology and Biotechnology",
        "topics": [
          {
            "number": "8.1",
            "name": "Cytology & Stem Cells: Types (Embryonic & Adult Stem Cells)",
            "topicCode": "MH-10-SCIT2-8-8.1",
            "subtopics": [
              "Stem cell pluripotency and totipotency",
              "Embryonic stem cells from blastocyst (inner cell mass)",
              "Adult stem cells from bone marrow, umbilical cord blood, adipose tissue",
              "Stem cell therapy in Parkinson, Alzheimer, diabetes, leukemia"
            ],
            "practiceSet": "Exercise 8.1",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.2",
            "name": "Organ Transplantation and Body Donation",
            "topicCode": "MH-10-SCIT2-8-8.2",
            "subtopics": [
              "Brain death concept",
              "Transplantation of kidneys, liver, heart, cornea, skin",
              "Transplantation of Human Organs Act 1994"
            ],
            "practiceSet": "Exercise 8.2",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.3",
            "name": "Biotechnology in Agriculture: GM Crops, Biofertilisers & Biopesticides",
            "topicCode": "MH-10-SCIT2-8-8.3",
            "subtopics": [
              "Bt Cotton (Bacillus thuringiensis cry gene against bollworm)",
              "Bt Brinjal, Golden Rice (Vitamin A enriched with beta-carotene)",
              "Herbicide-tolerant crop plants",
              "Biofertilisers: Rhizobium, Azotobacter, Mycorrhiza"
            ],
            "practiceSet": "Exercise 8.3",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.4",
            "name": "Biotechnology in Human Health: Vaccines, Insulin, Interferon & Gene Therapy",
            "topicCode": "MH-10-SCIT2-8-8.4",
            "subtopics": [
              "Recombinant DNA technology for Human Insulin (Humulin)",
              "Vaccine production through recombinant subunit antigens (Hepatitis B vaccine)",
              "Interferon (antiviral protein)",
              "Gene therapy for ADA deficiency and somatic cell genetic corrections",
              "DNA Fingerprinting in forensic medicine (Dr. Lalji Singh in India)"
            ],
            "practiceSet": "Exercise 8.4",
            "theorems": [],
            "problemSet": "Problem Set 8"
          },
          {
            "number": "8.5",
            "name": "White, Blue & Green Revolutions in India",
            "topicCode": "MH-10-SCIT2-8-8.5",
            "subtopics": [
              "Green Revolution (Dr. M.S. Swaminathan and Norman Borlaug high-yielding wheat/rice varieties)",
              "White Revolution (Dr. Verghese Kurien - Operation Flood dairy co-operatives / AMUL)",
              "Blue Revolution (Dr. Hiralal Chaudhari & Dr. Arun Krishnan - Aquaculture and Fisheries)"
            ],
            "practiceSet": "Exercise 8.5",
            "theorems": [],
            "problemSet": "Problem Set 8"
          }
        ]
      },
      {
        "number": "9",
        "name": "Social Health",
        "topics": [
          {
            "number": "9.1",
            "name": "Factors Affecting Social Health & Mental Stress",
            "topicCode": "MH-10-SCIT2-9-9.1",
            "subtopics": [
              "Physical, mental, economic and social relationship stability",
              "Mental stress causes: academic competition, nuclear families, loneliness, peer pressure"
            ],
            "practiceSet": "Exercise 9.1",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.2",
            "name": "Addictions, Alcoholism & Tobacco Hazards",
            "topicCode": "MH-10-SCIT2-9-9.2",
            "subtopics": [
              "Addiction to alcohol, tobacco, gutkha, drugs (narcotics)",
              "Carcinogenic oral cancer risks, cirrhosis of liver, nervous system depression"
            ],
            "practiceSet": "Exercise 9.2",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.3",
            "name": "Cyber Crimes & Incurable Media / Smartphone Addiction",
            "topicCode": "MH-10-SCIT2-9-9.3",
            "subtopics": [
              "Internet gaming disorder (Nomophobia)",
              "Cyber security crimes: hacking, online financial fraud, cyberbullying, phishing",
              "IT Act 2000 provisions"
            ],
            "practiceSet": "Exercise 9.3",
            "theorems": [],
            "problemSet": "Problem Set 9"
          },
          {
            "number": "9.4",
            "name": "Stress Management Techniques & Counseling Organisations",
            "topicCode": "MH-10-SCIT2-9-9.4",
            "subtopics": [
              "Laughter clubs, physical exercise, yoga, meditation, music and sports hobbies",
              "Salam Bombay Foundation (tobacco-free schools), Childline helpline (1098), Govt psychiatric counseling hotlines"
            ],
            "practiceSet": "Exercise 9.4",
            "theorems": [],
            "problemSet": "Problem Set 9"
          }
        ]
      },
      {
        "number": "10",
        "name": "Disaster Management",
        "topics": [
          {
            "number": "10.1",
            "name": "Disaster: Types (Geophysical, Biological, Man-Made) & Scope",
            "topicCode": "MH-10-SCIT2-10-10.1",
            "subtopics": [
              "Geophysical (Earthquake, tsunami, landslide, volcanic eruption)",
              "Biological (Epidemics, locust swarms, viral pandemics)",
              "Man-made (Industrial chemical leaks, nuclear radiation, terrorism, war)"
            ],
            "practiceSet": "Exercise 10.1",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.2",
            "name": "Disaster Management Authority Structure (NDMA, SDMA, DDMA)",
            "topicCode": "MH-10-SCIT2-10-10.2",
            "subtopics": [
              "National Disaster Management Authority (Prime Minister)",
              "State Disaster Management Authority (Chief Minister)",
              "District Disaster Management Authority (District Collector)",
              "National Disaster Response Force (NDRF) quick deployment battalions"
            ],
            "practiceSet": "Exercise 10.2",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.3",
            "name": "Disaster Management Cycle: Pre-Disaster & Post-Disaster Planning",
            "topicCode": "MH-10-SCIT2-10-10.3",
            "subtopics": [
              "Pre-disaster: Risk assessment, early warning systems, preventive preparedness, mock drills",
              "Post-disaster: Emergency rescue, relief distribution, rehabilitation, reconstruction"
            ],
            "practiceSet": "Exercise 10.3",
            "theorems": [],
            "problemSet": "Problem Set 10"
          },
          {
            "number": "10.4",
            "name": "First Aid, Rescue Techniques & Mock Drills",
            "topicCode": "MH-10-SCIT2-10-10.4",
            "subtopics": [
              "Bleeding control, burn wound dressing, fractures splint immobilization",
              "CPR (Cardio-Pulmonary Resuscitation)",
              "School and community mock drills evaluating emergency response time"
            ],
            "practiceSet": "Exercise 10.4",
            "theorems": [],
            "problemSet": "Problem Set 10"
          }
        ]
      }
    ]
  }
];
