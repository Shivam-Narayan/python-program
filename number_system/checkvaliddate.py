#Write a Python program to check the validity of the date.
def isValid(d, m, y):
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check if the month and year are valid
    if m < 1 or m > 12 or y < 1:
        return False
    
    # Check for leap year and adjust days in February
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        daysInMonth[1] = 29
    
    # Check if the day is valid for the given month
    if d < 1 or d > daysInMonth[m - 1]:
        return False
    
    return True

# Taking input from the user
d = int(input("Enter the day: "))
m = int(input("Enter the month: "))
y = int(input("Enter the year: "))

print("{}/{}/{}".format(d, m, y))
if isValid(d, m, y):
    print("It is a valid date.")
else:
    print("It is an invalid date.")
