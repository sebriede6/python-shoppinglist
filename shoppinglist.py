
import sqlite3      # import sqlite3 to be able to connect

# connect to sqlite database (if not exist, create)
conn = sqlite3.connect('shoppinglist.db')

# create cursor object to run sql commands
cursor = conn.cursor()

# create table to groceries.db
cursor.execute('''
CREATE TABLE IF NOT EXISTS shoppinglist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    amount INTEGER NOT NULL,
    price FLOAT);
''')
# create first function to add input (CREATE)
def add_groceries(name, amount, price):
    cursor.execute('''
INSERT INTO shoppinglist (name, amount, price) VALUES (?, ?, ?)
''', (name, amount, price))
    conn.commit()
    print(f"{name} was added.")

# create read function
def show_shoppinglist():
    cursor.execute('SELECT * FROM shoppinglist')
    shoppinglist = cursor.fetchall()
    for groceries in shoppinglist:
        print(groceries) 

# create update function
def update_groceries(id, name, amount, price):
    cursor.execute('''
UPDATE shoppinglist SET name = ?, amount = ?, price = ?
WHERE id = ?
''', (name, amount, price, id))
    conn.commit()
    print(f"update groceries with id {id}")  

# create search function
def search_groceries(name):
    cursor.execute('''
SELECT * FROM shoppinglist WHERE name = ?
''', (name,))
    shoppinglist = cursor.fetchall()
    print(f"Looking for groceries {name}: ")
    for groceries in shoppinglist:
        print(groceries)

# create delete function
def delete_groceries(id):
    cursor.execute('''
DELETE FROM shoppinglist WHERE id = ?
''',(id,))
    conn.commit()
    print(f"Groceries with id {id} has been deleted.")


# While-Loop to keep the programm running 
def main():
    while True:
        print("-----Shoppinglist-----")
        print("1. Add groceries to your shoppinglist")
        print("2. Show shoppinglist")
        print("3. Update groceries")
        print("4. Search for groceries")
        print("5. Delete groceries")
        print("6. End the programm")

        choice = int(input("Please choose 1, 2, 3, 4, 5 or 6: "))

        if choice == 1:
            print("Please enter groceries you want to add to your shoppinglist: ")
            name = input("name: ")
            amount = input("amount: ")
            price = input("price: ")
            add_groceries(name, amount, price)
        elif choice == 2:
            show_shoppinglist()
        elif choice == 3:
            print("Please update the data with id: ")
            id = input("id: ")
            name = input("name: ")
            amount = input("amount: ")
            price = input("price: ")
            update_groceries(id, name, amount, price)
        elif choice == 4:
            print("Please enter the name of the groceries you are looking for: ")
            name = input("name: ")
            search_groceries(name)
        elif choice == 5:
            print("Please enter the id of the groceries you want to delete: ")
            id = input("id: ")
            delete_groceries(id)
        elif choice == 6:
            print("Program is ended! Goodbye, see you soon.")
            break                                                           # breaks the loop
        else:
            print("Invalid input. Please choose 1, 2, 3, 4, 5 or 6.")   
if __name__ == "__main__":
    main()




