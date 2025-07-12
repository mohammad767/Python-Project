import random
import string

letters = string.ascii_letters
nums = string.digits
sings = string.punctuation
stuffs = letters + nums + sings

def pass_gesut(my_pass):
    

    while True:
        l = len(my_pass)
        # passw = "".join(random.sample(stuffs, l))
        if my_pass.isdigit():
            print("first")
            passw = "".join(random.sample(nums, l))
            if my_pass == passw:
                print("OK")
                print(f"Your password is {passw}")
                print("Password is Correct")
                break
            else:
                print("No")
                print(passw)
                print(my_pass)
        if my_pass.isalpha():
            print("second")
            if my_pass.islower():
                print("lower")
                passw = "".join(random.sample(string.ascii_lowercase, l))
                if my_pass == passw:
                    print("OK")
                    print(f"Your password is {passw}")
                    print("Password is Correct")
                    break
                else:
                    print("No")
                    print(passw)
                    print(my_pass)
            if my_pass.isupper():
                print("upper")
                passw = "".join(random.sample(string.ascii_uppercase, l))
                if my_pass == passw:
                    print("OK")
                    print(f"Your password is {passw}")
                    print("Password is Correct")
                    break
                else:
                    print("No")
                    print(passw)
                    print(my_pass)
            else:
                print("both")
                passw = "".join(random.sample(letters, l))
                if my_pass == passw:
                    print("OK")
                    print(f"Your password is {passw}")
                    print("Password is Correct")
                    break
                else:
                    print("No")
                    print(passw)
                    print(my_pass)
        for i in string.punctuation : 
            if i in my_pass : 
                print("Last one")
                passw = "".join(random.sample(stuffs, l))
                if my_pass == passw:
                    print("OK")
                    print(f"Your password is {passw}")
                    print("Password is Correct")
                    break
                else:
                    print("No")
                    print(passw)
                    print(my_pass)
pass_gesut(input("Enter the password : "))