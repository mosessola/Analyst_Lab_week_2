# HealthConnect Clinic — Data Analytics Track

**Programme:** AnalystLab Africa Experience Lab
**Assignment:** Week 4 — HealthConnect Project Kickoff & Problem Understanding
**Track:** Data Analytics
**Status:** Week 4 deliverables complete

## What this project is

HealthConnect Clinic is a fictional outpatient healthcare provider used across all AnalystLab
Africa tracks as a shared case study, kicking off at **Week 4** of the internship (Weeks 1–3 were
separate, track-specific skill-building and are not repeated here). The central project question,
per the official Week 4 brief, is:

> *"How can HealthConnect Clinic use data and AI to reduce missed appointments and improve the
> patient support experience?"*

As the **Data Analytics track**, our Week 4 responsibility is to understand the appointment data
and identify how it can be used to investigate appointment attendance and no-show patterns —
laying groundwork the Data Science, ML Engineering, and Generative AI tracks build on in later
weeks. This is discovery and planning work: business questions, KPI identification (not yet
calculation), a data-quality assessment, and an initial analysis approach — not a finished model
or dashboard.

The `HealthConnect_Clinic_Knowledge_Base.docx` resource is also part of the shared project
resources, but its primary users are the **Generative AI track** (Healthcare Information
Assistant design). It's kept here for cross-track reference only and is not used in this
Data Analytics output.

## Folder structure

```
HealthConnect_Project/
├── README.md                                       This file
├── data/
│   ├── HealthConnect_Appointment_Data.csv                Raw dataset (5,000 rows x 18 cols) — unmodified
│   └── HealthConnect_Data_Dictionary.xlsx                Field definitions — unmodified
├── notebooks/
│   ├── HealthConnect_Week4_EDA.ipynb                     Executed Week 4 exploratory analysis
├── docs/
│   ├── HealthConnect_Week4_Analysis_Document.docx        Main Week 4 output: brief, role, data review,                                                          approach, assumptions/limitations/risks
│   ├── HealthConnect_Week4_Project_Summary.docx          Required Part 4 submission item: concise summary,
│   │                                                       does not repeat the analysis document
│   └── HealthConnect_Clinic_Knowledge_Base.docx          Generative AI track resource (reference only)

```

## Where to start

1. **`docs/HealthConnect_Week4_Project_Summary.docx`** — the short version: problem, resources,
   key observations, approach, considerations, and proposed Week 5 focus.
2. **`docs/HealthConnect_Week4_Analysis_Document.docx`** — the full Week 4 output: project brief,
   analyst role, data dictionary review, dataset inspection, full data-quality assessment,
   important-variable identification, 5 business questions, 5 KPIs (each explicitly linked to a
   business question, per the brief's requirement), initial analysis approach, and documented
   assumptions/limitations/risks.
3. **`notebooks/HealthConnect_Week4_EDA.ipynb`** — the executed code behind the analysis document:
   dataset inspection, data-quality checks, and the exploratory rate breakdowns used to identify
   important variables and justify the KPIs.

## Headline findings (Week 4)

- **48.5%** of appointments in the dataset end in **No-Show**, 46.3% Attended, 5.3% Cancelled.
- **Booking lead time** is the strongest signal found: no-show rate rises from **28%**
  (booked 0–7 days ahead) to **68%** (booked 46–60 days ahead).
- **Prior no-show history** is similarly strong: patients with 3+ previous no-shows show a
  **68–100%** no-show rate on their current appointment, vs. 44% for patients with no history.
- **Reminders** show a modest effect (47.4% no-show rate when sent vs. 51.4% when not), with
  **SMS** the best-performing channel among those tested.
- **Data quality is high**: no duplicate rows, all internal consistency rules hold. The only
  missingness is `reminder_channel` (fully explained by `reminder_sent = No`) and small gaps
  (<2%) in `distance_to_clinic_km` and `waiting_time_minutes`.

## KPIs identified (not yet calculated, per brief scope)

| KPI | Linked question(s) |
|---|---|
| No-Show Rate | Q1 |
| Attendance Rate | Q1 |
| Cancellation Rate | Q1, Q3 |
| Reminder Effectiveness | Q4 |
| Repeat No-Show Rate | Q2, Q5 |

Full definitions and justification in the Analysis Document, Section 10.

## Known open items going into Week 5

- Move from associative findings (Week 4) to significance-tested findings (chi-square /
  logistic regression).
- Decide and document a missing-data handling rule for `distance_to_clinic_km` and
  `waiting_time_minutes` before any calculation or modelling uses them.
- Confirm the 737 Sunday-dated appointments against real clinic operating-hours assumptions
  before using them in any hours-based segmentation.
- First KPI calculation pass, now that identification and justification are complete.
- Coordinate with the Data Science track on shared variable definitions for the no-show
  prediction model.


