import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
sns.set(style='dark')


# load cleaned dataframe
#cleaned1_df = pd.read_csv('group1.csv', delimiter = ',')
cleaned2_df = pd.read_csv('group2.csv', delimiter = ',')
cleaned3_df = pd.read_csv('group3.csv', delimiter = ',')
order_df_copy = pd.read_csv("group4.csv", delimiter=",")
groupedonetimedata = pd.read_csv('groupedonetimedata.csv', delimiter=',')


st.header('Sales Performance Dashboard')
st.subheader('Sales performance in 3 years')

# plot Sales performasnce dashboard 
fig = plt.figure(figsize=(15, 4))
ax = sns.lineplot(
    y="order_id", 
    x="order_purchase_timestamp",
    data=groupedonetimedata.sort_values('order_purchase_timestamp', ascending=True),
)
plt.ticklabel_format(style='plain', axis='y')
plt.xlabel("Year-Month")
plt.ylabel("Order")
plt.xticks(rotation=45)
plt.title('Order in 3 Years')
st.pyplot(fig)


# plot Delivery performasnce dashboard 
st.subheader('Delivery performance in 3 years')

fig = plt.figure(figsize=(10, 4))
ax = sns.barplot(order_df_copy, x="delivery_report", y='delivery_delta', estimator="count", errorbar=None)
ax.bar_label(ax.containers[0],fontsize=10)

plt.ylabel('Amount of Order')
plt.title('Delivery Performance')
st.pyplot(fig)


# Product performance
st.subheader("Best & Worst Performing Product by Category")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3"]

sns.barplot(x="price", y="product_category_name", data=cleaned3_df.groupby(by="product_category_name").sum().sort_values('price', ascending=False).head(10), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Revenue (in million)", fontsize=30)
ax[0].set_title("Best Performing Product Category", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(x="price", y="product_category_name", data=cleaned3_df.groupby(by="product_category_name").sum().sort_values('price', ascending=True).head(10), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Revenue", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product Category", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)


# Customer per Category
st.subheader("Best product category by order")

fig = plt.figure(figsize=(10, 5))
colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3","#D3D3D3"]
ax = sns.barplot(
    x="customer_id", 
    y="product_category_name",
    data=cleaned3_df.groupby(by="product_category_name").nunique().sort_values('customer_id', ascending=False).head(10),
    palette=colors_
)
plt.title("Number of customer per category", loc="center", fontsize=10)
plt.ylabel('product category name')
plt.xlabel('customer count')
ax.tick_params(axis='y', labelsize=15)
ax.tick_params(axis='x', labelsize=10)
st.pyplot(fig)


# Sales per city and state
st.subheader("Revenue per cities and states")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

sns.barplot(y="customer_city", x="price", data=cleaned2_df.groupby(by="customer_city").nunique().sort_values('price', ascending=False).head(10), ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Revenue (in million)", fontsize=30)
ax[0].set_title("Revenue by city", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(y="customer_state", x="price", data=cleaned2_df.groupby(by="customer_state").nunique().sort_values('price', ascending=False).head(10), ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Revenue (in million)", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Revenue by state", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)


# Number of customers per city and state
st.subheader("Customer per cities and states")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

sns.barplot(y="customer_city", x="customer_id", data=cleaned2_df.groupby(by="customer_city").nunique().sort_values("customer_id",ascending=False).head(10), ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Number of customers", fontsize=30)
ax[0].set_title("Customer by city", loc="center", fontsize=40)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(y="customer_state", x="customer_id", data=cleaned2_df.groupby(by="customer_state").nunique().sort_values("customer_id",ascending=False).head(10), ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Number of customers", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Customer by state", loc="center", fontsize=40)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)
