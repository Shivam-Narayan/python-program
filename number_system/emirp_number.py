#Write a Function to return “True” if the given number is EMIRP NUMBER otherwise return “False”.
#ex: 13, 17, 31, 37, 71, 73, 79, and 97.
def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def getReverse(n):
    rev = 0
    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

def isEmirp(n):
    return isPrime(n) and isPrime(getReverse(n))

n = int(input("Enter the number: "))
if isEmirp(n):
    print("{} is an Emirp Number".format(n))
else:
    print("{} is not an Emirp Number".format(n))
