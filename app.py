import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🍞 Bakery Sales Dashboard")

# Load data
df = pd.read_csv("data/bakery_sales_2000.csv")

# Data preprocessing
df['sale_date'] = pd.to_datetime(df['sale_date'])

# KPIs
total_revenue = df['item_price'].sum()
total_orders = len(df)
top_item = df['item_name'].value_counts().idxmax()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Revenue", f"{total_revenue}")
col2.metric("🧾 Total Orders", total_orders)
col3.metric("🏆 Top Item", top_item)

# ---- Charts ----

# Top Items
st.subheader("Top Selling Items")
item_counts = df['item_name'].value_counts()

fig1, ax1 = plt.subplots()
item_counts.plot(kind='bar', ax=ax1)
st.pyplot(fig1)

# Daily Sales
st.subheader("Daily Sales Trend")
daily_sales = df.groupby('sale_date')['item_price'].sum()

fig2, ax2 = plt.subplots()
daily_sales.plot(ax=ax2)
st.pyplot(fig2)

# Revenue by Item
st.subheader("Revenue by Item")
revenue = df.groupby('item_name')['item_price'].sum()

fig3, ax3 = plt.subplots()
revenue.plot(kind='pie', autopct='%1.1f%%', ax=ax3)
st.pyplot(fig3)