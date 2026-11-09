"""
AutoPrep AI - Report Generation Agent

Combines agent outputs and generates
JSON and Markdown project reports.
"""

import json
from pathlib import Path
from datetime import datetime


class ReportAgent:

    def __init__(self, output_dir="reports"):
        self.agent_name = "AutoPrep AI Report Generation Agent"
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_report(
        self,
        analysis_report,
        quality_report,
        preprocessing_plan,
        feature_report,
        validation_report,
    ):
        """Combine all agent reports into one final report."""

        final_report = {
            "project": "AutoPrep AI",
            "version": "1.0.0",
            "generated_at": datetime.now().isoformat(),
            "agent": self.agent_name,
            "data_analysis": analysis_report,
            "data_quality": quality_report,
            "preprocessing_plan": preprocessing_plan,
            "feature_engineering": feature_report,
            "validation": validation_report,
            "project_status": validation_report.get(
                "overall_status", "UNKNOWN"
            ),
        }

        return final_report

    def save_json(self, report, filename="autoprep_final_report.json"):
        """Save final report as JSON."""

        output_path = self.output_dir / filename

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4, default=str)

        return output_path

    def save_markdown(
        self,
        report,
        filename="autoprep_final_report.md",
    ):
        """Save a readable Markdown report."""

        analysis = report["data_analysis"]
        quality = report["data_quality"]
        features = report["feature_engineering"]
        validation = report["validation"]

        content = f"""# AutoPrep AI - Final Report

## Project Overview

- **Project:** {report['project']}
- **Version:** {report['version']}
- **Generated At:** {report['generated_at']}
- **Project Status:** {report['project_status']}

## 1. Data Analysis

- Total Rows: {analysis['total_rows']}
- Total Columns: {analysis['total_columns']}
- Numerical Features: {len(analysis['numerical_columns'])}
- Categorical Features: {len(analysis['categorical_columns'])}
- Duplicate Rows: {analysis['duplicate_rows']}
- Missing Values: {analysis['missing_values']}

## 2. Data Quality

- Missing Values: {quality['total_missing_values']}
- Duplicate Rows: {quality['duplicate_rows']}
- Constant Columns: {quality['constant_columns']}
- High Missing Columns: {quality['high_missing_columns']}

## 3. Feature Engineering

- Final Feature Count: {features['final_feature_count']}
- Numerical Feature Count: {features['numerical_feature_count']}
- Target Preserved: {features['target_preserved']}

## 4. Validation Results

- Total Checks: {validation['total_checks']}
- Passed: {validation['passed']}
- Failed: {validation['failed']}
- Overall Status: {validation['overall_status']}

### Validation Details

"""

        for check in validation["checks"]:
            content += (
                f"- **{check['status']}**: {check['check']}\n"
            )

        content += """
---

*Generated automatically by AutoPrep AI.*
"""

        output_path = self.output_dir / filename

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(content)

        return output_path
