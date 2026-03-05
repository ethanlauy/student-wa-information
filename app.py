import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="WA Information Portal", page_icon="📚")

st.title("2026 WA Information Portal")
st.write("Parents can check their child's WA dates and topics.")

# Load CSV
file_path = os.path.join(os.path.dirname(__file__), "wa_information_2026.csv")
df = pd.read_csv(file_path)

# Clean column names (remove spaces, weird characters)
df.columns = df.columns.str.strip()

# Show columns in logs (helps debugging)
st.write("Loaded columns:", df.columns)

# Rename columns safely
df = df.rename(columns={
    df.columns[0]: "Index Number",
    df.columns[1]: "Class"
})

# Convert index numbers
df["Index Number"] = pd.to_numeric(df["Index Number"], errors="coerce")
df = df.dropna(subset=["Index Number"])
df["Index Number"] = df["Index Number"].astype(int)

st.divider()

# Parent selects class
class_input = st.selectbox(
    "Select your child's class",
    sorted(df["Class"].unique())
)

# Filter students
class_df = df[df["Class"] == class_input]

# Parent selects index
index_input = st.selectbox(
    "Select your child's index number",
    sorted(class_df["Index Number"].unique())
)

if st.button("Show WA Information"):

    student = class_df[class_df["Index Number"] == index_input].iloc[0]

    st.subheader("WA Schedule")

    st.write("English WA:", student["English WA"])
    st.write("English Topic:", student["English WA Topic"])

    st.write("Math WA:", student["Maths WA"])
    st.write("Math Topic:", student["Maths WA Topic"])

    st.write("Science WA:", student["Science WA"])
    st.write("Science Topic:", student["Science WA Topic"])

    st.write("Mother Tongue WA:", student["Mother Tongue WA"])
    st.write("Mother Tongue Topic:", student["Mother Tongue WA Topic"])
