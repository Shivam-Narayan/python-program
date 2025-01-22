'''#write a python program to print fibonacci series within n or til n.
#011235813
def get_fibonacci(n: int) -> None:
    f1 = 0
    f2 = 1
    
    while f1<=n:
        print(f1,end=" ")
        f3 = f1+f2
        f1 = f2
        f2 = f3
n = int(input("Enter the number : "))
get_fibonacci(n)   '''

def get_fibonacci(n: int) -> None:
    f1 = 0
    f2 = 1
    while f1 <= n:
        print(f1, end=" ")
        f1, f2 = f2, f1 + f2

n = int(input("Enter the number: "))
get_fibonacci(n)