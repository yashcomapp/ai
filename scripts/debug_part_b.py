import sys
sys.path.append('scripts')
import build_cbse9_scie_ch4_part_b as pb

for fn_name in ['gen_4_2_2', 'gen_4_2_3', 'gen_4_3_1', 'gen_4_3_2']:
    try:
        fn = getattr(pb, fn_name)
        res = fn()
        print(f"{fn_name} OK: {len(res)} Qs")
    except Exception as e:
        print(f"Error in {fn_name}: {type(e).__name__}: {e}")
