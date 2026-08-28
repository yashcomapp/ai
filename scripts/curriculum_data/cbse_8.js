const { createTopic } = require('./helper');

const cbse8Subjects = [
  // 1. Ganit Prakash Part 1 (MGP1)
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
  },

  // 2. Ganit Prakash Part 2 (MGP2)
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
  },

  // 3. Curiosity Science (CURI)
  {
    docId: 'cbse_8_curi',
    board: 'CBSE',
    boardCode: 'CBSE',
    class: '8',
    subject: 'Curiosity Science',
    subjectCode: 'CURI',
    chapters: [
      {
        number: '1',
        name: 'Crop Production and Management',
        topics: [
          createTopic('CBSE', '8', 'CURI', '1', '1', 'Agricultural Practices: Kharif vs Rabi Crops', ['Definition of crop', 'Kharif crops (sown in rainy season e.g. paddy, maize)', 'Rabi crops (sown in winter season e.g. wheat, gram, pea)']),
          createTopic('CBSE', '8', 'CURI', '1', '2', 'Soil Preparation, Ploughing & Sowing Methods', ['Tilling and ploughing tools (plough, hoe, cultivator)', 'Selection of healthy seeds', 'Traditional tools vs modern seed drills']),
          createTopic('CBSE', '8', 'CURI', '1', '3', 'Adding Manure and Fertilisers & Crop Rotation', ['Organic manure vs chemical fertilisers (NPK, Urea)', 'Advantages of manure on soil texture and water retention', 'Crop rotation and leguminous plants with Rhizobium']),
          createTopic('CBSE', '8', 'CURI', '1', '4', 'Irrigation Systems: Traditional vs Modern (Drip & Sprinkler)', ['Traditional methods (moat, chain pump, dheli, rahat)', 'Sprinkler system for uneven land', 'Drip system for water conservation in arid regions']),
          createTopic('CBSE', '8', 'CURI', '1', '5', 'Protection from Weeds, Harvesting, Threshing & Storage', ['Weeds and weedicides (e.g. 2,4-D)', 'Harvesting tools (sickle, combine harvester)', 'Threshing and winnowing', 'Grain silos, granaries, and buffer stock storage'])
        ]
      },
      {
        number: '2',
        name: 'Microorganisms: Friend and Foe',
        topics: [
          createTopic('CBSE', '8', 'CURI', '2', '1', 'Classification of Microorganisms & Habitats', ['Bacteria, Fungi, Protozoa, Algae', 'Viruses: obligate intracellular nature', 'Habitats: ice cold to hot springs, desert to marshy land']),
          createTopic('CBSE', '8', 'CURI', '2', '2', 'Friendly Microbes: Food Production, Fermentation & Antibiotics', ['Lactobacillus in curd and cheese', 'Yeast in bread and alcohol fermentation', 'Commercial antibiotics (Penicillin, Streptomycin, Tetracycline)', 'Vaccine production and antibodies']),
          createTopic('CBSE', '8', 'CURI', '2', '3', 'Harmful Microorganisms: Human, Plant & Animal Diseases', ['Communicable diseases and pathogen modes of transmission', 'Carriers: Female Anopheles (Malaria), Aedes (Dengue)', 'Plant diseases: Citrus canker, Rust of wheat, Yellow vein mosaic', 'Anthrax disease in animals']),
          createTopic('CBSE', '8', 'CURI', '2', '4', 'Food Preservation Methods & Pasteurisation', ['Chemical preservatives (sodium benzoate, metabisulphite)', 'Common salt, sugar, oil, and vinegar preservation', 'Heat and cold treatments', 'Pasteurisation method (Louis Pasteur)']),
          createTopic('CBSE', '8', 'CURI', '2', '5', 'Nitrogen Fixation & the Nitrogen Cycle', ['Atmospheric nitrogen fixation by Rhizobium & blue-green algae', 'Lightning nitrogen fixation', 'Nitrification, assimilation, and denitrification steps in nitrogen cycle'])
        ]
      },
      {
        number: '3',
        name: 'Coal and Petroleum',
        topics: [
          createTopic('CBSE', '8', 'CURI', '3', '1', 'Exhaustible vs Inexhaustible Natural Resources', ['Inexhaustible resources (sunlight, air)', 'Exhaustible resources (coal, petroleum, minerals)']),
          createTopic('CBSE', '8', 'CURI', '3', '2', 'Coal: Carbonisation, Coke, Coal Tar and Coal Gas', ['Formation of coal from dead vegetation (Carbonisation)', 'Coke properties and uses in steel extraction', 'Coal tar and chemical products', 'Coal gas as industrial fuel']),
          createTopic('CBSE', '8', 'CURI', '3', '3', 'Petroleum: Refining & Fractional Distillation Products', ['Formation and drilling of petroleum oil', 'Fractional distillation column', 'Fractions: Petrol, Diesel, Kerosene, LPG, Lubricating oil, Paraffin wax, Bitumen']),
          createTopic('CBSE', '8', 'CURI', '3', '4', 'Natural Gas (CNG) & Conservation of Fossil Fuels', ['Compressed Natural Gas advantages and pipeline network', 'PCRA tips for saving petrol and diesel'])
        ]
      },
      {
        number: '4',
        name: 'Combustion and Flame',
        topics: [
          createTopic('CBSE', '8', 'CURI', '4', '1', 'Combustion Definition & Essential Conditions for Burning', ['Combustible vs non-combustible substances', 'Presence of oxygen/air necessity', 'Ignition temperature definition']),
          createTopic('CBSE', '8', 'CURI', '4', '2', 'Types of Combustion: Rapid, Spontaneous & Explosion', ['Rapid combustion (LPG burner)', 'Spontaneous combustion (white phosphorus, coal dust)', 'Explosion (fireworks, sudden gas expansion)']),
          createTopic('CBSE', '8', 'CURI', '4', '3', 'Structure of a Candle Flame (Three Zones)', ['Innermost dark zone (unburnt wax vapors)', 'Middle luminous yellow zone (incomplete combustion)', 'Outermost non-luminous blue zone (complete combustion & hottest)']),
          createTopic('CBSE', '8', 'CURI', '4', '4', 'Fuel Efficiency, Calorific Value & Harmful Effects of Burning', ['Calorific value (kJ/kg)', 'Ideal fuel characteristics', 'Harmful combustion products: carbon monoxide poisoning, acid rain (SO2, NO2), global warming (CO2)'])
        ]
      },
      {
        number: '5',
        name: 'Conservation of Plants and Animals',
        topics: [
          createTopic('CBSE', '8', 'CURI', '5', '1', 'Deforestation: Causes and Consequences', ['Agricultural expansion, logging, urbanisation', 'Desertification, soil erosion, and disrupted water cycle']),
          createTopic('CBSE', '8', 'CURI', '5', '2', 'Biosphere Reserves, National Parks & Wildlife Sanctuaries', ['Panchmarhi Biosphere Reserve', 'Core, buffer, and transition zones', 'In-situ vs ex-situ conservation']),
          createTopic('CBSE', '8', 'CURI', '5', '3', 'Flora, Fauna & Endemic Species', ['Flora and fauna definitions', 'Endemic species of Panchmarhi (sal, wild mango, Indian giant squirrel)']),
          createTopic('CBSE', '8', 'CURI', '5', '4', 'Endangered Species, Red Data Book, Migration & Reforestation', ['Threatened vs endangered vs extinct species', 'IUCN Red Data Book records', 'Bird migration reasons', 'Reforestation practices and Forest Conservation Act'])
        ]
      },
      {
        number: '6',
        name: 'Reproduction in Animals',
        topics: [
          createTopic('CBSE', '8', 'CURI', '6', '1', 'Modes of Reproduction: Sexual vs Asexual', ['Basic difference between sexual and asexual modes', 'Importance of reproduction in species continuity']),
          createTopic('CBSE', '8', 'CURI', '6', '2', 'Male and Female Reproductive Systems in Humans', ['Male organs: Testes, sperm ducts, penis, sperm structure', 'Female organs: Ovaries, oviducts (fallopian tubes), uterus, ovum']),
          createTopic('CBSE', '8', 'CURI', '6', '3', 'Fertilisation: Internal vs External Fertilisation', ['Zygote formation', 'Internal fertilisation in humans, cows, hens', 'External fertilisation in frogs and fish']),
          createTopic('CBSE', '8', 'CURI', '6', '4', 'Embryo Development, Viviparous vs Oviparous Animals', ['Cleavage, blastocyst, implantation in uterine wall, foetus formation', 'Viviparous (give birth) vs Oviparous (lay eggs)']),
          createTopic('CBSE', '8', 'CURI', '6', '5', 'Metamorphosis in Frog & Asexual Reproduction (Budding, Binary Fission)', ['Tadpole to adult metamorphosis under thyroxine control', 'Budding in Hydra', 'Binary fission in Amoeba', 'Cloning of Dolly the sheep'])
        ]
      },
      {
        number: '7',
        name: 'Reaching the Age of Adolescence',
        topics: [
          createTopic('CBSE', '8', 'CURI', '7', '1', 'Adolescence, Puberty & Physical Body Changes', ['Growth spurt, increase in height', 'Change in body shape and voice (Adam apple)', 'Sweat and sebaceous gland activation']),
          createTopic('CBSE', '8', 'CURI', '7', '2', 'Secondary Sexual Characteristics & Hormonal Control', ['Testosterone and estrogen roles', 'Endocrine system and pituitary master gland hormones']),
          createTopic('CBSE', '8', 'CURI', '7', '3', 'Reproductive Phase of Life & Menstrual Cycle', ['Menarche and Menopause', 'Uterine thickening, ovulation, and menstruation cycle']),
          createTopic('CBSE', '8', 'CURI', '7', '4', 'Sex Determination in Humans & Other Endocrine Hormones', ['XY sex chromosomes in males, XX in females', 'Thyroid (Thyroxine), Pancreas (Insulin), Adrenal (Adrenaline) glands', 'Metamorphosis hormones in insects (juvenile hormone, ecdysone)']),
          createTopic('CBSE', '8', 'CURI', '7', '5', 'Nutritional Needs of Adolescents & Reproductive Hygiene', ['Balanced diet and iron-rich foods', 'Personal hygiene, drug abuse prevention, HIV/AIDS awareness'])
        ]
      },
      {
        number: '8',
        name: 'Force and Pressure',
        topics: [
          createTopic('CBSE', '8', 'CURI', '8', '1', 'Force: A Push or a Pull & Resultant Forces', ['Forces due to interaction', 'Adding forces in same direction, subtracting opposing forces', 'Net resultant force and equilibrium']),
          createTopic('CBSE', '8', 'CURI', '8', '2', 'Effects of Force on State of Motion & Shape', ['Changing speed of object', 'Changing direction of motion', 'Changing physical shape of flexible objects']),
          createTopic('CBSE', '8', 'CURI', '8', '3', 'Contact Forces: Muscular Force & Friction Force', ['Muscular force action in living organisms', 'Frictional force opposing relative motion']),
          createTopic('CBSE', '8', 'CURI', '8', '4', 'Non-Contact Forces: Magnetic, Electrostatic & Gravitational', ['Magnetic attraction and repulsion', 'Electrostatic force using charged comb/straw', 'Universal gravitational pull of Earth']),
          createTopic('CBSE', '8', 'CURI', '8', '5', 'Pressure: Formula (P = F/A) & Liquid/Atmospheric Pressure', ['Pressure definition and SI unit Pascal (N/m²)', 'Dependence of pressure on surface contact area (sharp knife vs blunt)', 'Liquid pressure increases with depth & exerts equal sideways pressure', 'Atmospheric pressure measurement and Magdeburg hemispheres experiment'])
        ]
      },
      {
        number: '9',
        name: 'Friction',
        topics: [
          createTopic('CBSE', '8', 'CURI', '9', '1', 'Force of Friction & Microscopic Irregularities', ['Friction opposes relative motion between surfaces in contact', 'Interlocking of microscopic irregularities on surfaces', 'Rough vs smooth surfaces']),
          createTopic('CBSE', '8', 'CURI', '9', '2', 'Factors Affecting Friction: Normal Force & Surface Texture', ['Effect of pressing forces (normal reaction)', 'Spring balance measurement of friction']),
          createTopic('CBSE', '8', 'CURI', '9', '3', 'Static, Sliding & Rolling Friction (Hierarchy Comparison)', ['Static friction (maximum limiting friction)', 'Sliding friction is less than static friction', 'Rolling friction is much smaller than sliding friction']),
          createTopic('CBSE', '8', 'CURI', '9', '4', 'Friction: A Necessary Evil (Advantages & Disadvantages)', ['Advantages: Walking, writing, braking automobiles', 'Disadvantages: Wear and tear of shoes/tires, energy loss as heat']),
          createTopic('CBSE', '8', 'CURI', '9', '5', 'Methods of Increasing & Decreasing Friction & Fluid Drag', ['Increasing: Treaded tires, grooved soles, spikes for athletes', 'Decreasing: Lubricants (oil, grease, graphite), ball bearings', 'Fluid friction (Drag) and streamlined shapes in airplanes, fish, birds'])
        ]
      },
      {
        number: '10',
        name: 'Sound',
        topics: [
          createTopic('CBSE', '8', 'CURI', '10', '1', 'Sound Produced by Vibrating Bodies & Musical Instruments', ['Vibrating tuning fork, rubber band, string', 'Vocal cords (larynx) in humans', 'Wind, percussion, string musical instruments']),
          createTopic('CBSE', '8', 'CURI', '10', '2', 'Sound Needs a Medium for Propagation (Vacuum Bell Jar Experiment)', ['Propagation through solids, liquids, gases', 'Speed of sound comparison in different media', 'Cannot travel through vacuum']),
          createTopic('CBSE', '8', 'CURI', '10', '3', 'Human Ear Anatomy & Hearing Mechanism', ['Outer ear (pinna, ear canal)', 'Middle ear (tympanic membrane/eardrum, three tiny bones)', 'Inner ear (cochlea) and auditory nerve to brain']),
          createTopic('CBSE', '8', 'CURI', '10', '4', 'Amplitude, Time Period, Frequency, Loudness & Pitch', ['Oscillation and frequency (Hertz, Hz)', 'Loudness is proportional to square of amplitude (Decibels, dB)', 'Pitch/shrillness is determined by frequency']),
          createTopic('CBSE', '8', 'CURI', '10', '5', 'Audible vs Inaudible Sounds & Noise Pollution Control', ['Audible range: 20 Hz to 20,000 Hz', 'Infrasonic (<20 Hz) and Ultrasonic (>20 kHz) sounds', 'Noise vs music, health hazards of noise pollution, tree belt mitigation'])
        ]
      },
      {
        number: '11',
        name: 'Chemical Effects of Electric Current',
        topics: [
          createTopic('CBSE', '8', 'CURI', '11', '1', 'Electrical Conductivity of Liquids & Electrolytes', ['Good conductors vs poor conductors', 'Testing distilled water vs salt/acid/base solutions', 'LED and magnetic compass tester sensitivity']),
          createTopic('CBSE', '8', 'CURI', '11', '2', 'Chemical Effects of Current (Electrolysis of Water)', ['William Nicholson electrolysis experiment (1800)', 'Oxygen gas at positive anode, Hydrogen gas at negative cathode', 'Color changes in potato conduction test']),
          createTopic('CBSE', '8', 'CURI', '11', '3', 'Electroplating Principles, Setup & Industrial Applications', ['Electroplating definition using copper sulphate electrolyte', 'Cathode (object to be plated), Anode (pure metal plate)', 'Chromium plating on car rims/taps, Gold/silver plating on jewellery, Tin cans, Zinc galvanisation'])
        ]
      },
      {
        number: '12',
        name: 'Some Natural Phenomena',
        topics: [
          createTopic('CBSE', '8', 'CURI', '12', '1', 'Static Electricity & Charging by Friction', ['Rubbing glass rod with silk, plastic comb with hair', 'Positive and negative charge conventions', 'Like charges repel, unlike charges attract']),
          createTopic('CBSE', '8', 'CURI', '12', '2', 'Electroscope & Transfer of Electric Charge', ['Gold-leaf electroscope construction and working', 'Earthing / grounding definition']),
          createTopic('CBSE', '8', 'CURI', '12', '3', 'Lightning: Story of Lightning, Safety & Lightning Conductors', ['Benjamin Franklin kite experiment', 'Cloud charge accumulation and electric discharge', 'Lightning safety outdoors and indoors', 'Lightning conductor installation on buildings']),
          createTopic('CBSE', '8', 'CURI', '12', '4', 'Earthquakes: Tectonic Plates, Seismic Waves & Richter Scale', ['Fault zones and tectonic plate boundaries', 'Epicentre, focus, and seismic waves recorded by seismograph', 'Richter scale logarithmic measurement', 'Earthquake safe structural design and safety protocols'])
        ]
      },
      {
        number: '13',
        name: 'Light',
        topics: [
          createTopic('CBSE', '8', 'CURI', '13', '1', 'Laws of Reflection & Normal Angle Geometry', ['Angle of incidence = Angle of reflection (∠i = ∠r)', 'Incident ray, normal, and reflected ray lie in same plane', 'Regular vs diffused/irregular reflection']),
          createTopic('CBSE', '8', 'CURI', '13', '2', 'Image Formation by Plane Mirror & Lateral Inversion', ['Virtual, erect, same-size image at same distance behind mirror', 'Lateral inversion (left appears right and right appears left)']),
          createTopic('CBSE', '8', 'CURI', '13', '3', 'Multiple Images, Kaleidoscope & Periscope', ['Formula for number of images: n = (360/θ) - 1', 'Kaleidoscope construction and symmetrical patterns', 'Periscope working using two plane mirrors at 45°']),
          createTopic('CBSE', '8', 'CURI', '13', '4', 'Refraction & Dispersion of Light by Glass Prism', ['Splitting of white light into 7 colors (VIBGYOR)', 'Rainbow formation as natural dispersion']),
          createTopic('CBSE', '8', 'CURI', '13', '5', 'Human Eye Anatomy, Defects (Myopia/Hypermetropia) & Care', ['Cornea, iris, pupil, eye lens, retina, rods & cones, blind spot', 'Persistence of vision (1/16th second)', 'Near point (25 cm) and eye hygiene', 'Braille system for visually impaired (Louis Braille)'])
        ]
      }
    ]
  }
];

module.exports = { cbse8Subjects };
