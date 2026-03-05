import streamlit as st
import pandas as pd

st.set_page_config(page_title="WA Information Portal", page_icon="📚")

st.title("2026 WA Information Portal")

st.write("Parents can check their child's WA dates and topics.")

st.divider()

# Load Excel file
import os

file_path = os.path.join(os.path.dirname(__file__), "wa_information_2026.csv")
df = pd.read_csv(file_path)

# Convert index numbers
df["Index Number"] = df["Index Number"].astype(int)

# User inputs
class_input = st.selectbox(
    "Select Class",
    sorted(df["Class"].unique())
)

index_input = st.number_input(
    "Enter Index Number",
    min_value=1,
    max_value=40,
    step=1
)

if st.button("Check WA Information"):

    student = df[
        (df["Class"] == class_input) &
        (df["Index Number"] == index_input)
    ]

    if not student.empty:

        row = student.iloc[0]

        st.subheader("WA Schedule")

        st.write("English WA:", row["English WA"])
        st.write("Topic:", row["English WA Topic"])

        st.write("Math WA:", row["Maths WA"])
        st.write("Topic:", row["Maths WA Topic"])

        st.write("Science WA:", row["Science WA"])
        st.write("Topic:", row["Science WA Topic"])

        st.write("Mother Tongue WA:", row["Mother Tongue WA"])
        st.write("Topic:", row["Mother Tongue WA Topic"])

    else:
        st.error("Student not found.")
