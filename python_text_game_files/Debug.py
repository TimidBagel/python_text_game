import os
from os.path import exists
class Console:
    def ConsoleRun():
        inp = input()
        inp = inp.upper()
        match inp:
            case "GETFILES":
                curDirPath = os.getcwd()
                listONames = os.listdir(curDirPath)
                inp = input("List name or extension to find(Case Sensitive)\n")
                for i in listONames:
                    if inp in i:
                        print(i)
            case "VIEW":
                inp = input("Please type the script to see(Case Sensitive, you do not need to include \'.py\' for a python file, but you can): ")
                if exists(inp) or exists(inp+".py"):
                    if not "." in inp:
                        view = open(inp + ".py", 'r')
                    else:
                        view = open(inp, 'r')
                    print(view.read())
                else:
                    print("No file with that name found!")
            case "HELP":
                print("GetFiles: See files that contain a string in their name\nView: See the contents of files")
                
        if inp != "RESUME":
            Console.ConsoleRun()