import os.path
from os import path

def menu():
    print("\n_______________________\nWelcome to the store! \n")
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    print(" DEPARTMENTS: \n 1) Fruit \n 2) Poultry \n 3) Meat \n 4) Beverage \n 5) Frozen Foods \n 6) Dietary Foods \n 7) Kosher \n 8) Halal");
    whichscreen = str(input("What department do you want to enter? Type a number from 1-8: "));
    match(whichscreen):
        case "1":
            filepath = fileDir + "\\Project-Supermarket-Fruit.py";

        case "2":
            filepath = fileDir + "\\Screen2.py";

        case default:
            print("Please enter a number form 1-8");
            menu()

    filenamepath = {
        "__file__":filepath,
        "__name__":"__main__",
        };
    with open(filepath,"rb") as file:
        exec(compile(file.read(), filepath, "exec"),filenamepath);
      
def main():
    menu();
  
if __name__=="__main__":
    main();
