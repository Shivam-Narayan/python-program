#Write a Python program to print all 3-digit ARMSTRONG numbers.
def getCount(num):
    num = str(num)
    count = len(num)
    return count

def isArmStrong(num):
    sum = 0
    temp = num
    count = getCount(num)
    while temp != 0:
        digit = temp % 10
        sum += digit ** count
        temp //= 10
    return sum == num

# Taking input from the user
num = int(input("Enter the number:\n"))

print("Armstrong numbers between 100 and 1000 are:")
for i in range(100, 1000):
    if isArmStrong(i):
        print(i)
