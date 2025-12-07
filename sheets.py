# sheets.py

import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Google API scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Google Sheet name (must match exactly)
SHEET_NAME = "Coding_Club_Registrations"


def get_sheet():
    """
    Connect to Google Sheets and return the first worksheet.
    Uses service_account.json in the same folder.
    """
    creds = Credentials.from_service_account_file(
        "service_account.json", scopes=SCOPE
    )
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).sheet1
    return sheet


def get_all_data():
    """Return all rows as a list of dicts."""
    sheet = get_sheet()
    return sheet.get_all_records()


def is_duplicate(register_no: str) -> bool:
    """
    Check if a given Register No already exists in the sheet.
    Register No column = Column C = index 3.
    """
    sheet = get_sheet()
    reg_values = sheet.col_values(3)  # C column: Register No
    # First value is header "Register No", rest are data
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
    Append a new student row with auto Serial No.
    Columns:
    A: Serial No
    B: Name
    C: Register No
    D: Email
    E: Mobile
    F: Gender
    G: Stay Type
    H: Department
    I: Interests (comma separated)
    J: Languages (comma separated)
    """

    sheet = get_sheet()
    existing_data = sheet.get_all_records()
    serial_no = len(existing_data) + 1  # auto serial

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
        languages_str,
    ]

    sheet.append_row(row)
