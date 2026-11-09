# AutoPrep AI - System Architecture

## Overview

AutoPrep AI is a multi-agent intelligent data preprocessing
system designed to automate common data preparation tasks.

## Architecture

The system consists of seven specialized agents coordinated
by a central orchestrator.

### 1. Data Analyst Agent
- Inspects dataset dimensions.
- Identifies numerical and categorical columns.
- Analyzes data types and memory usage.

### 2. Data Quality Agent
- Detects missing values.
- Identifies duplicate records.
- Finds constant columns.
- Detects high-cardinality columns.

### 3. Preprocessing Planner Agent
- Creates preprocessing recommendations.
- Identifies columns to exclude.
- Defines numerical and categorical transformations.

### 4. Preprocessing Engine Agent
- Splits data into training and testing sets.
- Imputes missing values.
- Scales numerical features.
- Encodes categorical features.
- Prevents data leakage by fitting transformations
  only on training data.

### 5. Feature Engineering Agent
- Analyzes transformed features.
- Generates feature statistics.
- Checks target preservation.

### 6. Validation Agent
- Checks missing values and duplicates.
- Verifies feature consistency.
- Checks target column preservation.
- Produces validation results.

### 7. Report Generation Agent
- Combines agent outputs.
- Generates JSON reports.
- Generates Markdown reports.

## Workflow

```text
Input Dataset
     |
     v
Central Orchestrator
     |
     v
Data Analyst Agent
     |
     v
Data Quality Agent
     |
     v
Preprocessing Planner Agent
     |
     v
Preprocessing Engine Agent
     |
     v
Feature Engineering Agent
     |
     v
Validation Agent
     |
     v
Report Generation Agent
     |
     v
Processed Data + Reports
