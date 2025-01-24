#Define a function to check whether the given number is Neon number or not.
#Neon number is a number where the sum of digits of square of the number is equal to the number itself.
#Example: 9 is a Neon number. 9*9 = 81. Sum of digits = 8+1 = 9
#Example: 12 is not a Neon number. 12*12 = 144. Sum of digits = 1+4+4 = 9
'''
def is_neon(n: int) -> bool:
    temp = n * n
    sum = 0
    
    while temp != 0:
        sum  = sum + (temp%10)
        temp = temp // 10
    return sum == n
n = int(input("Enter the number : "))
if is_neon(n):
    print(f'{n} is a neon number')
else:
    print(f'{n} is not a neon number')'''
##############################################################################################   
    
def is_neon(n: int) ->bool:
    # Multiply n by itself to get the square of n
    # Convert the square to a string to iterate over each digit
    # Convert each digit back to an integer and sum them up
    # Check if the sum of the digits is equal to the original number
    return sum(int(digit) for digit in str(n * n)) == n

# Prompt the user to enter a number
n = int(input("Enter the number: "))

# Check if the entered number is a neon number
if is_neon(n):
    # Print that the number is a neon number
    print(f'{n} is a neon number')
else:
    # Print that the number is not a neon number
    print(f'{n} is not a neon number')
