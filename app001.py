import streamlit as st
from components.planet_input import get_planet_params
from components.spectral_plot import plot_spectrum
from components.habitability_predictor import is_hycean_candidate
from components.data_logger import log_run
from components.molecule_viewer import show_molecule
from components.atmosphere_model import simulate_spectrum
from components.educator_dashboard import show_dashboard
from components.educator_dashboard import show_dashboard, export_tools

# Show dashboard
st.markdown("---")
show_dashboard()

# Page setup
st.set_page_config(page_title="HyceanScope", layout="wide")

# Title
st.title("🔭 HyceanScope: Explore Exoplanet Habitability")

# Sidebar input
mass, radius, temp, composition, method = get_planet_params()

# Wavelength range
wavelengths = [1.0 + 0.01 * i for i in range(300)]  # 1–4 μm

# Spectrum simulation
spectrum = simulate_spectrum(wavelengths, composition, method)

# Plot spectrum
st.subheader("📈 Transmission Spectrum")
st.plotly_chart(plot_spectrum(wavelengths, spectrum), use_container_width=True)

# Habitability check
st.subheader("🧠 Hycean Classification")
if is_hycean_candidate(mass, radius, temp):
    st.success("🌊 This planet is a Hycean candidate!")
else:
    st.warning("🚫 Conditions not suitable for Hycean classification.")

# Log the run
log_run(mass, radius, temp, composition)

# Molecule viewer
st.subheader("🧪 Molecular Preview")
show_molecule(composition)

# Export buttons
try:
    import pandas as pd
    df = pd.read_csv("data/logs.csv", names=["timestamp", "mass", "radius", "temp", "composition"])
    export_tools(df, wavelengths, spectrum)
except:
    st.info("No logs available for export.")
