#Define a function to check weather the given no is spy no or not.
#Example is 22 -> 2+2, 2*2 = 4 like that no.
def is_spy(n: int) -> bool:
    sum = 0
    product = 1
    
    while n!= 0:
        digit = n%10
        sum = sum + digit
        product = product * digit
        n = n//10
    return sum == product

#Taking input from user.
n = int(input("Enter the number : "))
if is_spy(n):
    print(f"{n} is a spy number")
else:
    print(f"{n} is not a spy number")        