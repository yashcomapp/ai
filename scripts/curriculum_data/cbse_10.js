const { createTopic } = require('./helper');

const cbse10Subjects = [
  // 1. CBSE Class 10 Mathematics (MATH)
  {
    docId: 'cbse_10_math',
    board: 'CBSE',
    boardCode: 'CBSE',
    class: '10',
    subject: 'Mathematics',
    subjectCode: 'MATH',
    chapters: [
      {
        number: '1',
        name: 'Real Numbers',
        topics: [
          createTopic('CBSE', '10', 'MATH', '1', '1', 'Fundamental Theorem of Arithmetic & Prime Factorisation', ['Statement: Every composite number uniquely expressed as product of primes', 'Finding HCF and LCM using prime factors', 'Formula: HCF(a, b) * LCM(a, b) = a * b'], '', ['Fundamental Theorem of Arithmetic']),
          createTopic('CBSE', '10', 'MATH', '1', '2', 'Revisiting Irrational Numbers & Proof of Irrationality', ['Theorem: If p divides a², then p divides a', 'Rigorous proofs of irrationality for √2, √3, √5, 3+2√5 by contradiction'], '', ['Irrationality Theorem']),
          createTopic('CBSE', '10', 'MATH', '1', '3', 'Decimal Representation of Rational Numbers (2ⁿ5ᵐ denominator rule)', ['Terminating decimal condition: denominator in 2ⁿ5ᵐ form', 'Non-terminating recurring decimal criteria'])
        ]
      },
      {
        number: '2',
        name: 'Polynomials',
        topics: [
          createTopic('CBSE', '10', 'MATH', '2', '1', 'Geometric Meaning of Zeroes of a Polynomial', ['Parabolic graphs of quadratic polynomials (upward/downward opening)', 'Number of zeroes = number of X-axis intersections']),
          createTopic('CBSE', '10', 'MATH', '2', '2', 'Relationship Between Zeroes & Coefficients of Quadratic Polynomial', ['Sum of zeroes: α + β = -b/a', 'Product of zeroes: α * β = c/a', 'Forming quadratic polynomial: k[x² - (α+β)x + αβ]']),
          createTopic('CBSE', '10', 'MATH', '2', '3', 'Zeroes & Coefficients of Cubic Polynomials', ['Sum of zeroes: α + β + γ = -b/a', 'Sum of products in pairs: αβ + βγ + γα = c/a', 'Product of zeroes: αβγ = -d/a']),
          createTopic('CBSE', '10', 'MATH', '2', '4', 'Division Algorithm for Polynomials & Finding Remaining Zeroes', ['p(x) = g(x) * q(x) + r(x)', 'Finding remaining zeroes when two irrational or complex zeroes are given (e.g. ±√5/3)'])
        ]
      },
      {
        number: '3',
        name: 'Pair of Linear Equations in Two Variables',
        topics: [
          createTopic('CBSE', '10', 'MATH', '3', '1', 'Graphical Method & Consistency Conditions (a1/a2 vs b1/b2 vs c1/c2)', ['Intersecting lines (unique solution, consistent: a1/a2 != b1/b2)', 'Parallel lines (no solution, inconsistent: a1/a2 = b1/b2 != c1/c2)', 'Coincident lines (infinitely many solutions, dependent consistent: a1/a2 = b1/b2 = c1/c2)']),
          createTopic('CBSE', '10', 'MATH', '3', '2', 'Algebraic Method: Substitution Method', ['Expressing one variable in terms of the other and substituting']),
          createTopic('CBSE', '10', 'MATH', '3', '3', 'Algebraic Method: Elimination Method by Equating Coefficients', ['Multiplying equations by suitable constants and adding/subtracting']),
          createTopic('CBSE', '10', 'MATH', '3', '4', 'Equations Reducible to Linear Form (1/x, 1/y Substitutions)', ['Variable denominators substitution method u = 1/x, v = 1/y']),
          createTopic('CBSE', '10', 'MATH', '3', '5', 'Applied Word Problems (Upstream/Downstream, Time-Work, Digits, Ages, Geometry)', ['Upstream speed (x - y) and downstream speed (x + y)', 'Fixed charge and per km charge taxi problems', 'Two-digit number reversal problems'])
        ]
      },
      {
        number: '4',
        name: 'Quadratic Equations',
        topics: [
          createTopic('CBSE', '10', 'MATH', '4', '1', 'Standard Form & Identifying Quadratic Equations', ['Standard form: ax² + bx + c = 0 (a != 0)', 'Formulating quadratic equations from verbal descriptions']),
          createTopic('CBSE', '10', 'MATH', '4', '2', 'Solving Quadratic Equations by Factorisation (Splitting Middle Term)', ['Finding roots by factoring quadratic trinomials']),
          createTopic('CBSE', '10', 'MATH', '4', '3', 'Solving by Quadratic Formula (Shreedharacharya Formula)', ['Quadratic formula derivation: x = [-b ± √(b² - 4ac)] / (2a)']),
          createTopic('CBSE', '10', 'MATH', '4', '4', 'Nature of Roots & Discriminant (D = b² - 4ac)', ['D > 0: Two distinct real roots', 'D = 0: Two equal real roots', 'D < 0: No real roots / imaginary roots', 'Finding unknown parameter k for equal roots']),
          createTopic('CBSE', '10', 'MATH', '4', '5', 'Applied Word Problems (Speed-Distance, Pipes-Cisterns, Areas)', ['Train speed decrease/increase problems', 'Two water taps filling a pool together problems'])
        ]
      },
      {
        number: '5',
        name: 'Arithmetic Progressions',
        topics: [
          createTopic('CBSE', '10', 'MATH', '5', '1', 'AP Definition, First Term (a) & Common Difference (d)', ['Arithmetic progression sequence: a, a+d, a+2d, ...', 'Determining whether a given sequence forms an AP']),
          createTopic('CBSE', '10', 'MATH', '5', '2', 'nth Term of an AP Formula (a_n = a + (n - 1)d)', ['Finding specific terms, number of terms n, and first negative term of AP', 'nth term from the end formula: l - (n - 1)d']),
          createTopic('CBSE', '10', 'MATH', '5', '3', 'Sum of First n Terms of an AP (S_n = n/2[2a + (n - 1)d])', ['Sum formula with last term: S_n = n/2(a + l)', 'Relation between sum and nth term: a_n = S_n - S_(n-1)']),
          createTopic('CBSE', '10', 'MATH', '5', '4', 'Applied Real-Life Word Problems on AP Sums', ['Savings ladders, logs stacking, potato race distances, loan repayments'])
        ]
      },
      {
        number: '6',
        name: 'Triangles',
        topics: [
          createTopic('CBSE', '10', 'MATH', '6', '1', 'Similar Figures & Criteria of Similarity (AAA, SSS, SAS)', ['Definition of similarity (equiangular and proportional sides)', 'Equiangular triangles (AAA / AA similarity)', 'Proportional sides (SSS similarity)', 'Ratio of two sides and included angle (SAS similarity)']),
          createTopic('CBSE', '10', 'MATH', '6', '2', 'Basic Proportionality Theorem (Thales Theorem) & Its Converse', ['Statement and geometric proof: Line drawn parallel to one side dividing other two sides in same ratio', 'Converse of BPT theorem and proofs'], '', ['Basic Proportionality Theorem', 'Converse of Basic Proportionality Theorem']),
          createTopic('CBSE', '10', 'MATH', '6', '3', 'Areas of Similar Triangles Theorem', ['Ratio of areas of two similar triangles = square of ratio of corresponding sides = square of altitudes = square of medians'], '', ['Areas of Similar Triangles Theorem']),
          createTopic('CBSE', '10', 'MATH', '6', '4', 'Pythagoras Theorem & Its Converse', ['Theorem and geometric proof using similarity in right triangle', 'Converse of Pythagoras theorem', 'Applications in geometric calculations and ladder problems'], '', ['Pythagoras Theorem', 'Converse of Pythagoras Theorem'])
        ]
      },
      {
        number: '7',
        name: 'Coordinate Geometry',
        topics: [
          createTopic('CBSE', '10', 'MATH', '7', '1', 'Distance Formula: d = √[(x2 - x1)² + (y2 - y1)²]', ['Derivation of distance formula from Pythagoras theorem', 'Collinear points test and classifying triangles/quadrilaterals (equilateral, isosceles, square, rhombus, parallelogram)']),
          createTopic('CBSE', '10', 'MATH', '7', '2', 'Section Formula for Internal Division: (mx2+nx1)/(m+n)', ['Coordinates of point dividing line segment in ratio m1:m2', 'Finding ratio when dividing point coordinates are given', 'Midpoint formula: ((x1+x2)/2, (y1+y2)/2)', 'Points of trisection']),
          createTopic('CBSE', '10', 'MATH', '7', '3', 'Centroid of a Triangle Formula: ((x1+x2+x3)/3, (y1+y2+y3)/3)', ['Coordinates of point of concurrence of medians']),
          createTopic('CBSE', '10', 'MATH', '7', '4', 'Area of Triangle by Coordinates Formula', ['Area = 1/2 |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|', 'Condition for collinearity of three points: Area = 0'])
        ]
      },
      {
        number: '8',
        name: 'Introduction to Trigonometry',
        topics: [
          createTopic('CBSE', '10', 'MATH', '8', '1', 'Trigonometric Ratios of Acute Angle (sin, cos, tan, cot, sec, cosec)', ['Definitions in right triangle (Opposite, Adjacent, Hypotenuse)', 'Reciprocal relations: cosec = 1/sin, sec = 1/cos, cot = 1/tan = cos/sin']),
          createTopic('CBSE', '10', 'MATH', '8', '2', 'Trigonometric Ratios of Specific Angles (0°, 30°, 45°, 60°, 90°)', ['Values table derivation', 'Evaluating algebraic trigonometric expressions']),
          createTopic('CBSE', '10', 'MATH', '8', '3', 'Trigonometric Ratios of Complementary Angles', ['sin(90-θ) = cos θ, cos(90-θ) = sin θ', 'tan(90-θ) = cot θ, cot(90-θ) = tan θ', 'sec(90-θ) = cosec θ, cosec(90-θ) = sec θ']),
          createTopic('CBSE', '10', 'MATH', '8', '4', 'Trigonometric Identities & Rigorous Algebraic Proofs', ['sin²θ + cos²θ = 1', '1 + tan²θ = sec²θ', '1 + cot²θ = cosec²θ', 'Proving complex trigonometric identities'])
        ]
      },
      {
        number: '9',
        name: 'Some Applications of Trigonometry (Heights and Distances)',
        topics: [
          createTopic('CBSE', '10', 'MATH', '9', '1', 'Line of Sight, Angle of Elevation & Angle of Depression', ['Definitions and horizontal reference lines', 'Alternate interior angles relation for angle of depression']),
          createTopic('CBSE', '10', 'MATH', '9', '2', 'Single Triangle Height and Distance Problems', ['Direct height of tower, tree broken by storm, kite string length']),
          createTopic('CBSE', '10', 'MATH', '9', '3', 'Multi-Triangle & Dual Observer Word Problems', ['Two ships approaching lighthouse from opposite sides', 'Pedestal and statue heights, cloud reflection in lake problems'])
        ]
      },
      {
        number: '10',
        name: 'Circles',
        topics: [
          createTopic('CBSE', '10', 'MATH', '10', '1', 'Tangent to a Circle & Point of Contact', ['Secant vs tangent', 'Number of tangents from point inside, on, and outside circle']),
          createTopic('CBSE', '10', 'MATH', '10', '2', 'Tangent Perpendicular to Radius Theorem', ['Theorem and proof: Tangent at any point is perpendicular to radius through point of contact'], '', ['Tangent-Radius Perpendicularity Theorem']),
          createTopic('CBSE', '10', 'MATH', '10', '3', 'Lengths of Tangents from External Point Theorem', ['Theorem and proof: Tangents drawn from external point to a circle are equal in length', 'Inscribed circles in quadrilaterals (AB + CD = AD + BC)'], '', ['Tangent Segments Equality Theorem'])
        ]
      },
      {
        number: '11',
        name: 'Areas Related to Circles',
        topics: [
          createTopic('CBSE', '10', 'MATH', '11', '1', 'Perimeter (Circumference = 2πr) & Area of Circle (πr²)', ['Pi (π) as ratio of circumference to diameter', 'Distance covered in wheel revolutions']),
          createTopic('CBSE', '10', 'MATH', '11', '2', 'Area of Sector of a Circle (Major & Minor Sector)', ['Length of arc: l = (θ / 360) * 2πr', 'Area of sector: A = (θ / 360) * πr² = 1/2 * l * r']),
          createTopic('CBSE', '10', 'MATH', '11', '3', 'Area of Segment of a Circle (Major & Minor Segment)', ['Area of segment = Area of sector - Area of corresponding triangle', 'Triangle area with angle θ (1/2 r² sin θ)']),
          createTopic('CBSE', '10', 'MATH', '11', '4', 'Areas of Combinations of Plane Figures', ['Designs in circles, squares with semicircular ends, shaded region problem solving'])
        ]
      },
      {
        number: '12',
        name: 'Surface Areas and Volumes',
        topics: [
          createTopic('CBSE', '10', 'MATH', '12', '1', 'Surface Area of Combination of Solids', ['Toy (cone mounted on hemisphere), circus tent (cylinder with conical roof), capsule (cylinder with two hemispherical ends)']),
          createTopic('CBSE', '10', 'MATH', '12', '2', 'Volume of Combination of Solids', ['Gulab jamun sugar syrup volume, decorative solid shapes']),
          createTopic('CBSE', '10', 'MATH', '12', '3', 'Conversion of Solid from One Shape to Another', ['Melting spheres into cylinder, digging well and spreading embankment', 'Volume invariance principle']),
          createTopic('CBSE', '10', 'MATH', '12', '4', 'Frustum of a Right Circular Cone', ['Slant height of frustum: l = √[h² + (r1 - r2)²]', 'CSA = πl(r1 + r2), TSA = πl(r1 + r2) + πr1² + πr2²', 'Volume = 1/3 * πh(r1² + r2² + r1*r2)', 'Drinking glass and bucket problems'])
        ]
      },
      {
        number: '13',
        name: 'Statistics',
        topics: [
          createTopic('CBSE', '10', 'MATH', '13', '1', 'Mean of Grouped Data: Direct Method (Σ(f*x) / Σf)', ['Class marks and direct tabulation method']),
          createTopic('CBSE', '10', 'MATH', '13', '2', 'Mean of Grouped Data: Assumed Mean Method & Step-Deviation Method', ['Assumed mean (a) and deviations d_i = x_i - a: X̄ = a + (Σf*d / Σf)', 'Step deviation u_i = (x_i - a)/h: X̄ = a + h * (Σf*u / Σf)']),
          createTopic('CBSE', '10', 'MATH', '13', '3', 'Mode of Grouped Data Formula: l + [(f1 - f0)/(2f1 - f0 - f2)] * h', ['Modal class identification', 'Calculation of modal value']),
          createTopic('CBSE', '10', 'MATH', '13', '4', 'Median of Grouped Data Formula: l + [((N/2 - cf)/f)] * h', ['Cumulative frequency table and median class', 'Finding missing frequencies x and y when median is known']),
          createTopic('CBSE', '10', 'MATH', '13', '5', 'Empirical Relationship Between Measures of Central Tendency & Ogives', ['Empirical formula: 3 Median = Mode + 2 Mean', 'Less-than and more-than ogives intersection gives median'])
        ]
      },
      {
        number: '14',
        name: 'Probability',
        topics: [
          createTopic('CBSE', '10', 'MATH', '14', '1', 'Theoretical (Classical) Probability Definition: P(E) = n(E) / n(S)', ['Equally likely outcomes', 'Range of probability: 0 <= P(E) <= 1', 'Sure event (P=1) and Impossible event (P=0)']),
          createTopic('CBSE', '10', 'MATH', '14', '2', 'Complementary Events: P(E) + P(not E) = 1', ['Elementary events and sum of probabilities of all elementary events equals 1']),
          createTopic('CBSE', '10', 'MATH', '14', '3', 'Standard Probability Experiments (Coins, Dice, Cards & Marbles)', ['Tossing 2 and 3 coins sample space', 'Throwing a pair of dice (36 outcomes)', '52-card deck distribution (Spades, Hearts, Diamonds, Clubs, Face cards)'])
        ]
      }
    ]
  },

  // 2. CBSE Class 10 Science (SCI)
  {
    docId: 'cbse_10_sci',
    board: 'CBSE',
    boardCode: 'CBSE',
    class: '10',
    subject: 'Science',
    subjectCode: 'SCI',
    chapters: [
      {
        number: '1',
        name: 'Chemical Reactions and Equations',
        topics: [
          createTopic('CBSE', '10', 'SCI', '1', '1', 'Chemical Equations & Balancing Chemical Reactions', ['Word equations vs chemical equations', 'Law of conservation of mass in balancing', 'Physical state notation: (s), (l), (g), (aq) and catalysts/heat']),
          createTopic('CBSE', '10', 'SCI', '1', '2', 'Combination Reactions & Exothermic Reactions', ['Formation of single product from two or more reactants (CaO + H2O -> Ca(OH)2 quicklime to slaked lime)', 'Exothermic reactions: Burning of natural gas, respiration']),
          createTopic('CBSE', '10', 'SCI', '1', '3', 'Decomposition Reactions (Thermal, Electrolytic & Photolytic)', ['Thermal decomposition (FeSO4 heating, CaCO3 -> CaO + CO2, Pb(NO3)2 brown fumes of NO2)', 'Electrolytic decomposition of water (2:1 H2 to O2 volume ratio)', 'Photolytic decomposition of AgCl and AgBr in black and white photography', 'Endothermic reactions']),
          createTopic('CBSE', '10', 'SCI', '1', '4', 'Displacement & Double Displacement Reactions (Precipitation)', ['Displacement: Fe + CuSO4 -> FeSO4 + Cu (Reactivity series)', 'Double displacement: Na2SO4 + BaCl2 -> BaSO4 (white precipitate) + 2NaCl']),
          createTopic('CBSE', '10', 'SCI', '1', '5', 'Oxidation, Reduction, Redox Reactions & Corrosion/Rancidity', ['Oxidation: gain of oxygen / loss of hydrogen; Reduction: gain of hydrogen / loss of oxygen', 'Redox reaction examples (CuO + H2 -> Cu + H2O, ZnO + C -> Zn + CO, MnO2 + 4HCl -> MnCl2 + 2H2O + Cl2)', 'Corrosion of metals (rusting of iron, black silver sulphide, green basic copper carbonate)', 'Rancidity of fats and oils and prevention using antioxidants and nitrogen flushing'])
        ]
      },
      {
        number: '2',
        name: 'Acids, Bases and Salts',
        topics: [
          createTopic('CBSE', '10', 'SCI', '2', '1', 'Chemical Properties of Acids and Bases (Indicators, Metals, Carbonates)', ['Olfactory indicators (onion, vanilla, clove oil)', 'Reaction with metals -> Salt + H2 gas (Pop sound test)', 'Reaction of acids with metal carbonates & hydrogen carbonates -> Salt + CO2 + H2O (Lime water milkiness test)', 'Reaction of metal oxides (basic) with acids, non-metal oxides (acidic) with bases']),
          createTopic('CBSE', '10', 'SCI', '2', '2', 'What do all Acids and Bases have in Common? (H+ & OH- Ions)', ['Conduction of electricity in aqueous solutions due to free ions', 'Dry HCl gas vs aqueous HCl litmus test', 'Dilution of acid: exothermic process (Always add acid slowly to water with constant stirring)']),
          createTopic('CBSE', '10', 'SCI', '2', '3', 'pH Scale & Importance of pH in Everyday Life', ['pH = -log[H+], range 0 to 14', 'Human body pH range 7.0 - 7.8', 'Acid rain (pH < 5.6)', 'pH in digestive system (HCl acidity & antacid Mg(OH)2)', 'Tooth decay starts below pH 5.5 (calcium hydroxyapatite corrosion)', 'Self defense by animals and plants (methanoic acid in bee sting and nettle leaf sting, dock plant relief)']),
          createTopic('CBSE', '10', 'SCI', '2', '4', 'Chemicals from Common Salt: Sodium Hydroxide (Chlor-Alkali Process)', ['Electrolysis of brine: 2NaCl + 2H2O -> 2NaOH + Cl2 + H2', 'Anode: Cl2 gas; Cathode: H2 gas; Near cathode: NaOH solution; Uses of all three products']),
          createTopic('CBSE', '10', 'SCI', '2', '5', 'Bleaching Powder, Baking Soda, Washing Soda & Plaster of Paris', ['Bleaching powder: Ca(OH)2 + Cl2 -> CaOCl2 + H2O', 'Baking soda: NaCl + H2O + CO2 + NH3 -> NH4Cl + NaHCO3 (Baking powder = NaHCO3 + tartaric acid, CO2 puffiness)', 'Washing soda: Na2CO3 + 10H2O -> Na2CO3·10H2O', 'Plaster of Paris: CaSO4·2H2O (Gypsum heated at 373 K) -> CaSO4·1/2H2O + 1.5H2O'])
        ]
      },
      {
        number: '3',
        name: 'Metals and Non-metals',
        topics: [
          createTopic('CBSE', '10', 'SCI', '3', '1', 'Physical Properties of Metals and Non-metals & Exceptions', ['Malleability, ductility, thermal & electrical conductivity, sonority, metallic lustre', 'Exceptions: Mercury (liquid metal), Bromine (liquid non-metal), Iodine (lustrous non-metal), Diamond & Graphite, Alkali metals Na/K (soft, cut with knife, low melting point), Gallium/Caesium (melt on palm)']),
          createTopic('CBSE', '10', 'SCI', '3', '2', 'Chemical Properties of Metals (Reactivity with Oxygen, Water & Acids)', ['Amphoteric oxides (Al2O3 and ZnO react with both acids and bases e.g. Sodium aluminate / zincate)', 'Reaction of Na/K with cold water (violent), Mg with hot water, Al/Fe/Zn with steam, Cu/Ag/Au no reaction', 'Reaction of metals with dilute HNO3 (produces N2O/NO2 except Mg and Mn produce H2)', 'Aqua regia (3 HCl : 1 HNO3)']),
          createTopic('CBSE', '10', 'SCI', '3', '3', 'Reactivity Series of Metals & Displacement Reactions', ['Order: K > Na > Ca > Mg > Al > Zn > Fe > Pb > [H] > Cu > Hg > Ag > Au']),
          createTopic('CBSE', '10', 'SCI', '3', '4', 'Formation and Properties of Ionic Compounds', ['Electron dot structures (NaCl, MgCl2, CaO)', 'Properties: Physical nature (hard crystalline solids), high melting and boiling points, solubility in polar solvents, electrical conduction in molten/solution states']),
          createTopic('CBSE', '10', 'SCI', '3', '5', 'Metallurgy: Concentration of Ores, Roasting, Calcination & Reduction', ['Minerals, ores, gangue', 'Roasting (heating sulphide ores in excess air)', 'Calcination (heating carbonate ores in limited air)', 'Reduction of oxides using Carbon / Smelting or Thermite reaction (Fe2O3 + 2Al -> 2Fe + Al2O3 + Heat for welding railway tracks)', 'Electrolytic reduction of highly reactive metals (Na, Al)']),
          createTopic('CBSE', '10', 'SCI', '3', '6', 'Refining of Metals (Electrolytic Refining of Copper) & Corrosion Prevention', ['Electrolytic refining: impure anode, pure thin cathode, acidified CuSO4 electrolyte, anode mud', 'Prevention of corrosion: Painting, oiling, galvanisation (zinc coating), tin plating, anodising, alloying (Steel, Stainless steel, Brass, Bronze, Solder, Amalgam)'])
        ]
      },
      {
        number: '4',
        name: 'Carbon and its Compounds',
        topics: [
          createTopic('CBSE', '10', 'SCI', '4', '1', 'Covalent Bonding & Versatile Nature of Carbon (Catenation & Tetravalency)', ['Sharing of electron pairs (H2, O2, N2, CH4, CO2)', 'Catenation: self-linking property forming long chains, branched chains, rings', 'Tetravalency forming strong covalent bonds due to small atomic size']),
          createTopic('CBSE', '10', 'SCI', '4', '2', 'Saturated and Unsaturated Carbon Compounds & Homologous Series', ['Alkanes (C_n H_2n+2), Alkenes (C_n H_2n), Alkynes (C_n H_2n-2)', 'Homologous series: differing by -CH2- unit (14 u molar mass), gradation in physical properties']),
          createTopic('CBSE', '10', 'SCI', '4', '3', 'Nomenclature of Carbon Compounds (IUPAC Rules & Functional Groups)', ['Functional groups: Halogens (-Cl, -Br), Alcohol (-OH), Aldehyde (-CHO), Ketone (-CO-), Carboxylic acid (-COOH)', 'Prefixes and suffixes (meth-, eth-, prop-, but-, pent-, hex-)']),
          createTopic('CBSE', '10', 'SCI', '4', '4', 'Chemical Properties: Combustion, Oxidation, Addition & Substitution Reactions', ['Combustion: Blue clean flame vs yellow sooty flame', 'Oxidation using Alkaline KMnO4 or Acidified K2Cr2O7 (Ethanol -> Ethanoic acid)', 'Addition reaction of unsaturated hydrocarbons (Hydrogenation using Nickel catalyst for vegetable ghee)', 'Substitution reaction of methane with chlorine in sunlight']),
          createTopic('CBSE', '10', 'SCI', '4', '5', 'Ethanol & Ethanoic Acid: Properties, Reactions (Esterification & Saponification)', ['Ethanol (C2H5OH): reaction with Sodium (H2 gas evolution), dehydration with conc. H2SO4 to ethene', 'Ethanoic acid (CH3COOH): Vinegar (5-8% solution), Esterification reaction with alcohol -> Sweet smelling ester, Saponification (alkaline hydrolysis of esters to soap), Reaction with NaHCO3/Na2CO3 (effervescence of CO2)']),
          createTopic('CBSE', '10', 'SCI', '4', '6', 'Soaps, Detergents & Micelle Formation Cleansing Mechanism', ['Soap: Sodium/potassium salts of long chain fatty acids', 'Structure: Hydrophobic hydrocarbon tail (oil soluble) and Hydrophilic ionic head (water soluble)', 'Micelle formation and emulsification of grease', 'Hard water scum formation with Ca²⁺/Mg²⁺ and synthetic detergents advantage'])
        ]
      },
      {
        number: '5',
        name: 'Life Processes',
        topics: [
          createTopic('CBSE', '10', 'SCI', '5', '1', 'Autotrophic Nutrition & Photosynthesis Mechanism', ['Equation: 6CO2 + 12H2O -> C6H12O6 + 6O2 + 6H2O', 'Three events: Absorption of light energy by chlorophyll, conversion of light to chemical energy & water photolysis, reduction of CO2 to carbohydrates', 'Stomata opening and closing controlled by guard cells turgor']),
          createTopic('CBSE', '10', 'SCI', '5', '2', 'Heterotrophic Nutrition & Human Alimentary Canal Anatomy', ['Holozoic nutrition in Amoeba (pseudopodia, food vacuole)', 'Human digestive system: Mouth (salivary amylase), Stomach (HCl, pepsin, mucus), Small intestine (Bile juice for fat emulsification, pancreatic amylase/trypsin/lipase, intestinal juice), Villi absorption, Large intestine']),
          createTopic('CBSE', '10', 'SCI', '5', '3', 'Respiration: Breakdown of Glucose Pathways & Human Respiratory System', ['Glycolysis in cytoplasm -> Pyruvate (3-carbon)', 'Pathway 1 (Aerobic in mitochondria): CO2 + H2O + 38 ATP', 'Pathway 2 (Anaerobic yeast fermentation): Ethanol + CO2 + 2 ATP', 'Pathway 3 (Lack of oxygen in muscle cells): Lactic acid + 2 ATP (muscle cramps)', 'Human respiration: Nostrils, pharynx, larynx, trachea with cartilage rings, bronchi, alveoli for gas exchange with hemoglobin']),
          createTopic('CBSE', '10', 'SCI', '5', '4', 'Transportation in Humans: Heart Anatomy, Double Circulation & Blood Vessels', ['Four chambers of heart (right/left atria and ventricles)', 'Double circulation: Pulmonary circulation and Systemic circulation', 'Blood pressure (120/80 mmHg), Lymph / tissue fluid transport']),
          createTopic('CBSE', '10', 'SCI', '5', '5', 'Transportation in Plants: Xylem (Water & Minerals) & Phloem (Translocation)', ['Root pressure and transpiration pull in xylem vessels and tracheids', 'Translocation of sucrose in phloem sieve tubes and companion cells using ATP energy']),
          createTopic('CBSE', '10', 'SCI', '5', '6', 'Excretion in Humans (Nephron Anatomy & Urine Formation) & Excretion in Plants', ['Human excretory system: Pair of kidneys, ureters, urinary bladder, urethra', 'Nephron structure: Glomerular ultrafiltration, tubular selective reabsorption (glucose, amino acids, salts, water), tubular secretion, collecting duct', 'Hemodialysis / artificial kidney', 'Plant excretion: Stomatal transpiration, storage in leaves and bark, resins, gums'])
        ]
      },
      {
        number: '6',
        name: 'Control and Coordination',
        topics: [
          createTopic('CBSE', '10', 'SCI', '6', '1', 'Nervous System: Neuron Anatomy & Synapse Transmission', ['Receptors (gustatory, olfactory, photoreceptors, phonoreceptors)', 'Neuron structure: Dendrite, cell body, axon, nerve ending', 'Synapse chemical neurotransmitter transmission']),
          createTopic('CBSE', '10', 'SCI', '6', '2', 'Reflex Action and Reflex Arc', ['Involuntary sudden response pathway: Receptor -> Sensory neuron -> Spinal cord (Relay neuron) -> Motor neuron -> Effector muscle']),
          createTopic('CBSE', '10', 'SCI', '6', '3', 'Human Brain Anatomy & Functions (Forebrain, Midbrain, Hindbrain)', ['Forebrain: Cerebrum (thinking, sensory interpretation, voluntary motor control, memory, hunger center)', 'Midbrain: Visual and auditory reflex centers', 'Hindbrain: Cerebellum (posture and balance precision), Pons (respiratory regulation), Medulla oblongata (involuntary blood pressure, salivation, vomiting)']),
          createTopic('CBSE', '10', 'SCI', '6', '4', 'Coordination in Plants: Nastic Movements vs Tropic Movements', ['Nastic / non-directional immediate movement (Mimosa pudica touch-me-not turgor change)', 'Tropic movements: Phototropism, Geotropism, Chemotropism (pollen tube growth towards ovule), Hydrotropism']),
          createTopic('CBSE', '10', 'SCI', '6', '5', 'Plant Hormones (Auxin, Gibberellin, Cytokinin, Abscisic Acid, Ethylene)', ['Auxin (shoot tip elongation towards light)', 'Gibberellin (stem growth)', 'Cytokinin (rapid cell division in fruits/seeds)', 'Abscisic acid (stress hormone, stomatal closure, wilting of leaves)']),
          createTopic('CBSE', '10', 'SCI', '6', '6', 'Hormones in Animals: Endocrine Glands and Feedback Mechanism', ['Pituitary (Growth hormone - dwarfism/gigantism)', 'Thyroid (Thyroxine - Iodine requirement and goitre prevention)', 'Pancreas (Insulin - diabetes and blood glucose feedback regulation)', 'Adrenal (Adrenaline - Fight or flight emergency responses)', 'Testes (Testosterone) & Ovaries (Estrogen)'])
        ]
      },
      {
        number: '7',
        name: 'How do Organisms Reproduce?',
        topics: [
          createTopic('CBSE', '10', 'SCI', '7', '1', 'DNA Copying & Importance of Variation', ['DNA replication in cell division and biochemical inaccuracy creating variations', 'Survival advantage of variations in changing ecological niches']),
          createTopic('CBSE', '10', 'SCI', '7', '2', 'Asexual Reproduction Modes (Fission, Fragmentation, Regeneration, Budding, Vegetative Propagation, Spores)', ['Binary fission (Amoeba, Leishmania with whip-like flagellum)', 'Multiple fission (Plasmodium)', 'Fragmentation (Spirogyra)', 'Regeneration (Planaria, Hydra specialized cells)', 'Budding (Hydra, Yeast)', 'Vegetative propagation (Bryophyllum leaf notches, layering, grafting)', 'Spore formation (Rhizopus bread mould sporangia)']),
          createTopic('CBSE', '10', 'SCI', '7', '3', 'Sexual Reproduction in Flowering Plants (Pollination & Double Fertilisation)', ['Flower structure: Stamen (anther and filament) and Carpel/Pistil (stigma, style, ovary)', 'Self pollination vs Cross pollination (agents: wind, water, insects)', 'Pollen tube growth and pollen germination on stigma', 'Syngamy (male gamete + egg -> zygote) and Triple fusion (male gamete + 2 polar nuclei -> PEN endosperm)', 'Seed and fruit formation']),
          createTopic('CBSE', '10', 'SCI', '7', '4', 'Sexual Reproduction in Humans: Male & Female Reproductive Systems', ['Male system: Testes in scrotum (lower temperature for spermatogenesis), vas deferens, seminal vesicles & prostate gland (nourishing fluids), urethra, penis', 'Female system: Ovaries (egg release), oviduct / fallopian tube (site of fertilisation), uterus (implantation), cervix, vagina']),
          createTopic('CBSE', '10', 'SCI', '7', '5', 'Menstrual Cycle, Fertilisation, Implantation & Placenta', ['Monthly cycle (28 days) and shedding of uterine endometrium lining', 'Fertilisation in ampulla of fallopian tube', 'Placenta: specialized disc tissue with villi for glucose/oxygen exchange and embryonic waste removal', 'Gestation period (9 months) and parturition']),
          createTopic('CBSE', '10', 'SCI', '7', '6', 'Reproductive Health, Contraceptive Methods & STDs', ['Contraceptive barrier methods (condoms, diaphragms)', 'Chemical methods (oral contraceptive pills preventing ovulation)', 'Intrauterine devices (IUCDs - Copper-T)', 'Surgical methods (Vasectomy in males, Tubectomy in females)', 'Sexually Transmitted Diseases: Bacterial (Gonorrhoea, Syphilis) vs Viral (Warts, HIV/AIDS)'])
        ]
      },
      {
        number: '8',
        name: 'Heredity and Evolution',
        topics: [
          createTopic('CBSE', '10', 'SCI', '8', '1', 'Accumulation of Variation During Reproduction', ['Inheritance of traits from parental generations']),
          createTopic('CBSE', '10', 'SCI', '8', '2', 'Mendel Laws of Inheritance: Monohybrid Cross (Dominant vs Recessive)', ['Cross of Pure Tall (TT) and Pure Dwarf (tt)', 'F1 generation (all Tall - Tt) and F2 generation (Phenotypic ratio 3:1, Genotypic ratio 1:2:1)', 'Law of Segregation']),
          createTopic('CBSE', '10', 'SCI', '8', '3', 'Mendel Dihybrid Cross & Law of Independent Assortment', ['Cross of Round-Yellow (RRYY) and Wrinkled-Green (rryy)', 'F2 generation phenotypic ratio 9:3:3:1', 'Independent assortment of genes']),
          createTopic('CBSE', '10', 'SCI', '8', '4', 'Sex Determination in Humans & Environmental Sex Determination', ['Human sex chromosomes: XX (female) and XY (male)', '50% probability of male/female child determined strictly by father sperm (X or Y)', 'Environmental sex determination in reptiles (temperature dependent in turtles/lizards), snails changing sex'])
        ]
      },
      {
        number: '9',
        name: 'Light - Reflection and Refraction',
        topics: [
          createTopic('CBSE', '10', 'SCI', '9', '1', 'Spherical Mirrors: Terminology, Ray Rules & Concave Mirror Ray Diagrams', ['Pole (P), Focus (F), Centre of curvature (C), Principal axis, Focal length (f = R/2)', 'Four rules of ray tracing for spherical mirrors', 'Ray diagrams for all 6 object positions for concave mirror']),
          createTopic('CBSE', '10', 'SCI', '9', '2', 'Convex Mirror Ray Diagrams & Practical Applications', ['Ray diagrams for convex mirror (always virtual, erect, diminished)', 'Uses: Rear-view mirrors (wide field of view), street lights, concave mirror shaving and solar furnaces']),
          createTopic('CBSE', '10', 'SCI', '9', '3', 'Mirror Formula (1/f = 1/v + 1/u) & Magnification (m = -v/u = h\'/h)', ['New Cartesian Sign Convention rules', 'Solving numerical mirror problems']),
          createTopic('CBSE', '10', 'SCI', '9', '4', 'Refraction of Light & Snell Law of Refraction', ['Cause of refraction (change in speed of light in different media)', 'Snell Law: (sin i / sin r) = constant = n21', 'Refraction through a rectangular glass slab and lateral displacement']),
          createTopic('CBSE', '10', 'SCI', '9', '5', 'Absolute & Relative Refractive Index (n = c / v)', ['Speed of light in vacuum c = 3 * 10^8 m/s', 'Optical density: denser medium (slower light, bends towards normal) vs rarer medium (faster light, bends away from normal)', 'Relative refractive index n21 = v1 / v2']),
          createTopic('CBSE', '10', 'SCI', '9', '6', 'Spherical Lenses: Convex & Concave Lens Ray Diagrams', ['Optical centre (O), Principal focus (F1, F2), Focal length', 'Ray diagrams for convex lens (6 positions) and concave lens (2 positions)']),
          createTopic('CBSE', '10', 'SCI', '9', '7', 'Lens Formula (1/f = 1/v - 1/u) & Magnification (m = v/u = h\'/h)', ['Sign conventions for convex (+f) and concave (-f) lenses', 'Solving numerical lens problems']),
          createTopic('CBSE', '10', 'SCI', '9', '8', 'Power of a Lens Formula: P = 1 / f (in metres)', ['SI unit Dioptre (1 D = 1 m⁻¹)', 'Power of convex lens (+ve) and concave lens (-ve)', 'Combination of thin lenses: P = P1 + P2 + P3'])
        ]
      },
      {
        number: '10',
        name: 'The Human Eye and the Colourful World',
        topics: [
          createTopic('CBSE', '10', 'SCI', '10', '1', 'Human Eye Anatomy & Power of Accommodation', ['Cornea, iris (regulates pupil size), pupil, crystalline lens, ciliary muscles, retina (photoreceptor rods and cones), optic nerve', 'Power of accommodation: focal length adjustment for near point (25 cm) and far point (infinity)']),
          createTopic('CBSE', '10', 'SCI', '10', '2', 'Defects of Vision: Myopia (Near-sightedness) & Correction', ['Causes: Excessive curvature of eye lens or elongation of eyeball', 'Image formed in front of retina', 'Correction using concave lens of suitable focal length']),
          createTopic('CBSE', '10', 'SCI', '10', '3', 'Defects of Vision: Hypermetropia & Presbyopia', ['Hypermetropia causes: Focal length too long or eyeball too short; image behind retina; correction by convex lens', 'Presbyopia: Aging weakening of ciliary muscles and flexibility loss; correction by bifocal lenses (upper concave, lower convex)', 'Cataract surgery']),
          createTopic('CBSE', '10', 'SCI', '10', '4', 'Refraction Through a Triangular Glass Prism & Angle of Deviation (D)', ['Angle of prism (A), angle of incidence (i), angle of emergence (e)', 'Relation: i + e = A + D']),
          createTopic('CBSE', '10', 'SCI', '10', '5', 'Dispersion of White Light, Newton Glass Prism Experiment & Rainbow', ['Splitting into VIBGYOR (Red bends least, Violet bends most)', 'Recombination of spectrum using inverted second prism (Newton experiment)', 'Rainbow formation: Refraction -> Dispersion -> Internal Reflection -> Refraction in raindrops']),
          createTopic('CBSE', '10', 'SCI', '10', '6', 'Atmospheric Refraction (Twinkling of Stars, Advanced Sunrise & Delayed Sunset)', ['Continuous gradation of atmospheric refractive index', 'Apparent higher position of stars and twinkling effect (point source vs extended planet source)', 'Early sunrise (2 min before) and delayed sunset (2 min after) making day 4 min longer']),
          createTopic('CBSE', '10', 'SCI', '10', '7', 'Scattering of Light: Tyndall Effect & Color of Sky / Sunrise-Sunset', ['Tyndall effect in colloidal smoke/fog and dense forest canopy', 'Rayleigh scattering: Intensity ∝ 1/λ⁴', 'Blue color of sky (short wavelength blue scattered more)', 'Reddish appearance of sun at sunrise and sunset (longer red wavelength travels longer distance through atmosphere)'])
        ]
      },
      {
        number: '11',
        name: 'Electricity',
        topics: [
          createTopic('CBSE', '10', 'SCI', '11', '1', 'Electric Current (I = Q/t) & Potential Difference (V = W/Q)', ['Definition of electric charge (Coulomb), Ampere, Volt', 'Direction of conventional current vs electron flow', 'Ammeter (in series, low resistance) and Voltmeter (in parallel, high resistance)']),
          createTopic('CBSE', '10', 'SCI', '11', '2', 'Ohm Law & Circuit Diagram Verification', ['Statement: V ∝ I at constant temperature (V = IR)', 'Ohmic vs non-ohmic conductors and V-I slope = Resistance'], '', ['Ohm Law']),
          createTopic('CBSE', '10', 'SCI', '11', '3', 'Factors Affecting Resistance & Resistivity Formula (R = ρ * L / A)', ['Resistance depends on length (L), cross-sectional area (A), material, temperature', 'Resistivity (ρ in Ω·m) of conductors, alloys (Nichrome), insulators', 'Why heating elements of toasters/irons are made of alloys rather than pure metals']),
          createTopic('CBSE', '10', 'SCI', '11', '4', 'Resistors in Series Combination (Rs = R1 + R2 + R3)', ['Derivation of equivalent resistance', 'Current is same throughout, total voltage divides: V = V1 + V2 + V3', 'Disadvantages of series connection in domestic appliances']),
          createTopic('CBSE', '10', 'SCI', '11', '5', 'Resistors in Parallel Combination (1/Rp = 1/R1 + 1/R2 + 1/R3)', ['Derivation of equivalent resistance', 'Voltage is same across each resistor, total current divides: I = I1 + I2 + I3', 'Advantages of parallel connection in domestic circuits']),
          createTopic('CBSE', '10', 'SCI', '11', '6', 'Heating Effect of Electric Current & Joule Law of Heating (H = I²Rt)', ['Derivation: H = VIt = I²Rt = (V²/R)t (Joules)', 'Applications: Electric iron, heater, electric toaster, electric bulb (tungsten filament, inert argon/nitrogen filling), electric fuse safety mechanism'], '', ['Joule Law of Heating']),
          createTopic('CBSE', '10', 'SCI', '11', '7', 'Electric Power Formulas (P = VI = I²R = V²/R) & Commercial Units (kWh)', ['Power SI unit Watt (1 W = 1 V * 1 A)', 'Commercial unit of electrical energy: 1 kWh (1 Board of Trade Unit) = 3.6 * 10^6 Joules', 'Calculating electricity bills for household appliances'])
        ]
      },
      {
        number: '12',
        name: 'Magnetic Effects of Electric Current',
        topics: [
          createTopic('CBSE', '10', 'SCI', '12', '1', 'Magnetic Field & Properties of Magnetic Field Lines', ['Oersted experiment', 'Field lines emerge from North pole and enter South pole (closed continuous curves)', 'Closeness of lines indicates field strength', 'No two magnetic field lines intersect (two directions of compass needle impossible)']),
          createTopic('CBSE', '10', 'SCI', '12', '2', 'Magnetic Field Due to Current Carrying Straight Conductor & Right Hand Thumb Rule', ['Concentric circular magnetic field lines around straight wire', 'Maxwell Right Hand Thumb Rule (Thumb in current direction, curled fingers in field direction)']),
          createTopic('CBSE', '10', 'SCI', '12', '3', 'Magnetic Field Due to Circular Loop & Solenoid', ['Field at center of circular loop is uniform and perpendicular', 'Solenoid behaves like a bar magnet with North and South poles', 'Electromagnet formation inside soft iron core']),
          createTopic('CBSE', '10', 'SCI', '12', '4', 'Force on Current Carrying Conductor in Magnetic Field & Fleming Left Hand Rule', ['Lorentz magnetic force principle', 'Maximum force when conductor is perpendicular to magnetic field', 'Fleming Left Hand Rule (Forefinger = Field, Middle finger = Current, Thumb = Motion/Force)', 'Principle of electric motor']),
          createTopic('CBSE', '10', 'SCI', '12', '5', 'Domestic Electric Circuits: Live, Neutral, Earth Wires & Safety', ['Live wire (220 V, red insulation), Neutral wire (0 V, black insulation), Earth wire (green insulation)', 'Earthing of metallic appliances safety (prevents electric shocks)', 'Short circuiting vs overloading', 'Fuse rating and circuit breakers'])
        ]
      },
      {
        number: '13',
        name: 'Our Environment',
        topics: [
          createTopic('CBSE', '10', 'SCI', '13', '1', 'Ecosystem Components: Biotic & Abiotic Factors', ['Producers (chlorophyll containing autotrophs)', 'Consumers (herbivores, carnivores, omnivores, parasites)', 'Decomposers (bacteria and fungi recycling inorganic nutrients)']),
          createTopic('CBSE', '10', 'SCI', '13', '2', 'Food Chains, Food Webs & 10% Energy Transfer Law', ['Trophic levels (T1, T2, T3, T4)', 'Lindeman 10% Law: Only 10% energy transferred to next trophic level; 90% lost as heat and metabolic maintenance', 'Unidirectional energy flow']),
          createTopic('CBSE', '10', 'SCI', '13', '3', 'Biological Magnification of Non-Biodegradable Pesticides', ['Accumulation of persistent chemicals (e.g. DDT) increasing at successive trophic levels, maximum concentration in apex humans']),
          createTopic('CBSE', '10', 'SCI', '13', '4', 'Ozone Layer Depletion & Montreal Protocol (CFCs)', ['Formation of Ozone (O2 + UV -> O + O; O + O2 -> O3)', 'Ozone shields earth from harmful UV radiation (skin cancer, cataracts)', 'Depletion by Chlorofluorocarbons (CFCs in refrigerants/fire extinguishers)', 'UNEP Montreal Protocol (1987) banning CFC production']),
          createTopic('CBSE', '10', 'SCI', '13', '5', 'Solid Waste Management: Biodegradable vs Non-Biodegradable Waste', ['Biodegradable waste (broken down by biological enzymes)', 'Non-biodegradable waste (plastics, persistent chemicals)', 'Eco-friendly disposal: Composting, recycling, sewage treatment, banning disposable plastics'])
        ]
      }
    ]
  }
];

module.exports = { cbse10Subjects };
