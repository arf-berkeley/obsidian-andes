import json

nb = json.load(open('obsidian_geochem.ipynb', encoding='utf-8'))
for i, c in enumerate(nb['cells']):
    if c.get('cell_type') == 'code' and c.get('source') and 'CELL 5 - SOURCE SELECTION' in c['source'][0]:
        print(f"Found CELL 5 at index {i}, ID: {c.get('id')}")
        print(f"First line: {c['source'][0][:70]}")
        print(f"Total lines: {len(c['source'])}")
        
        # Check last few lines
        print("\nLast 5 lines:")
        for line in c['source'][-5:]:
            print(f"  {repr(line[:60])}")
        break
