# scripts/generate_ch12_topic3.py
# MH-9-SCIT-12-12.3: Reflection of Sound, Echo & Reverberation
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-12-12.3"

exam_data = [
    # 1-10: Laws of Reflection of Sound & Echo Basics
    ("What fundamental laws govern the reflection of sound waves when they strike a hard surface?",
     ["The angle of incidence equals the angle of reflection (i = r), and the incident wave, normal, and reflected wave all lie in the same plane",
      "The angle of reflection is always double the angle of incidence",
      "Sound waves only reflect at 90 deg angles",
      "Sound waves do not obey reflection laws"],
     "A", "OSC", "easy",
     "Sound waves strictly follow the identical geometric laws of reflection as light: angle of incidence equals angle of reflection (i = r), and the incident ray, normal, and reflected ray are coplanar."),

    ("What type of surface acts as a good reflector of sound waves?",
     ["Hard, smooth, rigid surfaces like solid concrete walls, metal plates, and polished wood",
      "Soft, porous, cushioned fabrics like heavy drapes and velvet curtains",
      "Spongy foam and acoustic fiber tiles",
      "Loose sand and sawdust"],
     "A", "OSC", "easy",
     "Hard, dense, non-porous surfaces reflect acoustic pressure waves efficiently with minimal absorption, functioning as good sound reflectors."),

    ("What is an 'echo' in acoustics?",
     ["The distinct repetition of the original sound caused by reflection from a distant obstacle or cliff",
      "A change in pitch due to moving source",
      "The complete absorption of sound by curtains",
      "Sound moving in a vacuum"],
     "A", "OSC", "easy",
     "An echo is the acoustic repetition of a sound caused by the reflection of sound waves from a distant barrier (such as a tall building, hill, or cliff)."),

    ("What is the physiological 'persistence of hearing' duration in the human brain?",
     ["Approximately 0.1 second (1/10th of a second)",
      "Approximately 1.0 second",
      "Approximately 0.01 second",
      "Approximately 5.0 seconds"],
     "A", "OSC", "easy",
     "The sensation of a sound persists in the human auditory cortex for roughly 0.1 seconds. Any reflected sound arriving within 0.1 s blends with the original sound rather than being perceived as a distinct echo."),

    ("To hear a distinct, separate echo, what is the minimum time delay required between the emission of the original sound and the arrival of the reflected sound?",
     ["At least 0.1 second (t >= 0.1 s)",
      "At least 1.0 second",
      "At least 0.01 second",
      "At least 10 seconds"],
     "A", "OSC", "easy",
     "Because human persistence of hearing lasts 0.1 s, a reflected sound must arrive after at least 0.1 s for the brain to recognize it as a separate, distinct echo."),

    ("Assuming the speed of sound in air at 22 deg C is 344 m/s, what is the minimum distance between the sound source and reflecting surface to hear a distinct echo?",
     ["17.2 metres", "34.4 metres", "8.6 metres", "68.8 metres"],
     "A", "OSC", "easy",
     "Total round-trip path is 2d = v * t = 344 * 0.1 = 34.4 m. Therefore, the minimum one-way obstacle distance is d = 34.4 / 2 = 17.2 metres."),

    ("If the speed of sound in freezing air at 0 deg C is 331 m/s, what is the minimum distance to hear an echo?",
     ["16.55 metres", "17.2 metres", "33.1 metres", "8.27 metres"],
     "A", "OSC", "medium",
     "At 0 deg C: 2d = 331 * 0.1 = 33.1 m, giving d = 33.1 / 2 = 16.55 metres."),

    ("How does an increase in air temperature affect the minimum distance required to hear a distinct echo?",
     ["The minimum distance increases because the speed of sound increases with temperature (d = v*t / 2)",
      "The minimum distance decreases",
      "The minimum distance remains strictly 17.2 m at all temperatures",
      "Echoes cannot form in warm air"],
     "A", "OSC", "medium",
     "Because sound speed v rises with temperature, the minimum distance d = v * (0.1) / 2 increases proportionally on hot days."),

    ("Why can we hear distinct echoes in large open valleys and mountainous canyons, but NOT in small ordinary living rooms?",
     ["In a small room, the reflecting walls are much closer than 17.2 m, so reflected sound returns within 0.1 s and blends with the original sound",
      "Small rooms have no air for sound to travel",
      "Furniture completely destroys all sound waves",
      "Walls in rooms only reflect light"],
     "A", "OSC", "easy",
     "Ordinary room walls are only 3-5 meters away. Reflected sound returns in under 0.03 s, merging seamlessly with original speech rather than forming a distinct echo."),

    ("A person standing at a distance d from a cliff claps their hands and hears the echo after 1.6 seconds. If sound travels at 340 m/s, how far is the cliff?",
     ["272 metres", "544 metres", "136 metres", "680 metres"],
     "A", "OSC", "easy",
     "2d = v * t = 340 * 1.6 = 544 m. Distance to cliff d = 544 / 2 = 272 metres."),

    # 11-20: Reverberation & Acoustic Control
    ("What is 'reverberation' in an enclosed hall or auditorium?",
     ["The persistence of sound due to repeated multiple reflections from walls, ceiling, and floor after the source stops",
      "The total cancellation of sound by interference",
      "The bending of sound waves through doorway openings",
      "The change in pitch of musical instruments"],
     "A", "OSC", "easy",
     "Reverberation is the prolonged persistence of sound within an enclosed space resulting from continuous multiple reflections off boundaries until acoustic energy is absorbed."),

    ("Why is excessive reverberation highly undesirable in a lecture hall or conference auditorium?",
     ["Overlapping reflections blur successive spoken syllables, making speech garbled and unintelligible",
      "It causes walls to crack from vibration",
      "It causes listeners to lose hearing permanently",
      "It raises room temperature by 10 deg C"],
     "A", "OSC", "easy",
     "Excessive reverberation causes sound reflections from previous words to overlap with incoming words, muddying articulation so listeners cannot decipher speech."),

    ("Which acoustic treatment is applied to the walls and ceilings of movie theaters and concert halls to control reverberation?",
     ["Covering them with sound-absorbing materials like perforated acoustic fiberboard, rough plaster, and heavy draperies",
      "Painting walls with shiny, glossy white enamel paint",
      "Covering all walls with polished metal mirrors",
      "Replacing all seats with hard marble slabs"],
     "A", "OSC", "easy",
     "Porous, fiber-based acoustic panels and heavy fabrics trap and absorb sound energy through viscous frictional resistance, dampening unwanted reverberation."),

    ("Why are the ceilings of concert halls, cinemas, and auditoriums typically designed with a curved (concave) shape?",
     ["So that sound reflects uniformly across the entire hall, reaching every audience member clearly",
      "To save construction cement and steel",
      "To prevent birds from nesting on the roof",
      "To focus 100% of sound energy onto the central front row only"],
     "A", "OSC", "easy",
     "A curved ceiling acts as a parabolic/concave reflector, bouncing sound waves downward uniformly into all rows of seating, including corners under balconies."),

    ("What is a 'soundboard' installed behind the speaker on a stage in an auditorium?",
     ["A curved reflective board that reflects speaker's voice forward in a parallel distributed wave to the audience",
      "An electronic musical keyboard",
      "A wooden floor for tap dancing",
      "A thick concrete barrier that absorbs sound"],
     "A", "OSC", "easy",
     "A concave soundboard placed behind the speaker focuses and redirects sound waves forward toward the audience, amplifying speech audibility across large halls."),

    ("Why are seats in modern cinema halls upholstered with thick cushioned fabric rather than bare plastic or wood?",
     ["Cushioned fabric absorbs sound, maintaining constant room acoustics whether the auditorium is full or empty",
      "Cushions are cheaper than plastic",
      "Fabric reflects sound better than hard plastic",
      "To prevent electrostatic spark generation"],
     "A", "OSC", "easy",
     "Cushioned seats mimic the acoustic absorption of human clothing, preventing empty seats from creating excessive reverberation and echo."),

    ("Which common medical diagnostic instrument functions by the principle of multiple reflections of sound waves inside a flexible tube?",
     ["Stethoscope", "Thermometer", "Sphygmomanometer", "Otoscope"],
     "A", "OSC", "easy",
     "A doctor's stethoscope captures heart and lung sounds at the chest piece and channels sound waves through flexible rubber tubing via successive internal reflections to the earpieces."),

    ("Which device uses a cone-shaped tube to guide sound waves forward in a specific direction via multiple reflections?",
     ["Megaphone (speaking trumpet)", "Microscope", "Barometer", "Periscope"],
     "A", "OSC", "easy",
     "A megaphone uses progressive conical reflections to channel outgoing acoustic wavefronts in a focused forward beam, preventing sound from dissipating in all directions."),

    ("What is the famous acoustic phenomenon observed in the Gol Gumbaz at Vijayapura (Bijapur), Karnataka?",
     ["A central whispering gallery where a faint whisper reflects multiple times and can be heard clearly across 40 meters, echoing over 10 times",
      "A room where sound travels faster than light",
      "A room with zero sound reflection",
      "An acoustic chamber that creates musical notes automatically"],
     "A", "OSC", "easy",
     "The circular whispering gallery of Gol Gumbaz features smooth curved masonry that reflects faint whispers repeatedly along the perimeter, echoing up to 10-12 times."),

    ("A person stands between two parallel cliffs and fires a pistol. If the first echo is heard after 2 seconds and the second echo after 3 seconds, what is the distance between the two cliffs? (Speed of sound = 340 m/s)",
     ["850 metres", "1700 metres", "680 metres", "340 metres"],
     "A", "OSC", "medium",
     "Distance to cliff 1: d_1 = (340 * 2) / 2 = 340 m. Distance to cliff 2: d_2 = (340 * 3) / 2 = 510 m. Total distance between cliffs = d_1 + d_2 = 340 + 510 = 850 metres.")
]

practice_data = [
    # 21-30: Quantitative & Conceptual Practice
    ("A boy shouts in front of a tall vertical wall and hears his echo after 0.8 seconds. If sound speed in air is 340 m/s, how far is the wall?",
     ["136 metres", "272 metres", "68 metres", "340 metres"],
     "A", "OSC", "easy",
     "d = (v * t) / 2 = (340 * 0.8) / 2 = 272 / 2 = 136 metres."),

    ("An echo is heard after 3 seconds. Taking sound speed as 342 m/s, calculate the distance between source and reflecting surface.",
     ["513 metres", "1026 metres", "342 metres", "171 metres"],
     "A", "OSC", "easy",
     "d = (342 * 3) / 2 = 1026 / 2 = 513 metres."),

    ("Why does an empty newly constructed hall produce more noticeable reverberation than a fully furnished apartment?",
     ["An empty hall has bare hard concrete walls that reflect sound repeatedly, while furniture and carpets absorb sound",
      "Empty halls have higher air pressure",
      "Furnished rooms have lower temperature",
      "Empty halls have no gravity"],
     "A", "OSC", "easy",
     "Hard bare walls, ceiling, and tiled floors have high reflection coefficients. Furniture, drapes, and books introduce porous absorbing materials that quench reflections."),

    ("State whether the following statement is True or False: If a person claps at a distance of 10 metres from a flat wall in air at 22 deg C, they will hear a distinct echo.",
     ["False", "True"],
     "A", "OTF", "easy",
     "At 10 m, total round-trip distance is 20 m. Sound takes 20 / 344 = 0.058 s to return. Since 0.058 s < 0.1 s, human ears cannot perceive a separate echo."),

    ("State whether the following statement is True or False: Both light waves and sound waves obey the law that the angle of incidence equals the angle of reflection.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Reflection of sound strictly obeys i = r across reflecting surfaces."),

    ("State whether the following statement is True or False: In a stethoscope, sound travels along the tube through multiple reflections.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Heart sound waves bounce along the inner walls of the flexible acoustic tube through repeated reflections."),

    ("A ship sends a sound signal down to the sea floor and receives the echo after 1.8 seconds. If sound travels at 1530 m/s in seawater, what is the ocean depth?",
     ["1377 metres", "2754 metres", "765 metres", "1530 metres"],
     "A", "OSC", "medium",
     "d = (v * t) / 2 = (1530 * 1.8) / 2 = 2754 / 2 = 1377 metres."),

    ("What happens to sound waves when they strike porous materials like foam sponges or glass wool?",
     ["Sound energy enters microscopic air pores where friction between moving air particles and pore walls converts sound into thermal energy",
      "Sound waves turn into radio waves",
      "Sound waves reflect with double speed",
      "Sound waves freeze inside the foam"],
     "A", "OSC", "medium",
     "Acoustic dissipation occurs as oscillating air molecules experience viscous drag within porous channels, converting acoustic pressure energy into low-grade heat."),

    ("A person stands between two cliffs and claps. He hears the first echo after 1.5 s and the second echo after 2.5 s. Taking v = 340 m/s, what is the distance between the cliffs?",
     ["680 metres", "1360 metres", "340 metres", "850 metres"],
     "A", "OSC", "medium",
     "d_1 = (340 * 1.5) / 2 = 255 m. d_2 = (340 * 2.5) / 2 = 425 m. Separation = 255 + 425 = 680 metres."),

    ("In an auditorium, why is a curved soundboard positioned with the speaker standing at its focal point?",
     ["So that sound waves emanating from the focus reflect from the curved board into a uniform parallel beam towards the audience",
      "To prevent sound from reaching the front row",
      "To absorb the speaker's breathing noises",
      "To make the speaker look taller"],
     "A", "OSC", "easy",
     "Placing the sound source at the focus of a parabolic reflector converts divergent vocal waves into parallel reflected waves projected across the entire hall.")
]

# Additional 20 questions to exam_data (total 40)
extra_exam = [
    ("Why does a musical horn or trumpet have a flared, conical opening bell at its end?",
     ["The conical flare guides outgoing sound waves through progressive multiple reflections, focusing sound energy forward rather than dispersing sideways",
      "To allow the musician to hold it comfortably",
      "To collect air from the room",
      "To reduce the loudness of the instrument"],
     "A", "OSC", "easy",
     "The expanding cone matches acoustic impedance with outside air and reflects sound waves forward in a directional beam."),

    ("What is the time interval known as 'reverberation time' defined as by acoustic engineers?",
     ["The time required for sound energy density in a room to decay by 60 decibels (to one-millionth of its initial value) after the source stops",
      "The time taken to hear the first echo",
      "The duration of a musical concert",
      "The time for sound to cross a room once"],
     "A", "OSC", "medium",
     "Sabine's reverberation time (RT60) is standardly defined as the time needed for acoustic sound pressure level to drop by 60 dB below its initial steady-state level."),

    ("If the reverberation time in an auditorium is too short (less than 0.5 seconds), how does the hall sound to musical performers?",
     ["Acoustically 'dead' and dry, lacking tonal richness and warmth",
      "Excessively loud and booming",
      "Full of distinct echoes",
      "High-pitched like a whistle"],
     "A", "OSC", "medium",
     "An over-damped hall with too much sound absorption cuts off harmonic resonance prematurely, making orchestral music sound flat and lifeless."),

    ("A student stands 85 m away from a cliff. On a cold day (speed of sound = 340 m/s), how long after shouting does the student hear the echo?",
     ["0.5 seconds", "0.25 seconds", "1.0 second", "0.1 second"],
     "A", "OSC", "easy",
     "Total path 2d = 2 * 85 = 170 m. Time t = 170 / 340 = 0.5 seconds."),

    ("Assertion (A): We cannot hear an echo in a standard classroom of length 10 metres.\nReason (R): The minimum distance of a reflecting barrier to hear a distinct echo in air at room temperature is 17.2 metres.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "In a 10 m room, reflected sound returns in ~0.058 s, which is well below the 0.1 s persistence of hearing threshold."),

    ("State whether the following statement is True or False: Rough surfaces do not reflect sound waves at all.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Rough surfaces reflect sound diffusely, scattering reflected acoustic waves in various directions."),

    ("State whether the following statement is True or False: On a hot summer day at 40 deg C, the minimum distance to hear an echo is greater than on a winter day at 10 deg C.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Because speed of sound increases with temperature, the 0.1 s round-trip distance (2d = v * 0.1) is larger in hotter air."),

    ("In an experiment on reflection of sound, two hollow pipes are angled toward a smooth board. Why must a screen be placed between the two pipes?",
     ["To prevent the observer from hearing sound coming directly from the clock source through air without reflection",
      "To absorb light from the room",
      "To keep the table balanced",
      "To cool the pipes"],
     "A", "OSC", "easy",
     "A central partition blocks direct line-of-sight sound, ensuring that only sound reflecting off the board at angle r = i enters the listener's ear pipe."),

    ("What is the speed of sound in air if a man hears the echo of his gunshot reflected from a mountain 510 m away after 3.0 seconds?",
     ["340 m/s", "170 m/s", "510 m/s", "680 m/s"],
     "A", "OSC", "easy",
     "v = 2d / t = (2 * 510) / 3.0 = 1020 / 3.0 = 340 m/s."),

    ("Which property of sound waves is directly demonstrated by the functioning of a megaphone, speaking tube, and stethoscope?",
     ["Successive multiple reflections of sound waves along guiding boundaries",
      "Refraction through air layers",
      "Polarization of sound",
      "Total absorption of acoustic energy"],
     "A", "OSC", "easy",
     "All three devices use successive reflections from interior walls to channel sound energy forward along a confined path without radial loss."),

    ("Why are acoustic panels with perforated wooden slats and mineral wool backing installed in cinema theatres?",
     ["To absorb unwanted reflected sound waves and prevent echo overlaps",
      "To reflect light towards the cinema screen",
      "To prevent sound from entering the projector",
      "To increase reverberation time to several minutes"],
     "A", "OSC", "easy",
     "Acoustic panels provide high sound absorption across conversational and low frequencies, preventing reflections from disturbing audience clarity."),

    ("A radar station uses radio waves, but a bathymetric echo-sounder must use acoustic waves. Why cannot electromagnetic waves easily measure ocean depth?",
     ["Seawater absorbs and attenuates high-frequency electromagnetic waves rapidly within meters, whereas acoustic compression waves propagate kilometers",
      "Radio waves travel too fast to be detected",
      "Electromagnetic waves bend at 90 degrees in saltwater",
      "Ocean floor absorbs 100% of all radio waves instantly"],
     "A", "OSC", "medium",
     "Water has high electrical conductivity which rapidly dissipates radio waves, whereas mechanical compression sound waves propagate efficiently over vast marine depths."),

    ("When sound reflects from a rigid wall back into the air, which parameter of the wave remains unchanged?",
     ["Frequency, speed, and wavelength",
      "Amplitude only",
      "Direction of propagation only",
      "Phase only"],
     "A", "OSC", "medium",
     "Because reflection occurs within the identical medium (air at same temperature), wave speed v and frequency f remain constant, hence wavelength lambda = v/f is also preserved."),

    ("A girl shouts in a canyon and hears an echo after 2.4 seconds. If air temperature is such that sound travels at 345 m/s, how far away is the opposite wall?",
     ["414 metres", "828 metres", "207 metres", "690 metres"],
     "A", "OSC", "easy",
     "Total path is 2d = v * t = 345 * 2.4 = 828 m. Distance d = 828 / 2 = 414 metres."),

    ("In an auditorium with a flat parallel ceiling, sound often experiences rapid buzzing repetitions between the floor and ceiling. What is this phenomenon called?",
     ["Flutter echo", "Diffraction grating", "Acoustic levitation", "Total internal reflection"],
     "A", "OSC", "medium",
     "Flutter echoes occur when sound bounces back and forth repeatedly between hard parallel reflective surfaces, creating a rapid buzzing flutter effect."),

    ("State whether the following statement is True or False: Heavy acoustic draperies hung along auditorium walls increase the reverberation time.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Heavy draperies absorb acoustic energy, reducing reverberation time rather than increasing it."),

    ("State whether the following statement is True or False: Sound reflections obey the law that the incident sound ray, the normal to the reflecting surface, and the reflected sound ray all lie in the same plane.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Like light, sound reflection is strictly coplanar: incident ray, normal, and reflected ray lie in a single plane."),

    ("A student fires a starting gun at an athletic track located 510 m away from a grandstand. How long after firing will the echo return if sound speed is 340 m/s?",
     ["3.0 seconds", "1.5 seconds", "0.75 seconds", "6.0 seconds"],
     "A", "OSC", "easy",
     "Round-trip distance 2d = 2 * 510 = 1020 m. Time taken t = 1020 / 340 = 3.0 seconds."),

    ("Why are soundboards in large concert halls shaped with a concave curvature rather than a flat plane?",
     ["A concave curvature reflects and focuses sound rays toward distant balcony audiences to provide even distribution",
      "Concave boards trap sound waves so no one can hear mistakes",
      "A curved board is lighter than a flat board",
      "Flat boards do not reflect sound waves at all"],
     "A", "OSC", "easy",
     "Concave acoustic soundboards direct reflected wave fronts evenly across the seating auditorium to eliminate acoustic dead zones."),

    ("What is the primary role of acoustic baffles hung vertically from gymnasium ceilings?",
     ["To absorb sound energy and suppress reverberation in large reverberant spaces",
      "To provide decorative lighting",
      "To protect the ceiling from stray balls",
      "To increase echo intensity"],
     "A", "OSC", "easy",
     "Suspended acoustic baffles intercept bouncing sound waves, converting sound vibrations into heat through fiber friction and reducing echo persistence.")
]

# Additional 20 questions to practice_data (total 30)
extra_practice = [
    ("A mountaineer fires a flare near a vertical rock face and hears the echo after 1.2 seconds. Taking sound speed as 340 m/s, what is the distance to the rock face?",
     ["204 metres", "408 metres", "102 metres", "340 metres"],
     "A", "OSC", "easy",
     "d = (340 * 1.2) / 2 = 204 metres."),

    ("Why are cinema hall floors covered with heavy carpets rather than polished marble tiles?",
     ["Carpets absorb sound reflections from floor surfaces, preventing flutter echoes and reverberation",
      "Carpets are required by electrical fire codes",
      "Carpets make the projector brighter",
      "Tiles absorb too much sound"],
     "A", "OSC", "easy",
     "Hard tiles reflect sound vigorously, causing excessive reverberation; soft carpets absorb acoustic energy."),

    ("A ship anchored in fog sounds its horn and receives an echo from a nearby iceberg after 4.0 seconds. If sound speed in air is 330 m/s, how far is the iceberg?",
     ["660 metres", "1320 metres", "330 metres", "990 metres"],
     "A", "OSC", "easy",
     "d = (330 * 4.0) / 2 = 1320 / 2 = 660 metres."),

    ("State whether the following statement is True or False: Reverberation and echo refer to the exact same acoustic phenomenon with identical time delays.",
     ["False", "True"],
     "A", "OTF", "easy",
     "An echo is a distinct separate repetition returning after 0.1 s; reverberation is a continuous persistence due to rapid overlapping reflections within 0.1 s."),

    ("State whether the following statement is True or False: If you whisper along the wall of a circular whispering gallery, sound is guided along the curved perimeter by multiple reflections.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Whispering galleries guide sound waves along concave perimeter walls through successive reflections with minimal dispersion."),

    ("An echo sounder on a trawler emits an acoustic pulse and receives the seabed reflection after 0.6 seconds. Taking sound speed in water as 1500 m/s, what is the sea depth?",
     ["450 metres", "900 metres", "225 metres", "1500 metres"],
     "A", "OSC", "easy",
     "d = (1500 * 0.6) / 2 = 900 / 2 = 450 metres."),

    ("Why does speech sound hollow and booming inside an empty bathroom with glossy tiled walls?",
     ["Multiple reflections from hard glazed tiles create persistent reverberation",
      "Bathrooms have no air pressure",
      "Water pipes absorb low frequencies",
      "Tiles change sound into ultrasound"],
     "A", "OSC", "easy",
     "Ceramic tiles have near-zero sound absorption, bouncing acoustic waves repeatedly to produce high reverberation."),

    ("A driver honks her horn 170 m away from a cliff on a day when sound travels at 340 m/s. How long after honking does she hear the echo?",
     ["1.0 second", "0.5 seconds", "2.0 seconds", "0.1 second"],
     "A", "OSC", "easy",
     "t = 2d / v = (2 * 170) / 340 = 340 / 340 = 1.0 second."),

    ("What happens to sound reflections in an open football stadium compared to an enclosed concert hall?",
     ["In an open stadium, sound waves radiate outward into the open sky with very few reflections, preventing reverberation",
      "Open stadiums have infinite reverberation",
      "Sound cannot travel in open stadiums",
      "Stadium grass reflects 100% of sound"],
     "A", "OSC", "easy",
     "Without walls or ceilings to trap and reflect acoustic energy, sound radiates away freely without reverberation."),

    ("Which part of an ancient Greek amphitheater was designed as a curved acoustic surface to project actors' voices to the topmost row of seats?",
     ["The semi-circular tiered stone seating rows (cavea) and the orchestra backing wall (skene)",
      "The wooden entrance gates",
      "The bronze shields on the perimeter",
      "The canvas sun roof"],
     "A", "OSC", "medium",
     "The tiered concave stone structure acted as a natural acoustic filter and reflector, reflecting voice fundamentals while suppressing low-frequency crowd noise."),

    ("A bat emits an ultrasonic pulse and receives the echo from a flying moth in 0.04 seconds. If sound travels at 340 m/s in air, how far away is the moth?",
     ["6.8 metres", "13.6 metres", "3.4 metres", "27.2 metres"],
     "A", "OSC", "easy",
     "2d = v * t = 340 * 0.04 = 13.6 m. Moth distance d = 13.6 / 2 = 6.8 metres."),

    ("Why do empty rooms echo much more prominently before moving furniture in?",
     ["Bare hard plaster walls reflect almost all incident sound energy, whereas furniture, rugs, and curtains absorb sound",
      "Empty rooms have higher gravitational fields",
      "Furniture adds sound waves to the room",
      "Plaster walls generate extra sound spontaneously"],
     "A", "OSC", "easy",
     "Bare masonry has an absorption coefficient near 0.02, reflecting 98% of acoustic energy. Furniture introduces soft porous surfaces with high absorption."),

    ("An acoustic technician measures that sound reflections in an auditorium take 1.2 seconds to decay to inaudibility. What is this parameter called?",
     ["Reverberation time", "Echo distance", "Wave period", "Acoustic impedance"],
     "A", "OSC", "easy",
     "Reverberation time is the duration required for sound pressure reflections within an enclosure to attenuate to negligible levels."),

    ("If you clap your hands in front of a flat concrete wall 34 metres away, how many seconds after the clap will you hear the echo? (Assume v = 340 m/s)",
     ["0.20 seconds", "0.10 seconds", "0.05 seconds", "0.40 seconds"],
     "A", "OSC", "easy",
     "Round-trip distance is 2 * 34 = 68 m. Time t = 68 / 340 = 0.20 seconds."),

    ("State whether the following statement is True or False: If a wall is positioned 10 metres from a speaker, the reflected sound produces a separate, distinct echo in normal air.",
     ["False", "True"],
     "A", "OTF", "easy",
     "At 10 m, reflected sound arrives in 20 / 340 = 0.059 s, which is well below the 0.1 s persistence of hearing threshold."),

    ("State whether the following statement is True or False: Stethoscopes utilize repeated reflections along the inner surface of rubber tubing to channel faint heartbeats to an ear tip.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Multiple internal reflections prevent radial dispersion, guiding acoustic energy efficiently to the listener's ears."),

    ("What happens to the minimum echo distance if you move from sea level air (v = 340 m/s) into warm desert air where v = 360 m/s?",
     ["The minimum echo distance increases from 17 m to 18 m",
      "The minimum echo distance decreases to 15 m",
      "The minimum distance remains strictly 17.2 m",
      "Echoes are impossible in warm air"],
     "A", "OSC", "medium",
     "Minimum distance d = v * 0.1 / 2. At v = 360 m/s, d = 360 * 0.1 / 2 = 18.0 metres, which is larger than at sea level."),

    ("Why are ceilings of concert halls curved rather than flat?",
     ["Curved ceilings reflect sound waves uniformly to all parts of the auditorium, reaching every seat evenly",
      "Curved ceilings allow birds to fly freely",
      "Flat ceilings collapse under sound pressure",
      "Curved ceilings reflect light better"],
     "A", "OSC", "easy",
     "A curved ceiling acts like an acoustic reflector, distributing sound wavefronts evenly across the hall and preventing acoustic dead spots."),

    ("In an echo experiment, a student stands 102 m away from a tall school building. If the echo arrives 0.6 seconds after shouting, what is the calculated speed of sound?",
     ["340 m/s", "170 m/s", "510 m/s", "680 m/s"],
     "A", "OSC", "easy",
     "v = 2d / t = (2 * 102) / 0.6 = 204 / 0.6 = 340 m/s."),

    ("Why can a person hear sound around the corner of an open doorway even when out of sight?",
     ["Sound waves have long wavelengths comparable to doorway dimensions and readily diffract and reflect around corners",
      "Sound waves pass through concrete doors effortlessly",
      "The person's ears emit gravitational rays",
      "Air particles are pushed out like bullets"],
     "A", "OSC", "easy",
     "Acoustic wavelengths in the audible range (a few tens of centimeters to a few meters) readily bend around edges (diffraction) and bounce from walls.")
]

mock_data = [
    # 71: Reflection of Sound Law Experiment Vector Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Smooth reflective wooden/metal board -->
  <line x1="40" y1="40" x2="300" y2="40" stroke="#38bdf8" stroke-width="4"/>
  <text x="110" y="30" fill="#38bdf8" font-size="10" font-weight="bold">Reflecting Hard Board</text>
  <!-- Normal line dashed -->
  <line x1="170" y1="40" x2="170" y2="160" stroke="#facc15" stroke-width="1.8" stroke-dasharray="4,4"/>
  <text x="175" y="155" fill="#facc15" font-size="9">Normal (N)</text>
  <!-- Screen between tubes -->
  <line x1="170" y1="40" x2="170" y2="120" stroke="#94a3b8" stroke-width="3"/>
  <text x="175" y="110" fill="#94a3b8" font-size="8">Partition Screen</text>
  <!-- Incident Pipe with ticking clock -->
  <line x1="70" y1="140" x2="170" y2="40" stroke="#4ade80" stroke-width="3"/>
  <circle cx="65" cy="145" r="8" fill="#fbbf24"/>
  <text x="35" y="165" fill="#fbbf24" font-size="9">Ticking Clock</text>
  <!-- Reflected Pipe to Ear -->
  <line x1="170" y1="40" x2="270" y2="140" stroke="#f87171" stroke-width="3"/>
  <text x="260" y="165" fill="#f87171" font-size="9">Listener's Ear</text>
  <!-- Angle arcs -->
  <text x="145" y="70" fill="#4ade80" font-size="10" font-weight="bold">i</text>
  <text x="185" y="70" fill="#f87171" font-size="10" font-weight="bold">r</text>
  <text x="70" y="180" fill="#cbd5e1" font-size="9.5">Law of Reflection of Sound: i = r confirmed by maximum tick audibility</text>
</svg>
</div>
In the standard laboratory apparatus for demonstrating the reflection of sound shown above, at what angle of the listener's pipe (r) is the ticking of the clock heard with maximum loudness?""",
     ["When angle of reflection r exactly equals angle of incidence i (r = i)""",
     "When angle r is 90 deg""",
     "When angle r is 0 deg""",
     "When angle r is double the angle i"],
     "A", "OSC", "easy""",
     "Sound reflection strictly follows the law of reflection: maximum acoustic energy enters the listening tube precisely when angle of reflection r equals angle of incidence i."),

    # 72: Echo 17.2m Threshold Vector Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Person source -->
  <circle cx="50" cy="90" r="10" fill="#38bdf8"/>
  <line x1="50" y1="100" x2="50" y2="145" stroke="#38bdf8" stroke-width="3"/>
  <text x="35" y="160" fill="#38bdf8" font-size="9" font-weight="bold">Observer</text>
  <!-- Tall Cliff -->
  <rect x="290" y="30" width="30" height="130" fill="#64748b"/>
  <text x="285" y="25" fill="#94a3b8" font-size="9" font-weight="bold">Cliff</text>
  <!-- Sound paths -->
  <line x1="60" y1="85" x2="290" y2="85" stroke="#4ade80" stroke-width="2"/>
  <polygon points="175,82 185,85 175,88" fill="#4ade80"/>
  <text x="140" y="78" fill="#4ade80" font-size="9">Forward Sound</text>
  <line x1="290" y1="105" x2="60" y2="105" stroke="#f87171" stroke-width="2" stroke-dasharray="4,3"/>
  <polygon points="175,102 165,105 175,108" fill="#f87171"/>
  <text x="140" y="120" fill="#f87171" font-size="9">Reflected Echo</text>
  <!-- Distance bar -->
  <line x1="50" y1="140" x2="290" y2="140" stroke="#facc15" stroke-width="2"/>
  <text x="120" y="155" fill="#facc15" font-size="10" font-weight="bold">d_min = 17.2 metres (at 22^{\circ}C)</text>
  <text x="60" y="178" fill="#cbd5e1" font-size="9">Persistence of Hearing = 0.1 s → Round trip 2d = 344 · 0.1 = 34.4 m</text>
</svg>
</div>
According to the echo threshold diagram, why is the minimum obstacle distance for hearing a distinct echo in air at 22 deg C exactly 17.2 metres?""",
     ["Because the brain retains sound for 0.1 s; traveling at 344 m/s, sound must cover a round-trip of 34.4 m (34.4 / 2 = 17.2 m)""",
     "Because sound waves cannot travel farther than 17.2 m in air""",
     "Because human vocal cords only produce waves 17.2 m long""",
     "Because the cliff absorbs all sound returning within 17.2 m"],
     "A", "OSC", "easy""",
     "Human persistence of hearing is 0.1 seconds. In 0.1 s, sound traveling at 344 m/s covers 2d = 34.4 m. For the reflected sound to be perceived as a distinct echo, one-way distance must be at least 34.4 / 2 = 17.2 m."),

    # 73: Curved Ceiling Auditorium Acoustic Focus
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Curved ceiling (concave) -->
  <path d="M 40,50 Q 170,15 300,50" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <text x="110" y="25" fill="#38bdf8" font-size="10" font-weight="bold">Curved Acoustic Ceiling</text>
  <!-- Speaker on stage -->
  <circle cx="60" cy="130" r="8" fill="#facc15"/>
  <text x="45" y="150" fill="#facc15" font-size="9">Speaker</text>
  <!-- Reflected sound rays covering all seats -->
  <line x1="60" y1="130" x2="100" y2="40" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="100" y1="40" x2="130" y2="140" stroke="#f87171" stroke-width="1.5"/>
  <line x1="60" y1="130" x2="180" y2="33" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="180" y1="33" x2="220" y2="140" stroke="#f87171" stroke-width="1.5"/>
  <line x1="60" y1="130" x2="260" y2="42" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="260" y1="42" x2="290" y2="140" stroke="#f87171" stroke-width="1.5"/>
  <!-- Audience seats -->
  <rect x="120" y="140" width="180" height="12" fill="#475569" rx="2"/>
  <text x="160" y="152" fill="#cbd5e1" font-size="9">Audience Seating Rows</text>
  <text x="60" y="175" fill="#cbd5e1" font-size="9.5">Curved ceiling reflects sound uniformly across every row</text>
</svg>
</div>
How does a curved concave ceiling improve the listening experience in an auditorium, as illustrated in the ray trace?""",
     ["It reflects sound waves downward uniformly to all seating rows, ensuring even acoustic loudness throughout the hall""",
     "It absorbs 100% of the speaker's sound""",
     "It speeds up the tempo of musical instruments""",
     "It prevents sound from leaving the stage"],
     "A", "OSC", "easy""",
     "The curved ceiling acts as a reflector that spreads sound waves downward across all audience sections, preventing dead spots under balconies and at the rear."),

    # 74: Stethoscope Multiple Reflections
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Chestpiece -->
  <circle cx="50" cy="95" r="18" fill="#64748b" stroke="#38bdf8" stroke-width="2"/>
  <text x="35" y="130" fill="#38bdf8" font-size="9">Chestpiece</text>
  <!-- Rubber tube with zigzag reflection ray inside -->
  <rect x="68" y="85" width="200" height="20" rx="3" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
  <!-- Multiple reflection ray (Yellow) -->
  <polyline points="68,95 100,86 130,104 160,86 190,104 220,86 250,104 268,95" fill="none" stroke="#facc15" stroke-width="2"/>
  <!-- Earpieces -->
  <path d="M 268,95 L 300,70" stroke="#94a3b8" stroke-width="3"/>
  <path d="M 268,95 L 300,120" stroke="#94a3b8" stroke-width="3"/>
  <circle cx="300" cy="70" r="5" fill="#f87171"/>
  <circle cx="300" cy="120" r="5" fill="#f87171"/>
  <text x="270" y="145" fill="#f87171" font-size="9">Doctor's Ears</text>
  <text x="45" y="45" fill="#facc15" font-size="10" font-weight="bold">Stethoscope: Sound Guided by Multiple Internal Reflections</text>
  <text x="50" y="175" fill="#cbd5e1" font-size="9.5">Acoustic waves reflect off tube walls without radial loss of energy</text>
</svg>
</div>
Which acoustic principle enables a doctor to hear faint heartbeat sounds through a stethoscope tubing without significant volume loss?""",
     ["Successive multiple reflections of sound waves along the inner surface of the flexible tube""",
     "Electromagnetic radio amplification""",
     "Ultrasound frequency upconversion""",
     "Sound traveling through vacuum channels"],
     "A", "OSC", "easy""",
     "Heartbeat sound waves enter the chest piece and reflect repeatedly from the internal walls of the tube, confining the acoustic energy within the tube until it reaches the doctor's ears."),

    # 75: Megaphone Directional Sound Beam
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Megaphone body -->
  <polygon points="50,85 50,105 180,145 180,45" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  <rect x="35" y="80" width="15" height="30" fill="#64748b"/>
  <text x="25" y="125" fill="#cbd5e1" font-size="8">Mouthpiece</text>
  <!-- Internal multiple reflection ray -->
  <polyline points="50,95 90,62 130,128 170,55 180,80" fill="none" stroke="#facc15" stroke-width="2"/>
  <!-- Forward sound beam spreading out -->
  <path d="M 180,45 L 300,20 L 300,170 L 180,145 Z" fill="#38bdf8" fill-opacity="0.1"/>
  <line x1="180" y1="95" x2="300" y2="95" stroke="#4ade80" stroke-width="2"/>
  <polygon points="280,91 295,95 280,99" fill="#4ade80"/>
  <text x="200" y="90" fill="#4ade80" font-size="9.5" font-weight="bold">Directed Forward</text>
  <text x="50" y="175" fill="#cbd5e1" font-size="9.5">Megaphone uses progressive reflections to beam sound in one direction</text>
</svg>
</div>
Why does speaking through a megaphone make a person's voice travel significantly farther in one direction?""",
     ["The conical tube reflects divergent sound waves repeatedly, channeling acoustic energy forward into a concentrated beam rather than spreading in all directions""",
     "It adds electrical battery energy to the voice""",
     "It increases the voice frequency into ultrasound""",
     "It absorbs surrounding air molecules"],
     "A", "OSC", "easy""",
     "The horn's conical walls prevent omnidirectional dissipation of vocal sound by reflecting waves forward along a guided path, concentrating sound intensity into a directional beam."),

    # 76: Whispering Gallery (Gol Gumbaz) Architecture
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Circular Dome Outline -->
  <ellipse cx="170" cy="100" rx="120" ry="60" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <text x="110" y="30" fill="#38bdf8" font-size="10" font-weight="bold">Gol Gumbaz Whispering Gallery</text>
  <!-- Whisperer -->
  <circle cx="55" cy="100" r="7" fill="#facc15"/>
  <text x="35" y="90" fill="#facc15" font-size="8">Whisperer</text>
  <!-- Listener across 40m -->
  <circle cx="285" cy="100" r="7" fill="#4ade80"/>
  <text x="265" y="90" fill="#4ade80" font-size="8">Listener</text>
  <!-- Creeping waves reflecting along boundary -->
  <path d="M 55,100 Q 80,45 110,42 T 170,40 T 230,42 T 285,100" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3"/>
  <text x="90" y="125" fill="#f43f5e" font-size="9.5">Whisper creeps along circular wall via repeated reflections</text>
  <text x="60" y="175" fill="#cbd5e1" font-size="9.5">Echoes repeat 10+ times across the 44-metre masonry dome</text>
</svg>
</div>
In the famous whispering gallery of Gol Gumbaz at Vijayapura, how can a faint whisper be heard clearly across the 44-meter diameter dome?""",
     ["Sound waves creep along the curved concave perimeter masonry wall through successive grazing reflections with very low energy loss""",
     "The dome contains acoustic electronic speakers""",
     "The dome is in a complete vacuum""",
     "Sound waves travel through underground water pipes"],
     "A", "OSC", "easy""",
     "The circular concave masonry guides sound waves along its perimeter boundary through repeated small-angle grazing reflections, preserving acoustic energy across large distances."),

    # 77: Reverberation Time Decay Curve
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Axes -->
  <line x1="40" y1="150" x2="300" y2="150" stroke="#94a3b8" stroke-width="2"/>
  <text x="280" y="165" fill="#94a3b8" font-size="9">Time (s)</text>
  <line x1="40" y1="150" x2="40" y2="25" stroke="#94a3b8" stroke-width="2"/>
  <text x="20" y="30" fill="#94a3b8" font-size="9">Sound Level (dB)</text>
  <!-- Decay curve 1: Bare hall (High reverberation) -->
  <path d="M 40,35 Q 120,45 180,70 T 290,145" fill="none" stroke="#f87171" stroke-width="2.5"/>
  <text x="180" y="60" fill="#f87171" font-size="9">Bare Hall (RT &gt; 3.0 s, Blurred)</text>
  <!-- Decay curve 2: Acoustically treated hall -->
  <path d="M 40,35 Q 70,80 110,120 T 140,150" fill="none" stroke="#4ade80" stroke-width="2.5"/>
  <text x="100" y="105" fill="#4ade80" font-size="9">Treated Hall (RT \approx 1.2 s, Crisp)</text>
  <text x="50" y="180" fill="#cbd5e1" font-size="9.5">Acoustic panels reduce RT60 to optimal speech intelligibility window</text>
</svg>
</div>
Comparing the acoustic decay curves in the graph, why is an optimal reverberation time (around 1.0 to 1.5 seconds) preferred for a multi-purpose auditorium?""",
     ["It provides sufficient musical warmth and fullness without blurring spoken speech articulation""",
     "It makes the hall completely silent at all times""",
     "It allows only low-frequency bass to be heard""",
     "It produces 100 distinct echoes"],
     "A", "OSC", "easy""",
     "An optimal reverberation time (~1-1.5 s) maintains musical resonance and voice fullness while allowing each spoken syllable to decay before the next begins, preserving intelligibility."),

    # 78: Soundboard Reflection Focus
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Concave soundboard behind stage -->
  <path d="M 70,30 A 100,100 0 0,0 70,160" fill="none" stroke="#38bdf8" stroke-width="5"/>
  <text x="30" y="20" fill="#38bdf8" font-size="9">Soundboard</text>
  <!-- Speaker at focus -->
  <circle cx="120" cy="95" r="7" fill="#facc15"/>
  <text x="110" y="80" fill="#facc15" font-size="9">Speaker at Focus F</text>
  <!-- Parallel reflected rays -->
  <line x1="120" y1="95" x2="66" y2="45" stroke="#4ade80" stroke-width="1.8"/>
  <line x1="66" y1="45" x2="300" y2="45" stroke="#4ade80" stroke-width="1.8"/>
  <line x1="120" y1="95" x2="60" y2="95" stroke="#4ade80" stroke-width="1.8"/>
  <line x1="60" y1="95" x2="300" y2="95" stroke="#4ade80" stroke-width="1.8"/>
  <line x1="120" y1="95" x2="66" y2="145" stroke="#4ade80" stroke-width="1.8"/>
  <line x1="66" y1="145" x2="300" y2="145" stroke="#4ade80" stroke-width="1.8"/>
  <text x="170" y="110" fill="#4ade80" font-size="9.5">Parallel Reflected Waves to Hall</text>
  <text x="50" y="175" fill="#cbd5e1" font-size="9.5">Soundboard directs speaker's acoustic energy into parallel forward wavefronts</text>
</svg>
</div>
In an auditorium, why is a parabolic soundboard placed behind the speaker with the speaker standing at its focus F?""",
     ["Rays originating from the focus reflect from the curved board into parallel rays projected straight towards the audience""",
     "It prevents the speaker from walking off stage""",
     "It absorbs 100% of the speaker's sound""",
     "It acts as a decorative mirror"],
     "A", "OSC", "easy""",
     "Placing the speaker at the focal point of a concave soundboard directs acoustic reflections forward in a parallel beam, preventing sound from dispersing wastefully into backstage walls."),

    # 79: Double Echo Between Two Parallel Cliffs
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Cliff 1 (Left) -->
  <rect x="25" y="30" width="20" height="120" fill="#64748b"/>
  <text x="15" y="25" fill="#94a3b8" font-size="8">Cliff 1</text>
  <!-- Person -->
  <circle cx="120" cy="90" r="7" fill="#38bdf8"/>
  <line x1="120" y1="97" x2="120" y2="135" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="80" fill="#38bdf8" font-size="8">Observer</text>
  <!-- Cliff 2 (Right) -->
  <rect x="295" y="30" width="20" height="120" fill="#64748b"/>
  <text x="285" y="25" fill="#94a3b8" font-size="8">Cliff 2</text>
  <!-- Distances -->
  <line x1="45" y1="110" x2="120" y2="110" stroke="#facc15" stroke-width="1.5"/>
  <text x="65" y="125" fill="#facc15" font-size="8.5">d_1 = 340 m</text>
  <line x1="120" y1="110" x2="295" y2="110" stroke="#4ade80" stroke-width="1.5"/>
  <text x="180" y="125" fill="#4ade80" font-size="8.5">d_2 = 510 m</text>
  <text x="40" y="150" fill="#f87171" font-size="9">Echo 1: t_1 = 2·340/340 = 2.0 s  |  Echo 2: t_2 = 2·510/340 = 3.0 s</text>
  <text x="50" y="175" fill="#cbd5e1" font-size="9.5">Total separation between cliffs = d_1 + d_2 = 340 + 510 = 850 metres</text>
</svg>
</div>
A man standing between two cliffs fires a gun and hears the first echo after 2.0 s and the second echo after 3.0 s. Taking sound speed as 340 m/s, what is the distance between the two cliffs?""",
     ["850 metres", "1700 metres", "680 metres", "340 metres"],
     "A", "OSC", "medium""",
     "Distance to nearer cliff: d_1 = (340 * 2) / 2 = 340 m. Distance to farther cliff: d_2 = (340 * 3) / 2 = 510 m. Distance between cliffs = d_1 + d_2 = 340 + 510 = 850 metres."),

    # 80: Acoustic Tile Porous Absorption
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="140" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="45" y="55" fill="#facc15" font-size="11" font-weight="bold">Sound Absorption in Porous Acoustic Panels:</text>
  <text x="45" y="85" fill="#e2e8f0" font-size="10.5">• Sound wave enters microscopic open air pores</text>
  <text x="45" y="110" fill="#e2e8f0" font-size="10.5">• Viscous drag &amp; friction between air &amp; fiber walls</text>
  <text x="45" y="135" fill="#4ade80" font-size="11" font-weight="bold">Acoustic kinetic energy → Minute thermal heat</text>
</svg>
</div>
How do porous acoustic ceiling panels extinguish sound reflections to control reverberation in cinema halls?""",
     ["Sound enters microscopic pores where friction against fiber walls dissipates acoustic vibrational energy into heat""",
     "They absorb sound using chemical battery cells""",
     "They reflect sound back into the microphone""",
     "They convert sound waves into radio broadcast signals"],
     "A", "OSC", "easy""",
     "Acoustic absorption converts mechanical sound energy into tiny amounts of heat as vibrating air molecules rub against the intricate fibers and pores of acoustic tiles."),

    # 81: Musical Trumpet Bell Flare
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Trumpet tube and flared bell -->
  <rect x="30" y="90" width="140" height="10" fill="#fbbf24"/>
  <path d="M 170,90 Q 230,85 270,45 L 270,145 Q 230,105 170,100 Z" fill="#fbbf24"/>
  <!-- Sound waves reflecting inside bell -->
  <path d="M 270,55 A 40,40 0 0,1 270,135" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <path d="M 290,45 A 60,60 0 0,1 290,145" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <text x="45" y="45" fill="#facc15" font-size="11" font-weight="bold">Flared Bell of Brass Instruments</text>
  <text x="40" y="175" fill="#cbd5e1" font-size="9.5">Gradual acoustic impedance matching guides sound waves forward</text>
</svg>
</div>
Why are brass musical instruments (such as trumpets and trombones) shaped with a flared bell at their opening?""",
     ["The expanding bell matches acoustic impedance with outside air, channeling sound outward through multiple reflections""",
     "To collect air from the room""",
     "To mute the high frequencies""",
     "To prevent moisture from escaping"],
     "A", "OSC", "easy""",
     "The flared bell smoothly transitions acoustic impedance from the narrow tube to open space, reflecting internal waves smoothly to project clear, powerful notes."),

    # 82: Master Topic 3 Synthesis Summary
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="20" y="20" width="300" height="150" rx="8" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="35" y="45" fill="#facc15" font-size="11" font-weight="bold">Chapter 12 Topic 3 Summary:</text>
  <text x="35" y="70" fill="#38bdf8" font-size="10">• Laws of Reflection: i = r (Smooth hard surfaces reflect)</text>
  <text x="35" y="95" fill="#4ade80" font-size="10">• Echo: Persistence = 0.1 s → d_min = 17.2 m at 22^{\circ}C</text>
  <text x="35" y="120" fill="#ec4899" font-size="10">• Reverberation: Repeated reflections; controlled by acoustic panels</text>
  <text x="35" y="145" fill="#a78bfa" font-size="10">• Applications: Stethoscope, Megaphone, Soundboard, Whispering Gallery</text>
</svg>
</div>
Which core condition is essential for human ears to distinguish an echo from original sound?""",
     ["The reflected sound wave must return after a minimum time delay of 0.1 seconds (d >= 17.2 m at 22 deg C)""",
     "The sound must travel faster than light""",
     "The frequency must be above 20 kHz""",
     "The room must be completely full of water"],
     "A", "OSC", "easy""",
     "Because persistence of hearing lasts 0.1 seconds, any reflected sound returning within 0.1 s merges with the original sound; an echo strictly requires t >= 0.1 s (d >= 17.2 m at 22 deg C).")
]

def generate():
    all_qs = []
    
    # 40 Exam (20 from exam_data + 20 from extra_exam)
    full_exam = exam_data + extra_exam
    for i, item in enumerate(full_exam, start=1):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "exam", "standard", item[5]))

    # 30 Practice (10 from practice_data + 20 from extra_practice)
    full_practice = practice_data + extra_practice
    for i, item in enumerate(full_practice, start=41):
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
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "mock", "foundation", item[5]))

    out_file = "scripts/ch12_topic3.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
