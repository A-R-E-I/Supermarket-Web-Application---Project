from flask import Flask, render_template, request, redirect
import os.path
from os import path

global whichfilename;
whichfilename = "LoginAccounts.doc";

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("ExtractInfo.html")

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
        Infofilename = open(whichfilename,"r");
        UserValue = Infofilename.read().split(",");
        Infofilename.close();
        username = UserValue[0].strip();
        userpasswd= UserValue[1].strip();
        return render_template("output3.html",username=username,password=userpasswd);

def CreateCheckFile():
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    fileexist = bool(path.exists(whichfilename));
    if(fileexist == False):
        status = "new";
    else:
        status = "edit"

    WriteToFile(status);

def WriteToFile(whichstatus):
    if(whichstatus == "new"):
        logacctfile = open(whichfilename,"x")
        logacctfile.close();
        logacctfile = open(whichfilename,"w")
    else:
        logacctfile = open(whichfilename,"a")

    logacctfile.write(str(username) + "," + str(userpasswd));

if __name__=="__main__":
    app.run();
