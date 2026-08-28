const { createTopic } = require('./helper');

const mh8Subjects = [
  // 1. MH Class 8 Mathematics (MTH)
  {
    docId: 'mh_8_mth',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '8',
    subject: 'Mathematics',
    subjectCode: 'MTH',
    chapters: [
      {
        number: '1',
        name: 'Rational and Irrational Numbers',
        topics: [
          createTopic('MH', '8', 'MTH', '1', '1', 'Rational Numbers & Number Line Representation', ['Definition of rational numbers m/n', 'Plotting fractions and negative rational numbers on number line', 'Equivalent fractions']),
          createTopic('MH', '8', 'MTH', '1', '2', 'Comparison of Rational Numbers', ['Cross multiplication rule (a/b vs c/d)', 'Comparing positive and negative rational numbers']),
          createTopic('MH', '8', 'MTH', '1', '3', 'Decimal Representation of Rational Numbers', ['Terminating decimal form', 'Non-terminating recurring decimal form (dot/bar notation)']),
          createTopic('MH', '8', 'MTH', '1', '4', 'Irrational Numbers & Representation of √2 on Number Line', ['Definition of irrational numbers (non-terminating non-recurring)', 'Geometric construction of √2 and √3 on number line using Pythagoras'])
        ]
      },
      {
        number: '2',
        name: 'Parallel Lines and Transversal',
        topics: [
          createTopic('MH', '8', 'MTH', '2', '1', 'Transversal & Angles Made by Transversal', ['Definition of transversal', 'Pairs of corresponding angles', 'Pairs of alternate interior & alternate exterior angles', 'Pairs of interior angles']),
          createTopic('MH', '8', 'MTH', '2', '2', 'Properties of Angles Formed by Parallel Lines & Transversal', ['Corresponding angles property (equal)', 'Alternate angles property (equal)', 'Interior angles property (supplementary = 180°)'], '', ['Interior Angles Theorem', 'Alternate Angles Theorem']),
          createTopic('MH', '8', 'MTH', '2', '3', 'Construction of Parallel Lines', ['Drawing parallel line through given point outside line using set squares', 'Drawing parallel line at given distance using compass'])
        ]
      },
      {
        number: '3',
        name: 'Indices and Cube Root',
        topics: [
          createTopic('MH', '8', 'MTH', '3', '1', 'Indices Laws with Integer Exponents', ['Product rule a^m * a^n', 'Quotient rule a^m / a^n', 'Power of power (a^m)^n', 'Zero exponent a^0 = 1', 'Negative exponent a^(-m) = 1/a^m']),
          createTopic('MH', '8', 'MTH', '3', '2', 'Meaning of Numbers Having Index in Rational Form (1/n)', ['Meaning of a^(1/n) as nth root of a', 'Reading and writing index forms (e.g. 5th root of 32)']),
          createTopic('MH', '8', 'MTH', '3', '3', 'Meaning of Numbers Having Index in Rational Form (m/n)', ['Meaning of a^(m/n) as mth power of nth root or nth root of mth power', 'Evaluation of fractional indices']),
          createTopic('MH', '8', 'MTH', '3', '4', 'Cube and Cube Root Calculations', ['Finding cube of positive and negative numbers and decimals', 'Finding cube root by prime factorisation method'])
        ]
      },
      {
        number: '4',
        name: 'Altitudes and Medians of a Triangle',
        topics: [
          createTopic('MH', '8', 'MTH', '4', '1', 'Altitude of a Triangle & Orthocentre (O)', ['Definition of altitude', 'Drawing altitudes in acute, right, and obtuse angled triangles', 'Point of concurrence: Orthocentre (O) location']),
          createTopic('MH', '8', 'MTH', '4', '2', 'Median of a Triangle & Centroid (G)', ['Definition of median and midpoint of side', 'Drawing medians of a triangle', 'Point of concurrence: Centroid (G)']),
          createTopic('MH', '8', 'MTH', '4', '3', 'Centroid 2:1 Ratio Property & Numerical Applications', ['Centroid divides each median in the ratio 2:1', 'Calculating segment lengths from centroid property'])
        ]
      },
      {
        number: '5',
        name: 'Expansion Formulae',
        topics: [
          createTopic('MH', '8', 'MTH', '5', '1', 'Expansion of (x + a)(x + b)', ['Formula: (x+a)(x+b) = x² + (a+b)x + ab', 'Application to algebraic and numerical expansions']),
          createTopic('MH', '8', 'MTH', '5', '2', 'Expansion of (a + b)³', ['Formula: (a+b)³ = a³ + 3a²b + 3ab² + b³ = a³ + b³ + 3ab(a+b)', 'Evaluating numerical cubes (e.g. 52³)']),
          createTopic('MH', '8', 'MTH', '5', '3', 'Expansion of (a - b)³', ['Formula: (a-b)³ = a³ - 3a²b + 3ab² - b³ = a³ - b³ - 3ab(a-b)', 'Evaluating numerical cubes (e.g. 48³)']),
          createTopic('MH', '8', 'MTH', '5', '4', 'Expansion of (a + b + c)²', ['Formula: (a+b+c)² = a² + b² + c² + 2ab + 2bc + 2ca', 'Simplification of polynomial expressions'])
        ]
      },
      {
        number: '6',
        name: 'Factorisation of Algebraic Expressions',
        topics: [
          createTopic('MH', '8', 'MTH', '6', '1', 'Factorisation of Quadratic Trinomial (ax² + bx + c)', ['Finding factors by splitting middle term', 'Sign rules in quadratic factorisation']),
          createTopic('MH', '8', 'MTH', '6', '2', 'Factorisation of (a³ + b³)', ['Formula: a³ + b³ = (a + b)(a² - ab + b²)', 'Factoring algebraic binomials']),
          createTopic('MH', '8', 'MTH', '6', '3', 'Factorisation of (a³ - b³)', ['Formula: a³ - b³ = (a - b)(a² + ab + b²)', 'Factoring algebraic expressions with differences of cubes']),
          createTopic('MH', '8', 'MTH', '6', '4', 'Rational Algebraic Expressions Simplification', ['Factorising numerator and denominator', 'Cancelling common polynomial factors'])
        ]
      },
      {
        number: '7',
        name: 'Variation',
        topics: [
          createTopic('MH', '8', 'MTH', '7', '1', 'Direct Variation & Constant of Variation (k)', ['Concept of direct proportion (x ∝ y)', 'Equation of variation x = ky', 'Finding constant of variation k']),
          createTopic('MH', '8', 'MTH', '7', '2', 'Inverse Variation & Constant Product', ['Concept of inverse variation (x ∝ 1/y)', 'Equation xy = k', 'Solving missing values in tables']),
          createTopic('MH', '8', 'MTH', '7', '3', 'Time, Work and Speed Word Problems', ['Man-days calculations', 'Speed and time variations in transportation'])
        ]
      },
      {
        number: '8',
        name: 'Quadrilateral: Constructions and Types',
        topics: [
          createTopic('MH', '8', 'MTH', '8', '1', 'Constructing Quadrilateral with Sides & Angles/Diagonals', ['Construction with 4 sides and 1 diagonal', 'Construction with 3 sides and 2 diagonals', 'Construction with adjacent sides and included angles']),
          createTopic('MH', '8', 'MTH', '8', '2', 'Rectangle & Square Properties and Constructions', ['Opposite sides equal, 90° angles, equal diagonals', 'Square construction with given side length']),
          createTopic('MH', '8', 'MTH', '8', '3', 'Rhombus & Parallelogram Properties and Constructions', ['Rhombus perpendicular bisecting diagonals', 'Parallelogram construction with adjacent sides and included angle']),
          createTopic('MH', '8', 'MTH', '8', '4', 'Trapezium & Kite Properties', ['Trapezium definition and parallel sides', 'Kite adjacent side equality and diagonal properties'])
        ]
      },
      {
        number: '9',
        name: 'Discount and Commission',
        topics: [
          createTopic('MH', '8', 'MTH', '9', '1', 'Discount Calculation on Marked Price', ['Discount = Marked Price - Selling Price', 'Discount % = (Discount / Marked Price) * 100']),
          createTopic('MH', '8', 'MTH', '9', '2', 'Commission & Commission Agent Services', ['Commission definition and rate percent', 'Income calculation of commission agents']),
          createTopic('MH', '8', 'MTH', '9', '3', 'Rebate on Handloom and Khadi Goods', ['Government subsidy and rebate discounts', 'Net amount paid by consumer'])
        ]
      },
      {
        number: '10',
        name: 'Division of Polynomials',
        topics: [
          createTopic('MH', '8', 'MTH', '10', '1', 'Introduction to Polynomials & Degree of Polynomial', ['Definition of polynomial in one variable', 'Degree of monomial and polynomial']),
          createTopic('MH', '8', 'MTH', '10', '2', 'Dividing a Monomial by a Monomial', ['Exponent subtraction in variable division', 'Coefficient division']),
          createTopic('MH', '8', 'MTH', '10', '3', 'Dividing a Polynomial by a Monomial & Binomial', ['Long division algorithm for polynomials', 'Dividend = Divisor * Quotient + Remainder'])
        ]
      },
      {
        number: '11',
        name: 'Statistics',
        topics: [
          createTopic('MH', '8', 'MTH', '11', '1', 'Average / Arithmetic Mean of Ungrouped Data', ['Mean formula: X̄ = Σx / N', 'Weighted mean calculations using frequency tables Σ(f * x) / N']),
          createTopic('MH', '8', 'MTH', '11', '2', 'Subdivided Bar Diagram Construction', ['Subdividing bar heights for multiple component data', 'Scale and labeling on graph']),
          createTopic('MH', '8', 'MTH', '11', '3', 'Percentage Bar Diagram Construction', ['Converting component frequencies to percentages (100%)', 'Constructing percentage bars and comparative analysis'])
        ]
      },
      {
        number: '12',
        name: 'Equations in One Variable',
        topics: [
          createTopic('MH', '8', 'MTH', '12', '1', 'Solving Equations in One Variable by Transposition', ['Adding, subtracting, multiplying, dividing non-zero terms on both sides', 'Solving brackets']),
          createTopic('MH', '8', 'MTH', '12', '2', 'Word Problems on Numbers, Ages, and Currency', ['Formulating linear equations from given conditions', 'Step-by-step verification of solutions'])
        ]
      },
      {
        number: '13',
        name: 'Congruence of Triangles',
        topics: [
          createTopic('MH', '8', 'MTH', '13', '1', 'One-to-One Correspondence & Congruence Concept', ['Vertices correspondence (ABC ↔ PQR)', 'Congruence of corresponding sides and angles']),
          createTopic('MH', '8', 'MTH', '13', '2', 'Tests of Congruence: SAS, SSS, ASA, AAS & Hypotenuse-Side', ['Side-Angle-Side test', 'Side-Side-Side test', 'Angle-Side-Angle & Angle-Angle-Side tests', 'Hypotenuse-Side test for right-angled triangles']),
          createTopic('MH', '8', 'MTH', '13', '3', 'Writing Congruence Proofs & Remaining Congruent Parts', ['Proving triangles congruent by specific test', 'Stating remaining congruent angles and sides'])
        ]
      },
      {
        number: '14',
        name: 'Compound Interest',
        topics: [
          createTopic('MH', '8', 'MTH', '14', '1', 'Compound Interest Formula: A = P(1 + r/100)^N', ['Principal, Rate, Period in years', 'Calculation of total amount A and Interest I = A - P']),
          createTopic('MH', '8', 'MTH', '14', '2', 'Applications of Formula: Population Growth and Depreciation', ['Formula for appreciation: A = P(1 + r/100)^N', 'Formula for depreciation / decay: A = P(1 - r/100)^N'])
        ]
      },
      {
        number: '15',
        name: 'Area',
        topics: [
          createTopic('MH', '8', 'MTH', '15', '1', 'Area of Parallelogram: Base * Height', ['Formula and derivation', 'Finding height or base when area is given']),
          createTopic('MH', '8', 'MTH', '15', '2', 'Area of Rhombus: 1/2 * Product of Diagonals', ['Formula: 1/2 * d1 * d2', 'Pythagoras theorem relation with rhombus sides and half diagonals']),
          createTopic('MH', '8', 'MTH', '15', '3', 'Area of Trapezium: 1/2 * (Sum of Parallel Sides) * Height', ['Formula: 1/2 * (a + b) * h', 'Word problems on cross-sectional canal and road areas']),
          createTopic('MH', '8', 'MTH', '15', '4', 'Area of Triangle with Heron Formula', ['Semi-perimeter s = (a+b+c)/2', 'Formula: A = √[s(s-a)(s-b)(s-c)]']),
          createTopic('MH', '8', 'MTH', '15', '5', 'Area of Irregular Polygons and Field Plots', ['Dividing plots into triangles and trapeziums', 'Summing individual region areas'])
        ]
      },
      {
        number: '16',
        name: 'Surface Area and Volume',
        topics: [
          createTopic('MH', '8', 'MTH', '16', '1', 'Surface Area & Volume of Cuboid and Cube', ['Total surface area = 2(lb + bh + lh)', 'Volume of cuboid = l * b * h', 'TSA of cube = 6l², Volume = l³']),
          createTopic('MH', '8', 'MTH', '16', '2', 'Curved Surface Area & Total Surface Area of Cylinder', ['Curved surface area = 2πrh', 'Total surface area = 2πr(r + h)']),
          createTopic('MH', '8', 'MTH', '16', '3', 'Volume of Cylinder & Capacity in Litres', ['Volume = πr²h', 'Conversion: 1 litre = 1000 cm³, 1 m³ = 1000 litres'])
        ]
      },
      {
        number: '17',
        name: 'Circle: Chord and Arc',
        topics: [
          createTopic('MH', '8', 'MTH', '17', '1', 'Properties of Chord of a Circle', ['Perpendicular drawn from centre to chord bisects chord', 'Segment joining centre and midpoint of chord is perpendicular to chord'], '', ['Perpendicular from centre to chord theorem']),
          createTopic('MH', '8', 'MTH', '17', '2', 'Arcs of a Circle & Measure of Arc', ['Minor arc, Major arc, and Semicircular arc', 'Central angle and measure of minor arc', 'Measure of major arc = 360° - measure of minor arc']),
          createTopic('MH', '8', 'MTH', '17', '3', 'Congruence of Arcs & Corresponding Chords', ['Arcs having equal measures and same radius are congruent', 'Chords corresponding to congruent arcs are congruent'])
        ]
      }
    ]
  },

  // 2. MH Class 8 General Science (SCI)
  {
    docId: 'mh_8_sci',
    board: 'Maharashtra Board',
    boardCode: 'MH',
    class: '8',
    subject: 'General Science',
    subjectCode: 'SCI',
    chapters: [
      {
        number: '1',
        name: 'Living World and Classification of Microbes',
        topics: [
          createTopic('MH', '8', 'SCI', '1', '1', 'Five Kingdom Classification System (Robert Whittaker)', ['Criteria for classification: complexity of cell, body organization, mode of nutrition, life style, phylogenetic relationship', 'Kingdom Monera, Protista, Fungi, Plantae, Animalia']),
          createTopic('MH', '8', 'SCI', '1', '2', 'Characteristics of Kingdom Monera, Protista & Fungi', ['Monera: unicellular prokaryotes (Streptococcus, Clostridium)', 'Protista: unicellular eukaryotes with pseudopodia/cilia (Amoeba, Euglena)', 'Fungi: saprophytic eukaryotes with chitin cell wall (Aspergillus, Penicillium, Yeast)']),
          createTopic('MH', '8', 'SCI', '1', '3', 'Classification of Microorganisms: Bacteria, Protozoa, Fungi, Algae', ['Size hierarchy in micrometres and nanometres', 'Bacteria shapes (coccus, bacillus, spirillum)', 'Protozoa free living and parasitic (Plasmodium, Entamoeba)', 'Algae autotrophs with chloroplast (Chlorella)']),
          createTopic('MH', '8', 'SCI', '1', '4', 'Viruses: Structure, Types & Pathogenicity', ['Submicroscopic size (10 to 100 nm)', 'DNA or RNA genome surrounded by protein coat', 'Bacteriophage and plant/animal viruses'])
        ]
      },
      {
        number: '2',
        name: 'Health and Diseases',
        topics: [
          createTopic('MH', '8', 'SCI', '2', '1', 'Health Definition & Types of Diseases', ['WHO definition of health (physical, mental, and social well-being)', 'Chronic vs acute diseases', 'Hereditary (Down syndrome) vs acquired diseases']),
          createTopic('MH', '8', 'SCI', '2', '2', 'Infectious Diseases & Modes of Transmission', ['Tuberculosis (Mycobacterium tuberculosis, BCG vaccine)', 'Hepatitis/Jaundice (Hepatitis virus)', 'Dysentery, Cholera (Vibrio cholerae), Typhoid (Salmonella typhi)', 'Transmission through air, contaminated water, food, vectors']),
          createTopic('MH', '8', 'SCI', '2', '3', 'Present Day Diseases: Dengue, Swine Flu, Bird Flu, AIDS', ['Dengue (Flavivirus / Aedes aegypti vector, thrombocytopenia)', 'Swine flu (Influenza virus H1N1)', 'AIDS (HIV virus, ELISA test for diagnosis)']),
          createTopic('MH', '8', 'SCI', '2', '4', 'Non-Infectious Diseases: Cancer, Diabetes & Heart Diseases', ['Cancer: uncontrolled cell division, biopsy, chemotherapy, radiation', 'Diabetes: insulin deficiency from pancreas, blood sugar monitoring', 'Heart attack: atherosclerosis, hypertension, angioplasty, bypass surgery']),
          createTopic('MH', '8', 'SCI', '2', '5', 'Generic Medicines & Lifestyle Diseases Prevention', ['Pradhan Mantri Jan Aushadhi Yojana', 'Generic vs branded medicines', 'First aid for heart disease (CPR - Cardio-Pulmonary Resuscitation)'])
        ]
      },
      {
        number: '3',
        name: 'Force and Pressure',
        topics: [
          createTopic('MH', '8', 'SCI', '3', '1', 'Contact and Non-Contact Forces', ['Contact forces: Muscular force, mechanical force, frictional force', 'Non-contact forces: Magnetic, electrostatic, gravitational forces']),
          createTopic('MH', '8', 'SCI', '3', '2', 'Balanced and Unbalanced Forces & Inertia', ['Newton first law of motion and inertia', 'Inertia of rest, inertia of motion, inertia of direction']),
          createTopic('MH', '8', 'SCI', '3', '3', 'Pressure Formula (P = F/A) & Pressure on Solids', ['Definition of pressure and SI unit N/m² (Pascal)', 'Effect of contact area on pressure (pins, heavy vehicle tires)']),
          createTopic('MH', '8', 'SCI', '3', '4', 'Pressure of Liquids and Gases', ['Liquid pressure formula (P = hρg) and depth dependence', 'Atmospheric pressure (1 bar = 10^5 Pa) and decrease with altitude']),
          createTopic('MH', '8', 'SCI', '3', '5', 'Buoyant Force & Archimedes Principle', ['Factors affecting buoyant force: volume of submerged object and density of liquid', 'Archimedes principle statement and applications', 'Law of flotation and relative density (hydrometer, lactometer)'])
        ]
      },
      {
        number: '4',
        name: 'Current Electricity and Magnetism',
        topics: [
          createTopic('MH', '8', 'SCI', '4', '1', 'Current Electricity & Electrostatic Potential', ['Flow of electrons in conductors', 'Electric potential definition and potential difference (V)', 'Unit of potential difference (Volt) and electric current (Ampere)']),
          createTopic('MH', '8', 'SCI', '4', '2', 'Dry Cell, Lead-Acid Cell & Ni-Cd Cells', ['Dry cell construction: zinc container cathode, carbon rod anode, ammonium chloride & manganese dioxide paste', 'Lead-acid cell: Pb and PbO2 electrodes in dilute H2SO4 (rechargeable)', 'Ni-Cd cells and lithium-ion cells']),
          createTopic('MH', '8', 'SCI', '4', '3', 'Electric Circuit Components & Symbols', ['Connecting wires, battery, plug key, bulb, ammeter, voltmeter']),
          createTopic('MH', '8', 'SCI', '4', '4', 'Magnetic Effect of Electric Current (Hans Christian Oersted)', ['Deflection of magnetic needle around current carrying conductor', 'Right hand thumb rule basics']),
          createTopic('MH', '8', 'SCI', '4', '5', 'Electromagnet Construction & Electric Bell Working', ['Winding insulated copper wire around iron nail', 'Electric bell circuit, striker, gong, and contact screw mechanism'])
        ]
      },
      {
        number: '5',
        name: 'Inside the Atom',
        topics: [
          createTopic('MH', '8', 'SCI', '5', '1', 'Dalton Atomic Theory & Thomson Plum Pudding Model', ['Dalton: hard indivisible spheres', 'Thomson: positively charged sphere with embedded negatively charged electrons (cathode ray discovery)']),
          createTopic('MH', '8', 'SCI', '5', '2', 'Rutherford Gold Foil Experiment & Nuclear Model of Atom', ['Alpha particle scattering experiment', 'Positively charged dense central nucleus, empty space around nucleus, planetary electrons', 'Drawbacks of Rutherford model (stability of orbital electrons)']),
          createTopic('MH', '8', 'SCI', '5', '3', 'Bohr Stable Orbit Atomic Model', ['Electrons revolve in discrete stable circular orbits (K, L, M, N shells)', 'Energy emission and absorption during quantum electron jumps']),
          createTopic('MH', '8', 'SCI', '5', '4', 'Subatomic Particles: Protons (p), Neutrons (n), Electrons (e)', ['Proton: positive charge in nucleus (1.6 * 10^-19 C)', 'Neutron: electrically neutral particle (James Chadwick, 1932)', 'Electron: negatively charged particle with negligible mass (1/1837 of H atom)']),
          createTopic('MH', '8', 'SCI', '5', '5', 'Atomic Number (Z), Mass Number (A) & Electronic Configuration', ['Atomic number Z = number of protons = number of electrons', 'Mass number A = protons + neutrons', 'Shell capacity formula 2n² (K=2, L=8, M=18, N=32)', 'Valence electrons and valency determination']),
          createTopic('MH', '8', 'SCI', '5', '6', 'Isotopes & Uses of Radioactive Isotopes', ['Definition: same atomic number Z, different mass number A (e.g. C-12, C-14; H-1, H-2, H-3)', 'Uses: Uranium-235 in nuclear reactors, Cobalt-60 in cancer therapy, Iodine-131 in goitre, Carbon-14 dating'])
        ]
      },
      {
        number: '6',
        name: 'Composition of Matter',
        topics: [
          createTopic('MH', '8', 'SCI', '6', '1', 'States of Matter: Solid, Liquid, Gas (Intermolecular Forces)', ['Intermolecular forces of attraction and particle spacing', 'Definite shape, volume, rigidity, fluidity, compressibility comparison']),
          createTopic('MH', '8', 'SCI', '6', '2', 'Elements, Compounds and Mixtures', ['Element: purest substance consisting of single type of atom', 'Compound: chemical combination of elements in fixed proportion by weight', 'Mixture: physical combination of substances in any proportion']),
          createTopic('MH', '8', 'SCI', '6', '3', 'Types of Mixtures: Homogeneous vs Heterogeneous', ['Homogeneous mixture: uniform composition throughout (solutions)', 'Heterogeneous mixture: non-uniform composition (suspensions, colloids)']),
          createTopic('MH', '8', 'SCI', '6', '4', 'Solutions, Suspensions and Colloids (Tyndall Effect)', ['Solution: solute and solvent, true solution particle size < 1 nm', 'Suspension: heterogeneous mixture particle size > 1000 nm, settles on standing', 'Colloid: particle size 1 to 1000 nm, Tyndall scattering of light (milk, ink, smoke)']),
          createTopic('MH', '8', 'SCI', '6', '5', 'Molecular Formula & Valency (Cross-Over Method)', ['Writing chemical formulae using constituent elements and valency cross-over technique'])
        ]
      },
      {
        number: '7',
        name: 'Metals and Non-metals',
        topics: [
          createTopic('MH', '8', 'SCI', '7', '1', 'Physical Properties of Metals', ['Lustre, hardness, malleability, ductility, conduction of heat and electricity, sonority, high density and melting points', 'Exceptions: Mercury and Gallium (liquids), Sodium and Potassium (soft, low density)']),
          createTopic('MH', '8', 'SCI', '7', '2', 'Physical Properties of Non-metals', ['Non-lustrous, brittle, poor conductors of heat and electricity', 'Exceptions: Diamond (hardest substance, good heat conductor), Graphite (good electric conductor), Iodine (lustrous)']),
          createTopic('MH', '8', 'SCI', '7', '3', 'Chemical Properties of Metals (Oxides, Water, Acids)', ['Reaction with oxygen: basic metal oxides', 'Reaction with water: metal hydroxides and hydrogen gas', 'Reaction with dilute acids: salt and hydrogen gas evolution']),
          createTopic('MH', '8', 'SCI', '7', '4', 'Chemical Properties of Non-metals (Oxides, Water, Acids)', ['Reaction with oxygen: acidic or neutral non-metal oxides (CO2, SO2)', 'Non-metals generally do not react with dilute acids']),
          createTopic('MH', '8', 'SCI', '7', '5', 'Uses of Metals/Non-metals, Noble Metals, Corrosion & Alloys', ['Noble metals: Gold, Silver, Platinum, Palladium and purity in Carats (24K, 22K)', 'Corrosion: Rusting of iron, green patina on copper, tarnishing of silver', 'Alloys: Brass (Cu+Zn), Bronze (Cu+Sn), Stainless Steel (Fe+C+Cr+Ni)'])
        ]
      },
      {
        number: '8',
        name: 'Pollution',
        topics: [
          createTopic('MH', '8', 'SCI', '8', '1', 'Pollution & Pollutants (Natural vs Man-made)', ['Definition of pollution and degradable vs non-degradable pollutants']),
          createTopic('MH', '8', 'SCI', '8', '2', 'Air Pollution: Causes, Pollutants & Effects', ['Pollutants: SO2, CO, NO, particulate matter (PM), lead compounds', 'Acid rain (formation of H2SO4 and HNO3) and corrosion of historical monuments (Taj Mahal)', 'Greenhouse effect and global warming']),
          createTopic('MH', '8', 'SCI', '8', '3', 'Water Pollution: Biological, Inorganic & Organic Pollutants', ['Domestic sewage, industrial effluents, agricultural pesticides and fertilisers', 'Eutrophication and depletion of dissolved oxygen (BOD)', 'Water-borne diseases (Typhoid, Jaundice, Amoebiasis)']),
          createTopic('MH', '8', 'SCI', '8', '4', 'Soil Pollution: Causes & Preventive Measures', ['Chemical fertilisers, plastic waste, radioactive fallout, saline soil', 'Solid waste management and organic farming methods'])
        ]
      },
      {
        number: '9',
        name: 'Disaster Management',
        topics: [
          createTopic('MH', '8', 'SCI', '9', '1', 'Earthquakes: Causes, Effects & Seismometer', ['Underground tectonic plate stress release', 'Seismometer and Richter scale measurement', 'Precautionary measures during earthquake']),
          createTopic('MH', '8', 'SCI', '9', '2', 'Fire: Types of Fire (Class A, B, C, D, E) & Fire Extinguishers', ['Class A (solid fires - wood, paper)', 'Class B (liquid fires - petrol, kerosene)', 'Class C (gas fires - LPG, methane)', 'Class D (combustible metal fires - Na, Mg)', 'Class E (electrical fires)', 'Fire extinguishers: CO2, dry powder, foam']),
          createTopic('MH', '8', 'SCI', '9', '3', 'Landslides / Rifts: Causes, Effects & Disaster Management Authority', ['Heavy rainfall, deforestation, excavation on mountain slopes', 'Malin landslide case study in Maharashtra', 'Disaster rescue techniques and first aid mock drills'])
        ]
      },
      {
        number: '10',
        name: 'Cell and Cell Organelles',
        topics: [
          createTopic('MH', '8', 'SCI', '10', '1', 'Cell Structure & Plant vs Animal Cell Comparison', ['Cell wall (cellulose in plant cells)', 'Plasma membrane: selectively permeable fluid-mosaic structure', 'Cytoplasm and cytosol']),
          createTopic('MH', '8', 'SCI', '10', '2', 'Nucleus & Endoplasmic Reticulum (Rough & Smooth)', ['Nucleus: nuclear membrane, nucleolus, chromatin network, genetic control', 'Endoplasmic Reticulum: RER with ribosomes (protein synthesis) and SER (lipid synthesis)']),
          createTopic('MH', '8', 'SCI', '10', '3', 'Golgi Complex & Lysosomes (Suicide Bags)', ['Golgi complex: cisternae, packaging and secretory organelle (Camillo Golgi)', 'Lysosomes: digestive hydrolytic enzymes, autolysis (suicide bags)']),
          createTopic('MH', '8', 'SCI', '10', '4', 'Mitochondria (Powerhouse of the Cell) & Plastids', ['Mitochondria: double membrane, cristae, matrix, ATP synthesis', 'Plastids: Chloroplasts (photosynthesis), Chromoplasts (colored pigments), Leucoplasts (storage)']),
          createTopic('MH', '8', 'SCI', '10', '5', 'Vacuoles & Cell Osmoregulation', ['Single membrane tonoplast in plant cell', 'Storage of water, sap, excretory substances'])
        ]
      },
      {
        number: '11',
        name: 'Human Body and Organ System',
        topics: [
          createTopic('MH', '8', 'SCI', '11', '1', 'Human Respiratory System Anatomy & Mechanism', ['Nose, pharynx, larynx (sound box), trachea (windpipe), bronchi, bronchioles, alveoli', 'Mechanism of breathing: Diaphragm and intercostal muscle movement']),
          createTopic('MH', '8', 'SCI', '11', '2', 'Gas Exchange in Alveoli & Cellular Respiration', ['Diffusion of oxygen and carbon dioxide across alveolar-capillary membrane', 'Aerobic breakdown of glucose to generate ATP']),
          createTopic('MH', '8', 'SCI', '11', '3', 'Human Circulatory System: Heart Anatomy & Pumping Cycle', ['Four chambers: Right and left atria, right and left ventricles', 'Pericardium membrane, valves (tricuspid, bicuspid/mitral, semilunar)', 'Systole and diastole pumping cycle']),
          createTopic('MH', '8', 'SCI', '11', '4', 'Blood Vessels: Arteries, Veins and Capillaries', ['Arteries: thick muscular walls, high pressure, no valves, carry oxygenated blood (except pulmonary artery)', 'Veins: thin walls, valves present, carry deoxygenated blood (except pulmonary vein)', 'Capillaries: single-cell thick endothelial layer for nutrient and gas exchange']),
          createTopic('MH', '8', 'SCI', '11', '5', 'Blood Composition, Blood Groups (ABO & Rh) & Blood Pressure', ['Plasma (55%) and formed elements (RBCs with hemoglobin, WBCs, platelets)', 'ABO blood groups (Karl Landsteiner) and Universal donor (O-) / recipient (AB+)', 'Sphygmomanometer blood pressure measurement (Normal 120/80 mmHg)'])
        ]
      },
      {
        number: '12',
        name: 'Introduction to Acid and Base',
        topics: [
          createTopic('MH', '8', 'SCI', '12', '1', 'Acids: Definition, Natural vs Mineral Acids & Properties', ['Sour taste, produces H+ ions in aqueous solution, turns blue litmus red', 'Natural organic acids (citric acid in lemon, tartaric acid in tamarind, lactic acid in curd, acetic acid in vinegar)', 'Mineral acids (HCl, H2SO4, HNO3)']),
          createTopic('MH', '8', 'SCI', '12', '2', 'Bases / Alkalis: Properties & Uses', ['Bitter taste, soapy touch, produces OH- ions in water, turns red litmus blue', 'Common bases: NaOH, KOH, Ca(OH)2 (slaked lime), Mg(OH)2 (antacid)']),
          createTopic('MH', '8', 'SCI', '12', '3', 'Indicators: Natural & Synthetic (Litmus, Phenolphthalein, Methyl Orange)', ['Natural indicators: Litmus (lichen extract), turmeric paper, red cabbage juice', 'Synthetic indicators: Phenolphthalein (colorless in acid, pink in base), Methyl orange (pink in acid, yellow in base)']),
          createTopic('MH', '8', 'SCI', '12', '4', 'Neutralisation Reaction & Industrial Applications', ['Acid + Base → Salt + Water (HCl + NaOH → NaCl + H2O)', 'Antacids for hyperacidity, lime application to acidic agricultural soil, treating alkaline industrial waste'])
        ]
      },
      {
        number: '13',
        name: 'Chemical Change and Chemical Bond',
        topics: [
          createTopic('MH', '8', 'SCI', '13', '1', 'Physical vs Chemical Changes & Indicators of Chemical Reaction', ['Reversible vs irreversible transformations', 'Change in color, evolution of gas, temperature change, precipitate formation']),
          createTopic('MH', '8', 'SCI', '13', '2', 'Natural Chemical Changes (Respiration, Photosynthesis, Rusting)', ['Photosynthesis: 6CO2 + 6H2O → C6H12O6 + 6O2', 'Respiration: C6H12O6 + 6O2 → 6CO2 + 6H2O + Energy', 'Rusting of iron in moist air']),
          createTopic('MH', '8', 'SCI', '13', '3', 'Man-Made Chemical Changes (Combustion, Effervescence, Bleaching)', ['Combustion of fuels', 'Cleaning tiles with hydrochloric acid', 'Softening hard water']),
          createTopic('MH', '8', 'SCI', '13', '4', 'Chemical Bonds: Ionic (Electrovalent) Bond Formation', ['Transfer of electrons from metal to non-metal to achieve stable octet', 'Formation of NaCl (Na+ and Cl-), MgCl2, CaO']),
          createTopic('MH', '8', 'SCI', '13', '5', 'Covalent Bond Formation (Single, Double & Triple Bonds)', ['Sharing of electron pairs between non-metallic atoms', 'Formation of H2, Cl2 (single bond), O2 (double bond), N2 (triple bond), H2O, CH4'])
        ]
      },
      {
        number: '14',
        name: 'Measurement and Effects of Heat',
        topics: [
          createTopic('MH', '8', 'SCI', '14', '1', 'Heat vs Temperature & Kinetic Theory of Heat', ['Heat as form of total kinetic energy (Joules / Calories)', 'Temperature as average kinetic energy of molecules (Degree Celsius, Kelvin, Fahrenheit)']),
          createTopic('MH', '8', 'SCI', '14', '2', 'Thermometer Types (Clinical, Laboratory, Maximum-Minimum)', ['Mercury and alcohol thermometers', 'Clinical thermometer range (35°C to 42°C) with constriction kink', 'Digital and infrared thermometers']),
          createTopic('MH', '8', 'SCI', '14', '3', 'Specific Heat Capacity & Calorimeter', ['Specific heat definition (c)', 'Heat absorbed or lost formula: Q = m * c * ΔT', 'Principle of heat exchange in copper calorimeter']),
          createTopic('MH', '8', 'SCI', '14', '4', 'Thermal Expansion of Solids (Linear, Areal, Volumetric)', ['Linear expansion coefficient (λ): Δl = l1 * λ * ΔT', 'Superficial / areal expansion (β) and cubical / volumetric expansion (γ)', 'Gaps in railway tracks and bi-metallic strips']),
          createTopic('MH', '8', 'SCI', '14', '5', 'Thermal Expansion of Liquids and Gases', ['Apparent vs real expansion of liquids', 'Expansion of gases under constant pressure'])
        ]
      },
      {
        number: '15',
        name: 'Sound',
        topics: [
          createTopic('MH', '8', 'SCI', '15', '1', 'Production & Propagation of Sound (Compressions & Rarefactions)', ['Vibration of tuning fork prongs', 'Longitudinal sound waves: high pressure compressions and low pressure rarefactions']),
          createTopic('MH', '8', 'SCI', '15', '2', 'Frequency, Wavelength & Velocity of Sound (v = ν * λ)', ['Frequency (Hz), Wavelength (λ in metres), Amplitude, Time period (T)', 'Wave equation: Velocity = Frequency * Wavelength']),
          createTopic('MH', '8', 'SCI', '15', '3', 'Human Vocal Cords & Sound Generation', ['Larynx structure, vocal cord tension adjustment during speech and singing']),
          createTopic('MH', '8', 'SCI', '15', '4', 'Human Ear Structure & Auditory Pathway', ['Pinna, auditory canal, tympanic membrane, malleus, incus, stapes bones, cochlea, auditory nerve']),
          createTopic('MH', '8', 'SCI', '15', '5', 'Noise Pollution, Decibel Scale & Protective Measures', ['Threshold of hearing (0 dB), Normal conversation (60 dB), Noise threshold (>80 dB)', 'Acoustic insulation, tree plantation, silencers in machinery'])
        ]
      },
      {
        number: '16',
        name: 'Reflection of Light',
        topics: [
          createTopic('MH', '8', 'SCI', '16', '1', 'Laws of Reflection of Light', ['Incident ray, reflected ray, normal to reflecting surface', 'Angle of incidence (i) = Angle of reflection (r)', 'Coplanar property of rays']),
          createTopic('MH', '8', 'SCI', '16', '2', 'Regular vs Irregular (Diffused) Reflection', ['Parallel incident rays on smooth vs rough surfaces', 'Visibility of non-luminous objects']),
          createTopic('MH', '8', 'SCI', '16', '3', 'Reflection of Reflected Light & Periscope', ['Successive reflections from two parallel or inclined mirrors', 'Periscope construction and applications in submarines']),
          createTopic('MH', '8', 'SCI', '16', '4', 'Multiple Images & Kaleidoscope', ['Formula for number of images: n = (360° / A) - 1', 'Kaleidoscope three rectangular mirror strips at 60°']),
          createTopic('MH', '8', 'SCI', '16', '5', 'Sunlight: White Light Dispersion & Rainbow Formation', ['Newton disc experiment', 'Seven spectrum colors (VIBGYOR)'])
        ]
      },
      {
        number: '17',
        name: 'Man Made Materials',
        topics: [
          createTopic('MH', '8', 'SCI', '17', '1', 'Plastic: Types (Thermoplastics vs Thermosetting Plastics)', ['Thermoplastics: reshaped on heating (Polythene, PVC, Polystyrene)', 'Thermosetting plastics: permanently hardened on heating (Bakelite, Melamine, Formica)']),
          createTopic('MH', '8', 'SCI', '17', '2', 'Plastic and Environment: 4R Principle', ['Non-biodegradable pollution hazard', '4R Principle: Reduce, Reuse, Recycle, Recover']),
          createTopic('MH', '8', 'SCI', '17', '3', 'Thermocol (Polystyrene) Properties and Hazards', ['Thermal insulation and shock absorption packaging uses', 'Carcinogenic styrene vapors on burning, disposal issues']),
          createTopic('MH', '8', 'SCI', '17', '4', 'Glass: Composition, Types and Manufacturing', ['Raw materials: Silica (SiO2), soda, limestone', 'Types: Soda-lime glass, Borosilicate (Pyrex) glass, Silica glass, Optical glass, Colored glass, Toughened / safety glass'])
        ]
      },
      {
        number: '18',
        name: 'Ecosystems',
        topics: [
          createTopic('MH', '8', 'SCI', '18', '1', 'Structure of Ecosystem: Biotic and Abiotic Factors', ['Abiotic factors: Air, water, soil, sunlight, temperature, minerals', 'Biotic factors: Producers (autotrophs), Consumers (herbivores, carnivores, omnivores), Decomposers (bacteria, fungi)']),
          createTopic('MH', '8', 'SCI', '18', '2', 'Types of Ecosystems: Terrestrial & Aquatic', ['Terrestrial ecosystems: Forest, grassland, evergreen, desert ecosystems', 'Aquatic ecosystems: Freshwater (river, pond, lake) and Marine (ocean, estuary) ecosystems']),
          createTopic('MH', '8', 'SCI', '18', '3', 'Biomes & Ecosystem Degradation Due to Human Activities', ['Global biomes distribution', 'Dam construction, deforestation, urbanization, industrialization impact', 'Ecosystem conservation initiatives'])
        ]
      },
      {
        number: '19',
        name: 'Life Cycle of Stars',
        topics: [
          createTopic('MH', '8', 'SCI', '19', '1', 'Properties of the Sun and Stars', ['Composition (Hydrogen, Helium), Mass, Radius, Surface temperature', 'Units: Light year, Astronomical Unit (AU)']),
          createTopic('MH', '8', 'SCI', '19', '2', 'Birth of Stars: Interstellar Clouds & Protostars', ['Gravitational contraction of hydrogen and dust clouds', 'Nuclear fusion trigger (4 Hydrogen → 1 Helium + Energy)']),
          createTopic('MH', '8', 'SCI', '19', '3', 'Evolution of Stars (Low Mass vs High Mass Stars)', ['Main sequence equilibrium (Gas pressure vs Gravity)', 'Red giant stage expansion']),
          createTopic('MH', '8', 'SCI', '19', '4', 'End Stages of Stars: White Dwarf, Neutron Star & Black Hole', ['Chandrasekhar Limit (1.4 Solar Masses)', 'Low mass stars end as White Dwarf and Planetary Nebula', 'Massive stars undergo Supernova explosion ending as Neutron Star or Black Hole'])
        ]
      }
    ]
  }
];

module.exports = { mh8Subjects };
