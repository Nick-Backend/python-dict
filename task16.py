book = {
    "titl": "Python Basics",
    "author": "Diyorbek Jumanov",
    "pages": 250
    }
key_name = input("Key nomini kiriting: ")

if key_name in book:
    book.pop(key_name) 
    print("Kalit o'chirildi ")

else:
    print("Bunday kalit yo'q ")

print(book)      