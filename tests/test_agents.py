"""
AutoPrep AI - Agent Unit Tests

Tests the core functionality of AutoPrep AI agents.
"""

import unittest
import pandas as pd

from src.agents import (
    DataAnalystAgent,
    DataQualityAgent,
    PreprocessingPlannerAgent,
    PreprocessingEngineAgent,
    FeatureEngineeringAgent,
    ValidationAgent,
)


class TestAutoPrepAgents(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "Age": [25, 30, 35, 40, 45, 50, 55, 60],
            "Salary": [25000, 30000, 35000, 40000,
                       45000, 50000, 55000, 60000],
            "Department": [
                "IT", "HR", "IT", "Sales",
                "HR", "Sales", "IT", "HR"
            ],
            "Attrition": [
                "No", "Yes", "No", "No",
                "Yes", "No", "Yes", "No"
            ],
        })

    def test_data_analyst(self):
        agent = DataAnalystAgent()
        result = agent.analyze(self.df)

        self.assertEqual(result["total_rows"], 8)
        self.assertEqual(result["total_columns"], 4)
        self.assertIn("Age", result["numerical_columns"])

    def test_data_quality(self):
        agent = DataQualityAgent()
        result = agent.analyze(self.df)

        self.assertEqual(result["total_missing_values"], 0)
        self.assertEqual(result["duplicate_rows"], 0)

    def test_preprocessing_planner(self):
        analyst = DataAnalystAgent()
        quality = DataQualityAgent()

        analysis_report = analyst.analyze(self.df)
        quality_report = quality.analyze(self.df)

        planner = PreprocessingPlannerAgent()

        plan = planner.create_plan(
            analysis_report,
            quality_report,
            target_col="Attrition",
        )

        self.assertEqual(plan["target_column"], "Attrition")
        self.assertIn("Age", plan["numerical_features"])

    def test_preprocessing_engine(self):
        analyst = DataAnalystAgent()
        quality = DataQualityAgent()

        plan = PreprocessingPlannerAgent().create_plan(
            analyst.analyze(self.df),
            quality.analyze(self.df),
            target_col="Attrition",
        )

        engine = PreprocessingEngineAgent()

        result = engine.preprocess(
            self.df,
            plan,
            target_col="Attrition",
        )

        self.assertEqual(result["train_rows"], 6)
        self.assertEqual(result["test_rows"], 2)
        self.assertIsNotNone(result["pipeline"])

    def test_feature_engineering(self):
        analyst = DataAnalystAgent()
        quality = DataQualityAgent()

        plan = PreprocessingPlannerAgent().create_plan(
            analyst.analyze(self.df),
            quality.analyze(self.df),
            target_col="Attrition",
        )

        result = PreprocessingEngineAgent().preprocess(
            self.df,
            plan,
            target_col="Attrition",
        )

        report = FeatureEngineeringAgent().analyze(
            result["train_processed"],
            result["test_processed"],
            target_col="Attrition",
        )

        self.assertGreater(report["final_feature_count"], 0)
        self.assertTrue(report["target_preserved"])

    def test_validation(self):
        analyst = DataAnalystAgent()
        quality = DataQualityAgent()

        plan = PreprocessingPlannerAgent().create_plan(
            analyst.analyze(self.df),
            quality.analyze(self.df),
            target_col="Attrition",
        )

        result = PreprocessingEngineAgent().preprocess(
            self.df,
            plan,
            target_col="Attrition",
        )

        report = ValidationAgent().validate(
            result["train_processed"],
            result["test_processed"],
            target_col="Attrition",
        )

        self.assertEqual(report["overall_status"], "PASS")
        self.assertEqual(report["failed"], 0)


if __name__ == "__main__":
    unittest.main()
