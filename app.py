import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="WA Information Portal", page_icon="📚")

st.title("2026 WA Information Portal")
st.write("Parents can check their child's WA dates and topics.")

# Load CSV file
file_path = os.path.join(os.path.dirname(__file__), "wa_information_2026.csv")
df = pd.read_csv(file_path, skiprows=1)

# Clean column names
df.columns = df.columns.str.strip()

# Ensure index numbers are integers
df["Index Number"] = pd.to_numeric(df["Index Number"], errors="coerce")
df = df.dropna(subset=["Index Number"])
df["Index Number"] = df["Index Number"].astype(int)

st.divider()

# Select class
class_input = st.selectbox(
    "Select your child's class",
    sorted(df["Class"].unique())
)

# Filter class
class_df = df[df["Class"] == class_input]

# Select index number
index_input = st.selectbox(
    "Select your child's index number",
    sorted(class_df["Index Number"].unique())
)

if st.button("Show WA Information"):

    student = class_df[class_df["Index Number"] == index_input].iloc[0]

    st.subheader("WA Schedule")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### English")
            st.write("Date:", student["English WA"])
            st.write("Topic:", student["English WA Topic"])

        with st.container(border=True):
            st.markdown("### Science")
            st.write("Date:", student["Science WA"])
            st.write("Topic:", student["Science WA Topic"])

    with col2:
        with st.container(border=True):
            st.markdown("### Math")
            st.write("Date:", student["Maths WA"])
            st.write("Topic:", student["Maths WA Topic"])

        with st.container(border=True):
            st.markdown("### Mother Tongue")
            st.write("Date:", student["Mother Tongue WA"])
            st.write("Topic:", student["Mother Tongue WA Topic"])
