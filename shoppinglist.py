
import sqlite3

# Verbindung zu sqlite-DB (falls nicht vorhanden ist, dann wird Sie erstellt)
conn = sqlite3.connect("shoppinglist.py")

# Erstellung von Cursor um sql-Befehl durchzuführen.
cursor = conn.cursor()

# Erstellung von Tabellen in shoppinglist.db
cursor.execute('''
CREATE TABLE IF NOT EXISTS groceries (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VACHAR (32) NOT NULL,
amount INTEGER NOT NULL,
price FLOAT NOT NULL);
''')

#erste Funktion hinzufügen
def add_article ():
    name = input("Welchen Artikel Möchtest du hinzufügen")
    amount = input("Wieviele Artikel sollen hinzugefügt werden")
    price = input("Was soll der Artikel kosten")
    cursor.execute('''
INSERT INTO article (name, amount, price) VALUES (?,?,?)
''', (name, amount, price))
    conn.commit()
    print(f"{name} wurde hinzugefügt")

#Erstellung von READ Funktion
def show_groceries():
    cursor.execute('SELECT id, name FROM groceries')
    groceries = cursor.fetchall()
    for name in groceries:
        print(name)

        # Update Funktion
        def update_articles(id, name, amount, price):
         cursor.execute('''
        UPDATE groceries SET name = ?, amount = ?, price = ?
        WHERE id = ?
        ''',(name, amount, price, id))
        conn.commit()
        print(f"updatet articles with id {id}")

        # adding a delte function to delete an article
        def delete_article(id):
         cursor.execute('''
        DELETE FROM groceries WHERE id = ?
        ''',(id,))
        conn.commit()
        print(f"article has been deletet with id {id}")

    # define main function to get the user input
    # user can choose from create, read, update and delete function

    def main():
        while True:
            print("-------groceries-------")
            print("1. add first article")
            print("2. show groceries")
            print("3. refresh article")
            print("4. delete article")
            print("5. end programm")
            

            choice = input("Bitte wähle eine Option (1, 2, 3, 4, 5oder 6): ")

            if choice == "1":
                print("Bitte gib die Daten des neuen Artikels ein: ")
                name = input("name: ")
                amount = input("amount: ")
                price = input("price: ")
                add_article(name, amount, price)
            elif choice == "2":
                show_groceries()
            elif choice == "3":  
                print("Bitte gib die aktualierten Daten mit id ein: ")  
                id = input("id: ")
                name = input("name: ")
                amount = input("amount: ")
                price = input("price: ")
                update_articles(id, name ,amount, price)
            elif choice == "4":
                print("Bitte gib die ID des zu löschenden Artikels ein: ")
                id = input("id: ")
            elif choice == "6":
                add_article
            elif choice == "5":
                print("Programm wird beendet.Auf Wiedersehen!")
                break
            else:
                print("Ungültige Eingabe! Bitte wähle 1, 2, 3, 4 oder 5")

        if __name__ == "__main__":
            main()
               




