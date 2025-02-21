sales_data = {
    "Store_A": {
        "Laptop": 15,
        "Phone": 30,
        "Tablet": 10
    },
    "Store_B": {
        "Laptop": 25,
        "Phone": 20,
        "Tablet": 15
    },
    "Store_C": {
        "Laptop": 10,
        "Phone": 35,
        "Tablet": 5
    }
}

#Find the total sales for each product across all stores.

def total(dict1):
    total_quantity = {}
    for store,products in dict1.items():
        for product,quantity in products.items():
            total_quantity[product] = total_quantity.get(product,0) + quantity

    return total_quantity


#Identify the store with the highest total sales (sum of all products).
def highest_total_sales(dict2):
    total_sales = {}
    for store, products in dict2.items():
        total_sales[store] = sum(products.values())
    highest_store = max(total_sales, key=total_sales.get)
    print(f"Highest sales : {highest_store} : {total_sales[highest_store]}")
    return total_sales

total_quantity = total(sales_data)

#Find the best-selling product (i.e., the product with the highest total sales).
def best_selling_product(dict3):

    sorted_total_quantity = {k: v for k, v in sorted(total_quantity.items(), key=lambda item: item[1], reverse=True)}
    keys = list(sorted_total_quantity.keys())
    values = list(sorted_total_quantity.values())
    print(f"Best selling product : {keys[0]} : {values[0]}")


print(total_quantity)
total(sales_data)
total_sales = highest_total_sales(sales_data)


sorted_total_sales = {k: v for k, v in sorted(total_sales.items(), key=lambda item: item[1], reverse=True)}

best_selling_product(total_quantity)
print(sorted_total_sales)