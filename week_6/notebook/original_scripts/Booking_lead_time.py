import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from pathlib import Path
import statsmodels.formula.api as smf


file_path = Path(__file__).resolve().parent / "HealthConnect_Appointment_Data.csv"
df = pd.read_csv(file_path)


# ------------------------------------------------------------
# 5. ANALYSIS 1 — BOOKING LEAD TIME
# ------------------------------------------------------------

df["lead_time_group"] = pd.cut(
    df["booking_lead_days"],
    bins=[-1, 7, 14, 30, 45, 60, np.inf],
    labels=[
        "0-7 days",
        "8-14 days",
        "15-30 days",
        "31-45 days",
        "46-60 days",
        "61+ days"
    ]
)
df["lead_time_group"] = df["lead_time_group"].cat.remove_unused_categories()

lead_time_table = pd.crosstab(
    df["lead_time_group"],
    df["appointment_outcome"]
)

print("\n" + "=" * 60)
print("BOOKING LEAD TIME × APPOINTMENT OUTCOME")
print("=" * 60)

print(lead_time_table)

lead_time_rates = (
    df.groupby("lead_time_group", observed=True)["appointment_outcome"]
    .apply(lambda x: (x == "No-Show").mean() * 100)
)

print("\nNo-show rate by booking lead time:")
print(lead_time_rates.round(2))
# ------------------------------------------------------------
# CHI-SQUARE TEST
# ------------------------------------------------------------

chi2, p_value, degrees_of_freedom, expected = chi2_contingency(
    lead_time_table
)

print("\n" + "=" * 60)
print("CHI-SQUARE TEST — BOOKING LEAD TIME")
print("=" * 60)

print(f"Chi-square statistic: {chi2:.4f}")
print(f"Degrees of freedom: {degrees_of_freedom}")
print(f"P-value: {p_value:.6f}")

alpha = 0.05

if p_value < alpha:
    print("Decision: Reject H0")
    print("Conclusion: Booking lead time is statistically associated")
    print("with appointment outcome.")
else:
    print("Decision: Fail to reject H0")
    print("Conclusion: There is insufficient evidence of an")
    print("association between booking lead time and appointment outcome.")
    # ------------------------------------------------------------
# CRAMER'S V — EFFECT SIZE
# ------------------------------------------------------------

n = lead_time_table.to_numpy().sum()
min_dimension = min(lead_time_table.shape) - 1

cramers_v = np.sqrt(
    chi2 / (n * min_dimension)
)

print("\nCramer's V:")
print(f"{cramers_v:.4f}")
# ============================================
# TEST 2: PREVIOUS NO-SHOW HISTORY
# ============================================

# Create previous no-show groups
df["previous_no_show_group"] = pd.cut(
    df["previous_no_shows"],
    bins=[-1, 0, 1, np.inf],
    labels=[
        "0 previous no-shows",
        "1 previous no-show",
        "2+ previous no-shows"
    ]
)

# Create contingency table
previous_no_show_table = pd.crosstab(
    df["previous_no_show_group"],
    df["appointment_outcome"]
)

print("\nPrevious No-Show History vs Appointment Outcome:")
print(previous_no_show_table)

# Calculate no-show rate for each group
no_show_rate_history = (
    df.assign(
        is_no_show=df["appointment_outcome"].eq("No-Show")
    )
    .groupby("previous_no_show_group", observed=False)["is_no_show"]
    .mean() * 100
)

print("\nNo-Show Rate by Previous No-Show History:")
print(no_show_rate_history.round(2))
# Chi-square test of independence
chi2, p_value, dof, expected = chi2_contingency(
    previous_no_show_table
)

print("\nChi-Square Test:")
print(f"Chi-square statistic: {chi2:.4f}")
print(f"Degrees of freedom: {dof}")
print(f"P-value: {p_value:.6f}")

# Decision
alpha = 0.05

if p_value < alpha:
    print("Decision: Reject H0")
    print(
        "Conclusion: Previous no-show history is "
        "statistically associated with appointment outcome."
    )
else:
    print("Decision: Fail to reject H0")
    print(
        "Conclusion: There is not enough evidence of a "
        "statistically significant association."
    )
    # Cramer's V for previous no-show history
n = previous_no_show_table.to_numpy().sum()
min_dimension = min(previous_no_show_table.shape) - 1

cramers_v = np.sqrt(
    chi2 / (n * min_dimension)
)

print("\nCramer's V:")
print(f"{cramers_v:.4f}")
# ============================================
# TEST 3: REMINDER EFFECTIVENESS
# ============================================

print("\n" + "=" * 60)
print("REMINDER STATUS × APPOINTMENT OUTCOME")
print("=" * 60)

# Create contingency table
reminder_table = pd.crosstab(
    df["reminder_sent"],
    df["appointment_outcome"]
)

print(reminder_table)

# Calculate no-show rate
reminder_no_show_rate = (
    df.assign(
        is_no_show=df["appointment_outcome"].eq("No-Show")
    )
    .groupby("reminder_sent", observed=False)["is_no_show"]
    .mean() * 100
)

print("\nNo-Show Rate by Reminder Status:")
print(reminder_no_show_rate.round(2))
# ============================================
# CHI-SQUARE TEST — REMINDER EFFECTIVENESS
# ============================================

chi2, p_value, dof, expected = chi2_contingency(
    reminder_table
)

print("\n" + "=" * 60)
print("CHI-SQUARE TEST — REMINDER EFFECTIVENESS")
print("=" * 60)

print(f"Chi-square statistic: {chi2:.4f}")
print(f"Degrees of freedom: {dof}")
print(f"P-value: {p_value:.6f}")

alpha = 0.05

if p_value < alpha:
    print("Decision: Reject H0")
    print(
        "Conclusion: Reminder status is statistically associated "
        "with appointment outcome."
    )
else:
    print("Decision: Fail to reject H0")
    print(
        "Conclusion: There is not enough evidence of a "
        "statistically significant association."
    )
    # Cramer's V for reminder effectiveness
n = reminder_table.to_numpy().sum()
min_dimension = min(reminder_table.shape) - 1

cramers_v = np.sqrt(
    chi2 / (n * min_dimension)
)

print("\nCramer's V:")
print(f"{cramers_v:.4f}")
# ============================================
# PHASE 4 — INTERACTION ANALYSIS
# INTERACTION 1: REMINDER × PREVIOUS NO-SHOWS
# ============================================

print("\n" + "=" * 60)
print("REMINDER EFFECTIVENESS BY PREVIOUS NO-SHOW HISTORY")
print("=" * 60)

# Calculate no-show rate for each combination
reminder_history_rate = (
    df.assign(
        is_no_show=df["appointment_outcome"].eq("No-Show")
    )
    .groupby(
        ["previous_no_show_group", "reminder_sent"],
        observed=False
    )["is_no_show"]
    .mean() * 100
)

print("\nNo-Show Rate:")
print(reminder_history_rate.round(2))
# Reshape results for easier comparison
reminder_history_table = reminder_history_rate.unstack()

print("\nReminder × Previous No-Show Comparison:")
print(reminder_history_table.round(2))
# Calculate the reminder effect within each previous no-show group
reminder_effect = (
    reminder_history_table["No"] -
    reminder_history_table["Yes"]
)

print("\nReminder Effect by Previous No-Show History:")
print(reminder_effect.round(2))

print("\nInterpretation:")
for group, effect in reminder_effect.items():
    print(
        f"{group}: {effect:.2f} percentage-point reduction "
        "in no-show rate when a reminder was sent."
    )
    # ============================================
# FORMAL INTERACTION TEST
# REMINDER × PREVIOUS NO-SHOW HISTORY
# ============================================

print("\n" + "=" * 60)
print("INTERACTION TEST — REMINDER × PREVIOUS NO-SHOW HISTORY")
print("=" * 60)

# Create binary no-show outcome
df["is_no_show"] = (
    df["appointment_outcome"] == "No-Show"
).astype(int)

# Convert reminder status to binary
df["reminder_binary"] = (
    df["reminder_sent"] == "Yes"
).astype(int)

# Logistic regression with interaction
interaction_model = smf.logit(
    "is_no_show ~ reminder_binary * previous_no_shows",
    data=df
).fit(disp=False)

print(interaction_model.summary())
print("\n" + "=" * 60)
print("REMINDER EFFECTIVENESS BY BOOKING LEAD TIME")
print("=" * 60)

reminder_lead_table = pd.crosstab(
    df["lead_time_group"],
    df["reminder_sent"],
    values=df["is_no_show"],
    aggfunc="mean"
) * 100

print("\nNo-Show Rate:")
print(reminder_lead_table.round(2))
lead_interaction_model = smf.logit(
    "is_no_show ~ reminder_binary * C(lead_time_group)",
    data=df
).fit(disp=False)

print("\n" + "=" * 60)
print("INTERACTION TEST — REMINDER × BOOKING LEAD TIME")
print("=" * 60)

print(lead_interaction_model.summary())