    # 🛒 E-Commerce Sales & Profit Analysis Dashboard

## 📌 Project Overview

This is an end-to-end **E-Commerce Sales & Profit Analysis** project built using:

- **Python** (Data Generation + Exploratory Data Analysis)
- **MySQL** (Database Design + SQL Queries)
- **Power BI** (Interactive Dashboard)
- **DAX** (Business KPI Calculations)

The objective of this project is to simulate a real-world e-commerce business environment and analyze sales performance, profit trends, customer behavior, and product insights using industry-standard tools.

This project demonstrates strong data analytics, database design, and business intelligence skills suitable for **Data Analyst Internship / Entry-Level Data Analyst roles**.

---

# 🎯 Project Objectives

- Generate realistic synthetic sales data (800–1000 rows)
- Perform Exploratory Data Analysis (EDA)
- Design and implement a normalized MySQL database
- Write analytical SQL queries for business KPIs
- Build an interactive 3-page Power BI dashboard
- Apply DAX formulas for KPI calculations
- Derive meaningful business insights

---

# 🗂 Project Directory Structure

```
Ecommerce_Sales_Profit_Analysis/
│
├── data/
│   └── ecommerce_sales.csv
│
├── notebooks/
│   └── eda_analysis.ipynb
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── powerbi/
│   └── ecommerce_dashboard.pbix
│
├── screenshots/
│   ├── executive_summary.png
│   ├── product_performance.png
│   └── customer_insights.png
│
├── docs/
│   └── project_documentation.md
│
├── data_generation.py
│
└── README.md
```

---

# 🧠 Step 1 — Data Generation (Python)

## 🔹 Tools Used:
- pandas
- numpy
- faker
- random

## 🔹 Dataset Details:
Generated 900 synthetic records with the following fields:

- order_id
- order_date (last 12 months)
- customer_id
- customer_segment (Consumer, Corporate, Home Office)
- region (North, South, East, West)
- state
- city
- product_category (Electronics, Furniture, Clothing, Grocery)
- product_subcategory
- product_name
- quantity
- unit_price
- discount (%)
- revenue
- cost
- profit

## 🔹 Business Logic Used:

```
revenue = quantity × unit_price × (1 - discount)
cost = 60–80% of unit price
profit = revenue - cost
```

The dataset was exported as:

```
data/ecommerce_sales.csv
```

---

# 📊 Step 2 — Exploratory Data Analysis (EDA)

Performed using:
- pandas
- matplotlib
- seaborn

## 🔎 Analysis Performed:

- Dataset structure & summary
- Missing value check
- Revenue distribution
- Profit distribution
- Sales by region
- Profit by category
- Monthly revenue trend
- Top 10 products by revenue
- Customer segment analysis
- Correlation heatmap

## 📌 Key EDA Insights:

- Electronics category generates highest profit.
- West region contributes strong revenue performance.
- Higher discounts negatively impact profit margin.
- Consumer segment contributes the majority of revenue.
- Revenue shows seasonal variation across months.

---

# 🗄 Step 3 — Database Design (MySQL)

## 🔹 Database Name:
```
ecommerce_sales_db
```

## 🔹 Tables Created:

### 1️⃣ customers
- customer_id (Primary Key)
- customer_segment
- region
- state
- city

### 2️⃣ products
- product_id (Primary Key)
- product_category
- product_subcategory
- product_name

### 3️⃣ orders
- order_id (Primary Key)
- order_date
- customer_id (Foreign Key)

### 4️⃣ order_items
- order_item_id (Primary Key)
- order_id (Foreign Key)
- product_id (Foreign Key)
- quantity
- unit_price
- discount
- revenue
- cost
- profit

## 🔗 Relationships:

customers → orders → order_items ← products

This follows a **Star Schema design**, optimized for Power BI reporting.

---

# 📈 Step 4 — SQL Business Queries

## 🔹 KPIs Calculated:

- Total Revenue
- Total Profit
- Profit Margin %
- Sales by Region
- Top 5 Products
- Monthly Sales Trend
- Revenue by Customer Segment
- Loss-Making Products

## Example Query — Total Revenue:

```sql
SELECT SUM(revenue) AS total_revenue
FROM order_items;
```

---

# 📊 Step 5 — Power BI Dashboard

Built a **3-page interactive dashboard**.

---

## 📄 Page 1 — Executive Summary

✔ KPI Cards:
- Total Revenue
- Total Profit
- Profit Margin %
- Total Orders
- Average Order Value

✔ Monthly Revenue Trend (Line Chart)  
✔ Sales by Region (Bar Chart)
![Executive Summary](images/Execute_Summary.png)
---

## 📄 Page 2 — Product Performance

✔ Revenue by Category  
✔ Profit by Category  
✔ Top 10 Products  
✔ Discount vs Profit (Scatter Plot)
![Product Performance](images/Product_Performance.png)
---

## 📄 Page 3 — Customer Insights

✔ Revenue by Customer Segment  
✔ Region Filter (Slicer)  
✔ Category Filter  
✔ Date Slicer  
✔ Detailed Orders Table  
![Customer Insights](images/Customer_Insights.png)
---

# 🧮 DAX Measures Used

```DAX
Total Revenue = SUM(order_items[revenue])

Total Profit = SUM(order_items[profit])

Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)

Total Orders = DISTINCTCOUNT(orders[order_id])

Average Order Value = DIVIDE([Total Revenue], [Total Orders])
```

---

# 📌 Key Business Insights

- Electronics is the highest revenue-generating category.
- Consumer segment contributes the largest portion of sales.
- Profit margin averages ~17%.
- High discounts reduce profitability significantly.
- Revenue fluctuates seasonally across months.
- Certain products contribute disproportionately to total profit.

---

# 🛠 Tools & Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- MySQL
- SQL
- Power BI
- DAX

---

# 🚀 Skills Demonstrated

✔ Data Cleaning & Preparation  
✔ Exploratory Data Analysis  
✔ Relational Database Design  
✔ SQL Query Writing  
✔ Data Modeling  
✔ DAX Calculations  
✔ Business Intelligence Reporting  
✔ Dashboard Design  
✔ Business Insight Generation  

---

# 📌 Conclusion

This project simulates a real-world e-commerce analytics workflow from data generation to executive-level reporting. It demonstrates practical skills required for entry-level Data Analyst roles and showcases the ability to convert raw data into actionable business insights.

---

**Author:** Sunil Kakde  
**Role Targeted:** Data Analyst / Business Intelligence Analyst  

---