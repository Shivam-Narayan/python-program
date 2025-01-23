#Write a function to return number of EVEN digits and number of ODD digits in the number.
def getEvenOddCount(n):
    evenCount = 0
    oddCount = 0
    while n != 0:
        digit = n % 10
        if digit % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
        n //= 10
    return [evenCount, oddCount]

# Taking input from the user
n = int(input("Enter the number: "))
result = getEvenOddCount(n)
print("Number of even digits in the number:", result[0])
print("Number of odd digits in the number:", result[1])
