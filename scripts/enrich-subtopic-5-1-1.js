const fs = require('fs');
const path = require('path');

const standardOarOptions = [
  "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
  "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
  "Assertion (A) is true, but Reason (R) is false.",
  "Assertion (A) is false, but Reason (R) is true."
];

const enrichedMap = {
  "CBSE-8-CURI-5-5.1.1-OAR-001": {
    text: "Given below are two statements labeled as Assertion (A) and Reason (R):\nAssertion (A): A stationary car parked on a road does not move until a person comes forward and pushes it.\nReason (R): For any mechanical force to come into play, there must be a physical interaction between at least two objects.",
    options: standardOarOptions,
    correctAnswer: "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    solution: "A force is not a property of an isolated object; it arises only when two objects interact. The car remains at rest because no unbalanced force acts upon it. When a person pushes against the car, contact between the person's hands and the car produces an external force that can set the car into motion.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OAR-002": {
    text: "Given below are two statements labeled as Assertion (A) and Reason (R):\nAssertion (A): When an archer stretches the bowstring of a bow to shoot an arrow, the shape of the bow bends.\nReason (R): An applied muscular force can change the shape and curvature of a flexible object.",
    options: standardOarOptions,
    correctAnswer: "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    solution: "When the archer pulls the string, muscular force is exerted on the bow. Force not only changes the state of motion of an object, but can also deform or bend flexible bodies. Here, the force changes the shape of the bow, storing elastic potential energy.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OAR-003": {
    text: "Given below are two statements labeled as Assertion (A) and Reason (R):\nAssertion (A): A cricket fielder stops a fast boundary shot by placing both hands in front of the rolling ball.\nReason (R): An applied external force opposite to the direction of motion can reduce the speed of a moving object to zero.",
    options: standardOarOptions,
    correctAnswer: "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    solution: "When the fielder applies muscular force in the direction opposing the ball's motion, the opposing force decelerates the ball until its velocity becomes zero. This demonstrates that a force can change the speed and state of motion of an object.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OMC-001": {
    text: "In a science laboratory, students are experimenting with different objects using pushes and pulls. Which of the following effects can be directly produced on an object by applying an external force? (Select all that apply)",
    options: [
      "Changing the speed of a moving object",
      "Changing the direction of motion of an object",
      "Changing the total mass of the object",
      "Changing the physical shape of a flexible object"
    ],
    correctAnswer: "Changing the speed of a moving object, Changing the direction of motion of an object, Changing the physical shape of a flexible object",
    correctAnswers: [
      "Changing the speed of a moving object",
      "Changing the direction of motion of an object",
      "Changing the physical shape of a flexible object"
    ],
    solution: "According to the laws of motion in NCERT Class 8, force can: (1) set a stationary body into motion, (2) increase or decrease speed, (3) change the direction of motion, and (4) alter the shape of an object. Force cannot create or destroy mass, so total mass remains strictly constant.",
    difficulty: "hard"
  },
  "CBSE-8-CURI-5-5.1.1-OMC-002": {
    text: "During a classroom discussion on Chapter 5 'Exploring Forces', the teacher asks students to identify the fundamental characteristics of force. Which of the following statements are scientifically correct? (Select all that apply)",
    options: [
      "A force arises only when there is an interaction between at least two bodies.",
      "A force acting in the direction of motion of an object increases its speed.",
      "A single isolated object can exert a force on itself without interacting with any other object.",
      "Forces applied on an object in opposite directions subtract from each other."
    ],
    correctAnswer: "A force arises only when there is an interaction between at least two bodies., A force acting in the direction of motion of an object increases its speed., Forces applied on an object in opposite directions subtract from each other.",
    correctAnswers: [
      "A force arises only when there is an interaction between at least two bodies.",
      "A force acting in the direction of motion of an object increases its speed.",
      "Forces applied on an object in opposite directions subtract from each other."
    ],
    solution: "A force requires interaction between two objects. It cannot act in total isolation. Pushing in the direction of motion increases speed. Opposite forces oppose each other, so the resultant net force is their difference.",
    difficulty: "hard"
  },
  "CBSE-8-CURI-5-5.1.1-OMC-003": {
    text: "Which of the following real-life situations demonstrate an external force causing a change in the state of motion of an object? (Select all that apply)",
    options: [
      "A cyclist applying hand brakes to bring a bicycle to a complete stop",
      "A football striker kicking a stationary ball into the goal net",
      "A textbook resting undisturbed on a flat study table overnight",
      "A hockey player deflecting a moving ball toward a teammate with a stick"
    ],
    correctAnswer: "A cyclist applying hand brakes to bring a bicycle to a complete stop, A football striker kicking a stationary ball into the goal net, A hockey player deflecting a moving ball toward a teammate with a stick",
    correctAnswers: [
      "A cyclist applying hand brakes to bring a bicycle to a complete stop",
      "A football striker kicking a stationary ball into the goal net",
      "A hockey player deflecting a moving ball toward a teammate with a stick"
    ],
    solution: "'State of motion' refers to an object's speed and direction of movement (including rest as zero speed). Braking changes speed from moving to stop. Kicking changes speed from rest to motion. Deflecting changes the direction of motion. A resting book undisturbed is experiencing balanced forces with zero change in state of motion.",
    difficulty: "hard"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-001": {
    text: "Pooja wants to take a notebook out of a tightly packed study desk. She grips the handle of the drawer and slides it toward herself so that she can see inside. Which type of physical action has Pooja performed on the drawer?",
    options: [
      "A pull, because the applied force is directed toward herself.",
      "A push, because any action on furniture is defined as a push.",
      "A gravitational force exerted by the notebook on the desk.",
      "A magnetic repulsion between the handle and her fingers."
    ],
    correctAnswer: "A pull, because the applied force is directed toward herself.",
    solution: "A 'pull' is a force applied in a direction toward the source of the force (the person). When Pooja grips the handle and slides the drawer toward her body, she is exerting a pull.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-002": {
    text: "During a football match at school, an attacker kicks a stationary football from the penalty spot into the goal post. How should the mechanical action exerted by the player's boot on the football be classified?",
    options: [
      "As a push, because the contact force directs the ball forward and away from the player's foot.",
      "As a pull, because the foot drags the ball inward toward the player's knees.",
      "As an electrostatic attraction between the leather ball and the grass blades.",
      "As pure gravity, because only gravity can initiate motion on a sports field."
    ],
    correctAnswer: "As a push, because the contact force directs the ball forward and away from the player's foot.",
    solution: "When the player strikes the ball with his foot, he exerts a contact force directed away from his body, propelling the ball forward. Actions that move an object away from the source of force are classified as pushes.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-003": {
    text: "A student is entering the school library. The door sign says 'PUSH'. When the student applies force on the door plate, the door swings forward into the room and closes behind him. Why is this action classified as a push?",
    options: [
      "Because the force applied moves the door away from the student's body.",
      "Because the force moves the door closer toward the student's chest.",
      "Because library doors can only operate with non-contact magnetic forces.",
      "Because the door increases in weight while swinging on its hinges."
    ],
    correctAnswer: "Because the force applied moves the door away from the student's body.",
    solution: "Applying a force that drives an object away from the person exerting it is defined as a push. Since the student presses the door forward away from himself, it is a push.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-004": {
    text: "In a science activity, Neha holds a soft yellow sponge block between both palms and presses her hands firmly together. She observes that the sponge flattens. When she releases her hands, it springs back to its original form. What property of force does this experiment demonstrate?",
    options: [
      "Force can alter the shape and volume of an elastic object without changing its mass.",
      "Forces can only act on objects that are already in rapid motion.",
      "Compressing an object turns its solid matter into a temporary liquid.",
      "The mass of the sponge increases while her palms are pressing against it."
    ],
    correctAnswer: "Force can alter the shape and volume of an elastic object without changing its mass.",
    solution: "Compressing a sponge between two hands applies opposing contact forces that deform the porous structure, changing its shape. The total amount of matter (mass) inside the sponge remains strictly unchanged.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-005": {
    text: "During a football penalty shootout, the striker fires the ball toward the top corner at high speed. The goalkeeper dives, extends both gloves, and firmly grabs the ball, bringing it to a dead stop. What effect did the goalkeeper's force produce on the ball?",
    options: [
      "It changed the state of motion of the ball from high-speed motion to rest.",
      "It increased the forward speed of the ball toward the net.",
      "It destroyed the mass and chemical composition of the football.",
      "It eliminated the gravitational pull of the Earth on the football."
    ],
    correctAnswer: "It changed the state of motion of the ball from high-speed motion to rest.",
    solution: "When the goalkeeper applies muscular force opposite to the flight of the ball, the ball decelerates until its speed becomes zero. This is a classic demonstration of an external force changing the state of motion of a moving body.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-006": {
    text: "In an Indian classical music concert, a musician tunes a sitar by gently pulling the metallic string sideways with his index finger and releasing it to create a musical note. Which of the following best describes this mechanical action?",
    options: [
      "A pull, because the musician draws the string toward his fingers, displacing it from its rest position.",
      "A push, because strings can only vibrate under forward compression.",
      "A gravitational force exerted by the wooden body of the sitar on the air.",
      "A chemical reaction between the musician's fingernails and the metal alloy."
    ],
    correctAnswer: "A pull, because the musician draws the string toward his fingers, displacing it from its rest position.",
    solution: "Plucking a sitar string involves gripping or hooking the string and drawing it toward oneself against its tension. Displacing an object toward oneself is classified as a pull.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-007": {
    text: "During a school Sports Day tug-of-war match, Team A pulls the rope to the left with a force of 500 N, while Team B pulls the rope to the right with a force of 420 N. What is the magnitude and direction of the net resultant force acting on the rope?",
    options: [
      "80 N toward the left, because opposing forces subtract from each other.",
      "920 N toward the left, because all applied forces always add up.",
      "80 N toward the right, because the smaller force always determines direction.",
      "0 N, because ropes in sports cannot carry an unbalanced force."
    ],
    correctAnswer: "80 N toward the left, because opposing forces subtract from each other.",
    solution: "When two forces act along the same straight line in opposite directions on an object, the net force is equal to the difference between the two forces: 500 N - 420 N = 80 N. The object accelerates in the direction of the larger force (to the left, toward Team A).",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-008": {
    text: "A warehouse worker is moving heavy cartons across a concrete floor. He stands behind a large 40 kg wooden box, places his hands against the rear side, and drives it forward toward the storage bay. How should this action be categorized?",
    options: [
      "A push, because the applied force is directed forward, moving the box away from the worker.",
      "A pull, because moving any heavy object requires a towing pull.",
      "A frictional force acting in the forward direction of motion.",
      "A magnetic repulsion between the concrete floor and the wooden base."
    ],
    correctAnswer: "A push, because the applied force is directed forward, moving the box away from the worker.",
    solution: "When the worker leans against the rear of the box and exerts force directed forward (away from his body), the action is classified as a push.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-009": {
    text: "A cricket bowler bowls a ball toward a batsman at 120 km/h. The batsman swings his bat and drives the ball through the covers toward the boundary at 90 km/h in a different direction. What fundamental property of force does this hit illustrate?",
    options: [
      "An applied force can alter both the speed and the direction of motion of a moving body.",
      "An applied force can only change speed, while direction changes require electric fields.",
      "The collision destroys the mass of the cricket ball temporarily.",
      "The bat does not exert any mechanical force on the cricket ball."
    ],
    correctAnswer: "An applied force can alter both the speed and the direction of motion of a moving body.",
    solution: "When the bat strikes the ball, it delivers an impulsive contact force that changes both the ball's speed and its direction of travel. This demonstrates that a force can modify the entire state of motion of an object.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-010": {
    text: "At a railway station, a passenger holds the telescopic handle of a wheeled suitcase and walks along the platform, leading the suitcase behind her. Which of the following statements correctly identifies the primary action on the suitcase?",
    options: [
      "The passenger is pulling the suitcase, because the applied force draws the suitcase forward along her path.",
      "The passenger is pushing the suitcase, because wheels always require forward compression.",
      "The suitcase moves on its own because wheels completely eliminate all forces.",
      "The suitcase moves forward due to gravitational repulsion from the railway platform."
    ],
    correctAnswer: "The passenger is pulling the suitcase, because the applied force draws the suitcase forward along her path.",
    solution: "When the passenger holds the handle and walks ahead of the suitcase, her arm exerts tension that pulls the suitcase behind her. Drawing an object along one's path toward oneself is classified as a pull.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-011": {
    text: "A student rolls a glass marble across a very smooth horizontal glass table. In a theoretical ideal situation where air resistance and friction between surfaces are completely zero, what will happen to the moving marble?",
    options: [
      "It will continue to move in a straight line at a constant speed forever.",
      "It will automatically stop moving after traveling exactly one meter.",
      "It will spontaneously change its direction without any contact.",
      "It will accelerate rapidly and fly upward into the ceiling."
    ],
    correctAnswer: "It will continue to move in a straight line at a constant speed forever.",
    solution: "According to Newton's First Law of Motion (and Galileo's principle taught in Class 8), a body in motion will continue to move with constant speed along a straight path unless acted upon by an external unbalanced force. Without friction or air resistance, the marble never slows down.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-012": {
    text: "A village blacksmith heats an iron rod red-hot in a furnace and repeatedly strikes it with a heavy steel hammer to flatten the tip into a sharp spade. Which of the following statements correctly explains the physical effect of the hammer's blows?",
    options: [
      "The repeated impact force deforms the heated iron, altering its shape into a flat blade.",
      "The hammer strikes increase the total mass and density of iron atoms.",
      "The hammer strikes destroy the gravitational pull acting on the iron rod.",
      "The shape change is caused only by heat, while the hammer exerts zero force."
    ],
    correctAnswer: "The repeated impact force deforms the heated iron, altering its shape into a flat blade.",
    solution: "Heating softens the metallic bonds in iron, making it malleable. When the heavy hammer strikes the hot iron, it exerts a large contact force that flattens and reshapes the metal into a blade. Total mass remains strictly conserved.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-013": {
    text: "In a rural village, a farmer draws drinking water from a 20-meter deep open well using a bucket attached to a thick jute rope passing over a pulley. Why is the act of lifting the bucket classified as a pull?",
    options: [
      "Because the farmer exerts tension on the rope, drawing the rope toward his hands to raise the bucket.",
      "Because ropes can only transmit push forces through a pulley groove.",
      "Because water inside a bucket automatically exerts an upward push.",
      "Because the pulley creates a magnetic field that lifts the water."
    ],
    correctAnswer: "Because the farmer exerts tension on the rope, drawing the rope toward his hands to raise the bucket.",
    solution: "Flexible ropes cannot be pushed; they can only transmit tension when pulled. The farmer grips the rope and pulls it downward toward himself, causing the bucket on the other side of the pulley to rise upward.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-015": {
    text: "Two students, Aman and Kabir, are trying to move a heavy steel filing cabinet across a classroom floor. Aman pushes from the left with a force of 70 N, while Kabir pushes from the right with a force of 45 N. Assuming floor friction is negligible, what will happen to the cabinet?",
    options: [
      "The cabinet will accelerate toward the right with a net resultant force of 25 N.",
      "The cabinet will move toward the left with a combined force of 115 N.",
      "The cabinet will remain completely stationary because forces always cancel out.",
      "The cabinet will lift off the floor due to balanced horizontal forces."
    ],
    correctAnswer: "The cabinet will accelerate toward the right with a net resultant force of 25 N.",
    solution: "Because the forces act in opposite directions along the same horizontal line, they subtract: Net Force = 70 N (to right) - 45 N (to left) = 25 N toward the right (in the direction of the larger force exerted by Aman).",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-016": {
    text: "Two children play with a wooden toy car on a carpeted floor. Each child ties a string to opposite ends of the car and pulls horizontally with an equal force of exactly 15 N in opposite directions. Which of the following correctly describes the net force and movement of the car?",
    options: [
      "The net force is 0 N, and the toy car remains completely stationary.",
      "The net force is 30 N, and the car moves back and forth rapidly.",
      "The net force is 15 N, and the car moves toward the older child.",
      "The toy car will start spinning because equal forces cause rotation."
    ],
    correctAnswer: "The net force is 0 N, and the toy car remains completely stationary.",
    solution: "When two equal forces act in opposite directions along the same line of action on an object, the resultant net force is zero: 15 N - 15 N = 0 N. With balanced forces and zero net force, the car remains at rest.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-017": {
    text: "A student rubs a plastic comb briskly against dry hair and holds it 1 cm above tiny scraps of paper resting on a table. Without the comb touching the paper, the scraps leap upward and cling to the comb. What does this observation teach us about forces?",
    options: [
      "Forces can act across a distance without direct physical contact between the two interacting bodies.",
      "Pushes and pulls can only happen when surfaces rub against each other directly.",
      "Dry hair destroys the gravitational attraction of the Earth on paper.",
      "The paper jumps because the air between the comb and paper becomes a vacuum."
    ],
    correctAnswer: "Forces can act across a distance without direct physical contact between the two interacting bodies.",
    solution: "Rubbing the plastic comb transfers electrons, giving it an electrostatic charge. The charged comb exerts an attractive electrostatic force on the paper scraps across the air gap. This proves that non-contact forces can act without physical contact.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OSC-018": {
    text: "In textbook science, why is it essential to define force as 'an interaction between at least two objects' rather than simply 'a push or a pull'?",
    options: [
      "Because a force cannot exist on an isolated object; one object must exert the force while another experiences it.",
      "Because pushes and pulls only occur in sports and cannot happen in daily life.",
      "Because single objects only experience force if their temperature is above boiling point.",
      "Because forces only exist when three or more objects are touching simultaneously."
    ],
    correctAnswer: "Because a force cannot exist on an isolated object; one object must exert the force while another experiences it.",
    solution: "A force is an interaction between two objects. An isolated single object cannot push or pull itself. There must always be at least two bodies interacting (e.g. foot and football, hand and door, magnet and iron nail) for a force to come into play.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OTF-001": {
    text: "In everyday language and elementary physics, any action that involves pushing or pulling an object to change its position, speed, or direction can be classified as a force.",
    options: ["True", "False"],
    correctAnswer: "True",
    solution: "In science, a push or a pull on an object is broadly termed a force. Whenever an interaction involves pushing, pulling, kicking, lifting, or hitting, a force is acting.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.1-OTF-002": {
    text: "A stationary football resting on an open playground can start rolling rapidly on its own without any wind, incline, or external push/pull acting upon it.",
    options: ["True", "False"],
    correctAnswer: "False",
    solution: "A stationary object cannot change its state of rest without an external unbalanced force acting upon it. Without any external force (such as a kick, a push, or strong wind), the ball will remain at rest.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.1-OTF-003": {
    text: "Common daily actions such as lifting a school bag, kicking a ball, opening a drawer, and flicking a carrom striker are all examples of forces acting as pushes or pulls.",
    options: ["True", "False"],
    correctAnswer: "True",
    solution: "Lifting and opening a drawer are forms of pulling; kicking and flicking are forms of pushing. All these physical actions exert contact forces on the respective objects.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.1-OTF-004": {
    text: "When a person pushes against a solid brick wall, the wall does not move. Therefore, scientifically speaking, zero force was applied by the person's hands.",
    options: ["True", "False"],
    correctAnswer: "False",
    solution: "Even if an object does not move, force is still applied. The person exerts a muscular force on the wall, and the wall exerts an equal and opposite normal force. The forces are balanced, resulting in zero net motion, but force is definitely present.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OTF-005": {
    text: "A single isolated object floating in deep outer space can experience a mechanical force without interacting with any other object or field.",
    options: ["True", "False"],
    correctAnswer: "False",
    solution: "A force requires an interaction between at least two bodies (or a body and a field). An isolated body with no surrounding matter or fields cannot experience a force.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.1-OTF-006": {
    text: "When two people push a broken-down car from behind in the same forward direction, their individual forces combine together to produce a larger net force.",
    options: ["True", "False"],
    correctAnswer: "True",
    solution: "Forces applied on an object in the same direction add up to one another. If person A exerts 200 N and person B exerts 250 N in the same direction, the total net force is 450 N.",
    difficulty: "easy"
  }
};

const outputFilePath = path.join(__dirname, '..', 'backups', 'reports', 'enriched_subtopic_5_1_1.json');
fs.writeFileSync(outputFilePath, JSON.stringify(enrichedMap, null, 2), 'utf8');
console.log(`Successfully generated ${Object.keys(enrichedMap).length} enriched questions for Subtopic 5.1.1`);
