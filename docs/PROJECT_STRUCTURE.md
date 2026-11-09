# AutoPrep AI - Project Structure

AutoPrep AI follows a modular architecture that separates agents, orchestration, configuration, testing, and documentation.

## Directory Structure

```text
Auto-Prep-AI/
│
├── app.py
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── .streamlit/
│   └── config.toml
│
├── data/
│   └── README.md
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── INSTALLATION.md
│   ├── USAGE.md
│   └── PROJECT_STRUCTURE.md
│
├── src/
│   ├── __init__.py
│   ├── orchestrator.py
│   │
│   └── agents/
│       ├── __init__.py
│       ├── data_analyst.py
│       ├── data_quality.py
│       ├── preprocessing_planner.py
│       ├── preprocessing_engine.py
│       ├── feature_engineering.py
│       ├── validation.py
│       └── report_agent.py
│
└── tests/
    ├── test_agents.py
    └── README.md
