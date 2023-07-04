import database

# print the results from an given list
def printResult(result):
    print("The following devices have been found that match best your requirements:")
    for field in result:
        print(field)
            

# get user input to get the best matching laptop
def evalLaptop():
    print("What is important about the Laptop?")
    print("Display, RAM, Storage or Batteryhours?")
    print("Selection:", end=" ")
    selection = input()
    
    db = database.Database()
    db.getLaptopHighScore("display")
    
    if selection.lower() == "display":
        printResult(db.getLaptopHighScore("display"))
        return
    elif selection.lower() == "ram":
        printResult(db.getLaptopHighScore("ram"))
        return
    elif selection.lower() == "storage":
        printResult(db.getLaptopHighScore("storage"))
        return
    elif selection.lower() == "batterhours":
        printResult(db.getLaptopHighScore("batteryhours"))
        return
    else:
        print("Invalid Selection")
    

# get user input to get the best matching computer
def evalComputer():
    print("What is important about the Computer?")
    print("CPU, GPU, RAM or Storage?")
    print("Selection:", end=" ")
    selection = input()
    
    db = database.Database()
    
    if selection.lower() == "cpu":
        printResult(db.getComputerHighScore("cpu"))
        return
    elif selection.lower() == "gpu":
        printResult(db.getComputerHighScore("gpu"))
        return
    elif selection.lower() == "ram":
        printResult(db.getComputerHighScore("ram"))
        return
    elif selection.lower() == "storage":
        printResult(db.getComputerHighScore("storage"))
        return
    else:
        printResult("Invalid Selection")
    

            
def main():
    print("What kind of hardware do you need?")
    print("Possible Selections: laptop computer")

    print("Selection:", end=" ")
    selection = input()

    # The input has to be a string
    if(isinstance(selection, str)):
        if(selection.lower() == "laptop"):
            evalLaptop()
        elif(selection.lower() == "computer"):
            evalComputer()
        else:
            print("Invalid Selection")
    else:
        print("Invalid Selection")

if __name__ == "__main__":
    main()