def merge_and_sum(dict1, dict2):
    merged_dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value

    return merged_dict


dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 40}

result = merge_and_sum(dict1, dict2)
print(result)