# Sales Analytics Dashboard

An end-to-end data analytics project built on the Kaggle Superstore dataset,
covering data cleaning, SQL analysis, exploratory data analysis, and an
interactive dashboard — structured like a real industry project.

---

## Dashboard Preview

![Dashboard](exports/screenshots/01_dashboard_full.png)

---

## Key Business Findings

- Revenue grew 30%+ from 2014 to 2017 with consistent Nov/Dec spikes
- Discounts above 20% generate negative profit — orders with 30%+ discount
  lose an average of $107 per order
- Tables and Bookcases are loss-making sub-categories despite high sales volume
- West region leads in revenue; Central has the lowest profit margins
- Consumer segment drives 51% of total revenue

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core programming language |
| Pandas | Data loading, cleaning, feature engineering |
| Matplotlib / Seaborn | Exploratory data analysis charts |
| SQLite | KPI queries and aggregations |
| Plotly Dash | Interactive web dashboard |

---

## Project Structure

\`\`\`
sales-analytics-dashboard/
├── data/
│   └── processed/          <- Cleaned dataset (28 columns, 9,994 rows)
├── notebooks/
│   ├── 01_data_cleaning    <- Cleaning, type fixing, feature engineering
│   ├── 02_sql_analysis     <- SQLite KPI queries
│   └── 02_eda              <- 6 EDA charts
├── sql/
│   └── kpi_queries.sql     <- Raw SQL queries
├── exports/
│   ├── *.png               <- EDA charts
│   └── screenshots/        <- Dashboard screenshots
└── dashboard.py            <- Plotly Dash interactive dashboard
\`\`\`

---

## How to Run

### 1. Clone the repository
\`\`\`bash
git clone https://github.com/Abdul-Haq-DS/sales-analytics-dashboard.git
cd sales-analytics-dashboard
\`\`\`

### 2. Create environment and install dependencies
\`\`\`bash
conda create -n sales-analytics python=3.11
conda activate sales-analytics
pip install pandas matplotlib seaborn plotly dash jupyter
\`\`\`

### 3. Download the dataset
Download the Superstore dataset from Kaggle and place it at:
data/raw/Sample - Superstore.csv

Link: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

### 4. Run notebooks in order
- notebooks/01_data_cleaning.ipynb
- notebooks/02_sql_analysis.ipynb
- notebooks/02_eda.ipynb

### 5. Launch the dashboard
\`\`\`bash
python dashboard.py
\`\`\`
Open browser at: http://127.0.0.1:8051

---

## EDA Charts

| Chart | Insight |
|---|---|
| Monthly trend | Revenue grows consistently, peaks every Nov/Dec |
| Category performance | Technology leads in both revenue and profit |
| Sub-category profit | Tables and Bookcases lose money |
| Discount impact | 30%+ discount = negative profit |
| Region heatmap | West dominates, Central lags |
| Yearly growth | 30%+ YoY growth from 2014 to 2017 |

---

## Dataset

- Source: Kaggle Superstore Dataset
- Rows: 9,994 orders
- Columns: 21 original + 7 engineered = 28 total
- Period: January 2014 to December 2017

---

## Author

Abdul
Data Analyst Portfolio Project

---

## Portfolio

| Project | Description | Link |
|---|---|---|
| Project 1 | Sales Analytics Dashboard | This repo |
| Project 2 | Customer Segmentation (K-Means) | [View](https://github.com/Abdul-Haq-DS/customer-segmentation) |
