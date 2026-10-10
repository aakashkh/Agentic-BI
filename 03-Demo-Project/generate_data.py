#!/usr/bin/env python3
"""
Generate realistic retail sales data for the Agentic BI workshop demo project.
Creates CSV files in 03-Demo-Project/Data/ for FactSales, DimCustomer, DimProduct, and DimDate.
"""

import os
import csv
import random
from datetime import datetime, timedelta

def generate_data():
    data_dir = os.path.join(os.path.dirname(__file__), "Data")
    os.makedirs(data_dir, exist_ok=True)
    random.seed(42)

    # 1. DimCustomer (200 Customers)
    customers_file = os.path.join(data_dir, "DimCustomer.csv")
    segments = ["Consumer", "SMB", "Enterprise"]
    countries = ["USA", "Canada", "United Kingdom", "Germany", "India", "Australia"]
    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Avery", "Priya", "Rahul", "Lukas", "Emma", "Liam", "Sophia", "Noah", "Olivia", "Ethan"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Khandelwal", "Patel", "Schneider", "Wilson"]

    customers = []
    with open(customers_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["CustomerID", "CustomerName", "CustomerSegment", "Country"])
        for i in range(1, 201):
            cid = f"CUST-{i:04d}"
            name = f"{random.choice(first_names)} {random.choice(last_names)}"
            seg = random.choice(segments)
            country = random.choice(countries)
            writer.writerow([cid, name, seg, country])
            customers.append(cid)

    # 2. DimProduct (50 Products across Categories & SubCategories)
    products_file = os.path.join(data_dir, "DimProduct.csv")
    catalog = {
        "Electronics": {
            "Laptops": [("ProBook 15", 899.99), ("UltraSlim 13", 1199.99), ("Workstation Z", 1899.99)],
            "Audio": [("NoiseCancel Headphones", 199.99), ("Wireless Earbuds", 129.99), ("Studio Soundbar", 299.99)],
            "Accessories": [("Ergo Mouse", 49.99), ("Mechanical Keyboard", 89.99), ("4K Monitor 27\"", 349.99)]
        },
        "Apparel": {
            "Clothing": [("Cotton Polo Shirt", 34.99), ("Denim Jacket", 79.99), ("Performance Hoodie", 59.99)],
            "Footwear": [("Trail Runner Shoes", 119.99), ("Casual Sneakers", 89.99), ("Leather Boots", 149.99)]
        },
        "Home & Office": {
            "Furniture": [("Ergonomic Office Chair", 249.99), ("Standing Desk 60\"", 499.99), ("Bookshelf Unit", 149.99)],
            "Lighting": [("LED Desk Lamp", 39.99), ("Ambient Floor Light", 79.99)]
        },
        "Sports": {
            "Fitness": [("Yoga Mat Pro", 29.99), ("Adjustable Dumbbell Set", 199.99), ("Smart Fitness Watch", 159.99)],
            "Outdoor": [("Camping Tent 4P", 189.99), ("Hiking Backpack 45L", 99.99)]
        }
    }

    products = []
    pid_counter = 1
    with open(products_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ProductID", "ProductName", "ProductCategory", "SubCategory", "UnitPrice"])
        for cat, subcats in catalog.items():
            for subcat, items in subcats.items():
                for pname, price in items:
                    pid = f"PROD-{pid_counter:04d}"
                    writer.writerow([pid, pname, cat, subcat, price])
                    products.append((pid, price))
                    pid_counter += 1

    # 3. DimDate (Calendar 2023-01-01 to 2026-12-31)
    dates_file = os.path.join(data_dir, "DimDate.csv")
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2026, 12, 31)

    dates = []
    with open(dates_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Year", "Quarter", "MonthName", "MonthNumber", "DayOfWeek"])
        curr = start_date
        while curr <= end_date:
            d_str = curr.strftime("%Y-%m-%d")
            q_str = f"Q{(curr.month - 1) // 3 + 1}"
            m_name = curr.strftime("%B")
            m_num = curr.month
            dow = curr.strftime("%A")
            writer.writerow([d_str, curr.year, q_str, m_name, m_num, dow])
            if curr <= datetime(2026, 9, 20):
                dates.append(curr)
            curr += timedelta(days=1)

    # 4. FactSales (5,000 Sales Transactions)
    sales_file = os.path.join(data_dir, "FactSales.csv")
    with open(sales_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["TransactionID", "OrderDate", "CustomerID", "ProductID", "Quantity", "UnitPrice", "DiscountAmount", "SalesAmount"])
        
        for tid in range(10001, 15001):
            tx_id = f"TX-{tid}"
            order_date = random.choice(dates).strftime("%Y-%m-%d")
            cid = random.choice(customers)
            pid, base_price = random.choice(products)
            qty = random.choices([1, 2, 3, 4, 5, 10], weights=[50, 25, 15, 5, 3, 2])[0]
            unit_price = base_price
            discount = round(random.choice([0, 0, 0, 0.05, 0.10, 0.15]) * (qty * unit_price), 2)
            sales_amt = round((qty * unit_price) - discount, 2)

            writer.writerow([tx_id, order_date, cid, pid, qty, unit_price, discount, sales_amt])

    print(f"Data generation complete!")
    print(f"DimCustomer: 200 rows")
    print(f"DimProduct: {len(products)} rows")
    print(f"DimDate: 1,461 rows")
    print(f"FactSales: 5,000 rows")

if __name__ == "__main__":
    generate_data()
