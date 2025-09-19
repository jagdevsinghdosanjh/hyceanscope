import numpy as np

def simulate_spectrum(wavelengths, composition, method="simple"):
    if method == "Simple":
        return simulate_spectrum_simple(wavelengths, composition)
    elif method == "Radiative Transfer":
        return simulate_spectrum_rt(wavelengths, composition)

def simulate_spectrum_simple(wavelengths, composition):
    wavelengths = np.array(wavelengths)  # ✅ Convert list to NumPy array
    spectrum = np.ones_like(wavelengths)

    if "CH4" in composition:
        spectrum *= 1 - 0.05 * np.exp(-((wavelengths - 3.3)**2) / 0.1)
    if "H2O" in composition:
        spectrum *= 1 - 0.03 * np.exp(-((wavelengths - 2.7)**2) / 0.2)
    if "CO2" in composition:
        spectrum *= 1 - 0.04 * np.exp(-((wavelengths - 4.3)**2) / 0.15)

    return spectrum

# def simulate_spectrum_simple(wavelengths, composition):
#     spectrum = np.ones_like(wavelengths)
#     if 'CH4' in composition:
#         spectrum *= 1 - 0.05 * np.exp(-((wavelengths - 3.3)**2) / 0.1)
#     if 'H2O' in composition:
#         spectrum *= 1 - 0.03 * np.exp(-((wavelengths - 1.4)**2) / 0.05)
#     return spectrum

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

# import numpy as np

# def simulate_spectrum(wavelengths, composition):
#     spectrum = np.ones_like(wavelengths)
#     if 'CH4' in composition:
#         spectrum *= 1 - 0.05 * np.exp(-((wavelengths - 3.3)**2) / 0.1)
#     if 'H2O' in composition:
#         spectrum *= 1 - 0.03 * np.exp(-((wavelengths - 1.4)**2) / 0.05)
#     return spectrum
