def getEvenOddCount(n):
    evenCount = 0
    oddCount = 0
    while n != 0:
        digit = n % 10
        if digit % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
        n = n // 10
    return [evenCount, oddCount]

n = int(input("Enter the number: "))
a = getEvenOddCount(n)
print("Number of even digits in the number:", a[0])
print("Number of odd digits in the number:", a[1])

    
'''def getoddeven(n: int):
    if n%2 == 0:
        print("Even number")
    else:
        print("odd number")
        
n = int(input("Enter the number: "))
getoddeven(n) '''               