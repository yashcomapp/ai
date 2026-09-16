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
        name: "Exploring the Investigative World of Science",
        topics: [
          createTopic('CBSE', '8', 'CURI', '1', '1', "Science Begins with Curiosity", ["Everyday observations that spark curiosity (puffed puri, sliced apple browning, morning dew)","Spirit of scientific inquiry: Asking \"Why?\" and \"How?\"","Observation as the starting point of scientific inquiry"]),
          createTopic('CBSE', '8', 'CURI', '1', '2', "What is Scientific Investigation?", ["Formulating focused, testable scientific questions","Systematic observation, variable identification, and controlled experiments","Data collection, evidence evaluation, and drawing conclusions","Scientific tools, measurements, and honest documentation"])
        ]
      },
      {
        number: '2',
        name: "The Invisible Living World: Beyond Our Naked Eye",
        topics: [
          createTopic('CBSE', '8', 'CURI', '2', '1', "What is a Cell?", ["Cell as the fundamental structural and functional unit of life","History of cell discovery: Robert Hooke cork slice observation (1665)","Antonie van Leeuwenhoek: discovery of living microorganisms in water","Compound microscope and slide preparation techniques (onion peel with safranin, cheek cells with methylene blue)","Essential cell components: Cell membrane, cytoplasm, nucleus, cell wall, and plastids"]),
          createTopic('CBSE', '8', 'CURI', '2', '2', "What Are the Levels of Organisation in the Body of a Living Organism?", ["Unicellular organisms (Amoeba, Paramecium, Chlamydomonas)","Multicellular organisms and division of labour","Hierarchy: Cell → Tissue → Organ → Organ System → Organism"]),
          createTopic('CBSE', '8', 'CURI', '2', '3', "What Are Microorganisms?", ["Microscopic organisms invisible to the naked eye","Major groups of microorganisms: Bacteria, Fungi, Protozoa, and Algae","Habitats of microbes: pond water, soil suspensions, extreme heat, and ice","Viruses: characteristics and reproduction inside host cells"]),
          createTopic('CBSE', '8', 'CURI', '2', '4', "How Are We Connected to Microbes?", ["Beneficial microbes: Curd making (Lactobacillus), baking and brewing fermentation (Yeast)","Production of antibiotics (Penicillin) and vaccines","Decomposition of organic matter and nutrient recycling (Nitrogen fixation)","Harmful microbes (Pathogens): infectious diseases in humans, animals, and crops","Food spoilage and food preservation techniques (salting, sugar, oil, vinegar, pasteurization)"]),
          createTopic('CBSE', '8', 'CURI', '2', '5', "Why is Cell Considered to Be a Basic Unit of Life?", ["Independent existence and essential life processes occurring inside a single cell","Cell division for growth and repair","Synthesis of biomolecules and energy generation in cells"])
        ]
      },
      {
        number: '3',
        name: "Health: The Ultimate Treasure",
        topics: [
          createTopic('CBSE', '8', 'CURI', '3', '1', "Health: Is It More Than Not Falling Sick?", ["Definition of health: complete physical, mental, and social well-being","Being healthy vs being merely disease-free","Dimensions of wellness and emotional balance"]),
          createTopic('CBSE', '8', 'CURI', '3', '2', "How Can We Stay Healthy?", ["Balanced diet and nutritional requirements across growing age","Personal hygiene, regular handwashing, and oral healthcare","Physical exercise, yoga, outdoor activities, and correct posture","Adequate sleep, relaxation, and mental peace","Safe drinking water and clean surroundings"]),
          createTopic('CBSE', '8', 'CURI', '3', '3', "How Do We Know That We Are Unwell?", ["Body signals, symptoms, and clinical signs of illness (fever, fatigue, pain, cough)","Difference between symptoms (subjective feeling) and signs (objective indication)","When to seek medical advice and diagnostic testing"]),
          createTopic('CBSE', '8', 'CURI', '3', '4', "Diseases: What Are the Causes and Types?", ["Classification into Communicable (Infectious) and Non-communicable (Non-infectious) diseases","Causative agents: bacteria, viruses, fungi, protozoa, and parasitic worms","Modes of disease transmission: airborne droplets, contaminated water/food, vectors (mosquitoes, flies), direct contact","Lifestyle diseases, nutritional deficiency disorders, and genetic conditions"]),
          createTopic('CBSE', '8', 'CURI', '3', '5', "How to Prevent and Control Diseases?", ["Body defense mechanisms and the immune system (innate and acquired immunity)","Vaccination and immunization: principle, memory cells, and Universal Immunization Programme","Proper use of antibiotics and avoiding self-medication","Vector control: preventing mosquito breeding, proper sanitation, and community hygiene"])
        ]
      },
      {
        number: '4',
        name: "Electricity: Magnetic and Heating Effects",
        topics: [
          createTopic('CBSE', '8', 'CURI', '4', '1', "Does an Electric Current Have a Magnetic Effect?", ["Deflection of a magnetic compass needle near a current-carrying wire (Oersted discovery)","Magnetic field around a straight current-carrying wire","4.1.1 Electromagnets: winding insulated wire on an iron core, polarity, and factors affecting strength (number of turns, current)","Applications of electromagnets: Electric bell mechanism, magnetic cranes, electric motors"]),
          createTopic('CBSE', '8', 'CURI', '4', '2', "Does a Current Carrying Wire Get Hot?", ["Electrical resistance and heating effect in conductors","Experiments with nichrome wire and factors affecting heat produced (current, resistance, time)","Heating appliances: electric iron, room heater, water geyser, toaster, electric kettle","Electrical safety devices: Electric fuse (working principle, low melting point alloy) and Miniature Circuit Breakers (MCBs)"]),
          createTopic('CBSE', '8', 'CURI', '4', '3', "How Does a Battery Generate Electricity?", ["Chemical origin of electric current: conversion of chemical energy to electrical energy","4.3.1 Voltaic (Galvanic) Cells: Luigi Galvani, Alessandro Volta, simple copper-zinc cell setup","4.3.2 Dry Cells: structure, carbon rod cathode, zinc container anode, ammonium chloride electrolyte paste","4.3.3 Rechargeable Batteries: lead-acid, lithium-ion, and sustainable energy storage"])
        ]
      },
      {
        number: '5',
        name: "Exploring Forces",
        topics: [
          createTopic('CBSE', '8', 'CURI', '5', '1', "What is a Force?", ["Force as a push or a pull acting on an object","Everyday examples: kicking, pulling, lifting, opening, pushing","Forces arise due to interaction between two or more bodies"]),
          createTopic('CBSE', '8', 'CURI', '5', '2', "What Can a Force Do to the Bodies on Which It is Applied?", ["Changing state of motion: moving a stationary body or stopping a moving body","Changing the speed (speeding up or slowing down) of an object","Changing the direction of motion of a moving body","Changing the shape and dimensions of an object (elastic deformation of spring, clay, sponge)"]),
          createTopic('CBSE', '8', 'CURI', '5', '3', "Are Forces an Interaction Between Two or More Objects?", ["Forces require interaction between at least two bodies","Magnitude and direction of force","Net force calculation: forces acting in same direction add up; opposing forces subtract","Balanced forces (net force = 0) vs Unbalanced forces (produces acceleration)","SI unit of force: Newton (N)"]),
          createTopic('CBSE', '8', 'CURI', '5', '4', "What Are the Different Types of Forces?", ["Contact Forces: Muscular force (muscles of animals/humans), Frictional force (opposing relative motion between contacting surfaces)","Non-Contact Forces: Magnetic force (action at a distance between poles), Electrostatic force (force exerted by a charged body), Gravitational force (universal attraction between masses)"]),
          createTopic('CBSE', '8', 'CURI', '5', '5', "Weight and Its Measurement", ["Mass (amount of matter in kilograms) vs Weight (gravitational force W = m × g in Newtons)","Variation of weight with gravitational acceleration","Working principle and calibration of a Spring Balance"]),
          createTopic('CBSE', '8', 'CURI', '5', '6', "Floating and Sinking", ["Upthrust / Buoyant force exerted by liquids on immersed objects","Relationship between density of object, density of fluid, and buoyant force","Why an iron nail sinks while a massive iron ship floats","Apparent weight loss in fluids and applications of buoyancy"])
        ]
      },
      {
        number: '6',
        name: "Pressure, Winds, Storms, and Cyclones",
        topics: [
          createTopic('CBSE', '8', 'CURI', '6', '1', "Pressure", ["Definition of pressure: Force per unit area (Pressure = Force / Area)","SI unit of pressure: Pascal (Pa = N/m²)","Effect of contact surface area on pressure (broad shoulder straps, pointed drawing pins, sharp knives, wide tyres of tractors)"]),
          createTopic('CBSE', '8', 'CURI', '6', '2', "Pressure Exerted by Air", ["Atmospheric pressure: weight of the air column extending above Earth surface","Demonstrations of atmospheric pressure: rubber sucker adhesion, crushed tin can experiment","Pressure exerted by liquids and gases on container walls and variation with depth"]),
          createTopic('CBSE', '8', 'CURI', '6', '3', "Formation of Wind", ["Wind as moving air caused by atmospheric pressure differences","Air expands on heating and becomes lighter/less dense (warm air rises)","Convection currents in the atmosphere","Uneven heating of land and water: Land breeze and Sea breeze","Global wind circulation patterns due to uneven solar heating of equator and poles"]),
          createTopic('CBSE', '8', 'CURI', '6', '4', "High-Speed Winds Result in Lowering of Air Pressure", ["Scientific relationship: high wind speed leads to reduced pressure (Bernoulli principle)","Experimental demonstrations: blowing over a paper strip, blowing between suspended ping-pong balls","Lifting of tin roofs during high-speed storms"]),
          createTopic('CBSE', '8', 'CURI', '6', '5', "Storms, Thunderstorms, and Lightning", ["Formation of thunderstorms: rising warm moist air, condensation, updrafts, and raindrops","Separation of electric charges in storm clouds and lightning discharge","Safety precautions and lightning conductors on tall buildings"]),
          createTopic('CBSE', '8', 'CURI', '6', '6', "Cyclone", ["Structure and life cycle of a cyclone: low-pressure eye, spiraling high-speed winds, and eyewall","Factors contributing to cyclone development: wind speed, wind direction, temperature, and humidity","Destruction caused by cyclones: storm surges, coastal flooding, and structural damage","Cyclone warning systems (satellites and Doppler radars), evacuation, and disaster preparedness"])
        ]
      },
      {
        number: '7',
        name: "Particulate Nature of Matter",
        topics: [
          createTopic('CBSE', '8', 'CURI', '7', '1', "What is Matter Composed of?", ["Matter is made up of exceedingly tiny constituent particles (atoms and molecules)","Experiments demonstrating continuous space between particles (interparticle spaces)","Continuous motion of particles and diffusion (food aroma, potassium permanganate in water)","Forces of attraction between particles (cohesive forces)"]),
          createTopic('CBSE', '8', 'CURI', '7', '2', "What Decides Different States of Matter?", ["7.2.1 Solid state: closely packed particles, fixed shape and volume, high rigidity, low compressibility","7.2.2 Liquid state: loosely packed particles, definite volume, variable shape taking container contour, fluidity","7.2.3 Gaseous state: widely spaced particles, indefinite shape and volume, high compressibility, filling entire space"]),
          createTopic('CBSE', '8', 'CURI', '7', '3', "How Does the Interparticle Spacing Differ in the Three States of Matter?", ["Quantitative comparison of interparticle spaces across solids, liquids, and gases","Compressibility of gases vs liquids and solids (syringe piston experiment)","Effect of temperature on kinetic energy and interparticle spacing","Changes of state: melting, boiling, evaporation, condensation, and sublimation"])
        ]
      },
      {
        number: '8',
        name: "Nature of Matter: Elements, Compounds, and Mixtures",
        topics: [
          createTopic('CBSE', '8', 'CURI', '8', '1', "What Are Mixtures?", ["Definition of mixture: physical combination of two or more substances in any variable ratio","Homogeneous mixtures (uniform composition e.g. air, sugar syrup, alloys)","Heterogeneous mixtures (non-uniform composition e.g. salad, muddy water, chalk in water)","Retaining of individual properties by constituent substances"]),
          createTopic('CBSE', '8', 'CURI', '8', '2', "What Are Pure Substances?", ["Pure substance definition: single type of particle with fixed physical and chemical constants","Sharp melting and boiling points as indicators of purity","Differences between pure substances and mixtures"]),
          createTopic('CBSE', '8', 'CURI', '8', '3', "What Are the Types of Pure Substances?", ["8.3.1 Elements: simplest pure substances consisting of one type of atom, chemical symbols","Classification of elements: Metals (lustre, malleability, ductility, conductivity), Non-metals, and Metalloids","8.3.2 Compounds: chemical combination of two or more elements in a definite mass ratio (e.g. water H₂O, carbon dioxide CO₂, sodium chloride NaCl)","Chemical bonds and breakdown of compounds by chemical/electrical methods only"]),
          createTopic('CBSE', '8', 'CURI', '8', '4', "How Do We Use Elements, Compounds, and Mixtures?", ["Industrial and everyday applications of metals (copper wiring, iron structures, gold jewellery)","Applications of non-metals (oxygen for respiration, nitrogen in fertilisers, chlorine for water purification)","Importance of compounds and common mixtures in technology, pharmaceuticals, and agriculture"]),
          createTopic('CBSE', '8', 'CURI', '8', '5', "What Are Minerals?", ["Naturally occurring inorganic substances found in Earth crust with definite crystal structures","Ores as minerals from which metals are extracted economically","Conservation of mineral resources and sustainable mining practices"])
        ]
      },
      {
        number: '9',
        name: "The Amazing World of Solutes, Solvents, and Solutions",
        topics: [
          createTopic('CBSE', '8', 'CURI', '9', '1', "What Are Solute, Solvent, and Solution?", ["Definition of a solution as a homogeneous mixture of solute and solvent","Solute (dissolved substance in smaller amount) vs Solvent (dissolving medium in larger amount)","Water as the universal solvent and aqueous vs non-aqueous solutions","Different solution types: solid-in-liquid, liquid-in-liquid, gas-in-liquid (aerated drinks)"]),
          createTopic('CBSE', '8', 'CURI', '9', '2', "How Much Solute Can a Fixed Amount of Solvent Dissolve?", ["Unsaturated vs Saturated solutions at a specific temperature","Definition of Solubility: maximum grams of solute dissolved in 100g of solvent at a given temperature","Effect of temperature on solubility of solid solutes in liquids","Supersaturated solutions and crystallization","Preparation of standard Oral Rehydration Solution (ORS)"]),
          createTopic('CBSE', '8', 'CURI', '9', '3', "Solubility of Gases", ["Dissolution of atmospheric gases (oxygen and carbon dioxide) in water","Vital importance of dissolved oxygen for aquatic animals and plants","Effect of temperature and pressure on solubility of gases (effervescence in soda bottles, thermal pollution effects)"]),
          createTopic('CBSE', '8', 'CURI', '9', '4', "Density and Floating or Sinking in Liquids", ["Concept of density: Mass per unit volume (Density = Mass / Volume)","Comparison of densities of different liquids (oil, water, glycerin, honey)","Density column experiments and understanding floatation based on relative density","Effect of dissolved solutes (like salt) on liquid density and buoyancy (swimming in Dead Sea)"])
        ]
      },
      {
        number: '10',
        name: "Light: Mirrors and Lenses",
        topics: [
          createTopic('CBSE', '8', 'CURI', '10', '1', "What Are Spherical Mirrors?", ["Curved reflecting surfaces of a spherical shell","Concave mirror (converging mirror, inner surface reflecting) vs Convex mirror (diverging mirror, outer surface reflecting)","Spoon reflection demonstration (inner scooped face vs outer curved back)","Geometric terms: Pole (P), Centre of Curvature (C), Radius of Curvature (R), Principal Axis, Principal Focus (F), and Focal Length (f = R/2)"]),
          createTopic('CBSE', '8', 'CURI', '10', '2', "Characteristics of Images Formed by Spherical Mirrors", ["Real images (procurable on screen, inverted) vs Virtual images (cannot be formed on screen, erect)","Magnified, diminished, and same-size images","Ray diagrams and image characteristics formed by concave mirrors at various object positions","Image formation by convex mirrors (always virtual, erect, and diminished)","Practical uses: Concave mirrors in torches, dentist examination, solar cookers; Convex mirrors as vehicle rear-view mirrors and wide-angle street mirrors"]),
          createTopic('CBSE', '8', 'CURI', '10', '3', "Laws of Reflection", ["Incident ray, point of incidence, normal, and reflected ray","First Law: Angle of incidence (∠i) = Angle of reflection (∠r)","Second Law: Incident ray, normal, and reflected ray all lie in the same plane","Regular reflection vs Diffuse / irregular reflection on rough surfaces","Image properties in a plane mirror: virtual, erect, laterally inverted, equidistant"]),
          createTopic('CBSE', '8', 'CURI', '10', '4', "Refraction of Light and Spherical Lenses", ["Phenomenon of refraction: bending of light when passing between different transparent media","Convex Lens (converging lens, thicker in middle) and Concave Lens (diverging lens, thinner in middle)","Optical centre (O), principal axis, principal focus (F), and focal length of lenses","Image formation by convex lenses (real and inverted vs virtual and magnified)","Image formation by concave lenses (always virtual, erect, diminished)","Applications: magnifying glasses, corrective spectacles, microscopes, telescopes, cameras"]),
          createTopic('CBSE', '8', 'CURI', '10', '5', "Dispersion of Light and Rainbow Formation", ["Splitting of white sunlight into its seven constituent colors (Dispersion of light)","Glass prism experiment and the visible spectrum (VIBGYOR)","Recombination of colors using Newton disc","Formation of rainbow in the sky by tiny raindrops acting as natural prisms"])
        ]
      },
      {
        number: '11',
        name: "Keeping Time with the Skies",
        topics: [
          createTopic('CBSE', '8', 'CURI', '11', '1', "How Does the Moon Appearance Change and Why?", ["Phases of the Moon: New Moon (Amavasya), Waxing Crescent, First Quarter, Waxing Gibbous, Full Moon (Purnima), Waning phases","Revolution of the Moon around Earth and sunlight reflection","Synodic lunar month (29.5 days) and the concept of Tithis in Indian astronomy"]),
          createTopic('CBSE', '8', 'CURI', '11', '2', "How Did Calendars Come into Existence?", ["Historical evolution of timekeeping using astronomical cycles","Lunar calendars based strictly on lunar phase cycles","Solar calendars based on Earth revolution around the Sun (365.25 days, Gregorian calendar)","Luni-solar calendars: intercalary months (Adhik Maas / Mala Masa) reconciling solar and lunar years","The Indian National Calendar (Saka calendar)"]),
          createTopic('CBSE', '8', 'CURI', '11', '3', "Are Festivals Related to Astronomical Phenomena?", ["Connection between cultural festivals and celestial alignments","Festivals celebrated on Full Moon (Raksha Bandhan, Guru Purnima, Buddha Purnima, Holi)","Festivals celebrated on New Moon (Diwali) or specific Crescent phases (Eid-ul-Fitr)","Solstices, equinoxes, and harvest festivals (Makar Sankranti, Pongal, Bihu, Baisakhi)"]),
          createTopic('CBSE', '8', 'CURI', '11', '4', "Why Do We Launch Artificial Satellites in Space?", ["Difference between natural satellites (the Moon) and human-made artificial satellites","Satellite orbits: Low Earth Orbit (LEO), Polar Orbit, and Geostationary Orbit (GEO)","Critical applications: Weather forecasting, cyclone tracking, telecommunication, GPS navigation, remote sensing, and disaster management","India space achievements: ISRO missions (Aryabhata, INSAT, IRS, Chandrayaan, Mangalyaan, Aditya-L1)"])
        ]
      },
      {
        number: '12',
        name: "How Nature Works in Harmony",
        topics: [
          createTopic('CBSE', '8', 'CURI', '12', '1', "How Do We Experience and Interpret Our Surroundings?", ["Concept of Habitat: natural dwelling environment fulfilling an organism life needs","Terrestrial habitats (forests, grasslands, deserts, mountains) and Aquatic habitats (ponds, rivers, oceans, wetlands)","Biotic components (producers, consumers, decomposers) and Abiotic components (sunlight, air, water, soil, temperature)","Dynamic interactions between biotic and abiotic factors"]),
          createTopic('CBSE', '8', 'CURI', '12', '2', "Who All Live Together in Nature?", ["Organism: single living individual","Population: group of individuals of the same species living in a habitat","Community: interacting populations of different species sharing a habitat","Ecosystem: biological community together with its physical abiotic environment","Symbiotic relationships, mutualism, and pollination partnerships (insects, birds, and flowering plants)"]),
          createTopic('CBSE', '8', 'CURI', '12', '3', "Does Every Organism in a Community Matter?", ["Trophic levels: Producers (autotrophs), Primary consumers (herbivores), Secondary & Tertiary consumers (carnivores/omnivores), Decomposers","Food Chains and interwoven Food Webs","Ecological interdependency and cascade effects: impact of removing keystone species (e.g. dragonflies, bees, apex predators) on community equilibrium","Nutrient recycling and energy flow through ecosystems"]),
          createTopic('CBSE', '8', 'CURI', '12', '4', "Balance in Nature and Conservation", ["Biodiversity importance for ecological stability, resilience, and climate regulation","Human disruptions: habitat fragmentation, deforestation, pollution, invasive alien species, overexploitation","Threatened and endangered species (IUCN Red List awareness)","Conservation measures: In-situ (National Parks, Wildlife Sanctuaries, Biosphere Reserves) and Ex-situ (Botanical gardens, Seed banks, Zoos)","Traditional Indian ecological heritage: Sacred groves (Devrai), community forest reserves, Chipko conservation movement"])
        ]
      },
      {
        number: '13',
        name: "Our Home: Earth, a Unique Life Sustaining Planet",
        topics: [
          createTopic('CBSE', '8', 'CURI', '13', '1', "Why is Earth a Unique Planet?", ["Earth as the only known cradle of life in the universe","Habitable Zone (\"Goldilocks Zone\") positioning from the Sun","Optimal temperature ranges enabling liquid water existence","Life-sustaining crust, rocks, minerals, and fertile soil layer"]),
          createTopic('CBSE', '8', 'CURI', '13', '2', "What Do the Planets of Our Solar System Look Like?", ["Comparative physical conditions of Solar System planets (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune)","Hostile environments: runaway greenhouse heat on Venus, arid low-pressure cold of Mars, crushing pressures on gas giants","Why Earth uniquely supports complex multicellular life"]),
          createTopic('CBSE', '8', 'CURI', '13', '3', "What Makes the Earth Suitable for Life to Exist?", ["Earth interconnected spheres: Geosphere (Lithosphere), Hydrosphere, Cryosphere (polar ice and glaciers), Atmosphere, and Biosphere","Life-sustaining biogeochemical cycles: Water Cycle, Carbon Cycle, Oxygen Cycle, and Nitrogen Cycle","Atmospheric shield: Ozone layer filtering solar ultraviolet radiation and greenhouse effect maintaining global warmth","Earth geomagnetic field (magnetosphere) shielding solar winds and cosmic radiation"]),
          createTopic('CBSE', '8', 'CURI', '13', '4', "Protecting Our Living Planet and Sustainability", ["Anthropogenic threats: Global warming, climate change, ocean acidification, plastic pollution, and loss of topsoil","Sustainable resource stewardship: Conservation of freshwater, transitioning to renewable energy (solar, wind, biomass)","Circular economy and the 5 R (Refuse, Reduce, Reuse, Repurpose, Recycle)","Individual and collective civic action for environmental preservation and planetary health"])
        ]
      }
    ]
  }
];

module.exports = { cbse8Subjects };
