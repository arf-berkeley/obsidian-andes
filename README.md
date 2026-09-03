# Andean Obsidian Geochemical Sourcing Notebook

[![Voila](https://img.shields.io/badge/launch-Voila-blue.svg)](https://mybinder.org/v2/gh/arf-berkeley/obsidian-andes/HEAD?urlpath=voila%2Frender%2Fnotebooks%2Fobsidian_geochem.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/arf-berkeley/obsidian-andes/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2Fobsidian_geochem.ipynb)

An interactive notebook for XRF sourcing of obsidian from the Andes of South America, portable across VS Code (with Miniconda), classic Jupyter, Voilà, and Binder. Geochemical data must be in PPM. For Weight% data from a Bruker instrument process the data first using the code [Bruker XRF PPM Plot] (https://github.com/arf-berkeley/bruker-xrf-ppm-plot)

## Reproducible environment

Dependencies use minimum-version constraints (`>=`), not exact pins, so conda/pip can always resolve a working, compatible set on whatever Python version, OS, or kernel happens to be available (local Miniconda, WSL, another Linux shell, or Binder's build image) instead of failing when an old exact pin has no build for that platform.

- `environment.yml` for conda/mamba/Miniconda (also the file Binder's `repo2docker` auto-detects — the name must be exactly `environment.yml`, not `.yaml`)
- `requirements.txt` for pip/venv

### Conda / Miniconda (recommended for long-term reproducibility)

Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) if you don't already have conda, then:

```bash
conda env create -f environment.yml
conda activate obsidian-geochem
jupyter lab
```

To use this environment as a Jupyter kernel inside VS Code: open the Command Palette → "Python: Select Interpreter" (or "Jupyter: Select Kernel") → choose the `obsidian-geochem` conda environment.

### Pip / venv

Only use this path if conda/Miniconda is unavailable. It requires a working C/C++ compiler toolchain on some platforms if pre-built wheels aren't available for your Python version — conda avoids this entirely.

```bash
python -m pip install -r requirements.txt
jupyter lab
```

## Run the notebook

### VS Code

1. Open this folder in VS Code.
2. Create/activate the `obsidian-geochem` conda environment as above (Miniconda recommended).
3. Open notebooks/obsidian_geochem.ipynb, select the `obsidian-geochem` kernel, and use **Run > Run All Cells**.

### Jupyter Notebook or JupyterLab

```bash
jupyter notebook notebooks/obsidian_geochem.ipynb
```

### Voilà

```bash
voila notebooks/obsidian_geochem.ipynb
```

### Binder

Launch the repository on [mybinder.org](https://mybinder.org) and either open the notebook directly in JupyterLab, or append `/voila/render/notebooks/obsidian_geochem.ipynb` to the Binder URL to launch it as a Voilà app. The root `environment.yml` (minimum-version constraints, including `voila`) is used to build the Binder image — `repo2docker` only recognizes the `.yml` extension, so keep this filename exact.

## Archival guidance

To improve long-term reuse and archival stability:

1. Keep the notebook, data files, and environment files together in the repository.
2. Dependency versions use minimum-version constraints (`>=`) rather than exact pins, so the environment can always solve on whatever kernel/OS/Python is available years from now — a wide compatible range is more archival-safe than an exact pin that eventually has no available build.
3. Prefer local CSV data files over network-based sources; the notebook's Data Upload tab also accepts direct/Google Sheets URLs as a fallback, but for archival snapshots keep a local copy of the CSVs bundled with the repository (Google Sheets links are not guaranteed to remain valid for years).
4. Prefer conda/Miniconda over pip for local runs when possible — conda-forge distributes pre-built binaries for a wider range of platforms, whereas pip may need to compile numpy/pandas from source if no matching wheel exists, which can fail without a C compiler installed.
5. When depositing to Zenodo, include the repository archive or a DOI-linked release snapshot, and reference the exact commit/tag whose environment files were used to generate the results.
6. Update CITATION.cff with the release version and DOI once a Zenodo archive is created, so downstream users can cite the exact archived version.
