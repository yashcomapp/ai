# scripts/generate_ch15_topic5.py
# MH-9-SCIT-15-15.5: Endocrine System in Humans & Hormones
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-15-15.5"

exam_data = [
    # 1-10: Endocrine Glands Basics & Pituitary Gland
    ("Why are endocrine glands referred to as 'ductless glands'?",
     ["They secrete chemical messengers directly into the bloodstream without using specialized secretory ducts",
      "They have no blood vessels supplying them",
      "They are located completely outside the human body",
      "They secrete digestive enzymes directly into the intestine"],
     "A", "OSC", "easy",
     "Endocrine glands lack excretory ducts; they discharge hormones directly into capillary blood, which carries them to distant target tissues."),

    ("Which endocrine gland located at the base of the brain is known as the 'master gland' because its secretions regulate other endocrine glands?",
     ["Pituitary gland (hypophysis)", "Adrenal gland", "Thyroid gland", "Pancreas"],
     "A", "OSC", "easy",
     "The anterior pituitary synthesizes tropic hormones (TSH, ACTH, FSH, LH) that regulate downstream peripheral endocrine organs under hypothalamic control."),

    ("Which hormone secreted by the anterior pituitary stimulates cell division, protein synthesis, and elongation of long bones in children?",
     ["Growth Hormone (GH / Somatotropin)", "Insulin", "Thyroxine", "Prolactin"],
     "A", "OSC", "easy",
     "Somatotropin (Growth Hormone) stimulates systemic tissue growth, osteogenesis at epiphyseal plates, and amino acid uptake for protein synthesis."),

    ("What medical condition results from the severe HYPOSECRETION of Growth Hormone during childhood and skeletal development?",
     ["Pituitary dwarfism", "Gigantism", "Acromegaly", "Cretinism"],
     "A", "OSC", "easy",
     "Deficiency of growth hormone before puberty causes pituitary dwarfism, characterized by proportionate short stature with normal mental development."),

    ("What clinical disorder is caused by the excessive HYPERSECRETION of Growth Hormone during adulthood after epiphyseal plate closure?",
     ["Acromegaly (abnormal enlargement of face, hands, and feet bones)", "Gigantism", "Goitre", "Addison's disease"],
     "A", "OSC", "medium",
     "In adults, closed growth plates prevent vertical elongation; excess GH leads to periosteal bone thickening in the jaw, brow ridge, hands, and feet (acromegaly)."),

    ("Which posterior pituitary hormone stimulates uterine smooth muscle contractions during childbirth and milk ejection during breastfeeding?",
     ["Oxytocin", "Prolactin", "Vasopressin", "Progesterone"],
     "A", "OSC", "easy",
     "Oxytocin coordinates positive feedback uterine contractions during labor and triggers myoepithelial contraction in mammary glands for milk letdown."),

    ("Which posterior pituitary hormone regulates water reabsorption in the collecting ducts of the kidneys to concentrate urine?",
     ["Antidiuretic Hormone (ADH / Vasopressin)", "Aldosterone", "Glucagon", "Calcitonin"],
     "A", "OSC", "easy",
     "ADH (vasopressin) inserts aquaporin-2 water channels into renal collecting duct membranes, promoting water reabsorption back into the bloodstream."),

    ("A deficiency in Antidiuretic Hormone (ADH) leads to excessive excretion of dilute urine and constant extreme thirst, known as:",
     ["Diabetes insipidus", "Diabetes mellitus", "Uremia", "Nephritis"],
     "A", "OSC", "medium",
     "Diabetes insipidus results from inadequate ADH release or renal unresponsiveness, producing polyuria (10-20 L/day) and compensatory polydipsia."),

    ("Which essential trace mineral is biochemically required for the thyroid gland to synthesize thyroxine (T4) and triiodothyronine (T3)?",
     ["Iodine", "Iron", "Calcium", "Zinc"],
     "A", "OSC", "easy",
     "Iodine atoms are covalently attached to tyrosine residues in thyroglobulin inside thyroid follicles to produce functional T3 and T4 hormones."),

    ("Abnormal enlargement of the thyroid gland visible as a prominent swelling in the anterior neck due to dietary iodine deficiency is called:",
     ["Simple goitre", "Acromegaly", "Tetany", "Cushing's syndrome"],
     "A", "OSC", "easy",
     "Inadequate dietary iodine depresses thyroxine synthesis; elevated TSH levels stimulate compensatory hypertrophy of follicular cells, producing a simple goitre."),

    # 11-20: Thyroid, Parathyroid & Adrenal Glands
    ("Severe congenital hypothyroidism in infants leading to stunted physical growth and severe mental retardation is termed:",
     ["Cretinism", "Myxoedema", "Grave's disease", "Dwarfism"],
     "A", "OSC", "easy",
     "Untreated neonatal thyroid deficiency causes cretinism, marked by irreversible cognitive impairment, low basal metabolic rate, and skeletal dysplasia."),

    ("Which thyroid hormone works antagonistically to Parathyroid Hormone (PTH) to LOWER blood calcium levels by promoting bone calcium deposition?",
     ["Calcitonin", "Thyroxine", "Aldosterone", "Somatostatin"],
     "A", "OSC", "medium",
     "Calcitonin secreted by parafollicular C-cells inhibits osteoclast bone resorption and promotes calcium excretion, reducing hypercalcemic blood levels."),

    ("What is the primary function of Parathyroid Hormone (PTH / Parathormone)?",
     ["It INCREASES blood calcium ion concentration by stimulating osteoclast bone resorption and renal Ca2+ reabsorption",
      "It lowers blood sugar levels",
      "It destroys white blood cells",
      "It causes dehydration"],
     "A", "OSC", "medium",
     "PTH restores circulating calcium by mobilizing calcium from bone matrices, increasing renal calcium reabsorption, and activating vitamin D for intestinal uptake."),

    ("Severe hypocalcemia resulting from accidental surgical removal of the parathyroid glands causes sustained painful muscle spasms known as:",
     ["Tetany", "Osteoporosis", "Rickets", "Arthritis"],
     "A", "OSC", "hard",
     "Low serum ionized calcium increases neuronal and sarcolemmal sodium permeability, causing spontaneous repetitive firing and sustained spastic contractions (tetany)."),

    ("Where are the suprarenal adrenal glands anatomically situated in the human body?",
     ["Fitted like caps on the upper poles of both kidneys",
      "Inside the lungs",
      "Beneath the tongue",
      "Inside the pelvic bone"],
     "A", "OSC", "easy",
     "The adrenal glands are retroperitoneal endocrine organs resting atop the superior pole of each kidney, composed of an outer cortex and inner medulla."),

    ("Which 'emergency hormone' (fight-or-flight hormone) is rapidly released by the adrenal medulla during intense fear, anger, or acute physical stress?",
     ["Adrenaline (Epinephrine)", "Insulin", "Thyroxine", "Melatonin"],
     "A", "OSC", "easy",
     "Adrenaline primes the body for emergency response by increasing cardiac output, dilating skeletal muscle bronchioles and arterioles, and elevating blood glucose."),

    ("What physiological response is triggered when adrenaline binds to adrenergic receptors in the cardiovascular and respiratory systems?",
     ["Elevated heart rate, increased cardiac output, and dilation of bronchioles",
      "Constriction of airways and cessation of heartbeat",
      "Immediate onset of deep sleep",
      "Complete paralysis of voluntary muscles"],
     "A", "OSC", "easy",
     "Adrenaline stimulates beta-1 adrenergic receptors on cardiac tissue and beta-2 receptors on bronchial smooth muscle, maximizing oxygen and blood delivery."),

    ("Which mineralocorticoid hormone secreted by the adrenal cortex regulates sodium retention and potassium excretion in the kidney tubules?",
     ["Aldosterone", "Cortisol", "Adrenaline", "Calcitonin"],
     "A", "OSC", "medium",
     "Aldosterone stimulates Na+/K+ pumps in distal convoluted tubules and collecting ducts, conserving sodium and water while excreting potassium."),

    ("Glucocorticoids like cortisol secreted by the adrenal cortex regulate:",
     ["Glucose metabolism (gluconeogenesis), protein breakdown, and anti-inflammatory immune suppression",
      "Strictly bone length in teenagers",
      "Direct transmission of auditory signals to the ear",
      "Production of saliva in the mouth"],
     "A", "OSC", "medium",
     "Cortisol mobilizes amino acids and fatty acids for hepatic gluconeogenesis during prolonged stress, while dampening inflammatory cytokine cascades."),

    ("Chronic hyposecretion of adrenal cortex hormones (cortisol and aldosterone) produces bronze skin pigmentation, extreme fatigue, and severe hypotension, known as:",
     ["Addison's disease", "Cushing's syndrome", "Graves' disease", "Hashimoto's thyroiditis"],
     "A", "OSC", "hard",
     "Primary adrenal insufficiency (Addison's disease) leads to electrolyte depletion, hypoglycemia, hypotension, and ACTH-mediated melanin hyperpigmentation."),

    # 21-30: Pancreas, Gonads & Feedback Control
    ("Why is the pancreas classified as a 'heterocrine' or mixed gland?",
     ["It possesses both exocrine acini that secrete digestive enzymes and endocrine Islets of Langerhans that secrete hormones",
      "It produces both blood and urine",
      "It operates only during nighttime",
      "It is located partially in the brain and partially in the abdomen"],
     "A", "OSC", "easy",
     "Over 98% of the pancreas consists of exocrine acini discharging pancreatic juice via ducts, while scattered endocrine Islets of Langerhans secrete hormones directly into blood."),

    ("Which cells within the Islets of Langerhans synthesize and secrete the hormone insulin?",
     ["Beta (beta) cells", "Alpha (alpha) cells", "Delta (delta) cells", "F cells"],
     "A", "OSC", "easy",
     "Beta cells make up the majority of islet cell mass and manufacture insulin in response to elevated blood glucose levels."),

    ("What is the primary biochemical role of insulin in regulating blood glucose homeostasis?",
     ["It facilitates cellular glucose uptake via GLUT-4 transporters and stimulates hepatic glycogenesis, LOWERING blood glucose",
      "It breaks down glycogen into glucose, raising blood sugar",
      "It converts red blood cells into glucose",
      "It stops blood from clotting"],
     "A", "OSC", "easy",
     "Insulin promotes glucose transport into muscle and adipose tissues, stimulates glycogen synthesis in the liver, and inhibits gluconeogenesis."),

    ("Which hormone secreted by alpha cells of the Islets of Langerhans acts antagonistically to insulin by converting liver glycogen into glucose?",
     ["Glucagon", "Somatostatin", "Thyroxine", "Aldosterone"],
     "A", "OSC", "easy",
     "Glucagon stimulates hepatic glycogenolysis and gluconeogenesis, elevating circulating blood glucose during fasting or hypoglycemic states."),

    ("A metabolic disease characterized by chronic hyperglycemia, frequent urination (polyuria), excessive thirst (polydipsia), and insulin insufficiency is:",
     ["Diabetes mellitus", "Diabetes insipidus", "Addison's disease", "Cretinism"],
     "A", "OSC", "easy",
     "Diabetes mellitus stems from impaired insulin secretion (Type 1) or peripheral insulin resistance (Type 2), leading to systemic glucose dysregulation."),

    ("Which primary male sex hormone is synthesized by the interstitial cells of Leydig in the testes?",
     ["Testosterone", "Estrogen", "Progesterone", "Prolactin"],
     "A", "OSC", "easy",
     "Testosterone promotes spermatogenesis and the development of secondary sexual characteristics in males (deep voice, facial hair, muscular build)."),

    ("Which ovarian hormone is responsible for the development of female secondary sexual characteristics and proliferation of the uterine endometrium?",
     ["Estrogen", "Testosterone", "Glucagon", "Aldosterone"],
     "A", "OSC", "easy",
     "Estrogens secreted by ovarian follicles stimulate pubertal secondary sexual traits and repair the endometrium during the pre-ovulatory follicular phase."),

    ("Which hormone secreted by the corpus luteum in the ovary prepares and maintains the uterine endometrium for blastocyst implantation during pregnancy?",
     ["Progesterone", "Oxytocin", "Prolactin", "Luteinizing Hormone (LH)"],
     "A", "OSC", "easy",
     "Progesterone transforms the proliferative endometrium into a secretory receptive lining and suppresses uterine myometrial contractions during pregnancy."),

    ("Which endocrine gland located behind the sternum plays a crucial role in childhood immune maturation by training T-lymphocytes, but atrophies after puberty?",
     ["Thymus gland", "Thyroid gland", "Pineal gland", "Adrenal gland"],
     "A", "OSC", "medium",
     "The thymus secretes thymosin, orchestrating T-cell differentiation and immunocompetence before gradually regressing into fibrofatty tissue in adulthood."),

    ("How does the human body maintain stable hormone concentrations through a 'negative feedback mechanism'?",
     ["An increase in the circulating target hormone inhibits further secretion of the upstream releasing or stimulating hormones",
      "The hormone destroys all receptor tissues permanently",
      "The hormone is excreted unchanged in tears",
      "Hormone levels keep doubling indefinitely without stopping"],
     "A", "OSC", "medium",
     "In negative feedback, the biological output or elevated peripheral hormone concentration feeds back to inhibit hypothalamic or pituitary tropic drivers, stabilizing homeostasis."),

    # 31-40: Fill in blanks, Numerical, Multi-choice
    ("The tiny pine cone-shaped endocrine gland in the epithalamus that secretes melatonin to regulate sleep-wake circadian rhythms is the ________ gland.",
     ["pineal", "pituitary", "thymus", "thyroid"],
     "A", "OFB", "easy",
     "The pineal gland responds to optic light-dark cycles by synthesizing melatonin, which governs diurnal physiological rhythms."),

    ("In an adult human, normal fasting blood glucose concentration strictly ranges between 70 and ________ mg/dL of blood.",
     ["99 (or 100)", "250", "500", "20"],
     "A", "OFB", "easy",
     "Clinical diagnostic criteria classify normal fasting capillary or plasma glucose between 70 and 99 mg/dL; values >= 126 mg/dL indicate diabetes."),

    ("A normal human adult body contains ________ separate parathyroid glands embedded on the posterior surface of the thyroid lobes.",
     ["4 (two pairs)", "2", "8", "1"],
     "A", "ONE", "easy",
     "Humans typically possess four parathyroid glands: one superior and one inferior gland on the posterior border of each thyroid lateral lobe."),

    ("State whether True or False: Hormones act at extremely low physiological concentrations and are directly transported to target cells via circulating blood plasma.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Hormones circulate in nanomolar or picomolar concentrations and interact with high-affinity target receptor proteins to elicit intracellular signaling cascades."),

    ("Which of the following endocrine glands are paired organs present symmetrically on both left and right sides of the human body? (Select all that apply)",
     ["Adrenal glands, Ovaries in females, and Testes in males",
      "Only the pituitary gland and thyroid gland",
      "Only the pancreas and liver",
      "Only the thymus gland"],
     "A", "OMC", "easy",
     "Adrenals (superior poles of both kidneys), ovaries (bilateral in pelvic cavity), and testes (bilateral in scrotum) exist as anatomical paired organs."),

    ("State whether True or False: Steroid hormones (such as testosterone and estrogen) are lipid-soluble and can easily cross target cell plasma membranes to bind intracellular receptors.",
     ["True", "False"],
     "A", "OTF", "medium",
     "Steroid hormones are lipophilic cholesterol derivatives; they diffuse across phospholipid bilayers and interact with nuclear receptors to modulate gene transcription."),

    ("What happens to blood glucose and cellular metabolism when insulin secretion fails completely in Type 1 Diabetes Mellitus?",
     ["Cells cannot absorb glucose effectively, leading to severe hyperglycemia, glycosuria, and dangerous ketoacidosis",
      "Blood sugar drops to zero instantly",
      "The body converts all muscles into solid gold",
      "The brain stops using oxygen entirely"],
     "A", "OSC", "medium",
     "Without insulin, glucose cannot enter myocytes or adipocytes, accumulating in blood while cells catabolize fats, generating excessive acidic ketone bodies."),

    ("Which gland coordinates the entire endocrine system by providing the physiological neuroendocrine bridge between the nervous system and the pituitary?",
     ["Hypothalamus", "Cerebellum", "Medulla oblongata", "Thalamus"],
     "A", "OSC", "easy",
     "The hypothalamus receives systemic neural inputs and secretes hypophysiotropic releasing and inhibiting hormones into the hypophyseal portal system."),

    ("Assertion (A): Adrenaline increases blood pressure, respiration rate, and blood sugar levels during emotional or physical crisis.\nReason (R): Adrenaline acts to divert maximum oxygen and energetic glucose to skeletal muscles and the brain for emergency survival.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is not the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     "Adrenaline orchestrates sympathetic autonomic fight-or-flight adjustments, prioritizing perfusion and substrate supply to vital muscular and cerebral tissues."),

    ("Which two hormones work antagonistically in tandem to tightly clamp blood glucose within the narrow physiological range of 70-110 mg/dL?",
     ["Insulin and Glucagon", "Thyroxine and Calcitonin", "Adrenaline and Noradrenaline", "Estrogen and Progesterone"],
     "A", "OSC", "easy",
     "Insulin promotes glucose storage when blood sugar rises after meals, while glucagon stimulates glycogen breakdown when blood sugar drops during fasting.")
]

practice_data = [
    # 41-50: Advanced Endocrine Mechanisms
    ("What structural feature distinguishes peptide/protein hormones (like insulin) from steroid hormones (like cortisol) in terms of receptor binding?",
     ["Peptide hormones are water-soluble and bind to cell-surface transmembrane receptors, whereas steroid hormones cross the membrane to bind intracellular receptors",
      "Peptide hormones are made of pure fats and dissolve bones",
      "Steroid hormones cannot enter the bloodstream",
      "Peptide hormones have no effect on living organisms"],
     "A", "OSC", "medium",
     "Hydrophilic peptide hormones cannot cross the hydrophobic lipid bilayer; they trigger secondary messenger cascades (e.g. cAMP) via cell-surface G-protein coupled or tyrosine kinase receptors."),

    ("In Graves' disease (autoimmune hyperthyroidism), what causes the thyroid gland to become persistently overactive?",
     ["Autoantibodies (thyroid-stimulating immunoglobulins) continuously bind to and stimulate TSH receptors, independent of negative feedback",
      "A total lack of iodine in table salt",
      "Destruction of the pituitary gland by bacteria",
      "Complete surgical removal of the neck"],
     "A", "OSC", "hard",
     "TSI autoantibodies mimic TSH by activating follicular TSH receptors, driving unrelenting thyroid hormone overproduction and causing exophthalmos (protruding eyes)."),

    ("How does the kidney respond when circulating levels of Aldosterone rise sharply?",
     ["It increases sodium and water reabsorption into blood while increasing potassium ion excretion into urine",
      "It ceases urine production entirely",
      "It excretes all blood cells into the bladder",
      "It produces huge quantities of pure sugar"],
     "A", "OSC", "medium",
     "Aldosterone upregulates epithelial sodium channels (ENaC) and basolateral Na+/K+ pumps in principal cells, conserving fluid volume and raising blood pressure."),

    ("Which endocrine tissue secretes Erythropoietin (EPO) to stimulate red blood cell erythropoiesis in bone marrow during hypoxic conditions?",
     ["Kidneys (renal interstitial peritubular capillary cells)", "Spleen", "Pancreas", "Thyroid gland"],
     "A", "OSC", "medium",
     "When renal oxygen sensors detect arterial hypoxia, interstitial peritubular fibroblasts synthesize EPO, which stimulates erythroid progenitor proliferation in bone marrow."),

    ("Why is milk letdown in nursing mothers triggered when the baby begins suckling, even before significant milk is ingested?",
     ["Suckling sensory nerves fire afferent impulses to the hypothalamus, triggering rapid neurohypophyseal oxytocin release (neuroendocrine reflex)",
      "The baby's cry mechanically pushes milk through the skin",
      "Milk is made of air that expands when warm",
      "The stomach compresses the chest"],
     "A", "OSC", "medium",
     "Suckling evokes a neuroendocrine reflex arc: mechanical nipple stimulation signals hypothalamic paraventricular nuclei to discharge oxytocin, contracting mammary alveoli."),

    ("What pathological syndrome is caused by chronic excessive cortisol production (often due to an ACTH-secreting pituitary adenoma or corticosteroid medication)?",
     ["Cushing's syndrome (characterized by moon face, buffalo hump, and central obesity)",
      "Addison's disease",
      "Cretinism",
      "Grave's disease"],
     "A", "OSC", "hard",
     "Hypercortisolemia breaks down peripheral muscle proteins and redistributes adipose tissue to the supraclavicular fat pad ('buffalo hump'), face ('moon face'), and abdomen."),

    ("Which enzyme in the juxtaglomerular apparatus of the kidney triggers the Renin-Angiotensin-Aldosterone System (RAAS) when renal blood flow drops?",
     ["Renin", "Pepsin", "Trypsin", "Amylase"],
     "A", "OSC", "medium",
     "Renin cleaves circulating angiotensinogen into angiotensin I, which ACE converts to angiotensin II to trigger vasoconstriction and aldosterone release."),

    ("What is the function of Somatostatin secreted by delta (delta) cells of the pancreatic Islets of Langerhans?",
     ["It acts as an inhibitory paracrine regulator that dampens the secretion of both insulin and glucagon",
      "It speeds up heart contractions",
      "It stimulates bone marrow growth",
      "It synthesizes antibodies"],
     "A", "OSC", "hard",
     "Delta-cell somatostatin exerts local paracrine restraint over nearby alpha and beta cells, modulating postprandial nutrient absorption and hormonal surges."),

    ("State whether True or False: Exocrine secretions (like pancreatic digestive enzymes) travel through specialized ducts to body cavities, whereas endocrine secretions have no ducts.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Exocrine glands possess ducts through which their secretions are delivered to specific epithelial surfaces; endocrine glands discharge directly into surrounding interstitium and blood."),

    ("Why does drinking large amounts of water lead to the rapid excretion of copious dilute urine within 30-60 minutes?",
     ["Dilution of blood decreases plasma osmolarity, turning off hypothalamic osmoreceptors and suppressing ADH secretion by the posterior pituitary",
      "The bladder shrinks under pressure",
      "Water destroys the kidneys' filtration membrane",
      "Water dissolves the adrenal cortex"],
     "A", "OSC", "medium",
     "Hypo-osmolar plasma inhibits supraoptic hypothalamic osmoreceptors; reduced circulating ADH leaves renal collecting ducts water-impermeable, eliminating excess fluid."),

    # 51-60: Further Hormonal Regulation & Case Problems
    ("Which pituitary hormone stimulates the thyroid gland to synthesize and release thyroxine (T4)?",
     ["Thyroid-Stimulating Hormone (TSH / Thyrotropin)", "Adrenocorticotropic Hormone (ACTH)", "Follicle-Stimulating Hormone (FSH)", "Growth Hormone (GH)"],
     "A", "OSC", "easy",
     "Thyrotropin (TSH) from anterior pituitary basophils stimulates thyroid iodide uptake, thyroglobulin iodination, and pinocytotic release of thyroid hormones."),

    ("What is the biochemical precursor molecule from which all human steroid hormones (aldosterone, cortisol, testosterone, estrogen, progesterone) are synthesized?",
     ["Cholesterol", "Glucose", "Amino acids", "Phospholipids"],
     "A", "OSC", "medium",
     "Steroidogenic enzymes in adrenal cortex and gonadal mitochondria cleave the side chain of cholesterol to yield pregnenolone, the mother steroid for all steroid hormones."),

    ("A patient presents with weight loss, heat intolerance, rapid resting pulse (tachycardia), and protruding eyeballs (exophthalmos). Which disorder is most probable?",
     ["Hyperthyroidism (Graves' disease)", "Hypothyroidism (Myxoedema)", "Hypoparathyroidism (Tetany)", "Addison's disease"],
     "A", "OSC", "medium",
     "Excess circulating thyroid hormones drastically accelerate basal metabolic rate and cellular oxygen consumption, generating excessive heat and autonomic tachycardia."),

    ("Which hormone induces ovulation of the mature graafian follicle and transforms the ruptured follicle into the corpus luteum in females?",
     ["Luteinizing Hormone (LH)", "Follicle-Stimulating Hormone (FSH)", "Human Chorionic Gonadotropin (hCG)", "Prolactin"],
     "A", "OSC", "medium",
     "A mid-cycle LH surge triggers follicular rupture (ovulation) and luteinization of the remaining granulosa and theca cells into the steroidogenic corpus luteum."),

    ("What is the primary function of Follicle-Stimulating Hormone (FSH) in males?",
     ["It stimulates Sertoli (nurse) cells in the seminiferous tubules to support and nurture developing sperm cells (spermatogenesis)",
      "It stimulates facial beard growth",
      "It stimulates adrenaline secretion",
      "It causes bone lengthening"],
     "A", "OSC", "medium",
     "FSH binds to Sertoli cells in the testicular seminiferous epithelium, stimulating the synthesis of androgen-binding protein (ABP) vital for spermatogenesis."),

    ("In an emergency stress response, noradrenaline (norepinephrine) works alongside adrenaline primarily by:",
     ["Causing widespread vasoconstriction of peripheral blood vessels, raising systemic arterial blood pressure",
      "Inducing deep unconsciousness",
      "Lowering body temperature to freezing",
      "Stopping heart contractions"],
     "A", "OSC", "medium",
     "Noradrenaline binds to alpha-adrenergic receptors on vascular smooth muscle, inducing systemic vasoconstriction that elevates peripheral vascular resistance and blood pressure."),

    ("State whether True or False: The pancreas produces both the hormone insulin to lower blood glucose and pancreatic amylase to digest carbohydrates in the small intestine.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The pancreas performs dual exocrine functions (secreting digestive enzymes including amylase, trypsin, and lipase) and endocrine functions (secreting insulin and glucagon)."),

    ("Which endocrine hormone promotes the retention of bone density in women and causes rapid bone loss (osteoporosis) when its levels drop sharply after menopause?",
     ["Estrogen", "Thyroxine", "Adrenaline", "Insulin"],
     "A", "OSC", "medium",
     "Estrogen inhibits osteoclastic bone resorption; postmenopausal cessation of ovarian estrogen synthesis leads to accelerated bone mineral loss and osteoporosis."),

    ("A patient with severe dehydration and low blood pressure is injected with a synthetic hormone that causes immediate fluid retention and vasoconstriction. This drug mimics:",
     ["Vasopressin (Antidiuretic Hormone / ADH)", "Insulin", "Oxytocin", "Calcitonin"],
     "A", "OSC", "medium",
     "Vasopressin activates V2 receptors in renal ducts to conserve water and V1 receptors on vascular smooth muscle to induce compensatory vasoconstriction."),

    ("The hormone melatonin is produced by the pineal gland in response to darkness. Its synthesis is strongly INHIBITED by:",
     ["Exposure to bright blue-spectrum light entering the retina",
      "Eating salty foods",
      "Drinking cold water",
      "Speaking aloud"],
     "A", "OSC", "easy",
     "Retinal ganglion cells project light signals via the retinohypothalamic tract to the suprachiasmatic nucleus (SCN), suppressing daytime pineal melatonin synthesis."),

    # 61-70: High-Yield Practice Questions
    ("Which physiological parameter is monitored by hypothalamic osmoreceptors to adjust ADH release?",
     ["Blood plasma osmolarity (solute concentration)", "Total volume of air in lungs", "Number of hair follicles on head", "Skin surface area"],
     "A", "OSC", "medium",
     "Hypothalamic osmoreceptors shrink or swell in response to changes in blood extracellular osmolarity, fine-tuning ADH secretion within a 1% sensitivity margin."),

    ("What is the physiological role of calcitonin in human skeletal physiology?",
     ["It temporarily slows down osteoclast activity when serum calcium spikes abnormally after calcium-rich meals",
      "It dissolves the skeleton into soft cartilage",
      "It stops blood from flowing through bones",
      "It causes immediate tooth loss"],
     "A", "OSC", "medium",
     "Calcitonin acts as an emergency brake on osteoclasts during acute hypercalcemia, facilitating bone mineralization and urinary calcium excretion."),

    ("Which endocrine disorder results from immune-mediated destruction of pancreatic beta cells, requiring lifelong exogenous insulin administration?",
     ["Type 1 Diabetes Mellitus", "Type 2 Diabetes Mellitus", "Diabetes Insipidus", "Gestational Diabetes"],
     "A", "OSC", "easy",
     "Type 1 diabetes is an autoimmune disease where autoreactive T cells destroy insulin-producing pancreatic beta cells, resulting in absolute insulin deficiency."),

    ("In Type 2 Diabetes Mellitus, the primary underlying defect in early stages is:",
     ["Peripheral insulin resistance in skeletal muscle, liver, and adipose tissues despite normal or elevated insulin secretion",
      "Complete surgical removal of the pancreas",
      "Destruction of all red blood cells",
      "Hyperactivity of the pineal gland"],
     "A", "OSC", "medium",
     "Type 2 diabetes begins with impaired insulin sensitivity in target tissues; beta cells compensate by producing extra insulin until chronic exhaustion triggers overt hyperglycemia."),

    ("What is the function of human chorionic gonadotropin (hCG) produced by the early embryonic trophoblast during pregnancy?",
     ["It maintains the corpus luteum so it continues secreting progesterone to prevent uterine menstruation",
      "It triggers labor contractions immediately",
      "It stops the fetus from developing bones",
      "It destroys the placenta"],
     "A", "OSC", "hard",
     "hCG mimics LH, rescuing the corpus luteum from degeneration during the first trimester until the placenta matures enough to take over progesterone synthesis."),

    ("Which hypothalamic releasing hormone stimulates the anterior pituitary to secrete LH and FSH?",
     ["Gonadotropin-Releasing Hormone (GnRH)", "Thyrotropin-Releasing Hormone (TRH)", "Corticotropin-Releasing Hormone (CRH)", "Growth Hormone-Releasing Hormone (GHRH)"],
     "A", "OSC", "medium",
     "Pulsatile release of GnRH from the arcuate and preoptic hypothalamic nuclei stimulates pituitary gonadotroph cells to secrete FSH and LH."),

    ("State whether True or False: Both nervous and endocrine systems work cooperatively to maintain internal homeostasis, with the nervous system providing rapid localized responses and the endocrine system providing broader, longer-lasting metabolic control.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Neural signaling operates via millisecond electrical impulses and neurotransmitters across synapses, whereas endocrine signaling operates via circulating hormones over hours or days."),

    ("Which hormone increases cardiac output and triggers hepatic glycogen breakdown to provide immediate glucose fuel during extreme physical exertion?",
     ["Adrenaline", "Calcitonin", "Melatonin", "Oxytocin"],
     "A", "OSC", "easy",
     "Adrenaline stimulates adrenergic receptors across liver, muscle, and cardiovascular tissue to prepare the organism for intense fight-or-flight energy expenditure."),

    ("What is the primary role of thyroid hormones (T3 and T4) in cellular respiration?",
     ["They increase mitochondrial oxygen consumption, basal metabolic rate (BMR), and cellular ATP turnover",
      "They stop cellular respiration entirely",
      "They convert glucose into solid fat exclusively",
      "They freeze cellular cytoplasm"],
     "A", "OSC", "medium",
     "Thyroid hormones upregulate Na+/K+ ATPase synthesis and uncoupling proteins, increasing mitochondrial respiration, baseline oxygen consumption, and body heat production."),

    ("When blood calcium levels drop below 8.5 mg/dL, which endocrine gland detects this drop directly and secretes corrective hormone?",
     ["Parathyroid glands (secreting Parathyroid Hormone / PTH)", "Thyroid gland (secreting Calcitonin)", "Pineal gland (secreting Melatonin)", "Thymus gland (secreting Thymosin)"],
     "A", "OSC", "easy",
     "Calcium-sensing receptors (CaSR) on chief cells of the parathyroid glands detect hypocalcemia, immediately triggering PTH release to mobilize skeletal and renal calcium.")
]

mock_data = [
    # 71: Major Endocrine Glands in Human Body Map
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="220" viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="220" rx="8" fill="#090d16"/>
  <!-- Head & Neck -->
  <circle cx="100" cy="50" r="22" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="108" cy="52" r="4" fill="#facc15"/>
  <text x="140" y="45" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">1. Pituitary & Hypothalamus</text>
  <!-- Thyroid -->
  <path d="M 94 85 Q 100 90 106 85 Q 100 98 94 85" fill="#ec4899"/>
  <text x="140" y="88" fill="#ec4899" font-size="10" font-family="sans-serif" font-weight="bold">2. Thyroid (Thyroxine / Calcitonin)</text>
  <!-- Adrenals & Kidneys -->
  <rect x="85" y="125" width="12" height="18" rx="5" fill="#334155"/>
  <path d="M 85 125 L 91 118 L 97 125 Z" fill="#eab308"/>
  <rect x="105" y="125" width="12" height="18" rx="5" fill="#334155"/>
  <path d="M 105 125 L 111 118 L 117 125 Z" fill="#eab308"/>
  <text x="140" y="125" fill="#eab308" font-size="10" font-family="sans-serif" font-weight="bold">3. Adrenals (Adrenaline / Cortisol)</text>
  <!-- Pancreas -->
  <path d="M 88 150 Q 110 148 115 155 Q 100 158 88 150" fill="#22c55e"/>
  <text x="140" y="155" fill="#22c55e" font-size="10" font-family="sans-serif" font-weight="bold">4. Pancreas (Insulin / Glucagon)</text>
  <!-- Gonads -->
  <circle cx="92" cy="188" r="7" fill="#a855f7"/>
  <circle cx="108" cy="188" r="7" fill="#a855f7"/>
  <text x="140" y="192" fill="#a855f7" font-size="10" font-family="sans-serif" font-weight="bold">5. Gonads (Testes / Ovaries)</text>
</svg>
</div>
In the anatomical map of human endocrine glands above, which numbered gland functions as a heterocrine organ possessing both digestive exocrine acini and hormone-secreting endocrine islets?""""",
     ["Gland 4: Pancreas", "Gland 1: Pituitary", "Gland 2: Thyroid", "Gland 3: Adrenals"],
     "A", "OSC", "medium",
     "The pancreas (Gland 4) is a mixed heterocrine organ: 99% of its mass secretes exocrine pancreatic digestive juices into the duodenum, while the Islets of Langerhans release insulin and glucagon into blood."),

    # 72: Blood Glucose Feedback Loop
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#111827"/>
  <!-- Central Balance -->
  <rect x="120" y="20" width="160" height="35" rx="6" fill="#1f2937" stroke="#38bdf8" stroke-width="2"/>
  <text x="200" y="42" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Normal Glucose (70-100 mg/dL)</text>
  <!-- High blood sugar loop -->
  <path d="M 280 35 Q 360 40 360 100 Q 360 160 280 165" stroke="#ef4444" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
  <text x="310" y="85" fill="#f87171" font-size="9" font-family="sans-serif">Blood sugar Rises</text>
  <rect x="230" y="145" width="110" height="40" rx="5" fill="#15803d"/>
  <text x="285" y="162" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Beta Cells -> Insulin</text>
  <text x="285" y="176" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">Glucose -> Glycogen</text>
  <!-- Low blood sugar loop -->
  <path d="M 120 35 Q 40 40 40 100 Q 40 160 120 165" stroke="#eab308" stroke-width="2" fill="none"/>
  <text x="45" y="85" fill="#facc15" font-size="9" font-family="sans-serif">Blood sugar Drops</text>
  <rect x="60" y="145" width="110" height="40" rx="5" fill="#b45309"/>
  <text x="115" y="162" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Alpha Cells -> Glucagon</text>
  <text x="115" y="176" fill="#fef08a" font-size="8" font-family="sans-serif" text-anchor="middle">Glycogen -> Glucose</text>
</svg>
</div>
According to the dual-hormone glucose regulation loop above, what cellular mechanism restores homeostatic blood sugar following a heavy carbohydrate meal?""""",
     ["Pancreatic beta cells release insulin, promoting cellular glucose uptake and hepatic glycogen storage",
      "Alpha cells release glucagon to double the blood sugar",
      "The kidneys excrete all blood into the urine",
      "Thyroxine converts blood glucose into heavy metals"],
     "A", "OSC", "medium",
     "Postprandial hyperglycemia activates pancreatic beta cells to release insulin; insulin stimulates muscle/adipose glucose uptake and activates hepatic glycogen synthase to convert excess glucose to glycogen."),

    # 73: Thyroid & TSH Negative Feedback
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <!-- Hypothalamus -->
  <rect x="40" y="25" width="130" height="35" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="105" y="47" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Hypothalamus (TRH)</text>
  <line x1="170" y1="42" x2="220" y2="42" stroke="#38bdf8" stroke-width="2"/>
  <!-- Anterior Pituitary -->
  <rect x="220" y="25" width="140" height="35" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="290" y="47" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pituitary (TSH)</text>
  <line x1="290" y1="60" x2="290" y2="110" stroke="#facc15" stroke-width="2"/>
  <!-- Thyroid -->
  <rect x="220" y="110" width="140" height="35" rx="5" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
  <text x="290" y="132" fill="#ec4899" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Thyroid (T3 & T4)</text>
  <!-- Negative Feedback Arrow -->
  <path d="M 220 128 Q 60 128 60 60" stroke="#ef4444" stroke-width="3" stroke-dasharray="4" fill="none"/>
  <text x="80" y="105" fill="#ef4444" font-size="9" font-family="sans-serif" font-weight="bold">(-) Negative Feedback</text>
</svg>
</div>
In the hypothalamic-pituitary-thyroid regulatory axis depicted above, what physiological response occurs if blood levels of T3 and T4 rise significantly above normal?""""",
     ["High T3 and T4 exert negative feedback on the hypothalamus and anterior pituitary, suppressing further TRH and TSH secretion",
      "TSH secretion increases tenfold to make even more thyroxine",
      "The thyroid gland undergoes immediate necrosis",
      "The anterior pituitary stops all heart beats"],
     "A", "OSC", "medium",
     "Elevated circulating free T3/T4 binds to nuclear receptors in pituitary thyrotrophs and hypothalamic neurons, downregulating TRH and TSH transcription and restoring baseline balance."),

    # 74: Adrenal Gland Anatomy: Cortex vs Medulla
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Adrenal Cross Section -->
  <path d="M 60 150 Q 120 30 180 150 Z" fill="#eab308" stroke="#facc15" stroke-width="2"/>
  <path d="M 85 145 Q 120 70 155 145 Z" fill="#b91c1c" stroke="#f87171" stroke-width="2"/>
  <text x="120" y="130" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Medulla</text>
  <text x="120" y="55" fill="#fef08a" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Cortex</text>
  <!-- Labels -->
  <line x1="160" y1="50" x2="220" y2="50" stroke="#facc15" stroke-width="2"/>
  <text x="230" y="45" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">Outer Cortex:</text>
  <text x="230" y="60" fill="#e2e8f0" font-size="9" font-family="sans-serif">- Aldosterone (Mineralocorticoid)</text>
  <text x="230" y="75" fill="#e2e8f0" font-size="9" font-family="sans-serif">- Cortisol (Glucocorticoid)</text>
  <line x1="145" y1="125" x2="220" y2="125" stroke="#f87171" stroke-width="2"/>
  <text x="230" y="120" fill="#f87171" font-size="10" font-family="sans-serif" font-weight="bold">Inner Medulla:</text>
  <text x="230" y="135" fill="#e2e8f0" font-size="9" font-family="sans-serif">- Adrenaline (Epinephrine)</text>
  <text x="230" y="150" fill="#e2e8f0" font-size="9" font-family="sans-serif">- Noradrenaline (Norepinephrine)</text>
</svg>
</div>
Based on the adrenal cross-sectional diagram above, what functional distinction exists between the adrenal cortex and the adrenal medulla?""""",
     ["The cortex secretes steroid hormones (aldosterone and cortisol) under ACTH/RAAS control, while the medulla secretes catecholamines (adrenaline) under direct sympathetic nerve control",
      "The cortex secretes pure water while the medulla secretes solid salt",
      "The medulla is an exocrine organ with salivary ducts",
      "The cortex produces digestive enzymes for the stomach"],
     "A", "OSC", "hard",
     "The adrenal cortex originates from mesoderm and synthesizes life-sustaining corticosteroid hormones, whereas the inner medulla originates from neural crest ectoderm and functions as a modified sympathetic ganglion."),

    # 75: Calcium Homeostasis: PTH vs Calcitonin
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Target line -->
  <line x1="50" y1="95" x2="350" y2="95" stroke="#334155" stroke-width="2" stroke-dasharray="3"/>
  <text x="200" y="90" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Normal Blood Calcium (9 - 11 mg/dL)</text>
  <!-- Hypercalcemia response -->
  <rect x="50" y="20" width="130" height="45" rx="5" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
  <text x="115" y="38" fill="#ec4899" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Blood Ca2+ HIGH</text>
  <text x="115" y="54" fill="#f472b6" font-size="9" font-family="sans-serif" text-anchor="middle">Thyroid -> Calcitonin</text>
  <text x="115" y="80" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">v Bone deposition</text>
  <!-- Hypocalcemia response -->
  <rect x="220" y="125" width="130" height="45" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="285" y="143" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Blood Ca2+ LOW</text>
  <text x="285" y="159" fill="#fde047" font-size="9" font-family="sans-serif" text-anchor="middle">Parathyroid -> PTH</text>
  <text x="285" y="115" fill="#f87171" font-size="9" font-family="sans-serif" text-anchor="middle">^ Bone resorption</text>
</svg>
</div>
In the antagonistic calcium balance model illustrated above, what direct cellular action does Parathyroid Hormone (PTH) take to raise dangerously low blood calcium levels?""""",
     ["It stimulates osteoclasts in bone to dissolve calcium salts, promotes renal calcium reabsorption, and activates vitamin D for gut absorption",
      "It deposits all blood calcium into tooth enamel permanently",
      "It stimulates thyroid calcitonin release to drop calcium further",
      "It filters all calcium out through sweat glands"],
     "A", "OSC", "medium",
     "PTH acts on osteoblasts to induce RANKL expression, driving osteoclastogenesis and bone mineral demineralization, while upregulating renal Ca2+ reabsorption and 1-alpha-hydroxylase to yield active calcitriol."),

    # 76: Pituitary Anterior vs Posterior Lobes
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#111827"/>
  <!-- Hypothalamus above -->
  <rect x="130" y="15" width="140" height="30" rx="4" fill="#1f2937" stroke="#38bdf8" stroke-width="2"/>
  <text x="200" y="34" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Hypothalamus</text>
  <!-- Anterior Pituitary -->
  <circle cx="150" cy="115" r="35" fill="#2563eb" stroke="#60a5fa" stroke-width="2"/>
  <text x="150" y="112" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Anterior Lobe</text>
  <text x="150" y="126" fill="#bfdbfe" font-size="8" font-family="sans-serif" text-anchor="middle">(Adenohypophysis)</text>
  <!-- Posterior Pituitary -->
  <circle cx="230" cy="115" r="30" fill="#7c3aed" stroke="#c084fc" stroke-width="2"/>
  <text x="230" y="112" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Posterior Lobe</text>
  <text x="230" y="126" fill="#e9d5ff" font-size="8" font-family="sans-serif" text-anchor="middle">(Neurohypophysis)</text>
  <!-- Axons vs Portal -->
  <line x1="160" y1="45" x2="150" y2="80" stroke="#f59e0b" stroke-width="3" stroke-dasharray="2"/>
  <line x1="220" y1="45" x2="230" y2="85" stroke="#ef4444" stroke-width="3"/>
  <text x="75" y="170" fill="#60a5fa" font-size="9" font-family="sans-serif">Synthesizes GH, TSH, ACTH, LH, FSH</text>
  <text x="220" y="170" fill="#c084fc" font-size="9" font-family="sans-serif">Stores & releases Oxytocin, ADH</text>
</svg>
</div>
How does the posterior pituitary (neurohypophysis) differ fundamentally in origin and function from the anterior pituitary (adenohypophysis)?""""",
     ["The posterior pituitary does not synthesize its own hormones; it stores and releases oxytocin and ADH synthesized in hypothalamic neurosecretory cell bodies",
      "The posterior pituitary secretes digestive saliva while the anterior lobe secretes urine",
      "The anterior lobe is made of bone while the posterior lobe is made of cartilage",
      "The posterior lobe operates only in infants"],
     "A", "OSC", "hard",
     "The neurohypophysis is an anatomical extension of hypothalamic neuroectoderm containing axon terminals from paraventricular and supraoptic nuclei; the adenohypophysis develops from oral Rathke's pouch ectoderm and synthesizes hormones de novo."),

    # 77: Growth Hormone Pathologies: Gigantism vs Acromegaly
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Childhood GH excess -->
  <rect x="30" y="30" width="160" height="130" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="55" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">GH Excess BEFORE Puberty</text>
  <text x="110" y="80" fill="#facc15" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">GIGANTISM</text>
  <text x="110" y="105" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Epiphyseal plates OPEN</text>
  <text x="110" y="125" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Extreme proportionate height (> 7-8 ft)</text>
  <!-- Adult GH excess -->
  <rect x="210" y="30" width="160" height="130" rx="6" fill="#27272a" stroke="#ec4899" stroke-width="2"/>
  <text x="290" y="55" fill="#ec4899" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">GH Excess IN ADULTHOOD</text>
  <text x="290" y="80" fill="#f472b6" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">ACROMEGALY</text>
  <text x="290" y="105" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Epiphyseal plates CLOSED</text>
  <text x="290" y="125" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Thickening of jaw, hands, brow, feet</text>
</svg>
</div>
Why does hypersecretion of growth hormone in a 40-year-old adult result in acromegaly (thickened facial features and hands) rather than gigantism (increased vertical height)?""""",
     ["Epiphyseal growth plates of long bones are permanently ossified and fused after puberty, preventing further longitudinal bone growth",
      "Adults stop absorbing calcium completely",
      "The heart shrinks so blood cannot reach the legs",
      "Growth hormone changes into water after age 25"],
     "A", "OSC", "medium",
     "Following pubertal growth spurt completion, gonadal steroids trigger epiphyseal cartilage ossification and plate fusion; subsequent somatotropin excess stimulates only subperiosteal appositional bone growth, resulting in acromegalic enlargement."),

    # 78: RAAS (Renin-Angiotensin-Aldosterone System)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <!-- Kidney -->
  <rect x="30" y="40" width="85" height="40" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="72" y="58" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Kidney (Low BP)</text>
  <text x="72" y="72" fill="#93c5fd" font-size="8" font-family="sans-serif" text-anchor="middle">Releases Renin</text>
  <line x1="115" y1="60" x2="155" y2="60" stroke="#38bdf8" stroke-width="2"/>
  <!-- Liver Angiotensinogen -> Ang I -> Ang II -->
  <rect x="155" y="40" width="95" height="40" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="202" y="58" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Angiotensin II</text>
  <text x="202" y="72" fill="#fef08a" font-size="8" font-family="sans-serif" text-anchor="middle">Powerful Vasoconstrictor</text>
  <line x1="250" y1="60" x2="290" y2="60" stroke="#facc15" stroke-width="2"/>
  <!-- Adrenal Cortex -->
  <rect x="290" y="40" width="85" height="40" rx="5" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
  <text x="332" y="58" fill="#22c55e" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Adrenal Cortex</text>
  <text x="332" y="72" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle">Aldosterone</text>
  <!-- Outcome Box -->
  <rect x="70" y="115" width="260" height="50" rx="6" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="200" y="135" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Conserves Na+ and Water in Renal Tubules</text>
  <text x="200" y="152" fill="#bbf7d0" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">^ Blood Volume & Blood Pressure Restored!</text>
</svg>
</div>
In the RAAS physiological cascade shown above, what triggers the initial release of renin from juxtaglomerular cells in the kidney?""""",
     ["A drop in renal perfusion pressure, decreased blood volume, or reduced sodium chloride delivery to the macula densa",
      "High atmospheric humidity",
      "Eating too much sugar",
      "Excessive oxygen in the lungs"],
     "A", "OSC", "hard",
     "Renal baroreceptors detect arteriolar hypotension, sympathetic nerves fire via beta-1 receptors, and macula densa cells sense reduced NaCl flux, triggering juxtaglomerular renin exocytosis."),

    # 79: Comparison: Nervous vs Endocrine System
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Nervous System Box -->
  <rect x="25" y="25" width="165" height="140" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="107" y="48" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Nervous Control</text>
  <text x="107" y="72" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Electrical (Action Potential)</text>
  <text x="107" y="92" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Extremely rapid (milliseconds)</text>
  <text x="107" y="112" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Highly localized (synapses)</text>
  <text x="107" y="132" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Short-lived duration</text>
  <!-- Endocrine System Box -->
  <rect x="210" y="25" width="165" height="140" rx="6" fill="#27272a" stroke="#a855f7" stroke-width="2"/>
  <text x="292" y="48" fill="#a855f7" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Endocrine Control</text>
  <text x="292" y="72" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Chemical (Hormones in blood)</text>
  <text x="292" y="92" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Slower onset (seconds to hours)</text>
  <text x="292" y="112" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Widespread systemic targets</text>
  <text x="292" y="132" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Prolonged, long-lasting effects</text>
</svg>
</div>
Which characteristic is unique to endocrine regulation compared to nervous system regulation according to the comparison chart above?""""",
     ["Endocrine signals are chemical messengers transported systemically via bloodstream, producing widespread and long-lasting metabolic changes",
      "Endocrine signals travel faster than electricity across nerves",
      "Endocrine signals never affect internal organs",
      "Endocrine signals only operate when an individual is asleep"],
     "A", "OSC", "medium",
     "While nervous coordination provides millisecond-fast precision via synaptic point-to-point connections, endocrine coordination broadcasts hormones systemically through blood to elicit prolonged metabolic adaptations."),

    # 80: Diabetes Mellitus: Type 1 vs Type 2
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Type 1 Box -->
  <rect x="25" y="25" width="165" height="140" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
  <text x="107" y="48" fill="#ef4444" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Type 1 Diabetes</text>
  <text x="107" y="72" fill="#fca5a5" font-size="9" font-family="sans-serif" text-anchor="middle">- Autoimmune beta-cell destruction</text>
  <text x="107" y="92" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Absolute lack of insulin</text>
  <text x="107" y="112" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Onset: Usually children/juveniles</text>
  <text x="107" y="132" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">- Treatment: Daily insulin injections</text>
  <!-- Type 2 Box -->
  <rect x="210" y="25" width="165" height="140" rx="6" fill="#1e293b" stroke="#eab308" stroke-width="2"/>
  <text x="292" y="48" fill="#eab308" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Type 2 Diabetes</text>
  <text x="292" y="72" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle">- Peripheral insulin resistance</text>
  <text x="292" y="92" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Target cells fail to respond to insulin</text>
  <text x="292" y="112" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Onset: Usually adults, lifestyle link</text>
  <text x="292" y="132" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">- Treatment: Diet, exercise, metformin</text>
</svg>
</div>
What fundamental pathophysiological difference differentiates Type 1 Diabetes from Type 2 Diabetes?""""",
     ["Type 1 involves autoimmune destruction of beta cells causing absolute insulin deficiency, whereas Type 2 primarily involves target tissue insulin resistance",
      "Type 1 is caused by eating too much table salt",
      "Type 2 only affects the brain while Type 1 affects the feet",
      "Type 1 can be cured by drinking plain water"],
     "A", "OSC", "hard",
     "Type 1 diabetes is mediated by T-cell autoimmune destruction of beta cells, producing zero endogenous insulin; Type 2 is driven by progressive insulin receptor insensitivity compounded by secretory dysfunction."),

    # 81: Pineal Gland & Melatonin Circadian Rhythm
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#111827"/>
  <!-- Daytime Phase -->
  <rect x="30" y="30" width="150" height="130" rx="6" fill="#1f2937" stroke="#facc15" stroke-width="2"/>
  <circle cx="105" cy="60" r="14" fill="#facc15"/>
  <text x="105" y="90" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Daylight (Sunlight)</text>
  <text x="105" y="110" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">SCN inhibits Pineal</text>
  <text x="105" y="130" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Melatonin LOW (Alert)</text>
  <!-- Nighttime Phase -->
  <rect x="220" y="30" width="150" height="130" rx="6" fill="#1f2937" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="295" cy="60" r="14" fill="#38bdf8"/>
  <text x="295" y="90" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Darkness (Night)</text>
  <text x="295" y="110" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">Pineal actively secretes</text>
  <text x="295" y="130" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Melatonin HIGH (Sleep)</text>
</svg>
</div>
Why does looking at bright smartphone or tablet screens late at night disrupt normal sleep onset?""",
     ["Blue light from screens stimulates retinal ganglion cells, suppressing pineal melatonin synthesis and delaying sleep readiness",
      "Screens emit radiation that permanently destroys the thyroid gland",
      "Screen light cools the brain down to freezing",
      "Electronic screens absorb red blood cells from the eyes"],
     "A", "OSC", "medium",
     "Short-wavelength blue light stimulates melanopsin-containing intrinsically photosensitive retinal ganglion cells, signalling the SCN to halt pineal melatonin secretion and causing circadian insomnia."),

    # 82: Iodine Deficiency & Simple Goitre Mechanism
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Step 1 -->
  <rect x="20" y="30" width="105" height="40" rx="4" fill="#27272a" stroke="#ef4444" stroke-width="2"/>
  <text x="72" y="47" fill="#ef4444" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Low Dietary Iodine</text>
  <text x="72" y="60" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Thyroxine (T4) drops</text>
  <line x1="125" y1="50" x2="155" y2="50" stroke="#f87171" stroke-width="2"/>
  <!-- Step 2 -->
  <rect x="155" y="30" width="105" height="40" rx="4" fill="#27272a" stroke="#facc15" stroke-width="2"/>
  <text x="207" y="47" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">No Negative Feedback</text>
  <text x="207" y="60" fill="#fef08a" font-size="8" font-family="sans-serif" text-anchor="middle">Pituitary fires high TSH</text>
  <line x1="260" y1="50" x2="290" y2="50" stroke="#facc15" stroke-width="2"/>
  <!-- Step 3 -->
  <rect x="290" y="30" width="95" height="40" rx="4" fill="#27272a" stroke="#ec4899" stroke-width="2"/>
  <text x="337" y="47" fill="#ec4899" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Chronic TSH Surge</text>
  <text x="337" y="60" fill="#f472b6" font-size="8" font-family="sans-serif" text-anchor="middle">Hypertrophy</text>
  <!-- Result Box -->
  <rect x="60" y="105" width="280" height="55" rx="6" fill="#831843" stroke="#f43f5e" stroke-width="2"/>
  <text x="200" y="127" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Thyroid Follicles Swell Enormously</text>
  <text x="200" y="146" fill="#fbcfe8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Visible Enlargement: Simple Goitre in Neck!</text>
</svg>
</div>
Why does a deficiency of dietary iodine lead to massive visible enlargement of the thyroid gland (simple goitre)?""""",
     ["Without iodine, thyroxine synthesis drops; the absence of negative feedback causes the anterior pituitary to continuously secrete elevated TSH, stimulating thyroid follicular hypertrophy",
      "Iodine deficiency causes bacterial infection inside the throat",
      "The thyroid absorbs table salt from the air to replace iodine",
      "Lack of iodine freezes the neck muscles into hard stone"],
     "A", "OSC", "medium",
     "Low thyroxine levels eliminate negative feedback suppression at the pituitary; persistently high TSH levels relentlessly stimulate thyroid follicular cell proliferation and colloid production, expanding the gland into a goitre.")
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

output_path = os.path.join(os.path.dirname(__file__), "ch15_topic5.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
