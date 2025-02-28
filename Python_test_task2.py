'''Find and Count Duplicates in a List and print it on screen.'''

numbers = [4, 5, 6, 4, 7, 8, 5, 9, 4, 7, 6, 10]

counts = {}
for i in numbers:
  counts[i] = counts.get(i, 0) + 1

print("Duplicate numbers and their counts : \n")
for key, value in counts.items():
  print(f"{key} appears {value} times.\n")