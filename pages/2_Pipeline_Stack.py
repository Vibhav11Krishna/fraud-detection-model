import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pipeline & Tech Stack", page_icon="⚙️", layout="wide")

st.title("⚙️ Model Pipeline & Tech Stack Architecture")
st.markdown("A comprehensive breakdown of the core libraries, machine learning algorithms, and code operations powering this system.")

st.markdown("---")
st.subheader("🛠️ Core Technology Stack Overview")

# Structured table for the tech stack with verified image/icon slugs and descriptions
tech_stack_data = [
    {
        "Technology": "Python 3.13",
        "Category": "Core Framework",
        "Icon Slug": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/python.svg",
        "Role & Responsibility": "Serves as the primary backend runtime environment executing data transformations and model scoring."
    },
    {
        "Technology": "Streamlit",
        "Category": "Core Framework",
        "Icon Slug": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/streamlit.svg",
        "Role & Responsibility": "Powers the interactive multi-page web application interface and user widgets."
    },
    {
        "Technology": "Pandas & NumPy",
        "Category": "Core Framework",
        "Icon Slug": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/pandas.svg",
        "Role & Responsibility": "Handles high-performance dataframe formatting, numerical array manipulations, and telemetry processing."
    },
    {
        "Technology": "XGBoost",
        "Category": "Machine Learning",
        "Icon Slug": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/xgboost.svg",
        "Role & Responsibility": "Executes optimized gradient-boosted decision trees to compute real-time fraud probability classifications."
    },
    {
        "Technology": "Scikit-Learn",
        "Category": "Machine Learning",
        "Icon Slug": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/scikitlearn.svg",
        "Role & Responsibility": "Manages categorical label encoding, feature scaling, and performance evaluation metrics."
    },
    {
        "Technology": "Joblib",
        "Category": "Machine Learning",
        "Icon Slug": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/anaconda.svg",
        "Role & Responsibility": "Handles efficient serialization, caching, and loading of trained `.pkl` model artifacts."
    },
    {
        "Technology": "SHAP",
        "Category": "Explainability & Ops",
        "Icon Slug": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/plotly.svg",
        "Role & Responsibility": "Computes TreeExplainer Shapley values to generate transparent, audit-ready feature impact breakdowns."
    },
    {
        "Technology": "Git & GitHub",
        "Category": "Explainability & Ops",
        "Icon Slug": "https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/git.svg",
        "Role & Responsibility": "Maintains source code version control, remote backups, and collaborative repository tracking."
    }
]

formatted_tech = []
for item in tech_stack_data:
    formatted_tech.append({
        "Icon": f'<img src="{item["Icon Slug"]}" width="22" style="vertical-align: middle;" />',
        "Technology": item["Technology"],
        "Category": item["Category"],
        "Role & Responsibility": item["Role & Responsibility"]
    })

tech_df = pd.DataFrame(formatted_tech)
st.write(tech_df.to_html(escape=False, index=False), unsafe_allow_html=True)

st.markdown("---")
st.subheader("🔄 End-to-End Pipeline Workflow & Code Operations")
st.markdown("Detailed breakdown of what each pipeline phase executes programmatically:")

workflow_data = [
    {
        "Pipeline Stage": "1️⃣ Data Ingestion",
        "Target Component": "PaySim Financial Dataset",
        "What the Code Does": "Loads streaming parameters, maps raw transaction types (CASH_IN, CASH_OUT, TRANSFER), and initializes form variables."
    },
    {
        "Pipeline Stage": "2️⃣ Feature Engineering",
        "Target Component": "Custom Delta Formulas",
        "What the Code Does": "Computes structural imbalance vectors programmatically: <code>errorBalanceOrg = newbalanceOrig + amount - oldbalanceOrg</code> and corresponding destination balance anomalies."
    },
    {
        "Pipeline Stage": "3️⃣ Ensemble Classification",
        "Target Component": "XGBoost & Joblib Engine",
        "What the Code Does": "Deserializes trained model artifacts via <code>joblib.load()</code>, passes structured inputs through gradient-boosted trees, and computes real-time fraud probability scores."
    },
    {
        "Pipeline Stage": "4️⃣ Explainability Audit",
        "Target Component": "SHAP TreeExplainer",
        "What the Code Does": "Calculates local Shapley values across individual features, sorting positive and negative model contribution pushes to display itemized tabular telemetry."
    }
]

st.table(workflow_data)