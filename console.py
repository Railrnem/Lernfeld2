import database

class HardwareEvaluator:
    # Initialize neccessary Database Objects
    def __init__(self):
        self.db = database.Database()

    # Print Results
    def printResult(self, result):
        print("The following devices have been found that match best your requirements:")
        for field in result:
            print(field)

    # Find the best laptop for the user
    def evalLaptop(self):
        print("What is important about the Laptop?")
        print("Display, RAM, Storage or Batteryhours?")
        print("Selection:", end=" ")
        selection = input()

        if selection.lower() == "display":
            self.printResult(self.db.getLaptopHighScore("display"))
        elif selection.lower() == "ram":
            self.printResult(self.db.getLaptopHighScore("ram"))
        elif selection.lower() == "storage":
            self.printResult(self.db.getLaptopHighScore("storage"))
        elif selection.lower() == "batteryhours":
            self.printResult(self.db.getLaptopHighScore("batteryhours"))
        else:
            print("Invalid Selection")

    # Find the best computer for the user
    def evalComputer(self):
        print("What is important about the Computer?")
        print("CPU, GPU, RAM or Storage?")
        print("Selection:", end=" ")
        selection = input()

        if selection.lower() == "cpu":
            self.printResult(self.db.getComputerHighScore("cpu"))
        elif selection.lower() == "gpu":
            self.printResult(self.db.getComputerHighScore("gpu"))
        elif selection.lower() == "ram":
            self.printResult(self.db.getComputerHighScore("ram"))
        elif selection.lower() == "storage":
            self.printResult(self.db.getComputerHighScore("storage"))
        else:
            self.printResult("Invalid Selection")

    # Main function of the HardwareEvaluator
    def main(self):
        print("What kind of hardware do you need?")
        print("Possible Selections: laptop computer")

        print("Selection:", end=" ")
        selection = input()

        if isinstance(selection, str):
            if selection.lower() == "laptop":
                self.evalLaptop()
            elif selection.lower() == "computer":
                self.evalComputer()
            else:
                print("Invalid Selection")
        else:
            print("Invalid Selection")

if __name__ == "__main__":
    evaluator = HardwareEvaluator()
    evaluator.main()