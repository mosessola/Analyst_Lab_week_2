# HealthConnect Clinic — Data Analytics Track

**Programme:** AnalystLab Africa Experience Lab
**Track:** Data Analytics
**Status:** Week 4 (Problem Understanding), Week 5 (Analysis & KPI Development), and Week 6
(Advanced Analytics & Decision Support) complete

## What this project is

HealthConnect Clinic is a fictional outpatient healthcare provider used across all AnalystLab
Africa tracks as a shared case study. The central project question is:

> *"How can HealthConnect Clinic use data and AI to reduce missed appointments and improve the
> patient support experience?"*

Progress so far, as the **Data Analytics track**:

- **Week 4:** problem understanding, data-quality assessment, business questions, KPIs identified (not calculated).
- **Week 5:** moved into analysis — calculated the 5 KPIs, deepened EDA, built a dashboard, produced 6 business insights.
- **Week 6:** did **not** repeat Week 5. Instead: statistically validated the 3 strongest Week 5 findings (chi-square tests, effect sizes), formally tested 2 segments Week 5 never tested (appointment type, reminder channel), ran interaction and multivariate models, refined the dashboard into a decision-support tool, and completed a real cross-track integration with the Data Science track (a concrete feature-relevance artefact, not just a conversation).

The `HealthConnect_Clinic_Knowledge_Base.docx` resource is part of the shared project resources,
but its primary users are the **Generative AI track**. It's kept here for cross-track reference
only and is not used in this Data Analytics output.

## Folder structure

```
HealthConnect_Project/week6
├── README.md
├── data/
│   ├── HealthConnect_Appointment_Data.csv                     Raw dataset — unmodified
│   └── HealthConnect_Data_Dictionary.xlsx                      Field definitions — unmodified
├── notebooks/
│   ├── HealthConnect_Week6_Advanced_Analytics.ipynb            Week 6: statistical validation, interaction models,
│   │                                                             refined dashboard, cross-track artefact generation
│   ├── original_scripts/                                       Original standalone scripts (statistical testing
│   │   ├── HealthConnect_Week6_Advanced_Analytics.py             logic) that Week 6's notebook is built from and
│   │   └── Booking_lead_time.py                                  extends with additional segment tests
│   ├── build_notebook.py / build_week5_notebook.py / build_week6_notebook.py   Notebook build scripts
│   └── preview*.html                                           HTML exports of each executed notebook
├── docs/
│   ├── HealthConnect_Week6_Advanced_Analytics_Report.docx/.pdf Week 6 main output: integration readiness, stat
│   │                                                             validation, new segment tests, interaction models,
│   │                                                             refined dashboard, actions, cross-track integration,
│   │                                                             updated risk register
│   ├── HealthConnect_Week6_Project_Summary.docx/.pdf           Week 6 Part 4 summary (13 required points)
│   └── HealthConnect_Clinic_Knowledge_Base.docx                Generative AI track resource (reference only)
├── outputs/
│   ├── week6_validated_dashboard.png                           Week 6 refined decision-support dashboard
│   └── HealthConnect_Week6_Feature_Relevance.csv               Cross-track integration artefact for Data Science

## Where to start

- **This week (Week 6):** `docs/HealthConnect_Week6_Project_Summary.pdf` (short version), then
  `docs/HealthConnect_Week6_Advanced_Analytics_Report.pdf` (full report), then
  `notebooks/HealthConnect_Week6_Advanced_Analytics.ipynb` for the code.
- **Cross-track artefact:** `outputs/HealthConnect_Week6_Feature_Relevance.csv`.
## Week 6 headline results

**Statistical validation of Week 5's top 3 findings:**

| Finding | p-value | Effect size (Cramer's V) | Verdict |
|---|---|---|---|
| Booking lead time | <0.001 | 0.197 | Confirmed — strongest driver |
| Previous no-shows | <0.001 | 0.089 | Confirmed — smaller effect than raw % suggests |
| Reminder sent | 0.006 | 0.045 | Confirmed but very small effect |

**New segment tests (not covered in Week 5):**

| Segment | p-value | Verdict |
|---|---|---|
| Appointment type | 0.104 | Not significant — downgraded from "weak" to "not supported" |
| Reminder channel | 0.006 | Significant — SMS confirmed genuinely better, not noise |

**Interaction analysis:** the reminder effect appears descriptively larger for patients with more
prior no-shows (2.65pp → 10.02pp reduction), but the formal interaction test is **not**
statistically significant (p = 0.143) — reported honestly as unconfirmed rather than a validated
finding.

**Combined multivariate model:** booking lead time, previous no-shows, and reminder status all
remain significant predictors even when controlling for each other — supporting their use
together as independent features.

## Cross-track integration (Week 6 mandatory requirement)

Produced `HealthConnect_Week6_Feature_Relevance.csv` for the Data Science track: a ranked,
statistically validated feature table with explicit include/exclude/caution recommendations,
replacing Week 5's descriptive-only findings as the basis for their feature-selection decisions.

## Known open items going into Week 7

- Re-validate the three confirmed predictors once a refined Data Science model is available.
- Re-test the reminder × prior-history interaction if a larger dataset becomes available.
- Resolve carried-forward items: Sunday-appointment operating-hours question, missing-data
  handling rule for distance/waiting time.
- No causal test (e.g. A/B reminder pilot) has been run yet — all findings remain observational.

## Reproducing this project

```bash
# Week 6
cd ../notebooks && python3 build_week6_notebook.py
jupyter nbconvert --to notebook --execute --inplace HealthConnect_Week6_Advanced_Analytics.ipynb
cd ../docs && node build_week6_report.js && node build_week6_summary.js
```
