import streamlit as st
from components.planet_input import get_planet_params
from components.spectral_plot import plot_spectrum
from components.habitability_predictor import is_hycean_candidate
from components.data_logger import log_run
from components.molecule_viewer import show_molecule

# from components.atmosphere_model import simulate_spectrum
st.set_page_config(page_title="HyceanScope", layout="wide")

st.title("🔭 HyceanScope: Explore Exoplanet Habitability")

# mass, radius, temp, composition = get_planet_params()
# wavelengths = [1.0 + 0.01*i for i in range(300)]  # 1–4 μm range
# spectrum = simulate_spectrum(wavelengths, composition)
mass, radius, temp, composition, method = get_planet_params()

if method == "Simple":
    from components.atmosphere_model import simulate_spectrum_simple as simulate_spectrum
else:
    from components.atmosphere_model import simulate_spectrum_rt as simulate_spectrum

wavelengths = [1.0 + 0.01*i for i in range(300)]
spectrum = simulate_spectrum(wavelengths, composition)

st.plotly_chart(plot_spectrum(wavelengths, spectrum), use_container_width=True)

if is_hycean_candidate(mass, radius, temp):
    st.success("🌊 This planet is a Hycean candidate!")
else:
    st.warning("🚫 Conditions not suitable for Hycean classification.")

log_run(mass, radius, temp, composition)

show_molecule(composition)

