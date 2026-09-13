import streamlit as st
import pandas as pd

st.set_page_config(page_title="Compliance & Strategy", page_icon="📑", layout="wide")

st.title("📑 Enterprise Compliance & Risk Mitigation Strategy")
st.markdown("Operational guidelines, mitigation frameworks, and regulatory protocols for integrating automated fraud prediction into live banking workflows.")

st.markdown("---")

# Section 1: False Positive Management & Mitigation Matrix
st.subheader("⚖️ False Positive Management & Customer Friction Reduction")
st.markdown("""
As observed during validation, legitimate high-value account closures or complete wallet liquidations can occasionally trigger false positives due to complete balance depletion (`0.00`). Hard-blocking legitimate users creates severe customer friction. 

To resolve this, the system implements a **Tiered Risk Resolution Matrix**:
""")

matrix_data = [
    {
        "Risk Tier": "🟢 Low Risk (0% - 30%)",
        "Automated Action": "Instant Clearance",
        "Customer Experience": "Zero Friction",
        "Protocol Description": "Transaction clears the processing pipeline immediately without user interruption."
    },
    {
        "Risk Tier": "🟡 Moderate Risk (31% - 70%)",
        "Automated Action": "Frictionless Telemetry Check",
        "Customer Experience": "Background Verification",
        "Protocol Description": "Cross-references device fingerprint, IP geolocation, and velocity checks before silent clearance."
    },
    {
        "Risk Tier": "🟠 High Risk / Suspicious (71% - 89%)",
        "Automated Action": "Step-Up Authentication",
        "Customer Experience": "SMS / App OTP Challenge",
        "Protocol Description": "Temporarily pauses transfer execution and prompts the user for secondary multi-factor verification."
    },
    {
        "Risk Tier": "🔴 Critical Risk (90% - 100%)",
        "Automated Action": "Automated Account Hold",
        "Customer Experience": "Security Review Lock",
        "Protocol Description": "Freezes transfer immediately, flags account for human fraud analyst review, and logs SHAP telemetry."
    }
]

matrix_df = pd.DataFrame(matrix_data)
st.table(matrix_df)

st.markdown("---")

# Section 2: Regulatory Alignment & Audit Readiness
st.subheader("🛡️ Regulatory Framework & Financial Audit Readiness")
st.markdown("Ensuring absolute alignment with global banking compliance requirements and algorithmic transparency laws:")

reg_col1, reg_col2 = st.columns(2, gap="large")

with reg_col1:
    st.markdown("""
    #### 🔍 1. Explainability & The 'Right to Explanation'
    * **SHAP Transparency:** Leveraging Shapley Additive exPlanations guarantees that internal compliance officers and external regulators can legally justify *why* a specific automated action was taken.
    * **Eliminating Bias:** Itemized contribution tables ensure decisions are driven by mathematical ledger errors (`errorBalanceOrg`) rather than demographic or proxy bias.
    """)

with reg_col2:
    st.markdown("""
    #### 📋 2. Immutable Audit Logs & Traceability
    * **Telemetry Logging:** Every model inference logs exact input parameters, calculated error deltas, and probability scores.
    * **Forensic Readiness:** Compliance teams can instantly export complete audit trails for fraud investigations or anti-money laundering (AML) reporting.
    """)

st.markdown("---")

# Section 3: Operational Deployment Lifecycle
st.subheader("🚀 Production Deployment & Human-in-the-Loop Operations")
st.markdown("""
* **Human-in-the-Loop (HITL) Review:** High-risk automated flags feed directly into a secure queue for human compliance analysts, combining AI speed with human oversight.
* **Continuous Model Retraining:** Scheduled ingestion of newly confirmed fraud patterns ensures the XGBoost ensemble adapts to evolving cyber-attack vectors.
""")