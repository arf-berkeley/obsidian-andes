import json

nb_path = 'obsidian_geochem.ipynb'
nb = json.load(open(nb_path, encoding='utf-8'))

# New cell source code
new_code = """# CELL 5 - SOURCE SELECTION WITH MAP & CHECKBOXES
# Fixed: Uses go.Figure instead of FigureWidget to avoid Plotly validation errors

# Data validation
if 'srcs_locs' not in globals():
    raise ValueError("Data not loaded: run the Data Loading cell first.")

srcs_locs = srcs_locs.copy()
srcs_locs['Lat']  = pd.to_numeric(srcs_locs['Lat'],  errors='coerce')
srcs_locs['Long'] = pd.to_numeric(srcs_locs['Long'], errors='coerce')
srcs_locs = srcs_locs.dropna(subset=['Lat', 'Long'])

if srcs_locs.empty:
    raise ValueError("srcs_locs contains no valid coordinates.")

# Extract data
names  = srcs_locs['Name'].astype(str).tolist()
groups = srcs_locs['Group'].astype(str).tolist()
lats   = srcs_locs['Lat'].astype(float).tolist()
lons   = srcs_locs['Long'].astype(float).tolist()

# Debug output
print(f"📍 First 3 coordinates:")
for i in range(min(3, len(names))):
    print(f"   {names[i]}: Lat={lats[i]}, Long={lons[i]}")
print(f"   Lat range: {min(lats):.2f} to {max(lats):.2f}")
print(f"   Long range: {min(lons):.2f} to {max(lons):.2f}")
print()

# Map center and zoom
center_lat = np.mean(lats)
center_lon = np.mean(lons)
max_span   = max(max(lats) - min(lats), max(lons) - min(lons))
zoom = (5 if max_span > 10 else 6 if max_span > 5 else 7 if max_span > 2 else 8 if max_span > 1 else 11)

# Create static go.Figure (NOT FigureWidget) - avoids Plotly validation errors
fig = go.Figure(data=[go.Scattermapbox(
    lat=lats, lon=lons, mode='markers+text', text=names, textposition='top center',
    customdata=groups,
    marker=dict(size=10, color='steelblue'),
    hovertemplate='<b>%{text}</b><br>Group: %{customdata}<extra></extra>')])

fig.update_layout(
    mapbox=dict(style='open-street-map', center=dict(lat=center_lat, lon=center_lon), zoom=zoom),
    height=500, margin=dict(r=0, l=0, t=30, b=0), title="🗺️ Obsidian Sources"
)
fig.show()

# Selection UI with checkboxes
unique_groups = sorted(list(set(groups)))
checkboxes = [widgets.Checkbox(value=False, description=g) for g in unique_groups]
selected_names, selected_groups = [], []

def on_cb_change(change):
    global selected_names, selected_groups
    selected_names = [n for n, g in zip(names, groups) if any(cb.value and unique_groups[i] == g for i, cb in enumerate(checkboxes))]
    selected_groups = list(set([g for n, g in zip(names, groups) if any(cb.value and unique_groups[i] == g for i, cb in enumerate(checkboxes))]))

for cb in checkboxes:
    cb.observe(on_cb_change, names='value')

output = widgets.Output()
button = widgets.Button(description='Get Selection', button_style='primary')

def on_get_sel(b):
    output.clear_output()
    with output:
        selected = [unique_groups[i] for i, cb in enumerate(checkboxes) if cb.value]
        if selected:
            print(f"✅  {len(selected)} source(s): {', '.join(selected)}")
            globals()['selected_groups'] = selected
        else:
            print("⚠️  No sources selected")

button.on_click(on_get_sel)

print("\\n📌 Select obsidian sources using checkboxes below:")
display(checkbox_widget := widgets.VBox(checkboxes, layout=widgets.Layout(border='1px solid #ccc', padding='10px', height='120px', overflow_y='auto')))
display(button, output)"""

# Convert to JSON array format (each line becomes a separate array element)
source_lines = new_code.split('\n')
source_array = [line + '\n' for line in source_lines[:-1]] + [source_lines[-1]]

# Find cell 5 and replace
for i, cell in enumerate(nb['cells']):
    if cell.get('id') == '#VSC-eaa89851':
        print(f"Found cell at index {i}")
        print(f"  Old: {len(cell['source'])} lines")
        cell['source'] = source_array
        print(f"  New: {len(cell['source'])} lines")
        break

# Save
json.dump(nb, open(nb_path, 'w', encoding='utf-8'), indent=1)
print(f"\n✅ Cell replaced and notebook saved!")
