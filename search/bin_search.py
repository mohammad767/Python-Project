import random
lst = list(range(1, 1001))  

def search(x,arr) :
    arr = sorted(arr)
    while True:
        ch_number = arr[len(arr) // 2]
        print(f"Checking: {ch_number}")
        print(arr)
        if ch_number == x:
            return True
        elif ch_number < x:
            arr = [num for num in arr if num > ch_number]
        elif ch_number > x:
            arr = [num for num in arr if num < ch_number]  
        
        
def main():
    x = int(input("Enter a number to search: "))
    result = search(x, lst)
    if result:
        print(f"{x} found in the list.")
    else:
        print(f"{x} not found in the list.")
main()
        
        
    