# -*- coding: utf-8 -*-
"""
Generator for MH-9-SCIT-9-9.4: Disaster Management: First Aid Principles (RICE, ABC & Patient Transportation)
40 Exam + 30 Practice + 12 Mock (with SVGs) = 82 Questions
"""
import json

TOPIC_CODE = "MH-9-SCIT-9-9.4"
OUTPUT_FILE = "scripts/ch9_topic4.json"

exam_data = [
    {
        "q": "What does the acronym 'ABC' stand for in emergency first aid evaluation?",
        "options": [
            "Airway, Breathing, Circulation",
            "Accident, Bleeding, Casualty",
            "Action, Bandage, Care",
            "Alertness, Breathing, Consciousness"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The ABC rule of first aid prioritizes: A - Airway (clear of obstruction), B - Breathing (respiratory ventilation), and C - Circulation (cardiac pulse and blood flow)."
    },
    {
        "q": "What is the primary action of the 'R' in the RICE principle used for soft tissue injuries like sprains and contusions?",
        "options": [
            "Rest: Immobilize the injured joint or limb immediately to prevent further ligament damage",
            "Run: Exercise the joint vigorously to warm up muscles",
            "Rub: Massage the swollen area intensely with force",
            "Radiate: Expose the wound to direct ultraviolet sunlight"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "'R' stands for Rest. Stopping physical activity and immobilizing the affected area protects injured ligaments and muscle fibers from aggravated tearing."
    },
    {
        "q": "What is the recommended compression-to-breath ratio when performing Cardiopulmonary Resuscitation (CPR) on an unresponsive adult casualty?",
        "options": ["30 chest compressions to 2 rescue breaths", "10 chest compressions to 5 rescue breaths", "50 chest compressions to 10 rescue breaths", "5 chest compressions to 1 rescue breath"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Standard international resuscitation guidelines mandate 30 chest compressions followed by 2 rescue breaths (a 30:2 cycle) at a rate of 100-120 compressions per minute."
    },
    {
        "q": "Why is ice applied to an acute ankle sprain under the 'I' of the RICE protocol?",
        "options": [
            "Cold causes local vasoconstriction, reducing internal blood leakage, edema, and numbing pain",
            "Cold causes vasodilation to increase bleeding into the joint",
            "Cold permanently freezes the bones together",
            "Cold turns the skin completely sterile"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Applying cold constricts blood vessels (vasoconstriction), which limits localized swelling and inflammatory fluid accumulation while depressing pain receptor excitability."
    },
    {
        "q": "What is the immediate, life-saving first aid treatment for a second-degree burn on a person's forearm?",
        "options": [
            "Cool the burned area under clean, cold running water for at least 10 to 15 minutes",
            "Apply butter, ghee, or cooking oil over the blisters",
            "Puncture all blister bubbles with a sewing needle",
            "Wrap the burn tightly with unsterilized adhesive tape"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Cooling under gentle running tap water for 10-15 minutes halts thermal tissue injury, reduces edema, and relieves intense burning pain. Greases and needle punctures introduce severe infections."
    },
    {
        "q": "Under the RICE protocol, why should an injured swollen sprained ankle be elevated above heart level ('E' - Elevation)?",
        "options": [
            "To promote venous blood and lymphatic fluid drainage back toward the heart, reducing localized swelling",
            "To make the leg longer than the other leg",
            "To prevent the patient from ever walking again",
            "To increase arterial blood rushing into the injury"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Elevating the injured extremity uses gravity to assist venous return and lymphatic drainage, drastically decreasing interstitial fluid buildup (edema)."
    },
    {
        "q": "Which emergency maneuver is performed on a conscious adult who is choking and unable to speak or cough due to a complete airway obstruction?",
        "options": ["Heimlich maneuver (abdominal thrusts)", "RICE protocol", "Mouth-to-mouth resuscitation", "Direct sternal fracture"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The Heimlich maneuver delivers quick inward and upward abdominal thrusts just above the navel, elevating the diaphragm and forcing air out of the lungs to expel the obstruction."
    },
    {
        "q": "When a victim suffers a bone fracture in the lower leg, what is the crucial rule when applying an emergency splint?",
        "options": [
            "Immobilize the fractured bone as well as the joints immediately above and below the fracture site",
            "Forcefully snap and twist the bone back into straight alignment",
            "Tighten metal wire directly over the skin until bleeding stops",
            "Ask the victim to run on the fractured leg to test bone strength"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "An effective splint must immobilize the joints above and below the fractured bone to prevent bone fragments from moving, tearing nerves, or severing blood vessels."
    },
    {
        "q": "What is the primary first aid measure to arrest severe arterial bleeding from a deep forearm laceration?",
        "options": [
            "Apply direct continuous manual pressure over the wound using a clean sterile pad",
            "Pour hot boiling water over the cut",
            "Wash the cut with strong toilet cleaner",
            "Leave the wound open and encourage continuous bleeding"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Firm direct pressure over the bleeding site with a sterile dressing compresses the ruptured vessels, promoting platelet aggregation and blood clot formation."
    },
    {
        "q": "Which patient transportation technique is most suitable for moving a conscious person with an injured ankle who can bear partial weight on their sound leg?",
        "options": ["Human Crutch method", "Firefighter's carry", "Cradle method", "Backpack carry"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The Human Crutch method involves standing beside the victim on their injured side, supporting their arm over the rescuer's shoulder, acting as a supportive crutch."
    },
    {
        "q": "What position should an unconscious but breathing casualty with no suspected spinal injury be placed in while awaiting medical responders?",
        "options": ["Recovery position (lateral recumbent position)", "Flat on their stomach facing down", "Sitting upright in a straight chair", "Hanging upside down by their feet"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The Recovery position places the victim on their side with the head tilted back, keeping the tongue from obstructing the airway and allowing fluids or vomit to drain freely."
    },
    {
        "q": "What is the recommended chest compression depth when performing adult CPR?",
        "options": ["5 to 6 cm (approx. 2 to 2.4 inches)", "1 to 2 cm", "10 to 15 cm", "Less than 0.5 cm"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Effective CPR requires depressing the adult lower sternum at least 5 cm but no more than 6 cm to adequately compress the heart chambers between the sternum and spine."
    },
    {
        "q": "Which symptom distinguishes life-threatening heatstroke from mild heat exhaustion?",
        "options": [
            "Extremely high core body temperature (>40 deg C), hot dry red skin, and altered mental status or unconsciousness",
            "Profuse sweating with pale cool clammy skin",
            "Normal body temperature with mild thirst",
            "Mild shivering and cold blue fingernails"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Heatstroke is a medical emergency characterized by thermoregulatory failure: body temperature spikes above 40 deg C (104 deg F), sweating ceases (hot dry skin), and neurological impairment ensues."
    },
    {
        "q": "When carrying an injured casualty on an emergency stretcher along a flat corridor, how should the stretcher be oriented?",
        "options": [
            "Feet first, so the front bearer can watch the path and the rear bearer monitors the casualty's face and breathing",
            "Head first at all times",
            "Tilted completely vertically",
            "Turned upside down with the casualty underneath"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Standard stretcher discipline requires carrying the casualty feet first, allowing the rear bearer continuous visual observation of the patient's breathing and consciousness."
    },
    {
        "q": "What is the primary danger of applying ice directly onto bare skin for an extended duration without a cloth barrier?",
        "options": [
            "Ice burn or local tissue frostbite",
            "Instant third-degree heat blistering",
            "Immediate bone calcification",
            "Electric shock"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Direct application of ice to bare skin for prolonged periods damages dermal cells and can cause superficial frostbite ('ice burn'); ice should always be wrapped in a cloth."
    },
    {
        "q": "Which method is best suited for a single rescuer carrying a lightweight child or small adult over a short distance?",
        "options": ["Cradle method", "Two-handed seat", "Four-handed seat", "Stretcher relay"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The cradle method involves the rescuer lifting the victim with one arm behind the back and the other beneath the knees, ideal for children and conscious lightweight individuals."
    },
    {
        "q": "What should a first-aider do if a patient faints (syncope) and collapses to the floor?",
        "options": [
            "Lay the person flat on their back and elevate their legs approximately 30 cm (12 inches) to restore cerebral blood flow",
            "Shake the victim vigorously by their head",
            "Force the victim to immediately stand up and run",
            "Pour hot tea directly into the victim's mouth"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Fainting occurs due to temporary cerebral hypoperfusion. Laying the patient supine and elevating the legs uses gravity to return blood from the extremities to the brain."
    },
    {
        "q": "In the event of an electric shock where the casualty is still in contact with the live electric cable, what is the rescuer's first action?",
        "options": [
            "Switch off the main electric supply or separate the victim using a dry non-conducting wooden stick",
            "Grab the victim's bare hand with wet hands",
            "Pour water over the electric wire",
            "Perform CPR while the current is still flowing"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Ensuring personal safety is paramount. The rescuer must disconnect the power source or use non-conductive insulators (dry wood, rubber) before touching the victim."
    },
    {
        "q": "What should a first-aider NEVER do when treating a victim with a chemical burn caused by an unknown dry powder chemical on their skin?",
        "options": [
            "Immediately apply water before brushing away the dry powder",
            "Brush off the excess dry powder with a clean cloth before flushing with copious water",
            "Remove contaminated clothing carefully",
            "Seek urgent specialized hospital medical care"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Many dry industrial chemicals (like dry lime or sodium) react violently and exothermically with small amounts of water, producing severe thermal and chemical burns. The dry powder must be brushed off first."
    },
    {
        "q": "Which phase of the Disaster Management Cycle includes building cyclone shelters, conducting evacuation drills, and stockpiling medical supplies before a disaster occurs?",
        "options": ["Preparedness", "Recovery", "Rehabilitation", "Post-disaster audit"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Preparedness encompasses pre-disaster planning, early warning systems, evacuation training, and supply stockpiling to ensure effective emergency response."
    },
    {
        "q": "Select ALL components of the RICE protocol for acute ligament sprains:",
        "options": [
            "Rest",
            "Ice",
            "Compression",
            "Running"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "RICE stands for Rest, Ice, Compression, and Elevation. Running exacerbates ligament tearing."
    },
    {
        "q": "Select ALL actions that must be performed when checking the 'A' (Airway) and 'B' (Breathing) of an unconscious casualty:",
        "options": [
            "Perform the head-tilt, chin-lift maneuver to pull the tongue away from the throat",
            "Look for chest rising and falling",
            "Listen near the casualty's mouth for breath sounds and feel for exhaled air on your cheek",
            "Force feed solid biscuits into the victim's mouth"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "The head-tilt chin-lift opens the airway, followed by 'Look, Listen, and Feel' for breathing for up to 10 seconds. Never feed an unconscious patient."
    },
    {
        "q": "Select ALL valid patient transportation methods:",
        "options": [
            "Human Crutch method",
            "Cradle method",
            "Firefighter's carry",
            "Dragging a conscious patient by their hair"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Human crutch, cradle, and firefighter's carry are standard certified evacuation techniques."
    },
    {
        "q": "True or False: In Cardiopulmonary Resuscitation (CPR), chest compressions should be delivered at a rapid tempo of 100 to 120 compressions per minute.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. A compression rate of 100-120 bpm (matching the beat of the song 'Stayin' Alive') maximizes cardiac output during CPR."
    },
    {
        "q": "True or False: When applying an elastic compression bandage to an injured sprained wrist, the bandage should be wrapped so tightly that fingers turn blue and cold.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Bandages must be snug to support the joint and limit swelling, but never so tight that they impede arterial blood circulation or cause cyanosis/numbness."
    },
    {
        "q": "True or False: Burn blisters should be popped immediately to release the sterile serum fluid inside.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Intact blisters provide a natural sterile biological barrier against infection. Puncturing them creates an open wound vulnerable to microbial contamination."
    },
    {
        "q": "True or False: The Heimlich maneuver should only be performed if the victim cannot breathe, talk, or cough forcefully.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "medium",
        "exp": "True. If the victim can cough forcefully or speak, they should be encouraged to cough out the obstruction on their own; abdominal thrusts are reserved for complete airway obstruction."
    },
    {
        "q": "Assertion (A): Cardiopulmonary Resuscitation (CPR) must be initiated immediately upon confirming that a victim is unresponsive and not breathing normally.\\nReason (R): Irreversible biological brain death begins within 4 to 6 minutes of cardiac arrest due to acute oxygen deprivation of cerebral neurons.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Brain neurons cannot survive without oxygen. Immediate chest compressions sustain artificial perfusion to the brain and myocardium until defibrillation or advanced life support arrives."
    },
    {
        "q": "Assertion (A): Cotton wool or fluffy fabrics must never be applied directly onto open weeping burns.\\nReason (R): Loose cotton fibers adhere tenaciously to the burned tissue, causing excruciating pain and tearing freshly healing tissue upon removal.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Only sterile, non-adherent, lint-free dressings or clean plastic cling film should cover burns to prevent fibers from becoming embedded in raw dermis."
    },
    {
        "q": "Assertion (A): Placing an unconscious breathing casualty in the recovery position maintains a patent airway.\\nReason (R): The lateral recumbent posture with a tilted head prevents the relaxed tongue from falling backward into the pharynx and allows vomit to drain away from the trachea.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "In an unconscious person, muscle tone relaxes and the tongue falls into the pharyngeal airway. The recovery position utilizes gravity to keep the airway clear and prevent aspiration."
    },
    {
        "q": "Fill in the blank: The maneuver used to open the airway of an unconscious casualty without suspected spinal injury is the head-tilt, ________-lift maneuver.",
        "options": ["chin", "ear", "shoulder", "nose"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "The head-tilt, chin-lift pulls the tongue forward away from the posterior pharyngeal wall, opening the respiratory conduit."
    },
    {
        "q": "Fill in the blank: In the RICE principle, the letter 'C' stands for ________ using an elastic crepe bandage.",
        "options": ["Compression", "Circulation", "Cooling", "Cleaning"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "'C' represents Compression, which stabilizes the damaged joint and mechanically restricts inflammatory fluid swelling."
    },
    {
        "q": "Fill in the blank: The emergency abdominal thrust maneuver used to dislodge a foreign object from the windpipe of a choking victim is named the ________ maneuver.",
        "options": ["Heimlich", "Koch", "Pasteur", "Fleming"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Dr. Henry Heimlich invented the Heimlich maneuver in 1974 for choking emergencies."
    },
    {
        "q": "Fill in the blank: When carrying an injured patient up a flight of stairs or into an ambulance on a stretcher, the casualty should be carried ________ first.",
        "options": ["head", "feet", "sideways", "knees"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "hard",
        "exp": "While stretcher transport is normally feet-first on flat ground, casualties are transported head-first when moving uphill or ascending stairs to keep the head elevated."
    },
    {
        "q": "Fill in the blank: A temporary loss of consciousness caused by an abrupt decrease in blood supply to the brain is medically termed ________.",
        "options": ["syncope", "sprain", "tetanus", "contusion"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "Syncope is the precise medical term for fainting or temporary loss of consciousness due to transient cerebral ischemia."
    },
    {
        "q": "In a continuous CPR cycle, how many total chest compressions will a rescuer deliver across 5 complete consecutive cycles of 30:2?",
        "options": ["150", "100", "200", "300"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Total compressions = 5 cycles * 30 compressions/cycle = 150 compressions."
    },
    {
        "q": "When applying ice to an acute ligament sprain under the RICE protocol, an ice pack should be applied for how many minutes at a time?",
        "options": ["15", "60", "120", "2"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Ice should be applied for 15 to 20 minutes every 2-3 hours; longer continuous exposure risks skin frostbite and reflex vasodilation."
    },
    {
        "q": "According to the American Heart Association (AHA) and Resuscitation Council standards, what is the target minimum chest compression rate in compressions per minute during CPR?",
        "options": ["100", "60", "40", "160"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "CPR guidelines require delivering compressions at a tempo of 100 to 120 compressions per minute."
    },
    {
        "q": "If a first-aider cools a burn under gentle running tap water for exactly 12 minutes, how many seconds of cooling has the burn received?",
        "options": ["720", "600", "500", "840"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Time in seconds = 12 minutes * 60 seconds/minute = 720 seconds."
    },
    {
        "q": "How many total core components make up the comprehensive RICE first aid protocol for musculoskeletal sprains?",
        "options": ["4", "3", "5", "7"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "The RICE protocol consists of exactly 4 components: Rest, Ice, Compression, and Elevation."
    }
]

practice_data = [
    {
        "q": "What is the very first action a rescuer must take before approaching an injured victim at an accident scene?",
        "options": [
            "Check for scene safety (ensure there is no fire, falling debris, live wire, or oncoming traffic)",
            "Run immediately to touch the victim without looking around",
            "Start chest compressions on anyone nearby",
            "Take photographs for social media"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Scene safety is the foremost priority in any emergency response to ensure the rescuer does not become another casualty."
    },
    {
        "q": "What does a first-aider look for when checking the 'C' (Circulation) in an unconscious non-breathing casualty?",
        "options": [
            "Presence of a central pulse (carotid pulse in the neck) and signs of normal circulation",
            "Hair color and facial shape",
            "Number of teeth in the mouth",
            "Thickness of the victim's wallet"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Checking circulation involves palpating the carotid artery in the groove beside the trachea for up to 10 seconds to detect cardiac output."
    },
    {
        "q": "Which patient carry method involves two rescuers interlocking their hands and wrists to form a sturdy four-handed seat for a conscious casualty?",
        "options": ["Four-hand seat method", "Firefighter's drag", "Cradle carry", "Blanket drag"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "In the four-hand seat, two rescuers each grasp their own left wrist with their right hand, and then grasp the other rescuer's right wrist, creating a rigid supportive square chair."
    },
    {
        "q": "How should an open bleeding nose (epistaxis) be managed as immediate first aid?",
        "options": [
            "Pinch the soft lower part of the nose firmly and lean slightly forward for 10 minutes",
            "Tilt the head far backward and swallow the blood",
            "Blow the nose forcefully into a cloth",
            "Plug the nose with burning paper"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Pinching the nasal alae while leaning forward exerts direct pressure on Kiesselbach's plexus while preventing blood from trickling down the throat into the stomach/airway."
    },
    {
        "q": "Why is it dangerous to tilt a bleeding nose victim's head backward?",
        "options": [
            "Blood flows down the pharynx into the stomach causing nausea/vomiting, or enters the trachea causing airway compromise",
            "It turns the blood into bone instantly",
            "It causes immediate permanent blindness",
            "It increases regional room temperature"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Tilting the head back causes blood to pool in the throat, triggering coughing, gagging, vomiting, and potential aspiration into the lungs."
    },
    {
        "q": "What type of dressing should be applied to an open chest wound ('sucking chest wound') to prevent tension pneumothorax?",
        "options": [
            "A three-sided occlusive dressing acting as a flutter valve",
            "A completely permeable coarse fishnet",
            "A heavy plaster cast wrapping the entire body",
            "Direct application of dry sand"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Taping a plastic dressing on three sides allows air to escape the pleural space during exhalation while sealing shut during inhalation, preventing tension pneumothorax."
    },
    {
        "q": "What is the primary indicator that an elastic compression bandage on a sprained ankle is too tight?",
        "options": [
            "The victim's toes become cold, pale or bluish (cyanotic), numb, and tingle",
            "The bandage feels warm and comfortable",
            "The victim can wiggle their toes easily",
            "The swelling resolves completely in 5 seconds"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Numbness, tingling, pallor, coldness, or delayed capillary refill in distal toes indicate impaired arterial perfusion, requiring immediate bandage loosening."
    },
    {
        "q": "When managing a heat exhaustion patient, what is the best first aid action?",
        "options": [
            "Move victim to a cool shaded spot, loosen tight clothing, fan them, and give cool water or ORS sips",
            "Wrap the victim in three heavy wool blankets",
            "Force the victim to drink boiling black coffee",
            "Ask the victim to run a 5-kilometer marathon"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Shade, passive cooling, fanning, and oral rehydration with electrolytes reverse hypovolemia and mild hyperthermia in heat exhaustion."
    },
    {
        "q": "What should be done if a casualty has an object (like a piece of glass or iron nail) impaled deeply into their thigh?",
        "options": [
            "Do NOT remove the impaled object; stabilize it in place using bulky rolled dressings and seek emergency surgery",
            "Yank the object out forcefully immediately",
            "Push the object deeper into the bone",
            "Twist the object in a circular motion"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The embedded object acts as a tamponade plugging severed blood vessels. Pulling it out causes uncontrollable hemorrhage; it must be stabilized in place."
    },
    {
        "q": "Which patient transport method is most appropriate for dragging an unconscious victim through a narrow, smoke-filled corridor in a building fire?",
        "options": ["Firefighter's crawl / blanket drag", "Four-handed seat", "Stretcher on shoulders", "Human crutch"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "In smoke-filled spaces, cooler air and visibility exist near the floor; dragging the casualty along the ground keeps both rescuer and victim beneath the toxic smoke."
    },
    {
        "q": "What is the primary sign that CPR chest compressions are being performed effectively on an adult?",
        "options": [
            "A carotid pulse is palpable in sync with each compression and the chest visibly recoils completely between compressions",
            "The victim's ribcage cracks loudly on every single touch",
            "The rescuer stops to rest every 10 seconds",
            "The casualty's eyes turn bright neon green"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Effective CPR produces a palpable carotid pulsation during compressions, and full chest recoil allows the heart ventricles to refill with blood."
    },
    {
        "q": "When a victim suffers an acute sprain, for how long should the RICE treatment protocol be continued following the injury?",
        "options": ["First 48 to 72 hours (2 to 3 days)", "Only the first 60 seconds", "Continuously for 6 months without stopping", "Never longer than 5 minutes"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The inflammatory acute response (bleeding, edema) peaks during the initial 48-72 hours, making RICE most effective during this window."
    },
    {
        "q": "What is a major symptom of internal bleeding in an accident victim whose abdomen was struck by a vehicle?",
        "options": [
            "Abdominal rigidity, cold clammy pale skin, rapid weak pulse, and dizziness",
            "Bright yellow hair",
            "Violent uncontrollable laughing",
            "Immediate increase in appetite"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Internal hemorrhage causes signs of hypovolemic shock: rapid thready pulse, cold sweaty skin, drop in blood pressure, and a tense, tender abdomen."
    },
    {
        "q": "In the event of an earthquake, what is the internationally practiced protective drill for individuals trapped inside a building?",
        "options": [
            "Drop, Cover, and Hold On (under a sturdy desk or table)",
            "Run into a crowded glass elevator immediately",
            "Jump out of a top floor window",
            "Stand directly beneath heavy glass chandeliers"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "'Drop, Cover, and Hold On' protects against the primary cause of earthquake injury: falling ceilings, plaster, and shattered furniture."
    },
    {
        "q": "What should a first-aider do if a seizure (epileptic fit) occurs in a person in a classroom?",
        "options": [
            "Clear away hard/sharp furniture nearby, cushion their head with a folded jacket, and never force objects into their mouth",
            "Force a metal spoon or wooden stick between their teeth",
            "Restrain their arms and legs forcibly with ropes",
            "Pour water into their mouth while shaking"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Protect the head and remove dangerous objects. Forcing items into the mouth causes broken teeth and airway obstruction; seizures terminate naturally in 1-3 minutes."
    },
    {
        "q": "Select ALL actions that constitute proper immediate burn care:",
        "options": [
            "Cooling under cold running tap water for 10-15 minutes",
            "Covering loosely with a clean, sterile non-stick dressing or clean plastic wrap",
            "Removing constricting rings, bracelets, and watches before edema develops",
            "Applying ice directly until the skin freezes solid"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Cooling with water, removing tight jewelry before swelling, and covering with sterile non-stick wrap are correct. Applying ice directly causes frostbite."
    },
    {
        "q": "Select ALL reasons why full chest recoil is critical during CPR chest compressions:",
        "options": [
            "Allows the heart chambers to refill with venous blood before the next compression",
            "Generates negative thoracic pressure drawing blood back to the heart",
            "Maximizes myocardial and cerebral perfusion pressure",
            "Allows the rescuer to take a 10-minute nap"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "medium",
        "exp": "Complete recoil allows negative intrathoracic pressure to pull blood into the ventricles; leaning on the chest prevents cardiac refill and reduces CPR efficacy."
    },
    {
        "q": "Select ALL items that can serve as improvised emergency splints in a disaster field setting:",
        "options": [
            "Sturdy wooden sticks or tree branches",
            "Thick folded newspapers or magazines",
            "An uninjured adjacent leg (anatomical splinting)",
            "Wet tissue paper"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Rigid boards, rolled newspapers, or even the patient's own uninjured leg can provide effective splinting stability in emergencies."
    },
    {
        "q": "True or False: A tourniquet should be applied loosely and adjusted up and down the limb every 5 minutes.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. A tourniquet is a life-saving tool for catastrophic limb bleeding; it must be applied tightly enough to halt arterial flow completely and left in place until surgery."
    },
    {
        "q": "True or False: In the Heimlich maneuver, abdominal thrusts are directed inward and upward toward the victim's diaphragm.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Inward and upward thrusts displace the diaphragm upward, generating an artificial cough to expel the foreign object from the windpipe."
    },
    {
        "q": "True or False: If a patient suffering from heatstroke is conscious, they should be given ice-cold water to gulp down rapidly in large quantities.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "medium",
        "exp": "False. Gulping cold water can induce stomach cramps, vomiting, and aspiration. Small, frequent sips of cool water or electrolyte solution are indicated."
    },
    {
        "q": "True or False: An improvised stretcher can be assembled using two sturdy wooden poles threaded through the sleeves of two inverted, buttoned jackets.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Threading long poles through buttoned heavy coats or jackets creates a reliable, field-tested emergency canvas stretcher."
    },
    {
        "q": "Assertion (A): Direct pressure is superior to an impromptu tourniquet for ordinary bleeding wounds.\\nReason (R): Tourniquets completely occlude all arterial blood flow to the distal limb, risking irreversible tissue necrosis and nerve palsy if left on unnecessarily.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Direct pressure halts over 90% of bleeds without compromising distal limb perfusion. Tourniquets are strictly reserved for catastrophic life-threatening hemorrhage."
    },
    {
        "q": "Assertion (A): During CPR, interruptions in chest compressions must be minimized to less than 10 seconds.\\nReason (R): Coronary and cerebral perfusion pressure drops to zero almost instantly when compressions stop and takes several compressions to rebuild.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Maintaining continuous blood flow is vital. Each pause destroys the vascular pressure gradient required to keep brain cells alive."
    },
    {
        "q": "Fill in the blank: The universal emergency contact phone number in India that integrates Police, Fire, and Ambulance services is ________.",
        "options": ["112", "100", "108", "911"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "112 is India's unified Emergency Response Support System (ERSS) national emergency telephone number."
    },
    {
        "q": "Fill in the blank: In first aid terminology, a violent twisting injury that damages or tears ligaments connecting bones at a joint is called a ________.",
        "options": ["sprain", "strain", "fracture", "dislocation"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "A sprain is a stretch or tear of ligament tissue connecting bones; a strain involves muscles or tendons."
    },
    {
        "q": "Fill in the blank: The device that analyzes heart rhythms and delivers an electric shock to restart the heart in ventricular fibrillation during sudden cardiac arrest is an ________.",
        "options": ["AED (Automated External Defibrillator)", "ECG monitor", "EEG cap", "oxygen cylinder"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "An Automated External Defibrillator (AED) provides automated rhythm analysis and defibrillating shocks to restore normal sinus rhythm."
    },
    {
        "q": "Fill in the blank: When performing two-rescuer transport using a chair, the method where rescuers carry an injured person seated on an ordinary household wooden chair is the ________ method.",
        "options": ["chair carry", "cradle carry", "piggyback", "firefighter carry"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "The chair carry allows two rescuers to safely carry a conscious patient up or down narrow stairs."
    },
    {
        "q": "If a rescuer maintains an exact rate of 110 chest compressions per minute for 3 continuous minutes, how many compressions did they deliver?",
        "options": ["330", "220", "300", "440"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Total compressions = 110 * 3 = 330 compressions."
    },
    {
        "q": "How many rescue breaths are delivered after every set of 30 chest compressions in standard single-rescuer adult CPR?",
        "options": ["2", "5", "1", "10"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Standard CPR calls for exactly 2 rescue breaths after every 30 chest compressions."
    }
]

svg_diagrams = [
    # SVG 1: ABC of First Aid
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Emergency Life Support: The ABC of First Aid</text>
  <!-- A: Airway -->
  <g transform="translate(30, 45)">
    <rect x="0" y="0" width="130" height="155" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="30" fill="#38bdf8" font-size="16" font-weight="bold" text-anchor="middle">A: AIRWAY</text>
    <text x="12" y="60" fill="#f8fafc" font-size="10">&#8226; Open the airway</text>
    <text x="12" y="80" fill="#f8fafc" font-size="10">&#8226; Head-tilt chin-lift</text>
    <text x="12" y="100" fill="#f8fafc" font-size="10">&#8226; Clear obstructions</text>
    <text x="12" y="120" fill="#f8fafc" font-size="10">&#8226; Prevent tongue block</text>
    <rect x="10" y="130" width="110" height="18" rx="4" fill="#0369a1"/>
    <text x="65" y="143" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Clear Conduit</text>
  </g>
  <!-- B: Breathing -->
  <g transform="translate(185, 45)">
    <rect x="0" y="0" width="130" height="155" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="65" y="30" fill="#10b981" font-size="16" font-weight="bold" text-anchor="middle">B: BREATHING</text>
    <text x="12" y="60" fill="#f8fafc" font-size="10">&#8226; Check 5-10 sec</text>
    <text x="12" y="80" fill="#f8fafc" font-size="10">&#8226; LOOK for chest rise</text>
    <text x="12" y="100" fill="#f8fafc" font-size="10">&#8226; LISTEN for sounds</text>
    <text x="12" y="120" fill="#f8fafc" font-size="10">&#8226; FEEL exhaled air</text>
    <rect x="10" y="130" width="110" height="18" rx="4" fill="#15803d"/>
    <text x="65" y="143" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Ventilation</text>
  </g>
  <!-- C: Circulation -->
  <g transform="translate(340, 45)">
    <rect x="0" y="0" width="130" height="155" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="65" y="30" fill="#ef4444" font-size="16" font-weight="bold" text-anchor="middle">C: CIRCULATION</text>
    <text x="12" y="60" fill="#f8fafc" font-size="10">&#8226; Check carotid pulse</text>
    <text x="12" y="80" fill="#f8fafc" font-size="10">&#8226; If absent: CPR</text>
    <text x="12" y="100" fill="#f8fafc" font-size="10">&#8226; 30 Compressions</text>
    <text x="12" y="120" fill="#f8fafc" font-size="10">&#8226; 2 Rescue breaths</text>
    <rect x="10" y="130" width="110" height="18" rx="4" fill="#991b1b"/>
    <text x="65" y="143" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Perfusion</text>
  </g>
</svg>''',

    # SVG 2: RICE Principle Quadrant
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">The RICE Principle for Soft-Tissue Injuries (Sprains)</text>
  <!-- 4 Quadrants -->
  <g transform="translate(30, 42)">
    <!-- R: Rest -->
    <rect x="0" y="0" width="210" height="75" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="15" y="25" fill="#38bdf8" font-size="13" font-weight="bold">R - REST</text>
    <text x="15" y="45" fill="#f8fafc" font-size="10">&#8226; Stop activity immediately</text>
    <text x="15" y="62" fill="#94a3b8" font-size="9">&#8226; Immobilize joint to protect torn ligaments</text>
    <!-- I: Ice -->
    <rect x="230" y="0" width="210" height="75" rx="6" fill="#1e293b" stroke="#0284c7"/>
    <text x="245" y="25" fill="#38bdf8" font-size="13" font-weight="bold">I - ICE</text>
    <text x="245" y="45" fill="#f8fafc" font-size="10">&#8226; Cold pack for 15-20 min every 2-3 hrs</text>
    <text x="245" y="62" fill="#94a3b8" font-size="9">&#8226; Vasoconstriction reduces swelling &amp; pain</text>
    <!-- C: Compression -->
    <rect x="0" y="85" width="210" height="75" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="15" y="110" fill="#fbbf24" font-size="13" font-weight="bold">C - COMPRESSION</text>
    <text x="15" y="130" fill="#f8fafc" font-size="10">&#8226; Wrap snug elastic crepe bandage</text>
    <text x="15" y="147" fill="#94a3b8" font-size="9">&#8226; Limits edema (check for distal circulation)</text>
    <!-- E: Elevation -->
    <rect x="230" y="85" width="210" height="75" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="245" y="110" fill="#34d399" font-size="13" font-weight="bold">E - ELEVATION</text>
    <text x="245" y="130" fill="#f8fafc" font-size="10">&#8226; Prop limb above level of the heart</text>
    <text x="245" y="147" fill="#94a3b8" font-size="9">&#8226; Gravity promotes venous fluid return</text>
  </g>
</svg>''',

    # SVG 3: CPR Hand Placement & Depth
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Cardiopulmonary Resuscitation (CPR): Chest Compression Mechanics</text>
  <!-- Chest Profile -->
  <g transform="translate(60, 50)">
    <!-- Sternum outline -->
    <rect x="40" y="30" width="140" height="100" rx="20" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
    <line x1="110" y1="40" x2="110" y2="120" stroke="#f43f5e" stroke-width="4"/>
    <circle cx="110" cy="95" r="14" fill="#ef4444"/>
    <text x="110" y="100" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Hands</text>
    <!-- Labels on left -->
    <text x="110" y="150" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">Center of Chest</text>
    <text x="110" y="165" fill="#94a3b8" font-size="9" text-anchor="middle">Lower half of sternum</text>
  </g>
  <!-- Compression Specs Panel -->
  <g transform="translate(260, 50)">
    <rect x="0" y="0" width="200" height="150" rx="8" fill="#1e293b" stroke="#38bdf8"/>
    <text x="100" y="25" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">CPR Protocol Standards</text>
    <text x="15" y="55" fill="#f8fafc" font-size="10">&#8226; Rate: 100 to 120 / min</text>
    <text x="15" y="78" fill="#f8fafc" font-size="10">&#8226; Depth: 5 to 6 cm (Adult)</text>
    <text x="15" y="101" fill="#f8fafc" font-size="10">&#8226; Ratio: 30 Compressions : 2 Breaths</text>
    <text x="15" y="124" fill="#f8fafc" font-size="10">&#8226; Allow full chest recoil</text>
    <rect x="15" y="132" width="170" height="14" rx="3" fill="#0369a1"/>
    <text x="100" y="143" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Minimal Interruptions (&lt; 10s)</text>
  </g>
</svg>''',

    # SVG 4: Heimlich Maneuver
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Heimlich Maneuver for Choking (Complete Airway Obstruction)</text>
  <!-- Victim & Rescuer schematic -->
  <g transform="translate(60, 50)">
    <circle cx="80" cy="30" r="16" fill="#334155" stroke="#94a3b8"/>
    <!-- Torso -->
    <rect x="60" y="48" width="40" height="75" rx="8" fill="#1e293b" stroke="#38bdf8"/>
    <!-- Hands positioned above navel below xiphoid -->
    <circle cx="80" cy="85" r="10" fill="#ef4444"/>
    <!-- Inward and upward arrows -->
    <path d="M 100 85 L 125 70" stroke="#f59e0b" stroke-width="3" marker-end="url(#arr)"/>
    <text x="135" y="73" fill="#fbbf24" font-size="10" font-weight="bold">Inward &amp; Upward</text>
    <!-- Trachea arrow pointing out object -->
    <path d="M 80 30 L 80 15 L 45 15" stroke="#10b981" stroke-width="2"/>
    <circle cx="40" cy="15" r="4" fill="#ef4444"/>
    <text x="35" y="8" fill="#10b981" font-size="9">Obstruction Expelled</text>
  </g>
  <!-- Action checklist -->
  <g transform="translate(260, 50)">
    <rect x="0" y="0" width="200" height="150" rx="8" fill="#1e293b" stroke="#f59e0b"/>
    <text x="100" y="25" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Execution Steps</text>
    <text x="12" y="55" fill="#f8fafc" font-size="10">1. Stand behind victim</text>
    <text x="12" y="75" fill="#f8fafc" font-size="10">2. Wrap arms around waist</text>
    <text x="12" y="95" fill="#f8fafc" font-size="10">3. Place fist above navel</text>
    <text x="12" y="115" fill="#f8fafc" font-size="10">4. Quick, upward thrusts</text>
    <text x="12" y="135" fill="#38bdf8" font-size="9">Forces diaphragm up &#8594; Air blast</text>
  </g>
</svg>''',

    # SVG 5: Burn Degree Classification & First Aid
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Burn Classification &amp; Emergency First Aid Rules</text>
  <!-- 3 Burn Degrees -->
  <g transform="translate(25, 45)">
    <!-- 1st Degree -->
    <rect x="0" y="0" width="140" height="110" rx="6" fill="#1e293b" stroke="#eab308"/>
    <text x="70" y="24" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">1st Degree (Superficial)</text>
    <text x="10" y="50" fill="#f8fafc" font-size="9">&#8226; Epidermis only</text>
    <text x="10" y="70" fill="#f8fafc" font-size="9">&#8226; Redness, mild pain</text>
    <text x="10" y="90" fill="#f8fafc" font-size="9">&#8226; No blisters</text>
    <!-- 2nd Degree -->
    <rect x="155" y="0" width="140" height="110" rx="6" fill="#1e293b" stroke="#f97316"/>
    <text x="225" y="24" fill="#fdba74" font-size="11" font-weight="bold" text-anchor="middle">2nd Degree (Partial)</text>
    <text x="165" y="50" fill="#f8fafc" font-size="9">&#8226; Epidermis + Dermis</text>
    <text x="165" y="70" fill="#f8fafc" font-size="9">&#8226; Fluid blisters, severe pain</text>
    <text x="165" y="90" fill="#f8fafc" font-size="9">&#8226; DO NOT puncture blisters!</text>
    <!-- 3rd Degree -->
    <rect x="310" y="0" width="140" height="110" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="380" y="24" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">3rd Degree (Full)</text>
    <text x="320" y="50" fill="#f8fafc" font-size="9">&#8226; All skin layers + fat</text>
    <text x="320" y="70" fill="#f8fafc" font-size="9">&#8226; Charred, white, leathery</text>
    <text x="320" y="90" fill="#f8fafc" font-size="9">&#8226; Nerves destroyed (no pain)</text>
  </g>
  <!-- First Aid Banner -->
  <rect x="25" y="165" width="450" height="50" rx="6" fill="#15803d"/>
  <text x="250" y="186" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">FIRST AID: Cool with running tap water for 10-15 minutes immediately!</text>
  <text x="250" y="204" fill="#dcfce7" font-size="10" text-anchor="middle">Cover loosely with sterile plastic wrap / clean cloth. Never apply ice, butter, or oil.</text>
</svg>''',

    # SVG 6: Patient Transportation Methods
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Casualty Transportation Methods in First Aid</text>
  <!-- 4 Methods Cards -->
  <g transform="translate(25, 45)">
    <!-- Cradle Method -->
    <rect x="0" y="0" width="105" height="160" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="52" y="25" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Cradle Carry</text>
    <text x="8" y="55" fill="#f8fafc" font-size="9">&#8226; Single rescuer</text>
    <text x="8" y="75" fill="#f8fafc" font-size="9">&#8226; Children or</text>
    <text x="8" y="90" fill="#f8fafc" font-size="9">lightweight conscious</text>
    <text x="8" y="105" fill="#f8fafc" font-size="9">persons</text>
    <text x="52" y="145" fill="#7dd3fc" font-size="8" text-anchor="middle">Arm under knees</text>
    <!-- Human Crutch -->
    <rect x="115" y="0" width="105" height="160" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="167" y="25" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Human Crutch</text>
    <text x="123" y="55" fill="#f8fafc" font-size="9">&#8226; Leg/ankle injury</text>
    <text x="123" y="75" fill="#f8fafc" font-size="9">&#8226; Conscious victim</text>
    <text x="123" y="90" fill="#f8fafc" font-size="9">&#8226; Rescuer supports</text>
    <text x="123" y="105" fill="#f8fafc" font-size="9">on injured side</text>
    <text x="167" y="145" fill="#86efac" font-size="8" text-anchor="middle">Arm over shoulder</text>
    <!-- Four-Hand Seat -->
    <rect x="230" y="0" width="105" height="160" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="282" y="25" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">4-Hand Seat</text>
    <text x="238" y="55" fill="#f8fafc" font-size="9">&#8226; Two rescuers</text>
    <text x="238" y="75" fill="#f8fafc" font-size="9">&#8226; Interlocked wrists</text>
    <text x="238" y="90" fill="#f8fafc" font-size="9">&#8226; For conscious victim</text>
    <text x="238" y="105" fill="#f8fafc" font-size="9">unable to walk</text>
    <text x="282" y="145" fill="#fde68a" font-size="8" text-anchor="middle">Rigid hand chair</text>
    <!-- Stretcher -->
    <rect x="345" y="0" width="105" height="160" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="397" y="25" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Stretcher</text>
    <text x="353" y="55" fill="#f8fafc" font-size="9">&#8226; Severe fractures</text>
    <text x="353" y="75" fill="#f8fafc" font-size="9">&#8226; Unconscious</text>
    <text x="353" y="90" fill="#f8fafc" font-size="9">&#8226; Spine injuries</text>
    <text x="353" y="105" fill="#f8fafc" font-size="9">&#8226; Carry feet first</text>
    <text x="397" y="145" fill="#fca5a5" font-size="8" text-anchor="middle">Poles + Blanket</text>
  </g>
</svg>''',

    # SVG 7: Fracture Splinting
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Emergency Splinting of Fractured Limb</text>
  <!-- Limb with fracture -->
  <g transform="translate(60, 60)">
    <!-- Lower leg outline -->
    <rect x="30" y="30" width="220" height="30" rx="15" fill="#334155"/>
    <!-- Fracture break jagged line -->
    <line x1="140" y1="30" x2="145" y2="45" stroke="#ef4444" stroke-width="3"/>
    <line x1="145" y1="45" x2="138" y2="60" stroke="#ef4444" stroke-width="3"/>
    <text x="140" y="20" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">Fracture Site</text>
    <!-- Rigid Wooden Splint underneath -->
    <rect x="10" y="65" width="260" height="15" rx="3" fill="#b45309"/>
    <text x="140" y="95" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">Rigid Splint (Plank / Folded Newspaper)</text>
    <!-- Triangular bandage ties (Above & Below fracture) -->
    <line x1="60" y1="20" x2="60" y2="85" stroke="#38bdf8" stroke-width="4"/>
    <line x1="100" y1="20" x2="100" y2="85" stroke="#38bdf8" stroke-width="4"/>
    <line x1="180" y1="20" x2="180" y2="85" stroke="#38bdf8" stroke-width="4"/>
    <line x1="220" y1="20" x2="220" y2="85" stroke="#38bdf8" stroke-width="4"/>
  </g>
  <!-- Rules banner -->
  <rect x="40" y="165" width="420" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
  <text x="250" y="185" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">GOLDEN RULE OF SPLINTING</text>
  <text x="250" y="203" fill="#f8fafc" font-size="10" text-anchor="middle">Immobilize the joint above (knee) and the joint below (ankle). Do not attempt to reset bones!</text>
</svg>''',

    # SVG 8: Bleeding Control Sequence
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Protocol for Controlling External Hemorrhage</text>
  <!-- Step 1: Direct Pressure -->
  <g transform="translate(30, 50)">
    <rect x="0" y="0" width="125" height="135" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="62" y="25" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">1. Direct Pressure</text>
    <text x="10" y="55" fill="#f8fafc" font-size="9">&#8226; Sterile pad directly</text>
    <text x="10" y="70" fill="#f8fafc" font-size="9">over bleeding cut</text>
    <text x="10" y="90" fill="#f8fafc" font-size="9">&#8226; Firm palm pressure</text>
    <text x="10" y="110" fill="#f8fafc" font-size="9">&#8226; Halts 90% bleeds</text>
  </g>
  <!-- Arrow -->
  <path d="M 160 115 L 180 115" stroke="#f8fafc" stroke-width="2"/>
  <!-- Step 2: Elevation -->
  <g transform="translate(185, 50)">
    <rect x="0" y="0" width="125" height="135" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="62" y="25" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">2. Elevation</text>
    <text x="10" y="55" fill="#f8fafc" font-size="9">&#8226; Elevate limb</text>
    <text x="10" y="70" fill="#f8fafc" font-size="9">above heart level</text>
    <text x="10" y="90" fill="#f8fafc" font-size="9">&#8226; Lowers arterial</text>
    <text x="10" y="105" fill="#f8fafc" font-size="9">pressure head</text>
  </g>
  <!-- Arrow -->
  <path d="M 315 115 L 335 115" stroke="#f8fafc" stroke-width="2"/>
  <!-- Step 3: Pressure Bandage / Tourniquet -->
  <g transform="translate(340, 50)">
    <rect x="0" y="0" width="130" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="65" y="25" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">3. Pressure Bandage</text>
    <text x="10" y="55" fill="#f8fafc" font-size="9">&#8226; Tie bandage firmly</text>
    <text x="10" y="75" fill="#f8fafc" font-size="9">&#8226; If arterial jetting</text>
    <text x="10" y="90" fill="#f8fafc" font-size="9">persists: Tourniquet</text>
    <text x="10" y="110" fill="#f8fafc" font-size="9">5 cm above wound</text>
  </g>
  <text x="250" y="210" fill="#94a3b8" font-size="10" text-anchor="middle">If dressing soaks through, add more pads on top. NEVER remove the initial clotted pad!</text>
</svg>''',

    # SVG 9: Recovery Position
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">The Recovery Position (Lateral Recumbent Posture)</text>
  <!-- Casualty lying on side schematic -->
  <g transform="translate(70, 50)">
    <!-- Head tilted back with hand under cheek -->
    <circle cx="60" cy="50" r="18" fill="#334155" stroke="#94a3b8"/>
    <!-- Body profile on side -->
    <rect x="80" y="40" width="120" height="40" rx="15" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <!-- Bent knee supporting body -->
    <path d="M 180 60 L 220 90 L 240 75" fill="none" stroke="#10b981" stroke-width="8"/>
    <text x="220" y="115" fill="#86efac" font-size="9" text-anchor="middle">Bent leg prevents rolling forward</text>
    <!-- Fluid drain arrow from mouth -->
    <path d="M 50 55 L 30 70" stroke="#38bdf8" stroke-width="2" marker-end="url(#arr)"/>
    <text x="25" y="85" fill="#38bdf8" font-size="9">Vomit / saliva drains safely</text>
  </g>
  <!-- Rationale Box -->
  <rect x="40" y="160" width="420" height="55" rx="6" fill="#1e293b" stroke="#334155"/>
  <text x="250" y="180" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">For Unconscious, Breathing Casualties (No Spine Trauma)</text>
  <text x="250" y="200" fill="#f8fafc" font-size="10" text-anchor="middle">Head tilted back keeps airway open; prevents choking and tongue obstruction.</text>
</svg>''',

    # SVG 10: Heatstroke vs Heat Exhaustion
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Heat Exhaustion vs Life-Threatening Heatstroke</text>
  <!-- Heat Exhaustion Panel -->
  <g transform="translate(30, 45)">
    <rect x="0" y="0" width="205" height="165" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="102" y="25" fill="#fde68a" font-size="13" font-weight="bold" text-anchor="middle">HEAT EXHAUSTION</text>
    <text x="15" y="55" fill="#f8fafc" font-size="10">&#8226; Profuse heavy sweating</text>
    <text x="15" y="75" fill="#f8fafc" font-size="10">&#8226; Pale, cool, clammy skin</text>
    <text x="15" y="95" fill="#f8fafc" font-size="10">&#8226; Dizziness, weakness, nausea</text>
    <text x="15" y="115" fill="#f8fafc" font-size="10">&#8226; Body temp &lt; 40 &#176;C</text>
    <rect x="15" y="130" width="175" height="22" rx="4" fill="#78350f"/>
    <text x="102" y="145" fill="#fde68a" font-size="9" font-weight="bold" text-anchor="middle">Action: Shade, rest, cool fluids</text>
  </g>
  <!-- Heatstroke Panel -->
  <g transform="translate(265, 45)">
    <rect x="0" y="0" width="205" height="165" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="102" y="25" fill="#fca5a5" font-size="13" font-weight="bold" text-anchor="middle">HEATSTROKE (CRITICAL)</text>
    <text x="15" y="55" fill="#f8fafc" font-size="10">&#8226; No sweating (Dry, hot, red skin)</text>
    <text x="15" y="75" fill="#f8fafc" font-size="10">&#8226; High body temp &gt; 40 &#176;C</text>
    <text x="15" y="95" fill="#f8fafc" font-size="10">&#8226; Confusion, delirium, seizures</text>
    <text x="15" y="115" fill="#f8fafc" font-size="10">&#8226; May collapse unconscious</text>
    <rect x="15" y="130" width="175" height="22" rx="4" fill="#991b1b"/>
    <text x="102" y="145" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Action: Rapid ice water cooling / 112</text>
  </g>
</svg>''',

    # SVG 11: Improvised Stretcher
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Assembling an Improvised Stretcher (Field Disaster First Aid)</text>
  <!-- Two long poles -->
  <g transform="translate(50, 50)">
    <rect x="0" y="20" width="400" height="12" rx="4" fill="#b45309"/>
    <rect x="0" y="110" width="400" height="12" rx="4" fill="#b45309"/>
    <!-- Buttoned Jackets / Blanket canvas -->
    <rect x="80" y="32" width="240" height="78" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="200" y="65" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Heavy Blanket or Buttoned Jackets</text>
    <text x="200" y="85" fill="#f8fafc" font-size="9" text-anchor="middle">Sleeves turned inside-out with poles threaded through</text>
    <!-- Bearer handles -->
    <text x="40" y="75" fill="#94a3b8" font-size="9" text-anchor="middle">Bearer 1</text>
    <text x="360" y="75" fill="#94a3b8" font-size="9" text-anchor="middle">Bearer 2</text>
  </g>
  <!-- Test note -->
  <text x="250" y="195" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Safety Rule: Always test stretcher strength with a healthy person before lifting casualty.</text>
</svg>''',

    # SVG 12: Disaster Management Cycle
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">The Comprehensive Disaster Management Cycle</text>
  <!-- Central Circle -->
  <circle cx="250" cy="130" r="30" fill="#334155" stroke="#94a3b8"/>
  <text x="250" y="134" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">DISASTER</text>
  <!-- Pre-Disaster (Top/Left) -->
  <!-- 1. Mitigation -->
  <rect x="40" y="55" width="130" height="50" rx="6" fill="#14532d" stroke="#22c55e"/>
  <text x="105" y="75" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">1. MITIGATION</text>
  <text x="105" y="92" fill="#dcfce7" font-size="8" text-anchor="middle">Risk reduction &amp; bylaws</text>
  <!-- 2. Preparedness -->
  <rect x="330" y="55" width="130" height="50" rx="6" fill="#0369a1" stroke="#38bdf8"/>
  <text x="395" y="75" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">2. PREPAREDNESS</text>
  <text x="395" y="92" fill="#e0f2fe" font-size="8" text-anchor="middle">Mock drills, early warnings</text>
  <!-- Post-Disaster (Bottom/Right) -->
  <!-- 3. Response -->
  <rect x="330" y="155" width="130" height="50" rx="6" fill="#991b1b" stroke="#ef4444"/>
  <text x="395" y="175" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">3. RESPONSE</text>
  <text x="395" y="192" fill="#fee2e2" font-size="8" text-anchor="middle">Search, rescue &amp; First Aid</text>
  <!-- 4. Recovery -->
  <rect x="40" y="155" width="130" height="50" rx="6" fill="#78350f" stroke="#f59e0b"/>
  <text x="105" y="175" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">4. RECOVERY</text>
  <text x="105" y="192" fill="#fef3c7" font-size="8" text-anchor="middle">Rebuilding &amp; Rehabilitation</text>
</svg>'''
]

mock_questions = [
    {
        "q": "Based on the ABC of First Aid flowchart, what is the very first step before attempting to evaluate a victim's breathing or pulse?",
        "options": [
            "Open the Airway (A) using the head-tilt chin-lift maneuver to clear obstructions",
            "Administer 50 chest compressions",
            "Give the victim hot milk to drink",
            "Wrap the legs in heavy plaster bandages"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The flowchart designates Airway (A) as the prerequisite first step: without an open, clear airway, no spontaneous respiration or artificial resuscitation is possible."
    },
    {
        "q": "Referring to the RICE quadrant diagram, what is the physiological benefit of applying cold ice ('I') to an acute sprain?",
        "options": [
            "Causes localized vasoconstriction, curbing internal capillary bleeding, fluid edema, and pain",
            "Permanently stops blood circulation in the entire leg",
            "Heats the muscle to 100 deg C",
            "Softens the bone to allow realignment"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The diagram details that cold application induces vasoconstriction, which limits edema and decreases local nerve conduction velocity to relieve pain."
    },
    {
        "q": "According to the CPR chest compression diagram, what is the precise anatomical target for hand placement on an adult casualty?",
        "options": [
            "The center of the chest on the lower half of the sternum",
            "Directly over the left lower ribs over the spleen",
            "On the upper throat above the thyroid cartilage",
            "Over the upper abdomen below the belly button"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Hand placement is centered on the lower half of the sternum, avoiding the xiphoid process to prevent internal liver trauma."
    },
    {
        "q": "In the Heimlich maneuver diagram for a choking victim, in which direction must the rescuer's abdominal thrusts be forcefully delivered?",
        "options": [
            "Quickly inward and upward just above the navel",
            "Downwards toward the knees",
            "Horizontally sideways against the ribs",
            "Straight downward on the shoulders"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The diagram displays inward and upward thrusts directed toward the diaphragm to compress residual lung air and pop out the foreign obstruction."
    },
    {
        "q": "Based on the burn classification and first aid chart, what is the single most critical immediate treatment for all thermal burns?",
        "options": [
            "Cool the burned area under clean running tap water for 10-15 minutes immediately",
            "Smear the skin with thick butter, oil, or toothpaste",
            "Puncture and peel away all blister skins",
            "Rub the burn with coarse sand"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The chart highlights the mandatory rule: cooling with gentle running water for 10-15 minutes stops dermal heat progression and minimizes burn depth."
    },
    {
        "q": "Examining the patient transportation methods panel, which technique allows two rescuers to form a stable interlocked hand-seat to carry a conscious patient who cannot walk?",
        "options": [
            "Four-Hand Seat method",
            "Cradle Carry",
            "Human Crutch method",
            "Firefighter's drag"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The four-hand seat employs two rescuers interlocking four wrists to construct a stable, rigid seat for conscious non-ambulatory casualties."
    },
    {
        "q": "According to the fracture splinting diagram, what is the golden rule when securing an emergency splint to a broken lower leg?",
        "options": [
            "Immobilize the joint above (knee) and the joint below (ankle), tying bandages above and below the fracture site",
            "Force the broken bones together until they click loudly",
            "Tie the bandage directly over the jagged fracture point",
            "Remove all shoes and socks by forcefully twisting the foot"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Splints must span and immobilize the joints immediately proximal and distal to the fracture to prevent bone movement and secondary tissue damage."
    },
    {
        "q": "Based on the bleeding control sequence, what must a first-aider do if the initial sterile gauze pad placed on a severe wound becomes completely soaked through with blood?",
        "options": [
            "Add additional absorbent pads on top and maintain firm pressure without removing the initial pad",
            "Yank off the soaked pad and throw it away",
            "Wash the wound out with hot soapy water",
            "Stop all pressure and leave the wound open"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The protocol warns: never remove the initial dressing because doing so disrupts delicate blood clots. Place fresh pads directly over the soaked one and maintain pressure."
    },
    {
        "q": "In the Recovery Position diagram, why is the unconscious breathing patient placed on their side with the head tilted back?",
        "options": [
            "It prevents the tongue from falling back into the throat and allows vomit or saliva to drain freely without entering the lungs",
            "It turns the victim's hair black",
            "It makes the victim wake up instantly within 1 second",
            "It stops all blood flow to the heart"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The lateral posture ensures airway patency by keeping the tongue forward and allowing gravitational drainage of fluids to prevent fatal aspiration."
    },
    {
        "q": "Referring to the Heatstroke versus Heat Exhaustion comparison panel, which life-threatening sign uniquely indicates heatstroke?",
        "options": [
            "Extremely high body temperature (>40 deg C) accompanied by hot, red, completely dry skin (cessation of sweating)",
            "Profuse sweating with pale cold clammy skin",
            "Mild headache with normal body temperature",
            "Shivering and freezing cold fingers"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Heatstroke represents thermal regulatory breakdown where sweating fails, skin turns hot and dry, and body temperature surges past 40 deg C, demanding emergency cooling."
    },
    {
        "q": "Based on the improvised stretcher diagram, how can two long wooden poles be converted into a reliable field stretcher without nails or screws?",
        "options": [
            "By threading the poles through the inside-out sleeves of two buttoned heavy jackets or wrapping a strong blanket around them",
            "By tying the poles together with fragile sewing thread",
            "By balancing the patient on a single pole like a tightrope",
            "By gluing the poles together with paper paste"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Threading poles through inside-out sleeves of sturdy buttoned jackets creates an improvised canvas stretcher capable of safely bearing adult weight."
    },
    {
        "q": "Examining the Disaster Management Cycle wheel, which phase includes conducting mock drills, testing early warning sirens, and training emergency rescue teams before a disaster strikes?",
        "options": [
            "Preparedness phase",
            "Post-disaster recovery phase",
            "Immediate response phase",
            "Debris cleanup phase"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The cycle assigns emergency drills, early warnings, and contingency planning to the pre-disaster Preparedness quadrant."
    }
]

def make_doc(item, idx, vault, category, svg=None):
    code = f"{TOPIC_CODE}-{item['type']}-{idx:03d}"
    doc = {
        "questionCode": code,
        "topicCode": TOPIC_CODE,
        "chapterNumber": 9,
        "subjectCode": "SCIT",
        "class": 9,
        "board": "MH",
        "text": item["q"],
        "options": item["options"],
        "correctAnswer": item["ans"],
        "type": item["type"],
        "difficulty": item["difficulty"],
        "marks": 4,
        "negativeMarks": 0,
        "status": "published",
        "usageCount": 0,
        "examCategory": category,
        "vault": vault,
        "explanation": item["exp"]
    }
    if svg:
        doc["figureSvg"] = svg
        doc["requiresFigure"] = True
    return doc

def generate_all():
    docs = []
    idx = 1
    # 40 Exam
    for item in exam_data:
        docs.append(make_doc(item, idx, "exam", "standard"))
        idx += 1
    # 30 Practice
    for item in practice_data:
        docs.append(make_doc(item, idx, "practice", "standard"))
        idx += 1
    # 12 Mock
    for i, item in enumerate(mock_questions):
        svg = svg_diagrams[i]
        docs.append(make_doc(item, idx, "mock", "foundation", svg))
        idx += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(docs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(docs)} questions for {TOPIC_CODE} -> {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_all()
