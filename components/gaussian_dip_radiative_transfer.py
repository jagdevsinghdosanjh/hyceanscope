def simulate_spectrum(wavelengths, composition, method="simple"):
    if method == "simple":
        return simulate_simple(wavelengths, composition)
    elif method == "rt":
        return simulate_radiative_transfer(wavelengths, composition)
