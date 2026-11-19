const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');
const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[trimmed.slice(0, idx).trim()] = v;
    }
  }
});
const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

// Concise, crisp explanations map for all 140 questions in MH-8-SCI-5
// Written strictly to pedagogical standard: 1-3 sentences, direct conceptual depth, zero boilerplate headers, zero option letter references.
const cleanExplanations = {
  // --- 5.2.1: Alpha Particle Scattering Experiment ---
  'MH-8-SCI-5-5.2.1-OSC-001': 'Rutherford used alpha particles (\(\\alpha\)-particles) emitted by a radioactive source, which are fast-moving doubly positively charged helium ions (\(^4_2\\text{He}^{2+}\)) with a mass of \(4\\text{ u}\).',
  'MH-8-SCI-5-5.2.1-OSC-002': 'Gold is exceptionally malleable and can be hammered into an extremely thin sheet of about \(10^{-7}\\text{ m}\) (around 1000 atoms thick), allowing alpha particles to interact with individual atoms without overlapping layers.',
  'MH-8-SCI-5-5.2.1-OSC-003': 'A circular screen coated with zinc sulfide (\(\\text{ZnS}\)) was placed around the gold foil to detect scattered alpha particles, which produced tiny flashes of light (scintillations) when striking the phosphor screen.',
  'MH-8-SCI-5-5.2.1-OSC-004': 'Because more than 99% of the alpha particles passed straight through the gold foil without any deflection, Rutherford concluded that most of the space inside an atom is completely empty.',
  'MH-8-SCI-5-5.2.1-OSC-005': 'Only about 1 in 20,000 alpha particles bounced straight back (\(180^\\circ\)), proving that the positive charge and mass must be concentrated in an extraordinarily small, dense core.',
  'MH-8-SCI-5-5.2.1-OSC-006': 'Under Ernest Rutherford\'s guidance, the microscopic observation and counting of scintillations were physically carried out by his associates Hans Geiger and Ernest Marsden.',
  'MH-8-SCI-5-5.2.1-OSC-007': 'Only an ultra-dense, concentrated positive charge can exert the immense repulsive electrostatic Coulomb force required to repel a fast, heavy alpha particle backward.',
  'MH-8-SCI-5-5.2.1-OSC-008': 'Rutherford\'s scattering law shows that the number of scattered particles is inversely proportional to \(\\sin^4(\\theta / 2)\), meaning wide-angle deflections are extremely rare.',
  'MH-8-SCI-5-5.2.1-OSC-009': 'The radioactive source was placed inside a thick lead block with a narrow slit to absorb stray radiation and collimate the alpha particles into a sharp, straight beam.',
  'MH-8-SCI-5-5.2.1-OSC-010': 'The impact parameter is the perpendicular distance between the initial straight-line trajectory of the incident alpha particle and the center of the target nucleus.',

  // --- 5.2.2: Nuclear Model of Atom ---
  'MH-8-SCI-5-5.2.2-OSC-001': 'According to Rutherford\'s nuclear model, almost the entire mass and all positive charge of an atom are concentrated in an extremely small, dense central core called the nucleus.',
  'MH-8-SCI-5-5.2.2-OSC-002': 'The radius of an atom is approximately \(10^{-10}\\text{ m}\) while the radius of the nucleus is about \(10^{-15}\\text{ m}\), making the atom about \(10^5\) (100,000) times larger than its nucleus.',
  'MH-8-SCI-5-5.2.2-OSC-003': 'Negatively charged electrons revolve around the nucleus in orbits, analogous to planets revolving around the Sun in the solar system.',
  'MH-8-SCI-5-5.2.2-OSC-004': 'The electrostatic attraction between the positively charged nucleus and negatively charged electrons provides the necessary centripetal force for orbital revolution.',
  'MH-8-SCI-5-5.2.2-OSC-005': 'An atom is electrically neutral as a whole because the total positive charge in the nucleus equals the total negative charge of all revolving electrons.',
  'MH-8-SCI-5-5.2.2-OSC-006': 'Electrons have negligible mass (\(1/1837\\text{ u}\)), so virtually 100% of the atom\'s mass is concentrated in the nucleus where protons and neutrons reside.',
  'MH-8-SCI-5-5.2.2-OSC-007': 'The vast majority of the volume of an atom consists of empty space between the tiny central nucleus and the outer revolving electrons.',
  'MH-8-SCI-5-5.2.2-OSC-008': 'Rutherford disproved J.J. Thomson\'s plum pudding model, which had incorrectly assumed that positive charge was spread uniformly throughout the atomic sphere.',
  'MH-8-SCI-5-5.2.2-OSC-009': 'The nuclear density of an atom is exceptionally high (about \(10^{17}\\text{ kg/m}^3\)) because nearly the entire mass of the atom is packed into a radius of only \(10^{-15}\\text{ m}\).',
  'MH-8-SCI-5-5.2.2-OSC-010': 'Rutherford\'s model is termed a planetary or nuclear model because the central heavy nucleus and surrounding orbiting electrons resemble the Sun and revolving planets.',

  // --- 5.2.3: Drawbacks of Rutherford Model ---
  'MH-8-SCI-5-5.2.3-OSC-001': 'According to Maxwell\'s classical electromagnetic theory, an accelerating charged particle (like an orbiting electron) must continuously radiate energy, causing it to spiral into the nucleus in \(10^{-8}\\text{ s}\).',
  'MH-8-SCI-5-5.2.3-OSC-002': 'Because classical physics predicts continuous energy loss and atomic collapse, Rutherford\'s model could not explain the inherent physical stability of real atoms.',
  'MH-8-SCI-5-5.2.3-OSC-003': 'Rutherford\'s model could not explain the discrete, sharp line emission spectra of elements like Hydrogen, as continuous spiraling should produce a continuous spectrum.',
  'MH-8-SCI-5-5.2.3-OSC-004': 'The model did not specify the allowed energy levels, radii of orbits, or the distribution and arrangement of electrons across different paths.',
  'MH-8-SCI-5-5.2.3-OSC-005': 'Circular motion involves constant change in the direction of velocity, which means orbiting electrons undergo continuous centripetal acceleration and should emit electromagnetic radiation under classical physics.',
  'MH-8-SCI-5-5.2.3-OSC-006': 'Classical electrodynamics applied to Rutherford\'s model calculates that an electron would collapse into the nucleus in less than a fraction of a microsecond (\(\\approx 10^{-8}\\text{ s}\)).',
  'MH-8-SCI-5-5.2.3-OSC-007': 'Niels Bohr resolved this fundamental drawback in 1913 by introducing quantum postulates that restrict electrons to non-radiating, stable stationary orbits.',
  'MH-8-SCI-5-5.2.3-OSC-008': 'Experimental observations prove that atoms possess sharp characteristic line spectra with specific wavelengths rather than a broad, continuous rainbow of radiation.',
  'MH-8-SCI-5-5.2.3-OSC-009': 'Rutherford could not explain why accelerating electrons do not radiate energy while moving in circular paths around the nucleus.',
  'MH-8-SCI-5-5.2.3-OSC-010': 'The main scientific limitation of Rutherford\'s model was the conflict between classical electrodynamics and the observed mechanical and optical stability of atoms.',

  // --- 5.3.1: Bohr Stable Orbit Atomic Model ---
  'MH-8-SCI-5-5.3.1-OSC-001': 'Niels Bohr postulated in 1913 that electrons revolve around the nucleus only in certain discrete, stable circular orbits without radiating energy.',
  'MH-8-SCI-5-5.3.1-OSC-002': 'The stable orbits are designated by principal quantum numbers \(n = 1, 2, 3, 4\\dots\) or by the letters K, L, M, N from the innermost shell outward.',
  'MH-8-SCI-5-5.3.1-OSC-003': 'The K-shell (\(n = 1\)) is closest to the nucleus and has the lowest energy level, representing the ground state of the electron.',
  'MH-8-SCI-5-5.3.1-OSC-004': 'As the distance from the nucleus increases (\(n = 1 \\to 2 \\to 3 \\to 4\)), the energy of the stationary orbits increases progressively.',
  'MH-8-SCI-5-5.3.1-OSC-005': 'According to Bohr\'s quantum condition, an electron can only revolve in orbits where its orbital angular momentum is an integral multiple of \(h / (2\\pi)\): \(L = mvr = n \\frac{h}{2\\pi}\).',
  'MH-8-SCI-5-5.3.1-OSC-006': 'While an electron remains in a permitted stationary orbit, it does not radiate or lose any energy, thereby maintaining atomic stability.',
  'MH-8-SCI-5-5.3.1-OSC-007': 'The maximum electron capacity of any shell is given by the formula \(2n^2\), where \(n\) is the principal quantum number (shell number).',
  'MH-8-SCI-5-5.3.1-OSC-008': 'For the L-shell (\(n = 2\)), the maximum electron holding capacity is \(2(2)^2 = 8\) electrons.',
  'MH-8-SCI-5-5.3.1-OSC-009': 'For the M-shell (\(n = 3\)), the theoretical maximum electron capacity is \(2(3)^2 = 18\) electrons.',
  'MH-8-SCI-5-5.3.1-OSC-010': 'Bohr successfully combined Rutherford\'s nuclear discovery with Max Planck\'s quantum theory of radiation to explain both atomic stability and discrete spectra.',

  // --- 5.3.2: Energy Emission & Absorption ---
  'MH-8-SCI-5-5.3.2-OSC-001': 'An electron absorbs a quantum of energy (\(\\Delta E = h\\nu\)) when it transitions from an inner orbit of lower energy to an outer orbit of higher energy.',
  'MH-8-SCI-5-5.3.2-OSC-002': 'When an electron jumps from a higher energy outer orbit to a lower energy inner orbit, it emits energy in the form of a photon of electromagnetic radiation: \(\\Delta E = E_2 - E_1 = h\\nu\).',
  'MH-8-SCI-5-5.3.2-OSC-003': 'The energy difference between two orbits determines the exact frequency (\(\\nu\)) and wavelength (\(\\lambda\)) of the emitted light photon according to \(\\Delta E = \\frac{hc}{\\lambda}\).',
  'MH-8-SCI-5-5.3.2-OSC-004': 'The normal state of an atom where electrons occupy the lowest possible permitted energy levels is called the ground state.',
  'MH-8-SCI-5-5.3.2-OSC-005': 'An atom enters an excited state when an electron absorbs energy and jumps to a higher energy level, where it typically stays for only about \(10^{-8}\\text{ s}\) before returning.',
  'MH-8-SCI-5-5.3.2-OSC-006': 'Atomic emission spectra consist of sharp discrete lines because electrons can only transition between quantized, fixed energy levels.',
  'MH-8-SCI-5-5.3.2-OSC-007': 'In a hydrogen atom, transitions of electrons from higher levels to the \(n = 2\) level (Balmer series) emit photons in the visible spectrum.',
  'MH-8-SCI-5-5.3.2-OSC-008': 'The constant \(h\) in the photon energy equation \(E = h\\nu\) is Planck\'s constant, with an approximate value of \(6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s}\).',
  'MH-8-SCI-5-5.3.2-OSC-009': 'Electrons cannot absorb fractional amounts of energy between orbits; they only absorb the precise quantum equal to the energy gap \(\\Delta E\) between the two states.',
  'MH-8-SCI-5-5.3.2-OSC-010': 'Flame test colors (like yellow for sodium and red for strontium) result from characteristic visible photons emitted when thermal-excited electrons drop back to ground states.',

  // --- 5.4.1: Protons ---
  'MH-8-SCI-5-5.4.1-OSC-001': 'A proton is a subatomic particle located in the nucleus that carries a unit positive electric charge of \(+1.6 \\times 10^{-19}\\text{ C}\) (or \(+1e\)).',
  'MH-8-SCI-5-5.4.1-OSC-002': 'The mass of a single proton is approximately \(1.6726 \\times 10^{-27}\\text{ kg}\), which is defined as approximately \(1\\text{ u}\) (atomic mass unit).',
  'MH-8-SCI-5-5.4.1-OSC-003': 'The number of protons in the nucleus of an atom defines its atomic number (\(Z\)), which uniquely determines the chemical identity of the element.',
  'MH-8-SCI-5-5.4.1-OSC-004': 'Ernest Rutherford is credited with the discovery and naming of the proton after identifying hydrogen nuclei in alpha particle transmutation experiments in 1919.',
  'MH-8-SCI-5-5.4.1-OSC-005': 'A hydrogen ion (\(\\text{H}^+\)) is simply a bare single proton, as a neutral hydrogen atom (\(^1_1\\text{H}\)) consists of only one proton and one electron.',
  'MH-8-SCI-5-5.4.1-OSC-006': 'The proton is approximately 1836 times heavier than an electron, meaning electrons contribute negligibly to total atomic mass.',
  'MH-8-SCI-5-5.4.1-OSC-007': 'Inside the nucleus, protons and neutrons are held together against electrostatic repulsion by the extremely powerful, short-range strong nuclear force.',
  'MH-8-SCI-5-5.4.1-OSC-008': 'The symbol for a proton is \(\\text{p}\) or \(^1_1\\text{H}\) or \(^1_1\\text{p}\), denoting a unit mass of 1 and a unit charge of +1.',
  'MH-8-SCI-5-5.4.1-OSC-009': 'In any electrically neutral atom, the total positive charge from all nuclear protons is exactly balanced by the total negative charge of orbital electrons.',
  'MH-8-SCI-5-5.4.1-OSC-010': 'The positive charge of a nucleus with atomic number \(Z\) is equal to \(+Ze\), where \(e = 1.602 \\times 10^{-19}\\text{ C}\).',

  // --- 5.4.2: Neutrons ---
  'MH-8-SCI-5-5.4.2-OSC-001': 'The neutron is an electrically neutral subatomic particle situated in the nucleus, carrying zero charge (\(0\\text{ C}\)).',
  'MH-8-SCI-5-5.4.2-OSC-002': 'The neutron was experimentally discovered by British physicist James Chadwick in 1932 by bombarding beryllium with alpha particles.',
  'MH-8-SCI-5-5.4.2-OSC-003': 'The mass of a neutron is approximately \(1.6749 \\times 10^{-27}\\text{ kg}\) (\(\\approx 1\\text{ u}\)), which is slightly greater than the mass of a proton.',
  'MH-8-SCI-5-5.4.2-OSC-004': 'Protons and neutrons reside together in the atomic nucleus and are collectively referred to as nucleons.',
  'MH-8-SCI-5-5.4.2-OSC-005': 'The standard ordinary hydrogen atom (Protium, \(^1_1\\text{H}\)) is the only atomic nucleus that contains zero neutrons.',
  'MH-8-SCI-5-5.4.2-OSC-006': 'The symbol for a neutron is \(\\text{n}\) or \(^1_0\\text{n}\), indicating a mass number of 1 and an electric charge of 0.',
  'MH-8-SCI-5-5.4.2-OSC-007': 'The number of neutrons in a nucleus is calculated by subtracting the atomic number from the mass number: \(N = A - Z\).',
  'MH-8-SCI-5-5.4.2-OSC-008': 'Because neutrons carry no electric charge, they are not deflected by electric or magnetic fields and can easily penetrate atomic nuclei.',
  'MH-8-SCI-5-5.4.2-OSC-009': 'Neutrons act as a nuclear "glue", providing attractive strong nuclear force that overcomes the electrostatic repulsion between positively charged protons.',
  'MH-8-SCI-5-5.4.2-OSC-010': 'A carbon-12 nucleus (\(^{12}_6\\text{C}\)) contains \(A - Z = 12 - 6 = 6\) neutrons and 6 protons.',

  // --- 5.4.3: Electrons ---
  'MH-8-SCI-5-5.4.3-OSC-001': 'An electron is a negatively charged subatomic particle carrying a unit charge of \(-1.6 \\times 10^{-19}\\text{ C}\) (or \(-1e\)).',
  'MH-8-SCI-5-5.4.3-OSC-002': 'The electron was discovered in 1897 by J.J. Thomson through cathode ray tube experiments measuring the charge-to-mass ratio (\(e/m\)).',
  'MH-8-SCI-5-5.4.3-OSC-003': 'The rest mass of an electron is approximately \(9.109 \\times 10^{-31}\\text{ kg}\), which is approximately \(1/1837\\text{ u}\) of a proton\'s mass.',
  'MH-8-SCI-5-5.4.3-OSC-004': 'Electrons are symbolized by \(\\text{e}^-\) or \(^0_{-1}\\text{e}\), indicating negligible mass (0) and a single unit negative charge (-1).',
  'MH-8-SCI-5-5.4.3-OSC-005': 'Electrons move rapidly in discrete orbits outside the nucleus, occupying the major volume of the atom while contributing almost nothing to its weight.',
  'MH-8-SCI-5-5.4.3-OSC-006': 'Electrons in the outermost shell are called valence electrons and are responsible for chemical bonding, reactivity, and compound formation.',
  'MH-8-SCI-5-5.4.3-OSC-007': 'When an atom gains one or more electrons, it forms a negatively charged ion called an anion; when it loses electrons, it forms a cation.',
  'MH-8-SCI-5-5.4.3-OSC-008': 'Cathode rays are streams of fast-moving electrons emitted from the negative cathode in a vacuum discharge tube under high voltage.',
  'MH-8-SCI-5-5.4.3-OSC-009': 'The charge of an electron was accurately determined by Robert Millikan in 1909 through his celebrated oil drop experiment.',
  'MH-8-SCI-5-5.4.3-OSC-010': 'Unlike protons and neutrons (which are composed of quarks), electrons are fundamental elementary leptons that cannot be broken down into smaller components.',

  // --- 5.5.1: Atomic Number (Z) ---
  'MH-8-SCI-5-5.5.1-OSC-001': 'The atomic number (\(Z\)) of an element is defined as the total number of protons present in the nucleus of an atom.',
  'MH-8-SCI-5-5.5.1-OSC-002': 'In an electrically neutral atom, the atomic number (\(Z\)) equals both the number of nuclear protons and the number of orbital electrons.',
  'MH-8-SCI-5-5.5.1-OSC-003': 'The atomic number is the fundamental property of an element and determines its position in the Modern Periodic Table as established by Henry Moseley.',
  'MH-8-SCI-5-5.5.1-OSC-004': 'An element with atomic number \(Z = 8\) has 8 protons in its nucleus, which uniquely identifies it as Oxygen (\(\\text{O}\)).',
  'MH-8-SCI-5-5.5.1-OSC-005': 'In standard nuclear notation (\(^A_Z\\text{X}\)), the atomic number \(Z\) is written as a subscript on the bottom-left of the chemical symbol.',
  'MH-8-SCI-5-5.5.1-OSC-006': 'No two different chemical elements can have the same atomic number; each element has its own distinct number of protons.',
  'MH-8-SCI-5-5.5.1-OSC-007': 'Chemical properties and bonding behavior are determined by the electron count and configuration, which directly depend on the atomic number \(Z\).',
  'MH-8-SCI-5-5.5.1-OSC-008': 'For Sodium (\(\\text{Na}\)), \(Z = 11\), meaning every neutral sodium atom contains exactly 11 protons and 11 electrons.',
  'MH-8-SCI-5-5.5.1-OSC-009': 'The atomic number \(Z\) is always an integer (\(1, 2, 3\\dots\)) because protons cannot be divided into fractional units in an atomic nucleus.',
  'MH-8-SCI-5-5.5.1-OSC-010': 'When an atom forms an ion by losing or gaining electrons, its atomic number \(Z\) remains completely unchanged because nuclear protons are not transferred.',

  // --- 5.5.2: Mass Number (A) ---
  'MH-8-SCI-5-5.5.2-OSC-001': 'The mass number (\(A\)) of an atom is defined as the total sum of protons (\(Z\)) and neutrons (\(N\)) present in its nucleus: \(A = Z + N\).',
  'MH-8-SCI-5-5.5.2-OSC-002': 'The number of neutrons in an atomic nucleus is found by subtracting the atomic number from the mass number: \(N = A - Z\).',
  'MH-8-SCI-5-5.5.2-OSC-003': 'In standard nuclear notation (\(^A_Z\\text{X}\)), the mass number \(A\) is placed as a superscript at the top-left of the element symbol.',
  'MH-8-SCI-5-5.5.2-OSC-004': 'For a Chlorine atom denoted as \(^{35}_{17}\\text{Cl}\), the number of neutrons is \(N = 35 - 17 = 18\) neutrons.',
  'MH-8-SCI-5-5.5.2-OSC-005': 'Atoms of different elements that share the exact same mass number (\(A\)) but have different atomic numbers (\(Z\)) are called isobars (e.g. \(^{40}_{18}\\text{Ar}\) and \(^{40}_{20}\\text{Ca}\)).',
  'MH-8-SCI-5-5.5.2-OSC-006': 'Electrons are excluded from the mass number calculation because their individual mass is negligible compared to protons and neutrons.',
  'MH-8-SCI-5-5.5.2-OSC-007': 'For Carbon-14 (\(^{14}_6\\text{C}\)), the nucleus contains 6 protons and \(14 - 6 = 8\) neutrons.',
  'MH-8-SCI-5-5.5.2-OSC-008': 'The mass number is always an integer because it represents a discrete count of whole nucleons (protons plus neutrons).',
  'MH-8-SCI-5-5.5.2-OSC-009': 'For Uranium-238 (\(^{238}_{92}\\text{U}\)), the nucleus contains \(238 - 92 = 146\) neutrons and 92 protons.',
  'MH-8-SCI-5-5.5.2-OSC-010': 'The actual atomic weight of an element is a weighted average of the mass numbers of all its naturally occurring isotopes based on their abundance.',

  // --- 5.5.3: Isotopes ---
  'MH-8-SCI-5-5.5.3-OSC-001': 'Isotopes are atoms of the same chemical element having identical atomic number (\(Z\)) but different mass numbers (\(A\)) due to differing numbers of neutrons.',
  'MH-8-SCI-5-5.5.3-OSC-002': 'Hydrogen has three isotopes: Protium (\(^1_1\\text{H}\), 0 neutrons), Deuterium (\(^2_1\\text{H}\), 1 neutron), and radioactive Tritium (\(^3_1\\text{H}\), 2 neutrons).',
  'MH-8-SCI-5-5.5.3-OSC-003': 'Isotopes of an element have nearly identical chemical properties because they have the same number of valence electrons and identical electronic configurations.',
  'MH-8-SCI-5-5.5.3-OSC-004': 'Isotopes differ in physical properties (such as density, boiling point, and nuclear stability) because of their difference in mass and neutron count.',
  'MH-8-SCI-5-5.5.3-OSC-005': 'Naturally occurring Carbon exists mainly as stable Carbon-12 (\(^{12}_6\\text{C}\)), stable Carbon-13 (\(^{13}_6\\text{C}\)), and radioactive Carbon-14 (\(^{14}_6\\text{C}\)).',
  'MH-8-SCI-5-5.5.3-OSC-006': 'Chlorine occurs naturally as \(^{35}\\text{Cl}\) (75%) and \(^{37}\\text{Cl}\) (25%), giving it a fractional average atomic mass of \(35.5\\text{ u}\).',
  'MH-8-SCI-5-5.5.3-OSC-007': 'Isotopes occupy the exact same position in the Modern Periodic Table because the table is organized strictly by atomic number (\(Z\)).',
  'MH-8-SCI-5-5.5.3-OSC-008': 'The term "isotope" was coined by Frederick Soddy from Greek words meaning "at the same place" on the periodic table.',
  'MH-8-SCI-5-5.5.3-OSC-009': 'Heavy water (\(\\text{D}_2\\text{O}\)) is formed from deuterium (hydrogen-2) and oxygen, and is used as a neutron moderator in nuclear power reactors.',
  'MH-8-SCI-5-5.5.3-OSC-010': 'Radioactive isotopes (radioisotopes) have unstable nuclei that spontaneously decay by emitting radiation such as alpha, beta, or gamma rays.',

  // --- 5.5.4: Uses of Isotopes ---
  'MH-8-SCI-5-5.5.4-OSC-001': 'Uranium-235 (\(^{235}\\text{U}\)) is widely used as nuclear fuel in power generation reactors to produce electrical energy via controlled nuclear fission.',
  'MH-8-SCI-5-5.5.4-OSC-002': 'Cobalt-60 (\(^{60}\\text{Co}\)) emits high-energy gamma rays and is commonly used in radiation therapy for the medical treatment of cancer tumors.',
  'MH-8-SCI-5-5.5.4-OSC-003': 'Iodine-131 (\(^{131}\\text{I}\)) is medically utilized for the diagnosis and radiotherapy treatment of thyroid gland disorders, including goiter and thyroid cancer.',
  'MH-8-SCI-5-5.5.4-OSC-004': 'Carbon-14 dating is an archeological technique used to determine the age of ancient organic fossils and historical wooden artifacts up to 50,000 years old.',
  'MH-8-SCI-5-5.5.4-OSC-005': 'Sodium-24 (\(^{24}\\text{Na}\)) is employed as a radioactive tracer in cardiology to detect blood circulatory blocks and blood clots.',
  'MH-8-SCI-5-5.5.4-OSC-006': 'Phosphorus-32 (\(^{32}\\text{P}\)) is used in agricultural science to track plant nutrient uptake and in medicine to treat leukemia (blood cancer).',
  'MH-8-SCI-5-5.5.4-OSC-007': 'Americium-241 (\(^{241}\\text{Am}\)) is an alpha-emitter widely used in commercial household ionization smoke detectors.',
  'MH-8-SCI-5-5.5.4-OSC-008': 'Food irradiation uses gamma emissions from Cobalt-60 or Cesium-137 to sterilize packaged foods and prolong preservation by killing microbes and pests.',
  'MH-8-SCI-5-5.5.4-OSC-009': 'Iridium-192 is used in industrial radiography to inspect internal cracks and flaws in metal castings and pipeline welds without destroying them.',
  'MH-8-SCI-5-5.5.4-OSC-010': 'Technetium-99m (\(^{99m}\\text{Tc}\)) is the most widely used medical radioisotope for imaging organs like the brain, heart, bones, and kidneys.',

  // --- 5.6.1: Electronic Configuration & Shells ---
  'MH-8-SCI-5-5.6.1-OSC-001': 'The distribution of electrons across the different energy shells (K, L, M, N) of an atom is called its electronic configuration.',
  'MH-8-SCI-5-5.6.1-OSC-002': 'The maximum number of electrons that can be accommodated in any shell is given by Bohr-Bury\'s \(2n^2\) rule, where \(n\) is the shell number.',
  'MH-8-SCI-5-5.6.1-OSC-003': 'For the first shell (K, \(n = 1\)), the maximum electron holding capacity is \(2(1)^2 = 2\) electrons.',
  'MH-8-SCI-5-5.6.1-OSC-004': 'For the second shell (L, \(n = 2\)), the maximum electron holding capacity is \(2(2)^2 = 8\) electrons.',
  'MH-8-SCI-5-5.6.1-OSC-005': 'For the third shell (M, \(n = 3\)), the theoretical maximum electron capacity is \(2(3)^2 = 18\) electrons.',
  'MH-8-SCI-5-5.6.1-OSC-006': 'For the fourth shell (N, \(n = 4\)), the theoretical maximum electron capacity is \(2(4)^2 = 32\) electrons.',
  'MH-8-SCI-5-5.6.1-OSC-007': 'According to the octet rule, the outermost valence shell of an atom cannot hold more than 8 electrons, regardless of its theoretical \(2n^2\) capacity.',
  'MH-8-SCI-5-5.6.1-OSC-008': 'Sodium (\(Z = 11\)) has 11 electrons distributed as 2 in K-shell, 8 in L-shell, and 1 in M-shell, written as (2, 8, 1).',
  'MH-8-SCI-5-5.6.1-OSC-009': 'Chlorine (\(Z = 17\)) has an electronic configuration of (2, 8, 7), needing 1 more electron to complete its stable octet.',
  'MH-8-SCI-5-5.6.1-OSC-010': 'Noble gases (like Neon 2, 8 and Argon 2, 8, 8) have complete octets (or duplet for Helium 2), making them chemically inert and unreactive.',

  // --- 5.6.2: Valence Electrons & Valency ---
  'MH-8-SCI-5-5.6.2-OSC-001': 'Valence electrons are the electrons present in the outermost shell of an atom, which directly dictate the chemical reactivity and valency of the element.',
  'MH-8-SCI-5-5.6.2-OSC-002': 'Valency is the combining capacity of an atom, defined as the number of electrons lost, gained, or shared to achieve a stable octet (or duplet) configuration.',
  'MH-8-SCI-5-5.6.2-OSC-003': 'For elements with 1, 2, 3, or 4 valence electrons, the valency is equal to the number of valence electrons (e.g. Sodium has 1 valence electron, so valency = 1).',
  'MH-8-SCI-5-5.6.2-OSC-004': 'For elements with 5, 6, 7, or 8 valence electrons, valency is calculated by subtracting valence electrons from 8: \(\\text{Valency} = 8 - \\text{valence electrons}\).',
  'MH-8-SCI-5-5.6.2-OSC-005': 'Oxygen has an electronic configuration of (2, 6) with 6 valence electrons; its valency is \(8 - 6 = 2\).',
  'MH-8-SCI-5-5.6.2-OSC-006': 'Carbon has an electronic configuration of (2, 4); with 4 valence electrons, it shares 4 electrons and is tetravalent (valency = 4).',
  'MH-8-SCI-5-5.6.2-OSC-007': 'Noble gases (Neon, Argon) have 8 valence electrons, so their valency is \(8 - 8 = 0\), explaining why they do not form chemical compounds under standard conditions.',
  'MH-8-SCI-5-5.6.2-OSC-008': 'Magnesium has an electronic configuration of (2, 8, 2); by losing its 2 valence electrons to form \(\\text{Mg}^{2+}\), its valency is 2.',
  'MH-8-SCI-5-5.6.2-OSC-009': 'Helium has 2 valence electrons in its only shell (K-shell), completing a stable duplet configuration and giving it a valency of 0.',
  'MH-8-SCI-5-5.6.2-OSC-010': 'Elements in the same vertical group of the Periodic Table have the same number of valence electrons and therefore exhibit identical valency and similar chemical properties.'
};

async function updateAll140() {
  console.log('=== UPDATING ALL 140 CHAPTER 5 QUESTIONS WITH CLEAN EXPLANATIONS ===');
  const batch = db.batch();
  let count = 0;

  for (const [id, exp] of Object.entries(cleanExplanations)) {
    const ref = db.collection('questions').doc(id);
    batch.update(ref, {
      explanation: exp,
      solution: exp,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });
    count++;
  }

  await batch.commit();
  console.log(`✓ Successfully updated all ${count} questions in Firestore with clean, short, foundation-grade explanations.`);
}

updateAll140().catch(console.error);
