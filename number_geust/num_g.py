import random

def CG_num(num) :
    """ This function can guest the number that you Enter """
    while True :
        if num < 0 or num > 100 :
            print("Try again")
            CG_num(int(input("Enter a number betwean 0 to 100 : ")))
        
        else:
            if num > 75:
                c_num = random.randint(76, 100)
                if num == c_num :
                        print(f"Your number is {c_num}")
                        break
            elif num >= 50:
                c_num = random.randint(50, 75)
                if num == c_num :
                        print(f"Your number is {c_num}")
                        break
            elif num >= 25:
                c_num = random.randint(25, 49)
                if num == c_num :
                        print(f"Your number is {c_num}")
                        break
            else:
                c_num = random.randint(0, 24)
                if num == c_num :
                        print(f"Your number is {c_num}")
                        break

# CG_num(int(input("Enter your number : ")))


def PG_num(num) :
    """With this function you can geust what number that cpu creat"""
    if num < 0 or num > 100 :
            print("Try again")
            CG_num(int(input("Enter a number betwean 0 to 100 : ")))
    if num > 75:
        c_num = random.randint(76, 100)
    elif num >= 50:
        c_num = random.randint(50, 75)
    elif num >= 25:
        c_num = random.randint(25, 49)
    else:
        c_num = random.randint(0, 24)
        
    if num == c_num :
          print(f"Congratulations! Your number is {c_num}.")
    else:
        print(f"Sorry, the random number was {c_num}. Try again.")
        PG_num(int(input("Enter a number between 0 to 100: ")))
        
# PG_num(int(input("Enter your geust number from 0 to 100 : ")))


        
    