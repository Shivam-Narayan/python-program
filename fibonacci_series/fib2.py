#Write a python program to print first nth fibonacci number.
def get_fibonacci(count: int) ->int:
    f1 = 0
    f2 = 1
    if count == 0:
        return None
    elif count == 1:
        return f1
    elif count == 2:
        return f2
    else:
        while count>2:
            f3 = f1+f2
            f1 = f2
            f2 = f3
            count = count - 1
        return f3    
       
n = int(input("Enter the number : "))
print(get_fibonacci(n))      
#####################################################################
'''def get_fibonacci(count: int):
    if count <= 0:
        return
    elif count == 1:
        print(0)
        return
    f1, f2 = 0, 1
    print(f1, end=" ")
    print(f2, end=" ")
    for _ in range(2, count):
        f3 = f1 + f2
        print(f3, end=" ")
        f1, f2 = f2, f3

n = int(input("Enter the number: "))
get_fibonacci(n)'''

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