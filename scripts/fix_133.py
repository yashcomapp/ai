with open("scripts/build_clean_ch1.py", "r", encoding="utf-8") as f:
    text = f.read()

old_arch2_arch3 = """        # Arch 2: Algebraic midpoint: AM = MB => ax - b = cx + d => find x
        {
            'data': [(4, 3, 2, 9, 6, 21), (5, 4, 3, 10, 7, 31), (6, 2, 3, 13, 5, 28),
                     (4, 5, 2, 11, 8, 27), (5, 6, 2, 18, 8, 34), (6, 4, 2, 20, 6, 32),
                     (7, 3, 4, 15, 6, 39), (5, 8, 3, 16, 12, 52), (6, 5, 3, 19, 8, 43), (7, 2, 3, 22, 6, 40)],"""

new_arch2_arch3 = """        # Arch 2: Algebraic midpoint: AM = MB => ax - b = cx + d => find x
        {
            'data': [(5, 2, 2, 7, 3, 13), (4, 1, 2, 7, 4, 15), (6, 2, 3, 13, 5, 28),
                     (4, 3, 2, 9, 6, 21), (5, 4, 3, 10, 7, 31), (4, 5, 2, 11, 8, 27),
                     (5, 7, 2, 20, 9, 38), (3, 2, 1, 18, 10, 28), (4, 7, 2, 15, 11, 37), (5, 8, 3, 16, 12, 52)],"""

text = text.replace(old_arch2_arch3, new_arch2_arch3)

with open("scripts/build_clean_ch1.py", "w", encoding="utf-8") as f:
    f.write(text)

print("build_clean_ch1.py 1.3.3 distinctness fixed.")
