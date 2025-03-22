#Write a Python program to print all 3-digit ARMSTRONG numbers.
'''
Input:153
Output: Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input: 120
Output: No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9

Input: 1253
Output: No
1253 is not a Armstrong Number
1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723

Input: 1634
Output: Yes
1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634

'''

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

# def is_armstrong(num):
#     digits = list(map(int, str(num)))  # Convert number to list of digits
#     count = len(digits)
#     return sum(map(lambda x: x ** count, digits)) == num

# # Find Armstrong numbers between 100 and 1000
# print("Armstrong numbers between 100 and 1000:")
# for i in range(100, 1000):
#     if is_armstrong(i):
#         print(i)
