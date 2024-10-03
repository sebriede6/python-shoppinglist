#python-shoppinglist
shoppinglist = []
print(shoppinglist)
print("Deine Einkaufsliste")

item = input("Bitte gib den Artikel ein, der zur Liste hinzugefügt werden soll!: ")
shoppinglist.append(item)
print(f"{shoppinglist} Der Artikel wurde hinzugefügt")

if len(shoppinglist) == 0:
 print("Deine Einkaufsliste") 
else:
 print("Deine Einkaufsliste ist voll")

for words in shoppinglist:
 print(words)
             