import pandas as pd
import sqlite3

orders = pd.read_csv("orders.csv")
users = pd.read_json("users.json")

conn = sqlite3.connect("restaurants.db")
restaurants = pd.read_sql("SELECT * FROM restaurants", conn)

final_data = orders.merge(users, on="user_id", how="left")
final_data = final_data.merge(restaurants, on="restaurant_id", how="left")

final_data.to_csv("final_food_delivery_dataset.csv", index=False)

print("Dataset Created Successfully")
