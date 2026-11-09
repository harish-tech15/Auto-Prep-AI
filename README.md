# AutoPrep AI
### Multi-Agent Intelligent Data Preprocessing System

AutoPrep AI is an intelligent, multi-agent data preprocessing system designed to analyze datasets, identify data quality issues, recommend preprocessing operations, engineer features, and validate processed datasets.

## Key Features

- Automated dataset analysis
- Data quality inspection
- Missing value and duplicate detection
- Preprocessing recommendations
- Approval-based preprocessing workflow
- Numerical feature scaling
- Categorical feature encoding
- Feature engineering analysis
- Data validation and quality checks
- Automated report generation
- Central agent orchestration
- Interactive Streamlit dashboard

## Multi-Agent Architecture

The workflow consists of seven stages:

1. **Data Analyst Agent** – Analyzes dataset structure and statistics.
2. **Data Quality Agent** – Identifies missing values, duplicates, constant columns, and potential issues.
3. **Preprocessing Planner Agent** – Recommends suitable preprocessing operations.
4. **Preprocessing Engine** – Executes approved preprocessing operations.
5. **Feature Engineering Agent** – Analyzes feature importance, variance, and correlation.
6. **Validation Agent** – Checks the processed training and testing datasets.
7. **Report Agent** – Generates final Markdown, JSON, and summary reports.

## Dataset

The project was tested using the IBM HR Employee Attrition dataset.

- Original records: 1,470
- Original columns: 35
- Target column: `Attrition`
- Training records: 1,176
- Testing records: 294
- Train-test split: 80/20

## Data Processing

- Numerical imputation when required
- Categorical imputation when required
- One-hot encoding
- Standard scaling
- Constant-column identification
- Identifier-column exclusion
- Target-column protection
- Train-test leakage prevention

## Validation Results

The completed workflow passed all 15 validation checks.

| Validation Metric | Result |
|---|---:|
| Total checks | 15 |
| Passed | 15 |
| Failed | 0 |
| Overall status | PASS |

## Generated Outputs

- `train_processed.csv`
- `test_processed.csv`
- `preprocessing_pipeline.joblib`
- `preprocessing_report.json`
- `feature_engineering_report.json`
- `validation_report.json`
- `autoprep_final_report.md`
- `autoprep_final_report.json`
- `autoprep_summary.txt`

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Joblib

## Project Objective

The objective of AutoPrep AI is to reduce repetitive data preparation work through an organized, transparent, and validation-driven multi-agent workflow.

## Disclaimer

This project is developed for educational and demonstration purposes. Preprocessing recommendations should be reviewed before applying them to real-world datasets.

---

**Project:** AutoPrep AI  
**Category:** Artificial Intelligence / Data Science  
**Architecture:** Multi-Agent Data Preprocessing System
