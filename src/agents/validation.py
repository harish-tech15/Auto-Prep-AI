"""
AutoPrep AI - Validation Agent

Validates processed datasets and checks
data quality, feature consistency, and target preservation.
"""

import pandas as pd


class ValidationAgent:

    def __init__(self):
        self.agent_name = "AutoPrep AI Validation Agent"

    def validate(
        self,
        train_df,
        test_df,
        target_col="Attrition",
    ):
        """Run validation checks on processed datasets."""

        if not isinstance(train_df, pd.DataFrame):
            raise TypeError("Training data must be a DataFrame.")

        if not isinstance(test_df, pd.DataFrame):
            raise TypeError("Testing data must be a DataFrame.")

        checks = []

        def add_check(name, condition, details=""):
            checks.append({
                "check": name,
                "status": "PASS" if condition else "FAIL",
                "details": details,
            })

        # Dataset dimensions
        add_check(
            "Training dataset is not empty",
            not train_df.empty,
        )

        add_check(
            "Testing dataset is not empty",
            not test_df.empty,
        )

        # Missing values
        add_check(
            "Training data has no missing values",
            not train_df.isnull().any().any(),
        )

        add_check(
            "Testing data has no missing values",
            not test_df.isnull().any().any(),
        )

        # Duplicate rows
        add_check(
            "Training data has no duplicate rows",
            not train_df.duplicated().any(),
        )

        add_check(
            "Testing data has no duplicate rows",
            not test_df.duplicated().any(),
        )

        # Feature consistency
        train_features = [
            col for col in train_df.columns
            if col != target_col
        ]

        test_features = [
            col for col in test_df.columns
            if col != target_col
        ]

        add_check(
            "Train and test features match",
            train_features == test_features,
        )

        # Target preservation
        add_check(
            "Target column exists in training data",
            target_col in train_df.columns,
        )

        add_check(
            "Target column exists in testing data",
            target_col in test_df.columns,
        )

        # Feature count
        add_check(
            "At least one feature is available",
            len(train_features) > 0,
        )

        # Numeric data validation
        numeric_train = train_df.select_dtypes(
            include=["number"]
        )

        add_check(
            "Training numeric values are finite",
            bool(numeric_train.empty or
                 numeric_train.map(
                     lambda value: pd.notna(value)
                     and abs(value) != float("inf")
                 ).all().all()),
        )

        total_checks = len(checks)
        passed = sum(
            item["status"] == "PASS" for item in checks
        )
        failed = total_checks - passed

        return {
            "agent": self.agent_name,
            "total_checks": total_checks,
            "passed": passed,
            "failed": failed,
            "overall_status": "PASS" if failed == 0 else "FAIL",
            "checks": checks,
        }

    def display_report(self, report):
        """Display validation results."""

        print("\n" + "=" * 55)
        print("       AUTOPREP AI - VALIDATION REPORT")
        print("=" * 55)

        for item in report["checks"]:
            print(
                f"[{item['status']}] {item['check']}"
            )

        print("-" * 55)
        print(f"Total Checks : {report['total_checks']}")
        print(f"Passed       : {report['passed']}")
        print(f"Failed       : {report['failed']}")
        print(f"Overall      : {report['overall_status']}")
        print("=" * 55)
