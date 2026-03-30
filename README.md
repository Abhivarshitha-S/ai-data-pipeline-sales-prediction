# AI-Driven Data Pipeline with SQL Insights and Sales Prediction

## Overview
This project is an end-to-end data pipeline that integrates ETL processes, SQL-based data analysis, and machine learning for sales prediction.

It demonstrates how raw data can be transformed into meaningful insights and predictive models.

---

## Tech Stack
- Python
- Pandas
- SQLite
- Scikit-learn
- Git & GitHub

---

## Project Workflow

### 1. ETL Process
- Extract data from source files
- Transform and clean data
- Load into SQLite database

### 2. SQL Analysis
- Total sales by product
- Top-selling products
- Aggregations using groupby

### 3. AI Prediction
- Linear Regression model
- Predicts total sales based on quantity

---

## 📂 Project Structure

my_project/
│
├── etl/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── sql/
│ └── query.py
│
├── ai/
│ └── predict.py
│
├── data/
│ └── database.db
│
└── pipeline.py


---

## How to Run?

```bash
python pipeline.py


📊 Sample Output
ETL completed successfully
SQL insights printed
Model trained with Mean Squared Error
Sales prediction generated

🎯 Key Features
End-to-end pipeline automation
SQL-based business insights
Machine learning integration
Modular and scalable code structure

🚀 Future Improvements
Add more features for prediction
Use advanced ML models
Build a dashboard (Power BI / Streamlit)

