text = "assalomu alaykum"
def count_letters(text):
    result = {}

    for char in text:
        if char != " ":         
            
            if char in result:
                result[char] += 1
            else:
                result[char] = 1

    return result

print(count_letters(text))
