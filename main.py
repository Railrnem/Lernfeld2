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
    print("Selection:", end=" ")
    selection = input()
    print()
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
    print("What kind of hardware do you need?")
    print("Possible Selections: laptop new")

    print("Selection:", end=" ")
    selection = input()
    print()

    if(isinstance(selection, str)):
        if(selection.lower() == "laptop"):
            evalLaptop()
        if(selection.lower() == "new"):
            addHardware()
    else:
        print("Invalid Selection")

if __name__ == "__main__":
    main()