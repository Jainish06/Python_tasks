sales_data = {
    "Store_A": {"Laptop": 15, "Phone": 30, "Tablet": 10},
    "Store_B": {"Laptop": 25, "Phone": 20, "Tablet": 15},
    "Store_C": {"Laptop": 10, "Phone": 35, "Tablet": 5}
}

product_prices = {
    "Laptop": 1000,
    "Phone": 500,
    "Tablet": 300
}

store_revenue = {}
for store, products in sales_data.items():
    revenue = sum(products[product] * product_prices[product] for product in products)
    store_revenue[store] = revenue

most_profitable_store = max(store_revenue, key=store_revenue.get)

print(f"Revenue per store: {store_revenue}")
print(f"Most profitable store: {most_profitable_store}")


