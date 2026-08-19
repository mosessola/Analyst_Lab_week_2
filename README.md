# Analyst_Lab_week_2
Power BI executive dashboard analyzing retail sales, profitability, and regional performance using the Superstore dataset. Built as part of the AnalystLab Africa Data Analytics Internship (Week 2: Business Analytics Case Study).
# Superstore Retail BI Dashboard

An executive Power BI dashboard built for a fictional national retail company, analyzing sales performance, profitability, customer behavior, and regional trends. Built as part of the **AnalystLab Africa Data Analytics Internship Programme — Week 2: Business Analytics Case Study**.

## Business Scenario

Acting as a Junior Business Intelligence Analyst, this project transforms raw transactional retail data into an interactive dashboard that helps management monitor performance and make data-driven strategic decisions — covering overall sales health, regional and segment performance, product profitability, and time trends.

## Dataset

- **Source:** [Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) (Kaggle)
- **Size:** 9,994 orders, 28 columns after cleaning
- **Period covered:** January 2014 – December 2017
- **Fields:** Order/ship dates, customer segment, region/state/city, product category & sub-category, sales, profit, discount, quantity

## Tech Stack

| Tool | Purpose |
|---|---|
| Python (pandas) | Data cleaning & transformation, run in Jupyter Notebook |
| Power BI | Dashboard development, DAX measures, interactive visuals |
| Power Query | In-tool data shaping |

## Repository Contents
reports/
├── Business_Intelligence_Overview_Report.docx        (Week 2)
├── Business_Insights_and_Recommendations.docx        (Week 2)
├── Project_Continuity_Summary.docx                    ← NEW
├── DAX_Measures_Documentation.docx                     ← NEW
├── Business_Insights_and_Recommendations_Week3.docx   ← NEW
exports/
├── Dashboard_Export_Week2.pdf                          (rename old one)
├── Dashboard_Export_Week3.pdf                          ← NEW, once you export it
powerbi/
├── Analyst_Lab_Dashboard.pbix                          (overwrite with your updated version)

## Data Preparation

Using pandas, the raw dataset was:
- Inspected for structure, data types, and completeness
- Checked for missing values and duplicate records
- Corrected for proper data types (dates parsed, postal codes kept as strings)
- Enriched with calculated columns: **Profit Margin**, **Shipping Duration**, **Order Year/Month**, and a loss-flag (**Is Loss**) for risk analysis

Full pipeline: [`notebooks/Superstore_Data_Cleaning.ipynb`](notebooks/Superstore_Data_Cleaning.ipynb)

## Dashboard

**KPI Cards:** Total Sales · Total Profit · Total Orders · Average Sales · Profit Margin

**Visuals:** Sales & Profit trend over time · Sales by Region (map + bar) · Sales by Segment (donut) · Sales/Profit by Category · Profit by Sub-Category · Top Products by Profit (table) · Regional/Category/Date slicers

## Key Findings

- **Technology (17.4%) and Office Supplies (17.0%) margins** far outperform **Furniture (2.5%)**, despite similar revenue.
- **Tables (–8.6% margin) and Bookcases (–3.0% margin)** are net loss-making sub-categories.
- **West (14.9%) and East (13.5%) regions** lead on profitability; **Central (7.9%)** lags significantly.
- Discounts above 30% are collectively loss-making — **1,166 such orders lost a combined –$125,007**.
- **Home Office (14.0% margin)** is the most profitable segment per dollar sold, ahead of Corporate and Consumer.

Full insights, risks, opportunities, and recommendations: [`reports/Business_Insights_and_Recommendations.docx`](reports/Business_Insights_and_Recommendations.docx)

## Recommendations (Summary)

1. Introduce a minimum-margin discount cap on low-margin categories.
2. Review pricing and supplier costs for Tables and Bookcases.
3. Reallocate marketing/inventory investment toward Technology and Office Supplies.
4. Launch a Central-region and underperforming-state improvement plan.
5. Build a targeted Home Office growth campaign.

## Author

**Moses Oluwatosin**
Junior Business Intelligence Analyst — AnalystLab Africa Data Analytics Internship Programme

---
*This project is part of the AnalystLab Africa Data Analytics Internship Programme (Week 2 Assignment). #AnalystLabAfrica*
