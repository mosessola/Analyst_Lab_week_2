# HealthConnect Clinic — Data Analytics Track

**Programme:** AnalystLab Africa Experience Lab
**Track:** Data Analytics
**Status:** Week 4 (Problem Understanding) and Week 5 (Analysis & KPI Development) complete

## What this project is

HealthConnect Clinic is a fictional outpatient healthcare provider used across all AnalystLab
Africa tracks as a shared case study. The central project question, per the official brief, is:

> *"How can HealthConnect Clinic use data and AI to reduce missed appointments and improve the
> patient support experience?"*

As the **Data Analytics track**, Week 4 covered problem understanding, data-quality assessment,
and identifying business questions and candidate KPIs. **Week 5 moved into actual analysis** —
calculating those KPIs, deepening the exploratory analysis, building a visual dashboard, and
producing business insights, building directly on the Week 4 foundation (not restarting).

The `HealthConnect_Clinic_Knowledge_Base.docx` resource is part of the shared project resources,
but its primary users are the **Generative AI track**. It's kept here for cross-track reference
only and is not used in this Data Analytics output.

## Folder structure

```
HealthConnect_Project/
├── README.md
├── data/
│   ├── HealthConnect_Appointment_Data.csv              Raw dataset (5,000 rows x 18 cols) — unmodified
│   └── HealthConnect_Data_Dictionary.xlsx               Field definitions — unmodified
├── notebooks/
│   ├── HealthConnect_Week5_Analytics.ipynb              Week 5: deepened EDA, KPI calculations, dashboard
│   ├── build_notebook.py / build_week5_notebook.py      Scripts that generate the notebooks (reproducibility)
├── docs/
│   ├── HealthConnect_Week4_Analysis_Document.docx/.pdf  Week 4 output: brief, role, data review, data quality,
│   │                                                      business questions, KPIs identified+linked, approach,
│   │                                                      assumptions/limitations/risks
│   ├── HealthConnect_Week4_Project_Summary.docx/.pdf    Week 4 Part 4 submission summary
│   ├── HealthConnect_Week5_Analytics_Report.docx/.pdf   Week 5 output: Week 4 recap, data prep confirmation,
│   │                                                      deepened EDA, 5 calculated KPIs, dashboard, 6 business
│   │                                                      insights, cross-track note, updated risk register
│   ├── HealthConnect_Week5_Project_Summary.docx/.pdf    Week 5 Part 4 submission summary 
├── outputs/
│   ├── waiting_distance_by_outcome.png                  Week 5 chart
│   └── week5_kpi_dashboard.png                          Week 5 4-panel dashboard
```

## Where to start

- **This week (Week 5):** start with `docs/HealthConnect_Week5_Project_Summary.pdf` (short
  version), then `docs/HealthConnect_Week5_Analytics_Report.pdf` (full report with KPI
  calculations and dashboard), then `notebooks/HealthConnect_Week5_Analytics.ipynb` for the code.
- **Prior week (Week 4):** `docs/HealthConnect_Week4_Analysis_Document.pdf` and
  `docs/HealthConnect_Week4_Project_Summary.pdf`.

## Week 5 headline results

**KPIs calculated:**

| KPI | Linked question(s) | Value |
|---|---|---|
| No-Show Rate | Q1 | 48.5% |
| Attendance Rate | Q1 | 46.3% |
| Cancellation Rate | Q1, Q3 | 5.3% |
| Reminder Effectiveness | Q4 | 47.4% (sent) vs 51.4% (not sent); SMS best channel |
| Repeat No-Show Rate | Q2, Q5 | 10.6% of appointments from patients w/ ≥2 prior no-shows; 61.0% no-show rate within that segment |

**Key business insights:**

- Booking lead time and prior no-show history remain the two strongest, and largely independent, drivers.
- Cancellations behave differently from no-shows (flat ~5% rate vs. lead time) — validates treating them separately.
- Reminders help modestly; SMS is the best channel, but reminders alone won't fix a 48.5% no-show rate.
- Waiting time and distance to clinic remain weak standalone predictors.

## Known open items going into Week 6

- Move from associative findings to statistically significance-tested findings (chi-square / logistic regression).
- Test further variable interactions beyond lead time × prior no-shows.
- Resolve carried-forward Week 4 items: Sunday-appointment operating-hours question, and a documented missing-data handling rule for distance/waiting time.
- Translate business insights into a stakeholder-ready recommendation with estimated impact.

