#Write a Python program to check whether the number is EVIL or ODIOUS
#15 -> Convert to Binary -> 1111 -> if even number of 1’s -> Evil Number
#16 -> Convert to Binary -> 10000 -> if odd number of 1’s -> Odious Number
def decimalToBinary(num):
    binary = ""
    if num == 0:
        return "0"
    while num != 0:
        rem = num % 2
        binary = str(rem) + binary
        num = num // 2
    return binary

n = int(input("Enter decimal number: "))
a = decimalToBinary(n)
count1 = a.count("1")

if count1 % 2 == 0:
    print("{} is an Evil Number".format(n))
else:
    print("{} is an Odious Number".format(n))
