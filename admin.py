# admin.py

import streamlit as st
import pandas as pd
from sheets import get_all_data

st.set_page_config(page_title="Coding Club Admin", page_icon="🛠️")

st.title(" Coding Club - Admin Dashboard")

# (Optional) Simple password protection
password = st.text_input("Enter password", type="password")
CORRECT_PASSWORD = "club25"

if password != CORRECT_PASSWORD:
    st.warning("Enter the correct password to view Registered Members.")
    st.stop()

data = get_all_data()

if not data:
    st.info("No registrations yet.")
else:
    df = pd.DataFrame(data)
    st.subheader(" Registered Coders")
    st.dataframe(df, use_container_width=True)

    # Download as CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇ Download as CSV",
        data=csv,
        file_name="coding_club_registrations.csv",
        mime="text/csv",
    )

