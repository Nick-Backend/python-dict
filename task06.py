dicts = {   
     "group_a": "Ali",
     "group_b": "Vali",
     "group_d": "G'ani",
     "group_c": "Ali"
         }

enter_name = input("Key nomini kiriting: ")
result = dicts.get(enter_name)

if result is None:
    print("Topilmadi")

else:
    print(result)    
