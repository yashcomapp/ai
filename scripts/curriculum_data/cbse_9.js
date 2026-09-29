const { createTopic } = require('./helper');

const cbse9Subjects = [
  // =========================================================================
  // 1. CBSE Class 9: Mathematics (Standard NCERT Curriculum)
  // =========================================================================
  {
    docId: 'cbse_9_math',
    board: 'CBSE',
    boardCode: 'CBSE',
    class: '9',
    subject: 'Mathematics',
    subjectCode: 'MATH',
    chapters: [
      {
        number: '1',
        name: 'Number Systems',
        topics: [
          createTopic('CBSE', '9', 'MATH', '1', '1', 'Real Numbers: Rational Numbers & Decimal Expansions', ['Definition of rational numbers p/q (q != 0)', 'Terminating vs non-terminating recurring decimals', 'Converting 0.p̄ and 0.pq̄ to p/q fraction form']),
          createTopic('CBSE', '9', 'MATH', '1', '2', 'Irrational Numbers & Geometric Construction on Number Line', ['Definition of irrational numbers (non-terminating non-repeating)', 'Constructing √2, √3, √5 on number line using Pythagoras spiral method', 'Locating √x geometrically for any positive real number x']),
          createTopic('CBSE', '9', 'MATH', '1', '3', 'Operations on Real Numbers & Rationalisation of Surds', ['Properties of addition, subtraction, multiplication, division of irrationals', 'Rationalising monomial and binomial denominators using conjugate surds (1/(a + √b))']),
          createTopic('CBSE', '9', 'MATH', '1', '4', 'Laws of Exponents for Real Numbers', ['Fractional exponents a^(p/q)', 'Laws: a^p * a^q = a^(p+q), (a^p)^q = a^(pq), a^p / a^q = a^(p-q), a^p * b^p = (ab)^p'])
        ]
      },
      {
        number: '2',
        name: 'Polynomials',
        topics: [
          createTopic('CBSE', '9', 'MATH', '2', '1', 'Polynomials in One Variable, Degree & Classification', ['Terms, coefficients, degree of polynomial', 'Monomials, binomials, trinomials', 'Linear, quadratic, cubic, zero polynomials']),
          createTopic('CBSE', '9', 'MATH', '2', '2', 'Zeroes of a Polynomial & Geometric Meaning', ['Evaluating p(k) for given value k', 'Finding zeroes of linear and quadratic polynomials algebraically']),
          createTopic('CBSE', '9', 'MATH', '2', '3', 'Remainder Theorem & Long Division Algorithm', ['Statement: If p(x) is divided by (x - a), remainder is p(a)', 'Verifying polynomial division by long division method'], '', ['Remainder Theorem']),
          createTopic('CBSE', '9', 'MATH', '2', '4', 'Factor Theorem & Splitting Middle Term for Quadratics', ['Statement: (x - a) is a factor of p(x) if and only if p(a) = 0', 'Factoring quadratic trinomials ax² + bx + c', 'Factoring cubic polynomials using trial and factor theorem'], '', ['Factor Theorem']),
          createTopic('CBSE', '9', 'MATH', '2', '5', 'Algebraic Identities (Squares, Cubes & Three Variables)', ['(x + y + z)² = x² + y² + z² + 2xy + 2yz + 2zx', '(x ± y)³ = x³ ± y³ ± 3xy(x ± y)', 'x³ + y³ + z³ - 3xyz = (x + y + z)(x² + y² + z² - xy - yz - zx)', 'Conditional identity: If x + y + z = 0, then x³ + y³ + z³ = 3xyz'])
        ]
      },
      {
        number: '3',
        name: 'Coordinate Geometry',
        topics: [
          createTopic('CBSE', '9', 'MATH', '3', '1', 'Cartesian Coordinate Plane, Axes & Quadrants', ['X-axis (abscissa) and Y-axis (ordinate)', 'Origin (0,0)', 'Four quadrants (I: +,+, II: -,+, III: -,-, IV: +,-)']),
          createTopic('CBSE', '9', 'MATH', '3', '2', 'Plotting Points & Reading Coordinates on Graph', ['Plotting points (x, y) with positive and negative coordinates', 'Points lying on axes (x, 0) and (0, y)'])
        ]
      },
      {
        number: '4',
        name: 'Linear Equations in Two Variables',
        topics: [
          createTopic('CBSE', '9', 'MATH', '4', '1', 'Linear Equation Standard Form: ax + by + c = 0', ['Identifying coefficients a, b, c', 'Expressing word statements as linear equations in two variables']),
          createTopic('CBSE', '9', 'MATH', '4', '2', 'Solutions of a Linear Equation in Two Variables', ['Infinitely many solutions property', 'Finding four distinct solutions (x, y) for a given equation']),
          createTopic('CBSE', '9', 'MATH', '4', '3', 'Graph of a Linear Equation in Two Variables', ['Plotting solutions and drawing straight line graph', 'Equations of lines parallel to X-axis (y = k) and Y-axis (x = k)'])
        ]
      },
      {
        number: '5',
        name: 'Introduction to Euclid Geometry',
        topics: [
          createTopic('CBSE', '9', 'MATH', '5', '1', 'Euclid Definitions, Axioms & Historical Context', ['Point, line, surface definitions', '7 Euclidean Axioms (Things equal to same thing are equal, etc.)']),
          createTopic('CBSE', '9', 'MATH', '5', '2', 'Euclid Five Postulates & Parallel Postulate', ['Postulate 1 to 4: Straight line, terminated line, circle, right angles', 'Postulate 5: Playfair axiom and equivalent versions of parallel postulate'])
        ]
      },
      {
        number: '6',
        name: 'Lines and Angles',
        topics: [
          createTopic('CBSE', '9', 'MATH', '6', '1', 'Basic Terms: Ray, Line Segment, Collinear & Types of Angles', ['Acute, right, obtuse, straight, reflex angles', 'Complementary and supplementary angles', 'Adjacent angles and linear pair axiom']),
          createTopic('CBSE', '9', 'MATH', '6', '2', 'Vertically Opposite Angles Theorem & Intersecting Lines', ['Proving vertically opposite angles are equal when two lines intersect'], '', ['Vertically Opposite Angles Theorem']),
          createTopic('CBSE', '9', 'MATH', '6', '3', 'Parallel Lines & Transversal Angle Theorems', ['Corresponding angles axiom', 'Alternate interior angles theorem and converse', 'Consecutive interior angles supplementary theorem and converse'], '', ['Alternate Interior Angles Theorem', 'Consecutive Interior Angles Theorem']),
          createTopic('CBSE', '9', 'MATH', '6', '4', 'Angle Sum Property of a Triangle & Exterior Angle Theorem', ['Sum of angles in a triangle is 180° theorem', 'Exterior angle = sum of two interior opposite angles theorem'], '', ['Angle Sum Theorem of Triangle', 'Exterior Angle Theorem'])
        ]
      },
      {
        number: '7',
        name: 'Triangles',
        topics: [
          createTopic('CBSE', '9', 'MATH', '7', '1', 'Congruence Criteria: SAS and ASA Axioms/Theorems', ['Side-Angle-Side (SAS) congruence axiom', 'Angle-Side-Angle (ASA) congruence theorem and AAS corollary'], '', ['ASA Congruence Theorem']),
          createTopic('CBSE', '9', 'MATH', '7', '2', 'Isosceles Triangle Theorems & Angle-Side Relationships', ['Angles opposite to equal sides of an isosceles triangle are equal theorem', 'Sides opposite to equal angles of a triangle are equal theorem'], '', ['Isosceles Triangle Theorem', 'Converse of Isosceles Triangle Theorem']),
          createTopic('CBSE', '9', 'MATH', '7', '3', 'SSS and RHS Congruence Criteria', ['Side-Side-Side (SSS) congruence rule', 'Right angle-Hypotenuse-Side (RHS) congruence rule'], '', ['SSS Congruence Rule', 'RHS Congruence Rule']),
          createTopic('CBSE', '9', 'MATH', '7', '4', 'Inequalities in a Triangle', ['Angle opposite to longer side is greater theorem', 'Side opposite to greater angle is longer theorem', 'Sum of any two sides of a triangle is greater than third side theorem'], '', ['Triangle Inequality Theorem'])
        ]
      },
      {
        number: '8',
        name: 'Quadrilaterals',
        topics: [
          createTopic('CBSE', '9', 'MATH', '8', '1', 'Angle Sum Property of a Quadrilateral (360°)', ['Proof that sum of four interior angles of a quadrilateral is 360°']),
          createTopic('CBSE', '9', 'MATH', '8', '2', 'Properties of Parallelograms & Theorems', ['Diagonal divides parallelogram into two congruent triangles', 'Opposite sides and angles are equal theorems', 'Diagonals bisect each other theorem and converses'], '', ['Parallelogram Diagonal Congruence Theorem', 'Parallelogram Diagonals Bisection Theorem']),
          createTopic('CBSE', '9', 'MATH', '8', '3', 'The Midpoint Theorem & Its Converse', ['Segment joining midpoints of two sides of a triangle is parallel to third side and half of it', 'Converse: Line drawn through midpoint of one side parallel to another side bisects third side'], '', ['Midpoint Theorem', 'Converse of Midpoint Theorem'])
        ]
      },
      {
        number: '9',
        name: 'Circles',
        topics: [
          createTopic('CBSE', '9', 'MATH', '9', '1', 'Circle Anatomy: Chord, Arc, Sector, Segment', ['Radius, diameter, chord, secant, tangent basics', 'Minor/major arcs, minor/major sectors, segments']),
          createTopic('CBSE', '9', 'MATH', '9', '2', 'Perpendicular from Centre to Chord & Distance Theorems', ['Perpendicular from centre to chord bisects the chord theorem and converse', 'Equal chords of a circle are equidistant from centre theorem and converse'], '', ['Perpendicular to Chord Bisection Theorem', 'Equal Chords Equidistance Theorem']),
          createTopic('CBSE', '9', 'MATH', '9', '3', 'Angle Subtended by Arc at Centre & Circumference', ['Angle subtended by arc at centre is double the angle subtended at remaining circumference', 'Angles in same segment of a circle are equal theorem', 'Angle in a semicircle is a right angle (90°)'], '', ['Inscribed Angle Theorem', 'Angle in Semicircle Theorem']),
          createTopic('CBSE', '9', 'MATH', '9', '4', 'Cyclic Quadrilaterals: Opposite Angle Sum Theorem', ['Opposite angles of cyclic quadrilateral are supplementary (sum = 180°)', 'Converse: If opposite angles sum to 180°, quadrilateral is concyclic'], '', ['Cyclic Quadrilateral Theorem', 'Converse of Cyclic Quadrilateral Theorem'])
        ]
      },
      {
        number: '10',
        name: 'Heron Formula',
        topics: [
          createTopic('CBSE', '9', 'MATH', '10', '1', 'Heron Formula Derivation & Semi-Perimeter', ['Semi-perimeter s = (a + b + c) / 2', 'Area formula: A = √[s(s - a)(s - b)(s - c)]', 'Area of equilateral and isosceles triangles using Heron formula']),
          createTopic('CBSE', '9', 'MATH', '10', '2', 'Applications in Finding Areas of Quadrilaterals & Land Plots', ['Splitting quadrilaterals along diagonal into two triangles', 'Real-world field and banner triangular design calculations'])
        ]
      },
      {
        number: '11',
        name: 'Surface Areas and Volumes',
        topics: [
          createTopic('CBSE', '9', 'MATH', '11', '1', 'Surface Area & Volume of Right Circular Cone', ['Slant height formula: l = √(r² + h²)', 'Curved Surface Area = πrl', 'Total Surface Area = πr(r + l)', 'Volume = 1/3 * πr²h']),
          createTopic('CBSE', '9', 'MATH', '11', '2', 'Surface Area & Volume of Sphere and Hemisphere', ['Surface Area of Sphere = 4πr²', 'Curved Surface Area of Hemisphere = 2πr²', 'Total Surface Area of Hemisphere = 3πr²', 'Volume of Sphere = 4/3 * πr³', 'Volume of Hemisphere = 2/3 * πr³'])
        ]
      },
      {
        number: '12',
        name: 'Statistics',
        topics: [
          createTopic('CBSE', '9', 'MATH', '12', '1', 'Bar Graphs & Histograms with Varying Base Widths', ['Constructing bar graphs', 'Histograms with uniform class width', 'Histograms with varying class intervals: Adjusted Frequency formula']),
          createTopic('CBSE', '9', 'MATH', '12', '2', 'Frequency Polygons Construction', ['Using mid-points / class marks (Upper limit + Lower limit)/2', 'Constructing frequency polygon with and without histogram'])
        ]
      }
    ]
  },

  // =========================================================================
  // 2. CBSE Class 9: Science (Standard NCERT Curriculum)
  // =========================================================================
  {
    docId: 'cbse_9_sci',
    board: 'CBSE',
    boardCode: 'CBSE',
    class: '9',
    subject: 'Science',
    subjectCode: 'SCI',
    chapters: [
      {
        number: '1',
        name: 'Matter in Our Surroundings',
        topics: [
          createTopic('CBSE', '9', 'SCI', '1', '1', 'Particulate Nature of Matter & Characteristics of Particles', ['Matter made of tiny particles', 'Particles have space between them, attract each other, and continuously move (Brownian motion)']),
          createTopic('CBSE', '9', 'SCI', '1', '2', 'States of Matter: Solid, Liquid, Gas (Density, Compressibility)', ['Solid, liquid, gas comparison on shape, volume, rigidity, compressibility, diffusion']),
          createTopic('CBSE', '9', 'SCI', '1', '3', 'Change of State: Melting, Boiling & Latent Heat', ['Melting point and Latent Heat of Fusion', 'Boiling point and Latent Heat of Vaporisation', 'Effect of temperature change (Kelvin scale = °C + 273.15)']),
          createTopic('CBSE', '9', 'SCI', '1', '4', 'Effect of Pressure, Sublimation & Deposition', ['Liquefaction of gases by increasing pressure and decreasing temperature', 'Sublimation of camphor/ammonium chloride, dry ice (solid CO2)']),
          createTopic('CBSE', '9', 'SCI', '1', '5', 'Evaporation & Factors Affecting Evaporation', ['Surface phenomenon vs bulk phenomenon', 'Factors: surface area, temperature, humidity, wind speed', 'Evaporative cooling mechanism (earthen pots, sweating, cotton clothes)'])
        ]
      },
      {
        number: '2',
        name: 'Is Matter Around Us Pure?',
        topics: [
          createTopic('CBSE', '9', 'SCI', '2', '1', 'Pure Substances vs Mixtures (Elements, Compounds & Mixtures)', ['Element definition (metals, non-metals, metalloids)', 'Compounds: fixed composition by mass, distinct chemical properties', 'Mixtures: homogeneous vs heterogeneous']),
          createTopic('CBSE', '9', 'SCI', '2', '2', 'Solutions: Concentration, Saturated Solutions & Solubility', ['Solute and solvent', 'Mass by mass percentage & mass by volume percentage concentration formulas', 'Saturated vs unsaturated solutions, effect of temperature on solubility']),
          createTopic('CBSE', '9', 'SCI', '2', '3', 'Suspensions, Colloids & Tyndall Effect', ['Properties of suspension: heterogeneous, visible particles, filtration separation', 'Properties of colloid: Tyndall light scattering effect, Brownian motion, dispersed phase & dispersion medium types (sol, gel, emulsion, aerosol)']),
          createTopic('CBSE', '9', 'SCI', '2', '4', 'Separation Techniques of Mixtures', ['Evaporation, centrifugation, separating funnel for immiscible liquids', 'Sublimation, paper chromatography for dye separation', 'Simple distillation vs fractional distillation (fractionating column) for miscible liquids, air component separation'])
        ]
      },
      {
        number: '3',
        name: 'Atoms and Molecules',
        topics: [
          createTopic('CBSE', '9', 'SCI', '3', '1', 'Laws of Chemical Combination (Conservation of Mass & Constant Proportions)', ['Law of Conservation of Mass (Lavoisier)', 'Law of Definite / Constant Proportions (Proust) with water and ammonia examples'], '', ['Law of Conservation of Mass', 'Law of Constant Proportions']),
          createTopic('CBSE', '9', 'SCI', '3', '2', 'Dalton Atomic Theory & Modern Atomic Symbols (IUPAC)', ['Postulates of Dalton theory explaining chemical laws', 'IUPAC symbols of elements and Latin names (Fe, Na, K, Cu, Au, Ag)']),
          createTopic('CBSE', '9', 'SCI', '3', '3', 'Atomic Mass, Unified Mass Unit (u) & Relative Atomic Mass', ['Standard reference: Carbon-12 isotope (1/12th mass)', 'Atomic mass scale definitions']),
          createTopic('CBSE', '9', 'SCI', '3', '4', 'Molecules of Elements, Compounds, Ions & Radicals', ['Molecules of elements (monoatomic, diatomic, polyatomic e.g. He, O2, P4, S8)', 'Cations (+) vs Anions (-), polyatomic ions (NH4+, SO4^2-, CO3^2-, NO3-)']),
          createTopic('CBSE', '9', 'SCI', '3', '5', 'Writing Chemical Formulae & Valency Cross-Over', ['Valency rules and criss-cross method for binary compounds and polyatomic salts']),
          createTopic('CBSE', '9', 'SCI', '3', '6', 'Molecular Mass & Formula Unit Mass Calculations', ['Calculating molecular mass by summing atomic masses of constituent atoms', 'Formula unit mass of ionic compounds (e.g. NaCl, CaCl2)'])
        ]
      },
      {
        number: '4',
        name: 'Structure of the Atom',
        topics: [
          createTopic('CBSE', '9', 'SCI', '4', '1', 'Charged Particles: Electron (J.J. Thomson) & Proton (E. Goldstein Canal Rays)', ['Discovery of cathode rays and electrons (e/m ratio)', 'Canal rays / anode rays and proton discovery']),
          createTopic('CBSE', '9', 'SCI', '4', '2', 'Thomson Plum Pudding Model & Rutherford Alpha Scattering Experiment', ['Thomson model limitations', 'Rutherford alpha particle scattering with gold foil', 'Discovery of atomic nucleus and nuclear planetary model', 'Drawbacks of Rutherford model (electrodynamic orbital collapse)']),
          createTopic('CBSE', '9', 'SCI', '4', '3', 'Bohr Model of Atom & Energy Shells (K, L, M, N)', ['Discrete non-radiating circular orbits', 'Quantum energy transitions']),
          createTopic('CBSE', '9', 'SCI', '4', '4', 'Discovery of Neutrons (James Chadwick, 1932)', ['Charge neutral particle in nucleus with mass equal to proton']),
          createTopic('CBSE', '9', 'SCI', '4', '5', 'Bohr-Bury Rules of Electron Distribution & Valency', ['Max electrons in shell = 2n² (K=2, L=8, M=18, N=32)', 'Octet rule for outermost valence shell', 'Valency definition and determination for first 20 elements']),
          createTopic('CBSE', '9', 'SCI', '4', '6', 'Atomic Number (Z), Mass Number (A), Isotopes & Isobars', ['Z = protons, A = protons + neutrons', 'Isotopes: same Z, different A (fractional atomic mass of Chlorine = 35.5 u)', 'Isobars: same A, different Z (e.g. 40_Ar_18 and 40_Ca_20)', 'Applications of isotopes in nuclear energy, medicine, archaeology'])
        ]
      },
      {
        number: '5',
        name: 'The Fundamental Unit of Life',
        topics: [
          createTopic('CBSE', '9', 'SCI', '5', '1', 'Discovery of Cell & Cell Theory (Hooke, Leeuwenhoek, Schleiden, Schwann, Virchow)', ['Robert Hooke cork cells (1665)', 'Anton van Leeuwenhoek free living cells (1674)', 'Cell Theory postulates (All organisms made of cells, Omnis cellula-e-cellula)']),
          createTopic('CBSE', '9', 'SCI', '5', '2', 'Plasma Membrane: Structure, Diffusion & Osmosis (Hypotonic, Isotonic, Hypertonic)', ['Phospholipid bilayer with proteins', 'Diffusion of gases (CO2, O2)', 'Osmosis across semi-permeable membrane: endosmosis, exosmosis, plasmolysis']),
          createTopic('CBSE', '9', 'SCI', '5', '3', 'Cell Wall, Plasmolysis & Turgidity in Plant Cells', ['Cellulose composition, protection against osmotic burst']),
          createTopic('CBSE', '9', 'SCI', '5', '4', 'Nucleus, Chromosomes, DNA & Prokaryotic vs Eukaryotic Cells', ['Nuclear envelope, nucleoplasm, nucleolus, chromatin threads', 'Chromosomes containing DNA and genes', 'Prokaryotes (nucleoid, 70S ribosomes, no membrane organelles) vs Eukaryotes (true nucleus, 80S ribosomes)']),
          createTopic('CBSE', '9', 'SCI', '5', '5', 'Cytoplasm & Cell Organelles (ER, Golgi, Lysosomes, Mitochondria, Plastids, Vacuoles)', ['Endoplasmic Reticulum (RER & SER membrane biogenesis)', 'Golgi apparatus (packaging and secretor)', 'Lysosomes (digestive enzymes, suicide bags)', 'Mitochondria (cristae, ATP synthesis, own DNA & ribosomes)', 'Plastids (Chloroplasts, Chromoplasts, Leucoplasts)', 'Vacuoles and central sap vacuole in plants'])
        ]
      },
      {
        number: '6',
        name: 'Tissues',
        topics: [
          createTopic('CBSE', '9', 'SCI', '6', '1', 'Plant Tissues: Meristematic Tissues (Apical, Intercalary, Lateral)', ['Characteristics of meristematic cells (dense cytoplasm, prominent nuclei, thin walls)', 'Apical meristem (root and shoot tips length)', 'Intercalary meristem (internode growth)', 'Lateral meristem / cambium (secondary girth growth)']),
          createTopic('CBSE', '9', 'SCI', '6', '2', 'Simple Permanent Plant Tissues (Parenchyma, Collenchyma, Sclerenchyma)', ['Parenchyma (storage, aerenchyma, chlorenchyma)', 'Collenchyma (flexibility and mechanical support, pectin thickening)', 'Sclerenchyma (dead cells with lignin walls, husk of coconut)']),
          createTopic('CBSE', '9', 'SCI', '6', '3', 'Complex Permanent Plant Tissues: Xylem and Phloem', ['Xylem elements: Tracheids, vessels, xylem parenchyma, xylem fibres (unidirectional water transport)', 'Phloem elements: Sieve tubes, companion cells, phloem parenchyma, phloem fibres (bidirectional food translocation)']),
          createTopic('CBSE', '9', 'SCI', '6', '4', 'Animal Tissues: Epithelial Tissues (Squamous, Cuboidal, Columnar, Ciliated, Stratified)', ['Simple squamous (alveoli, blood vessels)', 'Stratified squamous (skin wear and tear)', 'Cuboidal (kidney tubules)', 'Columnar and ciliated columnar (intestine, respiratory tract)']),
          createTopic('CBSE', '9', 'SCI', '6', '5', 'Animal Tissues: Connective Tissues (Blood, Bone, Cartilage, Ligament, Tendon, Areolar, Adipose)', ['Fluid connective tissue: Blood plasma, RBCs, WBCs, platelets', 'Skeletal connective tissues: Bone (calcium-phosphate matrix), Cartilage (chondrocytes, ear/nose tips)', 'Dense connective: Ligaments (bone to bone), Tendons (muscle to bone)', 'Packaging: Areolar and Adipose (fat storage subcutaneous insulator)']),
          createTopic('CBSE', '9', 'SCI', '6', '6', 'Animal Tissues: Muscular Tissue (Striated, Smooth, Cardiac) & Nervous Tissue (Neuron)', ['Striated / skeletal muscle (voluntary, multinucleate, striations)', 'Smooth / involuntary muscle (spindle shaped, unstriated, internal organs)', 'Cardiac muscle (involuntary, branched, uninucleate, intercalated discs)', 'Nervous tissue: Neuron anatomy (cyton/cell body, dendrites, axon, myelin sheath, synapse)'])
        ]
      },
      {
        number: '7',
        name: 'Motion',
        topics: [
          createTopic('CBSE', '9', 'SCI', '7', '1', 'Distance vs Displacement & Uniform vs Non-Uniform Motion', ['Scalar quantity distance vs vector quantity displacement', 'Zero displacement with non-zero distance', 'Equal distances in equal time intervals']),
          createTopic('CBSE', '9', 'SCI', '7', '2', 'Speed, Velocity & Average Speed/Velocity Formulas', ['Speed = Distance / Time (m/s)', 'Velocity = Displacement / Time', 'Average Speed = Total Distance / Total Time', 'Average Velocity = (u + v) / 2 for uniform acceleration']),
          createTopic('CBSE', '9', 'SCI', '7', '3', 'Acceleration (Uniform & Non-Uniform) & Retardation', ['Acceleration formula: a = (v - u) / t', 'SI unit m/s²', 'Deceleration / negative acceleration (retardation)']),
          createTopic('CBSE', '9', 'SCI', '7', '4', 'Graphical Representation: Distance-Time & Velocity-Time Graphs', ['Slope of distance-time graph = Speed', 'Slope of velocity-time graph = Acceleration', 'Area under velocity-time graph = Displacement']),
          createTopic('CBSE', '9', 'SCI', '7', '5', 'Derivation of Three Equations of Motion by Graphical Method', ['First equation: v = u + at', 'Second equation: s = ut + 1/2 * at²', 'Third equation: v² - u² = 2as'], '', ['Equations of Motion']),
          createTopic('CBSE', '9', 'SCI', '7', '6', 'Uniform Circular Motion & Centripetal Acceleration', ['Speed constant but direction continuously changing', 'Formula for circular speed: v = 2πr / T', 'Centripetal acceleration toward center'])
        ]
      },
      {
        number: '8',
        name: 'Force and Laws of Motion',
        topics: [
          createTopic('CBSE', '9', 'SCI', '8', '1', 'Balanced & Unbalanced Forces and Galileo Inclined Plane Experiment', ['Net zero force in balanced system', 'Galileo deduction of inertia of moving bodies']),
          createTopic('CBSE', '9', 'SCI', '8', '2', 'Newton First Law of Motion, Inertia & Mass', ['Statement of first law of motion', 'Mass as quantitative measure of inertia (heavier object = more inertia)'], '', ['Newton First Law of Motion']),
          createTopic('CBSE', '9', 'SCI', '8', '3', 'Momentum (p = mv) & Newton Second Law of Motion (F = ma)', ['Definition of linear momentum and SI unit kg·m/s', 'Mathematical derivation: F = k * d(mv)/dt = ma', 'SI unit Newton (N) = 1 kg·m/s²', 'Applications: cricketer pulling hands back, high jump cushion'], '', ['Newton Second Law of Motion']),
          createTopic('CBSE', '9', 'SCI', '8', '4', 'Newton Third Law of Motion: Action & Reaction Pairs', ['Statement: To every action, there is an equal and opposite reaction', 'Action and reaction act on two different bodies simultaneously', 'Walking, swimming, rocket propulsion, gun recoil'], '', ['Newton Third Law of Motion']),
          createTopic('CBSE', '9', 'SCI', '8', '5', 'Law of Conservation of Linear Momentum & Recoil of Gun', ['Total momentum before collision = Total momentum after collision (m1u1 + m2u2 = m1v1 + m2v2)', 'Recoil velocity of gun formula: V = -(m/M) * v'], '', ['Law of Conservation of Momentum'])
        ]
      },
      {
        number: '9',
        name: 'Gravitation',
        topics: [
          createTopic('CBSE', '9', 'SCI', '9', '1', 'Universal Law of Gravitation & Gravitational Constant (G)', ['Formula: F = G * (m1 * m2) / r²', 'Value and SI unit of G = 6.673 * 10^-11 N·m²/kg² (Cavendish)', 'Importance of universal gravitation (planetary orbits, ocean tides)'], '', ['Universal Law of Gravitation']),
          createTopic('CBSE', '9', 'SCI', '9', '2', 'Free Fall & Acceleration Due to Gravity (g = GM/R²)', ['Free fall definition and independence of falling body mass', 'Calculation of g on Earth surface = 9.8 m/s²', 'Variation of g with altitude, depth, and equator vs poles (g_pole > g_equator)']),
          createTopic('CBSE', '9', 'SCI', '9', '3', 'Motion of Objects Under Gravity (Equations with g)', ['Modifying equations of motion: v = u + gt, h = ut + 1/2*gt², v² - u² = 2gh', 'Sign conventions for upward and downward projectile motion']),
          createTopic('CBSE', '9', 'SCI', '9', '4', 'Mass vs Weight & Weight on the Moon (W_moon = 1/6 * W_earth)', ['Mass is constant scalar quantity (kg)', 'Weight is gravitational force vector W = mg (Newton)', 'Derivation of moon weight being 1/6th of earth weight']),
          createTopic('CBSE', '9', 'SCI', '9', '5', 'Thrust, Pressure, Buoyancy & Archimedes Principle', ['Thrust definition (perpendicular force) and Pressure = Thrust / Area', 'Buoyant upthrust force exerted by liquids', 'Archimedes Principle statement and applications (ships, submarines, hydrometers)', 'Relative density = Density of substance / Density of water'], '', ['Archimedes Principle'])
        ]
      },
      {
        number: '10',
        name: 'Work and Energy',
        topics: [
          createTopic('CBSE', '9', 'SCI', '10', '1', 'Work Done by Constant Force (W = F * s * cosθ)', ['Scientific conception of work', 'Positive work (force along displacement), Negative work (friction opposing motion), Zero work (force perpendicular to displacement)', 'SI unit of work: Joule (1 J = 1 N·m)']),
          createTopic('CBSE', '9', 'SCI', '10', '2', 'Kinetic Energy Formula (KE = 1/2 * m * v²)', ['Definition of kinetic energy', 'Mathematical derivation of KE = 1/2 * m * v²', 'Work-Energy theorem (Work done = Change in KE)']),
          createTopic('CBSE', '9', 'SCI', '10', '3', 'Gravitational Potential Energy Formula (PE = mgh)', ['Energy stored due to change in position or configuration', 'Derivation of PE = mgh above ground reference level']),
          createTopic('CBSE', '9', 'SCI', '10', '4', 'Law of Conservation of Energy & Freely Falling Body Proof', ['Statement: Energy cannot be created nor destroyed, only transformed', 'Mathematical proof that Total Mechanical Energy (KE + PE) is constant at all points of free fall'], '', ['Law of Conservation of Energy']),
          createTopic('CBSE', '9', 'SCI', '10', '5', 'Power: Rate of Doing Work & Commercial Unit (kWh)', ['Power formula P = W / t (Watt, 1 W = 1 J/s)', 'Kilowatt (kW) and Horsepower (1 hp = 746 W)', 'Commercial unit of electrical energy: 1 kWh (Unit) = 3.6 * 10^6 Joules'])
        ]
      },
      {
        number: '11',
        name: 'Sound',
        topics: [
          createTopic('CBSE', '9', 'SCI', '11', '1', 'Production and Propagation of Longitudinal Sound Waves', ['Vibrating tuning fork and propagation through air', 'Compressions (regions of high pressure/density) and Rarefactions (low pressure/density)']),
          createTopic('CBSE', '9', 'SCI', '11', '2', 'Wave Characteristics: Frequency, Wavelength, Amplitude, Speed', ['Wavelength (λ), Frequency (ν = 1/T), Amplitude (A)', 'Wave speed relationship: v = ν * λ', 'Pitch depends on frequency, Loudness depends on amplitude, Quality/Timbre depends on waveform']),
          createTopic('CBSE', '9', 'SCI', '11', '3', 'Speed of Sound in Different Media & Sonic Boom', ['Speed of sound in solids > liquids > gases', 'Temperature dependence of speed of sound (344 m/s at 22°C in air)', 'Supersonic speed and shock wave sonic boom']),
          createTopic('CBSE', '9', 'SCI', '11', '4', 'Reflection of Sound, Echo & Reverberation', ['Laws of reflection of sound', 'Echo condition: Minimum obstacle distance = 17.2 m (persistence of hearing 0.1 s)', 'Reverberation in auditoriums and sound absorbing materials (curtains, compressed fiberboard)']),
          createTopic('CBSE', '9', 'SCI', '11', '5', 'Applications of Ultrasound & SONAR (Sound Navigation and Ranging)', ['Medical echocardiography, ultrasonography, kidney stone breaking', 'Industrial metal flaw detection', 'SONAR depth calculation formula: 2d = v * t'])
        ]
      },
      {
        number: '12',
        name: 'Improvement in Food Resources',
        topics: [
          createTopic('CBSE', '9', 'SCI', '12', '1', 'Crop Variety Improvement & Plant Hybridisation', ['Breeding for higher yield, improved quality, biotic and abiotic resistance, wider adaptability', 'Hybridisation (intervarietal, interspecific, intergeneric) and GM crops']),
          createTopic('CBSE', '9', 'SCI', '12', '2', 'Crop Production Management: Nutrients, Manures & Fertilisers', ['16 essential plant nutrients (Macro vs Micro nutrients)', 'Organic manures (compost, vermicompost, green manure)', 'Chemical fertilisers (NPK hazards on soil microflora)']),
          createTopic('CBSE', '9', 'SCI', '12', '3', 'Irrigation Systems & Cropping Patterns (Mixed, Intercropping, Rotation)', ['Wells, canal systems, river lift systems, tanks', 'Mixed cropping (wheat + gram), Intercropping (soybean + maize), Crop rotation']),
          createTopic('CBSE', '9', 'SCI', '12', '4', 'Crop Protection Management: Weeds, Insect Pests & Diseases', ['Weeds (Xanthium, Parthenium, Cyperinus)', 'Insect pests (chewing, sucking, boring insects)', 'Biopesticides and preventive grain storage measures']),
          createTopic('CBSE', '9', 'SCI', '12', '5', 'Animal Husbandry: Cattle Farming, Poultry, Fish Production & Apiculture', ['Cattle farming: Milk producers (milch) vs Draught animals (Bos indicus, Bos bubalis)', 'Poultry farming: Broilers (meat) vs Layers (eggs)', 'Fish production: Capture fishing, Aquaculture, Composite fish culture (Catla, Rohu, Mrigal, Grass carp)', 'Apiculture: Honey bee varieties (Apis cerana indica, Apis mellifera) and pasturage'])
        ]
      },
      {
        number: '13',
        name: 'Class 7 Science Foundation Core',
        topics: [
          createTopic('CBSE', '9', 'SCI', '13', '1', 'Living World, Cell Biology & Human Body Systems (7th Review)', ['Adaptations in plants and animals across habitats', 'Structure of plant and animal tissues & cell organelles', 'Nutrition, digestive process & respiration in living organisms', 'Circulation and transportation of substances in animals & plants']),
          createTopic('CBSE', '9', 'SCI', '13', '2', 'Motion, Force, Work, Heat & Static Electricity (7th Review)', ['Types of motion: oscillatory, periodic, circular & speed calculations', 'Force, work done & mechanical advantage of simple machines', 'Heat transfer mechanisms (conduction, convection, radiation) & thermometers', 'Static electric charges: frictional electricity, electroscope & lightning phenomena']),
          createTopic('CBSE', '9', 'SCI', '13', '3', 'Properties of Matter, Chemical Changes & Natural Resources (7th Review)', ['Physical vs chemical changes and indicators of chemical reactions', 'Elements, compounds & molecular formulae basics', 'Acids, bases and neutralisation in daily life', 'Natural resources: air, water, soil properties & conservation'])
        ]
      },
      {
        number: '14',
        name: 'Science General Knowledge & Discoveries',
        topics: [
          createTopic('CBSE', '9', 'SCI', '14', '1', 'Indian Scientific Institutions & Space Missions', ['Indian Space Research Organisation (ISRO) & Satish Dhawan Space Centre', 'Key missions: Chandrayaan lunar missions, Mangalyaan Mars Orbiter, Aditya-L1 solar observatory, Gaganyaan', 'Atomic & Defense Research: BARC (Homi Bhabha), DRDO (APJ Abdul Kalam), TIFR, CSIR labs', 'Astronomical facilities in India: GMRT (Pune), IUCAA, ARIES Nainital, Hanle Observatory Ladakh']),
          createTopic('CBSE', '9', 'SCI', '14', '2', 'Famous Scientists, Inventions & Nobel Breakthroughs', ['Eminent Indian scientists: Dr. Homi J. Bhabha, Sir C.V. Raman (Raman Effect), Jagadish Chandra Bose, Srinivasa Ramanujan, Satyendra Nath Bose', 'Global pioneer scientists: Isaac Newton, Albert Einstein, Marie Curie, Galileo Galilei, Michael Faraday, Louis Pasteur, Alexander Fleming', 'Major Nobel Prize winning discoveries in Physics, Chemistry, and Physiology', 'Everyday scientific inventions: light bulb, telephone, x-rays, penicillin, semiconductor transistors, lasers']),
          createTopic('CBSE', '9', 'SCI', '14', '3', 'Environmental Milestones, Biodiversity Treaties & Emerging Science', ['International ecological agreements: Montreal Protocol (ozone protection), Paris Climate Accord, Kyoto Protocol, Ramsar Wetlands Convention', 'India flagship conservation initiatives: Project Tiger, Project Elephant, Devrai sacred groves, Chipko movement', 'Modern science frontiers: Nanotechnology, CRISPR gene editing, Artificial Intelligence in diagnostics, Quantum computing, Renewable green hydrogen'])
        ]
      }
    ]
  },

  // =========================================================================
  // 3. CBSE Class 9: Mathematics - Ganita Manjari (NEP 2020 NCF-SE Curriculum)
  // =========================================================================
  {
    docId: 'cbse_9_mgm',
    board: 'CBSE',
    boardCode: 'CBSE',
    class: '9',
    subject: 'Mathematics (Ganita Manjari)',
    subjectCode: 'MGM',
    chapters: [
      {
        number: '1',
        name: 'Orienting Yourself: The Use of Coordinates',
        topics: [
          createTopic('CBSE', '9', 'MGM', '1', '1', 'Position and Coordinates on a Grid', ['Cartesian coordinate system, origin, X and Y axes', 'Locating objects on grids and map coordinate systems']),
          createTopic('CBSE', '9', 'MGM', '1', '2', 'Quadrants, Signs & Plotting Points', ['Four quadrants and sign conventions (+,+, -,+, -,-, +,-)', 'Plotting coordinates (x, y) with positive and negative numbers', 'Points on axes (x, 0) and (0, y)']),
          createTopic('CBSE', '9', 'MGM', '1', '3', 'Geometric Figures & Distances on Coordinate Grids', ['Drawing geometric shapes using coordinates', 'Measuring horizontal and vertical distances on grid lines'])
        ]
      },
      {
        number: '2',
        name: 'Introduction to Linear Polynomials',
        topics: [
          createTopic('CBSE', '9', 'MGM', '2', '1', 'Expressions to Linear Polynomials in One Variable', ['Variables, constants, coefficients, and degree 1 polynomials', 'Distinction between algebraic expressions and polynomials']),
          createTopic('CBSE', '9', 'MGM', '2', '2', 'Value of a Polynomial & Finding Zeroes', ['Evaluating p(k) for given value k', 'Finding zero of linear polynomial ax + b algebraically']),
          createTopic('CBSE', '9', 'MGM', '2', '3', 'Geometric Interpretation & Straight Line Graphs', ['Graphing linear polynomials y = ax + b', 'Zero as x-intercept of the linear graph'])
        ]
      },
      {
        number: '3',
        name: 'The World of Numbers',
        topics: [
          createTopic('CBSE', '9', 'MGM', '3', '1', 'Rational Numbers & Decimal Representations', ['Definition of rational numbers p/q (q != 0)', 'Terminating vs non-terminating recurring decimal expansions', 'Converting repeating decimals 0.p̄ and 0.pq̄ to fraction form']),
          createTopic('CBSE', '9', 'MGM', '3', '2', 'Irrational Numbers & Geometric Construction on Number Line', ['Non-terminating non-repeating numbers', 'Constructing √2, √3, √5 using Pythagoras spiral method', 'Locating √x on number line']),
          createTopic('CBSE', '9', 'MGM', '3', '3', 'Operations on Real Numbers & Rationalisation of Surds', ['Properties of addition, subtraction, multiplication, division of real numbers', 'Rationalising binomial denominators with conjugate surds 1/(a + √b)']),
          createTopic('CBSE', '9', 'MGM', '3', '4', 'Laws of Exponents for Real Numbers', ['Fractional exponents a^(p/q)', 'Laws of exponents: a^p * a^q = a^(p+q), (a^p)^q = a^(pq), a^p/a^q = a^(p-q), a^p * b^p = (ab)^p'])
        ]
      },
      {
        number: '4',
        name: 'Exploring Algebraic Identities',
        topics: [
          createTopic('CBSE', '9', 'MGM', '4', '1', 'Square Identities & Geometric Proofs', ['Identity I: (a + b)² = a² + 2ab + b²', 'Identity II: (a - b)² = a² - 2ab + b²', 'Identity III: (a + b)(a - b) = a² - b²', 'Geometric area dissections proving identities']),
          createTopic('CBSE', '9', 'MGM', '4', '2', 'Three-Variable Trinomial Squares', ['Expansion: (x + y + z)² = x² + y² + z² + 2xy + 2yz + 2zx', 'Applications in algebraic simplification']),
          createTopic('CBSE', '9', 'MGM', '4', '3', 'Cubic Identities & Factorisation', ['(x ± y)³ = x³ ± y³ ± 3xy(x ± y)', 'x³ + y³ + z³ - 3xyz = (x + y + z)(x² + y² + z² - xy - yz - zx)', 'Conditional identity: If x + y + z = 0, x³ + y³ + z³ = 3xyz']),
          createTopic('CBSE', '9', 'MGM', '4', '4', 'Factorisation using Identities & Splitting Middle Term', ['Factoring quadratic trinomials ax² + bx + c', 'Factoring cubic expressions using trial and factor theorem'])
        ]
      },
      {
        number: '5',
        name: "I'm Up and Down, and Round and Round",
        topics: [
          createTopic('CBSE', '9', 'MGM', '5', '1', 'Periodic Patterns, Rotational & Line Symmetry', ['Rotational symmetry and order of rotation', 'Symmetry axes and cyclic geometric transformations']),
          createTopic('CBSE', '9', 'MGM', '5', '2', 'Circle Geometry: Chords, Arcs & Central Angles', ['Circle elements: Radius, diameter, chord, sector, segment', 'Perpendicular from centre to chord bisects chord', 'Equal chords are equidistant from centre']),
          createTopic('CBSE', '9', 'MGM', '5', '3', 'Inscribed Angles & Cyclic Quadrilaterals', ['Angle subtended by arc at centre is double angle at circumference', 'Angle in a semicircle is 90°', 'Opposite angles of cyclic quadrilateral are supplementary (180°)'])
        ]
      },
      {
        number: '6',
        name: 'Measuring Space: Perimeter and Area',
        topics: [
          createTopic('CBSE', '9', 'MGM', '6', '1', 'Perimeters and Areas of Plane Figures', ['Perimeter and area of rectilinear figures', 'Area formulas for triangles, parallelograms, trapeziums']),
          createTopic('CBSE', '9', 'MGM', '6', '2', 'Heron Formula Derivation & Triangles', ['Semi-perimeter s = (a + b + c) / 2', 'Area formula: A = √[s(s - a)(s - b)(s - c)]', 'Area of equilateral and isosceles triangles']),
          createTopic('CBSE', '9', 'MGM', '6', '3', 'Applications in Finding Areas of Polygons & Land Plots', ['Dividing complex quadrilaterals along diagonals', 'Real-world field and land measurement problems'])
        ]
      },
      {
        number: '7',
        name: 'The Mathematics of Maybe: Introduction to Probability',
        topics: [
          createTopic('CBSE', '9', 'MGM', '7', '1', 'Chance, Uncertainty & Random Experiments', ['Concept of chance and outcome in random events', 'Sample space and elementary events']),
          createTopic('CBSE', '9', 'MGM', '7', '2', 'Empirical vs Theoretical Probability', ['Empirical probability formula: P(E) = Number of trials event occurred / Total trials', 'Theoretical probability P(E) = n(E) / n(S)', 'Probability scale from 0 (impossible) to 1 (certain)']),
          createTopic('CBSE', '9', 'MGM', '7', '3', 'Probability in Daily Life & Simulations', ['Coin tossing, dice rolling, spinning wheels', 'Applications in weather forecasting and decision making'])
        ]
      },
      {
        number: '8',
        name: 'Predicting What Comes Next?: Exploring Sequences and Progressions',
        topics: [
          createTopic('CBSE', '9', 'MGM', '8', '1', 'Number Patterns, Sequences & General Term', ['Identifying numerical and geometric patterns', 'Writing general term rules (nth term an)']),
          createTopic('CBSE', '9', 'MGM', '8', '2', 'Introduction to Arithmetic Progressions (AP)', ['First term a, common difference d', 'General form of AP: a, a+d, a+2d, ...', 'Finding terms in an AP sequence']),
          createTopic('CBSE', '9', 'MGM', '8', '3', 'Geometric Patterns & Real-Life Growth Models', ['Multiplicative sequences and doubling growth', 'Sequences in nature: Fibonacci pattern, tree branching'])
        ]
      },
      {
        number: '9',
        name: 'Propositions and their Converses',
        topics: [
          createTopic('CBSE', '9', 'MGM', '9', '1', 'Mathematical Statements, Axioms & Deductive Logic', ['Statements that are mathematically true or false', 'Axioms, postulates, definitions and theorems']),
          createTopic('CBSE', '9', 'MGM', '9', '2', 'Conditional Statements (If-Then) & Converses', ['Hypothesis and conclusion in implications', 'Formulating converse of a theorem', 'True vs false converses and counterexamples']),
          createTopic('CBSE', '9', 'MGM', '9', '3', 'Direct Proofs & Proof by Contradiction', ['Direct deductive proofs from axioms', 'Indirect proofs (proof by contradiction method)'])
        ]
      },
      {
        number: '10',
        name: 'How Quantities Combine: Understanding Data',
        topics: [
          createTopic('CBSE', '9', 'MGM', '10', '1', 'Data Representation: Bar Graphs & Histograms', ['Grouped frequency distribution tables', 'Constructing bar graphs and uniform histograms', 'Histograms with varying intervals: adjusted frequency']),
          createTopic('CBSE', '9', 'MGM', '10', '2', 'Frequency Polygons & Data Distributions', ['Class marks (Upper limit + Lower limit)/2', 'Constructing frequency polygons with and without histograms']),
          createTopic('CBSE', '9', 'MGM', '10', '3', 'Measures of Central Tendency & Weighted Averages', ['Mean, median, and mode for ungrouped data', 'Weighted arithmetic mean and mixing proportions'])
        ]
      },
      {
        number: '11',
        name: 'The World of Algorithms',
        topics: [
          createTopic('CBSE', '9', 'MGM', '11', '1', 'Step-by-step Algorithms & Flowcharts', ['Definition of algorithm as precise sequence of steps', 'Flowchart symbols and logical decision branching']),
          createTopic('CBSE', '9', 'MGM', '11', '2', 'Division Algorithm & Euclid Subtraction Algorithm for GCD', ['Division algorithm: Dividend = Divisor * Quotient + Remainder', "Euclid's subtraction method for Greatest Common Divisor (GCD/HCF)"]),
          createTopic('CBSE', '9', 'MGM', '11', '3', 'Number Theoretic Algorithms & Prime Testing', ['Sieve of Eratosthenes for prime numbers', 'Algorithms for divisibility tests and prime factorisation'])
        ]
      },
      {
        number: '12',
        name: 'Quadrilaterals',
        topics: [
          createTopic('CBSE', '9', 'MGM', '12', '1', 'Angle Sum Property of a Quadrilateral (360°)', ['Proof that sum of four interior angles of a quadrilateral is 360°']),
          createTopic('CBSE', '9', 'MGM', '12', '2', 'Properties of Parallelograms & Theorems', ['Diagonal divides parallelogram into two congruent triangles', 'Opposite sides and angles are equal theorems', 'Diagonals bisect each other theorem and converses'], '', ['Parallelogram Diagonal Congruence Theorem', 'Parallelogram Diagonals Bisection Theorem']),
          createTopic('CBSE', '9', 'MGM', '12', '3', 'The Midpoint Theorem & Its Converse', ['Segment joining midpoints of two sides of a triangle is parallel to third side and half of it', 'Converse: Line drawn through midpoint of one side parallel to another side bisects third side'], '', ['Midpoint Theorem', 'Converse of Midpoint Theorem'])
        ]
      },
      {
        number: '13',
        name: 'Two Variables, One Line',
        topics: [
          createTopic('CBSE', '9', 'MGM', '13', '1', 'Linear Equation Standard Form: ax + by + c = 0', ['Identifying coefficients a, b, c', 'Expressing word problems as two-variable linear equations']),
          createTopic('CBSE', '9', 'MGM', '13', '2', 'Solutions of Linear Equations in Two Variables', ['Infinitely many solutions property', 'Finding distinct solution pairs (x, y)']),
          createTopic('CBSE', '9', 'MGM', '13', '3', 'Graph of Linear Equations & Intersecting Lines', ['Plotting solutions and drawing straight line graph', 'Equations of lines parallel to axes (x = k, y = k)'])
        ]
      },
      {
        number: '14',
        name: 'Math of Space: Surface Area and Volume',
        topics: [
          createTopic('CBSE', '9', 'MGM', '14', '1', 'Surface Area & Volume of Right Circular Cone', ['Slant height formula: l = √(r² + h²)', 'Curved Surface Area = πrl', 'Total Surface Area = πr(r + l)', 'Volume = 1/3 * πr²h']),
          createTopic('CBSE', '9', 'MGM', '14', '2', 'Surface Area & Volume of Sphere and Hemisphere', ['Surface Area of Sphere = 4πr²', 'Curved Surface Area of Hemisphere = 2πr²', 'Total Surface Area of Hemisphere = 3πr²', 'Volume of Sphere = 4/3 * πr³', 'Volume of Hemisphere = 2/3 * πr³']),
          createTopic('CBSE', '9', 'MGM', '14', '3', 'Composite 3D Solids & Real-World Mensuration', ['Combining cones, cylinders and hemispheres', 'Volume and surface area in practical packaging and engineering'])
        ]
      }
    ]
  },

  // =========================================================================
  // 4. CBSE Class 9: Science - Exploration (NEP 2020 NCF-SE Curriculum)
  // =========================================================================
  {
    docId: 'cbse_9_scie',
    board: 'CBSE',
    boardCode: 'CBSE',
    class: '9',
    subject: 'Science (Exploration)',
    subjectCode: 'SCIE',
    chapters: [
      {
        number: '1',
        name: 'Exploration: Entering the World of Secondary Science',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '1', '1', 'Scientific Method, Inquiry & Observation', ['Formulating hypotheses, designing controlled experiments', 'Qualitative vs quantitative observations, recording scientific data']),
          createTopic('CBSE', '9', 'SCIE', '1', '2', 'Science Tools, Safety & Laboratory Skills', ['Standard laboratory apparatus, hazard symbols and safety precautions', 'SI base and derived units, measurement accuracy and precision'])
        ]
      },
      {
        number: '2',
        name: 'Cell: The Building Block of Life',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '2', '1', 'Discovery of Cell & Cell Theory', ['Robert Hooke cork cells (1665)', 'Anton van Leeuwenhoek free living cells', 'Cell Theory: Schleiden, Schwann, Virchow (Omnis cellula-e-cellula)']),
          createTopic('CBSE', '9', 'SCIE', '2', '2', 'Plasma Membrane: Structure, Diffusion & Osmosis', ['Phospholipid bilayer with embedded proteins', 'Diffusion of gases (CO2, O2)', 'Osmosis across semi-permeable membrane: endosmosis, exosmosis, plasmolysis']),
          createTopic('CBSE', '9', 'SCIE', '2', '3', 'Nucleus, Chromosomes & Cell Organelles', ['Nuclear envelope, nucleolus, chromatin and DNA genes', 'Prokaryotic vs Eukaryotic cell comparison', 'Endoplasmic Reticulum, Golgi apparatus, Lysosomes, Mitochondria, Plastids, Vacuoles'])
        ]
      },
      {
        number: '3',
        name: 'Tissues in Action',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '3', '1', 'Plant Tissues: Meristematic & Simple Permanent', ['Apical, intercalary, lateral meristems (cambium)', 'Parenchyma (storage, aerenchyma, chlorenchyma)', 'Collenchyma (flexibility), Sclerenchyma (lignified walls)']),
          createTopic('CBSE', '9', 'SCIE', '3', '2', 'Complex Plant Tissues: Xylem and Phloem', ['Xylem: Tracheids, vessels, xylem parenchyma, fibres (water transport)', 'Phloem: Sieve tubes, companion cells, phloem parenchyma, fibres (food translocation)']),
          createTopic('CBSE', '9', 'SCIE', '3', '3', 'Animal Tissues: Epithelial, Connective, Muscular & Nervous', ['Epithelial tissues: Squamous, cuboidal, columnar, ciliated', 'Connective tissues: Blood, bone, cartilage, ligaments, tendons, areolar, adipose', 'Muscular tissue: Striated, smooth, cardiac', 'Nervous tissue: Neuron structure (cyton, dendrites, axon, synapse)'])
        ]
      },
      {
        number: '4',
        name: 'Describing Motion Around Us',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '4', '1', 'Distance, Displacement, Speed & Velocity', ['Scalar distance vs vector displacement', 'Uniform vs non-uniform motion', 'Average speed and average velocity formulas']),
          createTopic('CBSE', '9', 'SCIE', '4', '2', 'Acceleration & Graphical Analysis of Motion', ['Acceleration formula: a = (v - u) / t (m/s²)', 'Distance-time graph slope = speed', 'Velocity-time graph slope = acceleration, area under v-t graph = displacement']),
          createTopic('CBSE', '9', 'SCIE', '4', '3', 'Equations of Motion & Circular Motion', ['Graphical derivation: v = u + at, s = ut + 1/2*at², v² - u² = 2as', 'Uniform circular motion and centripetal acceleration (v = 2πr/T)'], '', ['Equations of Motion'])
        ]
      },
      {
        number: '5',
        name: 'Exploring Mixtures and their Separation',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '5', '1', 'Pure Substances, Elements & Compounds', ['Elements: metals, non-metals, metalloids', 'Compounds: fixed mass ratio and chemical bonds', 'Homogeneous vs heterogeneous mixtures']),
          createTopic('CBSE', '9', 'SCIE', '5', '2', 'Solutions, Suspensions & Colloids', ['Solute and solvent, mass percentage concentration', 'Colloidal properties, Tyndall effect, dispersed phase and medium types']),
          createTopic('CBSE', '9', 'SCIE', '5', '3', 'Separation Techniques for Mixtures', ['Evaporation, centrifugation, separating funnel', 'Paper chromatography, simple distillation, fractional distillation for miscible liquids'])
        ]
      },
      {
        number: '6',
        name: 'How Forces Affect Motion',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '6', '1', 'Balanced & Unbalanced Forces and Inertia', ['Net resultant forces', 'Galileo inclined plane experiment and concept of inertia', 'Newton First Law of Motion'], '', ['Newton First Law of Motion']),
          createTopic('CBSE', '9', 'SCIE', '6', '2', 'Momentum & Newton Second Law of Motion', ['Linear momentum p = mv (kg·m/s)', 'Mathematical derivation: F = ma (Newton, N)', 'Impulsive forces in sports and daily life'], '', ['Newton Second Law of Motion']),
          createTopic('CBSE', '9', 'SCIE', '6', '3', 'Newton Third Law & Conservation of Momentum', ['Action and reaction forces acting on distinct bodies', 'Law of conservation of linear momentum: m1u1 + m2u2 = m1v1 + m2v2', 'Recoil of gun and rocket propulsion'], '', ['Newton Third Law of Motion', 'Law of Conservation of Momentum'])
        ]
      },
      {
        number: '7',
        name: 'Work, Energy, and Simple Machines',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '7', '1', 'Work Done by Constant Force', ['Work formula: W = F * s (Joule, 1 J = 1 N·m)', 'Positive, negative, and zero work']),
          createTopic('CBSE', '9', 'SCIE', '7', '2', 'Kinetic and Potential Energy & Conservation Law', ['Kinetic energy formula: KE = 1/2 * m * v²', 'Gravitational potential energy formula: PE = mgh', 'Law of Conservation of Mechanical Energy'], '', ['Law of Conservation of Energy']),
          createTopic('CBSE', '9', 'SCIE', '7', '3', 'Power & Commercial Unit of Energy', ['Power P = W / t (Watt, 1 W = 1 J/s)', 'Commercial electrical energy: 1 kWh = 3.6 * 10^6 Joules', 'Simple machines and mechanical advantage'])
        ]
      },
      {
        number: '8',
        name: 'Journey Inside the Atom',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '8', '1', 'Subatomic Particles: Electrons, Protons & Neutrons', ['J.J. Thomson cathode ray experiments and electron discovery', 'Goldstein canal rays and proton discovery', 'Chadwick neutron discovery in nucleus']),
          createTopic('CBSE', '9', 'SCIE', '8', '2', 'Atomic Models: Thomson, Rutherford & Bohr', ['Thomson plum pudding model', 'Rutherford alpha particle gold foil scattering and nuclear model', 'Bohr planetary model with discrete circular energy orbits (K, L, M, N)']),
          createTopic('CBSE', '9', 'SCIE', '8', '3', 'Bohr-Bury Scheme, Valency, Isotopes & Isobars', ['Electron distribution rules (2n²)', 'Valency for first 20 elements', 'Atomic number (Z) and Mass number (A)', 'Isotopes (same Z, different A) and Isobars (same A, different Z)'])
        ]
      },
      {
        number: '9',
        name: 'Atomic Foundations of Matter',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '9', '1', 'Laws of Chemical Combination', ['Law of Conservation of Mass (Lavoisier)', 'Law of Constant Proportions (Proust)'], '', ['Law of Conservation of Mass', 'Law of Constant Proportions']),
          createTopic('CBSE', '9', 'SCIE', '9', '2', 'Dalton Atomic Theory, Molecules & Radicals', ['Postulates of Dalton atomic theory', 'Molecules of elements and compounds', 'Polyatomic ions and radicals (NH4+, SO4^2-, CO3^2-)']),
          createTopic('CBSE', '9', 'SCIE', '9', '3', 'Writing Chemical Formulae & Molecular Mass', ['Criss-cross valency method for ionic and covalent compounds', 'Calculating molecular mass and formula unit mass in unified atomic mass units (u)'])
        ]
      },
      {
        number: '10',
        name: 'Sound Waves: Characteristics and Applications',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '10', '1', 'Production and Propagation of Sound Waves', ['Vibrating objects as source of sound', 'Longitudinal mechanical waves: compressions and rarefactions', 'Medium necessity (sound cannot travel in vacuum)']),
          createTopic('CBSE', '9', 'SCIE', '10', '2', 'Wave Parameters: Wavelength, Frequency, Amplitude & Speed', ['Wavelength (λ), frequency (ν = 1/T), amplitude (A), wave velocity (v = νλ)', 'Pitch, loudness and timbre/quality', 'Speed of sound in solids, liquids, gases']),
          createTopic('CBSE', '9', 'SCIE', '10', '3', 'Reflection of Sound, Echo, Reverberation & Ultrasound', ['Laws of reflection of sound', 'Echo conditions (minimum 17.2 m)', 'Reverberation and acoustic treatment', 'Ultrasound applications: echocardiography, ultrasonography, SONAR (2d = vt)'])
        ]
      },
      {
        number: '11',
        name: 'Reproduction: How Life Continues',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '11', '1', 'Asexual Reproduction Modes', ['Binary and multiple fission (Amoeba, Plasmodium)', 'Budding (Hydra, Yeast), spore formation, fragmentation', 'Vegetative propagation in plants (cuttings, runners, layering)']),
          createTopic('CBSE', '9', 'SCIE', '11', '2', 'Sexual Reproduction in Flowering Plants', ['Structure of a flower: Sepals, petals, stamens (anther/filament), carpel (stigma/style/ovary)', 'Pollination (self vs cross) and fertilization process', 'Seed and fruit formation']),
          createTopic('CBSE', '9', 'SCIE', '11', '3', 'Human Reproduction & Adolescence', ['Male and female reproductive anatomy overview', 'Puberty, hormonal changes, gamete production', 'Reproductive hygiene and health awareness'])
        ]
      },
      {
        number: '12',
        name: 'Patterns in Life: Diversity and Classification',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '12', '1', 'Basis of Biological Classification', ['Need for classification and hierarchy of taxonomic categories (Kingdom to Species)', 'Binomial nomenclature system (Linnaeus)']),
          createTopic('CBSE', '9', 'SCIE', '12', '2', 'Five Kingdom Classification Overview', ['Kingdom Monera, Protista, Fungi, Plantae, Animalia characteristics', 'Plant kingdom divisions (Thallophyta, Bryophyta, Pteridophyta, Gymnosperms, Angiosperms)', 'Animal kingdom non-chordates and chordates introduction']),
          createTopic('CBSE', '9', 'SCIE', '12', '3', 'Biodiversity & Ecological Balance', ['Significance of biodiversity in ecosystems', 'Threats to biodiversity and national/global conservation measures'])
        ]
      },
      {
        number: '13',
        name: 'Earth as a System: Energy, Matter, and Life',
        topics: [
          createTopic('CBSE', '9', 'SCIE', '13', '1', 'Earth Spheres & Biogeochemical Cycles', ['Atmosphere, hydrosphere, lithosphere, biosphere interactions', 'Water cycle, Nitrogen cycle (fixation, nitrification, denitrification), Carbon cycle']),
          createTopic('CBSE', '9', 'SCIE', '13', '2', 'Atmospheric Dynamics & Greenhouse Effect', ['Role of atmosphere in climate control, winds and rains', 'Greenhouse gases, global warming and ozone layer depletion']),
          createTopic('CBSE', '9', 'SCIE', '13', '3', 'Natural Resources & Sustainable Management', ['Soil erosion, water harvesting and conservation', 'Renewable vs non-renewable energy resources, sustainable development goals'])
        ]
      }
    ]
  }
];

module.exports = { cbse9Subjects };
