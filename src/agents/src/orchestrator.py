"""
AutoPrep AI - Central Agent Orchestrator

Coordinates all seven agents and executes
the complete preprocessing workflow.
"""

import joblib
import pandas as pd

from pathlib import Path

from src.agents import (
    DataAnalystAgent,
    DataQualityAgent,
    PreprocessingPlannerAgent,
    PreprocessingEngineAgent,
    FeatureEngineeringAgent,
    ValidationAgent,
    ReportAgent,
)


def run_autoprep_workflow(
    dataset_path,
    target_col="Attrition",
    output_dir="outputs",
    report_dir="reports",
):
    """
    Execute the complete AutoPrep AI workflow.

    Args:
        dataset_path: Path to the input CSV dataset.
        target_col: Target column for preprocessing.
        output_dir: Directory for processed datasets.
        report_dir: Directory for generated reports.

    Returns:
        Dictionary containing workflow results.
    """

    print("\n" + "=" * 65)
    print("       AUTOPREP AI - CENTRAL AGENT ORCHESTRATOR")
    print("=" * 65)

    output_path = Path(output_dir)
    report_path = Path(report_dir)

    output_path.mkdir(parents=True, exist_ok=True)
    report_path.mkdir(parents=True, exist_ok=True)

    # Load dataset
    print("\n[1/7] Loading dataset...")

    dataset_path = Path(dataset_path)

    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {dataset_path}"
        )

    df = pd.read_csv(dataset_path)

    if target_col not in df.columns:
        raise ValueError(
            f"Target column '{target_col}' not found."
        )

    print(f"Dataset loaded: {df.shape}")

    # Agent 1: Data Analyst
    print("\n[2/7] Running Data Analyst Agent...")

    analyst = DataAnalystAgent()
    analysis_report = analyst.analyze(df)
    analyst.display_summary(analysis_report)

    # Agent 2: Data Quality
    print("\n[3/7] Running Data Quality Agent...")

    quality_agent = DataQualityAgent()
    quality_report = quality_agent.analyze(df)
    quality_agent.display_report(quality_report)

    # Agent 3: Preprocessing Planner
    print("\n[4/7] Running Preprocessing Planner Agent...")

    planner = PreprocessingPlannerAgent()

    preprocessing_plan = planner.create_plan(
        analysis_report,
        quality_report,
        target_col=target_col,
    )

    planner.display_plan(preprocessing_plan)

    # Agent 4: Preprocessing Engine
    print("\n[5/7] Running Preprocessing Engine Agent...")

    engine = PreprocessingEngineAgent()

    preprocessing_result = engine.preprocess(
        df,
        preprocessing_plan,
        target_col=target_col,
    )

    train_df = preprocessing_result["train_processed"]
    test_df = preprocessing_result["test_processed"]

    train_file = output_path / "train_processed.csv"
    test_file = output_path / "test_processed.csv"

    train_df.to_csv(train_file, index=False)
    test_df.to_csv(test_file, index=False)

    pipeline_file = output_path / "preprocessing_pipeline.joblib"

    joblib.dump(
        preprocessing_result["pipeline"],
        pipeline_file,
    )

    print(f"Training data saved: {train_file}")
    print(f"Testing data saved: {test_file}")
    print(f"Pipeline saved: {pipeline_file}")

    # Agent 5: Feature Engineering
    print("\n[6/7] Running Feature Engineering Agent...")

    feature_agent = FeatureEngineeringAgent()

    feature_report = feature_agent.analyze(
        train_df,
        test_df,
        target_col=target_col,
    )

    feature_agent.display_report(feature_report)

    # Agent 6: Validation
    print("\nRunning Validation Agent...")

    validation_agent = ValidationAgent()

    validation_report = validation_agent.validate(
        train_df,
        test_df,
        target_col=target_col,
    )

    validation_agent.display_report(validation_report)

    # Agent 7: Report Generation
    print("\n[7/7] Running Report Generation Agent...")

    report_agent = ReportAgent(output_dir=report_path)

    final_report = report_agent.generate_report(
        analysis_report=analysis_report,
        quality_report=quality_report,
        preprocessing_plan=preprocessing_plan,
        feature_report=feature_report,
        validation_report=validation_report,
    )

    json_report = report_agent.save_json(final_report)
    markdown_report = report_agent.save_markdown(final_report)

    print(f"JSON report saved: {json_report}")
    print(f"Markdown report saved: {markdown_report}")

    print("\n" + "=" * 65)
    print("       AUTOPREP AI WORKFLOW COMPLETED")
    print("=" * 65)

    print(
        f"Validation: {validation_report['overall_status']}"
    )
    print(
        f"Checks Passed: {validation_report['passed']}/"
        f"{validation_report['total_checks']}"
    )

    return {
        "analysis_report": analysis_report,
        "quality_report": quality_report,
        "preprocessing_plan": preprocessing_plan,
        "preprocessing_result": preprocessing_result,
        "feature_report": feature_report,
        "validation_report": validation_report,
        "final_report": final_report,
        "output_files": {
            "train": str(train_file),
            "test": str(test_file),
            "pipeline": str(pipeline_file),
            "json_report": str(json_report),
            "markdown_report": str(markdown_report),
        },
    }
