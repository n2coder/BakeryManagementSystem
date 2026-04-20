import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Bakery Dashboard", layout="wide")

# Title
st.title("🍞 Bakery Sales Intelligence Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/bakery_sales_2000.csv")
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df['day'] = df['sale_date'].dt.day_name()
    df['month'] = df['sale_date'].dt.month
    return df

df = load_data()

# ---- Sidebar Filters ----
st.sidebar.header("🔍 Filters")

# Date filter
min_date = df['sale_date'].min()
max_date = df['sale_date'].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)

# Item filter
items = st.sidebar.multiselect(
    "Select Items",
    options=df['item_name'].unique(),
    default=df['item_name'].unique()
)

# Apply filters
filtered_df = df[
    (df['sale_date'] >= pd.to_datetime(date_range[0])) &
    (df['sale_date'] <= pd.to_datetime(date_range[1])) &
    (df['item_name'].isin(items))
]

# ---- KPI Section ----
total_revenue = filtered_df['item_price'].sum()
total_orders = len(filtered_df)
top_item = filtered_df['item_name'].value_counts().idxmax()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Revenue", f"{total_revenue:.2f}")
col2.metric("🧾 Orders", total_orders)
col3.metric("🏆 Top Item", top_item)

st.markdown("---")

# ---- Charts Section ----
col1, col2 = st.columns(2)

# Top Items
with col1:
    st.subheader("Top Selling Items")
    item_counts = filtered_df['item_name'].value_counts()
    fig1, ax1 = plt.subplots()
    item_counts.plot(kind='bar', ax=ax1)
    st.pyplot(fig1)

# Revenue by Item
with col2:
    st.subheader("Revenue Distribution")
    revenue = filtered_df.groupby('item_name')['item_price'].sum()
    fig2, ax2 = plt.subplots()
    revenue.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
    st.pyplot(fig2)

# ---- Full Width Chart ----
st.subheader("📈 Daily Sales Trend")
daily_sales = filtered_df.groupby('sale_date')['item_price'].sum()

fig3, ax3 = plt.subplots()
daily_sales.plot(ax=ax3)
st.pyplot(fig3)

# ---- Advanced Insights ----
st.markdown("---")
st.subheader("📊 Advanced Insights")

col1, col2 = st.columns(2)

# Day-wise
with col1:
    st.write("Day-wise Sales")
    day_sales = filtered_df.groupby('day')['item_price'].sum()
    st.bar_chart(day_sales)

# Monthly
with col2:
    st.write("Monthly Sales")
    month_sales = filtered_df.groupby('month')['item_price'].sum()
    st.line_chart(month_sales)