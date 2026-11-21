import sys, os, json
sys.path.insert(0, os.path.abspath("."))
from scripts.generate_ch5_all import gen_5_1_1, gen_5_1_2

qs = gen_5_1_1() + gen_5_1_2()
with open("scripts/mh9_mth2_ch5_test.json", "w", encoding="utf-8") as f:
    json.dump(qs, f, indent=2)
print("Saved 160 questions to scripts/mh9_mth2_ch5_test.json")
