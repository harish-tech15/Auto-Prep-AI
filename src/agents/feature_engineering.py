"""
AutoPrep AI - Feature Engineering Agent

Analyzes processed features and generates
a feature engineering report.
"""

import pandas as pd


class FeatureEngineeringAgent:

    def __init__(self):
        self.agent_name = "AutoPrep AI Feature Engineering Agent"

    def analyze(self, train_df, test_df, target_col="Attrition"):
        """Analyze the engineered training and testing features."""

        if not isinstance(train_df, pd.DataFrame):
            raise TypeError("Training data must be a DataFrame.")

        if not isinstance(test_df, pd.DataFrame):
            raise TypeError("Testing data must be a DataFrame.")

        if train_df.empty or test_df.empty:
            raise ValueError("Processed datasets cannot be empty.")

        train_features = [
            col for col in train_df.columns
            if col != target_col
        ]

        test_features = [
            col for col in test_df.columns
            if col != target_col
        ]

        if train_features != test_features:
            raise ValueError(
                "Training and testing feature columns do not match."
            )

        numeric_columns = train_df[train_features].select_dtypes(
            include=["number"]
        ).columns.tolist()

        feature_statistics = {}

        for column in numeric_columns:
            feature_statistics[column] = {
                "mean": round(float(train_df[column].mean()), 4),
                "std": round(float(train_df[column].std()), 4),
                "minimum": round(float(train_df[column].min()), 4),
                "maximum": round(float(train_df[column].max()), 4),
            }

        report = {
            "agent": self.agent_name,
            "original_feature_count": len(train_features),
            "final_feature_count": len(train_features),
            "numerical_feature_count": len(numeric_columns),
            "engineered_feature_names": train_features,
            "target_column": target_col,
            "target_preserved": target_col in train_df.columns,
            "train_rows": len(train_df),
            "test_rows": len(test_df),
            "feature_statistics": feature_statistics,
        }

        return report

    def display_report(self, report):
        """Display feature engineering results."""

        print("\n" + "=" * 55)
        print("    AUTOPREP AI - FEATURE ENGINEERING REPORT")
        print("=" * 55)

        print(
            f"Original Feature Count: "
            f"{report['original_feature_count']}"
        )
        print(
            f"Final Feature Count: "
            f"{report['final_feature_count']}"
        )
        print(
            f"Numerical Features: "
            f"{report['numerical_feature_count']}"
        )
        print(
            f"Target Preserved: {report['target_preserved']}"
        )

        print("=" * 55)
