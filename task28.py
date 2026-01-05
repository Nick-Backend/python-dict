words = ["olma", "anor", "banan", "nok", "shaftoli"]

def group_by_length(words):
    result = {}

    for word in words:
        length = len(word)

        if length in result:
            result[length].append(word)
        else:
            result[length] = [word]

    return result

print(group_by_length(words))