const { createTopic } = require('./helper');

const mh9Subjects = [
  // 1. MH Class 9 Mathematics Part 1 - Algebra (MTH1)
  {
    docId: 'mh_9_mth1',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '9',
    subject: 'Mathematics Part - 1 (Algebra)',
    subjectCode: 'MTH1',
    chapters: [
      {
        number: '1',
        name: 'Sets',
        topics: [
          createTopic('MH', '9', 'MTH1', '1', '1', 'Sets: Definition, Elements & Methods of Writing (Listing & Rule Form)', ['Well-defined collection of objects', 'Roster / Listing method', 'Set-builder / Rule method']),
          createTopic('MH', '9', 'MTH1', '1', '2', 'Types of Sets: Singleton, Empty, Finite & Infinite Sets', ['Singleton set (one element)', 'Null / Empty set (∅ or {})', 'Finite set (countable elements)', 'Infinite set (N, W, I, Q, R)']),
          createTopic('MH', '9', 'MTH1', '1', '3', 'Equal Sets, Subsets & Universal Set', ['Equal sets condition (same elements)', 'Subset definition (A ⊆ B)', 'Universal set (U) and Complement of a set (A\')']),
          createTopic('MH', '9', 'MTH1', '1', '4', 'Venn Diagrams & Operations on Sets (Union & Intersection)', ['John Venn diagram representations', 'Intersection of sets (A ∩ B)', 'Disjoint sets', 'Union of sets (A ∪ B)']),
          createTopic('MH', '9', 'MTH1', '1', '5', 'Number of Elements in Set Formula: n(A ∪ B) = n(A) + n(B) - n(A ∩ B)', ['Cardinality of sets', 'Word problems on languages spoken, newspaper readers, sports participants'])
        ]
      },
      {
        number: '2',
        name: 'Real Numbers',
        topics: [
          createTopic('MH', '9', 'MTH1', '2', '1', 'Properties of Rational Numbers & Decimal Representation', ['p/q form where q != 0', 'Terminating vs non-terminating recurring forms', 'Order relation properties (Trichotomy law)']),
          createTopic('MH', '9', 'MTH1', '2', '2', 'Irrational Numbers: Geometric Proof of Irrationality of √2', ['Proof by contradiction', 'Representation of √5, √10 on number line']),
          createTopic('MH', '9', 'MTH1', '2', '3', 'Surds: Definition, Order, Like/Unlike Surds & Simplest Form', ['Definition of surd ⁿ√a', 'Order of surd (n)', 'Like / similar surds', 'Simplest radical form']),
          createTopic('MH', '9', 'MTH1', '2', '4', 'Operations on Surds & Comparison of Surds', ['Addition, subtraction, multiplication, division of surds', 'Comparing pure and mixed surds']),
          createTopic('MH', '9', 'MTH1', '2', '5', 'Rationalisation of Surds & Conjugate Pairs', ['Rationalising factor definition', 'Conjugate pair of binomial surd (√a + √b)(√a - √b)']),
          createTopic('MH', '9', 'MTH1', '2', '6', 'Absolute Value / Modulus of Real Numbers', ['Definition |x|', 'Solving modulus equations |x - a| = b'])
        ]
      },
      {
        number: '3',
        name: 'Polynomials',
        topics: [
          createTopic('MH', '9', 'MTH1', '3', '1', 'Introduction: Degree of Polynomials & Forms', ['Degree in one and more variables', 'Standard form, Index form, and Coefficient form']),
          createTopic('MH', '9', 'MTH1', '3', '2', 'Operations on Polynomials: Addition, Subtraction, Multiplication', ['Degree of sum, difference and product polynomials']),
          createTopic('MH', '9', 'MTH1', '3', '3', 'Division of Polynomials: Synthetic Division & Linear Method', ['Synthetic division algorithm using opposite coefficients', 'Linear division method']),
          createTopic('MH', '9', 'MTH1', '3', '4', 'Value of Polynomial, Remainder Theorem & Factor Theorem', ['Evaluating p(x) for x = a', 'Remainder theorem statement & verification', 'Factor theorem for checking factorability'], '', ['Remainder Theorem', 'Factor Theorem']),
          createTopic('MH', '9', 'MTH1', '3', '5', 'Factorisation of Polynomials (Middle Term Splitting & Substitution)', ['Factoring quadratic expressions (x² - x)² - 8(x² - x) + 12', 'Factoring cubic polynomials'])
        ]
      },
      {
        number: '4',
        name: 'Ratio and Proportion',
        topics: [
          createTopic('MH', '9', 'MTH1', '4', '1', 'Ratio Concepts & Properties of Ratio (a:b)', ['Units consistency', 'Order of terms', 'Multiplying/dividing terms by non-zero scalar']),
          createTopic('MH', '9', 'MTH1', '4', '2', 'Direct & Inverse Proportion Word Problems', ['Applications in work, rate, and geometry']),
          createTopic('MH', '9', 'MTH1', '4', '3', 'Properties of Equal Ratios (Invertendo, Alternendo, Componendo, Dividendo)', ['Invertendo: a/b = c/d => b/a = d/c', 'Alternendo: a/b = c/d => a/c = b/d', 'Componendo: (a+b)/b = (c+d)/d', 'Dividendo: (a-b)/b = (c-d)/d', 'Componendo-Dividendo: (a+b)/(a-b) = (c+d)/(c-d)']),
          createTopic('MH', '9', 'MTH1', '4', '4', 'Theorem on Equal Ratios & Continued Proportion', ['Theorem: a/b = c/d = (a+c)/(b+d)', 'Continued proportion a/b = b/c = c/d', 'Geometric mean formula b² = ac', 'k-method of proof'])
        ]
      },
      {
        number: '5',
        name: 'Linear Equations in Two Variables',
        topics: [
          createTopic('MH', '9', 'MTH1', '5', '1', 'Simultaneous Linear Equations & Elimination Method', ['Standard form ax + by = c', 'Eliminating variable by equating coefficients']),
          createTopic('MH', '9', 'MTH1', '5', '2', 'Substitution Method for Simultaneous Equations', ['Expressing one variable in terms of other and substituting']),
          createTopic('MH', '9', 'MTH1', '5', '3', 'Word Problems on Ages, Numbers, Speed-Distance & Fractions', ['Two-digit reversal problems', 'Numerator and denominator modifications', 'Speed and time variations'])
        ]
      },
      {
        number: '6',
        name: 'Financial Planning',
        topics: [
          createTopic('MH', '9', 'MTH1', '6', '1', 'Savings & Investments: Bank, Shares, Mutual Funds, Insurance', ['Importance of savings', 'Fixed deposit, recurring deposit, PPF, mutual funds (SIP), Life and Health insurance']),
          createTopic('MH', '9', 'MTH1', '6', '2', 'Income Tax Basics: PAN Card, Financial Year & Assessment Year', ['Direct tax vs Indirect tax', 'Permanent Account Number (PAN)', 'Financial Year (FY: 1 Apr - 31 Mar) vs Assessment Year (AY)']),
          createTopic('MH', '9', 'MTH1', '6', '3', 'Income Tax Computation, Tax Slabs & Deductions (80C, 80D)', ['Taxable income calculation', 'Deductions under section 80C up to 1.5 Lakh', 'Tax slabs for general citizens, senior citizens, and super senior citizens'])
        ]
      },
      {
        number: '7',
        name: 'Statistics',
        topics: [
          createTopic('MH', '9', 'MTH1', '7', '1', 'Primary vs Secondary Data & Grouped/Ungrouped Frequency Tables', ['Data collection methods', 'Class intervals: Inclusive (discrete) vs Exclusive (continuous) method', 'Class mark = (Lower limit + Upper limit)/2']),
          createTopic('MH', '9', 'MTH1', '7', '2', 'Cumulative Frequency Distribution (Less Than & More Than Types)', ['Running cumulative sum', 'Frequency interpretation']),
          createTopic('MH', '9', 'MTH1', '7', '3', 'Measures of Central Tendency: Mean, Median and Mode of Ungrouped Data', ['Mean: X̄ = Σx / N and Σ(f*x) / N', 'Median: Middle value of sorted array (N odd/even)', 'Mode: Most frequently occurring value'])
        ]
      }
    ]
  },

  // 2. MH Class 9 Mathematics Part 2 - Geometry (MTH2)
  {
    docId: 'mh_9_mth2',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '9',
    subject: 'Mathematics Part - 2 (Geometry)',
    subjectCode: 'MTH2',
    chapters: [
      {
        number: '1',
        name: 'Basic Concepts in Geometry',
        topics: [
          createTopic('MH', '9', 'MTH2', '1', '1', 'Coordinates of Points & Distance on Number Line (d(A, B))', ['Coordinates on number line', 'Distance formula: d(A, B) = Greater coordinate - Smaller coordinate']),
          createTopic('MH', '9', 'MTH2', '1', '2', 'Betweenness of Points (A-B-C) & Collinear Points', ['Condition: d(A, B) + d(B, C) = d(A, C)', 'Collinear vs non-collinear test']),
          createTopic('MH', '9', 'MTH2', '1', '3', 'Line Segment, Ray, Congruence of Segments & Midpoint', ['Segment definition and length', 'Opposite rays', 'Midpoint: AM = MB = 1/2 AB']),
          createTopic('MH', '9', 'MTH2', '1', '4', 'Conditional Statements, Converse, Postulates & Proofs', ['Antecedent (If part) vs Consequent (Then part)', 'Converse formulation', 'Direct and indirect proof methods'])
        ]
      },
      {
        number: '2',
        name: 'Parallel Lines',
        topics: [
          createTopic('MH', '9', 'MTH2', '2', '1', 'Properties of Parallel Lines & Interior Angles Theorem', ['Sum of interior angles on same side of transversal is 180° theorem', 'Indirect proof method'], '', ['Interior Angles Theorem']),
          createTopic('MH', '9', 'MTH2', '2', '2', 'Corresponding Angles & Alternate Angles Theorems', ['Alternate angles theorem proof', 'Corresponding angles theorem proof'], '', ['Alternate Angles Theorem', 'Corresponding Angles Theorem']),
          createTopic('MH', '9', 'MTH2', '2', '3', 'Tests for Parallel Lines (Interior, Alternate, Corresponding Angle Tests)', ['Proving two lines parallel using angle criteria'], '', ['Parallel Lines Tests']),
          createTopic('MH', '9', 'MTH2', '2', '4', 'Use of Properties of Parallel Lines (Triangle Angle Sum = 180°)', ['Theorem: Sum of all three angles of a triangle is 180°', 'Exterior angle theorem applications'], '', ['Angle Sum Property Theorem'])
        ]
      },
      {
        number: '3',
        name: 'Triangles',
        topics: [
          createTopic('MH', '9', 'MTH2', '3', '1', 'Theorem of Remote Interior Angles of a Triangle', ['Measure of exterior angle = sum of its remote interior angles'], '', ['Remote Interior Angles Theorem']),
          createTopic('MH', '9', 'MTH2', '3', '2', 'Congruence of Triangles Tests (SAS, ASA, SSS, Hypotenuse-Side)', ['Rigorous two-column geometric proofs', 'Corresponding angles/sides of congruent triangles (c.a.c.t. & c.s.c.t.)']),
          createTopic('MH', '9', 'MTH2', '3', '3', 'Isosceles Triangle Theorem & 30°-60°-90° / 45°-45°-90° Theorems', ['Isosceles triangle theorem and converse', '30°-60°-90° theorem: Side opposite 30° is 1/2 hyp, opposite 60° is √3/2 hyp', '45°-45°-90° theorem: Perpendicular sides are 1/√2 hyp'], '', ['Isosceles Triangle Theorem', '30-60-90 Triangle Theorem', '45-45-90 Triangle Theorem']),
          createTopic('MH', '9', 'MTH2', '3', '4', 'Median of Right Angled Triangle & Perpendicular Bisector Theorem', ['Length of median to hypotenuse = 1/2 hypotenuse', 'Perpendicular bisector theorem: Every point on perpendicular bisector is equidistant from endpoints'], '', ['Median to Hypotenuse Theorem', 'Perpendicular Bisector Theorem']),
          createTopic('MH', '9', 'MTH2', '3', '5', 'Angle Bisector Theorem & Similar Triangles', ['Every point on angle bisector is equidistant from arms of angle', 'Similar triangles: ratio of corresponding sides equal'], '', ['Angle Bisector Theorem'])
        ]
      },
      {
        number: '4',
        name: 'Constructions of Triangles',
        topics: [
          createTopic('MH', '9', 'MTH2', '4', '1', 'Constructing Triangle Given Base, Base Angle & Sum of Other Two Sides (AB + AC)', ['Compass and ruler step-by-step construction']),
          createTopic('MH', '9', 'MTH2', '4', '2', 'Constructing Triangle Given Base, Base Angle & Difference of Other Two Sides (AB - AC)', ['Case 1: AB > AC', 'Case 2: AC > AB']),
          createTopic('MH', '9', 'MTH2', '4', '3', 'Constructing Triangle Given Perimeter (AB + BC + CA) & Two Base Angles', ['Dividing baseline and drawing perpendicular bisectors'])
        ]
      },
      {
        number: '5',
        name: 'Quadrilaterals',
        topics: [
          createTopic('MH', '9', 'MTH2', '5', '1', 'Parallelogram Theorems & Tests for Parallelograms', ['Opposite sides and opposite angles theorem', 'Diagonals bisect each other theorem', 'Tests to prove a quadrilateral is a parallelogram'], '', ['Parallelogram Theorems', 'Parallelogram Tests']),
          createTopic('MH', '9', 'MTH2', '5', '2', 'Special Parallelograms: Rectangle, Rhombus and Square Theorems', ['Diagonals of rectangle are congruent', 'Diagonals of rhombus are perpendicular bisectors', 'Diagonals of square are congruent and perpendicular bisectors'], '', ['Rectangle Diagonals Theorem', 'Rhombus Diagonals Theorem']),
          createTopic('MH', '9', 'MTH2', '5', '3', 'Trapezium & Midpoint Theorem of Triangle', ['Midpoint theorem: Segment joining midpoints of two sides is parallel to third side and half of it', 'Converse of midpoint theorem'], '', ['Midpoint Theorem of Triangle', 'Converse of Midpoint Theorem'])
        ]
      },
      {
        number: '6',
        name: 'Circle',
        topics: [
          createTopic('MH', '9', 'MTH2', '6', '1', 'Chord Properties & Distance from Centre Theorems', ['Perpendicular from centre to chord bisects chord theorem and converse', 'Congruent chords are equidistant from centre theorem and converse'], '', ['Perpendicular to Chord Theorem', 'Congruent Chords Distance Theorem']),
          createTopic('MH', '9', 'MTH2', '6', '2', 'Incircle of a Triangle Construction', ['Constructing angle bisectors of triangle', 'Incentre (I) and inradius']),
          createTopic('MH', '9', 'MTH2', '6', '3', 'Circumcircle of a Triangle Construction', ['Constructing perpendicular bisectors of sides of triangle', 'Circumcentre (C) location in acute, right, and obtuse triangles'])
        ]
      },
      {
        number: '7',
        name: 'Coordinate Geometry',
        topics: [
          createTopic('MH', '9', 'MTH2', '7', '1', 'Axes, Origin & Plotting Coordinates on Cartesian Plane', ['X-axis, Y-axis, Origin (0,0)', 'Plotting points in all four quadrants']),
          createTopic('MH', '9', 'MTH2', '7', '2', 'Equations of Lines Parallel to Axes (x = a, y = b)', ['Line parallel to Y-axis: x = c', 'Line parallel to X-axis: y = c', 'Equation of X-axis (y=0) and Y-axis (x=0)']),
          createTopic('MH', '9', 'MTH2', '7', '3', 'Graph of Linear Equations in Two Variables: ax + by + c = 0', ['Finding solutions table and plotting straight lines on graph paper'])
        ]
      },
      {
        number: '8',
        name: 'Trigonometry',
        topics: [
          createTopic('MH', '9', 'MTH2', '8', '1', 'Trigonometric Ratios: sin θ, cos θ, tan θ Definitions', ['In right angled triangle: sin θ = Opposite / Hypotenuse', 'cos θ = Adjacent / Hypotenuse', 'tan θ = Opposite / Adjacent = sin θ / cos θ']),
          createTopic('MH', '9', 'MTH2', '8', '2', 'Relations Among Trigonometric Ratios & Identity sin²θ + cos²θ = 1', ['tan θ * tan (90-θ) = 1', 'sin θ = cos (90-θ) and cos θ = sin (90-θ)', 'Fundamental identity: sin²θ + cos²θ = 1']),
          createTopic('MH', '9', 'MTH2', '8', '3', 'Trigonometric Values of Standard Angles (0°, 30°, 45°, 60°, 90°)', ['Derivation of values using geometric triangles', 'Evaluating trigonometric algebraic expressions'])
        ]
      },
      {
        number: '9',
        name: 'Surface Area and Volume',
        topics: [
          createTopic('MH', '9', 'MTH2', '9', '1', 'Surface Area and Volume of Cone', ['Slant height l = √(r² + h²)', 'Curved Surface Area = πrl', 'Total Surface Area = πr(r + l)', 'Volume = 1/3 * πr²h']),
          createTopic('MH', '9', 'MTH2', '9', '2', 'Surface Area and Volume of Sphere and Hemisphere', ['Surface Area of Sphere = 4πr²', 'Volume of Sphere = 4/3 * πr³', 'Curved Surface Area of Hemisphere = 2πr²', 'Total Surface Area of Hemisphere = 3πr²', 'Volume of Hemisphere = 2/3 * πr³'])
        ]
      }
    ]
  },

  // 3. MH Class 9 Science and Technology (SCIT)
  {
    docId: 'mh_9_scit',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '9',
    subject: 'Science and Technology',
    subjectCode: 'SCIT',
    chapters: [
      {
        number: '1',
        name: 'Laws of Motion',
        topics: [
          createTopic('MH', '9', 'SCIT', '1', '1', 'Distance, Displacement, Speed and Velocity', ['Scalar distance vs vector displacement', 'Speed = distance / time, Velocity = displacement / time', 'Uniform vs non-uniform motion along straight line']),
          createTopic('MH', '9', 'SCIT', '1', '2', 'Acceleration (Positive, Negative/Deceleration, Zero)', ['Acceleration formula a = (v - u) / t', 'SI unit m/s²']),
          createTopic('MH', '9', 'SCIT', '1', '3', 'Distance-Time and Velocity-Time Graphs', ['Interpreting slopes for velocity and acceleration', 'Area under velocity-time graph gives displacement']),
          createTopic('MH', '9', 'SCIT', '1', '4', 'Equations of Motion by Graphical Method (v=u+at, s=ut+1/2at², v²=u²+2as)', ['Derivation of first, second, and third kinematic equations'], '', ['Kinematic Equations of Motion']),
          createTopic('MH', '9', 'SCIT', '1', '5', 'Uniform Circular Motion & Centripetal Force', ['v = 2πr / t', 'Centripetal force towards center formula F = mv²/r']),
          createTopic('MH', '9', 'SCIT', '1', '6', 'Newton Three Laws of Motion & Law of Conservation of Momentum', ['First law (Inertia)', 'Second law (F = ma)', 'Third law (Action and Reaction)', 'Conservation of momentum (m1u1 + m2u2 = m1v1 + m2v2)', 'Recoil of gun'], '', ['Newton Laws of Motion', 'Law of Conservation of Momentum'])
        ]
      },
      {
        number: '2',
        name: 'Work and Energy',
        topics: [
          createTopic('MH', '9', 'SCIT', '2', '1', 'Work: Positive, Negative and Zero Work (W = F * s * cosθ)', ['Definition of work, Joule and Erg (1 J = 10^7 erg)', 'Direction of force and displacement']),
          createTopic('MH', '9', 'SCIT', '2', '2', 'Energy & Kinetic Energy Derivation (KE = 1/2 * m * v²)', ['Definition of energy', 'Derivation using Newton second law and work formula']),
          createTopic('MH', '9', 'SCIT', '2', '3', 'Potential Energy Formula (PE = mgh)', ['Stored energy due to state or position']),
          createTopic('MH', '9', 'SCIT', '2', '4', 'Law of Conservation of Energy & Free Fall Proof', ['Transformation of energy forms', 'Proof that Total Energy = KE + PE is constant during free fall'], '', ['Law of Conservation of Energy']),
          createTopic('MH', '9', 'SCIT', '2', '5', 'Power: Rate of Doing Work & Commercial Electrical Energy', ['Power P = W / t (Watt, kW, Horsepower: 1 hp = 746 W)', '1 kWh = 3.6 * 10^6 J'])
        ]
      },
      {
        number: '3',
        name: 'Current Electricity',
        topics: [
          createTopic('MH', '9', 'SCIT', '3', '1', 'Electric Current & Potential Difference', ['Current I = Q / t (Ampere)', 'Potential difference V = W / Q (Volt)']),
          createTopic('MH', '9', 'SCIT', '3', '2', 'Ohm Law & Resistance of a Conductor', ['Statement: V = I * R (George Simon Ohm)', 'SI unit Ohm (Ω)', 'I-V characteristic graph of ohmic conductors'], '', ['Ohm Law']),
          createTopic('MH', '9', 'SCIT', '3', '3', 'Resistivity of Material (R = ρ * L / A)', ['Factors affecting resistance: length, cross-sectional area, material resistivity (ρ in Ω·m), temperature']),
          createTopic('MH', '9', 'SCIT', '3', '4', 'Resistors in Series (Rs = R1 + R2 + R3)', ['Same current through all resistors, V = V1 + V2 + V3', 'Equivalent resistance is greater than individual resistors']),
          createTopic('MH', '9', 'SCIT', '3', '5', 'Resistors in Parallel (1/Rp = 1/R1 + 1/R2 + 1/R3)', ['Same potential difference across all resistors, I = I1 + I2 + I3', 'Equivalent resistance is less than smallest resistor']),
          createTopic('MH', '9', 'SCIT', '3', '6', 'Domestic Electrical Wiring & Safety (Fuse, MCB, Earthing)', ['Live wire (brown/red), Neutral wire (blue/black), Earth wire (green/yellow)', 'Cartridge fuse and Miniature Circuit Breakers (MCB)'])
        ]
      },
      {
        number: '4',
        name: 'Measurement of Matter',
        topics: [
          createTopic('MH', '9', 'SCIT', '4', '1', 'Laws of Chemical Combination (Conservation of Mass & Constant Proportion)', ['Antoine Lavoisier and Joseph Proust laws'], '', ['Law of Conservation of Mass', 'Law of Constant Proportion']),
          createTopic('MH', '9', 'SCIT', '4', '2', 'Atom Size, Mass and Valency', ['Atomic radius in nanometres (1 nm = 10^-9 m)', 'Atomic mass unit (Dalton / u based on C-12)']),
          createTopic('MH', '9', 'SCIT', '4', '3', 'Mole Concept & Avogadro Number (N_A = 6.022 * 10²³)', ['Number of moles = Mass in grams / Molar mass', 'Avogadro number of particles in 1 mole']),
          createTopic('MH', '9', 'SCIT', '4', '4', 'Valency, Radicals (Basic vs Acidic) & Writing Chemical Formulae', ['Simple vs composite radicals', 'Cations (basic radicals) and Anions (acidic radicals)', 'Criss-cross valency method'])
        ]
      },
      {
        number: '5',
        name: 'Acids, Bases and Salts',
        topics: [
          createTopic('MH', '9', 'SCIT', '5', '1', 'Arrhenius Theory of Acids and Bases', ['Acid produces H+ (H3O+) in water', 'Base produces OH- in water', 'Strong vs weak acids and bases (degree of dissociation)']),
          createTopic('MH', '9', 'SCIT', '5', '2', 'pH Scale & Universal Indicator', ['pH range 0 to 14 (pH < 7 acidic, pH = 7 neutral, pH > 7 basic)', 'Measurement of pH using pH paper and digital pH meter']),
          createTopic('MH', '9', 'SCIT', '5', '3', 'Chemical Properties of Acids & Bases (Metals, Oxides, Carbonates)', ['Reaction with active metals -> Salt + H2 gas', 'Reaction with metal oxides -> Salt + H2O', 'Reaction with carbonates and bicarbonates -> Salt + H2O + CO2 gas']),
          createTopic('MH', '9', 'SCIT', '5', '4', 'Salts: Types, pH of Salt Solutions & Water of Crystallization', ['Neutral, acidic, basic salts', 'Water of crystallization in hydrated crystals (CuSO4·5H2O, FeSO4·7H2O, Na2CO3·10H2O, CaSO4·2H2O Plaster of Paris)']),
          createTopic('MH', '9', 'SCIT', '5', '5', 'Electrolysis of Water & Copper Sulphate Solution', ['Cathode (-ve) and Anode (+ve) reactions in electrolytic cell'])
        ]
      },
      {
        number: '6',
        name: 'Classification of Plants',
        topics: [
          createTopic('MH', '9', 'SCIT', '6', '1', 'Kingdom Plantae: Cryptogams (Non-flowering)', ['Division Thallophyta (Algae: Spirogyra, Ulva, Chara)', 'Division Bryophyta (Amphibians of plant kingdom: Moss/Funaria, Riccia, Marchantia)', 'Division Pteridophyta (Ferns: Nephrolepis, Marsilea, conducting tissues present)']),
          createTopic('MH', '9', 'SCIT', '6', '2', 'Phanerogams: Gymnosperms vs Angiosperms', ['Gymnosperms (Naked seeds, non-flowering evergreen woody e.g. Cycas, Pinus)', 'Angiosperms (Enclosed seeds within fruit, flowering)']),
          createTopic('MH', '9', 'SCIT', '6', '3', 'Angiosperms: Dicotyledonous vs Monocotyledonous Plants', ['Dicot (Two cotyledons, tap root system, reticulate venation, tetramerous/pentamerous flowers, open vascular bundles)', 'Monocot (Single cotyledon, fibrous root system, parallel venation, trimerous flowers, closed vascular bundles)'])
        ]
      },
      {
        number: '7',
        name: 'Energy Flow in an Ecosystem',
        topics: [
          createTopic('MH', '9', 'SCIT', '7', '1', 'Food Chain, Food Web & Trophic Levels', ['Producers, Primary consumers (herbivores), Secondary consumers (carnivores), Apex consumers, Decomposers']),
          createTopic('MH', '9', 'SCIT', '7', '2', 'The Energy Pyramid & Lindeman 10% Energy Rule', ['Energy decrease at successive trophic levels (Lindeman 10% law)', 'Unidirectional flow of energy in ecosystem']),
          createTopic('MH', '9', 'SCIT', '7', '3', 'Biogeochemical Cycles: Carbon Cycle, Oxygen Cycle, Nitrogen Cycle', ['Carbon cycle: Photosynthesis and respiration balance', 'Oxygen cycle: Photolysis and respiration', 'Nitrogen cycle: Nitrogen fixation, ammonification, nitrification, denitrification'])
        ]
      },
      {
        number: '8',
        name: 'Useful and Harmful Microbes',
        topics: [
          createTopic('MH', '9', 'SCIT', '8', '1', 'Useful Microbes: Lactobacilli, Rhizobium & Yeast', ['Lactobacilli in dairy fermentation and yogurt/probiotics', 'Rhizobium symbiosis in root nodules of leguminous plants for nitrogen fixation', 'Yeast (Saccharomyces cerevisiae) in bread baking and bio-ethanol fuel']),
          createTopic('MH', '9', 'SCIT', '8', '2', 'Antibiotics: Penicillin (Alexander Fleming) & Broad vs Narrow Spectrum', ['Discovery of penicillin (Penicillium notatum)', 'Broad spectrum (Amoxicillin, Tetracycline) vs Narrow spectrum antibiotics']),
          createTopic('MH', '9', 'SCIT', '8', '3', 'Harmful Microbes: Clostridium & Other Pathogens', ['Clostridium botulinum (food poisoning / botulism, anaerobic)', 'Pathogens of Dengue, Malaria, Bird Flu, Swine Flu, Hepatitis, Typhoid'])
        ]
      },
      {
        number: '9',
        name: 'Environmental Management',
        topics: [
          createTopic('MH', '9', 'SCIT', '9', '1', 'Weather, Climate & Meteorology', ['Meteorological elements, India Meteorological Department (IMD) forecasts, monsoon prediction models']),
          createTopic('MH', '9', 'SCIT', '9', '2', 'Solid Waste Management: Biodegradable vs Non-biodegradable', ['Domestic, industrial, hazardous, biomedical, e-waste', 'Principles of 7R (Rethink, Refuse, Reduce, Reuse, Recycle, Rethink, Recover)']),
          createTopic('MH', '9', 'SCIT', '9', '3', 'Scientific Waste Disposal: Composting, Vermicomposting, Incineration, Landfills', ['Segregation of dry and wet waste', 'Pyrolysis and sanitary landfilling']),
          createTopic('MH', '9', 'SCIT', '9', '4', 'Disaster Management: First Aid Principles (RICE - Rest, Ice, Compression, Elevation)', ['ABC of first aid (Airway, Breathing, Circulation)', 'Transportation methods for injured patients (cradle method, human crutch, stretcher)'])
        ]
      },
      {
        number: '10',
        name: 'Information Communication Technology (ICT)',
        topics: [
          createTopic('MH', '9', 'SCIT', '10', '1', 'Computer Hardware, Software & Generations of Computers', ['Input devices, CPU (ALU, Control Unit, Memory), Output devices', 'Operating system vs Application software']),
          createTopic('MH', '9', 'SCIT', '10', '2', 'Productivity Software: MS Word, MS Excel & MS PowerPoint', ['Formula creation in spreadsheets (SUM, AVERAGE)', 'Slide animations and presentations']),
          createTopic('MH', '9', 'SCIT', '10', '3', 'ICT in Science Education & Indian Supercomputers (PARAM)', ['Simulations, modeling, data analysis', 'C-DAC supercomputers (PARAM series by Dr. Vijay Bhatkar)'])
        ]
      },
      {
        number: '11',
        name: 'Reflection of Light',
        topics: [
          createTopic('MH', '9', 'SCIT', '11', '1', 'Mirrors: Plane Mirrors & Image Formation', ['Laws of reflection', 'Plane mirror image characteristics: virtual, erect, laterally inverted, same size, equal object-image distance']),
          createTopic('MH', '9', 'SCIT', '11', '2', 'Spherical Mirrors: Concave vs Convex Mirror Terminology', ['Pole (P), Centre of Curvature (C), Radius of Curvature (R), Principal Focus (F), Focal Length (f = R/2), Principal Axis']),
          createTopic('MH', '9', 'SCIT', '11', '3', 'Ray Diagrams for Concave Mirror at Different Object Positions', ['Object at infinity, beyond C, at C, between C and F, at F, between F and P', 'Real/inverted vs virtual/erect image nature']),
          createTopic('MH', '9', 'SCIT', '11', '4', 'Ray Diagrams for Convex Mirror & Uses', ['Diminished virtual erect image', 'Rear-view mirrors in vehicles, security surveillance']),
          createTopic('MH', '9', 'SCIT', '11', '5', 'Mirror Formula (1/f = 1/v + 1/u) & Magnification (m = -v/u)', ['Cartesian sign convention rules', 'Solving numerical ray optics problems'])
        ]
      },
      {
        number: '12',
        name: 'Study of Sound',
        topics: [
          createTopic('MH', '9', 'SCIT', '12', '1', 'Sound Waves: Velocity of Sound Formula (v = ν * λ)', ['Longitudinal wave nature: compressions and rarefactions', 'Factors affecting velocity of sound in gases: Density (v ∝ 1/√ρ), Temperature (v ∝ √T), Molecular weight (v ∝ 1/√M)']),
          createTopic('MH', '9', 'SCIT', '12', '2', 'Audible, Infrasonic and Ultrasonic Sound', ['Audible range 20 Hz to 20 kHz', 'Infrasound (<20 Hz - whales, elephants, earthquake waves)', 'Ultrasound (>20 kHz - bats, dolphins, medical SONAR)']),
          createTopic('MH', '9', 'SCIT', '12', '3', 'Reflection of Sound, Echo & Reverberation', ['Echo condition: minimum 17.2 m obstacle distance at 22°C', 'Acoustics of buildings and reverberation control']),
          createTopic('MH', '9', 'SCIT', '12', '4', 'SONAR Technique & Medical Ultrasonography', ['Transmitter and detector underwater echo sounding (2d = v * t)', 'Ultrasound scanning in obstetric and cardiac medicine']),
          createTopic('MH', '9', 'SCIT', '12', '5', 'Structure of Human Ear', ['Pinna, auditory meatus, tympanic membrane, ossicles (hammer, anvil, stirrup), cochlea with sensory hair cells'])
        ]
      },
      {
        number: '13',
        name: 'Carbon: An Important Element',
        topics: [
          createTopic('MH', '9', 'SCIT', '13', '1', 'Occurrence, Properties & Tetravalency of Carbon', ['Atomic number 6, electronic configuration (2,4), covalent bonding']),
          createTopic('MH', '9', 'SCIT', '13', '2', 'Allotropes of Carbon: Crystalline (Diamond, Graphite, Fullerenes)', ['Diamond: 3D tetrahedral network, hardest substance, non-conductor', 'Graphite: hexagonal layered structure, soft, lubricant, good electrical conductor (delocalized electrons)', 'Fullerenes: Buckyball C60 geodesic cage structure (Buckminster Fuller)']),
          createTopic('MH', '9', 'SCIT', '13', '3', 'Non-Crystalline / Amorphous Allotropes of Carbon', ['Coal (Anthracite, Bituminous, Lignite, Peat)', 'Coke, Charcoal, Lamp black / carbon black']),
          createTopic('MH', '9', 'SCIT', '13', '4', 'Hydrocarbons: Saturated (Alkanes) vs Unsaturated (Alkenes & Alkynes)', ['Methane (CH4), Ethane (C2H6)', 'Ethene (C2H4), Ethyne (C2H2)']),
          createTopic('MH', '9', 'SCIT', '13', '5', 'Carbon Dioxide (CO2) & Methane (CH4) Properties & Fire Extinguishers', ['CO2 preparation and lime water test (Ca(OH)2 + CO2 -> CaCO3 + H2O)', 'Dry ice and fire extinguisher mechanism', 'Methane marsh gas biogas production'])
        ]
      },
      {
        number: '14',
        name: 'Substances in Common Use',
        topics: [
          createTopic('MH', '9', 'SCIT', '14', '1', 'Important Salts: Common Salt (NaCl), Baking Soda (NaHCO3), Washing Soda (Na2CO3·10H2O)', ['Preparation, properties, and household/industrial uses']),
          createTopic('MH', '9', 'SCIT', '14', '2', 'Bleaching Powder (CaOCl2) & Plaster of Paris (CaSO4·1/2H2O)', ['Disinfection of drinking water with bleaching powder', 'POP casting of broken bones and statue sculpting']),
          createTopic('MH', '9', 'SCIT', '14', '3', 'Radioactive Substances & Alpha, Beta, Gamma Rays', ['Natural radioactivity (Henry Becquerel, Marie Curie)', 'Properties of α (He²⁺), β (high speed e⁻), γ (electromagnetic radiation)', 'Industrial, agricultural, medical applications (Cobalt-60, Iodine-131, Phosphorus-32) and radiation hazards']),
          createTopic('MH', '9', 'SCIT', '14', '4', 'Chemical Substances in Day-to-Day Life (Food Colors, Dyes, Artificial Sweeteners, Deodorants, Teflon, Ceramics)', ['Food adulteration dyes', 'Teflon non-stick cookware coating', 'Ceramics and porcelain bone china'])
        ]
      },
      {
        number: '15',
        name: 'Life Processes in Living Organisms',
        topics: [
          createTopic('MH', '9', 'SCIT', '15', '1', 'Transportation in Plants: Xylem (Water) & Phloem (Food Translocation)', ['Root pressure theory', 'Transpiration pull mechanism through stomata', 'Phloem transport using ATP energy']),
          createTopic('MH', '9', 'SCIT', '15', '2', 'Excretion: Excretion in Plants & Excretion in Humans', ['Plant excretion: shed leaves, resins, gums, calcium oxalate raphides', 'Human excretory system: Kidney nephron anatomy (Bowman capsule, glomerulus, renal tubule), urine formation, Dialysis artificial kidney']),
          createTopic('MH', '9', 'SCIT', '15', '3', 'Coordination in Plants (Tropic Movements & Phytohormones)', ['Phototropism, Geotropism, Hydrotropism, Thigmotropism', 'Plant hormones: Auxin, Gibberellin, Cytokinin, Abscisic acid (growth inhibitor)']),
          createTopic('MH', '9', 'SCIT', '15', '4', 'Coordination in Humans: Nervous System (CNS, PNS, ANS)', ['Brain anatomy: Cerebrum, Cerebellum, Medulla oblongata, Pons', 'Spinal cord and Reflex arc pathway']),
          createTopic('MH', '9', 'SCIT', '15', '5', 'Endocrine System in Humans & Hormones', ['Pituitary, Thyroid (Thyroxine), Parathyroid, Pancreas (Insulin/Glucagon), Adrenal (Adrenaline), Testes, Ovaries'])
        ]
      },
      {
        number: '16',
        name: 'Heredity and Variation',
        topics: [
          createTopic('MH', '9', 'SCIT', '16', '1', 'Inheritance, Chromosomes Types (Metacentric, Submetacentric, Acrocentric, Telocentric)', ['Centromere position and arms ratio', 'Homologous vs heterologous chromosomes, Autosomes vs Sex chromosomes']),
          createTopic('MH', '9', 'SCIT', '16', '2', 'DNA (Deoxyribonucleic Acid) - Watson & Crick Double Helix Model', ['Nucleotides: Deoxyribose sugar, Phosphate group, Nitrogen bases (Adenine-Thymine, Guanine-Cytosine)', 'Gene definition as functional segment of DNA', 'RNA types: mRNA, tRNA, rRNA']),
          createTopic('MH', '9', 'SCIT', '16', '3', 'Mendel Laws of Inheritance: Monohybrid Cross (3:1 Phenotype, 1:2:1 Genotype)', ['Gregor Johann Mendel experiments on Pisum sativum garden pea', 'Law of Segregation'], '', ['Law of Segregation']),
          createTopic('MH', '9', 'SCIT', '16', '4', 'Mendel Dihybrid Cross (9:3:3:1 Ratio) & Law of Independent Assortment', ['Punnett square cross of round-yellow and wrinkled-green seeds'], '', ['Law of Independent Assortment']),
          createTopic('MH', '9', 'SCIT', '16', '5', 'Genetic Disorders: Chromosomal (Down, Turner, Klinefelter) & Monogenic (Sickle Cell Anemia, Hemophilia)', ['Down syndrome (Trisomy 21 - 47 chromosomes)', 'Turner syndrome (44+XO)', 'Klinefelter syndrome (44+XXY)', 'Sickle cell anemia (HbA vs HbS genotype, red blood cell sickle deformity)'])
        ]
      },
      {
        number: '17',
        name: 'Introduction to Biotechnology',
        topics: [
          createTopic('MH', '9', 'SCIT', '17', '1', 'Tissue Culture: Technique, Nutrient Medium & Explants', ['Totipotency concept', 'Aseptic micropropagation, callogenesis, organogenesis, hardening']),
          createTopic('MH', '9', 'SCIT', '17', '2', 'Agricultural Biotechnology: GM Crops (Bt Cotton, Golden Rice) & Biofertilisers', ['Genetically Modified crops resistance against bollworm pest', 'Golden Rice with Vitamin A precursor beta-carotene', 'Biofertilisers (Azotobacter, Nostoc, Anabaena)']),
          createTopic('MH', '9', 'SCIT', '17', '3', 'Agri-tourism, Animal Husbandry & Sericulture', ['Preserving biodiversity and rural tourism', 'Cattle breeding and artificial insemination', 'Silk production from silkworm (Bombyx mori) and mulberry cultivation'])
        ]
      },
      {
        number: '18',
        name: 'Observing Space: Telescopes',
        topics: [
          createTopic('MH', '9', 'SCIT', '18', '1', 'Forms of Light & Electromagnetic Spectrum', ['Visible light (400-800 nm), Radio waves, Micro waves, Infrared, UV, X-rays, Gamma rays']),
          createTopic('MH', '9', 'SCIT', '18', '2', 'Optical Telescopes: Refracting (Galilean, Keplerian) & Reflecting (Newtonian, Cassegrain)', ['Refracting telescope using lenses and chromatic aberration defect', 'Reflecting telescope using parabolic concave mirrors (Newtonian and Cassegrain designs)']),
          createTopic('MH', '9', 'SCIT', '18', '3', 'Radio Telescopes: GMRT (Giant Metrewave Radio Telescope at Pune)', ['GMRT array of 30 parabolic dishes at Narayangaon near Pune (Prof. Govind Swarup)']),
          createTopic('MH', '9', 'SCIT', '18', '4', 'Space Telescopes: Hubble Space Telescope & Chandra X-ray Observatory', ['Atmospheric absorption and distortion avoidance', 'Hubble visual telescope and Chandra X-ray space observatory (Subrahmanyan Chandrasekhar)'])
        ]
      }
    ]
  }
];

module.exports = { mh9Subjects };
