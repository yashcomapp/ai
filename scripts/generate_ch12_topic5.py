# scripts/generate_ch12_topic5.py
# MH-9-SCIT-12-12.5: Structure of Human Ear
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-12-12.5"

# 40 Exam Questions
exam_data = [
    # 1-10: Outer Ear & Ear Drum
    ("What are the three fundamental anatomical divisions of the human ear?",
     ["Outer ear, middle ear, and inner ear",
      "Cornea, iris, and retina",
      "Nose, pharynx, and larynx",
      "Cerebrum, cerebellum, and medulla"],
     "A", "OSC", "easy",
     "The human ear is partitioned anatomically and functionally into the outer ear (funneling), middle ear (amplification), and inner ear (sensory transduction)."),

    ("What is the primary acoustic function of the outer ear flap (pinna)?",
     ["To collect sound waves from the surrounding environment and direct them into the auditory canal",
      "To convert sound into electrical nerve impulses",
      "To amplify sound pressure 100 times",
      "To equalize air pressure with the lungs"],
     "A", "OSC", "easy",
     "The funnel-shaped pinna gathers sound pressure waves from the surroundings and channels them down the external auditory meatus toward the eardrum."),

    ("What is the name of the thin, delicate membrane that separates the external auditory canal from the middle ear cavity?",
     ["Tympanic membrane (eardrum)", "Oval window", "Basilar membrane", "Tectorial membrane"],
     "A", "OSC", "easy",
     "The tympanic membrane, commonly known as the eardrum, terminates the auditory canal and vibrates in response to arriving sound waves."),

    ("How does the tympanic membrane respond when an acoustic compression (high pressure) reaches it?",
     ["The high pressure on the outside pushes the eardrum inward",
      "The eardrum bulges outward",
      "The eardrum freezes in place",
      "The eardrum detaches from the ear canal"],
     "A", "OSC", "easy",
     "When a high-pressure compression wave arrives, the external air pressure exceeds internal middle-ear pressure, pushing the flexible eardrum inward."),

    ("How does the tympanic membrane respond when an acoustic rarefaction (low pressure) reaches it?",
     ["The low pressure on the outside allows the eardrum to move outward",
      "The eardrum moves inward even further",
      "The eardrum stops vibrating entirely",
      "The eardrum emits sound back to the room"],
     "A", "OSC", "easy",
     "During a rarefaction, external air pressure drops below the middle-ear pressure, causing the eardrum to move outward, thereby faithfully mimicking wave cycles."),

    ("What is the length of the external auditory canal in an adult human?",
     ["Approximately 2.5 to 3 centimetres",
      "Approximately 10 to 12 centimetres",
      "Approximately 0.5 millimetres",
      "Approximately 25 centimetres"],
     "A", "OSC", "medium",
     "The adult external acoustic meatus is an S-shaped tube approximately 2.5 to 3 cm long leading from the concha of the pinna to the tympanic membrane."),

    ("What protective substances are produced inside the auditory canal to trap dust, insects, and microorganisms?",
     ["Earwax (cerumen) and tiny protective hairs",
      "Salivary amylase",
      "Gastric acid",
      "Hydrochloric acid"],
     "A", "OSC", "easy",
     "Ceruminous and sebaceous glands secrete cerumen (earwax), which combines with fine hairs to trap particulate debris and inhibit microbial growth."),

    ("Why can a severe blow or inserting sharp objects like hairpins into the ear canal cause permanent hearing loss?",
     ["It can rupture or perforate the delicate tympanic membrane, destroying its ability to vibrate effectively",
      "It dissolves the auditory nerve immediately",
      "It melts the skull bones",
      "It stops the heart from beating"],
     "A", "OSC", "easy",
     "Puncturing the paper-thin eardrum disrupts mechanical wave transmission to the middle ear bones, introducing conduction deafness and middle-ear infection risk."),

    # 9-18: Middle Ear & Auditory Ossicles
    ("Which three tiny bones (auditory ossicles) are housed inside the middle ear cavity?",
     ["Malleus (hammer), incus (anvil), and stapes (stirrup)",
      "Femur, tibia, and fibula",
      "Humerus, radius, and ulna",
      "Scapula, clavicle, and sternum"],
     "A", "OSC", "easy",
     "The middle ear contains the three smallest bones in the human body: the malleus (hammer), incus (anvil), and stapes (stirrup)."),

    ("Which bone of the middle ear is directly attached to the inner surface of the tympanic membrane?",
     ["Malleus (hammer)", "Incus (anvil)", "Stapes (stirrup)", "Temporal bone"],
     "A", "OSC", "easy",
     "The handle (manubrium) of the malleus is firmly fused to the center of the inner aspect of the tympanic membrane."),

    ("Which middle ear bone is the smallest bone in the human body, and where does its footplate attach?",
     ["Stapes (stirrup), attaching to the membrane of the oval window",
      "Malleus (hammer), attaching to the cochlea",
      "Incus (anvil), attaching to the pinna",
      "Hyoid bone, attaching to the tongue"],
     "A", "OSC", "easy",
     "The stapes is the smallest bone in the human body (measuring ~3 mm); its footplate fits snugly into the oval window of the inner ear."),

    ("What is the primary mechanical function of the auditory ossicles in hearing?",
     ["They act as a lever system that amplifies the vibrational pressure of sound waves before delivering them to the fluid-filled inner ear",
      "They generate electrical impulses directly for the brain",
      "They absorb all sound vibrations to keep the ear quiet",
      "They produce earwax to lubricate the eardrum"],
     "A", "OSC", "easy",
     "The ossicular chain operates as a mechanical lever system, concentrating force from the large eardrum onto the much smaller oval window to overcome acoustic impedance mismatch of cochlear fluid."),

    ("Why is pressure amplification necessary when sound passes from the middle ear to the inner ear?",
     ["The inner ear is filled with dense liquid (perilymph) which has much higher acoustic impedance than air, requiring greater pressure to vibrate",
      "Sound waves lose speed in air",
      "The brain cannot hear quiet sounds",
      "Inner ear fluid evaporates without pressure"],
     "A", "OSC", "medium",
     "Liquid resists displacement far more than air (~3600 times greater acoustic impedance). Ossicular lever ratio (~1.3) and area ratio (~17:1) boost pressure over 20-fold to set perilymph in motion."),

    ("What is the function of the Eustachian tube that connects the middle ear cavity to the back of the nasopharynx (throat)?",
     ["To equalize air pressure between the middle ear cavity and the outside atmosphere",
      "To drain excess tears from the eyes",
      "To pump oxygen into the inner ear",
      "To swallow sound waves during eating"],
     "A", "OSC", "easy",
     "The Eustachian tube vents the middle ear to atmospheric pressure during swallowing or yawning, ensuring balanced pressure on both faces of the eardrum."),

    ("Why do your ears feel 'plugged' or 'pop' when ascending in an aeroplane or riding an elevator up a high skyscraper?",
     ["External atmospheric pressure drops rapidly while middle-ear pressure remains higher, bulging the eardrum until the Eustachian tube opens to equalize pressure",
      "The ear bones temporarily melt",
      "Gravity stops acting on the head",
      "Sound waves travel backwards at high altitudes"],
     "A", "OSC", "easy",
     "As altitude rises, external air pressure falls. The higher air pressure trapped in the middle ear pushes the eardrum outward until swallowing opens the Eustachian tube with a 'pop'."),

    # 19-30: Inner Ear, Cochlea & Auditory Transduction
    ("What is the 'cochlea' in the inner ear?",
     ["A snail-shaped, coiled fluid-filled bony organ responsible for converting mechanical sound vibrations into electrical nerve impulses",
      "A muscle that wiggles the outer ear",
      "A tube that balances blood pressure",
      "A nerve that controls facial expressions"],
     "A", "OSC", "easy",
     "The cochlea is a coiled structure resembling a snail shell (~2.5 turns) containing fluid chambers and sensory hair cells that transduce vibrations into nerve signals."),

    ("Which specialized sensory organ located on the basilar membrane inside the cochlea contains microscopic auditory hair cells?",
     ["Organ of Corti", "Islets of Langerhans", "Corpus callosum", "Loop of Henle"],
     "A", "OSC", "medium",
     "The Organ of Corti rests on the basilar membrane within the cochlear duct; its rows of mechanoreceptor hair cells transduce fluid shearing forces into receptor potentials."),

    ("What cranial nerve carries electrical auditory impulses from the cochlea to the auditory cortex of the brain?",
     ["Auditory nerve (vestibulocochlear nerve, VIII cranial nerve)",
      "Optic nerve",
      "Olfactory nerve",
      "Vagus nerve"],
     "A", "OSC", "easy",
     "The vestibulocochlear nerve (8th cranial nerve) conducts action potentials from the cochlea to the temporal lobe of the cerebral cortex for sound perception."),

    ("How does the cochlea distinguish between high-frequency (treble) and low-frequency (bass) sound tones?",
     ["High-frequency sounds vibrate the stiff basilar membrane near the base (oval window), while low-frequency sounds vibrate the flexible apex near the tip",
      "High-frequency sounds are processed in the stomach",
      "Low frequencies only vibrate the pinna",
      "The eardrum changes color depending on frequency"],
     "A", "OSC", "medium",
     "The basilar membrane is tonotopically mapped: narrow and rigid at the base (resonating to high pitch up to 20 kHz), and wider and compliant at the apex (resonating to low pitch down to 20 Hz)."),

    ("Which part of the inner ear is responsible for maintaining body balance, posture, and equilibrium rather than hearing?",
     ["The semicircular canals and vestibular apparatus",
      "The cochlea",
      "The tympanic membrane",
      "The incus"],
     "A", "OSC", "easy",
     "The three fluid-filled semicircular canals and otolith organs detect rotational and linear head acceleration to maintain equilibrium, operating independently of hearing."),

    ("What fluid fills the scala vestibuli and scala tympani compartments inside the cochlea?",
     ["Perilymph", "Endolymph", "Cerebrospinal fluid", "Synovial fluid"],
     "A", "OSC", "medium",
     "Perilymph (rich in sodium ions, similar to extracellular fluid) fills the outer compartments, while endolymph (rich in potassium) fills the central scala media."),

    ("What role does the 'round window' (fenestra cochleae) play during sound transmission inside the cochlea?",
     ["It bulges outward into the middle ear to relieve fluid pressure as the incompressibility of cochlear fluid demands displacement when the oval window pushes in",
      "It allows air to circulate inside the brain",
      "It shines light into the cochlea",
      "It collects sound waves from the jaw"],
     "A", "OSC", "medium",
     "Because liquids are virtually incompressible, inward movement of the oval window requires compensatory outward bulging of the flexible round window membrane to permit fluid wave motion."),

    ("State whether the following statement is True or False: The human ear is sensitive to sound frequencies ranging from approximately 20 Hz to 20,000 Hz.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The normal audible spectrum for healthy young human ears spans roughly 20 Hz to 20 kHz."),

    ("State whether the following statement is True or False: The stapes is connected directly to the tympanic membrane.",
     ["False", "True"],
     "A", "OTF", "easy",
     "The malleus connects to the tympanic membrane; the stapes connects to the oval window at the opposite end of the ossicular chain."),

    ("State whether the following statement is True or False: Prolonged exposure to loud noises exceeding 85-90 dB can permanently damage auditory hair cells in the cochlea.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Excessive acoustic energy shears and kills delicate cochlear stereocilia hair cells, which do not regenerate in humans, leading to irreversible noise-induced hearing loss."),

    ("State whether the following statement is True or False: The middle ear bones act as levers that reduce sound pressure before it reaches the brain.",
     ["False", "True"],
     "A", "OTF", "easy",
     "The ossicles amplify acoustic pressure by a factor of roughly 20 to 30 times, rather than reducing it."),

    # 31-40: Sound Pathway & Clinical Connections
    ("What is the correct, chronological sequence of structures through which sound energy propagates during human hearing?",
     ["Pinna -> Auditory Canal -> Tympanic Membrane -> Malleus -> Incus -> Stapes -> Oval Window -> Cochlea -> Auditory Nerve -> Brain",
      "Brain -> Cochlea -> Stapes -> Incus -> Malleus -> Eardrum -> Pinna",
      "Pinna -> Cochlea -> Tympanic Membrane -> Auditory Canal -> Brain",
      "Eardrum -> Pinna -> Oval Window -> Auditory Canal -> Brain"],
     "A", "OSC", "easy",
     "Acoustic waves traverse the outer canal to the eardrum, are amplified through the ossicles (malleus-incus-stapes), enter cochlear fluid via the oval window, and fire nerve impulses to the brain."),

    ("What is 'conductive hearing loss'?",
     ["Hearing impairment caused by physical obstruction or damage in the outer or middle ear (such as earwax blockage or perforated eardrum) preventing sound from reaching the cochlea",
      "Damage to the auditory processing centers of the cerebral cortex",
      "Complete destruction of the auditory nerve",
      "Inability to speak words clearly"],
     "A", "OSC", "medium",
     "Conductive deafness arises when sound waves cannot be mechanically conducted to the inner ear, whereas sensorineural deafness involves hair cell or auditory nerve degradation."),

    ("What is 'sensorineural hearing loss'?",
     ["Hearing loss resulting from damage to the sensory hair cells of the cochlea or the auditory nerve fibers",
      "A buildup of wax in the ear canal",
      "A stiffening of middle ear bones",
      "A blocked Eustachian tube during a cold"],
     "A", "OSC", "medium",
     "Sensorineural impairment stems from neural or sensory receptor lesions (due to aging, ototoxic drugs, or chronic acoustic trauma)."),

    ("How does a cochlear implant restore auditory perception in individuals with severe sensorineural deafness?",
     ["It bypasses damaged cochlear hair cells by using an electrode array to directly stimulate auditory nerve fibers electrically",
      "It surgically glues the eardrum to the skull",
      "It amplifies air vibrations in the outer canal like a megaphone",
      "It regrows new human ear pinnae on the skin"],
     "A", "OSC", "medium",
     "Cochlear implants capture acoustic sound with an external microphone and processor, converting signals into electrical impulses that stimulate the auditory nerve directly."),

    ("Why can chewing gum or swallowing relieve ear discomfort during aircraft landing?",
     ["Swallowing engages the tensor veli palatini muscles to open the Eustachian tube, allowing air to enter the middle ear and relieve negative pressure",
      "Chewing gum vibrates the skull bones",
      "Gum absorbs excess sound waves from the engine",
      "Swallowing produces anesthetic saliva"],
     "A", "OSC", "easy",
     "Swallowing activates pharyngeal muscles that pull open the Eustachian tube valve, equalizing middle-ear pressure with atmospheric pressure."),

    ("Why is human hearing bidirectional (binaural)?",
     ["Having two ears on opposite sides of the head allows the brain to calculate minute differences in arrival time (interaural time difference) and intensity to localize sound sources in space",
      "One ear hears only high frequencies while the other hears only low frequencies",
      "One ear operates during the day and the other at night",
      "To listen to two conversations at once"],
     "A", "OSC", "easy",
     "Binaural audition enables sound source localization by detecting sub-millisecond arrival time differences (ITD) and head-shadow intensity variations (IID)."),

    ("What is the surface area ratio between the human tympanic membrane (~55 mm^2 active area) and the stapes footplate (~3.2 mm^2)?",
     ["Approximately 17 to 1",
      "Approximately 1 to 1",
      "Approximately 100 to 1",
      "Approximately 2 to 1"],
     "A", "OSC", "medium",
     "The large area ratio of ~17:1 concentrates vibrational acoustic force onto a tiny oval window area, yielding a ~17-fold pressure gain (P = F / A)."),

    ("What role does the acoustic reflex (stapedius reflex) play in protecting the inner ear?",
     ["Tiny muscles (stapedius and tensor tympani) contract involuntarily in response to loud sounds, stiffening the ossicular chain to dampen sound transmission",
      "It closes the pinna like an eyelid",
      "It pours earwax into the canal within one millisecond",
      "It shifts the cochlea into the skull cavity"],
     "A", "OSC", "medium",
     "The stapedius muscle contracts reflexively upon loud sounds (>85 dB), pulling the stapes away from the oval window to attenuate energy delivered to the delicate cochlea."),

    ("Why do elderly people frequently lose the ability to perceive high-pitched sounds first (presbycusis)?",
     ["Hair cells at the basal entrance of the cochlea bear the brunt of mechanical hydraulic stress throughout life and degrade earlier than apical hair cells",
      "The pinna shrinks with age",
      "The eardrum becomes too soft",
      "The Eustachian tube closes permanently"],
     "A", "OSC", "medium",
     "Basal hair cells register high frequencies and undergo continual cumulative mechanical shearing, making them the most susceptible to age-related degenerative loss."),

    ("Which part of the ear contains air, and which part contains fluid?",
     ["The outer ear canal and middle ear cavity contain air; the inner ear cochlea contains fluid",
      "All parts of the ear contain air only",
      "All parts of the ear contain fluid only",
      "The middle ear contains fluid and the inner ear contains air"],
     "A", "OSC", "easy",
     "The external auditory canal and middle ear are air-filled cavities, whereas the cochlea and vestibular labyrinth of the inner ear are completely fluid-filled."),

    ("What is the primary function of the tensor tympani muscle attached to the malleus?",
     ["It pulls the malleus medially to tense the tympanic membrane, dampening vibrations from loud chewing or self-vocalization",
      "It vibrates the pinna during flight",
      "It secretes earwax directly into the canal",
      "It connects the ear to the collarbone"],
     "A", "OSC", "medium",
     "The tensor tympani muscle tenses the eardrum to protect hearing against internal noise such as chewing."),

    ("Why does cupping your hand behind your ear help you hear distant faint sounds more clearly?",
     ["It artificially increases the effective surface aperture of the pinna, capturing and funneling more acoustic wavefront energy into the canal",
      "It heats the incoming sound waves",
      "It changes the frequency of sound to ultrasound",
      "It increases the speed of sound"],
     "A", "OSC", "easy",
     "Cupping your hand enlarges the pinna's acoustic collection area, focusing additional acoustic pressure waves into the meatus."),

    ("What happens to sound transmission if the tiny stapes bone becomes fused rigidly to the oval window (otosclerosis)?",
     ["The stapes cannot vibrate, causing severe conductive hearing loss because sound cannot enter the cochlear fluid",
      "Hearing improves dramatically",
      "The cochlea begins to emit loud music",
      "The eardrum turns into bone"],
     "A", "OSC", "medium",
     "Otosclerosis causes abnormal bone growth that locks the stapes footplate, preventing mechanical vibration of perilymph and causing conductive deafness."),

    ("State whether the following statement is True or False: Humans can hear sounds as quiet as 0 decibels, which represents the normal threshold of hearing.",
     ["True", "False"],
     "A", "OTF", "easy",
     "0 dB SPL corresponds to the average auditory threshold of human hearing at 1,000 Hz in healthy young individuals.")
]

# 30 Practice Questions
practice_data = [
    ("What is the medical term for the outer ear structure commonly referred to as the ear flap?",
     ["Pinna (or auricle)", "Cochlea", "Tympanum", "Incus"],
     "A", "OSC", "easy",
     "The pinna or auricle is the visible cartilaginous flap of the external ear."),

    ("Which middle ear bone is shaped like a blacksmith's anvil?",
     ["Incus", "Malleus", "Stapes", "Cochlea"],
     "A", "OSC", "easy",
     "The incus is named after the Latin word for anvil due to its characteristic shape."),

    ("Which middle ear bone is shaped like a stirrup?",
     ["Stapes", "Malleus", "Incus", "Pinna"],
     "A", "OSC", "easy",
     "The stapes resembles a horse-riding stirrup, possessing two crura and a flat footplate."),

    ("Which middle ear bone is shaped like a hammer?",
     ["Malleus", "Stapes", "Incus", "Mastoid"],
     "A", "OSC", "easy",
     "The malleus takes its name from the Latin word for hammer."),

    ("State whether the following statement is True or False: The Eustachian tube connects the middle ear to the stomach.",
     ["False", "True"],
     "A", "OTF", "easy",
     "The Eustachian tube links the middle ear to the nasopharynx (upper throat), not the stomach."),

    ("State whether the following statement is True or False: The semicircular canals play an essential role in hearing musical pitch.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Semicircular canals detect angular head rotation for balance; they have no role in acoustic hearing."),

    ("State whether the following statement is True or False: The auditory nerve transmits sound signals as electrical nerve impulses to the brain.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Action potentials triggered by hair cell depolarization are conducted along the 8th cranial nerve to the auditory cortex."),

    ("What happens to auditory perception if the middle ear cavity becomes filled with thick fluid during middle ear infection (otitis media)?",
     ["Vibrations of the eardrum and ossicles are severely dampened, resulting in temporary conductive hearing impairment",
      "Hearing acuity doubles immediately",
      "The patient can hear ultrasound frequencies",
      "The eardrum permanently disappears"],
     "A", "OSC", "easy",
     "Fluid accumulation restricts the free vibration of the tympanic membrane and ossicles, causing temporary conductive hearing loss."),

    ("How many turns does the spiral canal of the human cochlea make around its central modiolus axis?",
     ["Approximately 2.5 to 2.75 turns",
      "Approximately 10 turns",
      "Exactly 1 turn",
      "Zero turns (it is completely straight)"],
     "A", "OSC", "medium",
     "The human cochlea coils like a garden snail shell for roughly 2.5 to 2.75 helical turns."),

    ("Why does listening to loud music via in-ear earphones at maximum volume pose a severe hearing hazard?",
     ["Earphones deliver high sound pressure levels directly into the ear canal without acoustic dissipation, causing mechanical fatigue and death of cochlear hair cells",
      "Earphones melt the pinna cartilage",
      "Earphones generate nuclear radiation",
      "Earphones turn earwax into stone"],
     "A", "OSC", "easy",
     "In-ear earphones seal the ear canal and can produce levels over 105 dB, stressing hair cell stereocilia to irreversible failure."),

    # 11-20
    ("What membrane separates the scala media from the scala tympani and supports the Organ of Corti?",
     ["Basilar membrane", "Reissner's membrane", "Tympanic membrane", "Perichondrium"],
     "A", "OSC", "medium",
     "The basilar membrane forms the floor of the cochlear duct and supports the Organ of Corti containing the sensory hair cells."),

    ("Where are the hair cells that detect sound located?",
     ["Inside the cochlea on the Organ of Corti",
      "On the surface of the pinna",
      "Inside the Eustachian tube",
      "On the outer face of the eardrum"],
     "A", "OSC", "easy",
     "The mechanosensory hair cells reside in the Organ of Corti on the basilar membrane inside the cochlea."),

    ("What happens when sound vibrations cause stereocilia on hair cells to bend against the tectorial membrane?",
     ["Mechanically gated ion channels open, depolarizing the hair cell and triggering nerve impulses in the auditory nerve fibers",
      "The hair cells break off and are replaced every minute",
      "The hair cells release gastric juice",
      "The hair cells freeze like ice"],
     "A", "OSC", "medium",
     "Shearing deflection of stereocilia mechanically pulls open potassium-permeable channels, initiating depolarization and neurotransmitter release."),

    ("What is the primary function of the pinna's irregular outer cartilage folds (concha, tragus, helix)?",
     ["They create subtle frequency notches and spectral cues that assist the brain in determining whether sound comes from above, below, in front, or behind",
      "To hold reading eyeglasses securely",
      "To store spare oxygen",
      "To radiate excess body heat"],
     "A", "OSC", "medium",
     "The intricate convolutions of the pinna act as passive acoustic filters, imparting vertical elevation cues to incoming wavefronts."),

    ("State whether the following statement is True or False: Cerumen (earwax) possesses mild antibacterial and antifungal properties.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Cerumen contains lysozyme, fatty acids, and an acidic pH that inhibit bacterial and fungal proliferation in the moist canal."),

    ("State whether the following statement is True or False: The human ear canal is a completely straight tube perpendicular to the skull.",
     ["False", "True"],
     "A", "OTF", "easy",
     "The auditory canal has a natural gentle S-shaped curvature that shields the tympanic membrane from direct traumatic injury."),

    ("State whether the following statement is True or False: The stapes is connected to the round window.",
     ["False", "True"],
     "A", "OTF", "easy",
     "The stapes footplate connects to the oval window; the round window is located below it and acts as a pressure relief vent."),

    ("Why is yawning effective at popping your ears when descending during flight?",
     ["Yawning contracts the tensor veli palatini muscle, pulling open the Eustachian tube orifice and allowing air pressure to equilibrate",
      "Yawning increases brain temperature",
      "Yawning stops breathing momentarily",
      "Yawning rotates the ossicles 180 degrees"],
     "A", "OSC", "easy",
     "Yawning actively dilates the pharyngeal opening of the Eustachian tube, permitting pressurized air to balance across the eardrum."),

    ("What is 'tinnitus'?",
     ["The perception of ringing, buzzing, or hissing sounds in the ears in the absence of an external acoustic source",
      "Total absence of earwax",
      "Inflammation of the throat",
      "A crack in the jawbone"],
     "A", "OSC", "easy",
     "Tinnitus is phantom sound perception generated by hyperactivity in the auditory cortex following damage to peripheral hair cells."),

    ("What is the lever multiplication factor provided by the auditory ossicles malleus and incus?",
     ["Approximately 1.3 times",
      "Approximately 20 times",
      "Approximately 100 times",
      "Approximately 0.1 times"],
     "A", "OSC", "medium",
     "The malleus-incus lever arm ratio provides a mechanical force multiplication of roughly 1.3:1."),

    # 21-30
    ("When combined with the area ratio between eardrum and oval window (~17:1), what is the total pressure amplification factor achieved by the middle ear?",
     ["Roughly 22 times (17 * 1.3 \approx 22)",
      "Roughly 2 times",
      "Roughly 500 times",
      "Roughly 1 time (no amplification)"],
     "A", "OSC", "medium",
     "Multiplying the area advantage (~17) by the ossicular lever advantage (~1.3) gives an effective pressure amplification of approximately 22-fold."),

    ("Why cannot humans hear ultrasound frequencies above 20,000 Hz, whereas dogs can hear up to 40,000 Hz?",
     ["The human basilar membrane lacks hair cell receptors tuned to resonant frequencies above 20 kHz, and ossicle inertia filters out extreme frequencies",
      "Human eardrums are too thin to touch ultrasound",
      "Humans lack auditory nerves entirely",
      "Human brain has no temporal lobe"],
     "A", "OSC", "easy",
     "The mechanical stiffness and mass of the human basilar membrane and ossicles physically cannot transmit or resolve acoustic oscillations above 20 kHz."),

    ("State whether the following statement is True or False: Rupturing the eardrum always causes total, permanent deafness from which a person never recovers.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Minor eardrum perforations frequently heal spontaneously over several weeks or can be surgically repaired via tympanoplasty with good hearing recovery."),

    ("State whether the following statement is True or False: The auditory cortex where sound is consciously recognized is located in the temporal lobes of the cerebrum.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Auditory nerve pathways project to the primary auditory cortex situated in Heschl's gyri of the temporal lobes."),

    ("What is the function of the tiny hair cells in the cochlea?",
     ["They act as sensory mechanoreceptors that convert fluid wave vibrations into nerve impulses",
      "They keep the ear canal warm",
      "They filter dust particles from cochlear fluid",
      "They prevent earwax from entering the brain"],
     "A", "OSC", "easy",
     "Hair cells are biological mechanoreceptors whose stereocilia deflections transduce fluid vibrations into electrochemical receptor potentials."),

    ("Why can sudden intense sound blasts (such as bomb explosions or artillery fire) cause immediate hearing loss?",
     ["The extreme acoustic pressure wave exerts violent shearing forces that tear stereocilia off hair cells or rupture the eardrum",
      "The sound wave chemically turns perilymph into acid",
      "The sound wave stops blood flow to the lungs",
      "The sound wave freezes the skull bone"],
     "A", "OSC", "easy",
     "Acoustic blast trauma produces catastrophic pressure spikes that mechanically detach and destroy sensory hair cells and rupture the tympanum."),

    ("What happens to sound vibrations once they arrive at the oval window?",
     ["The piston-like motion of the stapes footplate pushes the oval window membrane, generating fluid traveling waves inside the cochlea",
      "They bounce back out of the ear",
      "They are converted directly into visible light",
      "They escape through the Eustachian tube"],
     "A", "OSC", "easy",
     "The stapes pushes into the oval window, propagating mechanical pressure waves through perilymph fluid in the scala vestibuli."),

    ("Which part of the ear acts as an impedance-matching transformer between air and fluid?",
     ["The middle ear with its eardrum and auditory ossicles",
      "The pinna",
      "The auditory canal",
      "The auditory cortex"],
     "A", "OSC", "medium",
     "The middle ear functions as an acoustic impedance transformer, bridging the huge acoustic impedance gulf between airborne sound and liquid-filled cochlea."),

    ("Why do children suffer from middle ear infections (otitis media) more frequently than adults?",
     ["In children, the Eustachian tube is shorter, narrower, and more horizontal, allowing bacteria from nasal colds to enter the middle ear cavity more easily",
      "Children have five eardrums in each ear",
      "Children lack earwax completely",
      "Children produce ultrasound naturally"],
     "A", "OSC", "easy",
     "The pediatric Eustachian tube is shorter and more horizontal, impairing natural drainage and facilitating retrograde migration of pharyngeal pathogens."),

    ("What type of energy transformation occurs inside the cochlea of the human ear?",
     ["Mechanical fluid wave energy is transformed into electrochemical electrical nerve impulses",
      "Thermal energy is transformed into nuclear energy",
      "Light energy is transformed into chemical potential energy",
      "Magnetic energy is transformed into gravitational energy"],
     "A", "OSC", "easy",
     "The Organ of Corti is a biological transducer converting mechanical acoustic fluid vibrations into electrochemical action potentials.")
]

# 12 Mock Questions with Vector SVG Diagrams
mock_data = [
    # 71: Overview of Ear Anatomy
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <!-- Outer Ear: Pinna & Canal -->
  <path d="M 30 50 C 15 70 15 130 35 150 C 45 140 45 60 30 50 Z" fill="#f87171" opacity="0.4" stroke="#ef4444" stroke-width="2"/>
  <text x="25" y="40" fill="#fca5a5" font-size="9" font-weight="bold">Pinna</text>
  <!-- Ear Canal -->
  <rect x="45" y="85" width="60" height="20" fill="#334155" stroke="#64748b"/>
  <text x="48" y="118" fill="#94a3b8" font-size="8">Ear Canal</text>
  <!-- Tympanic Membrane -->
  <line x1="105" y1="80" x2="105" y2="110" stroke="#facc15" stroke-width="3"/>
  <text x="90" y="72" fill="#facc15" font-size="8">Eardrum</text>
  <!-- Middle Ear Cavity & Ossicles -->
  <rect x="110" y="70" width="65" height="40" fill="#1e293b" stroke="#38bdf8" stroke-dasharray="2,2"/>
  <!-- Malleus, Incus, Stapes -->
  <line x1="106" y1="90" x2="125" y2="85" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="125" y1="85" x2="145" y2="88" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="145" y1="88" x2="165" y2="90" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="115" y="65" fill="#38bdf8" font-size="8" font-weight="bold">Ossicles</text>
  <!-- Inner Ear: Cochlea -->
  <path d="M 180 85 C 200 70 230 70 235 90 C 240 110 215 120 195 110 C 185 105 190 95 205 95 C 215 95 215 105 205 105" fill="none" stroke="#4ade80" stroke-width="3"/>
  <text x="240" y="95" fill="#4ade80" font-size="9" font-weight="bold">Cochlea</text>
  <!-- Auditory Nerve -->
  <line x1="230" y1="110" x2="280" y2="120" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,2"/>
  <text x="245" y="135" fill="#fda4af" font-size="8">Auditory Nerve</text>
  <!-- Eustachian Tube -->
  <line x1="140" y1="110" x2="160" y2="160" stroke="#e2e8f0" stroke-width="2"/>
  <text x="165" y="155" fill="#e2e8f0" font-size="8">Eustachian Tube</text>
  <text x="50" y="185" fill="#facc15" font-size="9">Path: Pinna -> Canal -> Eardrum -> Ossicles -> Cochlea -> Nerve</text>
</svg>
</div>
The diagram shows the major anatomical divisions of the human ear. Which numbered sequence accurately outlines the chronological pathway of acoustic energy from the external environment to the brain?""",
     ["Pinna -> Auditory Canal -> Tympanic Membrane -> Ossicles -> Cochlea -> Auditory Nerve""",
     "Auditory Nerve -> Cochlea -> Ossicles -> Eardrum -> Pinna""",
     "Pinna -> Eustachian Tube -> Cochlea -> Auditory Canal""",
     "Eardrum -> Pinna -> Cochlea -> Ossicles -> Brain"],
     "A", "easy""",
     "Sound waves are gathered by the pinna, travel along the auditory canal to vibrate the tympanum, are amplified by the ossicles, stimulate the fluid of the cochlea, and travel as nerve impulses along the auditory nerve."),

    # 72: Three Middle Ear Ossicles Lever System
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Eardrum -->
  <line x1="50" y1="50" x2="50" y2="140" stroke="#facc15" stroke-width="3"/>
  <text x="25" y="40" fill="#facc15" font-size="8">Eardrum</text>
  <!-- Malleus (Hammer) -->
  <path d="M 52 90 L 110 70 L 120 85 L 75 105 Z" fill="#38bdf8"/>
  <text x="70" y="65" fill="#38bdf8" font-size="9" font-weight="bold">Malleus</text>
  <!-- Incus (Anvil) -->
  <path d="M 120 70 L 170 80 L 160 120 L 135 95 Z" fill="#818cf8"/>
  <text x="140" y="65" fill="#818cf8" font-size="9" font-weight="bold">Incus</text>
  <!-- Stapes (Stirrup) -->
  <path d="M 170 85 L 210 75 L 210 95 Z" fill="#f43f5e"/>
  <line x1="210" y1="70" x2="210" y2="100" stroke="#f43f5e" stroke-width="3"/>
  <text x="215" y="75" fill="#f43f5e" font-size="9" font-weight="bold">Stapes</text>
  <!-- Oval Window -->
  <line x1="215" y1="65" x2="215" y2="105" stroke="#4ade80" stroke-width="3"/>
  <text x="220" y="115" fill="#4ade80" font-size="8">Oval Window</text>
  <text x="60" y="165" fill="#fde68a" font-size="9">Mechanical Lever Ratio: 1.3:1 | Area Ratio: 17:1</text>
  <text x="60" y="180" fill="#38bdf8" font-size="9">Total Pressure Amplification: ~22 times</text>
</svg>
</div>
The illustration depicts the three auditory ossicles of the middle ear. By what combined mechanical mechanism do these bones amplify sound pressure before it enters the fluid-filled inner ear?""",
     ["Through a lever ratio of ~1.3:1 combined with an area reduction ratio of ~17:1 from the large eardrum to the small stapes footplate, boosting pressure over 20-fold""",
     "By heating the air inside the middle ear cavity""",
     "By reflecting sound waves back and forth 100 times""",
     "By converting sound into laser light"],
     "A", "medium""",
     "Pressure is force divided by area (P = F / A). The ossicles provide a 1.3x lever force multiplication, while the surface area ratio (55 mm^2 eardrum to 3.2 mm^2 stapes footplate) yields an additional 17x gain, multiplying total pressure by ~22 times."),

    # 73: Cross-Section of Cochlea
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Cochlear duct cross section triangular -->
  <!-- Scala Vestibuli (top) -->
  <path d="M 50 40 Q 170 20 290 40 L 250 90 L 90 90 Z" fill="#0369a1" opacity="0.4" stroke="#38bdf8"/>
  <text x="120" y="55" fill="#38bdf8" font-size="9" font-weight="bold">Scala Vestibuli (Perilymph)</text>
  <!-- Scala Media (middle) -->
  <path d="M 90 90 L 250 90 L 220 135 L 120 135 Z" fill="#047857" opacity="0.4" stroke="#34d399"/>
  <text x="130" y="110" fill="#34d399" font-size="9" font-weight="bold">Scala Media (Endolymph)</text>
  <!-- Basilar membrane -->
  <line x1="120" y1="135" x2="220" y2="135" stroke="#facc15" stroke-width="3"/>
  <text x="225" y="138" fill="#facc15" font-size="8">Basilar Membrane</text>
  <!-- Organ of Corti with hair cells -->
  <circle cx="160" cy="130" r="4" fill="#ef4444"/>
  <circle cx="175" cy="130" r="4" fill="#ef4444"/>
  <text x="145" y="125" fill="#fca5a5" font-size="8">Hair Cells</text>
  <!-- Scala Tympani (bottom) -->
  <path d="M 120 135 L 220 135 L 250 170 Q 170 185 90 170 Z" fill="#0369a1" opacity="0.4" stroke="#38bdf8"/>
  <text x="120" y="165" fill="#38bdf8" font-size="9" font-weight="bold">Scala Tympani (Perilymph)</text>
</svg>
</div>
The cross-section above illustrates the three fluid compartments of the cochlear coil. Which critical sensory structure rests directly upon the basilar membrane in the scala media?""",
     ["The Organ of Corti containing sensory hair cells that transduce fluid motion into nerve impulses""",
     "The Eustachian valve""",
     "The malleus bone""",
     "The tympanic membrane"],
     "A", "medium""",
     "The Organ of Corti sits atop the basilar membrane in the scala media, where auditory hair cell stereocilia are deflected by acoustic traveling waves."),

    # 74: Frequency Tonotopy on Basilar Membrane
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Uncoiled Basilar Membrane Wedge -->
  <path d="M 50 90 L 290 60 L 290 130 L 50 100 Z" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Base near oval window -->
  <text x="40" y="55" fill="#ef4444" font-size="9" font-weight="bold">Base (Stiff & Narrow)</text>
  <text x="40" y="70" fill="#f87171" font-size="8">High Frequencies (~20 kHz)</text>
  <!-- Apex at tip -->
  <text x="210" y="45" fill="#22c55e" font-size="9" font-weight="bold">Apex (Flexible & Wide)</text>
  <text x="210" y="60" fill="#4ade80" font-size="8">Low Frequencies (~20 Hz)</text>
  <!-- Frequency markers along membrane -->
  <circle cx="70" cy="95" r="4" fill="#ef4444"/>
  <text x="65" y="115" fill="#f87171" font-size="8">16 kHz</text>
  <circle cx="130" cy="95" r="4" fill="#f59e0b"/>
  <text x="125" y="115" fill="#fbbf24" font-size="8">4 kHz</text>
  <circle cx="190" cy="95" r="4" fill="#3b82f6"/>
  <text x="185" y="115" fill="#60a5fa" font-size="8">1 kHz</text>
  <circle cx="260" cy="95" r="4" fill="#22c55e"/>
  <text x="255" y="115" fill="#4ade80" font-size="8">200 Hz</text>
  <text x="45" y="170" fill="#fde68a" font-size="9">Tonotopic Place Theory of Pitch Perception</text>
</svg>
</div>
The uncoiled basilar membrane shown above exhibits tonotopic mapping. Where along the membrane do high-pitched treble sounds (e.g. 15,000 Hz) produce maximum resonant vibration?""",
     ["Near the narrow, stiff base closest to the oval window""",
     "Near the wide, flexible apex at the far tip""",
     "Exactly at the geometric center only""",
     "Uniformly across the entire length simultaneously"],
     "A", "medium""",
     "The base of the basilar membrane is narrow and structurally rigid, causing high-frequency fluid waves to resonate and peak near the oval window entrance."),

    # 75: Eustachian Tube Pressure Equalization
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Middle ear cavity box -->
  <rect x="70" y="50" width="130" height="70" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="85" y="70" fill="#38bdf8" font-size="9" font-weight="bold">Middle Ear Cavity</text>
  <!-- Bulging eardrum -->
  <path d="M 70 50 Q 55 85 70 120" stroke="#facc15" stroke-width="3" fill="none"/>
  <text x="25" y="88" fill="#facc15" font-size="8">Bulging Eardrum</text>
  <!-- Outside low pressure -->
  <text x="20" y="40" fill="#94a3b8" font-size="8">P_out = 0.7 atm (High Altitude)</text>
  <!-- Inside high pressure -->
  <text x="85" y="95" fill="#f87171" font-size="8">P_in = 1.0 atm (Trapped)</text>
  <!-- Eustachian tube opening downwards -->
  <path d="M 150 120 L 150 160 L 210 170" stroke="#4ade80" stroke-width="3" fill="none"/>
  <text x="165" y="150" fill="#4ade80" font-size="8">Eustachian Tube</text>
  <text x="220" y="175" fill="#a7f3d0" font-size="8">To Throat</text>
  <text x="50" y="185" fill="#fde68a" font-size="9">Swallowing opens tube -> Equalizes P_in with P_out</text>
</svg>
</div>
When ascending rapidly in an aircraft (depicted above), the passenger experiences ear fullness and muffled hearing. Why does this happen, and how does swallowing resolve it?""",
     ["Lower external cabin pressure causes higher middle-ear pressure to push the eardrum outward; swallowing opens the Eustachian tube to vent air and equalize pressure""",
     "Air escapes through the skull bones""",
     "The ear canal fills with liquid""",
     "The cochlea stops functioning permanently"],
     "A", "easy""",
     "Pressure imbalance bends the tympanum outward, dampening vibration. Swallowing dilates the Eustachian tube, releasing trapped air into the pharynx to equalize pressure."),

    # 76: Cochlear Hair Cell Transduction
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Tectorial membrane above -->
  <rect x="70" y="40" width="200" height="16" fill="#64748b" rx="3"/>
  <text x="110" y="52" fill="#e2e8f0" font-size="8" font-weight="bold">Tectorial Membrane</text>
  <!-- Stereocilia hairs bending -->
  <line x1="145" y1="56" x2="135" y2="90" stroke="#facc15" stroke-width="2"/>
  <line x1="155" y1="56" x2="148" y2="90" stroke="#facc15" stroke-width="2"/>
  <line x1="165" y1="56" x2="160" y2="90" stroke="#facc15" stroke-width="2"/>
  <text x="175" y="75" fill="#facc15" font-size="8">Stereocilia deflection</text>
  <!-- Hair cell body -->
  <path d="M 130 90 L 175 90 L 165 145 L 140 145 Z" fill="#ef4444" stroke="#f87171" stroke-width="1.5"/>
  <text x="135" y="120" fill="#fde68a" font-size="8" font-weight="bold">Hair Cell</text>
  <!-- Synapse to Auditory Nerve Fiber -->
  <line x1="150" y1="145" x2="150" y2="175" stroke="#38bdf8" stroke-width="2.5"/>
  <circle cx="150" cy="175" r="4" fill="#38bdf8"/>
  <text x="160" y="175" fill="#38bdf8" font-size="8">Auditory Nerve Action Potentials</text>
  <text x="45" y="25" fill="#4ade80" font-size="9">Mechanical Shear -> K+ Influx -> Neurotransmitter Release</text>
</svg>
</div>
What vital cellular process occurs when sound waves cause stereocilia on hair cells to bend (illustrated above)?""",
     ["Mechanical bending opens ion channels, depolarizing the cell and initiating electrical impulses along the auditory nerve""",
     "Hair cells split in two by mitosis""",
     "Hair cells emit visible light flashes""",
     "Hair cells freeze to protect the brain"],
     "A", "medium""",
     "Tip links between stereocilia physically pull open mechanosensitive ion channels, allowing K+ influx from endolymph to trigger neurotransmitter release onto auditory nerve fibers."),

    # 77: Round Window Pressure Venting
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Cochlea fluid channel U-tube -->
  <path d="M 90 70 L 250 70 C 270 70 270 130 250 130 L 90 130" fill="none" stroke="#38bdf8" stroke-width="26"/>
  <!-- Stapes at Oval Window pushing in -->
  <rect x="75" y="57" width="15" height="26" fill="#ef4444"/>
  <line x1="50" y1="70" x2="75" y2="70" stroke="#facc15" stroke-width="2"/>
  <polygon points="75,67 85,70 75,73" fill="#facc15"/>
  <text x="35" y="52" fill="#ef4444" font-size="8">Stapes pushes IN (Oval Window)</text>
  <!-- Round Window bulging out -->
  <path d="M 90 117 Q 75 130 90 143" stroke="#4ade80" stroke-width="3" fill="none"/>
  <polygon points="75,130 65,130 75,127" fill="#4ade80"/>
  <text x="35" y="160" fill="#4ade80" font-size="8">Round Window bulges OUT</text>
  <text x="110" y="103" fill="#0f172a" font-size="9" font-weight="bold">Incompressible Cochlear Perilymph</text>
  <text x="50" y="180" fill="#fde68a" font-size="9">Incompressibility of liquid necessitates round window flexure</text>
</svg>
</div>
Because liquids inside the cochlea are essentially incompressible, what would happen if the round window membrane did NOT bulge outward when the stapes pushes inward at the oval window?""",
     ["The cochlear fluid could not move or form traveling waves, preventing hair cells from being stimulated and causing severe hearing impairment""",
     "The brain would explode from water pressure""",
     "Sound speed would become infinite""",
     "The eardrum would turn into glass"],
     "A", "medium""",
     "Enclosed incompressible liquid cannot be displaced in a rigid bony labyrinth without a flexible release port; the round window provides this essential mechanical compliance."),

    # 78: Semicircular Canals & Balance
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Three semicircular canals orthogonal -->
  <ellipse cx="140" cy="80" rx="35" ry="18" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <ellipse cx="170" cy="70" rx="18" ry="35" fill="none" stroke="#818cf8" stroke-width="3"/>
  <path d="M 125 90 C 130 130 180 130 185 90" fill="none" stroke="#f43f5e" stroke-width="3"/>
  <text x="75" y="35" fill="#38bdf8" font-size="9" font-weight="bold">Three Semicircular Canals (X, Y, Z planes)</text>
  <!-- Ampullae with cupula -->
  <circle cx="125" cy="90" r="5" fill="#facc15"/>
  <circle cx="185" cy="90" r="5" fill="#facc15"/>
  <text x="80" y="160" fill="#fde68a" font-size="9">Sense 3D angular rotation & head motion</text>
  <text x="80" y="175" fill="#4ade80" font-size="9">Maintain body balance and dynamic posture</text>
</svg>
</div>
The three semicircular canals shown above are oriented at right angles to one another. What essential function do they perform in the human body?""",
     ["Detecting rotational acceleration of the head in three-dimensional space to maintain balance and equilibrium""",
     "Analyzing musical melodies and harmony""",
     "Measuring atmospheric air pressure""",
     "Storing excess saliva from the mouth"],
     "A", "easy""",
     "The semicircular canals are aligned in three orthogonal geometric planes; fluid flow across their cupulae detects yaw, pitch, and roll angular head movements for equilibrium."),

    # 79: Comparison of Conductive vs Sensorineural Hearing Loss
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Box 1: Conductive Loss -->
  <rect x="25" y="30" width="135" height="120" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="4"/>
  <text x="35" y="50" fill="#fbbf24" font-size="9" font-weight="bold">Conductive Loss</text>
  <text x="35" y="70" fill="#cbd5e1" font-size="8">- Outer / Middle ear</text>
  <text x="35" y="85" fill="#cbd5e1" font-size="8">- Wax buildup, ruptured drum</text>
  <text x="35" y="100" fill="#cbd5e1" font-size="8">- Stiff ossicles (otosclerosis)</text>
  <text x="35" y="130" fill="#34d399" font-size="8">Often medically treatable</text>
  <!-- Box 2: Sensorineural Loss -->
  <rect x="180" y="30" width="135" height="120" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" rx="4"/>
  <text x="190" y="50" fill="#fda4af" font-size="9" font-weight="bold">Sensorineural Loss</text>
  <text x="190" y="70" fill="#cbd5e1" font-size="8">- Inner ear / Auditory nerve</text>
  <text x="190" y="85" fill="#cbd5e1" font-size="8">- Hair cell death (loud noise)</text>
  <text x="190" y="100" fill="#cbd5e1" font-size="8">- Aging (presbycusis)</text>
  <text x="190" y="130" fill="#f87171" font-size="8">Usually permanent</text>
  <text x="55" y="175" fill="#38bdf8" font-size="9">Two Distinct Categories of Auditory Impairment</text>
</svg>
</div>
What distinguishes sensorineural hearing loss from conductive hearing loss?""",
     ["Sensorineural loss involves damage to sensory hair cells or the auditory nerve and is typically permanent, whereas conductive loss involves mechanical blockage in outer/middle ear and is often reversible""",
     "Conductive loss affects only the left ear while sensorineural affects only the right ear""",
     "Sensorineural loss is caused exclusively by earwax""",
     "Conductive loss allows people to hear ultrasound"],
     "A", "medium""",
     "Conductive disorders impede acoustic wave transmission to the inner ear; sensorineural disorders involve structural loss of the transducers (hair cells) or neural pathways."),

    # 80: Acoustic Reflex Mechanism
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="180" viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="180" fill="#0f172a" rx="8"/>
  <!-- Stapes bone -->
  <path d="M 120 70 L 160 60 L 160 85 Z" fill="#94a3b8"/>
  <line x1="160" y1="55" x2="160" y2="90" stroke="#94a3b8" stroke-width="3"/>
  <text x="125" y="55" fill="#94a3b8" font-size="8">Stapes</text>
  <!-- Stapedius muscle contracting -->
  <rect x="180" y="70" width="40" height="15" fill="#ef4444" rx="2"/>
  <line x1="160" y1="75" x2="180" y2="75" stroke="#ef4444" stroke-width="2"/>
  <text x="182" y="65" fill="#fca5a5" font-size="8" font-weight="bold">Stapedius Muscle</text>
  <line x1="175" y1="88" x2="210" y2="88" stroke="#facc15" stroke-width="2"/>
  <polygon points="210,85 218,88 210,91" fill="#facc15"/>
  <text x="165" y="105" fill="#facc15" font-size="8">Pulls stapes footplate back</text>
  <!-- Dampened sound wave entering inner ear -->
  <path d="M 230 65 Q 240 75 230 85" stroke="#4ade80" stroke-width="1.5" fill="none"/>
  <text x="245" y="78" fill="#4ade80" font-size="8">Dampened Wave</text>
  <text x="45" y="145" fill="#38bdf8" font-size="9">Acoustic Reflex: Muscle contracts upon loud noise (>85 dB)</text>
  <text x="45" y="165" fill="#86efac" font-size="9">Stiffens ossicular chain to protect delicate cochlear hair cells</text>
</svg>
</div>
How does the stapedius muscle in the middle ear protect the inner ear from damage when exposed to loud acoustic sounds exceeding 85 decibels?""",
     ["It contracts involuntarily to pull the stapes away from the oval window, stiffening the ossicles and dampening sound energy transfer""",
     "It closes the external ear canal like a plug""",
     "It dissolves the sound wave into water""",
     "It increases sound amplification by 50 times"],
     "A", "medium""",
     "The stapedius reflex contracts the smallest skeletal muscle in the body, dampening ossicular vibrations and shielding the fragile cochlea from acoustic overstimulation."),

    # 81: Auditory Canal Resonance
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Closed tube resonator: Ear canal (length L ~ 2.5 cm) -->
  <rect x="60" y="60" width="160" height="40" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Eardrum closed end -->
  <line x1="220" y1="60" x2="220" y2="100" stroke="#ef4444" stroke-width="3"/>
  <text x="210" y="50" fill="#f87171" font-size="8">Eardrum (Node)</text>
  <!-- Open pinna end -->
  <text x="45" y="50" fill="#38bdf8" font-size="8">Entrance (Antinode)</text>
  <!-- Standing quarter wave lambda / 4 = L -->
  <path d="M 60 60 Q 140 80 220 80" stroke="#facc15" stroke-width="2" fill="none"/>
  <path d="M 60 100 Q 140 80 220 80" stroke="#facc15" stroke-width="2" fill="none"/>
  <text x="90" y="125" fill="#fde68a" font-size="9">L \approx 2.5 cm \implies \lambda = 4L \approx 10 cm</text>
  <text x="90" y="145" fill="#4ade80" font-size="9">f = v / \lambda = 340 / 0.10 \approx 3400 Hz</text>
  <text x="45" y="175" fill="#38bdf8" font-size="9">Natural acoustic quarter-wave resonance boosts human speech frequencies</text>
</svg>
</div>
The human auditory canal acts acoustically as a quarter-wave organ pipe closed at one end (by the tympanic membrane) with length \\(L \\approx 2.5\\text{ cm}\\). At approximately which frequency range does this physical resonance amplify sound pressure at the eardrum by 10 to 15 decibels?""",
     ["Around 3,000 Hz to 3,500 Hz (critical human speech consonant frequencies)""",
     "Around 20 Hz to 50 Hz""",
     "Around 100,000 Hz""",
     "Around 5 Hz"],
     "A", "hard""",
     "A tube closed at one end resonates at fundamental wavelength \\(\\lambda = 4L = 4 \\times 0.025\\text{ m} = 0.10\\text{ m}\\). The resonant frequency is \\(f = v / \\lambda = 340 / 0.10 = 3400\\text{ Hz}\\), matching the acoustic range of human speech clarity."),

    # 82: Sound Intensity Decibel Danger Threshold
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Decibel thermometer bar -->
  <rect x="50" y="40" width="240" height="25" fill="#22c55e" rx="4"/>
  <rect x="130" y="40" width="80" height="25" fill="#f59e0b"/>
  <rect x="210" y="40" width="80" height="25" fill="#ef4444" rx="4"/>
  <!-- Scale labels -->
  <text x="48" y="32" fill="#4ade80" font-size="8">0 dB (Whisper)</text>
  <text x="120" y="32" fill="#fbbf24" font-size="8">60 dB (Normal Speech)</text>
  <text x="195" y="32" fill="#f87171" font-size="8">85 dB (Hazard Line)</text>
  <text x="260" y="32" fill="#ef4444" font-size="8">120 dB (Pain)</text>
  <!-- Hazard indicator needle -->
  <line x1="210" y1="35" x2="210" y2="75" stroke="#ffffff" stroke-width="2"/>
  <polygon points="206,75 214,75 210,82" fill="#ffffff"/>
  <text x="150" y="95" fill="#fca5a5" font-size="9" font-weight="bold">85 dB: Occupational Danger Level</text>
  <text x="50" y="140" fill="#cbd5e1" font-size="8">- 85 dB: Hair cell damage begins with prolonged exposure</text>
  <text x="50" y="155" fill="#f87171" font-size="8">- >120 dB: Acute acoustic trauma and immediate pain</text>
  <text x="50" y="175" fill="#facc15" font-size="9">Earplugs and acoustic earmuffs required in noisy workplaces</text>
</svg>
</div>
According to acoustic health standards, what is the recognized continuous sound exposure threshold above which occupational noise causes cumulative, irreversible damage to cochlear hair cells?""",
     ["85 decibels (dB)", "20 decibels (dB)", "0 decibels (dB)", "200 decibels (dB)"],
     "A", "easy""",
     "Continuous exposure to sound levels at or above 85 dB shears and destroys stereocilia on auditory hair cells over time, necessitating industrial hearing protection.")
]

def generate():
    all_qs = []
    
    # 40 Exam
    for i, item in enumerate(exam_data, start=1):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "exam", "standard", item[5]))

    # 30 Practice
    for i, item in enumerate(practice_data, start=41):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "practice", "standard", item[5]))

    # 12 Mock
    for i, item in enumerate(mock_data, start=71):
        qcode = f"{TOPIC_CODE}-OSC-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], "OSC", item[3], "mock", "foundation", item[4]))

    out_file = "scripts/ch12_topic5.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
