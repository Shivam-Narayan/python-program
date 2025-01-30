#Define a function to check whether the given number is buzz number or not.
#Example 17 -> last no is 7 , 49 divisable by 7, 100 is not buzz no.
def is_buzz(n: int) -> bool:
    if n % 7 == 0 or n % 10 == 7:
        return True
    else:
        return False
    
#Taking input from user.
n = int(input("Enter the number: "))
if is_buzz(n):
    print(f"{n} is a buzz number")
else:
    print(f"{n} is not a buzz number")        
    

'''
def is_buzz(n: int) -> bool:
    # A number is a buzz number if it is divisible by 7 or ends with 7
    return n % 7 == 0 or n % 10 == 7

# Taking input from the user
n = int(input("Enter the number: "))
if is_buzz(n):
    print(f"{n} is a buzz number")
else:
    print(f"{n} is not a buzz number")'''
    