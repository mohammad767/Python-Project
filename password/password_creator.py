import string
import random

letters  = string.ascii_letters
nums = string.digits
sings = string.punctuation
stuffs = letters + nums + sings

def creat_p():
    while True:
        user = input("Do you want creat a password Y/N : ")
        if user.lower() == "y":
            length = int(input("Enter the length of your password : "))
            password = "".join(random.sample(stuffs,length))
            print(password)
        elif user.lower() == "n":
            break
        
creat_p()
    