D1 = {
    'list1': [4, 7, 10, 20],
    'list2': [7, 16, 9, 10],
    'list3': [13, 10, 4, 8],
    'list4': [7, 20, 6, 11]
}

unique_values = set()
for key in D1:
    unique_values.update(set(D1[key]))

print(unique_values)

