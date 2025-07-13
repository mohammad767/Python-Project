import getinput
import os
import time

class terminal():
    def __init__(self):
        self.text = getinput.Getinput()
    
   
    def __clear(self) :
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def __cdir(self):
        self.__clear()
        newdir = self.text.strinput("Enter the new directory : ")
        try : 
            os.chdir(newdir)
            return(newdir)
        except Exception :
                #print(newdir)
                print("Wrong directory!!")
                self.__cdir()   
    
    def __mkdir(self):
        self.__clear()
        name = self.text.strinput("Enter the name of folder : ")
        if os.path.exists(name) :
                print("This folder is exists")
                return
        os.mkdir(name)
        print(f"{name} folder created in {os.getcwd()}")
    
    def __rmdir(self):
        self.__clear()
        name = self.text.strinput("Enter the name of folder : ")
        if os.path.exists(name) :
            os.rmdir(name)
            print(f"{name} folder removed from {os.getcwd()}") 
            return  
        print("This folder is not exists")
        return
    
    def __showItem(self):
        self.__clear()
        items = os.listdir()
        print(os.getcwd())
        for idx, name in enumerate(items, start=1):
            print(f"{idx} {name}")
    
    def __mkfile(self):
        self.__clear()
        file = self.text.strinput("Enter the file name with format(filename.format) : ")
        if os.path.exists(file) :
            print("This file is already exists")
            return
        try : 
            with open(file,"w") as f :
                f.write("")
            print(f"File created")
            
        except Exception as e :
            print(e)
    
    def __rmfile(self) :
        self.__clear()
        file = self.text.strinput("Enter the file name with format(filename.format) : ")
        if os.path.exists(file) :
            try:
                os.remove(file)
                print("File removed")
            except Exception as e :
                print(e)
            return
        print("This file is not exists")
    
    def __renamefolder(self):
        self.__clear()
        dirname = self.text.strinput("Enter the folder name : ")
        if os.path.exists(dirname) :
            newname = self.text.strinput("Enter the new name : ")
            try :
                os.rename(dirname,newname)
                print(f"{dirname} changed to {newname}")
            except Exception as e :
                print(e)
        else :
            print("Folder is not exists")
    
    def __renamefile(self) :
        self.__clear()
        dirname = self.text.strinput("Enter the file name : ")
        if os.path.exists(dirname) :
            newname = self.text.strinput("Enter the new name : ")
            try :
                os.rename(dirname,newname)
                print(f"{dirname} changed to {newname}")
            except Exception as e :
                print(e)
        else :
            print("file is not exists")
    def run(self) :
        text = getinput.Getinput()
        while True :
            print("1 --> Change Directory")
            print("2 --> Create Folder")
            print("3 --> Remove Folder")
            print("4 --> Show Folder Item")
            print("5 --> Create File")
            print("6 --> Remove File")
            print("7 --> Rename Folder")
            print("8 --> Rename File")
            print("9 --> Exit")
            print("\n")
            print(f"Cruten directory : {os.getcwd()}")
            print("\n")
            choice = text.strinput("Enter the number : ")
            if choice == "1" :
                self.__cdir()
            elif choice == "2" :
                self.__mkdir()
            elif choice == "3" :
                self.__rmdir()
            elif choice == "4" :
                self.__showItem()
            elif choice == "5" :
                self.__mkfile()    
            elif choice == "6" :
                self.__rmfile()    
            elif choice == "7" :
                self.__renamefolder()  
            elif choice == "8" :
                self.__renamefile()
            elif choice == "9" :
                print("Goodbye")
                break
            else :
                print("Invalid input !!")
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')