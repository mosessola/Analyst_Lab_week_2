# HealthConnect Clinic — Week 7: Analytical Testing, KPI Validation & Dashboard Refinement

**Data Analytics Track · AnalystLab Africa Experience Lab · Moses Oluwatosin · September 2026**

Week 7 tests the Week 6 analytical outputs rather than extending them. The short version: every
Week 6 number reproduced exactly, but the tests behind them were specified against the wrong
outcome variable. Correcting that changed every published effect size and reversed one
recommendation that had already been delivered to the Data Science track.

---

## Headline result

Week 6 ran its chi-square tests as `crosstab(feature, appointment_outcome)`, where
`appointment_outcome` has three levels (Attended / Cancelled / No-Show). Two consequences:

1. `min(shape) - 1 = 2`, so **every Cramér's V was divided by √2**.
2. Each test asked *"is this feature associated with the three-way outcome?"* rather than
   *"...with no-shows?"*

| Feature | Week 6 p | Week 6 V | Corrected p | Corrected V |
|---|---|---|---|---|
| Booking lead time | <0.001 | 0.1967 | <0.001 | **0.2853** |
| Prior no-show history | <0.001 | 0.0889 | <0.001 | **0.1218** |
| Reminder channel | 0.0062 | 0.0425 | 0.0019 | **0.0562** |
| Reminder sent | 0.0061 | 0.0452 | 0.0038 | 0.0420 |
| Appointment type | 0.1042 | 0.0324 | **0.0380** | 0.0422 |

The **relative ranking is unchanged**, so the Week 6 prioritisation advice survives. But
`appointment_type` flips verdict, and Week 6 had already told Data Science to exclude it
*because it was not statistically significant*.

---

## What was tested

| ID | Component | Result |
|---|---|---|
| T1 | Dataset integrity (7 checks) | PASS — zero violations |
| T2 | Published KPIs | PASS with a denominator issue (cancellations in the base) |
| T3 | All five significance tests | **FAIL** — method defect (HC-W7-01) |
| T4 | The appointment_type exclusion | **FAIL** — rationale invalid (HC-W7-02) |
| T5 | Reminder effect vs lead-time confounding | PASS — effect survives, adjusted OR 0.810 |
| T6 | Reminder × prior-history interaction | PASS — conclusion upheld (p 0.143 → 0.200) |
| T7 | Lead-time stability across 15 segments | PASS — holds in 14 of 15 |
| T8 | Week 6 dashboard | **FAIL** — 4 defects (HC-W7-03, HC-W7-04) |

Full field-by-field record: [`outputs/week7_testing_validation_record.csv`](outputs/week7_testing_validation_record.csv)

---

## Refinements made

- All tests rebuilt on the decided-appointment base with a binary outcome and a Holm correction
  across the five-test family.
- `appointment_type` reclassified from *"not statistically supported"* to
  *"optional / low priority — real but negligible"* (LR test p = 0.0325, pseudo-R² gain 0.0013,
  no individual type significant).
- Dashboard rebuilt: every annotation now interpolated from the live results object at render
  time — the defect that produced stale titles cannot recur. Added Wilson 95% intervals, category
  sample sizes, a clinic-average reference line, an explicit analysis base in the header, and
  hatching plus a negative-verdict label on the non-significant panel.
- Both KPI bases (48.5% all appointments / 51.2% decided appointments) now reported and labelled.

---

## Cross-track contribution (HC-POD)

**Data Science.** `HealthConnect_Week6_Feature_Relevance.csv` was reissued as
[`HealthConnect_Week7_Feature_Relevance_v2.csv`](outputs/HealthConnect_Week7_Feature_Relevance_v2.csv)
— a drop-in replacement with corrected statistics, a `change_from_w6` column, and an adjusted odds
ratio for `reminder_sent` they can cite against the confounding challenge. They keep their feature
ordering; they need to correct their stated reason for dropping `appointment_type`.

**Project Management.** KPI denominator change and four new issue-log entries.

---

## Repository structure

```
data/                    HealthConnect_Appointment_Data.csv        (unmodified source)
notebooks/               HealthConnect_Week7_Testing_Refinement.ipynb
docs/                    HealthConnect_Week7_Project_Summary.docx
outputs/                 week7_refined_dashboard.png               (after)
                         HealthConnect_Week7_Feature_Relevance_v2.csv
                         week7_testing_validation_record.csv
                         week7_issue_log.csv
                         week7_kpi_significance_validation.csv
                         week7_segment_stability_tests.csv
```

## Reproducing

```bash
pip install pandas numpy scipy matplotlib statsmodels
jupyter nbconvert --execute --inplace notebooks/HealthConnect_Week7_Testing_Refinement.ipynb
```

Every figure in this README is produced by that notebook. No value is typed by hand.

---

## Open before Week 8

1. Data Science to confirm their model notes reflect the `appointment_type` correction (HC-W7-02).
2. Agree a single headline KPI base with Project Management.
3. Re-validate the three confirmed predictors against the refined model output.
4. No causal test has been run — a randomised reminder pilot is proposed for discussion (HC-W7-05).
5. Sunday appointment records remain unreconciled against Knowledge Base opening hours (HC-W5-02),
   deliberately deprioritised since day of week is not a significant predictor (p = 0.38).

## Limitation worth stating plainly

All findings are observational. Even the corrected Cramér's V of 0.285 is a small-to-moderate
effect — lead time is the best single predictor available and still leaves most variance
unexplained. A 48–51% no-show rate is also implausibly high for a real clinic, so these results
are methodologically sound rather than clinically representative.
