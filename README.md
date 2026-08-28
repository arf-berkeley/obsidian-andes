# Andean Obsidian Geochemical Sourcing Notebook

An interactive notebook for XRF sourcing of obsidian from the Andes of South America, portable across VS Code, classic Jupyter, Voilà, and Binder.

## Reproducible environment

All dependencies are exact-pinned (Python 3.11.9) so the notebook can be rebuilt identically years from now, even if newer package releases introduce breaking changes.

- environment.yaml for conda/mamba (also used by Binder)
- requirements.txt for pip

### Conda

```bash
conda env create -f environment.yaml
conda activate obsidian-geochem
jupyter lab
```

### Pip

```bash
python -m pip install -r requirements.txt
jupyter lab
```

## Run the notebook

### VS Code

Open notebooks/obsidian_geochem.ipynb in VS Code and run the cells in order.

### Jupyter Notebook or JupyterLab

```bash
jupyter notebook notebooks/obsidian_geochem.ipynb
```

### Voilà

```bash
voila notebooks/obsidian_geochem.ipynb
```

### Binder

Launch the repository on [mybinder.org](https://mybinder.org) and either open the notebook directly in JupyterLab, or append `/voila/render/notebooks/obsidian_geochem.ipynb` to the Binder URL to launch it as a Voilà app. The root environment.yaml pins the exact dependencies (including `voila`) used to build the Binder image.

## Archival guidance

To improve long-term reuse and archival stability:

1. Keep the notebook, data files, and environment files together in the repository.
2. Dependency versions are exact-pinned (`==`) in environment.yaml and requirements.txt — do not loosen these to range pins (`>=`), since newer package releases are not guaranteed to preserve behavior over a multi-year horizon.
3. Prefer local CSV data files over network-based sources.
4. When depositing to Zenodo, include the repository archive or a DOI-linked release snapshot, and reference the exact commit/tag whose environment files were used to generate the results.
5. Update CITATION.cff with the release version and DOI once a Zenodo archive is created, so downstream users can cite the exact archived version.
