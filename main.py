import database

def addLaptop():
    print("Enter a name for the laptop:", end=" ")
    name = input()
    print()
    print("Enter the display resolution: ", end=" ")
    display = input()
    print()
    print("Enter how much RAM the Laptop has: ", end=" ")
    ram = input()
    print()
    print("Enter how much storage the Laptop has: ", end=" ")
    storage = input()
    print()
    print("Enter how many hours the battery lasts: ", end=" ")
    battery = input()
    print()
    database.addLaptop(name, display, ram, storage, battery)


def addHardware():
    print("Please enter what kind of Hardware you want to add.")
    print("Possible Entrys: Laptop")
    selection = input()
    if(isinstance(selection, str)):
        if selection == "Laptop":
            addLaptop()
            
def evalLaptop():
    print("What is important about the Laptop?")
    print("Display, RAM, Storage or Batteryhours?")
    selection = input()
    
    if selection.lower == "display":
        pass
    elif selection.lower() == "ram":
        pass
    elif selection.lower() == "storage":
        pass
    elif selection.lower() == "batterhours":
        pass
    
    #print(database.printLaptop())
    

            
def main():
    print("Was für eine Hardware brauchst du?")
    print("Mögliche Eingaben: Laptop Neu")

    selection = input()

    if(isinstance(selection, str)):
        if(selection == "Laptop"):
            evalLaptop()
        if(selection == "Neu"):
            addHardware()
    else:
        print("Ungültige Eingabe")

if __name__ == "__main__":
    main()