"""
AutoPrep AI - Data Quality Agent

Identifies missing values, duplicate rows,
constant columns, and high-cardinality columns.
"""

import pandas as pd


class DataQualityAgent:

    def __init__(self, missing_threshold=0.50):
        self.agent_name = "AutoPrep AI Data Quality Agent"
        self.missing_threshold = missing_threshold

    def analyze(self, df: pd.DataFrame) -> dict:
        """Inspect the dataset for common data quality issues."""

        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")

        if df.empty:
            raise ValueError("Dataset is empty.")

        missing_counts = df.isnull().sum()
        missing_percentages = (
            missing_counts / len(df) * 100
        ).round(2)

        missing_summary = {
            column: {
                "count": int(missing_counts[column]),
                "percentage": float(missing_percentages[column]),
            }
            for column in df.columns
            if missing_counts[column] > 0
        }

        duplicate_rows = int(df.duplicated().sum())

        constant_columns = [
            column
            for column in df.columns
            if df[column].nunique(dropna=False) <= 1
        ]

        high_missing_columns = [
            column
            for column in df.columns
            if missing_percentages[column]
            >= self.missing_threshold * 100
        ]

        high_cardinality_columns = [
            column
            for column in df.select_dtypes(
                include=["object", "category"]
            ).columns
            if df[column].nunique(dropna=True) / len(df) > 0.90
        ]

        report = {
            "agent": self.agent_name,
            "total_missing_values": int(missing_counts.sum()),
            "missing_summary": missing_summary,
            "duplicate_rows": duplicate_rows,
            "constant_columns": constant_columns,
            "high_missing_columns": high_missing_columns,
            "high_cardinality_columns": high_cardinality_columns,
            "data_quality_status": (
                "REVIEW_REQUIRED"
                if (
                    missing_counts.sum() > 0
                    or duplicate_rows > 0
                    or constant_columns
                )
                else "GOOD"
            ),
        }

        return report

    def display_report(self, report: dict) -> None:
        """Print the data quality report."""

        print("\n" + "=" * 55)
        print("       AUTOPREP AI - DATA QUALITY REPORT")
        print("=" * 55)

        print(
            f"Missing Values: {report['total_missing_values']}"
        )
        print(f"Duplicate Rows: {report['duplicate_rows']}")

        print(
            f"Constant Columns: {report['constant_columns']}"
        )
        print(
            f"High Missing Columns: {report['high_missing_columns']}"
        )
        print(
            f"High Cardinality Columns: "
            f"{report['high_cardinality_columns']}"
        )

        print(
            f"Status: {report['data_quality_status']}"
        )

        print("=" * 55)
