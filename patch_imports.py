import json

nb_path = 'obsidian_geochem.ipynb'
nb = json.load(open(nb_path, encoding='utf-8'))

patch_lines = [
    "\n",
    "# Shim: newer plotly uses plain dicts for _js2py_relayout instead of traitlets.\n",
    "# Patch FigureWidget so observe/unobserve calls on those dicts are safe no-ops.\n",
    "class _ObservableDict(dict):\n",
    "    def observe(self, *a, **kw): pass\n",
    "    def unobserve(self, *a, **kw): pass\n",
    "\n",
    "_orig_fw_init = FigureWidget.__init__\n",
    "def _fw_init_patched(self, *args, **kwargs):\n",
    "    _orig_fw_init(self, *args, **kwargs)\n",
    "    for attr in ('_js2py_relayout', '_traceDeltas', '_js2py_pointsCallback'):\n",
    "        v = getattr(self, attr, None)\n",
    "        if isinstance(v, dict) and not isinstance(v, _ObservableDict):\n",
    "            object.__setattr__(self, attr, _ObservableDict(v))\n",
    "FigureWidget.__init__ = _fw_init_patched\n",
]

for i, cell in enumerate(nb['cells']):
    src = cell.get('source', [])
    if src and 'CELL 1' in src[0]:
        # Only add if not already patched
        if '_ObservableDict' not in ''.join(src):
            cell['source'] = src + patch_lines
            print(f"Patched imports cell {i}: now {len(cell['source'])} lines")
        else:
            print("Already patched")
        break

json.dump(nb, open(nb_path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print("Saved!")
