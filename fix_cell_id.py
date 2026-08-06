import json

nb_path = 'obsidian_geochem.ipynb'
nb = json.load(open(nb_path, encoding='utf-8'))

new_code_lines = [
    "# CELL 5 - SOURCE SELECTION WITH MAP & CHECKBOXES\n",
    "# Uses go.Figure (not FigureWidget) to avoid Plotly mapbox._derived validation errors\n",
    "\n",
    "if 'srcs_locs' not in globals():\n",
    "    raise ValueError(\"Data not loaded: run the Data Loading cell first.\")\n",
    "\n",
    "srcs_locs = srcs_locs.copy()\n",
    "srcs_locs['Lat']  = pd.to_numeric(srcs_locs['Lat'],  errors='coerce')\n",
    "srcs_locs['Long'] = pd.to_numeric(srcs_locs['Long'], errors='coerce')\n",
    "srcs_locs = srcs_locs.dropna(subset=['Lat', 'Long'])\n",
    "\n",
    "if srcs_locs.empty:\n",
    "    raise ValueError(\"srcs_locs contains no valid coordinates.\")\n",
    "\n",
    "names  = srcs_locs['Name'].astype(str).tolist()\n",
    "groups = srcs_locs['Group'].astype(str).tolist()\n",
    "lats   = srcs_locs['Lat'].astype(float).tolist()\n",
    "lons   = srcs_locs['Long'].astype(float).tolist()\n",
    "\n",
    "print(f\"📍 {len(names)} source locations loaded\")\n",
    "print(f\"   Lat range: {min(lats):.2f} to {max(lats):.2f}\")\n",
    "print(f\"   Long range: {min(lons):.2f} to {max(lons):.2f}\")\n",
    "\n",
    "center_lat = np.mean(lats)\n",
    "center_lon = np.mean(lons)\n",
    "max_span   = max(max(lats) - min(lats), max(lons) - min(lons))\n",
    "zoom = (5 if max_span > 10 else 6 if max_span > 5 else 7 if max_span > 2 else 8 if max_span > 1 else 11)\n",
    "\n",
    "fig = go.Figure(data=[go.Scattermapbox(\n",
    "    lat=lats, lon=lons, mode='markers+text', text=names, textposition='top center',\n",
    "    customdata=groups,\n",
    "    marker=dict(size=10, color='steelblue'),\n",
    "    hovertemplate='<b>%{text}</b><br>Group: %{customdata}<extra></extra>')])\n",
    "\n",
    "fig.update_layout(\n",
    "    mapbox=dict(style='open-street-map', center=dict(lat=center_lat, lon=center_lon), zoom=zoom),\n",
    "    height=500, margin=dict(r=0, l=0, t=30, b=0), title=\"🗺️ Obsidian Sources\"\n",
    ")\n",
    "fig.show()\n",
    "\n",
    "unique_groups = sorted(list(set(groups)))\n",
    "checkboxes = [widgets.Checkbox(value=False, description=g) for g in unique_groups]\n",
    "selected_names, selected_groups = [], []\n",
    "\n",
    "def on_cb_change(change):\n",
    "    global selected_names, selected_groups\n",
    "    sel = [unique_groups[i] for i, cb in enumerate(checkboxes) if cb.value]\n",
    "    selected_names  = [n for n, g in zip(names, groups) if g in sel]\n",
    "    selected_groups = list(set(g for g in groups if g in sel))\n",
    "\n",
    "for cb in checkboxes:\n",
    "    cb.observe(on_cb_change, names='value')\n",
    "\n",
    "output = widgets.Output()\n",
    "button = widgets.Button(description='Get Selection', button_style='primary')\n",
    "\n",
    "def on_get_sel(b):\n",
    "    output.clear_output()\n",
    "    with output:\n",
    "        sel = [unique_groups[i] for i, cb in enumerate(checkboxes) if cb.value]\n",
    "        if sel:\n",
    "            globals()['selected_groups'] = sel\n",
    "            print(f\"✅  {len(sel)} source(s) selected: {', '.join(sel)}\")\n",
    "        else:\n",
    "            print(\"⚠️  No sources selected\")\n",
    "\n",
    "button.on_click(on_get_sel)\n",
    "\n",
    "checkbox_widget = widgets.VBox(checkboxes, layout=widgets.Layout(\n",
    "    border='1px solid #ccc', padding='10px', height='120px', overflow_y='auto'))\n",
    "\n",
    "print(\"\\n📌 Select obsidian sources using checkboxes below:\")\n",
    "display(checkbox_widget)\n",
    "display(button, output)"
]

# Find the CELL 5 cell (adca16fb) and update it with new ID that VS Code expects
for i, cell in enumerate(nb['cells']):
    src = cell.get('source', [])
    if src and 'CELL 5' in (src[0] if isinstance(src, list) else src):
        print(f"Found at index {i}, ID={cell.get('id')}, lines={len(src)}")
        cell['id'] = 'eaa89851'  # Use the ID VS Code expects (without #VSC- prefix)
        cell['source'] = new_code_lines
        print(f"Updated: ID=eaa89851, lines={len(new_code_lines)}")
        break

json.dump(nb, open(nb_path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print("✅ Saved!")
