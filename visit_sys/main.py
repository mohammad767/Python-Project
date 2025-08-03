from fucs import *

if __name__ == "__main__" :
    ch = input("You are doctor or pation : ").lower()
    if ch == "pation":
        ch_2 = input("Do you have account (Y/N) : ").lower()
        if ch_2 == "n" :
            create_acc_p()
            login_p()
        elif ch_2 == "y" :
            login_p()
        else :
            print("Invalid input")
    elif ch == "doctor" :
        ch_2 = input("Do you have account (Y/N) : ").lower()
        if ch_2 == "n" :
            create_acc_d()
        elif ch_2 == "y" :
            login_d()
        else :
            print("Invalid input")
    else :
        print("Invalid input")