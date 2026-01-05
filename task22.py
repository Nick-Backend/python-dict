students = [
    {"name": "Ali", "group": "A"},
    {"name": "Soli", "group": "A"},
    {"name": "Vali", "group": "B"},
    {"name": "Karim", "group": "B"}
]

def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
   
   
    result = {}
  
    for student in students:
          group = student["group"]
          name = student["name"]
  
          if group in result:
              result[group].append(name)
          else:
              result[group] = [name]
  
    return result
print(group_students(students))