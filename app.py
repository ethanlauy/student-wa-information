import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="WA Information Portal", page_icon="📚")

st.title("2026 WA Information Portal")
st.write("Parents can check their child's WA dates and topics.")

# Load CSV safely
file_path = os.path.join(os.path.dirname(__file__), "wa_information_2026.csv")
df = pd.read_csv(file_path)

# Clean column names (removes hidden spaces from Excel)
df.columns = df.columns.str.strip()

# Rename columns just in case Excel renamed them
df = df.rename(columns={
    df.columns[0]: "Index Number",
    df.columns[1]: "Class"
})

# Convert index numbers
df["Index Number"] = pd.to_numeric(df["Index Number"], errors="coerce")

# Remove rows with missing index
df = df.dropna(subset=["Index Number"])

df["Index Number"] = df["Index Number"].astype(int)

st.divider()

# Select class
class_input = st.selectbox(
    "Select your child's class",
    sorted(df["Class"].unique())
)

# Filter students from class
class_df = df[df["Class"] == class_input]

# Select index number
index_input = st.selectbox(
    "Select your child's index number",
    sorted(class_df["Index Number"].unique())
)

if st.button("Show WA Information"):

    student = class_df[class_df["Index Number"] == index_input].iloc[0]

    st.subheader("WA Schedule")

    st.markdown(f"**English WA:** {student['English WA']}")
    st.markdown(f"Topic: {student['English WA Topic']}")

    st.markdown(f"**Math WA:** {student['Maths WA']}")
    st.markdown(f"Topic: {student['Maths WA Topic']}")

    st.markdown(f"**Science WA:** {student['Science WA']}")
    st.markdown(f"Topic: {student['Science WA Topic']}")

    st.markdown(f"**Mother Tongue WA:** {student['Mother Tongue WA']}")
    st.markdown(f"Topic: {student['Mother Tongue WA Topic']}")
