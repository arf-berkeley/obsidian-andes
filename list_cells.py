import json

nb = json.load(open('obsidian_geochem.ipynb', encoding='utf-8'))
for i, c in enumerate(nb['cells']):
    cell_id = c.get('id', 'NO ID')
    cell_type = c.get('cell_type', 'unknown')
    first_line = c.get('source', [''])[0][:50] if c.get('source') else 'EMPTY'
    print(f"{i:2}: {cell_id:20} [{cell_type:8}] {repr(first_line)}")
