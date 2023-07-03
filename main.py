import database

def printResult(result):
    print("The following devices have been found that match best your requirements:")
    for field in result:
        print(field)
            
def evalLaptop():
    print("What is important about the Laptop?")
    print("Display, RAM, Storage or Batteryhours?")
    print("Selection:", end=" ")
    selection = input()
    
    if selection.lower() == "display":
        printResult(database.getLaptopHighScore("display"))
        return
    elif selection.lower() == "ram":
        printResult(database.getLaptopHighScore("ram"))
        return
    elif selection.lower() == "storage":
        printResult(database.getLaptopHighScore("storage"))
        return
    elif selection.lower() == "batterhours":
        printResult(database.getLaptopHighScore("batteryhours"))
        return
    else:
        print("Invalid Selection")
    
def evalComputer():
    print("What is important about the Computer?")
    print("CPU, GPU, RAM or Storage?")
    print("Selection:", end=" ")
    selection = input()
    
    if selection.lower() == "cpu":
        printResult(database.getComputerHighScore("cpu"))
        return
    elif selection.lower() == "gpu":
        printResult(database.getComputerHighScore("gpu"))
        return
    elif selection.lower() == "ram":
        printResult(database.getComputerHighScore("ram"))
        return
    elif selection.lower() == "storage":
        printResult(database.getComputerHighScore("storage"))
        return
    else:
        printResult("Invalid Selection")
    

            
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