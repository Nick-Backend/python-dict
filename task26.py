def merge_dicts(a, b):
    result = a.copy()

    for key, value in b.items():
        result[key] = value

    return result
print(merge_dicts({"a": "a"}, {"b": "b"}))