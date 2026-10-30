# scripts/generate_ch14_topic3.py
# MH-9-SCIT-14-14.3: Radioactive Substances & Alpha, Beta, Gamma Rays
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-14-14.3"

exam_data = [
    # 1-10: Discovery & Fundamental Radioactivity
    ("What is radioactivity?""",
     ["The spontaneous emission of highly penetrating invisible radiations by the unstable nuclei of heavy elements",
      "The absorption of visible light by chemical compounds",
      "The chemical reaction between an acid and a metal",
      "The physical melting of metals at high temperatures"],
     "A", "OSC", "easy",
     "Radioactivity is a spontaneous nuclear phenomenon in which an unstable atomic nucleus loses energy by emitting radiation such as alpha, beta, and gamma rays."),

    ("Who discovered the phenomenon of natural radioactivity in 1896 using uranium salts and a photographic plate?""",
     ["Henri Becquerel", "Ernest Rutherford", "Marie Curie", "Wilhelm Rontgen"],
     "A", "OSC", "easy",
     "Henri Becquerel accidentally discovered radioactivity when uranium potassium sulfate blackened a wrapped photographic plate kept in a dark drawer."),

    ("Which two new radioactive elements were discovered by Marie and Pierre Curie from pitchblende ore?""",
     ["Polonium and Radium", "Uranium and Thorium", "Cobalt and Iodine", "Sodium and Potassium"],
     "A", "OSC", "easy",
     "Marie and Pierre Curie isolated the new radioactive elements Polonium (named after Poland) and Radium from tons of pitchblende uranium ore."),

    ("Elements having an atomic number (Z) greater than ________ generally exhibit natural radioactivity due to nuclear instability.",
     ["82 (Lead)", "20 (Calcium)", "40 (Zirconium)", "10 (Neon)"],
     "A", "OFB", "easy",
     "Elements with atomic number greater than 82 have high proton-to-neutron repulsion, making their nuclei spontaneously unstable and radioactive."),

    ("Which of the following is a naturally occurring radioactive element?""",
     ["Uranium", "Iron", "Aluminium", "Silicon"],
     "A", "OSC", "easy",
     "Uranium (atomic number 92) is a primordial radioactive element occurring naturally in the Earth's crust."),

    ("Which property of radioactive emissions did Ernest Rutherford investigate by passing rays through a transverse electric field in 1902?""",
     ["Their electrical charges and deflections towards positively and negatively charged metal plates",
      "Their boiling points and freezing points",
      "Their chemical taste and odor",
      "Their optical transparency in water"],
     "A", "OSC", "easy",
     "Rutherford used opposing charged electric plates to demonstrate that the radiation consists of positive (alpha), negative (beta), and neutral (gamma) components."),

    ("In Rutherford's electric field experiment, which rays deflected towards the negatively charged plate?""",
     ["Alpha (α) rays", "Beta (β) rays", "Gamma (γ) rays", "Cathode rays"],
     "A", "OSC", "easy",
     "Because unlike charges attract, the positively charged alpha rays deflected towards the negative electrical plate."),

    ("In Rutherford's electric field experiment, which rays deflected towards the positively charged plate with a noticeably larger deviation?""",
     ["Beta (β) rays", "Alpha (α) rays", "Gamma (γ) rays", "Anode rays"],
     "A", "OSC", "easy",
     "Beta rays carry negative charge and have very small mass (electrons), causing them to deflect strongly towards the positive plate."),

    ("Which radioactive radiation passes straight through an electric or magnetic field without suffering any deflection?""",
     ["Gamma (γ) rays", "Alpha (α) rays", "Beta (β) rays", "Proton beams"],
     "A", "OSC", "easy",
     "Gamma rays are uncharged electromagnetic photons; having no net electric charge, they experience zero Lorentz force in electric or magnetic fields."),

    ("State whether the following statement is True or False: Radioactivity is influenced by external physical factors such as temperature, pressure, or chemical bonding.",
     ["True", "False"],
     "B", "OTF", "easy",
     "Radioactivity is purely an intra-nuclear phenomenon; nuclear decay rates are completely independent of temperature, pressure, or chemical combination."),

    # 11-20: Nature of Alpha, Beta, Gamma
    ("What is the exact physical nature of an alpha (α) particle?""",
     ["A doubly ionized helium nucleus (He2+) consisting of 2 protons and 2 neutrons",
      "A fast-moving electron ejected from an atomic shell",
      "A high-energy packet of light (photon)",
      "A neutral neutron moving at low velocity"],
     "A", "OSC", "easy",
     "An alpha particle is identical to a helium-4 nucleus, composed of 2 protons and 2 neutrons with a net charge of +2e and mass ~4 u."),

    ("What is the mass and charge of an alpha particle compared to a proton?""",
     ["Mass is approximately 4 times that of a proton, and charge is +2 times the proton charge",
      "Mass is equal to 1 proton and charge is +1",
      "Mass is 1/1840 of a proton and charge is -1",
      "Mass is zero and charge is zero"],
     "A", "OSC", "medium",
     "Mass of He2+ is 4 u (approx 4 * mass of proton) and charge is +2e (two unit positive charges)."),

    ("What is the nature of a beta (β) particle emitted during nuclear radioactive decay?""",
     ["A fast-moving electron originating from the transformation of a nuclear neutron into a proton",
      "An orbital valence electron dislodged by heat",
      "A positively charged helium nucleus",
      "An uncharged high frequency light quantum"],
     "A", "OSC", "medium",
     "In beta-minus decay, a neutron inside an unstable nucleus transforms into a proton, emitting a high-speed electron (beta particle) and an antineutrino."),

    ("What is the nature of gamma (γ) radiation?""",
     ["High-frequency, short-wavelength electromagnetic radiation consisting of energetic photons",
      "A stream of heavy positive helium ions",
      "A beam of fast thermal neutrons",
      "A low-frequency sound wave travelling through matter"],
     "A", "OSC", "easy",
     "Gamma radiation consists of massless, charge-neutral electromagnetic photons of extremely high frequency and energy emitted by excited nuclei."),

    ("What is the speed of gamma rays in vacuum?""",
     ["Equal to the speed of light (3 x 10^8 m/s)",
      "Approximately 1/20 to 1/5 the speed of light",
      "Exactly 330 m/s (speed of sound)",
      "Zero because they are stationary waves"],
     "A", "OSC", "easy",
     "As electromagnetic waves, gamma rays propagate at the speed of light (c \approx 3 x 10^8 m/s) in vacuum."),

    ("Rank the three radioactive radiations in decreasing order of their ionizing power (highest to lowest):",
     ["Alpha (α) > Beta (β) > Gamma (γ)",
      "Gamma (γ) > Beta (β) > Alpha (α)",
      "Beta (β) > Alpha (α) > Gamma (γ)",
      "Gamma (γ) > Alpha (α) > Beta (β)"],
     "A", "OSC", "easy",
     "Because of their +2 charge, high mass, and slower velocity, alpha particles have the highest ionizing power (~100 times beta and ~10,000 times gamma)."),

    ("Rank the three radioactive radiations in decreasing order of their penetrating power through matter (highest to lowest):",
     ["Gamma (γ) > Beta (β) > Alpha (α)",
      "Alpha (α) > Beta (β) > Gamma (γ)",
      "Beta (β) > Gamma (γ) > Alpha (α)",
      "Alpha (α) > Gamma (γ) > Beta (β)"],
     "A", "OSC", "easy",
     "Gamma rays have the greatest penetrating power (requiring thick lead to attenuate), followed by beta rays (stopped by aluminium), while alpha rays are stopped by a sheet of paper."),

    ("Which material is sufficient to completely block and absorb alpha (α) particles?""",
     ["A single thin sheet of paper or 2 to 5 cm of air",
      "A 15 cm thick slab of solid lead",
      "A 1 meter thick wall of reinforced concrete",
      "A sheet of magnetic iron"],
     "A", "OSC", "easy",
     "Because alpha particles lose kinetic energy rapidly through intense ionization, they are completely stopped by a thin sheet of paper or human skin epidermis."),

    ("Which material is typically required to stop beta (β) particles?""",
     ["An aluminium sheet of about 2 to 5 mm thickness",
      "A single layer of tissue paper",
      "A 30 cm block of solid lead",
      "A vacuum chamber"],
     "A", "OSC", "easy",
     "Beta particles penetrate paper and skin, but are effectively shielded by a few millimeters of aluminium or plastic/plexiglass."),

    ("Which shielding material is most effective at absorbing penetrating gamma (γ) rays?""",
     ["Thick lead blocks (10-15 cm) or dense reinforced concrete walls",
      "A sheet of writing paper",
      "A thin aluminium foil (0.01 mm)",
      "A layer of dry cotton cloth"],
     "A", "OSC", "easy",
     "High-density materials with high atomic numbers, such as lead (Pb) and thick concrete, are required to attenuate high-energy gamma photons."),

    # 21-30: Radioisotopes in Medicine, Industry & Agriculture
    ("Which radioactive isotope is used in radiotherapy for destroying malignant cancerous tumors?""",
     ["Cobalt-60 (Co-60)", "Carbon-14 (C-14)", "Sodium-24 (Na-24)", "Uranium-235 (U-235)"],
     "A", "OSC", "easy",
     "Cobalt-60 emits energetic gamma rays that are collimated into pinpoint beams to destroy DNA in cancer tumor cells."),

    ("Which radioisotope is used for the diagnosis and treatment of thyroid gland disorders and goitre?""",
     ["Iodine-131 (I-131)", "Cobalt-60 (Co-60)", "Phosphorus-32 (P-32)", "Lead-206 (Pb-206)"],
     "A", "OSC", "easy",
     "The thyroid gland selectively absorbs iodine; radioactive Iodine-131 targets thyroid tissue to image function or ablate hyperactive/cancerous thyroid cells."),

    ("Which radioisotope is injected into the bloodstream as a medical tracer to detect blood clots, deep vein thrombosis, and circulatory restrictions?""",
     ["Sodium-24 (Na-24)", "Uranium-238 (U-238)", "Carbon-14 (C-14)", "Radium-226 (Ra-226)"],
     "A", "OSC", "easy",
     "Sodium-24 in sterile saline circulates freely; detecting gamma emissions downstream identifies blockages or poor circulation points in the vascular system."),

    ("Which radioisotope is utilized in archaeology and paleontology to determine the age of ancient organic fossils and wood artifacts (Radiocarbon dating)?""",
     ["Carbon-14 (C-14)", "Cobalt-60 (Co-60)", "Iodine-131 (I-131)", "Phosphorus-32 (P-32)"],
     "A", "OSC", "easy",
     "Living organisms maintain a steady ratio of C-14 to C-12. After death, C-14 decays with a half-life of 5,730 years, allowing precise chronological dating."),

    ("How is gamma radiation used in the food processing and agricultural industry?""",
     ["Food irradiation to inhibit sprouting in onions and potatoes, kill foodborne bacteria, and prolong shelf life",
      "Cooking raw food instantly into gourmet meals",
      "Replacing table salt and sugar in food recipes",
      "Turning fruit juices into carbonated sodas"],
     "A", "OSC", "easy",
     "Controlled doses of gamma rays from Co-60 inhibit sprouting in tuber vegetables and sterilize spices and fruits by destroying microbial pathogens without making food radioactive."),

    ("Which radioisotope is widely used in agricultural research to track the uptake and translocation of phosphate fertilizers in crop plants?""",
     ["Phosphorus-32 (P-32)", "Cobalt-60 (Co-60)", "Sodium-24 (Na-24)", "Uranium-235 (U-235)"],
     "A", "OSC", "medium",
     "Phosphorus-32 acts as an isotopic tracer in fertilizer; monitoring its movement through root systems and foliage reveals optimal fertilization schedules."),

    ("How is radioactive radiation used in industrial quality control to detect hidden cracks or internal structural defects in heavy metal castings and pipelines?""",
     ["Industrial radiography using gamma ray sources (such as Iridium-192 or Cobalt-60) and radiographic film",
      "Dipping the entire metal casting into liquid mercury",
      "Painting the metal with fluorescent acrylic colors",
      "Exposing the pipe to high-pressure steam"],
     "A", "OSC", "medium",
     "Gamma radiography works like a medical X-ray for metals: penetrating gamma rays expose photographic film behind the weld, revealing internal voids, cracks, or flaws."),

    ("What radioactive isotope is utilized in industrial thickness gauges to continuously monitor and control the thickness of manufactured sheets of paper, plastic, or metal foil?""",
     ["Beta-emitting radioisotopes (such as Strontium-90 or Krypton-85)",
      "Alpha-emitting Uranium-238",
      "High-energy neutron emitters",
      "Stable Lead-208"],
     "A", "OSC", "hard",
     "The attenuation of beta radiation passing through a moving sheet is directly proportional to its thickness, feeding real-time calibration back to automated rollers."),

    ("Assertion (A): Alpha particles have the lowest penetrating ability but pose the highest internal biological hazard if inhaled or ingested.\nReason (R): Because of their high mass (+2e charge), alpha particles deposit immense ionizing energy over a very short distance, causing catastrophic double-strand DNA damage to living cells.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     "Externally, alpha particles cannot penetrate dead skin; however, inside lung or digestive tissue, their high linear energy transfer (LET) produces massive cellular and genetic devastation."),

    ("Assertion (A): Gamma rays suffer no deflection when passing between the poles of a strong electromagnet.\nReason (R): Gamma rays are massless and uncharged electromagnetic photons carrying zero net electric charge.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "easy",
     "Magnetic Lorentz force F = q(v x B). Since charge q = 0 for gamma photons, the force is identically zero, resulting in a straight undeflected trajectory."),

    # 31-40: Fill in Blanks, Numerical & Multi-choice
    ("The SI unit of radioactive activity, defined as 1 nuclear disintegration per second, is the ________.",
     ["becquerel (Bq)", "curie (Ci)", "roentgen (R)", "gray (Gy)"],
     "A", "OFB", "easy",
     "The SI unit of radioactivity is the becquerel (Bq), where 1 Bq = 1 disintegration per second."),

    ("The non-SI historical unit of radioactivity, approximately equal to the activity of 1 gram of Radium-226 (3.7 x 10^10 disintegrations/sec), is the ________.",
     ["curie (Ci)", "becquerel (Bq)", "tesla (T)", "fermi (fm)"],
     "A", "OFB", "easy",
     "1 Curie (Ci) is defined as 3.7 x 10^10 disintegrations per second."),

    ("When a radioactive parent nucleus emits an alpha (α) particle, its atomic number (Z) decreases by ________ and its mass number (A) decreases by ________.",
     ["2 and 4", "1 and 0", "0 and 1", "2 and 2"],
     "A", "OFB", "easy",
     "An alpha particle is a helium nucleus (2 He 4). Emitting an alpha particle decreases Z by 2 and mass number A by 4."),

    ("When an unstable nucleus undergoes beta-minus (β-) decay, its atomic number (Z) ________ by 1 while its mass number (A) remains unchanged.",
     ["increases", "decreases", "doubles", "drops to zero"],
     "A", "OFB", "easy",
     "During beta decay, a neutron transforms into a proton (n -> p + e- + anti-nu), so atomic number increases by 1 while mass number remains constant."),

    ("A radioactive isotope sample has a half-life of 10 days. If an initial sample contains 80 mg of this isotope, what mass will remain undecayed after 30 days?""",
     ["10 mg", "20 mg", "40 mg", "5 mg"],
     "A", "ONE", "medium",
     "Number of half-lives elapsed n = 30 / 10 = 3. Remaining mass = 80 / (2^3) = 80 / 8 = 10 mg."),

    ("A radioactive source has an initial activity of 400 Bq. If its half-life is 5 hours, what will its activity be after 10 hours?""",
     ["100 Bq", "200 Bq", "50 Bq", "25 Bq"],
     "A", "ONE", "medium",
     "In 10 hours, 2 half-lives elapse. Activity = 400 / (2^2) = 400 / 4 = 100 Bq."),

    ("Which of the following radiations are classified as ionizing electromagnetic radiations?""",
     ["Gamma rays and X-rays", "Radio waves and Microwaves", "Infrared rays and Visible light", "Sound waves and Ultrasonic waves"],
     "A", "OMC", "easy",
     "Gamma rays and X-rays have sufficient photon energy (> 10-12 eV) to dislodge orbital electrons from atoms, creating ions."),

    ("Which of the following safety measures are mandatory when handling radioactive substances in nuclear facilities?""",
     ["Wearing lead-lined aprons and using thick lead shielding containers",
      "Using remote robotic tongs/manipulators behind leaded glass",
      "Wearing dosimeter radiation monitoring badges (TLD badges)",
      "All of the above"],
     "A", "OMC", "easy",
     "All of these are essential radiation protection protocols to minimize external and internal exposure to ionizing radiation."),

    ("What happens to an atom's atomic number (Z) and mass number (A) during gamma (γ) emission?""",
     ["Both atomic number (Z) and mass number (A) remain completely unchanged",
      "Atomic number decreases by 2 and mass number decreases by 4",
      "Atomic number increases by 1 and mass number is unchanged",
      "Atomic number decreases by 1 and mass number decreases by 1"],
     "A", "OSC", "easy",
     "Gamma emission simply de-excites a nuclear isomer from a higher nuclear energy state to a lower state without changing proton or neutron counts."),

    ("Why are film badges (dosimeters) worn by personnel working in hospital radiology and nuclear facilities?""",
     ["To record and monitor the cumulative ionizing radiation dose absorbed by the worker over time",
      "To prevent radioactive rays from entering the building",
      "To measure body temperature and pulse rate",
      "To act as a battery for medical equipment"],
     "A", "OSC", "easy",
     "Film badges contain photographic emulsions and filtration filters that darken proportionally to the accumulated radiation exposure, safeguarding occupational health.")
]

practice_data = [
    # 41-50: Practice on Properties of Radiations
    ("Which radioactive emission has the highest velocity?""",
     ["Gamma rays (equal to speed of light, c)",
      "Beta particles",
      "Alpha particles",
      "Thermal neutrons"],
     "A", "OSC", "easy",
     "Gamma rays are electromagnetic waves and travel at the speed of light (3 x 10^8 m/s), whereas alpha and beta particles have non-zero rest mass and travel slower."),

    ("Why do beta particles experience greater angular deflection than alpha particles in the same electric field despite having a smaller electric charge?""",
     ["Beta particles have an extremely small mass (approx 1/7350 of an alpha particle), resulting in a vastly higher charge-to-mass ratio (q/m)",
      "Beta particles are attracted by gravity",
      "Beta particles travel faster than light",
      "Alpha particles carry zero electric charge"],
     "A", "OSC", "medium",
     "Deflection angle in a transverse electric field is proportional to the specific charge (q/m). For beta particles, q/m is thousands of times larger than for alpha particles."),

    ("What is the electric charge on a beta-minus (β-) particle?""",
     ["-1.6 x 10^-19 Coulombs (-1e)",
      "+3.2 x 10^-19 Coulombs (+2e)",
      "Zero",
      "+1.6 x 10^-19 Coulombs (+1e)"],
     "A", "OSC", "easy",
     "A beta-minus particle is an electron carrying one elementary unit of negative charge: -1.6 x 10^-19 C."),

    ("What is the charge on an alpha (α) particle in Coulombs?""",
     ["+3.2 x 10^-19 Coulombs (+2e)",
      "-1.6 x 10^-19 Coulombs (-1e)",
      "Zero",
      "+6.4 x 10^-19 Coulombs (+4e)"],
     "A", "OSC", "medium",
     "An alpha particle has two protons and no electrons, so its net charge is +2e = +2 * (1.6 x 10^-19 C) = +3.2 x 10^-19 C."),

    ("Which type of radiation produces dense, straight, continuous ion tracks in a Wilson cloud chamber?""",
     ["Alpha (α) particles", "Beta (β) particles", "Gamma (γ) rays", "Neutrons"],
     "A", "OSC", "medium",
     "Because of their high mass, slow velocity, and strong double positive charge, alpha particles cause intense localized ionization, leaving thick, straight droplet tracks."),

    ("Why do beta particles produce thin, tortuous, zigzag tracks in a cloud chamber?""",
     ["Due to their light mass, they undergo frequent elastic collisions and scattering with orbital electrons of gas atoms",
      "They are attracted by air currents",
      "They freeze water droplets unevenly",
      "They are made of lightning bolts"],
     "A", "OSC", "medium",
     "Being lightweight electrons, beta particles are easily deflected when colliding with gas atoms, yielding wandering zig-zag ionization tracks."),

    ("Which biological effect can arise from excessive exposure of living tissue to high doses of ionizing radiation?""",
     ["Breakage of chromosomes and DNA strands leading to genetic mutations, leukemia, and cancer",
      "Instant transformation into a new biological species",
      "Strengthening of bone density and immunity",
      "Permanent increase in muscle strength"],
     "A", "OSC", "easy",
     "Ionizing radiation generates free radicals and breaks DNA chemical bonds, causing somatic cell destruction and germline genetic mutations."),

    ("What happens when an atom of Uranium-238 (92 U 238) emits an alpha particle?""",
     ["It transmutes into Thorium-234 (90 Th 234)",
      "It transmutes into Uranium-235",
      "It turns into Plutonium-239",
      "It turns into Lead-206 immediately"],
     "A", "OSC", "medium",
     "92 U 238 -> 90 Th 234 + 2 He 4. Atomic number drops from 92 to 90 (Thorium) and mass drops from 238 to 234."),

    ("What happens when Thorium-234 (90 Th 234) undergoes beta-minus emission?""",
     ["It transmutes into Protactinium-234 (91 Pa 234)",
      "It turns into Radium-230",
      "It turns into Uranium-238",
      "It breaks into two equal iron atoms"],
     "A", "OSC", "medium",
     "90 Th 234 -> 91 Pa 234 + -1 e 0. A neutron changes into a proton, raising the atomic number by 1 to 91 (Protactinium)."),

    ("State whether True or False: Radioactive waste from nuclear plants can be safely dumped into municipal household trash bins.",
     ["True", "False"],
     "B", "OTF", "easy",
     "Nuclear waste remains dangerously radioactive for thousands of years and must be vitrified, shielded in steel-lead canisters, and buried in deep geological repositories."),

    # 51-60: Applications & Detection Practice
    ("Which device is widely used in laboratories for detecting and counting ionizing radiation events?""",
     ["Geiger-Muller (GM) counter", "Barometer", "Hydrometer", "Galvanometer"],
     "A", "OSC", "easy",
     "A Geiger-Muller tube detects the Townsend avalanche ionization pulses produced when ionizing particles enter a low-pressure gas tube."),

    ("Why is Americium-241 (Am-241), an alpha emitter, safely used in domestic ionization smoke detectors?""",
     ["Alpha particles ionize air molecules between electrodes; smoke particles disrupt this current, triggering the alarm, while alpha rays cannot penetrate the plastic housing",
      "It heats the room during winter",
      "It emits light to guide people out of fire",
      "It releases water to extinguish fire"],
     "A", "OSC", "hard",
     "The alpha particles generate a steady ionization current in the chamber. Smoke absorbs the alpha rays, dropping the current and activating the circuit safely without external radiation leak."),

    ("Why is food irradiated with gamma rays safe to eat immediately after treatment?""",
     ["Irradiation destroys microbes through DNA breakage but leaves no residual radioactivity in the food",
      "The food becomes completely hot and cooked",
      "Gamma rays add vitamins to the food",
      "All atoms in the food are converted into carbon"],
     "A", "OSC", "easy",
     "Passing gamma rays through food does not induce nuclear activation; it kills bacteria without making food atoms radioactive."),

    ("What is the half-life of Carbon-14 used in radiocarbon dating?""",
     ["Approximately 5,730 years", "24 hours", "100 years", "1 million years"],
     "A", "OSC", "easy",
     "Carbon-14 decays back into Nitrogen-14 via beta decay with a half-life of 5,730 years."),

    ("Why cannot radiocarbon dating (C-14) be used to date rocks or dinosaur fossils that are 100 million years old?""",
     ["After about 50,000 to 60,000 years (approx 10 half-lives), the remaining C-14 is too minute to detect reliably",
      "Rocks never contain any carbon atoms",
      "Dinosaurs were immune to radioactivity",
      "C-14 turns into gold over millions of years"],
     "A", "OSC", "medium",
     "Because C-14 has a short half-life of 5,730 years, virtually all C-14 atoms decay within 60,000 years. Million-year-old rocks require long-lived isotopes like U-238 or K-40."),

    ("Which radioisotope is used in the treatment of bone cancer and leukemia to irradiate diseased bone marrow?""",
     ["Phosphorus-32 or Strontium-89", "Uranium-235", "Helium-4", "Carbon-12"],
     "A", "OSC", "medium",
     "Phosphorus-32 and Strontium-89 target bone tissue actively, delivering localized beta radiation to suppress abnormal hematopoiesis in leukemia."),

    ("Assertion (A): Lead containers with thick walls are universally used for storing and transporting radioactive substances.\nReason (R): Lead has high density and a high atomic number (Z = 82), providing exceptional shielding and attenuation against high-energy ionizing rays.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "easy",
     "High electron density in lead absorbs photons via photoelectric effect and Compton scattering, providing premier radiation attenuation."),

    ("State whether True or False: Beta particles are identical in mass and charge to cathode rays.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Both cathode rays and beta particles are streams of high-velocity electrons possessing charge -e and mass 1/1840 u."),

    ("What is the mass of a gamma photon at rest?""",
     ["Zero rest mass", "Equal to mass of an electron", "Equal to mass of a proton", "Equal to mass of a helium atom"],
     "A", "OSC", "easy",
     "Photons have zero invariant rest mass (m0 = 0)."),

    ("Which radioisotope is used to detect leaks in underground municipal water and gas pipeline networks without digging up roads?""",
     ["Sodium-24 (Na-24)", "Uranium-238 (U-238)", "Carbon-14 (C-14)", "Polonium-210 (Po-210)"],
     "A", "OSC", "easy",
     "A short-lived tracer like Na-24 is added to the flowing fluid; a radiation detector swept above ground identifies radioactive pooling at the exact underground leak site.")
]

# Add remaining practice questions to make exactly 30 (61-70)
practice_data.extend([
    ("Which of the following elements has no stable non-radioactive isotopes?""",
     ["Radium", "Iron", "Gold", "Copper"],
     "A", "OSC", "easy",
     "All isotopes of radium (atomic number 88) are radioactive with unstable nuclei."),

    ("What is emitted when an excited nucleus returns to its ground state without any change in proton or neutron number?""",
     ["Gamma ray photon (γ)", "Alpha particle", "Beta particle", "Positron"],
     "A", "OSC", "easy",
     "Gamma de-excitation releases excess nuclear binding energy as a high-frequency gamma photon."),

    ("How do alpha, beta, and gamma radiations affect a photographic plate wrapped in opaque black paper?""",
     ["They penetrate the paper and chemically expose/darken the silver halide emulsion",
      "They make the plate completely transparent like glass",
      "They have zero effect on photographic plates",
      "They erase existing photographs"],
     "A", "OSC", "easy",
     "All three forms of ionizing radiation penetrate paper and reduce silver halide grains, creating a latent image upon development."),

    ("A radioactive substance has a half-life of 2 hours. What fraction of the original radioactive nuclei will remain undecayed after 6 hours?""",
     ["1/8 (12.5%)", "1/4 (25%)", "1/2 (50%)", "1/16 (6.25%)"],
     "A", "ONE", "medium",
     "After 6 hours, 3 half-lives have elapsed (6 / 2 = 3). Fraction remaining = (1/2)^3 = 1/8."),

    ("Which radiation has the lowest ionization power?""",
     ["Gamma (γ) radiation", "Beta (β) radiation", "Alpha (α) radiation", "Proton beam"],
     "A", "OSC", "easy",
     "Because they carry no net charge and move at the speed of light, gamma rays interact weakly with electrons, giving the lowest ionization density."),

    ("State whether True or False: Radioactive emissions are deflected by gravity more strongly than by electric fields.",
     ["True", "False"],
     "B", "OTF", "easy",
     "Electrostatic forces on charged particles exceed gravitational forces by more than 10^36 times; gravitational deflection is utterly negligible."),

    ("The process by which an unstable atomic nucleus spontaneously transforms into another nucleus by emitting radiation is known as nuclear ________.",
     ["decay / disintegration", "fusion", "boiling", "sublimation"],
     "A", "OFB", "easy",
     "Radioactive decay or nuclear disintegration refers to spontaneous radioactive transformation."),

    ("Alpha particles consist of ________ protons and ________ neutrons.",
     ["2 and 2", "1 and 1", "2 and 4", "4 and 0"],
     "A", "OFB", "easy",
     "An alpha particle is a helium-4 nucleus composed of 2 protons and 2 neutrons."),

    ("Which property of radioisotopes makes them exceptional medical diagnostic tracers?""",
     ["They emit detectable radiation while behaving in identical chemical fashion to stable isotopes of the same element in the body",
      "They are highly toxic and destroy all cells",
      "They make body tissues glow in the dark visibly",
      "They permanently alter human DNA into plastic"],
     "A", "OSC", "medium",
     "Radioisotopes have identical valence electron configurations to stable isotopes, participating in normal biochemical pathways while emitting trackable gamma rays."),

    ("Which organization monitors radiation protection standards internationally?""",
     ["International Commission on Radiological Protection (ICRP) and IAEA",
      "World Health Organization only",
      "Interpol",
      "International Olympic Committee"],
     "A", "OSC", "easy",
     "The ICRP and International Atomic Energy Agency (IAEA) establish global radiation safety dose limits.")
])

# 12 Mock/Foundation Questions with Vector SVGs (71-82)
mock_data = [
    # 71: Rutherford's Electric Field Experiment apparatus
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#0f172a"/>
  <rect x="180" y="160" width="40" height="40" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="200" cy="180" r="6" fill="#facc15"/>
  <text x="200" y="205" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Source (Lead Block)</text>
  <rect x="110" y="70" width="16" height="70" rx="2" fill="#ef4444"/>
  <text x="95" y="110" fill="#f87171" font-size="12" font-family="sans-serif" text-anchor="end" font-weight="bold">(+) Plate</text>
  <rect x="274" y="70" width="16" height="70" rx="2" fill="#3b82f6"/>
  <text x="305" y="110" fill="#60a5fa" font-size="12" font-family="sans-serif" text-anchor="start" font-weight="bold">(-) Plate</text>
  <path d="M 200 160 Q 200 100 270 35" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="270" cy="35" r="4" fill="#38bdf8"/>
  <text x="270" y="25" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">α rays (+)</text>
  <path d="M 200 160 Q 200 100 120 35" fill="none" stroke="#f87171" stroke-width="2"/>
  <circle cx="120" cy="35" r="4" fill="#f87171"/>
  <text x="120" y="25" fill="#f87171" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">β rays (-)</text>
  <line x1="200" y1="160" x2="200" y2="35" stroke="#4ade80" stroke-width="2"/>
  <circle cx="200" cy="35" r="4" fill="#4ade80"/>
  <text x="200" y="25" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">γ rays (0)</text>
</svg>
</div>
The diagram depicts Rutherford's famous experiment separating radioactive radiations in a transverse electric field. Why do beta (β) rays suffer a much sharper angular deflection towards the positive plate than alpha (α) rays towards the negative plate?""",
     ["Beta particles have an extremely tiny electron mass (~1/7350 of an alpha particle), giving them a much higher charge-to-mass ratio (q/m)",
      "Beta particles travel much slower than alpha particles",
      "Alpha particles have negative charge",
      "The positive plate is twice as strong as the negative plate"],
     "A", "OSC", "hard",
     "The transverse deflection acceleration is a = qE/m. Because the electron mass is negligible compared to a helium nucleus, the specific charge (q/m) of beta particles is enormously larger, causing greater angular deviation."),

    # 72: Penetration power comparison through materials
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <rect x="130" y="30" width="8" height="140" fill="#f8fafc"/>
  <text x="134" y="182" fill="#f8fafc" font-size="10" font-family="sans-serif" text-anchor="middle">Paper</text>
  <rect x="230" y="30" width="16" height="140" fill="#94a3b8"/>
  <text x="238" y="182" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Al (5mm)</text>
  <rect x="330" y="30" width="30" height="140" fill="#475569"/>
  <text x="345" y="182" fill="#cbd5e1" font-size="10" font-family="sans-serif" text-anchor="middle">Lead (10cm)</text>
  <line x1="30" y1="60" x2="130" y2="60" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="130" cy="60" r="4" fill="#ef4444"/>
  <text x="25" y="55" fill="#38bdf8" font-size="11" font-family="sans-serif" font-weight="bold">α rays</text>
  <line x1="30" y1="100" x2="230" y2="100" stroke="#facc15" stroke-width="3"/>
  <circle cx="230" cy="100" r="4" fill="#ef4444"/>
  <text x="25" y="95" fill="#facc15" font-size="11" font-family="sans-serif" font-weight="bold">β rays</text>
  <line x1="30" y1="140" x2="340" y2="140" stroke="#4ade80" stroke-width="3"/>
  <circle cx="340" cy="140" r="4" fill="#ef4444"/>
  <text x="25" y="135" fill="#4ade80" font-size="11" font-family="sans-serif" font-weight="bold">γ rays</text>
</svg>
</div>
The chart visualizes the relative penetration powers of alpha, beta, and gamma radiations. If a radioactive source emitting all three rays is placed behind a 1 cm thick aluminium sheet, which radiation will emerge on the other side?""",
     ["Only gamma (γ) rays", "Both alpha and beta rays", "Only alpha rays", "All three rays unchanged"],
     "A", "OSC", "medium",
     "A sheet of paper stops all alpha particles, and 5-10 mm of aluminium absorbs beta particles completely. Therefore, only penetrating gamma rays pass through the 1 cm aluminium slab."),

    # 73: Ionization track comparison
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#0f172a"/>
  <line x1="40" y1="50" x2="360" y2="50" stroke="#38bdf8" stroke-width="6"/>
  <text x="40" y="38" fill="#38bdf8" font-size="11" font-family="sans-serif" font-weight="bold">α particle: Thick, straight, dense ion track</text>
  <path d="M 40 100 Q 90 85 140 115 T 240 90 T 360 120" fill="none" stroke="#facc15" stroke-width="2"/>
  <text x="40" y="88" fill="#facc15" font-size="11" font-family="sans-serif" font-weight="bold">β particle: Thin, zigzag track (multiple scattering)</text>
  <line x1="40" y1="150" x2="360" y2="150" stroke="#4ade80" stroke-width="1" stroke-dasharray="8,8"/>
  <text x="40" y="138" fill="#4ade80" font-size="11" font-family="sans-serif" font-weight="bold">γ ray: Sparse, feathery, secondary ionization droplets</text>
</svg>
</div>
The cloud chamber tracks above reflect the distinct ionizing behaviors of the three radiations. Why does an alpha particle produce a straight and dense ionization trail compared to the zigzag trail of a beta particle?""",
     ["Because an alpha particle is heavy (~7300 times heavier than an electron), it bulldozes through gas atoms without being deflected by individual atomic electrons",
      "Because alpha particles travel faster than light",
      "Because beta particles are magnetically guided into waves",
      "Because gamma rays push alpha particles in a line"],
     "A", "OSC", "hard",
     "The momentum of a massive alpha particle is so high that scattering by atomic electrons causes negligible deflection, resulting in continuous, straight, dense tracks."),

    # 74: Beta-minus nuclear transformation
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#18181b"/>
  <circle cx="80" cy="90" r="30" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
  <text x="80" y="88" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Neutron</text>
  <text x="80" y="104" fill="#cbd5e1" font-size="10" font-family="sans-serif" text-anchor="middle">(n: charge 0)</text>
  <path d="M 125 90 L 175 90" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="180,90 170,85 170,95" fill="#38bdf8"/>
  <circle cx="230" cy="65" r="24" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
  <text x="230" y="69" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Proton (p+)</text>
  <circle cx="310" cy="115" r="14" fill="#3b82f6" stroke="#60a5fa" stroke-width="2"/>
  <text x="310" y="119" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">β- (e-)</text>
  <text x="230" y="150" fill="#a1a1aa" font-size="10" font-family="sans-serif" text-anchor="middle">+ antineutrino (\nu̅)</text>
</svg>
</div>
How can an electron (beta-minus particle) be emitted from the atomic nucleus during beta decay when the nucleus contains only protons and neutrons?""",
     ["A neutron inside the nucleus spontaneously converts into a proton, creating an electron that is immediately ejected: n -> p + e- + antineutrino",
      "An orbital electron from the K-shell is sucked into the nucleus and bounced back",
      "The nuclear force crushes two protons into an electron",
      "Gamma rays condense into liquid electrons inside the nucleus"],
     "A", "OSC", "hard",
     "Beta particles do not pre-exist in the nucleus; they are created at the instant of decay via the weak nuclear interaction when a down quark in a neutron changes into an up quark, forming a proton and emitting an electron."),

    # 75: Half-life exponential decay curve
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#0f172a"/>
  <line x1="60" y1="160" x2="360" y2="160" stroke="#64748b" stroke-width="2"/>
  <line x1="60" y1="160" x2="60" y2="20" stroke="#64748b" stroke-width="2"/>
  <text x="360" y="180" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">Time (Half-lives: T_1/2)</text>
  <text x="45" y="25" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">Activity (N)</text>
  <circle cx="60" cy="30" r="4" fill="#38bdf8"/>
  <text x="50" y="35" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="end">N0 (100%)</text>
  <circle cx="135" cy="95" r="4" fill="#38bdf8"/>
  <text x="135" y="175" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">1 T</text>
  <text x="135" y="85" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">50%</text>
  <circle cx="210" cy="128" r="4" fill="#38bdf8"/>
  <text x="210" y="175" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">2 T</text>
  <text x="210" y="120" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">25%</text>
  <circle cx="285" cy="144" r="4" fill="#38bdf8"/>
  <text x="285" y="175" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">3 T</text>
  <text x="285" y="138" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">12.5%</text>
  <path d="M 60 30 Q 110 90 135 95 T 210 128 T 285 144 T 350 155" fill="none" stroke="#38bdf8" stroke-width="2"/>
</svg>
</div>
Based on the radioactive decay curve shown above, if an archaeologist measures that the C-14 activity in an ancient charcoal sample is exactly 12.5% of living tree charcoal, how many half-lives have elapsed since the organism died?""",
     ["3 half-lives (approx 17,190 years)",
      "1 half-life (approx 5,730 years)",
      "2 half-lives (approx 11,460 years)",
      "5 half-lives (approx 28,650 years)"],
     "A", "OSC", "medium",
     "Remaining fraction = (1/2)^n. Since 12.5% = 1/8 = (1/2)^3, exactly n = 3 half-lives have elapsed. 3 * 5,730 years = 17,190 years."),

    # 76: Magnetic deflection (Lorentz force direction)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <text x="200" y="25" fill="#a1a1aa" font-size="11" font-family="sans-serif" text-anchor="middle">Magnetic Field B (directed into page: ⊗)</text>
  <text x="100" y="70" fill="#64748b" font-size="14">⊗   ⊗   ⊗   ⊗   ⊗   ⊗</text>
  <text x="100" y="110" fill="#64748b" font-size="14">⊗   ⊗   ⊗   ⊗   ⊗   ⊗</text>
  <text x="100" y="150" fill="#64748b" font-size="14">⊗   ⊗   ⊗   ⊗   ⊗   ⊗</text>
  <path d="M 40 100 Q 120 100 160 50" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <text x="175" y="45" fill="#38bdf8" font-size="11" font-family="sans-serif" font-weight="bold">Ray 1 (Upward curve)</text>
  <line x1="40" y1="100" x2="280" y2="100" stroke="#4ade80" stroke-width="2"/>
  <text x="290" y="104" fill="#4ade80" font-size="11" font-family="sans-serif" font-weight="bold">Ray 2 (Straight)</text>
  <path d="M 40 100 Q 120 100 160 160" fill="none" stroke="#f87171" stroke-width="2"/>
  <text x="175" y="170" fill="#f87171" font-size="11" font-family="sans-serif" font-weight="bold">Ray 3 (Downward curve)</text>
</svg>
</div>
Radiations travel from left to right into a uniform magnetic field directed perpendicularly INTO the screen (⊗). Using Fleming's Left-Hand Rule, identify Ray 1, Ray 2, and Ray 3:""",
     ["Ray 1 = Alpha (α) rays, Ray 2 = Gamma (γ) rays, Ray 3 = Beta (β) rays",
      "Ray 1 = Beta rays, Ray 2 = Alpha rays, Ray 3 = Gamma rays",
      "Ray 1 = Gamma rays, Ray 2 = Beta rays, Ray 3 = Alpha rays",
      "Ray 1 = Neutrons, Ray 2 = Protons, Ray 3 = Electrons"],
     "A", "OSC", "hard",
     "By Fleming's Left-Hand Rule (or F = q(v x B)): positive charges (alpha) experience an upward Lorentz force; negative charges (beta) experience a downward force; neutral photons (gamma) experience zero force and travel undeflected."),

    # 77: Cancer Radiotherapy with Cobalt-60
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <circle cx="200" cy="115" r="22" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
  <text x="200" y="119" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Tumor</text>
  <line x1="80" y1="40" x2="185" y2="105" stroke="#4ade80" stroke-width="2"/>
  <line x1="320" y1="40" x2="215" y2="105" stroke="#4ade80" stroke-width="2"/>
  <line x1="200" y1="30" x2="200" y2="92" stroke="#4ade80" stroke-width="2"/>
  <text x="200" y="20" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Multiple intersecting Cobalt-60 γ-ray beams</text>
  <text x="200" y="165" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Max dose concentrated on tumor while sparing healthy tissue</text>
</svg>
</div>
Why does modern cancer radiation therapy use multiple intersecting weak gamma beams from different angles rather than a single intense beam?""",
     ["Intersecting beams deliver a lethal cumulative dose at the tumor focus while keeping the dose through surrounding healthy tissue below damaging thresholds",
      "To illuminate the tumor like a spotlight for surgeons",
      "Because gamma rays cannot be focused by a single lens",
      "To make the tumor glow in different colors"],
     "A", "OSC", "hard",
     "Each individual beam passes through healthy skin and organs with minimal harmless exposure, but their geometrical intersection delivers maximum destructive ionizing energy directly to malignant cells."),

    # 78: Medical Diagnostic Tracer (Thyroid I-131)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#18181b"/>
  <rect x="40" y="55" width="130" height="70" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="105" y="80" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Oral Dose I-131</text>
  <text x="105" y="100" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">(Sodium iodide tracer)</text>
  <path d="M 175 90 L 225 90" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="230,90 220,85 220,95" fill="#38bdf8"/>
  <rect x="235" y="45" width="135" height="90" rx="6" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="302" y="75" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Thyroid Gland</text>
  <text x="302" y="95" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Concentrates 80% iodine</text>
  <text x="302" y="115" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">Gamma camera scans</text>
</svg>
</div>
Why is Iodine-131 used specifically for thyroid gland examination rather than other radioisotopes like Cobalt-60 or Carbon-14?""",
     ["The thyroid gland is the only organ that actively and biologically concentrates iodine from the bloodstream",
      "Iodine-131 does not emit any radiation",
      "Iodine-131 is the cheapest isotope available",
      "Cobalt-60 is an organic fat molecule"],
     "A", "OSC", "medium",
     "The thyroid gland synthesizes thyroxine hormones using iodine. It absorbs over 80% of circulating iodine, providing organ-specific targeting without affecting other tissues."),

    # 79: Industrial Thickness Gauge with Beta Rays
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="40" y="85" width="320" height="18" fill="#cbd5e1"/>
  <text x="200" y="98" fill="#0f172a" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Moving Paper / Plastic Sheet</text>
  <circle cx="200" cy="40" r="14" fill="#facc15"/>
  <text x="200" y="20" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Beta Source (Sr-90)</text>
  <line x1="200" y1="55" x2="200" y2="85" stroke="#facc15" stroke-width="2" stroke-dasharray="3,3"/>
  <line x1="200" y1="103" x2="200" y2="135" stroke="#facc15" stroke-width="2" stroke-dasharray="3,3"/>
  <rect x="160" y="135" width="80" height="30" rx="4" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
  <text x="200" y="154" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">GM Detector</text>
</svg>
</div>
In an automated paper mill, what signal does the detector register if the paper sheet becomes accidentally thicker than the target specification?""",
     ["The count rate decreases because the thicker sheet absorbs more beta radiation",
      "The count rate increases to infinity",
      "The detector emits visible laser sparks",
      "The paper immediately burns into ashes"],
     "A", "OSC", "hard",
     "Beta radiation absorption follows an exponential attenuation law with thickness. A thicker sheet absorbs more beta electrons, reducing the detected count rate and signaling rollers to compress harder."),

    # 80: Food Irradiation & Sprout Inhibition
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#18181b"/>
  <rect x="40" y="50" width="130" height="80" rx="6" fill="#27272a" stroke="#f87171" stroke-width="2"/>
  <text x="105" y="80" fill="#f87171" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Non-Irradiated Onions</text>
  <text x="105" y="105" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Sprouts & rots in 2 weeks</text>
  <rect x="230" y="50" width="130" height="80" rx="6" fill="#27272a" stroke="#4ade80" stroke-width="2"/>
  <text x="295" y="80" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Gamma Irradiated (Co-60)</text>
  <text x="295" y="105" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Fresh & dormant for months</text>
</svg>
</div>
How does controlled gamma irradiation prevent sprouting in stored potatoes and onions without altering nutritional value?""",
     ["It inhibits mitotic cell division in the meristematic sprout buds by disrupting sprout cell DNA",
      "It completely freezes the vegetable into ice",
      "It coats the surface with a layer of metallic lead",
      "It converts carbohydrates into liquid water"],
     "A", "OSC", "medium",
     "Low-dose gamma irradiation selectively damages the DNA of actively dividing meristematic cells in the eyes/buds, keeping them dormant during long-term storage without affecting nutrient content."),

    # 81: Smoke Detector Ionization Chamber
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <circle cx="80" cy="95" r="12" fill="#facc15"/>
  <text x="80" y="70" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Am-241 Source</text>
  <line x1="95" y1="95" x2="160" y2="95" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
  <text x="130" y="85" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">α particles</text>
  <rect x="170" y="60" width="190" height="70" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="265" y="85" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Ionized Air (Current flows)</text>
  <text x="265" y="110" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle">Smoke enters -> Current drops -> Alarm!</text>
</svg>
</div>
In an ionization-type smoke detector, why is an alpha emitter (Americium-241) utilized rather than a beta or gamma emitter?""",
     ["Alpha particles produce high ionization in the narrow air gap between plates, so smoke particles easily absorb the alpha rays and interrupt the electric current",
      "Alpha particles can shoot through concrete walls to warn neighbors",
      "Beta and gamma rays are not allowed by fire departments",
      "Americium glows red in the dark to attract smoke"],
     "A", "OSC", "hard",
     "Because alpha particles have extremely high specific ionization, they ionize air efficiently across a tiny 1-2 cm gap. Heavy smoke particles attach to ions, dropping the current drastically and triggering the sensor."),

    # 82: Geiger-Muller Tube mechanism
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <rect x="50" y="55" width="280" height="80" rx="8" fill="#27272a" stroke="#94a3b8" stroke-width="2"/>
  <line x1="70" y1="95" x2="310" y2="95" stroke="#facc15" stroke-width="3"/>
  <text x="190" y="85" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Central Anode Wire (+)</text>
  <text x="190" y="125" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Cylindrical Cathode Wall (-)</text>
  <line x1="15" y1="95" x2="48" y2="95" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="50,95 40,90 40,100" fill="#38bdf8"/>
  <text x="25" y="85" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Ray in</text>
  <rect x="340" y="70" width="50" height="50" rx="4" fill="#3b82f6"/>
  <text x="365" y="100" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Counter</text>
</svg>
</div>
When an ionizing radiation enters a Geiger-Muller tube, what produces the electrical pulse recorded by the digital counter?""",
     ["Townsend avalanche: initial ions are accelerated by the high electric field, causing secondary collision ionization that produces a measurable electrical pulse",
      "The radioactive ray hits the wire and causes a physical vibration like a guitar string",
      "The gas inside catches fire and burns the circuit",
      "The tube creates a miniature nuclear explosion"],
     "A", "OSC", "hard",
     "The incoming ionizing photon or particle creates primary electron-ion pairs. In the intense electric field near the central anode wire, electrons gain enough energy to cause exponential secondary ionization (Townsend avalanche), creating a detectable pulse.")
]

all_questions = []

# Exam: 40 questions (1-40)
for idx, item in enumerate(exam_data):
    qnum = idx + 1
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "exam", "standard", item[5])
    )

# Practice: 30 questions (41-70)
for idx, item in enumerate(practice_data):
    qnum = idx + 41
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "practice", "standard", item[5])
    )

# Mock: 12 questions (71-82)
for idx, item in enumerate(mock_data):
    qnum = idx + 71
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "mock", "foundation", item[5])
    )

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE}")

output_path = os.path.join(os.path.dirname(__file__), "ch14_topic3.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
