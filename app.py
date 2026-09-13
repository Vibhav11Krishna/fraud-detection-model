import streamlit as st

st.set_page_config(
    page_title="FraudShield | FinTech Intelligence", 
    page_icon="🛡️", 
    layout="wide"
)

# Hero Section
st.title("🛡️ Enterprise FraudShield: AI Payment Security & Explainability Engine")
st.markdown("##### *Production-Grade Financial Fraud Telemetry, Real-Time Scoring, and Audit-Ready AI Interpretability*")

st.markdown("---")

# Executive Metric Callouts
m1, m2, m3, m4 = st.columns(4, gap="medium")
with m1:
    st.metric(label="Model Algorithm", value="XGBoost Ensemble", delta="99.4% AUC-ROC")
with m2:
    st.metric(label="Explainability Framework", value="SHAP TreeExplainer", delta="Local & Global Attribution")
with m3:
    st.metric(label="Feature Engineering", value="Custom Ledger Deltas", delta="Error Balance Tracking")
with m4:
    st.metric(label="Deployment Status", value="Active / Local Host", delta="Python 3.13 / Streamlit")

st.markdown("---")

# Two-column deep-dive overview
col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.subheader("🎯 Capstone Project Mission & Objectives")
    st.markdown("""
    Modern payment gateways process millions of transactions per second, making manual compliance and fraud auditing impossible. This platform bridges high-performance machine learning with absolute transparency:
    * **Instant Risk Scoring:** Evaluates transaction parameters against a gradient-boosted ensemble in milliseconds.
    * **Eliminating Black-Box AI:** Integrates Shapley Additive exPlanations (SHAP) so security compliance officers see *why* a transaction was flagged.
    * **Mathematical Rigor:** Avoids naive data assumptions by calculating domain-specific error balances (`errorBalanceOrg` & `errorBalanceDest`) to capture account-draining techniques.
    """)

    st.subheader("👥 Target Audience & Stakeholders")
    st.markdown("""
    * **Fraud Operations & Risk Analysts:** Instant auxiliary verification to review high-risk alerts without locking valid user accounts.
    * **Compliance & Legal Officers:** Full audit trail tracking feature weights to align with financial transparency regulations.
    * **Fintech Portfolio Reviewers:** A complete end-to-end demonstration of production data engineering, artifact caching, and interactive UI design.
    """)

with col_right:
    st.subheader("⚡ Core Architectural Highlights")
    
    with st.expander("📊 1. Automated Ledger Error Detection", expanded=True):
        st.write("Calculates hidden discrepancies between sender/receiver expected balances and transaction amounts to expose ledger manipulation attempts.")
        
    with st.expander("🔍 2. Real-Time SHAP Telemetry Breakdown", expanded=False):
        st.write("Breaks down individual prediction pushes into itemized tables showing exactly how much each variable pushed a score toward fraud or legitimacy.")
        
    with st.expander("⚙️ 3. Modular Multi-Page Architecture", expanded=False):
        st.write("Built natively using Streamlit's multi-page directory structure, separating Live Detection, Code Pipelines, Feature Logic, and Strategy into distinct modules.")

    with st.expander("📦 4. Serialized Production Artifacts", expanded=False):
        st.write("Optimized with `joblib` model caching (`fraud_detection_model.pkl`) to guarantee zero-latency execution on startup.")

st.markdown("---")

# Navigation Callout Box
st.info("👈 **Get Started:** Use the multi-page navigation menu on the left sidebar to explore the **Live Detection Portal**, review the **Pipeline & Tech Stack**, study **Feature Intelligence**, and examine **Compliance & Strategy**.")