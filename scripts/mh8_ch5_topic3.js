// scripts/mh8_ch5_topic3.js
// Topic 5.3: Bohr Stable Orbit Atomic Model
// Subtopics: 5.3.1, 5.3.2
// Vaults: exam, practice, foundation

const topic3Questions = [
  // ==========================================
  // SUBTOPIC 5.3.1: Electrons revolve in discrete stable circular orbits (K, L, M, N shells)
  // ==========================================
  {
    questionCode: "MH-8-SCI-5-5.3.1-OSC-001",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.3.1",
    parentTopicCode: "MH-8-SCI-5-5.3",
    parentTopicName: "Bohr Stable Orbit Atomic Model",
    subtopicCode: "MH-8-SCI-5-5.3.1",
    subtopicName: "Electrons revolve in discrete stable circular orbits (K, L, M, N shells)",
    topicNumber: "5.3.1",
    type: "OSC",
    difficulty: "easy",
    bloomLevel: "Remember",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "In Bohr's atomic model, what alphabetical letters are canonically designated for the concentric electron shells corresponding to principal quantum numbers \\(n = 1, 2, 3, 4\\) starting from the innermost shell outward?",
    options: [
      "K, L, M, N",
      "A, B, C, D",
      "P, Q, R, S",
      "X, Y, Z, W"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1913, Niels Bohr established that electrons reside in discrete concentric energy levels or shells around the nucleus designated by the principal quantum number \\(n\\):
\\[
\\begin{array}{|c|c|}
\\hline
\\text{Principal Quantum Number } (n) & \\text{Shell Letter Designation} \\\\
\\hline
n = 1 & \\text{K shell (innermost)} \\\\
n = 2 & \\text{L shell} \\\\
n = 3 & \\text{M shell} \\\\
n = 4 & \\text{N shell} \\\\
\\hline
\\end{array}
\\]
The notation originates from early spectroscopic X-ray emission lines discovered by Charles Glover Barkla.

### 2. Physical Context & Practical Illustration:
The K shell is closest to the nucleus and has the lowest energy (most tightly bound). As \\(n\\) increases, the shells lie further out and have progressively higher energy levels.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: K, L, M, N are the universally recognized shell designations for \\(n = 1, 2, 3, 4\\).
- **Option B is incorrect**: A, B, C, D is not used in atomic physics.
- **Option C is incorrect**: P, Q, R, S correspond to \\(n = 6, 7\\dots\\) or orbital subshells (s, p, d, f), not the first four principal shells.
- **Option D is incorrect**: X, Y, Z are spatial coordinate axes, not shell labels.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.1-OSC-002",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.3.1",
    parentTopicCode: "MH-8-SCI-5-5.3",
    parentTopicName: "Bohr Stable Orbit Atomic Model",
    subtopicCode: "MH-8-SCI-5-5.3.1",
    subtopicName: "Electrons revolve in discrete stable circular orbits (K, L, M, N shells)",
    topicNumber: "5.3.1",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Why are the orbits in Bohr's model designated as 'stationary orbits' or 'stationary states'?",
    options: [
      "The energy of an electron revolving in any of these permitted orbits remains constant and does not radiate away",
      "The electrons are physically stationary and fixed at rest inside the nucleus",
      "The nucleus ceases to exert any electrical force on the electron",
      "The atom ceases all internal motion at absolute zero temperature"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The term **stationary orbit** does NOT mean that the electron is motionless. Rather, it means that the **energy of the orbit is fixed and stationary with respect to time**:
\\[
\\frac{dE}{dt} = 0
\\]
While an electron moves along a permitted Bohr orbit, classical radiation laws are suspended by quantum postulate: the electron does not emit electromagnetic radiation despite its centripetal acceleration.

### 2. Physical Context & Practical Illustration:
Think of steps on a staircase. A ball resting on a specific step has a constant, fixed potential energy; it cannot exist suspended in mid-air between steps.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The energy of the electron in that orbit remains constant without radiation loss.
- **Option B is incorrect**: Common student misconception: electrons are constantly moving at high speed (\\(\\approx 2.2 \\times 10^6\\text{ m/s}\\) in K shell), not physically at rest.
- **Option C is incorrect**: Electrostatic attraction remains active and provides centripetal force.
- **Option D is incorrect**: Stationary state is a quantum mechanical concept, not a temperature-dependent state.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.1-OSC-003",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.3.1",
    parentTopicCode: "MH-8-SCI-5-5.3",
    parentTopicName: "Bohr Stable Orbit Atomic Model",
    subtopicCode: "MH-8-SCI-5-5.3.1",
    subtopicName: "Electrons revolve in discrete stable circular orbits (K, L, M, N shells)",
    topicNumber: "5.3.1",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "How does the energy of an electron shell change as its distance from the atomic nucleus increases (from K to L to M to N)?",
    options: [
      "The energy of the shell increases progressively (becomes less negative) as we move outward from K to N",
      "The energy decreases progressively to negative infinity at large distances",
      "The energy remains strictly identical for all shells regardless of distance",
      "The energy oscillates randomly depending on whether the shell number is odd or even"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a hydrogen-like atom, the energy of an electron in shell \\(n\\) is given by Bohr's energy formula:
\\[
E_n = -\\frac{13.6\\text{ eV}}{n^2} \\cdot Z^2
\\]
For hydrogen (\\(Z = 1\\)):
- K shell (\\(n = 1\\)): \\(E_1 = -13.6\\text{ eV}\\) (lowest energy, most stable)
- L shell (\\(n = 2\\)): \\(E_2 = -3.4\\text{ eV}\\)
- M shell (\\(n = 3\\)): \\(E_3 = -1.51\\text{ eV}\\)
- N shell (\\(n = 4\\)): \\(E_4 = -0.85\\text{ eV}\\)
As \\(n\\) increases, \\(E_n\\) increases (becomes less negative, approaching \\(0\\text{ eV}\\) at \\(n = \\infty\\)).

### 2. Physical Context & Practical Illustration:
An electron close to the positive nucleus is held very tightly in a deep potential well. Moving it outward requires overcoming electrostatic attraction, increasing its total potential energy.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The energy increases from \\(-13.6\\text{ eV}\\) towards \\(0\\text{ eV}\\) as we go outward from K to N.
- **Option B is incorrect**: Negative values decrease in magnitude, which represents an increase in total algebraic energy.
- **Option C is incorrect**: Different shells have distinct, discrete energy eigenvalues.
- **Option D is incorrect**: Energy variation is strictly monotonic with \\(n\\).`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.1-OSC-004",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.3.1",
    parentTopicCode: "MH-8-SCI-5-5.3",
    parentTopicName: "Bohr Stable Orbit Atomic Model",
    subtopicCode: "MH-8-SCI-5-5.3.1",
    subtopicName: "Electrons revolve in discrete stable circular orbits (K, L, M, N shells)",
    topicNumber: "5.3.1",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Which of the following statements correctly describes the relationship between the radius of Bohr orbits (\\(r_n\\)) and the principal quantum number \\(n\\)?",
    options: [
      "The orbital radius is directly proportional to the square of the shell number: \\(r_n \\propto n^2\\)",
      "The orbital radius is inversely proportional to the shell number: \\(r_n \\propto \\frac{1}{n}\\)",
      "The orbital radius increases linearly with the shell number: \\(r_n \\propto n\\)",
      "The orbital radius is constant and independent of \\(n\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In Bohr's derivation for hydrogen:
1. Centripetal force:
\\[
\\frac{m_e v^2}{r} = \\frac{e^2}{4\\pi\\varepsilon_0 r^2}
\\]
2. Quantization of angular momentum:
\\[
m_e v r = \\frac{nh}{2\\pi} \\implies v = \\frac{nh}{2\\pi m_e r}
\\]
Substituting \\(v\\) into the force equation gives:
\\[
r_n = \\frac{\\varepsilon_0 h^2}{\\pi m_e e^2} \\cdot \\frac{n^2}{Z} = a_0 \\frac{n^2}{Z}
\\]
where \\(a_0 \\approx 0.529\\text{ Å} = 0.0529\\text{ nm}\\) is the first Bohr radius.
Hence, \\(r_n \\propto n^2\\).

### 2. Physical Context & Practical Illustration:
If \\(n=1\\) has radius \\(r_1 = a_0\\), then:
- \\(n=2\\) (L shell) is \\(4a_0\\)
- \\(n=3\\) (M shell) is \\(9a_0\\)
- \\(n=4\\) (N shell) is \\(16a_0\\)
The spacing between consecutive shells widens rapidly as we move away from the nucleus.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The radius scales quadratically with the principal quantum number, \\(r_n \\propto n^2\\).
- **Option B is incorrect**: Inversely proportional would mean shells shrink toward the nucleus as \\(n\\) grows.
- **Option C is incorrect**: Linear scaling ignores the \\(v \\propto 1/n\\) dependence in angular momentum.
- **Option D is incorrect**: The shells occupy distinctly different physical radii.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.1-OSC-005",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.3.1",
    parentTopicCode: "MH-8-SCI-5-5.3",
    parentTopicName: "Bohr Stable Orbit Atomic Model",
    subtopicCode: "MH-8-SCI-5-5.3.1",
    subtopicName: "Electrons revolve in discrete stable circular orbits (K, L, M, N shells)",
    topicNumber: "5.3.1",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Evaluate",
    vault: "foundation",
    examCategory: "foundation",
    marks: 4,
    penaltyMarks: 1,
    text: "What is the orbital angular momentum of an electron moving in the M shell (\\(n = 3\\)) of a hydrogen atom according to Bohr's quantum condition?",
    options: [
      "\\(\\frac{3h}{2\\pi} = 1.5\\hbar\\)",
      "\\(\\frac{h}{2\\pi} = \\hbar\\)",
      "\\(\\frac{2h}{2\\pi} = 2\\hbar\\)",
      "\\(\\frac{9h}{2\\pi} = 4.5\\hbar\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Bohr's second postulate states that orbital angular momentum \\(L\\) is quantized:
\\[
L = m_e v r = n \\frac{h}{2\\pi} = n \\hbar
\\]
For the M shell, the principal quantum number is \\(n = 3\\).
Substituting \\(n = 3\\):
\\[
L = 3 \\cdot \\left(\\frac{h}{2\\pi}\\right) = \\frac{3h}{2\\pi} = 1.5 \\frac{h}{\\pi}
\\]

### 2. Physical Context & Practical Illustration:
Angular momentum cannot take arbitrary continuum values; it comes in discrete quantum packets of \\(\\hbar = \\frac{h}{2\\pi}\\). In the M shell, the electron carries exactly 3 units of this fundamental quantum of angular momentum.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: For \\(n = 3\\) (M shell), \\(L = \\frac{3h}{2\\pi}\\).
- **Option B is incorrect**: \\(\\frac{h}{2\\pi}\\) corresponds to the K shell (\\(n = 1\\)).
- **Option C is incorrect**: \\(\\frac{2h}{2\\pi}\\) corresponds to the L shell (\\(n = 2\\)).
- **Option D is incorrect**: \\(n^2 = 9\\) applies to the radius formula \\(r_n \\propto n^2\\), but angular momentum scales linearly as \\(n\\).`
  },

  // ==========================================
  // SUBTOPIC 5.3.2: Energy emission and absorption during quantum electron jumps
  // ==========================================
  {
    questionCode: "MH-8-SCI-5-5.3.2-OSC-001",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.3.2",
    parentTopicCode: "MH-8-SCI-5-5.3",
    parentTopicName: "Bohr Stable Orbit Atomic Model",
    subtopicCode: "MH-8-SCI-5-5.3.2",
    subtopicName: "Energy emission and absorption during quantum electron jumps",
    topicNumber: "5.3.2",
    type: "OSC",
    difficulty: "easy",
    bloomLevel: "Remember",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "When does an electron inside an atom emit electromagnetic radiation (such as visible light)?",
    options: [
      "When it transitions from an outer higher-energy shell to an inner lower-energy shell",
      "When it transitions from an inner lower-energy shell to an outer higher-energy shell",
      "While it continues revolving continuously in its ground state stationary orbit",
      "When the atom is subjected to absolute zero temperature in total darkness"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
According to Bohr's third postulate (Bohr's frequency condition):
An electron radiates energy in the form of a single photon of electromagnetic radiation ONLY when it jumps from an initial higher energy orbit (\\(E_2\\)) to a final lower energy orbit (\\(E_1\\)):
\\[
\\Delta E = E_2 - E_1 = h\\nu = \\frac{hc}{\\lambda}
\\]
where \\(h\\) is Planck's constant, \\(\\nu\\) is frequency, and \\(\\lambda\\) is wavelength.

### 2. Physical Context & Practical Illustration:
This is the working principle behind neon signs, fireworks, and LED lights. Atoms are excited by heat or electricity, and when their electrons fall back to lower shells, they emit bright flashes of colored light.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Dropping from high to low energy releases the energy surplus as an emitted photon.
- **Option B is incorrect**: Transitioning from lower to higher energy requires *absorption* of energy, not emission.
- **Option C is incorrect**: Stationary orbits are non-radiating; no light is emitted during steady orbital motion.
- **Option D is incorrect**: Cooling to absolute zero does not trigger de-excitation emission.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.2-OSC-002",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.3.2",
    parentTopicCode: "MH-8-SCI-5-5.3",
    parentTopicName: "Bohr Stable Orbit Atomic Model",
    subtopicCode: "MH-8-SCI-5-5.3.2",
    subtopicName: "Energy emission and absorption during quantum electron jumps",
    topicNumber: "5.3.2",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Understand",
    vault: "exam",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What happens when an atom in its ground state absorbs an exact quantum of energy matching the difference \\(\\Delta E = E_2 - E_1\\)?",
    options: [
      "An electron in an inner shell absorbs the energy and gets excited to an outer higher-energy shell",
      "The atomic nucleus splits instantly into two radioactive fragments",
      "All electrons in the atom freeze into permanent stationary positions",
      "The atom converts into an uncharged anti-matter particle"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
When incoming electromagnetic radiation or collision energy delivers an exact quantum equal to the energy gap between shells:
\\[
h\\nu = E_{\\text{outer}} - E_{\\text{inner}}
\\]
the electron absorbs the photon and makes an upward quantum jump to an outer shell. This state is known as an **excited state**.

### 2. Physical Context & Practical Illustration:
Excited states are transient and unstable; an excited electron typically resides in the higher level for only about \\(10^{-8}\\text{ s}\\) before spontaneously cascading back to a lower level and emitting light.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The electron absorbs the photon and transitions to a higher energy level (excitation).
- **Option B is incorrect**: Nuclear fission requires high-energy neutrons, not optical energy level absorption.
- **Option C is incorrect**: Absorbing energy increases orbital potential energy; it does not freeze electron motion.
- **Option D is incorrect**: Photons do not convert matter into antimatter in standard atomic transitions.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.2-OSC-003",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.3.2",
    parentTopicCode: "MH-8-SCI-5-5.3",
    parentTopicName: "Bohr Stable Orbit Atomic Model",
    subtopicCode: "MH-8-SCI-5-5.3.2",
    subtopicName: "Energy emission and absorption during quantum electron jumps",
    topicNumber: "5.3.2",
    type: "OSC",
    difficulty: "medium",
    bloomLevel: "Apply",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "If an electron in a hydrogen atom jumps from the L shell (\\(n = 2\\), \\(E_2 = -3.4\\text{ eV}\\)) to the K shell (\\(n = 1\\), \\(E_1 = -13.6\\text{ eV}\\)), what is the energy of the emitted photon?",
    options: [
      "\\(10.2\\text{ eV}\\)",
      "\\(17.0\\text{ eV}\\)",
      "\\(3.4\\text{ eV}\\)",
      "\\(13.6\\text{ eV}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
According to Bohr's frequency condition, the energy of the emitted photon is the algebraic difference between the initial higher state and the final lower state:
\\[
E_{\\text{photon}} = E_2 - E_1
\\]
Substituting the given energy values:
\\[
E_{\\text{photon}} = (-3.4\\text{ eV}) - (-13.6\\text{ eV}) = -3.4\\text{ eV} + 13.6\\text{ eV} = 10.2\\text{ eV}
\\]
This transition corresponds to the Lyman-\\(\\alpha\\) (\\(\\text{Ly}-\\alpha\\)) line in the ultraviolet region of the hydrogen spectrum.

### 2. Physical Context & Practical Illustration:
The \\(10.2\\text{ eV}\\) difference is emitted as a single ultraviolet photon having a wavelength of approximately \\(\\lambda = \\frac{1240\\text{ eV}\\cdot\\text{nm}}{10.2\\text{ eV}} \\approx 121.6\\text{ nm}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\((-3.4) - (-13.6) = 10.2\\text{ eV}\\).
- **Option B is incorrect**: \\(13.6 + 3.4 = 17.0\\text{ eV}\\) incorrectly adds magnitudes instead of finding their difference.
- **Option C is incorrect**: \\(3.4\\text{ eV}\\) is the energy of the \\(n=2\\) level alone.
- **Option D is incorrect**: \\(13.6\\text{ eV}\\) is the ionization energy from ground state to infinity.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.2-OSC-004",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.3.2",
    parentTopicCode: "MH-8-SCI-5-5.3",
    parentTopicName: "Bohr Stable Orbit Atomic Model",
    subtopicCode: "MH-8-SCI-5-5.3.2",
    subtopicName: "Energy emission and absorption during quantum electron jumps",
    topicNumber: "5.3.2",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Analyze",
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "Why does hydrogen gas in a discharge tube produce sharp, narrow spectral lines rather than a continuous rainbow spectrum?",
    options: [
      "Electrons can only occupy discrete quantized energy levels, so transitions emit photons with exact, distinct frequencies: \\(\\nu = \\frac{E_2 - E_1}{h}\\)",
      "Hydrogen molecules filter out all wavelengths of light except four primary colors",
      "Gas discharge tubes contain magnetic gratings that split continuous light into lines",
      "The speed of light inside the hydrogen discharge tube changes abruptly with temperature"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Because the stationary orbits have strictly quantized energy eigenvalues (\\(E_n = -13.6/n^2\\text{ eV}\\)), the energy differences between any two levels \\(\\Delta E = E_i - E_f\\) can only take discrete values.
Since the frequency of the emitted photon is directly tied to this energy gap by Planck's relation:
\\[
\\nu = \\frac{\\Delta E}{h}
\\]
only photons of specific, precise frequencies (wavelengths) can be emitted. When dispersed through a prism or diffraction grating, these discrete wavelengths appear as sharp, separate spectral lines (e.g. the Balmer series: \\(656.3\\text{ nm}\\) red, \\(486.1\\text{ nm}\\) blue-green, \\(434.0\\text{ nm}\\) blue, \\(410.2\\text{ nm}\\) violet).

### 2. Physical Context & Practical Illustration:
Just as a piano only plays specific notes (pitches) because its strings have discrete lengths, an atom only plays specific optical notes (spectral lines) because its electron orbits have discrete energies.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Quantized energy states lead directly to discrete emitted frequencies.
- **Option B is incorrect**: Hydrogen does not act as a multi-colored passive optical filter.
- **Option C is incorrect**: The lines are an intrinsic emission property of atomic structure, not caused by tube magnets.
- **Option D is incorrect**: The speed of light in vacuum is constant, and small refraction variations in low-pressure gas do not generate line spectra.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.2-OSC-005",
    chapterNumber: "5",
    class: "8",
    subjectCode: "SCI",
    boardCode: "MH",
    board: "Maharashtra Board",
    subject: "General Science",
    topicCode: "MH-8-SCI-5-5.3.2",
    parentTopicCode: "MH-8-SCI-5-5.3",
    parentTopicName: "Bohr Stable Orbit Atomic Model",
    subtopicCode: "MH-8-SCI-5-5.3.2",
    subtopicName: "Energy emission and absorption during quantum electron jumps",
    topicNumber: "5.3.2",
    type: "OSC",
    difficulty: "hard",
    bloomLevel: "Evaluate",
    vault: "foundation",
    examCategory: "foundation",
    marks: 4,
    penaltyMarks: 1,
    text: "Which spectroscopic series of hydrogen involves electron de-excitation jumps terminating in the L shell (\\(n = 2\\)), producing spectral lines in the visible region of the electromagnetic spectrum?",
    options: [
      "Balmer series",
      "Lyman series",
      "Paschen series",
      "Brackett series"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the hydrogen emission spectrum, different spectral series arise depending on the final energy level (\\(n_f\\)) of the transition:
\\[
\\frac{1}{\\lambda} = R_H \\left( \\frac{1}{n_f^2} - \\frac{1}{n_i^2} \\right)
\\]
- **Lyman series** (\\(n_f = 1\\), \\(n_i = 2, 3, 4\\dots\\)): Ultraviolet (UV) region.
- **Balmer series** (\\(n_f = 2\\), \\(n_i = 3, 4, 5, 6\\dots\\)): **Visible region** (and near-UV).
- **Paschen series** (\\(n_f = 3\\), \\(n_i = 4, 5, 6\\dots\\)): Infrared (IR) region.
- **Brackett series** (\\(n_f = 4\\), \\(n_i = 5, 6, 7\\dots\\)): Far-infrared (Far-IR) region.
- **Pfund series** (\\(n_f = 5\\), \\(n_i = 6, 7, 8\\dots\\)): Far-infrared region.

### 2. Physical Context & Practical Illustration:
The Balmer series lines were the very first spectral series discovered (by Johann Balmer in 1885) because their four prominent transitions fall right within the human visible sensitivity window (\\(400\\text{ nm}\\) to \\(700\\text{ nm}\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The Balmer series terminates at \\(n = 2\\) (L shell) and lies in the visible spectrum.
- **Option B is incorrect**: The Lyman series terminates at \\(n = 1\\) (K shell) and lies entirely in the ultraviolet region.
- **Option C is incorrect**: The Paschen series terminates at \\(n = 3\\) (M shell) in the infrared region.
- **Option D is incorrect**: The Brackett series terminates at \\(n = 4\\) (N shell) in the infrared region.`
  }
];

module.exports = { topic3Questions };
