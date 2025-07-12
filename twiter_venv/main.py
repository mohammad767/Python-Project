import funcs
from colorama import init, Fore, Style
init(autoreset=True)

if __name__ == "__main__" :
    ch = input(Fore.YELLOW+"Do you have an account(Y/N) : ").lower()
    if ch == "n" :
        funcs.create_acc()
        ch_2 = input(Fore.YELLOW+"Do you want login into your account(Y/N) : ").lower()
        if ch_2 == "n" :
            print(Fore.YELLOW+"Thanks")
        if ch_2 == "y" :
            funcs.login()
    if ch == "y" : 
        funcs.login()
    
