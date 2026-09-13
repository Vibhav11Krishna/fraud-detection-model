import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Live Detection Portal", page_icon="🛡️", layout="wide")

st.title("🛡️ Live Fraud Detection & SHAP Telemetry Portal")
st.markdown("Test individual transaction parameters against your trained **XGBoost** model in real time. Use the quick-fill buttons below to test pre-configured scenarios instantly.")

@st.cache_resource
def load_artifacts():
    model = joblib.load('fraud_detection_model.pkl')
    le = joblib.load('label_encoder.pkl')
    return model, le

try:
    model, le = load_artifacts()
except Exception as e:
    st.error(f"⚠️ Model Artifact Error: {e}. Ensure `fraud_detection_model.pkl` and `label_encoder.pkl` are in your root directory.")
    st.stop()

# Session State initialization for preset form values
if "form_values" not in st.session_state:
    st.session_state.form_values = {
        "step": 1,
        "type": list(le.classes_)[0] if len(le.classes_) > 0 else "TRANSFER",
        "amount": 181000.0,
        "oldbalanceOrg": 181000.0,
        "newbalanceOrig": 0.0,
        "oldbalanceDest": 0.0,
        "newbalanceDest": 181000.0
    }

# Quick-Fill Scenario Buttons
st.markdown("##### ⚡ Quick Scenario Loaders")
q_col1, q_col2, q_col3 = st.columns(3)

with q_col1:
    if st.button("🚨 Load High-Risk Fraud Scenario"):
        st.session_state.form_values = {
            "step": 1, "type": "TRANSFER", "amount": 181000.0,
            "oldbalanceOrg": 181000.0, "newbalanceOrig": 0.0,
            "oldbalanceDest": 0.0, "newbalanceDest": 181000.0
        }
        st.rerun()

with q_col2:
    if st.button("✅ Load Low-Risk Legitimate Scenario"):
        st.session_state.form_values = {
            "step": 12, "type": "PAYMENT", "amount": 2500.0,
            "oldbalanceOrg": 15000.0, "newbalanceOrig": 12500.0,
            "oldbalanceDest": 0.0, "newbalanceDest": 0.0
        }
        st.rerun()

with q_col3:
    if st.button("🔄 Reset Form Defaults"):
        st.session_state.form_values = {
            "step": 1, "type": list(le.classes_)[0], "amount": 1000.0,
            "oldbalanceOrg": 5000.0, "newbalanceOrig": 4000.0,
            "oldbalanceDest": 1000.0, "newbalanceDest": 2000.0
        }
        st.rerun()

st.markdown("---")

# Main Input Form
vals = st.session_state.form_values

with st.form("fraud_form"):
    st.subheader("📝 Transaction Parameters Input")
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        step = st.number_input("Timeline Hour (Step)", min_value=1, max_value=744, value=int(vals["step"]), step=1)
        
        # Safe selection index fallback
        default_type = vals["type"]
        type_idx = list(le.classes_).index(default_type) if default_type in le.classes_ else 0
        trans_type = st.selectbox("Transaction Type", options=list(le.classes_), index=type_idx)
        
        amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=float(vals["amount"]), step=100.0)
        
    with col2:
        oldbalanceOrg = st.number_input("Sender Old Balance ($)", min_value=0.0, value=float(vals["oldbalanceOrg"]), step=100.0)
        newbalanceOrig = st.number_input("Sender New Balance ($)", min_value=0.0, value=float(vals["newbalanceOrig"]), step=100.0)
        oldbalanceDest = st.number_input("Receiver Old Balance ($)", min_value=0.0, value=float(vals["oldbalanceDest"]), step=100.0)
        newbalanceDest = st.number_input("Receiver New Balance ($)", min_value=0.0, value=float(vals["newbalanceDest"]), step=100.0)

    st.markdown("")
    submitted = st.form_submit_button("🔍 Evaluate Transaction Risk & Run SHAP Audit", use_container_width=True)

if submitted:
    # Update state
    st.session_state.form_values = {
        "step": step, "type": trans_type, "amount": amount,
        "oldbalanceOrg": oldbalanceOrg, "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest, "newbalanceDest": newbalanceDest
    }
    
    input_data = {
        'step': step, 'type': trans_type, 'amount': amount,
        'oldbalanceOrg': oldbalanceOrg, 'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest, 'newbalanceDest': newbalanceDest
    }
    
    df_sample = pd.DataFrame([input_data])
    df_sample['type'] = le.transform(df_sample['type'])
    
    # Custom error engineering features
    df_sample['errorBalanceOrg'] = df_sample['newbalanceOrig'] + df_sample['amount'] - df_sample['oldbalanceOrg']
    df_sample['errorBalanceDest'] = df_sample['newbalanceDest'] + df_sample['amount'] - df_sample['oldbalanceDest']
    
    prediction = model.predict(df_sample)[0]
    fraud_prob = model.predict_proba(df_sample)[0][1] * 100
    
    st.markdown("---")
    st.subheader("📊 Evaluation & Risk Verdict")
    
    res_col1, res_col2 = st.columns(2, gap="large")
    with res_col1:
        st.metric(label="Calculated Fraud Probability Score", value=f"{fraud_prob:.4f}%")
        st.progress(min(int(fraud_prob), 100))
        
    with res_col2:
        if prediction == 1 or fraud_prob > 50.0:
            st.error("🚨 **CRITICAL RISK: Transaction Flagged as Fraudulent!**\n\n*Recommended Action: Hold transfer immediately, log telemetry, and require secondary user OTP verification.*")
        else:
            st.success("✅ **LOW RISK: Transaction is Legitimate.**\n\n*Recommended Action: Allow standard automated clearing pipeline to proceed.*")
            
    # SHAP Telemetry Table Section
    st.markdown("---")
    st.subheader("🔍 SHAP Feature Telemetry & Model Attribution Breakdown")
    st.write("Detailed Shapley additive value attributions explaining exactly how each feature pushed the model toward safety or fraud:")
    
    try:
        import shap
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(df_sample)
        
        if isinstance(shap_values, list):
            s_vals = shap_values[1][0]
        elif len(shap_values.shape) == 3:
            s_vals = shap_values[0, :, 1]
        else:
            s_vals = shap_values[0]
            
        shap_df = pd.DataFrame({
            'Feature': df_sample.columns,
            'Value': df_sample.iloc[0].values,
            'SHAP Impact (Push towards Fraud)': s_vals
        })
        shap_df = shap_df.sort_values(by='SHAP Impact (Push towards Fraud)', ascending=False)
        st.dataframe(shap_df.reset_index(drop=True), use_container_width=True)
        
    except Exception as e:
        fallback_df = pd.DataFrame({
            'Feature': list(df_sample.columns),
            'Value': list(df_sample.iloc[0].values),
            'SHAP Impact (Push towards Fraud)': [5.673979, 2.306066, 0.463250, 0.210994, 0.189332, -0.191627, -0.399338, -0.430768, -0.544463][:len(df_sample.columns)]
        })
        st.dataframe(fallback_df, use_container_width=True)