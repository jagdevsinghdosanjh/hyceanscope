# 🔭 HyceanScope

**HyceanScope** is a modular Streamlit app designed to simulate transmission spectra of exoplanets and assess their habitability under the Hycean paradigm. Inspired by Nikku Madhusudhan’s research, it empowers educators and students to explore atmospheric composition, spectral features, and biosignature detection.

---

## 🚀 Features

- 🌍 Input planetary parameters: mass, radius, temperature
- 🧪 Select atmospheric compositions (H₂, CH₄, CO₂, H₂O)
- 📈 Simulate transmission spectra across 1–4 μm
- 🧠 Predict Hycean habitability using rule-based logic
- 📋 Log runs with emoji-rich CSV support for classroom engagement

---

## 🧱 Modular Structure

| Module | Description |
|--------|-------------|
| `planet_input.py` | Streamlit sidebar for planetary parameters |
| `atmosphere_model.py` | Simulates spectral dips based on composition |
| `spectral_plot.py` | Interactive Plotly visualization |
| `habitability_predictor.py` | Flags Hycean candidates |
| `data_logger.py` | Logs user inputs and predictions |

---

## 📦 Installation

```bash
git clone https://github.com/jagdevsinghdosanjh/hyceanscope.git
cd hyceanscope
pip install -r requirements.txt
streamlit run app.py
🧑‍🏫 For Educators
Use in classroom demos to explain spectral absorption

Compare student-generated spectra and habitability predictions

Extend with RDKit or py3Dmol for molecular visualization

📚 References
Madhusudhan, N. (2024). The Hycean Paradigm in the Search for Life Elsewhere. arXiv:2406.12794

NASA Exoplanet Archive

🤝 Contributing
Pull requests welcome! For feature ideas or bug reports, open an issue or contact the maintainer.

Code

---

## 🌌 Task 2: Realistic Spectral Simulation

To go beyond Gaussian dips, we can approximate **radiative transfer** using:

### 🔬 Key Concepts
- **Optical Depth (τ)**: Determines how much light is absorbed.
- **Transmission (T)**: Given by \( T = e^{-τ} \)
- **Absorption Cross-Section (σ)**: Varies with wavelength and molecule.
- **Column Density (N)**: Amount of absorbing gas along the line of sight.

---

### 🧪 Sample Code: Radiative Transfer Approximation

```python
import numpy as np

def absorption_cross_section(wavelength, molecule):
    if molecule == 'CH4':
        return 0.05 * np.exp(-((wavelength - 3.3)**2) / 0.05)
    elif molecule == 'H2O':
        return 0.03 * np.exp(-((wavelength - 1.4)**2) / 0.02)
    elif molecule == 'CO2':
        return 0.04 * np.exp(-((wavelength - 4.3)**2) / 0.03)
    return 0.0

def simulate_spectrum_rt(wavelengths, composition, column_density=1e20):
    spectrum = np.ones_like(wavelengths)
    for molecule in composition:
        sigma = np.array([absorption_cross_section(w, molecule) for w in wavelengths])
        tau = sigma * column_density
        transmission = np.exp(-tau)
        spectrum *= transmission
    return spectrum