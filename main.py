import database

print("Was für eine Hardware brauchst du?")
print("Mögliche Eingaben: Laptop")

selection = input()

if(isinstance(selection, str)):
    if(selection == "Laptop"):
        print(database.printLaptop())
else:
    print("Ungültige Eingabe")
