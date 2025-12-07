import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Google API scopes
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Sheet name (must match your Google Sheet EXACTLY)
SHEET_NAME = "Coding_Club_Registrations"


def get_sheet():
    """
    Connect to Google Sheets using Streamlit secrets.
    THIS replaces the local service_account.json method.
    """
    creds_dict = st.secrets["gcp_service_account"]   # get secrets from Streamlit Cloud
    creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).sheet1
    return sheet


def get_all_data():
    """Return all records from the sheet."""
    sheet = get_sheet()
    return sheet.get_all_records()


def is_duplicate(register_no: str) -> bool:
    """Check if register number already exists."""
    sheet = get_sheet()
    reg_values = sheet.col_values(3)   # column C = Register No
    return register_no in reg_values


def add_student(
    name: str,
    reg_no: str,
    email: str,
    mobile: str,
    gender: str,
    stay_type: str,
    department: str,
    interests: list,
    languages: list,
):
    """
    Add a new student row with auto serial number.
    """
    sheet = get_sheet()
    data = sheet.get_all_records()
    serial_no = len(data) + 1  # auto-increment serial number

    interests_str = ", ".join(interests) if interests else ""
    languages_str = ", ".join(languages) if languages else ""

    row = [
        serial_no,
        name,
        reg_no,
        email,
        mobile,
        gender,
        stay_type,
        department,
        interests_str,
        languages_str
    ]

    sheet.append_row(row)
