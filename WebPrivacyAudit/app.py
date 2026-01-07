import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Privacy Audit Dashboard", page_icon="🔒", layout="wide")

# 2. Title & Header
st.title("🔒 University Privacy Compliance Auditor")
st.markdown("### Automated Detection of 'Pre-Consent' Tracking Cookies")
st.markdown("---")

# 3. Load Data
try:
  df = pd.read_csv("Privacy_audit_report.csv")
    
    # metrics
    total_sites = len(df)
    # We count how many rows have "YES" in them
    violations = len(df[df["Has_Tracking_Cookies"].astype(str).str.contains("YES")])
    safe_sites = total_sites - violations
    
    # 4. KPI Metrics (Top Row)
    col1, col2, col3 = st.columns(3)
    col1.metric("🌐 Total Websites Scanned", total_sites)
    col2.metric("✅ Safe / Compliant", safe_sites)
    col3.metric("⚠️ Privacy Violations", violations, delta="- High Risk", delta_color="inverse")

    st.divider()

    # 5. Charts & Data
    c1, c2 = st.columns([2, 1])

    with c1:
        st.subheader("📋 Detailed Forensic Report")
        
        # Function to color the table rows red/green
        def highlight_risk(val):
            color = '#ffcccb' if 'YES' in str(val) else '#90ee90'
            return f'background-color: {color}'
            
        # Show the table
        st.dataframe(df.style.map(highlight_risk, subset=['Has_Tracking_Cookies']), use_container_width=True)

    with c2:
        st.subheader("📊 Violation Ratio")
        # Pie Chart
        if total_sites > 0:
            fig = px.pie(values=[safe_sites, violations], names=["Safe", "Violations"], 
                         color_discrete_sequence=["#00CC96", "#EF553B"], hole=0.4)
            st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"⚠️ Error loading data: {e}")

    st.info("Make sure 'privacy_audit_report.csv' is in the same folder and closed!")
