const path = require('path');
const fs = require('fs');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[key] = val;
      }
    }
  });
}

const admin = require('firebase-admin');
const credential = JSON.parse(
  process.env.FIREBASE_SERVICE_ACCOUNT_KEY.startsWith('{')
    ? process.env.FIREBASE_SERVICE_ACCOUNT_KEY
    : Buffer.from(process.env.FIREBASE_SERVICE_ACCOUNT_KEY, 'base64').toString('utf-8')
);
if (!admin.apps.length) {
  admin.initializeApp({
    credential: admin.credential.cert(credential)
  });
}
const db = admin.firestore();

// --- 1. CHAPTER 9 REPLACEMENTS (54 Questions) ---
const ch9Replacements = {
  // Topic 9.1: Weather and Climate
  'MH-9-SCIT-9-9.1-OAR-031': {
    text: "Assertion (A): Climate does not change continuously like daily weather; it remains stable over a long period.\nReason (R): Climate is determined by averaging atmospheric conditions over a minimum baseline period of 30 consecutive years.",
    options: ["Both A and R are true, and R is the correct explanation of A", "Both A and R are true, but R is not the correct explanation of A", "A is true, but R is false", "A is false, but R is true"],
    correctAnswer: "A",
    solution: "Weather describes short-term atmospheric states that can change hourly, whereas climate is the long-term pattern calculated over 30 or more years.",
    type: "OAR"
  },
  'MH-9-SCIT-9-9.1-OAR-063': {
    text: "Assertion (A): Coastal regions experience an equable climate with little variation between daytime and nighttime temperatures.\nReason (R): Large water bodies heat up and cool down slowly compared to land, moderating coastal air temperatures.",
    options: ["Both A and R are true, and R is the correct explanation of A", "Both A and R are true, but R is not the correct explanation of A", "A is true, but R is false", "A is false, but R is true"],
    correctAnswer: "A",
    solution: "Because water has a high specific heat capacity, coastal areas enjoy moderate, equable climates unlike continental interiors.",
    type: "OAR"
  },
  'MH-9-SCIT-9-9.1-OFB-036': {
    text: "Fill in the blank: World Meteorological Day is celebrated globally every year on ________ March.",
    options: ["23rd", "15th", "5th", "28th"],
    correctAnswer: "A",
    solution: "World Meteorological Day is observed worldwide on 23rd March to commemorate the establishment of the World Meteorological Organization.",
    type: "OFB"
  },
  'MH-9-SCIT-9-9.1-OFB-065': {
    text: "Fill in the blank: The atmospheric condition at a specific place and specific time for a short duration is called ________.",
    options: ["weather", "climate", "monsoon", "season"],
    correctAnswer: "A",
    solution: "Weather refers to short-term atmospheric conditions (sunny, rainy, cloudy, windy) observed at a particular time and place.",
    type: "OFB"
  },
  'MH-9-SCIT-9-9.1-ONE-037': {
    text: "According to the World Meteorological Organization, climate of a region is determined by averaging weather records over how many minimum years?",
    options: ["30", "10", "5", "50"],
    correctAnswer: "A",
    solution: "A standard climate baseline requires continuous weather observation records over a minimum period of 30 consecutive years.",
    type: "ONE"
  },
  'MH-9-SCIT-9-9.1-ONE-040': {
    text: "If a region receives 120 mm of rain in June, 240 mm in July, 180 mm in August, and 60 mm in September, what is the total monsoon rainfall in millimeters?",
    options: ["600", "500", "480", "550"],
    correctAnswer: "A",
    solution: "Total rainfall = 120 + 240 + 180 + 60 = 600 mm.",
    type: "ONE"
  },
  'MH-9-SCIT-9-9.1-ONE-069': {
    text: "World Meteorological Day is celebrated on which date of March?",
    options: ["23", "21", "28", "15"],
    correctAnswer: "A",
    solution: "World Meteorological Day is celebrated on March 23rd every year.",
    type: "ONE"
  },
  'MH-9-SCIT-9-9.1-OSC-002': {
    text: "Which instrument is used at meteorological observatories to measure atmospheric pressure?",
    options: ["Barometer", "Thermometer", "Rain gauge", "Anemometer"],
    correctAnswer: "A",
    solution: "A barometer is the standard instrument used to measure atmospheric pressure.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.1-OSC-010': {
    text: "Which abiotic factor has the greatest influence on biodiversity and living organisms in a geographic region?",
    options: ["Climate", "Soil color", "Elevation alone", "Ocean salinity alone"],
    correctAnswer: "A",
    solution: "According to the textbook, of all abiotic factors affecting biodiversity, climate is by far the most important.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.1-OSC-012': {
    text: "Which of the following is NOT an element or factor that constitutes daily weather?",
    options: ["Soil mineral composition", "Atmospheric temperature", "Relative humidity", "Wind speed and direction"],
    correctAnswer: "A",
    solution: "Weather elements include temperature, atmospheric pressure, sunlight, clouds, humidity, rainfall, and wind. Soil mineral composition is a lithospheric property.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.1-OSC-017': {
    text: "What is the primary difference between 'weather' and 'climate'?",
    options: ["Weather is for short duration while climate is an average over a long period", "Weather never changes while climate changes daily", "Weather covers entire continents while climate covers a small city", "There is no difference between them"],
    correctAnswer: "A",
    solution: "Weather reflects short-term atmospheric conditions of a specific place, whereas climate is the long-term average over at least 30 years.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.1-OSC-055': {
    text: "Which instrument is used to measure the amount of rainfall received in a region?",
    options: ["Rain gauge", "Barometer", "Hygrometer", "Thermometer"],
    correctAnswer: "A",
    solution: "A rain gauge (or udometer) is used at weather observatories to measure rainfall depth in millimeters.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.1-OSC-073': {
    text: "Why is climate considered a crucial factor in planning human occupations and infrastructure?",
    options: ["It determines agricultural crop patterns, shelter designs, and seasonal activities", "It decides the color of houses", "It determines the language spoken by people", "It has no influence on human activities"],
    correctAnswer: "A",
    solution: "Climate directly determines suitable crops, clothing, housing architecture, transport, and economic occupations in any region.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.1-OSC-079': {
    text: "When air rises upon heating over a landmass, what kind of pressure area is formed?",
    options: ["Low pressure area", "High pressure area", "Zero pressure area", "Atmospheric vacuum"],
    correctAnswer: "A",
    solution: "When air heats up, it expands, becomes less dense, and rises, creating a localized low-pressure zone.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.1-OSC-080': {
    text: "In which year was the India Meteorological Department (IMD) established by the British government?",
    options: ["1875", "1947", "1905", "1950"],
    correctAnswer: "A",
    solution: "The India Meteorological Department (IMD) was founded in 1875 with its initial main observatory at Shimla.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.1-OTF-026': {
    text: "True or False: Climate changes continuously from hour to hour throughout a single day.",
    options: ["True", "False"],
    correctAnswer: "B",
    solution: "False. Weather changes continuously within a day (e.g. morning sunny, afternoon rainy), whereas climate remains stable over decades.",
    type: "OTF"
  },

  // Topic 9.2: Meteorology & IMD
  'MH-9-SCIT-9-9.2-OSC-008': {
    text: "Where is the head office of the India Meteorological Department (IMD) located?",
    options: ["New Delhi and Pune", "Bengaluru", "Nagpur", "Hyderabad"],
    correctAnswer: "A",
    solution: "IMD's central administrative headquarters is in New Delhi and its primary meteorological meteorological division is in Pune.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.2-OSC-014': {
    text: "Who developed the first statistical model for monsoon forecasting in India based on global weather parameters?",
    options: ["Sir Gilbert Walker", "Dr. Vasant Gowarikar", "Dr. Homi Bhabha", "Dr. APJ Abdul Kalam"],
    correctAnswer: "A",
    solution: "Sir Gilbert Walker, head of IMD in the 1930s, first discovered statistical links between global atmospheric patterns and Indian monsoon rainfall.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.2-OSC-046': {
    text: "In 1989, a modern parametric monsoon forecasting model based on 16 worldwide parameters was developed under the leadership of which renowned Indian scientist?",
    options: ["Dr. Vasant Gowarikar", "Sir Gilbert Walker", "Dr. Vikram Sarabhai", "Dr. C.V. Raman"],
    correctAnswer: "A",
    solution: "Dr. Vasant Gowarikar developed the 16-parameter monsoon forecasting model for IMD in 1989.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.2-OSC-049': {
    text: "Which Indian satellite series is utilized by IMD for high-resolution cloud imagery and weather monitoring?",
    options: ["INSAT and GSAT", "Aryabhata", "Rohini", "Chandrayaan"],
    correctAnswer: "A",
    solution: "Geostationary satellites of the INSAT and GSAT series provide continuous meteorological observations and cyclone tracking over the Indian subcontinent.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.2-OTF-025': {
    text: "True or False: The India Meteorological Department (IMD) provides specialized agricultural advisories to help farmers plan sowing and harvesting.",
    options: ["True", "False"],
    correctAnswer: "A",
    solution: "True. IMD issues regular Gramin Krishi Mausam bulletins to assist farmers with weather-based crop management.",
    type: "OTF"
  },

  // Topic 9.3: Solid Waste Management (Replaces all college engineering/phytoremediation questions!)
  'MH-9-SCIT-9-9.3-OAR-029': {
    text: "Assertion (A): Earthworms are called the farmer's best friends in waste management.\nReason (R): Earthworms convert wet organic waste into nutrient-rich vermicompost fertilizer.",
    options: ["Both A and R are true, and R is the correct explanation of A", "Both A and R are true, but R is not the correct explanation of A", "A is true, but R is false", "A is false, but R is true"],
    correctAnswer: "A",
    solution: "Earthworms decompose organic kitchen and farm waste, producing high-grade natural compost that enriches soil fertility.",
    type: "OAR"
  },
  'MH-9-SCIT-9-9.3-OFB-031': {
    text: "Fill in the blank: Kitchen leftovers, vegetable peels, and spoiled fruits are examples of ________ waste.",
    options: ["biodegradable", "non-biodegradable", "hazardous", "electronic"],
    correctAnswer: "A",
    solution: "Kitchen waste decomposes naturally by microbial action and is classified as biodegradable (wet) waste.",
    type: "OFB"
  },
  'MH-9-SCIT-9-9.3-OFB-033': {
    text: "Fill in the blank: The process of decomposing organic kitchen waste in pits using earthworms is called ________.",
    options: ["vermicomposting", "incineration", "landfilling", "pyrolysis"],
    correctAnswer: "A",
    solution: "Vermicomposting uses earthworms to break down wet solid waste into nutrient-dense vermicompost.",
    type: "OFB"
  },
  'MH-9-SCIT-9-9.3-OFB-035': {
    text: "Fill in the blank: Under the 7 principles of solid waste management, refusing to buy single-use plastic carry bags represents the principle of ________.",
    options: ["Refuse", "Recycle", "Reuse", "Rethink"],
    correctAnswer: "A",
    solution: "Saying 'no' to single-use plastics and disposable articles is an example of the 'Refuse' principle.",
    type: "OFB"
  },
  'MH-9-SCIT-9-9.3-OFB-068': {
    text: "Fill in the blank: Biomedical hospital waste like used syringes and bandages must be treated by controlled ________ to destroy infectious germs.",
    options: ["incineration", "composting", "vermicomposting", "open dumping"],
    correctAnswer: "A",
    solution: "Controlled high-temperature incineration destroys dangerous disease-causing pathogens in hospital biomedical waste.",
    type: "OFB"
  },
  'MH-9-SCIT-9-9.3-OMC-023': {
    text: "Which of the following materials are classified as 'Biodegradable (Wet) Waste'? (Select all that apply)",
    options: ["Vegetable peels and rotten fruits", "Leftover cooked food", "Plastic carry bags", "Dry fallen leaves"],
    correctAnswer: ["A", "B", "D"],
    solution: "Plant matter, food leftovers, and vegetable peelings decompose naturally and are biodegradable. Plastic bags are non-biodegradable.",
    type: "OMC"
  },
  'MH-9-SCIT-9-9.3-OMC-058': {
    text: "Which of the following are included in the '7 Rs' of Solid Waste Management? (Select all that apply)",
    options: ["Reduce", "Reuse", "Recycle", "Rethink"],
    correctAnswer: ["A", "B", "C", "D"],
    solution: "The 7 Rs include Rethink, Refuse, Reduce, Reuse, Recycle, Regulate/Public awareness, and Research.",
    type: "OMC"
  },
  'MH-9-SCIT-9-9.3-ONE-039': {
    text: "How many basic principles (Rs) are emphasized in standard solid waste management curricula?",
    options: ["7", "3", "5", "10"],
    correctAnswer: "A",
    solution: "There are 7 principles of solid waste management: Rethink, Refuse, Reduce, Reuse, Recycle, Regulate, and Research.",
    type: "ONE"
  },
  'MH-9-SCIT-9-9.3-ONE-070': {
    text: "If a household generates 2 kg of wet organic waste every day, how many kilograms of wet waste are produced in a month of 30 days?",
    options: ["60", "30", "90", "120"],
    correctAnswer: "A",
    solution: "Total waste generated = 2 kg/day * 30 days = 60 kg.",
    type: "ONE"
  },
  'MH-9-SCIT-9-9.3-OSC-002': {
    text: "Which of the following is an example of non-biodegradable waste that takes hundreds of years to decompose?",
    options: ["Plastic bottle", "Banana peel", "Cotton cloth", "Cardboard box"],
    correctAnswer: "A",
    solution: "Plastic bottles resist biological decomposition and persist in the environment for hundreds to thousands of years.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-003': {
    text: "What color bin is internationally recommended for collecting wet, biodegradable kitchen waste in household segregation?",
    options: ["Green bin", "Blue bin", "Red bin", "Yellow bin"],
    correctAnswer: "A",
    solution: "Green bins are designated for biodegradable wet waste, while Blue bins are designated for dry recyclable waste.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-004': {
    text: "Why should discarded medical syringes, cotton swabs, and expired medicines never be mixed with household garbage?",
    options: ["They contain infectious pathogens and toxic chemicals that spread disease", "They cause vegetables to rot faster", "They dissolve easily in water", "They make composting too sweet"],
    correctAnswer: "A",
    solution: "Biomedical waste contains hazardous disease-causing pathogens and must be collected and incinerated separately.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-005': {
    text: "Approximately how long does a natural banana peel take to decompose completely in soil?",
    options: ["3 to 4 weeks", "100 years", "10 days", "5 years"],
    correctAnswer: "A",
    solution: "According to the textbook waste degradation table, a banana peel degrades naturally in 3 to 4 weeks.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-008': {
    text: "Which of the following materials takes the longest time to degrade in the environment?",
    options: ["Thermocol (expanded polystyrene)", "Cotton cloth", "Wood piece", "Tin can"],
    correctAnswer: "A",
    solution: "Thermocol takes centuries or an infinite period to decompose, making it an extremely hazardous non-biodegradable pollutant.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-012': {
    text: "What is the primary benefit of making compost from household kitchen waste?",
    options: ["It produces nutrient-rich organic manure while reducing municipal garbage", "It generates plastic bags", "It prevents rain from falling", "It hardens the soil into concrete"],
    correctAnswer: "A",
    solution: "Composting converts biodegradable waste into organic humus, enriching garden and farm soil naturally without chemicals.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-013': {
    text: "What type of waste includes old mobile phones, broken television sets, and damaged computer components?",
    options: ["E-waste (Electronic waste)", "Biomedical waste", "Domestic wet waste", "Agricultural waste"],
    correctAnswer: "A",
    solution: "Discarded electrical and electronic devices are classified as E-waste.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-018': {
    text: "Using cloth bags repeatedly for grocery shopping instead of single-use polythene bags is an example of which waste management principle?",
    options: ["Reuse", "Incinerate", "Discard", "Landfill"],
    correctAnswer: "A",
    solution: "Reusing durable cloth bags eliminates the need for disposable plastic carry bags, illustrating the 'Reuse' principle.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-046': {
    text: "What is the primary objective of 'source segregation' in city solid waste management?",
    options: ["Separating wet and dry waste at the household level before collection", "Burning all garbage on the road", "Dumping everything into rivers", "Burying mixed waste in playgrounds"],
    correctAnswer: "A",
    solution: "Source segregation means separating wet biodegradable waste from dry recyclable waste at home before handing it over to municipal collectors.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-048': {
    text: "Which eco-friendly method uses microorganisms and earthworms together to convert organic waste into superior quality organic manure?",
    options: ["Vermicomposting", "Open dumping", "River disposal", "Roadside burning"],
    correctAnswer: "A",
    solution: "Vermicomposting utilizes earthworms to digest and convert organic waste into rich vermicompost manure.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-049': {
    text: "Why is open dumping and burning of municipal solid waste harmful to the environment?",
    options: ["It releases toxic poisonous smoke and foul odors while polluting groundwater", "It increases soil fertility", "It cleans the atmosphere", "It reduces global temperatures"],
    correctAnswer: "A",
    solution: "Open burning of mixed garbage releases harmful smoke, carbon monoxide, and toxic gases, causing severe air and water pollution.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-051': {
    text: "Which of the following wastes is classified as 'Hazardous Waste'?",
    options: ["Radioactive materials and toxic industrial chemicals", "Vegetable peelings", "Old newspapers", "Fallen tree twigs"],
    correctAnswer: "A",
    solution: "Radioactive isotopes and corrosive industrial chemicals are categorized as hazardous wastes due to their extreme danger.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-053': {
    text: "What is the most effective and eco-friendly way for citizens to manage wet kitchen waste at home?",
    options: ["Composting in a small compost pit or balcony compost bin", "Throwing it into the sewer line", "Dumping it in open plastic bags", "Burning it on the pavement"],
    correctAnswer: "A",
    solution: "Composting kitchen scraps in a home compost bin converts wet waste into valuable manure and prevents garbage pileups in cities.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-054': {
    text: "Which type of solid waste takes approximately 50 to 100 years to degrade in soil?",
    options: ["Tin cans", "Banana peels", "Newspapers", "Cotton rags"],
    correctAnswer: "A",
    solution: "According to the Balbharti textbook, metal tin cans take between 50 to 100 years to decompose naturally.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-071': {
    text: "Why are sanitary landfills lined at the bottom before solid waste is deposited?",
    options: ["To prevent polluted toxic liquid (leachate) from seeping into underground water", "To make the pit look attractive", "To help grass grow on garbage", "To keep the garbage dry and warm"],
    correctAnswer: "A",
    solution: "Lining landfill pits prevents contaminated liquid run-off (leachate) from percolating down and contaminating the groundwater table.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-073': {
    text: "Under the principle of 'Recycle', which of the following waste materials can be processed to create fresh paper products?",
    options: ["Old newspapers and discarded notebooks", "Broken glass bottles", "Banana peelings", "Used engine oil"],
    correctAnswer: "A",
    solution: "Used newspapers and paper notebooks are pulped and recycled into fresh paper and cardboard items.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-079': {
    text: "Which administrative rule should citizens follow regarding disposable carry bags to protect city drainage systems?",
    options: ["Use cloth or jute bags and avoid thin single-use plastic bags", "Throw plastic bags into open gutters", "Burn all plastic bags inside houses", "Use only thin plastic bags once and discard"],
    correctAnswer: "A",
    solution: "Using reusable cloth or jute bags prevents plastic from clogging city storm drains and causing urban flooding.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OSC-080': {
    text: "What does the 'Rethink' principle in solid waste management encourage us to do?",
    options: ["Re-evaluate our purchasing habits and lifestyle choices to minimize waste", "Buy more disposable plastic items", "Throw garbage without separating it", "Stop using dustbins"],
    correctAnswer: "A",
    solution: "The 'Rethink' principle asks us to rethink our daily consumer habits and actively choose products that generate minimal waste.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.3-OTF-026': {
    text: "True or False: Vermicompost produced using earthworms is richer in essential plant nutrients than ordinary uncomposted soil.",
    options: ["True", "False"],
    correctAnswer: "A",
    solution: "True. Earthworm digestion enriches organic waste with readily absorbable minerals, nitrogen, phosphorus, and potassium.",
    type: "OTF"
  },
  'MH-9-SCIT-9-9.3-OTF-059': {
    text: "True or False: Discarded plastic carry bags decompose naturally within 2 to 3 weeks.",
    options: ["True", "False"],
    correctAnswer: "B",
    solution: "False. Plastic carry bags are non-biodegradable and persist in nature for hundreds of years (up to 10 lakh years).",
    type: "OTF"
  },
  'MH-9-SCIT-9-9.3-OTF-061': {
    text: "True or False: Biodegradable waste can be safely composted to produce organic fertilizer.",
    options: ["True", "False"],
    correctAnswer: "A",
    solution: "True. Biodegradable wet waste breaks down naturally into nutrient-rich compost suitable for gardening and farming.",
    type: "OTF"
  },

  // Topic 9.4: Disaster Management & First Aid
  'MH-9-SCIT-9-9.4-OSC-004': {
    text: "What is the very first and most essential step in the immediate first aid care of a burn injury?",
    options: ["Hold the burned area under clean, cold running tap water for 10-15 minutes", "Apply thick cooking oil or butter immediately", "Pop any blisters that form with a pin", "Cover the burn tightly with wool"],
    correctAnswer: "A",
    solution: "Immediate cooling with clean running tap water stops heat from damaging deeper tissues and relieves severe pain.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.4-OSC-072': {
    text: "In the first-aid treatment of muscle sprains or ligament strains, what does the 'I' in the RICE principle represent?",
    options: ["Ice pack application to reduce pain and swelling", "Immediate running", "Injection administration", "Incision of the skin"],
    correctAnswer: "A",
    solution: "RICE stands for Rest, Ice application, Compression bandage, and Elevation of the injured joint.",
    type: "OSC"
  },
  'MH-9-SCIT-9-9.4-OTF-059': {
    text: "True or False: Burn blisters should be intentionally burst with a needle to let the fluid out.",
    options: ["True", "False"],
    correctAnswer: "B",
    solution: "False. Blisters act as a sterile protective barrier against infection; popping them exposes raw skin to bacterial contamination.",
    type: "OTF"
  }
};

console.log(`Defined ${Object.keys(ch9Replacements).length} clean Balbharti textbook replacements for Chapter 9.`);

// Export or run
module.exports = { ch9Replacements };
