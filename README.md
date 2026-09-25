# Andean Obsidian Geochemical Sourcing Notebook

[![Voila](https://img.shields.io/badge/launch-Voila-blue.svg)](https://mybinder.org/v2/gh/arf-berkeley/obsidian-andes/HEAD?urlpath=voila%2Frender%2Fnotebooks%2Fobsidian_geochem.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/arf-berkeley/obsidian-andes/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2Fobsidian_geochem.ipynb)

This is a free, interactive tool for **visually sourcing obsidian artifacts from the Andes** using XRF (X-ray fluorescence) geochemical data. You upload your elemental concentration data, and the notebook compares it against a table of chemistry from known Andean obsidian sources to help you identify where your artifacts came from. One Standard Deviation ellipses (containing 68% of values) are shown for each source. 

**No coding experience is required to use this tool.** You can run it entirely in your web browser without installing anything.

---

## Quickest way to get started (no installation needed)

Click one of the buttons below to launch the tool directly in your browser:

- **[Launch the Voila App](https://mybinder.org/v2/gh/arf-berkeley/obsidian-andes/HEAD?urlpath=voila%2Frender%2Fnotebooks%2Fobsidian_geochem.ipynb)** — Opens a clean, app-like interface. Best for most users. Just wait for it to load (this can take a minute or two the first time), then follow the on-screen instructions.

- **[Launch in JupyterLab](https://mybinder.org/v2/gh/arf-berkeley/obsidian-andes/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2Fobsidian_geochem.ipynb)** — Opens the full notebook environment if you want to see or modify the underlying code.

> **Tip:** Binder is a free cloud service, so it may take 1–2 minutes to start up. Be patient — once it loads, everything runs interactively.

---

## What you'll need

- **Your data** in a CSV (spreadsheet) file with elemental concentrations from XRF analysis. The notebook will walk you through uploading it.

- **Source Data** in a CSV (spreadsheet) file with elemental concentrations from Andean obsidian sources preferably from a calibrated XRF intrument. 

- **Source Location Data** in a CSV (spreadsheet) file with fields containing Latitude and Longitude for sources in the Andes and Group field that precisely matches the Source Data group field.

---
## How to use

- Select sources within the larger region of your study area.

- Use buttons turn on / off sample labels or show the points used to create the 1-SD source ellipses.

- Use the Camera icon in the plot views to export Scalable Vector Graphics (SVG). These can be converted to PDF or modified in an illustration software.
 
---

## Installing on your own computer (optional)

If you'd prefer to run the tool locally — for example, if you're working offline, with sensitive data, or want faster performance — follow the steps below. If any of this feels unfamiliar, the cloud version above works just as well.

### Recommended: Miniconda

[Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a lightweight tool that manages software dependencies so everything works together smoothly. Install it, then open a terminal (on Mac: Terminal app; on Windows: Anaconda Prompt) and type:

```bash
conda env create -f environment.yml
conda activate obsidian-geochem
jupyter lab
```

This will open the notebook in your browser. Navigate to `notebooks/obsidian_geochem.ipynb` and click **Run > Run All Cells** (or the ▶▶ button).

### Alternative: Run in a local IDE like VS Code

If you already use a local code editor:

1. Open this folder in code editor file browser.
2. Set up the conda environment as above.
3. Open `notebooks/obsidian_geochem.ipynb`, select the `obsidian-geochem` kernel when prompted, and run all cells.

### Alternative: pip (advanced)

If you can't install Miniconda, you can use pip, though this sometimes requires additional system tools on certain computers:

```bash
python -m pip install -r requirements.txt
jupyter lab
```

---

## For collaborators and archival use

If you're publishing results generated with this tool, citing it, or depositing data to a repository like Zenodo, here are some best practices:

- **Keep your data with the notebook.** Include your CSV files in the same folder/repository rather than relying on Google Sheets links, which can break over time.
- **The tool is designed for long-term reuse.** Dependency versions are specified flexibly so the software can be rebuilt on future systems without breaking — you shouldn't need to worry about this, but it means your results should be reproducible years from now.
- **For Zenodo deposits,** include the full repository and reference the specific version (release tag or commit) used to generate your published results.
- **Citation:** Update `CITATION.cff` with the release version and DOI once a Zenodo archive is created, so others can cite the exact version you used.

---

## Questions or problems?

Open an [issue](../../issues) on this repository and we'll help you out.
