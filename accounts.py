import os.path
from os import path

def account():
    global filename, username, password
    print("Enter Username and Password.\n");
    username = str(input("Username: "));
    password = str(input("Password: "));
    filename = username + ".doc"
    UserCheck()
    
def UserCheck():
    if(username == "" or password == ""):
        print("missing username or password");
        account();
    else:
        FileCheck();

def FileCheck():
    global adminfile, fileDir;
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    fileexist = bool(path.exists(filename));

    if(fileexist == False):
        accountinfo = str(input("Account does not exists. Do you want to create this account? (1 for yes, 2 for no)"))
        match(accountinfo):
            case "1":
                adminfile = open(filename,"x");
                adminfile.close();
                WriteToFile(username,password,filename);
                filepath = fileDir + "\\Project-Supermarket-Menu.py";
                filenamepath = {
                    "__file__":filepath,
                    "__name__":"__main__",
                    };
            case "2":
                account();
            case default:
                FileCheck()

        with open(filepath,"rb") as file:
            exec(compile(file.read(), filepath, "exec"),filenamepath);
    else:
        adminfile = open(filename,"r");
        checkpass(); 

def checkpass():
    adminvalue = adminfile.read().split(",")
    adminfile.close();
    userpwd = adminvalue[1].strip();
    if(password != userpwd):
        print("Wrong password. Try again");
        account();
    else:
        filepath = fileDir + "\\Project-Supermarket-Menu.py";
        filenamepath = {
            "__file__":filepath,
            "__name__":"__main__",
            };
    
    with open(filepath,"rb") as file:
        exec(compile(file.read(), filepath, "exec"),filenamepath);

def WriteToFile(name,passwd,thefile):
    adminfile = open(thefile,"w");
    adminfile.write(name + "," + passwd);
    adminfile.close();

def main():
    account();
  
if __name__=="__main__":
    main();
      
