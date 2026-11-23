// scripts/patch_part_a.js
const fs = require('fs');

let content = fs.readFileSync('scripts/build_cbse9_scie_ch12_part_a.py', 'utf8');

// 1. Line 226
content = content.replace(
  `f"**Step 1:** Complete taxonomy of humans:\\n- Kingdom: Animalia\\n- Phylum: Chordata (presence of notochord/backbone)\\n- Class: Mammalia (mammary glands, hair)\\n- Order: Primates (stereoscopic vision, grasping hands)\\n- Family: Hominidae\\n- Genus: Homo\\n- Species: sapiens.\\n\\n**Step 2:** Correct answer is '{item[0]}'."`,
  `f"**Step 1:** Complete taxonomy of humans:\\n- Kingdom: Animalia\\n- Phylum: Chordata (presence of notochord/backbone)\\n- Class: Mammalia (mammary glands, hair)\\n- Order: Primates (stereoscopic vision, grasping hands)\\n- Family: Hominidae\\n- Genus: Homo\\n- Species: sapiens.\\n\\n**Step 2:** Note that each taxonomic category specifies an increasingly refined group of anatomical and evolutionary traits.\\n\\n**Step 3:** Correct answer is '{item[0]}'."`
);

// 2. Line 322: Arch 2
content = content.replace(
  `f"**Step 1:** Universal rules of binomial nomenclature:\\n1. Biological names are derived from Latin and printed in italics.\\n2. The first word is the Genus (begins with a capital letter); the second word is the Species (begins with a lowercase letter).\\n3. When handwritten, both words must be underlined separately to indicate their Latin origin.\\n\\n**Step 2:** Correct answer is '{item[0]}'."`,
  `f"**Step 1:** Universal rules of binomial nomenclature:\\n1. Biological names are derived from Latin and printed in italics.\\n2. The first word is the Genus (begins with a capital letter); the second word is the Species (begins with a lowercase letter).\\n3. When handwritten, both words must be underlined separately to indicate their Latin origin.\\n\\n**Step 2:** These standardized international naming rules eliminate ambiguity across different world languages.\\n\\n**Step 3:** Correct answer is '{item[0]}'."`
);

// 3. Arch 3
content = content.replace(
  `            ("Mangifera indica", "Mangifera Indica; mangifera indica; Mangifera-indica"),
            ("Pisum sativum", "Pisum Sativum; pisum sativum; Pisum sativus"),
            ("Triticum aestivum", "Triticum Aestivum; triticum aestivum; Oryza sativa"),
            ("Ficus benghalensis", "Ficus Benghalensis; ficus religiosa; Azadirachta indica")`,
  `            ("Mangifera indica", "Pisum sativum; Triticum aestivum; Ficus benghalensis"),
            ("Pisum sativum", "Mangifera indica; Triticum aestivum; Oryza sativa"),
            ("Triticum aestivum", "Oryza sativa; Zea mays; Solanum tuberosum"),
            ("Ficus benghalensis", "Ficus religiosa; Azadirachta indica; Mangifera indica")`
);
content = content.replace(
  `f"**Step 1:** Common plant scientific names:\\n- Mango: *Mangifera indica*\\n- Garden pea: *Pisum sativum*\\n- Wheat: *Triticum aestivum*\\n- Banyan tree: *Ficus benghalensis*\\n\\n**Step 2:** Note that the genus begins with a capital letter and species with a lowercase letter, printed in italics. Correct name is '{item[0]}'."`,
  `f"**Step 1:** Common plant scientific names:\\n- Mango: *Mangifera indica*\\n- Garden pea: *Pisum sativum*\\n- Wheat: *Triticum aestivum*\\n- Banyan tree: *Ficus benghalensis*\\n\\n**Step 2:** Note that the genus begins with a capital letter and species with a lowercase letter, printed in italics.\\n\\n**Step 3:** Hence, the correct scientific name is '{item[0]}'."`
);

// 4. Arch 4
content = content.replace(
  `            ("Homo sapiens", "Homo Sapiens; homo sapiens; Homo-sapiens"),
            ("Panthera tigris", "Panthera Tigris; panthera tigris; Panthera leo"),
            ("Rana tigrina (Hoplobatrachus tigerinus)", "Bufo melanostictus; Rana temporaria; Hyla versicolor"),
            ("Musca domestica", "Musca Domestica; musca domestica; Periplaneta americana")`,
  `            ("Homo sapiens", "Panthera tigris; Rana tigrina; Musca domestica"),
            ("Panthera tigris", "Panthera leo; Canis familiaris; Felis catus"),
            ("Rana tigrina (Hoplobatrachus tigerinus)", "Bufo melanostictus; Rana temporaria; Hyla versicolor"),
            ("Musca domestica", "Periplaneta americana; Apis mellifera; Anopheles stephensi")`
);
content = content.replace(
  `f"**Step 1:** Common animal scientific names:\\n- Human: *Homo sapiens*\\n- Tiger: *Panthera tigris*\\n- Lion: *Panthera leo*\\n- Frog: *Rana tigrina*\\n- Housefly: *Musca domestica*\\n\\n**Step 2:** Correct name is '{item[0]}'."`,
  `f"**Step 1:** Common animal scientific names:\\n- Human: *Homo sapiens*\\n- Tiger: *Panthera tigris*\\n- Lion: *Panthera leo*\\n- Frog: *Rana tigrina*\\n- Housefly: *Musca domestica*\\n\\n**Step 2:** Scientific binominal names strictly follow the Genus species format.\\n\\n**Step 3:** Therefore, the correct scientific name is '{item[0]}'."`
);

// 5. Arch 6
content = content.replace(
  `            ("Allium cepa", "Allium Cepa; allium cepa; Allium sativum"),`,
  `            ("Allium cepa", "Allium sativum; Solanum melongena; Brassica oleracea"),`
);
content = content.replace(
  `f"**Step 1:** Common names cause immense confusion because: (1) They vary across regions and languages (e.g. onion is called pyaaz, kanda, ulli, cebolla), (2) The same name may denote different organisms in different countries, (3) Misleading names exist (e.g. jellyfish, starfish, silverfish are not true fishes).\\n\\n**Step 2:** Binomial nomenclature provides a unique, universal name across all countries. Correct answer is '{item[0]}'."`,
  `f"**Step 1:** Common names cause immense confusion because: (1) They vary across regions and languages (e.g. onion is called pyaaz, kanda, ulli, cebolla), (2) The same name may denote different organisms in different countries, (3) Misleading names exist (e.g. jellyfish, starfish, silverfish are not true fishes).\\n\\n**Step 2:** Binomial nomenclature provides a unique, universal name across all countries.\\n\\n**Step 3:** Correct answer is '{item[0]}'."`
);

// 6. Arch 8
content = content.replace(
  `            ("The genus name must start with a capital letter (Homo) and species name must start with lowercase (sapiens): Homo sapiens", "It should be Homo Sapiens; It should be written in French; The name should be three words"),
            ("Solanum tuberosum (printed in italics, genus capitalized, species lowercase)", "Solanum Tuberosum; solanum tuberosum; Solanum-tuberosum"),
            ("Panthera leo", "panthera Leo; Panthera Leo; panthera leo"),
            ("Because the genus name 'Panthera' must begin with a capital letter and species name 'leo' must begin with a lowercase letter", "Because Leo should be Greek; Because lions are not mammals; Because it lacks an underline in print")`,
  `            ("The genus name must start with a capital letter (Homo) and species name must start with lowercase (sapiens): Homo sapiens", "Both genus and species names must start with uppercase capital letters; The name should be written in French with accent marks; The generic name must be hyphenated with the specific epithet"),
            ("Solanum tuberosum (printed in italics, genus capitalized, species lowercase)", "Solanum Tuberosum (both genus and species capitalized); solanum tuberosum (both written in lowercase without capital); Solanum-tuberosum (words joined by an invalid hyphen)"),
            ("Panthera leo (capital P, lowercase l, printed in italics)", "panthera Leo (lowercase p, capital L); Panthera Leo (capital P, capital L); panthera leo (all lowercase letters without capital)"),
            ("Because the genus name 'Panthera' must begin with a capital letter and species name 'leo' must begin with a lowercase letter", "Because Leo should be Greek rather than Latin; Because lions are not classified within Kingdom Animalia; Because specific epithets require three capital letters")`
);
content = content.replace(
  `f"**Step 1:** Rules of binomial formatting:\\n- Genus starts with a CAPITAL letter.\\n- Species starts with a LOWERCASE letter.\\n- Italicized in print or underlined separately when handwritten.\\n\\n**Step 2:** Therefore, *Panthera leo* and *Solanum tuberosum* are strictly correct. Correct answer is '{item[0]}'."`,
  `f"**Step 1:** Rules of binomial formatting:\\n- Genus starts with a CAPITAL letter.\\n- Species starts with a LOWERCASE letter.\\n- Italicized in print or underlined separately when handwritten.\\n\\n**Step 2:** These typographic rules ensure taxonomic precision across scientific literature.\\n\\n**Step 3:** Correct answer is '{item[0]}'."`
);

// 7. Line 616
content = content.replace(
  `f"**Step 1:** Identify the combination of cell type, cell wall, and nutrition:\\n- Prokaryotic unicellular → Monera\\n- Eukaryotic unicellular → Protista\\n- Eukaryotic multicellular with chitin cell wall + heterotrophic → Fungi\\n- Eukaryotic multicellular with cellulose wall + autotrophic → Plantae\\n- Eukaryotic multicellular with NO cell wall + ingestive heterotrophic → Animalia.\\n\\n**Step 2:** Correct kingdom is '{item[0]}'."`,
  `f"**Step 1:** Identify the combination of cell type, cell wall, and nutrition:\\n- Prokaryotic unicellular → Monera\\n- Eukaryotic unicellular → Protista\\n- Eukaryotic multicellular with chitin cell wall + heterotrophic → Fungi\\n- Eukaryotic multicellular with cellulose wall + autotrophic → Plantae\\n- Eukaryotic multicellular with NO cell wall + ingestive heterotrophic → Animalia.\\n\\n**Step 2:** Note the presence or absence of a peptidoglycan/cellulose/chitin cell wall and mode of nutrition.\\n\\n**Step 3:** Correct kingdom is '{item[0]}'."`
);

// 8. Line 822
content = content.replace(
  `f"**Step 1:** Evolutionary sequence of the Plant Kingdom:\\n1. Thallophyta: non-differentiated body, non-vascular, aquatic spores.\\n2. Bryophyta: differentiated body, non-vascular, amphibious spores.\\n3. Pteridophyta: differentiated, vascular, non-seed spores.\\n4. Gymnosperms: differentiated, vascular, naked seeds in cones.\\n5. Angiosperms: differentiated, vascular, covered seeds in fruits with flowers.\\n\\n**Step 2:** Correct answer is '{item[0]}'."`,
  `f"**Step 1:** Evolutionary sequence of the Plant Kingdom:\\n1. Thallophyta: non-differentiated body, non-vascular, aquatic spores.\\n2. Bryophyta: differentiated body, non-vascular, amphibious spores.\\n3. Pteridophyta: differentiated, vascular, non-seed spores.\\n4. Gymnosperms: differentiated, vascular, naked seeds in cones.\\n5. Angiosperms: differentiated, vascular, covered seeds in fruits with flowers.\\n\\n**Step 2:** This evolutionary progression reflects increasing adaptation to terrestrial life.\\n\\n**Step 3:** Correct answer is '{item[0]}'."`
);

fs.writeFileSync('scripts/build_cbse9_scie_ch12_part_a.py', content, 'utf8');
console.log('Successfully patched build_cbse9_scie_ch12_part_a.py');
