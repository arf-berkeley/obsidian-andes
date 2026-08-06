import json

nb_path = 'obsidian_geochem.ipynb'
nb = json.load(open(nb_path, encoding='utf-8'))

new_source = [
    "# CELL 5 — SOURCE SELECTION\n",
    "\n",
    "srcs_locs['Lat']  = pd.to_numeric(srcs_locs['Lat'],  errors='coerce')\n",
    "srcs_locs['Long'] = pd.to_numeric(srcs_locs['Long'], errors='coerce')\n",
    "srcs_locs = srcs_locs.dropna(subset=['Lat', 'Long'])\n",
    "\n",
    "names  = srcs_locs['Name'].astype(str).tolist()\n",
    "groups = srcs_locs['Group'].astype(str).tolist()\n",
    "lats   = srcs_locs['Lat'].tolist()\n",
    "lons   = srcs_locs['Long'].tolist()\n",
    "\n",
    "center_lat, center_lon = np.mean(lats), np.mean(lons)\n",
    "span = max(max(lats) - min(lats), max(lons) - min(lons))\n",
    "zoom = 5 if span > 10 else 6 if span > 5 else 7 if span > 2 else 8 if span > 1 else 11\n",
    "\n",
    "fig = go.Figure(go.Scattermapbox(\n",
    "    lat=lats, lon=lons, mode='markers+text',\n",
    "    text=names, textposition='top center', customdata=groups,\n",
    "    marker=dict(size=10, color='steelblue'),\n",
    "    hovertemplate='<b>%{text}</b><br>Group: %{customdata}<extra></extra>'\n",
    "))\n",
    "fig.update_layout(\n",
    "    mapbox=dict(style='open-street-map', center=dict(lat=center_lat, lon=center_lon), zoom=zoom),\n",
    "    height=500, margin=dict(r=0, l=0, t=30, b=0), title='Obsidian Source Locations'\n",
    ")\n",
    "fig.show()\n",
    "\n",
    "unique_groups = sorted(set(groups))\n",
    "checkboxes = [widgets.Checkbox(value=False, description=g) for g in unique_groups]\n",
    "selected_names, selected_groups = [], []\n",
    "\n",
    "def update_selection(_=None):\n",
    "    global selected_names, selected_groups\n",
    "    sel = {unique_groups[i] for i, cb in enumerate(checkboxes) if cb.value}\n",
    "    selected_groups = sorted(sel)\n",
    "    selected_names  = [n for n, g in zip(names, groups) if g in sel]\n",
    "\n",
    "for cb in checkboxes:\n",
    "    cb.observe(update_selection, names='value')\n",
    "\n",
    "out = widgets.Output()\n",
    "btn = widgets.Button(description='Confirm Selection', button_style='primary')\n",
    "\n",
    "def on_confirm(_):\n",
    "    update_selection()\n",
    "    out.clear_output()\n",
    "    with out:\n",
    "        print(f\"{len(selected_groups)} group(s): {', '.join(selected_groups)}\" if selected_groups else \"Nothing selected.\")\n",
    "\n",
    "btn.on_click(on_confirm)\n",
    "\n",
    "display(widgets.VBox(checkboxes, layout=widgets.Layout(height='140px', overflow_y='auto', border='1px solid #ccc', padding='6px')))\n",
    "display(btn, out)"
]

for i, cell in enumerate(nb['cells']):
    src = cell.get('source', [])
    if src and 'CELL 5' in (src[0] if isinstance(src, list) else src):
        cell['source'] = new_source
        print(f"Updated cell {i} (ID: {cell.get('id')}): {len(new_source)} lines")
        break

json.dump(nb, open(nb_path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print("Saved!")
