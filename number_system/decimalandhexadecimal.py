#Write a python program to convert DECIMAL to HEXADECIMAL number.
def decimalToHexaDec(num):
    hexaDec = ""
    if num == 0:
        return "0"
    while num != 0:
        rem = num % 16
        if rem < 10:
            hexaDec = str(rem) + hexaDec
        elif rem == 10:
            hexaDec = "A" + hexaDec
        elif rem == 11:
            hexaDec = "B" + hexaDec
        elif rem == 12:
            hexaDec = "C" + hexaDec
        elif rem == 13:
            hexaDec = "D" + hexaDec
        elif rem == 14:
            hexaDec = "E" + hexaDec
        elif rem == 15:
            hexaDec = "F" + hexaDec
        num = num // 16
    return hexaDec

# Taking input from the user
dec = int(input("Enter decimal number: "))
print(f'The hexadecimal format of {dec} is {decimalToHexaDec(dec)}')

'''
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
'''