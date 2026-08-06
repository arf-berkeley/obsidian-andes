import json

# Load the notebook
with open('obsidian_geochem.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find and replace CELL 5 (the problematic cell)
new_cell_code = [
    "# CELL 5 - SOURCE SELECTION WITH MAP & CHECKBOXES\n",
    "# Fixed version avoiding Plotly FigureWidget property validation errors\n",
    "\n",
    "# --- Data validation ---\n",
    "if 'srcs_locs' not in globals():\n",
    "    raise ValueError(\"Data not loaded: run the Data Loading cell first.\")\n",
    "\n",
    "srcs_locs = srcs_locs.copy()\n",
    "\n",
    "if 'Lat' not in srcs_locs.columns or 'Long' not in srcs_locs.columns:\n",
    "    raise ValueError(\"srcs_locs is missing Lat/Long columns.\")\n",
    "\n",
    "srcs_locs['Lat']  = pd.to_numeric(srcs_locs['Lat'],  errors='coerce')\n",
    "srcs_locs['Long'] = pd.to_numeric(srcs_locs['Long'], errors='coerce')\n",
    "srcs_locs = srcs_locs.dropna(subset=['Lat', 'Long'])\n",
    "\n",
    "if srcs_locs.empty:\n",
    "    raise ValueError(\"srcs_locs contains no valid coordinates after cleaning.\")\n",
    "\n",
    "names  = srcs_locs['Name'].astype(str).tolist()\n",
    "groups = srcs_locs['Group'].astype(str).tolist()\n",
    "lats   = srcs_locs['Lat'].astype(float).tolist()\n",
    "lons   = srcs_locs['Long'].astype(float).tolist()\n",
    "\n",
    "# DEBUG: Print first few coordinates\n",
    "print(f\"📍 First 3 coordinates:\")\n",
    "for i in range(min(3, len(names))):\n",
    "    print(f\"   {names[i]}: Lat={lats[i]}, Long={lons[i]}\")\n",
    "print(f\"   Lat range: {min(lats):.2f} to {max(lats):.2f}\")\n",
    "print(f\"   Long range: {min(lons):.2f} to {max(lons):.2f}\")\n",
    "print()\n",
    "\n",
    "# --- Zoom calculation ---\n",
    "center_lat = np.mean(lats)\n",
    "center_lon = np.mean(lons)\n",
    "max_span   = max(max(lats) - min(lats), max(lons) - min(lons))\n",
    "zoom = (5  if max_span > 10 else\n",
    "        6  if max_span > 5  else\n",
    "        7  if max_span > 2  else\n",
    "        8  if max_span > 1  else\n",
    "        9  if max_span > 0.5 else 11)\n",
    "\n",
    "# --- Create Figure (using go.Figure to avoid FigureWidget property validation errors) ---\n",
    "fig = go.Figure(data=[go.Scattermapbox(\n",
    "    lat=lats,\n",
    "    lon=lons,\n",
    "    mode='markers+text',\n",
    "    text=names,\n",
    "    textposition='top center',\n",
    "    customdata=groups,\n",
    "    marker=dict(size=10, color='steelblue'),\n",
    "    hovertemplate='<b>%{text}</b><br><b>Group:</b> %{customdata}<extra></extra>'\n",
    ")])\n",
    "\n",
    "fig.update_layout(\n",
    "    mapbox=dict(\n",
    "        style='open-street-map',\n",
    "        center=dict(lat=center_lat, lon=center_lon),\n",
    "        zoom=zoom\n",
    "    ),\n",
    "    height=500,\n",
    "    margin=dict(r=0, l=0, t=30, b=0),\n",
    "    title=\"🗺️ Obsidian Source Locations\",\n",
    "    hovermode='closest'\n",
    ")\n",
    "\n",
    "fig.show()\n",
    "\n",
    "# --- Checkbox selection UI (since go.Figure doesn't support lasso in this notebook context) ---\n",
    "unique_groups = sorted(list(set(groups)))\n",
    "checkboxes = [widgets.Checkbox(value=False, description=g) for g in unique_groups]\n",
    "\n",
    "selected_names = []\n",
    "selected_groups = []\n",
    "\n",
    "def on_checkbox_change(change):\n",
    "    global selected_names, selected_groups\n",
    "    selected = [unique_groups[i] for i, cb in enumerate(checkboxes) if cb.value]\n",
    "    if selected:\n",
    "        selected_names = [n for n, g in zip(names, groups) if g in selected]\n",
    "        selected_groups = list(set([g for g in groups if g in selected]))\n",
    "\n",
    "for cb in checkboxes:\n",
    "    cb.observe(on_checkbox_change, names='value')\n",
    "\n",
    "# --- Selection button ---\n",
    "output = widgets.Output()\n",
    "button = widgets.Button(\n",
    "    description='Get Selection',\n",
    "    button_style='primary',\n",
    "    icon='check',\n",
    ")\n",
    "\n",
    "def on_get_selection(b):\n",
    "    global selected_names, selected_groups\n",
    "    output.clear_output()\n",
    "    with output:\n",
    "        selected = [unique_groups[i] for i, cb in enumerate(checkboxes) if cb.value]\n",
    "        if selected:\n",
    "            print(f\"✅  {len(selected)} source(s) selected:\\n\")\n",
    "            for g in selected:\n",
    "                print(f\"  • {g}\")\n",
    "            selected_names = [n for n, g in zip(names, groups) if g in selected]\n",
    "            selected_groups = list(set([g for g in groups if g in selected]))\n",
    "        else:\n",
    "            print(\"⚠️  No sources selected. Check boxes below and click Get Selection.\")\n",
    "\n",
    "button.on_click(on_get_selection)\n",
    "\n",
    "checkbox_widget = widgets.VBox(checkboxes, layout=widgets.Layout(\n",
    "    border='1px solid #ccc',\n",
    "    padding='10px',\n",
    "    height='150px',\n",
    "    overflow_y='auto'\n",
    "))\n",
    "\n",
    "print(\"\\n📌 Select obsidian sources using checkboxes below:\")\n",
    "display(checkbox_widget)\n",
    "display(button, output)\n",
]

# Find cell with the problematic code
found = False
for i, cell in enumerate(nb['cells']):
    if cell.get('cell_type') == 'code' and cell.get('source') and 'CELL 5 - SOURCE SELECTION' in cell['source'][0]:
        cell['source'] = new_cell_code
        found = True
        print(f"Replaced cell {i} (ID: {cell.get('id')})")
        print(f"New cell has {len(new_cell_code)} lines")
        break

if not found:
    print("ERROR: Cell with 'CELL 5 - SOURCE SELECTION' not found!")
    print("Looking for cells with 'FigureWidget'...")
    for i, cell in enumerate(nb['cells']):
        if cell.get('cell_type') == 'code' and cell.get('source') and 'FigureWidget' in ''.join(cell['source']):
            print(f"Found FigureWidget in cell {i} (ID: {cell.get('id')})")
    exit(1)

# Save the notebook
try:
    with open('obsidian_geochem.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print("Notebook saved successfully!")
except Exception as e:
    print(f"ERROR saving notebook: {e}")
    exit(1)
