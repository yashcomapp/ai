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

// Exact replacement dictionary for genuinely out-of-syllabus questions in MH-8-SCI-5
// Aligned 100% to Maharashtra State Board Class 8 General Science (Balbharti Ch 5)
const ch5Replacements = {
  // [1] 5.1.2-OSC-047: Convert angstrom
  'MH-8-SCI-5-5.1-OSC-047': {
    text: 'What is the approximate size (diameter) of an individual atom in metres as stated in the textbook?',
    options: ['\\(10^{-10}\\text{ m}\\)', '\\(10^{-3}\\text{ m}\\)', '\\(10^{-1}\\text{ m}\\)', '\\(10^{-6}\\text{ m}\\)'],
    correctAnswer: 'A',
    explanation: 'The typical diameter of an atom is of the order of \\(10^{-10}\\text{ metre}\\) (0.1 nanometre).'
  },

  // [2] 5.1.2-OSC-011: J.J. Thomson cathode ray deflection
  'MH-8-SCI-5-5.1.2-OSC-011': {
    text: "According to J.J. Thomson's Plum Pudding Model of the atom, how is the positive charge distributed inside an atom?",
    options: [
      'Concentrated exclusively in a tiny central nucleus',
      'Spread uniformly throughout the entire spherical volume of the atom',
      'Arranged in concentric outer circular shells',
      'Confined only to the outer boundary of the atom'
    ],
    correctAnswer: 'B',
    explanation: "In Thomson's plum pudding model, positive electric charge is spread evenly throughout the sphere of the atom, with negative electrons embedded inside it."
  },

  // [4] 5.2.1-OSC-008: Rutherford scattering formula sin^4
  'MH-8-SCI-5-5.2.1-OSC-008': {
    text: "In Rutherford's alpha-particle scattering experiment, what observation proved that most of the space inside the atom is empty?",
    options: [
      'A small fraction of alpha particles deflected through large angles',
      'One in 20,000 alpha particles bounced straight backwards',
      'All alpha particles were absorbed by the gold foil',
      'The vast majority of alpha particles passed straight through the gold foil without any deflection'
    ],
    correctAnswer: 'D',
    explanation: 'Most alpha particles passed straight through the thin gold foil without deflection, proving that most of the interior space of an atom is empty.'
  },

  // [5] 5.2.2-OSC-002: Nucleus size compared to atom
  'MH-8-SCI-5-5.2.2-OSC-002': {
    text: "How does the size of the atomic nucleus compare with the overall size of the atom in Rutherford's model?",
    options: [
      'The nucleus is approximately half the size of the atom',
      'The nucleus is extremely tiny compared to the overall size of the atom',
      'The nucleus is significantly larger than the electron orbits',
      'The nucleus and the atom have identical dimensions'
    ],
    correctAnswer: 'B',
    explanation: 'The atomic nucleus is extremely small compared to the overall size of the atom, occupying only a minute fraction of the total atomic volume.'
  },

  // [6] 5.2.2-OSC-003: Centripetal force in Rutherford model
  'MH-8-SCI-5-5.2.2-OSC-003': {
    text: "In Rutherford's atomic model, what provides the attractive force that keeps the revolving electrons in their orbits around the nucleus?",
    options: [
      'Gravitational attraction between protons and electrons',
      'Magnetic repulsion from revolving charges',
      'Nuclear strong force extending outside the nucleus',
      'Electrostatic attraction between the positively charged nucleus and negatively charged electrons'
    ],
    correctAnswer: 'D',
    explanation: 'The electrostatic force of attraction between the positively charged nucleus and the negatively charged electrons holds the revolving electrons in orbit.'
  },

  // [7] 5.2.2-OSC-010: Distance of closest approach 5 MeV
  'MH-8-SCI-5-5.2.2-OSC-010': {
    text: "Approximately what fraction of the alpha particles in Rutherford's experiment bounced back towards the source?",
    options: [
      'About 1 in 20,000 particles',
      'About 1 in 2 particles',
      'About 1 in 10 particles',
      'All of the particles'
    ],
    correctAnswer: 'A',
    explanation: 'Only about 1 out of 20,000 alpha particles rebounded through nearly 180 degrees, showing that the entire positive charge and mass are concentrated in a tiny dense nucleus.'
  },

  // [9] 5.2.2-OSC-013: Volume ratio 10^15
  'MH-8-SCI-5-5.2.2-OSC-013': {
    text: "According to Rutherford's nuclear model of the atom, where is almost the entire mass of an atom concentrated?",
    options: [
      'Evenly distributed throughout the outer electron orbits',
      'In the outer spherical boundary of the atom',
      'In a tiny, extremely dense central region called the nucleus',
      'Divided equally between revolving electrons and empty space'
    ],
    correctAnswer: 'C',
    explanation: 'Almost the entire mass and positive electric charge of an atom are concentrated in the central dense core called the nucleus.'
  },

  // [10] 5.2.3-OSC-002: Continuous emission spectrum in electrodynamics
  'MH-8-SCI-5-5.2.3-OSC-002': {
    text: "According to the established laws of classical physics, why was Rutherford's planetary model of the atom considered fundamentally unstable?",
    options: [
      'Revolving electrons would continuously radiate energy and spiral into the nucleus',
      'The positive nucleus would spontaneously repel all incoming light',
      'Electrons would gain infinite mass and break apart the atom',
      'Atoms would expand continuously until they exploded'
    ],
    correctAnswer: 'A',
    explanation: 'Classical physics dictates that an accelerating charged particle must continuously radiate energy, which would cause revolving electrons to spiral inward and collapse into the nucleus.'
  },

  // [11] 5.2.3-OSC-005: Bohr quantum condition L=mvr=nh/2pi
  'MH-8-SCI-5-5.2.3-OSC-005': {
    text: "Which scientist successfully removed the drawback of Rutherford's model in 1913 by introducing the concept of stable, non-radiating orbits?",
    options: [
      'Niels Bohr',
      'John Dalton',
      'J.J. Thomson',
      'James Chadwick'
    ],
    correctAnswer: 'A',
    explanation: "In 1913, Niels Bohr resolved the instability of Rutherford's model by postulating that electrons revolve in specific, stable orbits without radiating energy."
  },

  // [12] 5.2.3-OSC-008: Quantum mechanics foundation
  'MH-8-SCI-5-5.2.3-OSC-008': {
    text: "What major experimental fact about real atoms contradicted the collapse predicted for Rutherford's model?",
    options: [
      'Real atoms undergo continuous nuclear fusion',
      'Real atoms have no mass',
      'Real atoms are electrically charged at all times',
      'Real atoms are completely stable and do not collapse'
    ],
    correctAnswer: 'D',
    explanation: 'Matter is stable and atoms do not spontaneously collapse, proving that electrons do not spiral into the nucleus as classical physics predicted.'
  },

  // [13] 5.2.3-OSC-010: De Broglie 2pi r = n lambda
  'MH-8-SCI-5-5.2.3-OSC-010': {
    text: "In Bohr's atomic model, what prevents an electron from losing energy while it revolves in a stable orbit?",
    options: [
      'The electron stops moving while in orbit',
      'The orbit has a fixed, discrete energy level in which electrons do not radiate energy',
      'The nucleus continuously supplies electric current to the electron',
      'Gravity cancels out all electrical forces inside the atom'
    ],
    correctAnswer: 'B',
    explanation: 'In Bohr orbits, each shell has a definite energy; an electron does not radiate or lose energy as long as it remains in that stationary orbit.'
  },

  // [14] 5.2.3-OSC-011: Maxwell's theory
  'MH-8-SCI-5-5.2.3-OSC-011': {
    text: "What was the main limitation or drawback of Rutherford's nuclear model of the atom?",
    options: [
      'It could not explain the presence of electrons',
      'It claimed that all atoms are indivisible solid spheres',
      'It could not explain the electrical charge of gold atoms',
      'It could not explain why revolving electrons do not collapse into the nucleus'
    ],
    correctAnswer: 'D',
    explanation: "Rutherford's model could not explain the stability of the atom, as circular motion is accelerated motion which should theoretically cause the electron to radiate energy and fall into the nucleus."
  },

  // [15] 5.2.3-OSC-013: Discrete sharp atomic emission lines
  'MH-8-SCI-5-5.2.3-OSC-013': {
    text: "Why do different elements emit characteristic colors when their salts are heated in a flame (such as yellow for Sodium)?",
    options: [
      'Electrons absorb heat and emit light of characteristic energies when returning to lower orbits',
      'The nuclei of different elements melt at different rates in the flame',
      'The flame creates new elements with different colors',
      'Atoms burn completely and change their atomic numbers'
    ],
    correctAnswer: 'A',
    explanation: 'When heated, electrons absorb energy to jump to higher shells and then emit light of definite wavelengths when returning to lower shells, producing distinct colors.'
  },

  // [16] 5.2.3-OSC-017: Spiral collapse frequency
  'MH-8-SCI-5-5.2.3-OSC-017': {
    text: "In an atom, when an electron remains in its designated stable orbit, what happens to its energy?",
    options: [
      'Its energy decreases continuously to zero',
      'Its energy increases rapidly until it leaves the atom',
      'Its energy remains constant and unchanging',
      'Its energy fluctuates between positive and negative values'
    ],
    correctAnswer: 'C',
    explanation: 'While revolving in a permissible stable orbit, an electron has constant energy and does not radiate or absorb energy.'
  },

  // [18] 5.3.1-OSC-004: r_n proportional to n^2
  'MH-8-SCI-5-5.3.1-OSC-004': {
    text: "In Bohr's atomic model, how does the energy of an electron orbit change as its distance from the nucleus increases?",
    options: [
      'The energy decreases with increasing distance',
      'The energy of the orbit increases as the distance from the nucleus increases',
      'The energy remains exactly zero for all orbits',
      'The energy doubles and then drops to zero'
    ],
    correctAnswer: 'B',
    explanation: 'Orbits further away from the nucleus have higher energy levels (K < L < M < N).'
  },

  // [19] 5.3.1-OSC-005: Orbital angular momentum mvr=nh/2pi
  'MH-8-SCI-5-5.3.1-OSC-005': {
    text: "Which of the following electron shells is closest to the atomic nucleus in Bohr's model?",
    options: [
      'N shell',
      'L shell',
      'K shell',
      'M shell'
    ],
    correctAnswer: 'C',
    explanation: 'The K shell (corresponding to shell number \\(n = 1\\)) is the innermost orbit and closest to the nucleus.'
  },

  // [20] 5.3.1-OSC-009: Numerical Bohr radius 0.529 A
  'MH-8-SCI-5-5.3.1-OSC-009': {
    text: "What letters are officially assigned to represent the first four electron shells starting from the innermost shell outward?",
    options: [
      'K, L, M, N',
      'A, B, C, D',
      'P, Q, R, S',
      'W, X, Y, Z'
    ],
    correctAnswer: 'A',
    explanation: 'Bohr designated the electron shells outward from the nucleus as K (\\(n=1\\)), L (\\(n=2\\)), M (\\(n=3\\)), and N (\\(n=4\\)).'
  },

  // [21] 5.3.1-OSC-010: Singly ionized He+ radius
  'MH-8-SCI-5-5.3.1-OSC-010': {
    text: "Which electron shell in an atom possesses the lowest energy level?",
    options: [
      'K shell (\\(n = 1\\))',
      'L shell (\\(n = 2\\))',
      'M shell (\\(n = 3\\))',
      'N shell (\\(n = 4\\))'
    ],
    correctAnswer: 'A',
    explanation: 'The K shell is closest to the positively charged nucleus and has the lowest energy level of all electron shells.'
  },

  // [23] 5.3.1-OSC-015: Fractional quantum numbers
  'MH-8-SCI-5-5.3.1-OSC-015': {
    text: "Can an electron in Bohr's atomic model revolve in a shell between the K shell and L shell?",
    options: [
      'Yes, electrons can revolve at any arbitrary distance',
      'No, electrons can only revolve in specific, discrete orbits designated by whole numbers',
      'Yes, but only under high magnetic fields',
      'Yes, during chemical bond formation'
    ],
    correctAnswer: 'B',
    explanation: 'Bohr postulated that electrons can revolve only in specific discrete circular orbits, and intermediate positions are not permitted.'
  },

  // [25] 5.3.1-OSC-022: Orbital speed v_n \propto 1/n
  'MH-8-SCI-5-5.3.1-OSC-022': {
    text: "What is the maximum number of electrons that the first shell (K shell, \\(n = 1\\)) can hold according to the \\(2n^2\\) rule?",
    options: [
      '8 electrons',
      '18 electrons',
      '2 electrons',
      '32 electrons'
    ],
    correctAnswer: 'C',
    explanation: 'Using the formula \\(2n^2\\), for \\(n = 1\\), the maximum capacity is \\(2(1)^2 = 2\\) electrons.'
  },

  // [26] 5.3.1-OSC-025: Bohr radius 0.529 A
  'MH-8-SCI-5-5.3.1-OSC-025': {
    text: "What happens when an electron absorbs energy in Bohr's atomic model?",
    options: [
      'It jumps to an outer orbit of higher energy',
      'It drops into the atomic nucleus',
      'It converts into a neutron',
      'It splits into two smaller particles'
    ],
    correctAnswer: 'A',
    explanation: 'When an electron absorbs energy, it jumps from an inner lower-energy orbit to an outer higher-energy orbit.'
  },

  // [27] 5.3.1-OSC-026: De Broglie connect to Bohr
  'MH-8-SCI-5-5.3.1-OSC-026': {
    text: "What happens when an excited electron falls back from an outer orbit to an inner orbit in Bohr's model?",
    options: [
      'It absorbs additional heat from the surroundings',
      'It increases its mass',
      'It emits energy in the form of radiation (light)',
      'It stops revolving and becomes stationary'
    ],
    correctAnswer: 'C',
    explanation: 'When an electron jumps from an outer higher-energy shell to an inner lower-energy shell, it emits the excess energy as radiation.'
  },

  // [28] 5.3.1-OSC-028: Heisenberg uncertainty Schrodinger
  'MH-8-SCI-5-5.3.1-OSC-028': {
    text: "According to Bohr's model, how do electrons revolve around the nucleus?",
    options: [
      'In random, zigzag paths throughout the atom',
      'In concentric circular stable orbits around the nucleus',
      'In straight lines bouncing off the atom walls',
      'In spiral paths collapsing toward the center'
    ],
    correctAnswer: 'B',
    explanation: 'Bohr showed that electrons revolve in concentric circular orbits around the central nucleus.'
  },

  // [30] 5.3.2-OSC-003: Delta E = E2 - E1 = 10.2 eV
  'MH-8-SCI-5-5.3.2-OSC-003': {
    text: "If an electron moves from the K shell (\\(n = 1\\)) to the M shell (\\(n = 3\\)), does it absorb or emit energy?",
    options: [
      'It absorbs energy',
      'It emits energy',
      'It neither absorbs nor emits energy',
      'It destroys energy'
    ],
    correctAnswer: 'A',
    explanation: 'Moving from an inner shell (K) to an outer higher-energy shell (M) requires the absorption of energy.'
  },

  // [31] 5.3.2-OSC-004: Discrete quantized frequencies nu = (E2 - E1)/h
  'MH-8-SCI-5-5.3.2-OSC-004': {
    text: "What is the maximum electron capacity of the second shell (L shell, \\(n = 2\\)) calculated using \\(2n^2\\)?",
    options: [
      '2 electrons',
      '8 electrons',
      '18 electrons',
      '32 electrons'
    ],
    correctAnswer: 'B',
    explanation: 'For the L shell (\\(n = 2\\)), the maximum capacity is \\(2(2)^2 = 2 \\times 4 = 8\\) electrons.'
  },

  // [32] 5.3.2-OSC-005: Balmer series
  'MH-8-SCI-5-5.3.2-OSC-005': {
    text: "What is the maximum electron capacity of the M shell (\\(n = 3\\)) of an atom?",
    options: [
      '8 electrons',
      '2 electrons',
      '18 electrons',
      '32 electrons'
    ],
    correctAnswer: 'C',
    explanation: 'For the M shell (\\(n = 3\\)), the maximum capacity is \\(2(3)^2 = 2 \\times 9 = 18\\) electrons.'
  },

  // [33] 5.3.2-OSC-006: Delta E = hc/lambda
  'MH-8-SCI-5-5.3.2-OSC-006': {
    text: "What is the maximum electron capacity of the N shell (\\(n = 4\\)) calculated using the \\(2n^2\\) formula?",
    options: [
      '8 electrons',
      '18 electrons',
      '2 electrons',
      '32 electrons'
    ],
    correctAnswer: 'D',
    explanation: 'For the N shell (\\(n = 4\\)), the maximum capacity is \\(2(4)^2 = 2 \\times 16 = 32\\) electrons.'
  },

  // [34] 5.3.2-OSC-008: 6 spectral lines n=4
  'MH-8-SCI-5-5.3.2-OSC-008': {
    text: "Which of the following shells has higher energy: the L shell or the M shell?",
    options: [
      'L shell has higher energy',
      'M shell has higher energy',
      'Both have identical energy',
      'Neither shell possesses energy'
    ],
    correctAnswer: 'B',
    explanation: 'The M shell (\\(n = 3\\)) is further from the nucleus than the L shell (\\(n = 2\\)), so it has a higher energy level.'
  },

  // [35] 5.3.2-OSC-010: Rydberg formula series limit
  'MH-8-SCI-5-5.3.2-OSC-010': {
    text: "According to the octet rule in textbook science, what is the maximum number of electrons the outermost (valence) shell of an atom can accommodate?",
    options: [
      '2 electrons',
      '18 electrons',
      '32 electrons',
      '8 electrons'
    ],
    correctAnswer: 'D',
    explanation: 'The outermost shell of any atom can hold a maximum of 8 electrons (octet rule), regardless of its total theoretical capacity.'
  },

  // [38] 5.3.2-OSC-013: Delta E = h nu
  'MH-8-SCI-5-5.3.2-OSC-013': {
    text: "When an atom's outermost shell has 8 electrons, what is said about its stability and chemical reactivity?",
    options: [
      'It is highly reactive and explosive',
      'It has a complete octet and is chemically stable and inert',
      'It loses electrons instantly to form cations',
      'It converts into an isotope'
    ],
    correctAnswer: 'B',
    explanation: 'An atom with 8 electrons in its valence shell has a complete octet, making it exceptionally stable with very low chemical reactivity (like noble gases).'
  },

  // [41] 5.3.2-OSC-018: Lifetime 10^-8 s
  'MH-8-SCI-5-5.3.2-OSC-018': {
    text: "What is an atom said to be in when all its electrons reside in their lowest possible energy shells?",
    options: [
      'Excited state',
      'Ionized state',
      'Radioactive state',
      'Ground state'
    ],
    correctAnswer: 'D',
    explanation: 'When electrons occupy the lowest available energy levels, the atom is in its most stable state, known as the ground state.'
  },

  // [42] 5.3.2-OSC-019: H-alpha cyan photon
  'MH-8-SCI-5-5.3.2-OSC-019': {
    text: "What is the state of an atom called when one or more of its electrons jump to a higher energy shell after absorbing energy?",
    options: [
      'Excited state',
      'Ground state',
      'Inert state',
      'Zero state'
    ],
    correctAnswer: 'A',
    explanation: 'An atom is in an excited state when its electrons have absorbed energy and jumped to higher energy shells.'
  },

  // [44] 5.3.2-OSC-022: Photon 5 eV vs 10.2 eV
  'MH-8-SCI-5-5.3.2-OSC-022': {
    text: "What determines the amount of energy absorbed or emitted when an electron jumps between two shells in an atom?",
    options: [
      'The exact difference in energy between the two shells',
      'The speed of sound inside the laboratory',
      'The mass of the atomic nucleus',
      'The atmospheric air pressure'
    ],
    correctAnswer: 'A',
    explanation: 'The energy absorbed or emitted is exactly equal to the difference in energy between the initial and final shells.'
  },

  // [45] 5.3.2-OSC-024: Rydberg constant derivation
  'MH-8-SCI-5-5.3.2-OSC-024': {
    text: "Which element's atomic structure was initially explained in detail by Niels Bohr in 1913?",
    options: [
      'Uranium',
      'Gold',
      'Hydrogen',
      'Iron'
    ],
    correctAnswer: 'C',
    explanation: 'Bohr developed his atomic model specifically by analyzing the single-electron atom of Hydrogen.'
  },

  // [46] 5.3.2-OSC-025: Number of spectral lines n=4
  'MH-8-SCI-5-5.3.2-OSC-025': {
    text: "When an electron in an excited hydrogen atom returns from the L shell to the K shell, what form does the released energy take?",
    options: [
      'Sound wave',
      'Light radiation',
      'Mechanical vibration',
      'Magnetic field only'
    ],
    correctAnswer: 'B',
    explanation: 'Energy released during an electron transition is emitted as light radiation (electromagnetic radiation).'
  },

  // [47] 5.3.2-OSC-026: Fraunhofer lines
  'MH-8-SCI-5-5.3.2-OSC-026': {
    text: "If an electron in the ground state K shell receives an amount of energy smaller than required to reach the L shell, what happens?",
    options: [
      'The electron jumps halfway to a non-existent orbit',
      'The energy is not absorbed and the electron remains in the K shell',
      'The electron splits in half',
      'The nucleus loses a proton'
    ],
    correctAnswer: 'B',
    explanation: 'An electron can only jump if it receives the exact amount of energy needed to reach another permitted shell; otherwise, no transition occurs.'
  },

  // [48] 5.4.1-OSC-008: Specific charge of proton vs alpha
  'MH-8-SCI-5-5.4.1-OSC-008': {
    text: "What is the electric charge and location of a proton in an atom?",
    options: [
      'Negative charge, revolving in outer shells',
      'Neutral (no charge), inside the nucleus',
      'Positive charge, revolving in the K shell',
      'Positive charge, located inside the nucleus'
    ],
    correctAnswer: 'D',
    explanation: 'A proton carries a unit positive charge (\\(+1e\\)) and resides in the central nucleus of the atom.'
  },

  // [49] 5.4.1-OSC-018: Quark composition of proton uud
  'MH-8-SCI-5-5.4.1-OSC-018': {
    text: "What is the approximate mass of a proton in unified atomic mass units (u)?",
    options: [
      '\\(1\\text{ u}\\)',
      '\\(0\\text{ u}\\)',
      '\\(1/1837\\text{ u}\\)',
      '\\(10\\text{ u}\\)'
    ],
    correctAnswer: 'A',
    explanation: 'The mass of one proton is approximately \\(1\\text{ u}\\) (unified mass unit), which is roughly \\(1.66 \\times 10^{-27}\\text{ kg}\\).'
  },

  // [50] 5.4.2-OSC-007: Free neutron beta decay
  'MH-8-SCI-5-5.4.2-OSC-007': {
    text: "Which subatomic particle was discovered by James Chadwick in 1932?",
    options: [
      'Proton',
      'Electron',
      'Positron',
      'Neutron'
    ],
    correctAnswer: 'D',
    explanation: 'James Chadwick discovered the electrically neutral subatomic particle called the neutron in 1932.'
  },

  // [51] 5.4.2-OSC-010: Heisenberg uncertainty in nucleus
  'MH-8-SCI-5-5.4.2-OSC-010': {
    text: "Which of the following subatomic particles carries NO electrical charge (electrically neutral)?",
    options: [
      'Proton',
      'Electron',
      'Neutron',
      'Alpha particle'
    ],
    correctAnswer: 'C',
    explanation: 'A neutron is electrically neutral, carrying zero net electric charge.'
  },

  // [52] 5.4.2-OSC-018: Nuclear reaction Be-9 + alpha -> C-12 + n
  'MH-8-SCI-5-5.4.2-OSC-018': {
    text: "How does the mass of a neutron compare to the mass of a proton?",
    options: [
      'A neutron is 1837 times lighter than a proton',
      'A neutron has nearly the same mass as a proton (approx 1 u)',
      'A neutron has zero mass',
      'A neutron is twice as heavy as an alpha particle'
    ],
    correctAnswer: 'B',
    explanation: 'The mass of a neutron is nearly equal to that of a proton, approximately \\(1\\text{ u}\\).'
  },

  // [53] 5.4.3-OSC-006: Leptons vs Baryons Standard Model
  'MH-8-SCI-5-5.4.3-OSC-006': {
    text: "Which subatomic particle carries a negative electric charge and revolves around the nucleus?",
    options: [
      'Neutron',
      'Electron',
      'Proton',
      'Alpha particle'
    ],
    correctAnswer: 'B',
    explanation: 'Electrons are negatively charged subatomic particles that revolve outside the nucleus.'
  },

  // [54] 5.4.3-OSC-008: Electron spin quantum number Uhlenbeck
  'MH-8-SCI-5-5.4.3-OSC-008': {
    text: "What is the relative mass of an electron compared to the mass of a hydrogen atom (proton)?",
    options: [
      'Equal to the proton',
      'Approximately \\(1/1837\\) of a hydrogen atom',
      'Twice the mass of a proton',
      '100 times the mass of a proton'
    ],
    correctAnswer: 'B',
    explanation: 'An electron has a negligible mass, approximately \\(1/1837\\) times that of a hydrogen atom.'
  },

  // [56] 5.4.3-OSC-010: De Broglie wavelength 100V
  'MH-8-SCI-5-5.4.3-OSC-010': {
    text: "Why is the total mass of an atom almost entirely concentrated in its nucleus?",
    options: [
      'Electrons have negligible mass compared to protons and neutrons in the nucleus',
      'Protons and neutrons lose their mass when they leave the nucleus',
      'Electrons are located outside the atom',
      'Nuclei contain heavy gold particles'
    ],
    correctAnswer: 'A',
    explanation: 'Because electrons have negligible mass (\\(1/1837\\text{ u}\\)), practically all the mass of an atom comes from the protons and neutrons inside the nucleus.'
  },

  // [57] 5.5.1-OSC-004: Moseley's law sqrt(nu) = a(Z - b)
  'MH-8-SCI-5-5.5.1-OSC-004': {
    text: "What does the atomic number (\\(Z\\)) of an element represent?",
    options: [
      'The number of neutrons in the nucleus',
      'The total number of protons and neutrons combined',
      'The number of protons in the nucleus of an atom',
      'The number of electron shells in the atom'
    ],
    correctAnswer: 'C',
    explanation: 'The atomic number (\\(Z\\)) is defined as the number of protons in the nucleus of an atom (which equals the number of electrons in a neutral atom).'
  },

  // [59] 5.5.2-OSC-012: 1s orbital spin paired
  'MH-8-SCI-5-5.5.2-OSC-012': {
    text: "What does the mass number (\\(A\\)) of an atom represent?",
    options: [
      'The number of protons only',
      'The total number of protons and neutrons (nucleons) in the nucleus',
      'The number of electrons revolving around the nucleus',
      'The number of chemical bonds the atom can form'
    ],
    correctAnswer: 'B',
    explanation: 'The mass number (\\(A\\)) is the total number of protons and neutrons (nucleons) present in the nucleus of an atom: \\(A = Z + N\\).'
  },

  // [60] 5.5.2-OSC-014: Pauli Exclusion Principle 2n^2 derivation
  'MH-8-SCI-5-5.5.2-OSC-014': {
    text: "If an atom has atomic number \\(Z = 11\\) and mass number \\(A = 23\\), how many neutrons does it contain?",
    options: [
      '11 neutrons',
      '12 neutrons',
      '23 neutrons',
      '34 neutrons'
    ],
    correctAnswer: 'B',
    explanation: 'The number of neutrons is given by \\(N = A - Z = 23 - 11 = 12\\).'
  },

  // [62] 5.5.4-OSC-010: PCl5 expanded octet 3d orbital
  'MH-8-SCI-5-5.5.4-OSC-010': {
    text: "What is the valency of Carbon (atomic number \\(Z = 6\\), electronic configuration 2, 4)?",
    options: [
      '1',
      '4',
      '2',
      '6'
    ],
    correctAnswer: 'B',
    explanation: 'Carbon has 4 valence electrons in its outermost shell, giving it a valency of 4 (tetravalent).'
  },

  // [64] 5.6.2-OSC-027: PET scan positron annihilation
  'MH-8-SCI-5-5.6.2-OSC-027': {
    text: "Which radioactive isotope is widely used in medicine for the treatment of cancer?",
    options: [
      'Carbon-14',
      'Iodine-131',
      'Cobalt-60',
      'Sodium-24'
    ],
    correctAnswer: 'C',
    explanation: 'Cobalt-60 (\\(^{60}\\text{Co}\\)) is a radioactive isotope used in radiotherapy for the treatment of cancer.'
  }
};

// Generic cleaner for any boilerplate explanation
function cleanExplanation(text, correctAnswer, qText) {
  if (!text) return '';

  // Check if it has section markers
  let cleaned = text;

  // If it's structured with ### 1., ### 2., ### 3.
  if (/###\s*1\./i.test(cleaned)) {
    // Extract Section 1 or summary
    const sec1Match = cleaned.match(/###\s*1\.[^\n]*\n([\s\S]*?)(?=###\s*2\.|\n\n###|$)/i);
    if (sec1Match && sec1Match[1].trim()) {
      cleaned = sec1Match[1].trim();
    }
  }

  // Strip Physical Context: / Core Calculation: / Option Analysis:
  if (/Physical Context:/i.test(cleaned)) {
    // Try to extract Core Calculation or Physical Context without Option Analysis
    const calcMatch = cleaned.match(/Core Calculation\/Logic:\s*([\s\S]*?)(?=Option Analysis:|$)/i);
    const physMatch = cleaned.match(/Physical Context:\s*([\s\S]*?)(?=Core Calculation|$)/i);
    if (calcMatch && calcMatch[1].trim().length > 10) {
      cleaned = calcMatch[1].trim();
    } else if (physMatch && physMatch[1].trim().length > 10) {
      cleaned = physMatch[1].trim();
    }
  }

  // If Key Concept / Option Analysis
  if (/\*\*Key Concept:\*\*/i.test(cleaned)) {
    const conceptMatch = cleaned.match(/\*\*Key Concept:\*\*([\s\S]*?)(?=\*\*Option Analysis:\*\*|$)/i);
    if (conceptMatch && conceptMatch[1].trim()) {
      cleaned = conceptMatch[1].trim();
    }
  }

  // Remove all option letter references: Option A is correct, Option B is incorrect, etc.
  cleaned = cleaned.replace(/Option\s+[A-D]\s+is\s+(correct|incorrect|mathematically\s+correct)[^.\n]*[.\n]?/gi, '');
  cleaned = cleaned.replace(/-\s*\*\*\(?[A-D]\)?[\s\S]*?(?=(-\s*\*\*\(?[A-D]\)?|$))/g, '');
  cleaned = cleaned.replace(/-\s*Option\s+[A-D][^\n]*/gi, '');
  cleaned = cleaned.replace(/\*\*Option Analysis:\*\*[\s\S]*/gi, '');
  cleaned = cleaned.replace(/Option Analysis:[\s\S]*/gi, '');
  cleaned = cleaned.replace(/###\s*[1-3]\.[^\n]*/gi, '');

  // Clean trailing and extra whitespace
  cleaned = cleaned.replace(/\n{3,}/g, '\n\n').trim();

  // If it's still too long (> 300 chars), take the first 2-3 sentences
  if (cleaned.length > 250) {
    const sentences = cleaned.split(/(?<=[.?!])\s+/);
    if (sentences.length > 1) {
      let short = sentences[0];
      for (let i = 1; i < Math.min(sentences.length, 3); i++) {
        if ((short + ' ' + sentences[i]).length <= 250) {
          short += ' ' + sentences[i];
        } else break;
      }
      cleaned = short;
    }
  }

  // Remove any remaining stray bullet points or headers
  cleaned = cleaned.replace(/^[-*•]\s+/gm, '').trim();

  return cleaned;
}

async function runRealignment() {
  console.log('=== STARTING CHAPTER 5 CURRICULUM REALIGNMENT & BOILERPLATE CLEANSE ===');
  
  // 1. Fetch all questions with boilerplate or from Ch 5
  const ch5Snap = await db.collection('questions')
    .where('topicCode', '>=', 'MH-8-SCI-5')
    .where('topicCode', '<=', 'MH-8-SCI-5\uf8ff')
    .get();
  console.log(`Fetched ${ch5Snap.size} questions from MH-8-SCI-5.`);

  // Load all_boilerplate_questions.json to get any non-Ch5 questions
  const bpData = JSON.parse(fs.readFileSync('all_boilerplate_questions.json', 'utf8'));
  console.log(`Loaded ${bpData.count} total boilerplate questions from initial scan.`);

  const updates = [];

  // Handle Ch 5 questions
  ch5Snap.docs.forEach(doc => {
    const q = doc.data();
    const docId = doc.id;
    const qCode = q.questionCode || docId;

    if (ch5Replacements[docId] || ch5Replacements[qCode]) {
      const rep = ch5Replacements[docId] || ch5Replacements[qCode];
      updates.push({
        id: docId,
        data: {
          text: rep.text,
          options: rep.options,
          correctAnswer: rep.correctAnswer,
          explanation: rep.explanation,
          solution: rep.explanation,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        },
        type: 'OOS_REPLACEMENT',
        desc: `Replaced out-of-syllabus Q with textbook Class 8 Q: "${rep.text.slice(0, 50)}..."`
      });
    } else {
      // Check if explanation has boilerplate
      const exp = q.explanation || q.solution || '';
      if (/###\s*1\.|###\s*2\.|###\s*3\.|Physical Context:|Core Calculation|Option Analysis|Option [A-D] is correct|\*\*Key Concept:\*\*/i.test(exp)) {
        const cleaned = cleanExplanation(exp, q.correctAnswer, q.text);
        updates.push({
          id: docId,
          data: {
            explanation: cleaned,
            solution: cleaned,
            updatedAt: admin.firestore.FieldValue.serverTimestamp()
          },
          type: 'CH5_BOILERPLATE_CLEAN',
          desc: `Cleaned Ch 5 explanation: "${cleaned.slice(0, 50)}..."`
        });
      }
    }
  });

  // Handle Non-Ch5 boilerplate questions (MH-9-SCIT, MH-9-MTH2, MH-10-MTH2)
  for (const bq of bpData.questions) {
    if (!bq.topicCode.startsWith('MH-8-SCI-5')) {
      const exp = bq.fullExplanation || bq.fullSolution || '';
      const cleaned = cleanExplanation(exp, null, bq.text);
      updates.push({
        id: bq.id,
        data: {
          explanation: cleaned,
          solution: cleaned,
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        },
        type: 'NON_CH5_BOILERPLATE_CLEAN',
        desc: `Cleaned non-Ch5 explanation (${bq.topicCode}): "${cleaned.slice(0, 50)}..."`
      });
    }
  }

  console.log(`Total question updates to apply: ${updates.length}`);
  const byType = {};
  updates.forEach(u => byType[u.type] = (byType[u.type] || 0) + 1);
  console.log('Update breakdown by type:', byType);

  // Apply in Firestore batches (max 400 per batch)
  const batchSize = 400;
  for (let i = 0; i < updates.length; i += batchSize) {
    const chunk = updates.slice(i, i + batchSize);
    const batch = db.batch();
    chunk.forEach(u => {
      const ref = db.collection('questions').doc(u.id);
      batch.update(ref, u.data);
    });
    await batch.commit();
    console.log(`Committed batch ${Math.floor(i / batchSize) + 1} (${chunk.length} questions).`);
  }

  console.log('=== ALL UPDATES COMMITTED SUCCESSFULLY ===');
}

runRealignment().catch(console.error);
