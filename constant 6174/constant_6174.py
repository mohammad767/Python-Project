import random

def check_number(num):
    num = str(num)
    print(f"main number : {num}")
    
    
    if len(set(num)) == 1:  
        print("Invalid value: All digits are the same!")
        return
    
    steps = 0  
    while num != "6174":
        num_lst = sorted(num)         
        rev_lst = sorted(num, reverse=True)  
        
        small_num = int("".join(num_lst))  
        large_num = int("".join(rev_lst))  
        
        num = str(large_num - small_num)  
    
        num = num.zfill(4)
        
        print(f"Step {steps+1}: {large_num} - {small_num} = {num}")
        steps += 1
    
    print(f"Reached Kaprekar's constant 6174 in {steps} steps. 🎉")

numbers = [n for n in range(1000, 10000) if len(set(str(n))) > 1]  
check_number(random.choice(numbers))
