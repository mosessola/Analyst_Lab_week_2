# ============================================================
# HEALTHCONNECT CLINIC
# WEEK 6 — ADVANCED ANALYTICS & DECISION SUPPORT
# DATA ANALYTICS TRACK
# ============================================================

# ------------------------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
from pathlib import Path


# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

file_path = Path(__file__).resolve().parent / "HealthConnect_Appointment_Data.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("HEALTHCONNECT WEEK 6 — DATA LOADED")
print("=" * 60)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nColumn names:")
print(df.columns.tolist())
# ------------------------------------------------------------
# 3. BASIC DATA VALIDATION
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("BASIC DATA VALIDATION")
print("=" * 60)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nAppointment outcome distribution:")
print(df["appointment_outcome"].value_counts())
# ------------------------------------------------------------
# 4. WEEK 6 BASELINE KPIs
# ------------------------------------------------------------

total_appointments = len(df)

no_shows = (df["appointment_outcome"] == "No-Show").sum()
attended = (df["appointment_outcome"] == "Attended").sum()
cancelled = (df["appointment_outcome"] == "Cancelled").sum()

no_show_rate = no_shows / total_appointments * 100
attendance_rate = attended / total_appointments * 100
cancellation_rate = cancelled / total_appointments * 100

print("\n" + "=" * 60)
print("WEEK 6 BASELINE KPIs")
print("=" * 60)

print(f"Total appointments: {total_appointments:,}")
print(f"No-show rate: {no_show_rate:.1f}%")
print(f"Attendance rate: {attendance_rate:.1f}%")
print(f"Cancellation rate: {cancellation_rate:.1f}%")