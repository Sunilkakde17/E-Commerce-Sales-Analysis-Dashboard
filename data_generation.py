import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# -----------------------------
# BASIC SETTINGS
# -----------------------------
num_rows = 900  # between 800-1000

customer_segments = ['Consumer', 'Corporate', 'Home Office']
regions = ['North', 'South', 'East', 'West']

states_cities = {
    'North': ['Delhi', 'Chandigarh'],
    'South': ['Bangalore', 'Chennai'],
    'East': ['Kolkata', 'Bhubaneswar'],
    'West': ['Mumbai', 'Ahmedabad']
}

product_data = {
    'Electronics': {
        'Mobiles': ['iPhone', 'Samsung Galaxy', 'OnePlus'],
        'Laptops': ['Dell Laptop', 'HP Laptop', 'MacBook']
    },
    'Furniture': {
        'Chairs': ['Office Chair', 'Gaming Chair'],
        'Tables': ['Dining Table', 'Study Table']
    },
    'Clothing': {
        'Men': ['T-Shirt', 'Jeans'],
        'Women': ['Dress', 'Kurti']
    },
    'Grocery': {
        'Beverages': ['Tea', 'Coffee'],
        'Snacks': ['Chips', 'Biscuits']
    }
}

# -----------------------------
# GENERATE DATA
# -----------------------------

data = []

for i in range(num_rows):
    
    order_id = 1000 + i
    order_date = datetime.today() - timedelta(days=random.randint(0, 365))
    
    customer_id = random.randint(1, 300)
    customer_segment = random.choice(customer_segments)
    
    region = random.choice(regions)
    state = random.choice(states_cities[region])
    city = state
    
    category = random.choice(list(product_data.keys()))
    subcategory = random.choice(list(product_data[category].keys()))
    product_name = random.choice(product_data[category][subcategory])
    
    quantity = random.randint(1, 5)
    unit_price = random.randint(200, 5000)
    discount = round(random.uniform(0, 0.3), 2)
    
    revenue = quantity * unit_price * (1 - discount)
    
    cost_percentage = random.uniform(0.6, 0.8)
    cost = quantity * unit_price * cost_percentage
    
    profit = revenue - cost
    
    data.append([
        order_id, order_date, customer_id, customer_segment,
        region, state, city, category, subcategory, product_name,
        quantity, unit_price, discount,
        revenue, cost, profit
    ])

columns = [
    'order_id', 'order_date', 'customer_id', 'customer_segment',
    'region', 'state', 'city', 'product_category', 'product_subcategory',
    'product_name', 'quantity', 'unit_price', 'discount',
    'revenue', 'cost', 'profit'
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("data/ecommerce_sales.csv", index=False)

print("Dataset Generated Successfully!")