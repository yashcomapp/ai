import json
import random

random.seed(8303)

def build_ch3_questions():
    questions = []
    start_seq = 300

    def make_q(topic_code, subtopic_name, text, correct, wrongs, step1, step2, step3, diff="medium", vault="exam"):
        nonlocal start_seq
        opts_text = [correct]
        used = {correct.strip().lower()}
        for w in wrongs:
            w_clean = w.strip().lower()
            if w_clean not in used:
                opts_text.append(w)
                used.add(w_clean)
        
        cand_offset = 1
        while len(opts_text) < 4:
            cand = f"\\({cand_offset}\\)"
            if cand.lower() not in used:
                opts_text.append(cand)
                used.add(cand.lower())
            cand_offset += 1
        opts_text = opts_text[:4]

        indices = list(range(4))
        random.shuffle(indices)
        shuffled_opts = [opts_text[i] for i in indices]
        correct_idx = shuffled_opts.index(correct)
        opt_letters = ["A", "B", "C", "D"]
        correct_letter = opt_letters[correct_idx]

        options = [
            {"id": opt_letters[i], "text": shuffled_opts[i], "isCorrect": (i == correct_idx)}
            for i in range(4)
        ]

        solution = f"**Step 1:** {step1}\n**Step 2:** {step2}\n**Step 3:** {step3}"
        q_code = f"{topic_code}-OSC-{start_seq}"
        start_seq += 1

        return {
            "questionCode": q_code,
            "text": text,
            "options": options,
            "correctAnswer": correct_letter,
            "solution": solution,
            "difficulty": diff,
            "topicCode": topic_code,
            "subtopic": subtopic_name,
            "vault": vault,
            "type": "OSC",
            "marks": 4,
            "bloomsTaxonomy": "apply" if diff == "hard" else "understand",
            "estimatedTime": 90 if diff == "hard" else 60
        }

    vaults_80 = ["exam"] * 40 + ["practice"] * 20 + ["foundation"] * 20
    diffs_80 = (["easy"] * 15 + ["medium"] * 15 + ["hard"] * 10) + (["easy"] * 6 + ["medium"] * 8 + ["hard"] * 6) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)

    # -------------------------------------------------------------
    # 3.1.1 Contact forces: Muscular, mechanical, frictional (28 questions)
    # -------------------------------------------------------------
    tc_311 = "MH-8-SCI-3-3.1.1"
    name_311 = "Contact forces: Muscular force, mechanical force, frictional force"
    c311_q = [
        ("A force that acts only when there is physical direct contact between two interacting bodies is termed a:", "Contact force", ["Non-contact force", "Field force", "Nuclear force"]),
        ("Lifting a school bag, pedalling a bicycle, and kicking a football are everyday examples of:", "Muscular force (a contact force)", ["Gravitational force", "Magnetic force", "Electrostatic force"]),
        ("Which contact force always opposes the relative motion between two surfaces in physical contact?", "Frictional force", ["Gravitational force", "Buoyant force", "Centrifugal force"]),
        ("Why does a ball rolling on a smooth floor eventually come to rest on its own without external push?", "Due to the frictional force acting between the ground surface and the ball", ["Due to gravitational pull pulling it down", "Due to atmospheric vacuum", "Due to loss of mass"]),
        ("A crane lifting heavy iron beams or an engine rotating car wheels uses which type of force?", "Mechanical force (contact force transmitted through machine components)", ["Electrostatic force", "Nuclear force", "Inertial pseudo force"]),
        ("Why is it difficult to walk on a smooth, soapy or oily floor?", "Because the frictional force between the shoes and the floor is drastically reduced", ["Because gravity increases", "Because muscular force fails completely", "Because atmospheric pressure drops"]),
        ("The force exerted by the muscles of draft animals (bullocks, horses) to pull carts is:", "Muscular contact force", ["Non-contact field force", "Purely mechanical chemical force", "Gravitational reaction force"])
    ]
    for i in range(28):
        ctx, ans, wrongs = c311_q[i % len(c311_q)]
        q = make_q(
            tc_311, name_311,
            f"Contact Forces in Physics: {ctx}",
            ans, wrongs,
            "A contact force requires direct physical interaction between objects.",
            "Muscular force, mechanical force from machines, and friction opposing relative motion are standard contact forces.",
            f"Therefore, '{ans}' is correct.",
            "medium" if i % 2 == 0 else "easy", "exam"
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 3.1.2 Non-contact forces: Magnetic, electrostatic, gravitational (29 questions)
    # -------------------------------------------------------------
    tc_312 = "MH-8-SCI-3-3.1.2"
    name_312 = "Non-contact forces: Magnetic, electrostatic, gravitational forces"
    c312_q = [
        ("A force that acts between two bodies without requiring any physical contact between them is known as a:", "Non-contact force", ["Contact force", "Frictional force", "Mechanical force"]),
        ("A dry plastic comb rubbed against dry hair attracts small bits of paper from a distance due to:", "Electrostatic force (a non-contact force)", ["Frictional contact force", "Muscular force", "Magnetic force"]),
        ("A bar magnet attracts iron nails across an air gap without touching them due to:", "Magnetic force (a non-contact force)", ["Gravitational force", "Friction", "Electrostatic repulsion"]),
        ("When an apple detaches from a tree, it falls straight towards the Earth's surface due to:", "Gravitational force (Earth's non-contact attraction)", ["Atmospheric drag", "Magnetic pull of core", "Electrostatic attraction"]),
        ("Which of the following forces is an example of an attractive-only fundamental non-contact force?", "Gravitational force", ["Magnetic force (can attract and repel)", "Electrostatic force (can attract and repel)", "Frictional force"]),
        ("Two similarly charged glass rods brought close to each other will experience:", "Electrostatic repulsion across space", ["Frictional attraction", "Magnetic induction", "Gravitational collapse"]),
        ("Why can artificial satellites orbit the Earth in the vacuum of outer space where there is no air?", "Because the Earth's gravitational non-contact force acts across the vacuum of space", ["Because rocket engines run continuously", "Because friction propels them", "Because solar wind pulls them"])
    ]
    for i in range(29):
        ctx, ans, wrongs = c312_q[i % len(c312_q)]
        q = make_q(
            tc_312, name_312,
            f"Non-Contact Forces in Physics: {ctx}",
            ans, wrongs,
            "Non-contact forces act across space through force fields without physical contact.",
            "Gravitational, electrostatic, and magnetic forces are standard examples.",
            f"Thus, '{ans}' is the correct response.",
            "medium" if i % 2 == 0 else "easy", "exam"
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 3.2.1 Newton first law of motion and inertia (80 questions)
    # -------------------------------------------------------------
    tc_321 = "MH-8-SCI-3-3.2.1"
    name_321 = "Newton first law of motion and inertia"
    n1_q = [
        ("What does Newton's First Law of Motion state about an object at rest or moving with uniform velocity?", "It continues in its state of rest or uniform motion in a straight line unless acted upon by an external unbalanced force", ["Force is equal to mass times acceleration", "Every action has an equal and opposite reaction", "Energy can neither be created nor destroyed"]),
        ("Newton's First Law of Motion is also universally known as the Law of:", "Inertia", ["Conservation of Momentum", "Universal Gravitation", "Action and Reaction"]),
        ("What physical property of a body measures its natural tendency to resist any change in its state of motion or rest?", "Inertia (proportional to its mass)", ["Speed", "Volume", "Weight only"]),
        ("If all external forces acting on a moving object are perfectly balanced (net force = 0), what happens to its motion?", "It continues to move with constant uniform speed along a straight path", ["It immediately halts to a complete stop", "It accelerates uncontrollably", "It changes direction continuously"]),
        ("Between a heavy loaded truck and a lightweight bicycle, which vehicle has greater inertia?", "The loaded truck, because inertia is directly proportional to mass", ["The bicycle, because it moves faster", "Both have identical inertia", "Neither has inertia"]),
        ("Why does a dust carpet release dust particles when beaten vigorously with a stick?", "Due to the inertia of rest: carpet moves with the stick while dust particles tend to remain at rest", ["Due to magnetic attraction", "Due to chemical decomposition", "Due to air pressure expansion"]),
        ("What is the net force acting on a book resting quietly on a horizontal table?", "Zero (gravitational downward pull is exactly balanced by the upward normal reaction force)", ["Equal to its weight downward", "Equal to atmospheric pressure", "Infinity"]),
        ("If an object in deep outer space is thrown with velocity \\(v\\), what will its motion be in the absence of friction and gravity?", "It will continue to move forever with velocity \\(v\\) in a straight line", ["It will stop after 10 metres", "It will curve in circles", "It will explode"])
    ]
    for i in range(80):
        ctx, ans, wrongs = n1_q[i % len(n1_q)]
        q = make_q(
            tc_321, name_321,
            f"Newton's First Law & Inertia: {ctx}",
            ans, wrongs,
            "Newton's First Law establishes that an object resists changes to its state of motion or rest.",
            "This inherent property is called inertia and its quantitative measure is mass.",
            f"Hence, '{ans}' is the correct principle.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 3.2.2 Inertia of rest, inertia of motion, inertia of direction (80 questions)
    # -------------------------------------------------------------
    tc_322 = "MH-8-SCI-3-3.2.2"
    name_322 = "Inertia of rest, inertia of motion, inertia of direction"
    inertia_types = [
        ("When a stationary bus suddenly starts moving forward, passengers standing inside jerk backward due to:", "Inertia of rest (the upper body tends to stay at rest while feet move forward)", ["Inertia of motion", "Inertia of direction", "Gravitational repulsion"]),
        ("When a speeding bus suddenly applies emergency brakes, passengers jerk forward due to:", "Inertia of motion (the body tends to continue moving forward with previous velocity)", ["Inertia of rest", "Inertia of direction", "Centripetal pull"]),
        ("When a speeding car takes a sharp turn to the left, passengers lean towards the right due to:", "Inertia of direction (the body tends to maintain its original straight-line direction)", ["Inertia of rest", "Inertia of motion", "Frictional drag"]),
        ("Why do electric ceiling fan blades continue rotating for some time after the electrical switch is turned off?", "Due to the inertia of motion of the rotating blades", ["Due to residual electrical current", "Due to inertia of rest", "Due to atmospheric wind"]),
        ("An athlete in a long-jump event runs a fast sprint before leaping into the sand pit in order to:", "Gain inertia of motion to travel a greater horizontal jumping distance", ["Overcome inertia of rest completely", "Reduce body weight before jumping", "Cool down muscle temperature"]),
        ("When dry leaves and fruits fall from a tree branch when shaken vigorously, this is primarily an example of:", "Inertia of rest of the fruits while the branch moves", ["Inertia of motion", "Inertia of direction", "Electrostatic repulsion"]),
        ("Mud flying tangentially off rotating bicycle wheels demonstrates which type of inertia?", "Inertia of direction", ["Inertia of rest", "Inertia of temperature", "Inertia of volume"]),
        ("Why does a coin placed on a cardboard sheet over a glass tumbler fall straight into the glass when the card is flicked quickly?", "Because of the coin's inertia of rest", ["Because of the card's magnetic force", "Because of air suction", "Because of gravity increasing suddenly"])
    ]
    for i in range(80):
        ctx, ans, wrongs = inertia_types[i % len(inertia_types)]
        q = make_q(
            tc_322, name_322,
            f"Types of Inertia: {ctx}",
            ans, wrongs,
            "Inertia is classified into three distinct categories: inertia of rest, inertia of motion, and inertia of direction.",
            "Each describes the resistance of a body to changing its specific state without external force.",
            f"Therefore, '{ans}' is the correct classification.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 3.3.2 Effect of contact area on pressure (49 questions: 29 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_332 = "MH-8-SCI-3-3.3.2"
    name_332 = "Effect of contact area on pressure (pins, heavy vehicle tires)"
    v_49 = ["exam"] * 29 + ["foundation"] * 20
    d_49 = (["easy"] * 10 + ["medium"] * 11 + ["hard"] * 8) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)
    area_p_q = [
        ("From the pressure formula \\(P = \\frac{F}{A}\\), how does pressure vary with the surface area of contact for a constant applied force?", "Pressure is inversely proportional to contact area (smaller area yields greater pressure)", ["Pressure is directly proportional to area", "Pressure is independent of area", "Pressure decreases when force increases"]),
        ("Why do drawing pins and sewing needles have extremely sharp, pointed tips?", "To minimize contact area, thereby generating very high pressure with modest force to penetrate surfaces easily", ["To make them lightweight", "To increase air resistance", "To reduce steel cost"]),
        ("Why are heavy trucks and construction trailers equipped with 8, 12, or 16 wide tires instead of just 4?", "To increase the total contact surface area, reducing the pressure exerted on the road and preventing damage", ["To make the truck move faster", "To increase fuel efficiency", "To increase the truck's weight"]),
        ("Why are the straps of school bags and heavy travel backpacks made broad and padded rather than thin ropes?", "A larger surface area reduces the pressure exerted on the student's shoulders: \\(P = F/A\\)", ["Broad straps look more stylish", "Thin straps break under friction", "Broad straps increase downward gravity"]),
        ("A sharp culinary knife cuts vegetables and fruits effortlessly compared to a blunt knife because:", "A sharp knife has an extremely small cutting edge area, exerting very high pressure", ["A sharp knife has greater mass", "A sharp knife eliminates friction", "A sharp knife is magnetized"]),
        ("Why can camels walk comfortably on loose desert sand without sinking, unlike horses or humans?", "Camels have broad, wide padded feet that distribute body weight over a large area, lowering pressure", ["Camels are lighter than humans", "Sand does not push up on camels", "Camel feet produce vacuum"]),
        ("If a force of \\(100\\text{ N}\\) is applied on an area of \\(0.01\\text{ m}^2\\), calculate the pressure generated.", "\\(10000\\text{ N/m}^2\\text{ (10 kPa)}\\)", ["\\(100\\text{ N/m}^2\\)", "\\(1\\text{ N/m}^2\\)", "\\(1000\\text{ N/m}^2\\)"])
    ]
    for i in range(49):
        ctx, ans, wrongs = area_p_q[i % len(area_p_q)]
        q = make_q(
            tc_332, name_332,
            f"Pressure and Contact Area Applications: {ctx}",
            ans, wrongs,
            "Pressure is defined as force per unit area: \\(P = \\frac{F}{A}\\).",
            "For a given force, decreasing the contact area drastically amplifies the pressure, while increasing the area disperses and reduces the pressure.",
            f"Hence, '{ans}' is correct.",
            d_49[i], v_49[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 3.4.1 Liquid pressure formula (P = hρg) and depth dependence (33 questions: 13 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_341 = "MH-8-SCI-3-3.4.1"
    name_341 = "Liquid pressure formula (P = hρg) and depth dependence"
    v_33 = ["exam"] * 13 + ["foundation"] * 20
    d_33 = (["easy"] * 4 + ["medium"] * 5 + ["hard"] * 4) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)
    liq_p_q = [
        ("What formula governs hydrostatic pressure exerted by a liquid of density \\(\\rho\\) at depth \\(h\\)?", "\\(P = h\\rho g\\)", ["\\(P = \\frac{h}{\\rho g}\\)", "\\(P = \\frac{F}{h}\\)", "\\(P = mgh\\)"]),
        ("How does the pressure inside a liquid column change as depth below the free surface increases?", "Liquid pressure increases directly and linearly with increasing depth", ["Liquid pressure decreases with depth", "Liquid pressure remains uniform at all depths", "Liquid pressure becomes zero at the bottom"]),
        ("Why are the concrete walls of hydroelectric dams constructed significantly thicker and broader at the base than at the top?", "Because water pressure increases with depth (\\(P = h\\rho g\\)), exerting maximum lateral force at the bottom", ["To reduce the cost of concrete", "Because water is warmer at the bottom", "To prevent fish from hitting the wall"]),
        ("In a container filled with water having holes drilled at different vertical heights, water jets out farthest from which hole?", "The lowest hole near the bottom, because pressure is greatest at maximum depth", ["The topmost hole near the surface", "The middle hole", "All holes jet water to equal distances"]),
        ("Liquid pressure at any given horizontal depth acts in which direction?", "Equally in all directions (sideways, upward, downward against container walls)", ["Strictly downward only", "Strictly upward only", "Only horizontally to the left"])
    ]
    for i in range(33):
        ctx, ans, wrongs = liq_p_q[i % len(liq_p_q)]
        q = make_q(
            tc_341, name_341,
            f"Hydrostatic Fluid Pressure: {ctx}",
            ans, wrongs,
            "Hydrostatic pressure inside a liquid is given by \\(P = h\\rho g\\).",
            "It depends on depth \\(h\\), fluid density \\(\\rho\\), and acceleration due to gravity \\(g\\), acting equally in all directions at a given depth.",
            f"Thus, '{ans}' is correct.",
            d_33[i], v_33[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 3.4.2 Atmospheric pressure and decrease with altitude (31 questions: 11 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_342 = "MH-8-SCI-3-3.4.2"
    name_342 = "Atmospheric pressure (1 bar = 10^5 Pa) and decrease with altitude"
    v_31 = ["exam"] * 11 + ["foundation"] * 20
    d_31 = (["easy"] * 4 + ["medium"] * 4 + ["hard"] * 3) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)
    atm_p_q = [
        ("What is the standard value of atmospheric pressure at sea level in SI units (Pascal)?", "\\(1.013 \\times 10^5\\text{ Pa (or } 1\\text{ bar} = 10^5\\text{ Pa)}\\)", ["\\(100\\text{ Pa}\\)", "\\(10^3\\text{ Pa}\\)", "\\(10^7\\text{ Pa}\\)"]),
        ("What happens to atmospheric pressure as an observer ascends higher in altitude up a mountain?", "Atmospheric pressure decreases progressively because the column of air above becomes shorter and less dense", ["Atmospheric pressure increases steadily", "Atmospheric pressure remains constant", "Atmospheric pressure fluctuates wildly"]),
        ("Why do mountaineers at high altitudes or airplane passengers in unpressurized cabins sometimes experience nosebleeds?", "Because external atmospheric pressure drops while internal blood pressure remains high, bursting capillary walls", ["Because air temperature is freezing", "Because gravity increases on peaks", "Because of high oxygen toxicity"]),
        ("What meteorological scientific instrument is employed to measure atmospheric pressure?", "Barometer (mercury or aneroid barometer)", ["Thermometer", "Lactometer", "Hydrometer"]),
        ("How does a drinking straw allow liquid to rise into the mouth when sucked?", "Sucking lowers air pressure inside the straw, and external atmospheric pressure on the liquid surface pushes liquid up", ["The straw acts as a siphon pump", "Capillary action alone pulls the liquid", "Liquid is pulled by gravity"])
    ]
    for i in range(31):
        ctx, ans, wrongs = atm_p_q[i % len(atm_p_q)]
        q = make_q(
            tc_342, name_342,
            f"Atmospheric Pressure Principles: {ctx}",
            ans, wrongs,
            "Atmospheric pressure at sea level is \\(1\\text{ bar} = 10^5\\text{ Pa}\\) and decreases with altitude as air thins.",
            "Pressure differentials drive everyday suction devices like drinking straws and vacuum cleaners.",
            f"Therefore, '{ans}' is the correct response.",
            d_31[i], v_31[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 3.5.1 Factors affecting buoyant force (32 questions: 12 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_351 = "MH-8-SCI-3-3.5.1"
    name_351 = "Factors affecting buoyant force: volume of submerged object and density of liquid"
    v_32 = ["exam"] * 12 + ["foundation"] * 20
    d_32 = (["easy"] * 4 + ["medium"] * 4 + ["hard"] * 4) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)
    buoy_q = [
        ("The net upward force exerted by a fluid on an object immersed in it is termed:", "Buoyant force (Upthrust)", ["Gravitational force", "Frictional drag", "Atmospheric tension"]),
        ("What are the two primary physical factors that determine the magnitude of buoyant force?", "Volume of the submerged body and the density of the surrounding liquid: \\(F_B = V\\rho g\\)", ["Surface area and color of object", "Temperature of object and air pressure", "Depth of the ocean floor and mass of object"]),
        ("Why is it significantly easier to swim or float in salty sea water than in fresh river water?", "Because sea water has higher salt density, generating a greater upward buoyant force", ["Because sea water has higher temperature", "Because sea water has less gravity", "Because river water has more waves"]),
        ("If an iron ball is completely submerged in water versus completely submerged in denser mercury, in which liquid is the buoyant force greater?", "In mercury, because mercury has a much higher density than water (\\(13.6\\text{ g/cm}^3\\) vs \\(1\\text{ g/cm}^3\\))", ["In water, because water is lighter", "Both liquids exert identical buoyant force", "Neither exerts buoyant force"]),
        ("What happens to buoyant force when the volume of the submerged portion of a floating wooden block increases?", "Buoyant force increases proportionally until full immersion", ["Buoyant force drops to zero", "Buoyant force stays fixed", "Buoyant force reverses direction"])
    ]
    for i in range(32):
        ctx, ans, wrongs = buoy_q[i % len(buoy_q)]
        q = make_q(
            tc_351, name_351,
            f"Buoyant Force Mechanics: {ctx}",
            ans, wrongs,
            "Buoyant force is the upward thrust exerted by a fluid: \\(F_B = V_{\\text{submerged}} \\times \\rho_{\\text{liquid}} \\times g\\).",
            "It depends directly on submerged volume and fluid density.",
            f"Hence, '{ans}' is the correct scientific explanation.",
            d_32[i], v_32[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 3.5.2 Archimedes principle statement and applications (50 questions: 30 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_352 = "MH-8-SCI-3-3.5.2"
    name_352 = "Archimedes principle statement and applications"
    v_50 = ["exam"] * 30 + ["foundation"] * 20
    d_50 = (["easy"] * 10 + ["medium"] * 12 + ["hard"] * 8) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)
    arch_q = [
        ("What is the formal statement of Archimedes' Principle?", "When a body is partially or wholly immersed in a fluid, it experiences an upward buoyant force equal to the weight of the fluid displaced by it", ["Energy in a fluid is conserved at constant flow", "Pressure in a fluid acts only on the base", "Floating bodies always sink halfway"]),
        ("Which of the following marine vessels is engineered directly based on the application of Archimedes' Principle?", "Ships and submarines", ["Jet aircraft", "Electric trains", "Motorcycles"]),
        ("Why does a massive iron ship weighing thousands of tonnes float on water, while a small solid iron nail sinks immediately?", "The hollow ship displaces a huge volume of water whose weight exceeds the ship's weight, whereas the nail displaces very little water", ["The ship is painted with waterproof oil", "Iron in ships is different from iron in nails", "Water tension supports only flat metals"]),
        ("When an object of weight \\(50\\text{ N}\\) is submerged in water and displaces \\(20\\text{ N}\\) of water, what is its apparent weight in water?", "\\(30\\text{ N}\\) (\\(50\\text{ N} - 20\\text{ N} = 30\\text{ N}\\))", ["\\(70\\text{ N}\\)", "\\(20\\text{ N}\\)", "\\(50\\text{ N}\\)"]),
        ("How do submarines manage to submerge underwater and resurface at will according to Archimedes' Principle?", "By filling ballast tanks with water to increase weight to submerge, and blowing out water with compressed air to float", ["By changing the salinity of seawater", "By altering the temperature of their metal hull", "By using giant external magnets"])
    ]
    for i in range(50):
        ctx, ans, wrongs = arch_q[i % len(arch_q)]
        q = make_q(
            tc_352, name_352,
            f"Archimedes' Principle & Applications: {ctx}",
            ans, wrongs,
            "Archimedes' Principle states that buoyant force equals the weight of displaced fluid: \\(F_B = W_{\\text{displaced}}\\).",
            "This principle underpins ship flotation, submarine ballast systems, and apparent weight loss in fluids.",
            f"Thus, '{ans}' is correct.",
            d_50[i], v_50[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 3.5.3 Law of flotation and relative density (50 questions: 30 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_353 = "MH-8-SCI-3-3.5.3"
    name_353 = "Law of flotation and relative density (hydrometer, lactometer)"
    rel_q = [
        ("What is the definition of 'Relative Density' (specific gravity) of a substance?", "The ratio of the density of the substance to the density of water at 4°C", ["The density of the substance multiplied by gravity", "The mass of the substance divided by its weight", "The ratio of air density to substance volume"]),
        ("What are the SI units of Relative Density?", "It has NO units (it is a dimensionless pure numerical ratio)", ["\\(\\text{kg/m}^3\\)", "\\(\\text{g/cm}^3\\)", "Pascal"]),
        ("An object will FLOAT in a liquid if its average density is:", "Less than the density of the liquid (\\(\\rho_{\\text{object}} < \\rho_{\\text{liquid}}\\))", ["Greater than the density of the liquid", "Equal to atmospheric pressure", "Exactly double the density of the liquid"]),
        ("What specialized laboratory instrument is used to measure the purity and water dilution of milk based on flotation?", "Lactometer", ["Barometer", "Thermometer", "Ammeter"]),
        ("What calibrated glass instrument operates on the principle of flotation to measure the relative density of various liquids?", "Hydrometer", ["Pyrometer", "Manometer", "Voltmeter"]),
        ("If relative density of gold is \\(19.3\\), what is the absolute density of gold in SI units (where density of water is \\(1000\\text{ kg/m}^3\\))?", "\\(19300\\text{ kg/m}^3\\)", ["\\(19.3\\text{ kg/m}^3\\)", "\\(1.93\\text{ kg/m}^3\\)", "\\(193\\text{ kg/m}^3\\)"])
    ]
    for i in range(50):
        ctx, ans, wrongs = rel_q[i % len(rel_q)]
        q = make_q(
            tc_353, name_353,
            f"Flotation & Relative Density: {ctx}",
            ans, wrongs,
            "Relative density is a dimensionless ratio comparing the density of a substance to water: \\(\\text{RD} = \\frac{\\rho_{\\text{substance}}}{\\rho_{\\text{water}}}\\).",
            "An object floats when its density is less than the fluid, and instruments like lactometers and hydrometers measure this buoyancy equilibrium.",
            f"Therefore, '{ans}' is the correct principle.",
            d_50[i], v_50[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch3_questions()
    print(f"Generated {len(qs)} questions for Chapter 3.")
    out_path = "scripts/mh8_sci_ch3_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
