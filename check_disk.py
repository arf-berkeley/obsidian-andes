import json
nb = json.load(open('obsidian_geochem.ipynb', encoding='utf-8'))
for c in nb['cells']:
    cid = c.get('id', '')
    if 'eaa89851' in cid:
        src = c.get('source', [])
        print(f"ID: {cid}, lines: {len(src)}")
        print("First 3 lines:", src[:3])
        break
