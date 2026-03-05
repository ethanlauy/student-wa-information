import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="WA Information Portal", page_icon="📚")

st.title("2026 WA Information Portal")
st.write("Parents can check their child's WA dates and topics.")

# Load CSV and skip the title row
file_path = os.path.join(os.path.dirname(__file__), "wa_information_2026(Sheet1).csv")
df = pd.read_csv(file_path, skiprows=1)

# Clean column names
df.columns = df.columns.str.strip()

st.divider()

# Parent inputs
class_input = st.text_input("Enter your child's class (Example: 3P)")
index_input = st.text_input("Enter your child's index number")
name_input = st.text_input("Enter your child's name")

if st.button("Check WA Schedule"):

    if class_input == "" or index_input == "" or name_input == "":
        st.error("Please fill in all fields.")

    else:

        try:
            index_input = int(index_input)

            student = df[
                (df["Class"].str.lower() == class_input.lower()) &
                (df["Index Number"] == index_input) &
                (df["Name"].str.lower() == name_input.lower())
            ]

            if student.empty:
                st.error("The details entered are incorrect. Please check again.")

            else:

                student = student.iloc[0]

                st.success("Student verified successfully.")

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
                        st.markdown("### Mathematics")
                        st.write("Date:", student["Maths WA"])
                        st.write("Topic:", student["Maths WA Topic"])

                    with st.container(border=True):
                        st.markdown("### Mother Tongue")
                        st.write("Date:", student["Mother Tongue WA"])
                        st.write("Topic:", student["Mother Tongue WA Topic"])

        except:
            st.error("Index number must be a number.")
