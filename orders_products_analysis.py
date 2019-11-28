# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 22:47:41 2019

@author: Admin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


dataOrders = pd.read_csv("C:\\Users\\Admin\\Desktop\\Home\\Studies\\PFE\\ML_eCommerce_sales\\data\\orders.csv")
data_columns = dataOrders.columns.tolist()
dataItems = pd.read_csv("C:\\Users\\Admin\\Desktop\\Home\\Studies\\PFE\\ML_eCommerce_sales\\data\\items.csv")
data_columns = dataItems.columns.tolist()
dataProducts = pd.read_csv("C:\\Users\\Admin\\Desktop\\Home\\Studies\\PFE\\ML_eCommerce_sales\\data\\products.csv")
data_columns = dataProducts.columns.tolist()
dataCustomer = pd.read_csv("C:\\Users\\Admin\\Desktop\\Home\\Studies\\PFE\\ML_eCommerce_sales\\data\\customer.csv")
data_columns = dataCustomer.columns.tolist()


# comprendre les données 

all_orders_customer = dataOrders[dataOrders["customer_id"] == "9ef432eb6251297304e76186b10a928d"]

id = dataItems[dataItems["order_id"] == "00010242fe8c5a6d1ba2dd792cb16214"]["order_item_id"].sum()


orders = dataOrders["order_id"]

nb_item = pd.Series()

max_items = 0
for order in orders:
    nb_item = dataItems[dataItems["order_id"] == order]["order_item_id"].sum()
    if (nb_item > max_items):
        max_items = nb_item
        
sum_items = dataItems["order_item_id"].sum()
average_basket = sum_items // len(dataOrders) # use of integer division

frequency_products = (dataItems["product_id"].value_counts() / len(dataItems) * 100).sort_values(ascending=False)
frequency_products = pd.DataFrame(frequency_products)
frequency_products = frequency_products.rename(columns = {'Index':'product_iiid', 'product_id':'frequency'})
mean_frequency_products = frequency_products.mean()
best_product = frequency_products[frequency_products["frequency"] >= 0.1]

categories_frequent_products = dataProducts.loc[dataProducts["product_id"].isin (most_frequency_products.index.values.tolist())]["product_category_name"]

# evolution over time : months and years 

# ------- months -------
order_timestamp = dataOrders.loc[:,"order_purchase_timestamp"]
order_timestamp = pd.to_datetime(order_timestamp)
months = order_timestamp.dt.month

order_evolution_months = months.value_counts().sort_index()
order_evolution_months = pd.DataFrame(order_evolution_months)
mean_order_evolution_months = np.mean(order_evolution_months)
y_pos = np.arange(len(order_evolution_months.index.values.tolist()))

plt.bar(y_pos, order_evolution_months["order_purchase_timestamp"])
plt.xticks(y_pos, order_evolution_months.index.values.tolist())
plt.axhline(y=mean_order_evolution_months[0], color='r', linestyle='--')
plt.title("Evolution en fonction de mois")
plt.xlabel("Mois")
plt.ylabel("Nb de ventes")
plt.show()

# ----- year ------
years = order_timestamp.dt.year

order_evolution_years = years.value_counts().sort_index()
order_evolution_years = pd.DataFrame(order_evolution_years)

y_pos = np.arange(len(order_evolution_years.index.values.tolist()))

plt.bar(y_pos, order_evolution_years["order_purchase_timestamp"])
plt.xticks(y_pos, order_evolution_years.index.values.tolist())
plt.axhline(y=mean_order_evolution_months[0], color='r', linestyle='--')
plt.title("Evolution en fonction d'année")
plt.xlabel("Année")
plt.ylabel("Nb de ventes")
plt.show()

# the best sellers 

frequency_sellers = ((dataItems["seller_id"].value_counts() / len(dataItems)) * 100).sort_values(ascending=False)
frequency_sellers = pd.DataFrame(frequency_sellers)
frequency_sellers = frequency_products.rename(columns = {'seller_id':'frequency'})
mean_frequency_sellers = frequency_sellers.mean()
best_sellers = (frequency_sellers[frequency_sellers["frequency"] >= 0.1]).index.values.tolist()







        
    