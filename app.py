import streamlit as st
import pandas as pd
from pathlib import Path

from config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    DATA_DIR,
    OUTPUT_DIR,
)

st.set_page_config(
    page_title=PROJECT_NAME,
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 AutoPrep AI")
st.caption("Multi-Agent Intelligent Data Preprocessing System")

st.markdown("---")

st.subheader("Welcome to AutoPrep AI")
st.write(
    "Upload your dataset and explore its structure, "
    "data quality, and preprocessing readiness."
)

uploaded_file = st.file_uploader(
    "Upload your CSV dataset",
    type=["csv"],
)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.success("Dataset uploaded successfully!")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Rows", f"{df.shape[0]:,}")
        col2.metric("Total Columns", f"{df.shape[1]:,}")
        col3.metric("Missing Values", f"{df.isnull().sum().sum():,}")

        st.subheader("Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)

        st.subheader("Dataset Information")

        info_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str).values,
            "Missing Values": df.isnull().sum().values,
            "Unique Values": df.nunique().values,
        })

        st.dataframe(info_df, use_container_width=True)

        st.subheader("Missing Value Summary")
        missing_df = (
            df.isnull()
            .sum()
            .reset_index()
        )
        missing_df.columns = ["Column", "Missing Values"]
        missing_df = missing_df[
            missing_df["Missing Values"] > 0
        ]

        if missing_df.empty:
            st.info("No missing values found.")
        else:
            st.dataframe(missing_df, use_container_width=True)

    except Exception as error:
        st.error(f"Unable to read dataset: {error}")

else:
    st.info("Upload a CSV file to begin dataset analysis.")

st.markdown("---")

st.sidebar.title("AutoPrep AI")
st.sidebar.write(f"Version: {PROJECT_VERSION}")
st.sidebar.write("AI-powered preprocessing workflow")

st.sidebar.markdown(
    """
    **Planned Agents**
    - Data Analyst
    - Data Quality
    - Preprocessing Planner
    - Preprocessing Engine
    - Feature Engineering
    - Validation
    - Report Generation
    """
)

st.sidebar.caption("AutoPrep AI | Industry-oriented AI project")
