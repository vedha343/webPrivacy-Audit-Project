import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Privacy Auditor", page_icon="🔒", layout="wide")

# --- HEADER ---
st.title("🔒 University Privacy Compliance Auditor")
st.divider()

# --- SMART FILE LOADER ---
# This block looks for the file in the current folder AND the main folder
file_name = "Privacy_audit_report.csv"
main_folder_path = f"../{file_name}" # Looks one step back

try:
    if os.path.exists(file_name):
        df = pd.read_csv(file_name)
    elif os.path.exists(main_folder_path):
        df = pd.read_csv(main_folder_path)
    else:
        # If both fail, trigger the error
        raise FileNotFoundError
    
    # --- METRICS LOGIC ---
    total_sites = len(df)
    violations = len(df[df['Has_Tracking_Cookies'].astype(str).str.contains("YES")])
    safe_sites = total_sites - violations

    # --- TOP METRICS ROW ---
    col1, col2, col3 = st.columns(3)
    col1.metric("🌐 Total Websites", total_sites)
    col2.metric("✅ Safe", safe_sites)
    col3.metric("⚠️ Violations", violations, delta="- High Risk", delta_color="inverse")

    # --- CHARTS ---
    c1, c2 = st.columns([2, 1])

    with c1:
        st.subheader("📋 Detailed Report")
        filter_opt = st.radio("Show:", ["All Websites", "Violations Only"], horizontal=True)
        
        if filter_opt == "Violations Only":
            display_df = df[df['Has_Tracking_Cookies'].astype(str).str.contains("YES")]
        else:
            display_df = df
            
        def highlight_row(val):
            color = '#ffcccb' if 'YES' in str(val) else '#c9f7c4'
            return f'background-color: {color}'

        st.dataframe(display_df.style.map(highlight_row, subset=['Has_Tracking_Cookies']), use_container_width=True)

    with c2:
        st.subheader("📊 Compliance Ratio")
        if total_sites > 0:
            fig = px.pie(values=[safe_sites, violations], names=["Safe", "Violations"], 
                         color_discrete_sequence=["#00CC96", "#EF553B"], hole=0.4)
            st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error(f"🚨 ERROR: Could not find '{file_name}'")
    st.warning("Debugging Info:")
    st.write(f"1. We looked in: {os.getcwd()}")
    st.write(f"2. We also looked in the folder above.")
    st.write("Files we CAN see here:", os.listdir())
