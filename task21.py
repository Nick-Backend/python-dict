names = ["ozod", "ali", "sardor", "husan", "kamron", "ozod", "ali", "ozod", "ali",]
def count_names(names: list[str]) -> dict[str, int]:

    result = {}
    for name in names:
        if name not in result:
            result[name] = 1

        else:
            result[name] += 1

    return result            
     
print(count_names(names))        


