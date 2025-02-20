student_dict = {
    'nilesh-geography': 89,
    'alpesh-history': 77,
    'shital-math': 93,
    'dimpal-hindi': 68,
    'nilesh-english': 74,
    'alpesh-sci': 85,
    'shital-history': 91,
    'dimpal-geography': 87,
    'nilesh-sci': 83,
    'alpesh-math': 92,
    'dimpal-english': 78,
    'shital-hindi': 81,
    'nilesh-history': 90,
    'alpesh-geography': 79,
    'dimpal-math': 84,
    'shital-sci': 88,
    'nilesh-hindi': 71,
    'alpesh-english': 80,
    'dimpal-sci': 89,
    'shital-geography': 82,
    'nilesh-math': 93,
    'alpesh-hindi': 75,
    'dimpal-history': 90,
    'shital-english': 87
}

total_dict = {}
count = 0
count_dict = {}
sub_dict = {}
for key, value in student_dict.items():
    names = key.split('-')[0]
    if total_dict.get(names):
        total_dict[names] += value
        count_dict[names] += 1
    else:
        total_dict[names] = value
        count_dict[names] = 1

for key, value in student_dict.items():
    subs = key.split('-')[1]
    if sub_dict.get(subs):
        if value>sub_dict.get(subs):
            sub_dict[subs] = value
    else:
        sub_dict[subs] = value



print(total_dict)
print(count_dict)
print(sub_dict)












