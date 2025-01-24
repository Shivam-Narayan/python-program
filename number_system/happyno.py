#Write a function to return “True” if the number is HAPPY NUMBER otherwise return “False”.
#First few happy numbers are 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100.
def isHappy(num):
    while num > 9:
        sum = 0
        while num != 0:
            digit = num % 10
            sum = sum + digit * digit
            num = num // 10
        num = sum
    return num == 1 or num == 7

# Taking input from the user
num = int(input("Enter the number:\n"))

if isHappy(num):
    print("Given number is a Happy number")
else:
    print("Given number is not a Happy number")
