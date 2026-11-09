"""
AutoPrep AI - Main Entry Point

Run the complete intelligent data preprocessing workflow.
"""

import argparse

from config import DATA_DIR, TARGET_COLUMN
from src.orchestrator import run_autoprep_workflow


def main():
    parser = argparse.ArgumentParser(
        description="AutoPrep AI - Intelligent Data Preprocessing"
    )

    parser.add_argument(
        "--dataset",
        type=str,
        default=str(DATA_DIR / "IBM_HR_Attrition.csv"),
        help="Path to the input CSV dataset",
    )

    parser.add_argument(
        "--target",
        type=str,
        default=TARGET_COLUMN,
        help="Target column name",
    )

    args = parser.parse_args()

    print("\nStarting AutoPrep AI...")

    result = run_autoprep_workflow(
        dataset_path=args.dataset,
        target_col=args.target,
    )

    print("\nWorkflow execution finished.")

    print(
        "Final validation status:",
        result["validation_report"]["overall_status"],
    )


if __name__ == "__main__":
    main()
