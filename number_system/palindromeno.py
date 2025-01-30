def is_palindrome(n):
    # Convert the number to a string
    original = str(n)
    # Reverse the string
    reversed_num = original[::-1]
    # Check if the original and reversed strings are the same
    return original == reversed_num

# Input number
number = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
