from tkinter import * 

import random
import string
import os
import json
import datetime


letters = string.ascii_letters
nums = string.digits
id_stuff = nums + string.ascii_lowercase
sings = string.punctuation
stuffs = letters + nums + sings

    
def user_m() :
    while True:
        print("a --> add activity")
        print("s --> see the list")
        print("x --> exit")
        ch = input("Enter what you want to do : ")
        if ch.lower() == "a" :
            add_do()
        if ch.lower() == "s" :
            see_lst()
        if ch.lower() == "x" :
            print("Goodbye")
            break
    
def add_do() :
    filename = input("Enter the name of the file you want add your activity : ") + ".json"
    while True :
        ch = input("Do you want add activity(Y/N) : ")
        if ch.lower() == "n" :
            print("Goodbye")
            break
        if ch.lower() == "y" :
            do = input("Enter the activity in a short sentens : ")
            if len(do) < 50 :
                do_lst = [do]
                if os.path.exists(filename):
                    with open(filename, "r") as file:
                        try:
                            existing_data = json.load(file)
                        except json.JSONDecodeError:
                            existing_data = []
                else:
                    existing_data = []

                existing_data.extend(do_lst)
                with open(filename, "w",encoding="utf-8") as file:
                    json.dump(existing_data, file, indent=4)
                print(f"Data written to {filename} successfully!")
                
            if len(do) > 50 :
                print("Pleas write less")
                add_do()
                
def see_lst() :
    filename = input("Enter the name of the file : ") + ".json"
    with open(filename,"r") as file :
        data = json.load(file)
    win = Tk()
    win.title("To DO List")
    
    man_vars=  []
        
    def done() :
        nonlocal data
        selected_indices = [index for index, var in enumerate(man_vars) if var.get() == 1]
        for index in sorted(selected_indices, reverse=True):
            del data[index] 
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        win.destroy()
        
    
    
    for act in data :     
        var = IntVar()
        man_vars.append(var)
        chbt =  Checkbutton(win,text=act,variable=var)
        chbt.pack()
            
            
    Button(win,text="Finshe",command=done).pack()
    win.geometry("800x800")
    win.mainloop()
        

           
if __name__ == '__main__' :
        user_m()
             

                

    
    
    



