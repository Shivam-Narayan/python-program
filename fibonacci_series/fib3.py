#Write a python program to print first n fibonacci number.
def get_fibonacci(count: int) ->None:
    f1 = 0
    f2 = 1
    while count>0:
        print(f1,end=" ")
        f1 , f2 = f2, f1 + f2
        count = count - 1
n = int(input("Enter the number : "))
get_fibonacci(n)  
