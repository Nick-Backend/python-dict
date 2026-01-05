data = {
    "a": 0,
    "b": 5,
    "c": 0,
    "d": 3
}


def filter_non_zero(d):
    result = {}

    for key, value in d.items():
        if value != 0:
            result[key] = value

    return result
print(filter_non_zero(data))