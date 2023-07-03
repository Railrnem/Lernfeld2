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
    
    if selection.lower() == "display":
        print(database.getLaptopHighScore("display"))
        return
    elif selection.lower() == "ram":
        print(database.getLaptopHighScore("ram"))
        return
    elif selection.lower() == "storage":
        print(database.getLaptopHighScore("storage"))
        return
    elif selection.lower() == "batterhours":
        print(database.getLaptopHighScore("batteryhours"))
        return
    else:
        print("Invalid Selection")
    
def evalComputer():
    print("What is important about the Computer?")
    print("CPU, GPU, RAM or Storage?")
    selection = input()
    
    if selection.lower() == "cpu":
        print(database.getComputerHighScore("cpu"))
        return
    elif selection.lower() == "gpu":
        print(database.getComputerHighScore("gpu"))
        return
    elif selection.lower() == "ram":
        print(database.getComputerHighScore("ram"))
        return
    elif selection.lower() == "storage":
        print(database.getComputerHighScore("storage"))
        return
    else:
        print("Invalid Selection")
    

            
def main():
    print("What kind of hardware do you need?")
    print("Possible Selections: laptop computer")

    print("Selection:", end=" ")
    selection = input()

    if(isinstance(selection, str)):
        if(selection.lower() == "laptop"):
            evalLaptop()
        elif(selection.lower() == "computer"):
            evalComputer()
        else:
            print("Invalid Selection")
        #if(selection.lower() == "new"):
        #    addHardware()
    else:
        print("Invalid Selection")

if __name__ == "__main__":
    main()