import sys
sys.path.append('scripts')
import build_cbse9_scie_ch4_part_a as p

for fn_name in ['gen_4_1_1', 'gen_4_1_2', 'gen_4_1_3', 'gen_4_2_1']:
    try:
        fn = getattr(p, fn_name)
        res = fn()
        print(f"{fn_name} OK, generated {len(res)} questions")
    except Exception as e:
        print(f"Error in {fn_name}: {type(e).__name__}: {e}")
