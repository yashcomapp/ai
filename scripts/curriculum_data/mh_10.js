const { createTopic } = require('./helper');

const mh10Subjects = [
  // 1. MH Class 10 Mathematics Part 1 - Algebra (MTH1)
  {
    docId: 'mh_10_mth1',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '10',
    subject: 'Mathematics Part - 1 (Algebra)',
    subjectCode: 'MTH1',
    chapters: [
      {
        number: '1',
        name: 'Linear Equations in Two Variables',
        topics: [
          createTopic('MH', '10', 'MTH1', '1', '1', 'Simultaneous Linear Equations & Elimination/Substitution Methods', ['Standard form ax + by = c', 'Equating coefficients method', 'Substitution method for simultaneous equations']),
          createTopic('MH', '10', 'MTH1', '1', '2', 'Graphical Method of Solving Linear Equations', ['Table of values construction', 'Plotting straight lines and finding intersection point (x, y)']),
          createTopic('MH', '10', 'MTH1', '1', '3', 'Determinant & Cramer Rule (Determinant Method)', ['Value of 2x2 determinant |a b; c d| = ad - bc', 'Cramer Rule formulas: D, Dx, Dy and x = Dx/D, y = Dy/D']),
          createTopic('MH', '10', 'MTH1', '1', '4', 'Equations Reducible to a Pair of Linear Equations in Two Variables', ['Substitutions for variable denominators (e.g. 1/(x-y) = m, 1/(x+y) = n)']),
          createTopic('MH', '10', 'MTH1', '1', '5', 'Applied Word Problems (Numbers, Age, Speed-Distance, Boat & Stream)', ['Two-digit number reverse equations', 'Upstream and downstream river speed problems', 'Fixed charge and variable cost problems'])
        ]
      },
      {
        number: '2',
        name: 'Quadratic Equations',
        topics: [
          createTopic('MH', '10', 'MTH1', '2', '1', 'Quadratic Equation Definition, Standard Form & Roots', ['Standard form: ax² + bx + c = 0 (a != 0)', 'Deciding whether given values are roots/solutions of equation']),
          createTopic('MH', '10', 'MTH1', '2', '2', 'Solving Quadratic Equations by Factorisation Method', ['Splitting middle term and finding linear factors']),
          createTopic('MH', '10', 'MTH1', '2', '3', 'Solving Quadratic Equations by Completing the Square Method', ['Third term formula: [1/2 * (coefficient of x)]²', 'Transforming to perfect square trinomial (x + k)² = d']),
          createTopic('MH', '10', 'MTH1', '2', '4', 'Solving Quadratic Equations by Formula Method (Shreedharacharya)', ['Formula: x = [-b ± √(b² - 4ac)] / (2a)']),
          createTopic('MH', '10', 'MTH1', '2', '5', 'Nature of Roots & Discriminant (Δ = b² - 4ac)', ['Δ > 0: Real and unequal roots', 'Δ = 0: Real and equal roots', 'Δ < 0: Not real roots', 'Finding unknown k for equal roots']),
          createTopic('MH', '10', 'MTH1', '2', '6', 'Relation Between Roots and Coefficients (α + β, α * β)', ['α + β = -b/a and α * β = c/a', 'Obtaining quadratic equation from given roots: x² - (α+β)x + αβ = 0', 'Evaluating symmetric functions: α² + β², α³ + β³']),
          createTopic('MH', '10', 'MTH1', '2', '7', 'Applied Word Problems on Quadratic Equations', ['Speed-time-distance problems', 'Area and perimeter geometric dimensions', 'Consecutive natural/even/odd integer problems'])
        ]
      },
      {
        number: '3',
        name: 'Arithmetic Progression',
        topics: [
          createTopic('MH', '10', 'MTH1', '3', '1', 'Sequence & Arithmetic Progression (AP) Concept', ['Common difference d = t_(n) - t_(n-1)', 'Identifying whether given sequence is an AP']),
          createTopic('MH', '10', 'MTH1', '3', '2', 'nth Term of an AP Formula: t_n = a + (n - 1)d', ['Finding specific term values, total number of terms n', 'Three consecutive terms (a-d, a, a+d) and four terms (a-3d, a-d, a+d, a+3d)']),
          createTopic('MH', '10', 'MTH1', '3', '3', 'Sum of First n Terms of an AP: S_n = n/2 [2a + (n - 1)d]', ['Sum formula with last term: S_n = n/2 [t1 + tn]', 'Finding sum of even/odd natural numbers']),
          createTopic('MH', '10', 'MTH1', '3', '4', 'Applied Word Problems on AP', ['Savings schemes, loan repayments with decreasing monthly interest, auditorium seating rows'])
        ]
      },
      {
        number: '4',
        name: 'Financial Planning',
        topics: [
          createTopic('MH', '10', 'MTH1', '4', '1', 'Goods and Services Tax (GST), CGST and SGST Structure', ['GSTIN identification number (15 digits)', 'CGST (Central GST) and SGST (State GST) equality: CGST = SGST = 1/2 * GST Rate', 'Tax invoice layout: HSN code, SAC code, taxable value']),
          createTopic('MH', '10', 'MTH1', '4', '2', 'Input Tax Credit (ITC) & GST Payable in Business Chain', ['GST Payable = Output Tax - Input Tax Credit (ITC)', 'Manufacturer -> Wholesaler -> Retailer -> Consumer tax flow']),
          createTopic('MH', '10', 'MTH1', '4', '3', 'Shares: Face Value (FV), Market Value (MV), Dividend & Brokerage', ['At par (MV = FV), At premium (MV > FV), At discount (MV < FV)', 'Dividend calculated strictly on Face Value', 'Brokerage and GST on brokerage calculations']),
          createTopic('MH', '10', 'MTH1', '4', '4', 'Mutual Funds, Systematic Investment Plan (SIP) & NAV', ['Net Asset Value (NAV)', 'Return on Investment (ROI) calculation'])
        ]
      },
      {
        number: '5',
        name: 'Probability',
        topics: [
          createTopic('MH', '10', 'MTH1', '5', '1', 'Random Experiment, Outcome & Sample Space (S)', ['Sample space S and number of sample points n(S)', 'Sample spaces for tossing 1, 2, 3 coins', 'Sample spaces for throwing 1 and 2 dice (n(S) = 36)']),
          createTopic('MH', '10', 'MTH1', '5', '2', 'Types of Events: Certain, Impossible, Complementary Events', ['Subset event sets A, B, C and counting sample points n(A)']),
          createTopic('MH', '10', 'MTH1', '5', '3', 'Probability of an Event Formula: P(A) = n(A) / n(S)', ['Probability range: 0 <= P(A) <= 1 or 0% to 100%', 'Card deck problems (52 playing cards - 26 Red, 26 Black, 12 Face cards, 4 Aces)', 'Digit cards and committee formation problems'])
        ]
      },
      {
        number: '6',
        name: 'Statistics',
        topics: [
          createTopic('MH', '10', 'MTH1', '6', '1', 'Mean of Grouped Frequency Distribution: Direct Method', ['Class marks x_i and formula: X̄ = Σ(f_i * x_i) / N']),
          createTopic('MH', '10', 'MTH1', '6', '2', 'Mean by Assumed Mean Method & Step Deviation Method', ['Assumed mean (A), deviations d_i = x_i - A, formula: X̄ = A + d̄', 'Step deviation u_i = (x_i - A) / g, formula: X̄ = A + ū * g']),
          createTopic('MH', '10', 'MTH1', '6', '3', 'Median of Grouped Frequency Distribution Formula', ['Median = L + [(N/2 - cf) / f] * h', 'Continuous class intervals requirement']),
          createTopic('MH', '10', 'MTH1', '6', '4', 'Mode of Grouped Frequency Distribution Formula', ['Mode = L + [(f1 - f0) / (2f1 - f0 - f2)] * h', 'Modal class identification']),
          createTopic('MH', '10', 'MTH1', '6', '5', 'Histogram and Frequency Polygon Construction', ['Continuous classes on X-axis, frequency on Y-axis', 'Polygon joining midpoints of histogram tops']),
          createTopic('MH', '10', 'MTH1', '6', '6', 'Pie Diagram: Drawing & Interpreting Central Angles (θ)', ['Central angle formula: θ = (Value of component / Total value) * 360°', 'Protractor circle subdivision and sector interpretation'])
        ]
      }
    ]
  },

  // 2. MH Class 10 Mathematics Part 2 - Geometry (MTH2)
  {
    docId: 'mh_10_mth2',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '10',
    subject: 'Mathematics Part - 2 (Geometry)',
    subjectCode: 'MTH2',
    chapters: [
      {
        number: '1',
        name: 'Similarity',
        topics: [
          createTopic('MH', '10', 'MTH2', '1', '1', 'Ratio of Areas of Two Triangles (Base & Height Properties)', ['Ratio of areas = (b1 * h1) / (b2 * h2)', 'Triangles with equal heights: A1/A2 = b1/b2', 'Triangles with equal bases: A1/A2 = h1/h2', 'Triangles with equal bases and equal heights: A1 = A2']),
          createTopic('MH', '10', 'MTH2', '1', '2', 'Basic Proportionality Theorem (BPT) & Its Converse', ['Statement and geometric proof: Line parallel to side dividing remaining two sides in equal ratio', 'Converse of Basic Proportionality Theorem'], '', ['Basic Proportionality Theorem', 'Converse of BPT']),
          createTopic('MH', '10', 'MTH2', '1', '3', 'Property of Angle Bisector of a Triangle & Property of Three Parallel Lines', ['Angle bisector theorem: BD/DC = AB/AC and converse', 'Intercept theorem for three parallel lines: AB/BC = XY/YZ'], '', ['Angle Bisector Theorem', 'Three Parallel Lines Intercept Theorem']),
          createTopic('MH', '10', 'MTH2', '1', '4', 'Tests of Similarity of Triangles (AAA, AA, SAS, SSS)', ['Tests to prove triangles similar', 'Corresponding sides in proportion and corresponding angles congruent']),
          createTopic('MH', '10', 'MTH2', '1', '5', 'Theorem of Areas of Similar Triangles', ['Statement and proof: Ratio of areas of two similar triangles = square of ratio of corresponding sides (A1/A2 = s1²/s2² = h1²/h2² = m1²/m2²)'], '', ['Theorem of Areas of Similar Triangles'])
        ]
      },
      {
        number: '2',
        name: 'Pythagoras Theorem',
        topics: [
          createTopic('MH', '10', 'MTH2', '2', '1', 'Similarity of Right Angled Triangles & Theorem of Geometric Mean', ['Altitude to hypotenuse divides triangle into two triangles similar to original and to each other', 'Theorem of Geometric Mean: CD² = AD * DB'], '', ['Similarity and Right Angled Triangle Theorem', 'Theorem of Geometric Mean']),
          createTopic('MH', '10', 'MTH2', '2', '2', 'Pythagoras Theorem & Its Converse', ['Statement and geometric proof: In right triangle, Hypotenuse² = Base² + Height²', 'Converse of Pythagoras theorem', 'Pythagorean triplets identification (e.g. 3,4,5; 5,12,13; 8,15,17)'], '', ['Pythagoras Theorem', 'Converse of Pythagoras Theorem']),
          createTopic('MH', '10', 'MTH2', '2', '3', 'Application of Pythagoras Theorem in Acute & Obtuse Triangles', ['Obtuse angled triangle: AC² = AB² + BC² + 2 * BC * BD', 'Acute angled triangle: AC² = AB² + BC² - 2 * BC * BD']),
          createTopic('MH', '10', 'MTH2', '2', '4', 'Apollonius Theorem on Medians of Triangle', ['Statement and proof: In triangle ABC with median AM on BC, AB² + AC² = 2(AM² + BM²)', 'Calculating lengths of medians in triangles and diagonals of parallelograms'], '', ['Apollonius Theorem'])
        ]
      },
      {
        number: '3',
        name: 'Circle',
        topics: [
          createTopic('MH', '10', 'MTH2', '3', '1', 'Circles Passing Through 1, 2, and 3 Non-Collinear Points', ['Infinite circles through 1 and 2 points', 'Unique circle passing through 3 non-collinear points; No circle through 3 collinear points']),
          createTopic('MH', '10', 'MTH2', '3', '2', 'Tangent Theorem & Converse (Tangent Perpendicular to Radius)', ['Tangent theorem statement and proof: Tangent at point on circle is perpendicular to radius', 'Converse of tangent theorem'], '', ['Tangent Theorem', 'Converse of Tangent Theorem']),
          createTopic('MH', '10', 'MTH2', '3', '3', 'Tangent Segment Theorem (Tangents from External Point are Congruent)', ['Statement and proof: Tangent segments from external point are congruent (AP = BP)'], '', ['Tangent Segment Theorem']),
          createTopic('MH', '10', 'MTH2', '3', '4', 'Touching Circles Theorem (Externally & Internally Touching)', ['Theorem: Point of contact of touching circles lies on line joining their centres', 'Distance between centres: d = r1 + r2 (externally) and d = |r1 - r2| (internally)'], '', ['Theorem of Touching Circles']),
          createTopic('MH', '10', 'MTH2', '3', '5', 'Arc of a Circle, Central Angle & Measure of Arc', ['Minor arc, major arc, semicircular arc', 'Measure of minor arc = measure of central angle', 'Measure of circle = 360°']),
          createTopic('MH', '10', 'MTH2', '3', '6', 'Inscribed Angle Theorem & Corollary (Angles in Same Segment)', ['Statement and proof: Inscribed angle = 1/2 * intercepted arc', 'Angles in same segment are congruent', 'Angle in a semicircle is a right angle'], '', ['Inscribed Angle Theorem', 'Angle in Semicircle Theorem']),
          createTopic('MH', '10', 'MTH2', '3', '7', 'Cyclic Quadrilateral Theorem & Its Converse', ['Statement and proof: Opposite angles of cyclic quadrilateral are supplementary (sum = 180°)', 'Corollary: Exterior angle of cyclic quadrilateral = interior opposite angle', 'Converse of cyclic quadrilateral theorem'], '', ['Cyclic Quadrilateral Theorem', 'Converse of Cyclic Quadrilateral Theorem']),
          createTopic('MH', '10', 'MTH2', '3', '8', 'Theorem of Angle Between Tangent and Secant & Tangent Secant Segment Theorem', ['Tangent-Secant angle theorem: Angle = 1/2 * intercepted arc', 'Tangent Secant Segment Theorem: PT² = PA * PB', 'Theorem of internal and external division of chords: PA * PB = PC * PD'], '', ['Tangent Secant Theorem', 'Internal Division of Chords Theorem'])
        ]
      },
      {
        number: '4',
        name: 'Geometric Constructions',
        topics: [
          createTopic('MH', '10', 'MTH2', '4', '1', 'Construction of Similar Triangle (Having Common Vertex)', ['Step-by-step compass division and drawing parallel lines']),
          createTopic('MH', '10', 'MTH2', '4', '2', 'Construction of Similar Triangle (Having No Common Vertex)', ['Calculating dimensions using similarity ratio and constructing triangle']),
          createTopic('MH', '10', 'MTH2', '4', '3', 'Construction of Tangent to Circle at Point on Circle (Using & Without Centre)', ['Method 1: Extending radius and drawing perpendicular bisector', 'Method 2: Using inscribed angle and alternate segment chord']),
          createTopic('MH', '10', 'MTH2', '4', '4', 'Construction of Tangents to Circle from External Point', ['Drawing perpendicular bisector of OP and intersecting arcs'])
        ]
      },
      {
        number: '5',
        name: 'Coordinate Geometry',
        topics: [
          createTopic('MH', '10', 'MTH2', '5', '1', 'Distance Formula Derivation: d = √[(x2 - x1)² + (y2 - y1)²]', ['Distance of point (x, y) from origin: √(x² + y²)', 'Proving collinearity and types of quadrilaterals (Rhombus, Rectangle, Square)']),
          createTopic('MH', '10', 'MTH2', '5', '2', 'Section Formula for Internal Division: ((mx2+nx1)/(m+n), (my2+ny1)/(m+n))', ['Coordinates of point dividing line segment in ratio m:n', 'Midpoint formula: ((x1+x2)/2, (y1+y2)/2)', 'Centroid formula: G = ((x1+x2+x3)/3, (y1+y2+y3)/3)']),
          createTopic('MH', '10', 'MTH2', '5', '3', 'Slope of a Line: Formula m = tan θ and m = (y2 - y1) / (x2 - x1)', ['Slope definition with positive direction of X-axis', 'Slope of X-axis = 0, Slope of Y-axis is undefined', 'Parallel lines have equal slopes (m1 = m2)', 'Collinear points slope condition'])
        ]
      },
      {
        number: '6',
        name: 'Trigonometry',
        topics: [
          createTopic('MH', '10', 'MTH2', '6', '1', 'Trigonometric Ratios & Fundamental Identities', ['sin θ, cos θ, tan θ, cot θ, sec θ, cosec θ definitions', 'Identities: sin²θ + cos²θ = 1; 1 + tan²θ = sec²θ; 1 + cot²θ = cosec²θ', 'Proving trigonometric identities']),
          createTopic('MH', '10', 'MTH2', '6', '2', 'Evaluating Trigonometric Values for Standard Angles (0°, 30°, 45°, 60°, 90°)', ['Derivation table and simplification']),
          createTopic('MH', '10', 'MTH2', '6', '3', 'Application of Trigonometry: Line of Sight, Angle of Elevation & Depression', ['Height and distance problems: Lighthouse, ships, towers, broken trees, airplanes'])
        ]
      },
      {
        number: '7',
        name: 'Mensuration',
        topics: [
          createTopic('MH', '10', 'MTH2', '7', '1', 'Surface Area and Volume of Cuboid, Cube, Cylinder, Cone', ['Total Surface Area and Volume formulas review', 'Slant height of cone: l = √(r² + h²)', 'Cone CSA = πrl, TSA = πr(r+l), Volume = 1/3 πr²h']),
          createTopic('MH', '10', 'MTH2', '7', '2', 'Surface Area and Volume of Sphere and Hemisphere', ['Sphere: Surface area = 4πr², Volume = 4/3 πr³', 'Hemisphere: CSA = 2πr², TSA = 3πr², Volume = 2/3 πr³']),
          createTopic('MH', '10', 'MTH2', '7', '3', 'Frustum of a Cone: Surface Area & Volume', ['Slant height: l = √[h² + (r1 - r2)²]', 'CSA = πl(r1 + r2), TSA = πl(r1 + r2) + πr1² + πr2²', 'Volume = 1/3 * πh(r1² + r2² + r1*r2)']),
          createTopic('MH', '10', 'MTH2', '7', '4', 'Area of Sector & Length of Arc of a Circle', ['Length of arc: l = (θ / 360) * 2πr', 'Area of sector: A = (θ / 360) * πr² = 1/2 * l * r']),
          createTopic('MH', '10', 'MTH2', '7', '5', 'Area of Segment of a Circle (Minor & Major Segment)', ['Area of segment = Area of sector - Area of triangle', 'Area of triangle = 1/2 * r² * sin θ'])
        ]
      }
    ]
  },

  // 3. MH Class 10 Science and Technology Part 1 (SCIT1)
  {
    docId: 'mh_10_scit1',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '10',
    subject: 'Science and Technology Part - 1',
    subjectCode: 'SCIT1',
    chapters: [
      {
        number: '1',
        name: 'Gravitation',
        topics: [
          createTopic('MH', '10', 'SCIT1', '1', '1', 'Gravitation & Kepler Three Laws of Planetary Motion', ['Centripetal force definition', 'Kepler 1st Law (Law of Orbits - Elliptical orbit with Sun at one focus)', 'Kepler 2nd Law (Law of Areas - Equal areas in equal intervals of time)', 'Kepler 3rd Law (Law of Periods - T² ∝ r³)'], '', ['Kepler Laws of Planetary Motion']),
          createTopic('MH', '10', 'SCIT1', '1', '2', 'Newton Universal Law of Gravitation & Inverse Square Law Deduction', ['F = G * (m1 * m2) / r²', 'Value of G = 6.67 * 10^-11 N·m²/kg²', 'Derivation of inverse square law from Kepler 3rd law'], '', ['Newton Universal Law of Gravitation']),
          createTopic('MH', '10', 'SCIT1', '1', '3', 'Acceleration Due to Gravity (g = GM/R²) & Variations in g', ['Value of g on Earth surface = 9.8 m/s²', 'Variation with altitude / height (decreases)', 'Variation with depth (decreases to 0 at centre)', 'Variation along surface: g_pole (9.83 m/s²) > g_equator (9.78 m/s²)']),
          createTopic('MH', '10', 'SCIT1', '1', '4', 'Mass vs Weight & Gravitational Potential Energy', ['Mass (kg) vs Weight W = mg (N)', 'Gravitational Potential Energy at height h: -GMm/(R+h)']),
          createTopic('MH', '10', 'SCIT1', '1', '5', 'Free Fall, Equations of Motion Under Gravity & Escape Velocity (v_esc)', ['Free fall acceleration +g and -g equations', 'Escape velocity derivation: v_esc = √(2GM/R) = √(2gR) = 11.2 km/s on Earth', 'Weightlessness in space satellite'])
        ]
      },
      {
        number: '2',
        name: 'Periodic Classification of Elements',
        topics: [
          createTopic('MH', '10', 'SCIT1', '2', '1', 'Dobereiner Triads & Newlands Law of Octaves', ['Dobereiner: Arithmetic mean atomic mass of middle element (e.g. Li, Na, K; Ca, Sr, Ba)', 'Newlands Law of Octaves: Musical notes similarity (Sa, Re, Ga, Ma, Pa, Dha, Ni) up to Calcium']),
          createTopic('MH', '10', 'SCIT1', '2', '2', 'Mendeleev Periodic Table: Principles, Merits & Limitations', ['Periodic Law: Properties of elements are periodic functions of atomic masses', 'Merits: Predicted undiscovered elements (Eka-Boron/Scandium, Eka-Aluminium/Gallium, Eka-Silicon/Germanium), Noble gas inclusion', 'Limitations: Position of Hydrogen, Isotopes anomaly, Inversion of atomic masses (Co and Ni)']),
          createTopic('MH', '10', 'SCIT1', '2', '3', 'Modern Periodic Table (Henry Moseley, 1913): Structure (Periods & Groups)', ['Modern Periodic Law: Properties of elements are periodic functions of atomic numbers (Z)', '7 Horizontal Periods and 18 Vertical Groups', 's-block, p-block, d-block (transition elements), f-block (lanthanides and actinides)']),
          createTopic('MH', '10', 'SCIT1', '2', '4', 'Periodic Trends: Valency & Atomic Size (Atomic Radius)', ['Valency: determined by valence electrons (increases 1 to 4 then decreases to 0 across period, constant in group)', 'Atomic radius: Decreases across period (effective nuclear charge increases) and Increases down group (new shells added)']),
          createTopic('MH', '10', 'SCIT1', '2', '5', 'Periodic Trends: Metallic vs Non-Metallic Character & Electronegativity', ['Metallic character (electropositivity): Decreases across period, Increases down group', 'Non-metallic character & Electronegativity: Increases across period, Decreases down group', 'Gradation in Halogen group (F2 gas, Cl2 gas, Br2 liquid, I2 solid)'])
        ]
      },
      {
        number: '3',
        name: 'Chemical Reactions and Equations',
        topics: [
          createTopic('MH', '10', 'SCIT1', '3', '1', 'Chemical Reactions: Rules for Writing & Balancing Equations', ['Reactants and Products, State symbols (s, l, g, aq)', 'Step-by-step balancing method matching atom counts on LHS and RHS']),
          createTopic('MH', '10', 'SCIT1', '3', '2', 'Types of Reactions: Combination & Decomposition Reactions', ['Combination: 2Mg + O2 -> 2MgO', 'Decomposition: Thermal (CaCO3 -> CaO + CO2), Electrolytic (2H2O -> 2H2 + O2)']),
          createTopic('MH', '10', 'SCIT1', '3', '3', 'Displacement & Double Displacement (Precipitation) Reactions', ['Displacement: CuSO4 + Fe -> FeSO4 + Cu', 'Double displacement: AgNO3 + NaCl -> AgCl (white ppt) + NaNO3']),
          createTopic('MH', '10', 'SCIT1', '3', '4', 'Endothermic vs Exothermic Reactions & Factors Affecting Reaction Rate', ['Endothermic (absorbs heat) vs Exothermic (releases heat)', 'Factors: Nature of reactants, Particle size (smaller = faster), Concentration (higher = faster), Temperature, Catalyst (MnO2 in H2O2 decomposition)']),
          createTopic('MH', '10', 'SCIT1', '3', '5', 'Oxidation, Reduction, Redox Reactions, Corrosion & Rancidity', ['Oxidation: gain of oxygen / loss of hydrogen / loss of electrons', 'Reduction: gain of hydrogen / loss of oxygen / gain of electrons', 'Redox reaction examples and reducing/oxidizing agents', 'Corrosion: Rusting formula Fe2O3·xH2O, Galvanic cell action on iron surface', 'Rancidity of edible oils and antioxidant prevention'])
        ]
      },
      {
        number: '4',
        name: 'Effects of Electric Current',
        topics: [
          createTopic('MH', '10', 'SCIT1', '4', '1', 'Energy Transfer in an Electric Circuit & Joule Law of Heating', ['Power P = V * I = I²R = V²/R', 'Heat energy H = I²Rt (Joules)'], '', ['Joule Law of Heating']),
          createTopic('MH', '10', 'SCIT1', '4', '2', 'Heating Appliances & Short Circuit / Overloading Safety', ['Heating coil of high resistivity Nichrome alloy', 'Tungsten bulb filament (melting point 3422°C)', 'Electric fuse wire (lead-tin alloy with low melting point), MCB']),
          createTopic('MH', '10', 'SCIT1', '4', '3', 'Magnetic Effect of Electric Current & Right Hand Thumb Rule', ['Hans Christian Oersted discovery', 'Right hand thumb rule / Maxwell corkscrew rule for magnetic field direction']),
          createTopic('MH', '10', 'SCIT1', '4', '4', 'Magnetic Field of Solenoid & Fleming Left Hand Rule', ['Solenoid magnetic field like bar magnet', 'Fleming Left Hand Rule (Thumb = Force, Forefinger = Magnetic Field, Middle finger = Current)']),
          createTopic('MH', '10', 'SCIT1', '4', '5', 'Electric Motor: Principle, Construction & Working', ['Armature coil in strong magnetic field', 'Split ring commutator reversing current every half turn, Carbon brushes']),
          createTopic('MH', '10', 'SCIT1', '4', '6', 'Electromagnetic Induction (Michael Faraday) & Fleming Right Hand Rule', ['Galvanometer deflection when magnet moves in coil', 'Faraday Law of Induction: Induced current is produced whenever magnetic flux changes', 'Fleming Right Hand Rule for induced current direction']),
          createTopic('MH', '10', 'SCIT1', '4', '7', 'Electric Generator (AC & DC Generator) & Domestic AC Current', ['AC generator with two slip rings (50 Hz alternating current in India, reverses every 1/100 s)', 'DC generator with split ring commutator (unidirectional current)'])
        ]
      },
      {
        number: '5',
        name: 'Heat',
        topics: [
          createTopic('MH', '10', 'SCIT1', '5', '1', 'Latent Heat: Latent Heat of Fusion & Latent Heat of Vaporization', ['Temperature stays constant during phase change', 'Specific Latent Heat of Fusion of ice (80 cal/g or 3.33 * 10^5 J/kg)', 'Specific Latent Heat of Vaporization of steam (540 cal/g or 2.26 * 10^6 J/kg)']),
          createTopic('MH', '10', 'SCIT1', '5', '2', 'Regelation of Ice & Ice Skate Working', ['Phenomenon: Ice melts under pressure and refreezes when pressure is released']),
          createTopic('MH', '10', 'SCIT1', '5', '3', 'Anomalous Behavior of Water & Hope Apparatus', ['Water contracts on heating from 0°C to 4°C (Maximum density at 4°C = 1 g/cm³)', 'Hope apparatus experiment verifying 4°C water at bottom', 'Survival of aquatic plants and animals in frozen lakes']),
          createTopic('MH', '10', 'SCIT1', '5', '4', 'Dew Point, Humidity & Relative Humidity', ['Absolute humidity (mass of water vapor in 1 m³ air)', 'Relative Humidity % = [(Actual mass of vapor) / (Mass required for saturation)] * 100', 'Dew point temperature (100% relative humidity)']),
          createTopic('MH', '10', 'SCIT1', '5', '5', 'Unit of Heat & Specific Heat Capacity (c)', ['1 Calorie = 4.184 Joules (Heat to raise 1 g water by 1°C from 14.5°C to 15.5°C)', 'Specific heat capacity: Q = m * c * ΔT', 'Iron, copper, lead spheres in paraffin wax experiment (c_iron > c_copper > c_lead)']),
          createTopic('MH', '10', 'SCIT1', '5', '6', 'Principle of Heat Exchange & Calorimeter', ['Heat lost by hot object = Heat gained by cold object (in isolated system)'])
        ]
      },
      {
        number: '6',
        name: 'Refraction of Light',
        topics: [
          createTopic('MH', '10', 'SCIT1', '6', '1', 'Refraction of Light & Laws of Refraction', ['Bending of light at boundary of two transparent media', 'Incident ray, refracted ray, normal lie in same plane', 'Snell Law: sin i / sin r = constant (n)']),
          createTopic('MH', '10', 'SCIT1', '6', '2', 'Refractive Index (Absolute & Relative Refractive Index)', ['Absolute refractive index n = c / v (Vacuum speed / Medium speed)', 'Relative refractive index 2n1 = v1 / v2 = n2 / n1', 'Optical rarer to denser medium (bends towards normal) and vice versa']),
          createTopic('MH', '10', 'SCIT1', '6', '3', 'Apparent Depth & Twinkling of Stars / Atmospheric Refraction', ['Apparent depth = Real depth / Refractive index', 'Twinkling of stars due to changing atmospheric density and refractive index', 'Planets do not twinkle (extended source)', 'Advanced sunrise and delayed sunset']),
          createTopic('MH', '10', 'SCIT1', '6', '4', 'Dispersion of Light & Rainbow Formation', ['Separation of white light into spectrum colors (VIBGYOR) through prism', 'Wavelength order: Red (700 nm) to Violet (400 nm)', 'Rainbow formation (Combined refraction, dispersion, and total internal reflection)']),
          createTopic('MH', '10', 'SCIT1', '6', '5', 'Total Internal Reflection & Critical Angle (i_c)', ['When light travels from denser to rarer medium: Critical angle is angle of incidence where angle of refraction is 90°', 'When i > i_c: Total Internal Reflection occurs', 'Optical fibers and mirage phenomenon'])
        ]
      },
      {
        number: '7',
        name: 'Lenses',
        topics: [
          createTopic('MH', '10', 'SCIT1', '7', '1', 'Convex and Concave Lenses: Centers of Curvature & Focus', ['Biconvex (converging) vs Biconcave (diverging) lenses', 'Centers of Curvature (C1, C2), Radii (R1, R2), Optical Centre (O), Principal Focus (F1, F2), Focal Length (f)']),
          createTopic('MH', '10', 'SCIT1', '7', '2', 'Rules for Drawing Ray Diagrams for Lenses', ['Ray parallel to principal axis passes through focus', 'Ray passing through focus emerges parallel', 'Ray passing through optical centre passes without deviation']),
          createTopic('MH', '10', 'SCIT1', '7', '3', 'Ray Diagrams for Images Formed by Convex & Concave Lenses', ['Convex lens 6 positions (Real/inverted images, and Virtual/erect magnified image when object between F1 and O)', 'Concave lens (Always virtual, erect, diminished image)']),
          createTopic('MH', '10', 'SCIT1', '7', '4', 'Lens Formula (1/v - 1/u = 1/f) & Magnification (M = v/u = h2/h1)', ['Cartesian sign conventions for lenses', 'Numerical problem solving for object/image distances and heights']),
          createTopic('MH', '10', 'SCIT1', '7', '5', 'Power of Lens (P = 1/f in metres) & Combination of Lenses', ['Unit Dioptre (D)', 'Convex lens power is positive, Concave lens power is negative', 'Combined power P = P1 + P2']),
          createTopic('MH', '10', 'SCIT1', '7', '6', 'Human Eye Anatomy & Defects of Vision (Myopia, Hypermetropia, Presbyopia)', ['Ciliary muscles accommodation', 'Myopia (Near sightedness - concave lens correction)', 'Hypermetropia (Far sightedness - convex lens correction)', 'Presbyopia (Bifocal lens correction)']),
          createTopic('MH', '10', 'SCIT1', '7', '7', 'Optical Instruments: Simple Microscope, Compound Microscope & Astronomical Telescope', ['Simple microscope (Magnifying glass: M = 1 + D/f)', 'Compound microscope (Objective lens of small aperture and Eyepiece of large aperture)', 'Astronomical refracting telescope (Objective of large focal length/aperture and Eyepiece of small focal length)'])
        ]
      },
      {
        number: '8',
        name: 'Metallurgy',
        topics: [
          createTopic('MH', '10', 'SCIT1', '8', '1', 'Physical & Chemical Properties of Metals and Non-Metals', ['Reactivity of metals with oxygen, water, dilute acids, and other metal salt solutions', 'Reactivity series of metals']),
          createTopic('MH', '10', 'SCIT1', '8', '2', 'Ionic Compounds: Formation, Crystal Lattice & Properties', ['Electron transfer, strong electrostatic attraction force', 'High melting points, electrical conduction in liquid/molten state']),
          createTopic('MH', '10', 'SCIT1', '8', '3', 'Basic Principles of Metallurgy & Concentration of Ores', ['Minerals, ores, gangue matrix', 'Gravity separation: Wilfley table method & Hydraulic separation', 'Magnetic separation method (e.g. tin stone and magnetic wolframite)', 'Froth floatation method (for sulphide ores using pine oil and collectors)', 'Leaching method (Extraction of Aluminium from Bauxite using NaOH / Baeyer process)']),
          createTopic('MH', '10', 'SCIT1', '8', '4', 'Extraction of Reactive Metals: Electrolytic Reduction of Alumina (Hall-Heroult Process)', ['Purification of bauxite (Hall and Baeyer processes)', 'Electrolysis of molten alumina with Cryolite (Na3AlF6) and Fluorspar (CaF2)', 'Cathode: carbon lining (molten Al), Anode: graphite rods (O2 gas)']),
          createTopic('MH', '10', 'SCIT1', '8', '5', 'Extraction of Moderately & Less Reactive Metals (Roasting & Calcination)', ['Roasting of zinc blende (2ZnS + 3O2 -> 2ZnO + 2SO2)', 'Calcination of calamine (ZnCO3 -> ZnO + CO2)', 'Reduction of ZnO using carbon coke (ZnO + C -> Zn + CO)']),
          createTopic('MH', '10', 'SCIT1', '8', '6', 'Corrosion of Metals & Prevention Methods', ['Corrosion definition and electrochemical oxidation', 'Galvanisation (thin zinc coating on iron)', 'Tinning (coating copper/brass utensils with molten tin)', 'Anodisation (forming thick protective oxide layer on aluminium)', 'Electroplating (gold/silver coating)', 'Alloying (Stainless steel, Brass, Bronze)'])
        ]
      },
      {
        number: '9',
        name: 'Carbon Compounds',
        topics: [
          createTopic('MH', '10', 'SCIT1', '9', '1', 'Bonds in Carbon Compounds & Tetravalency / Catenation Ability', ['Covalent single, double, and triple bonds', 'Catenation power: open chains, branched chains, closed ring structures', 'Isomerism: Structural isomers of butane (n-butane and isobutane)']),
          createTopic('MH', '10', 'SCIT1', '9', '2', 'Hydrocarbons: Saturated (Alkanes) vs Unsaturated (Alkenes & Alkynes)', ['Alkanes (C_n H_2n+2), Alkenes (C_n H_2n), Alkynes (C_n H_2n-2)', 'Straight chain, branched chain and cyclic hydrocarbons (Cyclohexane, Benzene C6H6)']),
          createTopic('MH', '10', 'SCIT1', '9', '3', 'Functional Groups & Homologous Series', ['Halide (-X), Alcohol (-OH), Aldehyde (-CHO), Ketone (-CO-), Carboxylic Acid (-COOH), Ether (-O-), Ester (-COO-), Amine (-NH2)', 'Homologous series characteristics (same general formula, gradation in melting/boiling points)']),
          createTopic('MH', '10', 'SCIT1', '9', '4', 'IUPAC Nomenclature of Carbon Compounds', ['Parent alkane identification, numbering carbon chain from functional group side, prefix and suffix rules']),
          createTopic('MH', '10', 'SCIT1', '9', '5', 'Chemical Properties: Combustion, Oxidation, Addition & Substitution', ['Combustion equation: CH4 + 2O2 -> CO2 + 2H2O + Heat', 'Oxidation of ethanol with alkaline KMnO4 to ethanoic acid', 'Addition reaction of ethene with H2 (catalytic hydrogenation)', 'Substitution of methane with chlorine in presence of sunlight']),
          createTopic('MH', '10', 'SCIT1', '9', '6', 'Important Carbon Compounds: Ethanol & Ethanoic Acid', ['Ethanol properties, reaction with sodium (H2 gas), dehydration with conc. H2SO4 at 170°C to ethene', 'Ethanoic acid (Glacial acetic acid melting point 17°C), esterification reaction with ethanol, saponification reaction']),
          createTopic('MH', '10', 'SCIT1', '9', '7', 'Macromolecules and Polymers (Natural & Synthetic Polymers)', ['Polymers formed by repeated monomer units (Polyethylene from ethylene)', 'Natural polymers: Polysaccharides (starch, cellulose), Proteins (amino acids), DNA/RNA, Natural rubber (isoprene)', 'Synthetic polymers: Teflon, Nylon, Polystyrene, PVC, Terylene'])
        ]
      },
      {
        number: '10',
        name: 'Space Missions',
        topics: [
          createTopic('MH', '10', 'SCIT1', '10', '1', 'Need & Importance of Space Missions', ['Telecommunication, weather broadcasting, disaster management, military surveillance, astronomy']),
          createTopic('MH', '10', 'SCIT1', '10', '2', 'Artificial Satellites: Types & Functions', ['Weather satellites (INSAT, GSAT)', 'Communication satellites', 'Broadcast satellites', 'Navigational satellites (IRNSS / NavIC)', 'Earth observation satellites (IRS)', 'Military / surveillance satellites']),
          createTopic('MH', '10', 'SCIT1', '10', '3', 'Orbits of Artificial Satellites (GEO, MEO, LEO)', ['High Earth Orbits (HEO / GEO): Height > 35,786 km, Period 24 hours (geostationary)', 'Medium Earth Orbits (MEO): Height 2,000 to 35,786 km, Period 2 to 24 hours (GPS)', 'Low Earth Orbits (LEO): Height 180 to 2,000 km, Period 90 minutes (ISS, Hubble)']),
          createTopic('MH', '10', 'SCIT1', '10', '4', 'Satellite Launch Vehicles (PSLV by ISRO) & Multi-Stage Rockets', ['Newton 3rd law and conservation of momentum principle', 'Multi-stage rocket fuel stages detachment for mass reduction']),
          createTopic('MH', '10', 'SCIT1', '10', '5', 'Space Missions Beyond Earth (Moon, Mars) & Space Debris Management', ['Chandrayaan-1 (discovery of water molecules on Moon), Chandrayaan-2 and 3', 'Mangalyaan (Mars Orbiter Mission - MOM, 2013)', 'Space debris hazards to operational satellites and space debris mitigation methods'])
        ]
      }
    ]
  },

  // 4. MH Class 10 Science and Technology Part 2 (SCIT2)
  {
    docId: 'mh_10_scit2',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '10',
    subject: 'Science and Technology Part - 2',
    subjectCode: 'SCIT2',
    chapters: [
      {
        number: '1',
        name: 'Heredity and Evolution',
        topics: [
          createTopic('MH', '10', 'SCIT2', '1', '1', 'Heredity & Molecular Protein Synthesis (Transcription, Translation, Translocation)', ['Central Dogma of molecular biology: DNA -> RNA -> Protein', 'Transcription: Synthesis of mRNA from DNA template strand using RNA polymerase (Codons & Triplet codon discoveries by Dr. Har Gobind Khorana)', 'Translation: tRNA with anticodon complementary to mRNA brings amino acids to ribosome', 'Translocation: Ribosome moves along mRNA by one triplet codon']),
          createTopic('MH', '10', 'SCIT2', '1', '2', 'Mutation: Gene Sequences Alterations & Genetic Disorders', ['Sudden changes in nucleotide sequence', 'Sickle cell anemia monogenic mutation']),
          createTopic('MH', '10', 'SCIT2', '1', '3', 'Evolution & Evidences of Evolution (Morphological, Anatomical, Vestigial Organs, Paleontological, Connecting Links, Embryological)', ['Morphological: Similarity in bone and muscle structure of mouth/nose/ears', 'Anatomical: Similar bone structure in human hand, cat foreleg, whale flipper, bat wing', 'Vestigial organs: Appendix, tailbone (coccyx), wisdom teeth, ear pinna muscles', 'Paleontological: Fossils and Carbon Dating (C-14 half-life Willard Libby)', 'Connecting links: Peripatus (annelida & arthropoda), Duck-billed platypus (reptiles & mammals), Lungfish (fishes & amphibians)', 'Embryological: Extreme similarity in initial embryonic stages of vertebrates']),
          createTopic('MH', '10', 'SCIT2', '1', '4', 'Darwin Theory of Natural Selection & Lamarckism', ['Darwin "Origin of Species" (Survival of the fittest, Overproduction, Struggle for existence)', 'Lamarckism: Theory of inheritance of acquired characters (Use and disuse of organs - giraffe neck) and its disproof'], '', ['Darwin Theory of Natural Selection']),
          createTopic('MH', '10', 'SCIT2', '1', '5', 'Speciation & Journey of Human Evolution', ['Speciation: Formation of new species due to genetic variation and geographic/reproductive isolation', 'Human evolution chronology: Dryopithecus -> Ramapithecus -> Australopithecus -> Homo habilis (handy man) -> Homo erectus (upright man, discovered fire) -> Neanderthal man (first wise man, 100,000 yrs ago) -> Cro-Magnon man (Homo sapiens, 50,000 yrs ago) -> Agriculture (10,000 yrs ago)'])
        ]
      },
      {
        number: '2',
        name: 'Life Processes in Living Organisms Part - 1',
        topics: [
          createTopic('MH', '10', 'SCIT2', '2', '1', 'Living Organisms & Respiration (External vs Cellular Respiration)', ['Respiration at body level (inhalation/exhalation)', 'Respiration at cellular level (complete oxidation of glucose)']),
          createTopic('MH', '10', 'SCIT2', '2', '2', 'Aerobic Cellular Respiration: Glycolysis, TCA Cycle (Krebs Cycle) & Electron Transfer Chain (ETC)', ['Glycolysis (EMP pathway in cytoplasm): Glucose -> 2 Pyruvic acid + 2 ATP + 2 NADH2 + 2 H2O', 'TCA / Krebs Cycle (in mitochondrial matrix): Acetyl-CoA -> CO2 + H2O + NADH2 + FADH2 + ATP', 'Electron Transfer Chain (on mitochondrial cristae): NADH2 yields 3 ATP, FADH2 yields 2 ATP', 'Total yield = 38 ATP per glucose molecule']),
          createTopic('MH', '10', 'SCIT2', '2', '3', 'Anaerobic Respiration: Fermentation in Yeast and Muscle Cells', ['Fermentation of pyruvic acid to alcohol/lactic acid with 2 ATP yield', 'Lactic acid accumulation causing fatigue in athletes']),
          createTopic('MH', '10', 'SCIT2', '2', '4', 'Energy Production from Different Food Components (Proteins, Fats, Vitamins)', ['Carbohydrates yield 4 kcal/g energy', 'Proteins (amino acids) yield 4 kcal/g energy', 'Lipids / Fats (fatty acids and glycerol) yield 9 kcal/g energy', 'Water-soluble (B, C) and Fat-soluble (A, D, E, K) vitamins']),
          createTopic('MH', '10', 'SCIT2', '2', '5', 'Cell Division: Mitosis (Karyokinesis & Cytokinesis) & Somatic Growth', ['Karyokinesis stages: Prophase (chromosomes condense, nuclear membrane vanishes), Metaphase (chromosomes align on equatorial plate), Anaphase (centromeres split, sister chromatids pulled to opposite poles), Telophase (chromosomes decondense, nuclear membrane reforms)', 'Cytokinesis: Cell plate in plants, cleavage furrow in animals', 'Significance: Body growth, wound healing, blood cell restoration']),
          createTopic('MH', '10', 'SCIT2', '2', '6', 'Cell Division: Meiosis (Meiosis I, Meiosis II & Crossing Over)', ['Meiosis I: Prophase I stages (Leptotene, Zygotene, Pachytene crossing over/recombination, Diplotene, Diakinesis)', 'Reduction division (2n -> n) producing 4 haploid gametes', 'Significance of genetic variation in sexual reproduction'])
        ]
      },
      {
        number: '3',
        name: 'Life Processes in Living Organisms Part - 2',
        topics: [
          createTopic('MH', '10', 'SCIT2', '3', '1', 'Asexual Reproduction in Unicellular Organisms (Binary Fission, Multiple Fission, Budding)', ['Binary fission: Simple (Amoeba), Transverse (Paramecium), Longitudinal (Euglena)', 'Multiple fission in Amoeba during adverse conditions (cyst formation)', 'Budding in Yeast']),
          createTopic('MH', '10', 'SCIT2', '3', '2', 'Asexual Reproduction in Multicellular Organisms', ['Fragmentation (Spirogyra)', 'Regeneration (Planaria)', 'Budding (Hydra)', 'Vegetative propagation (Potato eyes, Bryophyllum foliar buds, Sugarcane root buds)', 'Spore formation (Mucor/Rhizopus sporangiospores)']),
          createTopic('MH', '10', 'SCIT2', '3', '3', 'Sexual Reproduction in Plants: Flower Structure, Pollination & Double Fertilisation', ['Floral whorls: Calyx, Corolla, Androecium (stamen), Gynoecium (carpel/pistil)', 'Unisexual vs Bisexual flowers', 'Self vs Cross pollination', 'Double fertilisation: Syngamy (Zygote) and Triple Fusion (Endosperm)']),
          createTopic('MH', '10', 'SCIT2', '3', '4', 'Human Male Reproductive System Anatomy & Spermatogenesis', ['Testes in scrotum, Seminiferous tubules, Epididymis, Vas deferens, Ejaculatory duct, Urethra', 'Accessory glands: Seminal vesicles, Prostate gland, Cowper glands', 'Sperm anatomy (Head with acrosome/nucleus, Middle piece with mitochondria, Tail)']),
          createTopic('MH', '10', 'SCIT2', '3', '5', 'Human Female Reproductive System Anatomy & Oogenesis', ['Pair of Ovaries, Oviducts (Fallopian tubes), Uterus, Vagina', 'Monthly ovulation of one mature ovum']),
          createTopic('MH', '10', 'SCIT2', '3', '6', 'Menstrual Cycle: Phases & Hormonal Control (FSH, LH, Estrogen, Progesterone)', ['Follicular phase (FSH stimulates follicle growth & estrogen secretion)', 'Ovulatory phase (LH surge causes follicle rupture and ovulation around day 14)', 'Luteal phase (Corpus luteum secretes progesterone to thicken endometrium)', 'Menstrual bleeding phase (Corpus albicans regression when fertilisation does not occur)']),
          createTopic('MH', '10', 'SCIT2', '3', '7', 'Reproduction & Modern Assistive Technologies (IVF, Surrogacy, Sperm Bank) & Twins', ['In Vitro Fertilisation (IVF - test tube baby)', 'Surrogacy (womb mother)', 'Sperm banks and Cryopreservation', 'Twins: Monozygotic (identical, same sex) vs Dizygotic (fraternal) twins and Siamese conjoined twins', 'Reproductive health and population explosion'])
        ]
      },
      {
        number: '4',
        name: 'Environmental Management',
        topics: [
          createTopic('MH', '10', 'SCIT2', '4', '1', 'Ecosystem Review & Balance of Food Chains/Webs', ['Biotic and Abiotic components interaction', 'Biogeochemical cycles equilibrium']),
          createTopic('MH', '10', 'SCIT2', '4', '2', 'Environmental Conservation & Factors Affecting Environment (Pollution & Laws)', ['Air, water, soil pollution sources', 'Environment Protection Act 1986, Forest Conservation Act 1980', 'National Green Tribunal (NGT)']),
          createTopic('MH', '10', 'SCIT2', '4', '3', 'Sacred Groves (Devrai) of Maharashtra & Conservation Heritage', ['Forests conserved in the name of God by local communities in Western Ghats']),
          createTopic('MH', '10', 'SCIT2', '4', '4', 'Biodiversity: Three Levels (Genetic, Species, Ecosystem Diversity)', ['Genetic diversity within same species', 'Species diversity in a region', 'Ecosystem diversity across geographic biomes']),
          createTopic('MH', '10', 'SCIT2', '4', '5', 'Biodiversity Hotspots & Classification of Threatened Species', ['34 Global Hotspots (Western Ghats, Indo-Burma, Himalayas in India)', 'IUCN Red Data Book categories: Endangered species (Lion-tailed macaque, Red panda), Rare species (Musk deer), Vulnerable species (Tiger, Lion), Indeterminate species (Giant squirrel / Shekru - State animal of Maharashtra)'])
        ]
      },
      {
        number: '5',
        name: 'Towards Green Energy',
        topics: [
          createTopic('MH', '10', 'SCIT2', '5', '1', 'Generation of Electrical Energy & Principle of Electromagnetic Induction', ['Turbine rotation driving generator armature', 'Thermal vs mechanical energy conversions']),
          createTopic('MH', '10', 'SCIT2', '5', '2', 'Thermal Power Plants & Air Pollution Problems', ['Burning of coal to produce high pressure steam', 'Energy conversion schematic: Chemical energy in coal -> Thermal energy -> Kinetic energy in steam -> Kinetic energy in turbine -> Electrical energy', 'Environmental problems: Greenhouse gas emissions (CO2), SOx/NOx toxic gases, fly ash disposal']),
          createTopic('MH', '10', 'SCIT2', '5', '3', 'Nuclear Power Plants: Nuclear Fission of Uranium-235', ['Chain reaction: U-235 + Neutron -> Barium-141 + Krypton-92 + 3 Neutrons + 200 MeV energy', 'Control rods (Boron/Cadmium) and Moderator (Heavy water/Graphite)', 'Nuclear waste disposal hazards and radiation accident risks (Chernobyl, Fukushima)']),
          createTopic('MH', '10', 'SCIT2', '5', '4', 'Natural Gas Power Plants', ['Combustion of natural gas driving gas turbine (Higher efficiency, lower pollution than coal)']),
          createTopic('MH', '10', 'SCIT2', '5', '5', 'Hydroelectric Power Plants: Clean Renewable Energy', ['Potential energy of dam water -> Kinetic energy of flowing water -> Kinetic energy in turbine -> Electrical energy', 'Advantages (no fuel combustion) and Disadvantages (displacement of villages, submergence of forests, river siltation)']),
          createTopic('MH', '10', 'SCIT2', '5', '6', 'Wind Energy & Solar Energy (Photovoltaic Cells & Solar Thermal Plants)', ['Windmill kinetic energy conversion', 'Solar Photovoltaic (PV) cells: Silicon semiconductor converting sunlight directly into DC electricity', 'Solar PV modules, strings, and arrays with inverters', 'Solar thermal collectors focusing sunlight to boil water for steam turbines'])
        ]
      },
      {
        number: '6',
        name: 'Animal Classification',
        topics: [
          createTopic('MH', '10', 'SCIT2', '6', '1', 'History of Animal Classification (Aristotle to Robert Whittaker & Carl Woese)', ['Artificial classification (Aristotle, Pliny)', 'Traditional two subkingdoms: Non-Chordates vs Chordates']),
          createTopic('MH', '10', 'SCIT2', '6', '2', 'Criteria for Modern Animal Classification', ['Levels of organization (Cellular, Tissue, Organ, Organ-system level)', 'Body symmetry (Asymmetrical e.g. Sponges, Radial e.g. Starfish/Hydra, Bilateral e.g. Human/Fish)', 'Germ layers (Diploblastic - Ectoderm & Endoderm; Triploblastic - Ectoderm, Mesoderm, Endoderm)', 'Body cavity / Coelom (Acoelomate e.g. Platyhelminthes, Pseudocoelomate e.g. Aschelminthes, Eucoelomate true coelom e.g. Annelida to Chordata)', 'Body segmentation (Metameric segmentation in Annelids)']),
          createTopic('MH', '10', 'SCIT2', '6', '3', 'Phylum Porifera (Sponges) & Phylum Coelenterata / Cnidaria', ['Porifera: Cellular level, ostia (pores) and osculum, collar cells (choanocytes), spicules (Sycon, Euspongia bath sponge)', 'Coelenterata: Radial symmetry, diploblastic, tentacles with cnidoblasts (stinging cells for defense/prey capture), Polyp vs Medusa body forms (Hydra, Jellyfish/Aurelia, Physalia, Sea anemone)']),
          createTopic('MH', '10', 'SCIT2', '6', '4', 'Phylum Platyhelminthes, Aschelminthes & Phylum Annelida', ['Platyhelminthes (Flatworms): Bilateral, triploblastic, acoelomate, hermaphrodite, hooks and suckers (Planaria, Tapeworm/Taenia, Liverfluke)', 'Aschelminthes (Roundworms): Pseudocoelomate, cylindrical body, sexual dimorphism (Ascaris intestinal worm, Filarial worm / Wuchereria bancrofti)', 'Annelida (Segmented worms): Eucoelomate, metameric rings, setae/parapodia for locomotion, closed circulation (Earthworm, Leech, Nereis)']),
          createTopic('MH', '10', 'SCIT2', '6', '5', 'Phylum Arthropoda & Phylum Mollusca', ['Arthropoda (Largest phylum): Jointed appendages, chitinous exoskeleton, open circulation, compound eyes (Crab, Prawn, Butterfly, Mosquito, Scorpion, Centipede)', 'Mollusca (Second largest phylum): Soft unsegmented body, calcareous shell, muscular foot, mantle cavity (Snail, Bivalve/Pearl oyster, Octopus)']),
          createTopic('MH', '10', 'SCIT2', '6', '6', 'Phylum Echinodermata & Phylum Hemichordata', ['Echinodermata: Calcareous spines, adult radial symmetry & larva bilateral symmetry, water vascular system with tube feet (Starfish, Sea urchin, Sea cucumber, Brittle star)', 'Hemichordata: Acorn worms, Proboscis, collar, trunk body, stomochord (Balanoglossus, Saccoglossus - Connecting link between non-chordates and chordates)']),
          createTopic('MH', '10', 'SCIT2', '6', '7', 'Phylum Chordata: Urochordata, Cephalochordata & Vertebrata Classes', ['Chordata features: Notochord, dorsal hollow nerve cord, pharyngeal gill slits', 'Subphylum Urochordata (Herdmania, Doliolum - Notochord only in larval tail)', 'Subphylum Cephalochordata (Amphioxus - Notochord extends whole length)', 'Class Cyclostomata (Jawless circular mouth e.g. Petromyzon)', 'Class Pisces (Fishes: cold-blooded, gills, fins, 2-chambered heart e.g. Shark, Rohu, Pomfret)', 'Class Amphibia (Dual habitat, moist skin, 3-chambered heart, external fertilisation e.g. Frog, Toad, Salamander)', 'Class Reptilia (Poikilotherms, creeping locomotion, scaly dry skin e.g. Wall lizard, Snake, Crocodile)', 'Class Aves (Birds: homeotherms, pneumatic bones, feathers, beak, 4-chambered heart e.g. Peacock, Pigeon, Ostrich)', 'Class Mammalia (Mammary glands, body hair, pinna, homeotherms, viviparous e.g. Bat, Whale, Human, Kangaroo)'])
        ]
      },
      {
        number: '7',
        name: 'Introduction to Microbiology',
        topics: [
          createTopic('MH', '10', 'SCIT2', '7', '1', 'Applied & Industrial Microbiology: Dairy Products & Cheese Production', ['Lactic acid fermentation of milk (Lactobacillus bulgaricus, Streptococcus thermophilus)', 'Cheese production: Coagulation by rennet microbial enzymes (Protease / Chymosin), ripening by fungi (Roquefort cheese)']),
          createTopic('MH', '10', 'SCIT2', '7', '2', 'Probiotics & Yoghurt Health Benefits', ['Probiotic organisms: Lactobacillus acidophilus, Bifidobacterium bifidum', 'Restoring gut microflora balance, suppressing pathogenic Clostridium']),
          createTopic('MH', '10', 'SCIT2', '7', '3', 'Bread, Vinegar Production & Microbial Enzymes', ['Yeast (Saccharomyces cerevisiae) baker yeast for bread sponge rise', 'Vinegar production (Ethanol oxidized to Acetic acid by Acetobacter and Gluconobacter)', 'Microbial enzymes: Proteases, lipases, cellulases used in detergents and fruit juice clarification']),
          createTopic('MH', '10', 'SCIT2', '7', '4', 'Industrial Organic Acids, Amino Acids & Antibiotics', ['Citric acid (Aspergillus niger), Gluconic acid, L-Glutamic acid (Monosodium glutamate / Ajinomoto)', 'Antibiotics: Penicillin, Cephalosporins, Streptomycin, Tetracycline, Rifamycin']),
          createTopic('MH', '10', 'SCIT2', '7', '5', 'Microbial Pollution Control (Bioremediation of Oil Spills & Sewage)', ['Hydrocarbonoclastic Bacteria (HCB): Pseudomonas and Alcanivorax borkumensis decomposing oceanic oil slicks', 'Sewage treatment plant (STP) using anaerobic microbial digesters', 'Bio-fuels: Bio-ethanol and bio-diesel from algae and sugarcane molasses'])
        ]
      },
      {
        number: '8',
        name: 'Cell Biology and Biotechnology',
        topics: [
          createTopic('MH', '10', 'SCIT2', '8', '1', 'Cytology & Stem Cells: Types (Embryonic & Adult Stem Cells)', ['Stem cell pluripotency and totipotency', 'Embryonic stem cells from blastocyst (inner cell mass)', 'Adult stem cells from bone marrow, umbilical cord blood, adipose tissue', 'Stem cell therapy in Parkinson, Alzheimer, diabetes, leukemia']),
          createTopic('MH', '10', 'SCIT2', '8', '2', 'Organ Transplantation and Body Donation', ['Brain death concept', 'Transplantation of kidneys, liver, heart, cornea, skin', 'Transplantation of Human Organs Act 1994']),
          createTopic('MH', '10', 'SCIT2', '8', '3', 'Biotechnology in Agriculture: GM Crops, Biofertilisers & Biopesticides', ['Bt Cotton (Bacillus thuringiensis cry gene against bollworm)', 'Bt Brinjal, Golden Rice (Vitamin A enriched with beta-carotene)', 'Herbicide-tolerant crop plants', 'Biofertilisers: Rhizobium, Azotobacter, Mycorrhiza']),
          createTopic('MH', '10', 'SCIT2', '8', '4', 'Biotechnology in Human Health: Vaccines, Insulin, Interferon & Gene Therapy', ['Recombinant DNA technology for Human Insulin (Humulin)', 'Vaccine production through recombinant subunit antigens (Hepatitis B vaccine)', 'Interferon (antiviral protein)', 'Gene therapy for ADA deficiency and somatic cell genetic corrections', 'DNA Fingerprinting in forensic medicine (Dr. Lalji Singh in India)']),
          createTopic('MH', '10', 'SCIT2', '8', '5', 'White, Blue & Green Revolutions in India', ['Green Revolution (Dr. M.S. Swaminathan and Norman Borlaug high-yielding wheat/rice varieties)', 'White Revolution (Dr. Verghese Kurien - Operation Flood dairy co-operatives / AMUL)', 'Blue Revolution (Dr. Hiralal Chaudhari & Dr. Arun Krishnan - Aquaculture and Fisheries)'])
        ]
      },
      {
        number: '9',
        name: 'Social Health',
        topics: [
          createTopic('MH', '10', 'SCIT2', '9', '1', 'Factors Affecting Social Health & Mental Stress', ['Physical, mental, economic and social relationship stability', 'Mental stress causes: academic competition, nuclear families, loneliness, peer pressure']),
          createTopic('MH', '10', 'SCIT2', '9', '2', 'Addictions, Alcoholism & Tobacco Hazards', ['Addiction to alcohol, tobacco, gutkha, drugs (narcotics)', 'Carcinogenic oral cancer risks, cirrhosis of liver, nervous system depression']),
          createTopic('MH', '10', 'SCIT2', '9', '3', 'Cyber Crimes & Incurable Media / Smartphone Addiction', ['Internet gaming disorder (Nomophobia)', 'Cyber security crimes: hacking, online financial fraud, cyberbullying, phishing', 'IT Act 2000 provisions']),
          createTopic('MH', '10', 'SCIT2', '9', '4', 'Stress Management Techniques & Counseling Organisations', ['Laughter clubs, physical exercise, yoga, meditation, music and sports hobbies', 'Salam Bombay Foundation (tobacco-free schools), Childline helpline (1098), Govt psychiatric counseling hotlines'])
        ]
      },
      {
        number: '10',
        name: 'Disaster Management',
        topics: [
          createTopic('MH', '10', 'SCIT2', '10', '1', 'Disaster: Types (Geophysical, Biological, Man-Made) & Scope', ['Geophysical (Earthquake, tsunami, landslide, volcanic eruption)', 'Biological (Epidemics, locust swarms, viral pandemics)', 'Man-made (Industrial chemical leaks, nuclear radiation, terrorism, war)']),
          createTopic('MH', '10', 'SCIT2', '10', '2', 'Disaster Management Authority Structure (NDMA, SDMA, DDMA)', ['National Disaster Management Authority (Prime Minister)', 'State Disaster Management Authority (Chief Minister)', 'District Disaster Management Authority (District Collector)', 'National Disaster Response Force (NDRF) quick deployment battalions']),
          createTopic('MH', '10', 'SCIT2', '10', '3', 'Disaster Management Cycle: Pre-Disaster & Post-Disaster Planning', ['Pre-disaster: Risk assessment, early warning systems, preventive preparedness, mock drills', 'Post-disaster: Emergency rescue, relief distribution, rehabilitation, reconstruction']),
          createTopic('MH', '10', 'SCIT2', '10', '4', 'First Aid, Rescue Techniques & Mock Drills', ['Bleeding control, burn wound dressing, fractures splint immobilization', 'CPR (Cardio-Pulmonary Resuscitation)', 'School and community mock drills evaluating emergency response time'])
        ]
      }
    ]
  }
];

module.exports = { mh10Subjects };
