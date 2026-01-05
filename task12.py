inventory = {"olma": 5,
             "behi": 4,
             "uzum": 9
            }

product = input("Mahsulotni kiriting: ")

inventory.setdefault(product, 0)

print(inventory)

