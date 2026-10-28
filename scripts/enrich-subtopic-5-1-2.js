const fs = require('fs');
const path = require('path');

const standardOarOptions = [
  "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
  "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
  "Assertion (A) is true, but Reason (R) is false.",
  "Assertion (A) is false, but Reason (R) is true."
];

const enrichedMap = {
  "CBSE-8-CURI-5-5.1.2-OAR-001": {
    text: "Given below are two statements labeled as Assertion (A) and Reason (R):\nAssertion (A): Opening a sliding wooden drawer requires a pulling action, whereas shutting it requires a pushing action.\nReason (R): In elementary physics, a force directed toward the person is classified as a pull, while a force directed away from the person is classified as a push.",
    options: standardOarOptions,
    correctAnswer: "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    solution: "When opening a drawer, a person applies force toward their body (a pull). When closing it, the force is directed away from the body into the desk (a push). Therefore, both statements are true and Reason correctly explains Assertion.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OAR-002": {
    text: "Given below are two statements labeled as Assertion (A) and Reason (R):\nAssertion (A): When a player kicks a football, the ball immediately accelerates forward and moves away from the player.\nReason (R): Kicking is an impulsive push force that alters the state of motion of the ball from rest to motion.",
    options: standardOarOptions,
    correctAnswer: "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    solution: "Kicking imparts a sharp contact force directed away from the player's foot. This unbalanced force changes the ball's state of motion, giving it velocity and kinetic energy.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OAR-003": {
    text: "Given below are two statements labeled as Assertion (A) and Reason (R):\nAssertion (A): Lifting a bucket full of water vertically upward from the floor requires an upward muscular force greater than the weight of the bucket.\nReason (R): The applied upward force must overcome the downward gravitational pull exerted by the Earth on the water and bucket.",
    options: standardOarOptions,
    correctAnswer: "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    solution: "Earth pulls the bucket downward with gravity (its weight). To lift it off the ground, a person must apply an upward contact force (pull) that equals and slightly exceeds gravity so that a net upward acceleration is created.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OMC-001": {
    text: "In daily household chores and school activities, forces can be classified as pushes or pulls. Which of the following actions rely primarily on a 'pull' force? (Select all that apply)",
    options: [
      "Drawing a bucket of water up from a well using a rope",
      "Opening a hinged window that swings inward toward you",
      "Pushing a manual lawnmower forward across a grassy lawn",
      "Plucking the string of an acoustic guitar"
    ],
    correctAnswer: "Drawing a bucket of water up from a well using a rope, Opening a hinged window that swings inward toward you, Plucking the string of an acoustic guitar",
    correctAnswers: [
      "Drawing a bucket of water up from a well using a rope",
      "Opening a hinged window that swings inward toward you",
      "Plucking the string of an acoustic guitar"
    ],
    solution: "Drawing water from a well involves pulling the rope. Opening an inward-swinging window draws it toward oneself (a pull). Plucking a guitar string draws the string sideways toward the fingers (a pull). Moving a lawnmower forward is a push.",
    difficulty: "hard"
  },
  "CBSE-8-CURI-5-5.1.2-OMC-002": {
    text: "Which of the following common actions performed in sports and daily life are scientifically categorized as 'pushes'? (Select all that apply)",
    options: [
      "Striking a carrom striker with your finger to hit a coin",
      "Kicking a football toward the goalpost",
      "Opening a desk drawer by pulling its handle",
      "Closing an open refrigerator door by pressing against the door face"
    ],
    correctAnswer: "Striking a carrom striker with your finger to hit a coin, Kicking a football toward the goalpost, Closing an open refrigerator door by pressing against the door face",
    correctAnswers: [
      "Striking a carrom striker with your finger to hit a coin",
      "Kicking a football toward the goalpost",
      "Closing an open refrigerator door by pressing against the door face"
    ],
    solution: "Striking a carrom coin, kicking a ball, and shutting a refrigerator door all apply forces directed away from the person, moving the object away from the body. These are pushes. Opening a drawer draws it toward the body, which is a pull.",
    difficulty: "hard"
  },
  "CBSE-8-CURI-5-5.1.2-OMC-003": {
    text: "Consider a classroom door fitted with a handle and hinges. Which of the following statements correctly describe the forces involved in operating this door? (Select all that apply)",
    options: [
      "Pulling the handle inward toward yourself applies a force that opens an inward-swinging door.",
      "Pushing against the door surface applies a force that drives the door forward to close it.",
      "A door can open and close continuously without any interaction with people or wind.",
      "The hinges act as a pivot point around which the door rotates when a push or pull is exerted."
    ],
    correctAnswer: "Pulling the handle inward toward yourself applies a force that opens an inward-swinging door., Pushing against the door surface applies a force that drives the door forward to close it., The hinges act as a pivot point around which the door rotates when a push or pull is exerted.",
    correctAnswers: [
      "Pulling the handle inward toward yourself applies a force that opens an inward-swinging door.",
      "Pushing against the door surface applies a force that drives the door forward to close it.",
      "The hinges act as a pivot point around which the door rotates when a push or pull is exerted."
    ],
    solution: "Doors require external force (from human hands, wind, or door closers) to move. Pulling moves it toward you; pushing moves it away. The hinges provide the fixed axis of rotation.",
    difficulty: "hard"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-001": {
    text: "During a physical education class, Ravi uses his foot to kick a stationary football lying on the ground across the sports field. Which of the following statements correctly describes this action?",
    options: [
      "It is an impulsive push force applied by his foot that accelerates the ball forward.",
      "It is a pull force that draws the football closer to his knees.",
      "It is a magnetic repulsion between the rubber boot and the synthetic grass.",
      "It is an electrostatic interaction caused by running in sports shoes."
    ],
    correctAnswer: "It is an impulsive push force applied by his foot that accelerates the ball forward.",
    solution: "Kicking exerts a sharp contact force directed away from the foot, transferring momentum and setting the stationary ball into forward motion. Actions driving objects away are pushes.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-002": {
    text: "An artisan is drawing drinking water from a village well. He grabs the rope with both hands and leans back, pulling the rope down toward his chest to bring the bucket up. What type of mechanical action is being applied to the rope?",
    options: [
      "A pulling action, because force is exerted along the rope toward the artisan's body.",
      "A pushing action, because water always exerts an upward push.",
      "A purely rotational force with zero linear tension in the rope.",
      "A non-contact gravitational force generated by the artisan's arms."
    ],
    correctAnswer: "A pulling action, because force is exerted along the rope toward the artisan's body.",
    solution: "The artisan applies tension by drawing the rope toward himself. Ropes cannot be pushed; they transmit force purely through tension when pulled.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-003": {
    text: "A shopkeeper wants to secure his shop in the evening. He pushes a heavy iron shutter downward until it clicks shut against the ground. How should the force exerted by the shopkeeper be classified?",
    options: [
      "As a downward push, because his hands press the shutter away from his chest toward the ground.",
      "As an upward pull, because iron shutters always resist movement with pull forces.",
      "As an electrostatic attraction between the metal shutter and the floor tile.",
      "As a magnetic force produced by the lock mechanism."
    ],
    correctAnswer: "As a downward push, because his hands press the shutter away from his chest toward the ground.",
    solution: "Applying a force that drives an object away from the person's torso (in this case, pushing downward away from the shoulders) is classified as a push.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-004": {
    text: "A student is playing with a toy bow and arrow made of flexible plastic. When she grips the arrow nock and pulls the elastic string backward, what effect does her muscular force have on the bow?",
    options: [
      "It bends the bow limbs, temporarily changing their shape and storing elastic energy.",
      "It permanently destroys the plastic material of the bow.",
      "It turns the solid bow limbs into a flexible liquid.",
      "It increases the total weight and mass of the plastic bow."
    ],
    correctAnswer: "It bends the bow limbs, temporarily changing their shape and storing elastic energy.",
    solution: "Pulling the string exerts a bending force on the bow limbs, altering their curvature (changing their shape). When released, the stored elastic potential energy propels the arrow forward.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-005": {
    text: "A hockey player wants to pass the ball to a teammate standing 10 meters away on the grass. He places the curved face of his stick against the ball and flicks it sharply forward. What kind of force action is this flick?",
    options: [
      "A push, because the stick exerts a forward contact force moving the ball away from the player.",
      "A pull, because hockey sticks can only drag balls backward.",
      "A non-contact gravitational pull exerted by the stick on the ball.",
      "An electrostatic discharge between the wooden stick and the ball."
    ],
    correctAnswer: "A push, because the stick exerts a forward contact force moving the ball away from the player.",
    solution: "Flicking or hitting a ball forward with a stick applies a contact force directed away from the player. This is a classic push.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-006": {
    text: "During an art class, a student presses a lump of soft sculpting clay between her thumbs and fingers to make a hollow bowl. Which of the following best describes the physical effect of her applied forces?",
    options: [
      "The forces change the shape and structure of the clay without altering its mass.",
      "The forces create new clay atoms, increasing the total mass.",
      "The forces can only change shape if the clay is moving at 10 m/s.",
      "The clay changes shape purely due to atmospheric pressure dropping in the room."
    ],
    correctAnswer: "The forces change the shape and structure of the clay without altering its mass.",
    solution: "Muscular contact forces applied on non-rigid, plastic materials like modeling clay or dough change their shape and contour. Mass remains strictly conserved.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-007": {
    text: "Two teams are competing in a tug-of-war contest. The red ribbon tied in the center of the rope stays completely stationary above the white chalk line on the grass. What can we scientifically conclude about the forces exerted by the two teams?",
    options: [
      "Both teams are pulling with equal force in opposite directions, resulting in zero net force.",
      "Neither team is applying any force on the rope.",
      "Team A is applying a push while Team B is applying a pull in the same direction.",
      "The rope stays stationary because ropes are immune to external forces."
    ],
    correctAnswer: "Both teams are pulling with equal force in opposite directions, resulting in zero net force.",
    solution: "When two teams pull in opposite directions with equal magnitudes, the forces balance each other (Net Force = F - F = 0 N). An object experiencing balanced forces remains at rest.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-008": {
    text: "In a supermarket, a customer pushes a loaded shopping cart along a flat tiled aisle. To turn the cart to the right into the snack aisle, the customer applies a sideways force to the cart handle. What effect does this sideways force produce?",
    options: [
      "It changes the direction of motion of the shopping cart.",
      "It permanently increases the mass of the groceries inside the cart.",
      "It eliminates the contact friction between the wheels and the floor.",
      "It causes the cart to fly upward toward the ceiling."
    ],
    correctAnswer: "It changes the direction of motion of the shopping cart.",
    solution: "Applying a force perpendicular to the direction of motion changes the direction of travel without necessarily changing speed. This demonstrates that force can alter the direction component of velocity.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-009": {
    text: "A cyclist traveling on a straight tarmac road applies the hand brakes firmly upon seeing a pedestrian. The rubber brake pads clamp against the metal wheel rims, bringing the bicycle to a stop. What did the braking force do to the state of motion?",
    options: [
      "It exerted an opposing frictional force that reduced the speed of the bicycle from moving to rest.",
      "It increased the forward velocity of the bicycle.",
      "It removed the gravitational pull of the Earth on the bicycle.",
      "It converted the bicycle into an isolated system with no external interactions."
    ],
    correctAnswer: "It exerted an opposing frictional force that reduced the speed of the bicycle from moving to rest.",
    solution: "Brake pads exert friction opposing the rotation of the wheels and motion of the bike. This opposing force decelerates the bicycle until its speed drops to zero, changing its state of motion.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-010": {
    text: "A student is opening an English textbook lying on a desk. She places her fingers under the front cover and lifts it upward and backward toward herself so that she can read page 1. How should this action be categorized?",
    options: [
      "A pull, because her fingers draw the cover upward and backward toward herself.",
      "A push, because any motion involving paper is a push.",
      "A non-contact magnetic repulsion between her fingers and the paper.",
      "A chemical action between ink and skin."
    ],
    correctAnswer: "A pull, because her fingers draw the cover upward and backward toward herself.",
    solution: "Lifting the cover toward oneself applies a force directed toward the person, which is categorized as a pull.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-011": {
    text: "A gardener pushes a wheelbarrow loaded with soil across the lawn. When he reaches a garden bed, he lifts the handles upward and forward to dump the soil out. Which statement correctly describes the forces applied during this process?",
    options: [
      "Pushing forward drives the wheelbarrow across the grass, while tilting the handles applies a force to change its orientation.",
      "The wheelbarrow moves solely due to internal forces generated by the soil.",
      "No force is needed to move a wheelbarrow once it has wheels.",
      "The soil falls out because gravity turns off when handles are lifted."
    ],
    correctAnswer: "Pushing forward drives the wheelbarrow across the grass, while tilting the handles applies a force to change its orientation.",
    solution: "The gardener exerts a horizontal push to move the wheelbarrow forward and an upward/rotational force on the handles to tilt the tray, allowing gravity to unload the soil.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-012": {
    text: "A tennis player hits an incoming tennis ball with high speed across the net. During the fraction of a second the ball is in contact with the racket strings, what happens to the ball?",
    options: [
      "The ball compresses momentarily (changing shape), and the force reverses its direction of motion.",
      "The ball's mass becomes zero during the impact.",
      "The ball travels through the racket strings without experiencing any force.",
      "The ball increases in temperature until it melts into rubber liquid."
    ],
    correctAnswer: "The ball compresses momentarily (changing shape), and the force reverses its direction of motion.",
    solution: "High-speed cameras show that during impact, the racket strings exert a large contact force that temporarily deforms (flattens) the tennis ball and reverses its direction of travel at high speed.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-013": {
    text: "A school bus is stuck in wet mud on a rainy morning. Four students and the driver stand behind the bus and push together in the same forward direction with forces of 250 N each. What is the total combined pushing force exerted on the bus?",
    options: [
      "1250 N in the forward direction, because forces in the same direction add together.",
      "0 N, because multiple people pushing always cancel each other out.",
      "250 N, because only the driver's force counts.",
      "500 N in the reverse direction, because mud opposes all forces."
    ],
    correctAnswer: "1250 N in the forward direction, because forces in the same direction add together.",
    solution: "When multiple forces act along the same line in the same direction, they add arithmetically: 5 people * 250 N = 1250 N forward. This combined net force helps overcome the mud resistance.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-015": {
    text: "A student is pulling a wooden block along a smooth lab table with a spring balance attached to it. The spring balance pointer stretches and shows a reading of 4.5 N. What does this reading indicate?",
    options: [
      "The magnitude of the pulling force exerted by the student on the wooden block.",
      "The total mass of the wooden block in kilograms.",
      "The volume of air displaced by the wooden block.",
      "The temperature change inside the spring balance."
    ],
    correctAnswer: "The magnitude of the pulling force exerted by the student on the wooden block.",
    solution: "A spring balance measures the magnitude of force (in Newtons) by the extension of its calibrated internal spring. A reading of 4.5 N indicates that a pulling force of 4.5 Newtons is being applied.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-016": {
    text: "A rubber ball is dropped from a height of 2 meters onto a hard concrete floor. When it strikes the floor, it bounces back upward. Which force is primarily responsible for reversing the downward motion of the ball into an upward bounce?",
    options: [
      "An upward normal contact force exerted by the hard floor on the compressed ball.",
      "An upward magnetic pull exerted by the ceiling of the room.",
      "Earth's gravity suddenly switching from downward to upward.",
      "The air inside the ball escaping into the room."
    ],
    correctAnswer: "An upward normal contact force exerted by the hard floor on the compressed ball.",
    solution: "Upon collision, the ball compresses against the rigid floor. The floor exerts an equal and opposite upward contact force (normal reaction) on the ball, accelerating it upward and causing the bounce.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-017": {
    text: "A student holds an inflated balloon between both hands and presses inward firmly. The balloon changes from a round spherical shape to an oval shape. Why does this change in shape occur?",
    options: [
      "The opposing inward forces exerted by her hands compress the flexible rubber skin and redistribute the air inside.",
      "The air molecules inside the balloon were destroyed by the pressure.",
      "The rubber skin turned into a liquid under hand temperature.",
      "The mass of the balloon decreased by half."
    ],
    correctAnswer: "The opposing inward forces exerted by her hands compress the flexible rubber skin and redistribute the air inside.",
    solution: "Applying balanced inward contact forces deforms the flexible rubber wall of the balloon, reshaping it without changing the mass or volume of enclosed air.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OSC-018": {
    text: "Why does a cricket ball rolling across a grass field gradually slow down and stop by itself, even if no player touches it?",
    options: [
      "Because an opposing contact force called friction acts between the rolling ball and the blades of grass.",
      "Because all moving objects naturally run out of energy and die after 10 seconds.",
      "Because Earth's gravity only pulls moving objects when they roll on grass.",
      "Because the mass of the cricket ball increases as it rolls."
    ],
    correctAnswer: "Because an opposing contact force called friction acts between the rolling ball and the blades of grass.",
    solution: "The ball does not stop 'on its own'; it stops because the contact force of friction between the grass and the leather surface acts in the direction opposite to motion, gradually decelerating the ball to zero speed.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OTF-001": {
    text: "In everyday situations, actions like opening a door, kicking a ball, or lifting a bag can always be grouped into the fundamental categories of pushes and pulls.",
    options: ["True", "False"],
    correctAnswer: "True",
    solution: "In elementary science, all mechanical contact actions—such as kicking, hitting, lifting, dragging, or pressing—are essentially variations of a push or a pull.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.2-OTF-002": {
    text: "Applying a force to an object can change its speed, its direction of motion, or its shape, but it can never change all three simultaneously.",
    options: ["True", "False"],
    correctAnswer: "False",
    solution: "A force can change all three simultaneously. For example, when a tennis ball hits a racket at an angle, the ball deforms (changes shape), changes its speed, and changes its direction of motion all at the same moment.",
    difficulty: "medium"
  },
  "CBSE-8-CURI-5-5.1.2-OTF-003": {
    text: "If two equal forces act on an object in exactly opposite directions along the same line, the object will experience an acceleration in the direction of the first force.",
    options: ["True", "False"],
    correctAnswer: "False",
    solution: "When two forces of equal magnitude act in opposite directions on an object, the resultant net force is zero (F - F = 0 N). With zero net force, there is no acceleration; the object remains in its current state of rest or uniform motion.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.2-OTF-004": {
    text: "When a blacksmith hammers a hot piece of iron, the applied force changes the shape of the iron while keeping its total mass conserved.",
    options: ["True", "False"],
    correctAnswer: "True",
    solution: "Mechanical forces deform malleable metals without creating or destroying matter, so the shape changes while the mass remains strictly constant.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.2-OTF-005": {
    text: "A force can act on an object only when a person or machine is physically touching that object directly.",
    options: ["True", "False"],
    correctAnswer: "False",
    solution: "Non-contact forces such as gravity, magnetic force, and electrostatic force can act across a distance without any direct physical contact.",
    difficulty: "easy"
  },
  "CBSE-8-CURI-5-5.1.2-OTF-006": {
    text: "When you squeeze a tube of toothpaste, the muscular force applied by your fingers changes the shape of the tube and forces the paste to move forward.",
    options: ["True", "False"],
    correctAnswer: "True",
    solution: "Squeezing is a contact force that deforms the flexible tube walls (shape change) and exerts pressure that expels the paste out of the nozzle (state of motion change).",
    difficulty: "easy"
  }
};

const outputFilePath = path.join(__dirname, '..', 'backups', 'reports', 'enriched_subtopic_5_1_2.json');
fs.writeFileSync(outputFilePath, JSON.stringify(enrichedMap, null, 2), 'utf8');
console.log(`Successfully generated ${Object.keys(enrichedMap).length} enriched questions for Subtopic 5.1.2`);
