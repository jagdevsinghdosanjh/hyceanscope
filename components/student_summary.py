import pandas as pd
import streamlit as st
import os

def show_student_summary(student_id):
    st.subheader(f"📘 Summary for: {student_id}")

    try:
        df = pd.read_csv("data/logs.csv", names=["timestamp", "student_id", "mass", "radius", "temp", "composition"])
    except FileNotFoundError:
        st.info("No submissions found.")
        return

    df = df[df["student_id"] == student_id]
    if df.empty:
        st.warning("No data found for this student.")
        return

    df["composition"] = df["composition"].fillna("").apply(lambda x: x.split(","))
    df["Hycean"] = df.apply(lambda row: 2 < row.mass < 10 and 1.5 < row.radius < 3.0 and 250 < row.temp < 350, axis=1)

    st.metric("Total Submissions", len(df))
    st.metric("Hycean Candidates", df["Hycean"].sum())

    st.write("### Submission History")
    st.dataframe(df[["timestamp", "mass", "radius", "temp", "composition", "Hycean"]])

    st.write("### Molecule Usage")
    all_mols = [mol for comp in df["composition"] for mol in comp]
    mol_counts = pd.Series(all_mols).value_counts()
    st.bar_chart(mol_counts)

    # Badge logic
    badge_files = ["gold.png", "silver.png", "bronze.png", "star.png"]
    badge_emojis = ["🥇", "🥈", "🥉", "🌟"]
    badge = badge_emojis[3]  # Default: 🌟

    if len(df) >= 10:
        badge = badge_emojis[0]
        badge_path = f"assets/badges/{badge_files[0]}"
    elif len(df) >= 7:
        badge = badge_emojis[1]
        badge_path = f"assets/badges/{badge_files[1]}"
    elif len(df) >= 4:
        badge = badge_emojis[2]
        badge_path = f"assets/badges/{badge_files[2]}"
    else:
        badge_path = f"assets/badges/{badge_files[3]}"

    st.subheader("🏅 Your Badge")
    if os.path.exists(badge_path):
        st.image(badge_path, width=60)
    else:
        st.markdown(f"{badge} Keep exploring!")
