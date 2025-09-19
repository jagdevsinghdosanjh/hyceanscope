import streamlit as st
import pandas as pd
from components.planet_input import get_planet_params
from components.spectral_plot import plot_spectrum
from components.habitability_predictor import is_hycean_candidate
from components.data_logger import log_run
from components.molecule_viewer import show_molecule
from components.atmosphere_model import simulate_spectrum
from components.educator_dashboard import show_dashboard, export_tools
from components.student_summary import show_student_summary

# Page setup
st.set_page_config(page_title="HyceanScope", layout="wide")

# Title
st.title("🔭 HyceanScope: Explore Exoplanet Habitability")

# Sidebar input
student_id, mass, radius, temp, composition, method = get_planet_params()
show_student_summary(student_id)


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
log_run(student_id, mass, radius, temp, composition)

# Molecule viewer
st.subheader("🧪 Molecular Preview")
show_molecule(composition)

# Educator dashboard
st.markdown("---")
show_dashboard()

# Export buttons
try:
    df = pd.read_csv("data/logs.csv", names=["timestamp", "student_id", "mass", "radius", "temp", "composition"])
    export_tools(df, wavelengths, spectrum)
except FileNotFoundError:
    st.info("No logs available for export.")
