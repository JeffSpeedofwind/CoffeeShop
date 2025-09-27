import streamlit as st
import pandas as pd

# Set Streamlit page configuration
st.set_page_config(layout="wide")

st.title("☕ Coffee Shop Main Dashboard")
st.markdown("---")

# Load the data
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    # Ensure date/datetime columns are correctly formatted
    df['date'] = pd.to_datetime(df['date'])
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

data = load_data('Coffee sales.csv')

# Key Metrics
st.header("📊 Sales Overview")
col1, col2, col3 = st.columns(3)

with col1:
    total_sales = data['money'].sum()
    st.metric(label="💰 Total Sales", value=f"${total_sales:,.2f}")

with col2:
    total_transactions = data.shape[0]
    st.metric(label="🛍️ Total Transactions", value=total_transactions)

with col3:
    avg_transaction = data['money'].mean()
    st.metric(label="💵 Avg. Transaction Value", value=f"${avg_transaction:,.2f}")

st.markdown("---")

# Line Chart of Sales Over Time (using st.line_chart)
st.header("📈 Daily Sales Trend")

# 1. Aggregate data for the chart
daily_sales = data.groupby('date')['money'].sum().reset_index()

# 2. Set the 'date' column as the index for st.line_chart to correctly treat it as the x-axis
daily_sales_indexed = daily_sales.set_index('date')

# 3. Rename the column for better chart legend
daily_sales_indexed.columns = ['Total Daily Sales ($)']

# 4. Create the simple Streamlit line chart
st.line_chart(daily_sales_indexed)

# Data Table
st.header("📋 Raw Data")
st.dataframe(data)