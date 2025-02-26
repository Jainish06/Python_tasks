# The most common complaint type.
# The percentage share of each complaint type

complaints = {
    "Late Delivery": 120,
    "Damaged Product": 95,
    "Wrong Item": 60,
    "Customer Service": 75,
    "Billing Issues": 50
}

def common_complaint(dict1):
    maxi = 0
    total_complaints = 0
    percent_dict = {}
    for names, num in dict1.items():
        total_complaints += num
        if num > maxi:
            maxi = num
            name = names
    for names, num in dict1.items():
        percent_dict[names] = round((num/total_complaints)*100,2)
    return name, percent_dict

name, percent_dict = common_complaint(complaints)
print(f"Top complaint : {name} \n Percentage of complaints : {percent_dict}")