# -*- coding: utf-8 -*-
"""
Chapter 19 Topic 19.2 Gold-Standard Question Authoring Engine
Class 9 Science & Technology: Class 7 Science Foundation Core
Topic 19.2: Motion, Force, Work, Heat & Static Electricity (7th Review)
Total: 40 brand-new gold-standard questions (20 OSC, 8 OTF, 6 OAR, 6 OMC)
"""

import json
from datetime import datetime, timezone

qs_t2 = []

# --- 20 OSC QUESTIONS ---
osc_t2 = [
    {
        "code": "MH-9-SCIT-19-19.2-OSC-001",
        "text": "A car travels a total distance of \\(180\\text{ km}\\) in \\(3\\text{ hours}\\). What is the average speed of the car?",
        "options": ["\\(50\\text{ km/h}\\)", "\\(60\\text{ km/h}\\)", "\\(90\\text{ km/h}\\)", "\\(540\\text{ km/h}\\)"],
        "ca": "B",
        "concept": "Average speed is calculated as total distance traversed divided by the total time taken: \\(\\text{Speed} = \\frac{\\text{Distance}}{\\text{Time}}\\).",
        "analysis": [
            "Incorrect; \\(180 / 3 = 60\\), not 50.",
            "\\(\\text{Speed} = \\frac{180\\text{ km}}{3\\text{ h}} = 60\\text{ km/h}\\).",
            "Incorrect; 90 corresponds to a 2-hour duration.",
            "Incorrect; 540 is the product of distance and time."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-002",
        "text": "Which type of motion is exhibited by the bob of an oscillating simple pendulum swinging to and fro?",
        "options": ["Circular non-periodic motion", "Oscillatory and periodic motion", "Random motion", "Linear uniform motion"],
        "ca": "B",
        "concept": "The motion of a pendulum bob repeatedly moving back and forth about an equilibrium position at regular intervals is classified as oscillatory and periodic motion.",
        "analysis": [
            "Incorrect; the motion does not complete full circles and is strictly periodic.",
            "The bob executes to-and-fro oscillatory motion that repeats at fixed time intervals (periodic).",
            "Incorrect; the trajectory is regular and harmonic, not random.",
            "Incorrect; the path is an arc, not a straight line."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-003",
        "text": "A constant force of \\(25\\text{ N}\\) acts on a box, displacing it through \\(4\\text{ m}\\) in the direction of the force. What is the work done?",
        "options": ["\\(100\\text{ J}\\)", "\\(29\\text{ J}\\)", "\\(6.25\\text{ J}\\)", "\\(200\\text{ J}\\)"],
        "ca": "A",
        "concept": "Work done by a force acting in the direction of motion is given by \\(W = F \\times s\\), where work is expressed in Joules (\\(\\text{J}\\)).",
        "analysis": [
            "\\(W = F \\times s = 25\\text{ N} \\times 4\\text{ m} = 100\\text{ J}\\).",
            "Incorrect; force and displacement are multiplied, not added.",
            "Incorrect; force is multiplied by displacement, not divided.",
            "Incorrect; 200 corresponds to double the actual displacement."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-004",
        "text": "Which class of lever has the fulcrum positioned in between the effort and the load (e.g., a pair of scissors or a seesaw)?",
        "options": ["Class 1 lever", "Class 2 lever", "Class 3 lever", "Compound pulley"],
        "ca": "A",
        "concept": "In a Class 1 lever, the fulcrum (F) lies between the effort (E) and the load (L), allowing the mechanical advantage to be greater than, equal to, or less than 1.",
        "analysis": [
            "In a Class 1 lever (e.g. scissors, crowbar, seesaw), the fulcrum is situated between the effort and the load.",
            "Incorrect; in a Class 2 lever (e.g. wheelbarrow, nutcracker), the load is in the middle.",
            "Incorrect; in a Class 3 lever (e.g. tongs, forearm), the effort is in the middle.",
            "Incorrect; a pulley is a wheel with a grooved rim, not a lever class."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-005",
        "text": "In a wheelbarrow or a nutcracker, the load is placed between the fulcrum and the effort. This is an example of:",
        "options": ["Class 1 lever", "Class 2 lever", "Class 3 lever", "Complex inclined plane"],
        "ca": "B",
        "concept": "In a Class 2 lever, the load is positioned between the fulcrum and the effort, ensuring that the effort arm is always longer than the load arm (mechanical advantage > 1).",
        "analysis": [
            "Incorrect; Class 1 has the fulcrum in the middle.",
            "A Class 2 lever always places the load between the fulcrum and the effort (\\(\\text{MA} > 1\\)).",
            "Incorrect; Class 3 places effort in the middle.",
            "Incorrect; an inclined plane is a sloping ramp, not a pivoted lever."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-006",
        "text": "When a glass rod is rubbed vigorously with a silk cloth, what type of electric charge does the glass rod acquire?",
        "options": ["Negative charge", "Positive charge", "Zero charge", "Alternating charge"],
        "ca": "B",
        "concept": "Frictional electrification transfers loosely bound electrons from the glass rod to the silk cloth; losing electrons leaves the glass rod with a net positive electric charge.",
        "analysis": [
            "Incorrect; the silk cloth gains electrons and acquires a negative charge.",
            "The glass rod transfers valence electrons to the silk cloth, leaving it with a net positive charge.",
            "Incorrect; friction produces net electrostatic separation.",
            "Incorrect; static charges are stationary, not alternating."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-007",
        "text": "What happens to the gold leaves of an electroscope when a charged rod is brought into contact with its brass disc?",
        "options": ["The leaves collapse completely", "The leaves diverge (spread apart)", "The leaves turn magnetic", "The leaves melt"],
        "ca": "B",
        "concept": "Like charges repel; electric charge conducts down the metal stem to both gold leaves, causing them to acquire like charges and diverge.",
        "analysis": [
            "Incorrect; leaves collapse only when discharged or grounded.",
            "Both gold leaves acquire the same type of electric charge and mutually repel, causing them to diverge.",
            "Incorrect; static electricity does not induce permanent ferromagnetism.",
            "Incorrect; electrostatic charges at low voltages produce no melting heat."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-008",
        "text": "Which scientist famously demonstrated that lightning is a giant discharge of static electricity using a kite in 1752?",
        "options": ["Sir Isaac Newton", "Benjamin Franklin", "Michael Faraday", "Thomas Edison"],
        "ca": "B",
        "concept": "Benjamin Franklin demonstrated in 1752 that thunderstorm clouds carry electrostatic charge and that lightning is an electrical spark discharge, leading to his invention of the lightning conductor.",
        "analysis": [
            "Incorrect; Newton formulated the laws of motion and gravitation.",
            "Benjamin Franklin established the electrical nature of lightning and invented the lightning rod.",
            "Incorrect; Faraday discovered electromagnetic induction in 1831.",
            "Incorrect; Edison developed the commercial incandescent light bulb."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-009",
        "text": "A lightning conductor installed on a tall building protects the structure by:",
        "options": ["Absorbing lightning and converting it into light", "Providing a safe, zero-resistance path for electric charge into the ground", "Preventing storm clouds from gathering above the building", "Reflecting lightning bolts back into outer space"],
        "ca": "B",
        "concept": "A lightning conductor consists of a pointed copper rod connected via a thick copper strip to a metal plate buried in moist earth, safely grounding atmospheric charge.",
        "analysis": [
            "Incorrect; lightning is discharged into the earth, not converted into domestic lighting.",
            "The thick copper conductor channels the massive electrostatic surge safely into the ground, protecting the building.",
            "Incorrect; conductors do not stop cloud formation.",
            "Incorrect; electrical arcs cannot be reflected like light waves."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-010",
        "text": "During the daytime along a seashore, cool air blows from the sea toward the land. This phenomenon is called a:",
        "options": ["Land breeze", "Sea breeze", "Trade cyclone", "Monsoon depression"],
        "ca": "B",
        "concept": "Land has a lower specific heat capacity than seawater, heating up faster during the day. Rising warm air over land draws cool air from the sea, creating a sea breeze.",
        "analysis": [
            "Incorrect; land breeze occurs at night when land cools faster than the sea.",
            "Daytime heating causes warm air to rise over land, pulling cooler air from the sea (sea breeze).",
            "Incorrect; trade winds are global planetary wind systems.",
            "Incorrect; monsoon depressions are synoptic low-pressure weather systems."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-011",
        "text": "Which fundamental principle governs the electrostatic interaction between two charged objects?",
        "options": ["Like charges attract, unlike charges repel", "Like charges repel, unlike charges attract", "All charges attract neutral objects exclusively", "Electric charges repel only at high temperatures"],
        "ca": "B",
        "concept": "The fundamental law of electrostatics states that like electric charges (positive-positive or negative-negative) repel each other, whereas opposite charges (positive-negative) attract.",
        "analysis": [
            "Incorrect; opposite charges attract, like charges do not attract.",
            "Like charges exert mutually repulsive forces, while unlike charges exert mutually attractive forces.",
            "Incorrect; like charges repel each other.",
            "Incorrect; electrostatic Coulomb forces operate independently of thermal temperature."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-012",
        "text": "An ebonite rod rubbed with cat's fur acquires a negative charge because:",
        "options": ["Electrons are transferred from the fur to the ebonite rod", "Protons move from the fur into the ebonite rod", "Neutrons are destroyed inside the rod", "The rod loses positive charges to the air"],
        "ca": "A",
        "concept": "In frictional charging, only outer electrons are mobile; cat's fur loses electrons readily, transferring them to the ebonite rod, which gains net negative charge.",
        "analysis": [
            "Electrons transfer from the fur onto the ebonite rod, creating an excess of electrons (negative charge).",
            "Incorrect; atomic nuclei (protons) are bound and do not move during friction.",
            "Incorrect; neutrons are uncharged and not destroyed.",
            "Incorrect; positive charges do not radiate into air under normal friction."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-013",
        "text": "What is the mechanical advantage (MA) of a simple machine defined as?",
        "options": ["\\(\\text{Load} \\times \\text{Effort}\\)", "\\(\\frac{\\text{Load}}{\\text{Effort}}\\)", "\\(\\frac{\\text{Effort}}{\\text{Load}}\\)", "\\(\\text{Load} - \\text{Effort}\\)"],
        "ca": "B",
        "concept": "Mechanical advantage is the ratio of the output resistive force (load) overcome by the machine to the input force (effort) applied: \\(\\text{MA} = \\frac{\\text{Load}}{\\text{Effort}}\\).",
        "analysis": [
            "Incorrect; force values are divided, not multiplied.",
            "\\(\\text{MA} = \\frac{\\text{Load}}{\\text{Effort}}\\); if \\(\\text{MA} > 1\\), the machine acts as a force multiplier.",
            "Incorrect; effort divided by load is the inverse ratio.",
            "Incorrect; subtraction does not calculate mechanical advantage."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-014",
        "text": "Which simple machine uses a sloped flat surface to raise heavy loads to a higher elevation with reduced applied effort?",
        "options": ["Wheel and axle", "Inclined plane", "Class 3 lever", "Fixed pulley"],
        "ca": "B",
        "concept": "An inclined plane spreads the vertical work over a longer sloping distance, reducing the required lifting effort force (\\(F = W \\sin \\theta\\)).",
        "analysis": [
            "Incorrect; wheel and axle uses rotational force transmission.",
            "An inclined plane (ramp) reduces the effort needed to elevate heavy cargo by increasing the distance traveled.",
            "Incorrect; Class 3 levers do not reduce input effort (\\(\\text{MA} < 1\\)).",
            "Incorrect; a single fixed pulley only redirects force without force multiplication."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-015",
        "text": "A girl pushes against a rigid concrete wall with a force of \\(200\\text{ N}\\) for \\(10\\text{ minutes}\\), but the wall does not move. What is the physical work done?",
        "options": ["\\(2000\\text{ J}\\)", "\\(200\\text{ J}\\)", "\\(0\\text{ J}\\)", "\\(120{,}000\\text{ J}\\)"],
        "ca": "C",
        "concept": "In physics, work is done only when a force produces a displacement in the direction of the force: \\(W = F \\times s\\). If displacement \\(s = 0\\), work done is zero.",
        "analysis": [
            "Incorrect; force multiplied by time is impulse, not mechanical work.",
            "Incorrect; displacement is zero.",
            "Because the displacement of the wall is zero (\\(s = 0\\)), the mechanical work done is \\(W = 200\\text{ N} \\times 0\\text{ m} = 0\\text{ J}\\).",
            "Incorrect; physiological exhaustion does not equal mechanical work."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-016",
        "text": "What type of force opposes the relative motion between two solid surfaces sliding in contact?",
        "options": ["Gravitational force", "Frictional force", "Electrostatic force", "Magnetic force"],
        "ca": "B",
        "concept": "Frictional force arises from microscopic interlocking of surface irregularities, always acting tangentially opposite to the direction of relative motion.",
        "analysis": [
            "Incorrect; gravity attracts masses vertically toward Earth's center.",
            "Friction acts parallel to the contact interface, resisting the sliding motion of bodies.",
            "Incorrect; electrostatic force acts between stationary electric charges.",
            "Incorrect; magnetic force acts between magnetic poles or moving charges."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-017",
        "text": "The blades of an electric ceiling fan rotating at a constant speed demonstrate:",
        "options": ["Uniform circular motion", "Non-periodic linear motion", "Oscillatory rectilinear motion", "Random brownian motion"],
        "ca": "A",
        "concept": "When a body moves along a circular path with constant angular speed, covering equal angular displacements in equal time intervals, it executes uniform circular motion.",
        "analysis": [
            "The fan blades rotate in a circular trajectory at constant angular velocity, executing uniform circular motion.",
            "Incorrect; the motion is rotational and periodic, not linear.",
            "Incorrect; oscillatory motion involves back-and-forth swing about an axis.",
            "Incorrect; the motion is strictly circular and deterministic."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-018",
        "text": "Which instrument is used to detect the presence and nature of electric charge on an object?",
        "options": ["Barometer", "Gold-leaf electroscope", "Ammeter", "Thermometer"],
        "ca": "B",
        "concept": "A gold-leaf electroscope consists of two delicate gold leaves hung from a conducting rod inside a glass enclosure, diverging when charged to signal the presence of electrostatic charge.",
        "analysis": [
            "Incorrect; barometers measure atmospheric air pressure.",
            "The gold-leaf electroscope is the classical laboratory instrument used to detect static electric charges.",
            "Incorrect; ammeters measure continuous electric current in circuits.",
            "Incorrect; thermometers measure thermal temperature."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-019",
        "text": "In a Class 3 lever (such as a pair of sugar tongs or a human arm lifting a weight), which component is located in the middle?",
        "options": ["Fulcrum", "Load", "Effort", "Pivot wedge"],
        "ca": "C",
        "concept": "In a Class 3 lever, the effort (E) is applied between the fulcrum (F) and the load (L), resulting in a mechanical advantage of less than 1 but offering magnified speed and distance.",
        "analysis": [
            "Incorrect; fulcrum in the middle defines a Class 1 lever.",
            "Incorrect; load in the middle defines a Class 2 lever.",
            "In Class 3 levers (e.g. tweezers, fishing rod, tongs), effort is applied in the middle.",
            "Incorrect; pivot wedge is synonymous with fulcrum."
        ]
    },
    {
        "code": "MH-9-SCIT-19-19.2-OSC-020",
        "text": "Atmospheric air pressure at sea level is approximately equal to:",
        "options": ["\\(1013\\text{ hPa} \\approx 1.013 \\times 10^5\\text{ N/m}^2\\)", "\\(100\\text{ N/m}^2\\)", "\\(5000\\text{ N/m}^2\\)", "\\(14.7\\text{ N/m}^2\\)"],
        "ca": "A",
        "concept": "Standard atmospheric pressure at sea level supports a \\(76\\text{ cm}\\) column of mercury, equivalent to approximately \\(1.013 \\times 10^5\\text{ Pa}\\) (or \\(1013\\text{ hPa}\\)).",
        "analysis": [
            "Standard atmospheric pressure is \\(1\\text{ atm} = 1.013 \\times 10^5\\text{ Pa} = 1013\\text{ hPa}\\).",
            "Incorrect; \\(100\\text{ Pa}\\) is a tiny fraction of atmospheric pressure.",
            "Incorrect; too low for sea-level pressure.",
            "Incorrect; \\(14.7\\) is pounds per square inch (psi), not \\(\\text{N/m}^2\\)."
        ]
    }
]

# --- 8 OTF QUESTIONS ---
otf_t2 = [
    {
        "code": "MH-9-SCIT-19-19.2-OTF-001",
        "text": "Work is done only when an applied force produces displacement in the object along the direction of the force.",
        "truth": True,
        "concept": "Work is mathematically defined as the dot product of force and displacement vectors (\\(W = F \\cdot s = F s \\cos \\theta\\)); without displacement, mechanical work is zero.",
        "analysis": "This statement is **True**. Force without displacement (e.g. pushing a stationary wall) does not perform any physical work."
    },
    {
        "code": "MH-9-SCIT-19-19.2-OTF-002",
        "text": "A Class 2 lever always has a mechanical advantage greater than 1 because the effort arm is longer than the load arm.",
        "truth": True,
        "concept": "In a Class 2 lever, the load lies between the fulcrum and effort, so the effort arm always exceeds the load arm, resulting in \\(\\text{MA} = \\frac{\\text{Effort Arm}}{\\text{Load Arm}} > 1\\).",
        "analysis": "This statement is **True**. Class 2 levers act as force multipliers because the effort arm is always greater than the load arm."
    },
    {
        "code": "MH-9-SCIT-19-19.2-OTF-003",
        "text": "Like electric charges attract each other, whereas unlike electric charges repel each other.",
        "truth": False,
        "concept": "The fundamental law of electrostatics states that like charges repel, whereas unlike charges attract.",
        "analysis": "This statement is **False**. In reality, like charges repel each other and unlike charges attract."
    },
    {
        "code": "MH-9-SCIT-19-19.2-OTF-004",
        "text": "A gold-leaf electroscope can detect whether an object carries an electric charge.",
        "truth": True,
        "concept": "When charge conducts to the gold leaves of an electroscope, mutual electrostatic repulsion causes the leaves to diverge, confirming the presence of charge.",
        "analysis": "This statement is **True**. The divergence of the gold leaves reliably signals the presence of static electric charge."
    },
    {
        "code": "MH-9-SCIT-19-19.2-OTF-005",
        "text": "During nighttime, a land breeze blows from the cool land toward the warmer sea.",
        "truth": True,
        "concept": "At night, land radiates heat faster than water due to lower specific heat, creating a cool high-pressure area over land that drives a breeze seaward.",
        "analysis": "This statement is **True**. Land cools faster than the ocean at night, driving a convective land breeze from land to sea."
    },
    {
        "code": "MH-9-SCIT-19-19.2-OTF-006",
        "text": "Friction between surfaces can be reduced by using lubricants like oil, grease, or graphite.",
        "truth": True,
        "concept": "Lubricants fill the microscopic asperities (irregularities) between solid surfaces, substituting fluid friction for solid-on-solid contact.",
        "analysis": "This statement is **True**. Applying lubricants forms a smooth thin layer that drastically reduces surface friction and mechanical wear."
    },
    {
        "code": "MH-9-SCIT-19-19.2-OTF-007",
        "text": "A single fixed pulley provides a mechanical advantage of 10, multiplying input force ten times.",
        "truth": False,
        "concept": "A single fixed pulley has an ideal mechanical advantage of \\(\\text{MA} = 1\\); its primary function is to change the direction of the applied force comfortably downwards.",
        "analysis": "This statement is **False**. A single fixed pulley has \\(\\text{MA} = 1\\) and serves only to alter the direction of the pulling effort."
    },
    {
        "code": "MH-9-SCIT-19-19.2-OTF-008",
        "text": "Lightning conductors protect tall structures by conducting atmospheric electrostatic charges safely into the earth.",
        "truth": True,
        "concept": "A pointed copper rod atop a building channels sudden lightning currents through low-resistance grounding cables directly into the earth.",
        "analysis": "This statement is **True**. Grounding atmospheric electrical charges prevents structural fire and explosive damage from lightning strikes."
    }
]

# --- 6 OAR QUESTIONS ---
oar_t2 = [
    {
        "code": "MH-9-SCIT-19-19.2-OAR-001",
        "text": "Assertion (A): Carrying a heavy suitcase while walking horizontally along a level road does zero physical work against gravity.\nReason (R): The gravitational force acts vertically downwards while displacement is horizontal, making the angle between force and displacement 90 degrees.",
        "ca": "A",
        "concept": "Work done is given by \\(W = F s \\cos \\theta\\). When force is perpendicular to displacement (\\(\\theta = 90^\\circ\\)), \\(\\cos 90^\\circ = 0\\), resulting in zero work against that force.",
        "a_exp": "True — No mechanical work is performed against gravity during horizontal displacement.",
        "r_exp": "True — Perpendicular orientation between gravitational force and displacement means \\(W = F s \\cos 90^\\circ = 0\\)."
    },
    {
        "code": "MH-9-SCIT-19-19.2-OAR-002",
        "text": "Assertion (A): A pair of sugar tongs or tweezers has a mechanical advantage of less than 1.\nReason (R): In a Class 3 lever, the effort arm is shorter than the load arm.",
        "ca": "A",
        "concept": "In Class 3 levers, the effort is in the middle, so effort arm is always shorter than load arm, yielding \\(\\text{MA} = \\frac{\\text{Effort Arm}}{\\text{Load Arm}} < 1\\).",
        "a_exp": "True — Class 3 levers trade force to gain precision and speed, operating with \\(\\text{MA} < 1\\).",
        "r_exp": "True — The effort arm is physically shorter than the load arm in all Class 3 levers."
    },
    {
        "code": "MH-9-SCIT-19-19.2-OAR-003",
        "text": "Assertion (A): A plastic comb rubbed on dry hair can attract small neutral pieces of paper.\nReason (R): The charged comb induces opposite electrostatic charges on the nearer sides of the paper bits, creating a net attractive force.",
        "ca": "A",
        "concept": "Electrostatic induction polarizes neutral dielectric matter; opposite induced charges closer to the comb experience stronger attraction than the repelled like charges further away.",
        "a_exp": "True — Frictional charging electrifies the comb, enabling it to pick up light bits of paper.",
        "r_exp": "True — Electrostatic induction produces attractive polarization in nearby neutral paper."
    },
    {
        "code": "MH-9-SCIT-19-19.2-OAR-004",
        "text": "Assertion (A): Sea breezes blow from the ocean onto coastal land during hot afternoons.\nReason (R): Water has a higher specific heat capacity than land, so land warms up faster than seawater under sunlight.",
        "ca": "A",
        "concept": "Differential solar heating causes lower pressure over warm land; cooler, denser maritime air rushes in from the sea to replace the rising warm air.",
        "a_exp": "True — Coastal regions experience a refreshing onshore sea breeze during sunny afternoons.",
        "r_exp": "True — High specific heat of water keeps seawater cooler than adjacent land during the day."
    },
    {
        "code": "MH-9-SCIT-19-19.2-OAR-005",
        "text": "Assertion (A): It is easier to roll a heavy barrel up an inclined ramp into a truck than to lift it vertically.\nReason (R): An inclined plane decreases the total work required to lift the barrel to the truck's height.",
        "ca": "C",
        "concept": "An inclined plane reduces the required input effort force by extending the distance, but the total mechanical work against gravity (\\(W = mgh\\)) remains identical.",
        "a_exp": "True — An inclined plane reduces the necessary pushing force, making loading easier.",
        "r_exp": "False — The ideal work done against gravity is \\(mgh\\), which remains unchanged regardless of ramp slope."
    },
    {
        "code": "MH-9-SCIT-19-19.2-OAR-006",
        "text": "Assertion (A): Tall buildings and transmission towers must be equipped with pointed metal lightning arresters.\nReason (R): Pointed conductors facilitate silent discharge and provide a low-resistance path to safely channel lightning into the ground.",
        "ca": "A",
        "concept": "High charge density at sharp metal points ionizes surrounding air to neutralize storm cloud charges, while providing a direct grounding pathway.",
        "a_exp": "True — Lightning arresters safeguard high-rise architecture from devastating electrical strikes.",
        "r_exp": "True — Sharp metallic spikes promote corona discharge and channel massive surge currents directly to earth."
    }
]

# --- 6 OMC QUESTIONS ---
omc_t2 = [
    {
        "code": "MH-9-SCIT-19-19.2-OMC-001",
        "text": "Which of the following are examples of Class 1 levers where the fulcrum is situated between the effort and the load? (Select all that apply)",
        "options": ["A pair of scissors", "A seesaw on a playground", "A crowbar opening a crate", "A wheelbarrow carrying sand"],
        "cas": ["A pair of scissors", "A seesaw on a playground", "A crowbar opening a crate"],
        "concept": "Class 1 levers place the pivot fulcrum centrally between the applied effort and load.",
        "analysis": {
            "A pair of scissors": "Correct; pivot pin serves as central fulcrum between handle effort and blade load.",
            "A seesaw on a playground": "Correct; central support post acts as fulcrum between the two riders.",
            "A crowbar opening a crate": "Correct; fulcrum rests on the floor between applied hand effort and lifted load.",
            "A wheelbarrow carrying sand": "Incorrect; a wheelbarrow is a Class 2 lever with load in the middle."
        }
    },
    {
        "code": "MH-9-SCIT-19-19.2-OMC-002",
        "text": "Which of the following statements are correct regarding frictional electricity and static charges? (Select all that apply)",
        "options": [
            "Friction between two insulators causes the transfer of valence electrons.",
            "The body that gains electrons becomes negatively charged.",
            "Like electric charges repel, while unlike charges attract.",
            "Protons are transferred from atomic nuclei during rubbing."
        ],
        "cas": [
            "Friction between two insulators causes the transfer of valence electrons.",
            "The body that gains electrons becomes negatively charged.",
            "Like electric charges repel, while unlike charges attract."
        ],
        "concept": "Static electricity arises from the transfer of mobile electrons between materials.",
        "analysis": {
            "Friction between two insulators causes the transfer of valence electrons.": "Correct; friction detaches surface electrons from one material to another.",
            "The body that gains electrons becomes negatively charged.": "Correct; excess electrons establish a net negative charge.",
            "Like electric charges repel, while unlike charges attract.": "Correct; this is the fundamental electrostatic law.",
            "Protons are transferred from atomic nuclei during rubbing.": "Incorrect; protons are tightly held inside atomic nuclei and do not transfer during friction."
        }
    },
    {
        "code": "MH-9-SCIT-19-19.2-OMC-003",
        "text": "Which of the following are effective methods commonly used to reduce friction between moving machine parts? (Select all that apply)",
        "options": [
            "Applying lubricating oil or grease",
            "Using ball bearings between rotating surfaces",
            "Polishing and smoothing contacting surfaces",
            "Sprinkling coarse dry sand onto rotating axle bearings"
        ],
        "cas": [
            "Applying lubricating oil or grease",
            "Using ball bearings between rotating surfaces",
            "Polishing and smoothing contacting surfaces"
        ],
        "concept": "Friction is reduced by smoothing surfaces, substituting rolling for sliding motion (ball bearings), and applying fluid lubricants.",
        "analysis": {
            "Applying lubricating oil or grease": "Correct; forms a fluid layer that prevents direct solid asperity interlocking.",
            "Using ball bearings between rotating surfaces": "Correct; rolling friction is far smaller than sliding friction.",
            "Polishing and smoothing contacting surfaces": "Correct; reduces macroscopic interlocking of surface bumps.",
            "Sprinkling coarse dry sand onto rotating axle bearings": "Incorrect; coarse sand increases roughness and friction, causing severe abrasion."
        }
    },
    {
        "code": "MH-9-SCIT-19-19.2-OMC-004",
        "text": "Which of the following are valid examples of periodic motion? (Select all that apply)",
        "options": [
            "The revolution of the Earth around the Sun",
            "The back-and-forth swing of a pendulum clock",
            "The rotation of the hands of a wristwatch",
            "A football kicked erratically across a muddy field"
        ],
        "cas": [
            "The revolution of the Earth around the Sun",
            "The back-and-forth swing of a pendulum clock",
            "The rotation of the hands of a wristwatch"
        ],
        "concept": "Motion that repeats itself identically at regular, fixed time intervals is termed periodic motion.",
        "analysis": {
            "The revolution of the Earth around the Sun": "Correct; repeats predictably every 365.25 days.",
            "The back-and-forth swing of a pendulum clock": "Correct; oscillates with a constant time period.",
            "The rotation of the hands of a wristwatch": "Correct; sweeps fixed circular angles in regular intervals.",
            "A football kicked erratically across a muddy field": "Incorrect; irregular and non-periodic."
        }
    },
    {
        "code": "MH-9-SCIT-19-19.2-OMC-005",
        "text": "Which of the following conditions result in zero mechanical work being done in physics? (Select all that apply)",
        "options": [
            "A person pushes with immense force against a locked steel gate that does not budge.",
            "A satellite moves in a circular orbit where gravitational force is always perpendicular to its velocity.",
            "A student carries a backpack stationary while waiting at a bus stop.",
            "A crane lifts a 500 kg concrete slab vertically upwards through 10 meters."
        ],
        "cas": [
            "A person pushes with immense force against a locked steel gate that does not budge.",
            "A satellite moves in a circular orbit where gravitational force is always perpendicular to its velocity.",
            "A student carries a backpack stationary while waiting at a bus stop."
        ],
        "concept": "\\(W = F s \\cos \\theta\\); work is zero if displacement \\(s = 0\\) or if force is perpendicular to motion (\\(\\theta = 90^\\circ\\)).",
        "analysis": {
            "A person pushes with immense force against a locked steel gate that does not budge.": "Correct; \\(s = 0\\) means \\(W = 0\\).",
            "A satellite moves in a circular orbit where gravitational force is always perpendicular to its velocity.": "Correct; \\(\\cos 90^\\circ = 0\\), so centripetal gravitational work is zero.",
            "A student carries a backpack stationary while waiting at a bus stop.": "Correct; \\(s = 0\\), so zero mechanical work is performed.",
            "A crane lifts a 500 kg concrete slab vertically upwards through 10 meters.": "Incorrect; force and displacement are aligned (\\(W = mgh > 0\\))."
        }
    },
    {
        "code": "MH-9-SCIT-19-19.2-OMC-006",
        "text": "Which of the following statements correctly describe convection currents in daily natural phenomena? (Select all that apply)",
        "options": [
            "Sea breezes develop during daytime as warm air over land rises and cooler marine air flows inward.",
            "Land breezes develop at night because land radiates heat faster than the sea, causing air to blow seaward.",
            "Convection currents require a fluid medium (liquid or gas) with mobile particles.",
            "Convection currents can freely propagate across the empty vacuum of outer space."
        ],
        "cas": [
            "Sea breezes develop during daytime as warm air over land rises and cooler marine air flows inward.",
            "Land breezes develop at night because land radiates heat faster than the sea, causing air to blow seaward.",
            "Convection currents require a fluid medium (liquid or gas) with mobile particles."
        ],
        "concept": "Convection involves macroscopic buoyancy-driven circulation of fluid particles caused by thermal density gradients.",
        "analysis": {
            "Sea breezes develop during daytime as warm air over land rises and cooler marine air flows inward.": "Correct; driven by daytime thermal differences.",
            "Land breezes develop at night because land radiates heat faster than the sea, causing air to blow seaward.": "Correct; driven by nighttime land cooling.",
            "Convection currents require a fluid medium (liquid or gas) with mobile particles.": "Correct; requires physical movement of mass.",
            "Convection currents can freely propagate across the empty vacuum of outer space.": "Incorrect; vacuum contains no matter to support convection currents."
        }
    }
]

# Assemble all 40 questions
# OSC
for item in osc_t2:
    lines = []
    corr_idx = ord(item['ca']) - 65
    for i, opt in enumerate(item['options']):
        let = chr(65 + i)
        is_c = (i == corr_idx)
        c_tag = " (Correct)" if is_c else ""
        lines.append(f"- **({let}) {opt}{c_tag}** — {item['analysis'][i]}")
    
    sol = f"""**Key Concept:**
{item['concept']}

**Option Analysis:**
{chr(10).join(lines)}"""
    
    qs_t2.append({
        "questionCode": item['code'],
        "type": "OSC",
        "class": "9",
        "subjectCode": "SCIT",
        "chapterNumber": "19",
        "topicCode": "MH-9-SCIT-19-19.2",
        "text": item['text'],
        "options": item['options'],
        "correctAnswer": item['ca'],
        "solution": sol,
        "isEnhanced": True,
        "marks": 4,
        "difficulty": "medium",
        "boardCode": "MH"
    })

# OTF
for item in otf_t2:
    truth_str = "True" if item['truth'] else "False"
    c_let = "A" if item['truth'] else "B"
    sol = f"""**Key Concept:**
{item['concept']}

**Statement Evaluation:**
- **Statement:** "{item['text']}"
- **Analysis:** {item['analysis']}
- **Conclusion ({c_let}) (Correct)** — The statement is verified as **{truth_str}**."""
    
    qs_t2.append({
        "questionCode": item['code'],
        "type": "OTF",
        "class": "9",
        "subjectCode": "SCIT",
        "chapterNumber": "19",
        "topicCode": "MH-9-SCIT-19-19.2",
        "text": item['text'],
        "options": ["True", "False"],
        "correctAnswer": truth_str,
        "solution": sol,
        "isEnhanced": True,
        "marks": 4,
        "difficulty": "medium",
        "boardCode": "MH"
    })

# OAR
for item in oar_t2:
    sol = f"""**Key Concept:**
{item['concept']}

**Assertion & Reason Analysis:**
- **Assertion (A):** {item['a_exp']}
- **Reason (R):** {item['r_exp']}
- **Conclusion ({item['ca']}) (Correct)** — Evaluated according to mechanical and physical science principles."""
    
    qs_t2.append({
        "questionCode": item['code'],
        "type": "OAR",
        "class": "9",
        "subjectCode": "SCIT",
        "chapterNumber": "19",
        "topicCode": "MH-9-SCIT-19-19.2",
        "text": item['text'],
        "options": [
            "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
            "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
            "Assertion (A) is true, but Reason (R) is false.",
            "Assertion (A) is false, but Reason (R) is true."
        ],
        "correctAnswer": item['ca'],
        "solution": sol,
        "isEnhanced": True,
        "marks": 4,
        "difficulty": "medium",
        "boardCode": "MH"
    })

# OMC
for item in omc_t2:
    lines = []
    for i, opt in enumerate(item['options']):
        let = chr(65 + i)
        is_c = (opt in item['cas'])
        c_tag = " (Correct)" if is_c else ""
        lines.append(f"- **({let}) {opt}{c_tag}** — {item['analysis'][opt]}")
        
    sol = f"""**Key Concept:**
{item['concept']}

**Option Analysis:**
{chr(10).join(lines)}"""
    
    qs_t2.append({
        "questionCode": item['code'],
        "type": "OMC",
        "class": "9",
        "subjectCode": "SCIT",
        "chapterNumber": "19",
        "topicCode": "MH-9-SCIT-19-19.2",
        "text": item['text'],
        "options": item['options'],
        "correctAnswers": item['cas'],
        "solution": sol,
        "isEnhanced": True,
        "marks": 4,
        "difficulty": "medium",
        "boardCode": "MH"
    })

print(f"Generated {len(qs_t2)} brand-new gold-standard questions for Topic 19.2.")

with open('backups/staging/mh9_scit_19_topic2_new.json', 'w', encoding='utf-8') as f:
    json.dump(qs_t2, f, indent=2, ensure_ascii=False)

print("Saved backups/staging/mh9_scit_19_topic2_new.json")
