"""
AutoPrep AI - Preprocessing Engine Agent

Builds and applies preprocessing pipelines
for numerical and categorical features.
"""

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class PreprocessingEngineAgent:

    def __init__(self, test_size=0.20, random_state=42):
        self.agent_name = "AutoPrep AI Preprocessing Engine Agent"
        self.test_size = test_size
        self.random_state = random_state
        self.pipeline = None

    def preprocess(self, df, plan, target_col="Attrition"):
        """Split data and apply the preprocessing plan."""

        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")

        if df.empty:
            raise ValueError("Dataset is empty.")

        if target_col not in df.columns:
            raise ValueError(
                f"Target column '{target_col}' was not found."
            )

        if df[target_col].isnull().any():
            raise ValueError(
                "Target column contains missing values. "
                "Handle them before training."
            )

        drop_columns = [
            col for col in plan.get("columns_to_drop", [])
            if col in df.columns and col != target_col
        ]

        clean_df = df.drop(columns=drop_columns).copy()

        numerical_features = [
            col for col in plan.get("numerical_features", [])
            if col in clean_df.columns and col != target_col
        ]

        categorical_features = [
            col for col in plan.get("categorical_features", [])
            if col in clean_df.columns and col != target_col
        ]

        X = clean_df.drop(columns=[target_col])
        y = clean_df[target_col]

        # Keep only features identified by the planner.
        selected_features = (
            numerical_features + categorical_features
        )

        if not selected_features:
            raise ValueError("No usable features were found.")

        X = X[selected_features]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=self.test_size,
            random_state=self.random_state,
            stratify=y if y.nunique() > 1 else None,
        )

        numerical_pipeline = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
            ]
        )

        categorical_pipeline = Pipeline(
            steps=[
                (
                    "imputer",
                    SimpleImputer(strategy="most_frequent"),
                ),
                (
                    "encoder",
                    OneHotEncoder(
                        handle_unknown="ignore",
                        sparse_output=False,
                    ),
                ),
            ]
        )

        transformers = []

        if numerical_features:
            transformers.append(
                ("numerical", numerical_pipeline, numerical_features)
            )

        if categorical_features:
            transformers.append(
                ("categorical", categorical_pipeline,
                 categorical_features)
            )

        self.pipeline = ColumnTransformer(
            transformers=transformers,
            remainder="drop",
        )

        # Fit only on training data to prevent data leakage.
        X_train_processed = self.pipeline.fit_transform(X_train)
        X_test_processed = self.pipeline.transform(X_test)

        feature_names = self.pipeline.get_feature_names_out()

        train_processed = pd.DataFrame(
            X_train_processed,
            columns=feature_names,
            index=X_train.index,
        )

        test_processed = pd.DataFrame(
            X_test_processed,
            columns=feature_names,
            index=X_test.index,
        )

        train_processed[target_col] = y_train
        test_processed[target_col] = y_test

        return {
            "train_processed": train_processed,
            "test_processed": test_processed,
            "pipeline": self.pipeline,
            "feature_names": feature_names.tolist(),
            "train_rows": len(X_train),
            "test_rows": len(X_test),
            "final_feature_count": len(feature_names),
            "dropped_columns": drop_columns,
        }
