# scripts/generate_ch12_topic1.py
# MH-9-SCIT-12-12.1: Sound Waves: Velocity of Sound Formula (v = \nu * \lambda)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-12-12.1"

exam_data = [
    # 1-10: Nature of Sound Waves & Fundamental Wave Quantities
    ("What type of wave is sound when it propagates through air or other fluids?",
     ["Mechanical longitudinal wave",
      "Electromagnetic transverse wave",
      "Transverse surface wave only",
      "Stationary electromagnetic wave"],
     "A", "OSC", "easy",
     "Sound is a mechanical longitudinal wave requiring a material medium to propagate, where medium particles oscillate parallel to the direction of wave energy propagation."),

    ("What are the alternating high-density and low-density regions produced during the propagation of a sound wave through air called?",
     ["Compressions and Rarefactions",
      "Crests and Troughs",
      "Nodes and Antinodes",
      "Poles and Foci"],
     "A", "OSC", "easy",
     "Compressions are regions of high pressure and high particle density, while rarefactions are regions of low pressure and low density created as vibrating particles oscillate back and forth."),

    ("What is the distance between any two consecutive compressions or two consecutive rarefactions of a sound wave called?",
     ["Wavelength (\\lambda)",
      "Time period (T)",
      "Wave amplitude (A)",
      "Frequency (\\nu)"],
     "A", "OSC", "easy",
     "The wavelength (\\lambda) is defined as the physical distance over which the wave shape repeats, specifically the distance between two successive compressions or rarefactions."),

    ("What is the SI unit of wavelength?",
     ["Metre (m)", "Hertz (Hz)", "Second (s)", "Metre per second (m/s)"],
     "A", "OSC", "easy",
     "Because wavelength measures physical length, its SI standard unit is the metre (m)."),

    ("What is defined as the number of complete wave cycles or oscillations passing a given point per second?",
     ["Frequency (\\nu or f)",
      "Time period (T)",
      "Wave velocity (v)",
      "Wavelength (\\lambda)"],
     "A", "OSC", "easy",
     "Frequency (\\nu) denotes the number of oscillations or cycles executed by the source and transmitted through the medium in one second."),

    ("What is the SI unit of frequency, named in honor of the German physicist Heinrich Hertz?",
     ["Hertz (Hz)", "Pascal (Pa)", "Decibel (dB)", "Joule (J)"],
     "A", "OSC", "easy",
     "The SI unit of frequency is Hertz (Hz), where 1 Hz equals 1 complete vibration or cycle per second (1 s^{-1})."),

    ("What is the time taken by a medium particle to complete one full oscillation called?",
     ["Time period (T)",
      "Frequency (\\nu)",
      "Acoustic phase",
      "Wavelength (\\lambda)"],
     "A", "OSC", "easy",
     "The time period (T) is the duration required for one complete wave cycle to pass a fixed point (T = 1 / \\nu)."),

    ("What is the fundamental mathematical relationship connecting wave velocity (v), frequency (\\nu), and wavelength (\\lambda)?",
     ["v = \\nu * \\lambda",
      "v = \\nu / \\lambda",
      "v = \\lambda / \\nu",
      "v = \\nu^2 * \\lambda"],
     "A", "OSC", "easy",
     "Since wave velocity is distance divided by time, v = \\lambda / T. Substituting frequency \\nu = 1/T yields the fundamental wave equation v = \\nu * \\lambda."),

    ("If a tuning fork produces a sound wave of frequency 512 Hz traveling at 340 m/s in air, what is its wavelength?",
     ["0.664 m", "1.506 m", "0.332 m", "174.08 m"],
     "A", "OSC", "medium",
     "Using \\lambda = v / \\nu: \\lambda = 340 / 512 \approx 0.664 m."),

    ("A sound wave has a wavelength of 0.85 m and travels at a speed of 340 m/s in air. What is its frequency?",
     ["400 Hz", "289 Hz", "200 Hz", "500 Hz"],
     "A", "OSC", "easy",
     "Frequency \\nu = v / \\lambda = 340 / 0.85 = 400 Hz."),

    # 11-20: Speed in Different States of Matter & Temperature Effects
    ("How does the speed of sound generally compare across the three states of matter (solids, liquids, and gases)?",
     ["Speed in solids > Speed in liquids > Speed in gases",
      "Speed in gases > Speed in liquids > Speed in solids",
      "Speed in liquids > Speed in solids > Speed in gases",
      "Speed is identical across all states of matter"],
     "A", "OSC", "easy",
     "Because solids have the highest elastic modulus and closely packed particles, sound travels fastest in solids (e.g. steel ~5900 m/s), intermediate in liquids (water ~1500 m/s), and slowest in gases (air ~340 m/s)."),

    ("What is the approximate speed of sound in dry air at 0^{\\circ}C?",
     ["331 m/s", "344 m/s", "1500 m/s", "3000 m/s"],
     "A", "OSC", "easy",
     "In dry air at standard atmospheric pressure and 0^{\\circ}C, the speed of sound is approximately 331 m/s (increasing by ~0.6 m/s for every 1^{\\circ}C rise)."),

    ("What is the speed of sound in air at normal room temperature (22^{\\circ}C to 25^{\\circ}C)?",
     ["Approximately 344 m/s to 346 m/s",
      "Approximately 1500 m/s",
      "Approximately 331 m/s",
      "Approximately 5000 m/s"],
     "A", "OSC", "easy",
     "At standard ambient room temperature (~22^{\\circ}C), sound travels in air at roughly 344 m/s to 346 m/s."),

    ("What is the approximate speed of sound in distilled water at 25^{\\circ}C?",
     ["Approximately 1498 m/s (nearly 1500 m/s)",
      "Approximately 344 m/s",
      "Approximately 5900 m/s",
      "Approximately 331 m/s"],
     "A", "OSC", "easy",
     "Sound travels roughly 4.3 times faster in water (~1500 m/s) than in atmospheric air due to higher bulk modulus."),

    ("What is the approximate speed of sound in solid steel or iron at room temperature?",
     ["Approximately 5000 m/s to 5900 m/s",
      "Approximately 344 m/s",
      "Approximately 1500 m/s",
      "Approximately 1000 m/s"],
     "A", "OSC", "easy",
     "Because steel has high elasticity and density, longitudinal acoustic vibrations propagate at nearly 5000 m/s to 5900 m/s."),

    ("How does an increase in the temperature of a gas affect the velocity of sound traveling through it?",
     ["Velocity increases directly proportional to the square root of absolute temperature (v \\propto \\sqrt{T})",
      "Velocity decreases as temperature rises",
      "Velocity remains completely unchanged",
      "Velocity drops to zero at high temperatures"],
     "A", "OSC", "medium",
     "In ideal gases, v = \\sqrt{\\gamma R T / M}. As absolute temperature T increases, thermal molecular motion accelerates sound energy transfer, so v \\propto \\sqrt{T}."),

    ("By approximately how much does the speed of sound in air increase for every 1^{\\circ}C rise in ambient temperature?",
     ["0.61 m/s per ^{\\circ}C",
      "10 m/s per ^{\\circ}C",
      "1.5 m/s per ^{\\circ}C",
      "0.1 m/s per ^{\\circ}C"],
     "A", "OSC", "medium",
     "Near room temperature, the rate of increase of sound velocity with temperature in air is approximately 0.61 m/s for each 1^{\\circ}C increment: v_T \\approx 331 + 0.61 T."),

    ("How does the velocity of sound in a gas vary with the molecular weight (M) of the gas molecules at constant temperature?",
     ["Velocity is inversely proportional to the square root of molecular weight (v \\propto 1 / \\sqrt{M})",
      "Velocity is directly proportional to molecular weight",
      "Velocity is independent of molecular weight",
      "Velocity is proportional to M^2"],
     "A", "OSC", "medium",
     "From v = \\sqrt{\\gamma R T / M}, lighter gas molecules (such as hydrogen) propagate sound much faster than heavy gases (such as oxygen) at the same temperature."),

    ("Comparing sound speeds in hydrogen gas (M = 2) and oxygen gas (M = 32) at the same temperature, how many times faster does sound travel in hydrogen?",
     ["4 times faster in hydrogen (\\sqrt{32/2} = \\sqrt{16} = 4)",
      "16 times faster in hydrogen",
      "2 times faster in hydrogen",
      "Both have identical speed"],
     "A", "OSC", "medium",
     "Velocity ratio v_{H2} / v_{O2} = \\sqrt{M_{O2} / M_{H2}} = \\sqrt{32 / 2} = \\sqrt{16} = 4. Sound travels 4 times faster in hydrogen (~1284 m/s) than in oxygen (~320 m/s)."),

    ("How does a change in atmospheric air pressure alone affect the speed of sound at a strictly constant temperature?",
     ["Pressure has no effect on sound speed if temperature is held constant",
      "Speed doubles when pressure doubles",
      "Speed is halved when pressure doubles",
      "Sound stops completely at high pressure"],
     "A", "OSC", "medium",
     "According to Boyle's law, as pressure P increases at constant temperature, density \\rho increases in the exact same proportion, keeping the ratio P/\\rho constant. Therefore, sound velocity is independent of pressure variations at constant temperature."),

    # 21-30: Amplitude, Loudness, Pitch & Propagation Media
    ("Can sound travel through an absolute vacuum (such as outer space)?",
     ["No, sound requires a material medium with inertia and elasticity to propagate",
      "Yes, sound travels faster in a vacuum than in air",
      "Yes, sound travels at the speed of light in a vacuum",
      "Only if the frequency is above 100 kHz"],
     "A", "OSC", "easy",
     "Because sound relies on mechanical collisions between particles to transmit wave energy, it cannot travel through a vacuum, as demonstrated by the classic bell jar experiment."),

    ("Which characteristic property of a sound wave determines its perceived loudness or volume?",
     ["The amplitude of vibration (Loudness \\propto Amplitude^2)",
      "The frequency of vibration",
      "The wavelength of the wave",
      "The direction of propagation"],
     "A", "OSC", "easy",
     "Loudness is proportional to the square of wave amplitude. A larger physical vibration imparts more acoustic energy, which human ears perceive as louder sound."),

    ("Which characteristic property of a sound wave determines its perceived pitch or shrillness?",
     ["The frequency of vibration (\\nu)",
      "The amplitude of vibration",
      "The speed of sound",
      "The humidity of air"],
     "A", "OSC", "easy",
     "Pitch is directly governed by frequency: higher frequency produces a high-pitched, shrill sound (like a whistle or child's voice), while lower frequency produces a low-pitched, bass sound (like a drum or thunder)."),

    ("What is 'timbre' or quality of a sound wave?",
     ["The characteristic tone quality that allows the ear to distinguish between two sounds of the same pitch and loudness produced by different instruments",
      "The volume measured in decibels",
      "The velocity of sound in solid wood",
      "The time period of the fundamental harmonic"],
     "A", "OSC", "medium",
     "Timbre is determined by the waveform and harmonic overtones, allowing human listeners to instantly tell a violin note from a flute playing the exact same frequency and loudness."),

    ("A lightning flash is seen instantly, but thunder is heard 3 seconds later. If the speed of sound is 340 m/s, how far away did the lightning strike?",
     ["1020 m (1.02 km)", "340 m", "680 m", "170 m"],
     "A", "OSC", "easy",
     "Because light travels at 3 * 10^8 m/s (virtually instantaneous over terrestrial distances), distance d = v * t = 340 m/s * 3 s = 1020 m (1.02 km)."),

    ("An acoustic sonar transmitter in a lake sends a sound pulse to the lake bed and detects the echo after 0.4 seconds. If sound travels at 1500 m/s in water, what is the depth of the lake?",
     ["300 m", "600 m", "150 m", "750 m"],
     "A", "OSC", "medium",
     "The sound travels down and reflects back, so total path is 2d = v * t. Thus d = (v * t) / 2 = (1500 * 0.4) / 2 = 600 / 2 = 300 m."),

    ("A sound wave of frequency 1000 Hz has a velocity of 340 m/s in air. How long will it take to travel a distance of 1.7 km?",
     ["5 seconds", "1.7 seconds", "0.5 seconds", "10 seconds"],
     "A", "OSC", "easy",
     "Distance d = 1.7 km = 1700 m. Time taken t = d / v = 1700 / 340 = 5 seconds."),

    ("What is the wavelength of the 1000 Hz sound wave in the previous question traveling at 340 m/s?",
     ["0.34 m (34 cm)", "3.4 m", "0.17 m", "340 m"],
     "A", "OSC", "easy",
     "Wavelength \\lambda = v / \\nu = 340 / 1000 = 0.34 m (34 cm)."),

    ("How does the presence of high humidity (water vapor) in atmospheric air affect the velocity of sound?",
     ["Velocity of sound increases slightly in humid air because moist air is less dense than dry air",
      "Velocity of sound decreases in humid air",
      "Velocity of sound is completely unaffected by humidity",
      "Sound cannot travel in humid air"],
     "A", "OSC", "medium",
     "Water vapor (molecular weight 18) is lighter than dry air (average molecular weight ~29). Humid air has lower density than dry air at the same temperature and pressure, so sound travels slightly faster in humid air."),

    ("Assertion (A): Astronauts on the surface of the Moon cannot talk directly to each other through the air without radio equipment.\nReason (R): The Moon has no atmosphere, and sound waves cannot travel through a vacuum.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "Sound is a mechanical pressure wave requiring matter particles to oscillate. In the vacuum of the lunar surface, sound cannot propagate, requiring radio (electromagnetic) transmitters.")
]

practice_data = [
    # 31-40: Quantitative Practice
    ("A sound source produces 40 compressions and 40 rarefactions in 0.5 seconds. What is the frequency of the wave?",
     ["80 Hz", "40 Hz", "20 Hz", "160 Hz"],
     "A", "OSC", "medium",
     "One complete wave cycle consists of one compression and one rarefaction. 40 complete cycles occur in 0.5 seconds. Frequency \\nu = 40 / 0.5 = 80 Hz."),

    ("What is the time period of the sound wave in the previous question with frequency 80 Hz?",
     ["0.0125 s (12.5 ms)", "0.025 s", "0.5 s", "0.08 s"],
     "A", "OSC", "easy",
     "Time period T = 1 / \\nu = 1 / 80 = 0.0125 seconds."),

    ("If a sound wave travels 680 m in 2 seconds in air, what is its velocity?",
     ["340 m/s", "1360 m/s", "170 m/s", "680 m/s"],
     "A", "OSC", "easy",
     "Velocity v = distance / time = 680 m / 2 s = 340 m/s."),

    ("If the wavelength of a sound wave is doubled while its velocity remains constant, what happens to its frequency?",
     ["The frequency is halved (\\nu / 2)",
      "The frequency is doubled (2\\nu)",
      "The frequency remains unchanged",
      "The frequency quadruples"],
     "A", "OSC", "easy",
     "From v = \\nu * \\lambda, \\nu = v / \\lambda. If \\lambda doubles at constant speed, frequency \\nu is cut in half."),

    ("A tuning fork labeled 256 Hz vibrates in air where the speed of sound is 332 m/s. How far does the sound travel while the fork completes 64 vibrations?",
     ["83 m", "166 m", "41.5 m", "332 m"],
     "A", "OSC", "medium",
     "Time for 64 vibrations: t = 64 / 256 = 0.25 s. Distance traveled d = v * t = 332 * 0.25 = 83 m."),

    ("State whether the following statement is True or False: Sound travels faster in cold air at 0^{\\circ}C than in warm air at 30^{\\circ}C.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Velocity of sound increases with temperature (v \\propto \\sqrt{T}); sound travels faster in warm air (~349 m/s at 30^{\\circ}C vs ~331 m/s at 0^{\\circ}C)."),

    ("State whether the following statement is True or False: In a longitudinal wave, particles of the medium vibrate perpendicular to the direction of wave travel.",
     ["False", "True"],
     "A", "OTF", "easy",
     "In longitudinal waves, particles vibrate parallel (along the line) of wave propagation; perpendicular vibration characterizes transverse waves."),

    ("State whether the following statement is True or False: The velocity of sound in granite rock is significantly higher than in air.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Granite has high mechanical elasticity, allowing sound waves to propagate at ~6000 m/s compared to only ~340 m/s in air."),

    ("A person hears the sound of an axe striking a tree 0.75 seconds after seeing the blow land. If the speed of sound in air is 340 m/s, how far is the person from the tree?",
     ["255 m", "170 m", "340 m", "510 m"],
     "A", "OSC", "easy",
     "Distance d = v * t = 340 m/s * 0.75 s = 255 m."),

    ("What is the ratio of the speed of sound in air (~340 m/s) to the speed of light in vacuum (~3 * 10^8 m/s)?",
     ["Light travels nearly one million times faster than sound in air",
      "Sound travels faster than light",
      "Both travel at exactly equal speeds",
      "Light is only 10 times faster than sound"],
     "A", "OSC", "easy",
     "Speed of light (3 * 10^8 m/s) is roughly 8.8 * 10^5 times faster than sound in air, explaining why visual flashes are seen long before sonic booms or thunder.")
]

# Additional 10 questions to exam_data (31-40)
extra_exam = [
    ("Which parameter of a sound wave remains strictly constant when it transitions from air into water?",
     ["Frequency (\\nu)", "Wavelength (\\lambda)", "Wave speed (v)", "Wave amplitude (A)"],
     "A", "OSC", "medium",
     "Frequency is determined solely by the vibrating source and does not change across media. Speed increases in water, causing wavelength to increase proportionally (v = \\nu \\lambda)."),

    ("When sound enters water from air, its speed increases from 340 m/s to 1500 m/s. What happens to its wavelength?",
     ["Wavelength increases by approximately 4.41 times",
      "Wavelength decreases by 4.41 times",
      "Wavelength remains exactly identical",
      "Wavelength drops to zero"],
     "A", "OSC", "medium",
     "Since frequency \\nu is constant, \\lambda_{water} / \\lambda_{air} = v_{water} / v_{air} = 1500 / 340 \approx 4.41. The wavelength stretches in the denser elastic medium."),

    ("What happens to sound propagation in air if all air molecules are completely removed with a vacuum pump?",
     ["Sound transmission drops to zero as vacuum cannot transmit mechanical vibrations",
      "Sound becomes 10 times louder",
      "Sound changes into high-frequency radio waves",
      "Sound speed accelerates to light speed"],
     "A", "OSC", "easy",
     "Without matter particles to collide and carry compressions, mechanical sound waves cease to propagate."),

    ("What is the graphical representation of a sound wave displaying pressure variation against distance called?",
     ["Pressure-distance waveform graph",
      "Magnetic hysteresis loop",
      "Vector phase circle",
      "Diffraction fringes"],
     "A", "OSC", "easy",
     "A pressure-distance waveform plots the acoustic pressure variation relative to atmospheric equilibrium, showing crests at compressions and troughs at rarefactions."),

    ("What is the distance between a compression and its immediately adjacent rarefaction in a sound wave of wavelength \\lambda?",
     ["\\lambda / 2 (half of the wavelength)",
      "\\lambda",
      "2\\lambda",
      "\\lambda / 4"],
     "A", "OSC", "medium",
     "A full wavelength spans two consecutive compressions. The distance between a compression peak and the adjacent rarefaction trough is half a wavelength (\\lambda / 2)."),

    ("Assertion (A): On a hot summer day, sound travels faster in air than on a cold winter day.\nReason (R): The speed of sound in a gas is directly proportional to the square root of its absolute temperature.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "Higher temperatures energize gas molecules, accelerating acoustic energy transfer according to v \\propto \\sqrt{T}."),

    ("State whether the following statement is True or False: Sound waves can propagate through solids, liquids, and gases, but not through empty space.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Sound is a mechanical wave requiring a material medium; it propagates through all three states of matter but cannot cross empty vacuum."),

    ("State whether the following statement is True or False: The pitch of a woman's voice is generally higher than that of a man because her vocal cords vibrate at a higher frequency.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Shorter, thinner vocal cords vibrate with higher fundamental frequency, producing a higher pitch."),

    ("A bat emits an ultrasound chirp of frequency 40 kHz. If sound travels at 340 m/s in air, what is the wavelength of the chirp?",
     ["8.5 mm (0.0085 m)", "85 cm", "0.85 m", "1.36 m"],
     "A", "OSC", "medium",
     "\\lambda = v / \\nu = 340 / 40000 = 0.0085 m = 8.5 mm."),

    ("If a siren has a frequency of 680 Hz and sound speed is 340 m/s, what is the distance between two consecutive compressions?",
     ["0.5 m (50 cm)", "1.0 m", "2.0 m", "0.25 m"],
     "A", "OSC", "easy",
     "The distance between consecutive compressions is the wavelength: \\lambda = v / \\nu = 340 / 680 = 0.5 m (50 cm).")
]

# Additional 20 questions to practice_data (total 30)
extra_practice = [
    ("A sound wave in air has a frequency of 2 kHz and a wavelength of 17 cm. How long will it take to travel 1.02 km?",
     ["3 seconds", "1.5 seconds", "6 seconds", "0.5 seconds"],
     "A", "OSC", "medium",
     "Velocity v = \\nu * \\lambda = 2000 Hz * 0.17 m = 340 m/s. Distance d = 1020 m. Time t = d / v = 1020 / 340 = 3 seconds."),

    ("What is the time period of a musical tuning fork vibrating at 200 Hz?",
     ["0.005 s (5 ms)", "0.05 s", "0.02 s", "0.002 s"],
     "A", "OSC", "easy",
     "T = 1 / \\nu = 1 / 200 = 0.005 seconds (5 ms)."),

    ("If the speed of sound in steel is 5000 m/s and in air is 340 m/s, a hammer blow to a long steel rail produces two sounds at the other end. Why?",
     ["Sound travels through the steel rail first and through the surrounding air second",
      "The hammer strikes twice due to recoil",
      "Steel generates two separate frequencies",
      "Sound echoes inside the hammer"],
     "A", "OSC", "easy",
     "Sound propagates through solid steel rail ~15 times faster than through air, so the solid-transmitted pulse arrives noticeably earlier than the airborne wave."),

    ("A person taps a 1000 m steel rail. How long does the sound take to reach an observer through the rail (v_{steel} = 5000 m/s) versus through air (v_{air} = 340 m/s)?",
     ["0.2 s through steel, and 2.94 s through air",
      "1.0 s through steel, and 1.0 s through air",
      "2.0 s through steel, and 0.5 s through air",
      "0.05 s through steel, and 10 s through air"],
     "A", "OSC", "medium",
     "Time through steel = 1000 / 5000 = 0.2 s. Time through air = 1000 / 340 \approx 2.94 s."),

    ("State whether the following statement is True or False: When a sound wave travels through air, the air molecules themselves are transported bodily across kilometers of distance.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Matter is not transported; air molecules only oscillate locally about their mean equilibrium positions, transferring energy from particle to particle."),

    ("State whether the following statement is True or False: Sound travels faster in helium gas than in atmospheric nitrogen gas at the same temperature.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Helium has a much lower molar mass (M = 4) than nitrogen (M = 28); because v \\propto 1 / \\sqrt{M}, sound travels faster in helium."),

    ("What happens to a person's voice when they speak after inhaling helium gas?",
     ["Their voice sounds cartoonishly high-pitched because the higher speed of sound in helium shifts resonant vocal tract frequencies upward",
      "Their voice turns into a deep bass roar",
      "Their vocal cords stop vibrating",
      "Their voice volume drops to zero"],
     "A", "OSC", "medium",
     "Sound travels roughly 3 times faster in low-density helium (~965 m/s). This increases resonant formant frequencies in the throat and mouth, creating a high-pitched timber."),

    ("If 25 complete sound waves are produced in 0.05 seconds, what is the frequency of the sound source?",
     ["500 Hz", "250 Hz", "1000 Hz", "125 Hz"],
     "A", "OSC", "easy",
     "Frequency \\nu = 25 / 0.05 = 500 Hz."),

    ("What is the wavelength of a sound wave if consecutive compressions are separated by 68 cm?",
     ["0.68 m", "1.36 m", "0.34 m", "6.8 m"],
     "A", "OSC", "easy",
     "By definition, the distance between two consecutive compressions is the wavelength: 68 cm = 0.68 m."),

    ("If a loudspeaker diaphragm moves back and forth with greater force, which property of the emitted sound wave increases?",
     ["The amplitude of the sound wave, increasing loudness",
      "The speed of sound in air",
      "The fundamental frequency",
      "The atmospheric pressure of the room"],
     "A", "OSC", "easy",
     "Greater physical excursion of the cone creates higher pressure peaks in compressions, raising the wave amplitude and perceived sound loudness."),

    # 10 more to complete 30 practice
    ("A sound wave has a frequency of 600 Hz and a speed of 360 m/s. What is the distance between a compression and the next rarefaction?",
     ["0.3 m (30 cm)", "0.6 m", "1.2 m", "0.15 m"],
     "A", "OSC", "medium",
     "Wavelength \\lambda = v / \\nu = 360 / 600 = 0.6 m. Distance between compression and adjacent rarefaction is \\lambda / 2 = 0.6 / 2 = 0.3 m (30 cm)."),

    ("How long does it take for a sound wave of wavelength 0.5 m and frequency 680 Hz to travel 1.7 km?",
     ["5 seconds", "10 seconds", "2.5 seconds", "1.7 seconds"],
     "A", "OSC", "easy",
     "Velocity v = \\nu * \\lambda = 680 * 0.5 = 340 m/s. Time t = 1700 m / 340 m/s = 5 seconds."),

    ("In an experiment, sound takes 1.2 seconds to travel down a metal tube and back. If the tube is 3000 m long, what is the speed of sound in the metal?",
     ["5000 m/s", "2500 m/s", "3000 m/s", "6000 m/s"],
     "A", "OSC", "medium",
     "Total round-trip distance is 2 * 3000 m = 6000 m. Velocity v = 6000 m / 1.2 s = 5000 m/s."),

    ("State whether the following statement is True or False: Frequency of sound is independent of the distance from the source.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Frequency depends strictly on the vibrating source and does not change as the sound travels away through the medium."),

    ("State whether the following statement is True or False: Amplitude of a sound wave decreases as it spreads outward from a point source.",
     ["True", "False"],
     "A", "OTF", "easy",
     "As the wave expands over spherical wavefronts, acoustic energy spreads over larger surface areas, causing amplitude and loudness to diminish with distance."),

    ("What is the ratio of wavelength of sound in water (v = 1500 m/s) to that in air (v = 340 m/s) for the same source frequency?",
     ["1500 / 340 \approx 4.41", "340 / 1500 \approx 0.23", "1.0", "15.0"],
     "A", "OSC", "easy",
     "Since frequency is constant, \\lambda_{water} / \\lambda_{air} = v_{water} / v_{air} = 1500 / 340 \approx 4.41."),

    ("Which property of the medium determines how fast compressions and rarefactions recover their original positions during wave travel?",
     ["Elasticity and inertia (density) of the medium",
      "Transparency of the medium",
      "Color of the medium",
      "Electrical resistivity"],
     "A", "OSC", "easy",
     "Wave speed is governed by Newton-Laplace relation: v = \\sqrt{Elasticity / Density}."),

    ("A child counts 4 seconds between seeing a fireworks shell explode and hearing the bang. Taking sound speed as 340 m/s, how far away was the firework?",
     ["1360 m (1.36 km)", "680 m", "340 m", "2720 m"],
     "A", "OSC", "easy",
     "Distance d = v * t = 340 * 4 = 1360 m."),

    ("If the frequency of a guitar string vibration is 440 Hz (standard concert pitch A4), what is its period of oscillation?",
     ["0.00227 seconds (2.27 ms)", "0.00454 seconds", "0.044 seconds", "0.001 seconds"],
     "A", "OSC", "easy",
     "T = 1 / 440 \approx 0.00227 s."),

    ("What is the acoustic effect called when sound waves pass from one medium into another of different density and change speed?",
     ["Refraction of sound", "Total reflection", "Doppler compression", "Photoacoustic emission"],
     "A", "OSC", "easy",
     "When sound crosses into a medium with different propagation speed, wave bends according to Snell's law, a phenomenon called refraction.")
]

mock_data = [
    # 71: Longitudinal Wave Compressions and Rarefactions Vector Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <text x="30" y="25" fill="#38bdf8" font-size="11" font-weight="bold">Longitudinal Sound Wave in Air</text>
  <!-- Particles representation -->
  <!-- Compression 1 -->
  <g fill="#f43f5e">
    <circle cx="50" cy="65" r="3"/><circle cx="55" cy="65" r="3"/><circle cx="60" cy="65" r="3"/><circle cx="65" cy="65" r="3"/>
    <circle cx="48" cy="85" r="3"/><circle cx="54" cy="85" r="3"/><circle cx="58" cy="85" r="3"/><circle cx="64" cy="85" r="3"/>
    <circle cx="52" cy="105" r="3"/><circle cx="56" cy="105" r="3"/><circle cx="62" cy="105" r="3"/><circle cx="66" cy="105" r="3"/>
  </g>
  <text x="45" y="125" fill="#f43f5e" font-size="9" font-weight="bold">Compression (C)</text>
  <!-- Rarefaction 1 -->
  <g fill="#38bdf8">
    <circle cx="110" cy="65" r="2.5"/><circle cx="130" cy="85" r="2.5"/><circle cx="115" cy="105" r="2.5"/>
  </g>
  <text x="105" y="125" fill="#38bdf8" font-size="9" font-weight="bold">Rarefaction (R)</text>
  <!-- Compression 2 -->
  <g fill="#f43f5e">
    <circle cx="180" cy="65" r="3"/><circle cx="185" cy="65" r="3"/><circle cx="190" cy="65" r="3"/><circle cx="195" cy="65" r="3"/>
    <circle cx="178" cy="85" r="3"/><circle cx="184" cy="85" r="3"/><circle cx="188" cy="85" r="3"/><circle cx="194" cy="85" r="3"/>
    <circle cx="182" cy="105" r="3"/><circle cx="186" cy="105" r="3"/><circle cx="192" cy="105" r="3"/><circle cx="196" cy="105" r="3"/>
  </g>
  <text x="175" y="125" fill="#f43f5e" font-size="9" font-weight="bold">Compression (C)</text>
  <!-- Rarefaction 2 -->
  <g fill="#38bdf8">
    <circle cx="240" cy="65" r="2.5"/><circle cx="260" cy="85" r="2.5"/><circle cx="245" cy="105" r="2.5"/>
  </g>
  <text x="235" y="125" fill="#38bdf8" font-size="9" font-weight="bold">Rarefaction (R)</text>
  <!-- Wavelength arrow -->
  <line x1="57" y1="145" x2="187" y2="145" stroke="#facc15" stroke-width="2"/>
  <polygon points="63,142 55,145 63,148" fill="#facc15"/>
  <polygon points="181,142 189,145 181,148" fill="#facc15"/>
  <text x="105" y="160" fill="#facc15" font-size="10" font-weight="bold">Wavelength (\\lambda)</text>
  <text x="60" y="180" fill="#cbd5e1" font-size="9.5">Distance between two consecutive compressions = \\lambda</text>
</svg>
</div>
In the diagram of a longitudinal sound wave propagating in air, what physical property distinguishes a Compression (C) region from a Rarefaction (R) region?""",
     ["Compressions are regions of high particle density and high pressure; Rarefactions are regions of low density and low pressure""",
     "Compressions have higher temperature than rarefactions""",
     "Particles in compressions move perpendicular to the wave""",
     "Rarefactions block light while compressions transmit light"],
     "A", "OSC", "easy""",
     "As air particles oscillate back and forth parallel to the wave direction, they crowd together to form high-pressure compressions and spread apart to create low-pressure rarefactions."),

    # 72: Pressure-Distance Waveform Sine Representation
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="30" y1="95" x2="310" y2="95" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="300" y="85" fill="#94a3b8" font-size="10">Distance (x)</text>
  <line x1="40" y1="20" x2="40" y2="170" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="45" y="30" fill="#94a3b8" font-size="10">Pressure (P)</text>
  <!-- Sine wave -->
  <path d="M 40,95 Q 75,35 110,95 T 180,95 T 250,95 T 320,95" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <circle cx="75" cy="40" r="4" fill="#f43f5e"/>
  <text x="65" y="30" fill="#f43f5e" font-size="9" font-weight="bold">Crest = Compression</text>
  <circle cx="145" cy="150" r="4" fill="#a855f7"/>
  <text x="135" y="165" fill="#a855f7" font-size="9" font-weight="bold">Trough = Rarefaction</text>
  <!-- Wavelength marker -->
  <line x1="75" y1="95" x2="215" y2="95" stroke="#facc15" stroke-width="2"/>
  <text x="135" y="85" fill="#facc15" font-size="10" font-weight="bold">\\lambda</text>
  <!-- Amplitude marker -->
  <line x1="75" y1="40" x2="75" y2="95" stroke="#4ade80" stroke-width="1.5"/>
  <text x="80" y="65" fill="#4ade80" font-size="9">Amplitude A</text>
</svg>
</div>
When a longitudinal sound wave is graphically represented as a pressure-distance waveform as shown, what do the crests and troughs correspond to in the actual gas medium?""",
     ["Crests correspond to compressions (maximum pressure), and troughs correspond to rarefactions (minimum pressure)""",
     "Crests correspond to rarefactions, and troughs correspond to compressions""",
     "Crests represent sound speed, troughs represent sound volume""",
     "Crests represent musical pitch, troughs represent noise"],
     "A", "OSC", "easy""",
     "Plotting density or acoustic pressure against propagation distance transforms compressions into positive crest peaks and rarefactions into negative trough valleys."),

    # 73: Wave Formula v = nu * lambda
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="140" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="45" y="55" fill="#facc15" font-size="12" font-weight="bold">Universal Acoustic Wave Equation:</text>
  <text x="45" y="85" fill="#38bdf8" font-size="13" font-weight="bold">v = \\nu · \\lambda  =  \\lambda / T</text>
  <text x="45" y="115" fill="#e2e8f0" font-size="10">v = Wave velocity in medium (m/s)</text>
  <text x="45" y="133" fill="#e2e8f0" font-size="10">\\nu = Frequency in Hertz (Hz = 1/s)</text>
  <text x="45" y="151" fill="#e2e8f0" font-size="10">\\lambda = Wavelength in metres (m)</text>
</svg>
</div>
A musical sound wave has a frequency of 500 Hz and travels at 350 m/s in air. According to the wave equation displayed above, what is the wavelength of the sound wave?""",
     ["0.70 m (70 cm)", "1.75 m", "0.35 m", "175 m"],
     "A", "OSC", "easy""",
     "From v = \\nu * \\lambda, wavelength is \\lambda = v / \\nu = 350 / 500 = 0.70 m (70 cm)."),

    # 74: Speed in Solids vs Liquids vs Gases Bar Chart
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <text x="25" y="25" fill="#facc15" font-size="11" font-weight="bold">Speed of Sound across States of Matter (m/s)</text>
  <!-- Bar 1: Air -->
  <rect x="30" y="45" width="34" height="20" fill="#f87171" rx="3"/>
  <text x="70" y="60" fill="#f87171" font-size="10">Air (Gas): ~340 m/s</text>
  <!-- Bar 2: Water -->
  <rect x="30" y="80" width="150" height="20" fill="#38bdf8" rx="3"/>
  <text x="185" y="95" fill="#38bdf8" font-size="10">Water (Liquid): ~1500 m/s</text>
  <!-- Bar 3: Steel -->
  <rect x="30" y="115" width="280" height="20" fill="#4ade80" rx="3"/>
  <text x="150" y="130" fill="#0f172a" font-size="9.5" font-weight="bold">Steel (Solid): ~5900 m/s</text>
  <text x="50" y="170" fill="#cbd5e1" font-size="10">Solids transmit sound fastest due to high elastic modulus</text>
</svg>
</div>
Why does sound travel roughly 17 times faster in solid steel than in atmospheric air, as illustrated in the velocity chart?""",
     ["Because solids possess much higher elasticity and closely bonded atoms that transmit vibrational forces rapidly""",
     "Because steel is hotter than air""",
     "Because sound waves change into light waves in steel""",
     "Because air molecules absorb 90% of sound energy"],
     "A", "OSC", "easy""",
     "Wave speed depends directly on elastic modulus (v = \\sqrt{E / \\rho}). Solids have immense tensile and bulk elasticity compared to gases, transferring mechanical disturbance far faster."),

    # 75: Temperature Dependence v vs sqrt(T)
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="140" rx="8" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="45" y="55" fill="#facc15" font-size="11" font-weight="bold">Temperature Effect on Sound Speed:</text>
  <text x="45" y="85" fill="#4ade80" font-size="12" font-weight="bold">v \\propto \\sqrt{T}  (T in Kelvin)</text>
  <text x="45" y="115" fill="#e2e8f0" font-size="10">v_T \\approx 331 + 0.61 · T_c (m/s)</text>
  <text x="45" y="145" fill="#38bdf8" font-size="10">At 0^{\circ}C: v = 331 m/s  |  At 20^{\circ}C: v \approx 343 m/s</text>
</svg>
</div>
According to the temperature relationship formula displayed, what is the speed of sound in air at a temperature of 25^{\\circ}C?""",
     ["Approximately 346.25 m/s", "331 m/s", "356 m/s", "320 m/s"],
     "A", "OSC", "medium""",
     "Using the linear approximation v = 331 + 0.61 * 25 = 331 + 15.25 = 346.25 m/s."),

    # 76: Molecular Weight Dependence (H2 vs O2)
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="140" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="45" y="50" fill="#facc15" font-size="11" font-weight="bold">Molecular Weight Invariant (v \\propto 1/\\sqrt{M}):</text>
  <text x="45" y="80" fill="#38bdf8" font-size="10.5">Hydrogen (H_2, M = 2): v \approx 1284 m/s</text>
  <text x="45" y="105" fill="#f87171" font-size="10.5">Oxygen (O_2, M = 32): v \approx 320 m/s</text>
  <text x="45" y="135" fill="#4ade80" font-size="11" font-weight="bold">Ratio: v_H / v_O = \\sqrt{32 / 2} = \\sqrt{16} = 4</text>
</svg>
</div>
Why does sound travel 4 times faster in hydrogen gas than in oxygen gas at identical temperature and pressure?""",
     ["Because hydrogen molecules are 16 times lighter, vibrating and transferring kinetic momentum 4 times faster (v \\propto 1/\\sqrt{M})""",
     "Because hydrogen is flammable""",
     "Because oxygen absorbs all sound waves""",
     "Because hydrogen atoms have negative charge"],
     "A", "OSC", "medium""",
     "In lighter gases with lower molecular weight M, molecular thermal velocities are higher, transmitting acoustic pressure pulses faster according to v \\propto 1/\\sqrt{M}."),

    # 77: Bell Jar Vacuum Experiment
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Glass Bell Jar -->
  <path d="M 120,150 L 120,70 A 50,50 0 0,1 220,70 L 220,150 Z" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <rect x="100" y="150" width="140" height="15" fill="#64748b"/>
  <!-- Electric Bell hanging -->
  <circle cx="170" cy="90" r="15" fill="#facc15"/>
  <line x1="170" y1="50" x2="170" y2="75" stroke="#94a3b8" stroke-width="2"/>
  <!-- Vacuum pump pipe below -->
  <rect x="160" y="165" width="20" height="20" fill="#475569"/>
  <text x="80" y="180" fill="#94a3b8" font-size="9">To Vacuum Pump</text>
  <text x="35" y="40" fill="#facc15" font-size="10" font-weight="bold">Bell Jar Experiment: Sound Fades to Silence in Vacuum</text>
</svg>
</div>
In the historic electric bell jar experiment depicted above, what happens to the ringing sound as the vacuum pump extracts air from inside the jar?""",
     ["The sound grows progressively fainter until it becomes completely inaudible, proving sound cannot travel in a vacuum""",
     "The sound pitch becomes higher like a whistle""",
     "The bell rings twice as loud""",
     "The bell changes into radio signals"],
     "A", "OSC", "easy""",
     "As air molecules are evacuated, fewer particles remain to transmit mechanical pressure vibrations from the bell clapper to the glass jar wall, silencing the bell."),

    # 78: Lightning and Thunder Timing
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Cloud & Lightning -->
  <path d="M 40,40 Q 60,25 80,40 Q 100,25 120,40 Q 130,55 120,70 Q 70,75 40,65 Z" fill="#475569"/>
  <polyline points="75,65 65,95 85,95 70,135" fill="none" stroke="#facc15" stroke-width="3"/>
  <text x="95" y="100" fill="#facc15" font-size="10" font-weight="bold">Lightning (Instant)</text>
  <!-- Observer -->
  <circle cx="280" cy="115" r="8" fill="#38bdf8"/>
  <line x1="280" y1="123" x2="280" y2="155" stroke="#38bdf8" stroke-width="2"/>
  <!-- Time gap label -->
  <text x="140" y="130" fill="#f87171" font-size="10" font-weight="bold">Thunder: \Deltat = 3.0 s</text>
  <text x="60" y="175" fill="#cbd5e1" font-size="10">d = v_sound · \Deltat = 340 m/s · 3.0 s = 1020 m (1.02 km)</text>
</svg>
</div>
During a thunderstorm, an observer sees a flash of lightning and hears the thunderclap exactly 3.0 seconds later. Taking the speed of sound as 340 m/s, how far away did the lightning strike?""",
     ["1020 m (1.02 km)", "340 m", "680 m", "170 m"],
     "A", "OSC", "easy""",
     "Because light travels at 300,000 km/s, the flash reaches the eye almost instantaneously (t \approx 0). Sound travels at 340 m/s, so distance d = v * t = 340 * 3.0 = 1020 m."),

    # 79: Tuning Fork Waveform Generation
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Tuning fork -->
  <path d="M 60,50 L 60,110 Q 60,130 80,130 L 80,165" fill="none" stroke="#94a3b8" stroke-width="5"/>
  <path d="M 80,50 L 80,110" fill="none" stroke="#94a3b8" stroke-width="5"/>
  <!-- Vibration arrows -->
  <path d="M 50,70 Q 55,70 60,70" stroke="#facc15" stroke-width="2"/>
  <path d="M 80,70 Q 85,70 90,70" stroke="#facc15" stroke-width="2"/>
  <!-- Wavefronts pushing out -->
  <path d="M 110,60 A 60,60 0 0,1 110,140" fill="none" stroke="#f43f5e" stroke-width="3"/>
  <path d="M 140,55 A 80,80 0 0,1 140,145" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
  <path d="M 170,50 A 100,100 0 0,1 170,150" fill="none" stroke="#f43f5e" stroke-width="3"/>
  <text x="180" y="45" fill="#f43f5e" font-size="9">C</text>
  <text x="145" y="48" fill="#38bdf8" font-size="9">R</text>
  <text x="40" y="30" fill="#facc15" font-size="10" font-weight="bold">Tuning fork prongs push air outward into compressions</text>
</svg>
</div>
How does the outward mechanical vibration of a tuning fork prong create a compression in the surrounding air?""",
     ["As the prong flexes outward, it rapidly compresses and pushes the adjacent air forward, creating a region of high density and pressure""",
     "It heats up the air to create thermal expansion""",
     "It creates an electric spark""",
     "It pulls air molecules into a vacuum"],
     "A", "OSC", "easy""",
     "When the prong pushes outward, it displaces and crowds adjacent air particles together to generate a compression; when it springs back, it leaves a low-density rarefaction behind."),

    # 80: Amplitude vs Pitch Waveforms
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Wave 1: High amplitude, low frequency (Loud bass) -->
  <path d="M 30,55 Q 60,20 90,55 T 150,55" fill="none" stroke="#f43f5e" stroke-width="3"/>
  <text x="165" y="55" fill="#f43f5e" font-size="9.5" font-weight="bold">High Amplitude (Loud Sound)</text>
  <!-- Wave 2: Low amplitude, high frequency (Soft shrill) -->
  <path d="M 30,125 Q 45,105 60,125 T 90,125 T 120,125 T 150,125" fill="none" stroke="#38bdf8" stroke-width="1.8"/>
  <text x="165" y="125" fill="#38bdf8" font-size="9.5" font-weight="bold">High Frequency (High Pitch)</text>
  <text x="40" y="175" fill="#cbd5e1" font-size="10">Amplitude governs loudness; Frequency governs pitch</text>
</svg>
</div>
Comparing the two waveforms shown in the diagram, what acoustic characteristic differentiates the top wave from the bottom wave?""",
     ["The top wave has greater amplitude (louder) and lower frequency (lower pitch); the bottom wave has higher frequency (higher pitch)""",
     "The top wave is ultrasonic and the bottom wave is infrasonic""",
     "The top wave travels faster than the bottom wave""",
     "Both waves have identical loudness and pitch"],
     "A", "OSC", "easy""",
     "The top wave has large vertical displacement (high amplitude = loud) and longer period (lower frequency = deeper pitch); the bottom wave has rapid oscillations (high frequency = shrill)."),

    # 81: Underwater Acoustic Transmission
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Water boundary -->
  <rect x="20" y="60" width="300" height="110" fill="#0284c7" fill-opacity="0.2"/>
  <line x1="20" y1="60" x2="320" y2="60" stroke="#38bdf8" stroke-width="2"/>
  <text x="30" y="45" fill="#94a3b8" font-size="10">Air: v_1 \approx 340 m/s</text>
  <text x="30" y="85" fill="#38bdf8" font-size="10">Water: v_2 \approx 1500 m/s</text>
  <text x="30" y="130" fill="#facc15" font-size="11" font-weight="bold">Wavelength expands: \lambda_2 = (v_2 / v_1) · \lambda_1 \approx 4.41 · \lambda_1</text>
  <text x="30" y="155" fill="#4ade80" font-size="10">Frequency \nu remains strictly constant across boundary</text>
</svg>
</div>
When a sound wave generated by an airborne loudspeaker enters lake water as illustrated, why does its wavelength stretch by approximately 4.41 times?""",
     ["Because the frequency remains constant while the speed of sound increases from 340 m/s to 1500 m/s in water (\\lambda = v / \\nu)""",
     "Because water molecules attract light photons""",
     "Because sound frequency drops to one-fourth in water""",
     "Because the lake absorbs the wave's kinetic energy"],
     "A", "OSC", "medium""",
     "Source frequency is invariant. Because water has higher bulk modulus, velocity jumps from ~340 m/s to ~1500 m/s, expanding wavelength by the factor 1500/340 \approx 4.41."),

    # 82: Master Chapter 12 Formula Summary Card
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="20" y="20" width="300" height="150" rx="8" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="35" y="45" fill="#facc15" font-size="11" font-weight="bold">Sound Wave Formulae &amp; Invariants:</text>
  <text x="35" y="70" fill="#38bdf8" font-size="10.5">1. Wave Equation: v = \\nu · \\lambda  =  \\lambda / T</text>
  <text x="35" y="95" fill="#4ade80" font-size="10.5">2. Temperature: v \\propto \\sqrt{T}  →  v_T \\approx 331 + 0.61·T_c</text>
  <text x="35" y="120" fill="#ec4899" font-size="10.5">3. Molecular Mass: v \\propto 1 / \\sqrt{M}</text>
  <text x="35" y="145" fill="#a78bfa" font-size="10.5">4. Medium Speed: v_solids &gt; v_liquids &gt; v_gases</text>
</svg>
</div>
According to the master summary of sound wave mechanics, which medium factor has ZERO effect on the velocity of sound in a gas at constant temperature?""",
     ["Variations in atmospheric gas pressure alone""",
     "Variations in absolute gas temperature""",
     "The molecular weight of the gas""",
     "The moisture humidity content in the air"],
     "A", "OSC", "easy""",
     "At constant temperature, density changes in direct proportion to pressure changes (P/\\rho = constant), rendering the velocity of sound completely independent of pressure variations.")
]

def generate():
    all_qs = []
    
    # 40 Exam (30 from exam_data + 10 from extra_exam)
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

    out_file = "scripts/ch12_topic1.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
