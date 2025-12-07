# app.py

import streamlit as st
from sheets import is_duplicate, add_student

st.set_page_config(page_title="Coding Club Registration", page_icon="🧠")

st.title(" CODING CLUB REGISTRATION FORM")
st.caption("Never be Quit to Learn")

st.write(
    "Fill this form to join the Coding Club. "
    "**Use your correct register number and email.**"
)

# ----- FORM FIELDS -----
name = st.text_input("Full Name")
reg_no = st.text_input("Register Number")
email = st.text_input("Email")
mobile = st.text_input("Mobile Number")

gender = st.radio("Gender", ["Male", "Female", "Other"], horizontal=True)

stay_type = st.radio("Stay Type", ["Hostel", "Day Scholar"], horizontal=True)

department = st.selectbox(
    "Department",
    ["CSE", "AI"]
)

interests = st.multiselect(
    "Interests",
    ["AI", "DSA Problem Solving", "Full Stack", "Others"],
)

languages = st.multiselect(
    "Programming Languages",
    ["Python", "C", "C++", "Java", "HTML/CSS", "Others"],
)

st.divider()

# ----- VALIDATION + SUBMIT -----
if st.button("Submit Registration", type="primary"):
    # Basic validation
    if not name or not reg_no or not email or not mobile:
        st.error("❌ Please fill all required fields (Name, Register No, Email, Mobile).")
    else:
        # Duplicate check
        if is_duplicate(reg_no):
            st.error("⚠️ This Register Number is already registered.")
        else:
            try:
                add_student(
                    name=name,
                    reg_no=reg_no,
                    email=email,
                    mobile=mobile,
                    gender=gender,
                    stay_type=stay_type,
                    department=department,
                    interests=interests,
                    languages=languages,
                )
                st.success("✅ Registration successful! Welcome to the Coding Club 🎉")
            except Exception as e:
                st.error(f"Something went wrong while saving your data: {e}")
