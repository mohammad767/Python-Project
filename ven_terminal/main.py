import terminal
import getinput
import os
import time

if  __name__ == '__main__':
    start = terminal.terminal()
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
        choice = text.strinput("Enter the number : ")
        if choice == "1" :
            start.cdir()
        elif choice == "2" :
            start.mkdir()
        elif choice == "3" :
            start.rmdir()
        elif choice == "4" :
            start.showItem()
        elif choice == "5" :
            start.mkfile()    
        elif choice == "6" :
            start.rmfile()    
        elif choice == "7" :
            start.renamefolder()  
        elif choice == "8" :
            start.renamefile
        elif choice == "9" :
            print("Goodbye")
            break
        else :
            print("Invalid input !!")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
