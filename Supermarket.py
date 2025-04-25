from flask import Flask, render_template, request, redirect
import os.path
from os import path

global whichfilename;
whichfilename = "LoginAdmin.doc";
userfile = "LoginUser.doc";

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("AdminUser.html")

@app.route("/select",methods=["POST"])
def WhichAccount():
    global account
    account = request.form.get("txtaccount")
    if(account == ""):
        return render_template("AdminUser.html");
    else:
        return render_template("ExtractInfo.html");

@app.route("/info",methods=["POST"])
def GetInfo():
    global username
    global userpasswd
    username = request.form.get("txtusername")
    userpasswd= request.form.get("txtpassword")
    if(username == "" or userpasswd == ""):
        return render_template("ExtractInfo.html");
    else:
        CreateCheckFile();
        GrabVal();

def GrabVal():
    Infofilename = open(whichfilename,"r");
    UserValue = Infofilename.read().split(",");
    Infofilename.close();
    username = UserValue[0].strip();
    userpasswd= UserValue[1].strip();

def CreateCheckFile():
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    print(Adaccount)
    if(Adaccount == 1):
        fileexist = bool(path.exists(whichfilename));
        if(fileexist == False):
            status = "new";
        else:
            status = "edit"
    else:
        fileexist = bool(path.exists(userfile));
        if(fileexist == False):
            status = "new";
        else:
            status = "edit"

    WriteToFile(status);


def WriteToFile(whichstatus):
    
     if(Adaccount == 1):
        if(whichstatus == "new"):
            logacctfile = open(whichfilename,"x")
            logacctfile.close();
            logacctfile = open(whichfilename,"w")
        else:
            logacctfile = open(whichfilename,"a")
     else:
        if(whichstatus == "new"):
            logacctfile = open(userfile,"x")
            logacctfile.close();
            logacctfile = open(userfile,"w")
        else:
            logacctfile = open(userfile,"a")

     logacctfile.write(str(username) + "," + str(userpasswd));
    

if __name__=="__main__":
    app.run();
