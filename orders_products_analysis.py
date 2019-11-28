# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 22:47:41 2019

@author: Admin
"""

import pandas as pd





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
most_frequency_products = frequency_products[frequency_products["frequency"] >= 0.1]

categories_frequent_products = dataProducts.loc[dataProducts["product_id"].isin (most_frequency_products.index.values.tolist())]["product_category_name"]




        
    