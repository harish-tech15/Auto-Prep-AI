"""
AutoPrep AI - Data Analyst Agent

Analyzes dataset structure, columns, data types,
numerical features, and categorical features.
"""

import pandas as pd


class DataAnalystAgent:

    def __init__(self):
        self.agent_name = "AutoPrep AI Data Analyst Agent"

    def analyze(self, df: pd.DataFrame) -> dict:
        """
        Analyze the input dataset and return a summary.
        """

        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")

        if df.empty:
            raise ValueError("Dataset is empty.")

        numerical_columns = (
            df.select_dtypes(include=["number"]).columns.tolist()
        )

        categorical_columns = (
            df.select_dtypes(
                include=["object", "category", "bool"]
            ).columns.tolist()
        )

        datetime_columns = (
            df.select_dtypes(include=["datetime"]).columns.tolist()
        )

        analysis = {
            "agent": self.agent_name,
            "total_rows": int(df.shape[0]),
            "total_columns": int(df.shape[1]),
            "numerical_columns": numerical_columns,
            "categorical_columns": categorical_columns,
            "datetime_columns": datetime_columns,
            "duplicate_rows": int(df.duplicated().sum()),
            "missing_values": int(df.isnull().sum().sum()),
            "column_data_types": {
                column: str(dtype)
                for column, dtype in df.dtypes.items()
            },
            "memory_usage_mb": round(
                df.memory_usage(deep=True).sum() / (1024 ** 2), 3
            ),
        }

        return analysis

    def display_summary(self, analysis: dict) -> None:
        """Display a readable dataset analysis summary."""

        print("\n" + "=" * 55)
        print("       AUTOPREP AI - DATA ANALYST REPORT")
        print("=" * 55)

        print(f"Rows              : {analysis['total_rows']}")
        print(f"Columns           : {analysis['total_columns']}")
        print(f"Numerical Features: {len(analysis['numerical_columns'])}")
        print(f"Categorical Features: {len(analysis['categorical_columns'])}")
        print(f"Duplicate Rows    : {analysis['duplicate_rows']}")
        print(f"Missing Values    : {analysis['missing_values']}")
        print(f"Memory Usage      : {analysis['memory_usage_mb']} MB")

        print("=" * 55)
