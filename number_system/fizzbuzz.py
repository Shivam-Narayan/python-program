#Write a python program to print fizz buzz.
n = int(input("Enter the number : "))
if n%3==0 and n%5 == 0:
    print("Fizz buzz")
elif n%3==0:
    print("Fizz")
elif n%5==0:
    print("Buzz")
else:
    print("No fizz buzz")            