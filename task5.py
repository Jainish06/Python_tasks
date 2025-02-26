#The employee with the highest sales.

#The top 3 employees sorted in descending order.

employee_sales = {
    "Alice": 5000,
    "Bob": 7500,
    "Charlie": 4200,
    "Diana": 9100,
    "Ethan": 6200
}

def highest_sales(dict1):
    maxi = 0
    for names, sales in dict1.items():
        if sales > maxi:
            maxi = sales
            name = names
    return name

name = highest_sales(employee_sales)
print(f"Top perforer : {name}")

top_3 = {k: v for k, v in sorted(employee_sales.items(), key=lambda item: item[1], reverse=True)}
print(list(top_3.items())[:3])