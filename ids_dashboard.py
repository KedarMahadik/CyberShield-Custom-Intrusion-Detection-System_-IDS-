import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="CyberShield IDS Dashboard", layout="wide")
st.title("🛡️ CyberShield Real-Time Security Monitor")

def load_data():
    """Pandas Pipeline for Log Management """
    try:
        # Load the unstructured log file 
        df = pd.read_csv('ids_security_events.log', sep='|', names=['Timestamp', 'Level', 'Event'])
        return df
    except:
        return pd.DataFrame()

# UI Layout 
placeholder = st.empty()

while True:
    df = load_data()
    
    with placeholder.container():
        if not df.empty:
            # Metric Row 
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Events", len(df))
            col2.metric("Critical Blocks", len(df[df['Level'].str.contains('CRITICAL')]))
            col3.metric("Warnings", len(df[df['Level'].str.contains('WARNING')]))

            # Visualizations 
            st.subheader("Event Distribution")
            event_counts = df['Level'].value_counts()
            st.bar_chart(event_counts)

            st.subheader("Recent Security Incident Logs")
            st.dataframe(df.tail(10), use_container_width=True)
        else:
            st.info("Waiting for security events...")

    time.sleep(2) # Refresh every 2 seconds