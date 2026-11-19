// scripts/mh8_ch5_topic3_part2.js
// Set B: Topic 5.3 Bohr Stable Orbit Atomic Model (Questions 006-010)

const topic3Part2Questions = [
  // 5.3.1 Set B
  {
    questionCode: "MH-8-SCI-5-5.3.1-OSC-006",
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
    text: "In Bohr's atomic model, what is the term used to describe the lowest possible energy state in which an electron normally revolves?",
    options: [
      "Ground state",
      "Excited state",
      "Ionized state",
      "Plasma state"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **ground state** is the lowest energy orbital configuration available to an atom:
- For Hydrogen, the single electron occupies the \\(n = 1\\) (K shell).
- The ground state energy is \\(E_1 = -13.6\\text{ eV}\\).
This state is completely stable and represents the minimum potential energy configuration of the electron-nucleus system. Any state with \\(n > 1\\) is called an **excited state**.

### 2. Physical Context & Practical Illustration:
An electron in its ground state will remain there forever unless external energy (heat, light, electrical discharge) is supplied to promote it to an excited level.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The ground state is the lowest, most stable orbital state.
- **Option B is incorrect**: An excited state has \\(n \\ge 2\\) with higher energy.
- **Option C is incorrect**: An ionized state occurs when an electron is completely removed to \\(n = \\infty\\).
- **Option D is incorrect**: Plasma is a high-temperature macroscopic state of completely ionized matter.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.1-OSC-007",
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
    text: "How does the orbital speed (\\(v_n\\)) of an electron vary as it moves from inner shells to outer shells (increasing \\(n\\)) in Bohr's model?",
    options: [
      "The orbital speed is inversely proportional to the shell number: \\(v_n \\propto \\frac{1}{n}\\), so electrons move fastest in the innermost K shell",
      "The orbital speed is directly proportional to \\(n^2\\), so electrons move fastest in the outermost shell",
      "The orbital speed is strictly constant and equal to the speed of light in all shells",
      "The orbital speed drops to zero in every even-numbered shell"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In Bohr's model:
1. Centripetal electrostatic balance: \\(\\frac{m_e v^2}{r} = \\frac{k Z e^2}{r^2} \\implies v^2 = \\frac{k Z e^2}{m_e r}\\)
2. Angular momentum quantization: \\(m_e v r = \\frac{nh}{2\\pi} \\implies r = \\frac{nh}{2\\pi m_e v}\\)
Substituting \\(r\\) into the velocity equation:
\\[
v_n = \\left(\\frac{2\\pi k e^2}{h}\\right) \\frac{Z}{n} = v_1 \\frac{Z}{n}
\\]
where \\(v_1 \\approx 2.18 \\times 10^6\\text{ m/s}\\) (about \\(1/137\\) of the speed of light \\(c\\)).
Therefore:
\\[
v_n \\propto \\frac{1}{n}
\\]
As the shell number \\(n\\) increases, orbital speed **decreases**:
- K shell (\\(n = 1\\)): \\(v_1 \\approx 2.18 \\times 10^6\\text{ m/s}\\)
- L shell (\\(n = 2\\)): \\(v_2 = v_1 / 2 \\approx 1.09 \\times 10^6\\text{ m/s}\\)
- M shell (\\(n = 3\\)): \\(v_3 = v_1 / 3 \\approx 0.73 \\times 10^6\\text{ m/s}\\)

### 2. Physical Context & Practical Illustration:
Just as Mercury orbits the Sun much faster (47 km/s) than distant Neptune (5 km/s), inner electrons orbit the nucleus much faster than outer electrons.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Velocity is inversely proportional to \\(n\\) (\\(v_n \\propto 1/n\\)).
- **Option B is incorrect**: Orbital radius scales as \\(n^2\\), but velocity scales as \\(1/n\\).
- **Option C is incorrect**: Subatomic particles always travel slower than the speed of light \\(c\\).
- **Option D is incorrect**: Electrons maintain rapid, non-zero velocities in all shells.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.1-OSC-008",
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
    text: "What is the physical significance of the negative sign in Bohr's atomic energy equation \\(E_n = -\\frac{13.6}{n^2}\\text{ eV}\\)?",
    options: [
      "It signifies that the electron is bound to the nucleus by an attractive electrostatic field and requires positive energy input to be freed",
      "It indicates that the electron possesses negative electrical charge only when orbiting",
      "It indicates that the electron is moving backward in time",
      "It represents an arithmetic error in early 20th-century spectroscopic units"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In potential energy theory, the reference zero point (\\(U = 0\\)) is defined when the electron and nucleus are infinitely separated (\\(r \\rightarrow \\infty\\)) and at rest.
As the electron is brought from infinity into an orbit of radius \\(r\\) by the attractive Coulomb force, work is done by the electric field, lowering the potential energy:
\\[
U(r) = -\\frac{1}{4\\pi\\varepsilon_0}\\frac{Ze^2}{r}
\\]
The total mechanical energy:
\\[
E = K + U = \\left(+\\frac{1}{2}m_e v^2\\right) + \\left(-\\frac{k Z e^2}{r}\\right) = -\\frac{1}{2} \\frac{k Z e^2}{r} = -\\frac{13.6\\text{ eV}}{n^2} < 0
\\]
The negative sign strictly signifies a **bound system**: the electron cannot escape the nucleus on its own. To liberate the electron (set \\(E = 0\\)), an external agent must supply at least \\(+13.6\\text{ eV}\\) of energy (ionization energy).

### 2. Physical Context & Practical Illustration:
A person sitting at the bottom of a well has negative gravitational potential energy relative to the surface; energy must be spent to lift them out.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The negative sign proves the electron is electrostatically bound in an attractive potential well.
- **Option B is incorrect**: Electron charge is negative regardless of state.
- **Option C is incorrect**: Quantum orbits obey forward thermodynamic time.
- **Option D is incorrect**: The negative sign is a rigorous physical consequence of potential energy integration.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.1-OSC-009",
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
    text: "What is the numerical radius of the first Bohr orbit (K shell, \\(n = 1\\)) of a neutral Hydrogen atom?",
    options: [
      "\\(0.529\\text{ Å} = 0.0529\\text{ nm} = 5.29 \\times 10^{-11}\\text{ m}\\)",
      "\\(1.000\\text{ Å} = 0.1000\\text{ nm}\\)",
      "\\(10^{-15}\\text{ m} = 1\\text{ fm}\\)",
      "\\(5.29\\text{ nm} = 5.29 \\times 10^{-9}\\text{ m}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The radius of the \\(n\\)-th Bohr orbit in a hydrogen-like atom (atomic number \\(Z\\)) is:
\\[
r_n = \\frac{4\\pi\\varepsilon_0 \\hbar^2}{m_e e^2} \\cdot \\frac{n^2}{Z}
\\]
For Hydrogen in its ground state (\\(Z = 1, n = 1\\)), this fundamental constant is known as the **Bohr radius** (\\(a_0\\)):
\\[
a_0 = \\frac{(8.854 \\times 10^{-12}) \\times (1.055 \\times 10^{-34})^2}{(9.109 \\times 10^{-31}) \\times (1.602 \\times 10^{-19})^2} = 5.29177 \\times 10^{-11}\\text{ m} \\approx 0.529\\text{ Å} = 0.0529\\text{ nm}
\\]

### 2. Physical Context & Practical Illustration:
The Bohr radius \\(a_0 \\approx 0.53\\text{ Å}\\) sets the fundamental length scale for all atomic, molecular, and chemical bond dimensions in the universe.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(r_1 = 0.529\\text{ Å} = 5.29 \\times 10^{-11}\\text{ m}\\).
- **Option B is incorrect**: \\(1.0\\text{ Å}\\) is the approximate diameter, not the radius.
- **Option C is incorrect**: \\(10^{-15}\\text{ m}\\) is the nuclear radius, not the electron orbital radius.
- **Option D is incorrect**: Off by two orders of magnitude (nm vs Å).`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.1-OSC-010",
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
    text: "For a singly ionized Helium ion (\\(\\text{He}^+\\), \\(Z = 2\\)), what is the radius of the K shell (\\(n = 1\\)) compared to the ground state Bohr radius of Hydrogen (\\(a_0\\))?",
    options: [
      "\\(r_1 = \\frac{a_0}{2} = 0.265\\text{ Å}\\)",
      "\\(r_1 = 2 a_0 = 1.058\\text{ Å}\\)",
      "\\(r_1 = 4 a_0 = 2.116\\text{ Å}\\)",
      "\\(r_1 = \\frac{a_0}{4} = 0.132\\text{ Å}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In Bohr's theory, the orbital radius of a one-electron ion depends on both \\(n\\) and nuclear charge \\(Z\\):
\\[
r_n = a_0 \\frac{n^2}{Z}
\\]
For singly ionized Helium \\(\\text{He}^+\\):
- Principal quantum number \\(n = 1\\) (K shell)
- Atomic number \\(Z = 2\\) (two nuclear protons)
Substituting:
\\[
r_1(\\text{He}^+) = a_0 \\frac{1^2}{2} = \\frac{a_0}{2} = \\frac{0.529\\text{ Å}}{2} = 0.2645\\text{ Å} \\approx 0.265\\text{ Å}
\\]

### 2. Physical Context & Practical Illustration:
Because the \\(\\text{He}^+\\) nucleus has twice the positive charge (\\(+2e\\)) of Hydrogen, it exerts twice the Coulomb attraction, pulling the electron into an orbit half as large.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(r_1 = a_0 / 2 = 0.265\\text{ Å}\\) because \\(r \\propto 1/Z\\).
- **Option B is incorrect**: Multiplies by \\(Z\\) instead of dividing by \\(Z\\).
- **Option C is incorrect**: Scales with \\(Z^2\\) erroneously.
- **Option D is incorrect**: \\(a_0 / 4\\) would correspond to \\(Z = 4\\) (\\(\\text{Be}^{3+}\\)).`
  },

  // 5.3.2 Set B
  {
    questionCode: "MH-8-SCI-5-5.3.2-OSC-006",
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
    text: "What mathematical relation links the energy gap \\(\\Delta E\\) between two electron orbits with the wavelength \\(\\lambda\\) of the emitted light photon?",
    options: [
      "\\(\\Delta E = \\frac{hc}{\\lambda}\\)",
      "\\(\\Delta E = h c \\lambda\\)",
      "\\(\\Delta E = \\frac{\\lambda}{hc}\\)",
      "\\(\\Delta E = \\frac{h}{\\lambda c^2}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
According to Planck and Bohr:
\\[
\\Delta E = E_{\\text{initial}} - E_{\\text{final}} = h\\nu
\\]
Using the wave relation for electromagnetic radiation \\(c = \\nu \\lambda \\implies \\nu = \\frac{c}{\\lambda}\\):
\\[
\\Delta E = \\frac{hc}{\\lambda}
\\]
where:
- \\(h = 6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s}\\) (Planck's constant)
- \\(c = 3.0 \\times 10^8\\text{ m/s}\\) (speed of light in vacuum)
- \\(\\lambda\\) = wavelength of the photon

### 2. Physical Context & Practical Illustration:
A larger energy gap \\(\\Delta E\\) corresponds to a shorter wavelength \\(\\lambda\\) (higher frequency, higher energy photon, e.g. UV or X-rays).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(\\Delta E = \\frac{hc}{\\lambda}\\) is the fundamental Planck-Einstein relation.
- **Option B is incorrect**: Multiplying by \\(\\lambda\\) inverts dimensional energy units.
- **Option C is incorrect**: Inversion of the fraction.
- **Option D is incorrect**: Erroneous dimensions of \\(c^2\\).`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.2-OSC-007",
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
    vault: "practice",
    examCategory: "standard",
    marks: 4,
    penaltyMarks: 1,
    text: "What minimum energy must be supplied to a ground-state Hydrogen atom (\\(n = 1\\), \\(E_1 = -13.6\\text{ eV}\\)) to completely detach the electron from the nucleus (ionization)?",
    options: [
      "\\(+13.6\\text{ eV}\\)",
      "\\(+3.4\\text{ eV}\\)",
      "\\(+10.2\\text{ eV}\\)",
      "\\(0\\text{ eV}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Ionization means transferring the electron from its ground state (\\(n = 1\\)) to infinity (\\(n = \\infty\\)), where it becomes a free electron with zero potential energy:
\\[
E_\\infty = 0\\text{ eV}
\\]
The **Ionization Energy (IE)** is:
\\[
\\text{IE} = E_\\infty - E_1 = 0 - (-13.6\\text{ eV}) = +13.6\\text{ eV}
\\]
In Joules:
\\[
13.6\\text{ eV} = 13.6 \\times 1.602 \\times 10^{-19}\\text{ J} \\approx 2.18 \\times 10^{-18}\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
Any photon with energy \\(\\ge 13.6\\text{ eV}\\) (wavelength \\(\\lambda \\le 91.2\\text{ nm}\\)) has enough punch to ionize hydrogen gas.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The ionization potential of Hydrogen is \\(+13.6\\text{ eV}\\).
- **Option B is incorrect**: \\(3.4\\text{ eV}\\) is the ionization energy from the excited \\(n=2\\) level.
- **Option C is incorrect**: \\(10.2\\text{ eV}\\) is the excitation energy to reach \\(n=2\\), not ionization to infinity.
- **Option D is incorrect**: Zero energy leaves the electron trapped in the ground state.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.2-OSC-008",
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
    text: "If an electron in a sample of hydrogen atoms is excited to the 4th energy level (\\(n = 4\\)), how many different possible spectral emission lines can be observed as the electrons cascade back down to the ground state?",
    options: [
      "6 spectral lines",
      "3 spectral lines",
      "4 spectral lines",
      "16 spectral lines"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
When an ensemble of atoms is excited to principal energy level \\(n\\), electrons can cascade down through various pathways.
The total number of possible distinct emission lines is given by the combination formula \\(^n\\text{C}_2\\):
\\[
N_{\\text{lines}} = \\frac{n(n - 1)}{2}
\\]
For \\(n = 4\\):
\\[
N_{\\text{lines}} = \\frac{4(4 - 1)}{2} = \\frac{4 \\times 3}{2} = 6\\text{ lines}
\\]
The 6 individual transitions are:
1. \\(4 \\rightarrow 1\\) (Lyman series)
2. \\(3 \\rightarrow 1\\) (Lyman series)
3. \\(2 \\rightarrow 1\\) (Lyman series)
4. \\(4 \\rightarrow 2\\) (Balmer series)
5. \\(3 \\rightarrow 2\\) (Balmer series)
6. \\(4 \\rightarrow 3\\) (Paschen series)

### 2. Physical Context & Practical Illustration:
In a gas discharge tube containing trillions of hydrogen atoms, all 6 transition pathways occur simultaneously among different atoms, producing 6 distinct spectral lines on a photographic plate.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(\\frac{4 \\times 3}{2} = 6\\) spectral lines.
- **Option B is incorrect**: 3 represents direct transitions from \\(n=4\\) only, ignoring secondary intermediate cascades.
- **Option C is incorrect**: Confuses shell number \\(n = 4\\) with line count.
- **Option D is incorrect**: \\(n^2 = 16\\) is the total orbital count, not transition combinations.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.2-OSC-009",
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
    text: "What is the typical average lifetime of an electron in an excited state before it spontaneously de-excites to a lower energy shell?",
    options: [
      "Approximately \\(10^{-8}\\text{ seconds}\\) (about 10 nanoseconds)",
      "Approximately 10 seconds",
      "Approximately 1 hour",
      "Infinitely long"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An excited atomic state is inherently unstable. By the principle of minimum potential energy, systems tend toward their lowest possible energy configuration.
Unless a state is 'metastable' (forbidden transition), the spontaneous transition lifetime (mean life \\(\\tau\\)) of an excited atomic orbital is:
\\[
\\tau \\approx 10^{-8}\\text{ s} = 10\\text{ ns}
\\]
Within this ten-billionth of a second, the electron spontaneously drops to a lower level, releasing the energy difference as a photon.

### 2. Physical Context & Practical Illustration:
This rapid nanosecond lifetime is why neon lamps stop glowing almost instantaneously the moment the electrical power switch is turned off.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Mean lifetime of typical atomic excited states is \\(\\approx 10^{-8}\\text{ s}\\).
- **Option B is incorrect**: 10 seconds is a billion times too long for allowed optical dipole transitions.
- **Option C is incorrect**: Macroscopic timescale with no subatomic validity.
- **Option D is incorrect**: Only the ground state has an infinite spontaneous lifetime.`
  },
  {
    questionCode: "MH-8-SCI-5-5.3.2-OSC-010",
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
    text: "What is the maximum wavelength (longest wavelength / series limit) of the photon emitted in the Balmer series of hydrogen (transition from \\(n_i = 3\\) to \\(n_f = 2\\), \\(\\text{H}_\\alpha\\) line)? (Given: \\(R_H \\approx 1.097 \\times 10^7\\text{ m}^{-1}\\))",
    options: [
      "\\(656.3\\text{ nm}\\) (red light)",
      "\\(486.1\\text{ nm}\\) (blue-green light)",
      "\\(121.6\\text{ nm}\\) (ultraviolet light)",
      "\\(364.6\\text{ nm}\\) (ultraviolet edge)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Rydberg's formula for the hydrogen spectrum:
\\[
\\frac{1}{\\lambda} = R_H \\left( \\frac{1}{n_f^2} - \\frac{1}{n_i^2} \\right)
\\]
For the longest wavelength line in the Balmer series (lowest energy transition, \\(n_f = 2\\), \\(n_i = 3\\), the \\(\\text{H}_\\alpha\\) line):
\\[
\\frac{1}{\\lambda} = R_H \\left( \\frac{1}{2^2} - \\frac{1}{3^2} \\right) = R_H \\left( \\frac{1}{4} - \\frac{1}{9} \\right) = R_H \\left( \\frac{5}{36} \\right)
\\]
Solving for \\(\\lambda\\):
\\[
\\lambda = \\frac{36}{5 R_H} = \\frac{36}{5 \\times (1.097 \\times 10^7\\text{ m}^{-1})} = \\frac{36}{5.485 \\times 10^7} \\approx 6.563 \\times 10^{-7}\\text{ m} = 656.3\\text{ nm}
\\]
This corresponds to bright red visible light.

### 2. Physical Context & Practical Illustration:
The \\(656.3\\text{ nm}\\) red \\(\\text{H}_\\alpha\\) emission line gives glowing hydrogen nebulae (like the Orion Nebula) their characteristic vibrant pinkish-red glow in astronomical photographs.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(\\lambda = 656.3\\text{ nm}\\) is the \\(\\text{H}_\\alpha\\) Balmer line.
- **Option B is incorrect**: \\(486.1\\text{ nm}\\) is the \\(\\text{H}_\\beta\\) transition from \\(n = 4 \\rightarrow 2\\).
- **Option C is incorrect**: \\(121.6\\text{ nm}\\) is the Lyman-\\(\\alpha\\) transition (\\(n = 2 \\rightarrow 1\\)) in the UV.
- **Option D is incorrect**: \\(364.6\\text{ nm}\\) is the shortest wavelength series limit (\\(n = \\infty \\rightarrow 2\\)) of the Balmer series.`
  }
];

module.exports = { topic3Part2Questions };
