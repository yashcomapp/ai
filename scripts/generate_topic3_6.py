# scripts/generate_topic3_6.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-3-3.6"
CHAPTER_NUM = 3

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Three wires & domestic supply standards
    ("""In standard domestic electrical supply in India, what is the nominal voltage and frequency of alternating current (AC)?""",
     ["\\(110\\text{ V},\\ 60\\text{ Hz}\\)",
      "\\(230\\text{ V},\\ 50\\text{ Hz}\\)",
      "\\(440\\text{ V},\\ 50\\text{ Hz}\\)",
      "\\(220\\text{ V},\\ 100\\text{ Hz}\\)"],
     "B", "OSC", "easy",
     "• In India, standard domestic power is supplied at a potential difference of \\(230\\text{ V}\\) (or \\(220\\text{-}240\\text{ V}\\)) with an alternating frequency of \\(50\\text{ Hz}\\).\nCorrect Choice is (B)."),

    ("""According to modern international safety standards, what is the insulation color code for the LIVE wire?""",
     ["Green or Yellow-Green", "Brown (or Red in old code)", "Black (or Blue in old code)", "White"],
     "B", "OSC", "easy",
     "• Live wire is insulated in brown (or conventionally red in earlier Indian wiring).\nCorrect Choice is (B)."),

    ("""What is the insulation color code for the NEUTRAL wire in modern domestic wiring?""",
     ["Light Blue (or Black in traditional code)", "Red", "Green", "Yellow"],
     "A", "OSC", "easy",
     "• Neutral wire carries light blue insulation (traditionally black).\nCorrect Choice is (A)."),

    ("""What is the insulation color code for the EARTH wire?""",
     ["Red or Brown", "Black or Blue", "Green or Yellow-Green stripe", "White"],
     "C", "OSC", "easy",
     "• The safety earth wire is always color-coded green or yellow with green stripes.\nCorrect Choice is (C)."),

    ("""What is the electrical potential of the neutral wire relative to the ground (earth) in a balanced domestic system?""",
     ["\\(230\\text{ V}\\)", "\\(115\\text{ V}\\)", "\\(0\\text{ V}\\)", "\\(-230\\text{ V}\\)"],
     "C", "OSC", "easy",
     "• The neutral wire is grounded at the local substation transformer and is maintained at approximately zero potential (\\(0\\text{ V}\\)).\nCorrect Choice is (C)."),

    ("""What is the potential difference between the Live wire and the Neutral wire in an Indian household?""",
     ["\\(0\\text{ V}\\)", "\\(110\\text{ V}\\)", "\\(230\\text{ V}\\)", "\\(440\\text{ V}\\)"],
     "C", "OSC", "easy",
     "• The potential difference between live (\\(230\\text{ V}\\)) and neutral (\\(0\\text{ V}\\)) is \\(230\\text{ V}\\).\nCorrect Choice is (C)."),

    ("""Why is domestic electricity supplied as Alternating Current (AC) rather than Direct Current (DC)?""",
     ["AC cannot give an electric shock",
      "AC voltage can be easily stepped up and stepped down using transformers for efficient long-distance transmission with minimal power loss",
      "DC travels only through vacuum",
      "AC produces no magnetic field"],
     "B", "OSC", "medium",
     "• AC can be stepped up to extremely high voltages for low-current transmission (reducing \\(I^2 R\\) line losses) and stepped down safely for domestic use via transformers.\nCorrect Choice is (B)."),

    ("""In a three-pin plug, why is the EARTH pin designed to be LONGER than the live and neutral pins?""",
     ["To fit snugly and look distinct",
      "So that the metallic appliance body is grounded FIRST before live contact is made, and remains grounded until after the live pin is disconnected",
      "To carry higher current than live",
      "To increase electrical resistance"],
     "B", "OSC", "medium",
     "• Being longer, the earth pin enters the earth socket first to establish ground protection, and disengages last during unplugging.\nCorrect Choice is (B)."),

    ("""Why is the EARTH pin in a 3-pin plug made THICKER than the live and neutral pins?""",
     ["To prevent it from being accidentally plugged into the live or neutral sockets and to provide very low electrical resistance",
      "To allow the user to pull the plug easily",
      "To generate heat faster",
      "To match the socket voltage"],
     "A", "OSC", "medium",
     "• Thicker pin prevents wrong insertion into smaller live/neutral sockets and offers lower resistance for quick fault current drainage.\nCorrect Choice is (A)."),

    ("""Which part of an electrical appliance is connected directly to the Earth wire?""",
     ["The heating filament", "The metallic chassis/casing", "The on/off indicator LED", "The inner copper coils"],
     "B", "OSC", "easy",
     "• The earth wire is fastened directly to the exposed metal body of the appliance (e.g., refrigerator, iron, microwave) to protect users from shock.\nCorrect Choice is (B)."),

    # 11-20: Fuses, MCBs, and circuit breakers
    ("""An electric fuse is a safety device based on which scientific principle?""",
     ["Magnetic effect of electric current",
      "Joule's heating effect of electric current (\\(H = I^2 R t\\))",
      "Chemical effect of electric current",
      "Electrostatic induction"],
     "B", "OSC", "easy",
     "• A fuse operates on Joule heating; excessive current generates sufficient thermal energy to melt the fuse wire.\nCorrect Choice is (B)."),

    ("""What are the key material properties required for a reliable fuse wire?""",
     ["High melting point and high resistance",
      "Low melting point and specific high resistivity compared to connecting copper wires",
      "High melting point and zero resistance",
      "Infinite melting point"],
     "B", "OSC", "medium",
     "• Fuse wire must have a low melting point so it melts before home wiring can overheat, and higher resistance than copper supply lines.\nCorrect Choice is (B)."),

    ("""A fuse wire is commonly made of an alloy of which two metals?""",
     ["Copper and Zinc (Brass)", "Lead (\\(Pb\\)) and Tin (\\(Sn\\))", "Iron and Carbon (Steel)", "Gold and Silver"],
     "B", "OSC", "easy",
     "• Standard fuse wire is an alloy of lead and tin (solder alloy) having a low melting temperature (around \\(183^\\circ\\text{C}\\) to \\(200^\\circ\\text{C}\\)).\nCorrect Choice is (B)."),

    ("""In a domestic circuit, the fuse must ALWAYS be connected in series with the:""",
     ["Neutral wire", "Live wire", "Earth wire", "Any wire at random"],
     "B", "OSC", "medium",
     "• The fuse must be connected strictly in series with the LIVE wire. If it were in the neutral wire, blowing the fuse would still leave the appliance at lethal live voltage (\\(230\\text{ V}\\)).\nCorrect Choice is (B)."),

    ("""What does 'MCB' stand for in modern electrical engineering?""",
     ["Main Current Battery",
      "Miniature Circuit Breaker",
      "Maximum Capacity Booster",
      "Micro Charge Balancer"],
     "B", "OSC", "easy",
     "• MCB stands for Miniature Circuit Breaker.\nCorrect Choice is (B)."),

    ("""What is a primary practical advantage of an MCB over a traditional cartridge fuse?""",
     ["MCB uses no electricity at all",
      "MCB can be quickly reset by flipping a switch once the fault is cleared, without needing to replace any burnt wire",
      "MCB makes the voltage zero everywhere",
      "MCB operates only during thunderstorms"],
     "B", "OSC", "easy",
     "• An MCB automatically trips off during an overload or short circuit and can be conveniently reset by hand after rectifying the fault.\nCorrect Choice is (B)."),

    ("""An electric iron of power \\(1000\\text{ W}\\) operates on a \\(230\\text{ V}\\) domestic supply. What is the approximate operating current, and which standard fuse rating should be selected?""",
     ["\\(2.1\\text{ A}\\), use \\(2\\text{ A}\\) fuse",
      "\\(4.35\\text{ A}\\), use \\(5\\text{ A}\\) fuse",
      "\\(10\\text{ A}\\), use \\(15\\text{ A}\\) fuse",
      "\\(20\\text{ A}\\), use \\(30\\text{ A}\\) fuse"],
     "B", "OSC", "medium",
     "• Operating current \\(I = \\frac{P}{V} = \\frac{1000}{230} \\approx 4.35\\text{ A}\\). The nearest safe standard fuse rating just above this current is \\(5\\text{ A}\\).\nCorrect Choice is (B)."),

    ("""What is a Residual Current Circuit Breaker (RCCB) primarily designed to detect?""",
     ["Slight drop in supply frequency",
      "Leakage of current to ground caused by human contact or insulation failure",
      "Overcharging of smartphones",
      "High ambient room temperature"],
     "B", "OSC", "medium",
     "• RCCB measures the difference between live and neutral currents; any imbalance (leakage current) trips the supply within \\(20\\text{--}30\\text{ ms}\\) to prevent electrocution.\nCorrect Choice is (B)."),

    ("""Why should a thick copper or iron wire NEVER be used as a makeshift fuse?""",
     ["Because copper is a bad conductor of electricity",
      "Because thick copper wire has a very high melting point and will not melt during a fault, causing house wiring to catch fire",
      "Because copper absorbs magnetic fields",
      "Because copper costs too little"],
     "B", "OSC", "medium",
     "• Thick copper wire has high current-carrying capacity and high melting point (\\(1085^\\circ\\text{C}\\)); it fails to melt during overload, destroying domestic appliances or igniting fires.\nCorrect Choice is (B)."),

    ("""Which circuit parameter directly triggers the thermal trip mechanism in an MCB?""",
     ["Bimetallic strip bending due to prolonged high current heating",
      "Water vapor condensation",
      "Radio waves from cell towers",
      "Static charge on plastic switches"],
     "A", "OSC", "medium",
     "• Prolonged overcurrent heats a bimetallic strip; due to unequal thermal expansion, it bends and mechanically releases the trip latch.\nCorrect Choice is (A)."),

    # 21-30: Short circuit vs Overloading, Earthing mechanism
    ("""What causes a 'SHORT CIRCUIT' in domestic wiring?""",
     ["Connecting one low-power LED lamp",
      "Direct physical contact between Live wire and Neutral wire due to worn-out insulation or appliance fault",
      "Turning off the main switch",
      "Switching on the geyser in winter"],
     "B", "OSC", "easy",
     "• A short circuit occurs when live and neutral wires touch directly, reducing circuit resistance to almost zero and causing a massive current surge.\nCorrect Choice is (B)."),

    ("""During a short circuit, how do resistance \\(R\\) and electric current \\(I\\) behave in the affected branch?""",
     ["Resistance becomes very large and current becomes zero",
      "Resistance drops to almost zero and current rises to an extremely large value",
      "Both resistance and current remain completely unchanged",
      "Current becomes negative while resistance doubles"],
     "B", "OSC", "easy",
     "• By Ohm's law \\(I = V/R\\), when \\(R \\to 0\\), current surges drastically, generating massive heat and sparks.\nCorrect Choice is (B)."),

    ("""What is meant by 'OVERLOADING' of an electrical circuit?""",
     ["Connecting a single \\(15\\text{ W}\\) bulb to a main switch",
      "Connecting too many high-power electrical appliances simultaneously to a single socket or circuit, drawing more current than the rated capacity of wires",
      "Switching on a ceiling fan during daytime",
      "Using an inverter during power cuts"],
     "B", "OSC", "easy",
     "• Overloading happens when total power demand draws current exceeding the safe current-carrying limit of the circuit wiring.\nCorrect Choice is (B)."),

    ("""How does earthing protect a person who touches an electric washing machine with damaged internal insulation?""",
     ["The earth wire absorbs the voltage and converts it to sound",
      "The low-resistance earth wire diverts the leakage current harmlessly to the ground, keeping the metal casing at near zero potential and blowing the fuse",
      "The earth wire doubles the power of the motor",
      "The earth wire prevents current from entering the house"],
     "B", "OSC", "medium",
     "• Human body resistance (\\(\\approx 1000\\text{--}100000\\,\\Omega\\)) is much higher than the earth wire (\\(< 1\\,\\Omega\\)); current preferentially flows to the ground through the earth wire.\nCorrect Choice is (B)."),

    ("""Why are charcoal and salt placed around the copper earth plate buried deep inside the ground?""",
     ["To generate extra electricity from soil chemical reactions",
      "To retain moisture and improve electrical conductivity of the surrounding soil, maintaining low earth resistance",
      "To prevent plant roots from growing into the copper plate",
      "To act as thermal insulation"],
     "B", "OSC", "medium",
     "• Salt and charcoal retain soil moisture and provide ionic conduction, keeping ground resistance extremely low for rapid dissipation of fault currents.\nCorrect Choice is (B)."),

    ("""Assertion (A): Domestic appliances are connected in parallel across the main supply lines.\nReason (R): In a parallel connection, every appliance receives the full rated potential difference (\\(230\\text{ V}\\)) and can be operated independently.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Parallel connection ensures identical \\(230\\text{ V}\\) voltage across each appliance and allows independent switching without interrupting others.\nCorrect Choice is (A)."),

    ("""Assertion (A): The electric fuse is always installed in the neutral wire.\nReason (R): The neutral wire carries returning electric current back to the substation.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is false, but (R) is true",
      "(A) is true, but (R) is false"],
     "C", "OAR", "medium",
     "• (A) is false: Fuse is strictly connected in the LIVE wire. If installed in neutral, blowing the fuse still leaves the live wire attached, causing electrocution hazard. (R) is true.\nCorrect Choice is (C)."),

    ("""Assertion (A): A person touching a live wire while standing barefoot on wet concrete gets a severe or fatal shock.\nReason (R): Wet skin and moist earth significantly reduce electrical resistance, allowing a large current to pass through the body to the ground.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Moisture dramatically drops skin resistance (from \\(100{,}000\\,\\Omega\\) dry down to \\(\\sim 1000\\,\\Omega\\) wet), creating an easy path for lethal current.\nCorrect Choice is (A)."),

    ("""State True or False: Two-pin plugs are safe for appliances with fully plastic, double-insulated outer casings (such as phone chargers or plastic table lamps).""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Double-insulated appliances (Class II) have non-conductive plastic bodies where internal faults cannot electrify an outer surface, so an earth pin is not needed.\nCorrect Choice is (A)."),

    ("""State True or False: If a \\(5\\text{ A}\\) fuse repeatedly blows in an air conditioner circuit, it is completely safe to replace it with a \\(30\\text{ A}\\) fuse without checking wire specifications.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Oversizing a fuse allows dangerous overcurrents to pass without tripping, causing wires inside walls to melt and ignite structure fires.\nCorrect Choice is (B)."),

    # 31-40: Safety precautions, calculations, numericals
    ("""What is the FIRST action that must be taken if a person comes into contact with a live electrical wire and is receiving an electric shock?""",
     ["Immediately pour a bucket of water on the person",
      "Switch off the main electrical supply switch or trip the circuit breaker immediately",
      "Grab the person's hands and pull forcefully with bare hands",
      "Wait 10 minutes for current to stop"],
     "B", "OSC", "easy",
     "• The primary and immediate action is to turn off the main switch to break the electrical circuit, stopping current through the victim.\nCorrect Choice is (B)."),

    ("""If the main switch cannot be reached immediately, how should an electric shock victim be separated from the live conductor?""",
     ["Using an aluminum ladder",
      "Using a dry wooden stick, rubber rod, or heavy dry cotton towel while standing on a dry non-conducting mat",
      "Using wet cloth gloves",
      "Using bare hands to tackle the victim"],
     "B", "OSC", "easy",
     "• Dry wood and rubber are electrical insulators that prevent the rescuer from becoming part of the circuit and suffering shock.\nCorrect Choice is (B)."),

    ("""Why should electrical switches and plug sockets never be operated with wet hands?""",
     ["Water damages the plastic casing color",
      "Water containing dissolved minerals is an electrical conductor, reducing skin contact resistance and creating a conductive path to live terminals",
      "Switches produce steam when touched by water",
      "Water reduces the voltage of the supply"],
     "B", "OSC", "easy",
     "• Normal tap water has dissolved ions making it conductive; moisture on skin drops electrical resistance to dangerous levels.\nCorrect Choice is (B)."),

    ("""A room has four \\(100\\text{ W}\\) bulbs and a \\(1000\\text{ W}\\) room heater connected to a \\(230\\text{ V}\\) supply. What is the total current drawn from the mains when all appliances are switched on?""",
     ["\\(1.5\\text{ A}\\)", "\\(3.8\\text{ A}\\)", "\\(6.09\\text{ A}\\)", "\\(12.5\\text{ A}\\)"],
     "C", "OSC", "medium",
     "• Total power \\(P = (4 \\times 100) + 1000 = 1400\\text{ W}\\).\nTotal current \\(I = \\frac{P}{V} = \\frac{1400}{230} \\approx 6.087\\text{ A} \\approx 6.09\\text{ A}\\).\nCorrect Choice is (C)."),

    ("""In a domestic circuit protected by a \\(5\\text{ A}\\) fuse, how many \\(60\\text{ W}\\) lamps at \\(230\\text{ V}\\) can be safely operated simultaneously without blowing the fuse?""",
     ["10 lamps", "15 lamps", "19 lamps", "25 lamps"],
     "C", "OSC", "medium",
     "• Maximum safe power \\(P_{\\max} = V \\times I = 230 \\times 5 = 1150\\text{ W}\\).\nNumber of lamps \\(n = \\frac{1150}{60} \\approx 19.16\\).\nThus, at most 19 lamps can run safely.\nCorrect Choice is (C)."),

    ("""A household electric circuit is rated for \\(15\\text{ A}\\) at \\(230\\text{ V}\\). Which of the following combinations of appliances can be safely operated simultaneously on this circuit?""",
     ["Two \\(2000\\text{ W}\\) water geysers",
      "A \\(1500\\text{ W}\\) geyser and a \\(1000\\text{ W}\\) electric iron",
      "A \\(2500\\text{ W}\\) induction cooker and a \\(2000\\text{ W}\\) heater",
      "Three \\(1800\\text{ W}\\) ovens"],
     "B", "OSC", "medium",
     "• Max capacity: \\(P = 230\\text{ V} \\times 15\\text{ A} = 3450\\text{ W}\\).\n(A) \\(4000\\text{ W}\\) (overload).\n(B) \\(1500 + 1000 = 2500\\text{ W} < 3450\\text{ W}\\) (safe).\n(C) \\(4500\\text{ W}\\) (overload).\n(D) \\(5400\\text{ W}\\) (overload).\nCorrect Choice is (B)."),

    ("""Fill in the blank: The wire having zero electrical potential with respect to the ground in a domestic electrical network is called the ________ wire.""",
     ["Live", "Neutral", "Phase", "High tension"],
     "B", "OFB", "easy",
     "• The neutral wire is grounded at the local distribution transformer and maintains zero potential.\nCorrect Choice is (B)."),

    ("""Fill in the blank: An automatic switch that cuts off the electrical supply during overload or short circuit using an internal electromagnet or bimetallic strip is known as a ________.""",
     ["Step-up transformer", "Miniature Circuit Breaker (MCB)", "Rheostat", "Galvanometer"],
     "B", "OFB", "easy",
     "• Miniature Circuit Breakers (MCBs) protect modern domestic circuits against overcurrents.\nCorrect Choice is (B)."),

    ("""Which of the following domestic appliances strictly requires a THREE-PIN plug with an effective Earth connection?""",
     ["Plastic LED table lamp",
      "Electric toaster with stainless steel outer chassis",
      "Battery-operated digital alarm clock",
      "Smartphone wall charger"],
     "B", "OSC", "easy",
     "• Appliances with exposed metal chassis (like a metallic toaster) present severe shock hazards if internal insulation touches the body, requiring direct earthing.\nCorrect Choice is (B)."),

    ("""What is the resistance of an ideal Earth connection in a domestic building electrical installation?""",
     ["Approximately \\(0\\,\\Omega\\) (less than \\(1\\,\\Omega\\))",
      "\\(1000\\,\\Omega\\)",
      "\\(100{,}000\\,\\Omega\\)",
      "Infinite resistance"],
     "A", "OSC", "easy",
     "• An effective earth ground should have very low resistance (less than \\(1\\,\\Omega\\) or at most \\(2\\,\\Omega\\)) to route fault currents quickly.\nCorrect Choice is (A).")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""What is the standard frequency of alternating current (AC) in domestic power supply in India?""",
     ["\\(25\\text{ Hz}\\)", "\\(50\\text{ Hz}\\)", "\\(60\\text{ Hz}\\)", "\\(100\\text{ Hz}\\)"],
     "B", "OSC", "easy",
     "• Standard domestic AC frequency in India is \\(50\\text{ Hz}\\) (50 complete cycles per second).\nCorrect Choice is (B)."),

    ("""In a domestic electrical cable, the brown insulated wire connects to:""",
     ["Live terminal", "Neutral terminal", "Earth terminal", "Direct ground"],
     "A", "OSC", "easy",
     "• In modern wiring standard (IEC), brown is the live conductor.\nCorrect Choice is (A)."),

    ("""In modern domestic wiring standards, the light blue wire connects to:""",
     ["Live terminal", "Neutral terminal", "Ground rod", "High voltage phase"],
     "B", "OSC", "easy",
     "• In IEC standards, light blue denotes the neutral wire.\nCorrect Choice is (B)."),

    ("""The green or green-yellow striped wire connects to:""",
     ["Live", "Neutral", "Earth (Ground)", "Phase 2"],
     "C", "OSC", "easy",
     "• Green or green-yellow represents safety ground (earth).\nCorrect Choice is (C)."),

    ("""Why are home appliances connected in parallel rather than in series?""",
     ["To decrease total power consumption to zero",
      "Because each appliance can operate independently with its own switch and receives the full \\(230\\text{ V}\\) rated voltage",
      "Because series wiring requires twice as many wires",
      "Because current is zero in parallel"],
     "B", "OSC", "easy",
     "• Parallel connection allows each appliance to receive full supply voltage and turn on/off independently without breaking the entire circuit.\nCorrect Choice is (B)."),

    ("""If home appliances were connected in series, what would happen when a single light bulb burned out?""",
     ["All other appliances on that circuit would immediately stop functioning",
      "All other bulbs would glow twice as bright",
      "Voltage across remaining bulbs would double",
      "The fuse would blow immediately"],
     "A", "OSC", "easy",
     "• In series, there is only one continuous path for current; if one device burns out (opens), current stops everywhere.\nCorrect Choice is (A)."),

    ("""A cartridge fuse contains a thin wire surrounded by:""",
     ["Water", "Glass or ceramic tube with metal caps", "Wood casing", "Rubber tube"],
     "B", "OSC", "easy",
     "• Cartridge fuses house the fuse element in a non-combustible glass or ceramic cylindrical body with metal end contacts.\nCorrect Choice is (B)."),

    ("""Which electrical quantity determines whether a fuse wire will melt?""",
     ["Electric current exceeding the rated ampere value",
      "Supply voltage dropping below \\(100\\text{ V}\\)",
      "High room air humidity",
      "Frequency dropping below \\(40\\text{ Hz}\\)"],
     "A", "OSC", "easy",
     "• Fuse melting is determined by overcurrent (\\(H = I^2 R t\\)); when current exceeds rated amperage, temperature exceeds the wire melting point.\nCorrect Choice is (A)."),

    ("""What happens to circuit resistance during a dead short circuit?""",
     ["It increases to infinity",
      "It drops to almost zero",
      "It remains constant at \\(100\\,\\Omega\\)",
      "It alternates between positive and negative"],
     "B", "OSC", "easy",
     "• Short circuit occurs when live and neutral come in direct contact with virtually zero load resistance.\nCorrect Choice is (B)."),

    ("""Why does a short circuit cause severe fire hazard?""",
     ["Because voltage becomes zero everywhere",
      "Because extremely high surge current through wire resistance produces intense heat by \\(H = I^2 R t\\), sparking or igniting insulation",
      "Because the battery discharges",
      "Because earth wire becomes positive"],
     "B", "OSC", "medium",
     "• High surge currents generate immense thermal energy according to Joule's law, capable of igniting plastic insulation and nearby combustible materials.\nCorrect Choice is (B)."),

    ("""What is the purpose of the main switch located at the consumer distribution board?""",
     ["To regulate room temperature",
      "To disconnect both live and neutral lines simultaneously, isolating the entire building from the power supply for maintenance and emergencies",
      "To measure daily electricity units",
      "To convert AC to DC"],
     "B", "OSC", "easy",
     "• The double-pole main switch disconnects both live and neutral simultaneously for complete safety.\nCorrect Choice is (B)."),

    ("""What is an electric shock physiologically?""",
     ["The sensation of heat on the skin",
      "The physiological effect caused when electric current passes through the body, causing involuntary muscle contractions or ventricular fibrillation",
      "A magnetic attraction to copper wires",
      "Static repulsion of clothes"],
     "B", "OSC", "easy",
     "• Electric shock occurs when external current flows through biological tissues, disrupting neural impulses and muscular control.\nCorrect Choice is (B)."),

    ("""Which current level through the human chest is generally considered potentially lethal (causing ventricular fibrillation)?""",
     ["\\(1\\text{ mA}\\)", "\\(5\\text{ mA}\\)", "\\(50\\text{ to }100\\text{ mA}\\)", "\\(10\\text{ A}\\)"],
     "C", "OSC", "medium",
     "• Current as low as \\(50\\text{--}100\\text{ mA}\\) (\\(0.05\\text{--}0.1\\text{ A}\\)) passing through the heart can induce fatal ventricular fibrillation.\nCorrect Choice is (C)."),

    ("""Why does a bird perching with both feet on a single high-voltage transmission wire NOT get electrocuted?""",
     ["Bird feathers are superconducting",
      "Both feet are on the same conductor at the same electrical potential, so potential difference between its feet is essentially zero and negligible current flows through its body",
      "Birds have infinitely high electrical resistance",
      "Transmission wires have zero voltage on their outer surface"],
     "B", "OSC", "medium",
     "• Electric current requires a potential difference (voltage gradient). Since both feet touch the same wire at virtually identical potential, \\(\\Delta V \\approx 0\\).\nCorrect Choice is (B)."),

    ("""Under what circumstance would the same perching bird suffer a fatal electric shock?""",
     ["If it sings loudly",
      "If its wing or body simultaneously touches another phase wire or a grounded steel transmission tower",
      "If the wire current increases",
      "If the wind blows against the wire"],
     "B", "OSC", "medium",
     "• Touching a grounded tower or adjacent wire creates a massive potential difference (e.g. \\(11\\text{ kV}\\)) across its body, causing immediate electrocution.\nCorrect Choice is (B)."),

    ("""What type of fuse is commonly used inside consumer electronic appliances such as amplifiers and microwave ovens?""",
     ["Porcelain re-wirable fuse", "Glass cartridge fuse", "High-voltage pole fuse", "Mercury switch fuse"],
     "B", "OSC", "easy",
     "• Compact glass cartridge fuses (with transparent tube to inspect the filament) are standard in electronic appliances.\nCorrect Choice is (B)."),

    ("""Why is an earth wire NOT required for a plastic-body electric immersion rod handle or plastic hair dryer labeled with the double-square symbol (Double Insulated)?""",
     ["Because double insulation provides two independent layers of non-conducting barriers, preventing any internal live wire from exposing high voltage to user touch",
      "Because plastic conducts electricity safely to the air",
      "Because hair dryers run on chemical fuel",
      "Because they use less than \\(1\\text{ V}\\)"],
     "A", "OSC", "medium",
     "• Class II double-insulated appliances have non-conductive enclosures ensuring that no single insulation breakdown can energize the outer surface.\nCorrect Choice is (A)."),

    ("""What is the purpose of the kWh (Kilowatt-hour) meter installed at the entrance of a building?""",
     ["To count the number of appliances in the house",
      "To measure the cumulative commercial electrical energy consumed over time for billing",
      "To regulate the incoming voltage to exactly \\(230\\text{ V}\\)",
      "To protect against lightning strikes"],
     "B", "OSC", "easy",
     "• The energy meter (electric meter) records energy consumption in \\(1\\text{ kWh} = 1\\text{ Unit} = 3.6 \\times 10^6\\text{ J}\\).\nCorrect Choice is (B)."),

    ("""In a domestic circuit, the fuse is connected to a \\(230\\text{ V}\\) line carrying an electric kettle rated \\(2300\\text{ W}\\). What minimum fuse rating is required?""",
     ["\\(5\\text{ A}\\)", "\\(10\\text{ A}\\)", "\\(13\\text{ A} \\text{ to } 15\\text{ A}\\)", "\\(30\\text{ A}\\)"],
     "C", "OSC", "medium",
     "• Operating current \\(I = \\frac{P}{V} = \\frac{2300}{230} = 10\\text{ A}\\). A fuse rating of at least \\(13\\text{ A}\\) or \\(15\\text{ A}\\) is selected to prevent nuisance blowing on startup.\nCorrect Choice is (C)."),

    ("""Which circuit element is shown in circuit diagrams as a zigzag line or rectangle with a diagonal line through it, or an S-curve inside a rectangle, representing a fuse?""",
     ["A circle with an arrow", "A rectangle with an axial line running through it", "Two parallel vertical lines", "A triangle pointing right"],
     "B", "OSC", "easy",
     "• Standard IEC schematic symbol for a fuse is a rectangle with a continuous straight line passing through the middle.\nCorrect Choice is (B)."),

    ("""State True or False: If an electrical fire breaks out, water should be sprayed on the wiring immediately to extinguish it.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Water is an electrical conductor and will conduct current back to the firefighter. Use dry chemical powder or \\(\\text{CO}_2\\) extinguishers after cutting power.\nCorrect Choice is (B)."),

    ("""State True or False: Earthing protects domestic appliances from high voltage spikes caused by lightning when a lightning arrester is grounded.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Proper grounding provides a direct, low-impedance path to earth for lightning discharge.\nCorrect Choice is (A)."),

    ("""An electric geyser is rated \\(3000\\text{ W},\\ 230\\text{ V}\\). How much current does it draw from the mains supply?""",
     ["\\(6.52\\text{ A}\\)", "\\(13.04\\text{ A}\\)", "\\(23.0\\text{ A}\\)", "\\(30.0\\text{ A}\\)"],
     "B", "OSC", "medium",
     "• Current \\(I = \\frac{P}{V} = \\frac{3000}{230} \\approx 13.04\\text{ A}\\).\nCorrect Choice is (B)."),

    ("""Why are two separate power circuits (\\(5\\text{ A}\\) and \\(15\\text{ A}\\)) commonly installed in Indian residences?""",
     ["\\(5\\text{ A}\\) circuit is for lighting, fans, and low-power electronics, while \\(15\\text{ A}\\) circuit is for heavy appliances like geysers, ACs, and heaters with thicker wiring",
      "One is for daytime and the other is for night",
      "One is for AC and the other is for DC",
      "To keep voltage lower in bedrooms"],
     "A", "OSC", "easy",
     "• Dedicated \\(15\\text{ A}\\) power circuits use heavier gauge wire to safely carry high current without resistive heating.\nCorrect Choice is (A)."),

    ("""Fill in the blank: The potential difference between two neutral wires from the same balanced transformer phase is ________ volts.""",
     ["\\(0\\)", "\\(115\\)", "\\(230\\)", "\\(440\\)"],
     "A", "OFB", "easy",
     "• Both neutral conductors are at zero ground reference potential, so potential difference between them is \\(0\\text{ V}\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: An alloy consisting of \\(63\\%\\) Tin and \\(37\\%\\) Lead forms a eutectic solder with a low melting point of about ________ \\(^\\circ\\text{C}\\).""",
     ["\\(100\\)", "\\(183\\)", "\\(500\\)", "\\(1085\\)"],
     "B", "OFB", "medium",
     "• \\(63/37\\) Sn-Pb solder melts sharply at \\(183^\\circ\\text{C}\\), making it ideal for fuse elements.\nCorrect Choice is (B)."),

    ("""Which device protects sensitive computers and home appliances from momentary high voltage spikes on the grid?""",
     ["Surge Protector / Metal Oxide Varistor (MOV)", "Rheostat", "Voltmeter", "Electrolytic capacitor only"],
     "A", "OSC", "easy",
     "• Surge protectors clamp transient overvoltage spikes by conducting surge currents safely to ground via MOVs.\nCorrect Choice is (A)."),

    ("""If a human body has an internal resistance of \\(1000\\,\\Omega\\) when wet, what current passes through the body when touching a \\(230\\text{ V}\\) live line while grounded?""",
     ["\\(0.023\\text{ A}\\)", "\\(0.23\\text{ A}\\ (230\\text{ mA})\\)", "\\(2.3\\text{ A}\\)", "\\(23\\text{ A}\\)"],
     "B", "OSC", "medium",
     "• By Ohm's law: \\(I = \\frac{V}{R} = \\frac{230\\text{ V}}{1000\\,\\Omega} = 0.23\\text{ A} = 230\\text{ mA}\\). This is well above the lethal fibrillation threshold (\\(50\\text{--}100\\text{ mA}\\)).\nCorrect Choice is (B)."),

    ("""What type of fire extinguisher is strictly used for electrical fires where live power may still be present?""",
     ["Water jet extinguisher", "Carbon dioxide (\\(\\text{CO}_2\\)) or Dry Chemical Powder extinguisher", "Foam extinguisher", "Acid extinguisher"],
     "B", "OSC", "easy",
     "• \\(\\text{CO}_2\\) and dry powder are non-conductive agents that smother flames without electrocuting the operator.\nCorrect Choice is (B)."),

    ("""What is the primary function of earthing in multi-storey residential buildings?""",
     ["To increase electric power supplied to upper floors",
      "To provide a zero-potential safe dissipation sink for leakage currents, static charges, and lightning discharge",
      "To eliminate the need for monthly power bills",
      "To run ceiling fans without switches"],
     "B", "OSC", "easy",
     "• Earthing establishes a common zero-voltage safety reference, safely dissipating leakage currents and lightning surges.\nCorrect Choice is (B).")
]

# 12 Foundation Mock Questions (501-512) with rich embedded vector SVGs
foundation_data = [
    # 501: Three-Pin Plug Anatomy
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="95" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Three-Pin Plug Architecture</text>
  <!-- Earth Pin (Top) -->
  <rect x="155" y="45" width="30" height="40" rx="6" fill="#10b981" stroke="#34d399" stroke-width="2"/>
  <text x="135" y="100" fill="#34d399" font-size="11" font-weight="bold">Earth Pin (E)</text>
  <text x="130" y="115" fill="#94a3b8" font-size="9">(Longer &amp; Thicker)</text>
  <!-- Live Pin (Bottom Right) -->
  <rect x="220" y="130" width="22" height="30" rx="4" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
  <text x="210" y="175" fill="#f87171" font-size="11" font-weight="bold">Live (L)</text>
  <text x="205" y="190" fill="#94a3b8" font-size="9">Brown / Red</text>
  <!-- Neutral Pin (Bottom Left) -->
  <rect x="98" y="130" width="22" height="30" rx="4" fill="#3b82f6" stroke="#60a5fa" stroke-width="2"/>
  <text x="80" y="175" fill="#60a5fa" font-size="11" font-weight="bold">Neutral (N)</text>
  <text x="82" y="190" fill="#94a3b8" font-size="9">Blue / Black</text>
</svg>
</div>
In the three-pin plug schematic shown above, why is the top Earth pin (E) engineered with a larger length and cross-sectional thickness compared to the Live (L) and Neutral (N) pins?""",
     ["To fit snugly and prevent insertion into smaller live/neutral sockets, while ensuring ground contact is made first before power arrives and broken last upon removal",
      "Because Earth pin carries 440 V high voltage",
      "To allow current to oscillate between live and earth pins equally",
      "To act as a spare replacement pin if the live pin bends"],
     "A", "OSC", "hard",
     "• The earth pin is longer so that it grounds the metal frame before the appliance becomes energized. It is thicker so that it cannot physically enter live or neutral socket openings.\nCorrect Choice is (A)."),

    # 502: Cartridge Fuse Structure
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <text x="95" y="28" fill="#38bdf8" font-size="13" font-weight="bold">Cartridge Fuse Structure</text>
  <!-- End caps -->
  <rect x="40" y="70" width="35" height="60" rx="3" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="265" y="70" width="35" height="60" rx="3" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5"/>
  <!-- Glass body -->
  <rect x="75" y="75" width="190" height="50" fill="#1e293b" stroke="#475569" stroke-width="2"/>
  <!-- Fuse wire -->
  <line x1="75" y1="100" x2="265" y2="100" stroke="#f59e0b" stroke-width="3" stroke-dasharray="8 4"/>
  <text x="110" y="93" fill="#f59e0b" font-size="11" font-weight="bold">Pb-Sn Alloy Fuse Wire</text>
  <!-- Labels -->
  <text x="25" y="150" fill="#cbd5e1" font-size="10">Brass Cap</text>
  <text x="120" y="150" fill="#cbd5e1" font-size="10">Glass/Ceramic Tube</text>
  <text x="250" y="150" fill="#cbd5e1" font-size="10">Brass Cap</text>
  <text x="50" y="180" fill="#93c5fd" font-size="10">Melting Point: ~183°C | Protects against Overcurrent</text>
</svg>
</div>
The figure illustrates a standard cartridge fuse. If this fuse is rated \\(5\\text{ A}\\) and a fault current of \\(18\\text{ A}\\) surges through it, what physical event takes place?""",
     ["Joule heating generates heat exceeding the alloy's low melting point, melting the wire and opening the circuit in fractions of a second",
      "The glass cartridge expands and stores the excess electrical charge indefinitely",
      "The wire resistance drops to zero and conducts all current to ground safely",
      "The brass caps magnetize and pull the wire outward without breaking it"],
     "A", "OSC", "medium",
     "• Heat produced \\(H = I^2 R t\\) rapidly exceeds the wire's dissipation capacity, melting the Pb-Sn alloy wire and breaking the path of current.\nCorrect Choice is (A)."),

    # 503: Earthing Protection Loop
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="80" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Earthing Safety Protection Circuit</text>
  <!-- Appliance Metal Case -->
  <rect x="40" y="50" width="130" height="90" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <text x="50" y="70" fill="#e2e8f0" font-size="11" font-weight="bold">Electric Refrigerator</text>
  <!-- Live wire fault -->
  <line x1="10" y1="95" x2="105" y2="95" stroke="#ef4444" stroke-width="2.5"/>
  <circle cx="105" cy="95" r="4" fill="#ef4444"/>
  <text x="15" y="90" fill="#ef4444" font-size="9">Live 230V</text>
  <text x="45" y="125" fill="#f87171" font-size="9">Insulation Fault (Touches Case)</text>
  <!-- Earth wire to ground -->
  <line x1="150" y1="140" x2="150" y2="180" stroke="#10b981" stroke-width="3"/>
  <line x1="130" y1="180" x2="170" y2="180" stroke="#10b981" stroke-width="3"/>
  <line x1="138" y1="186" x2="162" y2="186" stroke="#10b981" stroke-width="2.5"/>
  <line x1="144" y1="192" x2="156" y2="192" stroke="#10b981" stroke-width="2"/>
  <!-- Human touching case -->
  <circle cx="250" cy="80" r="14" fill="#fde047"/>
  <line x1="250" y1="94" x2="250" y2="145" stroke="#fde047" stroke-width="3"/>
  <line x1="250" y1="110" x2="170" y2="100" stroke="#fde047" stroke-width="2.5"/>
  <text x="215" y="165" fill="#fde047" font-size="10">User (R ~ 10,000 Ω)</text>
  <text x="100" y="215" fill="#34d399" font-size="10">Earth Path (R &lt; 1 Ω): Fault current bypasses user</text>
</svg>
</div>
In the fault scenario diagram above, an insulation failure causes the 230V live wire to contact the metal chassis of the refrigerator. Why does the person touching the chassis NOT receive a lethal shock?""",
     ["Because the user has lower resistance than copper",
      "Because the earth wire provides an ultra-low resistance path (\\(< 1\\,\\Omega\\)) compared to human body (\\(\\sim 10{,}000\\,\\Omega\\)), draining current to ground and blowing the fuse",
      "Because the refrigerator motor reverses direction and cancels the voltage",
      "Because alternating current cannot flow through human skin"],
     "B", "OSC", "hard",
     "• Current divides in inverse ratio of resistance. The earth wire resistance is negligible (\\(< 1\\,\\Omega\\)) relative to human body (\\(> 1000\\,\\Omega\\)), channeling virtually all current safely to ground and tripping protection.\nCorrect Choice is (B)."),

    # 504: Short Circuit vs Normal Load Circuit
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="85" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Short Circuit vs Normal Operation</text>
  <!-- Mains supply -->
  <text x="20" y="70" fill="#ef4444" font-size="10" font-weight="bold">Live (230V)</text>
  <text x="20" y="150" fill="#60a5fa" font-size="10" font-weight="bold">Neutral (0V)</text>
  <line x1="90" y1="65" x2="280" y2="65" stroke="#ef4444" stroke-width="2.5"/>
  <line x1="90" y1="145" x2="280" y2="145" stroke="#60a5fa" stroke-width="2.5"/>
  <!-- Normal Load -->
  <rect x="260" y="85" width="40" height="40" fill="#334155" stroke="#94a3b8" rx="4"/>
  <text x="265" y="110" fill="#f8fafc" font-size="9">Load R</text>
  <line x1="280" y1="65" x2="280" y2="85" stroke="#ef4444" stroke-width="2"/>
  <line x1="280" y1="125" x2="280" y2="145" stroke="#60a5fa" stroke-width="2"/>
  <!-- Direct Short Circuit Fault Contact -->
  <line x1="160" y1="65" x2="160" y2="145" stroke="#f59e0b" stroke-width="4"/>
  <circle cx="160" cy="105" r="10" fill="#ef4444"/>
  <text x="145" y="108" fill="#fff" font-size="11" font-weight="bold">⚡</text>
  <text x="100" y="180" fill="#fca5a5" font-size="10" font-weight="bold">Short Contact: R ≈ 0 → I → ∞ (Sparks &amp; Fire)</text>
</svg>
</div>
Referring to the electrical fault diagram, when the live and neutral wires touch directly at point ⚡ (bypassing load \\(R\\)), what happens to the electric current \\(I\\) and why?""",
     ["Current drops to zero because electricity gets confused",
      "Current surges to an extremely dangerous magnitude because the circuit resistance drops to near zero (\\(I = V / R \\to \\infty\\))",
      "Current stays the same because supply voltage is constant at 230V",
      "Current converts from AC to DC"],
     "B", "OSC", "medium",
     "• In a short circuit, bypass of the load resistance causes total resistance \\(R \\to 0\\). By Ohm's law \\(I = V/R\\), current skyrockets causing intense heating and sparks.\nCorrect Choice is (B)."),

    # 505: Overloading Schematic
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="95" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Circuit Overloading Mechanism</text>
  <!-- Multi-plug Socket Adapter -->
  <rect x="30" y="60" width="70" height="100" fill="#1e293b" stroke="#cbd5e1" stroke-width="2" rx="4"/>
  <text x="35" y="115" fill="#93c5fd" font-size="10" font-weight="bold">Single 5A Socket</text>
  <!-- 3 Heavy Loads plugged in -->
  <rect x="150" y="45" width="85" height="30" fill="#334155" rx="3"/>
  <text x="155" y="65" fill="#fde047" font-size="10">Heater: 1500W (6.5A)</text>
  <rect x="150" y="90" width="85" height="30" fill="#334155" rx="3"/>
  <text x="155" y="110" fill="#fde047" font-size="10">Iron: 1000W (4.3A)</text>
  <rect x="150" y="135" width="85" height="30" fill="#334155" rx="3"/>
  <text x="155" y="155" fill="#fde047" font-size="10">Geyser: 2000W (8.7A)</text>
  <!-- Current Sum -->
  <text x="35" y="195" fill="#ef4444" font-size="11" font-weight="bold">Total Current I = 6.5 + 4.3 + 8.7 = 19.5 A &gt;&gt; 5 A Rated Limit!</text>
</svg>
</div>
Based on the multi-plug diagram above, what dangerous condition has occurred and what is its primary effect on the domestic wall wiring?""",
     ["Short circuit; voltage increases to 1000V",
      "Overloading; total current drawn (19.5A) greatly exceeds the safe limit (5A), causing wiring inside walls to overheat and potentially melt insulation",
      "Phase cancellation; no power reaches any appliance",
      "Earthing failure; the wall gets magnetized"],
     "B", "OSC", "medium",
     "• Operating multiple high-wattage loads simultaneously on a single circuit draws cumulative current far in excess of wire rating, causing hazardous resistive overheating (overloading).\nCorrect Choice is (B)."),

    # 506: Miniature Circuit Breaker (MCB) Mechanism
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">MCB Dual-Trip Principle</text>
  <!-- Bimetallic strip (Thermal) -->
  <rect x="30" y="55" width="130" height="65" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="4"/>
  <text x="40" y="75" fill="#f59e0b" font-size="10" font-weight="bold">1. Thermal Trip (Bimetal)</text>
  <text x="40" y="95" fill="#cbd5e1" font-size="9">• Slow Overload Protection</text>
  <text x="40" y="110" fill="#cbd5e1" font-size="9">• Bending releases latch</text>
  <!-- Solenoid / Coil (Magnetic) -->
  <rect x="180" y="55" width="130" height="65" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <text x="190" y="75" fill="#38bdf8" font-size="10" font-weight="bold">2. Magnetic Trip (Solenoid)</text>
  <text x="190" y="95" fill="#cbd5e1" font-size="9">• Instant Short Circuit Trip</text>
  <text x="190" y="110" fill="#cbd5e1" font-size="9">• Plunger fires within &lt;10ms</text>
  <!-- Reset Toggle Switch -->
  <rect x="120" y="135" width="100" height="40" fill="#334155" stroke="#10b981" stroke-width="2" rx="4"/>
  <text x="135" y="160" fill="#10b981" font-size="11" font-weight="bold">Reset Lever (ON/OFF)</text>
  <text x="40" y="200" fill="#94a3b8" font-size="10">Reusable protection without wire replacement</text>
</svg>
</div>
How does an MCB provide dual-action protection against electrical circuit hazards?""",
     ["It uses a chemical battery and a water cooling pump",
      "It combines a bimetallic strip for slow thermal overload trip and an electromagnetic solenoid for instantaneous short-circuit trip",
      "It converts AC to DC during high current",
      "It uses optical lasers to detect smoke"],
     "B", "OSC", "hard",
     "• MCBs employ two tripping mechanisms: a bimetallic strip that bends under sustained moderate overcurrent (thermal protection), and a solenoid that instantaneously moves a plunger during extreme short circuits (magnetic protection).\nCorrect Choice is (B)."),

    # 507: Domestic Distribution Board Layout
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="75" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Domestic Consumer Supply Sequence</text>
  <!-- Flow Blocks -->
  <rect x="20" y="50" width="75" height="35" fill="#1e293b" stroke="#94a3b8" rx="3"/>
  <text x="25" y="72" fill="#e2e8f0" font-size="9">Electric Pole</text>
  <text x="100" y="72" fill="#38bdf8" font-size="12">→</text>
  <rect x="120" y="50" width="85" height="35" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="125" y="72" fill="#f59e0b" font-size="9">Company Fuse</text>
  <text x="210" y="72" fill="#38bdf8" font-size="12">→</text>
  <rect x="230" y="50" width="90" height="35" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="235" y="72" fill="#10b981" font-size="9">kWh Meter</text>
  <!-- Down Arrow -->
  <text x="270" y="110" fill="#38bdf8" font-size="14">↓</text>
  <!-- Main Switch & MCB Box -->
  <rect x="180" y="125" width="140" height="40" fill="#334155" stroke="#38bdf8" rx="4"/>
  <text x="190" y="150" fill="#38bdf8" font-size="10" font-weight="bold">Main Switch + MCB Board</text>
  <!-- Parallel Branch Circuits -->
  <rect x="20" y="180" width="135" height="35" fill="#1e293b" stroke="#60a5fa" rx="3"/>
  <text x="25" y="202" fill="#93c5fd" font-size="9">5A Lighting Circuit (Parallel)</text>
  <rect x="180" y="180" width="140" height="35" fill="#1e293b" stroke="#f87171" rx="3"/>
  <text x="185" y="202" fill="#fca5a5" font-size="9">15A Power Circuit (Parallel)</text>
</svg>
</div>
What is the correct logical sequence of electrical equipment encountered by power arriving at a home from the street transmission line?""",
     ["Consumer Appliances → kWh Meter → Main Switch → Substation",
      "Electric Pole → Electricity Board Fuse → kWh Meter → Main Switch / MCB Board → Domestic Parallel Sub-circuits",
      "Main Switch → Street Pole → Fuse → Domestic Appliances",
      "Earthing Pit → Lighting Circuit → kWh Meter → Electric Pole"],
     "B", "OSC", "medium",
     "• Electricity enters via the board's sealed main service fuse, passes through the revenue kWh meter, enters the consumer main switch/MCB distribution board, and branches to individual parallel load circuits.\nCorrect Choice is (B)."),

    # 508: Earthing Pit Design
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="105" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Earth Pit Cross-Section</text>
  <!-- Ground level -->
  <line x1="20" y1="50" x2="320" y2="50" stroke="#78350f" stroke-width="3"/>
  <text x="25" y="45" fill="#a16207" font-size="10">Ground Surface Level</text>
  <!-- Pit dug in earth -->
  <rect x="80" y="60" width="180" height="150" fill="#292524" stroke="#44403c" rx="4"/>
  <!-- Charcoal and salt layers -->
  <rect x="100" y="90" width="140" height="100" fill="#1c1917" stroke="#78716c" stroke-dasharray="3 3"/>
  <text x="110" y="115" fill="#cbd5e1" font-size="10">Alternate Layers of</text>
  <text x="110" y="130" fill="#fde047" font-size="10">Charcoal &amp; Salt</text>
  <!-- Copper Earth Plate -->
  <rect x="160" y="80" width="16" height="110" fill="#b45309" stroke="#d97706" stroke-width="2"/>
  <!-- Earth Conductor Wire going up -->
  <line x1="168" y1="80" x2="168" y2="35" stroke="#10b981" stroke-width="3"/>
  <text x="180" y="42" fill="#34d399" font-size="10">Copper Conductor to Home</text>
  <text x="50" y="205" fill="#93c5fd" font-size="9">Keeps earth resistance &lt; 1 Ω by maintaining soil moisture &amp; ions</text>
</svg>
</div>
In the earthing pit cross-section shown, what is the specific chemical and physical function of adding alternate layers of powdered charcoal and common salt (\\(\\text{NaCl}\\)) around the copper plate?""",
     ["Charcoal and salt prevent copper from melting at room temperature",
      "Common salt dissociates into conductive ions (\\(\\text{Na}^+, \\text{Cl}^-\\)) while charcoal retains moisture, drastically lowering the ground contact resistance",
      "They neutralize alternating current to produce direct current in the ground",
      "They keep insects away from the electrical cables"],
     "B", "OSC", "hard",
     "• Common salt dissociates into mobile ions to enhance electrolytic conductivity, and porous charcoal absorbs and retains moisture, maintaining minimal grounding resistance (\\(< 1\\,\\Omega\\)).\nCorrect Choice is (B)."),

    # 509: Residual Current Circuit Breaker (RCCB) Differential Core
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="25" fill="#38bdf8" font-size="13" font-weight="bold">RCCB Differential Sensing Toroid</text>
  <!-- Toroidal Core -->
  <circle cx="170" cy="115" r="50" fill="none" stroke="#64748b" stroke-width="14"/>
  <!-- Live coil -->
  <text x="35" y="80" fill="#ef4444" font-size="10" font-weight="bold">Live In (I_L)</text>
  <line x1="20" y1="95" x2="135" y2="95" stroke="#ef4444" stroke-width="3"/>
  <!-- Neutral coil -->
  <text x="35" y="155" fill="#60a5fa" font-size="10" font-weight="bold">Neutral Out (I_N)</text>
  <line x1="20" y1="135" x2="135" y2="135" stroke="#60a5fa" stroke-width="3"/>
  <!-- Condition -->
  <text x="180" y="105" fill="#10b981" font-size="9">Normal: I_L = I_N</text>
  <text x="180" y="120" fill="#10b981" font-size="9">Net Flux Φ = 0</text>
  <text x="180" y="140" fill="#ef4444" font-size="9">Leakage: I_L ≠ I_N</text>
  <text x="180" y="155" fill="#ef4444" font-size="9">Trips in &lt; 30 ms!</text>
  <text x="40" y="195" fill="#cbd5e1" font-size="10">Detects shock current leaking through a human body</text>
</svg>
</div>
How does an RCCB (Residual Current Circuit Breaker) detect that a person is receiving an electric shock from a faulty appliance?""",
     ["It detects that the wire temperature has reached 500°C",
      "It compares current entering through the Live wire (\\(I_L\\)) with current returning through the Neutral wire (\\(I_N\\)); if \\(I_L \\ne I_N\\) due to current leaking through the person to ground, it trips instantly",
      "It waits for the person to scream loudly",
      "It senses the change in air pressure in the room"],
     "B", "OSC", "hard",
     "• Under normal conditions, \\(I_{\\text{Live}} = I_{\\text{Neutral}}\\). If leakage to ground occurs (e.g. through a person), \\(I_L - I_N > 30\\text{ mA}\\), inducing magnetic flux in the sensing toroid that trips the breaker in milliseconds.\nCorrect Choice is (B)."),

    # 510: Fuse in Live vs Neutral Comparison
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Why Fuse Must Be in the LIVE Wire</text>
  <!-- Correct Configuration -->
  <text x="25" y="60" fill="#10b981" font-size="11" font-weight="bold">✓ SAFE: Fuse in Live Wire</text>
  <line x1="25" y1="80" x2="60" y2="80" stroke="#ef4444" stroke-width="2"/>
  <rect x="60" y="73" width="25" height="14" fill="#f59e0b" rx="2"/>
  <line x1="85" y1="80" x2="130" y2="80" stroke="#ef4444" stroke-width="2"/>
  <rect x="130" y="70" width="30" height="20" fill="#334155" rx="2"/>
  <text x="135" y="84" fill="#fff" font-size="8">Load</text>
  <text x="170" y="84" fill="#34d399" font-size="9">Blown fuse cuts 230V off completely!</text>
  <!-- Dangerous Configuration -->
  <text x="25" y="130" fill="#ef4444" font-size="11" font-weight="bold">✗ DANGEROUS: Fuse in Neutral Wire</text>
  <line x1="25" y1="150" x2="130" y2="150" stroke="#ef4444" stroke-width="2"/>
  <rect x="130" y="140" width="30" height="20" fill="#334155" rx="2"/>
  <text x="135" y="154" fill="#fff" font-size="8">Load</text>
  <line x1="160" y1="150" x2="200" y2="150" stroke="#3b82f6" stroke-width="2"/>
  <rect x="200" y="143" width="25" height="14" fill="#f59e0b" rx="2"/>
  <text x="40" y="190" fill="#fca5a5" font-size="10">Load remains at 230V live potential even when fuse blows!</text>
</svg>
</div>
What fatal hazard occurs if an electrician mistakenly connects the safety fuse in the NEUTRAL wire instead of the LIVE wire?""",
     ["The appliances will run backwards",
      "Even when the fuse blows and breaks the neutral return, the appliance remains directly connected to the 230V live wire; touching internal parts will deliver a fatal shock",
      "The electricity bill will increase tenfold",
      "The fuse will never melt under any circumstances"],
     "B", "OSC", "hard",
     "• If the fuse is on the neutral line, blowing it breaks the return circuit so appliances stop working, but the entire internal circuit remains energized at \\(230\\text{ V}\\) live potential, posing extreme shock hazard.\nCorrect Choice is (B)."),

    # 511: Resistance vs Temperature of Fuse Wire
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Joule Heating of Fuse Element</text>
  <!-- Coordinate axes -->
  <line x1="60" y1="160" x2="300" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <line x1="60" y1="160" x2="60" y2="40" stroke="#94a3b8" stroke-width="2"/>
  <text x="140" y="180" fill="#cbd5e1" font-size="10">Current Squared (I²)</text>
  <text x="15" y="100" fill="#cbd5e1" font-size="10" transform="rotate(-90 15,100)">Heat Rate (H/t)</text>
  <!-- Linear graph line H/t = I^2 * R -->
  <line x1="60" y1="160" x2="270" y2="55" stroke="#f59e0b" stroke-width="3"/>
  <circle cx="210" cy="85" r="5" fill="#ef4444"/>
  <text x="220" y="85" fill="#ef4444" font-size="10" font-weight="bold">Melting Threshold (T_melt)</text>
  <text x="70" y="60" fill="#38bdf8" font-size="10">H = I² · R · t (Joule's Law)</text>
</svg>
</div>
According to Joule's heating law \\(H = I^2 R t\\) shown in the graph, if the current through a fuse doubles from \\(2\\text{ A}\\) to \\(4\\text{ A}\\) while resistance remains roughly constant, by what factor does the rate of thermal energy generation increase?""",
     ["Doubles (factor of 2)",
      "Quadruples (factor of 4, since \\(H \\propto I^2\\))",
      "Increases eightfold (factor of 8)",
      "Remains unchanged"],
     "B", "OSC", "medium",
     "• Heat rate is directly proportional to the square of current: \\(P_{\\text{heat}} \\propto I^2\\). Doubling current multiplies heat production by \\(2^2 = 4\\).\nCorrect Choice is (B)."),

    # 512: Electrical Safety Protocol Infographic
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="80" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Emergency Electric Shock Action</text>
  <!-- Step 1 -->
  <circle cx="55" cy="70" r="18" fill="#ef4444"/>
  <text x="50" y="76" fill="#fff" font-size="14" font-weight="bold">1</text>
  <text x="85" y="65" fill="#fca5a5" font-size="11" font-weight="bold">Turn OFF Mains Immediately</text>
  <text x="85" y="80" fill="#cbd5e1" font-size="9">Cut the circuit at main switch / MCB</text>
  <!-- Step 2 -->
  <circle cx="55" cy="125" r="18" fill="#f59e0b"/>
  <text x="50" y="131" fill="#fff" font-size="14" font-weight="bold">2</text>
  <text x="85" y="120" fill="#fde047" font-size="11" font-weight="bold">Isolate with Insulator</text>
  <text x="85" y="135" fill="#cbd5e1" font-size="9">Use dry wood or rubber; NEVER bare hands</text>
  <!-- Step 3 -->
  <circle cx="55" cy="180" r="18" fill="#10b981"/>
  <text x="50" y="186" fill="#fff" font-size="14" font-weight="bold">3</text>
  <text x="85" y="175" fill="#34d399" font-size="11" font-weight="bold">Call Emergency Medical Help &amp; CPR</text>
  <text x="85" y="190" fill="#cbd5e1" font-size="9">Check pulse; administer artificial respiration</text>
</svg>
</div>
In the electrical emergency protocol above, why must a rescuer NEVER attempt to pull an electric shock victim away using their bare hands?""",
     ["Because the victim's clothes might tear",
      "Because the victim's body is at live electrical potential; touching with bare hands creates a parallel conductive path to ground through the rescuer, electrocuting both persons",
      "Because human sweat dissolves copper wires",
      "Because electrical current reverses into magnetic flux upon contact"],
     "B", "OSC", "medium",
     "• The human body is a conductor. Touching a victim in contact with live current forms a circuit through the rescuer to ground, causing both individuals to be electrocuted.\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-3-3.6-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-3-3.6-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-3-3.6-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch3_topic6.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
