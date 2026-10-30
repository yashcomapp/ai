# scripts/generate_ch15_topic4.py
# MH-9-SCIT-15-15.4: Coordination in Humans: Nervous System (CNS, PNS, ANS, Reflex Action)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-15-15.4"

exam_data = [
    # 1-10: Neuron Anatomy & Nerve Impulse
    ("What is the structural and functional unit of the human nervous system?",
     ["Neuron (nerve cell)", "Nephron", "Glial cell", "Muscle fiber"],
     "A", "OSC", "easy",
     "The neuron is the primary excitable structural and functional unit of the nervous system, specialized for receiving, conducting, and transmitting electrical impulses."),

    ("Which part of a neuron contains the nucleus, cytoplasm, and Nissl's granules, serving as the metabolic control center?",
     ["Cyton (cell body / soma)", "Axon", "Dendrite", "Myelin sheath"],
     "A", "OSC", "easy",
     "The cyton (soma) contains the metabolic machinery, including the nucleus, neuroplasm, and protein-synthesizing Nissl's granules."),

    ("What are the short, branched cytoplasmic extensions that receive nerve impulses from sensory receptors or neighboring neurons and conduct them TOWARDS the cyton?",
     ["Dendrites", "Axons", "Schwann cells", "Telodendria"],
     "A", "OSC", "easy",
     "Dendrites possess neurotransmitter receptors that collect chemical and sensory inputs, converting them into graded electrical potentials directed toward the cell body."),

    ("What is the single, long, cylindrical process that conducts nerve impulses AWAY from the cyton toward the synapse or effector organ?",
     ["Axon", "Dendrite", "Node of Ranvier", "Synaptic cleft"],
     "A", "OSC", "easy",
     "The axon conducts action potentials efferently away from the soma toward target terminal boutons across distances reaching up to 1 meter."),

    ("What is the function of the fatty myelin sheath covering the axons of many neurons in the central and peripheral nervous systems?",
     ["It acts as an electrical insulator that enables fast saltatory nerve impulse conduction from node to node",
      "It dissolves the axon into liquid water",
      "It absorbs oxygen from air to cool the brain",
      "It manufactures blood cells for the spinal cord"],
     "A", "OSC", "medium",
     "Myelin insulates the axon against ion leakage; action potentials jump rapidly between unmyelinated Nodes of Ranvier (saltatory conduction), accelerating transmission up to 120 m/s."),

    ("What are the regular gaps or periodic interruptions along the length of a myelinated nerve fiber called?",
     ["Nodes of Ranvier", "Synaptic knobs", "Nissl's bodies", "Dendritic spines"],
     "A", "OSC", "easy",
     "Nodes of Ranvier are periodic unmyelinated gaps where high densities of voltage-gated sodium channels regenerate action potentials during saltatory conduction."),

    ("What is a 'synapse' in the nervous system?",
     ["The microscopic junction or functional gap between the axon terminal of one neuron and the dendrite or soma of the next neuron",
      "The physical fusion of two bone joints",
      "The muscular valve between stomach and intestine",
      "The gap between two teeth"],
     "A", "OSC", "easy",
     "A synapse is a specialized intercellular junction where neurotransmitter chemicals diffuse across a microscopic synaptic cleft (~20 nm) to propagate signals to the postsynaptic cell."),

    ("How is a nerve impulse transmitted across a chemical synapse from the presynaptic knob to the postsynaptic dendrite?",
     ["Action potentials trigger the release of neurotransmitter molecules (such as acetylcholine) that diffuse across the synaptic cleft to bind specific postsynaptic receptors",
      "Electric spark jumps physically through open air like a lightning bolt",
      "The axon terminal physically bites into the dendrite",
      "Sound waves travel through the fluid"],
     "A", "OSC", "medium",
     "Depolarization opens voltage-gated calcium channels; calcium influx prompts synaptic vesicles to exocytose neurotransmitters into the cleft, generating an excitatory postsynaptic potential."),

    ("Which type of neuron carries sensory nerve impulses from peripheral sensory receptors (eyes, skin, ears) INWARD to the central nervous system (brain and spinal cord)?",
     ["Sensory neurons (afferent neurons)",
      "Motor neurons (efferent neurons)",
      "Association neurons (interneurons)",
      "Glial neurons"],
     "A", "OSC", "easy",
     "Sensory (afferent) neurons transmit incoming sensory information from peripheral receptors to the CNS for cognitive processing."),

    ("Which type of neuron carries regulatory motor impulses from the central nervous system OUTWARD to effector organs (muscles and glands)?",
     ["Motor neurons (efferent neurons)",
      "Sensory neurons",
      "Receptor neurons",
      "Afferent fibers"],
     "A", "OSC", "easy",
     "Motor (efferent) neurons conduct motor commands from the CNS to peripheral effectors (muscles, glands), triggering muscle contraction or glandular secretion."),

    # 11-20: Central Nervous System (Brain & Meninges)
    ("Which three protective connective tissue membranes (meninges) envelop the human brain and spinal cord, from outermost to innermost?",
     ["Dura mater, Arachnoid mater, and Pia mater",
      "Epidermis, Dermis, and Hypodermis",
      "Pleura, Pericardium, and Peritoneum",
      "Cartilage, Bone, and Marrow"],
     "A", "OSC", "medium",
     "The cranial meninges comprise the tough outer Dura mater, the web-like vascular Arachnoid mater, and the delicate, closely adhering inner Pia mater."),

    ("What is the function of the Cerebrospinal Fluid (CSF) circulating within the cerebral ventricles and subarachnoid space?",
     ["Acting as a hydraulic shock absorber, cushioning the brain from mechanical trauma and maintaining constant intracranial pressure",
      "Digesting food inside the skull",
      "Filtering urine from brain tissue",
      "Producing red blood cells for the eyes"],
     "A", "OSC", "easy",
     "CSF provides mechanical buoyancy, cushions the delicate brain tissue against cranial impacts, and circulates nutrients and neurochemical wastes."),

    ("Which is the largest and most prominent part of the human brain, accounting for approximately 80 to 85 percent of total brain mass?",
     ["Cerebrum (forebrain)", "Cerebellum", "Medulla oblongata", "Pons varolii"],
     "A", "OSC", "easy",
     "The cerebrum constitutes roughly 85% of total brain weight, governing consciousness, intelligence, memory, speech, sensory perception, and voluntary movement."),

    ("What deep longitudinal fissure divides the cerebrum into right and left cerebral hemispheres, and which thick tract of myelinated nerve fibers connects them?",
     ["Median longitudinal fissure; connected by the Corpus callosum",
      "Central sulcus; connected by the optic nerve",
      "Foramen magnum; connected by the spinal cord",
      "Sylvian fissure; connected by the thalamus"],
     "A", "OSC", "medium",
     "The longitudinal cerebral fissure divides the two hemispheres, which communicate and synchronize neural activity across a dense bridge of ~200 million axonal fibers called the corpus callosum."),

    ("What is the physiological function of the convoluted ridges (gyri) and shallow grooves (sulci) on the cerebral cortex surface?",
     ["They dramatically increase the surface area of the cerebral cortex, accommodating billions of additional neurons in the confined cranial cavity",
      "They allow rain water to drain away from the head",
      "They prevent the brain from overheating by creating air vents",
      "They help the skull bones slide past one another"],
     "A", "OSC", "medium",
     "Extensive cortical folding (gyrencephaly) triples the functional surface area of gray matter within the rigid confines of the human cranium."),

    ("Which part of the brain is the primary center for intelligence, conscious memory, reasoning, willpower, learning, and sensory perception?",
     ["Cerebrum (cerebral cortex)", "Medulla oblongata", "Spinal cord", "Cerebellum"],
     "A", "OSC", "easy",
     "Higher intellectual, linguistic, cognitive, and sensory-motor functions are orchestrated by specialized functional areas in the cerebral cortex."),

    ("Which part of the hindbrain, located beneath the occipital lobes of the cerebrum, coordinates voluntary muscle movements, maintaining posture, balance, and equilibrium?",
     ["Cerebellum", "Cerebrum", "Hypothalamus", "Medulla oblongata"],
     "A", "OSC", "easy",
     "The cerebellum fine-tunes motor precision, receives proprioceptive feedback from muscles and joints, and coordinates balance and fluid voluntary locomotion."),

    ("Why does acute alcohol intoxication cause a person to stagger, slur speech, and lose physical walking coordination?",
     ["Alcohol directly depresses cerebellar neural activity, impairing motor coordination and muscular equilibrium",
      "Alcohol breaks all the leg bones",
      "Alcohol paralyses the optic nerve completely",
      "Alcohol turns the inner ear fluid into ice"],
     "A", "OSC", "easy",
     "Ethanol selectively depresses GABAergic transmission in the cerebellum, sabotaging fine motor coordination and equilibrium, manifesting as cerebellar ataxia (staggering gait)."),

    ("Which critical part of the brain stem contains vital autonomic reflex centers controlling involuntary life-support functions like heartbeat, respiration, and blood pressure?",
     ["Medulla oblongata", "Cerebrum", "Cerebellum", "Corpus callosum"],
     "A", "OSC", "easy",
     "The medulla oblongata houses crucial autonomic centers regulating cardiac rhythm, vasoconstriction, respiratory rate, swallowing, sneezing, and vomiting."),

    ("Why is physical injury to the medulla oblongata or sudden severe compression of the brain stem almost instantaneously fatal?",
     ["It abruptly arrests autonomic cardiac pacing and respiratory center signaling, terminating heartbeat and breathing within seconds",
      "It causes all the teeth to fall out",
      "It shuts down vision permanently",
      "It turns blood into bone marrow"],
     "A", "OSC", "easy",
     "The medulla controls essential autonomous respiratory drive (dorsal/ventral respiratory groups) and cardiac acceleration/inhibition centers; damage halts vital vital functions."),

    # 21-30: Spinal Cord, ANS & Reflex Action
    ("What is the large opening in the base of the occipital skull bone through which the medulla oblongata exits to continue downward as the spinal cord?",
     ["Foramen magnum", "Optic foramen", "Mental foramen", "Pupillary aperture"],
     "A", "OSC", "easy",
     "The medulla oblongata merges into the spinal cord as it passes through the foramen magnum of the occipital bone into the vertebral neural canal."),

    ("How is gray matter and white matter distributed in a transverse cross-section of the human spinal cord compared to the cerebrum?",
     ["In the spinal cord, gray matter is internal (H-shaped) and white matter is external; in the cerebrum, gray matter is on the cortex outside and white matter is inside",
      "Both spinal cord and cerebrum have white matter only on the outside",
      "Both have gray matter only on the outside",
      "The spinal cord contains zero gray matter"],
     "A", "OSC", "medium",
     "The spinal cord has internal butterfly-shaped gray matter surrounded by ascending/descending myelinated tracts (white matter), reversing the arrangement seen in the cerebral hemispheres."),

    ("How many pairs of cranial nerves and spinal nerves constitute the human Peripheral Nervous System (PNS)?",
     ["12 pairs of cranial nerves and 31 pairs of spinal nerves",
      "10 pairs of cranial nerves and 20 pairs of spinal nerves",
      "31 pairs of cranial nerves and 12 pairs of spinal nerves",
      "24 pairs of cranial nerves and 62 pairs of spinal nerves"],
     "A", "OSC", "easy",
     "The human PNS comprises exactly 12 pairs of cranial nerves originating from the brain and 31 pairs of spinal nerves emerging segmentally from the spinal cord."),

    ("What are the two anatomically and functionally antagonistic divisions of the Autonomic Nervous System (ANS)?",
     ["Sympathetic nervous system and Parasympathetic nervous system",
      "Sensory nervous system and Motor nervous system",
      "Cerebral system and Cerebellar system",
      "Cranial system and Vertebral system"],
     "A", "OSC", "easy",
     "The ANS comprises the sympathetic ('fight or flight') and parasympathetic ('rest and digest') divisions, providing antagonistic neural control over visceral organs."),

    ("What physiological changes are triggered by the sympathetic nervous system during an acute emergency ('fight or flight' situation)?",
     ["Dilation of pupils, accelerated heart rate, dilation of bronchioles, elevation of blood pressure, and inhibition of digestive peristalsis",
      "Constriction of pupils, slowing of heartbeat, and stimulation of stomach digestion",
      "Inducing deep sleep and snoring",
      "Freezing of muscular joints"],
     "A", "OSC", "easy",
     "Sympathetic activation diverts blood to skeletal muscles, dilates airways, accelerates cardiac output, and suppresses digestive processes to prepare for emergency survival."),

    ("What physiological changes are triggered by the parasympathetic nervous system during calm, resting conditions ('rest and digest')?",
     ["Constriction of pupils, slowing of heart rate, constriction of bronchioles, and stimulation of digestive secretions and peristalsis",
      "Extreme adrenaline rush and high blood pressure",
      "Dilation of air passages and rapid pulse rate",
      "Complete cessation of urine formation"],
     "A", "OSC", "easy",
     "The parasympathetic division (via the vagus nerve) conserves energy, promotes digestion, slows heart rate, and maintains basal vegetative homeostasis."),

    ("What is a 'reflex action'?",
     ["A rapid, automatic, involuntary motor response to a sensory stimulus executed without conscious deliberation by the brain",
      "A planned voluntary decision to play football",
      "The slow logical solving of a mathematical equation",
      "The permanent storage of memories in the cerebrum"],
     "A", "OSC", "easy",
     "Reflexes are rapid, protective, involuntary behavioral loops coordinated primarily at the spinal level without waiting for conscious cortical processing."),

    ("What is the correct anatomical sequence of components in a standard spinal 'reflex arc'?",
     ["Receptor -> Sensory neuron -> Interneuron (spinal cord) -> Motor neuron -> Effector (muscle)",
      "Effector -> Motor neuron -> Brain -> Sensory neuron -> Receptor",
      "Brain -> Interneuron -> Receptor -> Muscle -> Skin",
      "Receptor -> Motor neuron -> Spinal cord -> Sensory neuron -> Effector"],
     "A", "OSC", "easy",
     "A reflex arc begins at a sensory receptor, transmits via an afferent neuron to spinal cord interneurons, and returns via an efferent motor neuron to trigger muscle contraction."),

    ("Why does a person involuntarily pull their hand away from a boiling hot stove before they even feel the conscious sensation of pain?",
     ["The protective reflex arc is processed and executed locally in the spinal cord, while pain signals take longer to ascend to the conscious cerebral cortex",
      "The hand has a tiny brain inside the fingers",
      "The stove pushes the hand away with heat magnetism",
      "Pain nerves travel faster than motor nerves"],
     "A", "OSC", "medium",
     "The spinal reflex arc executes withdrawal within ~20 milliseconds, safeguarding tissue from severe burns before ascending sensory tracts reach the somatosensory cortex for conscious pain awareness."),

    ("Assertion (A): Damage to the spinal cord below the neck can cause paralysis of the legs (paraplegia) while the head and arms function normally.\nReason (R): Ascending and descending nerve fiber tracts carrying sensory and motor signals between the brain and lower limbs are severed at the thoracic/lumbar injury level.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     "Transection of the spinal cord interrupts descending corticospinal motor tracts and ascending spinothalamic sensory tracts, isolating body segments below the lesion from cerebral control."),

    ("What is the 'all-or-none law' governing the firing of a neuronal action potential?",
     ["If an electrical stimulus reaches or exceeds the threshold level (-55 mV), an action potential of maximum, constant amplitude is generated; sub-threshold stimuli produce zero action potential",
      "All neurons in the brain fire at the exact same second",
      "A neuron either fires all its neurotransmitters or none at all",
      "Only one neuron can fire in a person's lifetime"],
     "A", "OSC", "medium",
     "Action potentials are digital binary signals: once threshold depolarization is reached, the regenerative positive-feedback opening of voltage-gated Na+ channels creates an impulse of uniform height regardless of stimulus excess."),

    ("Which part of the diencephalon acts as the executive sensory relay station, routing all incoming sensory impulses (except smell) to specific sensory areas of the cerebral cortex?",
     ["Thalamus", "Hypothalamus", "Medulla oblongata", "Cerebellum"],
     "A", "OSC", "easy",
     "The thalamus functions as the gateway to the cerebral cortex: visual, auditory, gustatory, and somatosensory tracts synapse in thalamic nuclei before being directed to specialized cortical lobes."),

    ("What is the primary function of the pons varolii located superior to the medulla oblongata?",
     ["Bridging communication between the cerebrum, cerebellum, and spinal cord, and regulating respiratory rhythm via pneumotaxic centers",
      "Filtering blood like a kidney",
      "Manufacturing red blood cells",
      "Controlling body balance in walking"],
     "A", "OSC", "medium",
     "The pons contains transverse fiber tracts connecting the two cerebellar hemispheres and houses the pneumotaxic center that limits inspiration to set breathing rhythm."),

    ("What enzyme present in the synaptic cleft rapidly hydrolyzes released acetylcholine, preventing continuous, uncontrolled muscle spasms?",
     ["Acetylcholinesterase", "Amylase", "Pepsin", "Lipase"],
     "A", "OSC", "easy",
     "Acetylcholinesterase breaks down acetylcholine into acetate and choline within milliseconds, terminating the postsynaptic signal and allowing the muscle membrane to repolarize."),

    ("What progressive autoimmune neurological disease is caused by immune destruction of the myelin sheath around axons in the Central Nervous System?",
     ["Multiple Sclerosis (MS)", "Parkinson's disease", "Alzheimer's disease", "Diabetes mellitus"],
     "A", "OSC", "medium",
     "In multiple sclerosis, autoreactive T-cells attack oligodendrocytes and myelin in the brain and spinal cord, forming sclerotic plaques that disrupt saltatory nerve conduction."),

    ("At which anatomical level of the lumbar spine is a diagnostic lumbar puncture (spinal tap) performed to sample CSF safely?",
     ["Between vertebrae L3 and L4 (or L4-L5), below the termination of the solid spinal cord",
      "Directly into the cervical neck vertebrae C1-C2",
      "Through the frontal skull bone",
      "Between thoracic vertebrae T1-T2"],
     "A", "OSC", "hard",
     "The adult spinal cord ends at L1-L2 (conus medullaris); inserting a needle into the subarachnoid space at L3-L4 accesses the cauda equina safely without puncturing the spinal cord."),

    ("Match the cerebral lobe to its primary cortical function: Occipital lobe -> ________; Temporal lobe -> ________.",
     ["Vision; Hearing and memory", "Taste; Muscular balance", "Smell; Temperature control", "Heartbeat; Breathing"],
     "A", "OSC", "easy",
     "The primary visual cortex is located in the posterior occipital lobe, while auditory perception and memory processing are seated in the temporal lobes."),

    ("Which neuroglial cells function as resident phagocytic immune macrophages, engulfing cellular debris and pathogens in the Central Nervous System?",
     ["Microglia", "Astrocytes", "Schwann cells", "Ependymal cells"],
     "A", "OSC", "medium",
     "Microglia are bone-marrow derived phagocytes in the CNS that activate and scavenge damaged neurons, plaques, and infectious agents during injury or disease."),

    ("What symptom is observed if a surgical cut cleanly transects the VENTRAL root of a lumbar spinal nerve while leaving the DORSAL root intact?",
     ["Complete motor paralysis of the innervated leg muscles with normal intact sensory sensation",
      "Loss of all sensation with normal muscle movement",
      "Complete loss of both sensation and movement",
      "Instant death"],
     "A", "OSC", "hard",
     "The Bell-Magendie law dictates functional root separation: dorsal roots carry only sensory afferents (retaining sensation), while ventral roots carry only motor efferents (causing motor paralysis if cut)."),

    ("Assertion (A): Conduction of a nerve impulse along a myelinated nerve axon is described as 'saltatory'.\nReason (R): The electrical impulse leaps or jumps from one Node of Ranvier to the next across insulating myelin segments.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "easy",
     "From the Latin *saltare* (to leap), saltatory conduction describes how action potentials jump from node to node, increasing transmission speed while conserving metabolic energy.")
]

practice_data = [
    # 31-40: Fill in blanks, Numerical, Multi-choice
    ("The central canal of the spinal cord and ventricles of the brain are filled with ________ fluid.",
     ["cerebrospinal (CSF)", "amniotic", "synovial", "peritoneal"],
     "A", "OFB", "easy",
     "Cerebrospinal fluid fills the brain ventricles, central canal of the spinal cord, and the subarachnoid space."),

    ("In a neuron, protein synthesis occurs in specialized ribonucleoprotein granules called ________ granules.",
     ["Nissl's", "zymogen", "glycogen", "calcium"],
     "A", "OFB", "easy",
     "Nissl's granules are dense aggregations of rough endoplasmic reticulum and ribosomes found in the cyton and proximal dendrites."),

    ("The junction across which a motor neuron stimulates a skeletal muscle fiber is called the ________ junction.",
     ["neuromuscular (motor end plate)", "synapse", "intervertebral", "cartilaginous"],
     "A", "OFB", "easy",
     "The neuromuscular junction is the chemical synapse between a somatic motor neuron terminal and a skeletal muscle fiber sarcolemma."),

    ("A nerve impulse travels along a myelinated axon at a speed of 100 meters per second. How long (in milliseconds) does it take to travel 1.5 meters from the spinal cord to the foot?",
     ["15 milliseconds", "1.5 milliseconds", "150 milliseconds", "0.15 milliseconds"],
     "A", "ONE", "easy",
     "Time = Distance / Speed = 1.5 m / 100 m/s = 0.015 seconds = 15 milliseconds."),

    ("How many total spinal nerves emerge from both sides of the human spinal cord combined?",
     ["62 nerves (31 pairs)", "31 nerves", "24 nerves", "12 nerves"],
     "A", "ONE", "easy",
     "There are 31 pairs of spinal nerves, totaling 62 individual spinal nerves emerging from the vertebral column."),

    ("Which of the following actions are regulated as involuntary autonomic reflexes by the brainstem or spinal cord?",
     ["Peristalsis in the intestine, constriction of pupils in bright light, and coughing/sneezing",
      "Writing a handwritten essay and reading a book",
      "Kicking a football into a goal post",
      "Singing a song at a concert"],
     "A", "OMC", "easy",
     "Pupillary reflexes, visceral gastrointestinal motility, and airway clearance reflexes are automatic involuntary reflexes mediated by autonomic pathways."),

    ("Which of the following cranial nerves are sensory nerves that carry sensory inputs to the brain?",
     ["Olfactory nerve (smell), Optic nerve (vision), and Vestibulocochlear nerve (hearing/balance)",
      "Vagus nerve and Hypoglossal nerve",
      "Sciatic nerve and Femoral nerve",
      "Spinal accessory nerve"],
     "A", "OMC", "medium",
     "Cranial nerves I (Olfactory), II (Optic), and VIII (Vestibulocochlear) are purely sensory cranial nerves dedicated to special senses."),

    ("Which neuroglial cells are responsible for producing the insulating myelin sheath around axons in the Peripheral Nervous System?",
     ["Schwann cells", "Oligodendrocytes", "Astrocytes", "Microglia"],
     "A", "OSC", "medium",
     "Schwann cells wrap around peripheral axons to synthesize myelin in the PNS, whereas oligodendrocytes myelinate axons in the CNS."),

    ("What is the physiological role of the hypothalamus located at the base of the diencephalon?",
     ["Regulating body temperature (thermostat), hunger, thirst, sleep-wake cycles, and controlling pituitary hormone secretions",
      "Pumping blood into the aorta",
      "Filtering urea from blood",
      "Holding the teeth in position"],
     "A", "OSC", "easy",
     "The hypothalamus is the master neuroendocrine integrator, regulating body temperature, circadian rhythms, emotional drives, and the autonomic nervous system."),

    ("Why is saltatory conduction in myelinated axons significantly more energy efficient than continuous conduction in unmyelinated axons?",
     ["Depolarization and ion exchange occur exclusively at the Nodes of Ranvier, requiring far less ATP expenditure by Na+/K+ pumps to restore resting potentials",
      "Myelinated axons burn sugar directly into electricity",
      "Myelinated axons generate cold light",
      "Unmyelinated axons have no sodium channels"],
     "A", "OSC", "hard",
     "Because ion flux is confined to nodal membranes (~0.1% of membrane area), far fewer ions cross, drastically reducing the metabolic ATP required by sodium-potassium pumps to recharge the neuron.")
]

# Add remaining 10 practice questions to make exactly 30 (41-50)
practice_data.extend([
    ("What is the resting membrane potential of a typical mammalian neuron?",
     ["Approximately -70 millivolts (inside negative relative to outside)",
      "+70 millivolts",
      "Zero millivolts",
      "-120 volts"],
     "A", "OSC", "medium",
     "In an unstimulated resting state, high intracellular K+ and permeable leak channels establish a resting potential of roughly -70 mV across the plasma membrane."),

    ("What rapid cellular ion flux produces the explosive depolarization phase of a neuronal action potential?",
     ["Rapid influx of sodium ions (Na+) through opened voltage-gated sodium channels into the cell",
      "Efflux of potassium ions out of the cell",
      "Pumping of water into the nucleus",
      "Inflow of chloride ions"],
     "A", "OSC", "medium",
     "Reaching threshold potential triggers voltage-gated Na+ channels to snap open; massive sodium influx depolarizes the membrane potential up to +30 mV."),

    ("What is the 'knee-jerk reflex' commonly tested by physicians using a rubber percussion hammer?",
     ["A monosynaptic stretch reflex of the patellar tendon that causes involuntary contraction of the quadriceps muscle to extend the knee",
      "A voluntary kick initiated by the cerebrum",
      "A symptom of complete knee joint failure",
      "An electric shock generated by bone marrow"],
     "A", "OSC", "easy",
     "Tapping the patellar tendon stretches muscle spindles, firing a sensory afferent that synapses directly on a motor neuron in the lumbar spinal cord to twitch the quadriceps."),

    ("What is the main excitatory neurotransmitter in the human central nervous system and neuromuscular junctions?",
     ["Acetylcholine (at neuromuscular junctions) and Glutamate (in CNS)",
      "Hemoglobin",
      "Insulin",
      "Glycogen"],
     "A", "OSC", "medium",
     "Acetylcholine mediates somatic motor transmission, while glutamate is the principal fast excitatory neurotransmitter in the brain cortex."),

    ("Which major cranial nerve (Cranial Nerve X) provides the extensive parasympathetic innervation to the heart, lungs, and gastrointestinal organs?",
     ["Vagus nerve", "Trigeminal nerve", "Facial nerve", "Optic nerve"],
     "A", "OSC", "medium",
     "The vagus nerve ('wandering nerve') carries over 75% of all parasympathetic outflow, slowing heart rate and stimulating visceral digestive organs."),

    ("What is the protective role of the 'blood-brain barrier' (BBB) formed by capillary endothelial tight junctions and astrocyte end-feet?",
     ["Strictly shielding brain neural tissue from circulating systemic toxins, pathogens, and sudden fluctuations in blood chemistry",
      "Preventing blood from entering the skull",
      "Stopping thoughts from leaving the head",
      "Preventing oxygen from entering the brain"],
     "A", "OSC", "medium",
     "Endothelial tight junctions and astrocytic podocytes create a selective physiological barrier, allowing vital glucose and oxygen through while blocking hydrophilic toxins and microbes."),

    ("State whether True or False: Damage to Broca's area in the left frontal lobe of the cerebral cortex impairs motor speech production (motor aphasia).",
     ["True", "False"],
     "A", "OTF", "easy",
     "Broca's area coordinates the motor vocalization muscles; lesions result in expressive aphasia, where patients understand language but cannot fluently articulate words."),

    ("Which structure in the temporal lobe of the cerebrum is critical for converting short-term memories into consolidated long-term memories?",
     ["Hippocampus", "Cerebellum", "Medulla", "Corpus callosum"],
     "A", "OSC", "medium",
     "The hippocampus plays an indispensable role in memory consolidation; bilateral hippocampal damage leaves patients unable to form new declarative memories (anterograde amnesia)."),

    ("How do pain-relieving local anesthetics (like lidocaine or novocaine) completely numb pain sensation during dental surgery?",
     ["They reversibly block voltage-gated sodium channels in sensory nerve fibers, preventing action potential generation and pain signal transmission",
      "They freeze the tooth into solid ice",
      "They destroy the brain's memory of teeth",
      "They convert pain into pleasant sweet taste"],
     "A", "OSC", "hard",
     "Local anesthetics physically occlude the inner pore of voltage-gated Na+ channels, arresting depolarizing influx and silencing pain action potentials from the surgical site."),

    ("What involuntary reflex causes the pupil of the eye to constrict rapidly in bright sunlight and dilate in dim light?",
     ["Pupillary light reflex (controlled by cranial nerves II and III and midbrain nuclei)",
      "Voluntary eye squinting",
      "Bleaching of cornea by ultraviolet light",
      "Melting of the lens"],
     "A", "OSC", "easy",
     "The pretectal midbrain nuclei process afferent optic signals, firing oculomotor parasympathetic fibers to contract iris sphincter muscles and protect retinal photoreceptors."),

    ("Which ion pump maintains the resting membrane potential of a neuron by actively expelling 3 Na+ ions out of the cell for every 2 K+ ions pumped in?",
     ["Sodium-potassium ATPase pump (Na+/K+ pump)", "Calcium uniporter", "Proton-ATP synthase", "Glucose transporter (GLUT)"],
     "A", "OSC", "medium",
     "The electrogenic Na+/K+ ATPase pump consumes ATP to transport 3 Na+ ions outward and 2 K+ ions inward, maintaining the resting potential at approximately -70 mV."),

    ("What event directly triggers the rapid depolarization phase of an axonal action potential once the threshold potential is reached?",
     ["Opening of voltage-gated sodium (Na+) channels leading to massive inward Na+ influx", "Efflux of chloride ions", "Closure of all potassium channels", "Pumping of glycogen into the axon"],
     "A", "OSC", "medium",
     "Depolarization to threshold opens voltage-gated Na+ channels; rapid influx of positive sodium ions drives the membrane potential from -70 mV up to +30 mV."),

    ("During the repolarization phase of an action potential, which channel opening restores the negative resting membrane potential inside the neuron?",
     ["Voltage-gated potassium (K+) channels opening to allow K+ efflux", "Sodium channel opening", "Calcium pumps reversing", "Chloride inflow stopped"],
     "A", "OSC", "medium",
     "Repolarization occurs when voltage-gated Na+ channels inactivate and slower voltage-gated K+ channels open, allowing K+ to exit the cell down its electrochemical gradient."),

    ("What is the correct sequence of the three protective cranial meninges covering the human brain from outermost to innermost?",
     ["Dura mater -> Arachnoid mater -> Pia mater", "Pia mater -> Dura mater -> Arachnoid mater", "Arachnoid mater -> Pia mater -> Dura mater", "Dura mater -> Pia mater -> Arachnoid mater"],
     "A", "OSC", "easy",
     "The cranial meninges consist of the tough outer Dura mater, the middle web-like Arachnoid mater, and the delicate vascular inner Pia mater adhering directly to brain tissue."),

    ("Which sequence correctly represents the complete anatomical path of a somatic spinal reflex arc?",
     ["Receptor -> Sensory neuron -> Interneuron in spinal cord -> Motor neuron -> Effector muscle", "Effector -> Motor neuron -> Spinal cord -> Sensory neuron -> Receptor", "Receptor -> Motor neuron -> Interneuron -> Sensory neuron -> Effector", "Brain cortex -> Sensory neuron -> Spinal cord -> Effector"],
     "A", "OSC", "easy",
     "A reflex arc starts with a sensory receptor detecting stimulus, transmitting impulses through afferent sensory neurons to the spinal cord gray matter, synapsing via interneurons to efferent motor neurons that trigger effector contraction."),

    ("Which division of the peripheral nervous system directly controls voluntary skeletal muscle contractions, such as walking or writing?",
     ["Somatic nervous system", "Sympathetic autonomic division", "Parasympathetic division", "Enteric nervous system"],
     "A", "OSC", "easy",
     "The somatic nervous system innervates striated skeletal muscles under conscious voluntary control, whereas the autonomic nervous system regulates involuntary cardiac and smooth muscles."),

    ("What is the primary function of the corpus callosum, the large C-shaped tract of white matter connecting the two cerebral hemispheres?",
     ["Facilitating interhemispheric communication and signal transfer between the left and right cerebral hemispheres", "Filtering blood into cerebrospinal fluid", "Directly controlling breathing rhythm", "Regulating body temperature"],
     "A", "OSC", "medium",
     "The corpus callosum contains over 200 million myelinated axonal fibers that bridge homologous cortical areas between the left and right cerebral hemispheres for unified cognitive processing."),

    ("Why can a severe blow or traumatic injury to the medulla oblongata at the base of the skull cause instantaneous death?",
     ["The medulla contains vital involuntary reflex centres controlling heartbeat, vasomotor tone, and respiration", "The medulla is the only bone in the skull", "The medulla produces all red blood cells in the body", "The medulla controls conscious thoughts and speech"],
     "A", "OSC", "medium",
     "The medulla oblongata houses vital autonomic centers for cardiac pace regulation, vasomotor blood pressure control, and respiratory rhythm generation; damage disrupts essential cardiac and ventilatory function."),

    ("Salivation upon placing food directly into the mouth is an unconditioned reflex, whereas salivating simply upon hearing a dinner bell is an example of a ________ reflex.",
     ["conditioned (acquired)", "voluntary somatic", "primitive spinal", "monosynaptic tendon"],
     "A", "OFB", "easy",
     "Conditioned (acquired) reflexes are learned responses developed through association and experience, famously demonstrated by Ivan Pavlov's classical conditioning experiments with dogs."),

    ("State whether True or False: According to the 'All-or-None' law of nerve conduction, if a stimulus reaches or exceeds the threshold potential, the neuron fires an action potential of constant full magnitude regardless of further increases in stimulus intensity.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The all-or-none principle states that an excitable neuron membrane either fires a complete action potential of full amplitude or none at all; stimulus strength is encoded by firing frequency, not action potential height.")
])

# 12 Mock/Foundation Questions with Vector SVGs (71-82)
mock_data = [
    # 71: Motor Neuron Anatomy
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#0f172a"/>
  <circle cx="80" cy="100" r="26" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="80" cy="100" r="10" fill="#0284c7"/>
  <text x="80" y="104" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">Nucleus</text>
  <line x1="45" y1="75" x2="60" y2="90" stroke="#38bdf8" stroke-width="3"/>
  <line x1="40" y1="100" x2="54" y2="100" stroke="#38bdf8" stroke-width="3"/>
  <line x1="45" y1="125" x2="60" y2="110" stroke="#38bdf8" stroke-width="3"/>
  <text x="45" y="60" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">Dendrites (Inputs)</text>
  <line x1="106" y1="100" x2="350" y2="100" stroke="#facc15" stroke-width="4"/>
  <rect x="130" y="90" width="30" height="20" rx="4" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <rect x="180" y="90" width="30" height="20" rx="4" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <rect x="230" y="90" width="30" height="20" rx="4" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <rect x="280" y="90" width="30" height="20" rx="4" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <text x="210" y="80" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Myelin Sheath (Schwann Cells)</text>
  <text x="170" y="130" fill="#facc15" font-size="9" font-family="sans-serif">Node of Ranvier</text>
  <text x="350" y="130" fill="#f87171" font-size="10" font-family="sans-serif" font-weight="bold">Axon Terminals</text>
</svg>
</div>
In the labeled multipolar neuron diagram above, what physiological advantage is conferred by the discontinuous myelin sheath segments?""",
     ["Action potentials jump rapidly between the exposed Nodes of Ranvier (saltatory conduction), increasing conduction velocity over tenfold",
      "Myelin cools the axon down so it does not melt",
      "Myelin absorbs red blood cells to nourish the axon",
      "Myelin prevents thoughts from escaping through the skull"],
     "A", "OSC", "hard",
     "Myelin eliminates capacitance and transverse current leakage; action potentials regenerate exclusively at high-conductance Nodes of Ranvier, propelling impulses at speeds exceeding 100 m/s."),

    # 72: Synapse chemical transmission
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <path d="M 50 40 L 160 40 Q 200 60 200 100 Q 200 140 160 160 L 50 160 Z" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="70" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">Axon Knob</text>
  <circle cx="150" cy="80" r="5" fill="#facc15"/>
  <circle cx="170" cy="100" r="5" fill="#facc15"/>
  <circle cx="150" cy="120" r="5" fill="#facc15"/>
  <text x="150" y="65" fill="#facc15" font-size="9" font-family="sans-serif">Vesicles (ACh)</text>
  <rect x="230" y="40" width="130" height="120" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="295" y="70" fill="#4ade80" font-size="10" font-family="sans-serif" font-weight="bold">Postsynaptic Dendrite</text>
  <line x1="230" y1="80" x2="238" y2="80" stroke="#f87171" stroke-width="3"/>
  <line x1="230" y1="100" x2="238" y2="100" stroke="#f87171" stroke-width="3"/>
  <line x1="230" y1="120" x2="238" y2="120" stroke="#f87171" stroke-width="3"/>
  <text x="295" y="105" fill="#f87171" font-size="9" font-family="sans-serif">Receptors</text>
  <text x="200" y="180" fill="#cbd5e1" font-size="10" font-family="sans-serif" text-anchor="middle">Synaptic Cleft (~20 nm gap)</text>
</svg>
</div>
Why can nerve transmission across a chemical synapse occur in ONE DIRECTION ONLY (unidirectional flow from axon terminal to dendrite)?""""",
     ["Synaptic vesicles containing neurotransmitters are located solely in presynaptic axon knobs, while specific receptor proteins exist only on the postsynaptic membrane",
      "Electric current cannot flow backwards in organic tissue",
      "The dendrite has muscular valves that physically slam shut",
      "The synaptic cleft is filled with solid rubber"],
     "A", "OSC", "medium",
     "Structural polarity dictates functional unidirectionality: neurotransmitter vesicles are confined strictly to presynaptic terminals, and receptor ion channels are localized exclusively on postsynaptic membranes."),

    # 73: Human Brain Major Functional Regions
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#0f172a"/>
  <ellipse cx="180" cy="80" rx="110" ry="55" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
  <text x="180" y="75" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Cerebrum</text>
  <text x="180" y="92" fill="#93c5fd" font-size="9" font-family="sans-serif" text-anchor="middle">(Intelligence, memory, voluntary thought)</text>
  <ellipse cx="270" cy="135" rx="40" ry="24" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <text x="270" y="138" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Cerebellum</text>
  <text x="270" y="150" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">(Balance & coordination)</text>
  <rect x="175" y="130" width="30" height="50" rx="4" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
  <text x="190" y="155" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Medulla</text>
  <text x="190" y="170" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">(Vital centers)</text>
  <line x1="190" y1="180" x2="190" y2="195" stroke="#ef4444" stroke-width="6"/>
  <text x="225" y="195" fill="#ef4444" font-size="9" font-family="sans-serif">-> Spinal cord</text>
</svg>
</div>
A gymnast performs a complex balance routine on a narrow 10 cm balance beam. Which region of the brain shown above is actively integrating sensory feedback from inner ear vestibular canals to keep her upright?""""",
     ["Cerebellum", "Cerebrum", "Medulla oblongata", "Spinal cord"],
     "A", "OSC", "easy",
     "The cerebellum coordinates motor firing patterns, compares intended movements with sensory feedback from vestibular organs, and continuously corrects posture to maintain physical balance."),

    # 74: Spinal Reflex Arc
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <ellipse cx="60" cy="100" r="18" fill="#ef4444"/>
  <text x="60" y="96" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Skin</text>
  <text x="60" y="108" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Receptor</text>
  <path d="M 78 100 Q 150 40 230 65" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <text x="150" y="45" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">Sensory (Afferent) Neuron</text>
  <rect x="230" y="50" width="130" height="100" rx="8" fill="#27272a" stroke="#facc15" stroke-width="2"/>
  <text x="295" y="70" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Spinal Cord (Gray matter)</text>
  <circle cx="280" cy="100" r="10" fill="#facc15"/>
  <text x="280" y="104" fill="#09090b" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Inter</text>
  <path d="M 270 110 Q 180 160 80 145" stroke="#4ade80" stroke-width="3" fill="none"/>
  <text x="180" y="165" fill="#4ade80" font-size="10" font-family="sans-serif" font-weight="bold">Motor (Efferent) Neuron</text>
  <rect x="40" y="135" width="40" height="25" rx="3" fill="#15803d"/>
  <text x="60" y="151" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Muscle</text>
</svg>
</div>
In the standard spinal reflex arc illustrated above, what critical role is performed by the interneuron (association neuron) inside the spinal gray matter?""""",
     ["It acts as an integrative relay bridge connecting the incoming sensory neuron to the outgoing motor neuron",
      "It transfers thoughts directly into the stomach",
      "It manufactures blood cells for the spinal canal",
      "It acts as a bone joint inside the vertebra"],
     "A", "OSC", "medium",
     "The spinal interneuron synapses with the dorsal root sensory axon and ventral horn motor dendrite, completing the local reflex circuit and simultaneously relaying collateral signals up to the brain."),

    # 75: Sympathetic vs Parasympathetic autonomic antagonism
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="40" y="45" width="140" height="100" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
  <text x="110" y="70" fill="#f87171" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Sympathetic (Emergency)</text>
  <text x="110" y="90" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Dilates pupils</text>
  <text x="110" y="108" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Accelerates heart rate</text>
  <text x="110" y="125" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">Inhibits digestion</text>
  <rect x="220" y="45" width="140" height="100" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="290" y="70" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Parasympathetic (Rest)</text>
  <text x="290" y="90" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Constricts pupils</text>
  <text x="290" y="108" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Slows heart rate</text>
  <text x="290" y="125" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">Stimulates digestion</text>
</svg>
</div>
A hiker suddenly encounters a charging wild bear in a forest. Which autonomic division immediately takes dominance, and what vital cardiovascular response does it execute?""""",
     ["Sympathetic system dominates: accelerates heart rate and dilates muscle vasculature to prepare for fight or flight",
      "Parasympathetic system dominates: induces deep sleep",
      "Both systems shut down completely",
      "The digestive system starts digesting food faster"],
     "A", "OSC", "easy",
     "Acute threats activate sympathetic thoracolumbar outflow, releasing noradrenaline to boost cardiac inotropy/chronotropy and divert blood flow to skeletal muscles for survival."),

    # 76: Action Potential Waveform
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <line x1="50" y1="150" x2="360" y2="150" stroke="#64748b" stroke-width="2"/>
  <line x1="50" y1="150" x2="50" y2="20" stroke="#64748b" stroke-width="2"/>
  <text x="360" y="170" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">Time (ms)</text>
  <text x="40" y="25" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">Voltage (mV)</text>
  <line x1="50" y1="130" x2="360" y2="130" stroke="#64748b" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="45" y="134" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="end">-70 mV (Rest)</text>
  <line x1="50" y1="110" x2="360" y2="110" stroke="#facc15" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="45" y="114" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="end">-55 mV (Threshold)</text>
  <path d="M 60 130 L 100 130 L 120 110 L 150 40 L 190 145 L 230 130 L 320 130" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <text x="145" y="30" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">+30 mV (Na+ influx)</text>
  <text x="210" y="165" fill="#f87171" font-size="9" font-family="sans-serif">Repolarization (K+ efflux)</text>
</svg>
</div>
What rapid molecular event is responsible for the steep upward spike (depolarization from -55 mV to +30 mV) in the action potential tracing above?""""",
     ["Rapid opening of voltage-gated sodium (Na+) channels, permitting massive sodium influx into the axon",
      "Efflux of potassium out of the cell",
      "Pumping of water into the nucleus",
      "Closing of all cell channels"],
     "A", "OSC", "hard",
     "Reaching the -55 mV threshold triggers the rapid opening of activation gates in voltage-gated Na+ channels; sodium rushes down its electrochemical gradient, flipping membrane polarity to +30 mV."),

    # 77: Cranial Meninges and CSF cross section
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="40" y="30" width="320" height="20" fill="#e2e8f0"/>
  <text x="200" y="44" fill="#0f172a" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Cranial Bone (Skull)</text>
  <rect x="40" y="55" width="320" height="12" fill="#475569"/>
  <text x="200" y="65" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">Dura Mater (Tough outer layer)</text>
  <rect x="40" y="72" width="320" height="18" fill="#0284c7" opacity="0.7"/>
  <text x="200" y="85" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Subarachnoid Space (Filled with CSF)</text>
  <rect x="40" y="95" width="320" height="8" fill="#dc2626"/>
  <text x="200" y="102" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Pia Mater (Inner vascular)</text>
  <rect x="40" y="108" width="320" height="50" rx="4" fill="#334155"/>
  <text x="200" y="135" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Cerebral Cortex (Brain Tissue)</text>
</svg>
</div>
What severe medical disease results from microbial bacterial or viral infection and inflammation of the protective meninges shown above?""""",
     ["Meningitis", "Gastritis", "Bronchitis", "Hepatitis"],
     "A", "OSC", "easy",
     "Meningitis is acute inflammation of the protective meningeal membranes surrounding the brain and spinal cord, presenting with fever, severe headache, and neck stiffness."),

    # 78: Spinal Cord Internal Cross Section
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <ellipse cx="200" cy="95" rx="140" ry="70" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/>
  <text x="200" y="45" fill="#09090b" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Outer White Matter (Myelinated tracts)</text>
  <path d="M 150 75 Q 170 95 150 115 Q 185 100 200 100 Q 215 100 250 115 Q 230 95 250 75 Q 215 90 200 90 Q 185 90 150 75 Z" fill="#64748b" stroke="#334155" stroke-width="2"/>
  <circle cx="200" cy="95" r="4" fill="#38bdf8"/>
  <text x="200" y="135" fill="#334155" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Inner Gray Matter ('H' butterfly shape)</text>
  <text x="200" y="178" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle">Central canal contains circulating CSF</text>
</svg>
</div>
Why does the inner core of the spinal cord appear gray ('gray matter') while the outer perimeter appears white ('white matter')?""""",
     ["Gray matter consists of unmyelinated cell bodies, dendrites, and synapses, while white matter consists of bundles of lipid-rich myelinated axonal tracts",
      "Gray matter is painted with melanin pigment",
      "White matter contains chalk deposits",
      "Gray matter is dead tissue"],
     "A", "OSC", "medium",
     "Lipid-rich myelin sheaths confer a glistening white appearance to longitudinal conduction tracts in the periphery; unmyelinated neuronal somata and neuropil form the central gray butterfly."),

    # 79: Hypothalamus Neuroendocrine Axis
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="130" y="30" width="140" height="50" rx="6" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="200" y="52" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Hypothalamus</text>
  <text x="200" y="68" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">(Body thermostat, hunger, thirst)</text>
  <line x1="200" y1="80" x2="200" y2="115" stroke="#f87171" stroke-width="4"/>
  <circle cx="200" cy="135" r="20" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
  <text x="200" y="139" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pituitary</text>
  <text x="200" y="175" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Master endocrine interface between brain and body hormones</text>
</svg>
</div>
How does the hypothalamus function as the supreme master coordinator linking the nervous system to the endocrine system?""""",
     ["It integrates brain neural inputs and synthesizes releasing and inhibiting neurohormones that directly control pituitary gland secretions",
      "It filters blood like the kidney",
      "It pumps blood like the heart",
      "It dissolves food like the stomach"],
     "A", "OSC", "medium",
     "The hypothalamus translates neural signals into hormonal commands: hypophyseal portal vessels carry hypothalamic releasing factors to regulate anterior pituitary endocrine output."),

    # 80: Corpus Callosum Interhemispheric Bridge
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <ellipse cx="120" cy="95" rx="60" ry="45" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
  <text x="120" y="95" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Left Hemisphere</text>
  <text x="120" y="112" fill="#93c5fd" font-size="9" font-family="sans-serif">(Logic & language)</text>
  <path d="M 170 95 L 230 95" stroke="#facc15" stroke-width="8"/>
  <text x="200" y="80" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Corpus Callosum</text>
  <ellipse cx="280" cy="95" rx="60" ry="45" fill="#334155" stroke="#4ade80" stroke-width="2"/>
  <text x="280" y="95" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Right Hemisphere</text>
  <text x="280" y="112" fill="#86efac" font-size="9" font-family="sans-serif">(Creativity & spatial)</text>
  <text x="200" y="170" fill="#cbd5e1" font-size="10" font-family="sans-serif" text-anchor="middle">Dense commissural tract of ~200 million myelinated axonal fibers</text>
</svg>
</div>
What cognitive deficit occurs in 'split-brain' patients whose corpus callosum has been surgically transected to treat severe epilepsy?""""",
     ["The two cerebral hemispheres cannot communicate directly, so sensory inputs perceived solely by one hemisphere cannot be verbally described by the left hemisphere",
      "The patient loses all memory permanently",
      "The patient can no longer walk or breathe",
      "The eyes stop moving completely"],
     "A", "OSC", "hard",
     "Sperry's Nobel prize-winning split-brain studies demonstrated that cutting the corpus callosum isolates the speech-dominant left hemisphere from visual/tactile information received exclusively by the right hemisphere."),

    # 81: Broca's Area vs Wernicke's Area
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <ellipse cx="200" cy="95" rx="130" ry="65" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="140" cy="95" r="16" fill="#ef4444"/>
  <text x="140" y="99" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Broca</text>
  <text x="140" y="125" fill="#f87171" font-size="9" font-family="sans-serif" text-anchor="middle">Motor speech</text>
  <circle cx="250" cy="115" r="16" fill="#3b82f6"/>
  <text x="250" y="119" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Wernicke</text>
  <text x="250" y="145" fill="#60a5fa" font-size="9" font-family="sans-serif" text-anchor="middle">Comprehension</text>
  <text x="200" y="175" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">Cortical speech centers in dominant left hemisphere</text>
</svg>
</div>
A stroke patient can fully understand spoken language and follow complex commands, but struggles immensely to physically articulate words. Which cortical area was damaged by the stroke?""""",
     ["Broca's area in the left frontal lobe",
      "Wernicke's area in the temporal lobe",
      "The cerebellum",
      "The visual cortex in the occipital lobe"],
     "A", "OSC", "medium",
     "Broca's expressive aphasia leaves linguistic comprehension intact while destroying the motor programming required for smooth articulation of speech."),

    # 82: Knee-Jerk Monosynaptic Reflex
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <rect x="50" y="80" width="30" height="30" rx="4" fill="#ef4444"/>
  <text x="65" y="100" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Hammer</text>
  <path d="M 90 95 Q 160 30 250 80" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <text x="170" y="45" fill="#38bdf8" font-size="9" font-family="sans-serif">Sensory neuron (Spindle stretch)</text>
  <rect x="250" y="60" width="100" height="80" rx="6" fill="#27272a" stroke="#facc15" stroke-width="2"/>
  <text x="300" y="85" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">L2-L4 Spinal Cord</text>
  <text x="300" y="110" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">(1 Synapse only!)</text>
  <path d="M 280 125 Q 180 160 100 130" stroke="#4ade80" stroke-width="3" fill="none"/>
  <text x="180" y="170" fill="#4ade80" font-size="9" font-family="sans-serif">Motor neuron -> Leg kicks!</text>
</svg>
</div>
Why is the patellar tendon knee-jerk reflex designated as a 'monosynaptic' reflex?""",
     ["The sensory afferent neuron synapses directly with the motor efferent neuron in the spinal cord without any intervening interneuron",
      "It requires exactly one million neurons to fire",
      "It operates only on one leg at a time",
      "It requires a single drop of water to function"],
     "A", "OSC", "hard",
     "The knee-jerk stretch reflex features a single central synapse: primary sensory afferents from muscle spindles connect directly to alpha motor neurons in the spinal cord.")
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

output_path = os.path.join(os.path.dirname(__file__), "ch15_topic4.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
