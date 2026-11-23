import json
import random
import os
from build_cbse8_curi_batch import make_question, get_vaults_and_diffs

random.seed(8825)

def run():
    with open("scripts/cbse8_curi_deficit_manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # -------------------------------------------------------------------------
    # CHAPTER 5 DATA
    # -------------------------------------------------------------------------
    ch5_cases = {
        "CBSE-8-CURI-5-5.1.1": [
            ("A force is fundamentally defined in elementary physics as:", "A push or a pull acting on an object resulting from its interaction with another object", ["The internal temperature of an object", "The speed at which an object travels", "The volume occupied by matter"]),
            ("Which action represents applying force as a PUSH?", "Hitting a tennis ball with a racquet", ["Opening a drawer towards yourself", "Drawing water from a well with a rope", "Plucking an apple from a branch"]),
            ("Which action represents applying force as a PULL?", "Towing a broken car using a steel cable", ["Kicking a soccer ball", "Closing a door firmly away from you", "Striking a cricket ball"]),
            ("Can a force act on an object without any interaction taking place between at least two objects?", "No, force always arises from an interaction between at least two bodies", ["Yes, force can exist alone in vacuum without interacting", "Only if the object has zero mass", "Yes, when light shines"])
        ],
        "CBSE-8-CURI-5-5.1.2": [
            ("When a goalkeeper dives and catches a fast-moving soccer ball, what effect of force is demonstrated?", "Stopping a moving object and bringing it to rest", ["Changing the color of the ball", "Increasing the mass of the ball", "Decomposing the rubber into gas"]),
            ("When a batsman strikes an incoming cricket ball with a bat, what effects of force are observed simultaneously?", "Change in both the speed and the direction of motion of the ball", ["Only a change in temperature", "Change in the mass of the cricket bat", "No physical change occurs"]),
            ("Lifting a heavy school bag from the classroom floor onto a desk involves applying:", "An upward muscular pull force against the downward force of gravity", ["Downward atmospheric pressure only", "Repulsive magnetic force", "Frictional force of air only"]),
            ("Rolling a lump of dough with a rolling pin (belan) to make a flat chapati demonstrates which effect of force?", "Change in the physical shape and dimensions of an object", ["Change in speed only", "Nuclear transmutation of matter", "Electrification of dough"])
        ],
        "CBSE-8-CURI-5-5.1.3": [
            ("A stationary car does not move simply because a person stands behind it without touching. Why?", "Force arises only when there is an active interaction (push/contact) between the person and the car", ["The person has zero weight", "The car has infinite gravity", "The air prevents force transmission"]),
            ("In an arm-wrestling contest between two athletes, the force exerted by each wrestler is an example of:", "Mutual interaction between two opposing physical bodies", ["Gravitational attraction only", "Electrostatic induction", "Unilateral non-interacting force"]),
            ("When a soccer player kicks a football, how do the foot and the ball interact?", "The foot exerts a forward push force on the ball, while the ball exerts an equal and opposite reaction force on the foot", ["Only the foot exerts force; the ball exerts zero force", "The ball pulls the foot forward", "Gravity pulls the ball into the foot"]),
            ("Forces in nature always occur in:", "Interacting pairs (action and reaction pairs)", ["Isolated single forces", "Groups of three only", "Random unpaired fluctuations"])
        ],
        "CBSE-8-CURI-5-5.2.1": [
            ("What does the 'state of motion' of an object describe in physics?", "Its speed of travel and its direction of motion (including state of rest when speed is zero)", ["Only the chemical composition of the object", "Its internal temperature and color", "The age of the material"]),
            ("What happens to an object at rest when an unbalanced external force acts on it?", "It begins to move in the direction of the applied net force", ["It remains permanently at rest", "Its mass decreases instantly to zero", "It dissolves into energy"]),
            ("Can a stationary toy cart start moving across a level floor entirely by itself without any external force acting on it?", "No, a net external force is strictly required to change an object's state of rest", ["Yes, due to internal thoughts", "Yes, if the room is illuminated", "Yes, after waiting one hour"]),
            ("When an applied braking force stops a moving bicycle, the state of motion changes from:", "A state of motion with non-zero speed to a state of rest (speed = 0)", ["A state of rest to high speed", "Circular motion to linear motion", "Positive charge to negative charge"])
        ],
        "CBSE-8-CURI-5-5.2.2": [
            ("When an applied force acts in the SAME direction as the motion of a moving bicycle, what happens to its speed?", "The speed of the bicycle increases (it accelerates)", ["The speed decreases", "The speed drops to zero immediately", "The direction reverses"]),
            ("When an applied force (like braking or friction) acts in the OPPOSITE direction to the motion of an object:", "The speed of the object decreases (it decelerates)", ["The speed increases rapidly", "The mass of the object increases", "The object turns upside down"]),
            ("If a ball is thrown vertically upward, why does its upward speed continuously decrease until it stops momentarily at peak height?", "The downward gravitational pull of the Earth acts continuously opposite to its upward motion", ["Air pushes the ball up faster", "The ball runs out of mass", "Sunlight pulls the ball down"]),
            ("If the net force acting on a moving object is exactly ZERO, how does its speed behave?", "The object continues to move at a constant, steady speed in a straight line", ["The object stops instantly", "The object accelerates to the speed of light", "The object starts spinning"])
        ],
        "CBSE-8-CURI-5-5.2.3": [
            ("How does a tennis player change the direction of motion of an incoming tennis ball?", "By applying a sideways/deflecting force on the ball with the tennis racquet", ["By blowing air with their mouth", "By shouting at the ball", "By stepping away from the net"]),
            ("When a car driver turns the steering wheel while driving along a curved road, what force causes the car to change its direction of motion?", "Frictional force exerted by the road surface on the tires directed towards the center of the turn", ["Downward gravity only", "Upward normal force only", "Air drag pushing backward"]),
            ("In cricket, when a batsman executes a leg glance, the force applied by the bat primarily changes:", "The direction of motion of the ball, while largely preserving its momentum", ["The color of the ball", "The diameter of the ball", "The atmospheric pressure"]),
            ("Can a moving body change its direction of motion without any net external force acting on it?", "No, changing direction strictly requires a net transverse external force", ["Yes, if the body is spherical", "Yes, if it travels in a vacuum", "Yes, by itself at midnight"])
        ],
        "CBSE-8-CURI-5-5.2.4": [
            ("Which everyday action provides clear evidence that force can change the shape and dimensions of an object?", "Squeezing an inflated rubber balloon or a sponge with both hands", ["Watching a stationary book on a desk", "Measuring the temperature of ice", "Switching on an electric bulb"]),
            ("When a metallic spring is pulled outward by applying a tensile force at both ends, what happens to its shape?", "The spring stretches, increasing its total length", ["The spring contracts into a ball", "The spring turns into liquid metal", "No physical change occurs"]),
            ("When you press an inflated football between your palms, the football becomes slightly flattened. What causes this deformation?", "The compressive forces applied by your palms exceed internal air pressure locally, distorting the elastic leather casing", ["Air escapes through pores", "Gravity pulls the football sideways", "Atmospheric pressure vanishes"]),
            ("Materials that return to their original shape after the deforming force is removed are called:", "Elastic materials (such as rubber bands and steel springs)", ["Plastic materials", "Brittle materials", "Rigid liquids"])
        ],
        "CBSE-8-CURI-5-5.3.1": [
            ("Why does a magnet attract an iron pin placed near it even across empty air without physical contact?", "Magnetic force is a non-contact field force that operates through the magnetic field generated by the magnet", ["The magnet blows air onto the pin", "Gravity pulls the pin towards North", "The pin is electrically grounded"]),
            ("Which of the following is classified as a CONTACT force requiring direct physical touch between surfaces?", "Muscular force and Frictional force", ["Gravitational force", "Electrostatic force", "Magnetic force"]),
            ("Which of the following is classified as an ACTION-AT-A-DISTANCE (Non-Contact) force?", "Gravitational force, Electrostatic force, and Magnetic force", ["Tension force in a rope", "Frictional drag", "Normal contact force"]),
            ("When you sit on a wooden chair, what two opposing forces are interacting between you and the chair?", "Your downward gravitational weight pressing on the chair and the chair's upward normal contact force supporting you", ["Magnetic attraction and repulsion", "Atmospheric wind pressure", "Nuclear fission force"])
        ],
        "CBSE-8-CURI-5-5.3.2": [
            ("Force is a vector quantity in physics because it possesses both:", "Magnitude (numerical size) and Direction of action", ["Mass and Volume", "Speed and Temperature", "Color and Density"]),
            ("If a force of \\(10\\ \\text{N}\\) acts due East and another force of \\(10\\ \\text{N}\\) acts due West, do they represent the same force?", "No, because although their magnitudes are equal, their directions of action are completely opposite", ["Yes, because both are 10 N", "Yes, because force has no direction", "Yes, if acting on the same body"]),
            ("Why is specifying the point of application and direction essential when describing a force?", "Applying force at different points or in different directions produces completely different physical effects (e.g., rotation vs translation)", ["Because formulas only work with words", "Because direction determines the mass of the object", "It is not essential at all"]),
            ("In scientific diagrams, how is a force vector typically represented graphically?", "By a straight arrow whose length represents the magnitude and arrowhead points in the direction of the force", ["By a circle of varying radius", "By a wavy colored line", "By a shaded rectangle"])
        ],
        "CBSE-8-CURI-5-5.3.3": [
            ("If two forces of magnitude \\(8\\ \\text{N}\\) and \\(6\\ \\text{N}\\) act on a box in the SAME horizontal direction, what is the net resultant force?", "\\(14\\ \\text{N}\\) in the direction of the applied forces (\\(8 + 6 = 14\\))", ["\\(2\\ \\text{N}\\)", "\\(48\\ \\text{N}\\)", "\\(0\\ \\text{N}\\)"]),
            ("If two forces of magnitude \\(15\\ \\text{N}\\) and \\(9\\ \\text{N}\\) act on an object in OPPOSITE directions, what is the net resultant force?", "\\(6\\ \\text{N}\\) in the direction of the larger (15 N) force (\\(15 - 9 = 6\\))", ["\\(24\\ \\text{N}\\)", "\\(135\\ \\text{N}\\)", "\\(0\\ \\text{N}\\)"]),
            ("In a game of tug-of-war, Team A pulls left with \\(500\\ \\text{N}\\) and Team B pulls right with \\(500\\ \\text{N}\\). What is the net horizontal force on the rope?", "\\(0\\ \\text{N}\\) (the forces cancel out completely)", ["\\(1000\\ \\text{N}\\) left", "\\(500\\ \\text{N}\\) right", "\\(250\\ \\text{N}\\)"]),
            ("If two equal and opposite forces of \\(20\\ \\text{N}\\) act on a stationary block, what motion will be observed?", "The block remains completely stationary because the net resultant force is zero", ["The block moves to the left", "The block moves to the right", "The block accelerates upward"])
        ],
        "CBSE-8-CURI-5-5.3.4": [
            ("Balanced forces acting on an object are defined as a system of forces whose:", "Resultant net force is strictly equal to zero (\\(F_{\\text{net}} = 0\\))", ["Resultant net force is positive", "Forces act in the same direction", "Forces cause sudden acceleration"]),
            ("Can balanced forces change the state of motion (speed or direction) of an object?", "No, balanced forces cannot change the speed or direction of motion; they can only cause deformation of shape", ["Yes, they always accelerate the body", "Yes, they make the object spin at light speed", "Only in outer space"]),
            ("Unbalanced forces acting on an object are defined as forces whose:", "Resultant net force is greater than zero, causing a change in the object's speed or direction of motion", ["Net sum is exactly zero", "Forces cancel each other out", "Forces produce no acceleration"]),
            ("When a heavy wooden crate finally begins to slide across a rough warehouse floor upon pushing, the applied push force is:", "Greater than the opposing maximum force of static friction (an unbalanced net force exists)", ["Equal to zero", "Less than static friction", "Balanced by atmospheric pressure"])
        ],
        "CBSE-8-CURI-5-5.3.5": [
            ("What is the standard SI unit of force named in honor of Sir Isaac Newton?", "Newton (symbol: N)", ["Joule (J)", "Pascal (Pa)", "Watt (W)"]),
            ("How is one Newton (\\(1\\ \\text{N}\\)) of force formally defined in fundamental SI units?", "The force required to impart an acceleration of \\(1\\ \\text{m/s}^2\\) to an object of mass \\(1\\ \\text{kg}\\) (\\(1\\ \\text{N} = 1\\ \\text{kg}\\cdot\\text{m/s}^2\\))", ["\\(1\\ \\text{kg}/\\text{m}\\)", "\\(1\\ \\text{Joule}\\cdot\\text{s}\\)", "\\(1\\ \\text{Pascal}/\\text{m}^2\\)"]),
            ("Approximately how many Newtons of downward gravitational force (weight) does an ordinary medium apple of mass \\(100\\ \\text{g}\\) (\\(0.1\\ \\text{kg}\\)) exert on your palm?", "Approximately \\(1\\ \\text{Newton}\\) (since \\(W = mg \\approx 0.1 \\times 9.8 \\approx 1\\ \\text{N}\\))", ["\\(100\\ \\text{Newtons}\\)", "\\(0.01\\ \\text{Newton}\\)", "\\(10\\ \\text{Newtons}\\)"]),
            ("What measuring instrument is calibrated in Newtons to measure the magnitude of a tensile force or weight directly?", "A Spring Balance (Dynamometer)", ["A chemical beam balance", "A mercury thermometer", "A graduated cylinder"])
        ],
        "CBSE-8-CURI-5-5.4.1": [
            ("Muscular force is defined in biomechanics as:", "The contact force exerted by the action of skeletal muscles contracting and relaxing inside a living body", ["The force of gravity acting on bones", "Magnetic attraction of blood iron", "Atmospheric air pressure on skin"]),
            ("Which of the following activities relies directly on muscular contact force?", "A bullock pulling a cart, lifting a bucket of water, and chewing food with jaws", ["A dry leaf falling from a tree to the ground", "An iron nail attracted to a bar magnet", "A plastic comb attracting bits of paper"]),
            ("Why is muscular force strictly classified as a contact force?", "Muscles can apply force on an external object only when physical contact is established directly or via an intermediary tool/rope", ["Muscles operate through empty space like radio waves", "Muscles generate gravitational fields", "Muscles have zero mass"]),
            ("What physiological mechanism generates mechanical tension during muscular force application?", "Contraction of muscle fibers driven by ATP hydrolysis in actin and myosin protein filaments", ["Thermal boiling of blood", "Static electric spark discharge", "Compression of air in lungs"])
        ],
        "CBSE-8-CURI-5-5.5.1": [
            ("What is the fundamental scientific difference between the MASS and the WEIGHT of an object?", "Mass is the intrinsic amount of matter in kilograms (invariant everywhere), while weight is the gravitational force acting on that mass in Newtons (varies with gravity)", ["Mass is measured in Newtons and weight in kilograms", "Mass changes on the Moon while weight stays constant", "There is no difference in physics"]),
            ("What are the standard SI units used to measure mass and weight, respectively?", "Kilogram (kg) for mass, and Newton (N) for weight", ["Gram for both", "Newton for mass and Kilogram for weight", "Pounds and litres"]),
            ("Which laboratory instrument measures the invariant inertial mass of an object by comparing it against standard reference masses?", "A two-pan Beam Balance (or physical balance)", ["A spring balance", "A clinical thermometer", "A barometer"]),
            ("If an astronaut has a mass of \\(60\\ \\text{kg}\\) on Earth, what is the astronaut's mass on the surface of the Moon?", "\\(60\\ \\text{kg}\\) (mass remains strictly constant regardless of location)", ["\\(10\\ \\text{kg}\\)", "\\(0\\ \\text{kg}\\)", "\\(360\\ \\text{kg}\\)"])
        ],
        "CBSE-8-CURI-5-5.5.2": [
            ("Which mathematical equation calculates the weight (\\(W\\)) of an object of mass \\(m\\) in a gravitational field of acceleration \\(g\\)?", "\\(W = m \\times g\\)", ["\\(W = m / g\\)", "\\(W = g / m\\)", "\\(W = m^2 \\times g\\)"]),
            ("On Earth where \\(g \\approx 9.8\\ \\text{m/s}^2\\) (or \\(\\sim 10\\ \\text{m/s}^2\\)), what is the approximate weight of a \\(50\\ \\text{kg}\\) student?", "Approximately \\(490\\ \\text{N}\\) (or \\(\\sim 500\\ \\text{N}\\))", ["\\(50\\ \\text{N}\\)", "\\(5\\ \\text{N}\\)", "\\(2500\\ \\text{N}\\)"]),
            ("The gravitational acceleration on the Moon is roughly \\(1/6^{\\text{th}}\\) of Earth's gravity (\\(g_{\\text{moon}} \\approx 1.63\\ \\text{m/s}^2\\)). What would the \\(60\\ \\text{kg}\\) astronaut weigh on the Moon?", "\\(100\\ \\text{N}\\) (compared to \\(600\\ \\text{N}\\) on Earth)", ["\\(600\\ \\text{N}\\)", "\\(60\\ \\text{N}\\)", "\\(0\\ \\text{N}\\)"]),
            ("At the exact gravitational center of the Earth (where \\(g = 0\\)), what would be the weight of an object?", "Zero Newtons (complete true weightlessness)", ["Infinite weight", "Double its surface weight", "Same as surface weight"])
        ],
        "CBSE-8-CURI-5-5.5.3": [
            ("A spring balance operates on which fundamental physical principle of elasticity formulated by Robert Hooke?", "Hooke's Law: The extension (stretch) of a helical spring is directly proportional to the applied tensile force within elastic limits", ["Ohm's Law: Current is proportional to voltage", "Boyle's Law: Pressure is inversely proportional to volume", "Law of conservation of mass"]),
            ("If a \\(100\\ \\text{g}\\) load stretches a calibrated spring balance by \\(2\\ \\text{cm}\\), how much will a \\(300\\ \\text{g}\\) load stretch the same spring within its elastic limit?", "\\(6\\ \\text{cm}\\) (\\(2\\ \\text{cm} \\times 3 = 6\\ \\text{cm}\\))", ["\\(4\\ \\text{cm}\\)", "\\(8\\ \\text{cm}\\)", "\\(1\\ \\text{cm}\\)"]),
            ("What happens if a load exceeding the maximum elastic limit of a spring balance is hung from it?", "The spring undergoes permanent plastic deformation and will no longer return to zero or measure accurately", ["The spring turns into gold", "The load evaporates", "The spring becomes five times stiffer"]),
            ("The pointer scale on a standard student spring balance is typically calibrated directly to read:", "Force in Newtons (N) and equivalent mass in grams/kilograms", ["Temperature in Celsius", "Atmospheric pressure in Pa", "Volume in millilitres"])
        ],
        "CBSE-8-CURI-5-5.6.2": [
            ("Density (\\(\\rho\\)) of any material substance is mathematically defined as its:", "Mass per unit volume (\\(\\text{Density} = \\frac{\\text{Mass}}{\\text{Volume}}\\))", ["Weight multiplied by volume", "Volume divided by mass", "Force per unit area"]),
            ("What is the standard SI unit of density, and what is the density of pure water at \\(4^\\circ\\text{C}\\)?", "\\(\\text{kg/m}^3\\), with water density equal to \\(1000\\ \\text{kg/m}^3\\) (or \\(1\\ \\text{g/cm}^3\\))", ["\\(\\text{g/m}^2\\), water \\(500\\ \\text{g/m}^2\\)", "\\(\\text{N/m}^3\\), water \\(100\\ \\text{N/m}^3\\)", "\\(\\text{J/kg}\\), water \\(4200\\ \\text{J/kg}\\)"]),
            ("An object floats on the surface of a liquid if its average density is:", "Less than the density of the liquid (\\(\\rho_{\\text{object}} < \\rho_{\\text{liquid}}\\))", ["Greater than the density of the liquid", "Equal to the density of granite", "Twice the density of mercury"]),
            ("Why does an ordinary wooden block float in water while a solid stone of identical size sinks to the bottom?", "The density of wood is less than that of water, while the density of stone is greater than that of water", ["Wood has zero gravity", "Stone has no buoyant force", "Wood dissolves water molecules"])
        ],
        "CBSE-8-CURI-5-5.6.3": [
            ("Why does a small solid iron nail sink in water, whereas a massive ship made of thousands of tons of iron and steel floats easily?", "The ship is hollow and encloses vast volumes of air, making its overall average density much less than that of water", ["The nail is heavier than the entire ship", "Saltwater hates nails", "The ship has giant magnets pulling it upward"]),
            ("According to Archimedes' Principle, the upward buoyant force exerted on a submerged body is equal to:", "The weight of the liquid displaced by the submerged portion of the body", ["The total mass of the Earth", "The volume of air inside lungs", "The surface tension of the water"]),
            ("Why does a cargo ship sink deeper into the water when it is heavily loaded with freight containers?", "It must submerge further to displace a greater volume and weight of water equal to its increased total weight", ["The freight containers push water into the ship", "The ocean becomes less dense", "The ship's steel expands"]),
            ("Why does a ship float higher in salty seawater than in a freshwater river?", "Seawater has dissolved salts making it denser than freshwater, so a smaller submerged volume displaces enough weight to balance the ship", ["Seawater has less waves", "River water has no buoyant force", "Salt creates downward suction"])
        ],
        "CBSE-8-CURI-5-5.6.4": [
            ("Why does a heavy stone feel noticeably lighter when submerged underwater inside a well or bucket?", "The upward buoyant force (upthrust) exerted by the displaced water partially offsets the downward weight of the stone", ["The stone loses actual mass underwater", "Water destroys gravity", "The rope becomes infinitely elastic"]),
            ("The 'apparent weight' of an object submerged in a liquid is calculated as:", "\\(\\text{Apparent Weight} = \\text{True Weight in Air} - \\text{Upthrust (Buoyant Force)}\\)", ["\\(\\text{Apparent Weight} = \\text{True Weight} + \\text{Upthrust}\\)", "\\(\\text{Apparent Weight} = \\text{True Weight} \\times \\text{Upthrust}\\)", "\\(\\text{Apparent Weight} = \\text{True Weight} / 2\\)"]),
            ("Which specialized floating glass instrument is calibrated to measure the relative density of liquids (such as milk or battery acid)?", "A Hydrometer (or Lactometer for milk purity)", ["A Barometer", "A Manometer", "A Calorimeter"]),
            ("A Lactometer floating in a jar of pure milk sinks to mark 'M'. If the milk has been heavily adulterated with water, the Lactometer will:", "Sink deeper because adulterated milk has lower density than pure milk", ["Float higher above the milk surface", "Remain at exactly mark 'M'", "Turn upside down"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 6 DATA
    # -------------------------------------------------------------------------
    ch6_cases = {
        "CBSE-8-CURI-6-6.1.1": [
            ("Pressure is fundamentally defined in physics as:", "The thrust (perpendicular force) acting per unit surface area (\\(\\text{Pressure} = \\frac{\\text{Force}}{\\text{Area}}\\))", ["The total mass of an object", "The speed of air particles", "The volume of liquid in a tank"]),
            ("For a constant applied force, what happens to the pressure when the contact surface area is HALVED?", "The pressure DOUBLES (pressure is inversely proportional to contact area)", ["The pressure halves", "The pressure drops to zero", "The pressure quadruples"]),
            ("Why does an elephant exert less pressure on the ground per square centimeter than a woman wearing pointed high-heeled stiletto shoes?", "The elephant's large, broad feet distribute its heavy weight across a very large contact area, reducing pressure", ["The elephant has no weight", "The woman is heavier than an elephant", "High heels absorb all gravity"]),
            ("Which of the following mathematical equations correctly represents pressure (\\(P\\)) in terms of force (\\(F\\)) and area (\\(A\\))?", "\\(P = \\frac{F}{A}\\)", ["\\(P = F \\times A\\)", "\\(P = \\frac{A}{F}\\)", "\\(P = F^2 \\times A\\)"])
        ],
        "CBSE-8-CURI-6-6.1.2": [
            ("What is the official SI unit of pressure named after French mathematician Blaise Pascal?", "Pascal (symbol: Pa, where \\(1\\ \\text{Pa} = 1\\ \\text{N/m}^2\\))", ["Newton (N)", "Joule (J)", "Watt (W)"]),
            ("A perpendicular force of \\(200\\ \\text{N}\\) acts uniformly over a flat surface area of \\(0.5\\ \\text{m}^2\\). What is the resulting pressure?", "\\(400\\ \\text{Pa}\\) (\\(200 / 0.5 = 400\\))", ["\\(100\\ \\text{Pa}\\)", "\\(1000\\ \\text{Pa}\\)", "\\(40\\ \\text{Pa}\\)"]),
            ("What is standard normal atmospheric pressure at sea level expressed in Pascals and in kilopascals (kPa)?", "Approximately \\(101{,}325\\ \\text{Pa}\\) (or \\(\\sim 101.3\\ \\text{kPa}\\))", ["\\(100\\ \\text{Pa}\\)", "\\(1000\\ \\text{Pa}\\)", "\\(1\\ \\text{Pa}\\)"]),
            ("The traditional pressure unit 'bar' is related to the SI unit Pascal by:", "\\(1\\ \\text{bar} = 10^5\\ \\text{Pa}\\) (or \\(100{,}000\\ \\text{Pa}\\))", ["\\(1\\ \\text{bar} = 1\\ \\text{Pa}\\)", "\\(1\\ \\text{bar} = 1000\\ \\text{Pa}\\)", "\\(1\\ \\text{bar} = 10^9\\ \\text{Pa}\\)"])
        ],
        "CBSE-8-CURI-6-6.1.3": [
            ("Why are cutting tools like knives, scissors, and axes manufactured with extremely sharp, thin cutting edges?", "A sharp edge has a microscopic contact area, producing immense pressure with modest applied force to slice materials easily", ["A sharp edge is heavier than a blunt edge", "Sharp edges prevent chemical rusting", "Sharp edges increase friction"]),
            ("Why are heavy school backpacks and mountaineering rucksacks designed with wide shoulder straps?", "Wide straps provide a large surface area over the shoulders, substantially reducing pressure and shoulder strain", ["Wide straps look fashionable", "Wide straps make the backpack weigh less", "Wide straps absorb sunlight"]),
            ("Why are heavy transport trucks and earthmovers fitted with 8 to 14 broad tires?", "To spread the massive gross vehicle weight over a large road contact area, preventing road damage and tire sinking", ["To allow trucks to drive faster than sports cars", "Because tires are inexpensive", "To look identical to trains"]),
            ("Why do wide wooden or concrete sleepers laid beneath railway tracks prevent the tracks from sinking into the ground?", "They distribute the immense localized weight of passing trains across a large ground surface area, keeping pressure low", ["They hold the rails with magnetic force", "They heat the steel rails in winter", "They absorb train sound waves"])
        ],
        "CBSE-8-CURI-6-6.2.1": [
            ("Atmospheric pressure is defined in meteorology and physics as:", "The pressure exerted by the weight of the vast vertical column of air above a unit surface area of the Earth", ["The wind blowing sideways across trees", "The heat radiated by the Earth's molten core", "The gravitational pull of the Moon on soil"]),
            ("Why do human bodies not get crushed flat beneath the enormous atmospheric pressure (approx. 100,000 N per square meter)?", "The internal fluids, blood pressure, and dissolved gases inside human tissues exert an equal outward pressure balancing atmospheric pressure", ["Human skin is made of solid steel", "Atmospheric air has zero mass", "Gravity does not act on humans"]),
            ("What happens to atmospheric pressure as one ascends to high altitudes in mountain ranges like the Himalayas?", "Atmospheric pressure decreases progressively because the height and density of the overlying air column decreases", ["Atmospheric pressure increases infinitely", "Atmospheric pressure remains strictly constant", "Atmospheric pressure drops to absolute zero at 500 m"]),
            ("Why do mountaineers climbing Mount Everest sometimes experience nosebleeds and breathing difficulty?", "Atmospheric pressure drops severely, causing internal blood pressure in delicate nasal capillaries to burst them outward", ["The cold freezes their blood solid", "The air becomes 100% carbon dioxide", "Gravity becomes double at high altitude"])
        ],
        "CBSE-8-CURI-6-6.2.2": [
            ("When a flat rubber suction cup is pressed firmly against a smooth glass wall, why does it stick tightly?", "Pressing expels air from beneath the cup; external atmospheric pressure presses firmly on the outside of the cup, holding it in place", ["Glue melts between the rubber and glass", "The rubber becomes magnetized", "A vacuum attracts glass atoms"]),
            ("How does liquid rise into a drinking straw when a person sips from a glass of juice?", "Sucking removes air from inside the straw, creating low pressure; external atmospheric pressure pushes the liquid up the straw", ["The mouth pulls liquid using magnetic force", "The straw heats the juice into steam", "Gravity reverses inside the plastic tube"]),
            ("What happens when air is pumped out from inside a closed tin can containing boiling water that has been sealed and cooled?", "The tin can crumples and crushes violently inward due to the large unbalanced external atmospheric pressure", ["The tin can expands like a balloon", "The tin can melts into a puddle", "The can remains unaffected"]),
            ("Which scientific instrument was invented by Evangelista Torricelli in 1643 to measure atmospheric pressure using a column of mercury?", "Mercury Barometer", ["Hydrometer", "Sphygmomanometer", "Anemometer"])
        ],
        "CBSE-8-CURI-6-6.2.3": [
            ("How does hydrostatic pressure in a stationary liquid vary with depth below the liquid surface?", "Pressure increases directly with depth according to \\(P = \\rho \\times g \\times h\\) (greater depth means greater overlying liquid weight)", ["Pressure decreases with depth", "Pressure is constant everywhere in liquid", "Pressure drops to zero at the bottom"]),
            ("Why are concrete dam walls built much thicker and wider at the base than at the top?", "Water pressure increases drastically with depth, exerting tremendous horizontal thrust on the deep bottom foundation", ["To save concrete at the top", "To build a wide road on the crest", "To prevent fish from jumping over"]),
            ("Liquid in a container exerts pressure:", "In all directions (downward on the base, upward, and sideways on the container walls) equally at a given depth", ["Only straight downward on the bottom floor", "Only upward towards the sky", "Only along the surface boundary"]),
            ("If three holes at different heights are punched into the side of a tall water bottle, what is observed regarding the water jets?", "Water spouts out farthest and with greatest velocity from the lowest hole, where hydrostatic pressure is highest", ["Water spouts farthest from the top hole", "All three jets travel identical distances", "Water flows only from the middle hole"])
        ],
        "CBSE-8-CURI-6-6.3.1": [
            ("What is 'wind' scientifically defined as in earth science?", "Air in horizontal motion across the Earth's surface driven by atmospheric pressure differences", ["A static layer of warm air", "Evaporating ocean steam", "The magnetic flow of solar flares"]),
            ("What fundamental natural driving force causes air to blow as wind from one geographical region to another?", "Pressure gradients: air always moves naturally from high-pressure regions to low-pressure regions", ["Air moves from low pressure to high pressure", "Air is attracted to mountains by gravity", "Earth's core pulls air westward"]),
            ("Which meteorological instrument measures the speed of wind, and which indicates wind direction?", "An Anemometer measures wind speed, and a Wind Vane (weather cock) indicates wind direction", ["A barometer measures speed, a thermometer indicates direction", "A hydrometer measures speed, a rain gauge indicates direction", "A seismograph measures both"]),
            ("The greater the difference in atmospheric pressure between two geographic areas:", "The faster and more violently the wind blows between them", ["The slower the wind moves", "The colder the air becomes instantly", "Wind stops blowing entirely"])
        ],
        "CBSE-8-CURI-6-6.3.2": [
            ("What happens to air when it is heated by solar radiation or a heat source?", "Air expands, its volume increases, and its density decreases (warm air becomes lighter and rises)", ["Air contracts and falls downward", "Air turns into liquid nitrogen", "Air mass increases"]),
            ("Why do smoke and hot flue gases rise upward through factory chimneys and kitchen exhaust vents?", "Hot air and smoke are much less dense (lighter) than the cooler surrounding ambient air, generating natural upward buoyancy", ["Smoke is attracted by the sky's gravity", "Chimneys suck air like vacuum pumps", "Smoke has zero temperature"]),
            ("When an empty plastic bottle with a deflated balloon stretched over its mouth is placed in a hot water tub, what happens?", "The balloon inflates because air trapped inside the bottle expands upon heating", ["The balloon is sucked into the bottle", "The bottle melts into glass", "The balloon shrinks"]),
            ("Cool air is heavier (denser) than warm air, so in the atmosphere cool air naturally:", "Sinks downward towards the Earth's surface, creating a local high-pressure region", ["Rises into space", "Burns into carbon dioxide", "Forms cumulus storm clouds"])
        ],
        "CBSE-8-CURI-6-6.3.3": [
            ("How are atmospheric convection currents generated in nature?", "Warm surface air expands and rises, while surrounding cooler, denser air rushes in horizontally to replace it, establishing a continuous cyclic circulation", ["By underground magma boiling rivers", "By the spinning of electric turbine fans", "By tidal waves pushing air"]),
            ("What role do atmospheric convection currents play in global weather patterns?", "They transport massive amounts of heat energy and moisture from equatorial tropics towards polar regions, regulating Earth's climate", ["They stop the Earth from rotating", "They prevent sunlight from reaching clouds", "They freeze tropical oceans"]),
            ("Why are domestic room heaters placed near the floor while air conditioner cooling units are installed high on walls?", "Warm air from floor heaters rises naturally to heat the room, while cold dense air from high AC vents sinks downward, creating efficient convection", ["Heaters look better near carpets", "Air conditioners need roof water", "Cold air rises and hot air sinks"]),
            ("Glider pilots and soaring birds like eagles can stay airborne for hours without flapping wings by riding:", "Rising columns of warm air called thermal convection currents (thermals)", ["High-altitude jet stream vacuums", "Earth's magnetic field lines", "Cold descending downdrafts"])
        ],
        "CBSE-8-CURI-6-6.3.4": [
            ("Why does land heat up much faster than adjacent seawater during sunny daytime hours?", "Land (soil and rock) has a substantially lower specific heat capacity than water, heating up and cooling down much more rapidly", ["Land absorbs 100% of cosmic rays", "Water reflects all sunlight", "Land is closer to the Sun"]),
            ("What causes a 'Sea Breeze' to blow along coastal areas during sunny daytime afternoons?", "Air over warm land rises, creating a low-pressure zone; cooler, denser air from above the sea moves inland to replace it", ["Warm air from the ocean blows onto cold land", "Tidal waves push wind onshore", "Underground ocean caves exhale air"]),
            ("What causes a 'Land Breeze' to blow along coastal regions during the night?", "At night, land cools faster than the sea; warmer air over the sea rises, drawing cooler air from the land out towards the sea", ["The moon attracts air toward the ocean", "Night waves create a vacuum", "Plants release nitrogen outward"]),
            ("The massive seasonal monsoon wind system that brings torrential rains to the Indian subcontinent is essentially:", "A giant continental-scale seasonal sea breeze driven by extreme differential heating between the Asian landmass and the Indian Ocean", ["A polar blizzard from Antarctica", "A volcanic eruption cloud", "A permanent hurricane"])
        ],
        "CBSE-8-CURI-6-6.3.5": [
            ("Why do global wind circulation patterns develop across the Earth rather than winds blowing strictly North-South?", "The Earth's spherical shape causes uneven solar heating (warm equator vs cold poles), and planetary rotation causes the Coriolis effect deflecting winds", ["The Moon's gravity pushes winds eastward", "Oceans are tilted at 45 degrees", "Global winds follow airplane flight paths"]),
            ("In the equatorial tropical belt (between \\(0^\\circ\\) and \\(30^\\circ\\) latitude), intense solar heating causes air to rise, producing:", "A permanent low-pressure equatorial belt (Intertropical Convergence Zone) where Trade Winds converge", ["A permanent polar ice desert", "Dry high-pressure downdrafts", "Zero cloud formation"]),
            ("The deflection of global wind currents to the right in the Northern Hemisphere and to the left in the Southern Hemisphere is caused by:", "The Coriolis Effect resulting from Earth's eastward axial rotation", ["The gravitational pull of Venus", "Solar flare magnetic attraction", "The shape of ocean continents"]),
            ("Subtropical belts around \\(30^\\circ\\text{N}\\) and \\(30^\\circ\\text{S}\\) where descending cool, dry air creates high pressure and arid conditions are associated with:", "Major global deserts (like the Sahara, Arabian, and Thar deserts)", ["Tropical rainforests", "Permafrost tundra", "Amazon river deltas"])
        ],
        "CBSE-8-CURI-6-6.4.1": [
            ("According to Bernoulli's principle in fluid dynamics, what happens to the static pressure of a moving fluid (like air) when its speed increases?", "High fluid velocity is accompanied by a simultaneous DECREASE in fluid static pressure", ["Static pressure increases exponentially", "Static pressure remains strictly constant", "Fluid velocity has no effect on pressure"]),
            ("When high-speed storm winds blow violently over the roof of a house, what localized pressure conditions develop?", "Air pressure immediately above the roof drops severely due to high wind speed, while normal high atmospheric pressure remains trapped inside the house", ["Pressure above the roof becomes infinite", "Pressure inside the house drops to zero", "Both pressures remain identical"]),
            ("In aerodynamic lift on an aircraft wing (aerofoil), the curved upper surface forces air to flow faster over the top than the bottom, generating:", "Lower pressure on top than below, resulting in a net upward aerodynamic lift force supporting the aircraft", ["Downward suction pushing the plane down", "Backward drag pulling the wings off", "Extreme heating of the aluminum wing"]),
            ("Why are modern racing cars designed with aerodynamic wings and spoilers?", "To create downward aerodynamic force (downforce) that presses the tires firmly against the track, increasing traction at high speeds", ["To make the car lighter than air", "To reflect headlights of competitors", "To catch rain for the radiator"])
        ],
        "CBSE-8-CURI-6-6.4.2": [
            ("When a student holds a strip of paper horizontally just below their bottom lip and blows hard horizontally OVER the top surface, what happens?", "The paper strip lifts upward into the horizontal airstream", ["The paper strip droops straight down", "The paper strip bursts into flame", "The paper strip tears in half"]),
            ("Why does the paper strip lift upward when blown over horizontally?", "Blowing creates high air velocity above the strip, reducing pressure above; higher atmospheric pressure below pushes the paper up", ["The student's breath is hot and buoyant", "The breath is magnetic", "Static electricity attracts the paper to the mouth"]),
            ("When two ping-pong balls are suspended side-by-side by light threads a few centimeters apart and air is blown between them, what happens?", "The two balls move towards each other and collide", ["The two balls fly apart in opposite directions", "The balls spin around each other without moving closer", "The balls drop to the floor"]),
            ("Why do the two suspended ping-pong balls move towards each other when air is blown through the narrow gap between them?", "High air velocity in the gap reduces pressure between them, and the higher outer atmospheric pressure pushes the balls inward", ["The air forms a vacuum that sucks rubber", "The balls become charged with opposite static electricity", "Air drag pulls threads together"])
        ],
        "CBSE-8-CURI-6-6.4.3": [
            ("During a severe cyclone or gale storm, why are corrugated tin and asbestos roofs often blown off and carried away into the sky?", "High-speed winds across the roof create very low pressure above; higher indoor pressure beneath the roof blows it upward like a projectile", ["The wind pulls the roof down into the basement", "Rainwater makes the roof too heavy to stay", "Lightning melts the supporting iron pillars"]),
            ("What practical architectural measure helps prevent lightweight roofs from being ripped off during cyclonic windstorms?", "Ensuring proper indoor ventilation or anchoring roof trusses firmly to reinforced concrete tie-beams with hurricane straps", ["Sealing every door and window completely airtight", "Painting the roof bright red", "Covering the roof with wet straw"]),
            ("Why should a person standing on a railway platform never stand too close to a fast-passing express train?", "The high-speed train creates a zone of low air pressure alongside it, and higher atmospheric pressure behind the person can push them towards the train", ["The train emits harmful radioactive waves", "The train's magnetic wheels pull clothing", "The train will suck the ground away"]),
            ("A perfume atomizer or paint spray gun operates on Bernoulli's principle by:", "Blowing a high-speed air jet over the top of a dip tube, dropping pressure and drawing liquid up to be atomized into a fine spray", ["Boiling perfume into steam", "Using an internal diesel combustion piston", "Magnetizing the liquid drops"])
        ],
        "CBSE-8-CURI-6-6.5.1": [
            ("How does a typical thunderstorm initiate in the atmosphere?", "Rapid vertical ascent of warm, humid surface air on hot days forms towering cumulonimbus clouds with strong internal updrafts and downdrafts", ["Cold dry winter air settles over mountains", "A sudden solar eclipse cools the stratosphere", "Ocean currents stop flowing"]),
            ("Inside an active thunderstorm cloud, violent friction occurs between rising warm air moisture and descending hail/ice pellets, causing:", "Massive separation and accumulation of static electrical charges within the cloud", ["Chemical synthesis of crude oil", "Nuclear transmutation of nitrogen into gold", "Total consumption of atmospheric oxygen"]),
            ("Why are thunderstorms frequently accompanied by torrential rainfall, heavy lightning flashes, and booming thunderclaps?", "Rapid condensation releases latent heat fueling violent convection, while massive electrical discharges heat air channels explosively", ["Thunder is caused by clouds physically smashing together like solid rocks", "Rain is produced by aeroplanes spraying salt", "Lightning is sunlight focused through ice prisms"]),
            ("During an outdoor thunderstorm, what is the safest emergency action if caught in an open field with no buildings nearby?", "Squat low on the balls of your feet with your head tucked between knees and hands covering ears, minimizing contact with the ground", ["Stand tall holding an open metal-tipped umbrella", "Take shelter under a solitary tall tree", "Lie completely flat in a puddle of water"])
        ],
        "CBSE-8-CURI-6-6.5.2": [
            ("In a towering thunderstorm cumulonimbus cloud, how do static electric charges typically separate and distribute?", "Positive charges accumulate near the upper cold regions of the cloud, while heavy negative charges gather near the lower cloud base", ["Positive charges gather only on the ground", "The cloud has only negative charges throughout", "Charges alternate randomly every second"]),
            ("What is a lightning flash fundamentally defined as in atmospheric physics?", "A colossal, high-voltage electric spark discharge between oppositely charged regions of clouds or between a cloud and the Earth", ["A beam of pure laser light from space", "Burning phosphorus dust in the sky", "A meteor burning up in the ozone layer"]),
            ("What causes the deafening booming sound of thunder that follows a lightning flash?", "The intense lightning bolt heats the surrounding air channel instantly to nearly \\(30{,}000\\ \\text{K}\\), causing explosive thermal expansion and shockwaves", ["Clouds colliding like solid cymbal plates", "Thunderbolts cracking solid rocks on mountain peaks", "Sound waves produced by falling raindrops"]),
            ("Why is the flash of lightning seen several seconds BEFORE the sound of thunder is heard, even though both occur simultaneously?", "Light travels through air at the speed of light (\\(300{,}000\\ \\text{km/s}\\)), whereas sound travels much slower at roughly \\(340\\ \\text{m/s}\\)", ["Thunder is generated only after lightning hits the ground", "The human ear takes 5 seconds to process sound", "Lightning travels along curved tracks while thunder travels straight"])
        ],
        "CBSE-8-CURI-6-6.5.3": [
            ("What is the function of a metallic Lightning Conductor installed on the highest point of tall buildings and historical monuments?", "To provide an unobstructed, low-resistance metallic path (copper rod/strip) that safely conducts lightning electrical discharge into the deep earth", ["To repel storm clouds with magnetic force", "To store lightning energy in household batteries", "To catch rainwater for gardens"]),
            ("How is the lower terminal of a lightning conductor safely grounded into the Earth?", "Connected to a thick copper plate buried deep in moist soil surrounded by charcoal and salt (earthing)", ["Tied to a wooden window frame", "Left dangling in the rooftop air", "Connected to the home electrical switchboard"]),
            ("Why is taking shelter beneath a tall, isolated tree during a thunderstorm extremely dangerous?", "Tall isolated trees are natural targets for lightning strikes, and current can jump sideways (side-flash) or travel through ground to nearby persons", ["The tree will drop heavy coconuts", "The tree leaves emit toxic carbon monoxide", "Tree roots attract rain"]),
            ("Why is talking on a corded landline telephone or bathing under a metal shower faucet discouraged during a severe lightning storm?", "Lightning strikes on outdoor utility lines or plumbing can conduct dangerous high-voltage electrical surges directly into the house", ["Water dissolves telephone signals", "The telephone speaker attracts thunder sound", "Metal faucets become magnetized"])
        ],
        "CBSE-8-CURI-6-6.6.1": [
            ("What is a tropical cyclone fundamentally defined as in meteorology?", "A massive, violently rotating low-pressure atmospheric storm system characterized by spiral gale winds, heavy rains, and a calm central 'eye'", ["A high-pressure anticyclone with clear sunny skies", "A local gentle afternoon sea breeze", "A dust storm confined to a desert"]),
            ("The calm, cloudless, low-wind circular central region of a fully developed tropical cyclone is termed the:", "Eye of the cyclone", ["Eye wall", "Spiral rainband", "Storm surge"]),
            ("Surrounding the calm central eye is the most violent, dangerous sector of the cyclone containing ferocious winds and torrential downpours called the:", "Eye wall", ["Outer feeder band", "Anticyclone ridge", "Stratospheric anvil"]),
            ("What is the approximate diameter of the calm central eye and the overall storm circulation of a mature tropical cyclone?", "Eye diameter is \\(10\\ \\text{to}\\ 30\\ \\text{km}\\), while the entire cyclone circulation spans \\(150\\ \\text{to}\\ 1000\\ \\text{km}\\)", ["Eye is 1 meter, storm is 100 meters", "Eye is 5000 km, storm is 10,000 km", "Eye spans the entire Indian Ocean"])
        ],
        "CBSE-8-CURI-6-6.6.2": [
            ("What is the primary thermodynamic 'fuel' and energy source that powers the birth and intensification of tropical cyclones?", "Latent heat of condensation released when vast amounts of warm ocean water evaporate (ocean surface temperature \\(\\ge 26.5^\\circ\\text{C}\\))", ["Volcanic heat from deep ocean hydrothermal vents", "Combustion of methane gas released from ocean floor", "Frictional heat of ocean waves"]),
            ("Which combination of meteorological factors is essential for the formation and development of a tropical cyclone?", "Warm ocean surface temperature (\\(\\ge 26.5^\\circ\\text{C}\\)), high atmospheric humidity, low vertical wind shear, and sufficient Coriolis force", ["Freezing polar water and zero humidity", "Extremely high vertical wind shear that tears clouds apart", "Presence of mountain ranges on the ocean floor"]),
            ("Why do tropical cyclones quickly weaken, dissipate, and die out once they make landfall and move over continental landmasses?", "They are cut off from their primary moisture and heat energy source (warm ocean water) and encounter high surface frictional drag from terrain", ["Land has too much oxygen", "The cyclone freezes over mountains", "The eye of the cyclone fills with solid rock"]),
            ("What are tropical cyclones called in the Atlantic and North-East Pacific Oceans, and in the North-West Pacific (around Japan and Philippines), respectively?", "Hurricanes in the Atlantic, and Typhoons in the North-West Pacific", ["Tornadoes and Blizzards", "Monsoons and Dust devils", "Gales and Squalls"])
        ],
        "CBSE-8-CURI-6-6.6.3": [
            ("What catastrophic coastal phenomenon caused by a tropical cyclone is responsible for the greatest loss of human life and property?", "Storm Surge: an abnormal, colossal rise of sea water pushed inland by ferocious winds and extremely low central barometric pressure", ["Sudden earthquake on the beach", "Freezing of coastal rivers into glaciers", "Formation of sand dunes overnight"]),
            ("Severe cyclone winds (often exceeding \\(150\\ \\text{to}\\ 250\\ \\text{km/h}\\)) cause widespread destruction by:", "Uprooting mature trees, tearing down overhead electric power and telecom lines, and destroying houses and infrastructure", ["Turning fertile farmland into solid glass", "Melting concrete buildings into liquid", "Evaporating all coastal drinking water wells"]),
            ("Inland torrential rainfall accompanying cyclones commonly leads to secondary disasters such as:", "Catastrophic riverine flooding, submergence of agricultural crops, landslides in hilly terrain, and waterborne disease epidemics", ["Severe agricultural drought and dust storms", "Forest fires triggered by extreme dry heat", "Volcanic ash eruptions"]),
            ("Following a devastating cyclonic disaster, public health authorities prioritize which measure to prevent cholera and gastroenteritis outbreaks?", "Distributing halogen/chlorine water purification tablets and ensuring safe boiled drinking water and emergency vaccination", ["Spraying perfumes across the city", "Encouraging drinking of raw flood water", "Shutting down all medical dispensaries"])
        ],
        "CBSE-8-CURI-6-6.6.4": [
            ("Which modern space technology provides continuous real-time tracking, satellite imagery, and early detection of cyclones over open oceans?", "Geostationary and Polar-orbiting Meteorological Earth Observation Satellites (such as INSAT and Kalpana)", ["Deep-space radio telescopes looking at distant stars", "Seismological underground sensors", "Submarine sonar tracking whales"]),
            ("What role do coastal Doppler Weather Radars (DWR) play in modern cyclone warning and disaster preparedness?", "They track the precise track, intensity, internal wind velocity, and heavy rainfall structure of a cyclone within a 400 km radius as it approaches coastlines", ["They shoot laser beams to destroy the storm clouds", "They warm the ocean water to calm the storm", "They predict earthquakes 5 years in advance"]),
            ("In India, which premier meteorological agency is officially mandated to monitor, track, and issue national cyclone forecasts and color-coded alerts?", "India Meteorological Department (IMD)", ["Geological Survey of India (GSI)", "National Dairy Development Board (NDDB)", "Oil and Natural Gas Corporation (ONGC)"]),
            ("What is the standard standard lead-time timeline for IMD's 'Cyclone Alert' and 'Cyclone Warning' bulletins prior to expected landfall?", "Cyclone Alert issued 48 hours in advance; Cyclone Warning issued at least 24 hours in advance", ["Issued 10 minutes before the storm arrives", "Issued only after the cyclone has completely passed", "Issued 6 months in advance"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 7 DATA
    # -------------------------------------------------------------------------
    ch7_cases = {
        "CBSE-8-CURI-7-7.1.1": [
            ("According to the modern particulate theory of matter, matter is composed of:", "Extremely tiny discrete constituent particles (atoms and molecules) that cannot be seen with ordinary microscopes", ["A continuous, unbroken solid jelly with no spaces", "Pure void with zero mass", "Solid light rays"]),
            ("Ancient Indian philosopher Acharya Kanada in the 6th century BCE postulated that all matter is composed of indestructible, indivisible particles named:", "Parmanu (or Anu)", ["Dalton", "Molecule", "Electron"]),
            ("Which simple experiment proves that particles of matter are unimaginably tiny?", "A tiny purple crystal of potassium permanganate (\\(\\text{KMnO}_4\\)) can impart distinct pink color to hundreds of litres of diluted water", ["Burning a piece of paper", "Measuring the boiling point of milk", "Melting an ice cube"]),
            ("Approximately how many water molecules are estimated to be present in a single tiny drop of water (about \\(0.05\\ \\text{mL}\\))?", "Approximately \\(10^{21}\\) molecules (more than a billion trillion molecules)", ["About 100 molecules", "About 5,000 molecules", "Zero molecules"])
        ],
        "CBSE-8-CURI-7-7.1.2": [
            ("When a teaspoon of table salt or sugar is completely dissolved in a glass of water, the liquid level does NOT increase. What does this demonstrate?", "Particles of water have vacant spaces (interparticle spaces) between them into which the solute particles disperse and fit", ["Salt particles disappear completely from the universe", "Water molecules shrink in volume", "Salt turns into invisible gas"]),
            ("When \\(50\\ \\text{mL}\\) of pure water and \\(50\\ \\text{mL}\\) of pure ethyl alcohol are mixed, the resulting total volume is slightly less than \\(100\\ \\text{mL}\\) (about \\(96\\ \\text{mL}\\)). Why?", "Smaller water molecules fit snugly into the vacant intermolecular voids between larger alcohol molecules", ["Four millilitres of liquid evaporate instantly", "Alcohol destroys water atoms", "Chemical combustion consumes mass"]),
            ("The vacant gaps or distances present between neighboring particles of matter are termed:", "Interparticle (or intermolecular) spaces", ["Atomic nuclei", "Chemical bonds", "Capillary voids"]),
            ("In which state of matter are the interparticle spaces the SMALLEST and most restricted?", "Solid state (particles are closely packed in rigid order)", ["Gaseous state", "Liquid state", "Plasma state"])
        ],
        "CBSE-8-CURI-7-7.1.3": [
            ("When an unlit incense stick (agarbatti) is kept in a room, you must go close to smell it, but when lit, its fragrance fills the entire room within seconds. Why?", "Heating increases the kinetic energy and thermal speed of fragrance particles, causing rapid diffusion into air molecules", ["Fire creates new perfume elements", "Smoke is heavier than air and sinks", "The stick burns into liquid"]),
            ("The spontaneous, passive intermingling and intermixing of particles of two different substances on their own is termed:", "Diffusion", ["Osmosis", "Sublimation", "Evaporation"]),
            ("What is the random, irregular, zigzag microscopic motion of suspended pollen grains or smoke particles in a fluid called?", "Brownian motion (discovered by botanist Robert Brown in 1827)", ["Newtonian linear motion", "Coriolis rotation", "Periodic oscillation"]),
            ("What causes the erratic zigzag trajectory of smoke particles observed under a microscope during Brownian motion?", "Continuous, uneven, random bombardments by invisible, rapidly moving air molecules colliding with the smoke particle from all directions", ["Convection currents from room heaters", "Static electrical repulsion of smoke", "Gravitational fluctuations"])
        ],
        "CBSE-8-CURI-7-7.1.4": [
            ("What fundamental forces hold the constituent particles of matter together in definite volumes and shapes?", "Interparticle (intermolecular) forces of attraction", ["Gravitational attraction between nuclei only", "Nuclear strong forces", "Centrifugal repulsion"]),
            ("The attractive force operating between particles of the SAME substance (such as water molecule to water molecule) is called:", "Cohesive force (cohesion)", ["Adhesive force", "Frictional drag", "Magnetic dipoles"]),
            ("The attractive force operating between particles of DIFFERENT substances (such as water molecules sticking to a clean glass tumbler wall) is called:", "Adhesive force (adhesion)", ["Cohesive force", "Surface tension", "Gravitational pull"]),
            ("Why is an iron nail extremely difficult to break by hammering compared to a stick of chalk or a rubber eraser?", "Cohesive interparticle forces of attraction between iron atoms are immensely stronger than those in chalk or rubber", ["Iron contains no atoms", "Chalk has no mass", "Rubber has zero friction"])
        ],
        "CBSE-8-CURI-7-7.2.1": [
            ("Which of the following physical characteristics uniquely defines the Solid state of matter?", "Definite shape, definite volume, high density, and negligible compressibility", ["Definite volume but no fixed shape", "Neither definite shape nor definite volume", "Infinite compressibility and zero density"]),
            ("Why do solid objects (like a wooden block, iron bar, or stone) possess a rigid, fixed shape?", "Constituent particles are closely packed in fixed geometric positions with very strong attractive forces, only vibrating about their mean positions", ["Particles move freely at high speed throughout the solid", "Solids have no interparticle attraction", "Solids contain zero heat energy"]),
            ("What type of internal motion is performed by atoms or molecules inside a solid at room temperature?", "Vibrational motion back and forth about their fixed mean lattice positions", ["Translational motion across the entire container", "Rotational free roaming throughout space", "Zero movement whatsoever"]),
            ("Can a solid block of copper metal be compressed significantly by squeezing with human hands?", "No, solids exhibit negligible compressibility because their interparticle spaces are already minimal", ["Yes, copper can be squeezed like a sponge", "Only if dipped in oil", "Yes, by 90%"])
        ],
        "CBSE-8-CURI-7-7.2.2": [
            ("Which physical properties characterize the Liquid state of matter?", "Definite volume, no fixed shape (takes the shape of the container), and can flow easily (fluidity)", ["Definite shape and infinite compressibility", "Neither definite shape nor definite volume", "Rigid structure like crystal"]),
            ("Why does water take the shape of whichever vessel (glass, bowl, or flask) it is poured into?", "Interparticle forces in liquids are weaker than in solids, allowing particles to slide, glide, and tumble past one another freely", ["Liquid particles have no mass", "Water molecules dissolve glass", "Liquids have zero density"]),
            ("Do liquids possess a fixed, definite volume at a constant temperature?", "Yes, liquids have a definite volume; \\(500\\ \\text{mL}\\) of milk remains \\(500\\ \\text{mL}\\) whether poured into a jug, bowl, or pan", ["No, liquid volume changes with container shape", "Liquid volume becomes zero in open air", "Volume doubles when poured"]),
            ("Substances in the liquid and gaseous states that have the ability to flow easily are collectively called:", "Fluids", ["Solids", "Crystals", "Minerals"])
        ],
        "CBSE-8-CURI-7-7.2.3": [
            ("Which physical properties uniquely describe the Gaseous state of matter?", "Neither a definite shape nor a definite volume, filling the entire volume of any container, and highly compressible", ["Definite shape and definite volume", "Definite volume but fixed shape", "Non-fluid rigid structure"]),
            ("Why does a small puff of cooking gas or perfume spread and expand to occupy the entire volume of a room?", "Interparticle attractive forces in gases are virtually negligible, and gas particles move at high velocities in all random directions", ["Gases are attracted to room walls by magnets", "Gases have higher density than liquids", "Gases have fixed crystalline lattices"]),
            ("What produces the continuous pressure exerted by a gas on the internal walls of its enclosing container (like an inflated football)?", "Continuous, rapid bombardments and collisions of billions of gas particles striking the container walls per unit area", ["The chemical corrosion of the rubber by oxygen", "Static electric sparks jumping across air", "Gravitational weight of the air column alone"]),
            ("In which state of matter do constituent particles possess the MAXIMUM kinetic energy and highest speeds at a given temperature?", "Gaseous state", ["Liquid state", "Solid state", "Frozen state"])
        ],
        "CBSE-8-CURI-7-7.3.1": [
            ("What is the correct increasing order of interparticle spaces among the three fundamental states of matter?", "\\(\\text{Solids} < \\text{Liquids} < \\text{Gases}\\)", ["\\(\\text{Gases} < \\text{Liquids} < \\text{Solids}\\)", "\\(\\text{Liquids} < \\text{Solids} < \\text{Gases}\\)", "\\(\\text{Solids} = \\text{Liquids} = \\text{Gases}\\)"]),
            ("What is the correct increasing order of interparticle forces of attraction among the three states of matter?", "\\(\\text{Gases} < \\text{Liquids} < \\text{Solids}\\)", ["\\(\\text{Solids} < \\text{Liquids} < \\text{Gases}\\)", "\\(\\text{Liquids} < \\text{Gases} < \\text{Solids}\\)", "\\(\\text{Gases} = \\text{Solids} < \\text{Liquids}\\)"]),
            ("What is the correct increasing order of particle kinetic energy and freedom of movement among the three states of matter at room temperature?", "\\(\\text{Solids} < \\text{Liquids} < \\text{Gases}\\)", ["\\(\\text{Gases} < \\text{Solids} < \\text{Liquids}\\)", "\\(\\text{Liquids} < \\text{Gases} < \\text{Solids}\\)", "\\(\\text{Solids} = \\text{Gases} < \\text{Liquids}\\)"]),
            ("What is the correct order of the rate of diffusion of matter across the three physical states?", "\\(\\text{Gases} > \\text{Liquids} > \\text{Solids}\\)", ["\\(\\text{Solids} > \\text{Liquids} > \\text{Gases}\\)", "\\(\\text{Liquids} > \\text{Gases} > \\text{Solids}\\)", "\\(\\text{Solids} = \\text{Liquids}\\)"])
        ],
        "CBSE-8-CURI-7-7.3.2": [
            ("Why can a large volume of natural gas or oxygen be compressed and packed into small, portable steel cylinders (CNG/LPG)?", "Gases have enormous interparticle spaces between molecules, allowing them to be pushed much closer together under pressure", ["Gas molecules shrink in diameter", "Gases turn into solid steel", "Gas atoms lose all electrons"]),
            ("If you take three identical \\(100\\ \\text{mL}\\) plastic syringes filled respectively with chalk powder (solid), water (liquid), and air (gas), which piston is easiest to push in?", "The syringe containing air (gas), because gases are highly compressible", ["The syringe containing chalk powder", "The syringe containing water", "All three pistons move equally easily"]),
            ("Why are liquids like water or hydraulic oil considered virtually INCOMPRESSIBLE for practical engineering purposes?", "Interparticle spaces in liquids are already very small; pushing particles closer encounters strong electrostatic repulsion between electron clouds", ["Liquids have infinite void space", "Liquids turn into gas when pressed", "Liquid particles have no mass"]),
            ("Hydraulic brake systems in automobiles and hydraulic excavators utilize which property of liquids?", "Incompressibility of liquids, allowing pressure applied at one point to be transmitted undiminished throughout the fluid (Pascal's Principle)", ["High compressibility like air", "Rapid evaporation into gas", "Chemical decomposition into ions"])
        ],
        "CBSE-8-CURI-7-7.3.3": [
            ("What effect does heating (increasing temperature) have on the constituent particles of any substance?", "Increases the average kinetic energy and vibrational/translational speed of the particles", ["Decreases their kinetic energy to zero", "Increases the mass of the particles", "Slows down particle motion"]),
            ("Why does the rate of diffusion of potassium permanganate crystals in hot water occur much faster than in cold water?", "Higher temperature imparts greater kinetic energy to water and solute particles, causing more vigorous collisions and faster dispersion", ["Hot water dissolves glass", "Potassium permanganate freezes in cold water", "Cold water has no particles"]),
            ("What happens to the intermolecular forces of attraction when a solid is heated towards its melting point?", "Thermal vibrations become vigorous enough to overcome and loosen the rigid attractive forces holding particles in fixed lattice positions", ["Attractive forces become infinitely strong", "Particles stop moving completely", "Atoms split into radioactive isotopes"]),
            ("Why do hot sizzling food aromas reach our nostrils several metres away, whereas the smell of cold food requires us to get close?", "Vapor particles from hot food have high kinetic energy, diffusing rapidly through air molecules at high velocity", ["Hot food emits radio waves", "Cold food contains no molecules", "Cold food has zero smell"])
        ],
        "CBSE-8-CURI-7-7.3.4": [
            ("The phase transition process by which a solid changes into a liquid upon heating at constant temperature is termed:", "Melting (or Fusion)", ["Boiling (Vaporization)", "Freezing (Solidification)", "Sublimation"]),
            ("The phase transition process by which a liquid changes into a gas throughout the bulk of the liquid at its boiling point is:", "Boiling (Vaporization)", ["Melting", "Condensation", "Deposition"]),
            ("The direct conversion of a solid into a vapor state upon heating without passing through the intermediate liquid state is called:", "Sublimation", ["Condensation", "Evaporation", "Fusion"]),
            ("Which of the following substances undergoes sublimation at room conditions, disappearing completely without leaving any liquid residue?", "Camphor, Naphthalene balls, and Ammonium chloride", ["Common table salt", "Granulated white sugar", "Iron nails"])
        ]
    }

    # Generate Chapters 5, 6, 7
    for ch_num, cases_dict in [(5, ch5_cases), (6, ch6_cases), (7, ch7_cases)]:
        item = next(x for x in manifest if str(x["chapterNumber"]) == str(ch_num))
        ch_questions = []
        start_seq = 300
        for lf in item["leafs"]:
            tc = lf["topicCode"]
            needed = lf["needed"]
            sub_name = lf["name"]
            if needed == 0:
                continue
            cases = cases_dict[tc]
            vaults, diffs = get_vaults_and_diffs(needed)

            for i in range(needed):
                ctx, ans, wrongs = cases[i % len(cases)]
                step1 = f"Identify the scientific concept relating to {sub_name}."
                step2 = f"Evaluate key principles: {ctx}"
                step3 = f"Therefore, the correct answer is {ans}."
                q = make_question(tc, sub_name, ctx, ans, wrongs, step1, step2, step3, diffs[i], vaults[i], start_seq)
                start_seq += 1
                ch_questions.append(q)

        out_path = f"scripts/cbse8_curi_ch{ch_num}_topup.json"
        with open(out_path, "w", encoding="utf-8") as out_f:
            json.dump(ch_questions, out_f, indent=2)
        print(f"Generated {len(ch_questions)} questions for Chapter {ch_num} -> {out_path}")

if __name__ == "__main__":
    run()
