import sys
import os

with open('scripts/build_cbse9_scie_ch2_part1.py', 'r', encoding='utf-8') as f:
    text = f.read()

import ast

tree = ast.parse(text)
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id.startswith('arch'):
                if isinstance(node.value, ast.Dict):
                    data_val = None
                    for k, v in zip(node.value.keys, node.value.values):
                        if isinstance(k, ast.Constant) and k.value == 'data':
                            data_val = v
                    if data_val and isinstance(data_val, ast.List):
                        for idx, elt in enumerate(data_val.elts):
                            if isinstance(elt, ast.Tuple):
                                str_elts = [e.value for e in elt.elts if isinstance(e, ast.Constant) and isinstance(e.value, str)]
                                if str_elts:
                                    last = str_elts[-1]
                                    parts = last.split(', ')
                                    if len(parts) < 3 and not any(k in last for k in ['Step', 'kg']):
                                        print(f"{target.id} item {idx}: only {len(parts)} options: '{last}'")
