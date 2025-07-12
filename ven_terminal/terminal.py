import getinput
import os


class terminal():
    def __init__(self):
        self.text = getinput.Getinput()
    
   
    def cdir(self):
        newdir = self.text.strinput("Enter the new directory : ")
        try : 
            os.chdir(newdir)
            return(newdir)
        except Exception :
                #print(newdir)
                print("Wrong directory!!")
                self.cdir()   
    
    def mkdir(self):
        name = self.text.strinput("Enter the name of folder : ")
        if os.path.exists(name) :
                print("This folder is exists")
                return
        os.mkdir(name)
        print(f"{name} folder created in {os.getcwd()}")
    
    def rmdir(self):
        name = self.text.strinput("Enter the name of folder : ")
        if os.path.exists(name) :
            os.rmdir(name)
            print(f"{name} folder removed from {os.getcwd()}") 
            return  
        print("This folder is not exists")
        return
    
    def showItem(self):
        items = os.listdir()
        print(os.getcwd())
        for idx, name in enumerate(items, start=1):
            print(f"{idx} {name}")
    
    def mkfile(self):
        file = self.text.strinput("Enter the file name with format(filename.format) : ")
        if os.path.exists(file) :
            print("This file is already exists")
            return
        try : 
            with open(file,"w") as f :
                f.write("")
            print(f"File created")
            os.close()
        except Exception as e :
            print(e)
    
    def rmfile(self) :
        file = self.text.strinput("Enter the file name with format(filename.format) : ")
        if os.path.exists(file) :
            try:
                os.remove(file)
                print("File removed")
            except Exception as e :
                print(e)
            return
        print("This file is not exists")
    
    def renamefolder(self):
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
    
    def renamefile(self) :
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
         
        
                    
                
            
                    
    
