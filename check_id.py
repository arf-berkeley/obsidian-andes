import json
nb = json.load(open('obsidian_geochem.ipynb', encoding='utf-8'))
for i, c in enumerate(nb['cells']):
    if 'eaa89851' in str(c.get('id', '')):
        print(f"Index {i}: ID={c['id']}, type={c['cell_type']}")
        if c.get('source'):
            print(f"  First line: {c['source'][0][:60]}")
            print(f"  Line count: {len(c['source'])}")
