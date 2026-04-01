import streamlit as st
from db_connection import get_data

# Title
st.title("Sales Analytics Dashboard (SQL)")

# Load data from database
df = get_data()

# Show data
st.subheader("Raw Data from Database")
st.write(df)

# Create revenue column
df["revenue"] = df["quantity"] * df["price"]

# Total Revenue
st.subheader("Total Revenue")
st.write(df["revenue"].sum())

# Sales by City
st.subheader("Sales by City")
sales_by_city = df.groupby("city")["revenue"].sum()
st.bar_chart(sales_by_city)

# Top Products
st.subheader("Top Selling Products")
top_products = df.groupby("product")["quantity"].sum()
st.bar_chart(top_products)