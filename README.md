# Andean Obsidian Geochemical Sourcing Notebook

[![Voila](https://img.shields.io/badge/launch-Voila-blue.svg)](https://mybinder.org/v2/gh/arf-berkeley/obsidian-andes/HEAD?urlpath=voila%2Frender%2Fnotebooks%2Fobsidian_geochem.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/arf-berkeley/obsidian-andes/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2Fobsidian_geochem.ipynb)

An interactive notebook for XRF sourcing of obsidian from the Andes of South America, portable across VS Code (with Miniconda), classic Jupyter, Voilà, and Binder. Geochemical data must be in PPM. For Weight% data from a Bruker instrument process the data first using the code [Bruker XRF PPM Plot](https://github.com/arf-berkeley/bruker-xrf-ppm-plot)

## How to use
### Voilà

```bash
The simplest way to use this app is with Voila
[![Voila](https://img.shields.io/badge/launch-Voila-blue.svg)](https://mybinder.org/v2/gh/arf-berkeley/obsidian-andes/HEAD?urlpath=voila%2Frender%2Fnotebooks%2Fobsidian_geochem.ipynb)
voila notebooks/obsidian_geochem.ipynb
```

### Binder
Binder allows you to run and edit the code in a browser. Launch the repository on [mybinder.org](https://mybinder.org) and either open the notebook directly in JupyterLab, or append `/voila/render/notebooks/obsidian_geochem.ipynb` to the Binder URL to launch it as a Voilà app. The root `environment.yml` (minimum-version constraints, including `voila`) is used to build the Binder image — `repo2docker` only recognizes the `.yml` extension, so keep this filename exact.
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/arf-berkeley/obsidian-andes/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2Fobsidian_geochem.ipynb)

### IDE (e.g., VS Code)
1. Open this folder in your IDE.
2. Create/activate the `obsidian-geochem` conda environment as above (Miniconda recommended).
3. Open notebooks/obsidian_geochem.ipynb, select the `obsidian-geochem` kernel, and use **Run > Run All Cells**.

### Jupyter Notebook or JupyterLab
```bash
jupyter notebook notebooks/obsidian_geochem.ipynb
```
