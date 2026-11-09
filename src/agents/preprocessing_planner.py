"""
AutoPrep AI - Preprocessing Planner Agent

Creates a preprocessing plan based on
dataset analysis and data quality reports.
"""


class PreprocessingPlannerAgent:

    def __init__(self):
        self.agent_name = "AutoPrep AI Preprocessing Planner Agent"

    def create_plan(
        self,
        analysis_report: dict,
        quality_report: dict,
        target_col: str = "Attrition",
    ) -> dict:
        """Generate a structured preprocessing plan."""

        if not analysis_report or not quality_report:
            raise ValueError("Analysis and quality reports are required.")

        numerical_columns = analysis_report.get(
            "numerical_columns", []
        )

        categorical_columns = analysis_report.get(
            "categorical_columns", []
        )

        missing_summary = quality_report.get(
            "missing_summary", {}
        )

        constant_columns = quality_report.get(
            "constant_columns", []
        )

        high_cardinality_columns = quality_report.get(
            "high_cardinality_columns", []
        )

        excluded_columns = []

        # Protect the target column from preprocessing.
        numerical_features = [
            col for col in numerical_columns
            if col != target_col
        ]

        categorical_features = [
            col for col in categorical_columns
            if col != target_col
        ]

        if target_col in numerical_columns:
            excluded_columns.append(target_col)

        if target_col in categorical_columns:
            excluded_columns.append(target_col)

        # Identify constant columns for removal.
        columns_to_drop = [
            col for col in constant_columns
            if col != target_col
        ]

        # Identify likely identifier columns.
        identifier_columns = [
            col for col in analysis_report.get(
                "column_data_types", {}
            )
            if col.lower() in [
                "id",
                "employeeid",
                "employeenumber",
                "customerid",
            ]
        ]

        columns_to_drop.extend(
            col for col in identifier_columns
            if col != target_col and col not in columns_to_drop
        )

        # Create numerical preprocessing instructions.
        numerical_steps = [
            "Impute missing values using median",
            "Apply StandardScaler",
        ]

        # Create categorical preprocessing instructions.
        categorical_steps = [
            "Impute missing values using most frequent value",
            "Apply OneHotEncoder with unknown category handling",
        ]

        # Record missing-value recommendations.
        missing_actions = {}

        for column, details in missing_summary.items():
            if column == target_col:
                missing_actions[column] = (
                    "Review target missing values before training"
                )
            elif column in numerical_features:
                missing_actions[column] = "Median imputation"
            elif column in categorical_features:
                missing_actions[column] = "Mode imputation"

        plan = {
            "agent": self.agent_name,
            "target_column": target_col,
            "numerical_features": numerical_features,
            "categorical_features": categorical_features,
            "excluded_columns": excluded_columns,
            "columns_to_drop": columns_to_drop,
            "high_cardinality_columns": high_cardinality_columns,
            "missing_value_actions": missing_actions,
            "numerical_preprocessing": numerical_steps,
            "categorical_preprocessing": categorical_steps,
            "train_test_split": {
                "test_size": 0.20,
                "random_state": 42,
            },
            "leakage_prevention": (
                "Split data before fitting preprocessing transformers"
            ),
        }

        return plan

    def display_plan(self, plan: dict) -> None:
        """Display the generated preprocessing plan."""

        print("\n" + "=" * 55)
        print("       AUTOPREP AI - PREPROCESSING PLAN")
        print("=" * 55)

        print(f"Target Column: {plan['target_column']}")
        print(
            f"Numerical Features: {len(plan['numerical_features'])}"
        )
        print(
            f"Categorical Features: {len(plan['categorical_features'])}"
        )
        print(f"Columns to Drop: {plan['columns_to_drop']}")

        print("\nNumerical Processing:")
        for step in plan["numerical_preprocessing"]:
            print(f"- {step}")

        print("\nCategorical Processing:")
        for step in plan["categorical_preprocessing"]:
            print(f"- {step}")

        print("=" * 55)
