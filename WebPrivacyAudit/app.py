import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Privacy Auditor", page_icon="🔒", layout="wide")

# --- HEADER ---
st.title("🔒 University Privacy Compliance Auditor")
st.markdown("### 🕵️ Automated Detection of 'Pre-Consent' Tracking Cookies")
st.markdown("This dashboard analyzes whether educational websites track users illegally before they accept cookies.")
st.divider()

# --- LOAD DATA ---
try:
    # FIXED: Using Capital 'P' to match your GitHub file exactly
    df = pd.read_csv("Privacy_audit_report.csv")
    
    # --- METRICS LOGIC ---
    total_sites = len(df)
    
    # We look for "YES" in the violation column to count bad sites
    violations = len(df[df['Has_Tracking_Cookies'].astype(str).str.contains("YES")])
    safe_sites = total_sites - violations

    # --- TOP METRICS ROW ---
    col1, col2, col3 = st.columns(3)
    col1.metric("🌐 Total Websites Scanned", total_sites)
    col2.metric("✅ Safe / Compliant", safe_sites)
    col3.metric("⚠️ Privacy Violations", violations, delta="- High Risk", delta_color="inverse")

    st.write("") # Spacer

    # --- CHARTS AND TABLES ---
    c1, c2 = st.columns([2, 1])

    with c1:
        st.subheader("📋 Detailed Forensic Report")
        
        # Filter Options
        filter_opt = st.radio("Show:", ["All Websites", "Violations Only"], horizontal=True)
        
        if filter_opt == "Violations Only":
            display_df = df[df['Has_Tracking_Cookies'].astype(str).str.contains("YES")]
        else:
            display_df = df
            
        # Color Coding: Red for Violation, Green for Safe
        def highlight_row(val):
            color = '#ffcccb' if 'YES' in str(val) else '#c9f7c4'
            return f'background-color: {color}'

        # Show the table
        st.dataframe(display_df.style.map(highlight_row, subset=['Has_Tracking_Cookies']), use_container_width=True)

    with c2:
        st.subheader("📊 Compliance Ratio")
        if total_sites > 0:
            fig = px.pie(
                values=[safe_sites, violations], 
                names=["Safe", "Violations"], 
                color_discrete_sequence=["#00CC96", "#EF553B"], 
                hole=0.4
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No data found.")

except FileNotFoundError:
    st.error("🚨 ERROR: 'Privacy_audit_report.csv' not found.")
    st.info("Check the filename on GitHub! It is Case Sensitive.")
