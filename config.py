"""
AutoPrep AI - Project Configuration
"""

from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
REPORT_DIR = BASE_DIR / "reports"

# Dataset configuration
DATASET_NAME = "IBM HR Analytics Employee Attrition"
TARGET_COLUMN = "Attrition"

# Train-test configuration
TEST_SIZE = 0.20
RANDOM_STATE = 42

# Data quality configuration
MISSING_VALUE_THRESHOLD = 0.50
DUPLICATE_CHECK = True

# Feature engineering
DROP_CONSTANT_COLUMNS = True
DROP_IDENTIFIER_COLUMNS = True

# Project information
PROJECT_NAME = "AutoPrep AI"
PROJECT_VERSION = "1.0.0"
PROJECT_DESCRIPTION = (
    "Multi-Agent Intelligent Data Preprocessing System"
)

# Create required directories when the project runs
for directory in [DATA_DIR, OUTPUT_DIR, REPORT_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
