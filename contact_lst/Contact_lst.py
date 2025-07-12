import csv
import os
from tkinter import *
import datetime



def add_c() :
    data = [["name","family","phone number"]]
    while True:
        ch = input("Do you want add contact(Y/N) : ")
        if ch.lower() == "n" :
            print("goodbye")
            break
        if ch.lower() == "y" :
            per = []
            name = input("Enter the name of the person : ")
            family = input("Enter the family of the person(you can press enter to skip it) : ")
            if not family :
                family = "/////"
            while True :
                phone = input("Enter the phone number : ")
                if len(phone) == 11 and  (phone.startswith("09") or phone.startswith("+98")) :
                    break
                else :
                    print("Try again")
            per.extend([name, family, phone])
            data.append(per)
            filename = "Contact.csv"
            mode = "a" if os.path.exists(filename) else "w"
            if mode == "a" :
                data = data[1:]
            with open(filename,mode,newline="",encoding="utf-8") as file :
                writer = csv.writer(file)
                writer.writerows(data)
            print("Contact added successfully!")

def see_c() :
    with open("Contact.csv") as file :
        data = csv.reader(file)   
        con = []
        for i in data:
            con.append(i)
            
        con = con[1:]
        win = Tk()
        win.title("Contact list")
        for i in con :
            lbl = Label(win,text=f"Name = {i[0]}")
            lbl.pack(anchor='w', pady=2)
            if i[1] != "/////" :
                lbl_2 = Label(win,text=f"family = {i[1]}")
                lbl_2.pack(anchor='w', pady=2)
            lbl_3 = Label(win,text=f"phone number = {i[2]}")
            lbl_3.pack(anchor='w', pady=2)
            sep =Label(win, text="-" * 40)
            sep.pack(anchor='w', pady=2)
        win.geometry("800x800")
        win.mainloop()
        
def dele_c():
    with open("Contact.csv","r") as file :
        data = csv.reader(file)
        name = input("Enter your name : ")
        
        data = [row for row in data if row and row[0] != name]
                
        with open("Contact.csv","w",newline="") as file : 
            writer = csv.writer(file)
            writer.writerows(data)

if __name__ == "__main__" :
    while True:
        print("a --> Add Contact")
        print("s --> See Contact")
        print("d --> Delete Contact")
        print("x --> exit")
        ch = input("Enter what you want to do : ")
        if ch.lower() == "a" :
            add_c()
        if ch.lower() == "s" :
            see_c()
        if ch.lower() == "d" :
            dele_c()
        if ch.lower() == "x":
            print("Goodbye")
            break
        
        