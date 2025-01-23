#Define a function to check weather given no is automorphic no or not.
#Example of automorphic no is 5 -> 25 , 25 -> 625
def is_automorphic(n: int) ->bool:
    square = n*n
    while n>0:
        if n%10 != square%10:
            return False
        n = n//10
        square = square//10
    return True
n = int(input("Enter the number : "))
if is_automorphic(n):
    print(f"{n} is a automorphic number")
else:
    print(f"{n} is not a automorphic number")        
    
'''def is_automorphic(n: int) -> bool:
    square = n * n
    # Convert both the number and its square to strings
    str_n = str(n)
    str_square = str(square)
    # Check if the square ends with the number
    return str_square.endswith(str_n)

# Take input from the user
n = int(input("Enter the number: "))
if is_automorphic(n):
    print(f"{n} is an automorphic number")
else:
    print(f"{n} is not an automorphic number")'''
    