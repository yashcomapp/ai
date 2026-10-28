const fs = require('fs');
const path = require('path');

const standardOarOptions = [
  "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
  "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
  "Assertion (A) is true, but Reason (R) is false.",
  "Assertion (A) is false, but Reason (R) is true."
];

const enrichedMap = {
  "CBSE-8-CURI-5-5.1.3-OAR-001": {
    text: "Given below are two statements labeled as Assertion (A) and Reason (R):\nAssertion (A): A force comes into play only when there is an interaction between at least two objects.\nReason (R): An isolated object existing alone in space cannot exert a force upon itself to change its state of rest.",
    options: standardOarOptions,
    correctAnswer: "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    solution: "A force is an interaction between two bodies. One object exerts the force while another experiences it. An isolated body with no surrounding matter or fields cannot push or pull itself; therefore, interaction is mandatory.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OAR-002": {
    text: "Given below are two statements labeled as Assertion (A) and Reason (R):\nAssertion (A): When a student holds a heavy school bag by its fabric strap, her fingers feel a downward pull.\nReason (R): Muscular force is a contact force that acts only when there is physical contact between the hand and the bag strap.",
    options: standardOarOptions,
    correctAnswer: "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    solution: "Muscular force is produced by the action of muscles in our body. It can only be exerted on an object through direct physical contact (or through a connector like a strap or rope). Both statements are true and Reason explains Assertion.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OAR-003": {
    text: "Given below are two statements labeled as Assertion (A) and Reason (R):\nAssertion (A): Two bar magnets resting on separate wooden desks 5 meters apart do not noticeably attract or repel each other.\nReason (R): Magnetic force is a non-contact force whose strength decreases rapidly as the distance between the interacting magnets increases.",
    options: standardOarOptions,
    correctAnswer: "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    solution: "Magnetic force acts through magnetic fields without physical contact. However, field intensity diminishes sharply with increasing distance, making the force negligible when the magnets are separated by a large gap.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OMC-001": {
    text: "In a physics class, students are asked to give examples of forces that arise from direct physical contact between interacting bodies (Contact Forces). Which of the following are examples of Contact Forces? (Select all that apply)",
    options: [
      "A bullock pulling a cart across a dirt road (Muscular force)",
      "A dry leaf falling from a tree toward the ground (Gravitational force)",
      "Rubber shoe soles gripping a wet floor to prevent slipping (Friction force)",
      "A magnet picking up steel paperclips from a table without touching them (Magnetic force)"
    ],
    correctAnswer: "A bullock pulling a cart across a dirt road (Muscular force), Rubber shoe soles gripping a wet floor to prevent slipping (Friction force)",
    correctAnswers: [
      "A bullock pulling a cart across a dirt road (Muscular force)",
      "Rubber shoe soles gripping a wet floor to prevent slipping (Friction force)"
    ],
    solution: "Contact forces require physical contact between interacting surfaces. Muscular force and friction are contact forces. Gravity and magnetic force act across empty space without contact (non-contact forces).",
    difficulty: "hard"
  },
  "CBSE-8-CURI-5-5.1.3-OMC-002": {
    text: "Which of the following forces can act on an object across a distance without requiring any direct mechanical or physical contact? (Select all that apply)",
    options: [
      "Gravitational force pulling a cricket ball downward toward Earth",
      "Electrostatic force between a rubbed plastic straw and an uncharged balloon",
      "Frictional force between bicycle tires and the asphalt road",
      "Magnetic force between opposite poles of two bar magnets"
    ],
    correctAnswer: "Gravitational force pulling a cricket ball downward toward Earth, Electrostatic force between a rubbed plastic straw and an uncharged balloon, Magnetic force between opposite poles of two bar magnets",
    correctAnswers: [
      "Gravitational force pulling a cricket ball downward toward Earth",
      "Electrostatic force between a rubbed plastic straw and an uncharged balloon",
      "Magnetic force between opposite poles of two bar magnets"
    ],
    solution: "Gravitational force, electrostatic force, and magnetic force are field forces that act at a distance without physical contact (non-contact forces). Friction requires direct mechanical contact between sliding or rolling surfaces.",
    difficulty: "hard"
  },
  "CBSE-8-CURI-5-5.1.3-OMC-003": {
    text: "During a laboratory lesson on Chapter 5 'Exploring Forces', students test various interacting pairs of objects. Which of the following observations correctly demonstrate the principle that 'forces arise due to interaction'? (Select all that apply)",
    options: [
      "A man standing motionless 2 meters behind a car does not move the car until he physically pushes it.",
      "A compass needle deflects only when a bar magnet is brought into its magnetic neighborhood.",
      "A single stone sitting alone in an empty jar accelerates spontaneously without touching anything.",
      "Two students wearing roller skates push against each other's palms and both roll backward simultaneously."
    ],
    correctAnswer: "A man standing motionless 2 meters behind a car does not move the car until he physically pushes it., A compass needle deflects only when a bar magnet is brought into its magnetic neighborhood., Two students wearing roller skates push against each other's palms and both roll backward simultaneously.",
    correctAnswers: [
      "A man standing motionless 2 meters behind a car does not move the car until he physically pushes it.",
      "A compass needle deflects only when a bar magnet is brought into its magnetic neighborhood.",
      "Two students wearing roller skates push against each other's palms and both roll backward simultaneously."
    ],
    solution: "Forces require interaction. Just standing near a car does not apply force until contact is made. A magnet interacts with a compass through its field. Two skaters pushing each other experience mutual reaction forces, demonstrating mutual interaction.",
    difficulty: "hard"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-001": {
    text: "What is the primary condition necessary for any mechanical force to come into play between physical objects?",
    options: [
      "There must be an interaction between at least two objects.",
      "Both objects must be made of magnetic metals.",
      "The objects must be moving at speeds greater than 10 m/s.",
      "The objects must be submerged in a liquid."
    ],
    correctAnswer: "There must be an interaction between at least two objects.",
    solution: "A force is an interaction between at least two bodies. Without interaction (either via contact or a field), no force can exist or act upon an object.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-002": {
    text: "A man stands 1 meter behind a broken-down car parked on a level road. He watches the car intently for 5 minutes. Why does the car remain completely stationary?",
    options: [
      "Because merely standing near an object does not cause an interaction; a physical push is needed.",
      "Because cars only move if their paint is reflective.",
      "Because the man's gaze applies an opposing gravitational repulsion.",
      "Because the car's engine generates an internal stopping force."
    ],
    correctAnswer: "Because merely standing near an object does not cause an interaction; a physical push is needed.",
    solution: "No force is exerted simply by standing near an object. To apply muscular force, the man must interact physically with the car by placing his hands on it and pushing.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-003": {
    text: "Two school friends wearing roller skates stand face-to-face on a smooth rink. Student X places her palms against Student Y's palms and gives a gentle push. What happens to the two students?",
    options: [
      "Both Student X and Student Y roll backward away from each other.",
      "Only Student Y moves backward, while Student X remains perfectly still.",
      "Only Student X moves forward, while Student Y is glued to the floor.",
      "Neither student moves because forces between friends cancel out."
    ],
    correctAnswer: "Both Student X and Student Y roll backward away from each other.",
    solution: "Force is a mutual interaction. When Student X pushes Student Y, Student Y simultaneously exerts an equal and opposite reaction force on Student X. On low-friction skates, both students accelerate backward away from each other.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-004": {
    text: "Two identical wooden blocks are placed side by side on a clean glass table, separated by a gap of 5 cm. If no person touches them and no air blows, do they exert a mechanical push or pull on each other?",
    options: [
      "No, because there is no mechanical contact or active field interaction between them.",
      "Yes, because wooden blocks always attract each other magnetically.",
      "Yes, because stationary objects generate spontaneous repulsions.",
      "No, unless they are heated with a flame."
    ],
    correctAnswer: "No, because there is no mechanical contact or active field interaction between them.",
    solution: "Mechanical contact forces require physical contact. Without contact or measurable magnetic/electrostatic fields, no noticeable force acts between the two separate blocks.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-005": {
    text: "What does the scientific statement 'Force arises due to interaction' mean in CBSE Class 8 Science?",
    options: [
      "A force is not an isolated property of a single object, but an action between at least two bodies.",
      "Forces can only be generated by living animals and human muscles.",
      "An object stores a reservoir of force inside it that leaks out over time.",
      "Forces only exist when objects are in destructive collisions."
    ],
    correctAnswer: "A force is not an isolated property of a single object, but an action between at least two bodies.",
    solution: "An object does not 'contain' force. Force is an interactive event between two or more bodies (one exerting the force and the other experiencing it).",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-006": {
    text: "A pet owner holds a leather leash attached to a dog's neck collar. When the dog suddenly spots a squirrel and bolts forward, the leash tightens. Which two objects are primarily interacting through tension force to hold the dog back?",
    options: [
      "The dog's collar and the owner's hand via the tightened leash.",
      "The dog's paws and the squirrel's tail across the lawn.",
      "The leather leash and the air molecules surrounding the dog.",
      "The dog's ears and the Earth's magnetic poles."
    ],
    correctAnswer: "The dog's collar and the owner's hand via the tightened leash.",
    solution: "The interaction occurs through the connector (the leash). The owner holds one end, and the dog's collar is attached to the other, transmitting tension force between them.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-007": {
    text: "A student holds a strong bar magnet 2 cm away from an iron paperclip lying on a notebook. The paperclip suddenly leaps across the 2 cm gap and sticks to the magnet. Why did this happen without direct touch?",
    options: [
      "Magnetic force is a non-contact force that acts across space through a magnetic field.",
      "The paperclip melted into a liquid and flowed toward the magnet.",
      "The air between the magnet and paperclip pushed the clip with high pressure.",
      "The magnet generated an electric spark that pulled the paperclip."
    ],
    correctAnswer: "Magnetic force is a non-contact force that acts across space through a magnetic field.",
    solution: "Magnetic force does not require physical contact between the magnet and the magnetic material. The magnetic field exerts an attractive force across the intervening air gap, pulling the paperclip.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-008": {
    text: "Which of the following statements best explains why an isolated object floating in a total vacuum cannot experience an applied muscular force?",
    options: [
      "Muscular force requires physical contact with muscles or limbs of an interacting body.",
      "Muscles cannot produce force in the absence of sunlight.",
      "Objects in a vacuum lose all their mass instantly.",
      "Vacuum creates infinite friction that cancels all forces."
    ],
    correctAnswer: "Muscular force requires physical contact with muscles or limbs of an interacting body.",
    solution: "Muscular force is a contact force. Without another physical body (such as hands or feet) to touch and interact with the object, muscular force cannot be exerted.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-009": {
    text: "A student presses both hands against a solid classroom brick wall and pushes as hard as possible for 30 seconds. The wall does not budge. Did a force interaction take place?",
    options: [
      "Yes, the student exerted a muscular push on the wall, and the wall exerted an equal opposing reaction force on the hands.",
      "No, because in science, force is only defined if the object moves at least 1 meter.",
      "No, inanimate objects like walls are incapable of taking part in force interactions.",
      "Yes, but only because the student's body temperature warmed the brick."
    ],
    correctAnswer: "Yes, the student exerted a muscular push on the wall, and the wall exerted an equal opposing reaction force on the hands.",
    solution: "Force does not require motion to exist. The student applies a contact force, and the rigid wall applies an equal and opposite normal force. The forces are balanced, resulting in zero movement, but the interaction is real.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-010": {
    text: "A ripe coconut detaches from the stem of a tall palm tree and plummets downward toward the sand. Which type of force causes the coconut to fall toward the Earth without any rope or push?",
    options: [
      "Non-contact gravitational force exerted by the Earth on the mass of the coconut.",
      "Contact muscular force exerted by the palm tree branches.",
      "Electrostatic repulsion between the coconut shell and the sky.",
      "Magnetic attraction between coconut water and underground iron ore."
    ],
    correctAnswer: "Non-contact gravitational force exerted by the Earth on the mass of the coconut.",
    solution: "Gravity is a universal non-contact attractive force that Earth exerts on all objects near its surface, pulling them toward its center without requiring physical contact.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-011": {
    text: "In a physics laboratory, a teacher hangs a small iron sphere from a cotton thread. When a bar magnet is brought close to the sphere from the side, the thread tilts toward the magnet. What does this observation illustrate?",
    options: [
      "The magnet exerts an attractive non-contact force across the air gap, pulling the sphere sideways.",
      "The iron sphere was repelled by the surrounding air molecules.",
      "The cotton thread pushed the iron sphere toward the magnet.",
      "The magnet created an electric current that evaporated the air."
    ],
    correctAnswer: "The magnet exerts an attractive non-contact force across the air gap, pulling the sphere sideways.",
    solution: "The magnetic field of the bar magnet exerts an attractive force on the ferromagnetic iron sphere across the space, pulling it away from the vertical resting line.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-012": {
    text: "During a tug-of-war game between Class 8A and Class 8B, both teams pull on the jute rope with great effort. How is the force transmitted between the two teams?",
    options: [
      "Through tension in the rope, which acts as the physical medium connecting the two interacting teams.",
      "Through radio waves traveling through the air between the students.",
      "Through gravitational waves bouncing between the shoes of the competitors.",
      "The rope generates internal energy that pushes both teams away."
    ],
    correctAnswer: "Through tension in the rope, which acts as the physical medium connecting the two interacting teams.",
    solution: "The rope acts as the physical connector. Each team pulls on their end of the rope, setting up tension that transmits forces between the two competing groups.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-013": {
    text: "A hockey ball is resting quietly on an AstroTurf field. Which of the following conditions is strictly required to change its state from rest to motion?",
    options: [
      "An external interaction, such as a player striking the ball with a stick.",
      "Allowing 10 minutes of time to pass undisturbed.",
      "Decreasing the humidity of the ambient air.",
      "Covering the ball with a dark cloth."
    ],
    correctAnswer: "An external interaction, such as a player striking the ball with a stick.",
    solution: "An object at rest cannot move spontaneously. It requires an interaction with an external agent (such as a hockey stick or foot) applying an unbalanced force.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-014": {
    text: "A heavy dictionary rests on a wooden study table. Which pair of forces are actively interacting in the vertical direction to keep the dictionary stationary?",
    options: [
      "The downward gravitational pull of the Earth and the upward normal contact force of the table surface.",
      "Downward atmospheric air pressure and upward magnetic levitation from the carpet.",
      "A forward friction force and a backward tension force.",
      "An inward electrostatic force and an outward centrifugal force."
    ],
    correctAnswer: "The downward gravitational pull of the Earth and the upward normal contact force of the table surface.",
    solution: "The dictionary is pulled downward by Earth's gravity (its weight). The solid tabletop resists compression and exerts an equal upward contact force (normal reaction). These balanced forces keep the dictionary at rest.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-015": {
    text: "A student rubs a plastic ruler vigorously against a woollen sweater and holds it over bits of paper on a desk. The paper bits jump upward and cling to the ruler. Why did this interaction happen?",
    options: [
      "Rubbing transferred electric charges, allowing the charged ruler to exert an attractive non-contact electrostatic force on the paper.",
      "The woollen sweater transferred magnetic north poles to the plastic ruler.",
      "The ruler became hot and created a vacuum that sucked the paper up.",
      "The gravitational pull of the ruler became stronger than the Earth."
    ],
    correctAnswer: "Rubbing transferred electric charges, allowing the charged ruler to exert an attractive non-contact electrostatic force on the paper.",
    solution: "Friction between wool and plastic transfers electrons, charging the ruler. The charged object exerts an electrostatic force on the uncharged paper bits across the air gap, lifting them without direct initial contact.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-016": {
    text: "An astronaut on a spacewalk outside the International Space Station holds a 5 kg metal container while floating freely. If the astronaut throws the container forward, what will happen to the astronaut?",
    options: [
      "The astronaut will accelerate backward, because throwing involves a mutual interaction exerting equal and opposite forces.",
      "The astronaut will stay completely still, because only objects that are thrown move.",
      "The astronaut will accelerate forward alongside the container.",
      "The astronaut will spin downward due to Earth's gravity switching poles."
    ],
    correctAnswer: "The astronaut will accelerate backward, because throwing involves a mutual interaction exerting equal and opposite forces.",
    solution: "Newton's Third Law (mutual interaction): When the astronaut's hands push the container forward, the container exerts an equal and opposite force pushing the astronaut backward. In microgravity, both move in opposite directions.",
    difficulty: "hard"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-017": {
    text: "Why is it more scientifically precise to explain force as 'an interaction between objects' rather than simply 'a push or a pull'?",
    options: [
      "Because interaction highlights that force requires two participants and naturally encompasses non-contact forces like gravity and magnetism.",
      "Because pushes and pulls only happen in mechanical engineering, not physics.",
      "Because the word 'force' cannot be used for moving objects.",
      "Because interaction proves that energy and mass are the same thing."
    ],
    correctAnswer: "Because interaction highlights that force requires two participants and naturally encompasses non-contact forces like gravity and magnetism.",
    solution: "Defining force as an interaction emphasizes that force is mutual (requires at least two bodies) and correctly covers both contact interactions (muscular, friction) and field interactions (gravity, electrostatic, magnetic).",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OSC-018": {
    text: "A student wants to demonstrate to her class that non-contact forces can act across a barrier. She places a steel paperclip on top of a thin cardboard sheet and moves a bar magnet underneath the cardboard. What will happen?",
    options: [
      "The paperclip will follow the magnet across the cardboard, showing that magnetic fields act through non-magnetic barriers.",
      "The paperclip will burst into flames due to electrical short circuiting.",
      "The cardboard will block 100% of the magnetic field, leaving the paperclip motionless.",
      "The magnet will stick permanently to the wood fibers of the cardboard."
    ],
    correctAnswer: "The paperclip will follow the magnet across the cardboard, showing that magnetic fields act through non-magnetic barriers.",
    solution: "Magnetic fields pass through non-magnetic materials like paper, cardboard, glass, and plastic. The magnet beneath the cardboard attracts the steel clip on top, causing it to glide along as the magnet moves.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.3-OTF-001": {
    text: "A solitary object floating in completely empty outer space, far away from all celestial bodies, can experience an applied mechanical force without interacting with anything else.",
    options: ["True", "False"],
    correctAnswer: "False",
    solution: "Force requires an interaction between at least two bodies or a body and a field. An isolated object cannot experience an external force without an interacting partner.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.3-OTF-002": {
    text: "When a bar magnet is brought near an iron nail, an attractive magnetic force comes into play even before the magnet physically touches the nail.",
    options: ["True", "False"],
    correctAnswer: "True",
    solution: "Magnetic force is a non-contact force that operates through a magnetic field across the intervening air space.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.3-OTF-003": {
    text: "When a student sits on a wooden stool, the stool exerts an upward contact force on the student that balances the downward pull of gravity.",
    options: ["True", "False"],
    correctAnswer: "True",
    solution: "The stool provides an upward normal contact force balancing the downward gravitational force (weight), resulting in equilibrium and zero acceleration.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.3-OTF-004": {
    text: "If two physical objects are completely isolated from each other and do not interact through physical contact or force fields, zero force acts between them.",
    options: ["True", "False"],
    correctAnswer: "True",
    solution: "Forces are created by interactions. In the absence of contact or field interaction, no force can exist between two bodies.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.3-OTF-005": {
    text: "Electrostatic forces and magnetic forces are examples of non-contact forces because they can act on objects across empty space without physical contact.",
    options: ["True", "False"],
    correctAnswer: "True",
    solution: "Both electrostatic and magnetic forces operate through electric and magnetic fields, exerting forces across distance without requiring surfaces to touch.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.3-OTF-006": {
    text: "Friction is classified as a non-contact force because it acts between objects without their microscopic surface irregularities interlocking.",
    options: ["True", "False"],
    correctAnswer: "False",
    solution: "Friction is strictly a contact force. It arises precisely from the physical contact and interlocking of microscopic surface irregularities between two touching surfaces.",
    difficulty: "easy"
  }
};

const outputFilePath = path.join(__dirname, '..', 'backups', 'reports', 'enriched_subtopic_5_1_3.json');
fs.writeFileSync(outputFilePath, JSON.stringify(enrichedMap, null, 2), 'utf8');
console.log(`Successfully generated ${Object.keys(enrichedMap).length} enriched questions for Subtopic 5.1.3`);
