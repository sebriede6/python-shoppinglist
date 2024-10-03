# erstellt eine leere Liste
shoppinglist=[]
print("Ihre Einkaufsliste ist leer.")
# nimmt den input des Benutzers und speichert es in der Variable Item
def add_item():
    item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: ")

    if len(item) == 0:
        print("Ihre Einkaufsliste ist leer, bitte geben Sie einen Artikel ein!")
    else:
        
    
    # druckt den eingegebenen Artikel auf dem Bildschirm aus
     
        print ("Ihre Artikel :", item)

    #fügt den eingegeben Artikel zur Einkaufliste hinzu

    shoppinglist.append(item)
    print("der Artikel wurde der Liste hinzugefügt")

    # druckt die Einkaufliste mit den eingefügten Artikeln auf diBildschirm
    print(shoppinglist)
    
add_item() 


def show_shoppinglist():
   
   if len(shoppinglist) == 0:
        print ("Deine Einkaufliste ist leer")

   else:
       
        print(shoppinglist)


# überprüft den Input des Benutzers und reagiert je nach Eingabe der Zahlen was als nächstes gemacht werden soll

while True:
    print("------------------------ Einkaufsliste -----------------------------")
    print("Hier ist deine Einkaufsliste")
    print(shoppinglist)
    print("Bitte wähle Sie aus, was Sie als nächstes machen möchten: ")
    print("1. Artikel zur Einkaufsliste hinzufügen")
    print("2. Einkaufsliste anzeigen")
    print("3. Programm beenden")
    choice = int(input("Bitte wählen Sie aus: ")) 
    print("ihre Auswahl: ", choice)
    if choice == 1:
        add_item()
    elif choice == 2:
          print("schauen Sie mal nach unten...")
    elif choice == 3:
        print("Programm wird beendet! Auf Wiedersehen") 

        # break beendet die Schleife 
        break
    else:
        print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3")   

