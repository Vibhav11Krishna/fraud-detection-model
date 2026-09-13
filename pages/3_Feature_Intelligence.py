import streamlit as st
import pandas as pd

st.set_page_config(page_title="Feature Intelligence", page_icon="🔍", layout="wide")

st.title("🔍 Advanced Feature Engineering & SHAP Intelligence")
st.markdown("A deep-dive technical analysis into how custom financial ledger errors and SHAP (Shapley Additive exPlanations) expose transactional anomalies.")

st.markdown("---")

# Section 1: Custom Math Telemetry
st.subheader("📐 Mathematical Formulation of Ledger Anomaly Features")
st.markdown("""
Standard machine learning models often fail on financial datasets because they evaluate balances in isolation (`oldBalance`, `newBalance`) without verifying the conservation of money. To solve this, custom delta features are engineered into the pipeline:
""")

math_col1, math_col2 = st.columns(2, gap="medium")

with math_col1:
    st.markdown("##### 🔴 Sender Balance Error (`errorBalanceOrg`)")
    st.latex(r"\text{errorBalanceOrg} = \text{newbalanceOrig} + \text{amount} - \text{oldbalanceOrg}")
    st.write("In a normal ledger, this value should compute close to `0.0`. When hackers execute unauthorized fund exfiltration, this calculation breaks down due to forced balance manipulation.")

with math_col2:
    st.markdown("##### 🔵 Receiver Balance Error (`errorBalanceDest`)")
    st.latex(r"\text{errorBalanceDest} = \text{newbalanceDest} + \text{amount} - \text{oldbalanceDest}")
    st.write("Exposes discrepancies where receiving accounts do not account for incoming transfers correctly, flagging automated mule accounts.")

st.markdown("---")

# Section 2: Behavioral Signatures Table
st.subheader("📊 Behavioral Transaction Signatures & Decision Boundaries")
st.markdown("How the XGBoost model differentiates between legitimate human behavior and malicious automation:")

signature_data = [
    {
        "Behavioral Pattern": "Account Wiping (0.00 Balance)",
        "Transaction Type": "TRANSFER / CASH_OUT",
        "Model Signal": "🚨 High Fraud Risk",
        "Underlying Mechanism": "Attackers immediately drain target accounts down to an exact zero balance to maximize extraction before account freezes."
    },
    {
        "Parameter Discrepancy": "Unmatched Delta Errors",
        "Transaction Type": "Any Type",
        "Model Signal": "🚨 High Fraud Risk",
        "Underlying Mechanism": "Non-zero `errorBalanceOrg` flags data tampering or automated bot scripts injecting fabricated transaction ledgers."
    },
    {
        "Behavioral Pattern": "Residual Capital Retention",
        "Transaction Type": "PAYMENT / DEBIT",
        "Model Signal": "✅ High Legitimacy",
        "Underlying Mechanism": "Normal consumer spending typically leaves fractional capital behind, which tree classifiers recognize as organic human behavior."
    },
    {
        "Behavioral Pattern": "Micro-Transactions",
        "Transaction Type": "CASH_IN",
        "Model Signal": "✅ High Legitimacy",
        "Underlying Mechanism": "Regular deposits and peer-to-peer transfers align perfectly with expected conservation-of-mass balance formulas."
    }
]

sig_df = pd.DataFrame(signature_data)
st.table(sig_df)

st.markdown("---")

# Section 3: SHAP Interpretability Deep Dive
st.subheader("🧠 Post-Hoc Explainability: Game Theory Meets FinTech")
st.markdown("Why incorporating **SHAP TreeExplainer** transforms this project from a standard classifier into an audit-ready enterprise tool:")

exp_col1, exp_col2, exp_col3 = st.columns(3, gap="medium")

with exp_col1:
    st.markdown("#### 🔬 Shapley Values")
    st.write("Derived from cooperative game theory, SHAP calculates the exact marginal contribution of every feature (`amount`, `errorBalanceOrg`, etc.) toward pushing a prediction score away from the base value.")

with exp_col2:
    st.markdown("#### ⚖️ Positive vs. Negative Pushes")
    st.write("Features that increase the log-odds of fraud are quantified with positive SHAP impacts, while stabilizing parameters push the score downward toward safe legitimacy.")

with exp_col3:
    st.markdown("#### 📑 Regulatory Compliance")
    st.write("Provides financial institutions with legally justifiable explanations for every automated transaction hold or block, satisfying modern algorithmic transparency mandates.")