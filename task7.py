# The marketing channel with the highest conversion rate.

# The average conversion rate across all channels

marketing_performance = {
    "Facebook Ads": 3.2,
    "Google Ads": 4.8,
    "Email Marketing": 2.5,
    "Organic Search": 5.6,
    "Referral": 3.9
}

def highest_conversion_rate(dict1):
    maxi = 0
    sum = 0
    count = 0
    for names, rate in dict1.items():
        if rate > maxi :
            maxi = rate
            name = names
        sum += rate
        count += 1
    return sum, name, count

sum, name, count = highest_conversion_rate(marketing_performance)
print(f"Best Performing Channel: {name} : {marketing_performance[name]} \n Average : {round(sum/count,2)}")
