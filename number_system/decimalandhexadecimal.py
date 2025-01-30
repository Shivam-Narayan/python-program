#Write a python program to convert DECIMAL to HEXADECIMAL number.

def decimalToHexadecimal(num):
    hexChars = "0123456789ABCDEF"
    hexaDecimal = ""
    while num != 0:
        rem = num % 16
        hexaDecimal = hexChars[rem] + hexaDecimal
        num = num // 16
    return hexaDecimal

# Taking input from the user
dec = int(input("Enter decimal number: "))
print(f'The hexadecimal format of {dec} is {decimalToHexadecimal(dec)}')
