const { createTopic } = require('./helper');

const cbse9Subjects = [
  // =========================================================================
  // 1. CBSE Class 9: Mathematics - Ganita Manjari (NEP 2020 NCF-SE Curriculum)
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
  // 2. CBSE Class 9: Science - Exploration (NEP 2020 NCF-SE Curriculum)
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
