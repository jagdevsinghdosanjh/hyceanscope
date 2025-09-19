import streamlit as st

def get_planet_params():
    st.sidebar.header("Planetary Parameters")
    student_id = st.sidebar.text_input("Student ID or Name", value="anonymous")
    mass = st.sidebar.slider("Mass (Earth Masses)", 1.0, 15.0, 5.0)
    radius = st.sidebar.slider("Radius (Earth Radii)", 1.0, 4.0, 2.5)
    temp = st.sidebar.slider("Equilibrium Temp (K)", 150, 500, 300)
    composition = st.sidebar.multiselect("Atmospheric Composition", ["H2", "CH4", "CO2", "H2O", "CH3Cl", "DMS"])
    method = st.sidebar.radio("Spectral Simulation Method", ["Simple", "Radiative Transfer"])
    return student_id, mass, radius, temp, composition, method

# def get_planet_params():
#     st.sidebar.header("Planetary Parameters")
#     mass = st.sidebar.slider("Mass (Earth Masses)", 1.0, 15.0, 5.0)
#     radius = st.sidebar.slider("Radius (Earth Radii)", 1.0, 4.0, 2.5)
#     temp = st.sidebar.slider("Equilibrium Temp (K)", 150, 500, 300)
#     composition = st.sidebar.multiselect("Atmospheric Composition", ["H2", "CH4", "CO2", "H2O"])
#     return mass, radius, temp, composition

# def get_planet_params():
#     st.sidebar.header("Planetary Parameters")
#     mass = st.sidebar.slider("Mass (Earth Masses)", 1.0, 15.0, 5.0)
#     radius = st.sidebar.slider("Radius (Earth Radii)", 1.0, 4.0, 2.5)
#     temp = st.sidebar.slider("Equilibrium Temp (K)", 150, 500, 300)
#     composition = st.sidebar.multiselect("Atmospheric Composition", ["H2", "CH4", "CO2", "H2O"])
#     method = st.sidebar.radio("Spectral Simulation Method", ["Simple", "Radiative Transfer"])
#     return mass, radius, temp, composition, method

