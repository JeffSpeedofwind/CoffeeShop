import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(layout="wide")

st.title("📈 Detailed Sales Trends")
st.markdown("---")

# Load the data
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

data = load_data('Coffee sales.csv')

# Line chart of total money over time
st.header("💰 Total Money Over Time")
daily_sales = data.groupby('date')['money'].sum().reset_index()
fig = px.line(
    daily_sales,
    x='date',
    y='money',
    title="Total Daily Money Over Time",
    labels={'date': 'Date', 'money': 'Total Money ($)'}
)
st.plotly_chart(fig, use_container_width=True)