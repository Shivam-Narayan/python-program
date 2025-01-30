#write a python program to print fibonacci series within n or til n.
#011235813

'''num = int(input("Enter the last number:\n"))
f1 = 0
f2 = 1
while f1 <= num:
    print(f1, end=" ")
    f3 = f1 + f2
    f1 = f2
    f2 = f3'''


def getfibonacci(n: int):
    f1 = 0
    f2 = 1
    while f1 <= n:
        print(f1, end=" ")
        f3 = f1 + f2
        f1 = f2
        f2 = f3
                
#Taking input from user
n = int(input("Enter the number: "))
getfibonacci(n)