import pandas as pd
import streamlit as st
import plotly.io as pio
from components.spectral_plot import plot_spectrum

def show_dashboard():
    st.subheader("📊 Educator Dashboard")

    try:
        df = pd.read_csv("data/logs.csv", names=["timestamp", "student_id", "mass", "radius", "temp", "composition"])
    except FileNotFoundError:
        st.info("No student data logged yet.")
        return

    df["composition"] = df["composition"].fillna("").apply(lambda x: x.split(","))
    df["Hycean"] = df.apply(lambda row: 2 < row.mass < 10 and 1.5 < row.radius < 3.0 and 250 < row.temp < 350, axis=1)

    st.metric("Total Runs", len(df))
    st.metric("Hycean Candidates", df["Hycean"].sum())

    st.write("### Hycean Classification Summary")
    st.bar_chart(df["Hycean"].value_counts())

    st.write("### Recent Submissions")
    st.dataframe(df.tail(10))

    st.write("### Biosignature Frequency")
    biosignatures = ["CH4", "CO2", "H2O", "CH3Cl", "DMS"]
    counts = {bio: sum(bio in comp for comp in df["composition"]) for bio in biosignatures}
    st.bar_chart(pd.Series(counts))

    show_leaderboard(df)

def export_tools(df, wavelengths=None, spectrum=None):
    st.subheader("📤 Export Tools")

    # Export logs as CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📁 Download Logs (CSV)", data=csv, file_name="hyceanscope_logs.csv", mime="text/csv")

    # Export spectrum as PNG
    if wavelengths and spectrum is not None:
        fig = plot_spectrum(wavelengths, spectrum)
        png_bytes = pio.to_image(fig, format="png")
        st.download_button("🖼️ Download Spectrum (PNG)", data=png_bytes, file_name="spectrum.png", mime="image/png")

def show_leaderboard(df):
    st.subheader("🏆 Classroom Leaderboard")

    leaderboard = df["student_id"].value_counts().head(5)
    st.write("Top Contributors:")
    st.bar_chart(leaderboard)
