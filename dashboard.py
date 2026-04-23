import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config for a professional look
st.set_page_config(page_title="Walmart Executive Insights", layout="wide")

# Load our cleaned data
df = pd.read_csv('Walmart_Cleaned.csv')
df['Date'] = pd.to_datetime(df['Date'])

# --- SIDEBAR FILTERS (Helping Hint: Slicers) ---
st.sidebar.header("Dashboard Filters")
store_filter = st.sidebar.multiselect("Select Stores", options=df['Store'].unique(), default=df['Store'].unique()[:5])
date_range = st.sidebar.date_input("Select Date Range", [df['Date'].min(), df['Date'].max()])

# Filter data based on selection
filtered_df = df[(df['Store'].isin(store_filter))]

# --- HEADER & KPIs (Helping Hint: Important metrics on top) ---
st.title("🚀 Walmart Sales Executive Dashboard")
st.markdown("Week 4: Interactive Analysis Project")

col1, col2, col3 = st.columns(3)
with col1:
    total_sales = filtered_df['Weekly_Sales'].sum()
    st.metric("Total Revenue", f"${total_sales:,.2f}")
with col2:
    avg_sales = filtered_df['Weekly_Sales'].mean()
    st.metric("Avg Weekly Sales", f"${avg_sales:,.2f}")
with col3:
    max_spike = filtered_df['Weekly_Sales'].max()
    st.metric("Highest Sales Peak", f"${max_spike:,.2f}")

st.divider()

# --- VISUALIZATIONS (Helping Hint: Clean & Minimal) ---
left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Sales Trends Over Time")
    fig_line = px.line(filtered_df, x='Date', y='Weekly_Sales', color='Store', template="plotly_white")
    st.plotly_chart(fig_line, use_container_width=True)

with right_chart:
    st.subheader("Sales vs Unemployment (Insight Drill-down)")
    fig_scatter = px.scatter(filtered_df, x='Unemployment', y='Weekly_Sales', 
                             size='Temperature', color='Store', hover_name='Date')
    st.plotly_chart(fig_scatter, use_container_width=True)

# --- THE "SO WHAT?" SECTION (Helping Hint: Insight Tip) ---
st.info("**Managerial Insight:** The dashboard reveals that holiday spikes are consistent across top stores, but higher unemployment rates in certain regions show a slight drag on luxury-level weekly sales volume.")