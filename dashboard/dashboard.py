import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency
sns.set(style='dark')

# Load Data
full_merged = pd.read_csv("full_merged.csv")
rfm_table = pd.read_csv("rfm_table.csv")

st.title("E-commerce Data Analysis Dashboard")
st.sidebar.title("Navigation")

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Choose a Page",
    ["Home", "Product Analysis", "Sales Trends", "Payment Insights", "RFM Segmentation", "Advanced Visualizations"]
)

# Home Page
if page == "Home":
    st.header("Project Overview")
    st.write("""
        Welcome to the E-commerce Data Analysis Dashboard.
        This dashboard provides insights into product categories, sales trends, payment methods, and customer segmentation.
    """)
    # Summary Statistics
    total_transactions = len(full_merged)
    total_customers = rfm_table['customer_id'].nunique()
    avg_transaction_value = full_merged['price'].mean()

    st.subheader("Summary Statistics")
    st.write(f"**Total Transactions:** {total_transactions}")
    st.write(f"**Total Customers:** {total_customers}")
    st.write(f"**Average Transaction Value:** {avg_transaction_value:.2f} BRL")

# Product Analysis
elif page == "Product Analysis":
    st.header("Product Analysis")
    st.subheader("Top Product Categories by Purchase Frequency")
    top_categories = full_merged['product_category_name_english'].value_counts().head(10)
    st.bar_chart(top_categories)
    

    st.subheader("Top Product Categories by Total Transaction Value")
    category_total_value = full_merged.groupby('product_category_name_english')['price'].sum().sort_values(ascending=False)
    st.bar_chart(category_total_value.head(10))

# Sales Trends
elif page == "Sales Trends":
    st.header("Sales Trends")
    st.subheader("Monthly Sales Trends")
    sales_trends = full_merged.groupby('order_month').size()
    st.line_chart(sales_trends)

# Payment Insights
elif page == "Payment Insights":
    st.header("Payment Insights")
    st.subheader("Average Payment Value by Payment Type")
    avg_payment_value_by_type = full_merged.groupby('payment_type')['payment_value'].mean()
    st.bar_chart(avg_payment_value_by_type)

    st.subheader("Total Payment Value by Payment Type")
    total_payment_value_by_type = full_merged.groupby('payment_type')['payment_value'].sum()
    st.bar_chart(total_payment_value_by_type)

# RFM Segmentation
elif page == "RFM Segmentation":
    st.header("RFM Segmentation")
    st.subheader("Customer Distribution by RFM Segment")
    rfm_segment_counts = rfm_table['RFM_Segment'].value_counts()
    st.bar_chart(rfm_segment_counts)

    st.subheader("Top RFM Segments by Total Monetary Value")
    rfm_total_monetary_by_segment = rfm_table.groupby('RFM_Segment')['Monetary'].sum().sort_values(ascending=False)
    st.bar_chart(rfm_total_monetary_by_segment.head(10))

# Advanced Visualizations
elif page == "Advanced Visualizations":
    st.header("Advanced Visualizations")
    st.subheader("Scatter Plot: Product Weight vs Freight Value")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=full_merged,
        x='product_weight_g',
        y='freight_value',
        alpha=0.6
    )
    plt.title("Product Weight vs Freight Value")
    plt.xlabel("Product Weight (grams)")
    plt.ylabel("Freight Value (BRL)")
    st.pyplot(plt)

    st.subheader("Heatmap: Payment Type by Order Status")
    heatmap_data = full_merged.pivot_table(
        index='payment_type', columns='order_status', values='payment_value', aggfunc='sum'
    )
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="Blues")
    plt.title("Payment Type by Order Status (Total Payment Value)")
    st.pyplot(plt)

st.write("Thank you for exploring the dashboard!")
